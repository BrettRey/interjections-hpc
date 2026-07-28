#!/usr/bin/env python3
"""Validate the CABNC pre-pilot schemas and frozen design registries."""

from __future__ import annotations

import argparse
import csv
import itertools
from pathlib import Path


REQUIRED_TEMPLATES = {
    "analytic-span",
    "annotation-consensus",
    "annotation-manifest",
    "annotation-routes",
    "audio-feasibility",
    "codebook",
    "conversation-grouping",
    "decision-rules",
    "derived-outcomes",
    "dossier-evidence",
    "dossier-reservations",
    "duplicate-manifest",
    "expert-audit",
    "feasibility-gates",
    "fold-map",
    "form-covariates",
    "form-relations",
    "heldout-predictive-score",
    "immediate-cue",
    "leakage-audit",
    "leakage-checklist",
    "mechanical-eligibility",
    "model-comparisons",
    "model-registry",
    "neighbour-classification",
    "outer-block-membership",
    "packet-manifest",
    "post-offset-trajectory",
    "predictive-contrast",
    "predictive-covariance",
    "projective-declarations",
    "preoffset-eligibility",
    "primary-component-exclusions",
    "reliability-gates",
    "retrieval-bins",
    "role-separation-matrix",
    "sampling-disposition",
    "sampling-rules",
    "sign-type-dossier",
    "sign-type-retrieval-bridge",
    "sign-types",
    "source-classification",
    "speaker-registry",
    "surface-aliases",
    "token-sign-type-assignment",
}

RUN_PROVENANCE_FIELDS = {
    "annotation_run_id",
    "model_family_id",
    "repeat_index",
    "prompt_sha256",
    "packet_sha256",
    "response_sha256",
    "evidence_set_sha256",
}

