"""Fake-data design check (Gelman-style) for the lesion study.

Generates matrices from known data-generating processes, degrades them
with a fill (unknown) rate and a consensus-coding error rate, and runs
the frozen-draft lesion design (L2 at 60% masking) to estimate:
  - false-tier rates under a no-structure null,
  - power under structured worlds,
  - unresolved-assignment rates,
at the drafted n and at larger n, before any real cell is coded.

Sim-tiers approximate FREEZE section 8 without the bootstrap-CI
condition (noted in the report). Thresholds are the draft placeholders:
M2 beats M0 by >= 0.05 target-only log loss; Tier 1 also needs
M3 beats M1 by >= 0.01; Tier 2 needs M3 within 0.02 of M1.
"""
import json
import numpy as np

from lesion import IDX, TARGET_ONLY, lesion_run, random_mask

P = IDX
BASE = np.array([.55, .45, .35, .25, .30, .20, .55,
                 .40, .15, .35, .40, .50, .15, .45])


def bern(rng, probs):
    probs = np.asarray(probs, dtype=float)
    return (rng.random(probs.shape) < probs).astype(int)


def dgp_null(rng, n):
    return bern(rng, np.tile(BASE, (n, 1)))


def dgp_latent_class(rng, n):
    core = np.array([.9, .85, .05, .05, .02, .05, .9,
                     .8, .1, .8, .85, .9, .25, .5])
    ordinary = np.array([.15, .05, .85, .7, .8, .7, .15,
                         .1, .05, .1, .1, .15, .02, .2])
    expr_integr = np.array([.05, .05, .9, .1, .05, .02, .9,
                            .9, .05, .8, .85, .1, .05, .1])
    z = rng.choice(3, size=n, p=[.4, .4, .2])
    probs = np.choose(z[:, None], [core, ordinary, expr_integr])
    return bern(rng, probs)


def dgp_crosscutting(rng, n):
    """Two independent anchors: A (distributional, interjection-like)
    drives P01, P02, P12, P13 and (negatively) P03-P05; B (stance)
    drives P08, P10, P11. P07 depends on A or B. INTJ should project
    to P12/P13 but not P10/P11; EXPRESSIVE the reverse."""
    A = rng.random(n) < .45
    B = rng.random(n) < .45
    C = rng.random(n) < .15
    hi, lo = .85, .12
    pr = np.tile(BASE, (n, 1)).astype(float)
    for name in ("P01", "P02", "P12", "P13"):
        pr[:, P[name]] = np.where(A, hi, lo)
    for name in ("P03", "P04", "P05"):
        pr[:, P[name]] = np.where(A, lo, hi)
    for name in ("P08", "P10", "P11"):
        pr[:, P[name]] = np.where(B, hi, lo)
    pr[:, P["P07"]] = np.where(A | B, .85, .15)
    pr[:, P["P09"]] = np.where(C, .85, .05)
    pr[:, P["P06"]] = np.where(A, .05, .5)
    pr[:, P["P14"]] = np.where(A, .7, .3)
    return bern(rng, pr)


def dgp_hub(rng, n):
    """Adversarial: one hub (P07) drives everything else. The category
    step should add nothing beyond the visible properties."""
    hub = rng.random(n) < .5
    pr = np.where(hub[:, None], .8, .2) * np.ones((n, 14))
    pr[:, P["P03"]] = np.where(hub, .2, .8)
    pr[:, P["P04"]] = np.where(hub, .2, .8)
    pr[:, P["P05"]] = np.where(hub, .2, .8)
    X = bern(rng, pr)
    X[:, P["P07"]] = hub.astype(int)
    return X


