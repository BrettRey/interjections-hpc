# Discarded target-evidence audit: design

Status: run 2026-11-04 as designed; report in `AUDIT.md`. Date: 2026-11-04.
Parent protocol: `../FREEZE-v2.md`.

## Purpose

Determine whether the held literature contains enough usable evidence for
the proposed primary targets, before a freeze asks those targets to bear
confirmatory weight. The audit classifies the *availability and structure
of evidence*. It does not estimate any source–target association, does not
run a lesion, and produces no cell that may be imported into the study
matrix. All sampled item–property pairs are recoded fresh if production
proceeds.

## Targets and sample

Three property silos, audited separately:

1. **Hosted P12:** prosodic separation when the sign occurs with a
   clausal or nominal host. A standalone boundary by itself does not
   count as the target observation. Every assertion also records the
   strength it supports: an attested separated occurrence does not by
   itself establish characteristic separation.
2. **P10 patterns and dimensions:** repetition-like evidence is first
   classified by pattern: adjacent repetition of the specified use;
   distributed recurrence across an utterance or discourse; lengthening;
   or lexicalized reduplication. These are recorded separately and never
   pooled in the audit. Distributed examples also record the positions
   involved (the specified use, another use/row, mixed, or unclear).
   Within each pattern, availability is recorded separately for
   strengthening the same contribution, multiplying depicted events,
   redundancy, and unavailability. Potts-style accumulated occurrences
   of *damn* across standalone and prenominal positions are distributed
   recurrence across uses unless the passage shows adjacent repetition
   of the specified use. The confirmatory target is chosen only after
   availability is reported by both pattern and effect dimension.
3. **P11 under negation only:** whether a specified contribution
   survives or is interpreted inside negation of a host proposition.
   Each assertion names the contribution being assessed and the host
   relationship: integrated inside the relevant construction, an
   external co-utterance accompanying a negative clause, or an
   independent adjacent turn. These environments are recorded separately
   and do not silently count as one target. Merely finding no suitable
   hosted evidence is `SILENCE` or another availability result.
   `INAPPLICABLE` requires a separate item–target eligibility record and
   human checking of every such judgment.

For every target, each assertion identifies the strength of proposition
it supports: attested possibility, recurrent or characteristic behaviour,
or a categorical/default claim. The audit preserves those strengths. It
does not convert possibility into characteristic behaviour, or
“can survive negation” into “must survive negation”.

The starting sample is `sample.csv`: twelve sign-types selected by
stratum before results are seen (canonical reactions; the *damn* family
and integrated expressive; a depictive case; interactional responses;
lexical controls). It is a purposive feasibility sample, not a sample
from a population and not a basis for estimating an English-wide rate.

## Retrieval

Packet builder v3 must be property-specific and versioned. For every
item–property pair it records the exact queries, source files searched,
builder version, packet hash, and whether retrieval was form-based,
behaviour/concept-based, or section-targeted.

Starting concept families, to be frozen in the builder before execution:

- **P12:** intonation unit, intonationally separate/integrated, pitch
  contour, prosodic boundary, set off, interpolation, appendage,
  detached, supplement/ation, host/anchor.
- **P10:** repeat, repeated, repetition, reduplication, iterative,
  multiple events, intensification/strengthening, prolonged/reiterated.
- **P11-negation:** negation, negative, not + host, scope, denied,
  cancellation, survival under negation, scope-bearing operator.

Candidate passages are relevance-ranked and deduplicated as in packet
v2, but item-form evidence is separated from class/context evidence.
Every excerpt retains filename, markdown line, nearest section, and a
publication page where the held markdown permits it to be recovered.
Bibliography and download-header material is excluded by rule and any
residual inclusion is a retrieval defect to count.

## Audit output for each item–target unit

Coders return evidence descriptors, not a study cell. Required fields
are specified in `assertion-schema.json`. The classification unit is an
item–target proposition: for P10, one pattern-by-effect-dimension
combination; for P11, one contribution-by-host-relationship combination;
for P12, one claim-strength level. The audit uses exactly one
availability class per such unit:

