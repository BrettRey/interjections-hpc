# CABNC census and pre-pilot decision report
**Date:** 2026-07-27
**Status:** Review checkpoint
**Decision requested:** Whether the validated CABNC retrieval infrastructure justifies the bounded manual pre-pilot described below. This report does **not** ask us to treat the corpus feasibility gate as passed.
## Executive decision
The CABNC acquisition, parsing, retrieval, provenance, and validation infrastructure has succeeded. It gives us a reproducible census of candidate strings in a frozen corpus source. It does not yet establish that CABNC contains enough independently codable form families for the proposed held-out projectibility study.

The appropriate decision is therefore:

> Proceed to a bounded manual pre-pilot, but do not begin the main coding study, claim corpus feasibility, or revise `main.tex` around a completed projectibility result.

The present census identifies 82 provisional retrieval bins that meet the conservative collection-block proxy and 85 that meet the recording proxy. These are upper-bound search bins, not eligible linguistic form families. Several manual and design-dependent judgments remain between retrieval and an analysis-ready sample.
## What has been established
### Frozen source and provenance
The corpus source is a pinned checkout of the CABNC Git repository:

- Repository: `https://github.com/saulalbert/CABNC.git`

- Commit: `0a28a11e168e312d1b9ad406a3352f31c13b86a2`

- Analysed subtree: `data/cabnc_talkbank_chat`

- Subtree object: `7f7f87611350439e404baa8f8c659f33e81efecb`

- Local checkout: `vendor/CABNC-0a28a11`


The acquisition script verifies the commit and subtree. The parser refuses to assign frozen-source provenance if the checkout is dirty or does not match the pinned source. The validator rechecks every source path, byte count, and SHA-256 digest.

Relevant files:

- [Acquisition script](../analysis/acquire-cabnc.sh)

- [Candidate alias inventory](../analysis/cabnc-form-aliases.csv)

- [Census parser](../analysis/cabnc_census.py)

- [Census validator](../analysis/validate_cabnc_census.py)

- [Automated tests](../analysis/tests/test_cabnc_census.py)

### Reproducible corpus census
The validated run contains:

| Quantity | Count |
| --- | ---: |
| CHAT files | 1,860 |
| Original AudioBNC recording IDs | 459 |
| Physical tapes | 273 |
| Collection blocks | 58 |
| Files without a recoverable recording ID | 196 |
| Physical main-tier lines | 246,783 |
| Analytic speaker turns | 244,131 |
| Candidate occurrences | 255,211 |
| Turn-initial candidate occurrences | 103,170 |
| Candidate-only turns | 36,151 |
| Fully timed turns | 186,223 |
| Partially timed turns | 0 |
| Untimed turns | 57,908 |

The parser and validator report version `0.5.0`. Sixteen automated tests pass across the census and pre-pilot schema suites. Repeated census runs produce identical tabular-output hashes. The run manifest intentionally records its execution time and therefore changes between runs; the substantive tabular outputs do not.
### Retrieval procedure
The census uses explicit aliases rather than fuzzy string matching. Within a main CHAT tier it applies longest-match precedence, so a listed multiword expression is retrieved as its own maximal bin rather than simultaneously counted as every component. A multiword expression cannot cross a main-tier boundary.

Adjacent main tiers are merged only when they have the same known listed speaker, both boundary times are available, and the positive gap is no greater than 2.5 seconds. The parser preserves the original same-speaker chain and the reason for every analytic-turn boundary. Timing status is retained separately for the candidate tier and the analytic turn.

The alias inventory currently contains:

- 238 explicit surface aliases;

- 207 provisional retrieval bins;

- 184 bins observed in the corpus;

- 10 explicit orthographic or phonological variant-block hints; and

- 21 complex surfaces carrying component-family flags.


