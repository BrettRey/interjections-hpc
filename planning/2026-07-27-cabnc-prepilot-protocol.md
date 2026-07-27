# CABNC pre-pilot protocol
## Decision
Run a transcript census and a small blinded feasibility pilot before reconstructing the manuscript's central projectibility section. Do not treat the pilot as evidence for the projection. Its purpose is to determine whether a confirmatory test can be made interpretable, independent, and adequately powered.

The CABNC study tests two symmetrical, edge-specific claims:

> Independently assigned `INTERJECTION_sem` membership improves prediction of post-offset floor-transfer trajectory for unseen component-blocked form families beyond a category-free baseline of matched immediate cues, independently assigned neighbouring classifications, and symmetrically available form covariates.

> Independently assigned `INTERJECTION_syn` membership improves prediction of the same target over the same baseline and folds.

The two co-primary contrasts are paired within one predeclared multilevel predictive model family. Success on either edge cannot rescue failure on the other. Conditional `sem | syn` and `syn | sem` contrasts diagnose complementarity; they are not additional projectibility tests. If the paper-level claim requires both cuts to have projective standing for this target, support is conjunctive.

The study does **not** by itself establish the three-category ontology, `INTERJECTION_prag` as a source category, causal direction, network order, stability, or transport beyond the corpus population. Floor-transfer trajectory is an interactional target property, not identical to `INTERJECTION_prag` membership. No interaction term or joint-membership result is interpreted as showing that the intersection of `syn` and `sem` is a fourth category.
## Why a pre-pilot is necessary
The existing project datasets cannot support this declaration. The morphology sample contains four preselected derivative families and an all-positive retained-semantics outcome; the _fie_ study contains one sign-type; and GloWbE lacks token-level sequential outcomes.

CABNC supplies natural conversation, transcript timing, and linked audio, but four feasibility facts remain unknown:

1. whether enough independently classified positive and negative form families survive disambiguation;

2. whether a mechanically anchored post-offset trajectory can be coded reliably without importing the source classifications;

3. whether `syn` and `sem` have enough discordant cases to estimate separate edges;

4. whether category-level information contributes anything beyond target-TCU completion, action type, prosody, and other immediate cues.

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

Transcripts are stated to be CC BY 3.0 in the repository README and TalkBank landing page. Audio remains subject to the original BNC research-use conditions. The transcript-only census requires no credentials; the current TalkBank download endpoint presently requires authentication. Audio will not be acquired or exposed to a local acoustic expert until Humber provides a written REB determination.
## Gate 0: authority and audio feasibility

Before event sampling or annotation-packet generation:

1. obtain Humber's written REB determination for CABNC audio access and local expert exposure;
2. confirm authenticated AudioBNC access and the permitted local-storage workflow;
3. audit 40 timed events spanning at least eight declared pilot blocks for target-tier location, clip completeness, waveform alignment, and recoverable participant identity;
4. convert each permitted clip locally to frozen-format lossless PCM WAV, then generate a time-scaled waveform, spectrogram, and 10-ms energy-activity proposal with frozen local code;
5. have a source-label-blind expert audit the proposed target offset and first-audible, first-vocal, and first-word-or-particle boundaries while listening to the WAV; require the algorithm--expert absolute difference for the boundary used in the primary derivation to have median no greater than 50 ms and 95th percentile no greater than 100 ms; and
6. activate the semantic-repetition fallback if authority, access, alignment, or measurement quality fails.

Gate 0 is evaluated before any annotation packet is generated. Transcript availability cannot waive the audio requirement after outcomes are visible.

Waveforms, spectrograms, and energy-activity proposals are measurement aids, not ground truth. Monophonic recordings may contain overlap, laughter, clicks, breaths, and handling noise. Raw audio and derived acoustic artifacts remain local unless the written authority and AudioBNC conditions explicitly permit hosted processing; hosted models receive transcript and evidence-card packets only.

The frozen local preparation utility is `analysis/prepare_cabnc_audio.py`. It accepts an already authorized local audio path plus explicit event ID, clip bounds, output root, and generation timestamp; it does not download or discover AudioBNC audio, locate a TCU, identify or align speakers, adjudicate an onset, or derive a trajectory. Its exact interface is:

```bash
python3 analysis/prepare_cabnc_audio.py \
  --input /approved/local/path/source-audio.ext \
  --output-root /approved/local/path/prepared-events \
  --event-id OPAQUE_EVENT_ID \
  --start-ms 123000 \
  --end-ms 136000 \
  --generated-at 2026-07-27T00:00:00Z
```

