"""Parse pilot codings, verify quotes, compute agreement.

Quote verification is exact after whitespace normalization, against
(a) the item's packet and (b) the full cited source file. Results go
to pilot-results.json; the human report is PILOT.md.
"""
import json
import re
from pathlib import Path

BASE = Path("analysis/matrix-lesion/pilot")
LIT = Path("literature")
PACKETS = json.loads((BASE / "packets.json").read_text())
ITEMS = list(PACKETS.keys())


def norm(s):
    return re.sub(r"\s+", " ", s or "").strip()


def extract_cells(text):
    """Find the last parseable {"cells": [...]} object in raw text."""
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
            if ids and all(i in ITEMS for i in ids):
                best = obj["cells"]
    return best


def load_family(name):
    stem = name.lower()
    if name in ("agy", "qwen"):
        cells = []
        for f in sorted((BASE / "codings").glob(f"raw-{stem}-*.txt")):
            got = extract_cells(f.read_text(errors="ignore"))
            if got:
                cells.extend(got)
        return cells
    f = BASE / "codings" / f"raw-{stem}.txt"
    return extract_cells(f.read_text(errors="ignore")) if f.exists() else None


def verify(cell):
    if cell.get("value") == "U":
        return "NA-U" if not cell.get("quote") else "U-WITH-QUOTE"
    q = norm(cell.get("quote"))
    if not q:
        return "MISSING-QUOTE"
    packet = norm(PACKETS[cell["item_id"]]["packet"])
    in_packet = q in packet
    src = LIT / (cell.get("source_file") or "")
    in_source = src.exists() and q in norm(
        src.read_text(encoding="utf-8", errors="ignore"))
    if in_packet and in_source:
        return "VERIFIED"
    if in_packet:
        return "PACKET-ONLY"
    if in_source:
        return "SOURCE-ONLY"
    return "NOT-FOUND"


def fleiss_kappa(matrix):
    """matrix: items x raters values from a fixed category set."""
    cats = ["Y", "N", "U"]
    n = len(matrix)
    r = len(matrix[0])
    counts = [[sum(1 for v in row if v == c) for c in cats]
              for row in matrix]
    p_j = [sum(row[j] for row in counts) / (n * r) for j in range(3)]
    pe = sum(p * p for p in p_j)
    po = 0.0
    for row in counts:
        po += (sum(x * x for x in row) - r) / (r * (r - 1))
    po /= n
    return (po - pe) / (1 - pe) if pe < 1 else 1.0


def main():
    fams = ["agy", "copilot", "qwen", "Claude"]
    coded = {}
    for fam in fams:
        cells = load_family(fam)
        if cells is None:
            print(f"{fam}: NO PARSEABLE CELLS")
            coded[fam] = {}
            continue
        d = {}
        for c in cells:
            d[c["item_id"]] = c
        coded[fam] = d
        vals = [d[i]["value"] for i in ITEMS if i in d]
        print(f"{fam}: {len(d)}/{len(ITEMS)} cells, "
              f"Y={vals.count('Y')} N={vals.count('N')} "
              f"U={vals.count('U')}")

    verif = {fam: {i: verify(d[i]) for i in d} for fam, d in coded.items()}
    for fam in fams:
        bad = {i: s for i, s in verif[fam].items()
               if s in ("NOT-FOUND", "MISSING-QUOTE", "U-WITH-QUOTE")}
        print(f"{fam} quote problems: {bad or 'none'}")

    table = {}
    for i in ITEMS:
        table[i] = {fam: (coded[fam].get(i, {}).get("value", "-"))
                    for fam in fams}
    print("\nitem            agy cop qwn cla")
    for i in ITEMS:
        t = table[i]
        print(f"{i:15s} {t['agy']}   {t['copilot']}   {t['qwen']}   "
              f"{t['Claude']}")

    indep = ["agy", "copilot", "qwen"]
    matrix = [[table[i][f] for f in indep] for i in ITEMS
              if all(table[i][f] != "-" for f in indep)]
    kappa = fleiss_kappa(matrix) if len(matrix) == len(ITEMS) else None
    print(f"\nFleiss kappa (agy/copilot/qwen, n={len(matrix)}): "
          f"{kappa if kappa is None else round(kappa, 3)}")

    for a in fams:
        for b in fams:
            if a < b:
                both = [i for i in ITEMS if table[i][a] != "-"
                        and table[i][b] != "-"]
                agree = sum(1 for i in both if table[i][a] == table[i][b])
                print(f"  {a}-{b}: {agree}/{len(both)}")

    consensus = {}
    for i in ITEMS:
        votes = [table[i][f] for f in indep
                 if table[i][f] not in ("U", "-")]
        if len(votes) >= 2 and len(set(votes)) == 1:
            consensus[i] = votes[0]
        elif len(votes) >= 2:
            consensus[i] = "SPLIT:" + "/".join(sorted(set(votes)))
        else:
            consensus[i] = "U"
    print("\nconsensus (3 independent, majority of non-U, need >=2):")
    for i in ITEMS:
        print(f"  {i:15s} {consensus[i]}")

    out = {"values": table, "verification": verif,
           "fleiss_kappa_indep": kappa, "consensus": consensus,
           "coded": coded}
    (BASE / "pilot-results.json").write_text(json.dumps(out, indent=1))
    print("\nwrote pilot-results.json")


if __name__ == "__main__":
    main()
