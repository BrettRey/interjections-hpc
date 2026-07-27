# CABNC bounded pre-pilot implementation manual

**Status:** Approved design implemented; execution remains blocked at Gate 0
**Governing documents:** [pre-pilot protocol](../../planning/2026-07-27-cabnc-prepilot-protocol.md), [approved amendment](../../planning/2026-07-27-prepilot-amendment.md), [architecture contract](../../planning/2026-07-27-architecture-contract.md), and [census decision report](../../planning/2026-07-27-cabnc-census-report.md)

## Purpose

This pre-pilot determines whether CABNC can support blinded, held-out tests of two symmetrical, edge-specific projections:

> Independently assigned `INTERJECTION_sem` membership improves prediction of post-offset floor-transfer trajectory for unseen component-blocked form families beyond a category-free baseline of matched immediate cues, independently assigned neighbouring classifications, and symmetrically available form covariates.

> Independently assigned `INTERJECTION_syn` membership improves prediction of the same target over the same baseline and folds.

The co-primary contrasts are paired within one predeclared multilevel predictive model family. Success on either edge cannot rescue failure on the other. Conditional `sem | syn` and `syn | sem` contrasts diagnose complementarity rather than serving as additional projectibility tests. No interaction or joint-membership result is interpreted as showing that the intersection is a fourth category.

It does not estimate either projection for publication. It tests whether the source classifications, comparison variables, floor-transfer measurements, grouping units, and holdout folds can be constructed without leakage and with adequate reliability and yield.

No finding from this pre-pilot establishes the three-category ontology, `INTERJECTION_prag`, causal direction, category-wide stability, maintenance, or corrective control.

Even the strongest later result would show, at most, calibrated compression and transport within the CABNC sampling frame. The category label is not expected to add information after its complete eligible diagnostic basis is known. A positive result would remain compatible with the classifications proxying stable sequential-design properties; the flat-diagnostic and neighbouring-category comparisons determine how much stronger an interpretation is warranted.

## Frozen declaration

| Field | Pre-pilot value |
|---|---|
| Source | Co-primary and edge-specific: declaration-specific `INTERJECTION_sem`; declaration-specific `INTERJECTION_syn` |
| Comparator | Common category-free baseline `B`: matched immediate cues, independently assigned neighbouring classifications, external form frequency or familiarity, and symmetrically available form covariates |
| Outcome | Four-way floor-transfer trajectory at 2.5 seconds: different-speaker first vocal onset; source-speaker first vocal onset; no new vocal onset; or valid unordered competing onsets. `Uncodable` is missingness |
| Bearer | Conventionalized constructional sign-type, nested in a conservative form-family holdout block |
| Population | Selected candidates and controls in the frozen CABNC sampling frame |
| Conditions | Intelligible target-bearing sequence with identifiable participants, a potential recipient, and an unclipped following window |
| Transformation | Primary component-blocked leave-one-outer-block-out evaluation; pathway-blocked sensitivity evaluation |
| Timescale | Signed latency from the acoustic offset of the target-bearing TCU; 2.5 seconds primary, with 1.5- and 2.0-second threshold sensitivities |
| Tolerance | Fixed from scientific utility and coding burden before pilot outcomes are examined; pilot variance informs feasibility, not the decision regions |
| Evidential standard | Blinded coding, disjoint source and target evidence, held-out predictive scoring, calibration, and design simulation |
| Failure conditions | Leakage, unreliable source or target coding, inadequate family/cell yield, indeterminate grouping, effectively deterministic immediate cues, or no useful held-out category advantage |

The source classification must not be revised in response to floor-transfer outcomes. A failed projection is demoted or retired under its declared scope; it is not rescued by redefining the bearer after target inspection.

## Identifier layers

The study must not use one overloaded “family” field. The final data model distinguishes:

1. `surface_alias_id`: one normalized string-matching rule and its intended bearer span;
2. `retrieval_bin_id`: a constructionally homogeneous search target emitted by the frozen census;
3. `sign_type_id`: an independently justified conventionalized constructional use;
4. `strict_variant_block_id`: spellings or phonological variants that must remain in one outer fold;
5. `principal_outer_block_id`: the complete unit removed in leave-one-family-out evaluation;
6. typed lexical and component relations that trigger sensitivity exclusions without creating transitive mega-families; and
7. `conversation_block_id`: the independently validated interaction/dependence group.

Retrieval bins are search devices. They do not become sign-types or holdout families merely because a string matcher assigned them an identifier.

All new identifiers are opaque. Category labels, neighbour labels, and expected outcomes never appear inside an identifier. The current census's descriptive `form_family_id` survives only as `legacy_form_family_id` for traceability.

The authoritative lexical/fold tables are `surface-aliases`, `retrieval-bins`, `sign-types`, `form-relations`, and `outer-block-membership`. `fold-map-template.csv` is only a convenient derived view and cannot override those tables.

## Roles and separation

| Role | May see | Must not see |
|---|---|---|
| Grouping/span adjudicator | Corpus metadata, IPU-style segmentation, relevant audio if approved | Category hypotheses or post-offset trajectory summaries |
| Dossier compiler | Form identity, external sources, dossier-only corpus evidence | Target-event outcomes and target-sample response frequencies |
| `INTERJECTION_syn` panel pass | Randomized standardized cards for the grammar-facing classification only | Semantic or neighbour decisions, target events, outcomes |
| `INTERJECTION_sem` panel pass | Randomized standardized cards for the semantics-facing classification only | Syntactic or neighbour decisions, target events, outcomes |
| Neighbour panel pass | One independently presented neighbouring classification at a time | Interjection-category decisions, target events, outcomes |
| Token-to-sign-type panel pass | Pre-offset event and frozen opaque sign-type rules | Category membership, post-offset sequence, outcomes |
| Immediate-cue and pre-offset eligibility panel pass | Preceding context and target-bearing TCU through acoustic offset | Dossier labels, post-offset silence or speech, outcomes |
| Acoustic expert | Local WAV, waveform, spectrogram, VAD proposal, and participant key | Source-category labels, source-cell summaries, predictions |
| Leakage auditor | Packet manifests, masks, hashes, joins, and coding histories | Linked unblinded analysis until audit is complete |
| Lead analyst | Frozen coded layers after audit | No role-specific exception; the lead may not repair labels from outcomes |

Each source or rival classification is run in a fresh stateless context. No conversation state, output, or rationale carries between `syn`, `sem`, neighbour, cue, token-assignment, or fittedness passes. Immediate cues are locked before token-to-sign-type assignment. Source-field expert audits never expose post-offset measurements, and acoustic/target audits never expose source labels.

The model-panel gate is evaluated before packet generation. Subjective fields use one Claude-family, one Gemini-family, and one GPT/Codex-family model. Exact checkpoints, provider routes, prompts, settings, schemas, and dates are frozen by layer. Every critical source card is run twice per family in fresh contexts; a source-category family vote exists only when its two runs agree. Brett's source-only and target-blind audit is a separate validity check, not another family vote. A local open-weight model may provide a portability stress test but cannot rescue the declared panel.

## Work order and freeze points

### Gate 0: authority and audio

1. Obtain Humber's written REB determination for CABNC audio access and local expert exposure.
2. Confirm authenticated AudioBNC access and the permitted local-storage workflow.
3. Audit 40 timed events spanning at least eight pilot blocks for target-tier location, clip completeness, and alignment.
4. Convert permitted clips locally to 16-kHz mono signed-16-bit PCM WAV, then produce time-scaled waveform, spectrogram, and 10-ms energy-activity proposals with frozen local code.
5. Have a source-label-blind expert listen and audit target offset plus first-audible, first-vocal, and first-word-or-particle onsets. For the boundary used in the primary derivation, require median absolute algorithm--expert difference no greater than 50 ms and the 95th percentile no greater than 100 ms.
6. If authority, access, alignment, or measurement quality fails, activate the semantic-repetition fallback before packet generation.

