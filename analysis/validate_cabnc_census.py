#!/usr/bin/env python3
"""Validate CABNC census smoke counts, IDs, and output hashes."""

from __future__ import annotations

import argparse
from collections import defaultdict
import csv
import hashlib
import json
from pathlib import Path
import subprocess


EXPECTED_COMMIT = "0a28a11e168e312d1b9ad406a3352f31c13b86a2"
EXPECTED_SUBTREE = "7f7f87611350439e404baa8f8c659f33e81efecb"
SUBTREE_PATH = "data/cabnc_talkbank_chat"
EXPECTED_PARSER_VERSION = "0.5.0"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def assert_unique(path: Path, field: str) -> int:
    seen = set()
    duplicates = []
    with path.open(encoding="utf-8", newline="") as handle:
        for line_number, row in enumerate(csv.DictReader(handle), start=2):
            value = row[field]
            if value in seen:
                duplicates.append((line_number, value))
            seen.add(value)
    if duplicates:
        preview = ", ".join(f"line {line}: {value}" for line, value in duplicates[:5])
        raise SystemExit(f"Duplicate {field} values in {path.name}: {preview}")
    return len(seen)


def git_output(arguments: list[str], workdir: Path) -> str:
    result = subprocess.run(
        ["git", "-C", str(workdir), *arguments],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def verify_source(source: Path, manifest: dict) -> None:
    repository_root = Path(
        git_output(["rev-parse", "--show-toplevel"], source)
    ).resolve()
    if source.resolve() != (repository_root / SUBTREE_PATH).resolve():
        raise SystemExit("Validation source is not the pinned CABNC subtree")
    observed_commit = git_output(["rev-parse", "HEAD"], repository_root)
    observed_subtree = git_output(
        ["rev-parse", f"HEAD:{SUBTREE_PATH}"],
        repository_root,
    )
    dirty = git_output(
        ["status", "--porcelain", "--untracked-files=all"],
        repository_root,
    )
    if observed_commit != EXPECTED_COMMIT or observed_commit != manifest["commit_sha"]:
        raise SystemExit(f"Source commit mismatch: {observed_commit}")
    if observed_subtree != EXPECTED_SUBTREE or observed_subtree != manifest["subtree_git_sha"]:
        raise SystemExit(f"Source subtree mismatch: {observed_subtree}")
    if dirty:
        raise SystemExit("Source checkout is dirty")


def verify_source_files(source: Path, census_dir: Path, smoke: dict) -> None:
    seen_paths = set()
    transcript_bytes = 0
    recording_urls: dict[str, set[str]] = defaultdict(set)
    manifest_path = census_dir / "file_manifest.csv"
    with manifest_path.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            relative_path = row["relative_path"]
            if relative_path in seen_paths:
                raise SystemExit(f"Duplicate source path in file manifest: {relative_path}")
            seen_paths.add(relative_path)
            source_path = source / relative_path
            if not source_path.is_file():
                raise SystemExit(f"Missing source transcript: {relative_path}")
            observed_bytes = source_path.stat().st_size
            if observed_bytes != int(row["bytes"]):
                raise SystemExit(f"Source byte-count mismatch: {relative_path}")
            if sha256_file(source_path) != row["file_sha256"]:
                raise SystemExit(f"Source hash mismatch: {relative_path}")
            if row["recording_id"]:
                recording_urls[row["recording_id"]].add(row["original_audio_url"])
            if row["tape_side_id"] != row["recording_id"]:
                raise SystemExit(f"Tape-side/legacy recording mismatch: {relative_path}")
            if row["collection_block_id"] != row["segment_id"][:3].upper():
                raise SystemExit(f"Collection-block mismatch: {relative_path}")
            if row["tape_id"] and not row["tape_side_id"].startswith(row["tape_id"]):
                raise SystemExit(f"Tape/tape-side mismatch: {relative_path}")
            transcript_bytes += observed_bytes
    disk_paths = {
        path.relative_to(source).as_posix()
        for path in source.rglob("*.cha")
    }
    if seen_paths != disk_paths:
        raise SystemExit("Source file manifest does not match the frozen subtree")
    if len(seen_paths) != smoke["n_files"]:
        raise SystemExit("Source file count does not match smoke counts")
    if transcript_bytes != smoke["n_transcript_bytes"]:
        raise SystemExit("Source byte total does not match smoke counts")
    collisions = [key for key, urls in recording_urls.items() if len(urls) > 1]
    if collisions:
        raise SystemExit(f"Recording ID collision: {collisions[0]}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--forms", type=Path, required=True)
    parser.add_argument("--expected-files", type=int, default=1860)
    parser.add_argument("--expected-main-tiers", type=int, default=246783)
    parser.add_argument("--expected-transcript-bytes", type=int, default=16597291)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    manifest_path = args.input / "run_manifest.json"
    hashes_path = args.input / "output_sha256.json"
    if not manifest_path.exists() or not hashes_path.exists():
        raise SystemExit("Missing run_manifest.json or output_sha256.json")

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    expected_hashes = json.loads(hashes_path.read_text(encoding="utf-8"))
    if manifest["parser_version"] != EXPECTED_PARSER_VERSION:
        raise SystemExit(f"Unexpected parser version: {manifest['parser_version']}")
    if manifest["output_hashes"] != expected_hashes:
        raise SystemExit("run_manifest.json and output_sha256.json disagree")
    if sha256_file(args.forms) != manifest["candidate_lexicon_sha256"]:
        raise SystemExit("Alias-table hash does not match run manifest")
    verify_source(args.source, manifest)
    smoke = manifest["smoke_counts"]
    if smoke["n_files"] != args.expected_files:
        raise SystemExit(f"Expected {args.expected_files} files; found {smoke['n_files']}")
    if smoke["n_physical_main_tier_lines"] != args.expected_main_tiers:
        raise SystemExit(
            f"Expected {args.expected_main_tiers} main-tier lines; "
            f"found {smoke['n_physical_main_tier_lines']}"
        )
    if smoke["n_transcript_bytes"] != args.expected_transcript_bytes:
        raise SystemExit(
            f"Expected {args.expected_transcript_bytes} transcript bytes; "
            f"found {smoke['n_transcript_bytes']}"
        )

    for filename, expected in expected_hashes.items():
        observed = sha256_file(args.input / filename)
        if observed != expected:
            raise SystemExit(f"Hash mismatch for {filename}: {observed} != {expected}")

    verify_source_files(args.source, args.input, smoke)

    n_turns = assert_unique(args.input / "turns.csv", "turn_id")
    n_occurrences = assert_unique(
        args.input / "candidate_occurrences.csv",
        "occurrence_id",
    )
    if n_turns != smoke["n_collapsed_turns"]:
        raise SystemExit(f"Turn count mismatch: {n_turns} != {smoke['n_collapsed_turns']}")
    if n_occurrences != smoke["n_candidate_occurrences"]:
        raise SystemExit(
            f"Candidate count mismatch: {n_occurrences} != {smoke['n_candidate_occurrences']}"
        )

    raw_segment_gate = 0
    raw_collection_gate = 0
    screened_recording_gate = 0
    screened_collection_gate = 0
    with (args.input / "census_by_form.csv").open(
        encoding="utf-8",
        newline="",
    ) as handle:
        for row in csv.DictReader(handle):
            if (
                int(row["n_turn_initial"]) >= 25
                and int(row["n_initial_segments"]) >= 10
                and int(row["n_initial_speakers"]) >= 10
            ):
                raw_segment_gate += 1
            if (
                int(row["n_turn_initial"]) >= 25
                and int(row["n_initial_collection_blocks"]) >= 10
                and int(row["n_initial_speakers"]) >= 10
            ):
                raw_collection_gate += 1
            if (
                int(row["n_initial_screened_proxy"]) >= 25
                and int(row["n_initial_screened_proxy_recordings"]) >= 10
                and int(row["n_initial_screened_proxy_speakers"]) >= 10
            ):
                screened_recording_gate += 1
            if (
                int(row["n_initial_screened_proxy"]) >= 25
                and int(row["n_initial_screened_proxy_collection_blocks"]) >= 10
                and int(row["n_initial_screened_proxy_speakers"]) >= 10
            ):
                screened_collection_gate += 1

    print(json.dumps({
        "status": "ok",
        "parser_version": manifest["parser_version"],
        "n_files": smoke["n_files"],
        "n_physical_main_tier_lines": smoke["n_physical_main_tier_lines"],
        "n_collapsed_turns": n_turns,
        "n_candidate_occurrences": n_occurrences,
        "raw_segment_family_gate": raw_segment_gate,
        "raw_collection_family_gate": raw_collection_gate,
        "screened_recording_family_gate": screened_recording_gate,
        "screened_collection_family_gate": screened_collection_gate,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
