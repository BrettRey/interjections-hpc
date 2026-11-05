"""Round-6 fake-data check: eligibility gate + multi-target aggregate.

Tests the Brett-approved amended architecture (2026-11-04): no
privileged primary property; a frozen eligibility function admits
non-assignment targets; per-projection gains are primary, with a
property-weighted family summary secondary.

Per fake dataset, for each rotation (intj, expr) and each candidate
non-assignment target (P14 excluded as a descriptor):
- source-complete one-cell records are computed (v2 machinery);
- an evidence layer is simulated per known cell (item-direct vs
  inherited, canonical proposition IDs);
- three candidate gates are applied to post-concealment scored cells;
- admitted per-property gains and aggregates are recorded.

Worlds: null, latent_class, crosscutting, hub, multianchor (from
simulate.py), each under uniform fill and scarce-negative knownness
(Y cells documented more often than N cells). INTJ targets P08/P09
additionally block P07 on a random half of rows, modelling
source-target proposition sharing.

Outputs results-round6-eligibility.json. Diagnostic only: candidate
thresholds here inform FREEZE-v3 drafting; nothing is frozen by
running this script.
"""
import json
import os
from collections import Counter, defaultdict

import numpy as np

from lesion import IDX, PROPS, source_complete_records, summarize_records
from simulate import DGPS, bern

P = IDX
CANDIDATES = {
    "intj": [P[p] for p in ("P06", "P08", "P09", "P10", "P11", "P12",
                            "P13")],
    "expr": [P[p] for p in ("P01", "P02", "P03", "P04", "P05", "P06",
                            "P09", "P10", "P11", "P12", "P13")],
}


def degrade_regime(X, rng, regime, err=0.05):
    if regime == "uniform":
        known = rng.random(X.shape) < 0.65
    else:  # scarce_negative: N values documented far less often
        pk = np.where(X == 1, 0.80, 0.35)
        known = rng.random(X.shape) < pk
    flip = (rng.random(X.shape) < err) & known
    Xc = X.copy()
    Xc[flip] = 1 - Xc[flip]
    return Xc, known


def evidence_layer(Xc, known, rng, p_direct=0.5, n_shared_props=3):
    """Return (direct bool array, proposition id array of str)."""
    n, m = Xc.shape
    direct = (rng.random(Xc.shape) < p_direct) & known
    props = np.empty(Xc.shape, dtype=object)
    for j in range(m):
        shared = rng.integers(0, n_shared_props, size=n)
        for i in range(n):
            props[i, j] = (f"item-{j}-{i}" if direct[i, j]
                           else f"class-{j}-{shared[i]}")
    return direct, props


def gate_stats(records, direct, props):
    if not records:
        return None
    resolved = [r for r in records if r["resolved"]]
    ys = sum(r["y"] == 1 for r in records)
    ns = sum(r["y"] == 0 for r in records)
    members = sum(r["assignment"] == 1 for r in resolved)
    nonmembers = sum(r["assignment"] == 0 for r in resolved)
    j = records[0]["target"]
    d_scores = [direct[r["row"], j] for r in records]
    p_scores = [props[r["row"], j] for r in records]
    counts = Counter(p_scores)
    return {
        "scored": len(records), "resolved": len(resolved),
        "y": ys, "n": ns, "members": members, "nonmembers": nonmembers,
        "item_direct": int(sum(d_scores)),
        "item_direct_y": int(sum(d and r["y"] == 1
                                 for d, r in zip(d_scores, records))),
        "item_direct_n": int(sum(d and r["y"] == 0
                                 for d, r in zip(d_scores, records))),
        "distinct_props": len(counts),
        "max_prop_share": max(counts.values()) / len(records),
    }


def gate_a(s):
    return (s["scored"] >= 20 and s["resolved"] >= 15 and s["y"] >= 4
            and s["n"] >= 4 and s["members"] >= 4
            and s["nonmembers"] >= 4)


def gate_b(s):
    return (gate_a(s) and s["item_direct"] >= 6
            and s["item_direct_y"] >= 2 and s["item_direct_n"] >= 2
            and s["distinct_props"] >= 4 and s["max_prop_share"] <= 0.5)


def gate_c(s):
    return (s["scored"] >= 15 and s["resolved"] >= 10 and s["y"] >= 3
            and s["n"] >= 3 and s["members"] >= 3
            and s["nonmembers"] >= 3 and s["item_direct"] >= 4
            and s["distinct_props"] >= 3
            and s["max_prop_share"] <= 0.6)


