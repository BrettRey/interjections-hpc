# CABNC pre-pilot field dictionary

**Status:** Draft; controlled values must be frozen before packet generation

This dictionary governs the CSV templates in this directory. A blank cell means structurally unavailable or not yet assigned. It never means `no`. A model pass or auditor uses `uncertain` when available evidence does not support a determinate subjective judgement. `Uncodable` records technically or contextually inadequate evidence and, for the primary trajectory, is missingness rather than a substantive outcome level.

## General conventions

- Identifiers are stable lowercase ASCII strings with underscores or opaque hexadecimal hashes.
- Multiple identifiers or labels in one cell are separated by `|` and sorted.
- Boolean fields use `yes` or `no`; blank is allowed only when a field is inapplicable or unavailable by design.
- Timestamps use ISO 8601 UTC.
- Confidence is ordinal: `1_low`, `2_moderate`, `3_high`, or `4_very_high`.
- Free-text notes cannot introduce information masked from that layer.
- Every subjective annotation row records the applicable `annotation_run_id`, `model_family_id`, `repeat_index`, and `coded_at`; expert rows record their audit identifier and timestamp.
- Consensus and audited rows remain additional rows or a versioned derivative table; raw model and expert rows are never overwritten.

## Status values

### `adjudication_status`

- `independent`
- `disagreement`
- `adjudicated`
- `frozen`
- `withdrawn_protocol_error`

`withdrawn_protocol_error` is used only for packet or protocol defects, not because a coded value is inconvenient.

### `dossier_status`

- `draft`
- `source_complete`
- `cards_generated`
- `independently_classified`
- `adjudicated`
- `frozen`
- `withdrawn_protocol_error`

### `fold_status`

- `proposed`
- `source_adjudicated`
- `audio_check_pending`
- `frozen`
- `excluded_no_defensible_block`

### `eligibility_status`

- `eligible`
- `excluded`
- `uncertain`

An event's post-offset trajectory cannot determine this status.

## Classification values

### `classification_target`

- `syn`
- `sem`

Neighbour classifications use their own table and one `neighbour_category` per row.

### Membership

The `membership` field in each source-classification row uses:

- `yes`
- `no`
- `uncertain`

The `full_profile` and `declaration_specific` cards are run in separate rows identified by `card_type`. Declaration-specific cards are presented first. A model pass may not see the paired card, another category's decision, another run's output, the manuscript, tools, browsing, memory, or post-offset evidence. The frozen manifest randomizes card order independently for each fresh stateless run.

### `card_type`

- `full_profile`
- `declaration_specific`

### `evidence_domain`

- `phonology`
- `morphology`
- `syntax`
- `semantics`
- `interaction`
- `diachrony`
- `sociolinguistics`
- `other`

These tags identify the evidence, not the ontological type of the category.

### `evidence_source_type`

- `published_primary`
- `published_secondary`
- `reference_grammar`
- `dictionary_or_lexicography`
- `dossier_corpus_segment`
- `analyst_judgement`

### `target_relation`

- `safe_source_evidence`
- `withheld_target`
- `withheld_close_proxy`
- `excluded_target_sample_summary`
- `irrelevant_to_declaration`

Any record other than `safe_source_evidence` or `irrelevant_to_declaration` must have `declaration_available=no`.

### Neighbour labels

Use zero or more of:

- `supplement`
- `expressive`
- `response_token`
- `discourse_marker`
- `routine_formula`
- `filler`
- `vocative`
- `parenthetical`
- `nonlexical_vocalization`
- `ordinary_lexical_response`
- `other_specified`

These are independent comparison classifications. They are not negative values of either interjection classification.

The `present` field uses `yes`, `no`, or `uncertain`.

### `quarantine_action`

- `none`
- `recompile_new_compiler`
- `drop_before_packet_generation`
- `retain_declared_sensitivity_only`

The action is fixed before target coding and cannot depend on a dossier's predictive performance.

### `assignment_status`

- `assigned`
- `outside_frozen_sign_types`
- `uncertain`
- `uncodable`

