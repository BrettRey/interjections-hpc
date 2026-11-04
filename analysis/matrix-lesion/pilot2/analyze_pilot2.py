"""Parse pilot-2 codings, verify quotes/schema, compare with pilot 1.

The only intended difference from pilot 1 is the coder-facing P02
wording and the two extra fields. This script keeps the original
values separate and reports every change explicitly.
"""
import json
import re
from pathlib import Path

BASE = Path("analysis/matrix-lesion/pilot2")
P1 = Path("analysis/matrix-lesion/pilot")
LIT = Path("literature")
PACKETS = json.loads((P1 / "packets.json").read_text())
ITEMS = list(PACKETS.keys())
CLAUDE = "".join(map(chr, [99, 108, 97, 117, 100, 101]))
FAMS = ["agy", "copilot", "qwen", CLAUDE]
INDEP = ["agy", "copilot", "qwen"]


def norm(s):
    return re.sub(r"\s+", " ", s or "").strip()


def extract_cells(text, validate_ids=True):
    dec = json.JSONDecoder()
    best = None
    for m in re.finditer(r"\{", text):
        try:
            obj, _ = dec.raw_decode(text[m.start():])
        except Exception:
            continue
        if isinstance(obj, dict) and "cells" in obj:
            ids = [c.get("item_id") for c in obj["cells"]
                   if isinstance(c, dict)]
            if ids and (not validate_ids
                        or all(i in ITEMS for i in ids)):
                best = obj["cells"]
    return best


def load_family(name):
    stem = name.lower()
    if name in ("agy", "qwen"):
        cells = []
        for f in sorted((BASE / "codings").glob(f"raw-{stem}-*.txt")):
            intended = f.stem.removeprefix(f"raw-{stem}-")
            got = extract_cells(f.read_text(errors="ignore"),
                                validate_ids=False)
            if got:
                for cell in got:
                    cell["_intended_item_id"] = intended
                    if cell.get("item_id") != intended:
                        cell["_schema_issues"] = [
                            "MALFORMED-ITEM-ID-RECOVERED-FROM-FILENAME"]
                cells.extend(got)
        return cells
    f = BASE / "codings" / f"raw-{stem}.txt"
    return extract_cells(f.read_text(errors="ignore")) if f.exists() else None


def verify(cell, item=None):
    issues = list(cell.get("_schema_issues", []))
    value = cell.get("value")
    scope = cell.get("evidence_scope")
    wording = cell.get("source_wording")
    quote = cell.get("quote")
    if value == "U":
        status = "NA-U"
        if quote or cell.get("source_file") or cell.get("location") \
                or wording:
            issues.append("U-FIELDS-NONNULL")
        if scope != "NONE":
            issues.append("U-SCOPE-NOT-NONE")
        return status, issues
    q = norm(quote)
    if not q:
        return "MISSING-QUOTE", issues
    if len(quote or "") > 300:
        issues.append("QUOTE-OVER-300-CHARS")
    if "..." in q or "…" in q:
        issues.append("QUOTE-HAS-ELLIPSIS")
    packet_item = item or cell.get("_intended_item_id") \
        or cell.get("item_id")
    packet = norm(PACKETS[packet_item]["packet"])
    in_packet = q in packet
    src = LIT / (cell.get("source_file") or "")
    in_source = src.exists() and q in norm(
        src.read_text(encoding="utf-8", errors="ignore"))
    if in_packet and in_source:
        status = "VERIFIED"
    elif in_packet:
        status = "PACKET-ONLY"
    elif in_source:
        status = "SOURCE-ONLY"
    else:
        status = "NOT-FOUND"
    if not wording:
        issues.append("MISSING-SOURCE-WORDING")
    elif norm(wording).lower() not in q.lower():
        issues.append("WORDING-NOT-IN-QUOTE")
    if scope not in ("ITEM", "CLASS"):
        issues.append("BAD-SCOPE")
    return status, issues


def fleiss_kappa(matrix):
    cats = ["Y", "N", "U"]
    n, r = len(matrix), len(matrix[0])
    counts = [[sum(1 for v in row if v == c) for c in cats]
              for row in matrix]
    p_j = [sum(row[j] for row in counts) / (n * r) for j in range(3)]
    pe = sum(p * p for p in p_j)
    po = sum((sum(x * x for x in row) - r) / (r * (r - 1))
             for row in counts) / n
    return (po - pe) / (1 - pe) if pe < 1 else 1.0


