# DRAFT PROTOCOL v4: Fixed-inventory lesion study of inquiry-relative classifications

**Status: DRAFT, NOT APPROVED, NOT FROZEN, NOT REGISTERED.** Prepared
2026-11-04 by the Claude Code session that evaluated v3
(`../../reviews/matrix-lesion-evaluation-2026-11-04/EVALUATION.md`,
with its addendum), after Brett accepted the evaluation and set the
assignment principle: "a simple tally is not the way to go. That's not
how HPC works. absences count, surely. No property on its own can
'decide membership'." This draft supersedes `FREEZE-v3.md` where they
conflict and otherwise carries v3 forward unchanged.

The v4 changes: membership is graded convergence, not a tally, for
every grouping (section 2); absences and presences have equal standing,
and opportunity documentation sets an absence's strength rather than
its admission (section 6); inherited evidence counts as one testimony
unit per source and inclusion judgment, with same-inclusion concealment
and an "entailed" dependence state (section 4); P04, P05, and P06 are
made disjoint (section 6); P08 coding carries a guard against
*CGEL*'s broad "expressive" (section 6); member-row and nonmember-row
contributions are reported separately (section 3). The development
record (section 12) lists what v4 does not yet incorporate from the
deeper v3 triage, which remains for Brett's decision.

From v3: no property is privileged as a primary target by theoretical
interest. v4 goes further: every candidate target is reported, with its
uncertainty and evidence counts, and none is admitted, selected, or
labelled (sections 3 and 8).
The commitment is a prespecified primary reconstruction analysis.
Numeric thresholds marked for approval do not bind until Brett approves
them in writing, the approved version is committed, and the same version
is registered before production coding begins.

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
“the 46 declared sign-types” or the relevant perspective's declared set
(section 5), not “English” without qualification.

The study evaluates named projections. A projection states:

- the bearers and bearer universe;
- the grouping and assignment rule;
- the permitted source observations;
- the concealed target property and environment;
- the reference set;
- the outcome measure and the membership model.

No result is a verdict on a category's overall standing. Each projection
can succeed, fail, or lack enough evidence independently.

**Two claims, kept apart.** A *record-reconstruction* claim says that,
for documented and scorable cells in the frozen coding, grouping G
recovers concealed target T from the permitted sources with a stated gain
over M0 and stated estimator contrasts. It is exact for the frozen record,
subject to coding sensitivity. A *projective-warrant* claim says that, for
the declared bearers, including those whose target is currently unknown,
observing the permitted sources warrants an expectation about T. The
second needs more than the first: semantically checked propositions;
source and target observations kept apart for reference rows as well as
target rows (section 2); the documentation diagnostics and mandatory
comparators; and robustness to defensible recodings. Primary gains
average over documented scorable cells only, and every result is reported
as record reconstruction unless those further conditions are met and
stated. Neither claim says anything about causal order, maintenance, or a
category's standing in general.

**What is estimated.** In Slater's terms, the record-reconstruction claim
concerns *cliquish stability* in the documented record: whether
possessing some of a cluster's properties "reliably (if imperfectly)
indicates the possession of whole cluster". It doesn't concern *instance
stability* (whether members resist losing cluster properties), and it
doesn't concern what maintains the cluster. Slater 2015 (*BJPS* 66(2):
375–411), as used in *Words That Won't Hold Still* ch. 4; the quotation is
from the held copy, a 2011 draft (§5.2), so no published page is given.

## 2. Principal lesion and comparisons

The principal experiment is **source-complete, membership inferred**:

1. Select one eligible target cell.
2. For the target row, retain every known cell in the rotation's permitted
   source set. Conceal the target and all non-source cells for that row.
3. Apply the same concealment to every reference row. A reference row's
   source cell that shares an observation with that row's own target
   value, is entailed by it, or rests on the same inclusion judgment
   (section 4) is concealed for the run, so no learned category–target
   association is built from duplicated evidence. Reference outcomes in
   the target column are the training observations. The version with
   reference rows left intact is reported only as the
   record-reconstruction result (section 1).
4. Refit the membership model to the information state left after
   concealment, separately for each projection, and infer every row's
   membership from it. M1 receives exactly the same information state.
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
- **M2, category/compression predictor:** the target row's graded
  membership (section 2, frozen analysis configuration) weights the
  target rates of the grouping's latent classes, each rate estimated
  from reference rows weighted by their own membership. There is no
  unresolved state; a row with little visible evidence receives
  posterior membership near the class prior, which pulls M2 toward M0.
- **M1, direct-property predictor:** regularized logistic/multinomial
  model using *the same permitted source columns*, and only those
  columns, for training and target rows. Missingness indicators and the
  imputation rule are part of the permitted information state and are
  fixed before fitting.
- **M3, sources plus membership:** the M1 model with the row's member
  posterior added as a feature. Against M2 it is a **sufficiency test**:
  if the visible sources add nothing once membership is known
  (loss(M2) − loss(M3) near zero), membership is approximately sufficient
  for the target, which is what it means for a grouping to carry what
  its sources tell us about that target. M3 against M1 remains only an
  estimator comparison.

Central reported contrasts:

| Contrast | Interpretation |
|---|---|
| loss(M0) − loss(M2) | grouping gain on the documented record |
| loss(M0) − loss(M1) | direct-source gain: recoverable structure in permitted sources |
| loss(M2) − loss(M1) | compression cost: performance lost (if positive) or gained (if negative) by using the grouping instead of the direct sources |
| loss(M2) − loss(M3) | sufficiency gap: what the visible sources add once membership is known |

