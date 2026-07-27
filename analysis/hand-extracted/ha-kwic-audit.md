# KWIC audit: bare-string `ha` in GloWbE Tanzania, Nigeria, Kenya

Samples pasted by Brett 2026-07-27, 20 tokens each. **Bare string, not
`ha_uh`.** Run as the first of the three untested conditioning items.

## Result

| variety | interjection | hectare | other | rate |
|---|---|---|---|---|
| TZ | 11 | 8 | 1 (garbled spam) | 55% |
| NG | 15 | 4 | 1 (typo for *has*) | 75% |
| KE | 7 | 11 | 2 (place names *Ha Tsiu*, *Ha Long*) | 35% |

## The homograph is *hectare*, and it is regionally patterned

`ha` is the standard abbreviation for hectare, and the contaminating tokens
are agricultural, NGO and development prose: *"85,000 ha in the nearby Wami
Basin"*, *"220,000 Ha. of the arable land"*, *"2,600 ha of marginal lands"*,
*"1.34 kg ha -1"*, *"10,281 ha in ONP of total 429,327 ha"*. Sources include
`un.org`, `unep.org`, `ilri.cgiar.org`, `rukwa.go.tz`, `medwelljournals.com`.

That is worse than a random contaminant. Development and agricultural web
text is exactly what GloWbE's African sections carry more of, so the
contaminant tracks the same axis the country effect is estimated on. Two place
names in the Kenyan sample (*Ha Tsiu* in Lesotho, *Ha Long* in Vietnam) add a
second, smaller source.

## What this does and does not show

It does **not** yet impugn the conditioning table. `ha` there is one of the ten
most frequent **interjection-tagged** forms, so the count is `_uh`-filtered and
hectares should already be excluded. Whether they are depends on the tagger,
and the tagger's record is not reassuring: it assigns all 373 Nigerian *haba*
tokens to noun categories and none to `UH`.

One circumstantial reason to check: Kenya sits fifth highest on `ha` in the
conditioning table at 25 per million, and Kenya's bare-string sample is the
*least* interjectional of the three at 35%. `ha`'s CV in the table is 0.41.

## The query that settles it

**`ha_uh`, KWIC, sections KE then TZ.** If hectare tokens appear under the
interjection tag, the core-item figure is contaminated in the African sections
and the comparison baseline is affected, not just the regional items. If none
appear, the tag is doing its job on this form and the table is fine.

Until that is run, this is a suspicion with a mechanism, not a finding.

---

# Settled: `ha_uh` shows hectares ARE tagged as interjections

Brett ran the settling query 2026-07-27. Twenty tagged tokens each.

| variety | interjection | *hectare* | other | rate |
|---|---|---|---|---|
| KE | 6 | 13 | 1 (proper name, *South Korea's Ha*) | **30%** |
| TZ | 8 | 11 | 1 (garbled text) | **40%** |

So the interjection tag does not exclude *hectare*. Sources are the same
agricultural and development set as the bare-string pull: `ilri.cgiar.org`,
`fao.org`, `un.org`, `rukwa.go.tz`, `sido.go.tz`, `afejnews.org`.

## Consequences

| | as tabulated | corrected on these rates |
|---|---|---|
| `ha` in Kenya | 24.9 pmw | ~7.5 pmw |
| `ha` in Tanzania | 16.8 pmw | ~6.7 pmw |
| Kenya's rank on `ha` | 5th of 20 | **19th of 20** |
| CV of `ha` | 0.41 | 0.49 |

**This reaches the comparison baseline, not the hedged periphery.** `ha` is one
of the ten core items, and its figure is wrong by a factor of three in at least
two varieties, in a direction set by how much agricultural and development prose
a section contains.

## What it corrected in the manuscript

The appendix passage added earlier the same day said core-item counts "are
restricted to the interjection tag, so they exclude other uses of the same
string." That is false, and this audit is what showed it. The passage now says
restriction is not exclusion, gives the Kenya and Tanzania figures, and states
that the tag fails worst where a homograph belongs to a text type a region
produces more of.

## Still open

Whether `ha` should stay in the analysis at all is Brett's call. The other core
items have not been checked under the tag, and there is now a reason to think
tag-restriction is weak generally rather than only for `ha`.
