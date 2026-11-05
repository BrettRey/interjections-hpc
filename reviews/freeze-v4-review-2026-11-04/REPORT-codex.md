# FREEZE-v4 review: codex
<!-- SUMMARY: codex's independent read of FREEZE-v4, saved verbatim by the parent session from stdout · status: received · updated: 2026-11-04 -->

Saved verbatim by the parent Claude session from `codex-stdout.txt`. Route: tools/codex/bin/codex-readonly (read-only wrapper). Prompt: `prompt.md`.

**RESPONSIBILITY NOTICE:** The yield-audit design explicitly requires Brett’s choice of a sealed or open census before anything runs. `DECISIONS.md` records that hold; I found no subsequent entry resolving it. This review does not lift it, and I ran no audit.

## 1. Verdict

**Approve a revised, sealed feasibility audit in principle, but do not run the present design unchanged; the protocol is not near freezable.** Graded latent-class membership is a plausible candidate, but the existing checks do not establish its estimability under the literature’s inherited, dependent, sparsely documented evidence—and the proposed audit omits evidence needed to answer that question.

I cannot substantiate the reversal condition that latent-class membership *cannot* work. Equally, the current evidence does not justify the stronger decision to “keep the convergence rule” regardless of what the feasibility audit finds.

## 2. Findings ranked by severity

### Blocking

**1. The yield audit cannot answer its central feasibility question.**  
*Where:* `yield-audit/DESIGN.md`, “Silos,” “Counts reported”; FREEZE §2.

The design says P10 and P11 “are not re-audited” and carries forward counts from twelve previously sampled items. But EXPRESSIVE now has additional, deliberately different bearers, and the relevant units have changed: strengthening under a specified repetition pattern and survival of a specified contribution under negation. P07 is also absent from the audit’s silos.

Consequently, old marginal coverage counts cannot establish whether ten current rows have three jointly visible EXPRESSIVE diagnostics, much less whether those diagnostics survive dependence concealment. This is precisely the possible failure that could reverse the recommendation to proceed.

**Fix:** Retain valid previous assertion records, but check P07/P08/P10/P11 coverage on the current inventory under explicit unit definitions. Report sealed aggregate counts of jointly documented diagnostics, independent testimony, polarity diversity, and post-concealment availability. Do not compute assignments or gains.

**2. The estimability safeguard counts cells where it needs to assess information.**  
*Where:* FREEZE §2, membership model; §4, testimony units.

The threshold requires “at least 10 bearer rows [with] three or more visible diagnostics.” Those could be the same three class-level claims repeated through ten inclusion judgments. Conversely, ten rows might document different, poorly connected diagnostic subsets. Neither situation establishes stable estimation of the intended class.

“Each diagnostic’s contribution comes from the fitted class-conditional rates” also does not ensure that “none decides membership.” An unconstrained fit can separate primarily on one diagnostic, or select a split inconsistent with the intended anchor. Merely orienting the resulting classes cannot repair that split. Indeed, M2’s predictions are unchanged by swapping class labels.

**Fix:** Treat LCA2 as a candidate. Before approval, specify checks for independent diagnostic support, overlapping observation patterns, fit stability, and compatibility with the declared anchor profile. Failure should mean **membership not estimable**, without restoring a tally or demanding any single property. Test these checks using the evidence structure actually found by the audit.

**3. Reference-side dependence remains an unresolved violation of the inference rule.**  
*Where:* FREEZE §2, principal experiment; §4, proposition-level concealment.

Reference rows remain “intact as coded,” while symmetric concealment “remains a Brett decision.” Thus reference memberships can incorporate the same observation or inclusion judgment that supplies their target outcomes. Concealing that dependence only in the scored row does not stop the learned category–target relationship from reflecting duplicated evidence.

**Fix:** Apply the source–target independence rule to every reference inference used to estimate the projection. A full-record reconstruction can remain separately reported, but it should not establish independent projective support. Specify whether concealment triggers membership refitting and apply the resulting information state consistently to M1 and M2.

### Important

**4. A sealed audit still needs a usable measurement schema.**  
*Where:* FREEZE §§2, 6; `properties.csv`; audit “Silos.”

The audit promises coding “under the v4 definitions,” yet P01 still requires separation, P10 lacks a settled pattern-by-effect representation, and P11 lacks a final contribution-by-host unit. The CSV still assigns P10/P11 `expr_assignment_eligible=no`, admits only Tier A, and retains obsolete P04/P05/P06 standards.

These are operational contradictions, not merely presentation defects. Different interpretations change both coverage and dependence counts.

