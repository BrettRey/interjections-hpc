import sys, numpy as np
sys.path.insert(0, sys.argv[1])
import harness as h
rng = np.random.default_rng(99)
cal = {"s_i": 0.825, "s_e": 0.75}
def phi(x, y):
    return np.corrcoef(x, y)[0, 1]
out = {}
for world in ("cross", "bonds"):
    acc = {}
    for _ in range(400):
        X = h.world_cross(rng)[0] if world == "cross" else h.world_bonds(rng, cal["s_i"], cal["s_e"])[0]
        for g, gd in h.GROUPINGS.items():
            rows = h.UNIVERSE[g]
            for t in gd["targets"]:
                v = []
                for p in gd["diag"]:
                    s = gd["sign"][p]
                    xp = X[rows, h.C[p]] if s > 0 else 1 - X[rows, h.C[p]]
                    xt = X[rows, h.C[t]]
                    if xp.std() > 0 and xt.std() > 0:
                        v.append(abs(phi(xp, xt)))
                acc.setdefault((g, t), []).append(np.mean(v))
    out[world] = {k: float(np.mean(v)) for k, v in acc.items()}
for g in h.GROUPINGS:
    print(g, " ".join(f"{t}: cross {out['cross'][(g,t)]:.2f} bonds {out['bonds'][(g,t)]:.2f}" for t in h.GROUPINGS[g]["targets"]))