`token-sign-type-assignment-template.csv` implements a pre-offset layer between retrieval and category modelling. Each isolated model pass sees the event only through target offset plus opaque, frozen sign-type rules. It cannot see category memberships, post-offset sequence, family votes, or another run's assignment. Assignment is to one frozen `sign_type_id`, `outside_frozen_sign_types`, `uncertain`, or `uncodable`; alternatives and the decisive pre-offset cue are retained. A token is never reassigned in response to its target trajectory.

For the *mum* outer block, the frozen source rules distinguish at least `standalone_summons`, `supplementary_vocative`, and `referential_nominal_use`. *Mum* is a vocative-NP adversarial control, not a presumed `no` for either interjection category. Its `syn` and `sem` values follow the ordinary source-only panel and audit rules.

### `role_id`

- `grouping_span_adjudication`
- `dossier_compilation`
- `source_syn_panel`
- `source_sem_panel`
- `neighbour_panel`
- `immediate_cue_panel`
- `preoffset_eligibility_panel`
- `token_sign_type_panel`
- `secondary_fittedness_panel`
- `acoustic_expert`
- `source_auditor`
- `leakage_auditor`

Role separation is enforced by isolated pass and audit manifests rather than by a ten-human-coder design. Source-field audits never expose post-offset outcomes. Acoustic and fittedness passes never expose source labels or source-cell summaries.

## Model-comparison registry

`model-comparisons.csv` is the authoritative four-arm declaration. Component names are pipe-separated and order-insensitive. `matched_common_baseline` (`B`) contains immediate cues, independently assigned neighbour labels, and symmetrically available form covariates; it contains neither interjection-category label. `model_sem` adds only declaration-specific `INTERJECTION_sem`; `model_syn` adds only declaration-specific `INTERJECTION_syn`; and `model_both` adds both.

`predictive-contrast.csv` declares `B + sem` versus `B` and `B + syn` versus `B` as paired co-primary, edge-specific contrasts scored on the same component-blocked folds. Their held-out score gains, covariance, and direct paired difference are reported jointly in the Gelman-style multilevel comparison. `B + syn + sem` versus `B + syn` and `B + syn + sem` versus `B + sem` are complementarity diagnostics only. No confirmatory `syn × sem` interaction is fitted. Joint membership and the overlap are never interpreted as an independently projectible fourth category.

The paper's advertised result is conjunctive: each edge must separately clear its frozen useful-effect and calibration rule. A stronger edge cannot compensate for a failed or ambiguous edge.

## Model-panel registry and consensus

`model-registry.csv`, `annotation-routes.csv`, `annotation-manifest-template.csv`, `duplicate-manifest-template.csv`, `annotation-consensus-template.csv`, and `expert-audit-template.csv` jointly govern subjective annotations.

- Freeze one Claude-family, one Gemini-family, and one GPT/Codex-family model, including exact checkpoint, provider route, prompt, settings, schema, and date for each layer.
- Route Claude 5 through Claude Code, Claude 4.6 and Gemini models through Agy while available, and GPT-family runs through Codex. An optional local open-weight run is a portability stress test only: it adds no vote and cannot rescue the panel.
- Run every critical source card twice per family in fresh stateless, tool-free, browse-free, memory-free, manuscript-free contexts with independently randomized card order.
- Retain raw responses, evidence-span references, refusals, parse failures, prompt hashes, and resolved model versions. A response citing unavailable evidence or violating the frozen schema is invalid, not hand-repaired.
- `within_family_stable=yes` only when the two family runs agree. A family with discordant runs contributes `uncertain`, not a tie-breaking vote.
- `unanimous_three_family_consensus=yes` only when the three stable family votes all agree. A final source `yes` or `no` additionally requires Brett's source-only, outcome-blind confirmation; otherwise `primary_label_eligible=no` and the final value is `uncertain`.
- Brett's audit is separate from the model vote. He audits every source and principal-neighbour dossier, every token disagreement or model instability, the frozen sample of cue assignments, and every acoustic boundary.
- A provider change during a layer forces that complete layer to be rerun under one newly frozen checkpoint before outcomes are inspected; versions are never silently pooled.

Agreement across model families is called **inter-model agreement**. Within-family duplicate stability and panel--audit agreement are reported separately.