Substantive comparators are declared per projection where relevant:
a leading single source property, an unthresholded convergence score,
and a broader or narrower alternative grouping. “Compression” claims must
also report the grouping's specification cost: number of source
properties, classes, and special cases, and the share of rows with
membership posteriors between 0.2 and 0.8.

### Cross-inquiry comparison

Local projections alone do not answer the comparative question in
section 1. A limited cross-inquiry comparison is therefore part of the
principal design wherever bearers and evidence overlap.

The comparison is INTJ versus EXPRESSIVE on every target admitted
for both groupings under section 8 (shared eligible targets). With
EXPRESSIVE now assigned by convergence over P07, P08, P10, and P11,
the candidate shared pool is P06, P09, P12, and P13; the corrected
audit already shows hosted P12 shallow. Whether any shared target can
pass for both groupings is to be checked in the yield audit
(section 12) before Round 7. If no shared target is admitted,
inquiry dependence is reported as unresolved; aggregates over
different admitted sets are never compared across groupings. Within
each shared target, both groupings are scored on:

- the intersection of their bearer universes;
- the same scored target cells and reference outcomes;
- the same M0 baseline and primary denominator;
- the same union source-information bundle, from which each assignment
  rule may use only its declared source properties;
- the same membership model and M0 fallback for thin classes.

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
refitted without that property, and predicts the omitted property.
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

**Membership model (both groupings).** Membership is graded
convergence, not a tally. For each grouping, a two-class binary
latent-class model is fitted by EM to every bearer row's visible
diagnostic cells. Unknown and concealed cells contribute nothing.
Estimation is MAP under Beta(2,2) priors on class-conditional rates and a
Dirichlet(2) prior on class sizes, which amounts to add-one smoothing of
each rate and size, as implemented in `sim_convergence_assignment.py`;
eight random starts, best penalized likelihood.
Each diagnostic's contribution comes from the fitted class-conditional
rates, so no diagnostic is weighted by hand, none is required, and
none decides membership. Presences and absences enter identically.
The *member class* is the class whose rates best match the grouping's
stated profile, declared here in advance: for INTJ, higher P01, P02,
and P07 and lower P03, P04, and P05; for EXPRESSIVE, higher P07, P08,
P10 strengthening, and P11 survival under negation. The orientation
labels a class; it doesn't weight evidence. A row's membership is its
posterior probability of the member class.

- **INTJ diagnostics:** P01, P02, P03, P04, P05, P07.
- **EXPRESSIVE diagnostics:** P07, P08, the P10 strengthening unit, and
  the P11 negation unit. The corrected target audit found P10 and P11
  thin (P10 item-direct for 4 of 12 sampled items; P11 item-direct for
  2, inherited for 2), so in the real record most of those cells may be
  U and EXPRESSIVE membership may rest largely on P07 and P08. The
  model handles that without a special case, since unknown cells
  contribute nothing, but the yield audit must show whether the
  membership-mass clause in section 8 can pass. In the sparse-evidence
  follow-up (`CONVERGENCE-CHECK.md`), convergence still beat the
  anchor-only rule with P10 and P11 documented for a third of rows
  (+0.032 against +0.009) and nearly matched it at 15% (+0.007 against
  +0.004 with scarce negatives); with the anchor that thin, P07, which
  INTJ also uses, could steer the class split.
- **Sensitivity:** both groupings refitted without P07, their one
  shared diagnostic, so that drift between them through it is visible.
  P07 stays in both primary sets: meaning is one of the converging
  diagnostics for the lexical category, not only a target.