REQUIRED_FIELDS = {
    "source-classification": {
        "dossier_id", "classification_target", "pass_id", "model_registry_id",
        "card_type", "membership", "within_family_stable",
        "cross_family_consensus", "expert_audit_status",
    } | RUN_PROVENANCE_FIELDS,
    "neighbour-classification": {
        "dossier_id", "neighbour_category", "pass_id", "model_registry_id",
        "present", "within_family_stable", "cross_family_consensus",
        "expert_audit_status",
    } | RUN_PROVENANCE_FIELDS,
    "token-sign-type-assignment": {
        "packet_event_id", "pass_id", "model_registry_id",
        "assigned_sign_type_id", "assignment_status", "within_family_stable",
        "cross_family_consensus", "expert_audit_status",
    } | RUN_PROVENANCE_FIELDS,
    "immediate-cue": {
        "packet_event_id", "pass_id", "annotation_run_id", "model_family_id",
        "model_registry_id", "repeat_index", "prompt_sha256", "packet_sha256",
        "response_sha256", "evidence_set_sha256", "syntactic_packaging", "tcu_complete_at_offset",
        "addressivity", "summons_status", "projected_source_continuation",
        "prosodic_independence", "stance_polarity", "stance_intensity",
        "repetition_type", "complement_presence", "within_family_stable",
        "cross_family_consensus", "expert_audit_status",
    },
    "preoffset-eligibility": {
        "packet_event_id", "expert_id", "expert_round",
        "potential_recipient_available_at_offset",
        "timing_adequate", "eligibility_status",
    },
    "mechanical-eligibility": {
        "packet_event_id", "following_sequence_unclipped", "mechanical_duplicate",
        "eligibility_status",
    },
    "post-offset-trajectory": {
        "packet_event_id", "measurement_id", "measurement_round",
        "audio_preparation_version", "prepared_wav_sha256",
        "waveform_png_sha256", "spectrogram_png_sha256", "activity_csv_sha256",
        "preparation_code_sha256", "provenance_json_sha256",
        "target_tcu_offset_ms", "target_offset_source",
        "first_audible_onset_ms", "first_audible_source",
        "first_vocal_onset_ms", "first_vocal_source",
        "first_word_onset_ms", "first_word_source", "timing_resolution_ms",
        "first_vocal_speaker_id", "first_vocalizer_type",
        "speaker_identity_status", "simultaneous_or_unordered_valid",
        "technical_problem", "context_request_status", "context_insufficient",
    },
    "derived-outcomes": {
        "packet_event_id", "outcome_derivation_version", "source_row_sha256",
        "derivation_code_sha256", "signed_first_audible_latency_ms",
        "signed_first_vocal_latency_ms", "signed_first_word_latency_ms",
        "vocal_entry_within_1500", "vocal_entry_within_2000",
        "vocal_entry_within_2500", "outcome_coding_status",
        "outcome_missingness_reason", "post_offset_trajectory",
        "primary_next_position_outcome", "derived_by", "derived_at",
        "integrity_check_status",
    },
    "packet-manifest": {
        "packet_event_id", "packet_layer", "packet_hash",
        "duplicate_manifest_hash", "evidence_set_sha256",
        "source_occurrence_key_hash", "collection_block_id",
        "principal_outer_block_id", "fold_map_version", "fold_map_hash",
        "random_seed", "external_model_audio_prohibited",
    },
    "dossier-evidence": {
        "dossier_id", "declaration_id", "target_relation", "proxy_rule_id",
        "collection_block_id", "speaker_ids", "text_screen_status",
    },
    "audio-feasibility": {
        "audio_audit_event_id", "principal_outer_block_id", "collection_block_id",
        "audio_preparation_version", "input_audio_sha256", "prepared_wav_sha256",
        "waveform_png_sha256", "spectrogram_png_sha256", "activity_csv_sha256",
        "preparation_code_sha256", "provenance_json_sha256", "sample_rate_hz",
        "channels", "sample_format", "activity_frame_ms", "audio_licence_ref",
        "audio_access_authorized", "external_model_audio_prohibited",
        "measurement_resolution_ms", "algorithm_target_offset_proposal_ms",
        "expert_target_offset_ms",
        "absolute_algorithm_expert_target_offset_difference_ms",
        "algorithm_first_vocal_onset_proposal_ms", "expert_first_vocal_onset_ms",
        "absolute_algorithm_expert_first_vocal_difference_ms",
        "expert_round_1_target_offset_ms",
        "expert_round_2_target_offset_ms",
        "expert_round_1_first_vocal_onset_ms",
        "expert_round_2_first_vocal_onset_ms",
        "absolute_expert_repeat_target_offset_difference_ms",
        "absolute_expert_repeat_first_vocal_difference_ms",
        "clip_complete", "status",
    },
    "primary-component-exclusions": {
        "test_outer_block_id", "excluded_train_bin_id", "trigger_atom_id",
        "trigger_relation_id", "fold_map_version", "status",
    },
    "fold-map": {
        "retrieval_bin_id", "sign_type_ids", "strict_variant_block_ids",
        "principal_outer_block_id", "direct_component_relation_ids",
        "pathway_relation_ids", "component_exclusion_rule",
        "pathway_exclusion_rule", "fold_map_version", "fold_map_hash",
    },
    "form-relations": {
        "relation_id", "left_bin_id", "right_bin_id", "relation_type",
        "pathway_relation_id", "outer_block_effect", "primary_component_effect",
        "pathway_sensitivity_effect", "evidence_basis", "freeze_version",
    },
    "model-registry": {
        "model_registry_id", "model_family", "provider", "execution_surface",
        "model_name", "model_version", "temperature", "top_p", "seed_policy",
        "tool_access", "network_access", "context_policy", "data_class_allowed",
        "prompt_protocol_version", "settings_sha256", "registry_version",
        "version_drift_action", "status",
    },
    "annotation-routes": {
        "route_id", "pass_id", "annotation_target", "model_registry_id",
        "repeat_count", "packet_layer", "prompt_id", "allowed_evidence_domains",
        "prohibited_fields", "consensus_role", "route_version",
    },
    "annotation-manifest": {
        "annotation_run_id", "route_id", "pass_id", "unit_id",
        "model_registry_id", "resolved_model_version", "repeat_index",
        "prompt_sha256", "packet_sha256", "response_sha256",
        "evidence_set_sha256", "settings_sha256", "input_manifest_sha256",
        "output_manifest_sha256", "version_drift_detected", "drift_action",
    },
    "duplicate-manifest": {
        "duplicate_pair_id", "pass_id", "unit_id", "model_registry_id",
        "first_run_id", "second_run_id", "first_response_sha256",
        "second_response_sha256", "first_label", "second_label", "stable",
    },
    "annotation-consensus": {
        "consensus_id", "pass_id", "unit_id", "stable_gpt_label",
        "stable_claude_label", "stable_gemini_label", "stable_family_count",
        "cross_family_label", "unanimous_three_family_consensus",
        "expert_audit_id", "expert_label", "expert_confirms_consensus",
        "primary_label_eligible",
    },
    "expert-audit": {
        "expert_audit_id", "pass_id", "unit_id", "audit_sampling_basis",
        "source_only_blind", "model_identities_masked", "model_outputs_frozen",
        "outcomes_unavailable", "expert_id", "expert_label", "consensus_label",
        "agreement", "audited_at",
    },
    "model-comparisons": {
        "model_id", "model_role", "components", "comparison_model_id",
        "evidential_status", "required_source_gates", "model_version",
    },
    "heldout-predictive-score": {
        "analysis_run_id", "fold_map_version", "test_outer_block_id",
        "holdout_type", "model_id", "aggregation_unit", "n_events",
        "log_predictive_density_sum", "log_predictive_density_mean",
        "multiclass_brier_score", "calibration_intercept", "calibration_slope",
        "predictor_count", "coding_burden_minutes",
    },
    "predictive-contrast": {
        "contrast_id", "left_model_id", "right_model_id", "estimand",
        "aggregation_unit", "paired_on", "covariance_set_id",
        "evidential_status", "minimum_useful_gain_id", "decision_role",
    },
    "predictive-covariance": {
        "analysis_run_id", "covariance_set_id", "row_contrast_id",
        "column_contrast_id", "covariance_estimate", "correlation_estimate",
        "uncertainty_method", "n_outer_blocks", "aggregation_unit",
    },
    "projective-declarations": {
        "declaration_id", "source_category", "outcome", "bearer", "population",
        "conditions", "transformations", "timescale", "tolerance_rule_id",
        "evidential_standard", "failure_rule_id", "scope_version", "status",
    },
    "decision-rules": {
        "rule_id", "applies_to", "metric", "operator", "threshold_source",
        "threshold_value", "simultaneous_procedure", "calibration_metrics",
        "calibration_tolerance_source", "calibration_tolerance_value",
        "central_member_robustness_rule", "failure_action", "rule_version", "status",
    },
    "reliability-gates": {
        "gate_id", "study_stage", "target", "statistic", "operator",
        "threshold", "decision_use", "gate_version",
    },
    "feasibility-gates": {
        "gate_id", "stage", "requirement", "operator", "threshold", "unit",
        "failure_action", "gate_version",
    },
    "outer-block-membership": {
        "principal_outer_block_id", "retrieval_bin_id", "membership_basis",
        "declaration_sem_side", "declaration_syn_side", "status", "freeze_version",
    },
    "sampling-disposition": {
        "candidate_event_id", "principal_outer_block_id", "within_block_rank",
        "global_round", "preoffset_pool_status", "eligibility_status",
        "assignment_status", "target_selection_status", "target_skip_rule_id",
        "selection_rule_version",
    },
    "sampling-rules": {
        "rule_id", "scope", "parameter", "value", "unit", "precedence",
        "rule_version",
    },
    "role-separation-matrix": {
        "left_pass_id", "right_pass_id", "shared_context_allowed",
        "shared_response_allowed", "minimum_model_families_per_pass",
        "matrix_version",
    },
}

