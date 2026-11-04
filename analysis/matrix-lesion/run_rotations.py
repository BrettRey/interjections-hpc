"""Round-4 fake-data run: rotations over groupings.

Each rotation is (assignment rule, primary targets). Run in the
multianchor world (each grouping has its own latent anchor) and in
the null world. Also records each grouping's gain on the OTHER
groupings' headline targets as a discrimination check.
"""
import json
import os

import numpy as np

from lesion import IDX
from simulate import one_dataset_l4

ROTATIONS = {
    "intj":   [IDX["P12"], IDX["P08"]],
    "expr":   [IDX["P10"], IDX["P11"]],
    "suppl":  [IDX["P12"]],
    "depict": [IDX["P10"], IDX["P13"]],
}
# discrimination: gain of each assignment on a foreign target set
FOREIGN = {
    "intj":   [IDX["P10"], IDX["P11"]],   # expr's targets
    "expr":   [IDX["P12"]],              # intj/suppl target
    "suppl":  [IDX["P10"], IDX["P11"]],
    "depict": [IDX["P11"]],
}

results = []
for world in ("multianchor", "null"):
    for g, targets in ROTATIONS.items():
        for label, tset in (("own", targets), ("foreign", FOREIGN[g])):
            rng = np.random.default_rng(hash((world, g, label)) % 2**31)
            rows = [one_dataset_l4(world, 33, rng, assignment=g,
                                   targets=tset)
                    for _ in range(30)]
            rows = [r for r in rows if r]
            d20 = float(np.median([r["d20"] for r in rows]))
            d20r = float(np.median([r["d20_resolved"] for r in rows]))
            hit = float(np.mean([r["d20"] >= 0.03 for r in rows]))
            unres = float(np.median([r["unresolved"] for r in rows]))
            results.append({"world": world, "grouping": g,
                            "targets": label, "median_d20": d20,
                            "median_d20_resolved": d20r,
                            "hit_rate_003": hit, "unresolved": unres})
            print(f"{world:12s} {g:7s} {label:8s} d20={d20:+.3f} "
                  f"d20|res={d20r:+.3f} hit@.03={hit:.2f} "
                  f"unres={unres:.2f}", flush=True)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "results-rotations.json")
with open(out, "w") as f:
    json.dump(results, f, indent=1)
print("wrote", out)
