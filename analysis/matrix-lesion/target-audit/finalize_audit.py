"""Stage 2 of the discarded target-evidence audit.

Applies model semantic verdicts with the 2026-11-04 correction layer
(semantic-verdicts.json v2, built by
apply_corrections_2026_11_04.py; no human adjudication has been
performed) to the mechanically verified results (audit-results.json,
produced by analyze_audit.py) and aggregates AVAILABILITY ONLY:
pair-level and unit-level evidence classes, assertion/proposition
structure, item-specific vs inherited support, stratum breakdowns.
No source-target association, assignment, or lesion.

Units for verdicted assertions are DERIVED from effective fields
(pattern, positions, effect dimension; contribution and host; claim
strength), never copied from coder unit labels. Non-verdicted
assertions (ADJACENT-ONLY and below) keep coder units for adjacent
reporting only. Proposition clusters come from the hand-reviewed
proposition-map.json, not quote-prefix keys.

Assertion-level effective outcomes:
- reject   -> assertion void
- downgrade-> contribution becomes ADJACENT-ONLY
- pass-weak-> kept, flagged (reported both included and excluded)
- pass / no verdict needed (ADJACENT-ONLY assertions) -> kept
Any ITEM-DIRECT/CLASS-INHERITED/CONFLICT assertion lacking a verdict
or effective block raises an error.

Outputs audit-final.json and AUDIT-tables.md; prints a summary.
"""
import json
from collections import Counter, defaultdict
from pathlib import Path

BASE = Path("analysis/matrix-lesion/target-audit")
RES = json.loads((BASE / "audit-results.json").read_text())
VERDICTS = json.loads((BASE / "semantic-verdicts.json").read_text())["verdicts"]
SAMPLE = {}
for line in (BASE / "sample.csv").read_text().strip().splitlines()[1:]:
    item, stratum, _ = line.split(",", 2)
    SAMPLE[item] = stratum

AVAIL = ["ITEM-DIRECT", "CLASS-INHERITED", "CONFLICT", "ADJACENT-ONLY",
         "RETRIEVAL-FAILURE-SUSPECTED", "INAPPLICABLE", "SILENCE"]
STRENGTH = {a: len(AVAIL) - i for i, a in enumerate(AVAIL)}
NEEDS_VERDICT = {"ITEM-DIRECT", "CLASS-INHERITED", "CONFLICT"}
FAMILIES = ["agy", "copilot", "qwen", "claude"]


def assertion_outcome(family, prop, item, a, include_weak):
    """Return (effective_contribution or None if void, label, record).

    Effective verdict and effective fields (correction layer) win over
    original coder and verdict labels.
    """
    contrib = a.get("availability_contribution")
    key = f"{family}|{prop}|{item}|{a.get('assertion_id')}"
    rec = VERDICTS.get(key, {})
    eff = rec.get("effective") or {}
    v = eff.get("verdict", rec.get("verdict"))
    if contrib in NEEDS_VERDICT:
        if v is None or not eff:
            raise SystemExit(
                f"missing verdict/effective block for {key}")
    if v == "reject":
        return None, "reject", rec
    if v == "downgrade":
        return "ADJACENT-ONLY", "downgrade", rec
    if v == "pass-weak" and not include_weak:
        return None, "pass-weak-excluded", rec
    return eff.get("contribution", contrib), v or "pass", rec


def derived_unit(prop, rec):
    """Derive the adjudicated unit string from effective fields."""
    eff = rec["effective"]
    if prop == "P10":
        pat = eff["repetition_pattern"]
        if pat == "distributed-recurrence" and \
                eff.get("repetition_positions"):
            pat = f"{pat}[{eff['repetition_positions']}]"
        return f"{pat}|{eff['effect_dimension']}"
    if prop == "P11":
        return (f"{eff['contribution_assessed']}"
                f"|{eff['host_relationship']}")
    return eff["claim_strength"]