| Class | Meaning |
|---|---|
| `ITEM-DIRECT` | at least one usable item-specific assertion about the specified use/environment |
| `CLASS-INHERITED` | usable evidence only through a class assertion explicitly including the item |
| `ADJACENT-ONLY` | related behaviour is documented, but not the target proposition/environment |
| `CONFLICT` | usable assertions support incompatible values or analyses |
| `SILENCE` | packets were searched adequately and no relevant assertion was found |
| `RETRIEVAL-FAILURE-SUSPECTED` | an expected source/section is absent, malformed, or visibly missed by retrieval |
| `INAPPLICABLE` | the frozen target environment cannot apply to this use |

For each assertion, record at minimum: source and stable location;
assertion, proposition, and observation identifiers; verbatim span(s)
with roles; source wording; supported value/dimension and supported
claim strength; item-specific versus inherited support; exact class if
inherited; quantifier/modality; language/variety; use slice;
construction and environment; for P10, repetition pattern and positions
involved; for P11, contribution assessed and host relationship; cited
or repeated lineage where determinable; coder and model provenance;
adjudication state.

Record source–target evidential dependence explicitly. For every
proposed source proposition that could later support assignment, classify
its relation to the target proposition as distinct observations,
distinct propositions in a shared passage, the same observation, or
inseparable support. A shared passage alone is not disqualifying. The
production question is whether the source value can be supported without
relying on the target observation.

Every `INAPPLICABLE` result requires a separate eligibility record
stating the frozen target environment, why it cannot apply to the
specified use, and the human checker who approved removing the unit from
the denominator. Unchecked coder-proposed inapplicability remains
provisional and is reported separately.

The audit report aggregates availability classes and assertion counts
only. It must not report target-by-source associations. Supported values
remain in the sealed audit artifact for semantic checking but are not
used to choose projections by expected direction.

## Coding and checking

- Property-siloed packets and prompts; no category labels or expected
  outcomes in coder instructions.
- Multiple quotation spans are allowed only with separate span roles.
- Mechanical validation covers every output: identifiers, values,
  continuous exact quotation, span roles, quote location, and the
  source wording appearing in a cited span.
- Semantic review covers every distinct assertion classified
  `ITEM-DIRECT` or `CLASS-INHERITED`, every `CONFLICT`, and a frozen
  sample of `ADJACENT-ONLY` and `SILENCE` results. Review checks language
  and variety before linguistic interpretation; the pilot-3 Siwu example
  is the calibration failure.
- Agreement is reported with marginals. Kappa is a diagnostic only and
  cannot rescue a target with inadequate coverage or assertion depth.

## Outputs that inform the freeze

For each target, the audit must produce:

- counts in each availability class, overall and by sample stratum;
- for P10, those counts separately by repetition pattern and effect
  dimension; for P11, separately by contribution and host relationship;
  for P12, separately by supported claim strength;
- number of distinct assertions, propositions, observations, and
  assertion clusters;
- item-specific versus inherited proportions;
- counts of distinct versus shared-observation source–target support;
- outcome-class support without cross-tabulating against sources;
- all proposed eligibility removals and their human-check status;
- number of assertions requiring human semantic review;
- retrieval-failure rate and any source families systematically missed;
- recommended minimum evidence-gate components for a later freeze
  decision, with the raw counts needed for Brett to set them.

Before production, Brett must freeze the conversion from preserved
assertion strengths and patterns to each cell value. The audit itself
does not choose a P10 pattern, collapse P11 host relationships, or turn
attested possibility into characteristic behaviour.

The audit does not itself set pass/fail thresholds. Brett sets those
after seeing whether scarcity is silence, retrieval failure, conflict,
or inapplicability. A target can proceed, be narrowed, be redesigned,
or be abandoned; none of those outcomes alters another target's status.

## Firewall

This audit is development data under `FREEZE-v2.md` section 9. It is
discarded for production values. No lesion, predictor comparison,
category assignment across a sampled row, or source–target association
may be computed from it. If an item later enters production, its targets
are coded again from production packets by coders who do not receive the
audit output.
