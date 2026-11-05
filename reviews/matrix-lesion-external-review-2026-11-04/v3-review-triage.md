# Triage: external review of FREEZE-v3 and Round 6 (2026-11-04)

Supersession note (2026-11-04): the deeper revised review triaged in
`v3-deeper-review-triage.md` supersedes this memo's treatment of
0.03/0.01 materiality labels, human-review scope, and Round 7 as the
immediate next step. Read the deeper triage for current
recommendations.

Review triaged: pasted model review received 2026-11-04, route not
recorded. Checked against `FREEZE-v3.md`, `SIMULATION.md`,
`sim_round6_eligibility.py`, `results-round6-eligibility.json`,
`lesion.py`, `items.csv`, and the corrected target-evidence audit.
Treated as recommendations, not Brett approval.

## Bottom line

Adopt the direction, adapt the implementation, defer the approvals.

The review is right that the v3 architecture no longer needs another
redesign. It is also right that one larger falsification-oriented
simulation round should precede approval of the numeric gate. It
overstates three things: Round 6 did not test the exact v3 gate, its
computation estimate needs a targeted condition list, and human
review of propositions behind *admitted* targets is sequenced too
late. Materiality values, the checker commitment, the P11 operator,
and the formal v1 scope remain Brett decisions.

## Verified against the local record

- The central architecture the review praises is in `FREEZE-v3.md`
  sections 1, 2, 4, and 8: every adequately evidenced
  non-assignment target is admitted by one frozen function,
  per-projection gains are primary, and the property-weighted family
  mean is secondary.
- The mechanical link between at least 4 member and 4 nonmember
  scorable cells and M2 is correct. Section 2 requires at least 3
  same-assignment reference outcomes, so a group of 4 leaves exactly
  3 references under exhaustive one-cell concealment.
- Round 6 used 25 datasets per world and knownness regime. Its
  evidence layer used item-direct probability 0.5 and three shared
  propositions per property. It compared gates A, B, and C in
  `sim_round6_eligibility.py`; none is exactly the section 8 gate.
  Round 6 therefore cannot calibrate the exact v3 numbers.
- The null wording needs the reviewer's caution. In the B gate JSON,
  null uniform INTJ has median property-weighted gain -0.026 with
  4.3% of admitted datasets at or above 0.03; scarce-negative INTJ
  has 12.5% on a tiny admitted denominator. "Centred" is too strong
  on 25 datasets.
- The log-loss conversion is correct. If gain is
  loss(M0) - loss(M2), then exp(gain) is the ratio of geometric-mean
  probabilities assigned to observed outcomes: 0.01 gives 1.010,
  0.03 gives 1.030, 0.05 gives 1.051, and 0.10 gives 1.105.
- One Round 6 null-uniform dataset across both rotations and all
  candidate targets took 0.47 s in a local benchmark. At that rate,
  1,000 datasets for one condition take about 8 minutes serially and
  12 such conditions about 1.6 hours, before new Round 7 machinery.
  Manageable, especially in parallel, but not a negligible rerun.
- The one-third single-form-family clause is almost inert on the
  current inventory. Only *damn* (3 rows) and *bang* (2) share a
  family, while the gate already requires at least 18 scorable
  cells. Keep it as a guard for extensions, but do not count it as
  active calibration evidence. Tier representation does more work.

## Adopt

1. **No further architectural redesign before Round 7.** The fixed
   inventory estimand, source-complete lesion, M0/M1/M2 contrasts,
   proposition-level concealment, automatic target admission, and
   cross-inquiry restriction to shared admitted targets stay.
2. **A larger Round 7 as falsification, not threshold shopping.** Use
   it to ask whether the fixed proposed gate behaves embarrassingly
   under plausible bad worlds. Do not tune numbers to maximize power
   and then present the same run as calibration.
