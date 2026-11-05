# Evaluation: soundness of the matrix-lesion study plan (FREEZE-v3)
<!-- SUMMARY: Claude evaluation of FREEZE-v3 at Brett's request; architecture sound as record reconstruction, not freezable; six measurement-schema and assignment-rule findings, four not in the prior triages · status: for Brett's decision · updated: 2026-11-04 -->

Evaluator: Claude Opus 5.5 (Claude Code, the session that revised
`inquiry-relative-categories.tex` on 2026-11-03/04). Read-only: nothing
under `analysis/matrix-lesion/` was changed (`FREEZE-v3.md` was open in
an editor). Read: `FREEZE-v3.md`, `properties.csv`, `lesion.py`
(`assign_intj`, `assign_expr`), `FREEZE.md` §6 property descriptions,
`ELIGIBILITY-PROPOSAL-TRIAGE-2026-11-04.md`, the evaluation handoff in
`matrix-lesion-study-plan-evaluation-2026-11-03.zip`, the three triages in
`reviews/matrix-lesion-external-review-2026-11-04/`, and the
matrix-lesion entries in `DECISIONS.md`. Sources checked: CGEL p. 24
(dependents subdivide into complements, modifiers, and determiners),
pp. 1360–1361; Potts 2007 pp. 166–171.

## Verdict

The architecture is sound as a design for **record reconstruction**: the
fixed declared inventory, exhaustive one-cell source-complete lesions,
M0/M1/M2 contrasts with M3 secondary, the assertion-first record,
proposition-level concealment, the outcome firewall, mechanical quote
checks, and the frozen eligibility function. I agree with the deeper v3
triage's claim architecture (record reconstruction, projective warrant,
world-side claims kept apart) and with its "no further architectural
redesign" line.

It isn't freezable. The blocking problems are in the measurement schema
and the assignment rules, which the deeper triage's revised sequence
already places before Round 7 (its steps 2–3). Four of the six findings
below aren't in the prior triages. Two of them come from divergence
between the FREEZE and the paper as revised yesterday and today: the
paper now treats the expressive category as a cluster, and treats
absences as weighing in the convergence.

## Findings not covered by the prior triages

### 1. Inheritance from the label under test presupposes membership (blocking for any projective claim)

Section 4 lets "a class-level assertion ... support several explicitly
included items". A cell inherited that way encodes two things: the
source's generalization about the class and the source's judgment that
the item belongs to it. When the class is the grouping under test, using
that cell as an **assignment source** imports the classification being
tested. Ameka's "interjections do not normally take inflections or
derivations", applied to *ouch* because Ameka lists *ouch* as an
interjection, gives P05 = N, which then counts toward INTJ membership.
If P13 for the same row is inherited from another Ameka statement about
interjections, the recovery follows from Ameka's inclusion of *ouch*,
not from any projection.

Nothing in v2 or v3 restricts assignment sources by inheritance status.
The item-specific restriction in section 4 applies to targets only. The
first triage's item 4 asks for assignment and target assertions to be
separated, but treats inheritance as a target-side sensitivity.
Proposition-level concealment doesn't help either, because the two
propositions are distinct; what they share is the class-inclusion
judgment.

Recommendation: a frozen rule that a cell inherited from a statement
about grouping G (or a label the source treats as equivalent) can't be
an assignment source for G in any analysis supporting a
projective-warrant claim. It may stay in the record-reconstruction
primary, labelled as such, where it shows that the literature organizes
its descriptions by the category. Also add a sensitivity restricting
both sides, sources and target, to item-specific support. The assertion
schema already records "the exact class if inherited", so this needs a
rule, not new data.

### 2. Property definitions overlap by entailment, and concealment has no state for that

The concealment rule's three states (distinct observations, distinct
propositions in a shared passage, same observation) don't catch
entailment between different propositions in different sources.

