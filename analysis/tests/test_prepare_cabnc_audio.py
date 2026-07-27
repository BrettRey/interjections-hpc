from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

import numpy as np
from scipy.io import wavfile


ANALYSIS_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ANALYSIS_DIR))

from prepare_cabnc_audio import (  # noqa: E402
    FRAME_MS,
    TARGET_SAMPLE_RATE,
    activity_rows,
    prepare_clip,
    read_fixed_wav,
)


class CabncAudioPreparationTests(unittest.TestCase):
    def test_activity_proposal_marks_tone_and_not_silence(self) -> None:
        samples = np.zeros(TARGET_SAMPLE_RATE, dtype=np.float64)
        start = TARGET_SAMPLE_RATE // 4
        end = TARGET_SAMPLE_RATE // 2
        time = np.arange(end - start) / TARGET_SAMPLE_RATE
        samples[start:end] = 0.2 * np.sin(2 * np.pi * 220 * time)
        rows = activity_rows(samples, TARGET_SAMPLE_RATE)
        self.assertEqual(len(rows), 1000 // FRAME_MS)
        self.assertTrue(
            all(row["energy_activity_proposal"] == "no" for row in rows[:20])
        )
        self.assertTrue(
            any(row["energy_activity_proposal"] == "yes" for row in rows[25:50])
        )

    def test_prepare_clip_writes_fixed_audio_images_activity_and_provenance(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            input_path = root / "source.wav"
            output_root = root / "prepared"
            sample_rate = 8_000
            time = np.arange(sample_rate) / sample_rate
            samples = np.asarray(0.1 * np.sin(2 * np.pi * 180 * time) * 32767, dtype=np.int16)
            wavfile.write(input_path, sample_rate, samples)

            event_dir = prepare_clip(
                input_path,
                output_root,
                event_id="evt-001",
                start_ms=100,
                end_ms=800,
                generated_at="2026-07-27T00:00:00Z",
            )
            expected = {
                "evt-001.wav",
                "evt-001-waveform.png",
                "evt-001-spectrogram.png",
                "evt-001-activity-10ms.csv",
                "evt-001-provenance.json",
            }
            self.assertEqual({path.name for path in event_dir.iterdir()}, expected)
            prepared_rate, prepared = read_fixed_wav(event_dir / "evt-001.wav")
            self.assertEqual(prepared_rate, TARGET_SAMPLE_RATE)
            self.assertAlmostEqual(prepared.size / prepared_rate, 0.7, places=2)

            provenance = json.loads(
                (event_dir / "evt-001-provenance.json").read_text(encoding="utf-8")
            )
            self.assertEqual(provenance["event_id"], "evt-001")
            self.assertEqual(provenance["clip_start_ms"], 100)
            self.assertEqual(provenance["clip_end_ms"], 800)
            self.assertEqual(provenance["activity_frame_ms"], FRAME_MS)
            self.assertEqual(len(provenance["wav_sha256"]), 64)
            self.assertIn("proposal only", provenance["activity_method"])

            with self.assertRaises(FileExistsError):
                prepare_clip(
                    input_path,
                    output_root,
                    event_id="evt-001",
                    start_ms=100,
                    end_ms=800,
                    generated_at="2026-07-27T00:00:00Z",
                )

    def test_invalid_bounds_and_event_id_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            input_path = root / "source.wav"
            wavfile.write(input_path, TARGET_SAMPLE_RATE, np.zeros(100, dtype=np.int16))
            with self.assertRaises(ValueError):
                prepare_clip(
                    input_path,
                    root / "out-a",
                    event_id="../escape",
                    start_ms=0,
                    end_ms=10,
                    generated_at="2026-07-27T00:00:00Z",
                )
            with self.assertRaises(ValueError):
                prepare_clip(
                    input_path,
                    root / "out-b",
                    event_id="evt-002",
                    start_ms=20,
                    end_ms=10,
                    generated_at="2026-07-27T00:00:00Z",
                )


if __name__ == "__main__":
    unittest.main()
