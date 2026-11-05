"""Correction layer for the discarded target-evidence audit (2026-11-04).

Approved by Brett Reynolds 2026-11-04 (P0 to P1 pass in
TRIAGE-2026-11-04-external-review.md). Reads the pre-correction verdicts
(pre-correction-2026-11-04/semantic-verdicts.json) and mechanical results
(audit-results.json, untouched), writes:

- semantic-verdicts.json (v2): original verdict and note preserved per
  assertion, plus an `effective` field block, a canonical proposition
  ID, and a correction note wherever the effective reading differs.
- proposition-map.json: hand-reviewed assertion to proposition map.

Original coder records are never modified. Re-running this script
reproduces both outputs from the preserved pre-correction inputs.
"""
import json
from pathlib import Path

BASE = Path("analysis/matrix-lesion/target-audit")
OLD = json.loads((BASE / "pre-correction-2026-11-04"
                  / "semantic-verdicts.json").read_text())["verdicts"]
RES = json.loads((BASE / "audit-results.json").read_text())

ASSERT = {}
for key, by_fam in RES["pairs"].items():
    prop, item = key.split("/")
    for fam, rec in by_fam.items():
        if not isinstance(rec, dict):
            continue
        for a in rec.get("valid_assertions", []):
            ASSERT[f"{fam}|{prop}|{item}|{a.get('assertion_id')}"] = a

# --- canonical propositions (hand-reviewed; see proposition-map.json) ---
PROP = {
    "agy|P10|DAMN_PRENOM|a1": "PROP-P10-POTTS-34",
    "claude|P10|DAMN_PRENOM|P10-DAMNPRENOM-A1": "PROP-P10-POTTS-34",
    "claude|P10|DAMN_PRENOM|P10-DAMNPRENOM-A2": "PROP-P10-POTTS-34",
    "copilot|P10|DAMN_PRENOM|potts-34-adjacrep-strength": "PROP-P10-POTTS-34",
    "copilot|P10|DAMN_PRENOM|potts-34-no-redundancy": "PROP-P10-POTTS-34",
    "qwen|P10|DAMN_PRENOM|A1": "PROP-P10-POTTS-34",
    "claude|P10|DAMN_REACT|P10-DAMNREACT-A1": "PROP-P10-POTTS-34",
    "claude|P10|DAMN_REACT|P10-DAMNREACT-A2": "PROP-P10-POTTS-34",
    "copilot|P10|DAMN_REACT|potts-adj-repeat-strengthen": "PROP-P10-POTTS-34",
    "qwen|P10|DAMN_REACT|A1": "PROP-P10-POTTS-34",
    "agy|P10|OKAY|ast-quirk-okay-p10": "PROP-P10-QUIRK-EMPH",
    "claude|P10|OKAY|P10-OKAY-A1": "PROP-P10-QUIRK-EMPH",
    "copilot|P10|HUH|A1-huh-adjacent-rep": "PROP-P10-DING-HUH",
    "copilot|P10|WOW|A1-wow-adjacent-rep": "PROP-P10-STANGE-WHOA65",
    "qwen|P10|WOW|A1": "PROP-P10-STANGE-WHOA65",
    "claude|P11|DAMN_REACT|A-P11-DAMN_REACT-1": "PROP-P11-CGEL-SCOPE",
    "claude|P11|OUCH|A-P11-OUCH-2": "PROP-P11-CGEL-SCOPE",
    "agy|P11|OUCH|ast-ouch-p11-cgel-01": "PROP-P11-CGEL-SCOPE",
    "claude|P11|WOW|A-P11-WOW-1": "PROP-P11-CGEL-SCOPE",
    "claude|P11|COFFEE|A-P11-COFFEE-1": "PROP-P11-CGEL-OR",
    "claude|P11|OUCH|A-P11-OUCH-1": "PROP-P11-HEINE-NEG",
    "agy|P11|OUCH|ast-ouch-p11-heine-01": "PROP-P11-HEINE-NEG",
    "copilot|P11|DAMN_REACT|A2-Potts-nondisplaceability-negation":
        "PROP-P11-POTTS-TENSE",
    "copilot|P11|GEE|A1": "PROP-P11-GEHWEILER-NEGEVAL",
    "copilot|P11|GEE|A3": "PROP-P11-GEHWEILER-NEGEVAL",
    "copilot|P11|WOW|A2-cgel-supplement": "PROP-P11-CGEL-BASELINE",
    "copilot|P11|OKAY|A1": "PROP-P11-OKAY-POLARITY",
    "copilot|P11|OUCH|A2": "PROP-P11-KAPLAN-NEG",
    "agy|P12|BANG_DEPICT|ast-bang-depict-p12-01": "PROP-P12-HEINE-SETOFF",
    "claude|P12|DAMN_REACT|DAMNR-BEH1": "PROP-P12-HEINE-SETOFF",
    "copilot|P12|DAMN_REACT|A3-class-inherited-prosodic-isolation":
        "PROP-P12-HEINE-SETOFF",
    "claude|P12|GEE|GEE-BEH1": "PROP-P12-HEINE-SETOFF",
    "agy|P12|HUH|ast_p12_huh_rec_01": "PROP-P12-HEINE-SETOFF",
    "agy|P12|HUH|ast_p12_huh_att_01": "PROP-P12-HEINE-SETOFF",
    "copilot|P12|MMHM|A3": "PROP-P12-HEINE-SETOFF",
    "claude|P12|OUCH|OUCH-BEH1": "PROP-P12-HEINE-SETOFF",
    "copilot|P12|OUCH|Heine-prosodic-class": "PROP-P12-HEINE-SETOFF",
    "claude|P12|WOW|WOW-BEH2": "PROP-P12-HEINE-SETOFF",
    "agy|P12|WOW|ast-p12-wow-pos": "PROP-P12-HEINE-LEFTPERIPH",
    "qwen|P12|WOW|A1": "PROP-P12-HEINE-LEFTPERIPH",
    "claude|P12|WOW|WOW-BEH1": "PROP-P12-WHARTON",
    "agy|P12|WOW|ast-p12-wow-rec": "PROP-P12-WHARTON",
    "agy|P12|WOW|ast-p12-wow-cat": "PROP-P12-WHARTON",
    "agy|P12|OUCH|ast-ouch-p12-001": "PROP-P12-ANDRASON",
    "qwen|P12|DAMN_REACT|assert_01": "PROP-P12-CGEL-ADVERB",
    "copilot|P12|OUCH|CGEL-supp-host": "PROP-P12-CGEL-SUPPOCC",
    "qwen|P12|BLOODY_PRENOM|a1": "PROP-P12-BLOODY-HOSTFORM",
    "qwen|P12|MMHM|A1": "PROP-P12-MMHM-CONTOUR",
}

