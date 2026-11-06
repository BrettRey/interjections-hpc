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

SOURCES = ["ljung2011", "potts2007", "mccready2010", "gutzmann2013", "wiktionary",
           "cgel2002", "quirk1985", "sie2005", "biber1999", "biber2021", "coca"]
ABBR = {"ljung2011": "L", "potts2007": "P", "mccready2010": "M", "gutzmann2013": "G", "wiktionary": "W",
        "cgel2002": "H", "quirk1985": "Q", "sie2005": "S", "biber1999": "B", "biber2021": "R", "coca": "C"}

# Repetition patterns for the P10 columns (decision call 2, Brett: "yes", 2026-11-05):
# adjacent; recurring with other material between, where each token meets a separate
# event, or all meet one event; "recurring" where the event distinction doesn't apply
# (a particle on successive clauses). Keyed (bearer, source letter, page); QPATTERN
# disambiguates two rows from one block by the start of the quotation.
P10_PATTERN = {
    ("DAMN_PRENOM", "P", "182"): "recurring: one event", ("CLASS:expressives", "P", "189"): "recurring: one event",
    ("OUCH", "G", "47"): "recurring: one event", ("OOPS", "G", "47"): "recurring: one event",
    ("CLASS:isolated UCIs", "G", "47"): "recurring: one event",
    ("DAMN_PRENOM", "G", "46"): "recurring: one event", ("DAMN_REACT", "G", "46"): "recurring: one event",
    ("VERY_INTENS", "G", "46"): "adjacent", ("TUTTUT", "W", "v1 W:tut:Interjection:1"): "adjacent",
    ("LAH", "W", "v1 W:lah:Particle:15"): "recurring", ("ALAS", "W", "W:alas:E1:Interjection:1"): "adjacent",
    ("BLOODY_PRENOM", "W", "W:bloody:E1:Adjective:3"): "recurring: one event",
    ("FUCKING_PRENOM", "W", "W:fucking:E1:Adjective:2"): "recurring: one event",
    ("VERY_INTENS", "W", "W:very:E1:Usage notes:0"): "adjacent", ("VERY_INTENS", "H", "585"): "adjacent",
    ("VERY_INTENS", "Q", "473"): "adjacent", ("CLASS:attributive adjectives and degree intensifiers", "Q", "981"): "adjacent",
    ("VERY_INTENS", "B", "1093"): "adjacent", ("VERY_INTENS", "R", "1088"): "adjacent",
    ("OOPS", "B", "1084"): "adjacent", ("OOPS", "R", "1079"): "adjacent",
    ("TUTTUT", "B", "1085"): "adjacent", ("TUTTUT", "R", "1079"): "adjacent",
    ("BYE", "B", "1086"): "adjacent", ("HEY", "R", "1050"): "adjacent",
}
P10_QPATTERN = {("BANG_DEPICT", "W", "Bang, bang"): "adjacent", ("BANG_DEPICT", "W", "Bang! Away"): "recurring: separate events"}
# Gutzmann 2013 p. 47 marks recurrence odd (#); in the recode that is P10A (availability), not P10S.
P10_RECODE = {("OUCH", "G", "47", "P10S"): "P10A", ("OOPS", "G", "47", "P10S"): "P10A",
              ("CLASS:isolated UCIs", "G", "47", "P10S"): "P10A"}
P10_NOTE = {("OUCH", "G", "47"): "N rests on # (infelicity) on a constructed example; COCA attests the pattern (source C)",
            ("OOPS", "G", "47"): "N rests on # (infelicity) on a constructed example; COCA attests the pattern (source C)",
            ("CLASS:isolated UCIs", "G", "47"): "scoped to the pattern tested in (104); COCA attests it for ouch and oops, and attests adjacent repetition for both"}

