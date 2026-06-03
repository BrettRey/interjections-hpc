#!/usr/bin/env python3
"""Compute reliability for the blind morphology-gain recode."""

from __future__ import annotations

import csv
from pathlib import Path

BASE = Path(__file__).parent / "morphgain-confirmatory"
SHEET = BASE / "morphgain-reliability-sheet.csv"
KEY = BASE / "morphgain-reliability-key.csv"
OUTFILE = BASE / "morphgain-reliability-results.csv"

CODES = [
    "exclude",
    "verbal_syntax",
    "semantic_residue",
    "interactional_residue",
    "targeted_entity",
]


def read_csv(path: Path) -> list[dict]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def kappa(primary: list[int], second: list[int]) -> float:
    total = len(primary)
    observed = sum(1 for first, other in zip(primary, second) if first == other) / total
    first_ones = sum(primary) / total
    second_ones = sum(second) / total
    expected = first_ones * second_ones + (1 - first_ones) * (1 - second_ones)
    if expected == 1:
        return 1.0 if observed == 1 else 0.0
    return (observed - expected) / (1 - expected)


def parse_binary(value: str, coding_id: str, code: str) -> int:
    value = str(value).strip()
    if value not in {"0", "1"}:
        raise ValueError(f"{coding_id}: {code} must be 0 or 1, got {value!r}")
    return int(value)


def main() -> None:
    sheet = {row["coding_id"]: row for row in read_csv(SHEET)}
    key = {row["coding_id"]: row for row in read_csv(KEY)}
    if set(sheet) != set(key):
        missing_from_sheet = sorted(set(key) - set(sheet))
        missing_from_key = sorted(set(sheet) - set(key))
        raise SystemExit(
            "Reliability sheet/key mismatch: "
            f"missing_from_sheet={missing_from_sheet}; missing_from_key={missing_from_key}"
        )

    results = []
    for code in CODES:
        primary = []
        second = []
        for coding_id in sorted(key):
            primary.append(parse_binary(key[coding_id][code], coding_id, code))
            second.append(parse_binary(sheet[coding_id][code], coding_id, code))
        agree = sum(1 for first, other in zip(primary, second) if first == other)
        results.append({
            "code": code,
            "n": len(primary),
            "agreements": agree,
            "percent_agreement": f"{agree / len(primary):.3f}",
            "cohens_kappa": f"{kappa(primary, second):.3f}",
        })

    with OUTFILE.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=[
            "code", "n", "agreements", "percent_agreement", "cohens_kappa",
        ])
        writer.writeheader()
        writer.writerows(results)

    for row in results:
        print(
            f'{row["code"]}\tn={row["n"]}\tagree={row["percent_agreement"]}\t'
            f'kappa={row["cohens_kappa"]}'
        )


if __name__ == "__main__":
    main()
