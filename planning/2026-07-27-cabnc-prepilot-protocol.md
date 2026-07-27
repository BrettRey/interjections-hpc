# CABNC pre-pilot protocol
## Decision
Run a transcript census and a small blinded feasibility pilot before reconstructing the manuscript's central projectibility section. Do not treat the pilot as evidence for the projection. Its purpose is to determine whether a confirmatory test can be made interpretable, independent, and adequately powered.

The CABNC study tests one primary narrow but central claim:

> Independently assigned `INTERJECTION_sem` membership provides a transportable representation that improves prediction of post-offset next-position trajectory for unseen form families beyond matched immediate cues, `INTERJECTION_syn`, and neighbouring classifications.

The `INTERJECTION_syn` edge is separately declared and secondary. It cannot substitute for a failed primary semantics-facing edge. Selecting the semantics-facing edge tests the projective standing of a non-syntactic category; it does not give semantics ontological priority.

It does **not** by itself establish the three-category ontology, `INTERJECTION_prag` as a source category, causal direction, network order, stability, or transport beyond the corpus population. Recipient treatment is an interactional target property, not identical to `INTERJECTION_prag` membership.
## Why a pre-pilot is necessary
The existing project datasets cannot support this declaration. The morphology sample contains four preselected derivative families and an all-positive retained-semantics outcome; the _fie_ study contains one sign-type; and GloWbE lacks token-level sequential outcomes.

CABNC supplies natural conversation, transcript timing, and linked audio, but four feasibility facts remain unknown:

1. whether enough independently classified positive and negative form families survive disambiguation;

2. whether a mechanically anchored post-offset trajectory can be coded reliably without importing the source classifications;

3. whether `syn` and `sem` have enough discordant cases to estimate separate edges;

4. whether category-level information contributes anything beyond current-turn completion, action type, prosody, and other immediate cues.

## Frozen corpus source
Use one immutable transcript snapshot and do not mix representations or releases.

