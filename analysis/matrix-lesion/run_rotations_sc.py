"""Round-4b: rotations under the source-complete lesion regime.

The target row keeps all its known SOURCE cells visible (the
observed side of the projective claim); targets are masked.
Reference rows stay intact. Deterministic per dataset, so reps=1.
"""
import json
import os

import numpy as np

from lesion import IDX
from simulate import one_dataset_l4

C = IDX
ROTATIONS = {
    # grouping: (source cols, own targets, foreign targets)
    "intj":   ([C["P01"], C["P02"], C["P03"], C["P04"], C["P05"], C["P07"]],
               [C["P12"]], [C["P10"], C["P11"]]),
    "expr":   ([C["P08"], C["P07"]],
               [C["P10"], C["P11"]], [C["P12"]]),
    "suppl":  ([C["P02"]],
               [C["P12"]], [C["P10"], C["P11"]]),
    "depict": ([C["P09"]],
               [C["P10"], C["P13"]], [C["P11"]]),
}

results = []
seed = 4000
for world in ("multianchor", "null", "latent_class"):
    for g, (src, own, foreign) in ROTATIONS.items():
        for label, tset in (("own", own), ("foreign", foreign)):
            seed += 1
            rng = np.random.default_rng(seed)
            rows = [one_dataset_l4(world, 33, rng, reps=1,
                                   assignment=g, targets=tset,
                                   source_cols=src)
                    for _ in range(40)]
            rows = [r for r in rows if r]
            d20 = float(np.median([r["d20"] for r in rows]))
            d20r = float(np.median([r["d20_resolved"] for r in rows]))
            d31 = float(np.median([r["d31"] for r in rows]))
            hit = float(np.mean([r["d20"] >= 0.03 for r in rows]))
            unres = float(np.median([r["unresolved"] for r in rows]))
            results.append({"world": world, "grouping": g,
                            "targets": label, "regime": "source_complete",
                            "median_d20": d20, "median_d20_resolved": d20r,
                            "median_d31": d31, "hit_rate_003": hit,
                            "unresolved": unres})
            print(f"{world:12s} {g:7s} {label:8s} d20={d20:+.3f} "
                  f"d20|res={d20r:+.3f} d31={d31:+.3f} hit@.03={hit:.2f} "
                  f"unres={unres:.2f}", flush=True)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "results-rotations-sc.json")
with open(out, "w") as f:
    json.dump(results, f, indent=1)
print("wrote", out)
