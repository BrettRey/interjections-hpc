"""Fetch the English Wiktionary entries for the items-v4 bearers and write a
cleaned, sense-by-sense text for extraction and quotation checking.

Brett, 2026-11-05: "what about searching en.wiktionary for the individual
bearers", then "please". Source: en.wiktionary.org via the MediaWiki API
(action=parse, wikitext and revision id), CC BY-SA 4.0. One request per page,
spaced out. Each block in wiktionary-senses.txt is headed
"=== W:<page>:<section>:<n> ===", which extractions cite as their locator.
"""
import csv
import json
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ITEMS = os.path.join(HERE, "..", "items-v4.csv")
UA = "interjections-research-script/0.1 (linguistics study; contact via GitHub BrettRey)"
EXTRA = {"BASTARD_SUPP": ["bastard"], "YOU_BASTARD": ["bastard", "you bastard"],
         "THE_HELL_WH": ["the hell", "hell"], "TUTTUT": ["tut-tut", "tut"],
         "BLOODY_INFIX": ["-bloody-", "bloody"], "HOWAREYOU": ["how are you"]}
POS = ("Adjective", "Adverb", "Interjection", "Noun", "Verb", "Infix", "Particle",
       "Pronoun", "Phrase", "Determiner", "Preposition", "Conjunction", "Proper noun")


def fetch(title, tries=5):
    """One polite request; on HTTP 429 wait for Retry-After (capped) and retry."""
    for k in range(tries):
        try:
            return _fetch(title)
        except urllib.error.HTTPError as e:
            if e.code != 429 or k == tries - 1:
                raise
            wait = min(int(e.headers.get("Retry-After") or 30), 180)
            time.sleep(wait)


def _fetch(title):
    q = urllib.parse.urlencode({"action": "parse", "page": title, "prop": "wikitext|revid",
                                "format": "json", "formatversion": "2", "redirects": "1"})
    req = urllib.request.Request("https://en.wiktionary.org/w/api.php?" + q, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def clean(s):
    s = re.sub(r"\{\{(?:lb|lbl)\|en\|([^}]*)\}\}", lambda m: "(" + m.group(1).replace("|_|", " ").replace("|", ", ") + ")", s)
    s = re.sub(r"\{\{(?:n-g|ng|non-gloss|gloss|gl)\|([^}]*)\}\}", r"\1", s)
    s = re.sub(r"\{\{(?:senseid|anchor|U)\|[^}]*\}\}", "", s)
    s = re.sub(r"\{\{(?:alternative form of|alt form|abbreviation of|synonym of|form of)\|en\|([^}|]*)[^}]*\}\}", r"alternative form of \1", s)
    s = re.sub(r"\{\{(?:l|m|w|vern|taxlink)\|(?:en\|)?([^}|]*)[^}]*\}\}", r"\1", s)
    s = re.sub(r"\[\[(?:[^]|]*\|)?([^]]*)\]\]", r"\1", s)
    s = re.sub(r"'''?", "", s)
    s = re.sub(r"\{\{[^{}]*\}\}", "", s)
    return re.sub(r"\s+", " ", s).strip()


items = list(csv.DictReader(open(ITEMS, encoding="utf-8")))
pages = {}
for it in items:
    for t in EXTRA.get(it["item_id"], [it["form"]]):
        pages.setdefault(t, []).append(it["item_id"])
blocks, log = [], []
for title, ids in pages.items():
    path = os.path.join(HERE, "raw", re.sub(r"[^A-Za-z0-9_-]", "_", title) + ".json")
    try:
        if os.path.exists(path):
            d = json.load(open(path))
        else:
            d = fetch(title)
            time.sleep(6.0)
    except Exception as e:
        log.append({"page": title, "items": ids, "status": f"error {e}"})
        continue
    if "error" in d:
        log.append({"page": title, "items": ids, "status": d["error"].get("code", "error")})
        continue
    json.dump(d, open(path, "w"), ensure_ascii=False)
    wt, rev = d["parse"]["wikitext"], d["parse"]["revid"]
    log.append({"page": title, "items": ids, "status": "ok", "revid": rev})
    if "==English==" not in wt:
        continue
    en = re.split(r"\n==[^=]", wt.split("==English==", 1)[1])[0]
    sec, n, buf = "Top", 0, []

    def flush():
        if buf:
            blocks.append((f"W:{title}:{sec}:{n}", rev, ids, "\n".join(buf)))

    for line in en.split("\n"):
        m = re.match(r"=+ ?([A-Z][A-Za-z ]+?) ?(\d*) ?=+\s*$", line)
        if m:
            flush(); buf = []
            name = m.group(1).strip()
            sec, n = (name + (m.group(2) or "")), 0
            continue
        if sec.rstrip("0123456789") in POS and re.match(r"#[^*:]", line):
            flush(); n += 1
            buf = [clean(line.lstrip("#").strip())]
            continue
        if line.startswith("#*"):
            if buf:
                buf.append("QUOTATION: " + clean(line.lstrip("#*").strip())[:300])
            continue
        if line.startswith("#:") and buf:
            buf.append("EXAMPLE: " + clean(line.lstrip("#:").strip())[:300])
            continue
        if line.strip():
            if sec.rstrip("0123456789") in POS and n == 0 and line.startswith("{{"):
                buf.append("HEADWORD: " + line.strip()[:200])
            elif sec.startswith(("Etymology", "Pronunciation", "Usage notes")):
                buf.append(clean(line)[:400])
    flush()
with open(os.path.join(HERE, "wiktionary-senses.txt"), "w", encoding="utf-8") as fh:
    for bid, rev, ids, text in blocks:
        fh.write(f"\n=== {bid} === (revid {rev}; bearers sharing this page: {', '.join(ids)})\n{text}\n")
json.dump(log, open(os.path.join(HERE, "fetch-log.json"), "w"), indent=1)
print(len(pages), "pages;", sum(1 for l in log if l["status"] == "ok"), "ok;", len(blocks), "blocks")
for l in log:
    if l["status"] != "ok":
        print("MISSING", l["page"], l["items"], l["status"])