def run(include_weak):
    out = {"pair_level": {}, "unit_level": defaultdict(dict),
           "unreviewed": [], "clusters": {}, "support_mix": Counter(),
           "source_target_relation": Counter()}
    clusters = defaultdict(list)
    for key, by_fam in RES["pairs"].items():
        prop, item = key.split("/")
        best = None
        unit_best = {}
        for family in FAMILIES:
            rec = by_fam.get(family)
            if not isinstance(rec, dict) or "valid_assertions" not in rec:
                continue
            eff = {}
            verdicted_ids = set()
            for a in rec["valid_assertions"]:
                contrib, label, vrec = assertion_outcome(
                    family, prop, item, a, include_weak)
                if contrib is None or contrib == "SILENCE":
                    continue
                aid = a.get("assertion_id")
                eff[aid] = contrib
                if best is None or STRENGTH[contrib] > STRENGTH[best]:
                    best = contrib
                if vrec:
                    verdicted_ids.add(aid)
                    unit = derived_unit(prop, vrec)
                    cur = unit_best.get(unit)
                    if cur is None or STRENGTH[contrib] > STRENGTH[cur]:
                        unit_best[unit] = contrib
                if contrib in NEEDS_VERDICT:
                    pid = vrec["canonical_proposition"]
                    clusters[pid].append(f"{family}:{item}:{aid}")
                    support = (vrec.get("effective") or {}).get(
                        "support_type", a.get("support_type"))
                    out["support_mix"][f"{prop}:{support}"] += 1
                    out["source_target_relation"][
                        f"{prop}:{a.get('source_target_observation_relation')}"] += 1
            # Coder units survive only for assertions with no verdict
            # (adjacent reporting); verdicted assertions already
            # contributed derived units above.
            for u in rec.get("units_valid", []):
                live = [eff[i] for i in u.get("assertion_ids", [])
                        if i in eff and i not in verdicted_ids]
                if not live:
                    continue
                ub = max(live, key=lambda c: STRENGTH[c])
                cur = unit_best.get(u["unit"])
                if cur is None or STRENGTH[ub] > STRENGTH[cur]:
                    unit_best[u["unit"]] = ub
        out["pair_level"][key] = best or "SILENCE"
        out["unit_level"][key] = unit_best
    out["clusters"] = {pid: sorted(m) for pid, m in
                       sorted(clusters.items())}
    out["support_mix"] = dict(out["support_mix"])
    out["source_target_relation"] = dict(out["source_target_relation"])
    out["unit_level"] = dict(out["unit_level"])
    return out


def summarize(final):
    by_prop = defaultdict(Counter)
    by_stratum = defaultdict(Counter)
    units_by_prop = defaultdict(Counter)
    for key, cls in final["pair_level"].items():
        prop, item = key.split("/")
        by_prop[prop][cls] += 1
        by_stratum[prop][f"{SAMPLE[item]}:{cls}"] += 1
    for key, units in final["unit_level"].items():
        prop = key.split("/")[0]
        for unit, cls in units.items():
            units_by_prop[prop][f"{unit} -> {cls}"] += 1
    return ({"pair_level_by_property": {k: dict(v) for k, v in by_prop.items()},
             "pair_level_by_stratum": {k: dict(v) for k, v in by_stratum.items()},
             "unit_level": {k: dict(v) for k, v in units_by_prop.items()}})


def main():
    with_weak = run(include_weak=True)
    strict = run(include_weak=False)
    final = {"including_pass_weak": {**summarize(with_weak),
                                     "pair_level": with_weak["pair_level"],
                                     "unit_detail": with_weak["unit_level"],
                                     "clusters": with_weak["clusters"],
                                     "support_mix": with_weak["support_mix"],
                                     "source_target_relation":
                                         with_weak["source_target_relation"]},
             "strict_pass_only": summarize(strict),
             "unreviewed": sorted(set(with_weak["unreviewed"]))}
    (BASE / "audit-final.json").write_text(json.dumps(final, indent=1))

    md = ["# Audit aggregates (generated by finalize_audit.py)\n"]
    for variant, data in (("Including pass-weak", final["including_pass_weak"]),
                          ("Strict pass only", final["strict_pass_only"])):
        md.append(f"\n## {variant}: pair-level availability (of 12 per property)\n")
        for prop, counts in data["pair_level_by_property"].items():
            row = ", ".join(f"{k} {counts.get(k, 0)}" for k in AVAIL
                            if counts.get(k, 0))
            md.append(f"- {prop}: {row}")
        md.append(f"\n## {variant}: unit-level availability\n")
        for prop, counts in data["unit_level"].items():
            md.append(f"### {prop}")
            for unit, n in sorted(counts.items()):
                md.append(f"- {unit}: {n} item(s)")
    md.append("\n## Canonical propositions behind ITEM-DIRECT / "
              "CLASS-INHERITED support (including pass-weak; "
              "proposition-map.json)\n")
    for ckey, members in sorted(final["including_pass_weak"]["clusters"].items()):
        md.append(f"- {ckey}\n  - {len(members)} assertion(s): "
                  + ", ".join(sorted(members)))
    md.append("\n## Support mix: " + json.dumps(
        final["including_pass_weak"]["support_mix"]))
    md.append("## Source-target relation: " + json.dumps(
        final["including_pass_weak"]["source_target_relation"]))
    if final["unreviewed"]:
        md.append("\n## UNREVIEWED assertions (excluded above)\n")
        md += [f"- {u}" for u in final["unreviewed"]]
    (BASE / "AUDIT-tables.md").write_text("\n".join(md) + "\n")
    print(json.dumps(final["including_pass_weak"]["pair_level_by_property"],
                     indent=1))
    print("clusters:", len(final["including_pass_weak"]["clusters"]),
          "| unreviewed:", len(final["unreviewed"]))


if __name__ == "__main__":
    main()
