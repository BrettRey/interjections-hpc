# DRAFT FREEZE: Property-matrix lesion study for Inquiry-Relative Categories

**Status: SUPERSEDED DEVELOPMENT DRAFT.** Retained as the record of design
development. The current consolidated proposal is `FREEZE-v2.md`, which
remains unapproved. Prepared originally 2026-11-03 by Muse
Code (muse-wonder-full-1.0) at Brett's request. Nothing in this document
binds anyone until Brett approves it in writing (a DECISIONS.md entry counts)
and the approved version is committed to git. The commit hash of the approved
version is the freeze point. Amendments after the freeze require a dated
amendment section in this file, with the reason, and never apply retroactively
to cells already coded or results already seen.

Values marked **[BRETT TO SET]** are placeholders. They must be fixed before
coding begins, not after the pilot's substantive results (as opposed to its
feasibility statistics) are known.

## 1. Projective declaration

- **Bearer:** conventionalized sign-types (a form in a specified conventional
  use), as listed in `items.csv`. Not spellings, not tokens.
- **Source:** for a given sign-type, any observed subset of its coded
  properties (P01-P14), under the lesion regimes in section 7.
- **Target:** the values of its remaining, masked properties. Primary targets
  for the category-standing claim are the TARGET-ONLY properties (P10, P11,
  P12, P13), which never enter the primary assignment rules. A projection
  that only recovers its own assignment diagnostics does not count.
- **Population and scope:** the 33 Tier-1 sign-types in `items.csv` (English,
  as described in the held grammatical and interactional literature).
  Tier-2 items (LAH, HABA) enter only under the fill rule in section 5.
- **Claim under test:** assignment to the lexical category INTERJECTION (and,
  separately, to the expressive grouping EXPRESSIVE), made from visible
  properties under the frozen rules in section 6, licenses expectations
  about unobserved properties of the same sign-type that beat (a) the
  base-rate predictor and, for the strong tier, (b) add information beyond
  direct prediction from the visible properties themselves, at the frozen
  tolerances in section 8.
- **Timescale/version:** the characterization of these uses in the held
  literature as of the freeze date. No diachronic claim.

## 2. Inquiry and use

The study serves one passage of `inquiry-relative-categories.tex`: the claim
(sec. 2.1, sec. 3.2) that membership in the lexical category "licenses
expecting the rest" of a member's profile. At present that claim reports the
co-occurrence of properties in published descriptions. The minimum reach
that would serve the paper is Tier 2 (moderate) in section 8: category-
mediated prediction beats base rates on target-only properties. Anything
less leaves the paper's claim at the level of its current descriptive
achievement, and the text must say so.

## 3. Items

`items.csv` lists 35 sign-types: 10 core, 17 boundary, 6 controls, 2 Tier-2
extension items. Controls are full rows, coded identically.

**Item list (35 sign-types; mirror of `items.csv`).**

