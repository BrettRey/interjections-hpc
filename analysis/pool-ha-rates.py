"""Partially pool the per-country validity rates for `ha`, and emit the multiverse.

Gelman's objection to the raw per-country rates is that they carry very unequal
precision: 8,100 tagged tokens for the United States against 420 for Ghana, so a
coefficient of variation computed across them as though they were equally precise
overstates dispersion. This shrinks each rate toward a common mean in proportion
to its own noise, using a beta-binomial hierarchical model with the prior
estimated by method of moments (empirical Bayes).

It also reports every defensible specification rather than one, since the
laughter decision is a fork the text describes but the figures do not implement.

Outputs `analysis/hand-extracted/ha-pooled-multiverse.csv`.
"""
import csv
import re
import statistics as st
from collections import Counter
from pathlib import Path

HERE = Path(__file__).parent
exec(open(HERE / 'filter-ha-concordance.py').read().split('def main()')[0])

REDUP = re.compile(r'\bha[\s,!.]+ha\b|\bhaha|\bah\s+ha\b|\ba\s+ha\b', re.I)
LAUGH = re.compile(r'\b(hee|hi hi|ho ho|hu hu|lol|haaa+|hahaha)\b', re.I)

WORDS_M = {'US': 386.8, 'CA': 134.8, 'GB': 387.6, 'IE': 101.0, 'AU': 148.2,
           'NZ': 81.4, 'IN': 96.4, 'LK': 46.6, 'PK': 51.4, 'BD': 39.5,
           'SG': 43.0, 'MY': 41.6, 'PH': 43.2, 'HK': 40.5, 'ZA': 45.4,
           'NG': 42.6, 'GH': 38.8, 'KE': 41.1, 'TZ': 35.2, 'JM': 39.6}


def load():
    d = {}
    for c in WORDS_M:
        p = HERE / 'hand-extracted' / 'ha-concordances' / f'ha_uh-{c}.tsv'
        d[c] = [l.split('\t')[-1] for l in p.read_text(encoding='utf-8').splitlines() if l.strip()]
    return d


def count(rows, laughter, unclear_weight):
    """Return (k, n) interjection tokens out of tokens sampled."""
    k = 0.0
    for x in rows:
        cl = classify(x)
        is_laugh = bool(REDUP.search(x) or LAUGH.search(x))
        if cl == 'interjection':
            if is_laugh and not laughter:
                continue
            k += 1
        elif cl == 'unclear':
            k += unclear_weight
    return k, len(rows)


def pool(obs):
    """Empirical-Bayes shrinkage of binomial rates. obs: {unit: (k, n)}.

    Prior Beta(a, b) fitted by method of moments on the observed rates, then
    each unit's posterior mean is (k + a) / (n + a + b). Units with small n move
    furthest toward the grand mean, which is the point.
    """
    rates = [k / n for k, n in obs.values()]
    m = st.mean(rates)
    v = st.variance(rates)
    # method of moments; guard against a variance too large for a beta fit
    scale = max(m * (1 - m) / v - 1, 1e-6) if v > 0 else 1e6
    a, b = m * scale, (1 - m) * scale
    return {u: (k + a) / (n + a + b) for u, (k, n) in obs.items()}, (a, b)


def main():
    data = load()
    tab = {}
    with open(HERE.parent / 'data' / 'glowbe-interjection-frequencies.csv') as f:
        for row in csv.DictReader(f):
            if row['item'] == 'ha':
                tab = {k: float(v) for k, v in row.items() if k != 'item'}

    specs = [(lg, uw, f"laughter={'in' if lg else 'out'}, unclear={lab}")
             for lg in (True, False)
             for uw, lab in ((0.0, 'excl'), (0.5, 'half'), (1.0, 'incl'))]

    out = []
    for laughter, uw, label in specs:
        obs = {c: count(data[c], laughter, uw) for c in WORDS_M}
        raw = {c: k / n for c, (k, n) in obs.items()}
        pooled, (a, b) = pool(obs)
        adj_raw = {c: tab[c] * raw[c] for c in WORDS_M}
        adj_pool = {c: tab[c] * pooled[c] for c in WORDS_M}
        cv = lambda d: st.stdev(d.values()) / st.mean(d.values())
        out.append(dict(spec=label, prior_a=round(a, 2), prior_b=round(b, 2),
                        mean_raw=round(st.mean(adj_raw.values()), 2),
                        cv_raw=round(cv(adj_raw), 3),
                        mean_pooled=round(st.mean(adj_pool.values()), 2),
                        cv_pooled=round(cv(adj_pool), 3),
                        ke_rank_raw=sorted(adj_raw, key=lambda k: -adj_raw[k]).index('KE') + 1,
                        ke_rank_pooled=sorted(adj_pool, key=lambda k: -adj_pool[k]).index('KE') + 1))

    dest = HERE / 'hand-extracted' / 'ha-pooled-multiverse.csv'
    with dest.open('w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(out[0]))
        w.writeheader()
        w.writerows(out)

    print(f"  {'specification':34} {'CV raw':>7} {'CV pooled':>10} {'KE rank':>9}")
    for o in out:
        print(f"  {o['spec']:34} {o['cv_raw']:7.3f} {o['cv_pooled']:10.3f} "
              f"{o['ke_rank_raw']:4} -> {o['ke_rank_pooled']:2}")
    print(f"\n  tabulated CV for comparison: "
          f"{st.stdev(tab.values())/st.mean(tab.values()):.3f}")
    print(f"  wrote {dest}")

    # how far does shrinkage move the noisiest and least noisy units?
    obs = {c: count(data[c], True, 0.0) for c in WORDS_M}
    pooled, _ = pool(obs)
    print("\n  shrinkage on the headline specification, largest movers:")
    moves = sorted(((c, obs[c][1], obs[c][0] / obs[c][1], pooled[c]) for c in WORDS_M),
                   key=lambda r: -abs(r[2] - r[3]))
    for c, n, r, p in moves[:5]:
        print(f"    {c}  n={n:5}  raw {r:6.1%} -> pooled {p:6.1%}  ({(p-r)*100:+.1f} pts)")


if __name__ == '__main__':
    main()
