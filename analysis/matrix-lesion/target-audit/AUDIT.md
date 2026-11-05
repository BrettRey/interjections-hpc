# Target-evidence audit: report (corrected 2026-11-04)

Status: run 2026-11-04 under `DESIGN.md`; discarded development data
under `FREEZE-v2.md` section 9. Nothing here is a study cell, and no
source-target association, category assignment, or lesion was computed
from it. Aggregation covers evidence availability and assertion
structure only.

Correction pass: this report replaces the same-day pre-correction
report after external review (`TRIAGE-2026-11-04-external-review.md`,
adopted in full) and the Brett-approved P0 to P1 correction pass.
Pre-correction artifacts are preserved in
`pre-correction-2026-11-04/`. Units are now derived from adjudicated
effective fields (`semantic-verdicts.json` v2,
`apply_corrections_2026_11_04.py`), propositions from the
hand-reviewed `proposition-map.json`, and bounded source-coverage
checks are recorded in `COVERAGE-2026-11-04.md`. Regression tests:
`analysis/tests/test_target_audit_finalize.py` (7 tests, passing;
all 7 fail against the pre-correction outputs).

Attribution correction: the pre-correction report described semantic
review as human. No human adjudication has been performed (confirmed
by Brett Reynolds, 2026-11-04). All semantic verdicts, original and
corrected, are model review. The exact original model route is not
recorded in the artifacts. Human adjudication under `FREEZE-v2.md`
section 7 remains outstanding, and no claim below rests on human
validation.

## What was run

- Twelve items (`sample.csv`) by three property silos: P10 repetition
  patterns and effect dimensions, P11 behaviour under negation only,
  and hosted P12 prosodic separation by claim strength. Thirty-six
  item-property pairs, property-siloed packets (`packets-v3.json`,
  roughly 10-12k characters each).
- Four coder routes, each blind to the other properties and to any
  hypothesis: Muse subagents (one fresh subagent per property;
  non-independent of the orchestrator, recorded as such), Copilot CLI,
  Agy CLI, and local Qwen (`qwen3.8:27b`, digest recorded per pair,
  temperature 0). Underlying models behind the Agy and Copilot routes
  are not exposed by those CLIs; `meta-*.json` records CLI version,
  prompt and packet hashes, timing, and exit status for every pair.
- Mechanical verification of every output (`analyze_audit.py`):
  JSON parse, exact identifiers, schema fields and controlled values,
  quote length (max 300 characters) and continuity against the pair's
  own packet. Defects split into fatal (assertion voided) and minor
  recoverable (recorded, not voiding: an item_id uniquely denoting the
  pair after case/punctuation normalization, a quote matching only
  after case folding, an unlocatable cited line when the quote
  verifies). An ambiguous bare form stays fatal.
- Model semantic review of every mechanically valid ITEM-DIRECT,
  CLASS-INHERITED, or CONFLICT assertion (`semantic-verdicts.json`;
  verdicts pass / pass-weak / downgrade / reject, each with a note,
  structured effective fields, and a canonical proposition ID).
  Availability is aggregated with and without pass-weak assertions
  (`finalize_audit.py`, `AUDIT-tables.md`, `audit-final.json`), with
  units derived from effective fields.

## Execution incidents that bound interpretation

- The Agy route exhausted its account quota mid-queue (HTTP 429,
  reset in about 155 hours at the time). Final Agy coverage is 18 of
  36 pairs; the 18 raw files preserve the error. Every pair retains at
  least the Copilot and Muse codings, so pair-level availability is
  still estimable, but Agy contributes no evidence for half the pairs
  and cross-family agreement involving Agy covers only those 18.
- The original local-Qwen queue had no output bound and produced an
  18 KB single-assertion response taking 1015 s. The remaining pairs
  were completed with `num_predict=5000` added (`run_qwen_bounded.py`,
  recorded in meta); prompts and all other settings are identical.
- Agy's remaining queue was run six-wide (`run_agy_parallel.py`) with
  identical prompts and outputs; only scheduling changed. This is how
  the quota limit was reached quickly rather than slowly, which does
  not change the total usable output.
- Model semantic review missed a disqualifying use-identity context
  that was present in its packet (Stange example (65), see P10 below)
  and issued a strict pass. Strict-pass status in this audit is
  therefore model confidence, not validated correctness. Production
  adjudication sampling must include unanimous and strict-pass cells,
  as `FREEZE-v2.md` section 7 already requires.

## Results

Coverage: Muse 36/36 pairs, Copilot 36/36, Qwen 36 files (35
parseable; P11 BANG_DEPICT returned a one-character response), Agy
18/36 (quota). Of 129 raw assertions, 89 survived mechanical
verification (Muse 37/37, Agy 16/17, Qwen 15/21, Copilot 21/54, of
which only 8 strictly clean). Ninety-seven defects were logged, 90 of
them Copilot's (53 fatal, mostly discontinuous quotes, wrong
identifiers and off-enum values; 37 minor). All 48 mechanically valid
ITEM-DIRECT, CLASS-INHERITED or CONFLICT assertions received a model
semantic verdict. Original verdicts: 15 pass, 18 pass-weak, 3
downgraded to ADJACENT-ONLY, 12 rejected. Effective verdicts after
correction: 14 pass, 17 pass-weak, 3 downgrade, 14 reject (both P10
WOW verdicts moved to reject as wrong use). No coder proposed
INAPPLICABLE or CONFLICT that survived, and none flagged
RETRIEVAL-FAILURE-SUSPECTED. Raw pair-level agreement between families
ran 55-72% on shared pairs. Full tables: `AUDIT-tables.md`;
pair-level detail: `audit-final.json`; propositions:
`proposition-map.json`.