- **P06 against P04 and P05.** CGEL (p. 24) subdivides dependents into
  complements, modifiers, and determiners, and number is inflection.
  As drafted, P04 ("takes no dependents/complements") and P05 cover
  determiners and number, so P06 Y implies P04 Y or P05 Y, and a class
  statement that a use takes no dependents entails P06 N. For INTJ,
  whose sources include P04 and P05, the P06 projection is partly
  definitional. Recommendation: make the definitions disjoint (P04 =
  complements and modifiers; P05 = inflection other than number; P06 =
  determiners and number), and add an "entailed" state to the
  source–target dependence record. P06 remains a legitimate EXPRESSIVE
  target.
- **P07 against P08 and P11.** The eligibility triage already notes
  that P08 and P09 sit close to P07 through shared passages. The
  specific mechanism is item 6 below for P08. For P11, Potts's
  independence property (p. 166) makes "not interpreted in the host's
  scope" close to a consequence of non-descriptive content, so INTJ →
  P11 partly projects a theory's entailment. Record which P11 cells
  rest on that theoretical link and which on reported scope behaviour.

### 3. EXPRESSIVE is assigned by one anchor; the paper now treats it as a cluster (Brett decision)

INTJ assignment converges over six diagnostics. EXPRESSIVE assignment
is P08 = Y with a P07 veto (`assign_expr`). Since round 6 (DECISIONS
2026-11-03), the paper says both groupings are assigned by convergence
and differ in the property each is anchored in. FREEZE-v3 (15:08)
predates or didn't absorb that.

The two options carry costs:

- **Convergence rule over meaning diagnostics** (P08 as anchor, plus
  P11 negation scope, P10 strengthening, and P07). This matches the
  paper, but it uses up P10 and P11 as EXPRESSIVE targets, and the
  audit found both shallow. In practice the rule may reduce to P08
  plus unresolved rows.
- **Keep the anchor-only rule.** This preserves those targets, but
  M2 is then nearly M1 (two sources), leave-one-source-property-out
  is degenerate, and the INTJ-versus-EXPRESSIVE comparison partly
  compares rule richness, not inquiries.

Either way, after findings 1 and 2, check whether any target in the
shared pool (P06, P09, P13) can pass for both groupings. The comparative
question may have no clean test on this inventory. That should be known
before Round 7, not after production.

### 4. Absences: a presence gate, and an unstated rule for stated non-occurrence

- **Presence gate.** `assign_intj` (and section 2) assigns MEMBER only
  if P01 = Y or P02 = Y is visible. A row with P03 = N, P04 = N,
  P05 = N, and P07 = Y visible (score 4, fraction 1.0) stays
  UNRESOLVED. Four converging diagnostics, three of them absences,
  can't assign membership. Given Brett's ruling today that a lack
  "might not outweigh, but it weighs", the gate should require one
  visible distributional diagnostic of either polarity (P01–P04),
  which keeps the anchoring in distribution without privileging
  presences.
- **Stated non-occurrence.** Section 6 says "Absence without
  opportunity is U" for P03–P05. Read as a rule about a coder's
  inference from packet silence, it's right. But the protocol never
  says that a source's explicit statement of non-occurrence (P05's own
  negative standard is "Source states invariance") is N, carrying the
  class-inheritance flag. Coders could read section 6 as turning
  Ameka-type class statements into U. That would remove most
  interjection absences from the record and make negatives, already
  Round 6's binding constraint, scarcer still. Recommendation: state
  that explicit non-occurrence is N, and record opportunity
  documentation as a strength field (stated, opportunity-documented,
  silence) rather than an admission condition. Any differential
  weighting goes in the frozen rule, not in coding.

### 5. The nonmember side measures control selection

INTJ nonmembers are a small, heterogeneous set chosen as controls: a
count noun, a non-count noun, an imperative verb, an adjective, an
adverb, and two prenominal modifiers. M2 gives all of them one pooled
nonmember distribution. The category under test licenses expectations
about its members. Its complement licenses nothing, so the share of
grouping gain contributed by nonmember rows reflects which controls
were chosen. This is a different point from the deeper triage's tier
strata. Recommendation: report member-row and nonmember-row
contributions to every gain separately, and base any projective
statement on member rows. The same applies to EXPRESSIVE.

