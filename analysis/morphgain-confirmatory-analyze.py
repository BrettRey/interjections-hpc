#!/usr/bin/env python3
"""Confirmatory analysis for the preregistered morphology-gain COHA study."""

from __future__ import annotations

import csv
import math
import random
from pathlib import Path

from scipy.stats import beta

SEED = 2026
BASE = Path(__file__).parent / "morphgain-confirmatory"
CODED = BASE / "morphgain-coded-primary.csv"
KEY = BASE / "morphgain-token-key.csv"


def read_csv(path: Path) -> list[dict]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict], fieldnames: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def jeffreys_interval(successes: int, total: int) -> tuple[float, float]:
    return (
        beta.ppf(0.025, successes + 0.5, total - successes + 0.5),
        beta.ppf(0.975, successes + 0.5, total - successes + 0.5),
    )


def main() -> None:
    coded = {row["coding_id"]: row for row in read_csv(CODED)}
    key = {row["coding_id"]: row for row in read_csv(KEY)}
    rows = []
    for coding_id, row in coded.items():
        merged = {**key[coding_id], **row}
        merged["year"] = int(merged["year"])
        merged["decade"] = int(merged["decade"])
        merged["exclude"] = int(merged["exclude"])
        merged["verbal_syntax"] = int(merged["verbal_syntax"])
        merged["semantic_residue"] = int(merged["semantic_residue"])
        merged["interactional_residue"] = int(merged["interactional_residue"])
        merged["targeted_entity"] = int(merged["targeted_entity"])
        rows.append(merged)

    included = [row for row in rows if row["exclude"] == 0]
    family_rows = []
    early_rows = []
    confirmatory_rows = []

    for family in sorted({row["family"] for row in rows}):
        fam = [row for row in included if row["family"] == family]
        decade_counts = {}
        for row in fam:
            decade_counts[row["decade"]] = decade_counts.get(row["decade"], 0) + 1
        qualifying_decades = [decade for decade, count in sorted(decade_counts.items()) if count >= 3]
        go = len(fam) >= 20 and len(qualifying_decades) >= 2
        family_rows.append({
            "family": family,
            "analyzable_tokens": len(fam),
            "decades_with_3plus": len(qualifying_decades),
            "go_no_go": "GO" if go else "NO-GO",
            "decade_counts": " ".join(f"{decade}:{decade_counts[decade]}" for decade in sorted(decade_counts)),
        })
        if not go:
            continue

        start = qualifying_decades[0]
        window_decades = []
        window = []
        for decade in sorted(decade_counts):
            if decade < start:
                continue
            window_decades.append(decade)
            window.extend(row for row in fam if row["decade"] == decade)
            if len(window) >= 10:
                break
        window.sort(key=lambda row: (row["year"], row["term"], int(row["kwic_line"])))
        successes = sum(1 for row in window if row["verbal_syntax"] == 1 and row["semantic_residue"] == 1)
        total = len(window)
        lower, upper = jeffreys_interval(successes, total)
        confirmatory_rows.append({
            "family": family,
            "earliest_window_decades": " ".join(map(str, window_decades)),
            "early_window_n": total,
            "successes": successes,
            "proportion": f"{successes / total:.3f}",
            "jeffreys_lower": f"{lower:.3f}",
            "jeffreys_upper": f"{upper:.3f}",
            "supported": "yes" if lower > 0.5 else "no",
        })
        for row in window:
            early_rows.append({
                "family": family,
                "coding_id": row["coding_id"],
                "token_id": row["token_id"],
                "term": row["term"],
                "year": row["year"],
                "decade": row["decade"],
                "genre": row["genre"],
                "source": row["source"],
                "context": row["context"],
                "verbal_syntax": row["verbal_syntax"],
                "semantic_residue": row["semantic_residue"],
                "interactional_residue": row["interactional_residue"],
                "targeted_entity": row["targeted_entity"],
            })

    write_csv(BASE / "morphgain-go-nogo-summary.csv", family_rows, [
        "family", "analyzable_tokens", "decades_with_3plus", "go_no_go", "decade_counts",
    ])
    write_csv(BASE / "morphgain-confirmatory-results.csv", confirmatory_rows, [
        "family", "earliest_window_decades", "early_window_n", "successes",
        "proportion", "jeffreys_lower", "jeffreys_upper", "supported",
    ])
    write_csv(BASE / "morphgain-earliest-windows.csv", early_rows, [
        "family", "coding_id", "token_id", "term", "year", "decade", "genre",
        "source", "context", "verbal_syntax", "semantic_residue",
        "interactional_residue", "targeted_entity",
    ])

    reliability_n = math.ceil(len(included) * 0.10)
    random.seed(SEED)
    reliability = random.sample(included, reliability_n)
    reliability.sort(key=lambda row: row["coding_id"])
    reliability_sheet = []
    for row in reliability:
        blinded = dict(row)
        blinded.update({
            "exclude": "",
            "exclusion_reason": "",
            "verbal_syntax": "",
            "semantic_residue": "",
            "interactional_residue": "",
            "targeted_entity": "",
            "coder_notes": "",
        })
        reliability_sheet.append(blinded)
    write_csv(BASE / "morphgain-reliability-sheet.csv", reliability_sheet, [
        "coding_id", "family", "term", "genre", "source", "left", "target",
        "right", "exclude", "exclusion_reason", "verbal_syntax",
        "semantic_residue", "interactional_residue", "targeted_entity",
        "coder_notes",
    ])
    write_csv(BASE / "morphgain-reliability-key.csv", reliability, [
        "coding_id", "token_id", "year", "decade", "exclude",
        "exclusion_reason", "verbal_syntax", "semantic_residue",
        "interactional_residue", "targeted_entity",
    ])

    semantic_values = {row["semantic_residue"] for row in included if row["verbal_syntax"] == 1}
    secondary_note = BASE / "morphgain-secondary-model-note.txt"
    if len(semantic_values) < 2:
        secondary_note.write_text(
            "Secondary diachronic model not estimated: among included tokens with "
            "verbal_syntax = 1, semantic_residue has no variation.\n",
            encoding="utf-8",
        )

    print("Confirmatory results")
    for row in confirmatory_rows:
        print(
            f'{row["family"]}\tn={row["early_window_n"]}\t'
            f'{row["successes"]}/{row["early_window_n"]}\t'
            f'Jeffreys95=[{row["jeffreys_lower"]}, {row["jeffreys_upper"]}]\t'
            f'supported={row["supported"]}'
        )
    print(f"Reliability sheet rows: {reliability_n}")


if __name__ == "__main__":
    main()
