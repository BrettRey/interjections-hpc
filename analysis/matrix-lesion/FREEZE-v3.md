# DRAFT PROTOCOL v3: Fixed-inventory lesion study of inquiry-relative classifications

**Status: DRAFT, NOT APPROVED, NOT FROZEN, NOT REGISTERED.** Prepared
2026-11-04 after the corrected target-evidence audit and Brett's
approval of the amended target-eligibility architecture
(`ELIGIBILITY-PROPOSAL-TRIAGE-2026-11-04.md`). This draft supersedes
`FREEZE-v2.md` as the current proposal where they conflict. v2 remains
the development record for the fixed-inventory estimand, predictors,
firewall, and assignment rules, which v3 incorporates except as
changed below. The central v3 change: no property is privileged as a
primary target by theoretical interest. A frozen eligibility function
(section 8) admits every non-assignment target with adequate
evidence, and the primary result is the family of per-projection
reconstruction gains over admitted targets. The word "confirmatory"
is retired in this project; the commitment is a prespecified primary
reconstruction analysis. Numeric gate thresholds marked for approval
do not bind until Brett approves them in writing, the approved
version is committed, and the same version is registered before
production coding begins.

## 1. Question and estimand

The study asks a fixed-inventory question:

> Given specified incomplete information about expressions in a declared
> inventory, how accurately do different groupings recover concealed
> properties, and how does that recoverability depend on the inquiry?

No expression has to be new to the investigator or to linguistics. A lesion
withholds a property value, and every quantity estimated from it, from the
prediction procedure in a particular run. Results are about this declared
inventory under stated information losses. They are not, by themselves,
estimates for all English signs, future coinages, or unseen languages.

The inventory is deliberately constructed, not a natural population and
not an exhaustive inventory of English. Scope statements must say
“33 Tier-1 declared sign-types” (plus any separately gated extension rows),
not “English” without qualification.

The study evaluates named projections. A projection states:

- the bearers and bearer universe;
- the grouping and assignment rule;
- the permitted source observations;
- the concealed target property and environment;
- the reference set;
- the outcome measure and unresolved-assignment policy.

No result is a verdict on a category's overall standing. Each projection
can succeed, fail, or lack enough evidence independently.

## 2. Principal lesion and comparisons

The principal experiment is **source-complete, membership inferred**:

1. Select one eligible target cell.
2. For the target row, retain every known cell in the rotation's permitted
   source set. Conceal the target and all non-source cells for that row.
3. Keep reference rows intact as coded, except that no reference row may
   contribute the target row's concealed value. Reference outcomes in the
   target column are the training observations.
4. Infer the target row's assignment only from its retained sources.
   Infer reference assignments only from their permitted sources.
5. Estimate every target-dependent quantity (base rates, category rates,
   direct-model coefficients, imputations) without the concealed target.
6. Predict the concealed value and score it once revealed.
7. Cycle through every eligible known target cell.

Larger losses (random subsets of target cells, sparse-row source losses,
and form-family blocks) are scenario variations. A whole target column is
never removed in a run whose predictors learn target associations from the
matrix.

### Predictors and what each comparison means

- **M0, base rate:** target distribution in the eligible reference set.
- **M2, category/compression predictor:** target distribution among
  reference rows assigned to the same grouping outcome; unresolved rows
  receive M0 in the primary all-rows score and are also reported
  separately.
- **M1, direct-property predictor:** regularized logistic/multinomial
  model using *the same permitted source columns*, and only those
  columns, for training and target rows. Missingness indicators and the
  imputation rule are part of the permitted information state and are
  fixed before fitting.
- **M3, properties plus category:** optional secondary estimator. Any
  M3–M1 difference is about this estimator's parameterization, pooling,
  or regularization. It is not evidence that a deterministic category
  added information beyond its inputs.

Central reported contrasts:

| Contrast | Interpretation |
|---|---|
| loss(M0) − loss(M2) | grouping gain: grouping supports informative expectations |
| loss(M0) − loss(M1) | direct-source gain: recoverable structure in permitted sources |
| loss(M2) − loss(M1) | compression cost: performance lost (if positive) or gained (if negative) by using the grouping instead of the direct sources |

Substantive comparators are declared per projection where relevant:
a leading single source property, an unthresholded convergence score,
and a broader or narrower alternative grouping. “Compression” claims must
also report the grouping's specification cost: number of source
properties, thresholds or special cases, and unresolved rate.