- **Families and derived states (2026-11-05).** How a family (section 6)
  is pooled depends on what it records, so that one mechanism doesn't
  count as several and distinct facts aren't counted as one. A family
  declared to record one fact (TRUTH_CONDITIONAL: P07D and P11E) counts
  once: its visible cells on a row share weight 1, as a testimony unit's
  cells do. A family of distinct facts under a joint constraint
  (POSITION: P01–P03) keeps full weight per cell, with the constraint
  enforced. The determinatives codebook pools columns within
  super-columns partially, in a hierarchical model; the two-class model
  here has no such level, so the rule is stated family by family.
  Correlated properties are not merged unless one follows logically
  from the other. Derived states
  (the POSITION family's standalone-only state, and every x) are never
  coded and never enter the fit. The relatedness facts (roots and word
  form, section 6) are never diagnostics; the analysis runs with and
  without them, pooled by base.
- **Copies check.** Before any result is read, the rows of each form
  family are duplicated and the verdict must not move.
- **Estimability [BRETT TO APPROVE NUMBERS].** A grouping's membership
  is reported as not estimable, and its projections as insufficient
  information, unless all four checks pass on the post-concealment
  record. (a) Support: at least 10 bearer rows carry three or more
  visible diagnostics, counting the cells of one testimony unit once.
  (b) Overlap: every pair of diagnostics is jointly visible on at least
  5 rows. (c) Stability: across 50 bootstrap refits, rows' member
  posteriors correlate with the full-record posteriors at 0.8 or above.
  (d) Anchor compatibility: the member class's rate on the anchoring
  diagnostic (P08 for EXPRESSIVE; P01 or P02 for INTJ) exceeds the other
  class's by at least 0.3. Labelling a class as the members can't
  rescue a split that fails (d). A failure is a finding, never a reason
  to fall back on a tally or a single property. A two-class model on two
  yes/no diagnostics can't settle which split is the member class, and P11
  is x (not applicable) for uses with no host environment, so such rows
  carry at most three EXPRESSIVE diagnostics. The x state is derived from
  the recorded host environment, never coded. A standalone-only use has
  no host unless an independent adjacent turn counts as one, which is
  open (section 13). The yield audit reports the counts these checks
  need (section 12).
- **Sensitivity:** a three-class model, so that a heterogeneous
  complement can split; reported beside the primary, never substituted
  for it.
- **To be frozen before production [BRETT TO APPROVE]:** whether
  absence strength (stated against opportunity-documented, section 6)
  enters as a likelihood weight, and the weights; how testimony units
  (section 4) are weighted (default: the cells of one unit share a
  total likelihood weight of 1).

**Fake-data requirement.** The checks in `CONVERGENCE-CHECK.md` used one
fit per dataset, no concealment, no testimony or absence-strength
weighting, and 33 rows, so they don't transfer automatically. Before any
number in this section is approved, the Round 7 harness reruns them on
this exact procedure: symmetric concealment, per-projection refit, the
chosen weightings, the estimability checks, and the 46-row inventory with
knownness patterned on the yield audit's sealed counts. It adds a
**bonds null world**, Thomson's sampling model applied to properties:
many overlapping, independent partial causes produce positive
associations among properties with no grouping at all. A record gain as
large there as in a world with a real cluster would show that record gain
can't tell a category from diffuse association (Shalizi, "*g*, a
Statistical Myth", 2007). The residual-dependence checks and the
sufficiency gap are the statistics expected to separate the two worlds,
and Round 7 tests whether they do.

The fake-data check behind this rule is `CONVERGENCE-CHECK.md`. Under
null worlds the model showed no positive bias and fewer material-looking
gains than the v3 tallies; it recovered the crosscutting dissociation;
and two and three classes agreed to within about 0.01. It also showed
that M1 is too weak at this size to certify compression (see
**Comparators** below).

**What the model is, and isn't.** The latent-class model is used as the
simplest summary of co-occurrence the record can support, not as a claim
about what holds a cluster together. Its structure is a common-cause
picture: each row is in one class, and the class produces each property
separately. HPC doesn't need that picture and in two respects departs
from it. Properties can sustain one another directly, as in the
prosodic–syntactic link argued in main.tex. And boundary items can
partly have a cluster rather than uncertainly belong to one class.
So a member posterior is epistemic, the model's uncertainty about which
class a row is in, and is never reported as a degree of membership. An
intermediate posterior may reflect genuine intermediacy or thin
evidence, and the model can't tell which. A mixed-membership
(grade-of-membership) model, in which partial membership is part of the
model, is the closer match to HPC; it is not adopted in v1 and is
untested at this size.

**Round 7 candidate: two crosscutting latent features.** Instead of two
separate one-grouping fits, a single model with two independent binary
latent features, one anchored in INTJ's diagnostics and one in
EXPRESSIVE's. Each row may have either feature, both, or neither, and
each candidate target may depend on either feature or both. Because the
features don't sum to one, the model represents crosscutting categories
directly, which a grade-of-membership model doesn't, and its target
loadings show which grouping carries which target. That is a more direct
test of inquiry dependence than comparing two separate fits. Round 7
tests whether it is estimable at 46 rows; if it isn't, the two separate
fits stay.

**Residual-dependence checks.** After each fit, report the pairwise
associations among diagnostics, and between diagnostics and targets,
that remain within the fitted classes, and run posterior predictive
checks: simulate matrices from the fitted model and compare their
pairwise association statistics with the observed record (Gelman and
Shalizi 2013, section 4, p. 17). Residual dependence explained by
shared testimony units is reported as such. Residual dependence not so
explained is the place where direct support between properties, or
subgroups within a class, would show. It's reported as a finding about
the cluster's internal structure, not corrected away.

**Comparators.** Any statement that a grouping compresses its sources
(M2 close to or better than the direct sources) also reports two
mandatory comparators: the best single diagnostic used alone as a
categorical predictor (all single-diagnostic predictors are reported,
without picking a winner after the fact), and an unthresholded
convergence score (the mean of signed visible diagnostics). In the
fake-data hub world, where one visible property drove every column, the
latent-class M2 beat the regularized M1 by 0.04 to 0.06. That
difference reflects M1's small-sample weakness, not information the
grouping added.

No assignment rule is yet specified for the separate SUPPLEMENT
expression–construction table. DEPICTIVE has no approved rule while it
remains deferred. Neither may borrow a rule silently from the sign-type
matrix.

**Probabilities.** M0 uses a Laplace-smoothed categorical distribution
with pseudocount `alpha = 1` for every outcome class. M2 is the target
row's posterior-weighted mixture of class target distributions. Each
class's distribution is Laplace-smoothed over reference rows weighted by
their posterior for that class; a class whose reference membership mass
is below 3 contributes the M0 distribution instead. If there is no known reference outcome for a target
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
target in the exhaustive one-cell analysis. There is no unresolved
state and no conditional-on-resolved analysis; intermediate memberships
stay in the primary score as they are.

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
- the distribution of graded membership over scored rows, and the
  effective member and nonmember mass;
- each contrast's contribution from member-weighted and
  nonmember-weighted rows, reported separately. A grouping licenses
  expectations about its members; its complement licenses none, so
  gain contributed by nonmember rows reflects which controls were
  declared and is never by itself evidence for a projection;
- coverage by bearer, source-evidence type, and target value;
- item-specific versus class-inherited target support;
- sensitivity to disputed codings and to removing high-leverage form
  families or assertion clusters.

Continuous estimates are the outcome. There are no outcome labels and no
materiality or negligible-gain thresholds: with 20 to 30 scored cells per
target, gains of a few hundredths of a nat sit near chance (the deeper v3
triage computed 5–10% of null configurations at or above 0.03), so a
fixed threshold would turn noise into a verdict. Every estimate is shown
with its uncertainty and counts, and the reader judges. Everything is
reported as record reconstruction (section 1); a projective-warrant
statement is made separately, only when the section 1 conditions are met
and named.

Dependence on evidence type or inventory composition is reported beside
each estimate, for example a gain concentrated in class-inherited
targets, with the item-specific result next to it. Removing assertion
clusters, form families, or disputed inclusions changes the domain or
evidence subset; it shows what the answer depends on rather than
supplying another sample from the same domain.

Uncertainty and dependence are reported in three distinct forms:

1. variation across lesion scenarios, and a bootstrap over rows that
   treats the declared inventory as one of many possible selections;
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
multiply independent confirmations of the class generalization.

**Testimony units.** Every inherited cell also records its
*inclusion judgment*: the source, the class named, and the passage
that places the item in that class. All cells a source attributes to
one item through statements about one class form a single testimony
unit. In assignment, a testimony unit counts once, however many cells
it supplies; each item-specific observation counts separately. This
applies to presences and absences alike. Inherited evidence is never
barred as a class. Barring it would fall mostly on absences, because
sources tend to show presences item by item in examples and to state
absences for the class.

Analyses must report results with class-inherited targets included and,
as sensitivities, (a) restricted to item-specifically documented
targets and (b) with every inherited cell removed from both sources and
targets. Sensitivity (b) is the strict test of whether a projection
survives without testimony.

A cell may rest on multiple spans only if every span is separately
identified and its role is stated (for example, one span establishes class
inclusion and another states the property). Ellipsis-joined text is not a
quotation. Publication pages must be resolved before production coding;
markdown line numbers may supplement them, not replace them.

Silence is U. N requires positive evidence under the property's stated
negative standard. No model-introspection value enters the primary record.

**Evidence tiers (v4).** Tier A, a quotation from a held source with its
page, remains the primary record. v4 admits Tier B, corpus attestation,
which FREEZE v1 reserved for a later amendment, under these terms:

- **Corpus.** CABNC (spoken British conversation, TalkBank CHAT
  transcription), the local checkout `vendor/CABNC-0a28a11` at the frozen
  commit and subtree recorded in `analysis/acquire-cabnc.sh`. It is
  searched locally by script. English-Corpora.org corpora (COCA, BNC) are
  used only through queries run by hand in a browser, never through the
  blocked wrapper, and only for cells CABNC leaves empty.
- **Presences and documented absences.** A Tier B cell supplies Y, or a
  positive value of a categorical unit, from an attested line of the
  specified use. It supplies N only from opportunity-documented
  non-occurrence: the property's corpus standard (`properties-v4.csv`)
  names the environment in which the property would show (for example,
  contexts where a rival verb or adjective analysis would need an
  inflected form for P05, or audio-measured hosted tokens for P12), and
  meaning properties have none. A frozen query retrieves those environments for the specified
  use, and at least K such opportunities show no instance [BRETT TO
  APPROVE K; draft 20]. Every Tier B cell records its counts (instances
  among opportunities), and a rate may be reported beside the value.
  Hits with no identifiable opportunities, or fewer than K, stay U:
  silence is still not N.
- **Record.** Corpus, file, and utterance or line ID; the line with
  enough context to identify the specified use; the frozen query string;
  and how the use was distinguished from same-form neighbours. Coding is
  done by the same property-siloed routes as Tier A, from the line and
  its context, with the same mechanical validation.
- **Scope.** Tier B searches target only cells left empty by Tier A in
  the yield audit's count (section 12), so the tier fills gaps rather than
  re-coding the record.
- **Reporting.** Every Tier B cell carries its tier. Primary results are
  reported on Tier A alone and on Tier A plus Tier B, with the difference
  shown; the section 8 counts are published for both. Tier B's Y and N
  fills are reported per property, so that filling which depends on the
  value is visible. Tiers are never pooled silently.

Tier C (model judgment or introspection) stays excluded. An **analyst
tier** (judgments by a named linguist from recorded test frames, coded
property by property with other columns hidden, reported separately) is
not admitted in v4. It is considered only for cells still empty after
Tiers A and B, which are expected to be mostly absences and the
controls' stance cells.

**Proposition-level concealment.** Hiding a spreadsheet target cell is
not enough if a retained source cell re-encodes the same observation.
For every scored source–target pair, the evidence record must state one
of: distinct observations; distinct propositions in a shared passage;
the same observation / inseparable support; **entailed** (the source
proposition entails the target value, or the reverse, under the frozen
property definitions); or **same inclusion** (source and target cells
are inherited through the same inclusion judgment). In the last three
cases, that source value is also concealed for the target row in the
run unless it has an independent supporting observation. Sharing a
passage is not by itself disqualifying. What matters is whether the
retained source can be supported without relying on the target
observation, on a proposition that entails it, or on the source's
classification of the item. This dependence classification is
semantic-audited, and its frequency is reported for each projection.
The rule applies to reference rows as well as target rows (section 2,
step 3; Brett, 2026-11-04). P11's x state is derived from the POSITION
family and the host record (section 6), so it is never coded and never
enters the membership fit. P11 values on rows with a host stay visible:
EXPRESSIVE projections onto P01–P03 conceal only P11's inapplicability
and missingness indicators, cell by cell, never the whole column
(2026-11-05).

## 5. Items, bearers, and rotations

The v4 inventory is `items-v4.csv` (46 rows): the 35 rows of
`items.csv` plus 11 rows that give EXPRESSIVE a bearer set from its own
literature. Rows are grouped by form family (*damn*, *bang*, *bloody*,
*bastard*). The item and property tables will be embedded verbatim in the
approved freeze; the CSV remains the machine-readable authority if a
rendered table and CSV disagree.

**v1 scope.** v1 covers INTJ and EXPRESSIVE on the sign-type matrix.
SUPPLEMENT, DEPICTIVE, and the sequential-action categories are outside
v1. Each will get its own bearer set, drawn from its own literature under
the rules below, in a later round, not token rows now.

**Bearer selection, per perspective.** Drawing every perspective's
bearers through the interjection literature would make the non-lexical
groupings look lexical and tilt the cross-inquiry comparison toward
INTJ. Each perspective's declared set is therefore selected from its
own literature by a rule fixed before coding:

- **INTJ:** the 35 rows of `items.csv` (core members from *CGEL*'s list,
  boundary cases from the interjection literature, lexical controls),
  plus every new single-word row as a nonmember candidate.
- **EXPRESSIVE:** the interjection rows, plus English expressive uses
  named in the expressive literature (Potts 2007; Ljung 2011's
  "slot filler" functions, pp. 33–35) that a grammar also describes
  (*CGEL*, or Quirk et al. 1985), so that their distribution and
  morphology aren't left to silence. Controls come from the same grammar
  passages: non-expressive items in the same slot (*very* beside
  *bloody* and *damn*, CGEL p. 584; *exactly* beside *the hell*,
  p. 1087; particularising and modal attributives beside expressive
  ones, pp. 557–558). Constructed controls are excluded, since a row must
  be codable from quotations; the supplementary epithet and infixation
  therefore have no control. A candidate with no grammar coverage is left out, which
  is why *son of a bitch*, *the devil*, and *like hell* aren't in v1.
  Slurs are not included in v1.

**Floors and balance.** Each perspective's declared set has at least 25
applicable bearers, with members and nonmembers each between 40% and 60%
of the set as judged from the selection rule (the coded record decides
actual membership). Controls are chosen for that perspective's contrast:
EXPRESSIVE's are integrated non-expressive counterparts, not nouns and
verbs chosen for INTJ. Equal set sizes are not a goal.

**Shared core.** All single-word rows are in both universes (41 rows),
so the cross-inquiry comparison runs on a planned intersection that
contains both groupings' members and nonmembers, not on whatever
interjection-literature rows happen to overlap.

### Bearer universes

A row's bearer is a sign-type: an identifiable expression in a
conventional use, the definition used in the paper. The three *damn*
rows are three sign-types, not one lexeme. INTJ's universe is the
sign-types whose expression is a single word; EXPRESSIVE's is every
sign-type in the inventory, including phrasal and sub-word ones. A
property is coded for the sign-type as specified: for a phrasal
sign-type such as the supplementary epithet *the bastard*, properties
concern the phrase in that use, not its head noun alone.

Each rotation fixes its own candidate universe before coding. Per row and
rotation, the states are member, nonmember, or not-a-bearer.
Not-a-bearer rows are excluded from scoring and reference sets. Declared
non-overlap of universes is a design domain, not an empirical finding.
Alignment of memberships within a shared universe is reportable.

### Candidate projections

| Rotation | Bearer | Permitted sources (draft) | Candidate targets (all reported, section 8) | Status |
|---|---|---|---|---|
| INTJ | lexical sign-types | P01-P05, P07 (distribution and morphology anchor; P07 from meaning) | P06, P08, P09, P10 units, P11 units, P12 hosted, P13 | candidate |
| EXPRESSIVE | conventional uses | P08, P10 units, P11 units (meaning anchor), P07 | P01-P06, P09, P12 hosted, P13 | candidate |
| SUPPLEMENT | expression–construction pairings | construction diagnostics excluding prosody | hosted prosodic separation | outside v1; own table and bearer set |
| DEPICTIVE | conventional depictive uses | P09 | repetition dimensions, P13 | outside v1; own bearer set from the depiction literature |

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
and alternation/acquisition targets for them, and their bearers (repair
formats, continuers, and closings that aren't interjections; words with
marginal phonology across categories) need sets of their own.

## 6. Properties

Property headings are analyst shorthand for evidence to extract. They are
not definitions, and sources need not use the heading. The current
starting set is `properties.csv` (P01-P14), with the following
pre-approval repairs required rather than inherited silently:

Since 2026-11-05, `properties-v4.csv` codes every property as a
possibility claim (subsection *Polarity, joint states and families*
below). P07 is coded as P07D, P11 as P11E, P12 as P12S and P12I, and P10
adds P10A and P10R; the old rows are kept as the record (type
superseded). Mentions of P07, P10, P11 and P12 elsewhere in this
protocol refer to the property, coded under the new identifiers. Where
the polarity is reversed, so is the member-class orientation: lower
P07D for both groupings, lower P11E for EXPRESSIVE.

- **P01:** separate solitary occurrence, contextual dependence, and a
  source's explicit conventional-utterance characterization. Do not infer
  syntactic ellipsis merely from context dependence.
- **P02:** retain only as shorthand for occurrence with another complete
  unit while retaining separate utterance-like status and not entering
  its construction, with source wording preserved. Ameka's *co-utterances*
  in their distributional context are calibration evidence, not a label
  match.
- **Absences (P03-P05, and every N value).** A source's explicit
  statement that the use lacks the property (invariance, no
  dependents, restriction to standalone or supplement positions) is N,
  with the class-inheritance and inclusion fields filled if it is
  stated for a class. Each N also records its *strength*: stated
  non-occurrence; non-occurrence documented with the environments in
  which the property had a genuine opportunity to appear; or both. A
  coder's inference from packet silence is U, never N. Opportunity
  documentation affects an absence's weight in assignment (section 2),
  not its admission. Absences and presences have equal standing.
- **P04, P05, and P06 are disjoint.** *CGEL* subdivides dependents
  into complements, modifiers, and determiners (p. 24), and number is
  inflection, so the v3 definitions let P06 be entailed by P04 and P05.
  In v4, P04 covers complements and modifiers only; P05 covers
  inflection other than number; P06 covers determiners (including
  quantifying determinatives) and number. Packets and prompts must
  state the split, and a source statement covering all dependents or
  all inflection supports the relevant cells of each property
  separately, with the dependence state "entailed" recorded between
  them (section 4).
- **P06:** record attested determiner/number combination separately from
  any conversion analysis. Sign-type identity must not be revised because
  an adverse combination appears.
- **P07-P09:** preserve whether the claim is about conventional
  contribution or an occurrence-level display/effect. Silence about a
  contribution is not its absence.
- **P08 guard.** *CGEL*'s general definition gives interjections
  "expressive rather than propositional meaning" (p. 1361) in a broad,
  non-propositional sense that covers conative *sh* and *hey*. The word
  *expressive*, or *emotive*, by itself does not support P08 = Y. The
  span must state evaluative or affective content for the specified
  use, or for a class whose stated content is evaluative or affective.
  Human proposition review checks every P08 cell against this guard.
- **P08 = N standard (v4).** N requires a source to exclude an
  evaluative or affective component for the specified use. Placement in
  a different descriptive class is not exclusion: *CGEL* pp. 557–558
  sets particularising attributives (*the main objection*) and modal
  attributives (*the probable result*) apart from expressive
  attributives (*the bloody tax inspector*), but never says that the
  first two lack stance. Such placements are recorded as *contrast*
  evidence. In the primary record the cell stays U; a predeclared
  sensitivity analysis codes contrast evidence as N. Silence is still
  U. A Tier B N for P08 isn't available, since stance has no corpus
  opportunity standard.
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
  excluding all such variants. A documented ordinary pronunciation is
  recorded as the descriptor P13D and leaves P13 unknown in the primary
  record. A declared sensitivity reads P13D = Y as P13 = N and reports how
  many IPA lines each cell rests on (decision call 3, Brett, 2026-11-05).
- **P14:** identifying glosses are descriptors of rows, not independently
  recovered sequential consequences. P14 is not a candidate target in
  its current form.
- No P16 is created merely to duplicate P11's negation component under a
  second number. The same observation may be a source in one projection
  and a target in another only under separately declared runs.

The governing schema for v4, including positive and negative standards,
units, roles in each grouping, admitted tiers, and corpus opportunity
standards, is `properties-v4.csv`; `properties.csv` is the v3 record and
does not govern. The yield audit codes under `properties-v4.csv`. If a property is repaired by splitting it,
the split, identifiers, and derivation from assertions are frozen before
production coding.

### Polarity, joint states and families (2026-11-05)

Adopted from the determinatives-as-nouns codebook
(`papers/queue/determinatives-as-nouns/planning/codebook.md`, sections
1, 4 and 6) at Brett's request ("make those fixes"). The audit behind
them is `notes/2026-11-05-complement-columns.md`.

- **One polarity.** Every property states a possibility. Y needs one
  admissible instance; N means never, held to the evidence rules of
  section 4. A universal stated negatively is reversed: P07 becomes
  P07D, *may contribute descriptive content*, which converts
  mechanically. Where conversion isn't mechanical, old cells become U:
  P11N becomes P11E, *may be interpreted inside the scope of host
  negation*, whose N (the wide reading is forced; Potts 2007, p. 172) is
  the expressive value.
- **x, not U.** A property that can't arise for a use is x, a status
  that is derived, never coded. P10S, P10M and P10R are x where the
  pattern is unavailable (P10A = N); P11E, P12S and P12I where the use
  has no host environment.
- **The POSITION family.** P01–P03 are three possibility claims over the
  positions a use occurs in, not a partition. N on all three is
  impossible. *Standalone only* (P01 Y, P02 N, P03 N) is a derived joint
  state. A statement that a use is always integrated or always
  standalone supports two cells as one proposition (dependence state:
  entailed).
- **Pairs give three states.** P12S with P12I, and P10S with P10R, give
  always, never, or either. There is no fourth state.
- **Contraries with gaps get their extension stated.** P09's N is
  "doesn't depict", which a non-iconic characterization supports; an
  iconic use that doesn't depict isn't thereby Y.
- **P06** records which disjunct supports Y. A conversion analysis is
  contrast evidence: U in the primary record, N in a predeclared
  sensitivity, as for P08.
- **Families.** Correlated properties stay separate unless one follows
  logically from the other, and are pooled by family in assignment
  (section 2). TRUTH_CONDITIONAL groups P07D and P11E: on Gutzmann's
  account (2013, pp. 32–37) both follow from use-conditional content
  not being truth-conditional.
- **Roots and word form.** Relatedness facts are drafted by rule in
  `morphology-facts-v4.csv` (`morphology_facts_v4.py`, string identity
  only, for Brett to approve): shared bases (*damn*, *bloody*,
  *bastard*, *bang*, *the*, *you*), the suffix *-ly*, and phrasal,
  reduplicated and sub-word forms. They take no m and link bearers (the
  four *damn* uses, the three *bloody* uses). They are never
  diagnostics or targets, they are pooled by base, and the tests run
  with and without them. Whether the uses of one form are one lexeme is
  not coded by rule (section 13).
- **Frames** (P10 patterns, P11 operators, P12's hosted environment)
  are proposed blind and frozen before Brett judges any cell. A frame
  needs a contrast within one use, and a property is split by frame
  only where some bearer's value changes across frames.

## 7. Coding and adjudication

- Coding is siloed by property. A coder sees one property description,
  shuffled bearers with controls interleaved, and a source packet for each
  bearer. It does not see other columns, assignments, item tiers, or
  rotation hypotheses. Bearers are described in plain words, never by
  identifiers that carry an analysis (DAMN_REACT, BASTARD_SUPP).
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

## 8. Reporting every candidate (replaces the v3 eligibility gate)

No target is selected, admitted, or labelled. For each grouping, every
candidate non-diagnostic target in section 5 is reported, in the order of
`properties-v4.csv`, in one table with no headline target. Reporting all
of them removes the post hoc selection the v3 gate guarded against,
without thresholds (Brett, 2026-11-04).

For every candidate the report gives the estimates and contrasts of
section 3 with their uncertainty, and these counts: applicable bearers;
post-concealment scorable cells, by outcome value and tier; item-specific
against inherited cells; distinct canonical propositions and testimony
units, and the largest proposition's share; control-tier and form-family
composition; effective member and nonmember mass. Counts are
post-concealment: raw known counts are shown only beside them.

Two conditions are arithmetic, not judgments:

- **Computable.** A target needs at least one reference outcome in each
  value among scorable cells; otherwise it is reported as not computable,
  with its counts.
- **Membership estimable.** If a grouping fails the estimability checks
  of section 2, its projections are reported as not interpretable, with
  their counts and the failed checks; no estimate is presented as a
  grouping result.

The discarded yield audit (section 12) is a **sealed census** (Brett,
2026-11-04): it codes the whole inventory, but investigators see only the
outputs listed in section 9, while item-level records are hashed and
sealed with the development artifacts. Production coding is coded fresh
and is the census for the study itself; before the reveal, investigators
receive only the same kind of sealed summary.

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
source–target associations. The sealed yield audit's script may emit only:
per-property counts (known cells by polarity and tier, item-specific
against inherited, N strength, distinct propositions and testimony units,
largest proposition share, control and family composition); per-grouping
counts for the estimability checks (rows with three or more visible
diagnostics, pairwise joint visibility); pass or fail for each
estimability check, with the identifier of each failed check. It
emits no item identities, no item-level values, no assignments, and no
cross-tabulation of one property against another. Its full output is
hashed and sealed, unopened before the registered analysis. If its items later enter production, they are
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
  the share of intermediate memberships are reported.
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

### Incorporated 2026-11-05

The polarity, joint-state, family and morphology rules (section 6), the
family pooling, derived-state and copies rules (section 2), the P11
concealment ruling (section 4), and plain-word bearer descriptions for
coders (section 7), after the determinatives-as-nouns codebook (Brett:
"make those fixes"; "what about the morphology columns, which include
roots. That would link bearers"). Round 7's results were produced
before these changes (`round7/RESULTS.md`). The 12-item target audit's
P10–P12 codings were made under the old standards; they are
development data and aren't converted.

### Incorporated into v4 (2026-11-04)

From the FREEZE-v3 evaluation and its addendum, accepted by Brett:
convergence assignment with graded membership for both groupings, no
gates, equal standing for absences (section 2); EXPRESSIVE assigned
over its meaning-field diagnostics rather than P08 alone; testimony
units, same-inclusion and entailed dependence states, and the strict
no-testimony sensitivity (section 4); disjoint P04/P05/P06, stated
non-occurrence as N with a strength field, and the P08 guard
(section 6); member-row and nonmember-row reporting (section 3). The
convergence check behind the section 2 rule is
`sim_convergence_assignment.py` with results in
`results-convergence-assignment.json` and `CONVERGENCE-CHECK.md`.

**Revisions after the Codex and Muse reviews (2026-11-04, Brett: "make
the revisions above (points 1–7). sealed.").** Reviews and manifest:
`../../reviews/freeze-v4-review-2026-11-04/`. Incorporated: the
record-reconstruction and projective-warrant claims kept apart, with
record-only outcome labels (sections 1 and 3); symmetric concealment
for reference rows and per-projection refit (section 2); estimability
checks for support, overlap, stability, and anchor compatibility, and a
fake-data rerun of the exact procedure required before any number is
approved (section 2); P08 contrast evidence U in the primary and N only
in a sensitivity (section 6); one governing schema, `properties-v4.csv`;
sign-types defined as expressions in conventional uses, the
supplementary epithet moved to EXPRESSIVE only, and the constructed
control dropped (section 5); the sealed census written into sections 8
and 9; Tier B able to supply N from opportunity-documented
non-occurrence where a property has an opportunity standard (Brett:
"Corpus evidence should be able to go beyond Ys"), with both gate
vectors published. P07 stays in both groupings' primary diagnostics,
against Muse's preference, because meaning is one of the converging
diagnostics; a no-P07 sensitivity covers both.

**Still open.** From the deeper v3 triage: the documentation-only
diagnostic, the proposition-review load estimate, and strata reporting.
From Muse's review: testimony weighting that splits one unit's weight
across its cells would discount absences, which are mostly stated for
classes; alternatives (a cap per cell rather than a split) need testing
in Round 7 before the weighting is approved. Round 7 builds the harness
now and calibrates only after the measurement schema is approved.

**Bearer sets (2026-11-04, Brett: "make it so").** v1 is restricted to
INTJ and EXPRESSIVE. EXPRESSIVE gets 12 rows from its own literature
(Potts 2007; Ljung 2011 pp. 33–35), each also described in a grammar,
with same-slot controls taken from the same grammar passages, in
`items-v4.csv`; P08 = N may rest on a source's stated contrast with
expressive items (section 6); each perspective's set has a stated selection rule, a
floor of 25 applicable bearers, and member/nonmember balance, and the
single-word rows form a planned shared core (section 5).

**Evidence order (2026-11-04, Brett).** Tier A literature first; the
yield audit counts what it leaves empty; targeted Tier B CABNC searches
for presence cells only; an analyst tier only for what is still empty
(section 4). Jespersen's *Negation* (1917) covers a negative use of
*the devil*, a different use from wh-emphasis; it's a candidate row for a
later round, not v1.

**Next development step.** The discarded yield audit in
`yield-audit/DESIGN.md`, run under the v4 definitions before Round 7,
to learn whether section 8 can admit any shared target.

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

These tables are generated from `items.csv` and `properties.csv`. If a table and its CSV disagree, the CSV governs and the disagreement must be logged as a deviation. **v4:** the governing inventory is `items-v4.csv`, which adds the 11 EXPRESSIVE rows listed below to the 35 shown here and restricts every row's rotations to INTJ and EXPRESSIVE (HOWAREYOU, the phrasal and sub-word additions, and the supplementary epithet to EXPRESSIVE only). The full mirror is regenerated at approval.

| ID | Use | Tier | Sources | Rotations |
|---|---|---|---|---|
| BASTARD_SUPP | He's taken my chair again, the bastard | expr-core | CGEL 1413; Ljung 34 | EXPR |
| YOU_BASTARD | You bastard! | expr-core | CGEL 353 n. 14 | EXPR |
| BLOODY_INTENS | It's bloody marvellous | expr-core | CGEL 584; Ljung 33 | INTJ;EXPR |
| DAMN_DEGREE | They drove damn fast | expr-core | CGEL 584–585; Ljung 33 | INTJ;EXPR |
| FUCKING_PRENOM | a fucking investigation | expr-core | CGEL 558 | INTJ;EXPR |
| BLOODY_INFIX | abso-bloody-lutely | expr-core | Quirk 1584; Ljung 34 | EXPR |
| THE_HELL_WH | What the hell is she trying to do? | expr-core | CGEL 1087; Ljung 34 | EXPR |
| VERY_INTENS | They drove very fast | expr-control | CGEL 584 | INTJ;EXPR |
| EXACTLY_WH | What exactly do you mean? | expr-control | CGEL 1087 | INTJ;EXPR |
| MAIN_PRENOM | the main objection | expr-control | CGEL 558 | INTJ;EXPR |
| PROBABLE_PRENOM | the probable result | expr-control | CGEL 557 | INTJ;EXPR |

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
v2 estimand and membership experiments as incorporated, the amended
target architecture's principle of no privileged primaries (the
eligibility function itself is since replaced by reporting every
candidate, section 8), leave-one-source-out as secondary, the
FREEZE-v3 evaluation, and the assignment principle that membership is
graded convergence with no tally and no decisive property. Still
needed before this draft can freeze:

0. The section 2 convergence specification (number of classes,
   absence weights by strength, testimony weighting), after the yield
   audit and Round 7, and the deeper v3 triage decisions listed in
   section 12.

1. Numbers for the estimability checks in section 2 (support, overlap,
   stability, anchor compatibility), after Round 7.
2. (Retired: outcome labels and their thresholds, and the eligibility
   gate, are replaced by reporting every candidate with uncertainty,
   sections 3 and 8.)
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

8. The polarity recode of 2026-11-05 (section 6) and the rules in
   `morphology-facts-v4.csv`, including the function-word bases *the*
   and *you*.
9. Whether an independent adjacent turn counts as a host for P11E and
   P12S. `properties-v4.csv` lists it as a host relation; section 2 had
   treated standalone uses as hostless.
10. Whether the uses of one form (*damn*, *bloody*, *bastard*, *bang*)
    are one lexeme. Until decided, the analysis runs both ways.
11. Forks from the determinatives project, not yet designed: holding
    out whole rows or form families rather than single cells; a
    property frame drawn from a source no grouping chose, balanced
    across perspectives; an *accepted* status for cells all model
    families agree on, audited by a stratified random gold sample.
12. Whether a class-level "never" statement (Potts 2007, p. 172;
    Gutzmann 2013, p. 37) supports P11E = N for the members it names.
    Under section 4's inheritance rules it does, as one testimony unit;
    under P11E the item-level evidence comes mostly from Y cells on
    controls.

Until those items are settled, this is a development protocol. It does
not authorize production coding.
