# Triage: target-eligibility proposal for the lesion study (2026-11-04)

Proposal triaged: pasted model proposal received 2026-11-04 (drop
P10, P11, P12 as privileged primaries; freeze an evidence-only
eligibility rule over the full property inventory; every passing
non-assignment property becomes a primary reconstruction target;
report hierarchical and per-property gains; leave-one-source-out as
secondary; replace narrow audit with coverage census; retire
"confirmatory"). Checked against `FREEZE-v2.md`, `properties.csv`,
`items.csv`, corrected `target-audit/AUDIT.md`, and the
projectibility-first framework. Treated as a proposal, not yet
Brett's decision.

## Bottom line

Adapt. Adopt the architecture. Do not adopt it verbatim.

Freezing an eligibility rule instead of privileged properties is the
right response to the corrected audit, and it fits both the
fixed-inventory estimand and `FREEZE-v2.md` section 8, which already
requires per-projection evidence gates. Retiring "confirmatory" for
"prespecified primary reconstruction analysis" is already adopted in
the corrected report and should extend to the freeze.

Four amendments are material. Without them the proposal reintroduces,
in new form, the selection and interpretation problems it removes.

## Adopt

1. **No privileged primary property.** P10 (one mixed-position Potts
   proposition, one pattern-unspecified Quirk proposition, no
   depictive contrast), P11 (one inherited CGEL proposition, no
   within-target contrast), and hosted P12 (no item-specific
   evidence, contested inherited lineages) stay in the matrix as
   ordinary candidates. None is frozen as primary. The corrected
   audit numbers stand as the calibration example of "too shallow".
2. **Eligibility as a frozen function, admission of all passers.**
   Criteria along the proposed dimensions (applicable bearers, known
   outcomes per class, item-direct count, distinct propositions,
   concentration, assignment non-overlap) match `FREEZE-v2.md`
   section 8 minimums. No post-audit picking among passers.
3. **Per-property gains plus a distribution, compression cost
   explicit.** Property-specific loss(M0) minus loss(M2) and
   loss(M2) minus loss(M1) remain the interpretable units. An
   aggregate consisting of one property must be visible as such.
4. **Assignment properties excluded from membership-inferred
   primaries; leave-one-source-out secondary.** Consistent with the
   inferred versus retained distinction already in `FREEZE-v2.md`.
5. **Retire "confirmatory target".** Primary means: targets passing a
   frozen evidence gate, analysed under a prespecified reconstruction
   analysis, with audit exposure documented.

## Adapt (four material amendments)

### A. No separate cheap census. Fold eligibility into production coding behind the locked gate script.

The proposed census asks for applicability, outcome counts,
item-direct versus inherited split, canonical proposition counts, and
concentration per property. That is production assertion coding in
all but name: roughly 33 bearers by up to 14 properties, with
use-identity, environment, strength, and dependence checks of
exactly the kind whose absence produced the Stange and Heine
failures. A cheaper pass would inflate counts with label errors.

A separate census also weakens the firewall. Investigators would
inspect per-property outcome counts before freezing thresholds,
which is selection with extra steps. `FREEZE-v2.md` section 9 already
supplies the better mechanism: code the full matrix, hash it, and let
a locked gate script emit only gate summaries. Amend as follows:

- Freeze eligibility thresholds numerically before production coding,
  calibrated from the corrected P10 to P12 audit (what failure looks
  like) and from a new fake-data run of the full gate-plus-aggregate
  pipeline under null, hub, and copied-assertion worlds.
- Production-code the full inventory once, assertion-first.
- Locked script applies the eligibility function, admits targets,
  and reports counts. Investigators do not browse outcome tables to
  tune thresholds. Any threshold change after gate output is a
  deviation, logged, with analyses after it exploratory.

"Evidence-only" also needs exact language. Outcome-class counts are
outcome marginals. Inspecting marginals through a locked script is
defensible and already frozen in principle. Calling it outcome-blind
without qualification overstates it. The firewall claim is: no
source-target association, assignment, or gain is inspected before
the gate locks.

### B. One predeclared primary summary, and no single usefulness score as the headline claim.

Reporting cell-weighted gain, property-weighted gain, per-property
gains, and a multilevel estimate, then narrating whichever impresses,
restores the researcher degrees of freedom the gate removed.
Predeclare one primary summary; the rest are secondary and labelled.