### Cross-inquiry comparison

Local projections alone do not answer the comparative question in
section 1. A limited cross-inquiry comparison is therefore part of the
principal design wherever bearers and evidence overlap.

The comparison is INTJ versus EXPRESSIVE on every target admitted
for both groupings under section 8 (shared eligible targets; on the
current inventory the candidate shared pool is P06, P09, P10, P11,
P12, P13, of which the corrected audit already shows P10 to P12
shallow in their audited forms). If no shared target is admitted,
inquiry dependence is reported as unresolved; aggregates over
different admitted sets are never compared across groupings. Within
each shared target, both groupings are scored on:

- the intersection of their bearer universes;
- the same scored target cells and reference outcomes;
- the same M0 baseline and primary denominator;
- the same union source-information bundle, from which each assignment
  rule may use only its declared source properties;
- the same unresolved policy (M0 fallback in the primary score).

No pattern is required in advance. One grouping may perform better on
both targets, both may perform similarly, or their order may reverse.
Any of those outcomes is informative. If the overlapping evidence is
inadequate, the report must state that inquiry dependence remains
unresolved even if separate local projections succeed.

### Secondary leave-one-source-property-out experiment

For each assignment source property in turn, a secondary run removes
that property from both the target row's visible record and the
assignment rule, infers modified membership (named for what it is:
for example INTJ-minus-P04, not INTJ) from the remaining sources
under thresholds frozen per fold, and predicts the omitted property.
This tests whether the rest of the diagnostic cluster recovers an
omitted component (cluster cohesion). It is a different projection
family from the outward non-assignment primaries, is reported
separately, and never pools with them.

### Secondary membership-retention experiment

A separate experiment may retain a previously established assignment
while removing underlying source observations. That tests whether the
label is a useful stored summary. It cannot be reported as evidence that
the target was inferable from the surviving sources. If the retained
assignment was originally based on the target, the run is excluded from
this secondary experiment unless that dependence is the explicitly stated
object of a retention analysis.

### Frozen analysis configuration

The machine-readable implemented rules are the starting rules for
approval. Listing source columns does not replace them.

**INTJ assignment** (sources P01, P02, P03, P04, P05, P07): score `+1`
for P01=Y, P02=Y, P03=N, P04=N, P05=N, and P07=Y; score `-1` for each
opposite known value; ignore unknown or concealed sources. Let `nvis`
be the number of visible eligible sources and `frac = score/nvis`.
Assignment is MEMBER only if P01=Y or P02=Y is visible, `nvis >= 2`,
`score >= 2`, and `frac >= 0.5`. It is NONMEMBER if `nvis >= 2` and
`frac <= 0`. Otherwise it is UNRESOLVED.

**EXPRESSIVE assignment** (sources P08 and P07): MEMBER if P08=Y is
visible and P07 is not a visible N; NONMEMBER if P08=N is visible;
otherwise UNRESOLVED.

No assignment rule is yet specified for the separate SUPPLEMENT
expression–construction table. DEPICTIVE has no approved rule while it
remains deferred. Neither may borrow a rule silently from the sign-type
matrix.

**Probabilities.** M0 and M2 use a Laplace-smoothed categorical
distribution with pseudocount `alpha = 1` for every outcome class. M2
uses the same-assignment reference distribution only when at least three
reference rows have known target values in that assignment outcome;
otherwise it uses M0. If there is no known reference outcome for a target
column, the target cell is not scoreable and is recorded under the
evidence gate rather than assigned a probability.

**M1.** The direct model is logistic/multinomial regression with L2
`C = 1.0`, `lbfgs`, and a maximum of 300 iterations. There is no tuning
on scored outcomes. Each permitted binary source contributes two
features: its value, with unknowns replaced by the visible reference
mean, and a missingness indicator. Training and target rows use the same
layout. A rotation whose permitted sources cease to be binary may not
run until its one-hot or ordinal encoding is separately frozen.

**Primary denominator.** Every bearer in the declared universe with a
known target and at least one reference outcome is scored once per
target in the exhaustive one-cell analysis. Unresolved assignments stay
in the denominator and receive M0 under M2 and M3. Conditional-on-resolved
results are secondary and always paired with assignment coverage.

