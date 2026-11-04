#!/usr/bin/env python3
"""Replay existing ha classification and descriptive arithmetic, without refits.

Reads existing project files; JSON output only on stdout. Never invokes the
original scripts' main functions (which would overwrite original outputs).
"""
from collections import Counter
import csv
import hashlib
import json
from pathlib import Path
import statistics as st
import subprocess

ROOT = Path(__file__).resolve().parents[3]
REV = "074dfb44cef5b18d292ac176ba5acbfedc76e3b1"
script = ROOT / "analysis/pool-ha-rates.py"
ns = {"__file__": str(script), "__name__": "readonly_ha_audit"}
exec(compile(script.read_text(), str(script), "exec"), ns)


def read_rows(relative):
    with (ROOT / relative).open(newline="") as f:
        return list(csv.DictReader(f))


def ranking(values, country="KE"):
    return sorted(values, key=lambda c: -values[c]).index(country) + 1


data = ns["load"]()
frequency_row = next(r for r in read_rows("data/glowbe-interjection-frequencies.csv") if r["item"] == "ha")
freq = {c: float(v) for c, v in frequency_row.items() if c != "item"}
count_row = next(r for r in read_rows("data/glowbe-raw-counts.csv") if r["item"] == "ha")
validity = {r["country"]: r for r in read_rows("data/ha-validity-rates.csv")}
country_counts = {}
for c, samples in data.items():
    k_in, n = ns["count"](samples, True, 0.0)
    k_out, n_out = ns["count"](samples, False, 0.0)
    assert n == n_out == int(validity[c]["n_coded"])
    assert int(k_in) == int(validity[c]["k_laughter_in"])
    assert int(k_out) == int(validity[c]["k_laughter_out"])
    country_counts[c] = {
        "exported_sample_n": n, "model_corpus_tagged_total": int(count_row[c]),
        "sample_fraction": n / int(count_row[c]),
        "classifier_retained_laughter_in": int(k_in),
        "classifier_retained_laughter_out": int(k_out),
        "classifier_counts": dict(Counter(ns["classify"](s) for s in samples)),
    }

multiverse = []
stored = {r["spec"]: r for r in read_rows("analysis/hand-extracted/ha-pooled-multiverse.csv")}
for laughter in (True, False):
    for weight, label in ((0., "excl"), (.5, "half"), (1., "incl")):
        spec = f"laughter={'in' if laughter else 'out'}, unclear={label}"
        obs = {c: ns["count"](samples, laughter, weight) for c, samples in data.items()}
        raw = {c: k / n for c, (k, n) in obs.items()}
        pooled, prior = ns["pool"](obs)
        adjusted_raw = {c: freq[c] * raw[c] for c in freq}
        adjusted_pooled = {c: freq[c] * pooled[c] for c in freq}
        output = {
            "spec": spec,
            "cv_raw": st.stdev(adjusted_raw.values()) / st.mean(adjusted_raw.values()),
            "cv_pooled": st.stdev(adjusted_pooled.values()) / st.mean(adjusted_pooled.values()),
            "ke_rank_raw": ranking(adjusted_raw), "ke_rank_pooled": ranking(adjusted_pooled),
            "prior_a": prior[0], "prior_b": prior[1],
            "max_rate_movement_percentage_points": max(abs(raw[c] - pooled[c]) * 100 for c in freq),
        }
        for field in ("cv_raw", "cv_pooled"):
            assert round(output[field], 3) == float(stored[spec][field])
        for field in ("ke_rank_raw", "ke_rank_pooled"):
            assert output[field] == int(stored[spec][field])
        multiverse.append(output)

validation = []
for n, line in enumerate((ROOT / "analysis/ha-labelled-validation-set.tsv").read_text().splitlines(), 1):
    gold, context = line.split("\t", 1)
    predicted = ns["classify"](context)
    validation.append({"line": n, "recorded_label": gold, "classifier_label": predicted, "context": context})

model_rows = read_rows("data/glowbe-raw-counts.csv")
model_countries = [c for c in model_rows[0] if c not in {"item", "tag"}]
commit_messages = {
    commit: subprocess.run(["git", "show", "--format=fuller", "--no-patch", commit], cwd=ROOT, capture_output=True, text=True, check=True).stdout
    for commit in ["9d87451", "0a8867d", "c9e5d9d", "d4770f1"]
}

requested = [
    "analysis/filter-ha-concordance.py", "data/ha-validity-rates.csv",
    "analysis/hand-extracted/ha-pooled-multiverse.csv", "analysis/pool-ha-rates.py",
    "analysis/conditioning-model.R",
]
dependencies = [
    "analysis/ha-labelled-validation-set.tsv", "data/glowbe-interjection-frequencies.csv",
    "data/glowbe-raw-counts.csv", "analysis/hand-extracted/ha-corrected-rates.csv",
    "analysis/conditioning-model-measerr.R",
] + [f"analysis/hand-extracted/ha-concordances/ha_uh-{c}.tsv" for c in data]
provenance = {}
for path in requested + dependencies:
    content = (ROOT / path).read_bytes()
    archive = subprocess.run(["git", "show", f"{REV}:{path}"], cwd=ROOT, capture_output=True, check=True).stdout
    provenance[path] = {
        "sha256": hashlib.sha256(content).hexdigest(), "matches_cited_revision": content == archive,
        "directly_requested": path in requested,
    }

result = {
    "archive_revision": REV,
    "sample_n_total": sum(len(v) for v in data.values()),
    "country_counts": country_counts,
    "validity_csv_exactly_matches_classifier_replay": True,
    "uncorrected_cv": st.stdev(freq.values()) / st.mean(freq.values()),
    "uncorrected_ke_rank": ranking(freq),
    "multiverse": multiverse,
    "multiverse_matches_stored_output_at_recorded_precision": True,
    "validation": {
        "n": len(validation),
        "exact_label_agreements": sum(r["recorded_label"] == r["classifier_label"] for r in validation),
        "binary_interjection_agreements": sum((r["recorded_label"] == "interjection") == (r["classifier_label"] == "interjection") for r in validation),
        "exact_label_disagreements": [r for r in validation if r["recorded_label"] != r["classifier_label"]],
    },
    "loo_design": {
        "items": len(model_rows), "countries": len(model_countries),
        "aggregate_cells": len(model_rows) * len(model_countries),
        "training_cells_per_pointwise_holdout": len(model_rows) * len(model_countries) - 1,
        "same_country_other_items": len(model_rows) - 1,
        "same_item_other_countries": len(model_countries) - 1,
    },
    "commit_messages": commit_messages,
    "input_provenance": provenance,
}
print(json.dumps(result, indent=2))