The manifest supplies the bounds and timestamp. The utility refuses an invalid event ID or an existing event directory, converts only that interval to 16-kHz mono signed-16-bit PCM WAV, and writes the WAV, waveform, spectrogram, 10-ms adaptive energy-activity proposal, and provenance hashes. Its energy flags cannot distinguish speech, laughter, breath, clicks, handling noise, or overlapping speakers. Listening and source-label-blind expert boundary audit therefore remain mandatory, and the utility and all outputs run and remain only on the approved local storage volume unless written authority says otherwise.
## Operational bearer and holdout
The operational sign-type is a conventionalized constructional use defined by a form family plus a profile that may include grammatical, semantic, or interactional contrasts. No domain has priority in fixing the bearer. A sign-type is never split because target tokens happen to receive different post-offset trajectories.

Standalone, prenominal, and complement-taking _damn_ illustrate sign-types distinguished grammatically. Conventional meaning contrasts or independently established interactional-action contrasts may equally distinguish sign-types. All sign-types belonging to one form family remain in the same outer fold. If uses of _oh_ differ only in the target outcome and no independent profile contrast distinguishes them, they remain unsplit for this declaration.

The primary outer evaluation holds out the entire conservative form block and also removes directly related component-bearing constructions from training. All variants, sign-types, and tokens of the block remain outside training. A weaker ordinary outer-block analysis is diagnostic only. A pathway-blocked sensitivity additionally removes independently documented recruitment or descent relatives. The primary prediction integrates over new speaker and conservative collection-block effects rather than exploiting identities learned from other forms; a secondary conditional analysis may ask about a new form used by an otherwise observed speaker or interaction. This establishes lexical generalization within CABNC, not unrestricted projectibility to new varieties or periods.
## Three separated evidence layers
### Layer 1: sign-type dossier
The dossier assigns `INTERJECTION_syn`, `INTERJECTION_sem`, and neighbouring-category labels using external sources and CABNC conversations reserved exclusively for dossier construction. Every corpus-derived dossier collection block and every resolved or unresolved matching speaker is reserved away from target events. There is no yield waiver. Dossier events never enter confirmatory evaluation.

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

A dossier compiler first compiles the evidence with form identity visible. `INTERJECTION_syn`, `INTERJECTION_sem`, and each neighbouring classification are judged in separate randomized, one-shot passes, one classification per row. No conversation state, rationale, or output carries between passes. Declaration-specific cards precede full-profile cards; presentation order, form masking, form guesses, decisive evidence IDs, and prohibited-evidence exposure are recorded. Agreement between evidence-only and ordinary classifications is a leakage diagnostic, not a requirement that a model fail to recognize a familiar form. Reliability gates apply to `syn` and `sem` separately; no combined result can pool an unreliable component with an easier one.

Every corpus-derived dossier fact records its segment, conservative collection block, sampled conversation block where available, and speakers. These units are reserved before target sampling. A mechanical audit checks dossier/target block and speaker disjointness before labels are joined.

Target tokens receive a separate panel-coded, pre-offset token-to-sign-type assignment. Model runs see opaque frozen sign-type rules, but no category membership or post-offset sequence. This layer resolves homographic and constructional uses without improvising the category-to-outcome join after coding. It has its own stability, agreement, expert-audit, and indeterminacy gates; a token cannot be reassigned because its outcome is inconvenient.
### Layer 2: target-token cue coding
Separate fresh model-panel passes assign only information available by the acoustic offset of the target-bearing turn-constructional unit. Hosted models receive redacted transcript/evidence cards rather than raw audio. Any acoustically based cue in a card comes from the frozen local measurement layer and retains its provenance. These variables supply the non-category comparators:

- position within the IPU-style analytic span and TCU;

- standalone or syntactically integrated realization;

- judged TCU completeness at the crop point;

- clause type and prior action type;

- addressivity and number of available recipients;

- summons status and projected source continuation;

- duration, syllable count, and speech rate;

- prosodic independence;

- pre-target pause and pre-offset overlap;

- directly observable stance polarity or intensity;

- repetition and complement presence;

- lexical frequency or familiarity from a source frozen independently of outcomes.


The cue passes see no dossier labels, post-offset timing, recipient action, outcome summaries, or predictions. Every timing field records whether it was audio-measured, transcript-derived, interpolated, estimated, or unavailable, together with effective resolution. Prosodic judgements record their audio or transcript basis. Form-level frequency and familiarity are joined from an independently frozen, hashed source rather than supplied by the model passes.