POPULATED_REGISTRIES = {
    "annotation-routes",
    "codebook",
    "decision-rules",
    "feasibility-gates",
    "leakage-checklist",
    "model-comparisons",
    "model-registry",
    "predictive-contrast",
    "projective-declarations",
    "reliability-gates",
    "role-separation-matrix",
    "sampling-rules",
}

FAILURE_CLASSES = {"halt", "remediable_before_unblinding", "note_only"}
MODEL_FAMILIES = {"gpt", "claude", "gemini"}
MODEL_PASSES = {"source_syn", "source_sem", "neighbour", "token_sign_type", "immediate_cue"}
ALL_PASSES = MODEL_PASSES | {"post_offset_mechanical"}

EXPECTED_SAMPLING_RULES = {
    "sr_001": ("preoffset_pilot", "draw_per_block", "15", "1"),
    "sr_002": ("target_pilot", "select_per_block", "10", "4"),
    "sr_003": ("preoffset_pilot", "minimum_eligible_per_block", "10", "3"),
    "sr_004": ("target_pilot", "minimum_codable_per_block", "8", "5"),
    "sr_005": ("all_pilot", "max_draws_per_speaker_per_block", "2", "1"),
    "sr_006": ("all_pilot", "max_draws_per_collection_per_block", "2", "1"),
    "sr_007": ("target_pilot", "max_global_speaker_share", "0.05", "3"),
    "sr_008": ("target_pilot", "max_global_collection_share", "0.10", "3"),
    "sr_009": ("target_pilot", "target_selection_order", "round_robin_within_block_rank_then_frozen_block_order", "2"),
    "sr_010": ("evaluation", "required_completed_preoffset_packets", "240", "6"),
    "sr_011": ("target_pilot", "maximum_target_packets", "160", "6"),
    "sr_012": ("confirmatory", "pilot_event_disposition", "exclude_all_pilot_occurrences", "7"),
    "sr_013": ("pathway_sensitivity", "minimum_retained_training_blocks", "10", "5"),
    "sr_014": ("pathway_sensitivity", "minimum_retained_blocks_per_sem_side", "4", "5"),
    "sr_015": ("evaluation", "required_completed_target_packets", "all_selected", "6"),
    "sr_016": ("evaluation", "maximum_evaluation_points", "1", "6"),
    "sr_017": ("all_pilot", "cap_conflict_action", "skip_and_continue", "3"),
    "sr_018": ("all_pilot", "sampling_disposition_log", "required", "7"),
}

