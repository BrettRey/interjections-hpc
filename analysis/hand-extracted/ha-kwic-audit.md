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