**Multiple targets.** Every admitted target and every repaired P10
dimension or P11 contribution-by-host unit is scored separately, and
per-projection gains are the primary outcomes. One secondary family
summary is predeclared: the equal-weight (property-weighted) mean of
admitted per-projection grouping gains within a grouping, reported
with its range across projections and alongside every constituent
gain. A cell-weighted mean is a labelled sensitivity only. No
aggregate is a verdict on a grouping's overall standing, and no
summary may be selected post hoc from among these for headline use.
Field strata (distribution, morphology, morphosyntax, meaning,
realization, interaction, from `properties.csv`) are fixed here for
stratified reporting.

## 3. Outcomes

For each projection, report:

- mean log loss for M0, M1, and M2, all scored cells combined;
- the three central contrasts above;
- assignment coverage (member / nonmember / unresolved);
- recovery conditional on resolved assignment;
- coverage by bearer, source-evidence type, and target value;
- item-specific versus class-inherited target support;
- sensitivity to disputed codings and to removing high-leverage form
  families or assertion clusters.

Continuous gains are the primary outcome. Labels summarize them locally
and never replace the estimates:

- **Supported gain:** under the primary coding, the fixed-inventory
  grouping gain reaches the projection's frozen materiality threshold
  and is not reversed by defensible alternative codings of the *same
  cases*. Dependence labels below may still qualify its interpretation.
- **Supported but coding-sensitive:** the primary coding reaches the
  threshold, but equally defensible recodings of the same cases move the
  gain across the threshold or across zero.
- **Evidence against a useful gain:** the primary estimate and its
  same-case coding-sensitivity range are concentrated at or below the
  frozen negligible threshold.
- **Insufficient information:** eligible targets, resolved assignments,
  outcome classes, or assertion support are too sparse to distinguish
  a useful gain from a negligible one.

Dependence on evidence type or inventory composition is reported as a
qualifier, not an automatic veto. For example, “supported gain,
concentrated in class-inherited targets” preserves both the full-record
result and the absence of a corresponding item-specific result. Removing
assertion clusters, form families, or disputed inclusions changes the
domain or evidence subset; it shows what the answer depends on rather
than supplying another sample from the same domain.

Evidence gates likewise have two levels. A computation gate asks whether
there is enough target and assignment support to make the fixed-inventory
comparison informative. A stronger linguistic interpretation additionally
depends on item-specific support, distinct assertions, and the codings'
semantic audit. Passing the first does not automatically license the
second.

Threshold values are projection-specific judgments set at approval.
Fake-data results inform estimator behaviour and feasibility; they do
not by themselves decide what gain is substantively useful. Thresholds
do not demote a grouping as a whole. Failure on one target leaves other
projections untouched.

Uncertainty and dependence are reported in three distinct forms:

1. variation across lesion scenarios;
2. robustness to plausible alternative codings of the same cases;
3. dependence on evidence type and inventory composition, including
   form-family and assertion-cluster exclusions.

At the exhaustive one-cell lesion size there is no mask-sampling error:
the summary is exact for the frozen inventory and coding. Coding and
composition sensitivity remain substantive.

## 4. Assertions first, matrix second

The matrix is a derived view of an assertion-level evidence record. Every
non-U cell must point to one or more assertion records containing:

- `assertion_id` (stable, unique to the source claim, not to each cell)
  and `proposition_id`/`observation_id` for each distinguishable claim or
  observation within it;
- source document, authors, year, and stable page or section location;
- verbatim quotation span or spans, each with its evidential role;
- the source's own wording for the behaviour or contribution;
- item-specific or class-level support, and the exact class if inherited;
- quantifier/modality (for example possible, usual, characteristic,
  normally, categorical, obligatory);
- language/variety and conventional use addressed;
- construction and environment addressed;
- source lineage: whether the passage repeats, cites, or depends on an
  earlier assertion, where that can be determined;
- the claim strength actually supported (attested possibility,
  recurrent/characteristic behaviour, or categorical/default claim);
- other cells or propositions supported by the same observation, where
  that dependence is known;
- coder, model provenance, adjudication state, and coding rationale.

A class-level assertion may support several explicitly included items.
Those cells share an assertion identifier. They can jointly demonstrate
that the descriptive record is inferentially organized, but they do not
multiply independent confirmations of the class generalization. Analyses
must report results with class-inherited targets included and, as a
sensitivity, restricted to item-specifically documented targets.

