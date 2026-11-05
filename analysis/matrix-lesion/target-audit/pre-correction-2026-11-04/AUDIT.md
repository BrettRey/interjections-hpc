# Target-evidence audit: report

Status: run 2026-11-04 under `DESIGN.md`; discarded development data
under `FREEZE-v2.md` section 9. Nothing here is a study cell, and no
source-target association, category assignment, or lesion was computed
from it. Aggregation covers evidence availability and assertion
structure only.

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
- Human semantic review of every mechanically valid ITEM-DIRECT,
  CLASS-INHERITED, or CONFLICT assertion (`semantic-verdicts.json`;
  verdicts pass / pass-weak / downgrade / reject, each with a note).
  Availability is then aggregated with and without pass-weak
  assertions (`finalize_audit.py`, `AUDIT-tables.md`,
  `audit-final.json`).

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

## Results

Coverage: Muse 36/36 pairs, Copilot 36/36, Qwen 36 files (35
parseable; P11 BANG_DEPICT returned a one-character response), Agy
18/36 (quota). Of 129 raw assertions, 89 survived mechanical
verification (Muse 37/37, Agy 16/17, Qwen 15/21, Copilot 21/54, of
which only 8 strictly clean). Ninety-seven defects were logged, 90 of
them Copilot's (53 fatal, mostly discontinuous quotes, wrong
identifiers and off-enum values; 37 minor). All 48 mechanically valid
ITEM-DIRECT, CLASS-INHERITED or CONFLICT assertions received a human
semantic verdict: 15 pass, 18 pass-weak, 3 downgraded to
ADJACENT-ONLY, 12 rejected. No coder proposed INAPPLICABLE or CONFLICT
that survived, and none flagged RETRIEVAL-FAILURE-SUSPECTED. Raw
pair-level agreement between families ran 55-72% on shared pairs. Full
tables: `AUDIT-tables.md`; pair-level detail: `audit-final.json`.

Pair-level availability after both checks (best surviving class across
families; including pass-weak, with strict pass-only in brackets):

- **P10 repetition:** ITEM-DIRECT 5 [3], SILENCE 7 [9], nothing
  inherited or merely adjacent. The five are the two *damn* rows,
  OKAY, HUH, and WOW. Behind them stand four distinct source
  propositions: Potts (2007) on repetition strengthening rather than
  redundancy (one proposition carrying both *damn* rows and both
  effect dimensions), Quirk et al. on OK repeated for emphasis, and
  two transcript tokens (Dingemanse's *Huh? Huh?*, Stange's *Wow, wow,
  wow*) that attest adjacent occurrence with no stated effect. By
  pattern and dimension: distributed-recurrence strengthening and
  redundancy are each supported for 2 items (the same Potts
  proposition), adjacent-repetition occurrence for 2-3 items, and
  event multiplication, lengthening, and lexicalized reduplication
  have no source-stated support at all in this sample (the single
  event-multiplication unit in the tables is a coder's label on a
  passage stating no effect). BANG_DEPICT, the item where event
  multiplication was most plausible, is SILENCE. Three of nine
  damn-family assertions across families miscoded Potts's distributed
  accumulation as adjacent repetition and were rejected.
- **P11 negation:** ITEM-DIRECT 2, CLASS-INHERITED 2, ADJACENT-ONLY 4,
  SILENCE 4 (identical under both variants). Three distinct
  propositions do all the work: CGEL's statement that supplements do
  not fall within the scope of negatives in the anchor (inherited by
  DAMN_REACT, OUCH, WOW through explicit class inclusion), Heine's
  English negation table (*Ouch! #Not/don't ouch!*, an item-specific
  attempted-negation observation with no host), and one control observation
  (COFFEE's descriptive content inside a negative's scope, integrated
  host). By unit: evaluative-stance in external-co-utterance position
  has inherited support for 3 items; evaluative-stance integrated and
  no-host have one item each; sequential-action and depictive units
  are adjacent only. Semantic review rejected the most visible
  would-be positives: Gehweiler's "negative contexts" for *gee* are
  negative-evaluation contexts, not negation, and a Potts scope quote
  concerns tense operators. DAMN_PRENOM and BLOODY_PRENOM, the
  integrated expressives the expressive rotation most needs, are
  ADJACENT-ONLY.