3. **Multinomial clarification.** If a frozen target retains more
   than two outcome classes, every retained class should meet the
   per-class floors. Current section 8 language ("at least two
   classes") would allow an effectively uninterpretable third class.
   If P10 and P11 remain separate binary dimensions, state that and
   remove the ambiguity.
4. **Retention as a secondary descriptive ratio.** Report
   retention = gain(M2) / gain(M1) only when direct-source gain is
   materially positive, alongside raw losses and compression cost.
   Raw losses stay authoritative. No retention success gate.
5. **Austere pre-reveal gate output.** State an explicit allowlist:
   PASS or FAIL by grouping and candidate target, plus failed clause
   identifiers for failures. No item identities, assignment lists, or
   target-by-assignment cross-tabulations before reveal. Full gate
   vectors can be sealed and published with the analysis.

## Adapt

1. **Round 7 must implement the exact section 8 gate.** Gates A/B/C
   are useful sensitivities, but the primary simulation object should
   be the exact draft function, including applicable-Bearer [REDACTED]
   at least one scorable control, form-family share, and
   post-concealment counts. Where fake data cannot represent a
   clause, say so rather than silently dropping it.
2. **Couple copied evidence to coded values.** Round 6 labels cells
   item-direct or inherited independently of the generated target
   values. Round 7 needs worlds in which one or two canonical
   propositions actually generate many coded target values, at low
   direct rates (for example 0.5, 0.25, 0.1, and 0 where coherent).
   Otherwise concentration criteria are tested cosmetically.
3. **Separate documentation mechanisms.** Include null worlds with
   scarce negatives, profile-dependent knownness based on visible
   assignment-like sources, target-value-dependent knownness, and
   both together. Add several source-target shared-observation
   blocking rates, not only P07 blocked on half the P08/P09 rows.
4. **Prespecify Round 7 outputs and embarrassment criteria.** At
   minimum: admission rate by target and rotation, empty-family
   rate, per-projection gain quantiles conditional on admission,
   material-label rate at 0.03 under null and adversarial worlds,
   any-material-projection rate within a family, aggregate gain
   quantiles, compression cost and retention where defined, and
   resolved coverage. Structured worlds also need admission yield,
   so an apparently safe gate that admits almost nothing is visible.
5. **Use the common 0.03/0.01 scale only as proposed draft values.**
   The geometric interpretation makes them intelligible, and a
   common scale is cleaner than projection-specific cutoffs. But
   section 3 needs an explicit small-gain report for 0.01 to 0.03
   that is neither "supported" nor "insufficient information" when
   the gate passed and coding sensitivity is narrow.
6. **Move 100% proposition review before the hash and gate.** Brett
   cannot review propositions behind admitted targets before
   admission exists, and post-gate semantic corrections would break
   the locked record. The workable form is human review, before
   hashing, of every distinct canonical proposition that supports a
   consensus non-U cell in any candidate target, plus disagreements
   and proposed negatives within each silo. Use a packet view that
   hides other columns, assignments, tiers, and expected direction.
   The load must be estimated and explicitly accepted; the audit
   sample alone generated 21 canonical propositions over 36 pairs,
   so trivial load cannot be assumed for full production.

## Reject

- **The claim that the 50% proposition ceiling by itself prevents
  the P12 pathology.** Corrected hosted P12 also fails through zero
  item-direct support and contested proposition lineages. A ceiling
  just below 50% could still let one copied proposition dominate a
  larger production target. Keep the ceiling provisionally, with
  cluster sensitivity, but do not treat it as independently proven.
- **Post-admission human proposition review as the main semantic
  control.** It is too late in the firewall sequence. Semantic
  effective fields must settle before the record is hashed and the
  locked gate runs.
- **Any suggestion that Round 6 approves the exact numeric gate.**
  It supports the architecture and shows no obvious aggregate bias
  in benign simulated evidence. It does not estimate the exact
  gate's operating behaviour.

## Defer to Brett

1. Approve the section 8 numeric thresholds after Round 7, including
   keeping the largest-proposition ceiling at 50%.
2. Approve a common materiality rule: supported at 0.03 nats per
   cell or above, negligible at 0.01 or below, and an explicit small
   range between them.
3. Confirm Brett Reynolds as the named human checker for every
   proposed INAPPLICABLE and not-a-bearer exclusion, and decide the
   actual proposition-review commitment (all candidate-target
   canonical propositions, or a named stratified sample if the load
   estimate makes 100% unreasonable).
4. Freeze negation as the primary P11 operator. It is already the
   draft default in section 6, and the eligibility architecture
   means a weak production record simply yields no admitted P11
   projection.
5. Restrict v1 explicitly to INTJ and EXPRESSIVE on the sign-type
   matrix. SUPPLEMENT already requires a separate linked table and
   DEPICTIVE is already deferred; the remaining decision is whether
   to remove both from v1 candidate scope rather than carry them as
   draft candidates.

## Prioritized punch list

1. Write a short Round 7 specification before coding it: exact gate,
   condition list, dataset counts, seeds, metrics, and what patterns
   would count as embarrassing enough to change a number.
2. Implement `sim_round7.py` with unit tests for the exact gate on
   hand-built records, including one-cell reference depletion and
   every retained multinomial class.
3. Run Round 7 with 1,000 datasets for each important null and
   adversarial condition, and enough structured-world datasets to
   estimate admission yield. Record runtime and parallelization.
4. Update `SIMULATION.md` with conditional and familywise results,
   not medians alone.
5. Amend `FREEZE-v3.md` only for items Brett approves: multinomial
   floors, materiality labels and values, retention ratio, gate
   output allowlist, proposition-review sequence and load, P11
   operator, and v1 scope.
6. After those approvals, complete the remaining checklist items,
   commit the signed freeze, and register the same version before
   production coding.

No change to `FREEZE-v3.md`, the numeric gate, or study scope is made
by this triage alone.