A cell may rest on multiple spans only if every span is separately
identified and its role is stated (for example, one span establishes class
inclusion and another states the property). Ellipsis-joined text is not a
quotation. Publication pages must be resolved before production coding;
markdown line numbers may supplement them, not replace them.

Silence is U. N requires positive evidence under the property's stated
negative standard. No model-introspection value enters the primary record.

**Proposition-level concealment.** Hiding a spreadsheet target cell is
not enough if a retained source cell re-encodes the same observation.
For every scored source–target pair, the evidence record must state one
of: distinct observations; distinct propositions in a shared passage;
or the same observation / inseparable support. In the third case, that
source value is also concealed for the target row in the run unless it
has an independent supporting observation. Sharing a passage is not by
itself disqualifying. What matters is whether the retained source can be
supported without relying on the target observation. This dependence
classification is semantic-audited, and its frequency is reported for
each projection.

## 5. Items, bearers, and rotations

The starting sign-type inventory is `items.csv` (35 rows): 33 Tier-1
rows and two Tier-2 regional rows, grouped by form family (the three
*damn* uses and two *bang* uses). The item and property tables will be
embedded verbatim in the approved freeze; the CSV remains the machine-
readable authority if a rendered table and CSV disagree.

### Bearer universes

Each rotation fixes its own candidate universe before coding. Per row and
rotation, the states are member, nonmember, or not-a-bearer.
Not-a-bearer rows are excluded from scoring and reference sets. Declared
non-overlap of universes is a design domain, not an empirical finding.
Alignment of memberships within a shared universe is reportable.

### Candidate projections

| Rotation | Bearer | Permitted sources (draft) | Candidate targets (admitted by section 8 gate) | Status |
|---|---|---|---|---|
| INTJ | lexical sign-types | P01-P05, P07 | P06, P08, P09, P10 units, P11 units, P12 hosted, P13 | candidate |
| EXPRESSIVE | conventional uses | P08, P07 | P01-P06, P09, P10 units, P11 units, P12 hosted, P13 | candidate |
| SUPPLEMENT | expression–construction pairings | construction diagnostics excluding prosody | hosted prosodic separation | separate linked table |
| DEPICTIVE | conventional depictive uses | P09 | repetition dimensions, P13 | deferred pending positives |

P14 is not a candidate target in any rotation (descriptor, section
6). P10 enters only as separately gated pattern-by-dimension units
and P11 only as separately gated contribution-by-host units under
the repaired definitions in section 6; neither enters as a pooled
column. Assignment properties are never membership-inferred targets
for their own grouping; they appear as targets only in the
leave-one-source-property-out secondary (section 2) under modified
grouping names.

The INTJ and EXPRESSIVE rotations use the sign-type matrix. SUPPLEMENT
does not: capability of a sign-type, function in one construction, and
prosody of an occurrence are different objects. It requires a linked
expression–construction table with integrated counterparts. DEPICTIVE
remains deferred unless the final inventory contains several independently
documented depictive positives under an explicit selection rationale.
BANG_DEPICT alone is not enough.

Sequential-action and phonological-stratum projections are not in v1:
the declared matrix lacks independently observed sequential consequences
and alternation/acquisition targets for them.

## 6. Properties

Property headings are analyst shorthand for evidence to extract. They are
not definitions, and sources need not use the heading. The current
starting set is `properties.csv` (P01-P14), with the following
pre-approval repairs required rather than inherited silently:

- **P01:** separate solitary occurrence, contextual dependence, and a
  source's explicit conventional-utterance characterization. Do not infer
  syntactic ellipsis merely from context dependence.
- **P02:** retain only as shorthand for occurrence with another complete
  unit while retaining separate utterance-like status and not entering
  its construction, with source wording preserved. Ameka's *co-utterances*
  in their distributional context are calibration evidence, not a label
  match.
- **P03-P05:** record the environments in which the specified use had a
  genuine opportunity to integrate, take dependents, or inflect. Absence
  without opportunity is U.
- **P06:** record attested determiner/number combination separately from
  any conversion analysis. Sign-type identity must not be revised because
  an adverse combination appears.
- **P07-P09:** preserve whether the claim is about conventional
  contribution or an occurrence-level display/effect. Silence about a
  contribution is not its absence.
- **P10:** split the evidence into strengthening, event multiplication,
  redundancy, and unavailability. More than one may be supported. The
  repetition form and prosodic context must be recorded.
