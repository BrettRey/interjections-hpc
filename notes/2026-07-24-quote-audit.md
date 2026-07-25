# Quote audit — full verbatim check of every quotation in main.tex
<!-- SUMMARY: every quotation in main.tex audited; 8 fixes applied; all 14 source quotations verified; separate open item: the intro's 'textbook cut it' claim is false of SIEG2, which Brett co-authored · status: all-quotes-verified; one intro pass outstanding (SIEG2 + Libert neglect) · updated: 2026-07-24 -->

Run 2026-07-24 against `main.tex` as submitted to JoP (PRAGMA-D-26-00584). Method: balanced-brace extraction of every `\enquote{}` (27 top-level, 29 counting two nested inside item 17), classification into source quotations vs. scare quotes/mentions, then verbatim string search against the source text with page verification from the PDF page images where pagination was recoverable.

## Headline

**Of the nine quotations checkable against sources held locally, one was clean.** Two are fabricated, one is misquoted, four hedge words are attached to the wrong properties, and one has the right words on the wrong page. All six defects are fixed.

Later passes then cleared four of the five quotations the first pass had filed as unverifiable: Bullokar and H&P 2005 from open repositories, Coulmas through Ameka's verbatim reproduction, and Wilkins from Brett's own copy. Only Libert 2019 is still unchecked. Those passes also turned up a separate, non-integrity problem in the introduction: the claim that the textbook cut interjections is false of the second edition, which Brett co-authored.

Two corrections to my own earlier verdicts, both from checking the primary source rather than reasoning about it: Wilkins p. 142 is verbatim, not a fabrication, and my grounds for calling it suspicious (its absence from Ameka) were an argument from the wrong source; and the Wilkins definition's "constructions" was Gehweiler's transcription error, not the paper's.

**Final: all 14 source quotations verified.** The audit is closed. Two page numbers still want a glance (Bullokar p. 373 in Turner's 1980 pagination, H&P 2005 p. 16), and two unsourced Latin glosses are now unquoted rather than cited.

What remains are not quotation defects but two problems in the introduction, both found while chasing sources, and both wanting one argumentative pass: the SIEG2 currency problem and the Libert neglect problem, below.

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

## Second pass, 2026-07-24: three of the five "unverifiable" quotes resolved

The first pass searched only the local filesystem by filename and stopped. Brett pushed back on both counts. A Spotlight content search plus three open repositories resolved three of the five.

| # | Line | Quoted words | Cited as | Verdict |
|---|------|--------------|----------|---------|
| 1 | 80 | a sudden passion of the mind | Bullokar 1586: 373 | **VERIFIED.** Bullokar's own text, from the Oxford Text Archive's open plain-text edition (`ota.bodleian.ox.ac.uk/.../0025`, `bullok2-0025.txt`, CC BY-NC-SA): "An Interi}ection iz a part of spe^ch that be^\|]to^kn^e}t}h a su}dden passion of the my^nd", i.e. in normalized spelling "An Interjection is a part of speech that betokeneth a sudden passion of the mind." The paper's gloss ("words that betoken") tracks Bullokar's "betokeneth" exactly. Page 373 is Turner's 1980 Leeds pagination and remains unchecked; the OTA text is unpaginated. |
| 3 | 94 | there really isn't anything interesting for a grammar to say | H&P 2005: 16 | **VERIFIED as wording**, and fuller than the paper suggests: "Leaving aside the minor category of interjections (covering words like *oh, hello, wow, ouch*, etc., about which there really isn't anything interesting for a grammar to say)". Page 16 still unchecked. **But see the SIEG2 problem below, which is the more serious issue.** |
| 9 | 389 | highly conventionalized prepatterned expressions whose occurrence is tied to more or less standard communication situations | Coulmas 1981: 2–3 | **VERIFIED** via Ameka's verbatim reproduction at p. 108, which cites the same page range: "highly conventionalised prepatterned expressions whose occurrence is tied to more or less standard communication situations" (Coulmas 1981: 2–3). One orthographic note: Coulmas/Ameka have British "conventionalised"; the paper silently Americanizes it to "conventionalized" inside the quotation marks. Restore the original spelling. |
| 6 | 248 | few, if any, papers focus on the morphology of interjections | Libert 2019 | **VERIFIED**, character-for-character, from Brett's Oxford Academic extract. Libert's sentence: "There does, however, seem to be one gap in the literature: few, if any, papers focus on the morphology of interjections." It is in the entry's Introduction. Page unconfirmed (OBO paginates the *Linguistics* module 67–76); OBO entries are usually cited by section rather than page, so a page may not be needed. **But the same paragraph contradicts the paper's framing — see below.** |
| 10 | 396 | a distinct pragmatic and semantic subtype of interjections | Wilkins 1992: 142 | **VERIFIED**, from Brett's own copy (`~/Downloads/wilkins1992.pdf`). Printed p. 142 confirmed by the running head. Wilkins: "It is true, however, that they form a distinct pragmatic and semantic subtype of interjections because they are tied to specific, and very common, situations, and their function is mainly to acknowledge, promote, and/or maintain social relations in accordance with cultural conventions." My suspicion that this matched the fabrication pattern was wrong. The second p. 142 cite at l. 1802 is also well supported by that page. |

