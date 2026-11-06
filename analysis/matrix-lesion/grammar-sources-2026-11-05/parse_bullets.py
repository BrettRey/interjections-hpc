"""Parse bullet-style report rows into TSV for check_quotes_g.py:
- **ITEM** | property | value | scope
  - "quotation" (pieces may be joined with ...)
  - p. N (section; PDF n; lines)
  - note lines
"""
import csv, re, sys
src, path = sys.argv[1], sys.argv[2]
w = csv.writer(sys.stdout, delimiter="\t")
w.writerow(["source", "item_id", "property", "value", "scope", "quote", "page", "note"])
rows, cur = [], None
for line in open(path, encoding="utf-8"):
    m = re.match(r"^\s*- \*\*(.+?)\*\*\s*\|\s*(.*)$", line)
    if m:
        if cur: rows.append(cur)
        rest = [c.strip() for c in m.group(2).split("|")]
        cur = {"item": m.group(1), "rest": rest, "quote": None, "page": "", "note": []}
        continue
    if cur is None:
        continue
    s = line.strip()
    if not s.startswith("- "):
        if s.startswith("#") or s == "":
            if s.startswith("#"): rows.append(cur); cur = None
        continue
    s = s[2:]
    if cur["quote"] is None:
        cur["quote"] = s
    elif not cur["page"] and re.match(r"(Same quotation, )?pp?\. \d", s):
        cur["page"] = s
    else:
        cur["note"].append(s)
if cur: rows.append(cur)
last = ""
for r in rows:
    rest = r["rest"]
    if len(rest) >= 3:
        prop, val, scope = rest[0], rest[1], rest[2]
    else:  # "P01 Y (weak); P04 Y | item" shape
        prop, val, scope = rest[0], "", rest[-1]
    q = r["quote"] or ""
    qs = re.findall(r'"([^"]+)"', q)
    if q.startswith("Same quotation"):
        qs, r["page"] = [last], q
    if not qs:
        continue
    last = qs[0]
    pm = re.search(r"pp?\. (\d+)", r["page"] or q)
    for x in qs:
        w.writerow([src, r["item"], prop, val, scope, x, pm.group(1) if pm else "", " ".join(r["note"])[:400]])
