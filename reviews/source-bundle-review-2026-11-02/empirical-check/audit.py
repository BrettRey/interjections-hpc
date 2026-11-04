#!/usr/bin/env python3
"""Read-only arithmetic audit of the manuscript's two withdrawn analyses.

Run from any directory. No linguistic recoding, model fitting, or project writes.
Output is JSON on stdout; all input data and source code remain untouched.
"""
from collections import Counter
import csv
import hashlib
import json
import math
from pathlib import Path
import random
import subprocess

from scipy.stats import beta

ROOT = Path(__file__).resolve().parents[3]
REVISION = "074dfb44cef5b18d292ac176ba5acbfedc76e3b1"
DATA = ROOT / "analysis" / "morphgain-confirmatory"


def rows(path):
    with Path(path).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def reliability(a, b):
    assert len(a) == len(b) > 0
    n = len(a)
    agreement_n = sum(x == y for x, y in zip(a, b))
    observed = agreement_n / n
    expected = sum(a.count(v) / n * b.count(v) / n for v in {0, 1})
    return {
        "n": n, "agreements": agreement_n,
        "observed_agreement": observed, "expected_agreement": expected,
        "kappa": None if expected == 1 else (observed - expected) / (1 - expected),
        "primary_margin": dict(Counter(a)), "second_margin": dict(Counter(b)),
    }


primary = rows(DATA / "morphgain-coded-primary.csv")
included = [r for r in primary if r["exclude"] == "0"]
key = {r["coding_id"]: r for r in rows(DATA / "morphgain-token-key.csv")}
reliability_key = {r["coding_id"]: r for r in rows(DATA / "morphgain-reliability-key.csv")}
recode = rows(DATA / "morphgain-reliability-sheet.csv")
assert set(reliability_key) == {r["coding_id"] for r in recode}
assert all(
    r[c] == reliability_key[r["coding_id"]][c]
    for r in primary if r["coding_id"] in reliability_key
    for c in ["exclude", "verbal_syntax", "semantic_residue", "interactional_residue", "targeted_entity"]
)
windows = []
for family in sorted({r["family"] for r in included}):
    family_rows = [r for r in included if r["family"] == family]
    decades = Counter(int(key[r["coding_id"]]["decade"]) for r in family_rows)
    eligible = sorted(d for d, n in decades.items() if n >= 3)
    window = []
    window_decades = []
    for decade in sorted(decades):
        if decade < eligible[0]:
            continue
        window_decades.append(decade)
        window.extend(r for r in family_rows if int(key[r["coding_id"]]["decade"]) == decade)
        if len(window) >= 10:
            break
    n = len(window)
    k = sum(r["verbal_syntax"] == r["semantic_residue"] == "1" for r in window)
    windows.append({
        "family": family, "included": len(family_rows),
        "decades_with_3plus": len(eligible), "window_decades": window_decades,
        "n": n, "assigned_successes": k,
        "jeffreys_95": [float(beta.ppf(p, k + .5, n - k + .5)) for p in [.025, .975]],
        "recode_overlap_ids": [r["coding_id"] for r in window if r["coding_id"] in reliability_key],
    })
sampled = random.Random(2026).sample(included, math.ceil(len(included) * .1))
morphgain = {
    "primary_rows": len(primary), "included": len(included),
    "excluded": len(primary) - len(included),
    "included_counts": {c: dict(Counter(r[c] for r in included)) for c in ["family", "verbal_syntax", "semantic_residue"]},
    "early_windows": windows,
    "recode_matches_declared_seed_and_sampling_frame": {r["coding_id"] for r in sampled} == set(reliability_key),
    "recode_family_counts": dict(Counter(r["family"] for r in recode)),
    "recode_decade_counts": dict(sorted(Counter(key[r["coding_id"]]["decade"] for r in recode).items())),
    "recode_notes_nonblank": sum(bool(r["coder_notes"].strip()) for r in recode),
    "reliability": {
        c: reliability([int(reliability_key[r["coding_id"]][c]) for r in recode], [int(r[c]) for r in recode])
        for c in ["exclude", "verbal_syntax", "semantic_residue", "interactional_residue", "targeted_entity"]
    },
}

