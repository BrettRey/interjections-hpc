# What the kinship paper offers this one
<!-- SUMMARY: Six approaches from english-kinship-terms (JEngL R&R) mapped onto this paper's open problems; they help most with framing and the GloWbE analysis, least with review board #2's held-out-prediction demand · status: candidates, none adopted · updated: 2026-10-30 -->

Prepared on 2026-10-30 in a PM session, at Brett's question "are there any
ideas or approaches from the kinship paper that would help with
interjections?" These are candidates for his decision; none is adopted.

Kinship sources, all under `../../english-kinship-terms/`:
`english-kinship-terms.md` (review copy of the current revision; section
numbers below are its own), its `DECISIONS.md`, and its private, gitignored
`reviews/` folder for analysis code and records.

## 1. Introduce the three categories through *CGEL*'s name/noun split

Kinship §2.1 separates a semantic classification, *proper name*, from a
lexical category, *proper noun* (*CGEL* pp. 515–516). *Clinton* is a proper
noun; *the University of Manchester* is a name headed by the common noun
*university*. The two overlap in canonical cases without being one category.

This paper's `INTERJECTION_syn`, `INTERJECTION_sem` and `INTERJECTION_prag`
are the same kind of split extended to three. Presenting them as a
generalization of a distinction *CGEL* readers already accept would make the
field-relative claim look familiar rather than exotic. It is the most direct
answer to the Journal of Linguistics referees' complaint about LIN-2026-0100
(the projectibility framework is never introduced for linguists), which
STATUS.md says applies here too. Kinship keeps HPC vocabulary out entirely;
here projectibility can appear operationally ("what membership lets you
predict"), glossed once with Goodman.

Where: the introduction, `sec:fieldrelative-nodes` and the "Category vs.
function" subsection. Check first: kinship records a deliberate departure from
*CGEL*'s own use of *proper name* (its DECISIONS.md, 2026-10-30), so cite
*CGEL* for the noun side and state the semantic sense in this paper's terms.

## 2. An evidential-scope subsection

Kinship §2.2 says what each kind of evidence is for. *CGEL* supplies
constructed illustrations, whose contrasts "express the proposed analysis,
not elicited judgments"; ethnographies describe practice; transcript excerpts
attest constructions in context; only the systematic sample supports
quantities.

This paper mixes more evidence types: the history of *gee*, residual
complement structure, euphemistic deformation, the COHA semantic-residue
study, the preregistered *fie* study (negative), the GloWbE conditioning
analysis, COHA turnover, and the planned CABNC pre-pilot. Saying up front what
each can and can't show is the cheapest fix for the overclaims review board #2
flagged (STATUS.md: "recovers structure at every level", "outperforms", the
`fig:fie-tau` caption, the morphology-gain wording).

## 3. The kinship §5 toolkit for the GloWbE analysis

- **Selection against availability** (§5, opening). A kin term's bare share is
  conditional on that term being chosen; a low rate can reflect grammar,
  preference, or few suitable occasions. The per-million rates here have the
  same ambiguity. Kinship adopted the opportunity-set treatment from
  `english-lbc-functionalist` for this (its DECISIONS.md, 2026-09-25).
- **Common weights over shared recorded contexts** (§5.3, Table 4), estimated
  in a multilevel model with household and corpus variation.
- **Adverse bounds** that assign unresolved cases to the less favourable
  outcome (§5.2), and **leave-one-corpus-out** checks (§5.2–5.3).
- **Per-form reporting** with the confound named: grouping doesn't separate
  relation from lexical form or register (§5.2–5.3).
- **Recovery simulations** under several generating scenarios, showing what the
  sample structure can support (§5.3). Code and records:
  `reviews/model-review-revision-2026-10-29/model-refit-2026-10-30/` and
  `recovery-final-2026-10-30/`.

Board #2's objection to the GloWbE model was that m1 tests whether overall
rates differ by country, not whether item types or boundaries behave
differently (ΔELPD 17.9, SE 13.3). The kinship design is set up to answer the
second kind of question.

## 4. Run the fake-data design check before Gate 0

On 2026-09-22 kinship simulated 80,000 studies with its planned sample
structure; illustrative 15-point contrasts were detected about 22–27% of the
time, so the sample's role was narrowed to validation and description before
any coding (its DECISIONS.md; `reviews/fake-data-simulation-2026-09-22/`).

The CABNC protocol already commits to design simulation (see
`source-hooks/gelman-2026-fake-data-simulation.md`), and that hook's trigger,
the Journal of Linguistics hold lifting, fired on 2026-09-23. Run it before
Gate 0: if the planned sample can't detect a `syn`-versus-`sem` paired
difference of practical size, the pre-pilot's role should shrink before the
AudioBNC licence and audio audit start.

For scale: kinship went from its R&R decision (2026-09-20) to a frozen
900-occurrence comparison (2026-09-23) and an integrated revision
(2026-10-27). It used one AI coder and Brett's label-concealed checks, and its
§5.1 says those checks give no reliability estimate. The CABNC pre-pilot has
sat at Gate 0 since 2026-07-27 with a three-family model panel, 45 schema
templates, 47 leakage checks and 29 reliability gates.

## 5. Local conventions as the explanatory target

Kinship §5.4 reads household bare *Sister* as favouring "a description of
conventional uses over a categorical division by kin relation". That matches
this paper's "conventionalized sign-types" as common bearers, and the
regional items (*haba*, *yaar*, *lah*). STATUS.md already asks for an
item-by-item diagnostic table; kinship's per-form, per-household reporting is
a usable format.

## 6. Recruitment as extension from recognized use (a lead only)

Kinship's learning proposal (abstract; §6.1–6.2): recognizing a form as
someone's designation supports extending familiar names' grammatical patterns
to it. A possible parallel here: a form recognized in exclamatory or response
use takes on interjection grammar (*God* → *gee*; `sec:recruitment`). Kinship
says its own corpus constrains this account but doesn't test it, so the
parallel is a lead, not support.

## Limits

Kinship's methods describe distributions in context. Review board #2's central
demand is whether membership predicts held-out data beyond the cues used to
assign it, and none of this answers that. Items 1–3 improve the framing and
the GloWbE section; items 4 and 5 bear on the CABNC pre-pilot only
indirectly.

## Venue note

*Journal of English Linguistics* suits an English-specific, corpus-based
paper, but kinship (JEngL-26-0039) is in revise-and-resubmit there, so the
same-journal concurrency rule that kept this paper from the Journal of
Linguistics applies.
