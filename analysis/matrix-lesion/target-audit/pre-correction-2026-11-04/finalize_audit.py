"""Stage 2 of the discarded target-evidence audit.

Applies human semantic verdicts (semantic-verdicts.json) to the
mechanically verified results (audit-results.json, produced by
analyze_audit.py) and aggregates AVAILABILITY ONLY: pair-level and
unit-level evidence classes, assertion/proposition structure,
item-specific vs inherited support, stratum breakdowns, family
agreement. No source-target association, assignment, or lesion.

Assertion-level semantic outcomes:
- reject   -> assertion void
- downgrade-> contribution becomes ADJACENT-ONLY
- pass-weak-> kept, flagged (reported both included and excluded)
- pass / no verdict needed (ADJACENT-ONLY assertions) -> kept
Any ITEM-DIRECT/CLASS-INHERITED/CONFLICT assertion lacking a verdict
is listed as UNREVIEWED and excluded from post-semantic counts.

Outputs audit-final.json and AUDIT-tables.md; prints a summary.
"""
import json
import re
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


def norm(s):
    return re.sub(r"\s+", " ", str(s)).strip().casefold()


def assertion_outcome(family, prop, item, a, include_weak):
    """Return (effective_contribution or None if void, verdict_label)."""
    contrib = a.get("availability_contribution")
    key = f"{family}|{prop}|{item}|{a.get('assertion_id')}"
    rec = VERDICTS.get(key, {})
    v = rec.get("verdict")
    if contrib in NEEDS_VERDICT and v is None:
        return None, "UNREVIEWED"
    if v == "reject":
        return None, "reject"
    if v == "downgrade":
        return "ADJACENT-ONLY", "downgrade"
    if v == "pass-weak" and not include_weak:
        return None, "pass-weak-excluded"
    # A verdict may correct an overclaimed contribution class (e.g.
    # ITEM-DIRECT coded on class-level evidence) without voiding it.
    return rec.get("effective_contribution", contrib), v or "pass"


def cluster_key(a):
    quotes = sorted(norm(s.get("quote", "")) for s in a.get("spans", [])
                    if s.get("role") in ("target-behaviour",
                                         "counterevidence"))
    return (norm(a.get("source_file", "")), tuple(quotes)[:1])


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
            for a in rec["valid_assertions"]:
                contrib, label = assertion_outcome(
                    family, prop, item, a, include_weak)
                if label == "UNREVIEWED":
                    out["unreviewed"].append(
                        f"{family}|{key}|{a.get('assertion_id')}")
                if contrib is None or contrib == "SILENCE":
                    continue
                eff[a.get("assertion_id")] = contrib
                if best is None or STRENGTH[contrib] > STRENGTH[best]:
                    best = contrib
                if contrib in NEEDS_VERDICT:
                    clusters[(prop, cluster_key(a))].append(
                        f"{family}:{item}:{a.get('assertion_id')}")
                    out["support_mix"][
                        f"{prop}:{a.get('support_type')}"] += 1
                    out["source_target_relation"][
                        f"{prop}:{a.get('source_target_observation_relation')}"] += 1
            for u in rec.get("units_valid", []):
                live = [eff[i] for i in u.get("assertion_ids", []) if i in eff]
                if not live:
                    continue
                ub = max(live, key=lambda c: STRENGTH[c])
                cur = unit_best.get(u["unit"])
                if cur is None or STRENGTH[ub] > STRENGTH[cur]:
                    unit_best[u["unit"]] = ub
        out["pair_level"][key] = best or "SILENCE"
        out["unit_level"][key] = unit_best
    out["clusters"] = {
        f"{prop}|{src}|{q[0][:80] if q else ''}": members
        for (prop, (src, q)), members in clusters.items()}
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
    md.append("\n## Distinct proposition clusters behind ITEM-DIRECT / "
              "CLASS-INHERITED support (including pass-weak)\n")
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