### Layer 3: post-offset floor-transfer measurement

The local acoustic expert sees the complete target-bearing event and ensuing sequence but no source-category labels, source-cell summaries, predictions, or model output. The lexical form remains audible; source-label blinding, rather than impossible form masking, protects this layer. A separate fittedness panel receives only the material required for the labelled secondary sensitivity and never assigns the primary outcome.

First record mechanical observations, using the locally audited acoustic artifacts and listening where required:

- target-TCU acoustic offset and its timing provenance;

- separate first-audible, first-participant-vocal, and first-word-or-particle onsets;

- identity of the participant producing the first new vocal onset;

- signed latency from the target-TCU offset;

- whether valid simultaneous or competitively overlapping onsets cannot be uniquely ordered;

- whether no new participant-produced vocal onset occurs by 1.5, 2.0, and 2.5 seconds; and

- technical or context problem.

Frozen code calculates signed first-audible, first-vocal, and first-word-or-particle latencies as onset minus target-TCU offset: positive for a post-offset gap, zero for boundary alignment, and negative for overlap. It derives the 2.5-second field from audited first-vocal timing, speaker identity, and valid unordered-onset status. Continuous signed first-vocal latency is reported alongside the categorical result.


Frozen code, rather than a target annotator, derives the four-way primary trajectory at 2.5 seconds:

- `DIFFERENT_SPEAKER_FIRST_VOCAL_ONSET_2500`;

- `SOURCE_SPEAKER_FIRST_VOCAL_ONSET_2500`;

- `NO_NEW_VOCAL_ONSET_2500`; or

- `UNORDERED_COMPETING_ONSETS_2500`.

An isolated inbreath or non-vocal handling noise is not a participant-produced vocal onset. A uniquely ordered onset may begin before target offset and therefore have negative signed latency. The fourth level is used only when valid competing onsets cannot be uniquely ordered, not whenever the uniquely first onset happens in overlap. Speaker ambiguity, corrupt or insufficient audio, and other technical failures produce `uncodable` missingness rather than a fifth substantive trajectory.

Recipient status, minimality, fittedness, same-trajectory continuation, and uptake are separately coded secondary fields and cannot change the primary label. The same frozen code reports 1.5- and 2.0-second summaries as threshold sensitivities. Uncodable and technical-failure rates are reported by source cell; differential attrition can fail the feasibility gate.
## Context windows and eligibility
The source-side packet contains up to two preceding TCUs, capped at 12 seconds, and the complete target-bearing TCU. It stops exactly at acoustic offset and contains no post-offset silence, recipient onset, later continuation, or following transcript.

The target packet contains the same preceding context and target-bearing TCU, then continues through the later of five post-offset seconds or two subsequent complete TCUs, capped at 12 seconds. Additional-context requests receive a separate logged status. `context_insufficient=yes` is entered only when the final permitted packet remains insufficient after any granted request and is therefore terminally uncodable.

Pre-offset eligibility panel passes see no following sequence. They judge intelligibility, participant identity, potential-recipient availability at offset, timing adequacy, quotation, metalinguistic mention, and reading aloud. Frozen code separately checks that the following packet is unclipped, nonduplicated, uncorrupted, and correctly bounded. The two layers are joined mechanically; actual response or nonresponse cannot determine potential-recipient availability.

Same-speaker continuation, silence, overlap, and candidate-only TCUs are outcomes or descriptive properties, not automatic exclusions. Untimed events remain in the census, but an event without adequate audio timing fails the primary study's pre-offset timing criterion rather than receiving an estimated trajectory.

The primary trajectory study requires audio-measured timing at a declared resolution. If REB approval, audio access, or measurement quality is unavailable, CABNC cannot be converted after coding into a transcript-timed 2.5-second study. The semantic-repetition fallback is activated.
## Census and form-family rules
Parse only `data/cabnc_talkbank_chat/**/*.cha`. Construct logical CHAT tiers before tokenization and respect episode and file boundaries. Construct IPU-style analytic spans, not interactional turns: join adjacent tiers only when they have the same known listed speaker, both boundary times are present, and the within-speaker gap is under 180 ms. Unknown identities, missing timing, speaker changes, and gaps of 180 ms or more force a split. Preserve the original same-speaker chain and a boundary-reason code for every join or split. Preserve all timing spans and flag rather than silently repair missing or inconsistent metadata.