| ID | Form | Use | Family | Tier | Rotations |
|---|---|---|---|---|---|
| AH | ah | receipt/reaction use, as in: Ah, so you were there | ah | core | INTJ;EXPR;SUPPL;DEPICT |
| HEY | hey | attention-getting use | hey | core | INTJ;EXPR;SUPPL;DEPICT |
| OH | oh | change-of-state / receipt use | oh | core | INTJ;EXPR;SUPPL;DEPICT |
| OOPS | oops | mishap reaction | oops | core | INTJ;EXPR;SUPPL;DEPICT |
| OUCH | ouch | pain reaction | ouch | core | INTJ;EXPR;SUPPL;DEPICT |
| SH | sh | silencing use | sh | core | INTJ;EXPR;SUPPL;DEPICT |
| UGH | ugh | disgust/dismay reaction | ugh | core | INTJ;EXPR;SUPPL;DEPICT |
| WOW | wow | amazement reaction | wow | core | INTJ;EXPR;SUPPL;DEPICT |
| ALAS | alas | dated lament | alas | core | INTJ;EXPR;SUPPL;DEPICT |
| AHA | aha | recognition / discovery display | aha | core | INTJ;EXPR;SUPPL;DEPICT |
| GEE | gee | surprise/emphasis reaction | gee | boundary | INTJ;EXPR;SUPPL;DEPICT |
| TUTTUT | tut-tut | disapproval click (spelling pronunciation excluded) | tuttut | boundary | INTJ;EXPR;SUPPL;DEPICT |
| DAMN_REACT | damn | standalone and supplementary stance use: Damn! / Damn, we're late | damn | boundary | INTJ;EXPR;SUPPL;DEPICT |
| DAMN_NP | damn | complement-taking use: Damn these mosquitoes! | damn | boundary | INTJ;EXPR;SUPPL;DEPICT |
| DAMN_PRENOM | damn | prenominal modifier: the damn car | damn | boundary | INTJ;EXPR;SUPPL;DEPICT |
| BANG_DEPICT | bang | sound depiction in narrative: Bang! | bang | boundary | INTJ;EXPR;SUPPL;DEPICT |
| BANG_NOUN | bang | count-noun use: a loud bang, two bangs | bang | control | INTJ;EXPR;SUPPL;DEPICT |
| MMHM | mm-hm | continuer use in storytelling | mmhm | boundary | INTJ;EXPR;SUPPL;DEPICT |
| HUH | huh | open repair initiator: Huh? | huh | boundary | INTJ;EXPR;SUPPL;DEPICT |
| BYE | bye | closing use | bye | boundary | INTJ;EXPR;SUPPL;DEPICT |
| OKAY | okay | acceptance/response use | okay | boundary | INTJ;EXPR;SUPPL;DEPICT |
| YES | yes | affirmative answer to polar question | yes | boundary | INTJ;EXPR;SUPPL;DEPICT |
| NO | no | negative answer to polar question | no | boundary | INTJ;EXPR;SUPPL;DEPICT |
| THANKS | thanks | thanking use | thanks | boundary | INTJ;EXPR;SUPPL;DEPICT |
| SORRY | sorry | apology use | sorry | boundary | INTJ;EXPR;SUPPL;DEPICT |
| HELLO | hello | greeting use | hello | boundary | INTJ;EXPR;SUPPL;DEPICT |
| BLOODY_PRENOM | bloody | prenominal modifier: the bloody car | bloody | boundary | INTJ;EXPR;SUPPL;DEPICT |
| HEAVENS | heavens | exclamatory use: Heavens! | heavens | boundary | INTJ;EXPR;SUPPL;DEPICT |
| COFFEE | coffee | count/mass noun, incl. answer use: Coffee. (reply to What would you like?) | coffee | control | INTJ;EXPR;SUPPL;DEPICT |
| STOP | stop | imperative verb use: Stop! / Stop the car! | stop | control | INTJ;EXPR;SUPPL;DEPICT |
| BLACK | black | adjective, incl. answer use: Black. (reply about colour) | black | control | INTJ;EXPR;SUPPL;DEPICT |
| QUICKLY | quickly | ordinary manner adverb | quickly | control | INTJ;EXPR;SUPPL;DEPICT |
| HOWAREYOU | how are you | formulaic greeting sequence | howareyou | control | EXPR;SUPPL;DEPICT |
| LAH | lah | Singapore/Malaysian English particle use | lah | extension | INTJ;EXPR;SUPPL;DEPICT |
| HABA | haba | Nigerian English surprise/exclamation use | haba | extension | INTJ;EXPR;SUPPL;DEPICT |

**Property list (14; mirror of `properties.csv`).**