## Reliability and sampling registries

`feasibility-gates.csv` stores the authority, audio, alignment, model-panel, and audit requirements. `reliability-gates.csv` stores each numeric pilot agreement gate as one statistic-specific row. `sampling-rules.csv` stores candidate counts, target-selection order, block minima, concentration caps, pilot-event disposition, and pathway-sensitivity minima. These populated registries, rather than prose paraphrases, determine automated validation. Confirmatory lower-confidence-bound gates are not yet present because they must be frozen only after design calculations establish adequate dossier and event counts.

The pre-pilot reliability registry must contain, at minimum:

- inter-model nominal alpha/raw agreement of `.80`/`.85` separately for `syn` and `sem`;
- inter-model nominal alpha/raw agreement of `.75`/`.80` for each principal neighbour;
- inter-model nominal alpha/raw agreement of `.80`/`.85` for token-to-sign-type assignment;
- inter-model nominal alpha/raw agreement of `.70`/`.80` for each principal categorical immediate cue;
- within-family duplicate stability of `.90` for `syn` and `sem` and `.85` for other subjective layers, with all critical source cards duplicated and at least 15% concealed duplicates in high-volume layers; and
- panel--audit raw agreement of `.85` for `syn` and `sem` and `.80` for neighbours, token assignment, and cues.

Do not calculate an annotation alpha for the mechanically derived trajectory. The 40-event local acoustic audit spans at least eight declared pilot blocks; for the boundary used in the primary derivation, median absolute algorithm--expert difference must be at most 50 ms and the 95th percentile at most 100 ms.

## Grouping and fold values

### `grouping_basis`

Use one or more of:

- `explicit_metadata`
- `recording_id`
- `episode_boundary`
- `time_continuity`
- `participant_continuity`
- `topic_or_setting_continuity`
- `audio_confirmation`
- `conservative_block_without_identity_claim`

### Continuity fields

`continuity_with_previous` and `continuity_with_next` use:

- `same_conversation`
- `different_conversation`
- `uncertain`
- `not_applicable`

### `collapse_decision`

- `join_same_speaker_ipu_span`
- `split_at_internal_boundary`
- `split_missing_timing`
- `split_unknown_speaker`
- `audio_check_pending`

The canonical parser artifacts are `analytic_spans.csv` and its span-initial lexical output, `span_initial_vocabulary.csv`; `analytic-span-template.csv` is the corresponding pre-pilot schema. Its key is `span_id`, and the unit is an IPU-style analytic span, never an interactional turn. Join adjacent main tiers only when both have the same known listed speaker, both boundary times are present, and the positive within-speaker gap is strictly under 180 ms. A speaker change, unknown identity, missing timing, or gap of 180 ms or more forces a split. Preserve the original same-speaker chain, every join or split reason, and all original tier indices. Sampled TCU completeness and source self-continuation are separately adjudicated fields and may not rewrite the frozen span parser.

Parser 0.6.0 produced 244,922 analytic spans while leaving the 255,211 retrieved occurrences unchanged. Sixteen otherwise eligible same-speaker boundaries were exactly 180 ms and therefore split. No 2.5-second target rule is part of the parser.

`boundary_reason_from_previous` uses:

- `segment_start`;
- `same_speaker_gap_under_180ms`;
- `speaker_change`;
- `unknown_speaker_identity`;
- `missing_boundary_timing`;
- `gap_at_least_180ms`; or
- `corrupt_or_inconsistent_metadata`.

### Component and pathway relations

Component relations do not automatically merge transitively. `relation_type` uses:

- `strict_variant`: accepted orthographic or phonological variants;
- `anchor_head`: a complex construction whose declared bearer is the anchor form;
- `constituent`: a complex construction contains the related form without an anchor-head identity claim;
- `lexical_root`: forms share a content-bearing lexical root;
- `reduplication`: a simple and reduplicated construction are related;
- `phonological_neighbor`: transcript or audio confusability is unresolved; or
- `pathway`: independently documented recruitment, descent, or substitution.