The local preparation command is [prepare_cabnc_audio.py](../prepare_cabnc_audio.py). It accepts an already authorized local audio file and explicit clip bounds; it does not download AudioBNC material, discover a TCU, align speakers, adjudicate an onset, or derive an outcome. Run it only on the approved local storage volume:

```bash
python3 analysis/prepare_cabnc_audio.py \
  --input /approved/local/path/source-audio.ext \
  --output-root /approved/local/path/prepared-events \
  --event-id OPAQUE_EVENT_ID \
  --start-ms 123000 \
  --end-ms 136000 \
  --generated-at 2026-07-27T00:00:00Z
```

The command requires `ffmpeg`, refuses an invalid event ID or existing event directory, converts the selected interval to a 16-kHz mono signed-16-bit PCM WAV, and writes a waveform PNG, spectrogram PNG, 10-ms frame-energy proposal CSV, and provenance JSON containing input, artifact, code, and command hashes. The supplied start/end bounds and timestamp must come from the frozen packet manifest. Energy flags are proposals only: they cannot distinguish speech from laughter, breath, clicks, handling noise, or overlapping speakers. The source-label-blind expert must listen and audit the boundaries. Audio and all derived artifacts remain local unless written authority explicitly permits otherwise.

### Gate A: interaction structure

1. Construct IPU-style analytic spans, not turns: join adjacent tiers only for the same known listed speaker when both boundary times exist and the gap is under 180 ms.
2. Unknown identities, missing timing, speaker changes, and gaps of 180 ms or more force a split. Preserve the original same-speaker chain and a boundary reason for every join or split.
3. Use the three-character BNC prefix as `collection_block_id`, the conservative independence and separation block.
4. Retain tape, tape-side, segment, and manually adjudicated sampled-conversation identifiers as distinct levels.
5. Freeze sampled `conversation_block_id` values where the metadata and permitted audio support them. Adjudicate target-bearing TCU boundaries and same-speaker self-continuations separately from the acoustic spans.

The canonical parser 0.6.0 outputs are `analytic_spans.csv` and `span_initial_vocabulary.csv`: 244,922 analytic spans, with the 255,211 retrieved occurrences unchanged. The strict `<180 ms` rule splits all gaps at or above the threshold, including 16 otherwise eligible same-speaker boundaries exactly at 180 ms. No 2.5-second target rule exists in the parser; target thresholds are applied only after local acoustic audit.

No family-yield claim may use “conversation” before Gate A is frozen.

### Gate B: lexical and constructional structure

1. Freeze the broad candidate alias inventory.
2. Adjudicate strict variants without recipient evidence.
3. Record typed component and constructional relations, including the intended bearer span inside complex matches.
4. Define pilot sign-types from source-only evidence.
5. Freeze strict outer blocks, direct component exclusions, and diachronic/pathway relations.
6. Make component-blocked evaluation primary; preserve the ordinary outer-block evaluation as the weaker diagnostic analysis.

No target outcome may be inspected while making these decisions.

### Gate C: packet construction

1. Freeze the three-family model registry, isolated pass and duplicate manifests, consensus rules, and expert-audit assignments.
2. Freeze a SHA-256-ranked candidate order within each of sixteen declared pilot outer blocks without inspecting outcomes; scan it until fifteen candidates satisfying the within-block caps enter each pre-offset pool.
3. Reserve every dossier collection block and every resolved or unresolved matching speaker away from target events, without a yield waiver.
4. Generate full-profile source, declaration-specific source, and 240 immediate-cue/pre-offset eligibility packets.
5. Select targets in frozen round-robin order, within-block rank first and block order second; skip and log any candidate that would breach a global cap, then generate at most 160 floor-transfer measurement packets.
6. Hash every packet and verify masking automatically.
7. Assign pseudonymous `packet_event_id` values; keep the occurrence-ID and sign-type joins outside model and audit files.

