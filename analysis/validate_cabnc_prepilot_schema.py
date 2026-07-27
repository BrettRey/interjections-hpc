#!/usr/bin/env python3
"""Validate CABNC pre-pilot templates, codebook, and leakage checklist."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


REQUIRED_TEMPLATES = {
    "audio-feasibility",
    "coder-assignment",
    "conversation-grouping",
    "derived-outcomes",
    "dossier-evidence",
    "dossier-reservations",
    "fold-map",
    "form-covariates",
    "form-relations",
    "hypothesis-awareness",
    "immediate-cue",
    "leakage-audit",
    "mechanical-eligibility",
    "neighbour-classification",
    "outer-block-membership",
    "packet-manifest",
    "post-offset-trajectory",
    "preoffset-eligibility",
    "primary-component-exclusions",
    "retrieval-bins",
    "sign-type-dossier",
    "sign-type-retrieval-bridge",
    "sign-types",
    "source-classification",
    "speaker-registry",
    "staffing-plan",
    "surface-aliases",
    "token-sign-type-assignment",
    "turn-collapse",
}

REQUIRED_FIELDS = {
    "source-classification": {
        "dossier_id", "classification_target", "card_type", "membership",
        "form_identity_masked", "presentation_order_index", "quarantine_action",
    },
    "token-sign-type-assignment": {
        "packet_event_id", "assigned_sign_type_id", "assignment_status",
    },
    "preoffset-eligibility": {
        "packet_event_id", "potential_recipient_available_at_offset",
        "timing_adequate", "eligibility_status",
    },
    "mechanical-eligibility": {
        "packet_event_id", "following_sequence_unclipped", "mechanical_duplicate",
        "eligibility_status",
    },
    "post-offset-trajectory": {
        "packet_event_id", "timing_source", "timing_resolution_ms",
        "first_post_offset_vocalizer_type", "first_post_offset_onset_ms",
        "first_entry_within_2500", "first_entry_minimality",
        "fitted_judgement",
    },
    "derived-outcomes": {
        "packet_event_id", "outcome_derivation_version",
        "post_offset_trajectory", "primary_next_position_outcome",
        "derived_by", "integrity_check_status",
    },
    "packet-manifest": {
        "packet_event_id", "collection_block_id", "principal_outer_block_id",
        "fold_map_version", "fold_map_hash", "random_seed",
    },
    "dossier-evidence": {
        "dossier_id", "declaration_id", "target_relation", "proxy_rule_id",
        "collection_block_id", "speaker_ids", "text_screen_status",
    },
    "coder-assignment": {
        "coder_id", "role_id", "is_protocol_author", "training_version",
        "separation_check_status",
    },
    "audio-feasibility": {
        "audio_audit_event_id", "collection_block_id",
        "audio_access_authorized", "measurement_resolution_ms",
        "absolute_offset_difference_ms", "clip_complete", "status",
    },
    "primary-component-exclusions": {
        "test_outer_block_id", "excluded_train_bin_id", "trigger_atom_id",
        "trigger_relation_id", "fold_map_version", "status",
    },
    "staffing-plan": {
        "coder_id", "role_id", "is_protocol_author", "training_version",
        "planned_status", "availability_confirmed", "conflict_check_status",
    },
}

FAILURE_CLASSES = {"halt", "remediable_before_unblinding", "note_only"}


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
    return field_name in header or any(
        field.endswith(f"_{field_name}") for field in header
    )


def validate(directory: Path) -> dict[str, int]:
    templates: dict[str, set[str]] = {}
    for path in sorted(directory.glob("*-template.csv")):
        name = path.name.removesuffix("-template.csv")
        templates[name] = set(read_header(path))

    missing_templates = REQUIRED_TEMPLATES - templates.keys()
    if missing_templates:
        raise SystemExit(f"Missing templates: {sorted(missing_templates)}")

    for template_name, required in REQUIRED_FIELDS.items():
        missing = required - templates[template_name]
        if missing:
            raise SystemExit(
                f"{template_name}-template.csv missing fields: {sorted(missing)}"
            )

    codebook_path = directory / "codebook.csv"
    seen_codebook = set()
    with codebook_path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise SystemExit("Codebook contains no controlled values")
    for row in rows:
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
            raise SystemExit(
                f"Codebook field {field_name} not found in {template_name}"
            )

    checklist_path = directory / "leakage-checklist.csv"
    seen_items = set()
    with checklist_path.open(encoding="utf-8", newline="") as handle:
        checklist_rows = list(csv.DictReader(handle))
    if len(checklist_rows) < 15:
        raise SystemExit("Leakage checklist is incomplete")
    for row in checklist_rows:
        item_id = row["audit_item_id"]
        if item_id in seen_items:
            raise SystemExit(f"Duplicate leakage audit item: {item_id}")
        seen_items.add(item_id)
        if row["failure_class"] not in FAILURE_CLASSES:
            raise SystemExit(
                f"Invalid failure class for {item_id}: {row['failure_class']}"
            )

    return {
        "n_templates": len(templates),
        "n_codebook_values": len(rows),
        "n_leakage_checks": len(checklist_rows),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        type=Path,
        default=Path(__file__).with_name("cabnc-prepilot"),
    )
    args = parser.parse_args()
    result = validate(args.input)
    print(
        "status=ok "
        f"templates={result['n_templates']} "
        f"codebook_values={result['n_codebook_values']} "
        f"leakage_checks={result['n_leakage_checks']}"
    )


if __name__ == "__main__":
    main()
