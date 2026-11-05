"""Apply the 2026-11-05 polarity recode to properties-v4.csv.

Brett, 2026-11-05: "make those fixes" (the fixes listed in
notes/2026-11-05-complement-columns.md, after the determinatives-as-nouns
codebook, planning/codebook.md sections 1, 4 and 6), and "what about the
morphology columns, which include roots. That would link bearers".

Rules adopted from that codebook:
- every column states a possibility; Y needs one admissible instance and
  N means never;
- a property that can't arise is x, a status distinct from U;
- columns whose sense changes are kept as the record (type superseded,
  recoded_as) and replaced by new rows, so no ID changes meaning;
- correlated properties stay separate and are pooled by family.

Adds the columns type, recoded_as, family, claim, x_when. Idempotent: it
refuses to run twice.
"""
import csv
import os

HERE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(HERE, "properties-v4.csv")
rows = list(csv.DictReader(open(PATH, encoding="utf-8")))
fields = list(rows[0].keys())
if "family" in fields:
    raise SystemExit("already recoded")
NEW = ["type", "recoded_as", "family", "claim", "x_when"]
fields += NEW
by = {r["property_id"]: r for r in rows}
for r in rows:
    for f in NEW:
        r[f] = ""
    r["type"] = "possibility"


def note(pid, text):
    by[pid]["notes"] = (by[pid]["notes"] + " " + text).strip()


def blank(**kw):
    r = {f: "" for f in fields}
    r.update(kw)
    return r


# Position family: three possibility claims over one domain.
for pid, claim in [("P01", "may constitute an utterance on its own as a conventional use"),
                   ("P02", "may occur beside a complete clause without entering its construction"),
                   ("P03", "may occur in an argument, complement, or modifier position")]:
    by[pid]["family"] = "POSITION"
    by[pid]["claim"] = claim
    note(pid, "Family POSITION (P01-P03): N on all three is impossible, since a use occurs "
              "somewhere; 'standalone only' (P01 Y, P02 N, P03 N) is a derived joint state, not coded.")
by["P02"]["negative_standard"] = (
    "Source states the use never occurs beside a complete clause without entering its "
    "construction, with the supplement environment addressed. A statement that the use is "
    "always integrated or always standalone supports this N and the matching P01 or P03 value "
    "as one proposition (dependence state: entailed)")

by["P04"].update(family="DEPENDENTS", claim="may take a complement or modifier")
by["P05"].update(family="INFLECTION", claim="may occur in an inflected form (number excluded)")

by["P06"].update(family="NOMINAL", claim="may occur with a determiner or in plural form")
by["P06"]["positive_standard"] += "; the cell records which disjunct supports Y (determiner / plural)"
by["P06"]["negative_standard"] = (
    "Explicit unacceptability statement for the specified use. A conversion analysis is "
    "contrast evidence: U in the primary record, N only in a predeclared sensitivity, as for P08")
note("P06", "Disjunctive, kept whole because it is a shared target.")

by["P07"].update(type="superseded", recoded_as="P07D")
note("P07", "Superseded 2026-11-05: its Y is a never-claim. Recoded as P07D with values "
            "reversed (old Y = P07D N; old N = P07D Y), which converts mechanically.")

by["P08"].update(family="STANCE", claim="may convey evaluative or affective content")

by["P09"].update(family="DEPICTION",
                 claim="may depict through resemblance between performance and what is depicted")
by["P09"]["negative_standard"] = ("Source states the use doesn't depict through resemblance "
                                  "(a statement that it is non-iconic counts)")

by["P10S"].update(family="REPETITION", claim="may strengthen the same contribution when repeated in the pattern",
                  x_when="P10A = N for the pattern (repetition unavailable)")
by["P10S"]["negative_standard"] = ("Source states repetition in the pattern never strengthens the "
                                   "contribution (for example, is redundant)")
note("P10S", "N narrowed 2026-11-05: unavailability is now x through P10A, not N "
             "(FREEZE section 6, P10: four evidence fields).")
by["P10M"].update(family="REPETITION", claim="may multiply depicted events when repeated in the pattern",
                  x_when="P10A = N for the pattern")

by["P11N"].update(type="superseded", recoded_as="P11E")
note("P11N", "Superseded 2026-11-05: Y needed one wide-scope example, which gives no 'never', "
             "and Y and N could both hold of one use. Recoded as P11E. Not convertible mechanically: "
             "old N becomes P11E Y; old Y becomes U unless the source states the wide reading is forced.")

by["P12"].update(type="superseded", recoded_as="P12S;P12I")
note("P12", "Superseded 2026-11-05: N ('characteristic integration') was a typical-case claim, "
            "not 'never'. Recoded as P12S (the hosted target) and P12I.")

by["P13"].update(family="PHONOLOGY",
                 claim="may have a conventional form with sounds outside ordinary English word phonology")
by["P14"]["type"] = "descriptor"