The canonical parser 0.6.0 rerun emits `analytic_spans.csv` and `span_initial_vocabulary.csv`. It produced 244,922 analytic spans while leaving the 255,211 retrieved occurrences unchanged. Sixteen otherwise eligible same-speaker boundaries were exactly 180 ms and were correctly split under the strict `<180 ms` rule. The parser contains no 2.5-second outcome logic; that threshold belongs only to the later locally audited target derivation.

A candidate is analytic-span-initial only if it is the first lexical token of the first main tier in the IPU-style span. Ignore CHAT markup, explicit noise codes, and transcription comments; do not skip filled pauses or response forms. Preserve raw, normalized, retrieval-bin, and form-block representations. Target-bearing TCU boundaries and same-speaker self-continuations in sampled material are adjudicated separately from acoustic spans using source-label-blind packets.

Use a versioned explicit alias table. Do not use stemming, edit distance, or model-generated clustering. Begin conservatively:

- keep _oh_ and _ooh_ separate;

- keep _yes_, _yeah_, and _yah/ya_ separate;

- keep _mm_, _mhm_, and _uh-huh_ separate;

- combine _ok_ and _okay_ only if an explicit phonological-family rule is accepted;

- normalize lengthened spellings only through enumerated aliases;

- place any aliases later combined in the same holdout fold.


Homographic forms such as _right_, _well_, _dear_, _god_, _great_, _please_, _sorry_, _thanks_, _shit_, _fuck_, and _damn_ enter the census as candidates, not as interjection tokens. Source-side adjudication determines constructional use without seeing the following sequence.

The census retains every occurrence and attaches flags. The study-eligible subset is derived only afterward. Every output row must trace back to corpus commit, collection block, tape, tape side, file, episode, tier, analytic span, original same-speaker chain, boundary reason, parser version, and alias-table version. The three-character BNC prefix is the conservative dependence block for corpus-wide spread; spans, transcript files, tape sides, and tapes are not called turns or conversations. Exact sampled conversation and TCU boundaries require separate manual adjudication.
## Sampling structure
After the raw census, stratify sign-types by the four source combinations:

- `syn+ / sem+`;

- `syn+ / sem−`;

- `syn− / sem+`;

- `syn− / sem−`.


The negative and discordant cells deliberately include neighbouring categories and controls; the yield gate does not require 24 strict interjection families. Candidate controls include supplements, expressives, response tokens, discourse markers, routine formulae, fillers, minimal lexical responses, vocatives, parentheticals, nonlexical vocalizations, and ordinary one-word TCUs.

The bounded pre-pilot begins with 240 pre-offset candidates: fifteen from each of sixteen source-selected outer blocks, frozen before outcome inspection: _oh_ and its anchor constructions, _ooh_, _ah_, _eh_, _ha_, _cor_, _ugh_, _gosh_, _mm_, _er/erm_, _yes_, _no_, _well_, _right_, _mum_, and _thanks/thank you_. Each fifteen-event pool is built by scanning its frozen SHA-256 rank and skipping candidates that would breach a within-block concentration cap. Target selection then scans eligible and assigned candidates in round-robin order, within-block rank first and frozen block order second. A candidate that would breach a global cap is logged and skipped, and scanning continues. The first ten admitted events per block proceed to target measurement, for at most 160 target packets. Opaque identifiers replace the labels in annotation packets. A block yielding fewer than ten eligible assigned and cap-compliant events is a feasibility failure, not an invitation to substitute a block after outcomes are known.

_Mum_ is deliberately a kinship-term vocative-NP control, not a presumed negative member of either interjection category. Source-only sign-type assignment distinguishes standalone summonses, supplementary vocatives within larger TCUs, and referential nominal uses. It tests whether the `syn` edge adds anything beyond supplement function, prosodic isolation, and standalone packaging; for `sem`, it is an adversarial neighbour whose polarity remains to be adjudicated. Addressivity, summons status, TCU completeness, and projected source continuation belong in the category-free immediate-cue layer.

The sixteen blocks test source-side variation and annotation feasibility. They are not preassigned to positive or negative `syn` or `sem` cells.

Within each pilot block, admit at most two candidates per speaker and two per collection block. Across selected target packets, no speaker may exceed 5% and no collection block may exceed 10%. Evaluate feasibility only after all 240 pre-offset packets and all selected target packets reach their declared stages. At least eight of ten selected targets per retained block must yield a primary-codable trajectory. Every pilot occurrence is excluded from both confirmatory training and confirmatory scoring; fresh occurrences from the same outer blocks may enter confirmation.