Search record: Spotlight content queries for "Interjections as Deictics", "Conversational Routine", "Bullokar", and "Student's Introduction to English Grammar" over the whole home directory (all hits were Brett's own citing files); `find` over Dropbox, iCloud, Documents, Desktop, Downloads and the Mendeley library; web searches for open repository copies, author copies, and MPG PuRe. Wilkins turned out to be in `~/Downloads` (downloaded by Brett during this session) and is now verified; Libert remains behind the Oxford paywall.

## The SIEG2 problem (new, and not an integrity issue)

`~/Documents/CGEL/` holds the second-edition manuscript, its errata, and the drafting chapters. Checking the intro's claim against them turned up a currency problem in the paper's opening paragraph.

`main.tex` l. 92–95 says H&P "dropped it from the textbook because 'there really isn't anything interesting for a grammar to say' about interjections", and the paragraph lands on "A category real enough for the definitive grammar but thin enough for the textbook to cut."

That is true of the 2005 first edition. **It is false of the second edition, which Brett co-authored.** SIEG2 (978-1-316-51464-1; Huddleston, Pullum & Reynolds) lists interjection among its lexical categories with examples, sets exercises requiring students to tag interjections, and treats interjections as one of the categories that can function as supplements. Its parallel remark, p. 24, is far softer and is a usable quotation in its own right:

> Can interjections ever be heads of phrases? It isn't clear, and we won't try to settle it. (Grammarians typically say very little about interjections, and we don't plan to be an exception.)

So a reviewer holding the current edition finds the paper's premise contradicted by a book the paper's author co-wrote. At a grammar venue like *Journal of Linguistics* that is a likely reviewer.

The fix improves the argument rather than weakening it: cite both editions. The first leaves interjections aside as having nothing interesting in them; the second reinstates the category but concedes that grammarians still say very little about it. That is a better version of the paper's premise, because it shows the category being readmitted without being described, which is exactly the gap the paper fills. It also removes the awkwardness of the author appearing not to know his own book.

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

   Fixed by quoting the definition whole with the hedges intact, and adding the observation that Gehweiler adopts it while calling those same hedged criteria the class's "obligatory properties" (also p. 73). That is a sharper illustration of co-occurrence-without-necessity than four scattered adverbs, since the parentheses are the field conceding the point. **Now verified directly against Wilkins 1992: 124** (running head confirmed; his numbered definition (1)), so the relay through Gehweiler is no longer load-bearing. One correction the primary source supplied: Gehweiler's block quote pluralizes "constructions", where Wilkins has the singular "does not enter into construction with other word classes". The paper had inherited Gehweiler's plural and now follows Wilkins.

   Ameka also supplies genuine, correctly-paired hedges if a second witness is ever wanted: p. 105, "Primary interjections are little words or non-words which in terms of their distribution can constitute an utterance by themselves and do not normally enter into construction with other word classes"; p. 105, "Primary interjections ... tend to be phonologically and morphologically anomalous"; p. 106, "Morphologically, interjections do not normally take inflections or derivations in those languages that make use of such forms."

**Still open, needs Brett:**
7. **Items 1, 3, 9 — resolved 2026-07-24** (see the second-pass table). Remaining: **item 10 (Wilkins p. 142)**, which is unverified and looks like the same paraphrase-in-quote-marks pattern as the confirmed fabrications, so do not submit anywhere until it is checked or rewritten; and **item 6 (Libert)**. Both are reachable through U of T. Also outstanding: page checks for Bullokar p. 373 (Turner 1980 pagination) and H&P 2005 p. 16, and restoring Coulmas's British "conventionalised" spelling at l. 389.
8. **The SIEG2 fix** — rewrite the intro's "dropped it from the textbook" claim to cite both editions (see the SIEG2 section above). This is the highest-value remaining edit: it repairs a claim that a *Journal of Linguistics* reviewer would likely catch, and it strengthens the paper's premise.
9. **Preprints** — done 2026-07-24: LingBuzz 009852 updated, SSRN 6954254 inactive, website mirror and GitHub repo pushed. Note that the next preprint version will need to carry the SIEG2 fix and the Wilkins resolution.

## The style linter fights correct quotation

After the fixes, `.house-style/check-style.py` reports four violations that are all **inside** the newly-corrected quotations and must not be acted on: "it is no longer used to refer" (l. 351, wants a contraction), "does not enter into" and "does not host" (ll. 431, 433, want contractions), and "word classes" (l. 432, wants "category"). The linter has no notion of `\enquote{}`, so the more faithfully a passage quotes, the more it complains.

This matters beyond tidiness. Someone clearing those warnings in good faith would silently rewrite Wilkins's and Gehweiler's words, which is a plausible route to exactly the defect this audit exists to catch: a quotation edited into house style until it is no longer a quotation. Either teach the linter to skip `\enquote{}` spans and quoted blocks, or treat every style warning that lands inside quote marks as a stop.

## Minor style note, not an integrity issue

The repaired Dingemanse passage now names the source with `\textcite{dingemanse2020}` at the paragraph's start and again with `\citep[191]{dingemanse2020}` two sentences later. House style flags the doubled citation of a source already named in the clause. The page reference has to live somewhere, so this was left as-is rather than changed unilaterally; a bare `(p.~191)` would also work, since the key is already cited in the paragraph.

## The Libert neglect problem (found 2026-07-24, needs an intro pass)

The sentence the paper quotes sits inside a paragraph that argues against the paper's broader framing. Libert, immediately before the quoted sentence:

> Interjections have received considerably less attention from linguists than the other parts of speech. This may be due, in part, to the just mentioned view that they are not really linguistic items and thus are of little or no interest from a linguistic point of view. **However, to say that they have been neglected, as some authors do, is an overstatement**; as can be seen in this article, scholars have been thinking and writing about different aspects of interjections for a long time [...] There does, however, seem to be one gap in the literature: few, if any, papers focus on the morphology of interjections.

So Libert's paragraph makes a narrow claim (the gap is specifically morphology) by explicitly rejecting the broad one (general neglect). The paper quotes the narrow sentence while its introduction leans on the broad framing, and Ameka's title, which the paper also cites, is literally "Interjections: The Universal Yet Neglected Part of Speech." A reviewer who follows the Libert citation lands on a sentence calling that framing an overstatement, one clause away from the words the paper borrowed. That reads as selective quotation even though the quotation itself is exact.

The fix strengthens the paper. Libert's distinction is the one the paper actually needs, and it is sharper than the neglect story: interjections have been written about at length, but their *category status* has been denied (Jespersen, Quirk, H&P 2005) and their morphology has gone undescribed. Those are claims about standing and about coverage of one subfield, not about volume of attention, and they survive Libert's objection intact. Under the lexical-category reframe this matters more, not less, since the premise there is denial of category status rather than neglect.

Note also that Libert supplies a source for half the footnote gloss at l. 747–749: "The word interjection comes from the Latin *interjicere* 'to throw between'." That is the verb, not the noun *interjectio*, and Libert says nothing about *ejaculatio*, so it covers part of the footnote only.