`outer_block_effect` is `merge`, `no_merge`, or `unresolved`. `primary_component_effect` is `exclude`, `no_exclude`, or `unresolved`. `pathway_sensitivity_effect` is `exclude`, `no_exclude`, or `unresolved`.

The principal outer block merges `strict_variant` and accepted `anchor_head` relations. The primary component-blocked fold applies every row with `primary_component_effect=exclude`, including direct `constituent`, `lexical_root`, and unresolved `phonological_neighbor` relations. The pathway-blocked sensitivity additionally applies every `pathway_sensitivity_effect=exclude` row. No step recursively expands through newly excluded bins.

The ordinary leave-one-outer-block-out fold is diagnostic only. For each edge, the confirmatory design requires at least six form blocks and about 150 events on each unanimous side after component blocking. A pathway-blocked edge is interpreted only when at least ten training blocks remain, including at least four blocks on each side of that edge's frozen declaration-specific contrast. Failure for one edge does not decide the other.

### `declaration_sem_side`

- `sem_positive`: every retained sign-type in the principal outer block has final declaration-specific `INTERJECTION_sem=yes`;
- `sem_negative`: every retained sign-type has final declaration-specific `INTERJECTION_sem=no`; or
- `mixed_or_uncertain`: the block contains both values or any uncertain judgement.

Only `sem_positive` and `sem_negative` count toward per-side block minima. The value is derived after source adjudication and before target outcomes are linked. It is repeated consistently on every membership row for the same principal outer block.

### `declaration_syn_side`

- `syn_positive`: every retained sign-type in the principal outer block has final declaration-specific `INTERJECTION_syn=yes`;
- `syn_negative`: every retained sign-type has final declaration-specific `INTERJECTION_syn=no`; or
- `mixed_or_uncertain`: the block contains both values or any uncertain judgement.

Only `syn_positive` and `syn_negative` count toward the `syn` edge's per-side block minima. Both edge-side values use the same principal blocks and are derived before target outcomes are linked. A mixed or uncertain block may contribute events to descriptive summaries but counts toward neither side minimum for that edge.

### Sampling precedence and disposition

Smaller numeric `precedence` values act first. Pre-offset pools are constructed by scanning each block's frozen SHA-256 rank and skipping candidates that would breach the two-per-speaker or two-per-collection within-block caps. Target selection then scans eligible and assigned candidates in round-robin order: within-block rank first and frozen block order second. A candidate that would breach a global cap is logged as `skipped_global_cap`, and scanning continues. Every scanned candidate receives one `sampling-disposition` row; neither a skip nor a replacement may consult post-offset information.

## Immediate-cue values

All immediate cues are observed from the preceding context and target-bearing TCU through acoustic offset only. They form the common category-free baseline for both co-primary edges. They may not encode an interjection label, expected uptake, actual floor transfer, or any post-offset fact. `span_position` records position within the IPU-style analytic span and never asserts that the span is an interactional turn.

### `syntactic_packaging`

- `standalone`
- `supplemented`
- `syntactically_integrated`
- `fragment_or_elliptical`
- `uncertain`
- `uncodable`

This is a local token-level cue, not `INTERJECTION_syn` membership.

### `tcu_complete_at_offset`

- `yes`
- `no`
- `uncertain`
- `uncodable`

### `prosodic_independence`

- `independent`
- `integrated`
- `mixed_or_uncertain`
- `uncodable`

### `addressivity`

- `addressed_single`
- `addressed_multiple`
- `broadcast_or_group`
- `self_directed`
- `uncertain`
- `uncodable`

### `summons_status`

- `summons`
- `not_summons`
- `uncertain`
- `uncodable`

Judge summons status from pre-offset form, addressivity, prosody, and sequential position only. A later response cannot establish that a token was a summons.

### `projected_source_continuation`

- `projected`
- `not_projected`
- `uncertain`
- `uncodable`

This records whether the source's pre-offset design observably projects additional material. It is not recoded from whether the source actually continues.

### `stance_polarity`

- `positive`
- `negative`
- `mixed`
- `neutral_or_none`
- `uncertain`
- `uncodable`

### `stance_intensity`

- `none`
- `low`
- `moderate`
- `high`
- `uncertain`
- `uncodable`