Require at least 25 eligible target events across at least 10 conservative collection blocks for each retained family before expert sampled-conversation adjudication. Cap each speaker's and collection block's contribution. Prefer 40–80 events per family and cap extremely frequent families so _oh_, _yeah_, and _mm_ do not dominate.

For each co-primary edge, require at least six form blocks and roughly 150 events on each side of its matched contrast in the confirmatory design. A block is positive only when every retained sign-type has final declaration-specific `yes` for that edge, and negative only when every retained sign-type has `no`; mixed or uncertain blocks count toward neither per-side minimum. Sparse discordant cells can limit or defeat one edge without deciding the other. They do not authorize a post hoc joint representation or any inference that the intersection is an additional category.
## Predictive estimand

The co-primary estimands are the expected changes in predictive quality for the four-way floor-transfer distribution when declaration-specific `INTERJECTION_sem` and, separately, declaration-specific `INTERJECTION_syn` are added to the same category-free baseline for a token from a previously unseen component-blocked form family. The token is produced by a speaker in a collection block drawn from the study's CABNC sampling frame. The two contrasts use identical folds and therefore support paired estimation of their block-level score differences and covariance.

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

The model arms share the same outcome model, folds, sampling frame, and symmetrically available covariates. Priors need not be mechanically identical when parameterizations differ; each arm receives priors calibrated to the same substantive scale and checked through the same prior-predictive workflow. Speaker, collection-block, form-block, and trajectory-specific effects are partially pooled under regularizing priors. The `syn` and `sem` coefficients are jointly estimated where both are present, but they are not forced into a two-member exchangeable hierarchy merely to invoke partial pooling.

After fitting, posterior-predictive checks examine trajectory prevalence, within-block distributions, speaker, collection-block, and sampled-conversation clustering, residual form and pathway structure, and whether the model reproduces the observed concentration of rare trajectories. Held-out calibration is reported by outer block, not only in the pooled sample.

## Model comparison

1. **Base rate:** outcome prevalence estimated from training data.

2. **Immediate-cue model:** only Layer 2 token-local variables.

3. **Matched common baseline:** immediate cues, independently assigned neighbouring classifications, external form frequency/familiarity, and symmetrically available covariates. It contains neither interjection-category label.

4. **Flat-diagnostic model:** the matched common baseline plus the unstructured Layer 1 diagnostic vector available under the same declaration-specific evidence mask, with no interjection category labels.

5. **`B + sem`:** the matched common baseline plus declaration-specific `INTERJECTION_sem`. Its held-out improvement over `B` is the co-primary semantics-facing test.

6. **`B + syn`:** the matched common baseline plus declaration-specific `INTERJECTION_syn`. Its held-out improvement over `B` is the co-primary grammar-facing test.

7. **`B + syn + sem`:** supplies two conditional complementarity diagnostics: `B + syn` versus `B + syn + sem`, and `B + sem` versus `B + sem + syn`. These measure non-redundancy conditional on the other cut and are not additional projectibility tests.

Full-profile memberships appear only in labelled sensitivities. No confirmatory `syn × sem` interaction is fitted, because it would invite the false suggestion that the overlap is a fourth category.


The complete eligible flat-diagnostic vector is an information-rich upper comparator. It may contain mixed-domain evidence but never the withheld target or a prohibited proxy. The category model is not required to beat a deterministic function of its complete eligible evidence. Its scientific value lies in calibrated generalization and compression under partial observation. Compare predictive performance together with predictor count, coding burden, and calibration; do not claim unique information after conditioning on the complete diagnostic basis.

Primary evaluation uses macro-averaged held-out log score or expected log predictive density, multiclass Brier score, calibration intercept, and calibration slope. Report all four score contrasts jointly at the held-out block level, including their paired differences and covariance. A claim that one cut contributes more than the other must use the direct paired contrast; it cannot be inferred because one edge crosses a threshold and the other does not. Also report each block's score contribution and uncertainty, group-level variance posteriors, shrinkage diagnostics, and blocks for which a category representation performs worse than the base rate. Accuracy is not a primary metric.