def dgp_multianchor(rng, n):
    """Four partly independent anchors, one per rotation:
    A distributional (INTJ), B stance (EXPRESSIVE), F supplement
    function (drives P02 and P12 beyond A), D depictive (P09, and
    P10 = does-not-strengthen)."""
    A = rng.random(n) < .40
    B = rng.random(n) < .40
    F = rng.random(n) < .35
    D = rng.random(n) < .18
    hi, lo = .85, .12
    pr = np.tile(BASE, (n, 1)).astype(float)
    pr[:, P["P01"]] = np.where(A, hi, lo)
    pr[:, P["P02"]] = np.where(A | F, hi, lo)
    for name in ("P03", "P04", "P05"):
        pr[:, P[name]] = np.where(A, lo, hi)
    pr[:, P["P06"]] = np.where(A, .05, .5)
    pr[:, P["P07"]] = np.where(A | B | D, .85, .15)
    pr[:, P["P08"]] = np.where(B, hi, lo)
    pr[:, P["P09"]] = np.where(D, hi, .05)
    pr[:, P["P10"]] = np.where(D, .05, np.where(B, hi, .25))
    pr[:, P["P11"]] = np.where(B, hi, lo)
    pr[:, P["P12"]] = np.where(A | F, hi, lo)
    pr[:, P["P13"]] = np.where(A | D, .30, .03)
    pr[:, P["P14"]] = np.where(A, .7, .3)
    return bern(rng, pr)


DGPS = {"null": dgp_null, "latent_class": dgp_latent_class,
        "crosscutting": dgp_crosscutting, "hub": dgp_hub,
        "multianchor": dgp_multianchor}


def degrade(X, rng, fill=0.65, err=0.05):
    known = rng.random(X.shape) < fill
    flip = (rng.random(X.shape) < err) & known
    Xc = X.copy()
    Xc[flip] = 1 - Xc[flip]
    return Xc, known


def sim_tier(d20, d31):
    if d20 >= 0.05 and d31 >= 0.01:
        return 1
    if d20 >= 0.05 and d31 >= -0.02:
        return 2
    return 3


def one_dataset(dgp, n, rng, draws=20, fill=0.65, err=0.05,
                assignment="intj", mask_frac=0.40):
    X = DGPS[dgp](rng, n)
    Xc, known = degrade(X, rng, fill=fill, err=err)
    d20s, d31s, unres = [], [], []
    for _ in range(draws):
        mask = random_mask(known, mask_frac, rng)
        r = lesion_run(Xc, known, mask, assignment=assignment)
        t = r["target"]
        if np.isnan(t["M0"]):
            continue
        d20s.append(t["M0"] - t["M2"])
        d31s.append(t["M1"] - t["M3"])
        unres.append(r["unresolved_rate"])
    if not d20s:
        return None
    d20, d31 = float(np.mean(d20s)), float(np.mean(d31s))
    return {"d20": d20, "d31": d31, "tier": sim_tier(d20, d31),
            "unresolved": float(np.mean(unres))}


PRIMARY_TARGETS = [IDX[p] for p in ("P10", "P11", "P12")]


def one_dataset_l4(dgp, n, rng, k=4, reps=2, fill=0.65, err=0.05,
                   assignment="intj", targets=None, source_cols=None):
    """L4 sparse-row regime: each row in turn is the target, reduced
    to k visible known cells; all other rows stay fully visible.
    Scores only PRIMARY_TARGETS (P10-P12); P13 excluded after round-2
    diagnostics showed near-zero oracle gain for a rare property.
    Returns pooled gains over all scored cells and over resolved rows
    only, plus the target-row unresolved rate."""
    from lesion import ASSIGNERS, logloss, predict_column, visible
    target_cols = PRIMARY_TARGETS if targets is None else targets
    X = DGPS[dgp](rng, n)
    Xc, known = degrade(X, rng, fill=fill, err=err)
    sums = {kk: [0.0, 0] for kk in ("M0", "M1", "M2", "M3")}
    sums_r = {kk: [0.0, 0] for kk in sums}
    unres = []
    for _ in range(reps):
        for r in range(n):
            kc = np.where(known[r])[0]
            if source_cols is not None:
                # source-complete regime: all known source cells of
                # the target row stay visible; targets (and any
                # non-source cells beyond k extras) are masked.
                keep = np.array([c for c in kc if c in source_cols])
                if len(keep) == 0:
                    continue
            elif len(kc) <= k:
                continue
            else:
                keep = rng.choice(kc, size=k, replace=False)
            mask = np.zeros_like(known)
            mask[r, kc] = True
            mask[r, keep] = False
            vis = visible(known, mask)
            a = ASSIGNERS[assignment](Xc, vis)
            unres.append(a[r] == 2)
            for j in target_cols:
                if not (known[r, j] and mask[r, j]):
                    continue
                res = predict_column(Xc, known, mask, j, a)
                if res is None:
                    continue
                sel = res["rows"] == r
                if not sel.any():
                    continue
                y = res["y"][sel]
                for kk in sums:
                    ll = logloss(y, res[kk][sel]) * len(y)
                    sums[kk][0] += ll
                    sums[kk][1] += len(y)
                    if a[r] != 2:
                        sums_r[kk][0] += ll
                        sums_r[kk][1] += len(y)
    if sums["M0"][1] == 0:
        return None
    ll = {kk: v[0] / v[1] for kk, v in sums.items()}
    llr = {kk: (v[0] / v[1] if v[1] else float("nan"))
           for kk, v in sums_r.items()}
    d20 = ll["M0"] - ll["M2"]
    d31 = ll["M1"] - ll["M3"]
    return {"d20": float(d20), "d31": float(d31),
            "d20_resolved": float(llr["M0"] - llr["M2"]),
            "tier": sim_tier(d20, d31),
            "unresolved": float(np.mean(unres))}