### Gate D: isolated panel annotation and audit

1. Run `syn`, `sem`, and each neighbour in separated randomized one-shot passes, twice per model family for critical source cards.
2. Run immediate-cue and pre-offset eligibility passes, including the concealed duplicate subset.
3. Lock cue files, then run token-to-sign-type assignment with opaque frozen rules.
4. Prepare and audit acoustic boundaries locally; run secondary fittedness in its own isolated panel pass.
5. Apply the frozen stability and consensus rules; unresolved source judgements remain `uncertain`.
6. Complete Brett's outcome-blind source audit and source-label-blind acoustic audit.
7. Run the enumerated leakage audit before joining layers.

### Gate E: feasibility decision

Evaluate once, after all 240 pre-offset candidates and all selected target packets have completed their applicable layers. Compute source-category and neighbour inter-model agreement, within-family duplicate stability, panel--audit agreement, token-assignment and cue reliability, acoustic-boundary agreement, indeterminacy, block/cell yield, trajectory variation, differential attrition, dominance, and design-simulation diagnostics. All pilot occurrences are excluded from confirmatory training and scoring. Fresh occurrences from the same outer blocks may enter a later confirmatory sample.

## Layer 1: sign-type dossier

### Dossier unit

A dossier describes one proposed `sign_type_id`, not an orthographic string in the abstract and not an individual target token. Constructional distinctions may be grammatical, semantic, or independently established interactional distinctions. Target-treatment differences alone never justify splitting a sign-type.

### Evidence records

Each factual claim is stored in long form in `dossier-evidence.csv`. Required tags include:

- evidence domain: `phonology`, `morphology`, `syntax`, `semantics`, `interaction`, `diachrony`, or `other`;
- evidence source: publication, reference work, corpus segment reserved for dossier construction, or analyst judgement;
- bearer scope and variety;
- whether the fact is available for full-profile classification;
- whether it is available for this declaration-specific classification;
- whether it is the target, a prohibited close proxy, or safe source evidence; and
- citation, locator, and confidence.

The declaration-specific evidence card removes the target token's response, target-sample response frequencies, and the following close proxies:

- observed recipient uptake or fitted next action;
- treatment of the target event as a complete move;
- post-offset recipient onset or response latency;
- source resumption versus recipient action in the target window; and
- any summary computed from target packets.

Full-profile classification may contain independently established mixed-domain facts, but it is a labelled sensitivity variable rather than the primary source for this declaration.

### Required classifications

Each source-classification row contains one judgement only. `syn`, `sem`, and each neighbour are assigned in separate randomized one-shot panel passes. For both interjection classifications, record:

- `yes`, `no`, or `uncertain` full-profile membership;
- `yes`, `no`, or `uncertain` declaration-specific membership;
- confidence on the frozen ordinal scale;
- the decisive evidence record IDs; and
- an explicit account of any difference between the two judgements.

Declaration-specific cards are always run before full-profile cards. Card order and presentation position are recorded. A model pass cannot view the two card types side by side or inherit another pass's output. Form-masked cards record whether the form was guessed. If prohibited evidence is seen, the dossier is quarantined under a rule frozen before Gate C; it cannot be retained or removed after its target performance is known.

Record neighbouring classifications independently, one category per row: supplement, expressive, response token, discourse marker, routine formula, filler, vocative, parenthetical, nonlexical vocalization, ordinary lexical response, and other specified neighbour. A neighbour win is preinterpreted as evidence that an established interaction-facing or neighbouring representation carries more sequential information than the tested source cut. It does not by itself establish `INTERJECTION_prag`.

### Dossier reservations

Every corpus-derived evidence record names its segment, collection block, sampled conversation block where available, and speakers. A separate reservation table is populated at compilation time. Target sampling mechanically rejects every reserved collection block and every resolved or unresolved matching speaker. There is no yield waiver. Unlogged corpus evidence cannot enter a dossier.