The preregistration will define a practically negligible region and a useful-prediction region on the scoring scale from scientific utility and coding burden before pilot outcomes are inspected. Pilot-derived variance components may inform feasibility simulations but cannot move these regions. Conclusions use both the full uncertainty distribution and those declared regions. This preserves a risk-bearing decision rule without reducing the analysis to one threshold or inviting an unspecified posterior to “speak for itself.”
## Claim-to-result map
| Result | Warranted conclusion | Manuscript consequence |
| --- | --- | --- |
| `B + sem` beats `B`, is calibrated, and meets its prespecified margin under component-blocked folds | `INTERJECTION_sem` supports transportable prediction of floor transfer in unseen CABNC form blocks | Report that corpus-bounded edge only |
| `B + syn` beats `B`, is calibrated, and meets its prespecified margin under the same folds | `INTERJECTION_syn` supports transportable prediction of the same target | Report that corpus-bounded edge only |
| The joint uncertainty distribution for both co-primary edges clears their simultaneous lower bounds and calibration tolerances | Both tested cuts have projective standing for this target and scope | Permit the conjunctive paper-level claim, without implying an intersection category |
| A conditional complementarity contrast succeeds | One cut preserves useful distinctions after the other is supplied | Report non-redundancy, not independent category legitimacy |
| Category model approaches the flat-diagnostic model with materially less information or coding burden | The category provides useful scientific compression | Report compression without claiming new information beyond full diagnostics |
| Flat diagnostics beat the category label | The label discards predictive information contained in its diagnostic basis | Retain only a weaker compression claim if the declared margin is met; otherwise demote the edge |
| Immediate cues or `B` equal or beat one category arm | Local action formation and rival classifications suffice for that edge under this design | Kill that edge; success of the other cannot rescue it |
| Neighbouring classifications beat both tested interjection cuts | The relabelling objection survives for this outcome; an interaction-facing representation may carry more sequential information | Do not claim distinctive payoff for the tested cuts; treat the interaction-facing interpretation as a prospectively specified hypothesis, not proof of `INTERJECTION_prag` |
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

- the frozen model registry, isolated pass manifests, expert-audit assignments, and layer separation prevent `syn`, `sem`, neighbour, cue/sign-type, and target information from carrying across roles;

- adjudication of one layer does not consult the other;

- timing, filenames, clip length, transcript truncation, and annotation order cannot reveal the target to source model passes;

- a random 10% of source packets matches the original transcript and audio boundaries;

- pilot outcomes were not used to tune membership criteria, block relations, scoring regions, or confirmatory defeat thresholds;

- token-to-sign-type assignments were made from pre-offset packets and opaque rules;

- panel-coded pre-offset eligibility and mechanical packet eligibility were joined without reference to trajectory;

- every timing value has declared provenance and primary events are audio-measured;

- primary outcomes were derived by frozen code from audited first-vocal-onset timing and speaker identity, with `uncodable` handled as missingness rather than as a substantive class;

- all declared checklist items are present, and every failure is handled according to its prospectively assigned class: halt, remediable before unblinding, or note only.


The report must discuss three unavoidable construct-validity risks. Standalone or complete grammatical packaging can itself create transition relevance; expressive action can itself normatively constrain a response; and fittedness judgements can import an analyst's semantic or interactional construal of the source. The mechanical trajectory, fittedness sensitivity, immediate-cue comparator, and flat-diagnostic comparator separate these routes as far as the design permits.
## Reliability and feasibility gates
Proceed to confirmation only if all applicable gates pass:

1. The frozen Claude-, Gemini-, and GPT/Codex-family model registry, isolated pass manifests, provider routes, checkpoints, prompts, schemas, settings, and author-audit plan are complete before packet release.

2. The pinned commit, subtree object, file count, tier count, and per-file hashes are reproduced.

3. Candidate extraction is deterministic, every warning is logged, and a blinded sample establishes acceptable extraction precision.

4. Conservative collection blocks are validated and used for corpus-wide independence; file segments, tape sides, and tapes are not counted as conversations by assumption. Exact conversations are adjudicated for sampled material.

5. Each co-primary confirmatory contrast independently has at least six form blocks and about 150 events on each side after component blocking.

6. At least half the retained blocks exhibit more than one primary trajectory; no primary trajectory is vanishingly rare.

7. In the pre-pilot, `INTERJECTION_syn` and `INTERJECTION_sem` each separately reach nominal alpha of at least .80 and raw agreement of at least .85. The principal neighbour labels -- expressive, response token, discourse marker, routine formula, filler, vocative, and supplement -- each reach nominal alpha of at least .75 and raw agreement of at least .80. Confidence intervals are reported but do not gate the small pilot. Confirmatory lower-bound requirements are frozen separately after design calculations establish an adequate number of dossiers.

8. In the pre-pilot, token-to-sign-type assignment reaches nominal alpha of at least .80 and raw agreement of at least .85.