### `repetition_type`

- `none`
- `immediate_self_repetition`
- `distributed_self_repetition`
- `other_repetition`
- `uncertain`
- `uncodable`

### `complement_presence`

- `none`
- `overt_complement`
- `constructionally_integrated_material`
- `uncertain`
- `uncodable`

### Timing provenance

Every `*_timing_source` or `timing_source` field uses:

- `audio_measured`
- `transcript_bullet`
- `transcript_interpolated`
- `model_or_analyst_estimate`
- `unavailable`

The primary trajectory study admits only `audio_measured` timing. `timing_resolution_ms` records the effective measurement resolution. `prosody_basis` uses `audio`, `transcript_only`, or `unavailable`.

`clause_type` and `prior_action_type` remain deliberately open cross-file dependencies. Their controlled values and decision rules must be developed from outcome-blind practice packets and frozen before Gate C; they cannot be improvised in production annotation or expanded after category effects are seen.

## Post-offset trajectory values

### Recipient availability

`potential_recipient_available_at_offset` is judged from the participant configuration and addressivity available at the target-bearing TCU offset. An actual subsequent response is not evidence that a recipient was available, and nonresponse is not evidence that none was available.

Values:

- `yes`
- `no`
- `uncertain`
- `uncodable`

`recipient_configuration_basis` records the pre-offset participant, addressivity, and participation-status evidence supporting that judgement.

### Local acoustic observations

`post-offset-trajectory-template.csv` stores source-label-blind local measurements, not a human or model classification of the primary outcome. The acoustic expert listens to the prepared WAV while inspecting its waveform, spectrogram, and 10-ms activity proposal. Record separately:

- `target_tcu_offset_ms`;
- `first_audible_onset_ms`, including any audible event requiring later type adjudication;
- `first_vocal_onset_ms`, the first participant-produced vocal onset;
- `first_word_onset_ms`, including a word or conventional particle;
- `first_vocal_speaker_id` and speaker-identity status; and
- whether valid simultaneous or competitively overlapping vocal onsets cannot be uniquely ordered.

An isolated inbreath and non-vocal noise such as a click or handling sound do not count as a participant-produced vocal onset. A uniquely ordered first vocal onset may begin before target offset and therefore have negative signed latency. Ordinary overlap does not enter the unordered class if one valid vocal onset can be uniquely identified as first.

`first_vocalizer_type` uses:

- `source_speaker`;
- `different_speaker`;
- `simultaneous_or_unordered`;
- `none_by_2500`;
- `ambiguous`; or
- `uncodable`.

`simultaneous_or_unordered_valid=yes` only when at least two valid participant vocal onsets cannot be uniquely ordered acoustically. Speaker ambiguity, corrupt or insufficient audio, and unresolved technical failure are `uncodable` missingness, not unordered competition.

### Signed latency and threshold flags

`signed_first_audible_latency_ms`, `signed_first_vocal_latency_ms`, and `signed_first_word_latency_ms` are onset minus target offset. Positive values are post-offset gaps, zero is boundary alignment, and negative values are overlap. They are blank only when the relevant onset is absent or the measurement is technically unresolvable. Frozen code derives and validates `vocal_entry_within_1500`, `vocal_entry_within_2000`, and `vocal_entry_within_2500`; the continuous signed first-vocal latency is also reported.

### Context and technical status

`context_request_status` uses `not_requested`, `requested_and_granted`, or `requested_unavailable`. A granted request leads to remeasurement from the final permitted packet. `context_insufficient=yes` means that the final packet remains insufficient after any permitted request and is terminally uncodable; the request itself does not create a fifth outcome. `technical_problem=yes` likewise records a defect that remains in the final permitted packet. Both fields use `yes` or `no`.

### `post_offset_trajectory`

- `DIFFERENT_SPEAKER_FIRST_VOCAL_ONSET_2500`
- `SOURCE_SPEAKER_FIRST_VOCAL_ONSET_2500`
- `NO_NEW_VOCAL_ONSET_2500`
- `UNORDERED_COMPETING_ONSETS_2500`

### `primary_next_position_outcome`

