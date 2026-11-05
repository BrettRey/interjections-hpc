# Discarded yield audit: design (not yet run)
<!-- SUMMARY: sealed evidence-existence census of all 46 rows under properties-v4.csv, covering every INTJ and EXPRESSIVE diagnostic and candidate target, to learn before Round 7 whether membership is estimable and how much evidence each candidate target has; revised after the Codex and Muse reviews · status: designed, not run · updated: 2026-11-04 -->

Parent protocol: `../FREEZE-v4.md` (draft). Recommended in
`../../../reviews/matrix-lesion-evaluation-2026-11-04/EVALUATION.md`
(yield check, handoff Q10) and revised after the reviews in
`../../../reviews/freeze-v4-review-2026-11-04/`.

## Purpose

Two questions, before Round 7 calibrates anything:

1. Is each grouping's membership estimable on the record the literature
   actually holds (FREEZE-v4 section 2, checks a to d)? Muse's review
   argues EXPRESSIVE may not be: P11 is inapplicable for uses with no
   host, and P10 and P11 were thin in the earlier audit.
2. Does the record hold enough evidence, per candidate target and in the
   targets the two groupings share, for the reported estimates to be
   more than noise? (There is no gate; this is read from the counts.)

The audit measures evidence existence only. It computes no
source–target association, lesion, or gain, and its cells are never
study data; anything that enters production is recoded fresh.

## Schema and silos

Coding follows `../properties-v4.csv`, the governing v4 schema (P04,
P05, P06 disjoint; the P08 guard, with contrast evidence kept U in the
primary; the P10S and P11N units with pattern and host fields; the
INAPPLICABLE state for P11N). One silo per property:

- INTJ diagnostics: P01, P02, P03, P04, P05, P07.
- EXPRESSIVE diagnostics: P07, P08, P10S, P11N.
- Candidate targets not already listed: P06, P09, P13.

P12 is excluded, since the earlier audit found no item-specific support
for hosted prosody. P10 and P11 are re-coded on all rows under their v4
units; the earlier 12-item audit doesn't cover the new rows or the
repaired units.

## Sample and the firewall

All 46 rows of `../items-v4.csv`. This makes the audit a coverage
census, which FREEZE-v3 had removed. Brett chose a **sealed census**
(2026-11-04): coders and model semantic review run inside a sealed
pipeline, and a locked script emits only the outputs listed in
FREEZE-v4 section 9. Item identities, item-level values, and any
cross-property tabulation are hashed and sealed with the development
artifacts and are not opened before the registered analysis. The
estimability checks c and d need a membership fit; the locked script
runs it and reports only pass or fail.

Packets follow the v3 builder requirements: qualification and
counter-evidence retrieved with the generalization, use-identity
context, and publication pages.

## What each record carries

For every non-U assertion: polarity; item-specific or inherited; if
inherited, the inclusion judgment (source, class named, inclusion
passage); for N values, strength (stated non-occurrence,
opportunity-documented, or both); canonical proposition ID; claim
strength (possibility, characteristic, categorical); for P10S the
repetition pattern; for P11N the host relation, or a checked
INAPPLICABLE record; and the dependence state against each diagnostic of
both groupings for the same row (distinct, shared passage, same
observation, entailed, same inclusion), because concealment now applies
to reference rows as well as target rows.

## Sealed outputs

Per property (no cross-property tables):

1. Known cells by polarity and tier, before and after concealment.
2. Item-specific against inherited cells, by polarity. For P01–P05,
   this answers how many absence records name a specific word.
3. N strength: stated only, opportunity-documented, both.
4. Distinct canonical propositions, distinct testimony units, and the
   largest single proposition's share.
5. Control-tier and form-family composition of known cells.

Per grouping:

6. Rows with three or more visible diagnostics, counting each testimony
   unit once; pairwise joint visibility of the diagnostics; P11N
   INAPPLICABLE count.
7. Pass or fail for estimability checks a to d, on Tier A and on Tier A
   plus Tier B, with the identifier of each failed check. The section 8
   counts per candidate target are reported under item 1 to 5; nothing
   is admitted or rejected.

## Routes

At least two model families, fresh sessions, with full provenance per
FREEZE-v3 section 7, mechanical quote verification on 100% of cells,
and model semantic review labelled as model review. Human review is not
claimed. Expected size: 46 rows × 12 properties = 552 item–property
packets.

## Second stage: corpus attestation (Tier B)

After the Tier A pass, and only for cells it leaves empty, search the
local CABNC checkout under FREEZE-v4 section 4 and the corpus standards
in `properties-v4.csv`:

- **Y** from an attested line of the specified use, for any property
  with a positive corpus standard.
- **N** only where the property has an opportunity standard (P05, P06,
  P12), from at least K opportunities with no instance; counts are
  recorded. Meaning properties (P07, P08, P09, P10S, P11N) and P13 have
  no corpus standard and get no Tier B cells.

Record the frozen query, the hits examined, the opportunities
identified, and the outcome. Report Y and N fills separately per
property, so that filling which depends on the value is visible. The
sealed outputs are recomputed on Tier A plus Tier B. Cells still empty
after this stage are the candidates for an analyst tier, which needs
Brett's decision.

## Stopping rule

Emit the sealed outputs, then stop. No target is approved or rejected
by this audit. Whether to proceed to Round 7, narrow the inventory, or
change scope is Brett's decision on these outputs.
