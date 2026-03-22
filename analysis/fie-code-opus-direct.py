#!/usr/bin/env python3
"""
Direct Opus coding of fie tokens.
Classifies each token by pattern-matching on context, with manual
overrides for edge cases. Writes fie-coded-opus.csv.
"""

import csv
import re
from pathlib import Path

INPUT = Path(__file__).parent / "fie-coding-sheet.csv"
OUTPUT = Path(__file__).parent / "fie-coded-opus.csv"

# OCR patterns: fie = he/she/the/five/fig/fire/field/etc.
OCR_VERBS = (
    r"(?:was|had|has|is|did|said|could|would|should|might|went|saw|felt|"
    r"looked|made|wrote|spoke|set|ran|put|got|took|carried|denied|added|"
    r"expressed|proposed|insisted|predicted|offered|testified|emphasized|"
    r"announced|smiled|sighed|tried|wondered|removed|stood|threw|knows|"
    r"means|claps|presents|contented|pulled|carries|lit|liked|turns|throws|"
    r"pictured|won|began|shut|relaxed|wanted|considered|sniffed|scuffed|"
    r"told|takes|looks|stood|drew|folded|stroked)"
)

def is_ocr(ctx):
    """Detect OCR noise where fie = he/the/she/fig/five/etc."""
    lc = ctx.lower()

    # Sentence-initial "FIe/FIE" + verb = "He"
    if re.search(r"FI[Ee]\s+" + OCR_VERBS, ctx):
        return "OCR: fie=He"
    if re.search(r"\.\s+FI[Ee]\s+" + OCR_VERBS, ctx):
        return "OCR: fie=He (after period)"
    # Lowercase fie + verb in non-dialogue context
    if re.search(r"(?<=[.?!]\s)fie\s+" + OCR_VERBS, ctx, re.IGNORECASE):
        return "OCR: fie=he (after sentence boundary)"

    # Specific OCR patterns
    ocr_specific = [
        (r"fie\s+(?:trade|real|question|contribution|energy|mayor|seclusive|fateful)", "OCR: fie=the"),
        (r"Paci\s*fie\s+Coast", "OCR: Pacific"),
        (r"spcci\s+fie", "OCR: specific"),
        (r"spec\s+fie\s+(?:grant|terrorists)", "OCR: specific"),
        (r"traf-?\d?\s*fie", "OCR: traffic"),
        (r"prceci\s+fie", "OCR: praecipe"),
        (r"electric\s+fie", "OCR: field"),
        (r"fie\s+ho\s+--", "OCR: fie ho (place name)"),
        (r"terr,?\s+fie", "OCR: terrific"),
        (r"fie\s+42\)", "OCR: garbled"),
        (r"fie\s+mem\.", "OCR: garbled"),
        (r"T\s+FIE\s+NE", "OCR: THE NEW"),
        (r"rU\s+fie\s+Ne0", "OCR: garbled masthead"),
        (r"fie,?\s+markably", "OCR: remarkably"),
        (r"Tra\s+f\s+fie", "OCR: traffic"),
        (r"fie\s+years\s+\"", "OCR: five years"),
        (r"fie\.\s+with\s+them", "OCR: garbled"),
        (r"fie\s+able\s+to\s+feel", "OCR: be able"),
        (r"21349\s+FIE\s+boy", "OCR: THE boy"),
        (r"fie\s+longer\s+knew", "OCR: no longer"),
        (r"fie\s+simply\s+wants", "OCR: he simply"),
        (r"fie\s+well\s+Penalties", "OCR: garbled"),
        (r"fie\s+or\s+She\s+rarely", "OCR: he or She"),
        (r"T\s+9-1\s+FIE", "OCR: garbled"),
        (r"FIE\s+R\.A\.ncu", "OCR: garbled"),
        (r"FIE\s+CONTINUED", "OCR: TO BE CONTINUED"),
        (r"FIE\s+LEFT", "OCR: HE LEFT"),
        (r"FIE\s+PICKED", "OCR: HE PICKED"),
        (r"EIGHTH\s+ARE\s+FIE", "OCR: garbled headline"),
        (r"At\s+fie\s+to\s+Deja", "OCR: garbled song title"),
        (r"fie\s+legs\s+off", "OCR: the legs"),
        (r"fie\s+from\s+Giulia", "OCR: title"),
        (r"Fie\.\s+\d+", "OCR: Fig. (figure)"),
        (r"fie\s+re\s+God", "OCR: He re God"),
        (r"fie\s+made\s+all\s+things", "OCR: He made"),
        (r"fie\s+sailed", "OCR: He sailed"),
        (r"fie\s+thegenate", "OCR: garbled"),
        (r"M'DuFr\s+fie", "OCR: garbled name"),
        (r"fie;\s+lawyer", "OCR: her lawyer"),
        (r"fie\s+Reinville", "OCR: the Reinville"),
        (r"equi\s+fie", "OCR: equipment"),
        (r"fie\.\s+suffered", "OCR: He suffered"),
        (r"fie\s+depended", "OCR: be depended"),
        (r"fie\s+In\s+this\s+way", "OCR: garbled footnote"),
        (r"fie\s+To\s+be\s+at\s+home", "OCR: garbled footnote"),
        (r"fie\s+New\s+York\s+Times", "OCR: the NYT"),
        (r"fie,\s+pleaded", "OCR: he pleaded"),
        (r"fie\s+belongs\s+With", "OCR: he belongs"),
        (r"fie\s+it\s+is\s+a\s+lamentable", "OCR: for it is"),
        (r"fie\s+hundred\s+members", "OCR: five hundred"),
        (r"fie\s+is\s+a\s+Democrat", "OCR: He is"),
        (r"fie\s+is\s+entirely\s+out", "OCR: he is"),
        (r"inclined\s+plane.*fie", "OCR: garbled"),
        (r"fie\s+is\s+a\s+great\s+organizer", "OCR: He is"),
        (r"fie\s+is\s+a\s+former", "OCR: He is"),
        (r"fie\s+is\s+accused", "OCR: He is"),
        (r"fie\s+is\s+most\s+likely\s+wounded", "OCR: He is"),
        (r"FI[Ee]\s+book\s+closes", "OCR: THE book"),
        (r"FI[Ee]\s+reporter", "OCR: THE reporter"),
        (r"fie\s+feet,\s+four\s+inches", "OCR: five feet"),
        (r"fie\s+circumscribed", "OCR: be circumscribed"),
        (r"fie\s+alloy\s+the\s+Poles", "OCR: he allow"),
        (r"Fie\s+proposed\s+that\s+the\s+United", "OCR: He proposed"),
        (r"Fie\s+also\s+denied", "OCR: He also"),
        (r"fie\s+must'\s+sell", "OCR: he must"),
        (r"Fie\s+never\s+uses\s+it", "OCR: He never"),
        (r"Fie's\s+one\s+of\s+the\s+classiest", "OCR: He's"),
        (r"fie\s+the\s+battle", "OCR: fight the battle"),
        (r"fie\.\s+the\s+address", "OCR: garbled"),
        (r"fie\s+mayor's\s+committee", "OCR: the mayor's"),
        (r"Fie\.\s+2o", "OCR: Fig. 20"),
        (r"Pee,\s+fie,\s+fo,\s+furry", "fee fi fo fum variant"),
        (r"fie\s+had\s+always\s+hoped", "OCR: he had"),
        (r"Fie\s+expressed\s+every", "OCR: He expressed"),
        (r"Fie\s+was\s+a\s+sociologist", "OCR: He was"),
        (r"Fie\s+was\s+not\s+an\s+ugly", "OCR: He was"),
        (r"Fie\s+hadn't\s+killed", "OCR: He hadn't"),
        (r"fie\s+was\s+ill", "OCR: he was"),
        (r"fie\s+was\s+going\s+to\s+kill", "OCR: he was"),
        (r"fie\s+is\s+pleased", "OCR: He is"),
        (r"Fie\s+has\s+never\s+missed", "OCR: He has"),
        (r"Fie\s+didn't\s+care", "OCR: He didn't"),
        (r"fie\s+was\s+vindicated", "OCR: he was"),
        (r"fie\s+was\s+very\s+tired", "OCR: he was"),
        (r"Fie\s+won't\s+--", "OCR: He won't"),
        (r"fie\s+saw\s+elementary", "OCR: he saw"),
        (r"Fie\s+denied\s+this", "OCR: He denied"),
        (r"fie\s+presented\s+at\s+the\s+White", "OCR: he presented"),
        (r"Fie\s+set\s+out\s+with", "OCR: He set out"),
        (r"fie\s+had\s+never\s+seen", "OCR: he had"),
        (r"Fie\s+claps\s+one\s+hand", "OCR: He claps"),
        (r"FI[Ee]\s+invited", "OCR: THE invited"),
        (r"FI[Ee]\s+could\s+not", "OCR: He could"),
        (r"FI[Ee]\s+has\s+some\s+girl", "OCR: He has"),
        (r"FI[Ee]\s+was\s+raging", "OCR: He was"),
        (r"FI[Ee]\s+NEXT\s+DAY", "OCR: THE NEXT"),
        (r"Fie\s+was\s+later\s+to\s+remind", "OCR: He was"),
        (r"fie\s+said\s+that\s+because", "OCR: he said"),
        (r"fie\s+and\s+the\s+air\s+staff", "OCR: He and the"),
        (r"fie\s+wrote\s+out\s+his\s+name", "OCR: he wrote"),
        (r"fie\s+could\s+stand\s+within", "OCR: he could"),
        (r"Fie\s+sighed\.\s+\"\"", "OCR: He sighed"),
        (r"fie\s+so\s+great,\s+why", "OCR: if he so"),
        (r"Fie\s+likes\s+things", "OCR: He likes"),
        (r"fie\s+smiled\.\s+His\s+voice", "OCR: He smiled"),
        (r"fie\s+was\s+beside\s+us", "OCR: he was"),
        (r"FIe\s+was\s+gunning", "OCR: He was"),
        (r"Fie\s+did\?\s+\"\"\s+She\s+seemed", "OCR: He did"),
        (r"fie\s+had\s+succeeded", "OCR: he had"),
        (r"fie\s+was\s+naked", "OCR: he was"),
        (r"fie\?\s+were\s+away\s+from\s+the\s+White", "OCR: he? were"),
        (r"FI[Ee]\s+had\s+always\s+imagined", "OCR: He had"),
        (r"fie\s+went\s+to\s+Switzerland", "OCR: he went"),
        (r"fie\s+mind\s+reflecting", "OCR: the mind"),
        (r"fie\s+was\s+unable\s+to\s+procure", "OCR: he was"),
        (r"fie\s+did\s+to\s+all\s+of\s+the", "OCR: he did"),
        (r"fie\s+offered\s+an\s+amendment", "OCR: he offered"),
        (r"fie\s+was\s+searched", "OCR: he was"),
        (r"fie\s+added\s+that\s+Mr", "OCR: he added"),
        (r"fie\s+was\s+held\s+for", "OCR: he was"),
        (r"fie\s+added\s+that\s+if\s+reports", "OCR: he added"),
        (r"fie\s+might\s+well\s+ask", "OCR: he might"),
        (r"fie\s+had\s+invested", "OCR: He had"),
        (r"fie\s+who\s+had\s+formerly", "OCR: he who"),
        (r"fie\s+had\s+booked\s+under", "OCR: he had"),
        (r"Fie\s+wants\s+us\s+to\s+write", "OCR: He wants"),
        (r"fie\s+through\s+the\s+door\s+silently", "OCR: file through"),
        (r"Fie\s+made\s+his\s+pack", "OCR: He made"),
        (r"fie\s+would\s+join\s+him", "OCR: he would"),
        (r"fie\s+had\s+looked\s+beyond", "OCR: he had"),
        (r"FI[Ee]\s+could\s+not\s+survive", "OCR: He could"),
        (r"fie\s+had\s+also\s+been\s+arrested", "OCR: He had"),
        (r"fie\.\s+Even\s+Mercedes", "OCR: garbled"),
        (r"fie\s+always\s+did\s+have", "OCR: he always"),
        (r"lit\s+fie\s+village", "OCR: little village"),
        (r"fie\s+in\s+reality", "OCR: this in reality"),
        (r"fie\s+wanted.*certified", "OCR: he wanted"),
        (r"fie\s+had\s+been\s+held\s+up", "OCR: he had"),
        (r"fie\s+was\s+the\s+most\s+extraordinary", "OCR: he was"),
        (r"fie\s+thought\s+of\s+what", "OCR: He thought"),
        (r"fie\s+a\s+nation", "OCR: as a nation"),
        (r"fie\s+deplor", "OCR: he deplored"),
        (r"fie\s+is\s+as\s+hard", "OCR: he is"),
        (r"fie\s+needn't", "OCR: He needn't"),
        (r"FIe\s+wants\s+to\s+hear", "OCR: He wants"),
        (r"fie\s+got\s+it\s+fuckin", "OCR: he got"),
        (r"fie\s+energy\s+that", "OCR: the energy"),
        (r"fie\s+said\s+--\s+but", "OCR: he said"),
        (r"Fie\s+was\s+later", "OCR: He was"),
        (r"Fie\s+insisted", "OCR: He insisted"),
        (r"fie\s+was\s+going\s+down", "OCR: he was"),
        (r"Fie\s+contented\s+himself", "OCR: He contented"),
        (r"fie\s+pulled\s+a\s+pair", "OCR: he pulled"),
        (r"fie\s+says,\s+he\s+will\s+not\s+rest", "OCR: he says"),
        (r"fie\s+lit\s+cigarettes", "OCR: he lit"),
        (r"fie\s+ran\s+toward", "OCR: he ran"),
        (r"fie\s+said\s+those\s+who", "OCR: he said"),
        (r"FI[Ee]\s+throws\s+something", "OCR: He throws"),
        (r"Fie\s+told\s+me\s+that\s+when", "OCR: He told"),
        (r"Fie\s+stood\s+up.*scratching", "OCR: He stood"),
        (r"Fie\s+wondered\s+if", "OCR: He wondered"),
        (r"Fie\s+founded.*testimony", "OCR: He founded"),
        (r"Fie\s+Gibson\s+assured", "OCR: garbled"),
        (r"Fie\s+made\s+no\s+official", "OCR: He made"),
        (r"fie\s+as\s+they\s+were\s+following", "OCR: garbled"),
        (r"Fie\s+will\s+doubtless", "OCR: he will"),
        (r"fie\s+had\s+nothing\s+in\s+his\s+clothing", "OCR: he had"),
        (r"fie\s+V\s+I\s+l\.1", "OCR: garbled"),
        (r"Fie\.\s+9\.\s+Smith", "OCR: Fig. 9"),
        (r"Fie\.\s+18\.", "OCR: Fig. 18"),
        (r"Fie\.\s+19\.", "OCR: Fig. 19"),
        (r"Fie\.\s+53\.", "OCR: Fig. 53"),
        (r"Fie\.\s+54\.", "OCR: Fig. 54"),
        (r"Fie\.\s+60\.", "OCR: Fig. 60"),
        (r"Fie\.\s+77\.", "OCR: Fig. 77"),
        (r"Fie\.\s+82\.", "OCR: Fig. 82"),
        (r"Fie\.\s+135\.", "OCR: Fig. 135"),
        (r"Fie\.\s+8\.5", "OCR: Fig. 8.5"),
        (r"FI[Ee]\s+\*\s+L\s+\*", "OCR: garbled Greek"),
        (r"Fie\.\s+55\.\s+Ancient", "OCR: Fig. 55"),
        (r"Kar4.*FIe\s+\*", "OCR: garbled title"),
        (r"Fie\s+93-", "OCR: Fig. 93"),
        (r"fie\.\s+170\.", "OCR: Fig. 170"),
        (r"fie\s+Gemora", "OCR: the Gemora"),
        (r"dampening\s+fie", "OCR: dampening field (Star Trek)"),
        (r"fie\.\s+Mm-hmm", "OCR: garbled (Crazy Ex)"),
        (r"fie\s+in\s+his\s+gray\s+eyes", "OCR: lie in his gray eyes"),
        (r"fie\s+know\?\s+Harold", "OCR: he know"),
        (r"Fie\s+removed\s+his\s+hand", "OCR: He removed"),
        (r"fie\s+is\s+nailed", "OCR: lie is nailed"),
    ]
    for pat, note in ocr_specific:
        if re.search(pat, ctx, re.IGNORECASE):
            return note

    return None


