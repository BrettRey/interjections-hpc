#!/usr/bin/env python3
"""Prepare preregistered morphology-gain COHA token sheets."""

from __future__ import annotations

import csv
import json
import random
import re
from pathlib import Path

SEED = 2026
BASE = Path(__file__).parent / "morphgain-confirmatory"
RAW = BASE / "raw"

FAMILIES = {
    "wow": ["wowed", "wowing", "wows"],
    "boo": ["booed", "booing", "boos"],
    "ooh": ["oohed", "oohing", "oohs"],
    "shoo": ["shooed", "shooing", "shoos"],
}
TERM_TO_FAMILY = {term: family for family, terms in FAMILIES.items() for term in terms}
TERMS = list(TERM_TO_FAMILY)


def clean(text: str) -> str:
    return re.sub(r"\s+", " ", str(text or "")).strip()


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def chart_counts(term: str) -> tuple[int | None, dict[int, int], str | None]:
    path = RAW / f"{term}-chart.json"
    if not path.exists():
        return None, {}, "missing"
    data = load_json(path)
    if "There was an error" in data.get("text", ""):
        return None, {}, "server_error"
    for table in data.get("tables", []):
        if not table or table[0][:2] != ["SECTION", "ALL"]:
            continue
        header = table[0]
        freq_row = next((row for row in table if row and row[0] == "FREQ"), None)
        if not freq_row:
            continue
        counts = {}
        for label, value in zip(header[2:], freq_row[2:]):
            if label.isdigit():
                counts[int(label)] = int(value.replace(",", ""))
        return int(freq_row[1].replace(",", "")), counts, None
    return None, {}, "no_freq_table"


def kwic_rows(term: str) -> tuple[list[dict], str | None]:
    path = RAW / f"{term}-kwic.json"
    if not path.exists():
        return [], "missing"
    data = load_json(path)
    if "There was an error" in data.get("text", ""):
        return [], "server_error"

    rows = []
    malformed = 0
    for table in data.get("tables", []):
        for row in table:
            if not row or not str(row[0]).isdigit():
                continue
            if len(row) < 6 or not re.fullmatch(r"\d{4}", str(row[2])):
                malformed += 1
                continue
            target_idx = None
            for i, cell in enumerate(row):
                if clean(cell).lower() == term:
                    target_idx = i
                    break
            if target_idx is None:
                context_cells = [clean(cell) for cell in row[5:] if clean(cell) not in {"A", "B", "C"}]
                context = max(context_cells, key=len) if context_cells else ""
                match = re.search(rf"(?<![A-Za-z]){re.escape(term)}(?![A-Za-z])", context, re.IGNORECASE)
                if not match:
                    malformed += 1
                    continue
                left = clean(context[:match.start()])
                target = context[match.start():match.end()]
                right = clean(context[match.end():])
            elif target_idx == 0 or target_idx + 1 >= len(row):
                malformed += 1
                continue
            else:
                left = clean(row[target_idx - 1])
                target = clean(row[target_idx])
                right = clean(row[target_idx + 1])
            year = int(row[2])
            rows.append({
                "term": term,
                "family": TERM_TO_FAMILY[term],
                "kwic_line": row[0],
                "doc_id": row[1],
                "year": year,
                "decade": (year // 10) * 10,
                "genre": clean(row[3]),
                "source": clean(row[4]),
                "left": left,
                "target": target,
                "right": right,
            })
    status = None if rows else "no_token_rows"
    if malformed:
        status = f"{status or 'ok'}; malformed_rows={malformed}"
    return rows, status


def dedupe(rows: list[dict]) -> tuple[list[dict], int]:
    seen = set()
    out = []
    duplicates = 0
    for row in rows:
        key = (
            row["doc_id"], row["year"], row["source"], row["left"].lower(),
            row["target"].lower(), row["right"].lower(),
        )
        if key in seen:
            duplicates += 1
            continue
        seen.add(key)
        out.append(row)
    return out, duplicates


def write_csv(path: Path, rows: list[dict], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fieldnames})


def main() -> None:
    all_rows = []
    summary_rows = []

    for term in TERMS:
        chart_total, decade_counts, chart_status = chart_counts(term)
        rows, kwic_status = kwic_rows(term)
        unique_rows, duplicate_count = dedupe(rows)
        all_rows.extend(unique_rows)
        summary_rows.append({
            "family": TERM_TO_FAMILY[term],
            "term": term,
            "chart_total": chart_total if chart_total is not None else "",
            "chart_status": chart_status or "ok",
            "kwic_token_rows": len(rows),
            "deduplicated_token_rows": len(unique_rows),
            "duplicate_rows_removed": duplicate_count,
            "kwic_status": kwic_status or "ok",
            "decades_with_3plus_raw": sum(1 for count in decade_counts.values() if count >= 3),
        })

    all_rows.sort(key=lambda row: (row["family"], row["term"], row["year"], int(row["kwic_line"])))
    for i, row in enumerate(all_rows, start=1):
        row["token_id"] = f"mg{i:04d}"
        row["context"] = clean(f'{row["left"]} {row["target"]} {row["right"]}')

    family_summary = []
    for family, terms in FAMILIES.items():
        rows = [row for row in all_rows if row["family"] == family]
        decade_counts = {}
        for row in rows:
            decade_counts[row["decade"]] = decade_counts.get(row["decade"], 0) + 1
        family_summary.append({
            "family": family,
            "raw_deduplicated_tokens": len(rows),
            "raw_decades_with_3plus": sum(1 for count in decade_counts.values() if count >= 3),
            "raw_go_no_go_before_exclusions": "GO" if len(rows) >= 20 and sum(1 for count in decade_counts.values() if count >= 3) >= 2 else "NO-GO",
        })

    randomized = all_rows[:]
    random.seed(SEED)
    random.shuffle(randomized)
    for i, row in enumerate(randomized, start=1):
        row["coding_id"] = f"mgc{i:04d}"

    write_csv(
        BASE / "morphgain-token-key.csv",
        randomized,
        [
            "coding_id", "token_id", "family", "term", "kwic_line", "doc_id",
            "year", "decade", "genre", "source", "left", "target", "right", "context",
        ],
    )
    write_csv(
        BASE / "morphgain-coding-sheet.csv",
        randomized,
        [
            "coding_id", "family", "term", "genre", "source", "left", "target", "right",
            "exclude", "exclusion_reason", "verbal_syntax", "semantic_residue",
            "interactional_residue", "targeted_entity", "coder_notes",
        ],
    )
    write_csv(
        BASE / "morphgain-extraction-summary.csv",
        summary_rows,
        [
            "family", "term", "chart_total", "chart_status", "kwic_token_rows",
            "deduplicated_token_rows", "duplicate_rows_removed", "kwic_status",
            "decades_with_3plus_raw",
        ],
    )
    write_csv(
        BASE / "morphgain-family-summary.csv",
        family_summary,
        ["family", "raw_deduplicated_tokens", "raw_decades_with_3plus", "raw_go_no_go_before_exclusions"],
    )

    print(f"Wrote {len(all_rows)} deduplicated raw token rows")
    for row in family_summary:
        print(f'{row["family"]}\t{row["raw_deduplicated_tokens"]}\t{row["raw_decades_with_3plus"]}\t{row["raw_go_no_go_before_exclusions"]}')


if __name__ == "__main__":
    main()