### Token-to-sign-type assignment

The dossier defines sign-types, but target tokens enter the analysis only through a separate pre-offset panel assignment. Each run receives the cue packet and opaque sign-type rules. It assigns a token to one frozen `sign_type_id`, records alternatives and confidence, or marks it outside all frozen sign-types. It never sees category membership or the post-offset sequence.

This assignment has its own reliability and indeterminacy gate. A token cannot be reassigned because its floor-transfer trajectory is inconvenient. The analysis join between event, sign-type, and dossier is generated only after the leakage audit.

## Layer 2: immediate-cue coding

The cue packet ends at the acoustic offset of the target-bearing TCU. It contains up to two preceding TCUs, capped at 12 seconds, plus the complete target-bearing TCU. It cannot expose post-offset silence, a following tier, recipient onset, or the source speaker's later continuation.

Code what is locally observable rather than inferring a category label. Required fields include:

- analytic-span and TCU position;
- standalone or syntactically integrated realization;
- TCU completeness at crop point;
- prior action type and clause type;
- addressivity and count of potential recipients;
- summons status and projected source continuation;
- duration, syllable count, and speech rate when measurable;
- prosodic independence;
- pre-target pause and pre-offset overlap;
- directly observable stance polarity or intensity;
- repetition and complement presence; and
- technical or context insufficiency.

Do not code “interjection-like,” expected response, response relevance, or any post-offset property.

Timing provenance accompanies every measured duration, pause, or overlap. Prosodic independence records whether its basis is audio or transcript only. Lexical frequency and familiarity are joined from an independently frozen, hashed source rather than entered by cue passes.

Immediate cues are locked before the opaque token-to-sign-type task is released. Any contradiction between a sampled TCU judgement and the frozen IPU-style analytic-span boundary is logged; it cannot rewrite the parser after packet generation. Acoustic spans are not treated as interactional turns.

## Pre-offset and mechanical eligibility

Panel eligibility judgements use the pre-offset packet only. They cover intelligibility, participant identity, potential-recipient availability at offset, timing adequacy, quotation, metalinguistic mention, and reading aloud. Actual response or nonresponse is never evidence for recipient availability.

Frozen code, not a human who can see the outcome, checks whether the following packet is unclipped, duplicated, corrupt, or incorrectly bounded. The two eligibility components are joined mechanically. Neither may be revised after source labels and trajectories are linked.

The primary trajectory study requires `audio_measured` timing with a declared resolution. If REB approval, audio access, or measurement quality is unavailable, the CABNC trajectory route stops. It is not converted after coding into a transcript-timed 2.5-second analysis. The predeclared semantic-repetition study then becomes the direct test.

## Layer 3: local post-offset floor-transfer measurement

The target packet contains the same preceding context and target-bearing TCU, followed by the later of five post-offset seconds or two complete subsequent TCUs, capped at 12 seconds. The lexical form remains visible. Candidate categories and controls are intermixed.

### Mechanical observations and audited boundaries

Record the mechanical fields from which frozen code will derive the trajectory:

- target-TCU acoustic offset;
- separate first-audible, first-participant-vocal, and first-word-or-particle onsets;
- identity of the participant producing the first new vocal onset;
- signed gap or overlap from target offset;
- whether no new participant-produced vocal onset occurs by 1.5, 2.0, and 2.5 seconds;
- whether valid simultaneous or competitively overlapping onsets cannot be uniquely ordered; and
- technical or contextual problems.

Frozen code calculates signed first-audible, first-vocal, and first-word-or-particle latencies as onset minus target-TCU offset: positive for a post-offset gap, zero at exact boundary alignment, and negative for overlap. It derives the 2.5-second outcome from audited first-vocal timing, speaker identity, and valid unordered-onset status. Continuous signed first-vocal latency is retained for analysis.

### Derived four-way primary trajectory