def is_formulaic(ctx):
    """Fee fi fo fum and variants."""
    lc = ctx.lower()
    if re.search(r"fee[,\s]+fie[,\s]+fo", lc):
        return True
    if re.search(r"fie[,\s]+foh?\b", lc):
        return True
    if re.search(r"fie[,\s]+fo[,\s]+fu", lc):
        return True
    if re.search(r"pee,\s+fie,\s+fo", lc):
        return True
    return False


def is_noun_use(ctx):
    """fie as a noun: 'a fie on/upon X', 'a fie for X'."""
    if re.search(r"\ba\s+fie\s+(?:on|upon|for)\b", ctx, re.IGNORECASE):
        return True
    return False


def is_metalinguistic(ctx):
    """Fie mentioned rather than used."""
    if re.search(r'words\s+like\s+["\']?\s*Fie', ctx, re.IGNORECASE):
        return True
    if re.search(r'the\s+word\s+["\']?fie', ctx, re.IGNORECASE):
        return True
    # Koran translation: "say not to them Fie"
    if re.search(r'say\s+not\s+to\s+them.*Fie', ctx, re.IGNORECASE):
        return True  # Actually this is metalinguistic instruction
    return False


def is_quoted_shakespeare(ctx):
    """Shakespeare quotation in non-fiction or metanarrative."""
    # These are genuine fie uses within the quoted text
    return False


