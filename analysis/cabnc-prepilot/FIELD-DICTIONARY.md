# CABNC pre-pilot field dictionary

**Status:** Draft; controlled values must be frozen before packet generation

This dictionary governs the CSV templates in this directory. A blank cell means structurally unavailable or not yet coded. It never means `no`. Coders use `uncertain` when the evidence is present but does not support a determinate judgement, and `uncodable` when the packet itself is technically or contextually inadequate.

## General conventions

- Identifiers are stable lowercase ASCII strings with underscores or opaque hexadecimal hashes.
- Multiple identifiers or labels in one cell are separated by `|` and sorted.
- Boolean fields use `yes` or `no`; blank is allowed only when a field is inapplicable or unavailable by design.
- Timestamps use ISO 8601 UTC.
- Confidence is ordinal: `1_low`, `2_moderate`, `3_high`, or `4_very_high`.
- Free-text notes cannot introduce information masked from that layer.
- Every completed coding row records `coder_id`, `coding_round`, and `coded_at`.
- Adjudicated rows remain additional rows or a versioned derivative table; original coder rows are never overwritten.

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

The `full_profile` and `declaration_specific` cards are coded in separate rows identified by `card_type`. Declaration-specific cards are presented first. A coder may not infer that answer by copying a full-profile answer after viewing both cards side by side; packet assignment controls card order and records it.

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

### `role_id`

- `source_syn`
- `source_sem`
- `neighbour`
- `cue_and_sign_type`
- `post_offset_trajectory`

Each role requires two distinct trained human coders. No coder may occupy more than one of these roles in the pilot.

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

- `retain_single_turn`
- `split_at_internal_boundary`
- `exclude_indeterminate`
- `audio_check_pending`

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

## Immediate-cue values

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

Clause type and prior action type require a separate pilot codebook developed from actual packets. Their values must be frozen before reliability coding and cannot be expanded in response to category effects.

### Timing provenance

Every `*_timing_source` or `timing_source` field uses:

- `audio_measured`
- `transcript_bullet`
- `transcript_interpolated`
- `coder_estimate`
- `unavailable`

The primary trajectory study admits only `audio_measured` timing. `timing_resolution_ms` records the effective measurement resolution. `prosody_basis` uses `audio`, `transcript_only`, or `unavailable`.

## Post-offset trajectory values

### Recipient availability

`potential_recipient_available_at_offset` is judged from the participant configuration and addressivity available at the target-bearing TCU offset. An actual subsequent response is not evidence that a recipient was available, and nonresponse is not evidence that none was available.

Values:

- `yes`
- `no`
- `uncertain`
- `uncodable`

`recipient_configuration_basis` records the pre-offset participant, addressivity, and participation-status evidence supporting that judgement.

### `first_post_offset_vocalizer_type`

- `source_speaker`
- `other_participant`
- `multiple_or_overlap`
- `none_in_window`
- `uncertain`
- `uncodable`

### `first_entry_within_2500`

- `yes`
- `no`
- `uncertain`
- `uncodable`

### `first_entry_minimality`

- `minimal_listener_tcu`
- `nonminimal_tcu`
- `not_applicable`
- `uncertain`
- `uncodable`

### `post_offset_trajectory`

- `RECIPIENT_NONMINIMAL_ENTRY_2500`
- `RECIPIENT_MINIMAL_ENTRY_2500`
- `SOURCE_ENTRY_2500`
- `NO_VOCAL_ENTRY_2500`
- `COMPETITIVE_OR_OTHER`
- `UNCODABLE`

### `primary_next_position_outcome`

- `recipient_nonminimal_entry_2500`
- `recipient_minimal_entry_2500`
- `source_entry_2500`
- `no_vocal_entry_2500`
- `outside_primary_contrast`
- `uncodable`

Both `post_offset_trajectory` and `primary_next_position_outcome` are deterministically derived from first-entry timing, first-vocalizer type, and minimality; coders assign neither.

### `fitted_judgement`

- `fitted_response`
- `not_fitted_response`
- `not_applicable`
- `uncertain`
- `uncodable`

Fittedness supports a labelled sensitivity outcome. It never changes the mechanical primary trajectory.

## Exclusion codes

Pre-offset human eligibility permits only:

- `unintelligible_target`
- `participants_unidentifiable`
- `no_potential_recipient_at_offset`
- `recipient_availability_uncertain`
- `quotation`
- `metalinguistic_mention`
- `reading_aloud`
- `timing_inadequate`

Mechanical eligibility permits only:

- `following_sequence_clipped`
- `transcription_corruption`
- `mechanical_duplicate`
- `protocol_packet_error`

Silence, overlap, source continuation, and lack of uptake are not exclusion codes.

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

No coder assignment batch may be released while this field is `fail` or `pending`.