# --- effective-field overrides (everything else defaults to coder fields).
# Each entry: field -> corrected value, plus _why (becomes correction_note).
CGEL_BASIS = ("Brett scope ruling 2026-11-04: CGEL Ch.15 p.1360 "
              "supplement properties are general to supplements, "
              "interjections included, despite preceding subsection (i).")
OVERRIDES = {
    "copilot|P10|HUH|A1-huh-adjacent-rep": {
        "effect_dimension": "none-stated-occurrence-only",
        "_why": "Verdict states occurrence only; event-multiplication "
                "was a coder label with no source-stated effect."},
    "agy|P10|OKAY|ast-quirk-okay-p10": {
        "repetition_pattern": "unclear",
        "effect_dimension": "strengthening",
        "_why": "Quirk note [b] and section 18.58 state repetition for "
                "emphasis without pinning the OK claim to adjacent "
                "repetition. Pattern unspecified; strengthening stands."},
    "claude|P10|OKAY|P10-OKAY-A1": {
        "repetition_pattern": "unclear",
        "effect_dimension": "strengthening",
        "_why": "Quirk note [b] and section 18.58 state repetition for "
                "emphasis without pinning the OK claim to adjacent "
                "repetition. Pattern unspecified; strengthening stands."},
    "copilot|P10|WOW|A1-wow-adjacent-rep": {
        "verdict": "reject",
        "use_status": "wrong-use",
        "effect_dimension": "none-stated-occurrence-only",
        "_why": "Stange 2016 ch.4 Side note 1, ex. (65) headed 'Whoa! "
                "spelt Wow!': source discards this token as whoa (stop). "
                "Wrong use for WOW amazement reaction; original strict "
                "pass and strengthening label void. Context was in packet."},
    "qwen|P10|WOW|A1": {
        "verdict": "reject",
        "use_status": "wrong-use",
        "effect_dimension": "none-stated-occurrence-only",
        "_why": "Same Stange (65) whoa token as the Copilot assertion; "
                "source discards it as whoa (stop). Wrong use; original "
                "pass-weak and inferred strengthening void."},
    "agy|P11|OUCH|ast-ouch-p11-heine-01": {
        "host_relationship": "no-host",
        "_why": "Attempted direct negation of standalone Ouch has no "
                "host proposition. Adjudicated to no-host, matching the "
                "Claude coding of identical Heine evidence; integrated "
                "label removed so one observation yields one unit."},
    "agy|P12|WOW|ast-p12-wow-cat": {
        "claim_strength": "recurrent-characteristic",
        "_why": "Categorical slice of Wharton sentence hedged by 'rarely "
                "integrated'; merged at recurrent strength, matching "
                "the passing recurrent slice of the same proposition."},
    "qwen|P12|WOW|A1": {
        "support_type": "class-inherited",
        "_why": "Support type aligned with the pre-existing "
                "effective_contribution correction: Heine proposition "
                "is class-level, not item-specific."},
    "agy|P12|OUCH|ast-ouch-p12-001": {
        "claim_strength": "attested-possible",
        "_why": "Andrason and Dlali claim is cross-linguistic and "
                "comparative; categorical English strength overclaimed. "
                "Attested-possible records the claim without asserting "
                "characteristic English behaviour."},
}
for k in ("claude|P11|DAMN_REACT|A-P11-DAMN_REACT-1",
          "claude|P11|OUCH|A-P11-OUCH-2",
          "agy|P11|OUCH|ast-ouch-p11-cgel-01",
          "claude|P11|WOW|A-P11-WOW-1"):
    OVERRIDES.setdefault(k, {})["_basis"] = CGEL_BASIS