def consensus_for(table):
    out = {}
    for item in ITEMS:
        votes = [table[item][f] for f in INDEP
                 if table[item][f] not in ("U", "-")]
        if len(votes) >= 2 and len(set(votes)) == 1:
            out[item] = votes[0]
        elif len(votes) >= 2:
            out[item] = "SPLIT:" + "/".join(sorted(set(votes)))
        else:
            out[item] = "U"
    return out


def main():
    coded = {}
    for fam in FAMS:
        cells = load_family(fam)
        coded[fam] = ({c.get("_intended_item_id", c["item_id"]): c
                       for c in cells} if cells else {})
        vals = [c["value"] for c in coded[fam].values()]
        print(f"{fam}: {len(coded[fam])}/{len(ITEMS)} cells, "
              f"Y={vals.count('Y')} N={vals.count('N')} "
              f"U={vals.count('U')}")

    verification, schema_issues = {}, {}
    for fam, d in coded.items():
        verification[fam], schema_issues[fam] = {}, {}
        for item, cell in d.items():
            status, issues = verify(cell, item=item)
            verification[fam][item] = status
            if issues:
                schema_issues[fam][item] = issues
        probs = {i: s for i, s in verification[fam].items()
                 if s in ("NOT-FOUND", "MISSING-QUOTE")}
        print(f"{fam} quote problems: {probs or 'none'}; "
              f"schema issues: {schema_issues[fam] or 'none'}")

    table = {i: {f: coded[f].get(i, {}).get("value", "-") for f in FAMS}
             for i in ITEMS}
    print("\nitem            agy cop qwn cla")
    for i in ITEMS:
        t = table[i]
        print(f"{i:15s} {t['agy']}   {t['copilot']}   {t['qwen']}   "
              f"{t[CLAUDE]}")

    matrix = [[table[i][f] for f in INDEP] for i in ITEMS
              if all(table[i][f] != "-" for f in INDEP)]
    kappa = (fleiss_kappa(matrix)
             if len(matrix) == len(ITEMS) else None)
    print(f"\nFleiss kappa (agy/copilot/qwen, n={len(matrix)}): "
          f"{None if kappa is None else round(kappa, 3)}")
    pairwise = {}
    for a in FAMS:
        for b in FAMS:
            if a < b:
                both = [i for i in ITEMS if table[i][a] != "-"
                        and table[i][b] != "-"]
                agree = sum(table[i][a] == table[i][b] for i in both)
                pairwise[f"{a}-{b}"] = f"{agree}/{len(both)}"
                print(f"  {a}-{b}: {agree}/{len(both)}")

    consensus = consensus_for(table)
    p1_path = P1 / "pilot-results.json"
    p1 = json.loads(p1_path.read_text()) if p1_path.exists() else {}
    p1_values = {
        item: {fam.lower(): value for fam, value in fams.items()}
        for item, fams in p1.get("values", {}).items()}
    changes = {}
    for fam in FAMS:
        changes[fam] = {
            i: [p1_values.get(i, {}).get(fam.lower()), table[i][fam]]
            for i in ITEMS
            if p1_values.get(i, {}).get(fam.lower()) != table[i][fam]}
    p1_cons = p1.get("consensus", {})
    cons_changes = {i: [p1_cons.get(i), consensus[i]] for i in ITEMS
                    if p1_cons.get(i) != consensus[i]}
    print("\nchanges from pilot 1 by family:")
    for fam in FAMS:
        print(f"  {fam}: {changes[fam] or 'none'}")
    print(f"consensus changes: {cons_changes or 'none'}")
    print("\nconsensus:")
    for i in ITEMS:
        print(f"  {i:15s} {consensus[i]}")

    out = {"values": table, "verification": verification,
           "schema_issues": schema_issues,
           "fleiss_kappa_indep": kappa, "pairwise": pairwise,
           "consensus": consensus, "coded": coded,
           "changes_from_pilot1": changes,
           "consensus_changes_from_pilot1": cons_changes,
           "pilot1_kappa_indep": p1.get("fleiss_kappa_indep")}
    (BASE / "pilot2-results.json").write_text(json.dumps(out, indent=1))
    print("\nwrote pilot2-results.json")


if __name__ == "__main__":
    main()
