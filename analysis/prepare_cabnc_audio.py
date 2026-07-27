#!/usr/bin/env python3
"""Prepare a permitted CABNC audio clip for local onset measurement.

The generated energy-based activity flags are measurement proposals only. They
cannot distinguish speech from laughter, breath, clicks, handling noise, or
overlapping speakers and therefore require listening plus expert audit.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import subprocess
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from scipy.io import wavfile  # noqa: E402


PREPARATION_VERSION = "0.1.0"
TARGET_SAMPLE_RATE = 16_000
FRAME_MS = 10
EVENT_ID_RE = re.compile(r"^[A-Za-z0-9._-]+$")
ACTIVITY_FIELDS = [
    "frame_index",
    "start_ms_relative",
    "end_ms_relative",
    "rms_dbfs",
    "estimated_noise_floor_dbfs",
    "activity_threshold_dbfs",
    "energy_activity_proposal",
]


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def run_checked(command: list[str]) -> str:
    completed = subprocess.run(
        command,
        check=True,
        capture_output=True,
        text=True,
    )
    return completed.stdout.strip()


def convert_clip(
    input_path: Path,
    output_path: Path,
    *,
    start_ms: int,
    end_ms: int,
) -> list[str]:
    if start_ms < 0 or end_ms <= start_ms:
        raise ValueError("clip bounds require 0 <= start_ms < end_ms")
    duration_ms = end_ms - start_ms
    command = [
        "ffmpeg",
        "-nostdin",
        "-hide_banner",
        "-loglevel",
        "error",
        "-ss",
        f"{start_ms / 1000:.3f}",
        "-i",
        str(input_path),
        "-t",
        f"{duration_ms / 1000:.3f}",
        "-map",
        "0:a:0",
        "-ac",
        "1",
        "-ar",
        str(TARGET_SAMPLE_RATE),
        "-c:a",
        "pcm_s16le",
        "-y",
        str(output_path),
    ]
    run_checked(command)
    return command


def read_fixed_wav(path: Path) -> tuple[int, np.ndarray]:
    sample_rate, samples = wavfile.read(path)
    if sample_rate != TARGET_SAMPLE_RATE:
        raise ValueError(
            f"prepared WAV sample rate is {sample_rate}, expected {TARGET_SAMPLE_RATE}"
        )
    if samples.dtype != np.int16:
        raise ValueError(f"prepared WAV dtype is {samples.dtype}, expected int16")
    if samples.ndim != 1:
        raise ValueError("prepared WAV must be mono")
    return sample_rate, samples.astype(np.float64) / np.iinfo(np.int16).max


def activity_rows(samples: np.ndarray, sample_rate: int) -> list[dict[str, str]]:
    frame_samples = sample_rate * FRAME_MS // 1000
    if frame_samples <= 0:
        raise ValueError("invalid frame size")
    if samples.size == 0:
        raise ValueError("prepared WAV contains no samples")

    rows: list[dict[str, str]] = []
    rms_values: list[float] = []
    for start in range(0, samples.size, frame_samples):
        frame = samples[start : start + frame_samples]
        rms = float(np.sqrt(np.mean(np.square(frame)))) if frame.size else 0.0
        rms_values.append(20.0 * np.log10(max(rms, 1e-6)))

    noise_floor = float(np.percentile(rms_values, 20))
    threshold = min(max(noise_floor + 10.0, -45.0), -25.0)
    for frame_index, rms_dbfs in enumerate(rms_values):
        start_ms = frame_index * FRAME_MS
        end_ms = min((frame_index + 1) * FRAME_MS, samples.size * 1000 / sample_rate)
        rows.append(
            {
                "frame_index": str(frame_index),
                "start_ms_relative": f"{start_ms:.3f}",
                "end_ms_relative": f"{end_ms:.3f}",
                "rms_dbfs": f"{rms_dbfs:.6f}",
                "estimated_noise_floor_dbfs": f"{noise_floor:.6f}",
                "activity_threshold_dbfs": f"{threshold:.6f}",
                "energy_activity_proposal": "yes" if rms_dbfs >= threshold else "no",
            }
        )
    return rows


def write_activity(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=ACTIVITY_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_waveform(path: Path, samples: np.ndarray, sample_rate: int) -> None:
    times = np.arange(samples.size) / sample_rate
    figure, axis = plt.subplots(figsize=(12, 3.2), constrained_layout=True)
    axis.plot(times, samples, color="#1f4e79", linewidth=0.55)
    axis.axhline(0, color="black", linewidth=0.35)
    axis.set(xlabel="Time from clip start (s)", ylabel="Amplitude", ylim=(-1, 1))
    figure.savefig(path, dpi=180)
    plt.close(figure)


def write_spectrogram(path: Path, samples: np.ndarray, sample_rate: int) -> None:
    figure, axis = plt.subplots(figsize=(12, 4.2), constrained_layout=True)
    axis.specgram(
        samples,
        NFFT=512,
        Fs=sample_rate,
        noverlap=384,
        cmap="magma",
        scale="dB",
    )
    axis.set(xlabel="Time from clip start (s)", ylabel="Frequency (Hz)")
    axis.set_ylim(0, min(8000, sample_rate / 2))
    figure.savefig(path, dpi=180)
    plt.close(figure)


def prepare_clip(
    input_path: Path,
    output_root: Path,
    *,
    event_id: str,
    start_ms: int,
    end_ms: int,
    generated_at: str,
) -> Path:
    if not EVENT_ID_RE.fullmatch(event_id):
        raise ValueError("event_id may contain only letters, digits, dot, underscore, and hyphen")
    if start_ms < 0 or end_ms <= start_ms:
        raise ValueError("clip bounds require 0 <= start_ms < end_ms")
    if not input_path.is_file():
        raise FileNotFoundError(input_path)
    event_dir = output_root / event_id
    event_dir.mkdir(parents=True, exist_ok=False)

    wav_path = event_dir / f"{event_id}.wav"
    waveform_path = event_dir / f"{event_id}-waveform.png"
    spectrogram_path = event_dir / f"{event_id}-spectrogram.png"
    activity_path = event_dir / f"{event_id}-activity-10ms.csv"
    provenance_path = event_dir / f"{event_id}-provenance.json"

    command = convert_clip(
        input_path,
        wav_path,
        start_ms=start_ms,
        end_ms=end_ms,
    )
    sample_rate, samples = read_fixed_wav(wav_path)
    rows = activity_rows(samples, sample_rate)
    write_activity(activity_path, rows)
    write_waveform(waveform_path, samples, sample_rate)
    write_spectrogram(spectrogram_path, samples, sample_rate)

    ffmpeg_version = run_checked(["ffmpeg", "-version"]).splitlines()[0]
    code_path = Path(__file__)
    provenance = {
        "preparation_version": PREPARATION_VERSION,
        "event_id": event_id,
        "generated_at": generated_at,
        "input_path": str(input_path.resolve()),
        "input_sha256": sha256_file(input_path),
        "clip_start_ms": start_ms,
        "clip_end_ms": end_ms,
        "wav_path": str(wav_path.resolve()),
        "wav_sha256": sha256_file(wav_path),
        "waveform_sha256": sha256_file(waveform_path),
        "spectrogram_sha256": sha256_file(spectrogram_path),
        "activity_sha256": sha256_file(activity_path),
        "preparation_code_sha256": sha256_file(code_path),
        "sample_rate_hz": sample_rate,
        "channels": 1,
        "sample_format": "signed 16-bit PCM",
        "activity_frame_ms": FRAME_MS,
        "activity_method": "adaptive frame RMS; proposal only; listening and audit required",
        "ffmpeg_version": ffmpeg_version,
        "ffmpeg_command": command,
    }
    provenance_path.write_text(
        json.dumps(provenance, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return event_dir


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output-root", required=True, type=Path)
    parser.add_argument("--event-id", required=True)
    parser.add_argument("--start-ms", required=True, type=int)
    parser.add_argument("--end-ms", required=True, type=int)
    parser.add_argument(
        "--generated-at",
        required=True,
        help="Frozen ISO 8601 timestamp for the provenance record",
    )
    args = parser.parse_args()
    event_dir = prepare_clip(
        args.input,
        args.output_root,
        event_id=args.event_id,
        start_ms=args.start_ms,
        end_ms=args.end_ms,
        generated_at=args.generated_at,
    )
    print(f"status=ok event_dir={event_dir} preparation_version={PREPARATION_VERSION}")


if __name__ == "__main__":
    main()
