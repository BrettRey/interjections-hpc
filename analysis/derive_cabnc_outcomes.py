#!/usr/bin/env python3
"""Derive frozen CABNC timing summaries and four-way trajectory outcomes."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
from pathlib import Path


DERIVATION_VERSION = "0.2.0"
OUTPUT_FIELDS = [
    "packet_event_id",
    "outcome_derivation_version",
    "source_row_sha256",
    "derivation_code_sha256",
    "signed_first_audible_latency_ms",
    "signed_first_vocal_latency_ms",
    "signed_first_word_latency_ms",
    "vocal_entry_within_1500",
    "vocal_entry_within_2000",
    "vocal_entry_within_2500",
    "outcome_coding_status",
    "outcome_missingness_reason",
    "post_offset_trajectory",
    "primary_next_position_outcome",
    "derived_by",
    "derived_at",
    "integrity_check_status",
]

AUDIO_HASH_FIELDS = {
    "prepared_wav_sha256",
    "waveform_png_sha256",
    "spectrogram_png_sha256",
    "activity_csv_sha256",
    "preparation_code_sha256",
    "provenance_json_sha256",
}
REQUIRED_INPUT_FIELDS = {
    "packet_event_id",
    "audio_preparation_version",
    *AUDIO_HASH_FIELDS,
    "target_tcu_offset_ms",
    "target_offset_source",
    "first_audible_onset_ms",
    "first_audible_source",
    "first_vocal_onset_ms",
    "first_vocal_source",
    "first_word_onset_ms",
    "first_word_source",
    "timing_resolution_ms",
    "first_vocal_speaker_id",
    "first_vocalizer_type",
    "speaker_identity_status",
    "simultaneous_or_unordered_valid",
    "technical_problem",
    "context_request_status",
    "context_insufficient",
}

BOUNDARY_SOURCES = {
    "expert_audio",
    "energy_activity_proposal_audited",
    "transcript_bullet_audited",
    "unavailable",
}
VOCALIZER_TYPES = {
    "source_speaker",
    "different_speaker",
    "simultaneous_or_unordered",
    "none_by_2500",
    "ambiguous",
    "uncodable",
}
SPEAKER_IDENTITY_STATUSES = {"resolved", "ambiguous", "unavailable", "not_applicable"}
TRAJECTORY_TO_PRIMARY = {
    "DIFFERENT_SPEAKER_ENTRY_2500": "different_speaker_entry_2500",
    "SOURCE_ENTRY_2500": "source_entry_2500",
    "NO_VOCAL_ENTRY_2500": "no_vocal_entry_2500",
    "SIMULTANEOUS_OR_UNORDERED_2500": "simultaneous_or_unordered_2500",
}


def row_sha256(row: dict[str, str]) -> str:
    canonical = json.dumps(row, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def is_sha256(value: str) -> bool:
    return len(value) == 64 and all(character in "0123456789abcdef" for character in value)


def parse_flag(value: str, field: str) -> bool:
    if value == "yes":
        return True
    if value == "no":
        return False
    raise ValueError(f"{field} must be yes or no; observed {value!r}")


def parse_nonnegative_number(value: str, field: str, *, required: bool) -> float | None:
    if not value:
        if required:
            raise ValueError(f"{field} is required")
        return None
    try:
        number = float(value)
    except ValueError as error:
        raise ValueError(f"{field} is not numeric: {value!r}") from error
    if not math.isfinite(number) or number < 0:
        raise ValueError(f"{field} must be a finite nonnegative number")
    return number


def format_number(value: float | None) -> str:
    if value is None:
        return ""
    if abs(value) < 1e-12:
        value = 0.0
    return format(value, ".15g")


def validate_boundary(
    row: dict[str, str], onset_field: str, source_field: str, *, required: bool
) -> float | None:
    onset = parse_nonnegative_number(row[onset_field], onset_field, required=required)
    source = row[source_field]
    if source not in BOUNDARY_SOURCES:
        raise ValueError(f"invalid {source_field}: {source!r}")
    if onset is None and source != "unavailable":
        raise ValueError(f"blank {onset_field} requires {source_field}=unavailable")
    if onset is not None and source == "unavailable":
        raise ValueError(f"numeric {onset_field} requires an audited boundary source")
    return onset


def validate_provenance(row: dict[str, str]) -> None:
    if not row["audio_preparation_version"]:
        raise ValueError("audio_preparation_version is required")
    for field in AUDIO_HASH_FIELDS:
        if not is_sha256(row[field]):
            raise ValueError(f"{field} must be a lowercase SHA-256 digest")
    try:
        resolution = float(row["timing_resolution_ms"])
    except ValueError as error:
        raise ValueError(
            f"timing_resolution_ms is not numeric: {row['timing_resolution_ms']!r}"
        ) from error
    if not math.isfinite(resolution) or resolution != 10:
        raise ValueError("primary trajectory requires 10 ms timing resolution")
    if row["context_request_status"] not in {
        "not_requested",
        "requested_and_granted",
        "requested_unavailable",
    }:
        raise ValueError(f"invalid context_request_status: {row['context_request_status']!r}")


def extract_boundaries(row: dict[str, str]) -> tuple[float, float | None, float | None, float | None]:
    target = validate_boundary(row, "target_tcu_offset_ms", "target_offset_source", required=True)
    assert target is not None
    audible = validate_boundary(row, "first_audible_onset_ms", "first_audible_source", required=False)
    vocal = validate_boundary(row, "first_vocal_onset_ms", "first_vocal_source", required=False)
    word = validate_boundary(row, "first_word_onset_ms", "first_word_source", required=False)
    if audible is not None and vocal is not None and audible > vocal:
        raise ValueError("first_audible_onset_ms cannot follow first_vocal_onset_ms")
    if vocal is not None and word is not None and vocal > word:
        raise ValueError("first_vocal_onset_ms cannot follow first_word_onset_ms")
    return target, audible, vocal, word


def derive_trajectory(row: dict[str, str], vocal_latency_ms: float | None = None) -> str:
    validate_provenance(row)
    target, _, vocal, _ = extract_boundaries(row)
    if vocal_latency_ms is None and vocal is not None:
        vocal_latency_ms = vocal - target

    technical_problem = parse_flag(row["technical_problem"], "technical_problem")
    context_insufficient = parse_flag(row["context_insufficient"], "context_insufficient")
    vocalizer = row["first_vocalizer_type"]
    identity = row["speaker_identity_status"]
    simultaneous_valid = row["simultaneous_or_unordered_valid"]

    if vocalizer not in VOCALIZER_TYPES:
        raise ValueError(f"invalid first_vocalizer_type: {vocalizer!r}")
    if identity not in SPEAKER_IDENTITY_STATUSES:
        raise ValueError(f"invalid speaker_identity_status: {identity!r}")
    if simultaneous_valid not in {"yes", "no", "not_applicable"}:
        raise ValueError(
            "simultaneous_or_unordered_valid must be yes, no, or not_applicable"
        )

    if technical_problem or context_insufficient:
        return "UNCODABLE"
    if vocalizer in {"ambiguous", "uncodable"} or identity in {"ambiguous", "unavailable"}:
        return "UNCODABLE"

    if vocalizer == "none_by_2500":
        if identity != "not_applicable" or simultaneous_valid != "not_applicable":
            raise ValueError("none_by_2500 requires not-applicable identity and simultaneity")
        if row["first_vocal_speaker_id"]:
            raise ValueError("none_by_2500 requires a blank first_vocal_speaker_id")
        if vocal_latency_ms is not None and vocal_latency_ms <= 2500:
            raise ValueError("none_by_2500 conflicts with first_vocal_onset_ms")
        return "NO_VOCAL_ENTRY_2500"

    if identity != "resolved":
        raise ValueError(f"{vocalizer} requires resolved speaker identity")
    if not row["first_vocal_speaker_id"]:
        raise ValueError(f"{vocalizer} requires first_vocal_speaker_id")
    if vocal_latency_ms is None:
        raise ValueError(f"{vocalizer} requires first_vocal_onset_ms")
    if vocal_latency_ms > 2500:
        raise ValueError(f"{vocalizer} conflicts with a first vocal onset after 2500 ms")

    if vocalizer == "simultaneous_or_unordered":
        if simultaneous_valid == "yes":
            return "SIMULTANEOUS_OR_UNORDERED_2500"
        return "UNCODABLE"
    if simultaneous_valid != "not_applicable":
        raise ValueError(f"{vocalizer} requires simultaneous_or_unordered_valid=not_applicable")
    if vocalizer == "source_speaker":
        return "SOURCE_ENTRY_2500"
    if vocalizer == "different_speaker":
        return "DIFFERENT_SPEAKER_ENTRY_2500"
    raise AssertionError(f"Unhandled vocalizer type: {vocalizer}")


def derive_row(row: dict[str, str], *, derived_at: str, code_sha256: str) -> dict[str, str]:
    if not is_sha256(code_sha256):
        raise ValueError("derivation_code_sha256 must be a lowercase SHA-256 digest")
    validate_provenance(row)
    target, audible, vocal, word = extract_boundaries(row)
    audible_latency = None if audible is None else audible - target
    vocal_latency = None if vocal is None else vocal - target
    word_latency = None if word is None else word - target
    trajectory = derive_trajectory(row, vocal_latency)

    if trajectory == "UNCODABLE":
        window_values = {1500: "uncodable", 2000: "uncodable", 2500: "uncodable"}
        coding_status = "uncodable"
        if parse_flag(row["technical_problem"], "technical_problem"):
            missingness_reason = "technical_problem"
        elif parse_flag(row["context_insufficient"], "context_insufficient"):
            missingness_reason = "context_insufficient"
        elif row["speaker_identity_status"] in {"ambiguous", "unavailable"}:
            missingness_reason = "speaker_identity_ambiguous"
        elif row["first_vocalizer_type"] in {"ambiguous", "uncodable"}:
            missingness_reason = "vocalizer_uncodable"
        else:
            missingness_reason = "simultaneous_or_unordered_not_validated"
        reported_trajectory = ""
        primary_outcome = ""
    else:
        window_values = {
            window: "yes" if vocal_latency is not None and vocal_latency <= window else "no"
            for window in (1500, 2000, 2500)
        }
        coding_status = "codable"
        missingness_reason = "not_applicable"
        reported_trajectory = trajectory
        primary_outcome = TRAJECTORY_TO_PRIMARY[trajectory]

    return {
        "packet_event_id": row["packet_event_id"],
        "outcome_derivation_version": DERIVATION_VERSION,
        "source_row_sha256": row_sha256(row),
        "derivation_code_sha256": code_sha256,
        "signed_first_audible_latency_ms": format_number(audible_latency),
        "signed_first_vocal_latency_ms": format_number(vocal_latency),
        "signed_first_word_latency_ms": format_number(word_latency),
        "vocal_entry_within_1500": window_values[1500],
        "vocal_entry_within_2000": window_values[2000],
        "vocal_entry_within_2500": window_values[2500],
        "outcome_coding_status": coding_status,
        "outcome_missingness_reason": missingness_reason,
        "post_offset_trajectory": reported_trajectory,
        "primary_next_position_outcome": primary_outcome,
        "derived_by": "analysis/derive_cabnc_outcomes.py",
        "derived_at": derived_at,
        "integrity_check_status": "pass",
    }


def derive_file(input_path: Path, output_path: Path, derived_at: str) -> int:
    code_sha256 = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    with input_path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise SystemExit("Input has no header")
        missing = REQUIRED_INPUT_FIELDS - set(reader.fieldnames)
        if missing:
            raise SystemExit(f"Input missing fields: {sorted(missing)}")
        rows = list(reader)

    seen_events: set[str] = set()
    derived_rows: list[dict[str, str]] = []
    for line_number, row in enumerate(rows, start=2):
        event_id = row["packet_event_id"]
        if not event_id:
            raise SystemExit(f"Blank packet_event_id at line {line_number}")
        if event_id in seen_events:
            raise SystemExit(f"Duplicate packet_event_id: {event_id}")
        seen_events.add(event_id)
        try:
            derived_rows.append(derive_row(row, derived_at=derived_at, code_sha256=code_sha256))
        except ValueError as error:
            raise SystemExit(f"{event_id}: {error}") from error

    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=OUTPUT_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(derived_rows)
    return len(derived_rows)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--derived-at", required=True, help="Frozen ISO 8601 UTC timestamp")
    args = parser.parse_args()
    count = derive_file(args.input, args.output, args.derived_at)
    print(f"status=ok rows={count} derivation_version={DERIVATION_VERSION}")


if __name__ == "__main__":
    main()
