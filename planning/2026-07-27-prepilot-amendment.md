# CABNC pre-pilot amendment after construct-validity review

**Date:** 2026-07-27
**Status:** Review checkpoint
**Scope:** Operational study design only; the approved three-category architecture is unchanged

## Why there is a second checkpoint

The approved census report authorized a bounded manual pre-pilot, not a specific set of coder-facing instruments. Building those instruments exposed decisions that would be difficult or impossible to repair after coding. A Claude Code/Claude 5 construct-validity audit identified seven such gaps, and the independent corpus and fold audits supplied two further corrections.

The right response is to amend the protocol before any event is sampled or any outcome is coded. `main.tex` remains untouched.

## Gate A result: interaction structure

The parser now merges adjacent same-speaker tiers only when:

1. the speaker is known and listed;
2. both boundary times are present; and
3. the gap is no greater than 2.5 seconds.

Every split retains its original same-speaker chain and a boundary-reason code. This corrects the earlier unconditional collapse of unknown identities, untimed tiers, and long gaps.

The validated census now contains:

| Quantity | Corrected value |
|---|---:|
| Analytic turns | 244,131 |
| Conservative collection blocks | 58 |
| Physical tapes | 273 |
| Tape sides | 459 |
| Provisional bins passing the screened collection-block proxy | 82 |

The three-character BNC collection prefix is the conservative corpus-wide dependence block. Transcript files, tape sides, and tapes are not called conversations. Exact conversations will be manually adjudicated only for sampled material. Repeated parser runs are byte-for-byte deterministic, all 15 current tests pass, and the independent validator passes.

## Required design amendments

### 1. One primary edge

The earlier wording, “`INTERJECTION_syn` or `INTERJECTION_sem`,” gave the analysis two chances to succeed. The amended primary declaration is:

> Independently assigned `INTERJECTION_sem` membership provides a transportable representation that improves prediction of post-offset next-position trajectory for unseen form families beyond matched immediate cues, `INTERJECTION_syn`, and neighbouring classifications.

The `INTERJECTION_syn` edge is separately declared and secondary. It cannot replace a failed primary result. Choosing the semantics-facing edge makes a non-syntactic category bear the principal empirical risk; it does not give semantics ontological priority.

### 2. A mechanical primary outcome

“Recipient treatment” required a coder to decide whether the next contribution was a fitted response. That judgement could import the coder's own semantic or interactional analysis of the source.

The amended primary outcome is four-way post-offset next-position trajectory:

1. recipient non-minimal entry;
2. recipient minimal entry;
3. source entry; or
4. no vocal entry within 2.5 seconds.

Fittedness is coded separately and used only in a labelled sensitivity analysis. Source entry and silence are no longer collapsed. The immediate-cue model receives TCU completeness and syntactic packaging; if those local properties already determine the trajectory, the category edge fails rather than taking credit for them.

### 3. Audio is a real gate

Every timing field now records its source and resolution. The primary trajectory study admits only audio-measured events. If REB approval, audio access, or measurement quality is unavailable, the CABNC route stops. We will not retrofit a transcript-timed 2.5-second outcome after seeing data. The semantic-repetition experiment is the predeclared fallback.

### 4. The missing token-to-sign-type layer

Dossiers classify sign-types, while target packets contain tokens. The original schemas had no blinded judgement connecting the two, especially for homographs such as *well*, *right*, and *what*.

The amended design adds a double-coded pre-offset token-to-sign-type assignment using opaque frozen sign-type rules. Coders see neither category membership nor the following sequence. Assignment has its own reliability gate, and token uses cannot be reclassified because of their outcomes.

### 5. Eligibility is split

Human coders use pre-offset material only to judge intelligibility, participant identity, potential-recipient availability, timing adequacy, quotation, mention, and reading aloud. Frozen code separately checks clipping, duplication, corruption, and packet boundaries.

This prevents a coder from excluding an event for “no potential recipient” after seeing that nobody responded.

### 6. Source and rival classifications are independent

`INTERJECTION_syn`, `INTERJECTION_sem`, and each neighbouring category are coded in separate randomized passes by distinct coder pairs. Declaration-specific cards precede full-profile cards. Form masking, form guesses, presentation order, and prohibited-evidence exposure are recorded.

Reliability is assessed separately for `syn` and `sem`; an easier grammar-facing judgement cannot conceal failure of the semantics-facing classification. Neighbouring labels cannot be generated by the same coder in the same pass as interjection membership.

### 7. Ten-coder staffing gate

The proposed separation requires two independent coders for each of five roles:

- `INTERJECTION_syn` classification;
- `INTERJECTION_sem` classification;
- neighbouring-category classification;
- pre-offset cue and subsequent opaque sign-type work; and
- post-offset trajectory.

The same cue pair locks its cue judgements before receiving the sign-type task. Recipient-trajectory coders cannot serve in any source, dossier, eligibility, or cue role. Models cannot fill these human coding positions.

If ten suitably trained coders cannot be recruited, CABNC is not an acceptable confirmatory route under this design. That is a feasibility result, not a reason to weaken blinding after the fact.

### 8. Stronger holdout protection

The census's retrieval identifier no longer doubles as sign-type or evaluation family. The operational tables now distinguish surface aliases, retrieval bins, sign-types, strict variants, principal outer blocks, component relations, and pathway relations.

The primary evaluation removes both the held-out outer block and every training bin sharing a directly declared lexical component. A weaker ordinary outer-block result is diagnostic only. A pathway-blocked sensitivity also removes independently documented recruitment or descent relatives, since the paper itself argues that such relatives share residues.

### 9. Fixed pre-pilot size and composition

The pre-pilot has one evaluation point after 160 events: ten from each of sixteen blocks selected without post-offset outcomes:

*oh*, *ooh*, *ah*, *eh*, *ha*, *cor*, *ugh*, *gosh*, *mm*, *er/erm*, *yes*, *no*, *well*, *right*, *mum*, and *thanks/thank you*.

These span expressive candidates, responses, fillers, discourse markers, a vocative, and a routine formula. If a declared block cannot supply ten eligible events, that is a feasibility failure. It is not replaced after target coding.

### 10. Auditable schemas rather than prose promises

The packet now contains:

- 29 validated schema templates;
- a populated controlled-value codebook;
- a 30-item leakage checklist;
- prospective `halt`, `remediable_before_unblinding`, and `note_only` failure classes;
- dossier reservation and speaker registries;
- coder-role and hypothesis-awareness records;
- timing provenance;
- frozen packet, fold-map, and evidence-card hashes; and
- deterministic derivation of the primary outcome.

The strongest possible positive interpretation remains modest: calibrated compression and transport within the CABNC sampling frame. It would not show that the label adds information after its complete diagnostic basis, establish `INTERJECTION_prag`, or prove causal network order.

## Decision requested

Approve the amended pre-pilot protocol with the following consequences:

1. `INTERJECTION_sem` bears the primary empirical risk and `INTERJECTION_syn` is secondary;
2. the outcome is four-way next-position trajectory, with fittedness secondary;
3. audio and ten independent coders are hard feasibility gates;
4. component-blocked evaluation is primary and pathway blocking is a sensitivity analysis; and
5. the fixed 160-event pilot is evaluated once, without outcome-driven replacement.

After approval, the remaining source-only work is to freeze the retrieval/variant/component/pathway tables and build the sign-type dossier cards. No post-offset outcome coding or manuscript reconstruction begins before the staffing, REB/audio, and leakage gates are satisfied.
