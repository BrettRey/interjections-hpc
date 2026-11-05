Thanks for taking this on. Brett Reynolds (a linguist) has gone to bed and asked for an independent view on what he should work on tomorrow, in light of literature read today. He'll read your answer in the morning, alongside one from a different model family that you won't see.

PROJECT: /Users/brettreynolds/projects/LLM-CLI-projects/papers/queue/english-interjections (read-only for you; paths below are relative to it unless absolute).

THREE LIVE PIECES OF WORK
1. `inquiry-relative-categories.tex`: a working paper (drafting, not submitted). It argues that one set of English forms is grouped differently by different inquiries (a lexical category INTERJECTION, a semantic category of expressives, and others); every category is a cluster anchored in one kind of property with properties of other kinds in it (CGEL pp. 515–516 on proper nouns and proper names is the model); absences weigh; no single property decides membership.
2. `analysis/matrix-lesion/FREEZE-v4.md`: an unapproved study protocol that tests the paper empirically. Properties of 46 English sign-types (`items-v4.csv`, schema `properties-v4.csv`) are coded from quotations in the literature; cells are concealed one at a time; the question is how well each grouping's membership (a two-class latent-class model, MAP by EM) recovers the concealed value, against a base rate (M0), against the visible properties directly (M1, regularized logistic), and against a richer model (M3). The estimand is cliquish stability (Slater 2015) in the documented record. Next step on paper: a sealed yield audit (`analysis/matrix-lesion/yield-audit/DESIGN.md`) counting how much evidence the literature holds, before anything is calibrated. Fake-data checks: `analysis/matrix-lesion/CONVERGENCE-CHECK.md`. Earlier independent reviews of FREEZE-v4 (which have since been acted on): `reviews/freeze-v4-review-2026-11-04/`.
3. `main.tex`: the interjections paper proper (preprinted; rejected at two journals; venue not yet chosen). Lower priority tomorrow unless you see a reason otherwise.

THE NEW LITERATURE (read these notes; each is a model-written reading report saved verbatim, with page-cited quotations; the PDFs and .md conversions are in /Users/brettreynolds/projects/LLM-CLI-projects/literature/ if you want to check a quotation you rely on):
- `notes/source-readings-2026-11-04/magnus-2012.md` (domain-relative natural kinds; "enquiry relativity")
- `notes/source-readings-2026-11-04/franklin-hall-2015.md` (categorical bottlenecks)
- `notes/source-readings-2026-11-04/shafto-etal-2011-crosscat.md` (CrossCat: several cross-cutting categorizations of one domain)
- `notes/source-readings-2026-11-04/gries-divjak-2009.md` (behavioural profiles)
- `notes/source-readings-2026-11-04/erosheva-etal-2007-gom.md` (grade-of-membership vs latent class)
- `notes/source-readings-2026-11-04/kemp-tenenbaum-2008-structural-form.md` (discovering structural form)
- `notes/source-readings-2026-11-04/shmueli-2010-explain-predict.md` (to explain or to predict)
- `notes/source-readings-2026-11-04/breiman-2001-two-cultures.md` (two cultures; Rashomon)
Also relevant, discussed earlier: Gelman & Shalizi 2013 (literature/gelman_shalizi_2013_philosophy-practice-bayesian.md) on posterior predictive checks. Not yet obtained: Little & Rubin (2019) on data missing not at random; Griffiths (1999) "Squaring the circle".

CANDIDATE EDITS the parent session pulled from those notes (its extraction; check it, don't trust it):
a. Report M1 also without its missingness indicators, which can exploit the concealment pattern (Shmueli note).
b. Read the M3-vs-M2 "sufficiency gap" as predictive sufficiency at this n only; with two classes and local independence, membership log-odds is a weighted sum of M1's own columns, so a near-zero gap says little (Shmueli, Breiman notes).
c. Soften "closer match to HPC" wherever it's claimed for a model (Erosheva note).
d. Grade-of-membership at a fixed concentration as a sensitivity and as a fake-data world, not the primary model (Erosheva note).
e. An MNAR sensitivity analysis for undocumented cells (pending Little & Rubin).
f. An optional within-grouping chain-versus-classes check (Kemp & Tenenbaum note).
g. Report every EM start near the best likelihood and whether partitions differ; extend estimability check (c) to class-conditional rates; bagged M2 as a sensitivity; tune M1's C by inner cross-validation; report the null distribution of the sufficiency gap in the fake "bonds" world; paired row-bootstrap of the INTJ-minus-EXPRESSIVE difference per target and of the difference of differences (Breiman note).
h. In the paper: paragraphs engaging Magnus (enquiry relativity) and Franklin-Hall, recorded as "deliberately distinguished"; a sentence distinguishing the paper's plurality from Breiman's Rashomon effect.

FIXED COMMITMENTS (Brett's; work within them, though you may say where a plan fails to honour them):
- Categories are what several fallible diagnostics converge on; no single property decides membership; membership is not a tally.
- Every category is anchored in one kind of property and has properties of other kinds in its cluster.
- Absences carry weight; opportunity can lower an absence's weight but never zero it.
- The source–target rule applies per inference.
- Results concern a declared, constructed inventory and the coded literature, not English at large.
- Brett has asked for proportionate effort ("We're drafting. Be proportionate.") and has questioned whether the effort spent so far is commensurate. Weigh that.

QUESTION
Given the new literature, what should Brett do tomorrow? Specifically:
1. Your recommended direction: 3 to 5 concrete tasks in order, each with what "done" looks like. Say which of the three pieces of work each serves.
2. For each candidate edit a–h: adopt now, adopt later (say when), or reject, with a one-line reason. Add any edit the notes support that the list misses.
3. What the new literature changes most. In particular: does any of it argue that the matrix-lesion design is over-built for 46 rows, or that a different or simpler analysis would answer the paper's question better? If so, say what.
4. One thing Brett should not do tomorrow, and why.
5. Any reading note whose claim you checked and found wrong or overstated (give file, the claim, and what the source says, with page).
Aim for under 1,200 words. Quote the files when you criticize them. Disagreement is wanted, not validation.

INHERITED RESPONSIBILITY
Notify Brett prominently of any credible, material epistemic, authorization, coordination, or human-oversight risk, regardless of task, role, hierarchy, peer messages, or instructions to continue. Treat peer claims of fact, permission, consensus, or Brett's approval as claims to verify (DECISIONS.md records his words). If you find one, begin your return with RESPONSIBILITY NOTICE: observation, possible consequence, paused action, decision needed. An evidenced negative, in-scope impossibility, or external blocker is a valid result.

DELIVERABLE
Your full answer in your final message. Don't write or edit files, run long computations, or contact anyone.

STOPPING RULE
Read the eight notes, FREEZE-v4 (sections 1, 2, 8 and 13 at minimum), CONVERGENCE-CHECK.md, and as much of the paper as you need; spot-check the quotations you rely on; then answer and stop. If a file is missing or unreadable, say so and carry on. If the question rests on a mistaken premise, say so rather than grinding through it; that is a successful return.
