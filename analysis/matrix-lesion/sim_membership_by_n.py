"""Membership recovery vs number of rows, EXPRESSIVE (2026-11-04).

Asks whether the sparse-P10/P11 membership drift in the convergence
follow-up is a small-n estimation effect or structural. Fits only the
assignment models (no lesion cells), so larger n is cheap. Reports
median Brier against the true expressive class, and a bootstrap 95%
interval for the median paired difference (LCA2 minus tally) to show
Monte Carlo uncertainty. Diagnostic only.
"""
import json
import numpy as np
from lesion import IDX, assign_expr
from sim_convergence_assignment import WORLDS, fit_lca, member_class, EXPR_SRC, EXPR_SIGN, EXPR_TALLY_SRC
from sim_round6_eligibility import degrade_regime

P = IDX
THIN = [P["P10"], P["P11"]]


def one(world, n, q, regime, rng):
    X, truth = WORLDS[world](rng, n)
    Xc, known = degrade_regime(X, rng, regime)
    for j in THIN:
        known[:, j] = rng.random(n) < q
    vis = np.zeros_like(known)
    vis[:, EXPR_TALLY_SRC] = known[:, EXPR_TALLY_SRC]
    a = assign_expr(Xc, vis)
    pm_t = np.where(a == 2, 0.5, a.astype(float))
    post, theta, _ = fit_lca(Xc[:, EXPR_SRC], known[:, EXPR_SRC], 2, rng)
    pm_l = post[:, member_class(theta, EXPR_SRC, EXPR_SIGN)]
    y = truth["expr"]
    return float(np.mean((pm_t - y) ** 2)), float(np.mean((pm_l - y) ** 2))


rng = np.random.default_rng(20261106)
out = {}
for world in ("crosscutting", "latent_class"):
    for regime in ("uniform", "scarce_negative"):
        for q in (0.65, 0.33, 0.15):
            for n in (33, 100, 300, 1000):
                sims = 200 if n <= 100 else 60
                vals = np.array([one(world, n, q, regime, rng) for _ in range(sims)])
                d = vals[:, 1] - vals[:, 0]
                boots = [np.median(rng.choice(d, len(d))) for _ in range(1000)]
                key = f"{world}/{regime}/q{q}/n{n}"
                out[key] = {"brier_tally": float(np.median(vals[:, 0])),
                            "brier_lca2": float(np.median(vals[:, 1])),
                            "diff_median": float(np.median(d)),
                            "diff_ci95": [float(np.quantile(boots, .025)), float(np.quantile(boots, .975))],
                            "sims": sims}
                print(f"{key:42s} tally {out[key]['brier_tally']:.3f}  lca2 {out[key]['brier_lca2']:.3f}  diff {out[key]['diff_median']:+.3f} [{out[key]['diff_ci95'][0]:+.3f},{out[key]['diff_ci95'][1]:+.3f}]", flush=True)
json.dump(out, open("results-membership-by-n.json", "w"), indent=1)
