"""Interjection-inventory turnover in COHA, 1820s-2010s.

Source: analysis/hand-extracted/interjection-lemmas-coha-by-decade.csv,
transcribed from a `_uh` lemma search on English-Corpora.org (COHA, 405M
words), 2026-07-27. Every row was checked against the interface's own
reported all-decades total before use.

The point of the figure is §4.7's claim: the category position persists while
the lexical inventory turns over. Three of the six most frequent interjection
lemmas in the 1820s are gone from the top six by the 2010s, and three forms
absent or negligible in the 1820s have replaced them.
"""
import csv
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / '.house-style'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import plot_style

SRC = Path(__file__).parent / 'hand-extracted' / 'interjection-lemmas-coha-by-decade.csv'
OUT = Path(__file__).parent.parent / 'figures' / 'interjection-turnover.pdf'

data = defaultdict(dict)
for r in csv.DictReader(SRC.open()):
    data[r['lemma']][int(r['decade'])] = float(r['per_mil'])

LEAVING = ['nay', 'o', 'ah']
ARRIVING = ['yeah', 'hey', 'uh']
HOLDING = ['no', 'oh', 'yes']

plot_style.setup(font_size=9, tick_size=8)
fig, axes = plt.subplots(1, 3, figsize=(7.4, 2.9), sharey=True)

panels = [
    (HOLDING,  'hold the top six', plot_style.COLORS['dark']),
    (LEAVING,  'drop out by the 2010s', plot_style.COLORS['secondary']),
    (ARRIVING, 'enter by the 2010s', plot_style.COLORS['tertiary']),
]

decades = sorted(next(iter(data.values())).keys())

for ax, (group, title, colour) in zip(axes, panels):
    # every other lemma in light grey, so each panel carries the whole field
    for lemma, series in data.items():
        ax.plot(decades, [series[d] for d in decades],
                color=plot_style.COLORS['light'], linewidth=0.7, zorder=1)
    # nudge labels apart where endpoints sit close together on the log scale
    NUDGE = {'no': 7, 'oh': -2, 'yes': -9, 'hey': 1, 'uh': -3, 'yeah': 2}
    for lemma in group:
        ys = [data[lemma][d] for d in decades]
        ax.plot(decades, ys, color=colour, linewidth=1.6, zorder=3)
        ax.annotate(lemma, xy=(decades[-1], ys[-1]),
                    xytext=(3, NUDGE.get(lemma, 0)),
                    textcoords='offset points', va='center', fontsize=8,
                    color=colour, fontstyle='italic')
    ax.set_yscale('symlog', linthresh=1)
    ax.set_title(title, fontsize=9)
    ax.set_xlim(1820, 2075)
    ax.set_xticks([1820, 1900, 2010])
    ax.set_xticklabels(['1820s', '1900s', '2010s'])
    plot_style.remove_spines(ax)
    plot_style.add_grid(ax, axis='y')

axes[0].set_ylabel('tokens per million words')
fig.tight_layout()
OUT.parent.mkdir(exist_ok=True)
fig.savefig(OUT, bbox_inches='tight')
print(f'wrote {OUT}')