Complex expressions such as _oh dear_, _oh my God_, _damn it_, and _fuck yeah_ have their own retrieval bins and retain links to relevant component families. Vocatives and other controls such as _mum_, _mummy_, _dad_, _daddy_, and _love_ have been added so that the eventual comparison is not restricted to presumed interjections.
## The numerical feasibility proxy
The raw retrieval gate requires at least 25 events, 10 transcript segments, and 10 speakers. A stricter automatic screen additionally requires usable timing, a recoverable recording ID, an available following turn, and known source and next-speaker identifiers.

| Gate | Provisional bins passing |
| --- | ---: |
| Raw retrieval proxy | 103 |
| Screened collection-block proxy | 82 |
| Screened recording proxy | 85  |

The screened proxy contains 74,601 turn-initial candidate occurrences. The automatic event screen excludes 27,737 turn-initial occurrences and leaves 75,433 before the stricter bin-level proxy is applied. High-frequency screened bins include _yeah_, _oh_, _no_, _mm_, _well_, _yes_, _what_, _so_, _right_, and _ah_. There is also promising representation among lower-frequency items and controls.

These figures show that CABNC contains abundant retrievable material. They do not show that 85 independent form families can enter the study. The current `form_family_id` field is retained for implementation compatibility, but its values remain provisional retrieval bins until variant, component, and sign-type adjudication is complete.
## What has not been established
### Conversation and dependence units
CABNC contains 1,860 `.cha` files, but those files are transcript segments rather than 1,860 independent conversations. The source exposes 459 original recording/tape-side IDs across 273 physical tapes, and 196 files lack a recoverable recording identifier. The three-character BNC prefix yields 58 conservative collection blocks. None of these levels is automatically an exact conversation boundary.

The principal study requires defensible grouping for training, holdout, and uncertainty estimation. We therefore cannot substitute transcript-file counts for conversation counts or yet claim that any bin meets a conversation-level gate.
### Recipient availability
The automatic screen establishes the presence of a following turn by a known speaker. It does not establish that this speaker was an intended or ratified recipient, heard the candidate, or had an opportunity to respond. Recipient availability remains a manual coding question.
### Sign-type and homograph adjudication
String retrieval does not classify conventionalized constructional uses. Forms such as _well_, _right_, _what_, _like_, _look_, _good_, and _love_ retrieve heterogeneous uses. Even apparently clearer forms may have reading- or position-specific exclusions. Source-category admission must be determined from a dossier that is insulated from recipient-treatment evidence.
### Leakage-free family folds
The alias table records initial variant-block hints, including _ok/okay_, _ay/aye_, _er/erm_, _hm/hmm_, _sh/shh_, _phew/whew_, _oops/whoops_, _oi/oy_, _um/umm_, and _yah/yeah/yeh_. These hints have not yet been converted into a final, linguistically adjudicated fold map.

Complex forms create a second leakage risk: a model must not train on _oh_, for example, and then count performance on _oh dear_ as generalization to an unseen family without an explicit component-blocked sensitivity analysis. We cannot yet claim that no variant or component relation crosses folds.
### Turn construction and timing
The revised parser no longer leaves a positive internal gap over 2.5 seconds inside an analytic turn. Missing boundary timing and changes involving unknown or unlisted speakers also force a split. The retained mechanical rule still requires manual validation against sampled transcript and audio context before analytic turns can be treated as interactionally adequate units.

Candidate timing is often sufficient for retrieval, but the study's sequential outcomes may require a defensible turn-constructional-unit or audio window. Fully timed transcript turns should not be described as automatically providing token-level or interactionally complete timing.
### Linguistic eligibility and the projectibility result
No recipient-treatment outcomes have been coded. No blinded reliability exercise has been run. No held-out model has been fitted. The census therefore establishes neither cross-domain projectibility nor a category effect. It supplies infrastructure and a candidate sampling frame for testing those claims.
## Claim boundary
The following statement is currently warranted:

> A verified, frozen CABNC source supports reproducible retrieval of a large set of candidate forms and controls. Eighty-two provisional retrieval bins meet the conservative collection-block proxy and 85 meet the recording proxy, justifying a bounded manual feasibility assessment.

