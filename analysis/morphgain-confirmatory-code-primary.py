#!/usr/bin/env python3
"""Primary coding pass for the morphology-gain COHA study.

The script reads the randomized, year-hidden coding sheet and writes a
coded version. Rules are intentionally conservative for plural -s forms:
plural nouns such as "boos" and "oohs" are excluded unless the local
context supports a finite verbal analysis.
"""

from __future__ import annotations

import csv
import re
from pathlib import Path

BASE = Path(__file__).parent / "morphgain-confirmatory"
INFILE = BASE / "morphgain-coding-sheet.csv"
OUTFILE = BASE / "morphgain-coded-primary.csv"
SUMMARY = BASE / "morphgain-coding-summary.csv"


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", str(text or "")).strip()


def low(text: str) -> str:
    return norm(text).lower()


def starts_any(text: str, prefixes: tuple[str, ...]) -> bool:
    text = low(text)
    return any(text.startswith(prefix) for prefix in prefixes)


def contains_any(text: str, needles: tuple[str, ...]) -> bool:
    text = low(text)
    return any(needle in text for needle in needles)


def excluded_plural_wows(context: str, left: str, right: str) -> str | None:
    text = low(context)
    if contains_any(text, (
        "pow wows", "workstations on wheels", "workouts of the week",
        "ciao wows", "wows alliance", "commissioner wows",
        "wows of afghanistan", "muffled wows", "open-mouthed",
        "chorus of wows", "no wows", "were wows",
    )):
        return "noun/proper-name/acronym use"
    if starts_any(right, (
        "french audiences", "fellow musicians", "the crowds", "cutting-edge",
        "them", "tv audience", "me", "the lollapalooza crowd",
        "white audiences", "' em", "20,000", "the nation",
    )):
        return None
    if re.search(r"\bwows\s+(audiences|crowds|fans|viewers|visitors|critics|them|him|her|me|us)\b", text):
        return None
    return "noun or non-verbal use"


def excluded_plural_boos(context: str, left: str, right: str) -> str | None:
    text = low(context)
    if contains_any(text, (
        "ms. boos", "boos alien", "class eleven boos live", "word cpuo-t",
        "the boos of sports", "torn out of the boos", "adam boos",
        "tree grows in brooklyn boos", "ty beanie boos",
    )):
        return "proper-name/metalinguistic/non-target use"
    if re.search(r"\b(nobody|crowd|audience|haunter|he|she|it|one)\s+boos\b", text):
        return None
    if starts_any(right, ("a sunset", "so loud", ".")):
        if re.search(r"\b(nobody|crowd|haunter)\s+boos\b", text):
            return None
    return "noun use"


def excluded_plural_oohs(context: str, left: str, right: str) -> str | None:
    text = low(context)
    if re.search(r"\b(crowd|everyone|everybody|she)\s+oohs\s+and\b", text):
        return None
    if "oohs and coos and smiles" in text:
        return None
    return "noun use"


def excluded_plural_shoos(context: str, left: str, right: str) -> str | None:
    text = low(context)
    if contains_any(text, (
        "shoos 1/2 soled", "machine shoos", "pairs of shoos",
        "ryan shoos", "boos and shoos", "shoos becky a look",
    )):
        return "OCR/proper-name/non-target use"
    if starts_any(right, (
        "away", "off", "out", "them", "him", "her", "us", "you",
        "everyone", "the women", "the children", "the mother bird",
        "neighborhood pet", "two or three cats", "it", "these thoughts",
    )):
        return None
    return "unclear or non-verbal use"


