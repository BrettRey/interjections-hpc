"""Concept sketch only: invented membership sets, arbitrary fixed positions."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge

OUT = Path(__file__).resolve().parent
plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["EB Garamond", "DejaVu Serif"],
    "font.size": 12,
    "pdf.fonttype": 42,
    "svg.fonttype": "none",
})

# Geometry is for label placement, not a feature space or embedding.
positions = {
    1: (.65, 2.45), 2: (1.65, 3.05), 3: (2.35, 2.30),
    4: (1.55, 1.50), 5: (.75, .65), 6: (3.25, 3.05),
    7: (3.85, 2.00), 8: (3.35, .90), 9: (2.35, .42),
}
members_a = {1, 2, 3, 4, 5}
members_b = {3, 4, 6, 7, 8}
blue, rust, grey = "#2E5077", "#C74F41", "#D5D5D5"

fig, axes = plt.subplots(1, 3, figsize=(11, 4.7))
fig.subplots_adjust(left=.025, right=.98, bottom=.20, top=.77, wspace=.15)
fig.text(.5, .94, "Same bearers, different groupings", ha="center", fontsize=19)
for ax, mode, title in zip(axes, ["a", "b", "both"],
                           ["Grouping A", "Grouping B", "Memberships together"]):
    ax.set(xlim=(.1, 4.55), ylim=(-.10, 3.65), aspect="equal")
    ax.axis("off")
    ax.set_title(title, fontsize=14, pad=13)
    for i, (x, y) in positions.items():
        a, b = i in members_a, i in members_b
        if mode == "both" and a and b:
            ax.add_patch(Wedge((x, y), .125, 90, 270, fc=blue, ec="none"))
            ax.add_patch(Wedge((x, y), .125, -90, 90, fc=rust, ec="none"))
        else:
            colour = grey
            if a and mode in ("a", "both"):
                colour = blue
            if b and mode in ("b", "both"):
                colour = rust
            ax.add_patch(Circle((x, y), .125, fc=colour, ec="none"))
        ax.text(x+.18, y, f"b{i}", va="center", ha="left", color="#262626")

legend_ax = fig.add_axes([.22, .12, .56, .045])
legend_ax.set(xlim=(0, 1), ylim=(0, 1))
legend_ax.axis("off")
for x, c, label in [(.02, blue, "A membership"), (.39, rust, "B membership"),
                    (.76, grey, "Not selected")]:
    legend_ax.scatter([x], [.5], s=55, color=c, edgecolors="none")
    legend_ax.text(x+.035, .5, label, va="center", fontsize=11)
fig.text(.5, .043, "Illustrative memberships. Positions and distances carry no meaning.",
         ha="center", fontsize=11, color="#444444")
for ext in ("png", "pdf", "svg"):
    fig.savefig(OUT/f"crosscutting-bearers.{ext}", dpi=180, facecolor="white")

assert members_a & members_b == {3, 4}
assert members_a - members_b and members_b - members_a
print("Saved conceptual sketch; no manuscript files changed.")
