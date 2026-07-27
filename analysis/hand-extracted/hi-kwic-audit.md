# KWIC audit: bare-string `hi` in GloWbE Nigeria and Ghana

Samples pasted by Brett 2026-07-27, 20 tokens each, bare string. Last of the
three previously untested conditioning items.

## Result: broadly clean

| variety | greeting | contaminants | rate |
|---|---|---|---|
| NG | 16 | 2 metalinguistic mentions, 1 garbled machine-translated text, 1 nominal *say hi* | 80% |
| GH | 17 | 1 *hi jack* (hijack), 1 *hi life* (highlife), 1 nominal *say hi* | 85% |

## The regionally-patterned one, and it is small

**`hi life` for *highlife***, the West African music genre written as two
words: *"combining the guitar hi life style of playing"* (`ghanashowbiz.com`).
That is the same shape as *hectare* in `ha` — a contaminant carried by text
types the region produces more of — but at 1 token in 20 rather than 8 to 11.

Two others worth naming because they recur for a greeting term rather than for
this variety. Metalinguistic mentions are frequent because *hi* is itself
discussable (*"after saying 'hello' and 'hi'"*, *"saying a friendly 'hi'"*),
and the nominal *say hi* is arguably not an interjection token at all. Both
should be roughly uniform across varieties. `hi jack` is a spacing error, not
regional.

## Summary across all items now probed

| form | interjection rate | contaminant | patterned by variety? | size |
|---|---|---|---|---|
| `ha` | 35–75% | *hectare* | **yes** | **large** |
| `yaar` | 60–65% | Tamil *yaar* 'who', proper names, Hindi matrix | **yes** | **large** |
| `haba` | ~85% | Hausa matrix, Pidgin matrix | yes | moderate |
| `hi` | 80–85% | *hi life* = highlife | yes | small |
| `eh` | 85–95% | transposition typo for *the* | no | small |
| `umm` (PK) | ~0% | Arabic teknonym *Umm* | one variety only | total |

**The generalization the paper can defend.** Raw-string counts are not
uniformly unreliable. Particular forms have particular homographs; some of
those homographs are carried by text types a region produces more of, and only
`ha` and `yaar` have one large enough to matter. That is a sharper and more
useful claim than a blanket caveat, and it says which figures need
qualification and which do not.

`eh` needs none. `hi` needs none at this magnitude. `ha` needs the `ha_uh`
check described in `ha-kwic-audit.md`, which is the one query still outstanding.