def excluded_booing(context: str, left: str, right: str) -> str | None:
    text = low(context)
    right_l = low(right)

    if contains_any(text, (
        "booing 's work", "booing's work", "sweet speaking",
        "took to booing and booing for causes",
    )):
        return "OCR/proper-name/non-target use"

    if re.search(r"\b(midst|chorus|volume|burst|outbreak|wave|storm|crescendo|mixture)\s+of\s+booing\b", text):
        return "noun use"
    if contains_any(text, (
        "booing and cheers", "cheers and booing", "booing or applause",
        "hissing booing", "whistling and booing", "booing and hissing",
        "booing and cheering",
    )):
        return "noun use"
    if re.search(r"\b(the|that|this|all|continued|prolonged|loudest|most prolonged|continued)\s+booing\b", text):
        return "noun use"
    if re.search(r"\bbooing\s+of\s+", text):
        return "noun use"
    if re.search(r"\bbooing\s+(filled|testified|started|stopped|got louder|was reserved|came|subsided|rang)\b", text):
        return "noun use"
    if re.search(r"\b(a|an|the)\s+booing\s+(crowd|audience|fans|spectators|war protesters)\b", text):
        return "adjectival use without recoverable verbal syntax"

    if re.search(r"\b(was|were|is|are|been|being|start(?:ed|s)?|begin(?:s|ning)?|began|kept|keep(?:s)?|continued?|stop(?:ped|s)?)\s+(?:really\s+|still\s+|actually\s+|loudly\s+)?booing\b", text):
        return None
    if re.search(r"\b(they|people|fans|crowd|audience|spectators|we|you|he|she|i)\s+(?:really\s+|actually\s+|still\s+)?booing\b", text):
        return None
    if starts_any(right_l, (
        "him", "her", "them", "me", "us", "you", "the ", "a ", "an ",
        "this ", "that ", "his ", "their ", "mcenroe", "players",
    )):
        return None
    if starts_any(right_l, ("at ", "from ")):
        return None

    return "no recoverable verbal syntax"


def excluded_oohing(context: str, left: str, right: str) -> str | None:
    text = low(context)
    right_l = low(right)

    if contains_any(text, (
        "oohing for money being smuggled", "oohing souls who",
        "oohing and aahing outward disapproval",
    )):
        return "OCR/adjectival/unclear use"

    if re.search(r"\b(was|were|is|are|been|being|finished|finish(?:ed)?|began|begin(?:s|ning)?|start(?:ed|s)?|spent|sit|sits|sat|heard them|came|come)\s+.*\boohing\b", text):
        return None
    if re.search(r"\boohing\s+and\s+a+h", text):
        return None
    if starts_any(right_l, (
        "and aah", "and ah", "and aa", "at ", "over ", "about ",
        "into ", "in amazement", "for the camera",
    )):
        return None

    return "no recoverable verbal syntax"


def excluded_shooing(context: str, left: str, right: str) -> str | None:
    text = low(context)
    if contains_any(text, (
        "vigorous \" shooing \" only scared", "\" shooing \" was bootless",
    )):
        return "noun use"
    if re.search(r"\bshooing\s+(motion|gesture|motions|gestures)\b", text):
        return "adjectival use without recoverable verbal syntax"
    return None


def excluded_wowing(context: str, left: str, right: str) -> str | None:
    text = low(context)
    if contains_any(text, ("pow , wowing", "pow wowing", "pow-wowing")):
        return "non-target compound"
    return None


def exclusion(row: dict) -> str | None:
    term = row["term"]
    context = norm(f'{row["left"]} {row["target"]} {row["right"]}')
    left = row["left"]
    right = row["right"]
    text = low(context)

    if re.search(rf"\b(word|term|form)\s+{re.escape(term)}\b", text):
        return "metalinguistic mention"

    if term == "wowed" and contains_any(text, (
        'going " wowed "', "wowed and \" zaddafuck",
        "not wowed much aptitude", "all wowed up", "wowed clear out",
        "the wowed explorers reported",
    )):
        return "non-verbal vocalization"
    if term == "wowing":
        return excluded_wowing(context, left, right)
    if term == "wows":
        return excluded_plural_wows(context, left, right)
    if term == "booed" and contains_any(text, (
        "hairts booed doon", "heart bowed down", "capt . nelms said he booed not",
        "auto horn , held down hard , booed past",
    )):
        return "OCR/proper-name/non-target use"
    if term == "booing":
        return excluded_booing(context, left, right)
    if term == "boos":
        return excluded_plural_boos(context, left, right)
    if term == "oohed" and contains_any(text, (
        "oohed the crowd to join him", "oohed pretty good for a war play",
        "oohed at in another way",
    )):
        return "OCR or unclear context"
    if term == "oohs":
        return excluded_plural_oohs(context, left, right)
    if term == "oohing":
        return excluded_oohing(context, left, right)
    if term == "shooing":
        return excluded_shooing(context, left, right)
    if term == "shoos":
        return excluded_plural_shoos(context, left, right)
    if term == "oohed" and "oohed in" in text:
        return "OCR or unclear context"

    return None