new_rows = [
    blank(property_id="P07D", name="DESCRIPTIVE", group="meaning", values="Y/N/U",
          intj_role="diagnostic", expr_role="diagnostic", tiers="A",
          positive_standard="Source assigns ordinary descriptive or truth-conditional content to the specified use (one admissible instance)",
          negative_standard="Source states the use makes no contribution to descriptive or truth-conditional content",
          notes="Possibility form of P07, values reversed; its sign is negative for both groupings. Shared diagnostic of INTJ and EXPRESSIVE; both keep a no-P07 sensitivity. Mixed items are Y (Gutzmann 2013, p. 10, intensifier fucking).",
          type="possibility", family="TRUTH_CONDITIONAL", claim="may contribute descriptive or truth-conditional content"),
    blank(property_id="P10A", name="REPEATABLE", group="meaning", values="Y/N/U + pattern",
          intj_role="descriptor", expr_role="descriptor", tiers="A",
          positive_standard="Source states or exemplifies the use repeated in the specified pattern",
          negative_standard="Source states the pattern is unavailable for the use",
          notes="Gate for P10S, P10M and P10R: where P10A = N for a pattern, they are x for it. Pattern recorded as for P10S.",
          type="possibility", family="REPETITION", claim="may be repeated in the pattern"),
    blank(property_id="P10R", name="REPETITION_REDUNDANT", group="meaning", values="Y/N/U + pattern",
          intj_role="descriptor", expr_role="descriptor", tiers="A",
          positive_standard="Source states or exemplifies repetition of the use in the pattern adding nothing (redundant)",
          negative_standard="Source states repetition in the pattern is never redundant",
          notes="FREEZE section 6, P10: more than one of strengthening, multiplication and redundancy may be supported.",
          type="possibility", family="REPETITION", claim="may be repeated in the pattern with no added effect",
          x_when="P10A = N for the pattern"),
    blank(property_id="P11E", name="EMBEDDABLE_UNDER_NEGATION", group="meaning", values="Y/N/U + host",
          intj_role="target", expr_role="diagnostic", tiers="A",
          positive_standard="Source states or exemplifies the specified contribution interpreted inside the scope of negation of a host clause (one admissible reading)",
          negative_standard="Source states the contribution is never interpreted in the scope of host negation: the wide reading is forced (Potts 2007, p. 172)",
          notes="Replaces P11N. N is the expressive value, so its sign is negative for EXPRESSIVE. Host relation recorded: integrated / external co-utterance / independent adjacent turn. Whether an independent adjacent turn counts as a host is open for Brett (FREEZE section 13).",
          type="possibility", family="TRUTH_CONDITIONAL",
          claim="may be interpreted inside the scope of host negation",
          x_when="no host environment of any recorded relation; derived from the host record and the POSITION family, never coded"),
    blank(property_id="P12S", name="PROSODY_SEPARATE", group="realization", values="Y/N/U",
          intj_role="target", expr_role="target", tiers="A;B",
          positive_standard="Source reports, or audio shows, a separate intonation unit when the use occurs with a host",
          negative_standard="Source states, or audio across the use's hosted occurrences shows, that it is never set off intonationally when hosted",
          notes="Replaces P12 as the hosted-prosody target. A standalone utterance boundary is not the target observation.",
          type="possibility", family="PROSODY", claim="may form a separate intonation unit when hosted",
          x_when="no host environment"),
    blank(property_id="P12I", name="PROSODY_INTEGRATED", group="realization", values="Y/N/U",
          intj_role="descriptor", expr_role="descriptor", tiers="A;B",
          positive_standard="Source reports, or audio shows, intonational integration with a host",
          negative_standard="Source states the use is never intonationally integrated when hosted",
          notes="With P12S, gives three joint states: always separate, always integrated, either.",
          type="possibility", family="PROSODY", claim="may be intonationally integrated with a host",
          x_when="no host environment"),
]
# Relatedness facts (roots and word form), drafted by rule in morphology-facts-v4.csv.
for pid, name, claim in [
        ("MB_DAMN", "BASE_damn", "contains the free form damn"),
        ("MB_BLOODY", "BASE_bloody", "contains the free form bloody"),
        ("MB_BASTARD", "BASE_bastard", "contains the free form bastard"),
        ("MB_BANG", "BASE_bang", "contains the free form bang"),
        ("MB_THE", "BASE_the", "contains the free form the"),
        ("MB_YOU", "BASE_you", "contains the free form you"),
        ("MW_LY", "SUFFIX_ly", "ends in the suffix -ly"),
        ("MW_PHRASAL", "PHRASAL", "is written as more than one word"),
        ("MW_REDUP", "REDUPLICATED", "is a reduplicated form"),
        ("MW_SUBWORD", "SUBWORD", "is inserted inside a word")]:
    new_rows.append(blank(
        property_id=pid, name=name, group="morphology", values="Y/N (by rule)",
        intj_role="relatedness", expr_role="relatedness", tiers="form",
        positive_standard=f"The row's form {claim} (string identity; see morphology-facts-v4.csv)",
        negative_standard="The row's form does not",
        notes="Fact of form drafted by rule, for Brett to approve; no m. Links bearers: never a diagnostic or target. Pooled by base; the tests run with and without these columns (determinatives-as-nouns codebook section 1).",
        type="relatedness", family="FORM_BASE" if pid.startswith("MB") else "FORM_WORD", claim=claim))
# P07D and P11E join the TRUTH_CONDITIONAL family; insert the new rows after the rows they replace.
order = []
after = {"P07": ["P07D"], "P10M": ["P10A", "P10R"], "P11N": ["P11E"], "P12": ["P12S", "P12I"]}
newby = {r["property_id"]: r for r in new_rows}
for r in rows:
    order.append(r)
    for pid in after.get(r["property_id"], []):
        order.append(newby.pop(pid))
order += list(newby.values())
with open(PATH, "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=fields)
    w.writeheader()
    w.writerows(order)
print(len(order), "rows written")
