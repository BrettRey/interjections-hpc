# Triage: deeper external review of FREEZE-v3 (2026-11-04)

Review triaged: pasted revised model review received 2026-11-04,
route not recorded. It withdraws part of the same reviewer's earlier
approval of the 0.03/0.01 thresholds and human-review commitment.
Checked against `FREEZE-v3.md`, `SIMULATION.md`, `lesion.py`,
`sim_round5.py`, `sim_round6_eligibility.py`, `items.csv`,
`properties.csv`, `inquiry-relative-categories.tex`, and the prior
triage in `v3-review-triage.md`. This memo supersedes that triage on
materiality, human-review scope and sequencing, and the claim that
Round 7 is the immediate next step. Its other recommendations stand
unless repeated or qualified below.

## Bottom line

Adopt the central correction, adapt several proposed remedies, and
defer every remaining approval.

The lesion architecture is defensible as a measure of reconstruction
of documented cells in a frozen coding. The current outcome language
lets that exact descriptive result sound like projective warrant over
the whole declared inventory. Those are different claims. The
protocol should separate them before it freezes measurement units,
simulation conditions, human-review load, or numeric thresholds.

This does not make lesion success evidentially inert. Where source
and target observations are semantically valid and distinguishable,
and documentation sensitivity does not explain the result away,
recovering concealed documented facts is evidence for a local
projective claim about the declared bearers. It is conditional,
graded evidence, not an automatic category verdict and not evidence
about English at large.

## Independent numeric verification

Both numerical counterexamples reproduce under the documented
Laplace-smoothed M0/M2 and exhaustive one-cell rules. Verification
script used for this triage: `/tmp/verify_review_numbers.py`.

1. **Null material-looking gains.** Exact enumeration over group
   outcome counts, with target Bernoulli(0.5) independent of group
   and conditioning on at least four outcomes in each class, gives
   P(gain at least 0.03) = 0.0970 for 18 items split 9/9, 0.0663
   for 24 split 12/12, and 0.0497 for 33 split 16/17. These match
   the review's Monte Carlo values (0.096, 0.065, 0.049). Mean null
   gains are -0.0205, -0.0168, and -0.0131.
2. **Selective documentation example.** The documented table
   (members 8Y/2N, nonmembers 2Y/8N) gives +0.1462 nats per cell.
   The stipulated complete table (members 9Y/7N, nonmembers 9Y/8N)
   gives -0.0284. These match the review's +0.146 and -0.028.

The first result does not make a realized fixed-inventory gain
uncertain as arithmetic. It shows that the same magnitude is not, by
itself, strong evidence against an accidental configuration. The
second shows that documented-cell gain and complete-inventory gain
are different quantities under outcome-dependent documentation.

## Claim architecture to settle before Round 7

FREEZE-v3 section 1 says results concern the declared inventory
under stated information losses, while sections 2, 3, and 8 score
only known, post-concealment scorable target cells. Section 10 lists
selective documentation as a threat. The review is right that the
qualification must enter the estimand and outcome labels, not remain
a limitation paragraph.

Recommended separation for Brett's decision:

- **Record-reconstruction claim.** For documented, scorable cells in
  the frozen coding, grouping G recovers concealed target T from
  permitted sources with a stated gain over M0 and stated estimator
  contrasts. This is exact for the frozen record, subject to coding
  sensitivity.
- **Projective-warrant claim.** For the declared bearers, including
  bearers whose target is currently U, observing the permitted
  sources warrants an expectation about T. This requires more than
  the recorded gain: semantically valid propositions,
  distinguishable source and target observations, comparator and
  documentation diagnostics, and robustness to defensible recodings.
- **World-side claim.** No causal order, maintenance, control, or
  category standing in general follows from either result without
  separate evidence. Current v3 language already avoids a global
  category verdict and should keep doing so.

Under that separation, "supported gain" in section 3 is too broad.
A threshold such as 0.03 may label the size of a documented
reconstruction gain. It should not by itself label projective
warrant. The earlier triage recommendation to use 0.03 and 0.01 as
supported/negligible decision values is withdrawn. They can remain
proposed descriptive reference bands pending Brett's judgment.

## Adopt

1. **Make documented-cell scope explicit in the estimand.** State in
   sections 1 to 3 that primary gains average over documented
   scorable cells only. Any extension to currently undocumented
   cells in the same inventory is a further projective claim with
   its own warrant conditions.
2. **No automatic evidential verdict at 0.03.** Keep continuous
   gains primary. Do not select a threshold to manufacture a
   conventional false-positive rate. Null and adversarial
   simulations report operating behaviour, including familywise
   material-looking gains, without becoming approval criteria.
3. **Freeze the measurement schema before final gate calibration.**
   Outcome alphabets, P10 pattern-by-effect units, P11
   contribution-by-host units, negative standards, applicability
   states, assignment-source representations, and derived columns
   must be fixed before candidate counts and class floors have a
   stable meaning. Section 6 currently lists these as repairs.
4. **Include assignment-source propositions in human-review scope.**
   P07 is a source for both INTJ and EXPRESSIVE and could otherwise
   escape a target-only proposition review. Source-target dependence
   judgments also need review because they determine concealment.
5. **Add an independent-observation sensitivity.** Estimate
   reference associations when shared source-target observations are
   concealed or excluded under a frozen rule, and report it beside
   the full-record result. Item-specific restriction is not the same
   sensitivity: an item-specific target can share an observation
   with its source, and an inherited target can be distinct.