- **P11:** do not pool operators in the primary version. Select one
  primary operator at freeze (negation is the draft default) and retain
  others as separate evidence fields. Add an explicit inapplicable state
  at the assertion layer for uses with no host environment; it is not the
  same as an unscored unknown.
- **P12:** define the *hosted* environment. A standalone utterance's own
  boundary is not by itself the target observation.
- **P13:** state the speech community whose phonology supplies the
  baseline and distinguish a permitted variant's existence from evidence
  excluding all such variants.
- **P14:** identifying glosses are descriptors of rows, not independently
  recovered sequential consequences. P14 is not a candidate target in
  its current form.
- No P16 is created merely to duplicate P11's negation component under a
  second number. The same observation may be a source in one projection
  and a target in another only under separately declared runs.

Negative standards remain in `properties.csv`, revised to match the
same principles at approval. If a property is repaired by splitting it,
the split, identifiers, and derivation from assertions are frozen before
production coding.

## 7. Coding and adjudication

- Coding is siloed by property. A coder sees one property description,
  shuffled bearers with controls interleaved, and a source packet for each
  bearer. It does not see other columns, assignments, item tiers, or
  rotation hypotheses.
- Packets separate item-form passages from class/context passages and
  preserve source wording. Publication page, section, and packet hash are
  recorded. A class/context passage supports a cell only under the
  evidence rules in section 4. The builder must retrieve qualification
  and counterevidence passages (hedges, weakening, conflicting or
  null findings in the same source discussion) with the same priority
  as the generalizations they qualify, and must include use-identity
  context sufficient to distinguish specified uses from same-form
  neighbours. Both requirements come from documented audit failures
  (one-sided Heine prosody packets; a discarded same-form token coded
  as the specified use). One-sided retrieval is a builder defect,
  counted and reported.
- Three independent routes are desired, but a route is not a model.
  For every call, preserve configured model identity or local digest where
  technically available, CLI version, prompt hash, packet hash, settings,
  raw response, timing, token/credit usage, and every retry. Sessions must
  be fresh and must not inherit project context.
- Mechanical validation is 100%, not sampled: identifier membership,
  required fields, allowed values, continuous exact quotation after a
  declared normalization rule, quote in cited packet and source, source
  wording in at least one cited span, and span-role completeness. A
  mechanical failure is retried only within a frozen retry ceiling. Every
  attempt is retained. If no valid attempt remains, the vote is U for
  primary scoring and the invalid original remains an audit record.
- Consensus is an actual majority among non-U valid votes, requiring at
  least two valid non-U votes. Statistical reports include quote-validated
  values only. Inter-model agreement is reported as agreement, never as
  human intercoder reliability, alongside value marginals and raw pairwise
  agreement because kappa is prevalence-sensitive.
- Human adjudication reviews semantic entailment, not only quotations:
  correct language/variety, specified use, class scope, quantification,
  environment, and whether the span supports the proposition. Review all
  distinct assertions on which admitted targets depend if feasible;
  otherwise a predeclared stratified sample that includes unanimous and
  strict-pass cells, disagreements, negatives, and U cells.
  Adjudication is packet-only where that is the declared evidence basis.
  Model semantic review may precede and triage human review, is always
  named as model review with route and model identity recorded, and
  never counts as human validation. The development audit contains no
  human adjudication; production must not repeat that mislabelling.
- Adjudication outcomes are structured effective fields (effective
  pattern, dimension, contribution, host, strength, support type, and
  use status as applicable, plus a canonical proposition ID), never
  prose qualifications alone. Derived cells and units are generated
  from effective fields. A qualification that cannot be represented as
  an effective-field correction does not change any count and must be
  reported as an unresolved adjudication defect.
- Applicability and eligibility denominators: every proposed
  INAPPLICABLE or not-a-bearer exclusion requires a separate record
  stating the frozen target environment, why it cannot apply, and the
  named human checker who approved it. Unchecked proposals remain in
  denominators. The human checker for production is Brett Reynolds
  unless a substitute is named at approval **[BRETT TO CONFIRM]**;
  expected load is every proposed exclusion plus the stratified
  assertion sample above, and production does not start until that
  commitment is explicit.

## 8. Target-eligibility function (replaces per-projection gate setting)