PROPOSITIONS = {
    "PROP-P10-POTTS-34": {
        "property": "P10", "status": "live",
        "statement": "Potts 2007 sec.2.6: for expressives, repetition "
                     "leads to strengthening rather than redundancy; "
                     "ex. (34) accumulates standalone Damn plus "
                     "prenominal damn (mixed positions).",
        "source": "Potts - 2007 - The expressive dimension.md",
        "note": "One proposition and one mixed-position example. Five "
                "assertions pass on it; five adjacent-repetition "
                "miscodings of it are rejected. Not two within-use "
                "effects."},
    "PROP-P10-QUIRK-EMPH": {
        "property": "P10", "status": "live",
        "statement": "Quirk et al. 1985 note [b] pp.982-983: expressions "
                     "like yes, no, well, OK, all right are often "
                     "repeated for emphasis (cf. 18.58).",
        "source": "quirk-et-al-1985-comprehensive-grammar-of-the-"
                  "english-language.md",
        "note": "Effect (emphasis/strengthening) explicit. Pattern "
                "unspecified: 18.58 covers adjacent reiteration and "
                "non-adjacent reinforcement."},
    "PROP-P10-DING-HUH": {
        "property": "P10", "status": "live-occurrence-only",
        "statement": "Dingemanse 2024 transcript token with adjacent "
                     "Huh? Huh? occurrence; no effect stated.",
        "source": "dingemanse_2024_interjections-heart-of-language.md",
        "note": "Occurrence evidence only. No effect dimension may be "
                "derived from it."},
    "PROP-P10-STANGE-WHOA65": {
        "property": "P10", "status": "rejected-wrong-use",
        "statement": "Stange 2016 ch.4 Side note 1 ex. (65) 'Whoa! "
                     "spelt Wow!': Teresa token discarded by source as "
                     "whoa meaning stop.",
        "source": "stange_2016_emotive-interjections-ch4.md",
        "note": "Both assertions on this token rejected as wrong use "
                "for WOW amazement reaction. Full context was present "
                "in packets-v3."},
    "PROP-P11-CGEL-SCOPE": {
        "property": "P11", "status": "live-inherited-single-proposition",
        "statement": "CGEL Ch.15 p.1360: supplements do not fall "
                     "within the scope of negatives in the anchor.",
        "source": "00-CGEL.md",
        "note": CGEL_BASIS + " Inherited by DAMN_REACT, OUCH, WOW. "
                "One proposition, one outcome direction, no "
                "within-target contrast."},
    "PROP-P11-CGEL-OR": {
        "property": "P11", "status": "live-control-separate-unit",
        "statement": "CGEL: subclausal or-coordination within scope "
                     "of a negative (tea or coffee).",
        "source": "00-CGEL.md",
        "note": "Integrated descriptive content. Control for a "
                "different unit; not contrast for external "
                "evaluative stance."},
    "PROP-P11-HEINE-NEG": {
        "property": "P11", "status": "live-separate-unit",
        "statement": "Heine 2023 ch.1 Table 1.4: interactives cannot "
                     "normally be negated; English Ouch! vs "
                     "#Not/don't ouch!",
        "source": "heine_2023_grammar-of-interactives_ch1.md",
        "note": "Attempted direct negation, no host. Distinct from "
                "anchor-negation scope survival."},
    "PROP-P11-POTTS-TENSE": {
        "property": "P11", "status": "rejected",
        "statement": "Potts scope wording concerning tense operators.",
        "source": "Potts - 2007 - The expressive dimension.md",
        "note": "Rejected: not negation evidence."},
    "PROP-P11-GEHWEILER-NEGEVAL": {
        "property": "P11", "status": "rejected",
        "statement": "Gehweiler on gee in negative-evaluation contexts.",
        "source": "(packet excerpt)",
        "note": "Rejected: negative evaluation is not linguistic "
                "negation."},
    "PROP-P11-CGEL-BASELINE": {
        "property": "P11", "status": "rejected",
        "statement": "CGEL baseline description of wow as supplement.",
        "source": "00-CGEL.md",
        "note": "Rejected as P11 evidence: no negation content."},
    "PROP-P11-OKAY-POLARITY": {
        "property": "P11", "status": "downgraded-adjacent",
        "statement": "Response elicitors lack affirmative counterparts.",
        "source": "(packet excerpt)",
        "note": "Downgraded: negation behaviour inferred, not stated."},
    "PROP-P11-KAPLAN-NEG": {
        "property": "P11", "status": "downgraded-adjacent",
        "statement": "Kaplan on negation of expressive content.",
        "source": "(packet excerpt)",
        "note": "Downgraded: class-inclusion link to ouch "
                "context-only."},
    "PROP-P12-HEINE-SETOFF": {
        "property": "P12", "status": "live-inherited-contested",
        "statement": "Heine 2023 ch.1 (incl. Zwicky on discourse "
                     "markers): interactives typically/likely set off "
                     "prosodically from surrounding text.",
        "source": "heine_2023_grammar-of-interactives_ch1.md",
        "note": "Hosted specificity weak. Contested within same "
                "section by PROP-P12-HEINE-QUAL, absent from "
                "packets-v3."},
    "PROP-P12-HEINE-LEFTPERIPH": {
        "property": "P12", "status": "live-inherited-contested",
        "statement": "Heine 2023 ch.1: most interactives can occur at "
                     "left periphery, prosodically separated from what "
                     "follows.",
        "source": "heine_2023_grammar-of-interactives_ch1.md",
        "note": "Attested-possible slices. Same qualification caveat "
                "as PROP-P12-HEINE-SETOFF."},
    "PROP-P12-WHARTON": {
        "property": "P12", "status": "live-inherited",
        "statement": "Wharton via Heine: interjections at utterance "
                     "edges separated from main clause, rarely "
                     "integrated into intonational units.",
        "source": "heine_2023_grammar-of-interactives_ch1.md",
        "note": "Second-hand lineage. Categorical slice corrected to "
                "recurrent. Only strict-pass P12 lineage (WOW)."},
    "PROP-P12-ANDRASON": {
        "property": "P12", "status": "live-inherited-weakened",
        "statement": "Andrason and Dlali via Heine: interjections "
                     "produced in isolation from accompanying clauses, "
                     "independent intonation units (comparative).",
        "source": "heine_2023_grammar-of-interactives_ch1.md",
        "note": "Strength corrected categorical to attested-possible "
                "for English OUCH."},
    "PROP-P12-HEINE-QUAL": {
        "property": "P12", "status": "qualifying-counterevidence",
        "statement": "Heine 2023 ch.1 lines 247-249: prosodic "
                     "boundaries may be weakened or disappear entirely; "
                     "O'Connell et al. 45% without pauses; Biber et "
                     "al. English inserts tend to attach prosodically "
                     "to larger structure.",
        "source": "heine_2023_grammar-of-interactives_ch1.md",
        "note": "No coder assertions (absent from packets-v3). "
                "Qualifies SETOFF and LEFTPERIPH strengths; coded "
                "here at proposition level under P1-7, not as "
                "fabricated assertions."},
    "PROP-P12-CGEL-ADVERB": {
        "property": "P12", "status": "rejected",
        "statement": "CGEL intonational separation for medial adverb "
                     "supplement, miscoded to Damn.",
        "source": "00-CGEL.md",
        "note": "Rejected: wrong bearer."},
    "PROP-P12-CGEL-SUPPOCC": {
        "property": "P12", "status": "rejected",
        "statement": "CGEL supplementary occurrence of ouch with hosts.",
        "source": "00-CGEL.md",
        "note": "Rejected as prosody evidence: no separation stated."},
    "PROP-P12-BLOODY-HOSTFORM": {
        "property": "P12", "status": "rejected",
        "statement": "Attested hosted form of bloody prenominal.",
        "source": "(packet excerpt)",
        "note": "Rejected: passages describe no prosodic separation."},
    "PROP-P12-MMHM-CONTOUR": {
        "property": "P12", "status": "downgraded-adjacent",
        "statement": "Continuer token high-low contour in storytelling.",
        "source": "(packet excerpt)",
        "note": "Downgraded: own contour, not host separation."},
}