def target_recoverable(row: dict) -> int:
    term = row["term"]
    text = low(f'{row["left"]} {row["target"]} {row["right"]}')
    right = low(row["right"])
    left = low(row["left"])
    if term.startswith("shoo"):
        return int(starts_any(right, (
            "away", "off", "out", "them", "him", "her", "us", "you",
            "everyone", "the ", "a ", "an ", "his ", "her ", "their ",
            "neighborhood pet", "two or three cats",
        )))
    if term.startswith("boo"):
        if re.search(r"\b(was|were|is|are|been|being)\s+boo", text):
            return 1
        if starts_any(right, ("him", "her", "them", "the ", "a ", "an ", "this ", "that ", "his ", "their ")):
            return 1
        return int(" at " in right or " from " in right)
    if term.startswith("ooh"):
        if starts_any(right, ("at ", "over ", "about ")):
            return 1
        return int(" at " in right or " over " in right or " about " in right)
    if term.startswith("wow"):
        if re.search(r"\b(was|were|is|are|been|being)\s+wow", text):
            return 1
        if starts_any(right, ("him", "her", "them", "me", "us", "the ", "a ", "an ", "audiences", "crowds", "fans", "viewers", "visitors", "critics", "20,000")):
            return 1
        return int("audience" in right or "crowd" in right or "audience" in left or "crowd" in left)
    return 0


def interactional_residue(row: dict) -> int:
    family = row["family"]
    text = low(f'{row["left"]} {row["target"]} {row["right"]}')
    if family in {"boo", "ooh", "shoo"}:
        return 1
    if family == "wow":
        return int(any(word in text for word in ("audience", "crowd", "fans", "viewers", "visitors", "people", "teachers", "musicians")))
    return 0


def code_row(row: dict) -> dict:
    reason = exclusion(row)
    coded = dict(row)
    if reason:
        coded.update({
            "exclude": "1",
            "exclusion_reason": reason,
            "verbal_syntax": "0",
            "semantic_residue": "0",
            "interactional_residue": "0",
            "targeted_entity": "0",
            "coder_notes": "excluded by primary coding rule",
        })
        return coded

    coded.update({
        "exclude": "0",
        "exclusion_reason": "",
        "verbal_syntax": "1",
        "semantic_residue": "1",
        "interactional_residue": str(interactional_residue(row)),
        "targeted_entity": str(target_recoverable(row)),
        "coder_notes": "primary coding rule",
    })
    return coded


def main() -> None:
    with INFILE.open(encoding="utf-8", newline="") as handle:
        rows = [code_row(row) for row in csv.DictReader(handle)]

    with OUTFILE.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    summary = {}
    for row in rows:
        key = (
            row["family"],
            row["term"],
            "included" if row["exclude"] == "0" else row["exclusion_reason"],
        )
        summary[key] = summary.get(key, 0) + 1
    with SUMMARY.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["family", "term", "status_or_reason", "count"])
        writer.writeheader()
        for (family, term, status_or_reason), count in sorted(summary.items()):
            writer.writerow({
                "family": family,
                "term": term,
                "status_or_reason": status_or_reason,
                "count": count,
            })

    included = sum(1 for row in rows if row["exclude"] == "0")
    print(f"coded={len(rows)} included={included} excluded={len(rows) - included}")
    by_family = {}
    for row in rows:
        fam = row["family"]
        by_family.setdefault(fam, [0, 0])
        by_family[fam][0] += 1
        by_family[fam][1] += row["exclude"] == "0"
    for family, (total, inc) in sorted(by_family.items()):
        print(f"{family}\t{inc}/{total} included")


if __name__ == "__main__":
    main()