6. **Distinguish plurality from comparative advantage.** Successful
   INTJ and EXPRESSIVE projections on different targets can support
   a plurality of useful inquiry-relative projections. Only a
   shared-target, common-denominator comparison supports a claim
   that one grouping predicts that target better. Reapply the
   computation gate to the common evaluation set.
7. **Rename the retention ratio.** Call it a predictive-performance
   ratio. It compares specified estimators; it is not a proportion
   of information retained.

## Adapt

1. **Mandatory comparators need exact estimators.** The review is
   right that Round 5 exposes M1 weakness: null d10 is -0.097 in
   `SIMULATION.md`, so M2 matching or beating this M1 is a narrow
   estimator result. Make an unthresholded convergence-score
   predictor and simple source predictors mandatory secondary
   comparators, but freeze their forms in the measurement schema.
   A theoretically chosen "most relevant diagnostic" is not always
   unique across automatically admitted targets. A cleaner default
   is one predeclared canonical source per grouping, plus optionally
   all single-source categorical predictors reported without picking
   a winner.
2. **Add a documentation-only diagnostic with a narrow meaning.**
   Use only permitted-source knownness indicators (never target
   knownness) to predict documented target values. This can reveal
   documentation structure in the descriptive record. It does not
   prove that documentation caused the category gain, because
   knownness can depend on the source values themselves.
3. **Consider symmetric proposition concealment, not only a
   sensitivity.** V3 conceals shared observations for the target
   row, while reference rows remain intact. If a reference row's
   assignment uses a source observation that also supports its
   target, the learned category-target association can itself be
   duplicated evidence. The full-record estimator can remain the
   reconstruction primary, but Brett should decide whether the
   projective interpretation requires the symmetric version.
4. **Round 7 can be built in two stages.** Implement and unit-test
   the harness now, including underlying-versus-documented scoring
   and exact gate logic. Run the final calibration only after the
   measurement schema fixes candidate units. A preliminary run on
   the current binary abstraction is a code check, not gate
   calibration.
5. **Human review needs a workload estimate before a 100 percent
   commitment.** Assignment sources plus candidate targets cover
   nearly every substantive property. Estimate distinct canonical
   propositions and dependence judgments from existing discarded
   material and a timed sample before deciding between comprehensive
   review and a predeclared risk-stratified design. Review remains
   pre-hash, packet-siloed, and blind to assignments and outcomes.
6. **Report performance by inventory stratum.** Full-inventory gain
   can be dominated by easy canonical-versus-control contrasts.
   Add fixed gain slices by the already declared analyst tiers
   (core, boundary, control) as sensitivity reporting. A separate
   boundary-only estimator is a different estimand and should not
   replace the declared result.
7. **Define the row bearer once.** The inquiry draft defines a
   sign-type as an identifiable expression in a conventional use, so
   "sign-type" is not necessarily the wrong term. FREEZE should
   import that definition explicitly and avoid wording that suggests
   33 lexemes.

## Reject or qualify

- **Reject a binary split in which reconstruction success is
  evidentially empty.** The review does not quite say this, but the
  protocol should not adopt that reading. Concealed documented facts
  are genuine test cases for the prediction procedure. Their warrant
  is scoped and conditional, not zero.
- **Reject null-crossing frequency as an approval criterion.** The
  verified 5 to 10 percent rates are calibration facts. The study
  is not a conventional population hypothesis test, and its actual
  inventory is fixed. They argue against automatic labels, not for
  tuning materiality to an arbitrary rate.
- **Reject unconditional comprehensive human review until load is
  known.** Comprehensive review may be the right design, but neither
  the reviewer nor this triage can commit Brett to it.
- **Qualify "freeze the schema before Round 7."** Freeze it before
  the calibration run whose results will be used to approve gate
  numbers. Harness construction and small dry runs can proceed.

## Defer to Brett

1. The claim architecture above, including what additional
   conditions convert a documented reconstruction result into a
   projective-warrant claim within the declared inventory.
2. Whether symmetric independent-observation concealment is a
   sensitivity or part of the primary projective estimator.
3. Final measurement schema: property splits, P10 units, P11 units
   and negation, negative standards, applicability, and assignment
   representations after any P01 split.
4. Numeric eligibility thresholds after the final Round 7.
5. Whether 0.03 and 0.01 remain descriptive reference bands, and the
   exact outcome vocabulary attached to them.
6. Human checker identity and actual review commitment after a load
   estimate.
7. Formal v1 restriction to INTJ and EXPRESSIVE, with SUPPLEMENT
   and DEPICTIVE outside v1 rather than draft candidates.

## Revised sequence

1. Decide the record-reconstruction versus projective-warrant claim
   architecture and outcome vocabulary.
2. Draft and approve the measurement schema, including canonical
   proposition and dependence effective fields.
3. Specify exact comparator estimators, documentation diagnostics,
   common-set cross-inquiry gate, and independent-observation rule.
4. Estimate human-review load from discarded material and decide
   the checker commitment.
5. Build the Round 7 harness with unit tests. Dry-run it on the
   current binary abstraction only as a code and metric check.
6. Run final Round 7 on the frozen schema. Report documented-record
   recovery and underlying-world recovery separately, plus empty
   families, admission yield, per-projection and familywise gains,
   documentation-only and simple-source baselines, and compression
   contrasts.
7. Create the next freeze draft from approved decisions, then sign,
   commit, and register before production coding.

No change to `FREEZE-v3.md`, the gate, thresholds, scope, or checker
commitment is made by this triage alone.
