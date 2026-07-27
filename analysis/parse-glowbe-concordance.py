"""Turn a saved English-Corpora results frame into a TSV.

The concordance lives in `<saved-name>_files/x3_*.html`, not in the top-level
HTML, which is only the frameset. Emits index / doc-id / country / genre /
source / context, tab-separated.

    python3 analysis/parse-glowbe-concordance.py x3_70rR.html > out.tsv
"""
import html
import re
import sys

CC = set("US CA GB IE AU NZ IN LK PK BD SG MY PH HK ZA NG GH KE TZ JM".split())
ROW = re.compile(r'^(\d+)\s+(\d+)\s+([A-Z]{2})\s+([A-Z])\s+(\S+)\s+(.*)$')


def main():
    raw = open(sys.argv[1], encoding='windows-1252', errors='replace').read()
    n = 0
    for tr in re.findall(r'<tr[^>]*>.*?</tr>', raw, re.S | re.I):
        text = ' '.join(html.unescape(re.sub(r'<[^>]+>', ' ', tr)).split())
        m = ROW.match(text)
        if m and m.group(3) in CC:
            print('\t'.join(m.groups()))
            n += 1
    print(f'{n} rows', file=sys.stderr)


if __name__ == '__main__':
    main()
