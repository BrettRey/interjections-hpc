# Triage of external evaluation of the matrix-lesion study plan

Date: 2026-11-04  
Reviewer product: model evaluation supplied by Brett (not a referee report)  
Triaged by: Muse Code (muse-wonder-full-1.0)

## Bottom-line verdict

**Continue developing the study. Do not approve or register the current FREEZE.** The review's central diagnosis is right: the draft turns particular predictive comparisons into a stronger, category-wide verdict than they can support. Its most consequential technical claims check out. The right response is a narrower redesign around individually stated projections, matched predictors, evidence provenance, and local outcomes, not abandonment of masked-cell analysis.

No redesign has been implemented from this review yet. Several choices are Brett's because they determine what claim the study is trying to support.

## What I verified

### Predictor and comparison problems

- Category assignment in `analysis/matrix-lesion/lesion.py` is computed deterministically from visible cells. Conditional on those values, the missingness pattern, and the fixed assignment rule, the label adds no Shannon information.
- M3 appends one-hot assignment indicators to the same visible-property matrix used by M1. A simpler duplicated-feature check with the same logistic settings changed log loss from 0.5134 to 0.4953 purely by changing the parameterization and therefore effective L2 shrinkage. I did not reproduce the reviewer's exact table because its train/test construction was not supplied, but the duplicated-predictor mechanism is real.
- `_features` trains on every non-target column, including columns outside a rotation's declared source set. In a source-complete test row those non-source values are replaced by reference means. M1 is therefore not an information-matched direct-property comparator.
- A whole-column mask makes `predict_column` return `None`, because no reference outcomes remain. L3 as drafted cannot be run.

### Fill gate and simulation reporting

- At independent 65% fill over 33 rows, the probability that at least 20 cells are known in every one of 14 columns is 0.0232, or about 2.3%. The additional row condition can only lower the joint pass rate. The predictive simulations do not apply this gate.
- The saved hub condition has Tier 1 = 0.10. Wording that it was “correctly kept out of Tier 1” is too strong. A negative median increment did not prevent individual passes.

### Pilot statistics and implementation

Applying the protocol rule that non-U votes without a continuous verbatim-checkable quote become U reproduces the reviewer's statistics exactly:

| Pilot | Raw κ | Quote-adjusted κ | Raw mean pairwise agreement | Adjusted mean pairwise agreement | Majority-consensus known |
|---|---:|---:|---:|---:|---:|
| 1 | 0.135 | 0.135 | 0.800 | 0.800 | 1/10 |
| 2 | 0.619 | 0.583 | 0.800 | 0.800 | 3/10 |
| 3 | 0.726 | 0.569 | 0.867 | 0.800 | 3/10 |

The voided votes are Copilot OUCH and MMHM in pilot 2 and Copilot OUCH in pilot 3. Consensus values do not change. The current analyzers record quote failures but include those votes in all agreement statistics. They also call a function “majority” while requiring unanimity among non-U votes; Y/Y/N becomes SPLIT. This did not change any pilot consensus.

### MMHM and BLACK

- Dingemanse's surrounding text and table explicitly identify the examples as Siwu with English translations. The pilot-3 Copilot MMHM Y is therefore not evidence for English MMHM as coded. This is a language-provenance failure, not merely a supplement-boundary disagreement. The pilot-2 MMHM quote came from the same material and was already invalid on continuity grounds.
- Wilkins's *black* passage concerns whether it conventionally constitutes an utterance without a preceding linguistic context. It does not positively restrict supplementary occurrence. It does not support P02=N under the drafted negative standard.

## Adopt

These changes should be incorporated before another freeze is drafted.