# (regex on the property label, column). First match wins; a label can map
# to several columns when joined by ';' or '+' or '/'.
RULES = [
    (r"NEW:TAKES_MODIFIER", "takes a modifier"), (r"NEW:PRO_ONE", "pro-form one"),
    (r"NEW:LY_ADVERB", "has ·ly adverb"), (r"NEW:RESTRICTED_HOSTS", "restricted hosts"),
    (r"NEW:CLAUSE_MEDIAL", "clause-medial position"), (r"NEW:IN_SITU", "wh-phrase in situ"),
    (r"NEW:PRE_WH", "before wh-word"), (r"NEW:WH_ALONE", "wh-phrase alone"),
    (r"NEW:CLITIC_HOST", "hosts a clitic"), (r"NEW:LENGTHENING", "lengthening, wide pitch range"),
    (r"NEW:FIXED_FORM", "fixed form"), (r"NEW:IMPERATIVE_POTENTIAL", "imperative potential"),
    (r"NEW:SYNDETIC_REPEAT", "repeated with and"), (r"NEW:SPREADS", "recurs at several points"),
    (r"NEW:PHONETIC_MOD", "phonetically modified variants"),
    (r"NEW:IN_STANDALONE_PHRASE", "modifier inside a standalone phrase"),
    (r"\bP07D\b", "P07D"), (r"\bP11E\b", "P11E"), (r"\bP12S\b", "P12S"), (r"\bP12I\b", "P12I"),
    (r"\bP10A\b", "P10A"), (r"\bP10R\b", "P10R"), (r"HISTORICAL_SOURCE", "historical source"),
    (r"NEW:(NOT_)?COMPARAB|COMPARABILITY", "comparable"), (r"NEW:ATTRIBUTIVE", "attributive"),
    (r"NEW:PREDICATIVE", "predicative"), (r"NEW:UTTERANCE_SCOPE", "utterance scope"),
    (r"NEW:VERB_MODIFIER", "modifies verbs"), (r"NEW:USE_DESCRIPTION_GLOSS", "glossed by its use"),
    (r"NEW:DELOCUTIVE_NOUN", "delocutive noun"), (r"NEW:DELOCUTIVE_VERB", "delocutive verb"),
    (r"NEW:INTONATION_SPECIFIED", "intonation specified"), (r"NEW:LEXICAL_TONE", "lexical tone"),
    (r"NEW:STRESS_SHIFT", "stress tied to use"), (r"NEW:HOST_STRESS", "host-stress conditioned"),
    (r"NEW:PRE_STRESS", "placed before stress"), (r"NEW:ETYM_NATURAL", "imitative or natural origin"),
    (r"NEW:CONATIVE", "conative"), (r"NEW:IRONIC", "ironic use"), (r"NEW:NONLITERAL", "nonliteral"),
    (r"NEW:CLAUSAL_FORM", "clausal form"), (r"NEW:TRANSITIVE", "transitive"), (r"NEW:CATENATIVE", "catenative"),
    (r"NEW:NONCOUNT", "non-count"), (r"NEW:COUNT", "count"), (r"NEW:FROZEN_PLURAL", "frozen plural"),
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
out.writerow(["bearer", "column", "value", "source", "page", "scope", "hedge", "label", "quote", "secondary", "basis"])
# Per-entry judgements of Wiktionary rows scoped to a page, headword or sense (adjudicate_scope.py).
IPA_LINES = {}  # Wiktionary pronunciation block id -> number of IPA lines (for P13D)
for d in sys.argv[2:]:
    try:
        blk = None
        for line in open(f"{d}/wiktionary-senses-v2.txt", encoding="utf-8"):
            if line.startswith("=== W:"):
                blk = line.split(" ===")[0][4:]
                IPA_LINES.setdefault(blk, 0)
            elif blk and "IPA(key)" in line:
                IPA_LINES[blk] += 1
    except FileNotFoundError:
        pass
# Ljung 2011 pp. 76-77, "phonologically regular forms like Ah!, Aha!, Mm!, Oh!, Ouch! and Wow!", is
# Ljung's own sentence: Quirk et al. 1985 section 2.58 Note, which Ljung cites for "quasi-linguistic
# noises", doesn't say it (checked 2026-11-05). So the row isn't secondary.
NOT_SECONDARY = {("ljung2011", "AH; AHA; OH; OUCH; WOW", "P13")}
ADJ = {}
for d in sys.argv[2:]:
    try:
        for a in csv.DictReader(open(f"{d}/scope-adjudication.tsv"), delimiter="\t"):
            ADJ[(a["bearer"], a["column"], a["page"])] = (a["verdict"], a["reason"])
    except FileNotFoundError:
        pass
SEC = re.compile(r"secondary|cited from|quoting|reporting|reported|as reported|, quoted|\bfrom (Potts|Kaplan|Ameka|Quirk|Huddleston|Carter|Gehweiler|Stenstr)", re.I)
unmapped = []
for src in SOURCES:
    rows = None
    for d in sys.argv[2:]:  # normalized grammar rows (norm-*.tsv) take precedence
        for name in (f"norm-{src}.tsv", f"rows-{src}.tsv"):
            try:
                rows = list(csv.DictReader(open(f"{d}/{name}"), delimiter="\t"))
                break
            except FileNotFoundError:
                pass
        if rows is not None:
            break
    if rows is None:
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
        hm = re.search(r"\(hedged: (.+)\)\s*$", v)
        hedge = hm.group(1) if hm else "hedged" if re.search(r"hedged|weak|approx|ambiguous|\?|nearest|or ", item + " " + v, re.I) else ""
        # Keep the source row's own qualifications (fixes 2026-11-05, after the GPT-Pro review):
        # a row scoped to a page, headword or sense is not evidence about the specified use, and
        # a value the report qualifies ("N (one token)", "mixed evidence") is not a plain value.
        sc_in, note = (r.get("scope") or "").strip(), (r.get("note") or "").strip()
        scoped = sc_in.startswith("page") or (sc_in.startswith("item") and sc_in != "item")
        scope_q = (f"source row scoped '{sc_in}', not to the specified use" + (f": {note[:240]}" if note else "")) if scoped else ""
        value_q = (f"the source report qualifies the value as '{v}'" + (f": {note[:240]}" if note and not scoped else "")
                   if re.search(r"one token|mixed evidence", v + " " + note, re.I) else "")
        base = (hedge if hedge not in ("", "hedged") else
                "Use match uncertain or evidence weak in the source report" if hedge == "hedged" else "")
        def combine(*parts):
            return "; ".join(p for p in parts if p)
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
                sec = (r.get("note", "")[:160] if m and (src, item, label) not in NOT_SECONDARY else "")
                h, sc, basis = combine(base, scope_q, value_q), scope, ""
                if c in ("P10S", "P10A", "P10R", "P10M"):
                    k = (b, ABBR[src], r["page"])
                    c = P10_RECODE.get(k + (c,), c)
                    pat = (r.get("pattern") or next((pp for (bb, ss, qp), pp in P10_QPATTERN.items()
                                                     if bb == b and ss == ABBR[src] and q.startswith(qp)), None)
                           or P10_PATTERN.get(k, "pattern unrecorded"))
                    c = f"{c} · {pat}"
                    h = combine(h, P10_NOTE.get(k, ""))
                base_c = c.split(" · ")[0]
                if scoped and (b, base_c, r["page"]) in ADJ:
                    verdict, why = ADJ[(b, base_c, r["page"])]
                    if verdict == "DUP":
                        continue
                    basis = f"{verdict}: {why}"
                    if verdict in ("USE", "WORD"):
                        h = combine(base, value_q)
                    elif verdict == "PRON":
                        # decision call 3 (D): an ordinary pronunciation is P13D, not P13 = N
                        blk = r["page"].replace("v1 ", "")
                        c, value, h = "P13D", "Y", combine(value_q)
                        basis = f"PRON: {why}; the block has {IPA_LINES.get(blk, '?')} IPA line(s)"
                    elif verdict == "ROUTE":
                        h = combine(base, why, value_q)
                    elif verdict == "OTHER_USE":
                        sc = "other-use"
                elif scoped and scope == "item":
                    basis = "UNJUDGED"
                out.writerow([b, c, value, ABBR[src], r["page"], sc, h, label, q, sec, basis])
for u in unmapped:
    print("UNMAPPED", *u, file=sys.stderr)