No property is a primary target by designation. For each grouping,
every candidate non-assignment target in section 5 is admitted as a
primary projection if and only if it passes the single frozen
eligibility function below, computed by the locked gate script
(section 9) from the hashed production record. There is no separate
coverage census: production coding is the census, and investigators
receive only gate-script summaries before the reveal. Thresholds are
frozen at approval, before production coding. Changing any threshold
after gate output exists is a deviation; analyses following such a
change are exploratory.

Counts are post-concealment scorable cells: known target cells on
eligible bearers, after proposition-level concealment (section 4)
removes or blocks cells whose only source support shares the target
observation. Raw known counts never admit a target. For binary
targets, outcome classes are Y and N under the property's negative
standard; for categorical units (repaired P10 dimensions, P11
units), each scored class counts separately and at least two classes
must meet the per-class floor.

Draft thresholds **[BRETT TO APPROVE NUMBERS]**, calibrated from the
corrected P10 to P12 audit (admission failures) and round-6 fake-data
checks (`SIMULATION.md`; no gate variant created positive aggregate
bias under the null, and evidence criteria are what exclude
audit-style shallow targets):

- applicable bearers (human-checked denominator, section 7) >= 25;
- scorable target cells >= 18;
- resolved assignments among scorable cells >= 12, with >= 4 member
  and >= 4 nonmember assignments;
- >= 4 scorable cells in each outcome class needed by the contrast;
- item-direct scorable cells >= 6, with >= 2 in each such outcome
  class;
- distinct canonical propositions behind scorable cells >= 4;
- no single canonical proposition behind more than 50% of scorable
  cells;
- scorable cells include at least one control-tier row and no more
  than one third from any single form family;
- target is not an assignment source for the grouping, and its
  evidence does not enter the grouping's assignment rule in any
  repaired or split form.

A candidate failing any clause is reported as insufficient
information for that grouping, with its full gate vector published.
Failure is a finding about the descriptive record, not a failed
category, and it does not affect other projections. If a grouping
admits no target, its primary family is empty and reported as such.
Materiality thresholds for calling an admitted gain supported
(section 3 labels) remain projection-level judgments set at approval
and are distinct from admission: the eligibility function decides
what is scored as primary, never what counts as success.

## 9. Outcome firewall and development data

Fake data and explicitly discarded pilots may be inspected for design.
Cells from those pilots are never study data. During production coding,
nobody computes cross-column associations, complete-row assignments,
lesion scores, predictor comparisons, or projection outcomes. Permitted
checks are schema validation, quote verification, packet-only semantic
adjudication inside one silo, and the frozen known-cell counts needed for
evidence gates. Once assembly is complete, the evidence record and
derived matrix are hashed. A locked gate script may then compute the
assignments needed solely to emit the predeclared gate summaries
(resolved counts, target-class counts, and distinct-assertion counts)
shown to the investigators. Its full assignment output is sealed with the
analysis artifacts and is not manually inspected before the registered
primary analysis. Any other inspection
goes in `DEVIATIONS.md`, and analyses after the reveal are exploratory.

A discarded target-evidence audit is development data. It may inspect
whether target evidence exists, but it must not report or use
source–target associations. If its items later enter production, they are
coded fresh under production packets and prompts.

## 10. Threats that design must keep visible

- **Descriptive-record scope:** results concern recovery within the
  declared inventory and coded literature. They do not estimate speaker
  behaviour in unseen cases without a new design.
- **Repeated assertions:** one source claim can support many cells.
  Assertion IDs, class-inheritance sensitivities, and assertion-cluster
  exclusions are mandatory.
- **Selective documentation:** known cells are not missing at random by
  default. Rich profiles for canonical examples and silence for controls
  can make the scored subset look more coherent. Coverage is part of the
  result.
- **Model contamination and dependence:** coding models were trained on
  overlapping text and read identical packets. Independent families do not
  guarantee independent errors. Blindness concerns columns, assignments,
  and hypotheses, not prior knowledge. Verbatim and semantic checks are
  therefore separate.
- **Circular packet retrieval:** a packet builder tuned to a framework's
  vocabulary can privilege some descriptions. Retrieval queries and missed-
  passage audits are process outcomes, not invisible preprocessing.
- **Complexity laundering:** an elaborate assignment rule can reproduce a
  matrix without providing a compact grouping. Specification cost and
  unresolved outcomes are reported.
- **Bearer drift:** sign-types, conventional uses, expression–construction
  pairings, and occurrences are never silently exchanged across rotations.

## 11. Files and reporting