- `DIFFERENT_SPEAKER_FIRST_VOCAL_ONSET_2500`: a participant other than the source produces the uniquely first new vocal onset by 2.5 seconds.
- `SOURCE_SPEAKER_FIRST_VOCAL_ONSET_2500`: the source produces the uniquely first new vocal onset by 2.5 seconds.
- `NO_NEW_VOCAL_ONSET_2500`: no participant-produced vocal onset occurs by 2.5 seconds.
- `UNORDERED_COMPETING_ONSETS_2500`: valid simultaneous or competitively overlapping onsets cannot be uniquely ordered.

Frozen code derives the label from audited first-vocal timing and speaker identity. An isolated inbreath or non-vocal handling noise is excluded. A uniquely ordered onset may begin in overlap and receive negative signed latency; it remains a source- or different-speaker onset. Speaker ambiguity, insufficient or corrupt audio, and other technical failures yield `uncodable` missingness, not a fifth trajectory. The same code derives 1.5- and 2.0-second threshold sensitivities.

Recipient status, entry minimality, fittedness, same-trajectory continuation, and uptake are coded separately. They cannot determine or change the primary trajectory. Fittedness supports a labelled sensitivity only.

## Eligibility

Eligibility is assembled from the pre-offset human layer and mechanical packet checks. An event requires:

- intelligible target-bearing material;
- identifiable participants;
- at least one plausible potential recipient;
- an unclipped following sequence; and
- no quotation, metalinguistic mention, reading aloud, transcription corruption, or mechanical duplicate.

Silence, overlap, same-speaker continuation, and a candidate-only TCU are not automatic exclusions. An event without adequate audio timing fails the primary study's pre-offset timing criterion rather than being assigned an estimated trajectory.

Every exclusion receives a prespecified code and evidence note. Silence, source entry, and lack of uptake are outcomes rather than exclusions. No exclusion may be invented after inspecting its effect on category performance.

## Pilot sampling

The pilot begins with 240 pre-offset candidates: fifteen from each of sixteen source-selected outer blocks, built under the within-block caps. Target selection scans the frozen blocks round-robin by within-block rank, skipping and logging candidates that would breach a global cap. Up to ten admitted events per block proceed to post-offset coding, for at most 160 target packets. The declared block list is:

1. *oh* and its anchor constructions;
2. *ooh*;
3. *ah*;
4. *eh*;
5. *ha*;
6. *cor*;
7. *ugh*;
8. *gosh*;
9. *mm*;
10. *er/erm*;
11. *yes*;
12. *no*;
13. *well*;
14. *right*;
15. *mum*; and
16. *thanks/thank you*.

Opaque block IDs replace these labels in model-facing material. The list supplies expressive candidates, response forms, fillers, discourse markers, a vocative, and a routine formula without consulting post-offset trajectories. If a listed block cannot supply ten eligible events under frozen source rules, that is a feasibility failure for the declared pilot; it is not replaced after outcome coding.

*Mum* is a kinship-term vocative-NP adversarial control, not a presumed negative member of either interjection category. Its source-only sign-type rules distinguish standalone summonses, supplementary vocatives within larger TCUs, and referential nominal uses. It tests whether the `syn` edge adds anything beyond supplement function, prosodic isolation, and standalone packaging; its `sem` polarity remains an empirical source judgement. Addressivity, summons status, TCU completeness, and projected source continuation stay in the common category-free cue baseline.

Sampling principles are:

- seek informative source-side variation without treating anticipated classifications as observed facts;
- include neighbouring controls, especially vocatives, discourse markers, formulas, fillers, and minimal lexical responses;
- include both high- and moderate-frequency retrieval bins;
- admit at most two candidates per speaker per pilot block and two per collection block per pilot block;
- avoid allowing *oh*, *yeah*, or *mm* to dominate;
- exclude every pilot occurrence from confirmatory training and scoring; and
- sample without consulting post-offset trajectories.

