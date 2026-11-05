"""Turn the verified report rows into one long table.

Each row of rows-<source>.tsv (from parse_tables.py, quotations checked by
check_quotes.py) becomes one or more long rows: bearer (or CLASS), column,
value, source, page, scope, hedge, quotation. Property labels from the four
reports are mapped to shared columns by the rules below; anything unmapped
is reported so the mapping can be extended by hand.
"""
import csv
import re
import sys

SOURCES = ["ljung2011", "potts2007", "mccready2010", "gutzmann2013"]
ABBR = {"ljung2011": "L", "potts2007": "P", "mccready2010": "M", "gutzmann2013": "G"}

# (regex on the property label, column). First match wins; a label can map
# to several columns when joined by ';' or '+' or '/'.
RULES = [
    (r"\bP01\b", "P01"), (r"\bP02\b", "P02"), (r"\bP03\b", "P03"), (r"\bP04\b", "P04"),
    (r"\bP05\b", "P05"), (r"\bP06\b", "P06"), (r"\bP07\b", "P07"), (r"\bP08\b", "P08"),
    (r"\bP09\b", "P09"), (r"\bP10S\b|repeatab", "P10S"), (r"\bP11N\b", "P11N"),
    (r"\bP12\b", "P12"), (r"\bP13\b", "P13"),
    (r"independence", "Potts:independence"),
    (r"nondisplac", "Potts:nondisplaceability"),
    (r"perspective", "Potts:perspective"),
    (r"ineffab", "Potts:ineffability"),
    (r"immediacy", "Potts:immediacy"),
    (r"NEW:(DEGREE|AMPLIFIER)\b", "degree modifier of adj/adv"),
    (r"NEW:GRADABLE_NOUN", "degree with gradable noun"),
    (r"NEW:(POST_WH|WH_SLOT)", "after wh-word"),
    (r"NEW:(INFIX|INSERTION)", "insertion into word/phrase"),
    (r"NEW:YOU_X", "You X! frame"),
    (r"NEW:PRE_NONNP", "emphasis before non-NP"),
    (r"NEW:(EMPHASIS|RETROACTIVE|BOOSTER)", "emphasis"),
    (r"NEW:TABOO", "taboo load"),
    (r"NEW:EXPRESSIVE_STRENGTH", "expressive strength"),
    (r"NEW:VALENCE", "valence shift"),
    (r"NEW:SCOPELESS", "scopeless (McCready)"),
    (r"NEW:DENIAL", "denial-immune"),
    (r"NEW:UNBINDABLE", "unbindable"),
    (r"NEW:EXPRESSIVE_MODIFIABLE", "modifiable by expressives"),
    (r"NEW:(SHUNTING|MAIN_CIE)", "main expressive content"),
    (r"NEW:COMBINES", "combines into formula"),
    (r"NEW:HOMONYM", "has homonym in other class"),
    (r"NEW:OPTATIVE", "optative verb form"),
    (r"NEW:INTERCHANGEABLE", "interchangeable swear word"),
    (r"NEW:CREATES_EPITHET", "creates epithet NP"),
    (r"NEW:STRESS_CUE", "stress cue"),
    (r"NEW:SLOT_FILLER", "slot filler (Ljung)"),
    (r"NEW:ADV_VS_ADJ", "host-class specialization"),
    (r"NEW:GRAMMATICALLY_REGULAR", "grammatically regular"),
    (r"NEW:NO_WORD_CLASS", "no word class"),
    (r"NEW:FORMULAIC", "formulaic"),
    (r"NEW:LOCAL_SCOPE", "local scope"),
    (r"NEW:FUNCTIONAL", "takes an argument (Gutzmann)"),
    (r"NEW:UCI_TYPE", "Gutzmann type"),
    (r"NEW:RESOURCE_SENSITIVE", "resource-sensitive"),
    (r"NEW:MULTIFUNCTIONAL", "multifunctional"),
    (r"NEW:ATTITUDE_TARGET", "attitude target"),
]
ITEMS = {r["item_id"] for r in csv.DictReader(open(sys.argv[1]))}

out = csv.writer(sys.stdout)
out.writerow(["bearer", "column", "value", "source", "page", "scope", "hedge", "label", "quote", "secondary"])
SEC = re.compile(r"secondary|cited from|quoting|reporting|reported|as reported|, quoted|\bfrom (Potts|Kaplan|Ameka|Quirk|Huddleston|Carter|Gehweiler|Stenstr)", re.I)
unmapped = []
for src in SOURCES:
    try:
        rows = list(csv.DictReader(open(f"{sys.argv[2]}/rows-{src}.tsv"), delimiter="\t"))
    except FileNotFoundError:
        continue
    last_quote = ""
    for r in rows:
        label, item = r["property"], r["item_id"]
        q = r["quote"]
        if q.startswith("(same quotation") or q.startswith("same quotation"):
            q = last_quote
        last_quote = q
        cols = []
        for part in re.split(r";|\+| / ", label):
            for rx, col in RULES:
                if re.search(rx, part, re.I):
                    cols.append(col)
                    break
        if not cols:
            unmapped.append((src, item, label))
            continue
        v = r["value"].strip()
        value = "Y" if re.match(r"Y\b", v, re.I) else "N" if re.match(r"N\b", v, re.I) else re.sub(r"\*", "", v)
        hedge = "hedged" if re.search(r"hedged|weak|approx|ambiguous|\?|nearest|or ", item + " " + v, re.I) else ""
        if item.upper().startswith("CLASS") or item.startswith("C") and "CLASS" in item:
            bearers, scope = [item], "class"
        else:
            ids = [b for b in re.findall(r"[A-Z][A-Z_]+", item) if b in ITEMS]
            if not ids or " or " in item:
                bearers, scope = [item], "other"
            else:
                bearers, scope = ids, "item"
        for b in bearers:
            for c in dict.fromkeys(cols):
                m = SEC.search(r.get("note", "") + " " + item)
                sec = (r.get("note", "")[:160] if m else "")
                out.writerow([b, c, value, ABBR[src], r["page"], scope, hedge, label, q, sec])
for u in unmapped:
    print("UNMAPPED", *u, file=sys.stderr)