| ID | Name | Group | Values | INTJ-eligible | EXPR-eligible |
|---|---|---|---|---|---|
| P01 | STANDALONE | distribution | Y/N/U | yes | no |
| P02 | SUPPLEMENT | distribution | Y/N/U | yes | no |
| P03 | INTEGRATED | distribution | Y/N/U | yes | no |
| P04 | DEPENDENTS | distribution | Y/N/U | yes | no |
| P05 | INFLECTS | morphology | Y/N/U | yes | no |
| P06 | NOMINAL_COMB | morphosyntax | Y/N/U | no | no |
| P07 | NONPROP | meaning | Y/N/U | yes | yes |
| P08 | STANCE | meaning | Y/N/U | no | yes |
| P09 | DEPICTIVE | meaning | Y/N/U | no | no |
| P10 | REPETITION | meaning | STRENGTHENS/MULTIPLIES/REDUNDANT/U | no | no |
| P11 | SCOPE | meaning | Y/N/U | no | no |
| P12 | PROSODY | realization | Y/N/U | no | no |
| P13 | PHONO_ANOM | realization | Y/N/U | no | no |
| P14 | SEQACTION | interaction | REACTION/CONTINUER/REPAIR/CLOSING/RESPONSE/GREETING/NONE/U | no | no |
 The analyst_tier
column is bookkeeping for the analysts and is NEVER shown to coders. Form
families (the three `damn` rows, the two `bang` rows) are blocking units for
every holdout and bootstrap in section 7, so shared form cannot leak across
the visible/masked divide.


> If this table and `items.csv` ever disagree, the CSV governs and the disagreement is a deviation to log (section 11).

Item-list decisions for Brett (drafted, not settled):

- DAMN_REACT merges standalone and supplementary stance `damn` into one
  sign-type, following the draft's treatment of the two as environments of
  one use. Split them if that misstates the theory.
- OH, YES, NO, OKAY are single-use slices of multifunctional forms. The
  use_gloss fixes the slice; coders code the slice, not the spelling.
- Items are anchored to external descriptions, with one flagged exception:
  COFFEE is the paper draft's own constructed example (sec. 2.1, reply
  "Coffee" to "What would you like?"), not drawn from a source. BLACK in
  the same paragraph is Wilkins's example (1992: 124-125). OPEN ISSUE
  (Brett, 2026-11-03): draft-internal control examples are exactly the
  rows a form-based packet search of the interjection literature will
  struggle to fill, so the control set may need replacing with contrast
  items the held literature itself discusses.

## 4. Properties

`properties.csv` gives the 14 columns, values, assignment eligibility, and
the standard a negative cell must meet. The property descriptions below
guide extraction of source-supported observations; they are not
definitions of the categories under investigation, and a source is never
required to use the heading's label. Coders preserve the source's own
wording in the coding record. Coder-facing text is derived from these
descriptions and from nothing else:

- **P01 STANDALONE.** In this use, the sign can constitute a complete
  utterance without a recoverable elided clause or head. Answer-economy
  fragments ("Coffee." in reply to an offer) code N: their interpretation
  depends on recovered structure.
- **P02 SUPPLEMENT.** Sources describe or exemplify the sign in this use
  occurring with a complete clausal or nominal unit while retaining a
  separate, utterance-like status and not entering integrated construction
  with that unit. Relevant source wording may include *supplement*,
  *co-utterance*, occurrence with another utterance, and contrasts between
  entering and not entering construction with other expressions. No one
  framework's wording is a gate. Brett's reading of Ameka (1992: 105) is
  the calibration example: its *co-utterances* occur in an explicitly
  distributional discussion contrasting utterance status with entering
  into construction, which is close to the syntactic territory CGEL treats
  under supplement function.
- **P03 INTEGRATED.** In this use, the sign occurs as an integrated
  constituent inside clause or NP structure (modifier, head, argument).
- **P04 DEPENDENTS.** In this use, the sign takes complements or other
  dependents of its own.
- **P05 INFLECTS.** In this use, the sign shows productive inflection
  (number, tense, person, degree). A historically plural or otherwise
  frozen shape (HEAVENS) codes N unless a live contrast is attested.
- **P06 NOMINAL_COMB.** The form combines with determiners and number as a
  nominal head ("a big X", "two Xs") for this use without a conversion
  analysis being required by the source. Expected to be Y mainly for
  nominal controls and BANG_NOUN.