No interim feasibility decision occurs before all 240 pre-offset packets and all selected target packets reach their declared stages. A block must yield at least ten eligible assigned and cap-compliant events from its fifteen candidates. At least eight of the ten target packets must produce a primary-codable trajectory. No required subjective primary field may have more than 15% combined uncertain and uncodable values, and no more than 15% of derived primary outcomes may be uncodable. The maximum absolute difference across source cells in exclusion, outside-contrast, or technical-failure rates is 10 percentage points. Selection and skipping follow the frozen order without using post-offset information, and every scanned candidate receives a disposition row. Fresh events from the same block may later enter confirmation. The pre-pilot must determine whether the full study can satisfy the block and event gates without weakening the declaration after seeing outcomes.

## Reliability and stop rules

Proceed beyond the pre-pilot only if the applicable gates in the approved protocol remain credible. In particular:

- the model registry freezes one Claude family, one Gemini family, and one GPT/Codex family, including exact checkpoint, route, prompt, settings, schema, and run date for every layer before packets are released;
- Claude 5 is routed through Claude Code; Claude 4.6 and Gemini models are routed through Agy while that route remains available; GPT-family work is routed through Codex. A local open-weight model is optional as a declared portability stress test and receives no vote or additional chance to rescue the panel;
- every critical source card is run twice per family in fresh stateless, tool-free, browse-free, memory-free, manuscript-free contexts with independently randomized card order. A family casts a `yes` or `no` vote only when its two runs agree; otherwise its vote is `uncertain`;
- a final source-category `yes` or `no` requires all three stable family votes to agree and Brett's separate source-only, outcome-blind confirmation. Any other result remains `uncertain`; Brett's audit is not a fourth vote;
- across the three stable family votes, pilot `INTERJECTION_syn` and `INTERJECTION_sem` nominal alpha is at least `.80` separately, with raw agreement at least `.85`; the principal neighbour labels each reach nominal alpha of at least `.75`, with raw agreement at least `.80`; confidence intervals are reported but do not gate this small pilot;
- within-family duplicate stability reaches at least `.90` for `syn` and `sem` and `.85` for other subjective layers. Critical source cards are duplicated in full; high-volume layers contain at least 15% concealed duplicates;
- pilot token-to-sign-type assignment reaches inter-model nominal alpha of at least `.80`, with raw agreement at least `.85`;
- each principal categorical immediate cue reaches inter-model nominal alpha of at least `.70`, with raw agreement at least `.80`;
- panel--audit agreement reaches at least `.85` for `syn` and `sem` and `.80` for neighbouring classifications, token assignment, and immediate cues. Brett audits every source and neighbour dossier, every token disagreement or model instability, the frozen sample's cue assignments, and every acoustic boundary;
- no nominal alpha is calculated for the mechanically derived four-way trajectory. For the boundary used in that derivation, the 40-event local audit requires median absolute algorithm--expert difference no greater than 50 ms and the 95th percentile no greater than 100 ms;
- no required subjective primary field above 15% combined uncertain and uncodable, and no more than 15% uncodable derived primary outcomes;
- sufficient variation within at least half the retained families;
- no leakage-audit failure;
- no dominant family, speaker, or conversation block; and
- a non-degenerate immediate-cue comparator.

Call the three-family statistic **inter-model agreement**, not inter-rater agreement. Report within-family duplicate stability and panel--audit agreement separately. Also report Gwet's AC1, raw agreement, confusion matrices, and cluster-bootstrap intervals by form family where the measure is defined. Thresholds are operational gates, not evidence for the substantive projection.

A joint `syn+sem` representation can be reported only if each classification independently clears its reliability gate. Pooling cannot let an easier grammar-facing judgement conceal failure of the semantics-facing one. Stronger confirmatory lower-confidence-bound gates are frozen separately after design calculations establish an adequate number of dossiers and events.

The negligible and useful predictive regions are frozen from scientific utility and coding burden before pilot outcomes are inspected. Pilot-derived variance components may inform whether the confirmatory design is feasible; they cannot move the decision regions.