def code_token(ctx):
    """Return (syn, sem, int, note) for a token."""

    # 1. OCR noise
    ocr = is_ocr(ctx)
    if ocr:
        return (0, 0, 0, ocr)

    # 2. Formulaic (fee fi fo fum)
    if is_formulaic(ctx):
        return (1, 0, 0, "Formulaic: fee fi fo fum")

    # 3. Noun use: "a fie on/upon X"
    if is_noun_use(ctx):
        return (0, 1, 0, "Noun: a fie on/upon X")

    # 4. Metalinguistic
    if is_metalinguistic(ctx):
        return (0, 0, 0, "Metalinguistic mention")

    # 5. "fie upon it" / "fie on it" / "fie upon X" in poetry/narrative voice
    #    (not addressed to an interlocutor) — syn=1, sem=1, int=0
    #    But most "fie upon X" IS addressed, so default is 1,1,1

    # 6. Koran "Fie on you and on that ye worship" — genuine interjection in translation
    if re.search(r"Fie\s+on\s+you\s+and\s+on\s+that\s+ye\s+worship", ctx):
        return (1, 1, 1, "Koran translation: genuine interjection")

    # 7. Narrative "fie!" not in dialogue
    #    "Fie! They passed down..." (DrSevier) — narrator's exclamation
    if re.search(r"Fie!\s+They\s+passed\s+down", ctx):
        return (1, 1, 0, "Narrative exclamation, not interactional")

    # 8. "cries fie" / "cry out fie" — fie is object of verb, partially integrated
    if re.search(r"cry\s+out\s+fie|cries?\s+fie", ctx, re.IGNORECASE):
        return (0, 1, 1, "Integrated: object of 'cry out'")

    # 9. "Fie upon your law" (Merchant of Venice) — in character dialogue
    # 10. "Fie on sinful fantasy" (Caliban) — song lyric, expressive

    # 11. "Tee fie!" (DropZone) — baby talk / nonsense
    if re.search(r"Tee\s+fie", ctx):
        return (1, 0, 0, "Baby talk / nonsense syllable")

    # 12. "fie and foe" (Play:FirstFlight) — paired with foe, partial formula
    if re.search(r"fie\s+and\s+foe", ctx, re.IGNORECASE):
        return (1, 1, 1, "Paired interjections: fie and foe")

    # 13. "shame shame fie for shame" (Play:AmIGoIllSaySo) — stream of consciousness
    if re.search(r"shame\s+fie\s+for\s+shame", ctx, re.IGNORECASE):
        return (1, 1, 0, "Stream of consciousness, not interactional")

    # Default: genuine interjection use in dialogue
    # The vast majority of surviving tokens are standalone exclamations
    # or reproaches in character dialogue: syn=1, sem=1, int=1
    return (1, 1, 1, "Genuine interjection: exclamation/reproach in dialogue")