9. Every critical source card is run twice for each model family in fresh stateless contexts. Within-family repeat agreement is at least .90 for `syn` and `sem` and .85 for other principal subjective fields. A concealed hash-selected 15% duplicate set supplies the corresponding stability check for high-volume token and cue fields.

9a. Each principal categorical immediate cue -- syntactic packaging, TCU completeness, prior action, addressivity, summons status, projected source continuation, and prosodic independence -- reaches nominal inter-model alpha of at least .70 and raw agreement of at least .80.

9b. Panel--audit raw agreement reaches .85 for `syn` and `sem` and .80 for remaining subjective fields. Brett reviews every source-category and principal-neighbour dossier, every token-assignment disagreement and model instability, and a frozen random sample of consensus cue assignments. He audits every acoustic boundary used in the primary derivation while blind to source labels.

9c. The local waveform/spectrogram/energy-activity proposal satisfies the algorithm--expert boundary gates in Gate 0. The mechanically derived four-way primary trajectory has no inter-model alpha because models do not assign it.

10. No required subjective primary field has more than 15% combined uncertain and uncodable values, and no more than 15% of derived primary outcomes are uncodable. The maximum absolute difference across source cells in exclusion, outside-contrast, or technical-failure rates is no greater than 10 percentage points.

11. All enumerated leakage checks pass under their prospectively assigned failure classes.

12. No outer block, speaker, collection block, or sampled conversation dominates the effective sample.

13. Simulation-based design analysis spans plausible null, small, and useful effects and variance components, and shows that the proposed design can distinguish scientifically different data-generating processes with tolerable rates of false warrant, missed warrant, and ambiguity. The full operating-characteristic curves are reported; no isolated 80% threshold substitutes for them.

14. The immediate-cue model is not already effectively deterministic.

15. All 240 pre-offset candidates and every target packet selected by the frozen rule reach the single evaluation point; there is no interim optional stopping.

16. Every pilot occurrence is excluded from confirmatory training and scoring. Fresh occurrences from the same frozen outer blocks may enter confirmation.

17. The pathway-blocked sensitivity is interpreted for an edge only if at least ten training outer blocks remain, including at least four blocks on each side of that edge's frozen contrast.


Report Krippendorff's nominal alpha, Gwet's AC1 under extreme prevalence, raw agreement, confusion matrices, within-model repeat agreement, panel--audit agreement, and cluster-bootstrap intervals by form family. Use weighted kappa only for ordinal confidence fields. Call agreement across Claude, Gemini, and GPT **inter-model agreement**, not human intercoder reliability or three independent samples from a human annotator population. Report acoustic measurement agreement separately. The thresholds remain operational pilot gates, but design simulations must also show how observed misclassification would attenuate or distort the substantive estimates; a composite label does not pass merely because its headline agreement coefficient clears a cutoff.

Passing these gates shows that a valid confirmatory study is feasible. It is not evidence that the projection succeeds.
## Frozen model panel, audit, and automation
The lead owns the protocol, thresholds, theoretical interpretation, and all manuscript prose.

Subjective annotations use one Claude-family model, one Gemini-family model, and one GPT/Codex-family model. The exact checkpoints, provider routes, system prompts, decoding settings, JSON schemas, and invocation dates are frozen before a layer begins. Claude 5 is routed through Claude Code; Claude 4.6 and Gemini models are routed through Agy while those allocations remain available; the GPT-family run uses Codex. A local open-weight model may be added as a portability stress test, but it does not create another chance for the declared panel to pass.

Each critical source card is sent twice to every family in fresh stateless contexts with tools, browsing, memory, and manuscript access disabled and independently randomized card order. Raw responses, evidence-span references, refusals, parse failures, prompt hashes, and model/version identifiers are retained. A family contributes a source-category vote only when its two runs agree. Confirmatory `yes` or `no` requires three stable family votes in agreement plus Brett's source-only, outcome-blind confirmation; anything else remains `uncertain`. A provider change during a layer requires rerunning that entire layer under one newly frozen checkpoint before outcomes are inspected; versions are not silently pooled.

For token assignment, immediate cues, and secondary fittedness, a frozen consensus rule is piloted before use. Brett's audit is a separate validity check, not another model vote or a substitute for a panel. Source-field audits never expose outcomes, and target/acoustic audits never expose source labels. Stateless prompting constrains information flow but cannot erase pretraining knowledge; evidence grounding, form-guess records, and prohibited-evidence checks diagnose that limitation.

