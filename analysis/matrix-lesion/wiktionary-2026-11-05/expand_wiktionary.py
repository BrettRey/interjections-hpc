"""Version 2 of the Wiktionary sense text, after both extraction agents found
that v1's cleaning stripped templates (IPA, etymons, examples, quotations,
some glosses) and that block ids repeated across etymologies.

For each saved page, the English section's wikitext is sent to the MediaWiki
expandtemplates API (POST, prop=wikitext), which replaces every template by
its output and keeps the line structure; HTML tags are then removed. Block
ids now carry the etymology number: W:<page>:E<k>:<section>:<n>. No length
caps. Polite: one request every 6 s, Retry-After honoured on HTTP 429.
"""
import html
import json
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
UA = "interjections-research-script/0.1 (linguistics study; contact via GitHub BrettRey)"
POS = ("Adjective", "Adverb", "Interjection", "Noun", "Verb", "Infix", "Particle", "Pronoun",
       "Phrase", "Determiner", "Preposition", "Conjunction", "Proper noun", "Prepositional phrase")


def expand(title, text, tries=5):
    data = urllib.parse.urlencode({"action": "expandtemplates", "title": title, "text": text,
                                   "prop": "wikitext", "format": "json", "formatversion": "2"}).encode()
    for k in range(tries):
        try:
            req = urllib.request.Request("https://en.wiktionary.org/w/api.php", data=data,
                                         headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)["expandtemplates"]["wikitext"]
        except urllib.error.HTTPError as e:
            if e.code != 429 or k == tries - 1:
                raise
            time.sleep(min(int(e.headers.get("Retry-After") or 30), 180))


def clean(s):
    s = re.sub(r"<ref[^>]*>.*?</ref>|<ref[^>]*/>", "", s, flags=re.S)
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"\[\[(?:Category|File|Image|Thesaurus):[^\]]*\]\]", "", s)
    s = re.sub(r"\x7f[^\x7f]*\x7f", "", s)
    s = re.sub(r"\[\[(?:[^]|]*\|)?([^]]*)\]\]", r"\1", s)
    s = re.sub(r"\[https?://\S+ ([^]]*)\]", r"\1", s)
    s = re.sub(r"'''?", "", s)
    s = re.sub(r"__[A-Z]+__", "", s)
    return re.sub(r"\s+", " ", html.unescape(s)).strip()


blocks, log = [], []
for fn in sorted(os.listdir(os.path.join(HERE, "raw"))):
    d = json.load(open(os.path.join(HERE, "raw", fn)))
    title, rev, wt = d["parse"]["title"], d["parse"]["revid"], d["parse"]["wikitext"]
    if "==English==" not in wt:
        log.append({"page": title, "status": "no English section"})
        continue
    en = "==English==" + re.split(r"\n==[^=]", wt.split("==English==", 1)[1])[0]
    out = os.path.join(HERE, "raw-expanded", fn)
    if os.path.exists(out):
        ex = json.load(open(out))["expanded"]
    else:
        ex = expand(title, en)
        json.dump({"title": title, "revid": rev, "expanded": ex}, open(out, "w"), ensure_ascii=False)
        time.sleep(6.0)
    log.append({"page": title, "status": "ok", "revid": rev})
    ety, sec, n, buf, seen, secid = 0, "Top", 0, [], {}, "Top"

    def flush():
        if buf:
            blocks.append((f"W:{title}:E{ety}:{secid}:{n}", rev, "\n".join(buf)))

    for line in ex.split("\n"):
        m = re.match(r"=+ ?([A-Z][A-Za-z ]+?) ?(\d*) ?=+\s*$", line)
        if m:
            flush(); buf = []
            name, num = m.group(1).strip(), m.group(2)
            if name == "Etymology":
                ety = int(num or 1)
            seen[(ety, name)] = seen.get((ety, name), 0) + 1
            sec, n = name, 0
            secid = name if seen[(ety, name)] == 1 else f"{name}#{seen[(ety, name)]}"
            continue
        base = sec
        if base in POS and re.match(r"#[^*:]", line):
            flush(); n += 1
            buf = [clean(line.lstrip("#").strip())]
        elif line.startswith("#*") and buf:
            buf.append("QUOTATION: " + clean(line.lstrip("#*:").strip()))
        elif line.startswith("#:") and buf:
            buf.append("EXAMPLE: " + clean(line.lstrip("#:*").strip()))
        elif line.strip():
            c = clean(line)
            if not c:
                continue
            if base in POS and n == 0:
                buf.append("HEADWORD: " + c)
            elif sec in ("Etymology", "Pronunciation", "Usage notes"):
                buf.append(c)
    flush()
with open(os.path.join(HERE, "wiktionary-senses-v2.txt"), "w", encoding="utf-8") as fh:
    for bid, rev, text in blocks:
        fh.write(f"\n=== {bid} === (revid {rev})\n{text}\n")
json.dump(log, open(os.path.join(HERE, "expand-log.json"), "w"), indent=1)
ids = [b[0] for b in blocks]
print(len(log), "pages;", len(blocks), "blocks;", len(ids) - len(set(ids)), "duplicate ids")
