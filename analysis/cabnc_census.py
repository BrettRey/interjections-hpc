#!/usr/bin/env python3
"""Build a deterministic transcript-only census from frozen CABNC CHAT files."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import platform
import re
import subprocess
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable
from urllib.parse import urlsplit
import unicodedata

PARSER_VERSION = "0.5.0"
DEFAULT_COMMIT = "0a28a11e168e312d1b9ad406a3352f31c13b86a2"
DEFAULT_SUBTREE_OBJECT = "7f7f87611350439e404baa8f8c659f33e81efecb"
REPOSITORY_URL = "https://github.com/saulalbert/CABNC.git"
SUBTREE_PATH = "data/cabnc_talkbank_chat"

TIMING_RE = re.compile(r"\x15(\d+)_(\d+)\x15|•(\d+)_(\d+)•")
EVENT_RE = re.compile(r"&=[^\s]+|\[(?:[^\]]*)\]|\((?:[^)]*)\)")
TOKEN_RE = re.compile(r"[^\W\d_]+(?:['’\-][^\W\d_]+)*", re.UNICODE)
SKIP_LEXICAL = {"xxx", "yyy", "www"}
UNKNOWN_SPEAKER_RE = re.compile(r"PSU[NG]$")
TAPE_ID_RE = re.compile(r"021A-C0897X[0-9]{4}XX", re.IGNORECASE)
TURN_MERGE_MAX_GAP_MS = 2500


@dataclass
class LogicalTier:
    kind: str
    label: str
    text: str
    line_number: int
    episode_index: int = 0


@dataclass
class MainTier:
    tier_index: int
    speaker_id: str
    raw_text: str
    episode_index: int
    line_number: int
    timing_spans: list[tuple[int, int]] = field(default_factory=list)
    original_same_speaker_chain_index: int = 0

    @property
    def start_ms(self) -> int | None:
        return min((start for start, _ in self.timing_spans), default=None)

    @property
    def end_ms(self) -> int | None:
        return max((end for _, end in self.timing_spans), default=None)


@dataclass
class Turn:
    turn_index: int
    episode_index: int
    speaker_id: str
    tiers: list[MainTier]
    boundary_reason_from_previous: str

    @property
    def start_ms(self) -> int | None:
        starts = [tier.start_ms for tier in self.tiers if tier.start_ms is not None]
        return min(starts) if starts else None

    @property
    def end_ms(self) -> int | None:
        ends = [tier.end_ms for tier in self.tiers if tier.end_ms is not None]
        return max(ends) if ends else None

    @property
    def raw_text(self) -> str:
        return " ".join(tier.raw_text for tier in self.tiers)

    @property
    def boundary_start_ms(self) -> int | None:
        return self.tiers[0].start_ms

    @property
    def boundary_end_ms(self) -> int | None:
        return self.tiers[-1].end_ms

    @property
    def timing_status(self) -> str:
        complete = [tier.start_ms is not None and tier.end_ms is not None for tier in self.tiers]
        if all(complete):
            return "fully_timed"
        if any(tier.start_ms is not None or tier.end_ms is not None for tier in self.tiers):
            return "partially_timed"
        return "untimed"

    @property
    def internal_positive_gaps_ms(self) -> list[int]:
        gaps = []
        for current, following in zip(self.tiers, self.tiers[1:]):
            if current.end_ms is None or following.start_ms is None:
                continue
            gap = following.start_ms - current.end_ms
            if gap > 0:
                gaps.append(gap)
        return gaps


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def normalize_surface(value: str) -> str:
    return unicodedata.normalize("NFC", value).casefold().strip()


def is_unknown_speaker_id(value: str) -> bool:
    return bool(UNKNOWN_SPEAKER_RE.search(value))


def timing_spans(text: str) -> list[tuple[int, int]]:
    spans = []
    for match in TIMING_RE.finditer(text):
        values = match.groups()
        start = int(values[0] or values[2])
        end = int(values[1] or values[3])
        spans.append((start, end))
    return spans


def clean_for_tokens(text: str) -> str:
    cleaned = TIMING_RE.sub(" ", text)
    cleaned = EVENT_RE.sub(" ", cleaned)
    cleaned = cleaned.replace("<", " ").replace(">", " ")
    cleaned = re.sub(r"&[-+]\S+", " ", cleaned)
    cleaned = re.sub(r"(?<!\w)0(?!\w)", " ", cleaned)
    return re.sub(r"\s+", " ", cleaned).strip()


def lexical_tokens(text: str) -> list[str]:
    tokens = []
    for match in TOKEN_RE.finditer(clean_for_tokens(text)):
        token = match.group(0)
        if normalize_surface(token) in SKIP_LEXICAL:
            continue
        tokens.append(token)
    return tokens


def split_tier_start(line: str) -> tuple[str, str, str] | None:
    if not line or line[0] not in "@*%":
        return None
    kind = line[0]
    body = line[1:]
    if ":" in body:
        label, text = body.split(":", 1)
        return kind, label.strip(), text.lstrip("\t ")
    return kind, body.strip(), ""


def build_logical_tiers(lines: list[str]) -> tuple[list[LogicalTier], list[dict], int]:
    tiers: list[LogicalTier] = []
    warnings: list[dict] = []
    current: LogicalTier | None = None
    physical_main_tiers = 0

    def flush() -> None:
        nonlocal current
        if current is not None:
            tiers.append(current)
            current = None

    for line_number, raw_line in enumerate(lines, start=1):
        line = raw_line.rstrip("\r\n")
        if line.startswith("*"):
            physical_main_tiers += 1
        start = split_tier_start(line)
        if start is not None:
            flush()
            current = LogicalTier(*start, line_number=line_number)
            continue
        if not line.strip():
            continue
        if line[:1].isspace() and current is not None:
            current.text = f"{current.text} {line.strip()}".strip()
            continue
        warnings.append({
            "line_number": line_number,
            "warning_code": "orphan_physical_line",
            "detail": line[:160],
        })
    flush()

    episode_index = 0
    for tier in tiers:
        if tier.kind == "@" and tier.label.casefold() == "new episode":
            episode_index += 1
        tier.episode_index = episode_index
    return tiers, warnings, physical_main_tiers


def collect_headers(tiers: Iterable[LogicalTier]) -> dict[str, list[str]]:
    headers: dict[str, list[str]] = defaultdict(list)
    for tier in tiers:
        if tier.kind == "@":
            headers[tier.label.casefold()].append(tier.text)
    return dict(headers)


def participant_codes(headers: dict[str, list[str]]) -> list[str]:
    codes: set[str] = set()
    for value in headers.get("participants", []):
        for entry in value.split(","):
            fields = entry.strip().split()
            if fields:
                codes.add(fields[0])
    for value in headers.get("id", []):
        fields = value.split("|")
        if len(fields) > 2 and fields[2]:
            codes.add(fields[2])
    return sorted(codes)


def header_first(headers: dict[str, list[str]], key: str) -> str:
    values = headers.get(key.casefold(), [])
    return values[0].strip() if values else ""


def original_audio_url(headers: dict[str, list[str]]) -> str:
    for comment in headers.get("comment", []):
        match = re.search(r"https?://\S+", comment)
        if match:
            return match.group(0)
    return ""


def recording_id_from_url(url: str) -> str:
    if not url:
        return ""
    return Path(urlsplit(url).path).stem


def tape_id_from_url(url: str) -> str:
    if not url:
        return ""
    match = TAPE_ID_RE.search(urlsplit(url).path)
    return match.group(0).upper() if match else ""


def collection_block_id_from_segment(segment_id: str) -> str:
    return segment_id[:3].upper() if len(segment_id) >= 3 else ""


def git_output(arguments: list[str], workdir: Path) -> str:
    result = subprocess.run(
        ["git", "-C", str(workdir), *arguments],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def verify_frozen_input(
    input_dir: Path,
    commit_sha: str,
    subtree_object: str,
) -> dict[str, str]:
    try:
        repository_root = Path(
            git_output(["rev-parse", "--show-toplevel"], input_dir)
        ).resolve()
    except (subprocess.CalledProcessError, FileNotFoundError) as error:
        raise ValueError("CABNC input must be inside the frozen Git checkout") from error

    expected_input = (repository_root / SUBTREE_PATH).resolve()
    if input_dir.resolve() != expected_input:
        raise ValueError(f"Expected CABNC subtree {expected_input}; received {input_dir.resolve()}")

    observed_commit = git_output(["rev-parse", "HEAD"], repository_root)
    observed_subtree = git_output(
        ["rev-parse", f"HEAD:{SUBTREE_PATH}"],
        repository_root,
    )
    dirty_status = git_output(
        ["status", "--porcelain", "--untracked-files=all"],
        repository_root,
    )
    if observed_commit != commit_sha:
        raise ValueError(f"CABNC commit mismatch: {observed_commit} != {commit_sha}")
    if observed_subtree != subtree_object:
        raise ValueError(
            f"CABNC subtree mismatch: {observed_subtree} != {subtree_object}"
        )
    if dirty_status:
        raise ValueError("CABNC checkout is dirty; refusing to assign frozen provenance")
    return {
        "repository_root": str(repository_root),
        "observed_commit": observed_commit,
        "observed_subtree": observed_subtree,
        "working_tree": "clean",
    }


def build_main_tiers(tiers: Iterable[LogicalTier], warnings: list[dict]) -> list[MainTier]:
    main_tiers = []
    for logical in tiers:
        if logical.kind != "*":
            continue
        spans = timing_spans(logical.text)
        for start, end in spans:
            if end < start:
                warnings.append({
                    "line_number": logical.line_number,
                    "warning_code": "negative_timing_span",
                    "detail": f"{start}_{end}",
                })
        main_tiers.append(MainTier(
            tier_index=len(main_tiers) + 1,
            speaker_id=logical.label,
            raw_text=logical.text,
            episode_index=logical.episode_index,
            line_number=logical.line_number,
            timing_spans=spans,
        ))
    return main_tiers


def collapse_turns(
    main_tiers: list[MainTier],
    listed_speakers: set[str],
) -> list[Turn]:
    turns: list[Turn] = []
    original_chain_index = 0
    previous_tier: MainTier | None = None
    for tier in main_tiers:
        same_original_chain = bool(
            previous_tier
            and previous_tier.speaker_id == tier.speaker_id
            and previous_tier.episode_index == tier.episode_index
        )
        if not same_original_chain:
            original_chain_index += 1
        tier.original_same_speaker_chain_index = original_chain_index

        boundary_reason = "file_start"
        if previous_tier is not None:
            if previous_tier.episode_index != tier.episode_index:
                boundary_reason = "episode_boundary"
            elif previous_tier.speaker_id != tier.speaker_id:
                boundary_reason = "speaker_change"
            elif (
                tier.speaker_id not in listed_speakers
                or is_unknown_speaker_id(tier.speaker_id)
            ):
                boundary_reason = "unknown_identity"
            elif previous_tier.end_ms is None or tier.start_ms is None:
                boundary_reason = "timing_missing"
            elif tier.start_ms - previous_tier.end_ms > TURN_MERGE_MAX_GAP_MS:
                boundary_reason = "gap_over_2500"
            else:
                boundary_reason = ""

        if turns and not boundary_reason:
            turns[-1].tiers.append(tier)
        else:
            turns.append(Turn(
                turn_index=len(turns) + 1,
                episode_index=tier.episode_index,
                speaker_id=tier.speaker_id,
                tiers=[tier],
                boundary_reason_from_previous=boundary_reason,
            ))
        previous_tier = tier
    return turns


def stable_id(*parts: object) -> str:
    payload = "\x1f".join(str(part) for part in parts)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:20]


def load_aliases(path: Path) -> tuple[dict[str, dict], str]:
    aliases: dict[str, dict] = {}
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        required = {"form_family_id", "normalized_surface", "alias_rule_id", "seed_group"}
        if not required.issubset(reader.fieldnames or []):
            missing = sorted(required - set(reader.fieldnames or []))
            raise ValueError(f"Alias table missing fields: {missing}")
        for row in reader:
            surface = normalize_surface(row["normalized_surface"])
            if not surface:
                raise ValueError("Alias table contains an empty surface")
            if surface in aliases:
                raise ValueError(f"Duplicate normalized surface: {surface}")
            row = dict(row)
            row["normalized_surface"] = surface
            row["variant_block_hint"] = row.get("variant_block_hint") or ""
            row["component_family_ids"] = row.get("component_family_ids") or ""
            aliases[surface] = row
    return aliases, sha256_file(path)


def turn_token_records(turn: Turn) -> tuple[list[dict], set[int]]:
    records: list[dict] = []
    tier_initial_indices: set[int] = set()
    for tier in turn.tiers:
        tier_tokens = lexical_tokens(tier.raw_text)
        if tier_tokens:
            tier_initial_indices.add(len(records))
        for tier_token_index, raw_surface in enumerate(tier_tokens):
            records.append({
                "raw_surface": raw_surface,
                "normalized_surface": normalize_surface(raw_surface),
                "tier_index": tier.tier_index,
                "tier_token_index": tier_token_index,
            })
    return records, tier_initial_indices


def csv_value(value: object) -> object:
    if value is None:
        return ""
    if isinstance(value, (list, dict, tuple)):
        return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    if isinstance(value, bool):
        return "1" if value else "0"
    return value


def write_csv(path: Path, rows: list[dict], fieldnames: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({key: csv_value(row.get(key, "")) for key in fieldnames})


def parse_corpus(
    input_dir: Path,
    aliases: dict[str, dict],
    commit_sha: str,
) -> tuple[dict[str, list[dict]], dict[str, int]]:
    file_rows: list[dict] = []
    turn_rows: list[dict] = []
    candidate_rows: list[dict] = []
    warning_rows: list[dict] = []
    vocabulary_counts: Counter[str] = Counter()
    vocabulary_segments: dict[str, set[str]] = defaultdict(set)
    vocabulary_speakers: dict[str, set[str]] = defaultdict(set)
    physical_main_total = 0
    max_alias_tokens = max((len(surface.split()) for surface in aliases), default=1)

    paths = sorted(input_dir.rglob("*.cha"), key=lambda item: item.relative_to(input_dir).as_posix())
    for path in paths:
        relative_path = path.relative_to(input_dir).as_posix()
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines(keepends=True)
        tiers, warnings, physical_main = build_logical_tiers(lines)
        physical_main_total += physical_main
        headers = collect_headers(tiers)
        segment_id = header_first(headers, "pid") or path.stem
        collection_block_id = collection_block_id_from_segment(segment_id)
        media_header = header_first(headers, "media")
        media_id = media_header.split(",", 1)[0].strip() if media_header else ""
        audio_url = original_audio_url(headers)
        recording_id = recording_id_from_url(audio_url)
        tape_side_id = recording_id
        tape_id = tape_id_from_url(audio_url)
        media_missing = "0missing" in path.parts or "missing" in media_header.casefold()
        participants = participant_codes(headers)
        mains = build_main_tiers(tiers, warnings)
        turns = collapse_turns(mains, set(participants))
        episode_values = sorted({turn.episode_index for turn in turns})
        timed_tiers = sum(1 for tier in mains if tier.timing_spans)
        first_times = [tier.start_ms for tier in mains if tier.start_ms is not None]
        last_times = [tier.end_ms for tier in mains if tier.end_ms is not None]

        for warning in warnings:
            warning_rows.append({"relative_path": relative_path, **warning})

        file_rows.append({
            "segment_id": segment_id,
            "relative_path": relative_path,
            "file_sha256": sha256_file(path),
            "bytes": path.stat().st_size,
            "pid": header_first(headers, "pid"),
            "media_id": media_id,
            "recording_id": recording_id,
            "tape_side_id": tape_side_id,
            "tape_id": tape_id,
            "collection_block_id": collection_block_id,
            "media_missing": media_missing,
            "original_audio_url": audio_url,
            "date": header_first(headers, "date"),
            "location": header_first(headers, "location"),
            "situation": header_first(headers, "situation"),
            "participant_codes": participants,
            "n_episodes_with_speech": len(episode_values),
            "n_main_tiers": len(mains),
            "n_physical_main_tier_lines": physical_main,
            "n_timed_tiers": timed_tiers,
            "first_ms": min(first_times) if first_times else None,
            "last_ms": max(last_times) if last_times else None,
            "parse_warning_count": len(warnings),
        })

        turn_ids = [
            stable_id(commit_sha, relative_path, turn.episode_index, turn.turn_index)
            for turn in turns
        ]
        for position, turn in enumerate(turns):
            previous_turn = turns[position - 1] if position else None
            next_turn = turns[position + 1] if position + 1 < len(turns) else None
            previous_id = turn_ids[position - 1] if position else ""
            next_id = turn_ids[position + 1] if position + 1 < len(turns) else ""
            same_episode_next = bool(next_turn and next_turn.episode_index == turn.episode_index)
            gap_ms = None
            overlap_ms = None
            if (
                same_episode_next
                and turn.boundary_end_ms is not None
                and next_turn.boundary_start_ms is not None
            ):
                difference = next_turn.boundary_start_ms - turn.boundary_end_ms
                if difference >= 0:
                    gap_ms = difference
                else:
                    overlap_ms = -difference

            tokens, tier_initial_indices = turn_token_records(turn)
            tiers_by_index = {tier.tier_index: tier for tier in turn.tiers}
            normalized_text = " ".join(record["normalized_surface"] for record in tokens)
            if tokens:
                first_surface = tokens[0]["normalized_surface"]
                vocabulary_counts[first_surface] += 1
                vocabulary_segments[first_surface].add(segment_id)
                vocabulary_speakers[first_surface].add(turn.speaker_id)

            turn_id = turn_ids[position]
            original_same_speaker_chain_id = stable_id(
                commit_sha,
                relative_path,
                turn.episode_index,
                "same_speaker_chain",
                turn.tiers[0].original_same_speaker_chain_index,
            )
            turn_rows.append({
                "turn_id": turn_id,
                "segment_id": segment_id,
                "relative_path": relative_path,
                "episode_index": turn.episode_index,
                "turn_index": turn.turn_index,
                "speaker_id": turn.speaker_id,
                "recording_id": recording_id,
                "tape_side_id": tape_side_id,
                "tape_id": tape_id,
                "collection_block_id": collection_block_id,
                "original_same_speaker_chain_id": original_same_speaker_chain_id,
                "boundary_reason_from_previous": turn.boundary_reason_from_previous,
                "first_tier_index": turn.tiers[0].tier_index,
                "last_tier_index": turn.tiers[-1].tier_index,
                "start_ms": turn.start_ms,
                "end_ms": turn.end_ms,
                "boundary_start_ms": turn.boundary_start_ms,
                "boundary_end_ms": turn.boundary_end_ms,
                "raw_text": turn.raw_text,
                "normalized_text": normalized_text,
                "previous_turn_id": previous_id,
                "previous_speaker": previous_turn.speaker_id if previous_turn else "",
                "next_turn_id": next_id if same_episode_next else "",
                "next_speaker": next_turn.speaker_id if same_episode_next else "",
                "gap_to_next_ms": gap_ms,
                "next_overlap_ms": overlap_ms,
                "speaker_listed": turn.speaker_id in participants,
                "speaker_unknown": is_unknown_speaker_id(turn.speaker_id),
                "timing_status": turn.timing_status,
                "timing_complete": turn.timing_status == "fully_timed",
                "max_internal_positive_gap_ms": max(
                    turn.internal_positive_gaps_ms,
                    default=None,
                ),
                "internal_gap_over_2500": any(
                    gap > 2500 for gap in turn.internal_positive_gaps_ms
                ),
                "internal_gap_over_12000": any(
                    gap > 12000 for gap in turn.internal_positive_gaps_ms
                ),
            })

            token_index = 0
            while token_index < len(tokens):
                alias = None
                matched_surface = ""
                token_end_index = token_index
                max_length = min(max_alias_tokens, len(tokens) - token_index)
                for length in range(max_length, 0, -1):
                    candidate_tokens = tokens[token_index:token_index + length]
                    if len({item["tier_index"] for item in candidate_tokens}) > 1:
                        continue
                    surface = " ".join(
                        item["normalized_surface"]
                        for item in candidate_tokens
                    )
                    if surface in aliases:
                        alias = aliases[surface]
                        matched_surface = surface
                        token_end_index = token_index + length - 1
                        break
                if alias is None:
                    token_index += 1
                    continue
                auto_exclusions = []
                if media_missing:
                    auto_exclusions.append("media_missing")
                if not turn.speaker_id:
                    auto_exclusions.append("source_speaker_unidentified")
                elif turn.speaker_id not in participants:
                    auto_exclusions.append("source_speaker_unlisted")
                elif is_unknown_speaker_id(turn.speaker_id):
                    auto_exclusions.append("source_speaker_unknown")
                if not same_episode_next:
                    auto_exclusions.append("no_following_sequence")
                elif next_turn.speaker_id not in participants:
                    auto_exclusions.append("next_speaker_unlisted")
                elif is_unknown_speaker_id(next_turn.speaker_id):
                    auto_exclusions.append("next_speaker_unknown")
                occurrence_id = stable_id(
                    commit_sha,
                    relative_path,
                    turn.episode_index,
                    turn.turn_index,
                    token_index,
                    token_end_index,
                    matched_surface,
                )
                candidate_start_tier = tiers_by_index[tokens[token_index]["tier_index"]]
                candidate_end_tier = tiers_by_index[
                    tokens[token_end_index]["tier_index"]
                ]
                candidate_rows.append({
                    "occurrence_id": occurrence_id,
                    "turn_id": turn_id,
                    "relative_path": relative_path,
                    "segment_id": segment_id,
                    "media_id": media_id,
                    "recording_id": recording_id,
                    "tape_side_id": tape_side_id,
                    "tape_id": tape_id,
                    "collection_block_id": collection_block_id,
                    "original_same_speaker_chain_id": original_same_speaker_chain_id,
                    "episode_index": turn.episode_index,
                    "speaker_id": turn.speaker_id,
                    "token_index": token_index,
                    "token_end_index": token_end_index,
                    "tier_index": tokens[token_index]["tier_index"],
                    "tier_token_index": tokens[token_index]["tier_token_index"],
                    "candidate_end_tier_index": tokens[token_end_index]["tier_index"],
                    "candidate_spans_main_tiers": (
                        tokens[token_index]["tier_index"] != tokens[token_end_index]["tier_index"]
                    ),
                    "candidate_tier_start_ms": candidate_start_tier.start_ms,
                    "candidate_tier_end_ms": candidate_end_tier.end_ms,
                    "raw_surface": " ".join(
                        item["raw_surface"]
                        for item in tokens[token_index:token_end_index + 1]
                    ),
                    "normalized_surface": matched_surface,
                    "form_family_id": alias["form_family_id"],
                    "alias_rule_id": alias["alias_rule_id"],
                    "seed_group": alias["seed_group"],
                    "variant_block_hint": alias["variant_block_hint"],
                    "component_family_ids": alias["component_family_ids"],
                    "turn_initial": token_index == 0,
                    "main_tier_initial": token_index in tier_initial_indices,
                    "candidate_final": token_end_index == len(tokens) - 1,
                    "candidate_only_turn": token_index == 0 and token_end_index == len(tokens) - 1,
                    "source_turn_start_ms": turn.start_ms,
                    "source_turn_end_ms": turn.end_ms,
                    "source_speaker_listed": turn.speaker_id in participants,
                    "source_speaker_unknown": is_unknown_speaker_id(turn.speaker_id),
                    "next_turn_id": next_id if same_episode_next else "",
                    "next_speaker_id": next_turn.speaker_id if same_episode_next else "",
                    "next_speaker_listed": (
                        next_turn.speaker_id in participants if same_episode_next else False
                    ),
                    "next_speaker_unknown": (
                        is_unknown_speaker_id(next_turn.speaker_id)
                        if same_episode_next else False
                    ),
                    "next_turn_start_ms": (
                        next_turn.boundary_start_ms if same_episode_next else None
                    ),
                    "gap_ms": gap_ms,
                    "overlap_ms": overlap_ms,
                    "auto_exclusion_code": ";".join(auto_exclusions),
                    "manual_status": "unreviewed",
                    "sign_type_id": "",
                })
                token_index = token_end_index + 1

    vocab_rows = [
        {
            "normalized_surface": surface,
            "n_turn_initial": count,
            "n_segments": len(vocabulary_segments[surface]),
            "n_speakers": len(vocabulary_speakers[surface]),
            "in_seed_alias_table": surface in aliases,
            "form_family_id": aliases.get(surface, {}).get("form_family_id", ""),
        }
        for surface, count in vocabulary_counts.items()
    ]
    vocab_rows.sort(key=lambda row: (-row["n_turn_initial"], row["normalized_surface"]))

    by_form: dict[str, list[dict]] = defaultdict(list)
    for row in candidate_rows:
        by_form[row["form_family_id"]].append(row)
    census_rows = []
    for family in sorted(by_form):
        rows = by_form[family]
        initial_rows = [row for row in rows if row["turn_initial"]]
        timed_initial_rows = [
            row for row in initial_rows
            if (
                row["candidate_tier_start_ms"] != ""
                and row["candidate_tier_start_ms"] is not None
                and row["candidate_tier_end_ms"] != ""
                and row["candidate_tier_end_ms"] is not None
            )
        ]
        unexcluded_initial_rows = [
            row for row in initial_rows
            if not row["auto_exclusion_code"]
        ]
        screened_proxy_rows = [
            row for row in timed_initial_rows
            if not row["auto_exclusion_code"]
        ]
        census_rows.append({
            "form_family_id": family,
            "normalized_surfaces": sorted({row["normalized_surface"] for row in rows}),
            "n_raw": len(rows),
            "n_turn_initial": len(initial_rows),
            "n_candidate_only": sum(row["candidate_only_turn"] for row in rows),
            "n_raw_segments": len({row["segment_id"] for row in rows}),
            "n_raw_media": len({row["media_id"] for row in rows if row["media_id"]}),
            "n_raw_recordings": len({row["recording_id"] for row in rows if row["recording_id"]}),
            "n_raw_collection_blocks": len({row["collection_block_id"] for row in rows if row["collection_block_id"]}),
            "n_raw_speakers": len({row["speaker_id"] for row in rows if row["speaker_id"]}),
            "n_initial_segments": len({row["segment_id"] for row in initial_rows}),
            "n_initial_media": len({row["media_id"] for row in initial_rows if row["media_id"]}),
            "n_initial_recordings": len({row["recording_id"] for row in initial_rows if row["recording_id"]}),
            "n_initial_collection_blocks": len({row["collection_block_id"] for row in initial_rows if row["collection_block_id"]}),
            "n_initial_speakers": len({row["speaker_id"] for row in initial_rows if row["speaker_id"]}),
            "n_initial_timed": len(timed_initial_rows),
            "n_initial_timed_segments": len({row["segment_id"] for row in timed_initial_rows}),
            "n_initial_timed_recordings": len({row["recording_id"] for row in timed_initial_rows if row["recording_id"]}),
            "n_initial_timed_collection_blocks": len({row["collection_block_id"] for row in timed_initial_rows if row["collection_block_id"]}),
            "n_initial_timed_speakers": len({row["speaker_id"] for row in timed_initial_rows if row["speaker_id"]}),
            "n_initial_auto_excluded": len(initial_rows) - len(unexcluded_initial_rows),
            "n_initial_unexcluded": len(unexcluded_initial_rows),
            "n_initial_unexcluded_segments": len({row["segment_id"] for row in unexcluded_initial_rows}),
            "n_initial_unexcluded_recordings": len({row["recording_id"] for row in unexcluded_initial_rows if row["recording_id"]}),
            "n_initial_unexcluded_collection_blocks": len({row["collection_block_id"] for row in unexcluded_initial_rows if row["collection_block_id"]}),
            "n_initial_unexcluded_speakers": len({row["speaker_id"] for row in unexcluded_initial_rows if row["speaker_id"]}),
            "n_initial_screened_proxy": len(screened_proxy_rows),
            "n_initial_screened_proxy_segments": len({row["segment_id"] for row in screened_proxy_rows}),
            "n_initial_screened_proxy_recordings": len({row["recording_id"] for row in screened_proxy_rows if row["recording_id"]}),
            "n_initial_screened_proxy_collection_blocks": len({row["collection_block_id"] for row in screened_proxy_rows if row["collection_block_id"]}),
            "n_initial_screened_proxy_speakers": len({row["speaker_id"] for row in screened_proxy_rows if row["speaker_id"]}),
        })

    datasets = {
        "file_manifest": file_rows,
        "turns": turn_rows,
        "candidate_occurrences": candidate_rows,
        "turn_initial_vocabulary": vocab_rows,
        "census_by_form": census_rows,
        "parse_warnings": warning_rows,
    }
    smoke = {
        "n_files": len(paths),
        "n_transcript_bytes": sum(row["bytes"] for row in file_rows),
        "n_recordings": len({row["recording_id"] for row in file_rows if row["recording_id"]}),
        "n_tape_sides": len({row["tape_side_id"] for row in file_rows if row["tape_side_id"]}),
        "n_tapes": len({row["tape_id"] for row in file_rows if row["tape_id"]}),
        "n_collection_blocks": len({row["collection_block_id"] for row in file_rows if row["collection_block_id"]}),
        "n_files_missing_recording_id": sum(not row["recording_id"] for row in file_rows),
        "n_physical_main_tier_lines": physical_main_total,
        "n_collapsed_turns": len(turn_rows),
        "n_fully_timed_turns": sum(row["timing_status"] == "fully_timed" for row in turn_rows),
        "n_partially_timed_turns": sum(row["timing_status"] == "partially_timed" for row in turn_rows),
        "n_untimed_turns": sum(row["timing_status"] == "untimed" for row in turn_rows),
        "n_turns_with_internal_gap_over_2500": sum(row["internal_gap_over_2500"] for row in turn_rows),
        "n_turns_with_internal_gap_over_12000": sum(row["internal_gap_over_12000"] for row in turn_rows),
        "n_unlisted_speaker_turns": sum(not row["speaker_listed"] for row in turn_rows),
        "n_unknown_speaker_turns": sum(row["speaker_unknown"] for row in turn_rows),
        "n_candidate_occurrences": len(candidate_rows),
        "n_parse_warnings": len(warning_rows),
    }
    return datasets, smoke


FIELDNAMES = {
    "file_manifest": [
        "segment_id", "relative_path", "file_sha256", "bytes", "pid", "media_id", "recording_id",
        "tape_side_id", "tape_id", "collection_block_id",
        "media_missing", "original_audio_url", "date", "location", "situation",
        "participant_codes", "n_episodes_with_speech", "n_main_tiers",
        "n_physical_main_tier_lines", "n_timed_tiers", "first_ms", "last_ms",
        "parse_warning_count",
    ],
    "turns": [
        "turn_id", "segment_id", "relative_path", "episode_index", "turn_index",
        "speaker_id", "first_tier_index", "last_tier_index", "start_ms", "end_ms",
        "boundary_start_ms", "boundary_end_ms", "recording_id", "tape_side_id",
        "tape_id", "collection_block_id", "original_same_speaker_chain_id",
        "boundary_reason_from_previous",
        "raw_text", "normalized_text", "previous_turn_id", "previous_speaker",
        "next_turn_id", "next_speaker", "gap_to_next_ms", "next_overlap_ms",
        "speaker_listed", "speaker_unknown", "timing_status", "timing_complete",
        "max_internal_positive_gap_ms", "internal_gap_over_2500",
        "internal_gap_over_12000",
    ],
    "candidate_occurrences": [
        "occurrence_id", "turn_id", "relative_path", "segment_id", "media_id", "recording_id",
        "tape_side_id", "tape_id", "collection_block_id", "original_same_speaker_chain_id",
        "episode_index", "speaker_id", "token_index", "token_end_index", "tier_index", "tier_token_index",
        "candidate_end_tier_index", "candidate_spans_main_tiers",
        "candidate_tier_start_ms", "candidate_tier_end_ms",
        "raw_surface", "normalized_surface", "form_family_id", "alias_rule_id", "seed_group",
        "variant_block_hint", "component_family_ids",
        "turn_initial", "main_tier_initial", "candidate_final", "candidate_only_turn",
        "source_turn_start_ms", "source_turn_end_ms", "source_speaker_listed",
        "source_speaker_unknown", "next_turn_id", "next_speaker_id",
        "next_speaker_listed", "next_speaker_unknown", "next_turn_start_ms",
        "gap_ms", "overlap_ms", "auto_exclusion_code",
        "manual_status", "sign_type_id",
    ],
    "turn_initial_vocabulary": [
        "normalized_surface", "n_turn_initial", "n_segments", "n_speakers",
        "in_seed_alias_table", "form_family_id",
    ],
    "census_by_form": [
        "form_family_id", "normalized_surfaces", "n_raw", "n_turn_initial",
        "n_candidate_only", "n_raw_segments", "n_raw_media", "n_raw_recordings", "n_raw_collection_blocks", "n_raw_speakers",
        "n_initial_segments", "n_initial_media", "n_initial_recordings", "n_initial_collection_blocks", "n_initial_speakers",
        "n_initial_timed", "n_initial_timed_segments", "n_initial_timed_recordings", "n_initial_timed_collection_blocks", "n_initial_timed_speakers",
        "n_initial_auto_excluded", "n_initial_unexcluded",
        "n_initial_unexcluded_segments", "n_initial_unexcluded_recordings", "n_initial_unexcluded_collection_blocks", "n_initial_unexcluded_speakers",
        "n_initial_screened_proxy", "n_initial_screened_proxy_segments",
        "n_initial_screened_proxy_recordings", "n_initial_screened_proxy_collection_blocks", "n_initial_screened_proxy_speakers",
    ],
    "parse_warnings": ["relative_path", "line_number", "warning_code", "detail"],
}


def write_outputs(
    output_dir: Path,
    datasets: dict[str, list[dict]],
    smoke: dict[str, int],
    args: argparse.Namespace,
    alias_sha256: str,
    source_verification: dict[str, str],
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    output_hashes = {}
    for name, rows in datasets.items():
        path = output_dir / f"{name}.csv"
        write_csv(path, rows, FIELDNAMES[name])
        output_hashes[path.name] = sha256_file(path)

    hash_path = output_dir / "output_sha256.json"
    hash_path.write_text(
        json.dumps(output_hashes, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    manifest = {
        "corpus_name": "CABNC",
        "repository_url": REPOSITORY_URL,
        "commit_sha": args.corpus_commit,
        "subtree_path": SUBTREE_PATH,
        "subtree_git_sha": args.subtree_object,
        "source_verification": source_verification,
        "input_dir": str(args.input.resolve()),
        "census_run_utc": datetime.now(timezone.utc).isoformat(),
        "license_id": "CC-BY-3.0",
        "license_url": "https://creativecommons.org/licenses/by/3.0/",
        "required_citation": "Albert, de Ruiter & de Ruiter (2015), CABNC",
        "parser_version": PARSER_VERSION,
        "python_version": platform.python_version(),
        "platform": platform.platform(),
        "locale_encoding": sys.getfilesystemencoding(),
        "candidate_lexicon_sha256": alias_sha256,
        "exact_command": " ".join(sys.argv),
        "smoke_counts": smoke,
        "output_hashes": output_hashes,
    }
    (output_dir / "run_manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True, help="Frozen cabnc_talkbank_chat directory")
    parser.add_argument("--forms", type=Path, required=True, help="Versioned form-alias CSV")
    parser.add_argument("--out", type=Path, required=True, help="Output directory")
    parser.add_argument("--corpus-commit", default=DEFAULT_COMMIT)
    parser.add_argument("--subtree-object", default=DEFAULT_SUBTREE_OBJECT)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if not args.input.is_dir():
        raise SystemExit(f"CABNC input directory not found: {args.input}")
    try:
        source_verification = verify_frozen_input(
            args.input,
            args.corpus_commit,
            args.subtree_object,
        )
    except ValueError as error:
        raise SystemExit(str(error)) from error
    aliases, alias_sha256 = load_aliases(args.forms)
    datasets, smoke = parse_corpus(args.input, aliases, args.corpus_commit)
    write_outputs(
        args.out,
        datasets,
        smoke,
        args,
        alias_sha256,
        source_verification,
    )
    print(json.dumps(smoke, sort_keys=True))


if __name__ == "__main__":
    main()
