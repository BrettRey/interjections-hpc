# Quote audit — full verbatim check of every quotation in main.tex
<!-- SUMMARY: 27 \enquote{} occurrences audited; 9 checkable against held sources, of which 1 clean, 7 defective, 1 page-wrong; 5 unverifiable for want of the source · status: fixes-pending · updated: 2026-07-24 -->

Run 2026-07-24 against `main.tex` as submitted to JoP (PRAGMA-D-26-00584). Method: balanced-brace extraction of every `\enquote{}` (27 top-level, 29 counting two nested inside item 17), classification into source quotations vs. scare quotes/mentions, then verbatim string search against the source text with page verification from the PDF page images where pagination was recoverable.

## Headline

**Of the nine quotations that could be checked against sources held locally, one was clean.** Two are fabricated, one is misquoted, four present invented hedge words as the literature's own, and one has the right words on the wrong page. Five more can't be checked because the source isn't held.

## Verdicts

| # | Line | Quoted words | Cited as | Verdict |
|---|------|--------------|----------|---------|
| 2 | 87 | marginal and anomalous | Quirk et al. 1985: 67 | **VERIFIED.** Wording, attribution and page all correct. The phrase modifies "(d) interjections" on printed p. 67; an OCR line break hides this in the markdown, which is why it looks like it describes numerals. |
| 7 | 272 | parenthetical strings that are not integrated in clause structure | H&P 2002: 1350 | **FABRICATED.** "parenthetical string" occurs 0 times in CGEL. The page is right: CGEL p. 1350 opens §15.5 Supplementation. Verbatim replacement on that same page: "elements which occupy a position in linear sequence without being integrated into the syntactic structure of the sentence". |
| 8 | 349 | bleached of [its] original meaning | Gehweiler 2008: 72 | **FABRICATED, and worse than recorded.** "original meaning" occurs 0 times anywhere in Gehweiler, not just on p. 72. The only "bleach" in the paper is "the colour of bleached bones" inside a BNC example. There is no correct page to move this to; it must be paraphrased or replaced with a real Gehweiler sentence. |
| 11 | 423 | commonly (occupy their own intonation unit) | cf. Ameka 1992, Wilkins 1992 | **NOT SUPPORTED by Ameka.** Ameka's single "commonly" is about *no* not being commonly used in auditor feedback. Wilkins unchecked (source not held). |
| 12 | 424 | typically (lack inflection) | as above | **NOT SUPPORTED by Ameka.** Four uses, none about inflection: particles' functions, particles' propositional content, discourse markers' integration, primary interjections vs. routines. |
| 13 | 424 | usually (resist syntactic integration) | as above | **NOT SUPPORTED by Ameka.** Four uses, none about this. The nearest genuine sentence uses a different word: "Discourse markers are also *typically* not we!1 [well] integrated into the grammar of the clause". |
| 14 | 425 | generally (express emotive meaning) | as above | **ABSENT.** "generally" occurs 0 times in Ameka 1992. |
| 17 | 715 | A kind may be natural "from the point of view of" some discipline or disciplinary matrix but not "from the point of view of" another | Boyd 1999: 150 | **WORDING OK, PAGE WRONG.** The sentence is on printed p. **160** (physical p. 20; offset confirmed across pp. 158–163). One dropped comma: Boyd has "matrix, but not". |
| 24 | 1372 | sample the space of possible resources | Dingemanse 2020 (no page) | **MISQUOTED.** Dingemanse wrote "sample the **landscape** of possible resources" ("space of possible" 0 hits, "landscape of possible" 1 hit). The substitution is not innocent: the next sentence in `main.tex` leans on "that space" to introduce the paper's own property-space vocabulary. |

## Unverifiable — source not held

Searched `literature/`, the whole portfolio tree, `~/Downloads`, `~/Documents`, and the Mendeley Desktop library.

| # | Line | Quoted words | Cited as | Note |
|---|------|--------------|----------|------|
| 1 | 80 | a sudden passion of the mind | Bullokar 1586: 373 | Not held in any form. |
| 3 | 94 | there really isn't anything interesting for a grammar to say | H&P 2005: 16 | The Mendeley copy of *A Student's Introduction* is front matter only (3 pages, confirms "First published 2005"). Brett co-authored the 2nd edition and will have a print copy. |
| 6 | 248 | few, if any, papers focus on the morphology of interjections | Libert 2019 | Oxford Bibliographies, paywalled, no page in the cite. |
| 9 | 389 | highly conventionalized prepatterned expressions whose occurrence is tied to more or less standard communication situations | Coulmas 1981: 2–3 | The Mendeley "Coulmas" folder holds only a Festschrift, not *Conversational Routine*. |
| 10 | 396 | a distinct pragmatic and semantic subtype of interjections | Wilkins 1992: 142 | Not held. Also the second source behind items 11–14. |

Given the confirmed rate among checkable quotations, treat all five as unverified rather than as presumptively sound.

## Unsourced glosses (not fabrication, but fix)

Items 19 and 20, l. 746–747, in a footnote: Latin *ejaculatio* glossed "a throwing out" and *interjectio* "a throwing between", both in quote marks with no citation. The glosses are standard, but quote marks without a source invite the same objection. Either cite a dictionary or drop the quote marks.

## Scare quotes and mentions — no source claim, no action

Items 4, 5, 15, 18, 21, 22, 23, 25, 26, 27 quote the word *interjection* or a phrase of the paper's own. Item 16 ("genuine kinds", l. 549) alludes to the natural-kinds debate without attribution but is hedged as "in the strongest sense", so it reads as a scare quote rather than a citation. Item 27 ("inconsistent", l. 2148) is a coding-reliability band defined in the paper itself.

## Method warning that matters beyond this paper

