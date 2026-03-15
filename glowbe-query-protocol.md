# GloWbE Query Protocol: Conditioning Recovers Structure (P5)

## Purpose

Test whether apparent gradience in interjection frequency decomposes when conditioned on country. If conditioning on country significantly reduces variance in relative frequency, the gradience is structured (not random) and the social-indexing maintenance claim holds.

## Corpus

GloWbE (Corpus of Global Web-Based English), 1.9 billion words, 20 countries.
Access: https://www.english-corpora.org/glowbe/

## Queries

### Core items (10 most frequent interjection-tagged)

For each item below, search with POS tag = interjection (UH). Record **frequency per million words** for each of the 20 countries.

| Item | Expected pattern |
|------|-----------------|
| yes | Broadly distributed |
| no | Broadly distributed |
| oh | Broadly distributed |
| yeah | Broadly distributed, possibly higher in informal-register countries |
| hi | Broadly distributed |
| hey | Broadly distributed |
| wow | Broadly distributed |
| hello | Broadly distributed |
| ah | Broadly distributed |
| ha | Broadly distributed |

### Regional control items (expected strong conditioning)

| Item | Expected pattern |
|------|-----------------|
| lah | Near-categorical in SG, MY; near-zero elsewhere |
| yaar | Near-categorical in IN, PK; near-zero elsewhere |
| haba | Near-categorical in NG; near-zero elsewhere |
| eh | Expected higher in CA, possibly AU, NZ |
| cheers | Expected higher in GB |

### Boundary items (fillers / routine formulae)

| Item | Expected pattern |
|------|-----------------|
| um | Broadly distributed (filler) |
| uh | Broadly distributed (filler) |
| bye | Broadly distributed (routine formula) |
| please | Broadly distributed (routine formula) |

## Countries (20)

AU, BD, CA, GH, GB, HK, IN, IE, JM, KE, MY, NZ, NG, PK, PH, SG, ZA, LK, TZ, US

## Recording format

Create a CSV with columns:

```
item, AU, BD, CA, GH, GB, HK, IN, IE, JM, KE, MY, NZ, NG, PK, PH, SG, ZA, LK, TZ, US
yes, [freq/million], ...
no, [freq/million], ...
```

Save as `data/glowbe-interjection-frequencies.csv`

## Analysis

1. **Pooled variance:** For each item, compute the coefficient of variation (CV = SD/mean) across 20 countries.

2. **Structured vs. uniform:** Compare CVs:
   - Regional controls (lah, yaar, haba) should have very high CVs (near-zero in most countries, high in 1-2).
   - Core items should have lower CVs if broadly distributed.
   - The interesting question: do core items show *any* structured geographic variation, or are they uniformly distributed?

3. **The test:** If conditioning on country produces significant reduction in prediction error (i.e., knowing the country helps predict the frequency), P5 holds. If all items are uniformly distributed and country adds no predictive power, the maintenance claim for social indexing is unsupported.

4. **Simple version:** Even without formal modelling, the CV comparison tells the story. If regional controls have CVs > 2.0 and core items have CVs < 0.5, that's structured variation. Report the table.

## What goes in the paper

- The frequency table (or a summary) in the text or as supplementary material
- A sentence or two reporting whether conditioning on country reduces variance
- Update "designed but unexecuted" to report actual results

## Defeat condition

If conditioned and pooled models perform identically (i.e., country adds no predictive power for any item, including the regional controls), the social-indexing maintenance claim is unsupported. Note: the regional controls (lah, yaar, haba) are expected to show strong conditioning almost trivially. The interesting question is whether core items also show non-trivial geographic structure.