def main():
    tokens = []
    with open(INPUT, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        tokens = list(reader)

    print(f"Coding {len(tokens)} tokens...")

    results = []
    counts = {}
    for token in tokens:
        syn, sem, intj, note = code_token(token["context"])
        results.append({
            "coding_id": token["coding_id"],
            "genre": token["genre"],
            "source": token["source"],
            "context": token["context"],
            "interjection_syn": syn,
            "interjection_sem": sem,
            "interjection_int": intj,
            "notes": note,
        })
        key = note.split(":")[0] if ":" in note else note
        counts[key] = counts.get(key, 0) + 1

    with open(OUTPUT, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "coding_id", "genre", "source", "context",
            "interjection_syn", "interjection_sem", "interjection_int", "notes"
        ])
        writer.writeheader()
        writer.writerows(results)

    print(f"\nCoding distribution:")
    for key, count in sorted(counts.items(), key=lambda x: -x[1]):
        print(f"  {key}: {count}")

    syn1 = sum(1 for r in results if r["interjection_syn"] == 1)
    sem1 = sum(1 for r in results if r["interjection_sem"] == 1)
    int1 = sum(1 for r in results if r["interjection_int"] == 1)
    n = len(results)
    print(f"\nOverall: syn={syn1}/{n} ({100*syn1/n:.1f}%)  sem={sem1}/{n} ({100*sem1/n:.1f}%)  int={int1}/{n} ({100*int1/n:.1f}%)")
    print(f"Output: {OUTPUT}")


if __name__ == "__main__":
    main()