EXPECTED_RELIABILITY_GATES = {
    "rg_001": ("source_syn_each_family", "within_family_repeat_stability", "gte", "0.90", "halt"),
    "rg_002": ("source_sem_each_family", "within_family_repeat_stability", "gte", "0.90", "halt"),
    "rg_003": ("each_principal_neighbour_each_family", "within_family_repeat_stability", "gte", "0.85", "halt"),
    "rg_004": ("token_sign_type_each_family", "within_family_repeat_stability", "gte", "0.85", "halt"),
    "rg_005": ("each_principal_immediate_cue_each_family", "within_family_repeat_stability", "gte", "0.85", "halt"),
    "rg_006": ("each_primary_source_unit", "stable_family_count", "eq", "3", "primary_label_eligibility"),
    "rg_007": ("each_primary_source_unit", "unanimous_three_family_consensus", "eq", "1", "primary_label_eligibility"),
    "rg_008": ("each_primary_source_unit", "expert_confirms_consensus", "eq", "1", "primary_label_eligibility"),
    "rg_009": ("source_syn_and_sem", "expert_audit_coverage", "eq", "1.00", "halt"),
    "rg_010": ("neighbour_and_token_disagreements", "expert_audit_coverage", "eq", "1.00", "halt"),
    "rg_011": ("consensus_immediate_cues", "expert_random_audit_fraction", "gte", "0.25", "halt"),
    "rg_012": ("consensus_immediate_cues", "expert_correction_rate", "lte", "0.10", "remediable_before_outcome_join"),
    "rg_013": ("primary_trajectory", "deterministic_recomputation_rate", "eq", "1.00", "halt"),
    "rg_014": ("expert_boundary_repeat", "median_absolute_difference_ms", "lte", "50", "halt"),
    "rg_015": ("expert_boundary_repeat", "percentile_95_absolute_difference_ms", "lte", "100", "halt"),
    "rg_016": ("each_primary_field", "proportion_uncertain_or_uncodable", "lte", "0.15", "halt"),
    "rg_017": ("uncodable_trajectory_rate", "max_absolute_source_cell_rate_difference", "lte", "0.10", "halt"),
    "rg_018": ("interjection_syn", "inter_model_nominal_alpha", "gte", "0.80", "halt"),
    "rg_019": ("interjection_syn", "inter_model_raw_agreement", "gte", "0.85", "halt"),
    "rg_020": ("interjection_sem", "inter_model_nominal_alpha", "gte", "0.80", "halt"),
    "rg_021": ("interjection_sem", "inter_model_raw_agreement", "gte", "0.85", "halt"),
    "rg_022": ("each_principal_neighbour", "inter_model_nominal_alpha", "gte", "0.75", "halt"),
    "rg_023": ("each_principal_neighbour", "inter_model_raw_agreement", "gte", "0.80", "halt"),
    "rg_024": ("token_sign_type_assignment", "inter_model_nominal_alpha", "gte", "0.80", "halt"),
    "rg_025": ("token_sign_type_assignment", "inter_model_raw_agreement", "gte", "0.85", "halt"),
    "rg_026": ("each_principal_categorical_immediate_cue", "inter_model_nominal_alpha", "gte", "0.70", "halt"),
    "rg_027": ("each_principal_categorical_immediate_cue", "inter_model_raw_agreement", "gte", "0.80", "halt"),
    "rg_028": ("source_syn_and_sem", "panel_audit_raw_agreement", "gte", "0.85", "halt"),
    "rg_029": ("remaining_subjective_fields", "panel_audit_raw_agreement", "gte", "0.80", "halt"),
}

EXPECTED_FEASIBILITY_GATES = {
    "fg_001": ("gate0_access", "audiobnc_research_use_licence_record", "eq", "present", "status"),
    "fg_002": ("gate0_access", "authenticated_audiobnc_access", "eq", "confirmed", "status"),
    "fg_003": ("gate0_access", "licence_compliant_local_storage_workflow", "eq", "confirmed", "status"),
    "fg_004": ("gate0_audio", "audited_events", "gte", "40", "events"),
    "fg_005": ("gate0_audio", "audited_pilot_blocks", "gte", "8", "outer_blocks"),
    "fg_006": ("gate0_audio", "measurement_resolution_ms", "eq", "10", "ms"),
    "fg_007": ("gate0_audio", "median_absolute_algorithm_expert_boundary_difference_ms", "lte", "50", "ms"),
    "fg_008": ("gate0_audio", "percentile_95_absolute_algorithm_expert_boundary_difference_ms", "lte", "100", "ms"),
    "fg_009": ("gatec_model_panel", "distinct_registered_model_families", "eq", "3", "families"),
    "fg_010": ("gatec_model_panel", "repeats_per_family_per_critical_pass", "eq", "2", "runs"),
    "fg_011": ("gatec_model_panel", "exact_resolved_versions_pinned", "eq", "confirmed", "status"),
    "fg_012": ("gatec_model_panel", "prompt_packet_response_evidence_and_settings_hashes", "eq", "complete", "status"),
    "fg_013": ("gatec_expert", "source_only_expert_auditor_available", "eq", "1", "expert"),
    "fg_014": ("gate0_data_governance", "raw_audio_sent_to_external_models", "eq", "0", "events"),
}