Pair-level availability after both checks (best surviving class across
families; including pass-weak, with strict pass-only in brackets):

- **P10 repetition:** ITEM-DIRECT 4 [2], SILENCE 8 [10], nothing
  inherited or merely adjacent. The four are the two *damn* rows,
  OKAY, and HUH. Behind them stand three live source propositions:
  Potts (2007, section 2.6) on repetition strengthening rather than
  redundancy, exemplified by mixed-position accumulation retaining
  standalone *Damn* while prenominal occurrences accumulate (one
  proposition and one example carrying both *damn* rows; units
  `distributed-recurrence[mixed]|strengthening` and `...|redundancy`,
  2 items each); Quirk et al. on OK repeated for emphasis
  (strengthening supported, repetition pattern unspecified even after
  checking section 18.58; unit `unclear|strengthening`, 1 item); and
  one transcript token (Dingemanse's *Huh? Huh?*) attesting adjacent
  occurrence with no stated effect (unit
  `adjacent-repetition|none-stated-occurrence-only`, 1 item). There
  is no support for adjacent-repetition strengthening, event
  multiplication, lengthening, or lexicalized reduplication in this
  sample. The pre-correction event-multiplication and
  adjacent-strengthening units were coder labels contradicted by
  their own verdict notes. BANG_DEPICT, the item where event
  multiplication was most plausible, is SILENCE. Five of ten
  mechanically valid P10 *damn* assertions miscoded Potts's
  distributed accumulation as adjacent repetition and were rejected.
  WOW is SILENCE after correction: both assertions coded Stange's
  example (65), which the source heads "Whoa! spelt Wow!" and
  discards as *whoa* meaning stop. That token is the wrong use for
  the amazement-reaction row, and its full context was present in the
  packet.
- **P11 negation:** ITEM-DIRECT 2, CLASS-INHERITED 2, ADJACENT-ONLY 4,
  SILENCE 4 (identical under both variants). Three distinct
  propositions do all the work, in three distinct units that must not
  be pooled: CGEL's statement that supplements do not fall within the
  scope of negatives in the anchor (Ch. 15, p. 1360; inherited by
  DAMN_REACT, OUCH, WOW as `evaluative-stance|external-co-utterance`,
  3 items, one proposition, one outcome direction); Heine's English
  negation table (*Ouch! #Not/don't ouch!*, attempted direct negation
  with no host; `evaluative-stance|no-host`, 1 item, after
  adjudicating the cross-family integrated/no-host inconsistency to
  no-host); and one control observation (COFFEE's descriptive content
  inside a negative's scope; `descriptive-content|integrated`, 1
  item). Inheritance of the CGEL proposition rests on a recorded
  scope ruling (Brett Reynolds, 2026-11-04): the supplement
  properties stated at p. 1360 are general to supplements,
  interjections included, despite preceding the interjection
  subsection, which itself places *ouch*, *wow*, and *damn* as
  supplements with clausal anchors. Semantic review rejected the most
  visible would-be positives: Gehweiler's "negative contexts" for
  *gee* are negative-evaluation contexts, not negation, and a Potts
  scope quote concerns tense operators. DAMN_PRENOM and
  BLOODY_PRENOM, the integrated expressives the expressive rotation
  most needs, are ADJACENT-ONLY. There is no contrasting observation
  inside the external evaluative-stance unit.
- **Hosted P12:** no item has item-direct evidence. CLASS-INHERITED 7
  [1], ADJACENT-ONLY 4 [10], SILENCE 1 (STOP). Every surviving
  assertion traces to survey generalizations in Heine (2023, ch. 1):
  Heine's own set-off claims (framing Zwicky on discourse markers),
  a left-periphery separation claim, Wharton on interjections at
  utterance edges, and Andrason and Dlali's comparative isolation
  claim. Corrected strengths: recurrent-characteristic carries 7
  items including pass-weak; attested-possible carries 3 items;
  categorical-default carries none (both pre-correction categorical
  units rested on verdict notes calling the strength overclaimed;
  Wharton's slice is merged at recurrent strength, Andrason and
  Dlali is attested-possible for English). Units are now one derived
  strength per assertion, so coder-listed weaker slices no longer
  count separately; recurrent support entails attested possibility
  without a second count. Only the Wharton lineage (WOW) survives
  strict review. The Heine set-off and left-periphery propositions
  are contested within their own section (see coverage below) and
  must not be read as settled characteristic hosted separation. Two
  coder errors remain instructive: Qwen linked a CGEL
  intonational-separation quote to *Damn* when its example was a
  medial adverb, and coded a continuer's own high-low contour (MMHM)
  as hosted separation.

Assertion depth, stated as distinct canonical propositions rather
than assertion counts, is thin everywhere: three live propositions
for P10 (plus one rejected wrong-use token), three for P11 in three
separate units, and four inherited lineages for P12 (all second-hand
survey claims in one Heine chapter, two of them contested by
qualifications in the same section). Support mix among surviving
queue assertions: P10 item-specific 8, P11 item-specific 3 and
class-inherited 4, P12 class-inherited 16. No queue assertion retains
item-specific support for P12 after correction. Source-target
dependence is unchanged in kind: same-observation support is
concentrated in P10, where the Potts example itself carries pattern
and effect. Under a future lesion, those cells are the ones whose
source support cannot be separated from the target observation.

Retrieval and coverage (replacing the pre-correction conclusion,
which same-packet disagreement could not support): within-packet
splits still show that several one-family positives were semantic
false positives (Copilot on P11 GEE and WOW, Qwen on P12
BLOODY_PRENOM) and that genuine single-family finds included
easy-to-miss tokens (Copilot's P10 HUH; Muse's P11 COFFEE). Those
comparisons test reading inside identical packets only. Bounded
checks of complete sections (`COVERAGE-2026-11-04.md`) found one
retrieval failure (Heine's prosody qualifications, boundary weakening,
pause findings, and prosodic attachment, absent from packets while
the generalizations they qualify were coded), one adequate coverage
case (CGEL scope proposition, retrieved with its inclusion text; no
further relevant scope statement in the survey), and one non-retrieval
failure (Stange token, full disqualifying context present). The
defensible summary is: the audited packets contain sparse usable
evidence for these precisely specified targets; coverage of the held
sources remains to be checked beyond the sections examined. No
general literature-versus-retrieval verdict is licensed.

## What this licenses for the freeze decision

No primary target is selected here, and the pre-correction P11
recommendation is withdrawn. Target selection is postponed until
Brett chooses among the options below on the corrected record. The
freeze commitment, when made, should read as a prespecified primary
reconstruction analysis: select and specify the primary
reconstruction analysis before inspecting its scores, while
documenting what the evidence audit contributed to that selection.
Target assertions and their values have been inspected during
development; only the primary reconstruction scores remain
uncomputed. Fresh production coding can improve consistency and
reduce anchoring. It does not create independent linguistic
observations from the same source assertions.

What each target could bear, on the corrected evidence:

- **P10** has two effect-bearing propositions with different pattern
  specificity (Potts distributed-mixed strengthening and
  non-redundancy, one example across the *damn* family; Quirk
  repetition-unspecified strengthening for OKAY) and one
  occurrence-only adjacent attestation (HUH). Adjacent strengthening
  has no support. Event multiplication, the dimension that would
  discriminate depictive from expressive repetition, has no support
  in this sample at all. Any P10 primary must state which pattern and
  dimension it reconstructs and must not present the Potts example
  as two within-use effects.
- **P11** narrow (evaluative stance, external co-utterance, anchor
  negation) rests on one inherited CGEL proposition across three
  items, all in one direction, with no contrasting observation inside
  the target. Attempted direct negation (OUCH, no host) and
  integrated descriptive scope (COFFEE) are separate descriptive
  units; pooling them confounds expressivity with supplementary
  versus integrated construction. On this record the narrow target
  can support a worked example or evidence map. It offers little
  room to demonstrate gain over a base-rate predictor, because there
  is nothing within the target to discriminate. A broader
  constructional comparison would need to be declared as such, with
  its own predictor. Integrated prenominal expressives remain
  adjacent only.
- **Hosted P12** has no item-specific evidence in the sample. Its
  seven inherited items rest on survey generalizations with weak
  hosted specificity, two lineages contested by qualifications in
  the same Heine section that production packets must retrieve.
  Options remain: narrow to recurrent-characteristic strength with
  the inherited and contested concentration reported as the finding;
  defer pending item-specific hosted prosody sources; or keep P12
  descriptive. Freezing it as a primary target on this record would
  test recovery of Heine chapter-1 generalizations.
- **Cross-inquiry comparison** (INTJ vs EXPRESSIVE on shared
  targets): the overlap of non-silent items remains tiny (the *damn*
  family carries most of it), so the comparative question would rest
  on very few scored cells whatever the gates.

Family performance for production planning is unchanged in outline:
Copilot produced 61% mechanically voided assertions and half the
semantic rejections, while contributing genuine single-family finds;
Qwen was slow and sparse; Agy was clean where quota allowed; the
non-independent Muse subagents were cleanest, which cannot count as
independent confirmation. Correction adds one lesson above throughput:
model semantic review passed a wrong-use token whose disqualifying
context was in-packet, and prose qualifications without structured
fields did not survive aggregation. Production adjudication needs
structured effective fields, proposition-level tracking, and human
review sampled to include strict-pass and unanimous cells.

No target is approved or rejected here, no gate threshold is set, and
nothing in this audit may be imported into a production matrix.
Sampled pairs would be recoded fresh from production packets.