### 6. P08 coding needs a guard against CGEL's broad "expressive"

CGEL's general definition gives interjections "expressive rather than
propositional meaning" (p. 1361), in a broad, non-propositional sense
that covers conative *sh* and *hey*. The paper keeps that sense apart
from the narrow stance sense (§2.3). P08's description ("conventionally
conveys an evaluative or affective stance") has no instruction against
coding Y from the word "expressive" alone. Inherited from CGEL's
sentence, P08 would be coded Y on the same proposition as P07 for every
listed interjection, collapsing EXPRESSIVE toward INTJ on inherited
rows. P08 hasn't been piloted. Recommendation: add an explicit
instruction that the word "expressive" by itself doesn't support P08;
the span must state evaluative or affective content. Then check that
guard in the human proposition review.

## Yield check before Round 7 (handoff Q10)

The eligibility triage already puts the INTJ pool at P06, P08, P09, and
P13, with zero to four projections possible. Findings 2 and 6 make P06
and P08 weaker for INTJ. Before Round 7, and before Brett commits to
reviewing every canonical proposition, run the same kind of discarded
evidence-existence audit used for P10–P12 on P06, P08, P09, and P13,
and on EXPRESSIVE's distribution targets. The firewall allows it. If
the gate would admit at most one target per grouping, the
cross-inquiry question can't be answered in this form, and the coding
and review cost should be weighed against that before production.

## Paper-side note (shared defect)

`inquiry-relative-categories.tex` §2.1 (round 7) says membership
licenses expecting that a member won't take determiners, number
marking, or quantification, or fill an argument position. Given CGEL
p. 24, that partly restates the diagnostics it follows (no dependents,
no inflection, no integrated position), the same entailment as finding
2. It can be fixed by framing it as projection from observed
environments to unobserved ones. Not changed; offered.

## Where these fit

Findings 1, 2, 4, and 6 belong in the measurement schema (deeper
triage, step 2). Finding 3 belongs in the assignment rules and
comparator specification (step 3). Finding 5 belongs in the outcome
reporting rules (step 3). The yield audit fits alongside its step 4
(load estimate).

## Addendum (2026-11-04, after Brett's reply)

Brett: "a simple tally is not the way to go. That's not how HPC works.
absences count, surely. No property on its own can 'decide
membership'." A side agent had pointed out that findings 1 and 4, taken
together, would bar most recorded absences from assignment. Most
absences come from class statements, while presences are often shown
item by item in examples. The findings are revised as follows.

- **Finding 4, replaced.** Patching the tally was the wrong fix. The
  assignment rule should be a convergence model, not a ±1 count with
  thresholds. Membership is graded, each diagnostic's contribution comes
  from how the diagnostics co-occur, both polarities count, and there is
  no gate and no decisive property. A latent-class model on the
  rotation's diagnostics is the obvious candidate. Its stability at
  roughly 34 rows, and the treatment of a heterogeneous complement (more
  than one class, or left unstructured), need checking in Round 7.
  Opportunity documentation sets an absence's weight, not whether it's
  admitted.
- **Finding 1, narrowed.** Inherited cells are admitted, not barred. All
  the cells a source attributes to an item through its statements about
  a class count as one unit of testimony; item-specific observations
  count separately. This applies to presences and absences alike. The
  circularity guard becomes a concealment rule: for the target row,
  conceal any source cell inherited through the same inclusion judgment
  as the target cell. Excluding all inherited cells becomes a strict
  sensitivity analysis, not the primary rule.
- **Finding 3** follows from the same principle: EXPRESSIVE also needs a
  convergence model, not P08 alone.
- **What remains is empirical.** If the literature mostly states
  absences at class level, the projective analysis will lean on
  testimony, and the strict sensitivity will show how much. No existing
  material counts item-specific against inherited absence records (the
  pilots covered P02, the audit P10 to P12). That count belongs in the
  yield audit.