def read_header(path: Path) -> list[str]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.reader(handle)
        try:
            header = next(reader)
        except StopIteration as error:
            raise SystemExit(f"Empty CSV template: {path.name}") from error
        if next(reader, None) is not None:
            raise SystemExit(f"Template must contain only a header: {path.name}")
    if not header or any(not field for field in header):
        raise SystemExit(f"Blank field in template: {path.name}")
    if len(header) != len(set(header)):
        raise SystemExit(f"Duplicate field in template: {path.name}")
    return header


def field_matches(header: set[str], field_name: str) -> bool:
    return field_name in header or any(field.endswith(f"_{field_name}") for field in header)


def read_rows(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise SystemExit(f"Missing CSV header: {path.name}")
        rows = list(reader)
    if not rows:
        raise SystemExit(f"Populated registry contains no rows: {path.name}")
    return reader.fieldnames, rows


def require_unique(rows: list[dict[str, str]], field: str, filename: str) -> dict[str, dict[str, str]]:
    indexed: dict[str, dict[str, str]] = {}
    for row in rows:
        value = row[field]
        if not value:
            raise SystemExit(f"Blank {field} in {filename}")
        if value in indexed:
            raise SystemExit(f"Duplicate {field} in {filename}: {value}")
        indexed[value] = row
    return indexed


def validate(directory: Path) -> dict[str, int]:
    templates = {
        path.name.removesuffix("-template.csv"): set(read_header(path))
        for path in sorted(directory.glob("*-template.csv"))
    }
    missing_templates = REQUIRED_TEMPLATES - templates.keys()
    if missing_templates:
        raise SystemExit(f"Missing templates: {sorted(missing_templates)}")

    for template_name, required in REQUIRED_FIELDS.items():
        missing = required - templates[template_name]
        if missing:
            raise SystemExit(f"{template_name}-template.csv missing fields: {sorted(missing)}")

    for registry_name in POPULATED_REGISTRIES:
        header, _ = read_rows(directory / f"{registry_name}.csv")
        if set(header) != templates[registry_name]:
            raise SystemExit(f"{registry_name}.csv header differs from its template")

    _, codebook_rows = read_rows(directory / "codebook.csv")
    seen_codebook: set[tuple[str, str, str, str]] = set()
    for row in codebook_rows:
        template_name = row["template_name"]
        field_name = row["field_name"]
        key = (row["codebook_version"], template_name, field_name, row["allowed_value"])
        if key in seen_codebook:
            raise SystemExit(f"Duplicate codebook value: {key}")
        seen_codebook.add(key)
        if template_name == "all":
            if not any(field_matches(header, field_name) for header in templates.values()):
                raise SystemExit(f"Codebook all-field matches no template: {field_name}")
        elif template_name not in templates:
            raise SystemExit(f"Codebook references unknown template: {template_name}")
        elif not field_matches(templates[template_name], field_name):
            raise SystemExit(f"Codebook field {field_name} not found in {template_name}")

    _, checklist_rows = read_rows(directory / "leakage-checklist.csv")
    checklist = require_unique(checklist_rows, "audit_item_id", "leakage-checklist.csv")
    if set(checklist) != {f"la_{number:03d}" for number in range(1, 48)}:
        raise SystemExit("Leakage checklist must contain exactly la_001 through la_047")
    for item_id, row in checklist.items():
        if row["failure_class"] not in FAILURE_CLASSES:
            raise SystemExit(f"Invalid failure class for {item_id}: {row['failure_class']}")

    _, role_rows = read_rows(directory / "role-separation-matrix.csv")
    observed_pairs: set[frozenset[str]] = set()
    for row in role_rows:
        pair = frozenset((row["left_pass_id"], row["right_pass_id"]))
        if len(pair) != 2 or not pair <= ALL_PASSES:
            raise SystemExit(f"Invalid pass pair: {sorted(pair)}")
        if pair in observed_pairs:
            raise SystemExit(f"Duplicate pass pair: {sorted(pair)}")
        observed_pairs.add(pair)
        if (
            row["shared_context_allowed"] != "no"
            or row["shared_response_allowed"] != "no"
            or row["minimum_model_families_per_pass"] != "3"
        ):
            raise SystemExit(f"Pass separation weakened for pair: {sorted(pair)}")
    expected_pairs = {frozenset(pair) for pair in itertools.combinations(ALL_PASSES, 2)}
    if observed_pairs != expected_pairs:
        raise SystemExit("Role matrix must prohibit all fifteen cross-pass overlaps")

    _, registry_rows = read_rows(directory / "model-registry.csv")
    model_registry = require_unique(registry_rows, "model_registry_id", "model-registry.csv")
    if {row["model_family"] for row in registry_rows} != MODEL_FAMILIES or len(registry_rows) != 3:
        raise SystemExit("Model registry must contain exactly GPT, Claude, and Gemini")
    for row in registry_rows:
        if row["temperature"] != "0" or row["tool_access"] != "none" or row["network_access"] != "none":
            raise SystemExit(f"Unsafe or stochastic model settings for {row['model_registry_id']}")
        if row["context_policy"] != "fresh_stateless_single_pass":
            raise SystemExit(f"Model context policy changed for {row['model_registry_id']}")
        if row["data_class_allowed"] != "redacted_text_only":
            raise SystemExit(f"Model data class changed for {row['model_registry_id']}")
        if row["version_drift_action"] != "halt_and_refreeze_before_new_packets":
            raise SystemExit(f"Version drift policy changed for {row['model_registry_id']}")
        if row["status"] == "active" and (
            row["model_version"] == "exact_resolved_snapshot_required"
            or len(row["settings_sha256"]) != 64
        ):
            raise SystemExit(f"Active registry row is not exactly frozen: {row['model_registry_id']}")

    _, route_rows = read_rows(directory / "annotation-routes.csv")
    require_unique(route_rows, "route_id", "annotation-routes.csv")
    routes_by_pass: dict[str, set[str]] = {pass_id: set() for pass_id in MODEL_PASSES}
    for row in route_rows:
        if row["pass_id"] not in MODEL_PASSES:
            raise SystemExit(f"Unknown model pass: {row['pass_id']}")
        if row["model_registry_id"] not in model_registry:
            raise SystemExit(f"Unknown model registry id: {row['model_registry_id']}")
        family = model_registry[row["model_registry_id"]]["model_family"]
        routes_by_pass[row["pass_id"]].add(family)
        if row["repeat_count"] != "2" or row["consensus_role"] != "family_vote":
            raise SystemExit(f"Annotation route is not a two-repeat family vote: {row['route_id']}")
        if not row["prohibited_fields"]:
            raise SystemExit(f"Annotation route lacks prohibited fields: {row['route_id']}")
    for pass_id, families in routes_by_pass.items():
        if families != MODEL_FAMILIES:
            raise SystemExit(f"Pass {pass_id} lacks the frozen three-family panel")

    _, sampling_rows = read_rows(directory / "sampling-rules.csv")
    sampling = require_unique(sampling_rows, "rule_id", "sampling-rules.csv")
    if set(sampling) != set(EXPECTED_SAMPLING_RULES):
        raise SystemExit("Sampling registry does not contain the frozen rule set")
    for rule_id, expected in EXPECTED_SAMPLING_RULES.items():
        row = sampling[rule_id]
        observed = (row["scope"], row["parameter"], row["value"], row["precedence"])
        if observed != expected:
            raise SystemExit(f"Sampling rule changed for {rule_id}: {observed}")

    _, reliability_rows = read_rows(directory / "reliability-gates.csv")
    reliability = require_unique(reliability_rows, "gate_id", "reliability-gates.csv")
    if set(reliability) != set(EXPECTED_RELIABILITY_GATES):
        raise SystemExit("Reliability registry does not contain the frozen pilot gates")
    for gate_id, expected in EXPECTED_RELIABILITY_GATES.items():
        row = reliability[gate_id]
        observed = (
            row["target"], row["statistic"], row["operator"], row["threshold"],
            row["decision_use"],
        )
        if row["study_stage"] != "prepilot" or observed != expected:
            raise SystemExit(f"Reliability gate changed for {gate_id}: {observed}")

    _, feasibility_rows = read_rows(directory / "feasibility-gates.csv")
    feasibility = require_unique(feasibility_rows, "gate_id", "feasibility-gates.csv")
    if set(feasibility) != set(EXPECTED_FEASIBILITY_GATES):
        raise SystemExit("Feasibility registry does not contain the frozen gates")
    for gate_id, expected in EXPECTED_FEASIBILITY_GATES.items():
        row = feasibility[gate_id]
        observed = (row["stage"], row["requirement"], row["operator"], row["threshold"], row["unit"])
        if observed != expected:
            raise SystemExit(f"Feasibility gate changed for {gate_id}: {observed}")
        if row["failure_action"] != "activate_semantic_repetition_fallback":
            raise SystemExit(f"Feasibility failure action changed for {gate_id}")

    _, model_rows = read_rows(directory / "model-comparisons.csv")
    models = require_unique(model_rows, "model_id", "model-comparisons.csv")
    required_models = {
        "base_rate", "immediate_cue", "matched_common_baseline", "flat_diagnostic",
        "model_sem", "model_syn", "model_both", "sem_given_syn", "syn_given_sem",
    }
    if set(models) != required_models:
        raise SystemExit("Model registry does not contain exactly the frozen nine arms")
    common = {"immediate_cues", "neighbour_labels", "form_covariates"}
    if set(models["matched_common_baseline"]["components"].split("|")) != common:
        raise SystemExit("Matched common baseline differs from its frozen components")
    sem = common | {"interjection_sem_declaration_specific"}
    syn = common | {"interjection_syn_declaration_specific"}
    both = sem | {"interjection_syn_declaration_specific"}
    if set(models["model_sem"]["components"].split("|")) != sem:
        raise SystemExit("Total sem model must add only declaration-specific sem")
    if set(models["model_syn"]["components"].split("|")) != syn:
        raise SystemExit("Total syn model must add only declaration-specific syn")
    if set(models["model_both"]["components"].split("|")) != both:
        raise SystemExit("Joint model must contain separate sem and syn main effects")
    if "interaction" in models["model_both"]["components"]:
        raise SystemExit("Joint model must not include a sem-by-syn interaction")
    if models["model_sem"]["comparison_model_id"] != "matched_common_baseline":
        raise SystemExit("Total sem comparison has the wrong baseline")
    if models["model_syn"]["comparison_model_id"] != "matched_common_baseline":
        raise SystemExit("Total syn comparison has the wrong baseline")
    if models["sem_given_syn"]["comparison_model_id"] != "model_syn":
        raise SystemExit("Conditional sem comparison has the wrong baseline")
    if models["syn_given_sem"]["comparison_model_id"] != "model_sem":
        raise SystemExit("Conditional syn comparison has the wrong baseline")
    for model_id in ("sem_given_syn", "syn_given_sem"):
        if models[model_id]["evidential_status"] != "complementarity_diagnostic":
            raise SystemExit(f"Conditional contrast must be a complementarity diagnostic: {model_id}")
    primary_arms = {row["model_id"] for row in model_rows if row["evidential_status"] == "co_primary"}
    if primary_arms != {"model_sem", "model_syn"}:
        raise SystemExit(f"Co-primary arms must be model_sem and model_syn: {sorted(primary_arms)}")

    _, contrast_rows = read_rows(directory / "predictive-contrast.csv")
    contrasts = require_unique(contrast_rows, "contrast_id", "predictive-contrast.csv")
    expected_contrasts = {
        "delta_sem_total": ("model_sem", "matched_common_baseline"),
        "delta_syn_total": ("model_syn", "matched_common_baseline"),
        "delta_sem_given_syn": ("model_both", "model_syn"),
        "delta_syn_given_sem": ("model_both", "model_sem"),
        "delta_sem_minus_syn": ("model_sem", "model_syn"),
    }
    if set(contrasts) != set(expected_contrasts):
        raise SystemExit("Predictive contrast registry is incomplete")
    for contrast_id, pair in expected_contrasts.items():
        row = contrasts[contrast_id]
        if (row["left_model_id"], row["right_model_id"]) != pair:
            raise SystemExit(f"Predictive contrast changed for {contrast_id}")
        if row["aggregation_unit"] != "form_block" or row["paired_on"] != "test_outer_block_id":
            raise SystemExit(f"Predictive contrast is not paired by held-out form block: {contrast_id}")
        if not row["covariance_set_id"]:
            raise SystemExit(f"Predictive contrast lacks covariance set: {contrast_id}")
        if contrast_id in {"delta_sem_given_syn", "delta_syn_given_sem"} and row["evidential_status"] != "complementarity_diagnostic":
            raise SystemExit(f"Conditional predictive contrast is not labelled diagnostic: {contrast_id}")
    if {row["covariance_set_id"] for row in contrast_rows} != {"joint_all_contrasts"}:
        raise SystemExit("All five predictive contrasts must share one joint covariance set")

    _, decision_rows = read_rows(directory / "decision-rules.csv")
    decision_rules = require_unique(decision_rows, "rule_id", "decision-rules.csv")
    expected_rule_ids = {"mug_sem", "mug_syn", "mug_conditional", "mug_sem_syn", "fail_sem_edge", "fail_syn_edge"}
    if set(decision_rules) != expected_rule_ids:
        raise SystemExit("Decision-rule registry is incomplete")
    for rule_id, row in decision_rules.items():
        if row["status"] == "active" and "TO_BE_FROZEN" in {
            row["threshold_value"], row["calibration_tolerance_value"]
        }:
            raise SystemExit(f"Active decision rule retains an unfrozen threshold: {rule_id}")
    for row in contrast_rows:
        if row["minimum_useful_gain_id"] not in decision_rules:
            raise SystemExit(f"Unknown decision rule in predictive contrast: {row['contrast_id']}")

    _, declaration_rows = read_rows(directory / "projective-declarations.csv")
    declarations = require_unique(declaration_rows, "declaration_id", "projective-declarations.csv")
    expected_sources = {
        "decl_sem_floor_transfer": "interjection_sem_declaration_specific",
        "decl_syn_floor_transfer": "interjection_syn_declaration_specific",
    }
    if set(declarations) != set(expected_sources):
        raise SystemExit("Projective declaration registry must contain exactly the sem and syn edges")
    for declaration_id, source in expected_sources.items():
        row = declarations[declaration_id]
        if row["source_category"] != source or row["outcome"] != "four_way_floor_transfer_2500":
            raise SystemExit(f"Projective declaration changed for {declaration_id}")
        if not all(row[field] for field in ("bearer", "population", "conditions", "transformations", "timescale", "evidential_standard")):
            raise SystemExit(f"Projective declaration is incomplete: {declaration_id}")
        if row["tolerance_rule_id"] not in decision_rules or row["failure_rule_id"] not in decision_rules:
            raise SystemExit(f"Projective declaration has an unknown rule: {declaration_id}")

    trajectory_values = {
        row["allowed_value"] for row in codebook_rows
        if row["template_name"] == "derived-outcomes" and row["field_name"] == "post_offset_trajectory"
    }
    required_trajectories = {
        "DIFFERENT_SPEAKER_ENTRY_2500", "SOURCE_ENTRY_2500", "NO_VOCAL_ENTRY_2500",
        "SIMULTANEOUS_OR_UNORDERED_2500",
    }
    if trajectory_values != required_trajectories:
        raise SystemExit("Derived trajectory codebook must contain exactly four substantive levels")

    obsolete_fields = {"fitted_judgement", "first_entry_minimality", "competitive_overlap", "fittedness_sensitivity_outcome"}
    for template_name in ("post-offset-trajectory", "derived-outcomes"):
        leaked = obsolete_fields & templates[template_name]
        if leaked:
            raise SystemExit(f"Obsolete subjective outcome fields remain in {template_name}: {sorted(leaked)}")

    controlled_derivation_fields = {
        "target_offset_source", "first_audible_source", "first_vocal_source",
        "first_word_source", "target_tcu_offset_ms", "first_audible_onset_ms",
        "first_vocal_onset_ms", "first_word_onset_ms", "first_vocalizer_type",
        "speaker_identity_status", "simultaneous_or_unordered_valid",
        "technical_problem", "context_request_status", "context_insufficient",
    }
    covered_derivation_fields = {
        row["field_name"] for row in codebook_rows if row["template_name"] == "post-offset-trajectory"
    }
    missing_controls = controlled_derivation_fields - covered_derivation_fields
    if missing_controls:
        raise SystemExit(f"Derivation inputs lack controlled values: {sorted(missing_controls)}")

    immediate_controls = {
        "syntactic_packaging", "tcu_complete_at_offset", "addressivity",
        "summons_status", "projected_source_continuation", "prosodic_independence",
        "stance_polarity", "stance_intensity", "repetition_type", "complement_presence",
    }
    covered_immediate = {
        row["field_name"] for row in codebook_rows if row["template_name"] == "immediate-cue"
    }
    if immediate_controls - covered_immediate:
        raise SystemExit(f"Enumerated immediate cues lack codebook values: {sorted(immediate_controls - covered_immediate)}")

    for field, expected in {
        "declaration_sem_side": {"sem_positive", "sem_negative", "mixed_or_uncertain"},
        "declaration_syn_side": {"syn_positive", "syn_negative", "mixed_or_uncertain"},
    }.items():
        observed = {
            row["allowed_value"] for row in codebook_rows
            if row["template_name"] == "outer-block-membership" and row["field_name"] == field
        }
        if observed != expected:
            raise SystemExit(f"Block-level {field} codebook is incomplete")

    holdout_values = {
        row["allowed_value"] for row in codebook_rows
        if row["template_name"] == "heldout-predictive-score" and row["field_name"] == "holdout_type"
    }
    if holdout_values != {"principal_outer_block", "component_exclusion", "pathway_exclusion"}:
        raise SystemExit("Held-out score codebook must cover principal, component, and pathway exclusions")

    return {
        "n_templates": len(templates),
        "n_codebook_values": len(codebook_rows),
        "n_leakage_checks": len(checklist_rows),
        "n_model_families": len(registry_rows),
        "n_annotation_routes": len(route_rows),
        "n_model_arms": len(model_rows),
        "n_predictive_contrasts": len(contrast_rows),
        "n_projective_declarations": len(declaration_rows),
        "n_decision_rules": len(decision_rows),
        "n_reliability_gates": len(reliability_rows),
        "n_feasibility_gates": len(feasibility_rows),
        "n_sampling_rules": len(sampling_rows),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=Path(__file__).with_name("cabnc-prepilot"))
    args = parser.parse_args()
    result = validate(args.input)
    print("status=ok " + " ".join(f"{key.removeprefix('n_')}={value}" for key, value in result.items()))


if __name__ == "__main__":
    main()