**Fix:** Supply one governing audit schema before packet generation. It need not freeze the production analysis, but must define audit units, negative standards, applicability, and allowable Tier B evidence. In particular, an ordinary corpus line cannot by itself demonstrate strengthening or survival under negation; punctuation alone cannot establish hosted prosodic separation.

**5. The newly admitted P08 negatives exceed what the checked passage establishes.**  
*Where:* FREEZE §6, “P08 = N standard”; `items-v4.csv`.

The rule permits N when a source “contrasts the use with expressive items in the same slot.” In CGEL pp. 557–558, modal, particularising, and expressive attributives occupy separate subsections. That establishes different described functions; it does not explicitly establish absence of every conventional evaluative or affective component. CGEL even characterizes *main* and related items through ranking in importance.

A sensitivity dropping these Ns is valuable, but does not make their primary evidential basis adequate.

**Fix:** Distinguish an explicit exclusion of stance from placement in another descriptive category. Code the latter U unless the passage actually excludes the defined contribution. Keep these items as intended controls; control selection does not determine coded polarity.

**6. The declared “single-word” shared core contains a construction-sized bearer.**  
*Where:* FREEZE §5; `items-v4.csv`, `BASTARD_SUPP`.

“All single-word rows” supposedly constitute the 42-row intersection, but `BASTARD_SUPP` is represented as *bastard* while its specified use is **the bastard**. CGEL p. 1413 describes the supplementary epithet as an NP and attributes non-reference, attitude, and prosody to that construction.

Treating those as properties of the lexical head risks assigning determiner combination, dependents, or supplementhood at inconsistent levels.

**Fix:** Define the bearer explicitly as an expression in a conventional use, with construction evidence linked to it. Either justify this row’s lexical INTJ comparison on that basis or exclude it from that universe. Also demonstrate the promised 40–60% selection balance; the current inventory does not document that calculation.

**7. The simulation implementation and declared priors disagree.**  
*Where:* FREEZE §2; `sim_convergence_assignment.py`, `fit_lca`.

The protocol specifies Beta(1,1) and Dirichlet(1) priors with “best penalized likelihood.” The code adds log-density penalties and uses updates `(successes + 1)/(trials + 2)` and `(class mass + 1)/(n + K)`. For a MAP objective, those correspond to Beta(2,2) and Dirichlet(2), not the stated uniform priors.

**Fix:** Choose the intended estimator and reconcile its objective, updates, and documentation. The existing checks remain useful diagnostics, but do not validate the exact declared estimator—especially at this sample size.

**8. Reconstruction scope still does not govern the outcome language.**  
*Where:* FREEZE §§1–3, 8; deeper-v3 triage.

“Grouping supports informative expectations” and “supported gain” can still outrun recovery of documented, scorable cells. Selective documentation remains principally a threat paragraph. The mandatory comparator estimators also remain incompletely specified.

**Fix:** Adopt the triage’s distinction between documented-record recovery and additional projective warrant. Specify comparator estimators and add the permitted-source-knownness diagnostic. Reapply eligibility to the actual common evaluation set, rather than assuming separate grouping admissions suffice.

### Minor

**9. Remove stale scope and inventory statements before approval.**  
*Where:* FREEZE §§1, 12–13; Appendix A; `CONVERGENCE-CHECK.md`.

These variously retain 49, 47, 35, and 33-row descriptions; §12 calls the already-incorporated v1 restriction unincorporated. The 33-row simulation is legitimate historical evidence, but not the current inventory.

**Fix:** Reconcile current specifications and label historical configurations explicitly.

## 3. Decisions I disagree with

I disagree with carrying old P10/P11 counts forward as sufficient for the new membership-feasibility question, with treating descriptive subsection contrasts as P08 negatives, and with adopting LCA2 before checking independent support and anchor compatibility.

`DECISIONS.md` corroborates Brett’s assignment principle, inventory revisions, and evidence-tier order. Those commitments do **not** establish the statistical adequacy of this particular latent-class implementation.

## 4. What should remain

Keep the fixed-inventory scope, graded membership, weight for absences, assertion-first provenance, testimony tracking, P08 guard, explicit dependence states, separate Tier A/A+B reporting, and production hold. Preserve the separation between outward projections and omitted-diagnostic cohesion tests, and the acknowledgement that M2 beating a weak M1 does not certify compression.

The source checks support those distinctions: Potts’s repetition example mixes positions, Ljung distinguishes several slot-filler functions, and CGEL distinguishes lexical items from the supplementary constructions containing them. Those distinctions should constrain the coding rather than disappear during aggregation.
