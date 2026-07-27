from __future__ import annotations

import csv
import sys
import tempfile
import unittest
from pathlib import Path


ANALYSIS_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ANALYSIS_DIR))

from derive_cabnc_outcomes import (  # noqa: E402
    OUTPUT_FIELDS,
    derive_file,
    derive_row,
    derive_trajectory,
)


def source_row(**overrides: str) -> dict[str, str]:
    digest = "a" * 64
    row = {
        "packet_event_id": "event_001",
        "audio_preparation_version": "0.1.0",
        "prepared_wav_sha256": digest,
        "waveform_png_sha256": digest,
        "spectrogram_png_sha256": digest,
        "activity_csv_sha256": digest,
        "preparation_code_sha256": digest,
        "provenance_json_sha256": digest,
        "target_tcu_offset_ms": "1000",
        "target_offset_source": "expert_audio",
        "first_audible_onset_ms": "1900",
        "first_audible_source": "expert_audio",
        "first_vocal_onset_ms": "2000",
        "first_vocal_source": "energy_activity_proposal_audited",
        "first_word_onset_ms": "2100",
        "first_word_source": "expert_audio",
        "timing_resolution_ms": "10",
        "first_vocal_speaker_id": "speaker_01",
        "first_vocalizer_type": "source_speaker",
        "speaker_identity_status": "resolved",
        "simultaneous_or_unordered_valid": "not_applicable",
        "technical_problem": "no",
        "context_request_status": "not_requested",
        "context_insufficient": "no",
    }
    row.update(overrides)
    return row


