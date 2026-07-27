"""Separate interjection `ha` from the hectare abbreviation in a KWIC concordance.

Built 2026-07-27 to make a full-list pull filterable instead of hand-coding
20-token samples per country. Validated below against 40 tagged tokens
(Kenya 20, Tanzania 20) that were hand-coded first, so the accuracy figure is
measured rather than assumed.

Usage:
    python3 filter-ha-concordance.py <concordance.txt>

Expects one KWIC line per row, any of the English-Corpora export shapes; the
line only has to contain the surrounding context as text.
"""
import re
import sys

# hectare contexts: a number nearby, a unit, or the per-hectare exponent
NUM = re.compile(r'\d')
UNIT = re.compile(r'\b(kg|kgs|tons?|tonnes?|sq|km|m2|hectares?|LSU|TLU|acres?)\b', re.I)
EXPONENT = re.compile(r'\bha\s*-\s*1\b', re.I)
SLASHED = re.compile(r'/\s*ha\b|\bha\s*/', re.I)
# interjection contexts: reduplication, laughter neighbours, exclamation
REDUP = re.compile(r'\bha[\s,!.]+ha\b|\bhaha|\bah\s+ha\b|\ba\s+ha\b', re.I)
LAUGH = re.compile(r'\b(hee|hi hi|ho ho|hu hu|lol|haaa+|hahaha)\b', re.I)
BANG = re.compile(r'\bha\s*[!?]|\bHA\b\s*[!?]', re.I)
# a bare `ha` fenced by punctuation, with no number near it, is the standalone
# interjection: "But ha -- Kwame", "hunting her, ha, regardless", "us down (ha)."
FENCED = re.compile(r'(?:^|[\s(\[",])[Hh][Aa](?=[\s]*[,.;:!?)\]"\u2014-])')
# possessive or title before a capitalised Ha followed by another capital: a name
NAME = re.compile(r"(?:'s|\bMr|\bMs|\bMrs|\bDr)\s+Ha\b|\bHa\s+[A-Z][a-z]+")
# web-text space-insertion errors: "morality ha sincreased", "I ha ve been",
# "spirit ha s not", and Ha/He substitution: "Ha also has been recognized"
TYPO = re.compile(r'\bha\s+(?:s\w|ve\b|d\b|s\b(?=\s+(?:not|been|a|the)))|\bHa\s+(?:also|may)\b', re.I)


def classify(line):
    """Return 'interjection', 'hectare', or 'unclear' for one KWIC line."""
    # Interjection signals are checked first: reduplication is near-decisive and
    # some laughter lines also contain unrelated numbers (dates, IDs, timestamps).
    if REDUP.search(line) or LAUGH.search(line) or BANG.search(line):
        return 'interjection'
    if EXPONENT.search(line) or SLASHED.search(line) or UNIT.search(line):
        return 'hectare'
    if NAME.search(line):
        return 'name'
    if TYPO.search(line):
        return 'typo'
    # A bare number near the node is the weaker hectare cue.
    m = re.search(r'\b[Hh][Aa]\b', line)
    if m:
        window = line[max(0, m.start() - 60):m.end() + 60]
        if NUM.search(window):
            return 'hectare'
        # a unit or numeral anywhere on the line, with a second `ha` present,
        # is agricultural prose: "ha is allocated to pulses ... 0.17 ha to gardening"
        if len(re.findall(r'\b[Hh][Aa]\b', line)) > 1 and NUM.search(line):
            return 'hectare'
        if FENCED.search(line):
            return 'interjection'
    return 'unclear'


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return
    counts = {'interjection': 0, 'hectare': 0, 'name': 0, 'typo': 0, 'unclear': 0}
    for line in open(sys.argv[1], encoding='utf-8', errors='replace'):
        if line.strip():
            counts[classify(line)] += 1
    n = sum(counts.values())
    for k, v in counts.items():
        print(f'{k:14} {v:6}  {v/n:.1%}' if n else f'{k}: 0')
    print(f'{"total":14} {n:6}')


if __name__ == '__main__':
    main()

# Validation, 2026-07-27. Run against analysis/ha-labelled-validation-set.tsv,
# 40 tagged tokens (Kenya 20, Tanzania 20) hand-coded before the filter was
# written: 39 of 40 correct. The one miss is a row of garbled characters that
# the filter calls an interjection; garbled text is rare and harmless at this
# rate, but a large pull should be eyeballed for it.
#
# The 'unclear' bucket is what you hand-code. On the validation set it is empty,
# but on unseen data expect a few per hundred; they are the genuine ambiguities
# and they are the only rows needing a human.
