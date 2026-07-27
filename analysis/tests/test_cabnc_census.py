from __future__ import annotations

import sys
import subprocess
import tempfile
import unittest
from pathlib import Path

ANALYSIS_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ANALYSIS_DIR))

from cabnc_census import (  # noqa: E402
    build_logical_tiers,
    collection_block_id_from_segment,
    is_unknown_speaker_id,
    lexical_tokens,
    parse_corpus,
    recording_id_from_url,
    tape_id_from_url,
    timing_spans,
    verify_frozen_input,
)


def alias(family: str) -> dict:
    return {
        "form_family_id": family,
        "normalized_surface": family,
        "alias_rule_id": "test",
        "seed_group": "test",
        "notes": "",
        "variant_block_hint": "",
        "component_family_ids": "",
    }


class CabncCensusTests(unittest.TestCase):
    def test_timing_spans_support_current_and_legacy_delimiters(self) -> None:
        text = "x \x1510_20\x15 y •30_45•"
        self.assertEqual(timing_spans(text), [(10, 20), (30, 45)])

    def test_recording_id_comes_from_original_audio_url(self) -> None:
        self.assertEqual(
            recording_id_from_url("http://example.test/audio/REC001.wav"),
            "REC001",
        )
        self.assertEqual(recording_id_from_url(""), "")
        self.assertEqual(
            tape_id_from_url(
                "http://example.test/audio/021A-C0897X0123XX-AZZP0.wav"
            ),
            "021A-C0897X0123XX",
        )
        self.assertEqual(tape_id_from_url(""), "")
        self.assertEqual(collection_block_id_from_segment("KB7RE01A"), "KB7")

    def test_unknown_speaker_code_is_detected(self) -> None:
        self.assertTrue(is_unknown_speaker_id("KC7PSUN"))
        self.assertTrue(is_unknown_speaker_id("KC7PSUG"))
        self.assertFalse(is_unknown_speaker_id("PS007"))

    def test_lexical_tokens_skip_chat_markup_and_preserve_filled_pause(self) -> None:
        text = "0 . &=cough [<] (.) <Oh> uh-huh xxx"
        self.assertEqual(lexical_tokens(text), ["Oh", "uh-huh"])

    def test_logical_tiers_join_wrapped_lines(self) -> None:
        tiers, warnings, physical_main = build_logical_tiers([
            "@UTF8\n",
            "*AAA:\tOh\n",
            "\tthere \x1510_20\x15\n",
        ])
        self.assertFalse(warnings)
        self.assertEqual(physical_main, 1)
        self.assertEqual(tiers[-1].kind, "*")
        self.assertEqual(tiers[-1].text, "Oh there \x1510_20\x15")

    def test_parse_corpus_builds_spans_and_marks_candidates(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            corpus = Path(temporary) / "chat"
            corpus.mkdir()
            transcript = corpus / "TEST.cha"
            transcript.write_text(
                "@UTF8\n"
                "@PID:\tTEST\n"
                "@Participants:\tAAA Alice Adult, BBB Bob Adult\n"
                "@ID:\teng|TEST|AAA||||||||\n"
                "@ID:\teng|TEST|BBB||||||||\n"
                "@Media:\tTEST, audio\n"
                "@Comment:\toriginal media http://example.test/audio/REC001.wav\n"
                "@New Episode\n"
                "*AAA:\tOh &=laughs \x1510_20\x15\n"
                "\twow\n"
                "*AAA:\tright \x1521_40\x15\n"
                "*BBB:\tYeah •41_50•\n"
                "@New Episode\n"
                "*AAA:\t0 .\n"
                "*BBB:\tHuh ? \x1560_70\x15\n"
                "@End\n",
                encoding="utf-8",
            )
            aliases = {
                name: alias(name)
                for name in ["oh", "wow", "right", "yeah", "huh"]
            }
            datasets, smoke = parse_corpus(corpus, aliases, "test-commit")

        self.assertEqual(smoke["n_files"], 1)
        self.assertEqual(smoke["n_physical_main_tier_lines"], 5)
        self.assertEqual(smoke["n_analytic_spans"], 4)
        self.assertFalse(datasets["parse_warnings"])

        spans = datasets["analytic_spans"]
        self.assertEqual(spans[0]["normalized_text"], "oh wow right")
        self.assertEqual(spans[0]["start_ms"], 10)
        self.assertEqual(spans[0]["end_ms"], 40)
        self.assertEqual(spans[0]["gap_to_next_span_ms"], 1)
        self.assertEqual(spans[1]["episode_index"], 1)
        self.assertEqual(spans[2]["episode_index"], 2)
        self.assertEqual(spans[2]["normalized_text"], "")

        candidates = {
            row["normalized_surface"]: row
            for row in datasets["candidate_occurrences"]
        }
        self.assertTrue(candidates["oh"]["span_initial"])
        self.assertTrue(candidates["oh"]["main_tier_initial"])
        self.assertEqual(candidates["oh"]["candidate_tier_start_ms"], 10)
        self.assertEqual(candidates["oh"]["candidate_tier_end_ms"], 20)
        self.assertEqual(candidates["oh"]["source_span_end_ms"], 40)
        self.assertEqual(candidates["oh"]["recording_id"], "REC001")
        self.assertEqual(candidates["oh"]["collection_block_id"], "TES")
        self.assertFalse(candidates["right"]["span_initial"])
        self.assertTrue(candidates["right"]["main_tier_initial"])
        self.assertTrue(candidates["yeah"]["candidate_only_span"])
        self.assertIn("no_following_sequence", candidates["huh"]["auto_exclusion_code"])

        vocabulary = {
            row["normalized_surface"]: row
            for row in datasets["span_initial_vocabulary"]
        }
        self.assertEqual(vocabulary["oh"]["n_span_initial"], 1)
        self.assertEqual(vocabulary["yeah"]["n_span_initial"], 1)
        self.assertEqual(vocabulary["huh"]["n_span_initial"], 1)
        self.assertNotIn("right", vocabulary)

        census = {
            row["form_family_id"]: row
            for row in datasets["census_by_form"]
        }
        self.assertEqual(census["oh"]["n_initial_timed_segments"], 1)
        self.assertEqual(census["oh"]["n_initial_timed_recordings"], 1)
        self.assertEqual(census["oh"]["n_initial_unexcluded"], 1)
        self.assertEqual(census["huh"]["n_initial_auto_excluded"], 1)
        self.assertEqual(census["huh"]["n_initial_unexcluded"], 0)

    def test_parse_corpus_prefers_longest_multiword_alias(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            corpus = Path(temporary) / "chat"
            corpus.mkdir()
            (corpus / "TEST.cha").write_text(
                "@UTF8\n"
                "@PID:\tTEST\n"
                "@Participants:\tAAA Alice Adult, BBB Bob Adult\n"
                "@Media:\tTEST, audio\n"
                "@New Episode\n"
                "*AAA:\tThank you . \x1510_20\x15\n"
                "*BBB:\tOkay . \x1521_30\x15\n"
                "@End\n",
                encoding="utf-8",
            )
            aliases = {
                "thank": alias("thank"),
                "thank you": {
                    **alias("thanks"),
                    "normalized_surface": "thank you",
                    "alias_rule_id": "multiword",
                },
            }
            datasets, _ = parse_corpus(corpus, aliases, "test-commit")

        candidates = datasets["candidate_occurrences"]
        self.assertEqual(len(candidates), 1)
        self.assertEqual(candidates[0]["normalized_surface"], "thank you")
        self.assertEqual(candidates[0]["form_family_id"], "thanks")
        self.assertEqual(candidates[0]["token_index"], 0)
        self.assertEqual(candidates[0]["token_end_index"], 1)
        self.assertTrue(candidates[0]["candidate_only_span"])

    def test_multiword_alias_does_not_cross_main_tier_boundary(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            corpus = Path(temporary) / "chat"
            corpus.mkdir()
            (corpus / "TEST.cha").write_text(
                "@UTF8\n"
                "@PID:\tTEST\n"
                "@Participants:\tAAA Alice Adult, BBB Bob Adult\n"
                "@Media:\tTEST, audio\n"
                "@New Episode\n"
                "*AAA:\tThank . \x1510_20\x15\n"
                "*AAA:\tyou . \x1521_30\x15\n"
                "*BBB:\tOkay . \x1531_40\x15\n"
                "@End\n",
                encoding="utf-8",
            )
            aliases = {
                "thank": alias("thank"),
                "thank you": {
                    **alias("thanks"),
                    "normalized_surface": "thank you",
                    "alias_rule_id": "multiword",
                },
            }
            datasets, _ = parse_corpus(corpus, aliases, "test-commit")

        candidates = datasets["candidate_occurrences"]
        self.assertEqual(len(candidates), 1)
        self.assertEqual(candidates[0]["normalized_surface"], "thank")
        self.assertFalse(candidates[0]["candidate_spans_main_tiers"])

    def test_span_boundaries_are_exclusive_and_auditable(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            corpus = Path(temporary) / "chat"
            corpus.mkdir()
            (corpus / "TEST.cha").write_text(
                "@UTF8\n"
                "@PID:\tTEST\n"
                "@Participants:\tAAA Alice Adult, BBB Bob Adult, "
                "TESTPSUN Unknown Unidentified\n"
                "@Media:\tTEST, audio\n"
                "@New Episode\n"
                "*AAA:\tA . \x1510_20\x15\n"
                "*AAA:\tB . \x15199_210\x15\n"
                "*AAA:\tC . \x15390_400\x15\n"
                "*AAA:\tD .\n"
                "*AAA:\tE . \x15500_510\x15\n"
                "*BBB:\tF . \x15511_520\x15\n"
                "*CCC:\tG . \x15521_530\x15\n"
                "*CCC:\tH . \x15531_540\x15\n"
                "*TESTPSUN:\tI . \x15541_550\x15\n"
                "*TESTPSUN:\tJ . \x15551_560\x15\n"
                "@New Episode\n"
                "*TESTPSUN:\tK . \x15561_570\x15\n"
                "@End\n",
                encoding="utf-8",
            )
            datasets, _ = parse_corpus(corpus, {}, "test-commit")

        spans = datasets["analytic_spans"]
        self.assertEqual(len(spans), 10)
        self.assertEqual(spans[0]["normalized_text"], "a b")
        self.assertEqual(spans[0]["first_tier_index"], 1)
        self.assertEqual(spans[0]["last_tier_index"], 2)
        self.assertEqual(
            [row["boundary_reason_from_previous"] for row in spans],
            [
                "file_start",
                "gap_at_least_180",
                "timing_missing",
                "timing_missing",
                "speaker_change",
                "speaker_change",
                "speaker_unlisted",
                "speaker_change",
                "speaker_unknown",
                "episode_boundary",
            ],
        )
        self.assertEqual(
            {row["original_same_speaker_chain_id"] for row in spans[:4]},
            {spans[0]["original_same_speaker_chain_id"]},
        )
        self.assertNotIn("internal_gap_over_2500", spans[0])
        self.assertNotIn("internal_gap_over_12000", spans[0])

    def test_unknown_next_speaker_is_screened(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            corpus = Path(temporary) / "chat"
            corpus.mkdir()
            (corpus / "TEST.cha").write_text(
                "@UTF8\n"
                "@PID:\tTEST\n"
                "@Participants:\tAAA Alice Adult, TESTPSUN Unknown Unidentified\n"
                "@Media:\tTEST, audio\n"
                "@New Episode\n"
                "*AAA:\tOh . \x1510_20\x15\n"
                "*TESTPSUN:\tYeah . \x1521_30\x15\n"
                "@End\n",
                encoding="utf-8",
            )
            datasets, _ = parse_corpus(
                corpus,
                {"oh": alias("oh"), "yeah": alias("yeah")},
                "test-commit",
            )

        oh = datasets["candidate_occurrences"][0]
        self.assertTrue(oh["next_speaker_unknown"])
        self.assertIn("next_speaker_unknown", oh["auto_exclusion_code"])

    def test_occurrence_id_is_stable_when_an_earlier_alias_is_added(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            corpus = Path(temporary) / "chat"
            corpus.mkdir()
            (corpus / "TEST.cha").write_text(
                "@UTF8\n"
                "@PID:\tTEST\n"
                "@Participants:\tAAA Alice Adult, BBB Bob Adult\n"
                "@Media:\tTEST, audio\n"
                "@New Episode\n"
                "*AAA:\tFoo oh . \x1510_20\x15\n"
                "*BBB:\tYeah . \x1521_30\x15\n"
                "@End\n",
                encoding="utf-8",
            )
            first, _ = parse_corpus(
                corpus,
                {"oh": alias("oh")},
                "test-commit",
            )
            second, _ = parse_corpus(
                corpus,
                {"foo": alias("foo"), "oh": alias("oh")},
                "test-commit",
            )

        first_oh = first["candidate_occurrences"][0]
        second_oh = [
            row for row in second["candidate_occurrences"]
            if row["normalized_surface"] == "oh"
        ][0]
        self.assertEqual(first_oh["occurrence_id"], second_oh["occurrence_id"])

    def test_occurrence_anchor_survives_span_resegmentation(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            corpus = Path(temporary) / "chat"
            corpus.mkdir()
            transcript = corpus / "TEST.cha"
            prefix = (
                "@UTF8\n"
                "@PID:\tTEST\n"
                "@Participants:\tAAA Alice Adult, BBB Bob Adult\n"
                "@Media:\tTEST, audio\n"
                "@New Episode\n"
                "*AAA:\tPrelude . \x1510_20\x15\n"
            )
            suffix = (
                "*BBB:\tYeah . \x15400_410\x15\n"
                "@End\n"
            )
            transcript.write_text(
                prefix + "*AAA:\tOh . \x15199_210\x15\n" + suffix,
                encoding="utf-8",
            )
            joined, _ = parse_corpus(corpus, {"oh": alias("oh")}, "test-commit")
            transcript.write_text(
                prefix + "*AAA:\tOh . \x15200_210\x15\n" + suffix,
                encoding="utf-8",
            )
            split, _ = parse_corpus(corpus, {"oh": alias("oh")}, "test-commit")

        joined_oh = joined["candidate_occurrences"][0]
        split_oh = split["candidate_occurrences"][0]
        self.assertFalse(joined_oh["span_initial"])
        self.assertTrue(split_oh["span_initial"])
        self.assertNotEqual(joined_oh["span_id"], split_oh["span_id"])
        self.assertEqual(joined_oh["occurrence_id"], split_oh["occurrence_id"])
        self.assertEqual(
            joined_oh["original_same_speaker_chain_id"],
            split_oh["original_same_speaker_chain_id"],
        )

    def test_frozen_input_verification_rejects_dirty_checkout(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            repository = Path(temporary) / "CABNC"
            subtree = repository / "data" / "cabnc_talkbank_chat"
            subtree.mkdir(parents=True)
            transcript = subtree / "TEST.cha"
            transcript.write_text("@UTF8\n@End\n", encoding="utf-8")
            subprocess.run(["git", "init", str(repository)], check=True, capture_output=True)
            subprocess.run(
                ["git", "-C", str(repository), "config", "user.email", "test@example.test"],
                check=True,
            )
            subprocess.run(
                ["git", "-C", str(repository), "config", "user.name", "Test"],
                check=True,
            )
            subprocess.run(
                ["git", "-C", str(repository), "add", "."],
                check=True,
            )
            subprocess.run(
                ["git", "-C", str(repository), "commit", "-m", "fixture"],
                check=True,
                capture_output=True,
            )
            commit = subprocess.run(
                ["git", "-C", str(repository), "rev-parse", "HEAD"],
                check=True,
                capture_output=True,
                text=True,
            ).stdout.strip()
            tree = subprocess.run(
                [
                    "git",
                    "-C",
                    str(repository),
                    "rev-parse",
                    "HEAD:data/cabnc_talkbank_chat",
                ],
                check=True,
                capture_output=True,
                text=True,
            ).stdout.strip()

            verified = verify_frozen_input(subtree, commit, tree)
            self.assertEqual(verified["working_tree"], "clean")
            transcript.write_text("@UTF8\n@Comment:\tdirty\n@End\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                verify_frozen_input(subtree, commit, tree)


if __name__ == "__main__":
    unittest.main()
