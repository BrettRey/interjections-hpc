"""Mechanical verification and availability aggregation for the
discarded target-evidence audit.

Checks every raw output: JSON parse, identifiers, schema fields and
controlled values, quote length and continuity against the pair's own
packet (exact, then whitespace-normalized), cited markdown line
present in the packet, unit -> assertion references.

Assertions failing any check are flagged and excluded from adjusted
counts. Pair availability is reported raw (as coded) and adjusted:
kept if a surviving assertion carries that contribution, else
downgraded to the strongest surviving contribution, else SILENCE
(unless the pair was coded INAPPLICABLE / RETRIEVAL-FAILURE-SUSPECTED
with no assertions, which is kept and flagged for human review).

Aggregation is availability and assertion structure ONLY. No
source-target association, assignment, or lesion is computed.
Outputs: audit-results.json, review-queue.md, stdout summary.
"""
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

BASE = Path("analysis/matrix-lesion/target-audit")
OUT = BASE / "codings"
PACKETS = json.loads((BASE / "packets-v3.json").read_text())
SCHEMA = json.loads((BASE / "assertion-schema.json").read_text())
SAMPLE = {}
for line in (BASE / "sample.csv").read_text().strip().splitlines()[1:]:
    item, stratum, _ = line.split(",", 2)
    SAMPLE[item] = stratum

PROPS = ("P10", "P11", "P12")
ITEMS = list(PACKETS["P10"])
AVAIL = ["ITEM-DIRECT", "CLASS-INHERITED", "CONFLICT", "ADJACENT-ONLY",
         "RETRIEVAL-FAILURE-SUSPECTED", "INAPPLICABLE", "SILENCE"]
STRENGTH = {a: len(AVAIL) - i for i, a in enumerate(AVAIL)}
REQUIRED = SCHEMA["required"]
ALLOWED = set(SCHEMA["properties"])
ENUMS = {k: v.get("enum") for k, v in SCHEMA["properties"].items()
         if "enum" in v}
FAMILIES = ["agy", "copilot", "qwen", "claude"]


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def norm_id(s):
    return re.sub(r"[^A-Za-z0-9]", "", str(s)).upper()


PACKET_NORM = {(p, i): norm(PACKETS[p][i]["packet"])
               for p in PROPS for i in ITEMS}
PACKET_FOLD = {(p, i): norm(PACKETS[p][i]["packet"]).casefold()
               for p in PROPS for i in ITEMS}
PACKET_RAW = {(p, i): PACKETS[p][i]["packet"] for p in PROPS for i in ITEMS}


def extract_json(text):
    text = text.split("\n[STDERR]")[0]
    text = re.sub(r"```(?:json)?", "", text)
    start = text.find("{")
    if start < 0:
        return None, "no JSON object found"
    try:
        obj, _ = json.JSONDecoder().raw_decode(text[start:])
        return obj, None
    except json.JSONDecodeError as e:
        return None, f"JSON decode error: {e}"


def load_family(family):
    """Return {(prop,item): pair-dict or {'_error': ...}}."""
    pairs = {}
    if family == "claude":
        for prop in PROPS:
            path = OUT / f"raw-claude-{prop}.txt"
            if not path.exists():
                for item in ITEMS:
                    pairs[(prop, item)] = {"_error": "file missing"}
                continue
            obj, err = extract_json(path.read_text())
            if err:
                for item in ITEMS:
                    pairs[(prop, item)] = {"_error": err}
                continue
            seen = set()
            for entry in obj.get("pairs", []):
                pair = entry.get("pair", entry)
                item = pair.get("item_id", "")
                pairs[(prop, item)] = pair
                seen.add(item)
            for item in ITEMS:
                if item not in seen:
                    pairs[(prop, item)] = {"_error": "pair absent"}
        return pairs
    for prop in PROPS:
        for item in ITEMS:
            path = OUT / f"raw-{family}-{prop}-{item}.txt"
            if not path.exists():
                pairs[(prop, item)] = {"_error": "file missing"}
                continue
            obj, err = extract_json(path.read_text())
            if err:
                pairs[(prop, item)] = {"_error": err}
                continue
            pairs[(prop, item)] = obj.get("pair", obj)
    return pairs


