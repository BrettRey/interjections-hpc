# The `ha` audit: result and the decision it forces
<!-- SUMMARY: all 20 GloWbE sections hand-filtered; ha's tabulated figures are the full tagged count including iterated laughter, which §6.1 says is excluded, so the stated criterion was never applied and the "lower bound" caveat is backwards · status: needs Brett's decision · updated: 2026-07-27 -->

Twenty pulls of tagged `ha_uh`, one per section, filtered with
`analysis/filter-ha-concordance.py` (39/40 on its labelled validation set).
Per-country rates in `analysis/hand-extracted/ha-corrected-rates.csv`.

## The finding that forces a decision

§6.1 states a criterion: "Iterated \mention{HA! HA!} is a rendering of
laughter, closer to eye dialect than to a lexical item, and **I exclude it on
that ground**; \mention{ha} used for sarcasm or scepticism is an interjectional
use and is counted." It then tells readers who would count laughter to "treat
the \mention{ha} figure as a lower bound."

**The exclusion is not in the figures.** Iterated laughter is 51.5% of tagged
`ha` in the United States and 63.0% in Great Britain. If it had been excluded,
the US figure would be near 10 per million rather than the tabulated 20.7. And
the tabulated 20.7 over a 386.8M-word section implies 8,007 tokens, against the
8,100 the interface reports for the whole tagged set: a 1% difference, so the
table is the full count.

So the caveat runs the wrong way. For a reader who accepts the stated
criterion, the figure is not a lower bound; it is roughly double.

## Three columns, and the choice between them

| | mean pmw | CV |
|---|---|---|
| as tabulated | 20.7 | 0.412 |
| corrected, laughter counted as interjectional | 13.2 | 0.396 |
| corrected, laughter excluded per the stated criterion | 4.0 | 0.793 |

**The choice is Brett's, because it is his analytical criterion, and the two
options give different papers:**

1. **Apply the exclusion.** `ha` becomes a 4.0 pmw item with CV 0.793, which
   moves it from the middle of the core group to the most variable core item.
   Consistent with the stated method, but it changes what `ha` contributes to
   the "core items show structured variation" claim.
2. **Drop the exclusion from the method.** Say that iterated laughter is
   counted, delete the "lower bound" sentence, and use the 13.2 pmw column. The
   paper already concedes the ground for this: it notes that "iterated
   \mention{haha} in digital writing has arguably conventionalized into a form
   in its own right".

Option 2 is the smaller edit and the better-motivated one on the paper's own
reasoning. Option 1 is what the current text promises.

## Contamination, which is a separate matter and now measured

Interjection rates in tagged `ha` run from 34.5% (Bangladesh) to 84.0% (Great
Britain). The contaminants differ by region, which is why per-country rates
were necessary:

- **hectare** dominates in East Africa and South Asia: Tanzania 48.4%, Kenya
  48.0%, Bangladesh 45.4%, Ghana 26.5%, Nigeria 26.6%
- **personal names** dominate in Singapore, where only 6.1% is hectare but
  roughly 30% is names, mostly Korean given names in drama recaps (*Jae Ha*,
  *In Ha*, *Chun Ha*, *go ha ni*) plus Chinese names

Singapore matters most because at 51.0 pmw it is the highest `ha` figure in the
table by double, and it is currently doing the most work in the claim that core
items show structured cross-country variation.

Rank changes on the laughter-counted correction are large: Kenya 5th to 15th,
Hong Kong 3rd to 8th, Tanzania 12th to 17th, Bangladesh 16th to 20th, while
the United States rises 8th to 3rd because others fall around it.

**But the CV barely moves, 0.412 to 0.396.** The correction compresses the top
of the distribution rather than spreading it, so the dispersion statistic §6.1
reports survives even though the country-by-country picture changes
substantially. Figure 1 plots the per-country values, so the figure changes
where the statistic does not.
