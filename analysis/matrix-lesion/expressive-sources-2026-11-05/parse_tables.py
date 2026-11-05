"""Parse report tables (item | property | value | scope | "quote" | page | note) into TSV rows for check_quotes.py.

Handles an optional leading row-number column and "same as row N" back-references."""
import re, sys, csv
src, path = sys.argv[1], sys.argv[2]
w = csv.writer(sys.stdout, delimiter="\t")
w.writerow(["source", "item_id", "property", "value", "scope", "quote", "page", "note"])
byrow, last = {}, ""
for line in open(path, encoding="utf-8"):
    if " | " not in line or re.match(r"^\|?\s*-{3}", line) or ("item_id" in line and "quotation" in line.lower()):
        continue
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    rownum = None
    if cells and re.fullmatch(r"\d+", cells[0]):
        rownum = cells.pop(0)
    if len(cells) < 6:
        continue
    item, prop, val, scope, quote, page = cells[:6]
    note = cells[6] if len(cells) > 6 else ""
    m = re.match(r"same as row (\d+)", quote)
    if m:
        quote = byrow.get(m.group(1), "")
    elif re.match(r"\(?same quotation", quote):
        quote = last
    if rownum:
        byrow[rownum] = quote
    last = quote
    page1 = re.split(r"[;,–-]", page)[0]
    for q in re.findall(r'"([^"]+)"', quote) or [quote]:
        w.writerow([src, item, prop, val, scope, q, page1, note])