- `different_speaker_first_vocal_onset_2500`
- `source_speaker_first_vocal_onset_2500`
- `no_new_vocal_onset_2500`
- `unordered_competing_onsets_2500`

Both fields are deterministic aliases derived from audited first-vocal timing, speaker identity, and valid unordered-onset status. Models and experts assign neither. A technically unresolvable event has both fields blank plus a populated `uncodable_reason`; `uncodable` is attrition/missingness and is never a fifth class. The same frozen derivation generates 1.5- and 2.0-second sensitivity labels.

`source_row_sha256` hashes the complete audited mechanical-observation row. `derivation_code_sha256` hashes the exact derivation script. Any mismatch among `vocal_entry_within_2500`, audio-measured signed first-vocal latency, speaker identity, unordered-onset status, and the derived label is an integrity failure rather than an analyst-resolved judgement.

`integrity_check_status=pass` means every derivation and provenance check succeeded. A failing source row isn't emitted; the derivation halts and records the error outside the derived table.

### `fittedness_sensitivity_outcome`

- `fitted_recipient_entry_2500`
- `nonfitted_recipient_entry_2500`
- `not_applicable`
- `uncodable`

### `fitted_judgement`

- `fitted_response`
- `not_fitted_response`
- `not_applicable`
- `uncertain`
- `uncodable`

Fittedness supports a labelled sensitivity outcome. It never changes the mechanical primary trajectory.

Recipient status, entry minimality, fittedness, same-trajectory continuation, and uptake remain separate secondary fields. They cannot determine or relabel the four-way primary trajectory.

### Audio preparation provenance

`analysis/prepare_cabnc_audio.py` is a local-only bounded preparation utility. Its required interface is `--input`, `--output-root`, `--event-id`, `--start-ms`, `--end-ms`, and `--generated-at`. The frozen packet manifest supplies the explicit bounds and timestamp. It converts only that authorized interval to a 16-kHz mono signed-16-bit PCM WAV and writes waveform, spectrogram, 10-ms adaptive energy-activity CSV, and provenance JSON artifacts. It refuses invalid event IDs and existing event directories.

The utility does not download audio, discover a TCU, identify or align speakers, adjudicate an onset, distinguish speech from laughter/breath/noise/overlap, or derive an outcome. Raw and derived audio artifacts remain on the approved local volume unless written authority explicitly permits otherwise. `prepared_wav_sha256`, `waveform_png_sha256`, `spectrogram_png_sha256`, `activity_csv_sha256`, `preparation_code_sha256`, and `provenance_json_sha256` bind every acoustic row to those local artifacts. Expert listening and audit remain mandatory.

## Exclusion codes

Pre-offset subjective panel eligibility permits only:

- `unintelligible_target`
- `participants_unidentifiable`
- `no_potential_recipient_at_offset`
- `recipient_availability_uncertain`
- `quotation`
- `metalinguistic_mention`
- `reading_aloud`
- `timing_inadequate`

Mechanical packet eligibility permits only:

- `following_sequence_clipped`
- `transcription_corruption`
- `mechanical_duplicate`
- `protocol_packet_error`

Silence, overlap, source continuation, and lack of uptake are not exclusion codes.

The two eligibility layers are joined mechanically only after both are frozen. Actual response, nonresponse, or later speech cannot establish pre-offset recipient availability or repair a failed packet check. `preoffset-eligibility-template.csv` records the source-label-blind expert and audit round explicitly; model-pass provenance belongs in the separate annotation manifest.

## Packet and masking checks

### `packet_layer`

- `source_full_profile`
- `source_declaration_specific`
- `immediate_cue`
- `preoffset_eligibility`
- `token_sign_type_assignment`
- `post_offset_trajectory`
- `mechanical_eligibility`

### `mask_check_status`

- `pass_automated`
- `pass_manual`
- `fail`
- `pending`

A source or cue packet with `fail` is withdrawn as a protocol error before coding. It cannot be repaired after its target label is known.

### `separation_check_status`

- `pass`
- `fail`
- `pending`

No annotation, audit, or acoustic-measurement batch may be released while this field is `fail` or `pending`.
