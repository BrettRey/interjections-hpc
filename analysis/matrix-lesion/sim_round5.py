"""Round-5 fake-data checks for repaired v2 lesion machinery.

This round differs from rounds 1-4 in four ways:
- source-complete, one-cell lesions are the run type;
- M1 receives exactly the rotation's permitted source columns;
- a copied-class-assertion world tests what happens when many target
  cells inherit one shared generalization;
- a selective-documentation world makes knownness depend on class and
  target value;
- a provisional per-projection evidence gate is applied and reported.
The gate below is a simulation diagnostic, not a proposed freeze value.
"""
import json
import os

import numpy as np

from lesion import IDX, source_complete_records, summarize_records
from simulate import DGPS, bern, degrade

P = IDX
BASE = np.array([.55, .45, .35, .25, .30, .20, .55,
                 .40, .15, .35, .40, .50, .15, .45])


def dgp_copied_class(rng, n):
    """Sources weakly indicate A; coded P12 mostly inherits from ONE
    class-level draw per A value rather than item-level draws."""
    A = rng.random(n) < 0.45
    hi, lo = .85, .15
    pr = np.tile(BASE, (n, 1)).astype(float)
    for name in ("P01", "P02", "P07"):
        pr[:, P[name]] = np.where(A, hi, lo)
    for name in ("P03", "P04", "P05"):
        pr[:, P[name]] = np.where(A, lo, hi)
    X = bern(rng, pr)
    # one assertion draw per latent class: members mostly inherit,
    # nonmembers mostly inherit the complementary assertion
    member_assertion = int(rng.random() < 0.80)
    item_level = rng.random(n) < 0.30
    inherited = np.where(A, member_assertion, 1 - member_assertion)
    independent = (rng.random(n) < 0.50).astype(int)
    X[:, P["P12"]] = np.where(item_level, independent, inherited)
    return X, ~item_level


def evidence_gate(records):
    if not records:
        return False
    resolved = [r for r in records if r["resolved"]]
    ys = sum(r["y"] == 1 for r in records)
    ns = sum(r["y"] == 0 for r in records)
    members = sum(r["assignment"] == 1 for r in resolved)
    nonmembers = sum(r["assignment"] == 0 for r in resolved)
    return (len(records) >= 20 and len(resolved) >= 15
            and ys >= 4 and ns >= 4
            and members >= 4 and nonmembers >= 4)


def summarize_condition(rows):
    def med(key):
        return float(np.median([r[key] for r in rows]))
    return {
        "sims": len(rows),
        "gate_pass_rate": float(np.mean([r["gate"] for r in rows])),
        "median_coverage": med("coverage"),
        "median_d20": med("d20"),
        "median_d10": med("d10"),
        "median_compression_cost": med("compression"),
        "median_d20_resolved": med("d20_resolved"),
        "hit_d20_003": float(np.mean([r["d20"] >= 0.03 for r in rows])),
    }


def one_world(world, n, rng, fill=0.65, err=0.05,
              membership_mode="infer", concealed=()):
    inherited = None
    if world == "copied_class":
        X, inherited = dgp_copied_class(rng, n)
    else:
        X = DGPS[world if world in DGPS else "latent_class"](rng, n)
    if world == "selective_latent":
        # knownness depends on class-like source profile and target
        latent_like = ((X[:, P["P01"]] == 1) | (X[:, P["P02"]] == 1))
        pk = np.full(X.shape, 0.45)
        pk[latent_like] = 0.85
        pk[:, P["P12"]] = np.where(X[:, P["P12"]] == 1, 0.90, 0.50)
        known = rng.random(X.shape) < pk
        flip = (rng.random(X.shape) < err) & known
        Xc = X.copy()
        Xc[flip] = 1 - Xc[flip]
    else:
        Xc, known = degrade(X, rng, fill=fill, err=err)
    rec = source_complete_records(
        Xc, known, "intj", [P["P12"]], membership_mode=membership_mode,
        concealed_source_cols=concealed)
    s = summarize_records(rec)
    row = {"gate": evidence_gate(rec),
           "coverage": s["assignment_coverage"],
           "d20": s["all"]["gain_M2_vs_M0"],
           "d10": s["all"]["gain_M1_vs_M0"],
           "compression": s["all"]["compression_cost_M2_minus_M1"],
           "d20_resolved": s["resolved"]["gain_M2_vs_M0"]}
    if inherited is not None:
        item_records = [r for r in rec if not inherited[r["row"]]]
        inh_records = [r for r in rec if inherited[r["row"]]]
        row["d20_item_level_only"] = (
            summarize_records(item_records)["all"]["gain_M2_vs_M0"]
            if item_records else float("nan"))
        row["d20_inherited_only"] = (
            summarize_records(inh_records)["all"]["gain_M2_vs_M0"]
            if inh_records else float("nan"))
        row["n_item_level"] = len(item_records)
    return row


def run(world, n, sims, seed, **kw):
    rng = np.random.default_rng(seed)
    gen_world = "latent_class" if world == "selective_latent" else world
    rows = []
    for _ in range(sims):
        rows.append(one_world(world, n, rng, **kw)
                    if world in ("copied_class", "selective_latent")
                    else one_world(gen_world, n, rng, **kw))
    out = {"world": world, "n": n, "kw": kw,
           **summarize_condition(rows)}
    if world == "copied_class":
        out["median_d20_item_level_only"] = float(np.nanmedian(
            [r["d20_item_level_only"] for r in rows]))
        out["median_d20_inherited_only"] = float(np.nanmedian(
            [r["d20_inherited_only"] for r in rows]))
        out["median_n_item_level"] = float(np.median(
            [r["n_item_level"] for r in rows]))
    return out


if __name__ == "__main__":
    conds = [
        ("null", 33, {}),
        ("latent_class", 33, {}),
        ("latent_class", 60, {}),
        ("crosscutting", 33, {}),
        ("copied_class", 33, {}),
        ("selective_latent", 33, {}),
        ("latent_class", 33,
         {"membership_mode": "retain",
          "concealed": (P["P01"], P["P02"])}),
        ("latent_class", 33,
         {"membership_mode": "infer",
          "concealed": (P["P01"], P["P02"])}),
    ]
    results = []
    for i, (world, n, kw) in enumerate(conds):
        r = run(world, n, sims=40, seed=5000 + i, **kw)
        results.append(r)
        extra = ""
        if world == "copied_class":
            extra = (f" item={r['median_d20_item_level_only']:+.3f}"
                     f" inh={r['median_d20_inherited_only']:+.3f}")
        print(f"{world:16s} n={n} {kw} gate={r['gate_pass_rate']:.2f} "
              f"d20={r['median_d20']:+.3f} d10={r['median_d10']:+.3f} "
              f"cost={r['median_compression_cost']:+.3f} "
              f"hit={r['hit_d20_003']:.2f} "
              f"cov={r['median_coverage']:.2f}{extra}", flush=True)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "results-round5.json")
    with open(out, "w") as f:
        json.dump(results, f, indent=1)
    print("wrote", out)