def check_assertion(a, prop, item):
    """Return defect strings. Entries prefixed MINOR: are recorded but
    mechanically recoverable without interpretation (item_id uniquely
    denoting the pair item after case/punctuation normalization, a
    quote matching only after case folding, an unlocatable cited line
    when the quote verifies). All other defects void the assertion.
    An ambiguous bare form (e.g. 'damn' for DAMN_PRENOM) stays fatal."""
    defects = []
    if not isinstance(a, dict):
        return ["assertion not an object"]
    for field in REQUIRED:
        if field not in a:
            defects.append(f"missing field {field}")
    extra = set(a) - ALLOWED
    if extra:
        defects.append(f"extra fields {sorted(extra)}")
    if a.get("item_id") != item:
        if norm_id(a.get("item_id", "")) == norm_id(item):
            defects.append(
                f"MINOR: item_id {a.get('item_id')!r} normalized to {item!r}")
        else:
            defects.append(f"item_id {a.get('item_id')!r} != {item!r}")
    if a.get("property_id") != prop:
        defects.append(f"property_id {a.get('property_id')!r} != {prop!r}")
    for field, enum in ENUMS.items():
        if field in a and a[field] not in enum:
            defects.append(f"{field} value {a[field]!r} not in enum")
    loc = a.get("location") or {}
    line = loc.get("markdown_line")
    if not isinstance(line, int):
        defects.append("MINOR: markdown_line not an integer")
    elif f"line~{line}" not in PACKET_RAW[(prop, item)] \
            and str(line) not in PACKET_RAW[(prop, item)]:
        defects.append(f"MINOR: markdown_line {line} not found in packet")
    spans = a.get("spans") or []
    if a.get("availability_contribution") not in ("SILENCE",) and not spans:
        defects.append("no spans for a non-SILENCE assertion")
    for s in spans:
        q = s.get("quote", "")
        if s.get("role") not in ("target-behaviour", "class-inclusion",
                                 "use-identification", "environment",
                                 "counterevidence"):
            defects.append(f"bad span role {s.get('role')!r}")
        if len(q) > 300:
            defects.append(f"quote over 300 chars ({len(q)})")
        if "..." in q or "\u2026" in q:
            defects.append("ellipsis inside quote")
        if q and q not in PACKET_RAW[(prop, item)] \
                and norm(q) not in PACKET_NORM[(prop, item)]:
            if norm(q).casefold() in PACKET_FOLD[(prop, item)]:
                defects.append(
                    "MINOR: quote matches packet only after case folding")
            else:
                defects.append("quote not a continuous substring of packet")
    # property-specific controlled fields
    if prop == "P10" and a.get("availability_contribution") != "SILENCE":
        if a.get("repetition_pattern") in (None, "not-applicable"):
            defects.append("P10 assertion without repetition_pattern")
    if prop == "P11" and a.get("availability_contribution") != "SILENCE":
        if a.get("contribution_assessed") in (None, "not-applicable"):
            defects.append("P11 assertion without contribution_assessed")
        if a.get("host_relationship") in (None, "not-applicable"):
            defects.append("P11 assertion without host_relationship")
    return defects


def adjusted_pair_availability(pair, valid_assertions):
    raw = pair.get("pair_availability")
    contribs = [a["availability_contribution"] for a in valid_assertions
                if a.get("availability_contribution") != "SILENCE"]
    if raw in ("INAPPLICABLE", "RETRIEVAL-FAILURE-SUSPECTED") \
            and not pair.get("assertions"):
        return raw
    if raw == "SILENCE" and not contribs:
        return "SILENCE"
    if raw in contribs:
        return raw
    if contribs:
        return max(contribs, key=lambda c: STRENGTH.get(c, 0))
    return "SILENCE"