If grouping, blinding, reliability, yield, or design identifiability fails, stop the CABNC route and activate the predeclared semantic-repetition experiment. Do not recover the corpus study by changing membership rules or excluding failed families after outcome inspection.

## Paired model comparisons

Fit one predeclared multilevel predictive model family with the same outcome coding, component-blocked folds, baseline variables, priors, and scoring rules in four arms:

1. `B`: the common category-free baseline;
2. `B + sem`;
3. `B + syn`; and
4. `B + syn + sem`.

The co-primary contrasts are `B + sem` versus `B` and `B + syn` versus `B`. Treat them as paired, edge-specific comparisons because every arm is scored on the same held-out blocks. Report their score improvements jointly, with their paired uncertainty and their direct paired difference, following Gelman's multilevel-comparison principle rather than treating two noisy point estimates as independent wins or losses. The paper's advertised result is conjunctive: both edges must clear their separately frozen useful-effect and calibration criteria. One cannot compensate for the other's failure.

The conditional contrasts `B + syn + sem` versus `B + syn` and `B + syn + sem` versus `B + sem` diagnose complementarity. They are not additional projectibility tests. Fit no confirmatory `syn × sem` interaction, and do not treat joint membership or the three-way overlap as an independently projectible fourth category.

## Files and audit trail

The schema templates in this directory define the allowed joins and annotation fields. Generated packets, transcript excerpts, audio, keys linking pseudonymous packet IDs to corpus occurrences, and completed model/audit files remain local and outside version control unless their licensing and privacy status has been explicitly cleared.

Every freeze records:

- corpus commit and subtree object;
- parser and alias-table hashes;
- grouping-rule version;
- fold-map version;
- dossier-evidence-mask version;
- packet-generation code and random seed;
- model registry, route, prompt, settings, isolated-pass, duplicate, randomized-card-order, and audit manifests;
- adjudication history; and
- output hashes.

The lead owns theoretical interpretation and manuscript prose. Frozen model passes may propose subjective classifications only under the declared consensus and audit rules. Automated tools may validate schemas, hashes, masking, joins, and derive the four-way trajectory from audited acoustic measurements; they may not listen to restricted audio remotely, override an expert boundary, or revise a source classification in light of an outcome.

## Fold-integrity rule

Every retrieval bin belongs to exactly one principal outer block. Every sign-type inherits its retrieval bin's block. A strict variant block is wholly contained within one principal outer block.

Each principal block receives source-derived `declaration_sem_side` and `declaration_syn_side` values before target outcomes are joined. For either edge, `*_positive` requires unanimous final declaration-specific `yes` across its retained sign-types and `*_negative` requires unanimous `no`; mixed or uncertain blocks count toward neither edge's per-side minimum.

For a held-out principal block, the primary fold removes that block and every training bin sharing a directly declared content-bearing lexical atom or unresolved audio-confusability relation with it. Expansion stops after that direct comparison: exclusions are not recursively followed through other excluded bins. The weaker ordinary outer-block fold is reported only as a diagnostic.

A pathway-blocked sensitivity fold additionally removes forms connected by an independently documented recruitment, substitution, or descent relation. This tests the paper's own path-dependence concern rather than assuming form families are exchangeable. Pathway relations are frozen from diachronic evidence before target coding.

The pathway relation graph over the sixteen declared pilot blocks is published before packet generation. For each edge, a pathway-blocked fold is interpreted only if at least ten training outer blocks remain, including at least four blocks on each side of that edge's frozen declaration-specific contrast. Otherwise that edge's sensitivity is reported as structurally unidentified rather than fitted after relaxing the graph.

This distinction supports two claims of different strength:

- the primary analysis tests generalization without exposure to the held-out form's declared lexical material;
- the ordinary outer-block analysis estimates how much the result depends on component exposure; and
- the pathway-blocked analysis estimates how much it depends on historically related families.

All relations and exclusions are frozen before post-offset trajectory coding. Pronouns, determiners, and high-frequency function words cannot become blocking atoms merely because they occur inside a formula.
