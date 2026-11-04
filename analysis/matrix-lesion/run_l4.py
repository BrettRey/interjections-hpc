"""Round-3 fake-data run: L4 sparse-row regime as primary tier test."""
import json
import os
from simulate import run_condition_l4

conds = [
    ("null", 33, {}),
    ("latent_class", 33, {}),
    ("crosscutting", 33, {}),
    ("crosscutting", 33, {"assignment": "expr"}),
    ("hub", 33, {}),
    ("latent_class", 60, {}),
    ("latent_class", 33, {"fill": 0.45}),
    ("latent_class", 33, {"k": 2}),
    ("latent_class", 33, {"k": 6}),
]
results = []
for i, (dgp, n, kw) in enumerate(conds):
    r = run_condition_l4(dgp, n, sims=40, seed=3000 + i, **kw)
    results.append(r)
    tag = dgp + ("/EXPR" if kw.get("assignment") == "expr" else "")
    print(f"{tag:16s} n={n:3d} {kw}  T1={r['tier1_rate']:.2f} "
          f"T<=2={r['tier2plus_rate']:.2f} d20={r['median_d20']:+.3f} "
          f"d20|res={r['median_d20_resolved']:+.3f} "
          f"d31={r['median_d31']:+.3f} unres={r['median_unresolved']:.2f}",
          flush=True)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "results-simulation-l4.json")
with open(out, "w") as f:
    json.dump(results, f, indent=1)
print("wrote", out)
