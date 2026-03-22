#!/usr/bin/env python3
"""
fie-prepare-coding.py
Parse COHA concordance data, apply exclusion rules, produce
a decade-blinded randomised coding sheet per the preregistration.
"""

import csv
import random
import re
import sys
from pathlib import Path

SEED = 2026
RAW = Path(__file__).parent / "fie-coha-raw.txt"
OUT_CODING = Path(__file__).parent / "fie-coding-sheet.csv"
OUT_EXCLUDED = Path(__file__).parent / "fie-excluded.csv"
OUT_SUMMARY = Path(__file__).parent / "fie-extraction-summary.txt"

# --- Parse raw COHA export ---

def parse_raw(path):
    """Parse the tab-delimited COHA concordance file."""
    records = []
    with open(path, "r", encoding="utf-8") as f:
        header = f.readline()  # skip header
        for i, line in enumerate(f, start=1):
            line = line.rstrip("\n")
            if not line:
                continue
            parts = line.split("\t", 4)
            if len(parts) < 5:
                continue
            line_num, year, genre, source, context = parts
            try:
                year = int(year)
            except ValueError:
                continue
            records.append({
                "raw_line": i,
                "year": year,
                "decade": (year // 10) * 10,
                "genre": genre.strip(),
                "source": source.strip(),
                "context": context.strip(),
            })
    return records


# --- Exclusion rules ---

OCR_PATTERNS = [
    # "fie" as OCR for "He" (sentence-initial or after period)
    r'(?<=[.?!]\s)fie\s+(?:was|had|has|is|did|said|could|would|should|might|went|saw|felt|looked|made|wrote|spoke|set|ran|put|got|took|carried|denied|added|expressed|proposed|insisted|predicted|offered|testified|emphasized|announced|smiled|sighed|tried|wondered|removed|stood|threw|looked|knows|means|claps|presents|contented|pulled|carries|lit|liked)',
    r'^fie\s+(?:was|had|has|is|did|said|could|would|should|might|went|saw|felt|looked|made|wrote|spoke|set|ran|put|got|took|carried|denied|added|expressed|proposed|insisted|predicted|offered|testified|emphasized|announced|smiled|sighed|tried|wondered|removed|stood|threw|looked|knows|means|claps|presents|contented|pulled|carries|lit|liked)',
    # "fie" as OCR for "the"
    r'\bfie\s+(?:trade|real|question|contribution|energy|mayor|de\.\s|seclusive|fateful)',
    # "fie" as OCR for "He" — only when followed by a past-tense verb
    # (bare FI[Ee] + space is too broad; catches genuine sentence-initial Fie)
    r'^FI[Ee]\s+(?:was|had|has|is|did|said|could|would|should|might|went|saw|felt|looked|made|wrote|spoke|set|ran|put|got|took|carried|denied|added|expressed|proposed|insisted|predicted|offered|testified|emphasized|announced|smiled|sighed|tried|wondered|removed|stood|threw|knows|means|claps|presents|contented|pulled|carries|lit|liked|turns|throws)',
    r'\.\s+FI[Ee]\s+(?:was|had|has|is|did|said|could|would|should|might|went|saw|felt|looked|made|wrote|spoke|set|ran|put|got|took|carried|denied|added|expressed|proposed|insisted|predicted|offered|testified|emphasized|announced|smiled|sighed|tried|wondered|removed|stood|threw|knows|means|claps|presents|contented|pulled|carries|lit|liked|turns|throws)',
    # Figure abbreviation
    r'Fie\.\s+\d+',
    r'Fie\.\s+[0-9]',
    # Garbled OCR
    r'fie\s+thegenate',
    r'spec\s+fie\s+grant',
    r'M\'DuFr\s+fie',
    r'fie\s+re\s+God',
    r'fie\s+made\s+all\s+things',
    r'fie\s+sailed',
    r'Paci\s*fie\s+Coast',
    r'spcci\s+fie',
    r'traf-?\d?\s*fie',
    r'prceci\s+fie',
    r'electric\s+fie',
    r'fie\s+ho\s+--',
    r'terr,?\s+fie',
    r'fie\s+42\)',
    r'fie\s+mem\.',
    r'T\s+FIE\s+NE',
    r'rU\s+fie\s+Ne0',
    r'fie,?\s+markably',
    r'Tra\s+f\s+fie',
    r'fie\s+years\s+"',
    r'fie\.\s+with\s+them',
    r'fie\s+able\s+to\s+feel',
    r'21349\s+FIE\s+boy',
    r'fie\s+longer\s+knew',
    r'fie\s+simply\s+wants',
    r'fie\s+well\s+Penalties',
    r'fie,\.\s+in\s+front',
    r'fie\s+or\s+She\s+rarely',
    r'T\s+9-1\s+FIE',
    r'FIE\s+R\.A\.ncu',
    r'FIE\s+CONTINUED',
    r'FIE\s+LEFT',
    r'FIE\s+PICKED',
    r'EIGHTH\s+ARE\s+FIE',
    r'At\s+fie\s+to\s+Deja',
    r'fie\s+legs\s+off',
    r'fie\s+from\s+Giulia',
]

def is_ocr_noise(context):
    """Check if the context is OCR noise (fie = he/the/fig/etc.)."""
    for pat in OCR_PATTERNS:
        if re.search(pat, context, re.IGNORECASE):
            return True
    return False

def is_metalinguistic(context):
    """Check if fie is mentioned rather than used."""
    patterns = [
        r'the\s+word\s+["\']?fie',
        r'words\s+like\s+["\']?\s*Fie',
        r'used\s+only\s+in\s+the\s+very\s+oldest\s+texts\s+as\s+accusatives.*fie',
        r'dampening\s+fie',  # Star Trek technobabble
    ]
    for pat in patterns:
        if re.search(pat, context, re.IGNORECASE):
            return True
    return False

def is_non_english(context):
    """Check for non-English passages."""
    patterns = [
        r'Mo\s+fie,\s+li\s+tan\s+to\s+maie',  # Creole
        r'oda\s+tee.*fie\s+bah\s+an\s+deh',  # Aphasic speech
    ]
    for pat in patterns:
        if re.search(pat, context, re.IGNORECASE):
            return True
    return False

def is_name_fragment(context):
    """Check if fie is part of a name (Miss Effie split)."""
    patterns = [
        r'Miss\s+Ef\s+--\s+fie',
        r'fie,?\s+ured\s+largely',  # "figured"
    ]
    for pat in patterns:
        if re.search(pat, context, re.IGNORECASE):
            return True
    return False

def classify_exclusion(rec):
    """Return exclusion reason or None if includable."""
    ctx = rec["context"]

    if is_ocr_noise(ctx):
        return "OCR noise"
    if is_metalinguistic(ctx):
        return "metalinguistic mention"
    if is_non_english(ctx):
        return "non-English"
    if is_name_fragment(ctx):
        return "name fragment"

    return None


# --- Main ---

def main():
    records = parse_raw(RAW)
    print(f"Parsed {len(records)} concordance lines from {RAW.name}")

    # Apply exclusions
    included = []
    excluded = []
    exclusion_counts = {}

    for rec in records:
        reason = classify_exclusion(rec)
        if reason:
            rec["exclusion_reason"] = reason
            excluded.append(rec)
            exclusion_counts[reason] = exclusion_counts.get(reason, 0) + 1
        else:
            included.append(rec)

    print(f"\nIncluded: {len(included)}")
    print(f"Excluded: {len(excluded)}")
    for reason, count in sorted(exclusion_counts.items(), key=lambda x: -x[1]):
        print(f"  {reason}: {count}")

    # Decade counts
    decade_counts = {}
    for rec in included:
        d = rec["decade"]
        decade_counts[d] = decade_counts.get(d, 0) + 1

    print(f"\nDecade counts (included):")
    decades_with_3plus = 0
    for d in sorted(decade_counts):
        n = decade_counts[d]
        flag = "" if n >= 3 else " [SPARSE]"
        if n >= 3:
            decades_with_3plus += 1
        print(f"  {d}s: {n}{flag}")

    # Go/no-go check
    total = len(included)
    go = total >= 50 and decades_with_3plus >= 3
    print(f"\n=== GO/NO-GO CHECK ===")
    print(f"Total analysable tokens: {total} (threshold: 50)")
    print(f"Decades with 3+ tokens: {decades_with_3plus} (threshold: 3)")
    print(f"Decision: {'GO' if go else 'NO-GO'}")

    if not go:
        print("Analysis cannot proceed. Prediction remains untested.")
        sys.exit(0)

    # Randomise and blind decade
    random.seed(SEED)
    random.shuffle(included)

    # Assign coding IDs
    for i, rec in enumerate(included, start=1):
        rec["coding_id"] = f"F{i:03d}"

    # Write coding sheet (decade-blinded)
    with open(OUT_CODING, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "coding_id", "genre", "source", "context",
            "interjection_syn", "interjection_sem", "interjection_int",
            "notes"
        ])
        for rec in included:
            writer.writerow([
                rec["coding_id"],
                rec["genre"],
                rec["source"],
                rec["context"],
                "",  # to be coded
                "",  # to be coded
                "",  # to be coded
                "",  # notes
            ])

    # Write excluded list
    with open(OUT_EXCLUDED, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["raw_line", "year", "decade", "genre", "source", "context", "exclusion_reason"])
        for rec in excluded:
            writer.writerow([
                rec["raw_line"], rec["year"], rec["decade"],
                rec["genre"], rec["source"], rec["context"],
                rec["exclusion_reason"]
            ])

    # Write decade key (separate file, not shown to coder)
    decade_key_path = Path(__file__).parent / "fie-decade-key.csv"
    with open(decade_key_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["coding_id", "year", "decade"])
        for rec in included:
            writer.writerow([rec["coding_id"], rec["year"], rec["decade"]])

    # Write summary
    with open(OUT_SUMMARY, "w", encoding="utf-8") as f:
        f.write(f"COHA fie extraction summary\n")
        f.write(f"{'='*40}\n")
        f.write(f"Raw concordance lines: {len(records)}\n")
        f.write(f"Included: {len(included)}\n")
        f.write(f"Excluded: {len(excluded)}\n\n")
        f.write(f"Exclusion counts:\n")
        for reason, count in sorted(exclusion_counts.items(), key=lambda x: -x[1]):
            f.write(f"  {reason}: {count}\n")
        f.write(f"\nDecade counts (included):\n")
        for d in sorted(decade_counts):
            f.write(f"  {d}s: {decade_counts[d]}\n")
        f.write(f"\nGo/no-go: {'GO' if go else 'NO-GO'}\n")
        f.write(f"Total analysable: {total}\n")
        f.write(f"Decades with 3+: {decades_with_3plus}\n")

    print(f"\nOutputs:")
    print(f"  Coding sheet: {OUT_CODING}")
    print(f"  Excluded list: {OUT_EXCLUDED}")
    print(f"  Decade key: {decade_key_path}")
    print(f"  Summary: {OUT_SUMMARY}")


if __name__ == "__main__":
    main()