def default_effect(prop, a):
    eff = {"verdict": None,  # filled from original verdict
           "contribution": a.get("availability_contribution"),
           "support_type": a.get("support_type"),
           "claim_strength": a.get("supported_claim_strength"),
           "use_status": "as-specified"}
    if prop == "P10":
        val = str(a.get("supported_value") or "").casefold()
        if "not redundancy" in val or "distinct from redundancy" in val:
            effect = "redundancy"
        elif "redundancy" in val:
            effect = "redundancy"
        elif "strengthening" in val or "emphasis" in val:
            effect = "strengthening"
        elif "event" in val:
            effect = "event-multiplication"
        else:
            effect = "none-stated-occurrence-only"
        pos = a.get("repetition_positions")
        if isinstance(pos, list):
            pos = "+".join(pos) if pos else None
        eff.update({"repetition_pattern": a.get("repetition_pattern"),
                    "repetition_positions": pos,
                    "effect_dimension": effect})
    if prop == "P11":
        eff.update({"contribution_assessed": a.get("contribution_assessed"),
                    "host_relationship": a.get("host_relationship")})
    return eff


def main():
    out = {}
    for key, rec in OLD.items():
        fam, prop, item, aid = key.split("|", 3)
        a = ASSERT[key]
        eff = default_effect(prop, a)
        eff["verdict"] = rec["verdict"]
        if rec.get("effective_contribution"):
            eff["contribution"] = rec["effective_contribution"]
        ov = OVERRIDES.get(key, {})
        why = ov.pop("_why", None) if ov else None
        basis = ov.pop("_basis", None) if ov else None
        if ov:
            eff.update(ov)
        new = {"verdict": rec["verdict"], "note": rec["note"],
               "effective": eff, "canonical_proposition": PROP[key]}
        if rec.get("effective_contribution"):
            new["effective_contribution"] = rec["effective_contribution"]
        if why:
            new["correction_note"] = why
        if basis:
            new["scope_basis"] = basis
        out[key] = new
    assert len(out) == 48 and set(PROP) == set(out)
    doc = {
        "_note": ("Model semantic verdicts on mechanically valid "
                  "ITEM-DIRECT/CLASS-INHERITED/CONFLICT assertions. "
                  "No human adjudication has been performed as of "
                  "2026-11-04 (confirmed by Brett Reynolds); the "
                  "pre-correction file's 'Human (orchestrator)' label "
                  "was incorrect. Original verdicts are model-produced; "
                  "the exact original model route is not recorded in "
                  "the artifacts. Correction layer (effective fields, "
                  "canonical propositions) applied 2026-11-04 under the "
                  "Brett-approved P0 to P1 pass; original verdict and "
                  "note preserved per assertion. Human adjudication "
                  "under FREEZE-v2 section 7 remains outstanding. "
                  "Effective verdicts: 14 pass, 17 pass-weak, "
                  "3 downgrade, 14 reject (two WOW P10 verdicts moved "
                  "to reject as wrong use)."),
        "verdicts": out}
    (BASE / "semantic-verdicts.json").write_text(
        json.dumps(doc, indent=1, ensure_ascii=False) + "\n")
    print("wrote semantic-verdicts.json:", len(out), "records")
    members = {}
    for key, pid in sorted(PROP.items()):
        members.setdefault(pid, []).append(key)
    pmap = {"_note": ("Hand-reviewed canonical proposition map, "
                      "2026-11-04 correction pass. Replaces quote-prefix "
                      "clustering, which split single propositions. "
                      "Members are verdict keys in "
                      "semantic-verdicts.json."),
            "propositions": {
                pid: {**meta, "members": members.get(pid, [])}
                for pid, meta in PROPOSITIONS.items()}}
    (BASE / "proposition-map.json").write_text(
        json.dumps(pmap, indent=1, ensure_ascii=False) + "\n")
    print("wrote proposition-map.json:", len(PROPOSITIONS),
          "propositions")


if __name__ == "__main__":
    main()
