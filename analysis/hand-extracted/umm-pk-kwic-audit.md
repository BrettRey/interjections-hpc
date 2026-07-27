# KWIC audit: `umm_uh` in GloWbE Pakistan

Twenty-token sample pasted by Brett from the English-Corpora.org KWIC display,
2026-07-27. Run to test whether Pakistan's anomalous `umm` count is the English
interjection or a substrate homograph.

## Why it was run

GloWbE Pakistan returns 1,191 `umm_uh` tokens against 153 `um_uh`, a ratio of
7.8. The median variety returns 0.33, and every other variety returns more
`um` than `umm`. A 24-fold departure from the median is not lengthening
behaviour.

## Result

| coding | n | notes |
|---|---|---|
| Arabic teknonym *Umm* ("mother of") | 19 | *Umm Salama* (8), *Umm Atiyah*, *Umm Sharik*, *Umm Sulaym*, *Ibn Umm Maktum*, *Umm Jamil*, *Umm Banin*, *Umm Imarah*, *umm al-Mumineen*, *Ummul Mu'minin* |
| English filler, **mentioned not used** | 1 | `1to1chat.net`: "Don't use tons of fillers like \"umm\" or \"soo\"" |
| English filler, ordinary use | **0** | |

Sources for the nineteen: `al-islam.org` (6), `tanzeem.org` (4),
`understanding-islam.com` (2), `sunniforum.com`, `islamicboard.com`,
`cssforum.com.pk`, `islamhelpline.com`, `islamicperspectives.com`,
`inter-islam.org`, `smma59.wordpress.com`, `maaref-foundation.com`. Hadith and
biographical literature, where *Umm X* is a standard naming formula.

## Bearing

Pakistan's `umm` figure is essentially all artifact, so the summed-variant CV
of 0.72 for `um` is wrong and the reported 0.61 on `um` alone is right. Do not
sum lengthened variants for Pakistan.

Two distinct problems compound here, and only the first is about spelling.
The teknonym is a cross-linguistic homograph. The twentieth token is a
metalinguistic mention, which is the use/mention issue §6.1 already raises for
*yes*, *no*, *ha* and others. A raw-string proxy is exposed to both at once.

Caveat on the sample: these are the twenty rows the interface displayed, not a
random draw, so the 19/20 rate is an indication rather than an estimate. It
does not need to be precise to settle the question, since the hypothesis under
test was whether the tokens are predominantly the interjection, and they are
not.