- Repository: [saulalbert/CABNC](https://github.com/saulalbert/CABNC)

- Commit: `0a28a11e168e312d1b9ad406a3352f31c13b86a2`

- Subtree: `data/cabnc_talkbank_chat/`

- Subtree Git object: `7f7f87611350439e404baa8f8c659f33e81efecb`

- Immutable archive: `https://codeload.github.com/saulalbert/CABNC/tar.gz/0a28a11e168e312d1b9ad406a3352f31c13b86a2`

- Observed archive SHA-256: `10c466d64830be7944385fe4253d3a5634eacf4788ff8d3fdb4113d7e26b4d38`

- Corpus landing page and DOI: [TalkBank CABNC](https://talkbank.org/ca/access/CABNC.html), [doi:10.21415/T55Q5R](https://doi.org/10.21415/T55Q5R)


The preliminary discovery counts used `data/cabnc_chat-v0.1/`, which the repository supersedes. They must not be cited or used for sampling. The frozen current subtree has these acquisition smoke checks:

- 1,860 `.cha` files;

- 16,597,291 transcript bytes;

- 246,783 physical main-tier lines;

- timing codes delimited by `U+0015`.


The files are transcript segments, not automatically independent conversations. The parser will preserve `segment_id`, media identifier, episode, and participant identifiers separately. A defensible conversation grouping must be established from corpus metadata before any conversation-spread gate is evaluated.

Transcripts are stated to be CC BY 3.0 in the repository README and TalkBank landing page. Audio remains subject to the original BNC research-use conditions. The transcript-only census requires no credentials; the current TalkBank download endpoint presently requires authentication. Audio will not be acquired or exposed to coders until Humber provides a written REB determination.
## Operational bearer and holdout
The operational sign-type is a conventionalized constructional use defined by a form family plus a profile that may include grammatical, semantic, or interactional contrasts. No domain has priority in fixing the bearer. A sign-type is never split because target tokens happen to receive different post-offset trajectories.

Standalone, prenominal, and complement-taking _damn_ illustrate sign-types distinguished grammatically. Conventional meaning contrasts or independently established interactional-action contrasts may equally distinguish sign-types. All sign-types belonging to one form family remain in the same outer fold. If uses of _oh_ differ only in the target outcome and no independent profile contrast distinguishes them, they remain unsplit for this declaration.

The primary outer evaluation holds out the entire conservative form block and also removes directly related component-bearing constructions from training. All variants, sign-types, and tokens of the block remain outside training. A weaker ordinary outer-block analysis is diagnostic only. A pathway-blocked sensitivity additionally removes independently documented recruitment or descent relatives. The primary prediction integrates over new speaker and conservative collection-block effects rather than exploiting identities learned from other forms; a secondary conditional analysis may ask about a new form used by an otherwise observed speaker or interaction. This establishes lexical generalization within CABNC, not unrestricted projectibility to new varieties or periods.
## Three separated evidence layers
### Layer 1: sign-type dossier
The dossier assigns `INTERJECTION_syn`, `INTERJECTION_sem`, and neighbouring-category labels using external sources and CABNC conversations reserved exclusively for dossier construction. Dossier conversations and speakers must be disjoint from target events wherever the corpus permits. Dossier events never enter confirmatory evaluation.

Each source category receives two recorded judgements:

1. **Full-profile membership:** the best classification using the category's mixed network of grammatical, semantic, and interactional properties.

2. **Declaration-specific membership:** the classification available after the exact post-offset trajectory target and its prespecified close proxies have been masked.


The second judgement is the primary source variable for this test. The first establishes that the test has not silently redefined the category as domain-pure. Disagreement between them measures how dependent the declaration is on the withheld evidence and must be reported as a sensitivity analysis.

Each dossier records:

- form family and sign-type identifiers;

- constructional-use description;

- included variants and excluded homographs;

- external sources and independently sampled dossier segments;

- conventionalization judgement and confidence;

- individual grammatical, semantic, and interactional diagnostics;

- neighbouring classifications;

- full-profile and declaration-specific category judgements;

- an evidence mask stating which facts were withheld for this declaration;

- any prohibited evidence accidentally seen.


The full dossier may describe response success, recipient uptake, or related interactional facts when they are part of a category's ordinary mixed individuation profile. The declaration-specific evidence card may not expose the target token's post-offset trajectory, target-sample frequencies, or a prespecified close proxy. Every fact is tagged by domain, evidence source, and whether it is available in the declaration-specific judgement.

For `INTERJECTION_syn`, record distributional status, ordinary clause function, morphology, argument structure, syntactic dependence, alternative lexical-category analyses, published grammatical analyses, and qualifications. Semantic or interactional evidence, including independent evidence of `INTERJECTION_sem` or `INTERJECTION_prag` membership, may bear on the full-profile judgement. The declaration-specific judgement withholds only the present post-offset trajectory target and its prohibited proxies.

For `INTERJECTION_sem`, record contribution type, effect of removal on at-issue content, conventional stance, perspective holder, displaceability, and semantic neighbours. Contextually inferred emotion alone is insufficient. Grammatical and independently established interactional evidence may bear on full-profile membership. Again, the declaration-specific judgement excludes the exact target and its close proxies rather than excluding an entire disciplinary domain.

A dossier team first compiles the evidence with form identity visible. `INTERJECTION_syn`, `INTERJECTION_sem`, and each neighbouring classification are judged in separate randomized passes, one classification per row, by distinct coder pairs. Declaration-specific cards precede full-profile cards; presentation order, form masking, and form guesses are recorded. Agreement between evidence-only and ordinary classifications is a leakage diagnostic, not a requirement that linguists somehow fail to recognize familiar forms. Reliability gates apply to `syn` and `sem` separately; a joint representation cannot pass by pooling an unreliable component with an easier one.

Every corpus-derived dossier fact records its segment, conservative collection block, sampled conversation block where available, and speakers. These units are reserved before target sampling. A mechanical audit checks dossier/target block and speaker disjointness before labels are joined.

Target tokens receive a separate double-coded, pre-offset token-to-sign-type assignment. Coders see opaque frozen sign-type rules, but no category membership or post-offset sequence. This layer resolves homographic and constructional uses without improvising the category-to-outcome join after coding. It has its own reliability and indeterminacy gate.
### Layer 2: target-token cue coding
A separate team codes only information available by the acoustic offset of the target-bearing turn-constructional unit. These variables supply the non-category comparators:

- position within turn and TCU;

- standalone or syntactically integrated realization;

- judged TCU completeness at the crop point;

- clause type and prior action type;

- addressivity and number of available recipients;

- duration, syllable count, and speech rate;

- prosodic independence;

- pre-target pause and pre-offset overlap;

- directly observable stance polarity or intensity;

- repetition and complement presence;

- lexical frequency or familiarity from a source frozen independently of outcomes.


The cue team sees no dossier labels, post-offset timing, recipient action, outcome summaries, or predictions. Every timing field records whether it was audio-measured, transcript-derived, interpolated, estimated, or unavailable, together with effective resolution. Prosodic judgements record their audio or transcript basis. Form-level frequency and familiarity are joined from an independently frozen, hashed source rather than supplied by cue coders.

### Layer 3: post-offset trajectory coding

Target coders see the complete target-bearing event and the ensuing sequence but no source-category labels, sampling strata, predictions, or model output. They retain the lexical form: masking it would make action interpretation less valid and cannot work reliably with audio. Controls and candidate categories are intermixed, coders remain naïve to the hypotheses, and a postcoding questionnaire measures hypothesis awareness.

First code mechanical observations:

- first post-offset speaker, form, and TCU shape;

- whether that speaker is an addressed or ratified recipient;

- first post-offset onset and its timing provenance;

- gap or overlap;

- source speaker enters before another participant;

- source speaker resumes the same trajectory;

- recipient entry is minimal or non-minimal;

- 2.5 seconds without any vocal entry;

- competitive overlap;

- technical or context problem.


Then code the mechanically anchored trajectory:

- `RECIPIENT_NONMINIMAL_ENTRY`: another participant produces a non-minimal TCU before source re-entry;

- `RECIPIENT_MINIMAL_ENTRY`: another participant produces a minimal listener TCU before source re-entry;

- `SOURCE_ENTRY`: the source speaker produces the first post-offset vocal entry;

- `NO_VOCAL_ENTRY_2500`: no participant produces a vocal entry within 2.5 seconds;

- `COMPETITIVE_OR_OTHER`;

- `UNCODABLE`.


The primary four levels remain separate. They define post-offset next-position trajectory rather than presupposing recipient uptake. Fittedness is coded separately and produces a labelled sensitivity outcome through frozen code. Coders do not enter a second collapsed outcome manually. Rates of `COMPETITIVE_OR_OTHER`, `UNCODABLE`, and technical failure are reported by source cell; differential attrition can fail the feasibility gate.
## Context windows and eligibility
The source-side packet contains up to two preceding TCUs, capped at 12 seconds, and the complete target-bearing TCU. It stops exactly at acoustic offset and contains no post-offset silence, recipient onset, later continuation, or following transcript.

The target packet contains the same preceding context and target-bearing TCU, then continues through the later of five post-offset seconds or two subsequent complete TCUs, capped at 12 seconds. Requests for more context use a logged `context_insufficient` rule.

Pre-offset eligibility coders see no following sequence. They judge intelligibility, participant identity, potential-recipient availability at offset, timing adequacy, quotation, metalinguistic mention, and reading aloud. Frozen code separately checks that the following packet is unclipped, nonduplicated, uncorrupted, and correctly bounded. The two layers are joined mechanically; actual response or nonresponse cannot determine potential-recipient availability.

Same-speaker continuation, silence, overlap, untimed but sequentially interpretable tiers, and candidate-only turns are outcomes or descriptive properties, not automatic exclusions.

The primary trajectory study requires audio-measured timing at a declared resolution. If REB approval, audio access, or measurement quality is unavailable, CABNC cannot be converted after coding into a transcript-timed 2.5-second study. The semantic-repetition fallback is activated.
## Census and form-family rules
Parse only `data/cabnc_talkbank_chat/**/*.cha`. Construct logical CHAT tiers before tokenization and respect episode and file boundaries. Merge adjacent main tiers only when they have the same known listed speaker, both boundary times are present, and the gap is no greater than 2.5 seconds. Preserve the original same-speaker chain and the reason for each analytic split. Preserve all timing spans and flag rather than silently repair missing or inconsistent metadata.

A candidate is turn-initial only if it is the first lexical token of the first main tier in the collapsed turn. Ignore CHAT markup, explicit noise codes, and transcription comments; do not skip filled pauses or response forms. Preserve raw, normalized, and form-family representations.

Use a versioned explicit alias table. Do not use stemming, edit distance, or model-generated clustering. Begin conservatively:

- keep _oh_ and _ooh_ separate;

- keep _yes_, _yeah_, and _yah/ya_ separate;

- keep _mm_, _mhm_, and _uh-huh_ separate;

- combine _ok_ and _okay_ only if an explicit phonological-family rule is accepted;

- normalize lengthened spellings only through enumerated aliases;

- place any aliases later combined in the same holdout fold.


Homographic forms such as _right_, _well_, _dear_, _god_, _great_, _please_, _sorry_, _thanks_, _shit_, _fuck_, and _damn_ enter the census as candidates, not as interjection tokens. Source-side adjudication determines constructional use without seeing the following sequence.

The census retains every occurrence and attaches flags. The study-eligible subset is derived only afterward. Every output row must trace back to corpus commit, collection block, tape, tape side, file, episode, tier, analytic turn, original same-speaker chain, parser version, and alias-table version. The three-character BNC prefix is the conservative dependence block for corpus-wide spread; tapes, tape sides, and files are not called conversations. Exact sampled conversation boundaries require manual adjudication.
## Sampling structure
After the raw census, stratify sign-types by the four source combinations:

- `syn+ / sem+`;

- `syn+ / sem−`;

- `syn− / sem+`;

- `syn− / sem−`.


The negative and discordant cells deliberately include neighbouring categories and controls; the yield gate does not require 24 strict interjection families. Candidate controls include supplements, expressives, response tokens, discourse markers, routine formulae, fillers, minimal lexical responses, vocatives, parentheticals, nonlexical vocalizations, and ordinary one-word TCUs.

The bounded pre-pilot has one evaluation point after 160 events: ten events from each of sixteen source-selected outer blocks, frozen before outcome inspection: _oh_ and its anchor constructions, _ooh_, _ah_, _eh_, _ha_, _cor_, _ugh_, _gosh_, _mm_, _er/erm_, _yes_, _no_, _well_, _right_, _mum_, and _thanks/thank you_. Opaque identifiers replace these labels in coder packets. A block that cannot supply ten eligible events under the frozen rules is a feasibility failure, not an invitation to substitute a block after outcomes are known.

Require at least 25 eligible target events across at least 10 conservative collection blocks for each retained family before manual sampled-conversation adjudication. Cap each speaker's and collection block's contribution. Prefer 40–80 events per family and cap extremely frequent families so _oh_, _yeah_, and _mm_ do not dominate.

For the primary semantics-facing edge, require at least six form families and roughly 150 events on each side of the matched `sem` contrast in the confirmatory design. The `syn` edge is secondary. Sparse discordant cells can limit or defeat one edge; they do not authorize a post hoc joint representation. A joint representation is reportable only if each component independently clears its reliability gate and is declared before confirmatory coding.
## Predictive estimand

The primary estimand is the expected quality of the predicted four-way post-offset next-position trajectory for a token from a previously unseen component-blocked form family, produced by a speaker in a collection block drawn from the study's CABNC sampling frame. The comparison of interest is the expected change in predictive quality when declaration-specific `INTERJECTION_sem` is added to matched immediate cues, `INTERJECTION_syn`, and independently assigned neighbouring classifications. The `syn` edge has a separately labelled secondary estimand.

The finite sampling frame must be explicit: form families are the deliberately constructed positive, discordant, and control families that survive the census and dossier gates, not a random sample of every possible English expression. Macro-averaging gives each retained family equal weight. Population claims beyond informal British conversation require replication.

For the primary estimand, predictions for the held-out block integrate over the posterior distribution of a new block effect and over new speaker and collection-block effects. A secondary, explicitly conditional estimand may retain speaker or interaction effects learned from other forms. The two answer different questions and cannot be pooled.

## Generative model and Bayesian workflow

The provisional outcome model is a multilevel categorical regression. For token (i), the four-way outcome (y_i) is drawn from a categorical distribution whose softmax-linear predictors contain one of the source representations below, plus varying effects for outer block, sign-type within block if identifiable, speaker, collection block, and sampled conversation where available. The census and grouping audit determine the actual crossing and nesting structure before outcome coding begins.

Each component-blocked leave-one-outer-block-out fold is fitted without any token from the held-out block or its directly declared lexical components. Its block effect is drawn from the posterior predictive distribution for a new block rather than estimated from held-out outcomes. Speaker and collection-block effects are likewise integrated out for the primary estimand. This makes uncertainty from form heterogeneity part of the prediction instead of hiding it in a plug-in estimate.

Before real outcomes are fitted:

1. standardize continuous predictors and state scientifically interpretable, regularizing priors for coefficients, intercepts, and group-level variation;
2. run prior-predictive simulations to reject priors that imply degenerate outcome proportions, implausible family heterogeneity, or near-certain effects;
3. use simulation-based calibration on synthetic data to verify the inference implementation;
4. run design simulations across a range of null, small, and substantively useful category effects and plausible outer-block, pathway, speaker, collection-block, and conversation variances.

The model arms share the same outcome model, folds, sampling frame, and symmetrically available covariates. Priors need not be mechanically identical when parameterizations differ; each arm receives priors calibrated to the same substantive scale and checked through the same prior-predictive workflow.

After fitting, posterior-predictive checks examine trajectory prevalence, within-block distributions, speaker, collection-block, and sampled-conversation clustering, residual form and pathway structure, and whether the model reproduces the observed concentration of rare trajectories. Held-out calibration is reported by outer block, not only in the pooled sample.

## Model comparison

1. **Base rate:** outcome prevalence estimated from training data.

2. **Immediate-cue model:** only Layer 2 token-local variables.

3. **Matched primary baseline:** immediate cues, declaration-specific `INTERJECTION_syn`, independently assigned neighbouring classifications, external form frequency/familiarity, and symmetrically available covariates.

4. **Flat-diagnostic model:** the unstructured Layer 1 diagnostic vector available under the same declaration-specific evidence mask, with no interjection category labels.

5. **Primary semantics-facing model:** the matched primary baseline plus declaration-specific `INTERJECTION_sem`. This model's held-out improvement over model 3 is the primary test.

6. **Secondary grammar-facing model:** the symmetrical secondary baseline plus declaration-specific `INTERJECTION_syn`; it is labelled secondary and cannot replace a failed primary result.

7. **Joint and full-profile sensitivities:** the predeclared `syn × sem` representation and full-profile memberships, only when each component independently clears reliability and leakage gates.


The complete eligible flat-diagnostic vector is an information-rich upper comparator. It may contain mixed-domain evidence but never the withheld target or a prohibited proxy. The category model is not required to beat a deterministic function of its complete eligible evidence. Its scientific value lies in calibrated generalization and compression under partial observation. Compare predictive performance together with predictor count, coding burden, and calibration; do not claim unique information after conditioning on the complete diagnostic basis.

Primary evaluation uses macro-averaged held-out log score or expected log predictive density, multiclass Brier score, calibration intercept, and calibration slope. Report each outer block's score contribution and uncertainty, the distribution of block-level score differences between arms, group-level variance posteriors, shrinkage diagnostics, and blocks for which the category representation performs worse than the base rate. Accuracy is not a primary metric.

The preregistration will define a practically negligible region and a useful-prediction region on the scoring scale from scientific utility and coding burden before pilot outcomes are inspected. Pilot-derived variance components may inform feasibility simulations but cannot move these regions. Conclusions use both the full uncertainty distribution and those declared regions. This preserves a risk-bearing decision rule without reducing the analysis to one threshold or inviting an unspecified posterior to “speak for itself.”
## Claim-to-result map
| Result | Warranted conclusion | Manuscript consequence |
| --- | --- | --- |
| Primary semantics-facing model beats the matched baseline, is calibrated, and meets the prespecified margin under component-blocked folds | `INTERJECTION_sem` supports transportable prediction of post-offset trajectory in unseen CABNC form blocks | Report one demonstrated, corpus-bounded cross-domain edge |
| Primary model also beats independently assigned neighbouring classifications | The semantics-facing cut preserves predictive information not captured by those coded neighbours | Strengthen the distinctiveness claim for the tested cut |
| Category model approaches the flat-diagnostic model with materially less information or coding burden | The category provides useful scientific compression | Report compression without claiming new information beyond full diagnostics |
| Flat diagnostics beat the category label | The label discards predictive information contained in its diagnostic basis | Retain only a weaker compression claim if the declared margin is met; otherwise demote the edge |
| Immediate cues and the matched baseline equal or beat `INTERJECTION_sem` | Local action formation and rival classifications suffice under this design | Kill the primary cross-domain edge; do not reinterpret the null as success |
| Neighbouring classifications beat both tested interjection cuts | The relabelling objection survives for this outcome; an interaction-facing representation may carry more sequential information | Do not claim distinctive payoff for the tested cuts; treat the interaction-facing interpretation as a prospectively specified hypothesis, not proof of `INTERJECTION_prag` |
| Secondary `INTERJECTION_syn` succeeds while primary `INTERJECTION_sem` fails | Only the secondary grammar-facing edge is supported | Report the primary failure prominently; do not substitute the secondary edge as the headline result |
| Pathway-blocked performance collapses | Apparent transport depended on historically related forms in training | Do not claim unrestricted new-family transport |
| Performance occurs only for frequent families or is miscalibrated | No transportable projection has been shown | Treat as failure under the declaration |

No result from this study establishes causal direction or the full three-node network.
## Leakage and validity audit
Before labels are joined, an independent auditor must verify:

- dossier and target collection blocks and speakers are disjoint under the frozen reservation registry;

- source packets contain no post-offset information;

- no declaration-specific source criterion uses the post-offset trajectory, fittedness sensitivity, or a prespecified close proxy; full-profile evidence is stored separately;

- response-token and similar comparator labels come from independent evidence;

- sign-type divisions, token-assignment rules, surface aliases, outer blocks, component relations, and pathway relations were frozen before target coding;

- no exclusion was made after target inspection;

- no strict variant crosses outer folds and every primary fold applies the frozen direct component exclusions;

- declaration-specific evidence cards and free-text notes contain no linked target-sample information;

- current-token prosody and TCU completeness are available to the immediate-cue comparator;

- structured and rival models receive symmetrically available covariates and substantively comparable, prior-predictively calibrated priors;

- the ten-coder role matrix separates `syn`, `sem`, neighbours, cue/sign-type work, and target trajectory as declared;

- adjudication of one layer does not consult the other;

- timing, filenames, clip length, transcript truncation, and annotation order cannot reveal the target to source coders;

- a random 10% of source packets matches the original transcript and audio boundaries;

- pilot outcomes were not used to tune membership criteria, block relations, scoring regions, or confirmatory defeat thresholds;

- token-to-sign-type assignments were made from pre-offset packets and opaque rules;

- human pre-offset eligibility and mechanical packet eligibility were joined without reference to trajectory;

- every timing value has declared provenance and primary events are audio-measured;

- primary outcomes were derived by frozen code from the uncollapsed trajectory field;

- all declared checklist items are present, and every failure is handled according to its prospectively assigned class: halt, remediable before unblinding, or note only.


The report must discuss three unavoidable construct-validity risks. Standalone or complete grammatical packaging can itself create transition relevance; expressive action can itself normatively constrain a response; and fittedness judgements can import an analyst's semantic or interactional construal of the source. The mechanical trajectory, fittedness sensitivity, immediate-cue comparator, and flat-diagnostic comparator separate these routes as far as the design permits.
## Reliability and feasibility gates
Proceed to confirmation only if all applicable gates pass:

1. Ten independent trained coders satisfy the frozen role-separation matrix before packet release.

2. The pinned commit, subtree object, file count, tier count, and per-file hashes are reproduced.

3. Candidate extraction is deterministic, every warning is logged, and a blinded sample establishes acceptable extraction precision.

4. Conservative collection blocks are validated and used for corpus-wide independence; file segments, tape sides, and tapes are not counted as conversations by assumption. Exact conversations are adjudicated for sampled material.

5. The primary semantics-facing confirmatory contrast has at least six form blocks and about 150 events on each side after component blocking. The secondary grammar-facing edge must independently satisfy its own yield gate.

6. At least half the retained blocks exhibit more than one primary trajectory; no primary trajectory is vanishingly rare.

7. `INTERJECTION_syn` and `INTERJECTION_sem` each separately reach Krippendorff's alpha of at least .80, with a lower 95% bound at least .70. Principal neighbour labels satisfy their separately declared gates.

8. Token-to-sign-type assignment reaches alpha of at least .80, with a lower 95% bound at least .70.

9. Post-offset trajectory alpha is at least .70, with a lower 95% bound at least .60.

10. No primary field has more than 15% uncertain or uncodable values, and exclusion or outside-contrast rates are not materially differential across source cells under the frozen tolerance.

11. All enumerated leakage checks pass under their prospectively assigned failure classes.

12. No outer block, speaker, collection block, or sampled conversation dominates the effective sample.

13. Simulation-based design analysis spans plausible null, small, and useful effects and variance components, and shows that the proposed design can distinguish scientifically different data-generating processes with tolerable rates of false warrant, missed warrant, and ambiguity. The full operating-characteristic curves are reported; no isolated 80% threshold substitutes for them.

14. The immediate-cue model is not already effectively deterministic.

15. All 160 declared pilot events reach the single evaluation point; there is no interim optional stopping.

16. Pilot events are excluded from confirmatory scoring or permanently confined to training and tuning.


Report Krippendorff's nominal alpha, Gwet's AC1 under extreme prevalence, raw agreement, confusion matrices, and cluster-bootstrap intervals by form family. Use weighted kappa only for ordinal confidence fields. Report timing agreement separately. The thresholds remain operational pilot gates, but design simulations must also show how observed misclassification would attenuate or distort the substantive estimates; a composite label does not pass merely because its headline agreement coefficient clears a cutoff.

Passing these gates shows that a valid confirmatory study is feasible. It is not evidence that the projection succeeds.
## Automation and agent roles
The lead owns the protocol, thresholds, theoretical interpretation, and all manuscript prose.

- **Codex engineering agent:** parser tests, manifests, deterministic extraction, fold integrity, and reproducibility checks.

- **Independent methodology agent:** leakage audit and claim-to-result mapping without access to linked outcomes.

- **Agy/Opus 4.6 Thinking:** construct-validity and philosophy-of-science review at the protocol and frozen-analysis gates.

- **Agy/Gemini 3.1 Pro:** independent corpus/sampling audit. Its numerical yield claims are treated as hypotheses until reproduced.

- **Claude Code/Claude 5:** used for high-stakes methodological or prose judgement when Agy's Claude allocation is exhausted or at the final gate.

- **Local models:** candidate triage, proposed alias or homograph flags, schema-format checks, and contradiction searches only after a human gold set exists. They do not assign final categories, code post-offset trajectory, judge prosodic boundaries, or determine inclusion.


No model output is a vote or a datum. Deterministic parsing and human-coded, blinded annotations remain the evidential basis.

## CHILDES disposition

Keep CABNC as the primary corpus. CHILDES changes the population, register, recipient, and often the observability of uptake at the same time: caregiver–child interaction is structured by development, scaffolding, repeated family routines, and substantial nonverbal response. It therefore cannot silently replace CABNC while preserving the adult-conversation estimand.

The strongest CHILDES use is an external developmental/register replication after the CABNC representation and analysis are frozen:

- Use the [HSLLD](https://talkbank.org/childes/access/Eng-NA/HSLLD.html) mealtime material, restricted to adult-produced target turns. It offers the broadest plausible family base, but its audio is unlinked, so the target must be the next **verbal** contribution rather than fine timing, overlap, silence, or nonverbal uptake.
- Use the linked-audio dinner subset of [Gleason](https://talkbank.org/childes/access/Eng-NA/Gleason.html) as a smaller audit of transcript-only classification, not as a silently pooled source of extra sample size.

Within HSLLD, all sessions and speakers from one family remain in the same resampling unit; intended addressee, recipient role and age, visit, activity, and next-speaker role are mandatory. A successful result would show transport to caregiver–child mealtime interaction. A failure would not by itself defeat the adult CABNC claim.

CHILDES downloads now require TalkBank registration and carry corpus-specific Ground Rules. Raw CHILDES transcript or media content remains local unless the actual hosted-model route has verified non-storage terms; local models may assist only within the mechanical and human-validated limits stated above.

## Predeclared fallback

If CABNC fails because post-offset trajectory cannot be separated from immediate action-formation cues, because the semantics-facing contrast is absent, because the ten-coder separation cannot be staffed, because audio-measured timing is unavailable, or because reliable trajectory coding is impossible, do not force a corpus result or substitute a developmentally different CHILDES result. Move to the independently normed semantic-repetition experiment already identified in the feasibility review. That experiment tests whether `INTERJECTION_sem`, assigned without repetition evidence, predicts that repetition intensifies rather than produces ordinary redundancy in held-out form families.

A failed CABNC feasibility gate therefore changes the direct test; it does not authorize extracting a forward-projectibility result from the existing morphology, _fie_, or GloWbE datasets.
## Work order
1. Implement acquisition, manifest, CHAT parser, and parser tests.

2. Produce raw form and turn-initial census with no target outcomes summarized by category.

3. Freeze the conservative collection-block hierarchy and the timing-bounded known-speaker turn rule; manually adjudicate sampled exact conversations.

4. Freeze the broad candidate lexicon, retrieval bins, sign-types, strict outer blocks, component exclusions, and pathway relations.

5. Confirm the ten-coder staffing gate and finalize the generative model skeleton, priors, prior-predictive checks, and simulation-based calibration on synthetic data.

6. Build disjoint dossier, source-classification, pre-offset cue/eligibility, token-assignment, and post-offset trajectory packets for the fixed 160-event double-coded pilot.

7. Run reliability, leakage, cell-yield, posterior-predictive design, and simulation gates without estimating a publishable category effect.

8. If the gates pass, preregister the confirmatory study and its claim-to-result map.

9. If they fail, activate the semantic-repetition fallback.


Only after Step 7 should the manuscript's projectibility section be assigned either a demonstrated-study or prospective-hypothesis architecture.