Recommended structure, consistent with `FREEZE-v2.md` section 1 ("No
result is a verdict on a category's overall standing. Each projection
can succeed, fail, or lack enough evidence independently") and with
projectibility-first discipline (the projective claim is the bearer;
categories are projectible derivatively through families of claims):

- Primary: per-projection gains (grouping by eligible property),
  each with its declaration (bearers, sources, target, reference
  set, unresolved policy) and cluster-aware uncertainty (bootstrap
  by item and by proposition; cells are crossed in items and
  properties, not exchangeable draws).
- Secondary summary: one property-weighted aggregate over eligible
  projections, plus its heterogeneity (range or partial-pooling
  spread), reported as a description of the family, never as a
  category-standing verdict. Cell-weighted aggregate as sensitivity.
- Stratify by field (distribution, morphology, morphosyntax,
  meaning, realization, interaction, per `properties.csv`) in
  advance, so an INTJ-distributional versus EXPRESSIVE-semantic
  split, if it appears, was not arranged after the fact. Field
  selects the question; it does not make projections succeed.
- Item-direct-only sensitivity per projection remains mandatory
  (`FREEZE-v2.md` section 4). An aggregate carried by inherited
  cells shows the record is inferentially organized around source
  generalizations. It does not multiply confirmations.

A reconstruction gain, however aggregated, warrants expectations
within this declared inventory under stated information loss. It
establishes no causal order, maintenance, or control. Freeze text
must keep warrant and world-side commitment separate, as now.

### C. The eligible pools are asymmetric, and the boring properties are mostly INTJ sources.

From `properties.csv` and `FREEZE-v2.md` section 5:

| Grouping | Assignment sources | Candidate non-assignment targets |
|---|---|---|
| INTJ | P01, P02, P03, P04, P05, P07 | P06, P08, P09, P10, P11, P12, P13, P14 |
| EXPRESSIVE | P07, P08 | P01, P02, P03, P04, P05, P06, P09, P10, P11, P12, P13, P14 |

Consequences the proposal understates:

- Inflection (P05) and dependents (P04), the proposal's hoped-for
  dense targets, cannot be INTJ primaries in the membership-inferred
  experiment. They are INTJ assignment evidence. They are legitimate
  EXPRESSIVE targets and INTJ leave-one-source-out secondaries.
- With P10, P11, P12 shallow and P14 excluded as a descriptor
  (`FREEZE-v2.md` section 6), the INTJ pool that could plausibly
  pass is P06 (nominal combinability), P08 (stance), P09
  (depictive), P13 (phonological anomaly). The INTJ primary family
  may contain zero to four projections. That outcome must be
  reportable as insufficient information, per gate rules, not
  rescued by lowering thresholds.
- P08 and P09 sit close to INTJ source P07 (non-propositional
  contribution). Source passages characterizing contribution will
  often support source and target together. Eligibility must count
  post-concealment scorable cells under proposition-level
  concealment (`FREEZE-v2.md` section 4), not raw known cells, or
  admitted targets will collapse at scoring time.
- Cross-grouping aggregates run over different target sets and are
  not comparable. The INTJ versus EXPRESSIVE comparison must stay on
  shared eligible targets with shared bearers, cells, baseline, and
  union information bundle (current `FREEZE-v2.md` design), with
  candidate shared pool P06, P09, P13 once P10 to P12 and P14 fall
  away. If no shared target passes, inquiry dependence is unresolved
  even if local projections succeed. Say so in advance.
- Negative cells will be the scarce resource. Every property's
  negative standard in `properties.csv` requires positive source
  evidence (explicit restriction, unacceptability, or full-form
  description); silence is U. Descriptive literature rarely states
  item-level negatives outside controls and celebrated contrasts.
  Gates requiring item-direct counts in each outcome class may admit
  almost nothing. Thresholds must be set with this asymmetry in view
  and tested in simulation, not discovered at the gate.

### D. Define concentration and applicability operationally, including human-checked denominators.

"No excessive dependence on one inherited assertion" needs metrics
before coding, for example: maximum share of known target cells from
any single canonical proposition; minimum distinct propositions;
minimum item-direct cells overall and per outcome class; maximum
share from one form family (in this inventory, effectively a *damn*
cap, since only *damn* (3 rows) and *bang* (2) share families;
tier representation across core, boundary, and control rows matters
more). Applicability removals (INAPPLICABLE) still require the
separate eligibility record with human checker from the audit
design. Model-proposed inapplicability cannot set denominators.
Human adjudication load is therefore part of the design cost, and
the current record has none. Budget it or narrow the inventory;
do not assume it away.

Leave-one-source-out needs its estimand renamed in the freeze:
membership inferred without P04 is a modified grouping
(INTJ-minus-P04), not INTJ. It tests whether the remaining
diagnostics recover the omitted one (cluster cohesion), with its own
assignment thresholds frozen per fold. Secondary status is correct.

## Projectibility check on the amended design

| Check | Status | Basis |
|---|---|---|
| Declaration per projection | GREEN | `FREEZE-v2.md` section 1 fields retained per eligible target |
| Non-trivial projection | YELLOW | Membership-inferred primaries exclude assignment evidence; residual risk is source-target proposition sharing (P07 to P08/P09), handled only if post-concealment counts govern eligibility |
| Warrant separate from world-side claims | GREEN if aggregate stays a family summary; RED if a single gain becomes a category-standing or kindhood verdict | Amendment B |
| Prospective revision | GREEN only if thresholds freeze before production coding and gate output cannot retune them; RED under census-then-threshold ordering | Amendment A |
| Scope | GREEN | Fixed declared inventory, 33 Tier-1 sign-types; no English-wide claim |

Projectibility is structural in the amended design: each eligible
projection states what observing source properties licenses one to
expect about a concealed property, for declared bearers, against M0
and M1, with a failure rule (insufficient information at the gate;
no gain at scoring) fixed in advance. The category earns keep
derivatively, projection by projection, which is the paper's thesis
in operational form.

## Recommended next step (no freeze rewrite yet)

1. Brett decides: adopt the amended eligibility architecture as the
   basis for FREEZE-v3, or amend further.
2. If adopted: fake-data check of the full pipeline (gate function
   with candidate thresholds, admission, per-projection gains,
   property-weighted summary) under null, latent-anchor, hub, and
   copied-assertion worlds at n=33, including scarce-negative
   regimes. Set numeric thresholds from that run plus the corrected
   audit calibration.
3. Draft FREEZE-v3 embedding the eligibility function, locked gate
   script specification, primary and secondary summaries, shared-
   target cross-inquiry rule, leave-one-source-out as secondary with
   renamed groupings, and human adjudication plan (who checks
   eligibility removals and what sample of assertions).
4. Only then production coding. No separate census.

P10, P11, and P12 need no further audit under any branch. Their
corrected audit records already serve as discardable development
evidence and threshold calibration.