- **P07 NONPROP.** The use's conventional contribution is not descriptive,
  truth-conditional content (it reacts, conveys, depicts, directs, or
  manages interaction rather than describing).
- **P08 STANCE.** The use conventionally conveys an evaluative or affective
  stance (the draft's narrow "expressive" anchor). Pure depiction and pure
  sequence management code N, per the negative standard.
- **P09 DEPICTIVE.** The use conventionally depicts a sound, event, or
  sensory scene through resemblance between performance and depicted scene.
- **P10 REPETITION.** Effect of immediate repetition of the form in this
  use: STRENGTHENS the same contribution, MULTIPLIES depicted events, or is
  REDUNDANT/unavailable. TARGET-ONLY.
- **P11 SCOPE.** Where the use occurs with a host proposition, its
  contribution survives negation or interrogation of that host (is not
  interpreted in their scope). TARGET-ONLY. Items with no host
  environment at all code U, not Y.
- **P12 PROSODY.** Occurrences characteristically form their own
  intonational unit, including alongside a host utterance. TARGET-ONLY
  under the primary assignment rule; admitted in one sensitivity rule.
- **P13 PHONO_ANOM.** The conventional form permits sounds or combinations
  outside the ordinary word phonology of standard BrE/AmE (clicks,
  vowelless syllables, /x/, etc.). TARGET-ONLY.
- **P14 SEQACTION.** The use's conventional sequential action, if any, in
  conversation. For lesion scoring, a binary HAS_SEQACTION is derived
  (any value but NONE/U) and kept separate from the categorical column.

## 5. Evidence and coding protocol

**Evidence tiers.** Tier A (admitted in the primary matrix): a quotation
from a held source in `literature/`, with page, that states or directly
exemplifies the property value for the item or for a class the source
explicitly includes the item in. Tier B (corpus attestation) is NOT
admitted in v1; adding it requires a freeze amendment specifying corpora
and query protocols. Tier C (model judgment/introspection) is excluded
from the primary matrix outright. It may be collected in parallel as an
exploratory annex and must never be merged into primary cells.

**Negative cells.** Silence in the literature is U, never N. An N requires
the per-property standard in `properties.csv` (an explicit restriction, a
paradigm, a characterization with no room for the property). This will
leave many cells unknown. That is the price of a matrix which is evidence
rather than recollection.

**Blinding.** Coding is siloed by property. Each coder receives: one
property's operational definition and negative standard; the item list for
that column in shuffled order, controls interleaved, identified by form
and use_gloss only; and a source packet per item (passages extracted from
`literature/*.md` by scripted search on the item's form, unedited).
Coders do not receive: the paper draft, the item tiers, any other column,
the assignment rules, or any statement of the hypothesis. All codings are
fresh, stateless runs. Coders must not consult sources outside the packet;
a value the packet does not support is U.

**Panel.** Three independent families code every column: Agy (print mode,
JSON schema enforced), Copilot (`-p`, validated output), Qwen3.8-27b via
Ollama (temperature 0, JSON mode). A fourth coder, Muse fresh-context
subagents, codes every column as well and is reported separately as
non-independent of the orchestrator (same model family; the orchestrator
has read the paper and does not code). Claude and Codex routes are
unavailable at drafting time and are not silently substituted later; adding
a family post-freeze requires an amendment.

**Output per cell (JSON):** item_id, property_id, value, quote (verbatim,
or null if U), source_file, page_or_location, coder_family, model_id,
run_timestamp. Values without a verbatim-checkable quote are
automatically U.

**Verification.** The orchestrator verifies every pilot quote, a random
20% of full-run quotes, and every quote attached to a disagreement,
against the held source file. A fabricated or materially misattributed
quote voids that coder's cell (set to U) and is logged; the pilot stop
rules in section 10 govern family-level suspension.

**Consensus and adjudication.** A cell's primary value is the majority of
the three independent families among non-U values, requiring at least two
non-U codings; otherwise U. Cells with a 1-1-1 or 1-1 split, and any cell
where verification voids a vote and breaks the majority, go to Brett with
the packets, as a packet-only judgment (he sees the same evidence the
coders saw, plus their quotes). Agreement statistics are reported as
inter-model agreement (Fleiss kappa over the three independent families),
never as intercoder reliability.

**Go/no-go gate (before any lesioning).** The primary analysis requires:
at least 25 Tier-1 items with 8 or more known (non-U) cells, and every
property with at least 20 known Tier-1 cells. Tier-2 items join a row only
if they reach 8 known cells. If the gate fails, the study is reported as
frozen but untestable on literature evidence alone, the fill pattern
itself is reported (it is a finding about the descriptive record), and no
lesion results are presented. No reduction of the property set to pass
the gate after coding.

**Outcome firewall.** Before the approved freeze is registered, design work
may inspect fake-data outcomes and explicitly discarded pilot artifacts, but
not lesion outcomes or cross-property patterns from the full study matrix.
During full coding, no one computes or inspects category assignments across
complete rows, cross-column associations, lesion scores, predictor
comparisons, or tier outcomes. Permitted pre-unblinding checks are confined
to the siloed coding task itself: schema validity, verbatim-quote
verification, packet-only adjudication of individual disagreements, and the
pre-specified known-cell counts needed for the go/no-go gate. The consensus
matrix is assembled by the committed script, hashed, and left unexamined
until the frozen primary lesion configuration is run. Any accidental
inspection beyond this firewall is recorded in `DEVIATIONS.md`, and any
analysis begun after the primary reveal is labelled exploratory.

## 6. Assignment rules (frozen before coding)

Assignment is computed from visible (unmasked, known) cells only, inside
every lesion run. A property that is masked for a run plays no part in
assigning the items in that run. This enforces the paper's source-target
rule mechanically.

**INTJ (primary rule R-INTJ-1).** Eligible visible properties: P01, P02,
P03, P04, P05, P07. Score: +1 for P01=Y, P02=Y, P03=N, P04=N, P05=N,
P07=Y; -1 for each opposite known value; 0 for U or masked. Outcomes:
MEMBER if (P01=Y or P02=Y among visible cells) and score >= 3;
NONMEMBER if score <= 0; otherwise UNRESOLVED. **[BRETT TO SET: the
threshold 3 and the P01/P02 gate.]**

Sensitivity rules, reported alongside but never substituted for the
primary: R-INTJ-2 (form-only, Wilkins-style: as R-INTJ-1 but P07
ineligible); R-INTJ-3 (as R-INTJ-1 but P12 eligible, +1 for P12=Y).

**EXPRESSIVE (primary rule R-EXPR-1).** MEMBER if P08=Y and P07=Y (both
visible); NONMEMBER if P08=N; otherwise UNRESOLVED. Sensitivity:
R-EXPR-2 (P08=Y alone suffices).

Predictions from an assignment use only rows whose target-cell value is
known and visible in that run (the run's reference set). Items assigned
UNRESOLVED receive the base-rate prediction under the category predictor,
and the unresolved rate is reported per regime.

## 7. Lesion regimes, predictors, metrics

Only known (non-U) cells are ever masked or scored. All masks are drawn
with a fixed seed recorded in the run configuration; the lesion code is
written and unit-tested on a synthetic matrix before the real matrix is
unblinded, and the tested version is the version run.

- **L1 leave-one-cell-out.** Every known cell masked once.
- **L2 random cell masks.** 20/40/60/80% of known cells masked, 500 draws
  per level.
- **L3 leave-one-column-out.** Each property in turn entirely masked as
  target; assignment and prediction use the other 13 only.
- **L4 sparse rows.** Each item reduced to k randomly chosen visible known
  cells, k = 2, 4, 6; 500 draws per k. All other rows fully visible.
- **L5 leave-one-form-family-out.** All rows of a form family masked as
  targets (with k of their cells left visible for assignment, k as in L4);
  reference set excludes the family entirely.

Predictors, applied identically within every run:

- **M0 base rate.** Target column's distribution over the reference set.
- **M1 properties-only.** Per-target L2-regularized logistic regression
  (binary targets) or multinomial equivalent (P10, P14-binary treated as
  binary) on visible property values, trained on the reference set;
  falls back to M0 when the reference set has fewer than 10 usable rows.
- **M2 category-mediated.** Assignment under the frozen rule from visible
  cells; prediction is the target distribution among reference rows with
  the same assignment outcome (MEMBER rows predict MEMBER targets'
  distribution, and so on; UNRESOLVED falls back to M0).
- **M3 category + properties.** M1 with the assignment outcome added as a
  feature.

Primary metric: mean log loss on masked known cells. Secondary: Brier
score, balanced accuracy. Reported overall, per property, per regime and
sparsity level, per predictor, and (primary) restricted to TARGET-ONLY
properties P10-P13. Uncertainty: 1,000 bootstrap resamples at the
form-family level. P10 and P14 are scored as categorical log loss under
M0/M2 and excluded from M1/M3 if any class has fewer than 5 reference
rows in a run (the exclusion is per-run, automatic, and counted).

## 8. Revision rule (demotion triggers)

Fixed before coding. Evaluated on L2 at the 60% mask level, TARGET-ONLY
properties, family-level bootstrap. **[BRETT TO SET: all four numeric
thresholds below.]**

- **Tier 1 (strong).** M2 log loss <= M0 log loss - 0.05, with the 95%
  bootstrap interval for the difference excluding 0, AND M3 log loss
  <= M1 log loss - 0.01. Reading: the category step both beats base rates
  on properties it was not assigned from, and adds information beyond the
  visible properties.
- **Tier 2 (moderate).** The M2-vs-M0 condition holds, and M3 is within
  0.02 log loss of M1 (no material loss). Reading: the category is an
  adequate compression of the profile; it licenses expectations under
  sparsity but adds nothing to a full record (the paper's sec. 3.4
  position).
- **Tier 3 (failure).** The M2-vs-M0 condition fails. Consequence, fixed
  in advance: the category-standing claim for that grouping demotes to a
  descriptive claim; the paper is revised to say so, and the lesion result
  is reported in the paper or its supplement either way. No post-hoc
  narrowing of items, properties, or sparsity level to escape Tier 3. A
  narrower claim (e.g. a subtype) may be stated as a new, untested
  proposal, clearly marked as such.

INTJ and EXPRESSIVE are tiered separately. Failure of one does not touch
the other's standing. Success at any tier establishes a stable, mutually
predictive profile under this coding of this inventory. It establishes
nothing about causal order, causal mechanisms, maintenance, or control,
and no wording in the paper may upgrade it to any of those on this
evidence.

## 9. Known threats, stated in advance

- **Pretraining contamination.** All four coder families were trained on
  text that includes the grammatical literature. Blinding protects against
  sight of other cells and of the hypothesis; it does not make coders
  ignorant of e.g. CGEL's interjection list. The Tier-A quote requirement
  is the mitigation: a cell stands on a checkable quotation, not on a
  model's recollection. Residual risk is disclosed in the paper.
- **Packet construction.** Scripted excerpt extraction can miss relevant
  passages that use synonyms or class-level statements. Misses inflate U,
  which biases toward the go/no-go gate, not toward confirmation.
- **Class-level statements.** A source's claim about "interjections"
  applied to an item the source counts as one is one observation about
  that source's class, reused across rows. Rows are therefore not fully
  independent; family-level bootstrap is a partial, not complete, answer.
  A sensitivity analysis restricts Tier A to item-specific statements
  only. **[BRETT TO SET: whether the sensitivity is run as co-primary.]**
- **Inventory scope.** Results concern this inventory as described in this
  literature. Projection to unlisted items is L5's business, and even
  there the reference set is the same descriptive tradition.

## 10. Pilot and stop rules

Before the full run: property P02, 10 items (OUCH, WOW, GEE, DAMN_PRENOM,
BANG_DEPICT, MMHM, BLOODY_PRENOM, COFFEE, STOP, BLACK), three independent
families plus the Muse coder. Each CLI route is first smoke-tested with
a trivial prompt (binary presence does not prove quota or auth).

Pilot measures feasibility only: quote accuracy (orchestrator checks
100%), Fleiss kappa among the three independent families, unknown rate,
wall-clock and cost per column. Stop/revise rules:

- Any fabricated or materially misattributed quote suspends that family
  pending review; two in the pilot remove it from the panel (replacement
  requires an amendment).
- Fleiss kappa < 0.40: revise the operational definitions, re-pilot once.
  A second failure goes back to Brett as a design problem, not a third
  pilot.
- Unknown rate > 60% on the pilot column: revise packet construction
  before proceeding; if a second pilot column (P05) also exceeds 60%, the
  go/no-go gate is expected to fail and Brett decides whether to proceed.

Pilot cell values are not reused in the full matrix; the pilot column is
re-coded in the full run by fresh runs.

## 11. Files, versioning, reporting

- `analysis/matrix-lesion/items.csv`, `properties.csv` (this draft).
- `analysis/matrix-lesion/packets/` (generated; scripted, versioned).
- `analysis/matrix-lesion/codings/` (raw JSON per family per column,
  append-only).
- `analysis/matrix-lesion/matrix.csv` (consensus matrix, generated by a
  committed script from `codings/` plus the adjudication log).
- `analysis/matrix-lesion/adjudication-log.md` (every adjudicated cell,
  with the deciding quote).
- `analysis/matrix-lesion/lesion.py` plus tests, `results/` (run configs
  with seeds, per-regime tables).
- AI disclosure in the paper must be extended to name every model family
  that codes cells, before submission.
- Deviations from this document, however small, are logged in a
  `DEVIATIONS.md` in the same directory, dated, with reasons. An empty
  deviations file is created at freeze time so its later absence of
  entries is itself checkable.

## 12. Fake-data design check (2026-11-03, pre-freeze; supersedes where noted)

At Brett's suggestion, the full pipeline was run on simulated matrices
from known data-generating processes before any real coding. Full
record: `SIMULATION.md` in this directory; code in `lesion.py`,
`simulate.py`, `run_l4.py`, `diagnose.py` (leakage test passes:
flipping every masked value changes no assignment and no prediction).
Findings that revise this draft, all still subject to Brett's approval:

1. **Assignment rules replaced by v2** (sparsity-aware; the v1 absolute
   score threshold in section 6 is unreachable under realistic
   sparsity). Section 6 is superseded by the implementations in
   `lesion.py`, whose docstrings state v2 exactly.
2. **Primary tier regime is L4 sparse-row** (k=4 and k=6), not L2 at
   60% masking (section 8 superseded on this point). L2 becomes a
   secondary stress test.
3. **P13 leaves the primary pooled target set** (near-zero oracle gain
   in simulation; possibility-strength property). Reported per
   property. Primary pooled targets P10-P12, with per-grouping primary
   targets (INTJ: P12; EXPRESSIVE: P10, P11) proposed, since the
   pooled test fails the crosscutting world the paper itself describes.
4. **Threshold proposal from the simulated null** (section 8 numbers
   superseded): Tier-2 gate at d20 >= 0.03 gives a false-tier rate of
   ~1% under the null and ~55% power in a strongly clustered world at
   n=33, k=4. The draft placeholder 0.05 would hold power to ~37%.
5. Every tier verdict is reported with its unresolved rate and the
   resolved-conditional gain.
6. Coding completeness dominates item count for power (n=33 at k=6
   beats n=60 at k=4). The go/no-go fill gate stays; at fill 0.45 the
   design has no power worth having.

Fake data validates the machinery and calibrates the thresholds. It
cannot validate packets, coders, or fill. The pilot still gates the
real run.

## 13. Rotations (2026-11-03, pre-freeze draft addition)

At Brett's suggestion, the single-grouping design generalizes to
rotations. A rotation is a frozen triple (assignment rule, source
properties, target properties) with its own declaration, null
calibration, and tier verdict. Rotations are tiered independently:
one rotation's failure demotes only its own claim. The full rotation
list is frozen before coding, and every frozen rotation is reported,
so there is no rotation-shopping. Draft rotation set (sources and
targets exclude each other by construction):

| Rotation | Bearer | Sources | Primary targets |
|---|---|---|---|
| INTJ (lexical category) | sign-type | P01-P05, P07 | P12; secondary P08, P06 |
| EXPRESSIVE | sign-type (conventional use) | P08, P07 | P10, P11 |
| SUPPLEMENT-capable | sign-type; see bearer amendment below | P02 (+P15, P16 if added) | P12 |
| DEPICTIVE | sign-type (conventional use) | P09 | P10 (categorical), P13 |

**Bearer universes differ per rotation, with overlap.** Each rotation
first fixes its candidate bearers; membership is then a subset of
that universe. A row can bear on several rotations or only one, and
the master item list flags this per row (`rotation_universes` in
`items.csv`, mirrored in the section 3 table). Draft universes: INTJ
bears on lexical sign-types only (HOWAREYOU, a clause, is not a
candidate for lexical category); EXPRESSIVE and DEPICTIVE bear on all
conventional uses in the list; SUPPLEMENT bears on all rows under the
capability reading, plus phrasal expression rows if approved below,
which would bear on no other rotation. Per row and rotation there are
then three states before any cell is coded: in-universe (member or
nonmember, cells possibly unknown), and not-a-bearer (the row is
excluded from that rotation's scoring and reference set entirely; it
is neither a nonmember nor a missing value). The overlap pattern
across universes and memberships (canonical items everywhere, stance
items outside the lexical category, supplement-only phrasal rows) is
reported as a result, since partial alignment of the bearer sets is
the paper's central descriptive claim.

Proposed additions requiring Brett's approval at freeze:

- **P15 CLEFT_RESIST, P16 NEGSCOPE_EXEMPT** (source columns for the
  SUPPLEMENT rotation, from the draft's sec. 2.2 tests, CGEL p. 1360):
  the expression in supplement use cannot be the focus of an it-cleft,
  and falls outside the scope of negation in its anchor. These give
  supplement assignment converging syntactic sources and keep P12
  (prosody) a clean target.
- **Expression-use rows for the SUPPLEMENT rotation** (appositive NP
  use, non-restrictive relative use, supplementary adverbial use,
  vocative NP use), scored only within that rotation. Without them
  the rotation tests supplement capability among lexical sign-types,
  not supplement function across expression categories, which is the
  draft's sec. 2.2 claim.
- Later rotations (SEQUENTIAL ACTION classes; PHONOLOGICAL STRATUM)
  need target columns this matrix does not have (sequential outcomes;
  alternation/acquisition behaviour). Named here so their absence from
  v1 is a decision, not an oversight.

Lesion regimes per rotation: source-complete is primary (sources are
the observed side of the claim; targets masked; reference rows
intact). Sparse-row random-k and random cell-masking are secondary
stress tests. Thresholds are calibrated per rotation against that
rotation's simulated null (single-target rotations are noisier under
the null; the shared 0.03 gate from section 12 does not transfer
unexamined). Fake-data record for rotations: SIMULATION.md, Round 4.
Headline results there: discrimination is clean (foreign-target gains
at null levels); power tracks source convergence (INTJ strongest at
n=33); DEPICTIVE awaits the categorical P10 implementation.

## Approval checklist for Brett

1. Item list: add, drop, or re-slice any rows. Confirm the DAMN_REACT
   merge and the control set.
2. Property list: add or drop columns; confirm TARGET-ONLY set (P10-P13).
3. Set the four numeric thresholds in sections 6 and 8.
4. Decide the class-level-statement sensitivity (section 9).
5. Confirm the panel (Agy, Copilot, Qwen local; Muse non-independent)
   and the exclusion of Tier-C judgment cells from the primary matrix.
6. Approve, then the freeze is committed and the pilot can be built.