def main():
    results = {"families": {}, "defects": [], "pairs": {}}
    review = []
    for family in FAMILIES:
        pairs = load_family(family)
        fam = {"raw_availability": Counter(), "adjusted_availability": Counter(),
               "assertions_raw": 0, "assertions_valid": 0,
               "assertions_valid_strict": 0, "errors": 0}
        for (prop, item), pair in sorted(pairs.items()):
            key = f"{prop}/{item}"
            results["pairs"].setdefault(key, {})[family] = {}
            rec = results["pairs"][key][family]
            if "_error" in pair:
                rec["error"] = pair["_error"]
                fam["errors"] += 1
                continue
            raw_avail = pair.get("pair_availability")
            rec["raw_availability"] = raw_avail
            fam["raw_availability"][f"{prop}:{raw_avail}"] += 1
            assertions = pair.get("assertions") or []
            valid, invalid = [], []
            for a in assertions:
                fam["assertions_raw"] += 1
                defects = check_assertion(a, prop, item)
                fatal = [d for d in defects if not d.startswith("MINOR:")]
                for d in defects:
                    results["defects"].append(
                        {"family": family, "pair": key,
                         "assertion_id": a.get("assertion_id"),
                         "severity": "minor" if d.startswith("MINOR:")
                         else "fatal",
                         "defect": d})
                if fatal:
                    invalid.append({"assertion_id": a.get("assertion_id"),
                                    "defects": defects})
                else:
                    valid.append(a)
                    fam["assertions_valid"] += 1
                    if not defects:
                        fam["assertions_valid_strict"] += 1
            if raw_avail == "SILENCE" and assertions:
                results["defects"].append(
                    {"family": family, "pair": key, "assertion_id": None,
                     "severity": "fatal",
                     "defect": "SILENCE pair carrying assertions"})
            adj = adjusted_pair_availability(pair, valid)
            rec["adjusted_availability"] = adj
            fam["adjusted_availability"][f"{prop}:{adj}"] += 1
            rec["n_assertions"] = len(assertions)
            rec["n_valid"] = len(valid)
            rec["invalid"] = invalid
            # units referencing only valid assertions
            valid_ids = {a.get("assertion_id") for a in valid}
            units = []
            for u in pair.get("units") or []:
                ids = [i for i in u.get("assertion_ids", []) if i in valid_ids]
                if ids:
                    units.append({"unit": u.get("unit"),
                                  "availability": u.get("availability"),
                                  "assertion_ids": ids})
            rec["units_valid"] = units
            rec["valid_assertions"] = valid
            for a in valid:
                if a.get("availability_contribution") in (
                        "ITEM-DIRECT", "CLASS-INHERITED", "CONFLICT"):
                    review.append((prop, item, family, a))
        results["families"][family] = {
            k: (dict(v) if isinstance(v, Counter) else v)
            for k, v in fam.items()}

    # audit-level pair availability: strongest adjusted class any family
    # supports with mechanically valid assertions (semantic check pending)
    audit_level = Counter()
    unit_counts = defaultdict(Counter)
    for key, by_fam in results["pairs"].items():
        prop, item = key.split("/")
        classes = [r.get("adjusted_availability") for r in by_fam.values()
                   if r.get("adjusted_availability")]
        best = max(classes, key=lambda c: STRENGTH.get(c, 0)) if classes \
            else "NO-DATA"
        results["pairs"][key]["audit_level_pre_semantic"] = best
        audit_level[f"{prop}:{best}"] += 1
        audit_level[f"{prop}:{SAMPLE.get(item)}:{best}"] += 1
        for r in by_fam.values():
            if not isinstance(r, dict):
                continue
            for u in r.get("units_valid", []):
                unit_counts[prop][u["unit"]] += 1
    results["audit_level_pre_semantic"] = dict(audit_level)
    results["unit_mentions_valid"] = {k: dict(v) for k, v in unit_counts.items()}

    # pairwise agreement on raw pair availability, with marginals
    agree = {}
    for i, f1 in enumerate(FAMILIES):
        for f2 in FAMILIES[i + 1:]:
            same = total = 0
            for by_fam in results["pairs"].values():
                a = by_fam.get(f1, {}).get("raw_availability")
                b = by_fam.get(f2, {}).get("raw_availability")
                if a and b:
                    total += 1
                    same += a == b
            agree[f"{f1} vs {f2}"] = {"agree": same, "of": total}
    results["pairwise_raw_agreement"] = agree

    (BASE / "audit-results.json").write_text(json.dumps(results, indent=1))

    # semantic review queue: every mechanically valid ITEM-DIRECT /
    # CLASS-INHERITED / CONFLICT assertion, deduplicated by quote
    lines = ["# Semantic review queue (mechanically valid assertions)\n",
             "Check: correct language/variety, specified use, correct "
             "environment, claim strength preserved, quote actually "
             "supports the coded contribution.\n"]
    seen = set()
    for prop, item, family, a in sorted(review, key=lambda t: t[:3]):
        quotes = tuple(s["quote"] for s in a.get("spans", []))
        dedupe = (prop, item, quotes)
        tag = "" if dedupe not in seen else " [same quotes as earlier entry]"
        seen.add(dedupe)
        lines.append(f"\n## {prop} / {item} / {family} / "
                     f"{a.get('assertion_id')}{tag}")
        lines.append(f"- contribution: {a.get('availability_contribution')}; "
                     f"support: {a.get('support_type')}; "
                     f"class: {a.get('inherited_class')}; "
                     f"strength: {a.get('supported_claim_strength')}; "
                     f"quantifier: {a.get('quantifier_modality')}; "
                     f"language: {a.get('language_variety')}")
        lines.append(f"- value: {a.get('supported_value')}; "
                     f"use: {a.get('use_slice')}; "
                     f"env: {a.get('construction_environment')}; "
                     f"pattern: {a.get('repetition_pattern')}; "
                     f"contribution_assessed: {a.get('contribution_assessed')}; "
                     f"host: {a.get('host_relationship')}; "
                     f"source-target: {a.get('source_target_observation_relation')}; "
                     f"also-assignment: {a.get('also_carries_assignment_evidence')}")
        lines.append(f"- source: {a.get('source_file')} "
                     f"line {(a.get('location') or {}).get('markdown_line')}")
        for s in a.get("spans", []):
            lines.append(f"  - [{s['role']}] \"{s['quote']}\"")
        lines.append(f"- rationale: {a.get('rationale')}")
    (BASE / "review-queue.md").write_text("\n".join(lines) + "\n")

    print(json.dumps(results["families"], indent=1))
    print("AUDIT-LEVEL (pre-semantic):",
          json.dumps(results["audit_level_pre_semantic"], indent=1))
    print("PAIRWISE RAW AGREEMENT:", json.dumps(agree, indent=1))
    print("defects:", len(results["defects"]),
          "| review-queue assertions:", len(review))


if __name__ == "__main__":
    main()