- `assertions/`: assertion records and source-span index.
- `packets/`: generated packets with builder version and hashes.
- `codings/`: append-only raw attempts and provider metadata.
- `adjudication-log.md`: every adjudicated cell and deciding spans.
- `matrix/`: generated consensus matrix, derivation script, and hash.
- `lesion/`: tested analysis code, configurations, seeds, and results.
- `DEVIATIONS.md`: created empty at freeze time.
- AI disclosure names every route and configured model family that coded
  assertions or cells.

Reports distinguish source assertions, derived cells, consensus values,
adjudicated values, and sensitivity values. Raw model outputs must never
be overwritten by cleaned results.

## 12. Development record

### Incorporated into v3 (2026-11-04)

The discarded target-evidence audit for P10, P11, and hosted P12 was
run, externally reviewed, and corrected under a Brett-approved
correction pass (`target-audit/TRIAGE-2026-11-04-external-review.md`,
corrected `target-audit/AUDIT.md`, `target-audit/COVERAGE-2026-11-04.md`).
Corrected findings: P10 rests on one mixed-position Potts proposition
and one pattern-unspecified Quirk proposition, with no depictive
contrast; the narrow P11 external target rests on one inherited CGEL
proposition with no within-target contrast (inheritance under Brett's
recorded scope ruling, CGEL Ch. 15 p. 1360); hosted P12 has no
item-specific evidence and contested inherited lineages. The audit
also established three process lessons now in sections 4, 7, and 8:
prose qualifications do not survive aggregation without structured
effective fields; packet builders can retrieve generalizations while
missing their same-section qualifications; and model semantic review
mislabelled as human review passed a wrong-use token whose context
was in-packet. No human adjudication exists in the development
record. Round-6 fake-data checks of the eligibility pipeline
(`sim_round6_eligibility.py`, `SIMULATION.md`) found no positive
aggregate bias under the null for any candidate gate, scarce
negatives as the binding admission constraint, and aggregate dilution
of crossed structure, motivating per-projection primaries with one
secondary property-weighted summary. Brett approved the amended
eligibility architecture on 2026-11-04. P10 to P12 require no further
audit; sampled pairs will be recoded fresh in production.

### Incorporated into v2

The fake-data rounds established that the original absolute assignment
threshold was unreachable under sparsity; that pooled targets dilute
rotation-specific structure; that source-complete and sparse-row regimes
ask different questions; and that coding completeness matters more than a
modest row-count increase. Their numerical power values are design
diagnostics only. They do not become operating characteristics until the
repaired pipeline, evidence gates, dependence structures, categorical
targets, and uncertainty rules are simulated together.

The three P02 pilots established that all routes can return parseable
cells, that verbatim quotation is usually respected, that framework-bound
instructions suppressed relevant Ameka evidence, and that relevance-ranked
packets improved retrieval for already-supported items without solving
fill. They did not establish semantic coding validity as a general
property; MMHM's Siwu evidence is the standing counterexample.

## Appendix A. Current item and property inventories (generated mirror)

These tables are generated from `items.csv` and `properties.csv`. If a table and its CSV disagree, the CSV governs and the disagreement must be logged as a deviation.

### Items

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

### Properties

| ID | Name | Group | Values | INTJ source | EXPRESSIVE source |
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

## 13. Approval checklist

Approved by Brett (2026-11-04): the fixed-inventory direction, the
v2 estimand and membership experiments as incorporated, and the
amended target-eligibility architecture (no privileged primaries,
single frozen eligibility function, per-projection primaries,
prespecified reconstruction terminology, leave-one-source-out as
secondary). Still needed before this draft can freeze:

1. Numeric eligibility thresholds in section 8 (draft numbers from
   round-6 simulation and corrected-audit calibration).
2. Numerical negligible-gain and materiality thresholds for section
   3 outcome labels.
3. Human checker commitment in section 7 (named checker, exclusion
   approvals, stratified assertion sample size).
4. Final item universes, controls, and form-family blocks; property
   splits and the primary P11 operator under the repaired unit
   definitions.
5. The supplement expression–construction table and DEPICTIVE
   deferral (unchanged from v2, still to confirm for v3 scope).
6. Model routes, batching, retry ceilings, and provenance
   requirements for production coding.
7. Registration venue and timing after the consolidated freeze is
   signed.

Until those items are settled, this is a development protocol. It does
not authorize production coding.