fie = rows(ROOT / "analysis/fie-coding-sheet-annotated.csv")
fie_by_id = {r["coding_id"]: r for r in fie}
fie_decades = {r["coding_id"]: r for r in rows(ROOT / "analysis/fie-decade-key.csv")}
fie_excluded = rows(ROOT / "analysis/fie-excluded.csv")
fie_reliability_key = {r["recode_id"]: r for r in rows(ROOT / "analysis/fie-reliability-key.csv")}
fie_recode = rows(ROOT / "analysis/fie-reliability-sheet.csv")
assert set(fie_reliability_key) == {r["recode_id"] for r in fie_recode}
fie_report = {
    "coded_rows": len(fie),
    "all_rows_have_binary_human_codes": all(r["human_" + c] in {"0", "1"} for r in fie for c in ["syn", "sem", "int"]),
    "joint_counts": dict(Counter("".join(r["human_" + c] for c in ["syn", "sem", "int"]) for r in fie)),
    "predicted_notes": dict(Counter(r["human_notes"] for r in fie if r["human_notes"].startswith("predicted"))),
    "predicted_note_count": sum(r["human_notes"].startswith("predicted") for r in fie),
    "excluded_rows": len(fie_excluded),
    "exclusion_reasons": dict(Counter(r["exclusion_reason"] for r in fie_excluded)),
    "selected_examples": {
        i: {k: fie_by_id[i][k] for k in ["context", "human_syn", "human_sem", "human_int", "human_notes"]}
        for i in ["F014", "F028", "F043", "F450", "F597"]
    },
    "reliability": {
        c: reliability(
            [int(fie_reliability_key[r["recode_id"]]["original_" + c]) for r in fie_recode],
            [int(r["recode_" + c]) for r in fie_recode],
        ) for c in ["syn", "sem", "int"]
    },
    "reliability_key_matches_analyzed_codes": all(
        r["original_" + c] == fie_by_id[r["coding_id"]]["human_" + c]
        for r in fie_reliability_key.values() for c in ["syn", "sem", "int"]
    ),
    "decade_summary": [
        {"decade": d, "n": sum(fie_decades[r["coding_id"]]["decade"] == d for r in fie),
         **{c: sum(int(r["human_" + c]) for r in fie if fie_decades[r["coding_id"]]["decade"] == d) for c in ["syn", "sem", "int"]}}
        for d in sorted({r["decade"] for r in fie_decades.values()})
    ],
    "iid_continuous_ordering_prior_probability": 1 / math.factorial(3),
}

input_paths = [
    "analysis/morphgain-confirmatory-code-primary.py", "analysis/morphgain-confirmatory-reliability.py",
    "analysis/morphgain-confirmatory-analyze.py", "analysis/fie-confirmatory-model.R",
    "analysis/fie-coding-sheet-annotated.csv", "analysis/fie-decade-key.csv", "analysis/fie-excluded.csv",
    "analysis/fie-reliability-key.csv", "analysis/fie-reliability-sheet.csv",
    "morphology-gain-coha-preregistration.md", "fie-coha-preregistration.md",
] + ["analysis/morphgain-confirmatory/" + name for name in [
    "morphgain-coded-primary.csv", "morphgain-reliability-key.csv", "morphgain-reliability-sheet.csv",
    "morphgain-token-key.csv", "morphgain-earliest-windows.csv", "RESULTS.md", "extraction-metadata.json",
]]
provenance = {}
for relative in input_paths:
    content = (ROOT / relative).read_bytes()
    archived = subprocess.run(["git", "show", f"{REVISION}:{relative}"], cwd=ROOT, capture_output=True, check=True).stdout
    provenance[relative] = {
        "sha256": hashlib.sha256(content).hexdigest(), "matches_cited_archive_revision": content == archived,
    }
print(json.dumps({"archive_revision": REVISION, "morphgain": morphgain, "fie": fie_report, "inputs": provenance}, indent=2))