1. **Retire Tier 1/Tier 2 as general category-standing verdicts.** Evaluate named projections. Make M2 versus M0 the first check and M2 versus a matched M1 the compression comparison. Retain M3 only as a secondary statement about a particular estimator. Add substantive comparators such as the leading single source property and a continuous convergence score.
2. **Use local outcome states.** For each projection, report gain, compression cost, uncertainty, coverage, and dependence. Distinguish evidence for a useful gain, evidence consistent with a negligible gain, and insufficient independent target information. One target failure must not demote a whole grouping.
3. **Create an assertion-level evidence record.** Each derived cell needs the supporting assertion, item-specific versus inherited status, quantifier/modality, language or variety, use slice, construction/environment, source lineage, and a reusable claim identifier. Class-level assertions must not be multiplied by row count without visibility.
4. **Make independently supported targets the primary evidence.** Assignment-supporting and target-supporting assertions need separation, with inherited and repeated target assertions handled as a declared sensitivity. Claim-level dependence is more fundamental than spreadsheet-column separation.
5. **Correct the selective-documentation point.** Retrieval misses and U do not simply bias the study toward failing. Richly documented canonical items and undocumented controls or counterexamples can also make the scored subset look more coherent.
6. **Fix analyzer discipline.** Mechanical checks should cover 100% of cells. Quote-invalid votes become U before agreement and consensus. Implement actual majority. Allow multiple identified spans only where each span has an explicit evidential role; never let an ellipsis masquerade as one quotation.
7. **Repair the simulation before using it for calibration.** Match M1's information set to the rotation sources, represent missingness consistently, drop or redefine L3, apply the intended evidence gates, implement the intended uncertainty calculation and dependence blocks, and test selective-documentation and copied-class-generalization worlds.
8. **Replace the global fill gate with projection-specific evidence requirements.** Required quantities should concern source information, usable targets, positive/alternative cases, and distinct assertion units. A sparse unrelated property should not veto a supported projection.
9. **Treat SUPPLEMENT as a linked expression–construction analysis.** Capability of a sign-type, function in a pairing, and prosody of an occurrence are different objects. A separate small table with integrated counterparts fits the paper better than adding generic construction-class rows to a lexical matrix.
10. **Defer DEPICTIVE unless it gains independently documented positive replication.** The inventory currently names BANG_DEPICT as the explicit sound-depiction case. TUTTUT is not, as inventoried, a clear second positive of the same kind.
11. **Record panel provenance properly.** Capture the configured model or digest where technically possible, CLI version, settings, prompt and packet hashes, raw attempts, retries, timing, tokens or credits, and proof of context isolation. A route name is not a model family.
12. **Audit semantic support, not just disagreements.** Human review should sample unanimous Y and N cells, U cells for retrieval failure, and every distinct assertion on which a primary target depends. Language, use, class scope, quantification, and entailment need checking.

## Adapt

The pressure is right, but the exact remedy needs fitting to this paper and evidence base.

- **Claim/source holdouts:** implement claim dependence directly and predeclare how source-tradition sensitivity will work. Do not assume a source holdout is automatically the right primary estimand. First separate at least two estimands: reconstruction within the descriptive record, and the stronger projection to targets supported by distinct assertions. The paper may value both, but results must not be conflated.
- **Property revision:** preserve source assertions in a first evidence layer, then derive matrix cells explicitly. Splitting every ambiguous property into more columns could simply create a second imposed ontology. Some properties should become multidimensional assertions; others need a narrower proposition, inapplicability state, or operator-specific version.
- **Human review of every distinct primary-target assertion:** feasible and worthwhile if the confirmatory set is narrowed. Audit load should be estimated from assertion counts during the target-availability stage rather than assumed in advance.
- **Narrowing to one or two projections:** likely the best route, but stage it. INTJ to hosted prosody and EXPRESSIVE to repetition/scope are candidates only if their target evidence survives audit. Other rotations can remain descriptive or deferred rather than being deleted from the research programme in one step.
- **Substantive comparators:** P02-only and stance-only comparisons are valuable. They are themselves local projections and should be declared, not added as post hoc explanations for a category result.

## Reject or qualify

- Reject any inference that masked-cell analysis is inherently invalid. It can test specific expectations when target support and dependencies are handled. Its default interpretation is about this deliberately built inventory and descriptive record, not a natural population of English signs.
- Reject treating the duplicated-predictor counterexample as proof that pooling or compression has no value. It refutes the current Tier 1 interpretation, not every usefulness claim for a grouping.
- Qualify source holdouts. Publications within a tradition are not independent samples, but an aggressive source holdout can also change the question and may be impossible where only one tradition documents a phenomenon. Claim lineage is the object to model.
- Qualify the proposed property table. Much of it is useful pressure, but its replacement propositions need testing against the paper's own categories/functions distinctions. For example, separating solitary occurrence, contextual dependence, and explicit ellipsis analysis is an improvement; treating any one decomposition as neutral would not be.
- Reject “five hundred masks” as uncertainty in itself. Mask resampling estimates mask-choice variability, not independent linguistic replication. Uncertainty needs row, family, and claim-level resampling appropriate to the stated scope.

## Prioritized punch list

### P0: before new coding

1. Reframe the study around named projections and local outcomes; rewrite the tiers and any category-standing language.
2. Specify M0/M1/M2 and substantive comparators with matched information.
3. Design the assertion record and target-independence rules.
4. Run a discarded, property-siloed target-evidence audit for hosted P12, P10, and P11. Include P13 only if DEPICTIVE stays in scope. Measure availability, distinct assertions, dependence on assignment evidence, retrieval failure, silence, conflict, and inapplicability. Do not inspect associations.
5. Fix pilot and future analyzers: quote-voiding, exact majority, 100% mechanical validation, and separated schema/semantic status.