The following statements are not currently warranted:

- CABNC contains 82 or 85 eligible or independent form families.

- The proxy-passing bins meet a conversation-level threshold.

- The current folds prevent variant or component leakage.

- A following turn is a recipient response.

- Transcript timing alone supports the intended sequential coding.

- The corpus demonstrates that interjection-category membership predicts recipient treatment.


The corpus parser also emits no warnings under its narrow structural warning rules. That should not be paraphrased as a claim that the CHAT data are globally clean or interactionally unambiguous.
## Bounded manual pre-pilot
The next stage should answer feasibility questions rather than estimate the paper's headline result.
### 1. Validate turn collapse
Audit a principled sample of merged and split same-speaker chains, including long-gap, missing-timing, and unknown-speaker boundaries. Record whether each mechanical boundary yields one usable turn, separate turns, or an interactionally indeterminate case. Freeze the validated rule before sampling the coding pilot.
### 2. Establish grouping units
Use transcript metadata and, where permitted, the associated recording structure to determine how recording IDs, episodes, transcript segments, and conversations relate. Produce an explicit grouping table and state which level will block folds and which will enter the hierarchical model.
### 3. Freeze variant and component relations
Adjudicate the provisional variant blocks. Separately flag compositional or lexical-component relationships. Define the principal leave-one-family-out folds and the stricter component-blocked sensitivity folds before outcome coding.
### 4. Prepare sign-type dossiers
For a deliberately small, heterogeneous set of candidate and comparison forms, prepare source-only dossiers containing the evidence allowed for `INTERJECTION_syn` and `INTERJECTION_sem` classification. Exclude recipient treatment and the exact outcome windows from these dossiers.
### 5. Run a blinded double-coded pilot
Independently code:

- source-side immediate cues;

- recipient availability;

- recipient treatment; and

- exclusions or indeterminacy.


The pilot should test whether the layers can be kept separate, whether coders can apply the outcome scheme reliably, and whether enough events survive manual exclusions within entire held-out families. It is not a miniature significance test.
### Stop or redirect conditions
Redirect to the semantic-repetition experiment if the manual pre-pilot shows that:

- conversation or dependence units cannot be reconstructed adequately;

- recipient availability is routinely indeterminate;

- audio access or timing is insufficient for the target outcomes;

- sign-type/source classification cannot be insulated from recipient outcomes; or

- the eligible family distribution collapses below a credible held-out design.

## Effect on the manuscript
`main.tex` remains untouched. This protects the architectural reconstruction from being organized around an empirical result that has not yet been shown feasible.

If the CABNC pilot succeeds, the paper can distinguish clearly among:

1. the three inquiry-relative category cuts;

2. the network relations hypothesized among them;

3. the particular cross-domain edge tested in held-out data; and

4. the broader edges left as explicit hypotheses.


If it fails, the architectural repair remains valid. The direct empirical test should then move to the pre-specified semantic-repetition experiment rather than being simulated through stronger prose about the existing evidence.
## Independent checks and model use
Independent methodological audits identified the conversation-unit, unknown-speaker, partial-timing, occurrence-ID, alias-leakage, component-overlap, and vocative-control issues now reflected in the pipeline and this claim boundary. Their outputs were treated as correlated critical evidence, not votes.

A local Mistral model was also tried as an optional mechanical candidate-recall screen. It stalled on both large and reduced prompts and produced no usable suggestions. No local-model output was incorporated into the alias inventory or methodological decisions.
## Proposed decision
Approve the bounded manual pre-pilot while retaining all three restrictions:

1. the 82 collection-block and 85 recording-proxy bins remain upper-bound retrieval results;

2. no full coding study begins until grouping, folds, dossiers, and pilot reliability are frozen; and

3. no claim of demonstrated projectibility enters the manuscript before held-out results exist.

---
comments:
  c1:
    body: all looks good
    by: user
    at: 2026-07-27T21:06:43.991Z