GATES = {"A_counts": gate_a, "B_evidence": gate_b, "C_relaxed": gate_c}


def one_dataset(world, regime, rng, n=33):
    X = DGPS[world](rng, n)
    Xc, known = degrade_regime(X, rng, regime)
    direct, props = evidence_layer(Xc, known, rng)
    out = {}
    for rotation, targets in CANDIDATES.items():
        per_prop = {}
        for j in targets:
            blocked = None
            if rotation == "intj" and PROPS[j] in ("P08", "P09"):
                blocked = {(int(r), int(j)): (P["P07"],)
                           for r in range(n) if rng.random() < 0.5}
            rec = source_complete_records(
                Xc, known, rotation, [j],
                blocked_sources_by_cell=blocked)
            if not rec:
                continue
            s = gate_stats(rec, direct, props)
            summ = summarize_records(rec)["all"]
            per_prop[PROPS[j]] = {
                **s,
                "d20": summ["gain_M2_vs_M0"],
                "d10": summ["gain_M1_vs_M0"],
                "cost": summ["compression_cost_M2_minus_M1"],
                "gates": {g: bool(f(s)) for g, f in GATES.items()},
            }
        out[rotation] = per_prop
    return out


def aggregates(per_prop, gate_name):
    admitted = {p: v for p, v in per_prop.items()
                if v["gates"][gate_name]}
    if not admitted:
        return {"n_admitted": 0}
    gains = [v["d20"] for v in admitted.values()]
    cells = sum(v["scored"] for v in admitted.values())
    cell_w = sum(v["d20"] * v["scored"]
                 for v in admitted.values()) / cells
    return {"n_admitted": len(admitted),
            "admitted": sorted(admitted),
            "prop_weighted_d20": float(np.mean(gains)),
            "cell_weighted_d20": float(cell_w),
            "max_prop_gain": float(max(gains)),
            "share_gain_from_best": float(
                max(gains) / sum(gains)) if sum(gains) > 0 else None}


def run(world, regime, sims=25, seed=0):
    rng = np.random.default_rng(seed)
    datasets = [one_dataset(world, regime, rng) for _ in range(sims)]
    summary = {"world": world, "regime": regime, "sims": sims}
    for rotation in CANDIDATES:
        rot = {}
        for gate_name in GATES:
            aggs = [aggregates(d[rotation], gate_name) for d in datasets]
            adm_counts = Counter()
            for d in datasets:
                for p, v in d[rotation].items():
                    adm_counts[p] += bool(v["gates"][gate_name])
            with_gain = [a for a in aggs if a["n_admitted"]]
            rot[gate_name] = {
                "median_n_admitted": float(np.median(
                    [a["n_admitted"] for a in aggs])),
                "admission_rate_by_property": {
                    p: adm_counts[p] / sims for p in sorted(adm_counts)},
                "median_prop_weighted_d20": (
                    float(np.median([a["prop_weighted_d20"]
                                     for a in with_gain]))
                    if with_gain else None),
                "median_cell_weighted_d20": (
                    float(np.median([a["cell_weighted_d20"]
                                     for a in with_gain]))
                    if with_gain else None),
                "frac_datasets_prop_weighted_ge_003": (
                    float(np.mean([a["prop_weighted_d20"] >= 0.03
                                   for a in with_gain]))
                    if with_gain else None),
            }
        # per-property median gain (all datasets, ungated) for context
        rot["ungated_median_d20"] = {
            p: float(np.median([d[rotation][p]["d20"] for d in datasets
                                if p in d[rotation]]))
            for p in sorted({p for d in datasets for p in d[rotation]})}
        summary[rotation] = rot
    return summary


if __name__ == "__main__":
    results = []
    worlds = ("null", "latent_class", "crosscutting", "hub",
              "multianchor")
    for wi, world in enumerate(worlds):
        for ri, regime in enumerate(("uniform", "scarce_negative")):
            r = run(world, regime, sims=25, seed=6100 + 10 * wi + ri)
            results.append(r)
            for rotation in ("intj", "expr"):
                b = r[rotation]["B_evidence"]
                print(f"{world:13s} {regime:16s} {rotation:5s} "
                      f"gateB adm={b['median_n_admitted']:.0f} "
                      f"propW={b['median_prop_weighted_d20']} "
                      f"ge003={b['frac_datasets_prop_weighted_ge_003']}",
                      flush=True)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "results-round6-eligibility.json")
    with open(out, "w") as f:
        json.dump(results, f, indent=1)
    print("wrote", out)