def run_condition_l4(dgp, n, sims, seed, **kw):
    rng = np.random.default_rng(seed)
    rows = [one_dataset_l4(dgp, n, rng, **kw) for _ in range(sims)]
    rows = [r for r in rows if r]
    tiers = np.array([r["tier"] for r in rows])
    return {"dgp": dgp, "n": n, "sims": len(rows), "kw": kw,
            "regime": "L4",
            "tier1_rate": float(np.mean(tiers == 1)),
            "tier2plus_rate": float(np.mean(tiers <= 2)),
            "median_d20": float(np.median([r["d20"] for r in rows])),
            "median_d20_resolved": float(np.median(
                [r["d20_resolved"] for r in rows])),
            "median_d31": float(np.median([r["d31"] for r in rows])),
            "median_unresolved": float(np.median(
                [r["unresolved"] for r in rows]))}


def run_condition(dgp, n, sims, seed, **kw):
    rng = np.random.default_rng(seed)
    rows = [one_dataset(dgp, n, rng, **kw) for _ in range(sims)]
    rows = [r for r in rows if r]
    tiers = np.array([r["tier"] for r in rows])
    return {"dgp": dgp, "n": n, "sims": len(rows), "kw": kw,
            "tier1_rate": float(np.mean(tiers == 1)),
            "tier2plus_rate": float(np.mean(tiers <= 2)),
            "median_d20": float(np.median([r["d20"] for r in rows])),
            "median_d31": float(np.median([r["d31"] for r in rows])),
            "median_unresolved": float(np.median(
                [r["unresolved"] for r in rows]))}


if __name__ == "__main__":
    results = []
    conds = []
    for dgp in DGPS:
        conds.append((dgp, 33, {}))
    conds += [("latent_class", 60, {}), ("latent_class", 100, {}),
              ("crosscutting", 60, {}),
              ("latent_class", 33, {"fill": 0.45}),
              ("null", 100, {})]
    for i, (dgp, n, kw) in enumerate(conds):
        r = run_condition(dgp, n, sims=60, seed=1000 + i, **kw)
        results.append(r)
        print(f"{dgp:14s} n={n:3d} {kw}  T1={r['tier1_rate']:.2f} "
              f"T<=2={r['tier2plus_rate']:.2f} d20={r['median_d20']:+.3f} "
              f"d31={r['median_d31']:+.3f} unres={r['median_unresolved']:.2f}",
              flush=True)
    # crosscutting world, EXPRESSIVE assignment: discrimination check
    r = run_condition("crosscutting", 33, sims=60, seed=2000,
                      assignment="expr")
    results.append(r)
    print(f"{'crosscut/EXPR':14s} n= 33  T1={r['tier1_rate']:.2f} "
          f"T<=2={r['tier2plus_rate']:.2f} d20={r['median_d20']:+.3f} "
          f"d31={r['median_d31']:+.3f} unres={r['median_unresolved']:.2f}",
          flush=True)
    import os
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "results-simulation.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=1)
    print("wrote", out_path)