- **Codex engineering agent:** parser tests, manifests, deterministic extraction, fold integrity, and reproducibility checks.

- **Independent methodology agent:** leakage audit and claim-to-result mapping without access to linked outcomes.

- **Agy/Opus 4.6 Thinking:** construct-validity and philosophy-of-science review at the protocol and frozen-analysis gates.

- **Agy/Gemini 3.1 Pro:** independent corpus/sampling audit. Its numerical yield claims are treated as hypotheses until reproduced.

- **Claude Code/Claude 5:** Claude-family annotation route and high-stakes final methodological or prose judgement.

- **Local models:** optional portability stress tests, candidate triage, alias or homograph flags, schema-format checks, and contradiction searches. They do not create extra panel votes, derive the primary trajectory, overrule audited acoustic boundaries, or determine inclusion.


No raw model output is a datum about the linguistic population. Frozen, evidence-grounded panel judgements, source-blind expert audit, deterministic parsing, and locally audited acoustic measurements are the annotation and measurement basis.

## CHILDES disposition

Keep CABNC as the primary corpus. CHILDES changes the population, register, recipient, and often the observability of uptake at the same time: caregiver–child interaction is structured by development, scaffolding, repeated family routines, and substantial nonverbal response. It therefore cannot silently replace CABNC while preserving the adult-conversation estimand.

The strongest CHILDES use is an external developmental/register replication after the CABNC representation and analysis are frozen:

- Use the [HSLLD](https://talkbank.org/childes/access/Eng-NA/HSLLD.html) mealtime material, restricted to adult-produced target turns. It offers the broadest plausible family base, but its audio is unlinked, so the target must be the next **verbal** contribution rather than fine timing, overlap, silence, or nonverbal uptake.
- Use the linked-audio dinner subset of [Gleason](https://talkbank.org/childes/access/Eng-NA/Gleason.html) as a smaller audit of transcript-only classification, not as a silently pooled source of extra sample size.

Within HSLLD, all sessions and speakers from one family remain in the same resampling unit; intended addressee, recipient role and age, visit, activity, and next-speaker role are mandatory. A successful result would show transport to caregiver–child mealtime interaction. A failure would not by itself defeat the adult CABNC claim.

CHILDES downloads now require TalkBank registration and carry corpus-specific Ground Rules. Raw CHILDES transcript or media content remains local unless the actual hosted-model route has verified non-storage terms; local models may assist only within the mechanical and human-validated limits stated above.

## Predeclared fallback

If CABNC fails because floor-transfer trajectory cannot be separated from immediate action-formation cues, because either declared contrast is unidentified, because the model-panel separation or audit cannot be implemented, because audio-measured timing is unavailable, or because reliable boundary measurement is impossible, do not force a corpus result or substitute a developmentally different CHILDES result. Move to the independently normed semantic-repetition experiment already identified in the feasibility review. That experiment tests whether `INTERJECTION_sem`, assigned without repetition evidence, predicts that repetition intensifies rather than produces ordinary redundancy in held-out form families.

A failed CABNC feasibility gate therefore changes the direct test; it does not authorize extracting a forward-projectibility result from the existing morphology, _fie_, or GloWbE datasets.
## Work order
0. Obtain the written REB determination, confirm authenticated audio access and storage conditions, and pass the 40-event audio/alignment audit.

1. Implement acquisition, manifest, CHAT parser, and parser tests.

2. Produce the raw form and analytic-span-initial census with no target outcomes summarized by category.

3. Freeze the conservative collection-block hierarchy and the under-180-ms known-speaker IPU-style span rule; manually adjudicate sampled TCUs, self-continuations, and exact conversations.

4. Freeze the broad candidate lexicon, retrieval bins, sign-types, strict outer blocks, component exclusions, and pathway relations.

5. Freeze the three-family model panel, isolated-pass and audit manifests, and the paired four-arm generative model skeleton; complete priors, prior-predictive checks, and simulation-based calibration on synthetic data.

6. Build disjoint dossier and source-classification packets plus 240 pre-offset cue/eligibility and token-assignment packets; select at most 160 target packets by the frozen eligibility order.

7. Run reliability, leakage, cell-yield, posterior-predictive design, and simulation gates without estimating a publishable category effect.

8. If the gates pass, preregister the confirmatory study and its claim-to-result map.

9. If they fail, activate the semantic-repetition fallback.


Only after Step 7 should the manuscript's projectibility section be assigned either a demonstrated-study or prospective-hypothesis architecture.
