# Triage: external review of the target-evidence audit (2026-11-04)

Review triaged: pasted model review of `AUDIT.md`, `semantic-verdicts.json`,
and `audit-final.json` (this folder), received 2026-11-04. Every factual
claim below was checked against the local JSON, `finalize_audit.py`,
`DESIGN.md`, `FREEZE-v2.md`, `packets-v3.md`, and the held source markdown
in `literature/`. Verification script: `/tmp/verify_audit_review.py`.

## Bottom line

Adopt the review. Postpone primary-target selection. Do not freeze P11 on
the current recommendation.

The review is right on each load-bearing point, and two of its cautious
points come out stronger on local checking (Stange *wow*, Heine packet
coverage). Nothing in it needs rejecting. One point needs Brett's factual
answer before it can be closed (who made the 48 semantic verdicts).

The audit's arithmetic and much of its prose are sound. The failure is
mechanical and fixable: semantic corrections were recorded as prose notes,
while `finalize_audit.py` regenerates units from the original coder fields.
Only one structured correction exists (`effective_contribution`, applied
once). Every other correction therefore dies before the tables.

## Verified findings

### 1. Semantic corrections do not reach the tables (Adopt)

Totals reproduce exactly: 129 raw assertions, 89 mechanically valid, 97
logged defects, 48 verdicts (15 pass, 18 pass-weak, 3 downgrade, 12 reject).

All five cited discrepancies are present in the local record:

- P10 HUH (`copilot:HUH:A1-huh-adjacent-rep`, pass-weak, "no effect
  dimension stated, occurrence only") still generates the unit
  `adjacent-repetition|event-multiplication -> ITEM-DIRECT: 1`.
- P10 WOW (`copilot:WOW:A1-wow-adjacent-rep`, strict pass, "no effect
  dimension") still generates `adjacent-repetition|strengthening` in both
  table variants, including strict pass only. The strict sensitivity
  cannot catch a strict-pass label error.
- P10 OKAY (both families, pass-weak, "adjacent pattern not specified",
  "Pattern should be unclear") still generates
  `adjacent-repetition|strengthening -> ITEM-DIRECT: 2`.
- P11 OUCH: the same Heine Table 1.4 evidence passes twice with
  incompatible hosts (`agy` integrated, `claude` no-host). The final P11
  units therefore contain both `evaluative-stance|integrated ->
  ITEM-DIRECT: 1` and `evaluative-stance|no-host -> ITEM-DIRECT: 1` for
  one attempted-negation observation. The verdict note itself names the
  inconsistency. Nothing adjudicates it.
- P12: both categorical-default units surviving in the weak-inclusive
  table carry verdict notes saying the strength is overclaimed (Andrason
  and Dlali for OUCH; Wharton "always separated" slice for WOW).
  `categorical-default -> CLASS-INHERITED: 2` remains.

Root cause, confirmed in code: `assertion_outcome()` in
`finalize_audit.py` honors reject, downgrade, pass-weak exclusion, and a
single `effective_contribution` override. It never touches pattern,
effect dimension, host relationship, contribution assessed, claim
strength, or support type. Units are copied from `units_valid` verbatim.
`AUDIT.md` prose often states the corrected reading (adjacent occurrence
with no stated effect; event-multiplication unit called a coder's label;
categorical slices flagged). The machine-readable record contradicts the
prose. Any gate set from `audit-final.json` inherits the uncorrected
labels.

Also confirmed: the report's "Three of nine damn-family assertions"
(`AUDIT.md`) is wrong on both numbers. Mechanically valid P10 *damn*
assertions number 10. Rejected Potts-pattern miscodes number 5 (Copilot
3, Qwen 2).

Proposition clustering is unreliable as generated. The quote-prefix key
splits the single Quirk claim into two clusters and the single Stange
token into two clusters (and likewise splits the Heine P11 sentence).
Prose proposition counts may be defensible. The generated map does not
establish them.

### 2. P11 has no discriminating core for the proposed narrow target (Adopt)

The proposed target is evaluative stance under anchor negation in
external co-utterance position. Within that unit, the surviving evidence
is one CGEL generalization inherited by three items (DAMN_REACT, OUCH,
WOW), all in the same direction (outside anchor-negative scope). No
contrasting observation exists inside the target.

The other two legs of the claimed "genuinely discriminating core" belong
to different units that `DESIGN.md` and `FREEZE-v2.md` explicitly forbid
pooling:

- OUCH attempted direct negation (`#Not/don't ouch!`): no host
  proposition, no anchor whose negation could be survived.
- COFFEE (`No, I would not like tea or coffee`): descriptive content,
  integrated host. A useful control for integrated descriptive content.
  It says nothing about evaluative stance in supplementary position.

Pooling them confounds expressivity with supplementary versus integrated
construction. A broader constructional comparison could be designed, but
it would have to be declared as a construction comparison, with its own
predictor and interpretation. It cannot be presented as evidence that an
expressive category earns predictive keep on the narrow target.

CGEL scope needs an explicit reading (Adopt, with one strengthening
nuance). Checked in `literature/00-CGEL.md` around the quoted sentence.
The sentence ("The supplements differ from the most central modifiers in
that they do not fall within the scope of negatives in the anchor")
closes subsection (h), PPs and AdvPs, illustrated by *in my opinion* and
*as you know*, immediately before subsection (i), Interjections. The
review is right that automatic inheritance from the word "supplements"
skips a scope decision. The nuance: subsection (i) explicitly places
central interjections (listing *ouch*, *wow*) and reanalysed *damn* "as
supplements with clausal anchors", so class inclusion has explicit
textual support. What remains undecided is whether the (h) scope
generalization, framed as a contrast with central modifiers for
clause-anchor supplements "very much like that of a modifier", is
intended for every supplement type in the survey. That reading must be
made and recorded before inheritance carries weight. Either way, the
cells remain one proposition with no within-target contrast.

### 3. P10 needs correction in both directions (Adopt, strengthened)

`AUDIT.md` contradicts itself. Its results section correctly lists Quirk
et al. on OK repeated for emphasis as a distinct proposition. Its
freeze section then says only Potts states an effect dimension. Both
OKAY verdicts accept strengthening. The freeze sentence is wrong.

Checked source contexts:

- Potts (34), as asserted: `repetition_positions: mixed`. The example
  retains standalone *Damn* while prenominal occurrences accumulate
  (*Damn, I left my damn keys in the damn car*). One mixed-position
  accumulation proposition currently yields `distributed-recurrence`
  strengthening and redundancy units on two rows (DAMN_REACT and
  DAMN_PRENOM). Those are not two separately observed within-use effects.
  Positions must enter the corrected unit identity.
- Quirk et al., note [b] (pp. 982-983 in held markdown): "expressions
  like yes, no, well, OK, all right are often repeated for emphasis (cf
  18.58 on repetition)". Section 18.58 (Reinforcement) defines repetition
  for emphasis and illustrates both adjacent reiteration (*It's far,
  far too expensive*) and non-adjacent reinforcement. It does not pin
  the OK claim to adjacent repetition. Correct unit: repetition,
  pattern unspecified, with strengthening (emphasis).
- HUH: adjacent occurrence only. No source-stated effect. The
  event-multiplication label must be removed, not caveated.
- WOW: worse than the review suggests. Stange (2016, ch. 4, Side note 1,
  example (65), headed "Whoa! spelt Wow!") introduces the Teresa token
  with the sentence "any utterances of Wow! whose meaning was 'stop'
  were discarded as misspellings of Whoa!, as in the following example".
  The token occurs in a rough play fight, followed by "let go". By the
  source's own analysis this is *whoa* (stop), excluded from the *Wow!*
  data. Both P10 WOW assertions code this token as the amazement-reaction
  use. The full disqualifying context was present in `packets-v3.md`,
  so this is a coding and semantic-review failure, not a packet omission.
  Verdicts should become reject (wrong use). P10 WOW then has no
  surviving evidence in this audit.
- Event multiplication: zero source-stated support. Confirmed.

Corrected P10 picture: two effect-bearing propositions with different
pattern specificity (Potts distributed-mixed strengthening and
non-redundancy; Quirk repetition-unspecified strengthening), one
occurrence-only adjacent attestation (HUH), no WOW, no event
multiplication. `adjacent-repetition|strengthening` drops to zero items.

### 4. Literature versus retrieval is not established (Adopt, strengthened)

The disagreement check compares coders inside identical packets. It can
detect reading misses. It cannot detect builder omissions shared by all
coders. `AUDIT.md` claims ("the packet builder itself was not the
binding constraint"; "the binding constraint is proposition depth in the
sources, not coder throughput or packet retrieval"; "retrieval failure
in the builder was not implicated") exceed the method. The report's own
concession that CGEL's supplement chapter was touched "only obliquely"
already contradicts the strong form.

Local check adds positive evidence of one-sided packet coverage. Heine
(2023, ch. 1) prosody discussion (`literature/heine_2023_grammar-of-
interactives_ch1.md`, lines 247-249) continues, immediately after the
audited generalizations, with boundary weakening ("prosodic boundaries
may be weakened or disappear entirely"), O'Connell et al.'s pause
findings (45% without preceding or following silent pauses), and Biber
et al. on English inserts tending to "attach themselves prosodically to
a larger structure". None of these passages appears in `packets-v3.md`
(all five string probes return zero), while the generalizations they
qualify do appear and were coded. Packet sentences were therefore more
categorical than their source section. These passages do not
automatically create negative cells for sampled items. They do change
the strength and interpretation of every inherited P12 proposition, and
they falsify any claim that builder coverage was checked and cleared.

Defensible replacement conclusion (adopt review wording): "The audited
packets contain sparse usable evidence for these precisely specified
targets; coverage of the held sources remains to be checked."

### 5. Human-review attribution (Defer to Brett; artifacts do not establish it)

`semantic-verdicts.json` describes its judgments as "Human
(orchestrator)". `AUDIT.md` calls them "Human semantic review" and
"human semantic verdict" four times over. `FREEZE-v2.md` section 7
promises human adjudication. No artifact names a human reviewer or
records human sign-off, and `AUDIT.md` elsewhere uses "orchestrator"
for the agent coordinating the Claude subagent coders ("non-independent
of the orchestrator").

Decision needed from Brett: did you (or another person) make these 48
judgments? If yes, record who, plainly, in the verdict file header. If
Muse made them as orchestrator, relabel as model semantic review in
`semantic-verdicts.json`, `finalize_audit.py`, and `AUDIT.md`, and treat
the freeze's human-adjudication requirement as unmet by this audit.
The judgments remain usable as model review. They do not then count as
the promised human validation. Given the Stange miss (disqualifying
context in-packet, strict pass issued), the label matters beyond
bookkeeping: production adjudication sampling must include unanimous
and strict-pass cells, as `FREEZE-v2.md` already requires.

### 6. "Confirmatory" wording (Adopt)

Adopt "prespecified primary reconstruction analysis" as the freeze term,
with the review's commitment sentence verbatim: "Select and specify the
primary reconstruction analysis before inspecting its scores, while
documenting what the evidence audit contributed to that selection."
Fresh production coding improves consistency and reduces anchoring. It
does not create independent linguistic observations from the same source
assertions, and it does not erase investigator knowledge gained in
development. This fits the fixed-inventory rationale without
overclaiming. Target values were inspected during the audit. Only the
primary reconstruction scores remain uncomputed. Say exactly that.

## What correction does to each target (preview, not a freeze decision)

- P10: adjacent-strengthening evidence disappears (0 items). Adjacent
  occurrence retains 1 item (HUH, occurrence only). Effect-bearing
  evidence is Potts (one mixed-position proposition across the *damn*
  family) plus Quirk (pattern-unspecified strengthening for OKAY, class
  list including *yes, no, well, all right*). Event multiplication
  remains empty, so P10 still cannot discriminate depictive from
  expressive repetition on this evidence base.
- P11 narrow (evaluative stance, external, anchor negation): 3 inherited
  items, 1 proposition, 1 outcome direction, pending the CGEL scope
  reading. Attempted direct negation (OUCH, no-host) and integrated
  descriptive scope (COFFEE) survive as separate descriptive units.
  They do not supply contrast for the narrow target. On current
  evidence the narrow target can support a worked example or evidence
  map. It offers little room to demonstrate gain over a base-rate
  predictor, because there is nothing to discriminate.
- P12 hosted: categorical-default units fall to recurrent at best once
  strengths are corrected. Strict WOW via Wharton survives. Heine's
  weakening and attachment passages must be coded as qualifying or
  conflicting class evidence before any inherited strength is asserted.
  Item-direct evidence remains zero in sample.

None of this is a failure of the lesion idea. It is a finding about this
evidence base and packet construction, which is what a discarded audit
exists to produce.

## Punch list (bounded correction pass; no target choice inside it)

P0, before any gate or target discussion:

1. Extend `semantic-verdicts.json` with structured effective fields:
   `effective_repetition_pattern`, `effective_repetition_positions`,
   `effective_effect_dimension` (including `none-stated-occurrence-only`),
   `effective_host_relationship`, `effective_contribution_assessed`,
   `effective_claim_strength`, `effective_support_type`,
   `effective_use_slice` (including wrong-use rejection). Preserve
   original coder records untouched.
2. Re-adjudicate the known set under the new fields: P10 HUH, WOW (both
   assertions to reject, wrong use, citing Stange (65)), OKAY (pattern
   to unspecified), Potts *damn* (mixed positions in unit identity),
   P11 OUCH Heine (single effective host: no-host attempted negation;
   void the integrated duplicate), P12 categorical slices (strength
   down). Then sweep all 48 verdicts for note-only corrections of the
   same kinds.
3. Patch `finalize_audit.py` to generate units from effective fields,
   not `units_valid` labels. Regenerate `audit-final.json` and
   `AUDIT-tables.md`. Add a regression check: no surviving unit may
   assert a pattern, effect, host, or strength that its verdict note
   denies (encode the five cases above as tests).
4. Replace generated clustering with a hand-reviewed canonical
   proposition map (assertion to proposition ID, with source location).
   Regenerate proposition counts from the map.
5. Correct reviewer attribution per Brett's answer to section 5.
   Regenerate `AUDIT.md` numbers from the corrected record (including
   5 of 10, P10 effect summary, P11 core claim removal, retrieval
   conclusion replacement).

P1, bounded source-coverage check (held literature only, no new coders):

6. CGEL supplement material: check packet coverage of the full
   supplementation survey containing subsections (h) and (i), record
   the scope reading for the anchor-negation generalization, and code
   any additional interjection-relevant scope statements as audit
   evidence or as checked absence.
7. Heine ch. 1 prosody section in full: code weakening, pause, and
   attachment passages as qualifying class evidence against each
   inherited P12 proposition; reassess strengths (CONFLICT is an
   available class and is currently unused).
8. Quirk and Stange checks are done in this triage (sections 3 above).
   File the outcomes as verdict-note citations. Potts section 2.6
   should be read in full once to confirm no within-use adjacent
   claim accompanies the mixed accumulation claim.

P2, freeze language (after P0 to P1):

9. Adopt "prespecified primary reconstruction analysis" plus the
   commitment sentence. Reassess each precisely defined unit for
   contrasting evidence (both outcome directions, item-specific
   separated from inherited, per `FREEZE-v2.md` section 8). Only then
   choose, narrow, redesign, or drop primary targets.

## Rejected items

None. The review contains no factual claim that failed local checking.
Its two explicitly hedged claims (Stange use identity, CGEL scope)
resolve in its favour on the first and remain open-by-design on the
second. Its one external citation for Heine matches the held local text.

## Decisions needed from Brett

1. Who made the 48 semantic verdicts? (Section 5. Gates relabelling and
   any human-validation claim.)
2. Approve the P0 to P1 correction pass as specified, with target
   selection explicitly postponed until regenerated tables exist?
   (Recommended: yes.)
3. CGEL scope reading: accept interjection inheritance under an
   explicit recorded reading, restrict the generalization to its (h)
   context, or leave inheritance suspended pending fuller CGEL checking?
   This can wait for punch item 6. It should not be decided from the
   single quoted sentence.

No `DECISIONS.md` or `STATUS.md` entry has been made. Both should follow
Brett's answers, recording what was decided (postponement, correction
pass scope, reviewer attribution) without importing audit values into
any production record.

## Outcome addendum (2026-11-04, same day)

Brett answered all three decisions. (1) Neither Brett nor any other
human made the 48 judgments; verdicts relabelled as model review, human
adjudication outstanding. (2) P0 to P1 approved and executed:
structured effective fields and re-adjudication
(`apply_corrections_2026_11_04.py`), derived units and canonical
propositions in `finalize_audit.py` and `proposition-map.json`,
regression tests passing, bounded coverage checks in
`COVERAGE-2026-11-04.md`, corrected `AUDIT.md` regenerated, decision
logged in project `DECISIONS.md`. (3) CGEL scope ruling by Brett from
printed Ch. 15 p. 1360: supplement properties apply to all
supplements, interjections included. Target selection remains
postponed. This memo is closed.
