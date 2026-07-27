"""Bootstrap intervals for the per-item coefficients of variation.

The CVs in §6.1 are computed across twenty country sections and reported as
point estimates, then compared with one another. Twenty units is few enough
that the comparisons need intervals before they can carry weight. This
resamples countries with replacement and reports percentile intervals, then
lists which pairwise comparisons survive.
"""
import csv
import random
import statistics as st
from pathlib import Path

SRC = Path(__file__).parent.parent / 'data' / 'glowbe-interjection-frequencies.csv'
REGIONAL = {'lah', 'yaar', 'haba'}


def cv(v):
    return st.stdev(v) / st.mean(v)


def main(B=4000, seed=11):
    random.seed(seed)
    est = {}
    for row in csv.DictReader(SRC.open()):
        v = [float(y) for k, y in row.items() if k != 'item']
        boots = sorted(cv([random.choice(v) for _ in v]) for _ in range(B))
        est[row['item']] = (cv(v), boots[int(.025 * B)], boots[int(.975 * B)])

    for it, (c, lo, hi) in sorted(est.items(), key=lambda r: -r[1][0]):
        print(f"  {it:8} {c:5.2f}  [{lo:5.2f}, {hi:5.2f}]")

    core = [k for k in est if k not in REGIONAL]
    mid = [k for k in core if k not in ('yes', 'no')]
    sep = [(a, b) for i, a in enumerate(mid) for b in mid[i + 1:]
           if est[a][1] > est[b][2] or est[b][1] > est[a][2]]
    print(f"\n  separable pairs within the core band (excluding yes/no): "
          f"{len(sep)} of {len(mid)*(len(mid)-1)//2}")
    top = max(est['yes'][2], est['no'][2])
    print("  yes/no separate from: " +
          ', '.join(sorted(k for k in mid if est[k][1] > top)))


if __name__ == '__main__':
    main()
