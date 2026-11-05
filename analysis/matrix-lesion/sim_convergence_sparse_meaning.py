"""Follow-up to the convergence check: EXPRESSIVE with sparse P10/P11.

A side agent noted (2026-11-04) that `sim_convergence_assignment.py`
documented P10 and P11 for about 65% of rows, while the corrected
target audit found them for about a third of sampled items (P10
item-direct 4/12; P11 item-direct 2 and inherited 2). This rerun keeps
every other cell as before and redraws knownness for P10 and P11 only,
independently of value, at q = 0.33 (audit-like) and q = 0.15 (stress).
EXPRESSIVE only: INTJ doesn't use P10 or P11 as diagnostics.
Diagnostic only; no real coded cell is used.
"""
import json
import sys
import time

import numpy as np

from lesion import IDX
from sim_convergence_assignment import WORLDS, rotation_records
from sim_round6_eligibility import degrade_regime

P = IDX
THIN = [P["P10"], P["P11"]]


def run(sims=150, seed=20261105, n=33, qs=(0.33, 0.15),
        worlds=("null", "latent_class", "hub", "crosscutting")):
    rng = np.random.default_rng(seed)
    out = {"meta": {"sims": sims, "n": n, "seed": seed, "qs": list(qs)}}
    for world in worlds:
        for regime in ("uniform", "scarce_negative"):
            for q in qs:
                fam = {"tally": [], "lca2": [], "lca3": [], "M1_conv": []}
                brier = {"tally": [], "lca2": [], "lca3": []}
                for _ in range(sims):
                    X, truth = WORLDS[world](rng, n)
                    Xc, known = degrade_regime(X, rng, regime)
                    for j in THIN:
                        known[:, j] = rng.random(n) < q
                    res = rotation_records(Xc, known, "expr", rng,
                                           truth["expr"])
                    t = res["targets"]
                    if t:
                        for r in ("tally", "lca2", "lca3"):
                            fam[r].append(np.mean(
                                [v["gain"][r] for v in t.values()]))
                        fam["M1_conv"].append(np.mean(
                            [v["gain_M1_conv"] for v in t.values()]))
                    for r in brier:
                        if r in res["membership"]:
                            brier[r].append(res["membership"][r]["brier"])
                key = f"{world}/{regime}/q{q}"
                out[key] = {
                    "family": {r: {"median": float(np.median(v)),
                                   "q05": float(np.quantile(v, .05)),
                                   "q95": float(np.quantile(v, .95)),
                                   "p_ge_0.03": float(np.mean(
                                       np.array(v) >= 0.03))}
                               for r, v in fam.items() if v},
                    "brier_median": {r: float(np.median(v))
                                     for r, v in brier.items() if v}}
                print(key, "done", flush=True)
    return out


if __name__ == "__main__":
    sims = int(sys.argv[1]) if len(sys.argv) > 1 else 150
    t0 = time.time()
    res = run(sims=sims)
    res["meta"]["runtime_s"] = round(time.time() - t0, 1)
    with open("results-convergence-sparse-meaning.json", "w") as fh:
        json.dump(res, fh, indent=1)
    print("runtime", res["meta"]["runtime_s"], "s")