class CabncOutcomeDerivationTests(unittest.TestCase):
    def test_four_trajectory_levels_and_missingness_are_mechanical(self) -> None:
        self.assertEqual(derive_trajectory(source_row()), "SOURCE_ENTRY_2500")
        self.assertEqual(
            derive_trajectory(source_row(first_vocalizer_type="different_speaker")),
            "DIFFERENT_SPEAKER_ENTRY_2500",
        )
        self.assertEqual(
            derive_trajectory(
                source_row(
                    first_vocalizer_type="simultaneous_or_unordered",
                    first_vocal_speaker_id="speaker_01|speaker_02",
                    simultaneous_or_unordered_valid="yes",
                )
            ),
            "SIMULTANEOUS_OR_UNORDERED_2500",
        )
        self.assertEqual(
            derive_trajectory(
                source_row(
                    first_vocalizer_type="none_by_2500",
                    first_vocal_speaker_id="",
                    speaker_identity_status="not_applicable",
                    first_vocal_onset_ms="",
                    first_vocal_source="unavailable",
                    first_word_onset_ms="",
                    first_word_source="unavailable",
                )
            ),
            "NO_VOCAL_ENTRY_2500",
        )
        self.assertEqual(
            derive_trajectory(source_row(speaker_identity_status="ambiguous")),
            "UNCODABLE",
        )

    def test_no_vocal_by_2500_may_retain_a_later_measured_onset(self) -> None:
        row = source_row(
            first_vocalizer_type="none_by_2500",
            first_vocal_speaker_id="",
            speaker_identity_status="not_applicable",
            first_vocal_onset_ms="3501",
            first_word_onset_ms="3600",
        )
        self.assertEqual(derive_trajectory(row), "NO_VOCAL_ENTRY_2500")
        with self.assertRaises(ValueError):
            derive_trajectory({**row, "first_vocal_onset_ms": "3500"})

    def test_simultaneous_tie_must_be_valid_at_frozen_resolution(self) -> None:
        row = source_row(
            first_vocalizer_type="simultaneous_or_unordered",
            first_vocal_speaker_id="speaker_01|speaker_02",
            simultaneous_or_unordered_valid="no",
        )
        self.assertEqual(derive_trajectory(row), "UNCODABLE")

    def test_technical_and_context_problems_are_missingness(self) -> None:
        for overrides in ({"technical_problem": "yes"}, {"context_insufficient": "yes"}):
            derived = derive_row(
                source_row(**overrides),
                derived_at="2026-07-27T00:00:00Z",
                code_sha256="b" * 64,
            )
            self.assertEqual(derived["outcome_coding_status"], "uncodable")
            self.assertEqual(derived["post_offset_trajectory"], "")
            self.assertEqual(derived["primary_next_position_outcome"], "")
            self.assertEqual(derived["vocal_entry_within_2500"], "uncodable")

    def test_signed_latencies_and_three_windows_are_derived(self) -> None:
        derived = derive_row(
            source_row(
                first_audible_onset_ms="900",
                first_vocal_onset_ms="2600",
                first_word_onset_ms="2750",
                first_vocalizer_type="different_speaker",
            ),
            derived_at="2026-07-27T00:00:00Z",
            code_sha256="b" * 64,
        )
        self.assertEqual(derived["signed_first_audible_latency_ms"], "-100")
        self.assertEqual(derived["signed_first_vocal_latency_ms"], "1600")
        self.assertEqual(derived["signed_first_word_latency_ms"], "1750")
        self.assertEqual(derived["vocal_entry_within_1500"], "no")
        self.assertEqual(derived["vocal_entry_within_2000"], "yes")
        self.assertEqual(derived["vocal_entry_within_2500"], "yes")

    def test_window_boundaries_are_inclusive(self) -> None:
        derived = derive_row(
            source_row(
                first_audible_onset_ms="3400",
                first_vocal_onset_ms="3500",
                first_word_onset_ms="3500",
            ),
            derived_at="2026-07-27T00:00:00Z",
            code_sha256="b" * 64,
        )
        self.assertEqual(derived["vocal_entry_within_1500"], "no")
        self.assertEqual(derived["vocal_entry_within_2000"], "no")
        self.assertEqual(derived["vocal_entry_within_2500"], "yes")

    def test_audio_provenance_and_boundary_sources_are_mandatory(self) -> None:
        with self.assertRaises(ValueError):
            derive_trajectory(source_row(prepared_wav_sha256="not-a-hash"))
        with self.assertRaises(ValueError):
            derive_trajectory(source_row(timing_resolution_ms="20"))
        with self.assertRaises(ValueError):
            derive_trajectory(source_row(first_vocal_source="unavailable"))
        with self.assertRaises(ValueError):
            derive_trajectory(
                source_row(first_audible_onset_ms="", first_audible_source="expert_audio")
            )

    def test_boundary_order_is_checked(self) -> None:
        with self.assertRaises(ValueError):
            derive_trajectory(source_row(first_audible_onset_ms="2050"))
        with self.assertRaises(ValueError):
            derive_trajectory(source_row(first_word_onset_ms="1950"))

    def test_obsolete_subjective_outcomes_are_absent(self) -> None:
        self.assertNotIn("fittedness_sensitivity_outcome", OUTPUT_FIELDS)
        self.assertNotIn("first_entry_minimality", OUTPUT_FIELDS)

    def test_file_derivation_matches_schema_and_rejects_duplicates(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            temporary_path = Path(temporary)
            input_path = temporary_path / "input.csv"
            output_path = temporary_path / "output.csv"
            row = source_row()
            with input_path.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=list(row), lineterminator="\n")
                writer.writeheader()
                writer.writerow(row)
            self.assertEqual(derive_file(input_path, output_path, "2026-07-27T00:00:00Z"), 1)
            with output_path.open(encoding="utf-8", newline="") as handle:
                reader = csv.DictReader(handle)
                self.assertEqual(reader.fieldnames, OUTPUT_FIELDS)
                output_rows = list(reader)
            self.assertEqual(len(output_rows), 1)
            self.assertEqual(len(output_rows[0]["source_row_sha256"]), 64)
            self.assertEqual(len(output_rows[0]["derivation_code_sha256"]), 64)

            with input_path.open("a", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=list(row), lineterminator="\n")
                writer.writerow(row)
            with self.assertRaises(SystemExit):
                derive_file(input_path, output_path, "2026-07-27T00:00:00Z")


if __name__ == "__main__":
    unittest.main()