- **Hosted P12:** no item has item-direct evidence. CLASS-INHERITED 7
  [1], ADJACENT-ONLY 4 [10], SILENCE 1 (STOP). Every surviving
  assertion traces to survey generalizations in Heine (2023, ch. 1):
  Zwicky on discourse markers ("typically ... prosodically separated
  from their surrounding context"), Heine's own "likely to be set off
  prosodically from surrounding text material", Wharton on
  interjections at utterance edges "separated off from the main
  clause" and "rarely integrated into intonational units", and
  Andrason and Dlali's comparative isolation claim. Only the Wharton
  proposition (for WOW) passed semantic review without a weakness
  flag, which is why the strict variant collapses to a single
  inherited item. The recurrent-characteristic strength level carries
  7 items including pass-weak; categorical-default slices rest on
  hedged sentences ("always ... rarely") and should not be read as
  categorical support. Two coder errors are instructive: Qwen linked
  a CGEL intonational-separation quote to *Damn* when its example was
  a medial adverb, and coded a continuer's own high-low contour
  (MMHM) as hosted separation.

Assertion depth, stated as distinct source propositions rather than
assertion counts, is therefore thin everywhere: about four for P10,
three for P11, and about four (all second-hand survey claims in one
Heine chapter) for P12. Support mix among surviving queue assertions:
P10 all item-specific (10, counting duplicates across families), P11
item-specific 3 and class-inherited 4, P12 class-inherited 15 (one
assertion reclassified down from item-direct on review).
Source-target dependence: most P11 and P12 support is
distinct-propositions-shared-passage (5 and 11 assertions), with
same-observation cases concentrated in P10 (5), where the Potts
example itself carries both the pattern and the effect. Under a
future lesion, those same-observation cells are the ones whose source
support cannot be separated from the target observation.

Retrieval/disagreement notes (from the design's required sample of
SILENCE and ADJACENT-ONLY results; cross-family splits on the same
packet): several apparent one-family positives against others' SILENCE
did not survive semantic review (Copilot on P11 GEE and WOW, Qwen on
P12 BLOODY_PRENOM), so those splits mark false positives, not misses.
Genuine single-family finds were easy-to-miss corpus tokens (Copilot's
P10 HUH and WOW adjacent repetitions, missed by Agy and Muse) and
one control observation (Muse's P11 COFFEE). Copilot returned adjusted
SILENCE on several P12 pairs where other families found class-level
prosody claims, partly because its assertions were voided mechanically
at the highest rate. The packet builder itself was not the binding
constraint in these splits: in every case the positive family's quotes
came from the same packet the SILENCE families searched.

## What this licenses for the freeze decision

The audit answers its narrow question: the held literature, as
retrieved into packets v3, documents these three candidate targets
very unevenly, and the binding constraint is proposition depth in the
sources, not coder throughput or packet retrieval. Scarcity is mostly
source silence on the specified use and environment; retrieval failure
in the builder was not implicated in any split examined, and the
loudest apparent gaps (one family's positive against others' silence)
often dissolved into semantic false positives on review.

What each target could bear, on this evidence, is Brett's call; the
raw material for setting per-projection evidence gates is:

- **P10** has item-specific evidence for 5 of 12 sampled items but
  from four distinct propositions, and only one (Potts) states an
  effect dimension. A confirmatory target built on the
  distributed-recurrence strengthening or redundancy dimension would
  be recovering one source generalization across the *damn* family, a
  legitimate fixed-inventory reconstruction but evidentially a single
  claim; a target built on adjacent occurrence has three
  independently attested items and no effect content. Event
  multiplication, the dimension that would discriminate depictive
  from expressive repetition, has no support in this sample at all.
- **P11** has a small but genuinely discriminating core: one
  item-specific unavailability observation, one integrated control
  falling inside scope, and one shared CGEL proposition inherited by
  three items. That is enough to define a narrow
  evaluative-stance-under-anchor-negation projection on a small
  bearer set, provided the inherited CGEL cells are tracked as one
  proposition cluster, as FREEZE-v2 already requires. It is not
  enough for integrated prenominal expressives, which are adjacent
  only; any expressive-rotation claim about them would need evidence
  this sample does not contain.
- **Hosted P12** has no item-specific evidence in the sample. Its
  seven inherited items rest on survey generalizations whose
  hosted-environment specificity is weak ("surrounding context",
  "most conspicuous" for standalone utterances), and only one
  item (WOW, via Wharton) survives strict review. Freezing hosted P12
  as a primary target on this record would test recovery of Heine's
  chapter-1 generalizations, nearly all of it class-inherited and
  pass-weak. Options the audit leaves open: narrow the target to the
  recurrent-characteristic strength with the inherited concentration
  reported as the finding; defer P12 pending sources that describe
  particular items' prosody with hosts (the supplement chapter of
  CGEL itself is a candidate the packets touched only obliquely); or
  drop it as a primary target and keep it descriptive.
- **Cross-inquiry comparison** (INTJ vs EXPRESSIVE on shared targets):
  on this sample the overlap of non-silent items is tiny (the *damn*
  family and WOW carry most of it), so the comparative question would
  rest on very few scored cells whatever the gates.

Family performance for production planning: one route (Copilot)
produced 61% mechanically voided assertions and half the semantic
rejections, while also contributing the two genuine single-family
corpus finds; Qwen was slow (about 4 minutes a pair) and sparse, with
4 of its 7 queued assertions rejected; Agy was clean where quota
allowed; the non-independent Muse subagents were cleanest, which
cannot count as independent confirmation. Mechanical verification
plus full semantic review of queue assertions caught every rejected
assertion found; agreement alone would have passed several (the
*gee* and Potts-tense errors were each single-family, but the Potts
(34) pattern error was made independently by two families).

No target is approved or rejected here, no gate threshold is set, and
nothing in this audit may be imported into a production matrix.
Sampled pairs would be recoded fresh from production packets.