### P1: before a new freeze

6. Re-specify properties and bearers from the assertion layer upward. Resolve P01, P06, P10, P11, hosted P12, P13, and P14's identifying glosses.
7. Design the separate expression–construction supplement table, or defer that rotation.
8. Expand DEPICTIVE on explicit evidence or defer it.
9. Rebuild the simulation around the real intended pipeline, including claim dependence, selective documentation, evidence gates, categorical targets, and uncertainty.
10. Write one consolidated protocol. Do not leave operative rules distributed across superseding draft sections.

### P2: production readiness

11. Pin down model provenance, context isolation, call batching, retry ceilings, and preservation of all attempts.
12. Estimate human semantic-review load from distinct assertions, not cells alone.
13. Decide which projections, if any, merit registration as confirmatory. Keep the rest explicitly descriptive or exploratory.

## Decisions needed from Brett

1. Is the confirmatory object one or two named projections, with other rotations deferred/descriptive, rather than four category verdicts?
2. Should the primary estimand require distinct target assertions, with class-inherited targets reported as a separate sensitivity?
3. Should SUPPLEMENT move to its own expression–construction table, as recommended here?
4. Should DEPICTIVE be expanded or deferred?
5. Should the next work be the target-evidence audit for P10-P12, as recommended, rather than another P02 or P05 pilot?

## Overall assessment

This is a strong review. Its verified implementation findings are accurate, and its conceptual central point aligns with the paper better than the current protocol does. The useful study is smaller and more evidence-conscious: an auditable evidence map and a few credible local predictive comparisons. That would be a genuine contribution. Four global rotation verdicts in the current form would overclaim.

## Addendum: reviewer's revised recommendation after Brett's objection

The reviewer subsequently accepted Brett's objection that the first evaluation had shifted too far toward generalization to previously unseen cases. That acceptance is also accepted here, with one scope correction.

The primary question should be framed as recovery inside a declared inventory under specified information loss: given the information permitted to a particular prediction procedure, how well do alternative groupings recover concealed properties of expressions in that inventory, and how does performance vary by inquiry? Historical innocence is not required. What must be unavailable is the concealed target, and every target-dependent estimate derived from it, within the run being evaluated. Cycling through every eligible target cell is therefore a legitimate primary design even though the expressions and facts are already known to the investigator.

This changes the disposition of the first review in three respects:

1. **Retain source-complete lesioning as the principal analysis.** The central comparisons become M2 versus M0 (does the grouping support informative expectations?), M1 versus M0 (how much recoverable structure do the permitted sources contain?), and M2 versus M1 (how much of that structure survives compression into the grouping?). M3 versus M1 is only a secondary estimator comparison.
2. **Separate two membership experiments.** The primary experiment infers membership from surviving source properties in each run and reports both assignment coverage and recovery conditional on assignment. A secondary experiment may retain a previously established membership while underlying observations are lost; that tests stored-summary retention, not inferability from the surviving evidence.
3. **Treat class-level inheritance as dependence to expose, not automatically as contamination.** Recovering five cells from other cells supported by the same class generalization can show that the coded record is inferentially organized by the classification. It does not supply five independent confirmations of that generalization. Results should therefore distinguish item-specifically documented targets from class-inherited targets, and conclusions should be checked under defensible alternative codings and sensitivity exclusions.

The earlier verified repairs still stand: no global category verdict from one target, information-matched M1, no whole-column outcome holdout for a predictor that needs reference outcomes, assertion-level provenance, matched handling of class statements and quantification, quote-voiding before statistics, exact majority, and per-projection evidence gates rather than the global fill gate.

Two qualifications to the revised recommendation:

- The current 35-row inventory is deliberately constructed and should be described as a fixed declared inventory, not as an exhaustive inventory of English interjections or English signs. A fixed-domain result is exact for that domain under the stated lesions; it is not thereby a population estimate.
- If “compression” is claimed, the cost of specifying the assignment rule and its exceptions must be made visible. That can be a transparent complexity accounting (source properties, thresholds, special cases, unresolved rate), not necessarily a formal description-length contest.

Uncertainty should accordingly be reported in three separate forms: variation across lesion scenarios, sensitivity to plausible coding alternatives, and sensitivity to inventory composition (including form families and disputed inclusions). At the one-cell lesion size, enumerating every eligible target gives a fixed-inventory result without pretending that masks are independent linguistic samples.

This addendum supersedes the earlier recommendation insofar as it implied that distinct target assertions must dominate the primary estimand or that the study should be narrowed mainly to secure new-case generalization. Named projections, matched comparators, assertion provenance, and local outcomes remain necessary.
