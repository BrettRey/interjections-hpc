"""Diagnostic: where does the M2-vs-M0 signal die in the latent-class world?"""
import numpy as np
from lesion import (IDX, PROPS, TARGET_ONLY, assign_intj, logloss,
                    predict_column, random_mask, visible)
from simulate import dgp_latent_class, degrade

rng = np.random.default_rng(7)
# regenerate with class labels
core = np.array([.9, .85, .05, .05, .02, .05, .9, .8, .1, .8, .85, .9, .25, .5])
ordinary = np.array([.15, .05, .85, .7, .8, .7, .15, .1, .05, .1, .1, .15, .02, .2])
expr = np.array([.05, .05, .9, .1, .05, .02, .9, .9, .05, .8, .85, .1, .05, .1])
n = 200
z = rng.choice(3, size=n, p=[.4, .4, .2])
probs = np.choose(z[:, None], [core, ordinary, expr])
X = (rng.random(probs.shape) < probs).astype(int)
Xc, known = degrade(X, rng, fill=0.65, err=0.05)

for frac in (0.2, 0.4, 0.6):
    mask = random_mask(known, frac, rng)
    a = assign_intj(Xc, visible(known, mask))
    core_rows = z == 0
    print(f"\nmask={frac}: assignment of true-core rows: "
          f"MEMBER {np.mean(a[core_rows]==1):.2f} "
          f"NON {np.mean(a[core_rows]==0):.2f} "
          f"UNRES {np.mean(a[core_rows]==2):.2f}")
    print(f"          assignment of others:        "
          f"MEMBER {np.mean(a[~core_rows]==1):.2f} "
          f"NON {np.mean(a[~core_rows]==0):.2f} "
          f"UNRES {np.mean(a[~core_rows]==2):.2f}")
    for j in TARGET_ONLY:
        r = predict_column(Xc, known, mask, j, a)
        if r is None:
            continue
        print(f"  {PROPS[j]}: M0 {logloss(r['y'], r['M0']):.3f}  "
              f"M2 {logloss(r['y'], r['M2']):.3f}  "
              f"M1 {logloss(r['y'], r['M1']):.3f}  "
              f"gain20 {logloss(r['y'], r['M0'])-logloss(r['y'], r['M2']):+.3f}  "
              f"(base rate {r['y'].mean():.2f}, scored {len(r['y'])})")
    # oracle: predict targets from TRUE class
    for j in TARGET_ONLY:
        scored = np.where(known[:, j] & mask[:, j])[0]
        ref = np.where(known[:, j] & ~mask[:, j])[0]
        p_or = np.array([(Xc[ref[z[ref] == z[r]], j].sum() + 1) /
                         (np.sum(z[ref] == z[r]) + 2) for r in scored])
        p_0 = np.full(len(scored), (Xc[ref, j].sum() + 1) / (len(ref) + 2))
        print(f"  {PROPS[j]} ORACLE gain vs M0: "
              f"{logloss(Xc[scored, j], p_0) - logloss(Xc[scored, j], p_or):+.3f}")