`literature/ameka1992-interjections.md` is **mirror-reversed OCR**: each word is character-reversed ("lanruoJ fo scitamgarP" for "Journal of Pragmatics"). A plain search of that file returns zero hits for ordinary English words, so any agent following the house "prefer the .md over the PDF" rule would have concluded that a quotation was absent from Ameka when the file simply cannot be searched. That is the mirror-image failure of the defect this audit is chasing: it manufactures false accusations instead of false quotations.

Two working rules follow. Before concluding a quotation is *not* in a source, check the file is prose at all: a `the `-per-10k-characters density below about 50 means the extraction is degraded and the verdict is void (Ameka scored 0.1; the sound files scored 55–99). And prefer `pdftotext -layout` on the PDF over the pre-made markdown for quote verification, because it preserves running heads, which is what made page verification possible for Quirk, CGEL and Boyd here.

## Fix list

**Applied 2026-07-24.** Clean rebuild afterwards: 33 pages, 0 overfull boxes, 9 underfull, no undefined citations or references, no rerun required, matching the pre-edit baseline exactly.

1. **DONE — l. 272.** Replaced with CGEL's actual p. 1350 wording, page retained: "elements which occupy a position in linear sequence without being integrated into the syntactic structure of the sentence".
2. **DONE — l. 348.** A real Gehweiler sentence was found, and it fits the claim better than the fabrication did. Printed p. 88 (running head "88 Elke Gehweiler"; article is JHP 9:1, 71–93, so printed = physical + 70): "*Jesus* has lost its propositional content, i.e. it is no longer used to refer and hence no longer influences truth conditions." Now cited with `\textcite[88]{gehweiler2008}`, which also fixes the house-style point that the author is the agent of the clause.
3. **DONE — l. 715.** Page 150 → 160, comma restored before "but not".
4. **DONE — l. 1372.** "space" → "landscape", page 191 added, and the following sentence rewritten so the paper's property-space vocabulary no longer depends on the misquote ("describes that landscape as a property space").
5. **DONE — l. 748–749.** Quote marks removed from the two Latin glosses.

6. **DONE — l. 423–437, and the diagnosis changed.** The four hedge words were **not invented, they were misfiled.** All four are Wilkins's own, in parentheses, inside his definition of interjection, which Gehweiler block-quotes on printed p. 73:

   > Interjection: A conventional lexical form which (commonly and) conventionally constitutes an utterance on its own, (typically) does not enter into constructions with other word classes, is (usually) monomorphemic, and (generally) does not host inflectional or derivational morphemes. (Wilkins 1992: 124)

   The defect was that each hedge had been attached to the wrong property:

   | Hedge | Wilkins's property | The old text's property |
   |---|---|---|
   | (commonly and) | constitutes an utterance on its own | occupies its own intonation unit |
   | (typically) | doesn't enter into constructions with other word classes | lacks inflection |
   | (usually) | is monomorphemic | resists syntactic integration |
   | (generally) | doesn't host inflectional or derivational morphemes | expresses emotive meaning |

   Emotive meaning is absent from Wilkins's definition altogether, so that fourth pairing had no source even after the reshuffle; §2.4 carries emotive meaning instead, and the paragraph after this one picks it up.

   Fixed by quoting the definition whole with the hedges intact, and adding the observation that Gehweiler adopts it while calling those same hedged criteria the class's "obligatory properties" (also p. 73). That is a sharper illustration of co-occurrence-without-necessity than four scattered adverbs, since the parentheses are the field conceding the point. A `% VERIFY BEFORE SUBMISSION` comment sits above the passage in `main.tex`: the wording is verified verbatim from Gehweiler's block quote, but the page cite is to Wilkins directly and should be checked against Wilkins 1992: 124 when a copy is available (Wilkins 1992 is JoP 18(2–3): 119–158, so both p. 124 here and p. 142 at l. 396 fall in range).

   Ameka also supplies genuine, correctly-paired hedges if a second witness is ever wanted: p. 105, "Primary interjections are little words or non-words which in terms of their distribution can constitute an utterance by themselves and do not normally enter into construction with other word classes"; p. 105, "Primary interjections ... tend to be phonologically and morphologically anomalous"; p. 106, "Morphologically, interjections do not normally take inflections or derivations in those languages that make use of such forms."

**Still open, needs Brett:**
7. **Items 1, 3, 6, 9, 10** — check against print or paywalled copies. Item 3 is quickest, being Brett's own book.
8. **Preprints** — LingBuzz 009852 and SSRN 6954254 still serve the uncorrected text of items 7, 8, 11–14, 17 and 24, and will keep doing so until the corrected PDF is posted.

## The style linter fights correct quotation

After the fixes, `.house-style/check-style.py` reports four violations that are all **inside** the newly-corrected quotations and must not be acted on: "it is no longer used to refer" (l. 351, wants a contraction), "does not enter into" and "does not host" (ll. 431, 433, want contractions), and "word classes" (l. 432, wants "category"). The linter has no notion of `\enquote{}`, so the more faithfully a passage quotes, the more it complains.

This matters beyond tidiness. Someone clearing those warnings in good faith would silently rewrite Wilkins's and Gehweiler's words, which is a plausible route to exactly the defect this audit exists to catch: a quotation edited into house style until it is no longer a quotation. Either teach the linter to skip `\enquote{}` spans and quoted blocks, or treat every style warning that lands inside quote marks as a stop.

## Minor style note, not an integrity issue

The repaired Dingemanse passage now names the source with `\textcite{dingemanse2020}` at the paragraph's start and again with `\citep[191]{dingemanse2020}` two sentences later. House style flags the doubled citation of a source already named in the clause. The page reference has to live somewhere, so this was left as-is rather than changed unilaterally; a bare `(p.~191)` would also work, since the key is already cited in the paragraph.
