# JoP rejection + citation-integrity forensics
<!-- SUMMARY: JoP rejected PRAGMA-D-26-00584 on a blanket citation-integrity policy (won't accept a revised version); two flagged quotes CONFIRMED confabulated; full 29-quote audit needed before any resubmission · status: action-needed · updated: 2026-07-23 -->

## Decision

- **Journal of Pragmatics rejected** manuscript **PRAGMA-D-26-00584** on **2026-07-23** (Co-EIC Stavros Assimakopoulos).
- **Blanket policy:** JoP rejects on identified citation-misattribution and **will not accept a revised version of the same paper**. JoP is permanently closed for this paper.
- Split review: R1 positive ("interesting and important"); R2 recommended rejection on prose density/clarity. The citation-integrity finding, surfaced in the editors' own checks, is what ended it.

## Citation forensics — CONFIRMED against the source texts (both in `literature/`)

Both flagged "quotations" are paraphrases wrapped in quote marks with a page cite. The underlying claims are correct and in the sources; the quoted **words** are not.

1. **H&P p. 1350** — `main.tex` l. 272–273: `\enquote{parenthetical strings that are not integrated in clause structure} \citep[1350]{HuddlestonPullum2002}`.
   - "parenthetical strings" appears **nowhere** in CGEL (`literature/huddlestonpullum2002.md`). CGEL's actual supplement wording: *"not integrated into the syntactic structure as a dependent"*; *"loosely attached, set off from the rest in speech by separate intonational phrasing and in writing by punctuation"*; *"elements that occupy a linear position but are not integrated into the structure of the clause."* Fix: use one of these verbatim with its correct page, or drop the quote marks and paraphrase.

2. **Gehweiler 2008 p. 72** — `main.tex` l. 349–350: `\enquote{bleached of [its] original meaning}` `\citep[72]{gehweiler2008}`.
   - Gehweiler p. 72 (`literature/gehweiler2008-gee.md`) is a page of **BNC/GoogleGroups corpus examples** of "Jesus!". The only "bleached" on that page is inside a BNC example ("the colour of bleached bones") — unrelated to semantic bleaching. No Gehweiler sentence there matches the quote. Her thesis is about bleaching, but that quotation isn't hers. Fix: paraphrase, or find a real verbatim Gehweiler sentence + correct page.

## Scope: this is not just two quotes

The paper has **29 `\enquote{}` quotations**. If two flagged ones are both confabulated, none can be trusted on inspection. **A full quote audit — every direct quote verified verbatim against its source and page — is the honesty gate before any resubmission.** This is the source-grounding LAW failure mode (paraphrase presented as verbatim quote); the signature risk of LLM-assisted drafting. Consider a portfolio-wide quote spot-check of other recently drafted papers.

## Reviewer triage (for the eventual revision)

**R2 (reject vote):** hostile tone, two real signals under it — (a) prose density/clarity: define "profile," "supports inferences," and name the pragmatic framework behind "contributes to theoretical pragmatics"; (b) **R2 independently flags the "Homeostatics" framing as unmotivated** — the same HPC-banner issue being trimmed programme-wide; reframe this paper projectibility-first too. Resist R2 on the path-dependence paragraph: that's the novel core (R1 valued it) — clarify, don't cut.

**R1 (positive vote):** adopt most; several catch internal inconsistencies —
- *hello* = interjection on p. 5 but routine formula on p. 24 (fix inconsistency).
- "goddammit preserves VO structure" filed under morphology but is syntactic — and §Syntax already treats *damn*'s complement as syntactic residue (internal contradiction).
- "token" → "type" for *oh*; agreement direction ("verb agrees with subject NP", not the reverse); Tables 2 and 3 need intro sentences.
- Substantive: must a hearer *identify* a form as an interjection to make the predictions? (*Bummer!*, *groovy*) — distinguish form-driven from category-driven inference.
- Libert (2012), single-property definition of interjections — real missing reference; verify it exists, then engage.
- Reject R1's anti-contraction note: house style prefers contractions.

## Plan

1. Full 29-quote audit → list every confabulated/mis-paged quote with correct wording + page.
2. Fix citations (verbatim + correct page, or paraphrase).
3. Clarity pass + projectibility-first reframe (drop the homeostatic banner).
4. Adopt R1's punch list.
5. Retarget: **Corpus Pragmatics** (designated backup), only after making the GloWbE/COHA method central; complete a venue-decision record first. JoP is closed.
6. Surfaces not yet updated (PORTFOLIO, website, dashboard, venue ledger, prediction ledger) — pending; only STATUS.md state line corrected so far.

## Sources verified

- `literature/huddlestonpullum2002.md` (CGEL 2002) — supplement definitions checked.
- `literature/gehweiler2008-gee.md` (Gehweiler 2008, "gee") — p. 72 checked.
