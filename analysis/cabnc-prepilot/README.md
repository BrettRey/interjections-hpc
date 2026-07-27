# CABNC bounded pre-pilot manual

**Status:** Draft for independent audit; not yet frozen
**Governing documents:** [pre-pilot protocol](../../planning/2026-07-27-cabnc-prepilot-protocol.md), [architecture contract](../../planning/2026-07-27-architecture-contract.md), and [census decision report](../../planning/2026-07-27-cabnc-census-report.md)

## Purpose

This pre-pilot determines whether CABNC can support a blinded, held-out test of one primary declared projection:

> Independently assigned `INTERJECTION_sem` membership provides a transportable representation that improves prediction of post-offset next-position trajectory for unseen form families beyond matched immediate cues, `INTERJECTION_syn`, and neighbouring classifications.

The separately declared `INTERJECTION_syn` edge is secondary. It cannot replace the primary edge if `INTERJECTION_sem` fails. Selection of the semantics-facing edge as primary tests the standing of a non-syntactic category; it does not give semantics prior ontological status.

It does not estimate that projection for publication. It tests whether the source classifications, comparison variables, recipient outcomes, grouping units, and holdout folds can be constructed without leakage and with adequate reliability and yield.

No finding from this pre-pilot establishes the three-category ontology, `INTERJECTION_prag`, causal direction, category-wide stability, maintenance, or corrective control.

Even the strongest later result would show, at most, calibrated compression and transport within the CABNC sampling frame. The category label is not expected to add information after its complete eligible diagnostic basis is known. A positive result would remain compatible with the classifications proxying stable turn-design properties; the flat-diagnostic and neighbouring-category comparisons determine how much stronger an interpretation is warranted.

## Frozen declaration

| Field | Pre-pilot value |
|---|---|
| Source | Primary: declaration-specific `INTERJECTION_sem`; secondary: separately declared `INTERJECTION_syn` |
| Outcome | Four-way post-offset next-position trajectory within 2.5 seconds: recipient non-minimal entry; recipient minimal entry; source entry; or no vocal entry |
| Bearer | Conventionalized constructional sign-type, nested in a conservative form-family holdout block |
| Population | Selected candidates and controls in the frozen CABNC sampling frame |
| Conditions | Intelligible target-bearing sequence with identifiable participants, a potential recipient, and an unclipped following window |
| Transformation | Primary component-blocked leave-one-outer-block-out evaluation; pathway-blocked sensitivity evaluation |
| Timescale | Immediate treatment following the acoustic offset of the target-bearing TCU |
| Tolerance | Fixed from scientific utility and coding burden before pilot outcomes are examined; pilot variance informs feasibility, not the decision regions |
| Evidential standard | Blinded coding, disjoint source and target evidence, held-out predictive scoring, calibration, and design simulation |
| Failure conditions | Leakage, unreliable source or target coding, inadequate family/cell yield, indeterminate grouping, effectively deterministic immediate cues, or no useful held-out category advantage |

The source classification must not be revised in response to recipient outcomes. A failed projection is demoted or retired under its declared scope; it is not rescued by redefining the bearer after target inspection.

## Identifier layers

The study must not use one overloaded “family” field. The final data model distinguishes:

1. `surface_alias_id`: one normalized string-matching rule and its intended bearer span;
2. `retrieval_bin_id`: a constructionally homogeneous search target emitted by the frozen census;
3. `sign_type_id`: an independently justified conventionalized constructional use;
4. `strict_variant_block_id`: spellings or phonological variants that must remain in one outer fold;
5. `principal_outer_block_id`: the complete unit removed in leave-one-family-out evaluation;
6. typed lexical and component relations that trigger sensitivity exclusions without creating transitive mega-families; and
7. `conversation_block_id`: the independently validated interaction/dependence group.

Retrieval bins are search devices. They do not become sign-types or holdout families merely because a string matcher assigned them an identifier.

All new identifiers are opaque. Category labels, neighbour labels, and expected outcomes never appear inside an identifier. The current census's descriptive `form_family_id` survives only as `legacy_form_family_id` for traceability.

The authoritative lexical/fold tables are `surface-aliases`, `retrieval-bins`, `sign-types`, `form-relations`, and `outer-block-membership`. `fold-map-template.csv` is only a convenient derived view and cannot override those tables.

## Roles and separation

| Role | May see | Must not see |
|---|---|---|
| Grouping/turn adjudicator | Corpus metadata, transcript segmentation, relevant audio if approved | Category hypotheses or post-offset trajectory summaries |
| Dossier compiler | Form identity, external sources, dossier-only corpus evidence | Target-event outcomes and target-sample response frequencies |
| `INTERJECTION_syn` classifier | Randomized standardized cards for the grammar-facing classification only | Semantic or neighbour decisions, target events, outcomes |
| `INTERJECTION_sem` classifier | Randomized standardized cards for the semantics-facing classification only | Syntactic or neighbour decisions, target events, outcomes |
| Neighbour classifier | One independently presented neighbouring classification at a time | Interjection-category decisions, target events, outcomes |
| Token-to-sign-type coder | Pre-offset event and frozen opaque sign-type rules | Category membership, post-offset sequence, outcomes |
| Immediate-cue and pre-offset eligibility coder | Preceding context and target-bearing TCU through acoustic offset | Dossier labels, post-offset silence or speech, outcomes |
| Recipient-trajectory coder | Target event and ensuing sequence, with lexical form visible | Source-category labels, cue labels, sampling stratum, predictions |
| Leakage auditor | Packet manifests, masks, hashes, joins, and coding histories | Linked unblinded analysis until audit is complete |
| Lead analyst | Frozen coded layers after audit | No role-specific exception; the lead may not repair labels from outcomes |

No recipient-trajectory coder may serve in a source, token-assignment, cue, pre-offset eligibility, or dossier role. The `syn`, `sem`, and neighbour classifications use distinct coder pairs. Immediate cues are locked before the same pair performs any token-to-sign-type assignment. Adjudication within one layer cannot consult another layer.

The staffing gate is evaluated before packet generation. The design requires ten independent coders: two each for `syn`, `sem`, neighbours, pre-offset cue/sign-type work, and recipient trajectory. Dossier compilation, grouping, and leakage auditing may use additional non-target personnel. Models cannot fill these human coding roles.

## Work order and freeze points

### Gate 0: authority and audio

1. Obtain Humber's written REB determination for CABNC audio access and coder exposure.
2. Confirm authenticated AudioBNC access and the permitted local-storage workflow.
3. Audit 40 timed events spanning at least eight pilot blocks for target-tier location, clip completeness, and alignment.
4. Measure boundaries at 10 ms resolution; on a double-marked subset require median absolute coder difference no greater than 50 ms and the 95th percentile no greater than 100 ms.
5. If authority, access, alignment, or measurement quality fails, activate the semantic-repetition fallback before packet generation.

### Gate A: interaction structure

1. Use the validated mechanical rule: merge adjacent same-speaker tiers only for a known listed speaker when both boundary times exist and the gap is no greater than 2.5 seconds.
2. Preserve the original same-speaker chain and boundary reason for every split.
3. Use the three-character BNC prefix as `collection_block_id`, the conservative independence and separation block.
4. Retain tape, tape-side, segment, and manually adjudicated sampled-conversation identifiers as distinct levels.
5. Freeze sampled `conversation_block_id` values where the metadata and permitted audio support them.

No family-yield claim may use “conversation” before Gate A is frozen.

### Gate B: lexical and constructional structure

1. Freeze the broad candidate alias inventory.
2. Adjudicate strict variants without recipient evidence.
3. Record typed component and constructional relations, including the intended bearer span inside complex matches.
4. Define pilot sign-types from source-only evidence.
5. Freeze strict outer blocks, direct component exclusions, and diachronic/pathway relations.
6. Make component-blocked evaluation primary; preserve the ordinary outer-block evaluation as the weaker diagnostic analysis.

No target outcome may be inspected while making these decisions.

### Gate C: packet construction

1. Confirm that the ten-coder staffing gate is satisfied.
2. Freeze a SHA-256-ranked draw order of fifteen pre-offset candidates for each of sixteen declared pilot outer blocks without inspecting outcomes.
3. Reserve dossier collection/conversation blocks and speakers away from target events.
4. Generate full-profile source, declaration-specific source, and 240 immediate-cue/pre-offset eligibility packets.
5. Select the first ten eligible and assigned events per block in the frozen draw order, then generate at most 160 recipient-trajectory packets.
6. Hash every packet and verify masking automatically.
7. Assign pseudonymous `packet_event_id` values; keep the occurrence-ID and sign-type joins outside coder files.

### Gate D: blinded double coding

1. Double-code `syn`, `sem`, and each neighbour classification in separated passes.
2. Double-code immediate cues and pre-offset eligibility.
3. Lock the cue files, then double-code token-to-sign-type assignments.
4. Double-code post-offset trajectory and fittedness separately.
5. Resolve only within-layer disagreements.
6. Run the enumerated leakage audit before joining layers.

### Gate E: feasibility decision

Evaluate once, after all 240 pre-offset candidates and all selected target packets have completed their applicable layers. Compute per-category reliability, token-assignment reliability, cue and trajectory reliability, indeterminacy, block/cell yield, trajectory variation, differential attrition, dominance, and design-simulation diagnostics. All pilot occurrences are excluded from confirmatory training and scoring. Fresh occurrences from the same outer blocks may enter a later confirmatory sample.

## Layer 1: sign-type dossier

### Dossier unit

A dossier describes one proposed `sign_type_id`, not an orthographic string in the abstract and not an individual target token. Constructional distinctions may be grammatical, semantic, or independently established interactional distinctions. Target-treatment differences alone never justify splitting a sign-type.

### Evidence records

Each factual claim is stored in long form in `dossier-evidence.csv`. Required tags include:

- evidence domain: `phonology`, `morphology`, `syntax`, `semantics`, `interaction`, `diachrony`, or `other`;
- evidence source: publication, reference work, corpus segment reserved for dossier construction, or analyst judgement;
- bearer scope and variety;
- whether the fact is available for full-profile classification;
- whether it is available for this declaration-specific classification;
- whether it is the target, a prohibited close proxy, or safe source evidence; and
- citation, locator, and confidence.

The declaration-specific evidence card removes the target token's response, target-sample response frequencies, and the following close proxies:

- observed recipient uptake or fitted next action;
- treatment of the target event as a complete move;
- post-offset recipient onset or response latency;
- source resumption versus recipient action in the target window; and
- any summary computed from target packets.

Full-profile classification may contain independently established mixed-domain facts, but it is a labelled sensitivity variable rather than the primary source for this declaration.

### Required classifications

Each source-classification row contains one judgement only. `syn`, `sem`, and each neighbour are assigned in separate randomized passes by their designated coder pairs. For both interjection classifications, record:

- `yes`, `no`, or `uncertain` full-profile membership;
- `yes`, `no`, or `uncertain` declaration-specific membership;
- confidence on the frozen ordinal scale;
- the decisive evidence record IDs; and
- an explicit account of any difference between the two judgements.

Declaration-specific cards are always coded before full-profile cards. Card order and presentation position are recorded. A coder cannot view the two card types side by side. Form-masked cards record whether the form was guessed. If prohibited evidence is seen, the dossier is quarantined under a rule frozen before Gate C; it cannot be retained or removed after its target performance is known.

Record neighbouring classifications independently, one category per row: supplement, expressive, response token, discourse marker, routine formula, filler, vocative, parenthetical, nonlexical vocalization, ordinary lexical response, and other specified neighbour. A neighbour win is preinterpreted as evidence that an established interaction-facing or neighbouring representation carries more sequential information than the tested source cut. It does not by itself establish `INTERJECTION_prag`.

### Dossier reservations

Every corpus-derived evidence record names its segment, collection block, sampled conversation block where available, and speakers. A separate reservation table is populated at compilation time. Target sampling mechanically rejects every reserved collection block and every resolved or unresolved matching speaker. There is no yield waiver. Unlogged corpus evidence cannot enter a dossier.

### Token-to-sign-type assignment

The dossier defines sign-types, but target tokens enter the analysis only through a separate pre-offset assignment. Two coders receive the cue packet and opaque sign-type rules. They assign a token to one frozen `sign_type_id`, record alternatives and confidence, or mark it outside all frozen sign-types. They never see category membership or the post-offset sequence.

This assignment has its own reliability and indeterminacy gate. A token cannot be reassigned because its recipient trajectory is inconvenient. The analysis join between event, sign-type, and dossier is generated only after the leakage audit.

## Layer 2: immediate-cue coding

The cue packet ends at the acoustic offset of the target-bearing TCU. It contains up to two preceding TCUs, capped at 12 seconds, plus the complete target-bearing TCU. It cannot expose post-offset silence, a following tier, recipient onset, or the source speaker's later continuation.

Code what is locally observable rather than inferring a category label. Required fields include:

- turn and TCU position;
- standalone or syntactically integrated realization;
- TCU completeness at crop point;
- prior action type and clause type;
- addressivity and count of potential recipients;
- duration, syllable count, and speech rate when measurable;
- prosodic independence;
- pre-target pause and pre-offset overlap;
- directly observable stance polarity or intensity;
- repetition and complement presence; and
- technical or context insufficiency.

Do not code “interjection-like,” expected response, response relevance, or any post-offset property.

Timing provenance accompanies every measured duration, pause, or overlap. Prosodic independence records whether its basis is audio or transcript only. Lexical frequency and familiarity are joined from an independently frozen, hashed source rather than entered by cue coders.

Immediate cues are locked before those coders receive the opaque token-to-sign-type task. Any contradiction between a target coder's TCU judgement and the frozen analytic turn boundary is logged; it cannot rewrite the parser after packet generation.

## Pre-offset and mechanical eligibility

Human eligibility judgements use the pre-offset packet only. They cover intelligibility, participant identity, potential-recipient availability at offset, timing adequacy, quotation, metalinguistic mention, and reading aloud. Actual response or nonresponse is never evidence for recipient availability.

Frozen code, not a human who can see the outcome, checks whether the following packet is unclipped, duplicated, corrupt, or incorrectly bounded. The two eligibility components are joined mechanically. Neither may be revised after source labels and trajectories are linked.

The primary trajectory study requires `audio_measured` timing with a declared resolution. If REB approval, audio access, or measurement quality is unavailable, the CABNC trajectory route stops. It is not converted after coding into a transcript-timed 2.5-second analysis. The predeclared semantic-repetition study then becomes the direct test.

## Layer 3: post-offset trajectory coding

The target packet contains the same preceding context and target-bearing TCU, followed by the later of five post-offset seconds or two complete subsequent TCUs, capped at 12 seconds. The lexical form remains visible. Candidate categories and controls are intermixed.

### Mechanical observations

Record the mechanical fields from which frozen code will derive the trajectory:

- first post-offset speaker, form, TCU shape, and onset;
- whether that speaker was an addressed or ratified recipient;
- gap or overlap;
- whether the first vocal entry begins within 2.5 seconds;
- whether the first entry is by the source or another participant;
- whether an other-participant first entry is minimal or non-minimal;
- whether the source speaker resumes the same trajectory;
- whether another participant's entry is minimal or non-minimal;
- whether 2.5 seconds pass without any vocal entry;
- competitive overlap; and
- technical or contextual problems.

### Derived primary trajectory

- `RECIPIENT_NONMINIMAL_ENTRY_2500`: another participant produces the first vocal entry within 2.5 seconds and it is non-minimal.
- `RECIPIENT_MINIMAL_ENTRY_2500`: another participant produces the first vocal entry within 2.5 seconds and it is minimal.
- `SOURCE_ENTRY_2500`: the source speaker produces the first vocal entry within 2.5 seconds.
- `NO_VOCAL_ENTRY_2500`: no participant produces a vocal entry within 2.5 seconds.
- `COMPETITIVE_OR_OTHER`: competitive entry or another trajectory that cannot enter the principal contrast.
- `UNCODABLE`: insufficient evidence for a defensible trajectory label.

Coders do not enter this label. Frozen code derives it from first-entry timing, vocalizer type, and minimality, with `NO_VOCAL_ENTRY_2500` taking precedence over any entry beginning later in the longer context packet. This is a `post_offset_next_position_trajectory`, not yet an interpretation of recipient uptake. The four primary levels remain separate. `COMPETITIVE_OR_OTHER` and `UNCODABLE` rates are reported by source cell, and differential attrition beyond the frozen tolerance fails the gate.

Fittedness is coded separately: whether the recipient entry is interpretable as a fitted response to the target-bearing TCU. A frozen derivation produces the primary four-way outcome and a labelled fitted-response sensitivity outcome. Coders never enter a second “collapsed” outcome manually.

## Eligibility

Eligibility is assembled from the pre-offset human layer and mechanical packet checks. An event requires:

- intelligible target-bearing material;
- identifiable participants;
- at least one plausible potential recipient;
- an unclipped following sequence; and
- no quotation, metalinguistic mention, reading aloud, transcription corruption, or mechanical duplicate.

Silence, overlap, same-speaker continuation, and a candidate-only turn are not automatic exclusions. An event without adequate audio timing fails the primary study's pre-offset timing criterion rather than being assigned an estimated trajectory.

Every exclusion receives a prespecified code and evidence note. Silence, source entry, and lack of uptake are outcomes rather than exclusions. No exclusion may be invented after inspecting its effect on category performance.

## Pilot sampling

The pilot begins with 240 pre-offset candidates: fifteen from each of sixteen source-selected outer blocks. The first ten eligible and assigned events in each frozen draw order proceed to post-offset coding, for at most 160 target packets. The declared block list is:

1. *oh* and its anchor constructions;
2. *ooh*;
3. *ah*;
4. *eh*;
5. *ha*;
6. *cor*;
7. *ugh*;
8. *gosh*;
9. *mm*;
10. *er/erm*;
11. *yes*;
12. *no*;
13. *well*;
14. *right*;
15. *mum*; and
16. *thanks/thank you*.

Opaque block IDs replace these labels in coder-facing material. The list supplies expressive candidates, response forms, fillers, discourse markers, a vocative, and a routine formula without consulting post-offset trajectories. If a listed block cannot supply ten eligible events under frozen source rules, that is a feasibility failure for the declared pilot; it is not replaced after outcome coding.

Sampling principles are:

- seek informative source-side variation without treating anticipated classifications as observed facts;
- include neighbouring controls, especially vocatives, discourse markers, formulas, fillers, and minimal lexical responses;
- include both high- and moderate-frequency retrieval bins;
- admit at most two candidates per speaker per pilot block and two per collection block per pilot block;
- avoid allowing *oh*, *yeah*, or *mm* to dominate;
- exclude every pilot occurrence from confirmatory training and scoring; and
- sample without consulting post-offset trajectories.

No interim feasibility decision occurs before all 240 pre-offset packets and all selected target packets reach their declared stages. A block must yield at least ten eligible assigned events from its fifteen candidates. At least eight of the ten target packets must produce a primary-codable trajectory, while global uncertain or uncodable rates must remain at or below 15%. Selection and replacement follow the frozen draw order without using post-offset information. Fresh events from the same block may later enter confirmation. The pre-pilot must determine whether the full study can satisfy the block and event gates without weakening the declaration after seeing outcomes.

## Reliability and stop rules

Proceed beyond the pre-pilot only if the applicable gates in the approved protocol remain credible. In particular:

- the ten-coder role-separation and training gate passes before packets are released;
- pilot `INTERJECTION_syn` and `INTERJECTION_sem` nominal alpha is at least `.80` separately, with raw agreement at least `.85`; confidence intervals are reported but do not gate this small pilot;
- the principal neighbour labels -- expressive, response token, discourse marker, routine formula, filler, vocative, and supplement -- each reach pilot nominal alpha of at least `.75`, with raw agreement at least `.80`;
- pilot token-to-sign-type assignment reaches nominal alpha of at least `.80`, with raw agreement at least `.85`;
- pilot post-offset trajectory reaches nominal alpha of at least `.70`, with raw agreement at least `.80`;
- no primary field above 15% uncertain or uncodable;
- sufficient variation within at least half the retained families;
- no leakage-audit failure;
- no dominant family, speaker, or conversation block; and
- a non-degenerate immediate-cue comparator.

Also report Gwet's AC1, raw agreement, confusion matrices, and cluster-bootstrap intervals by form family. Thresholds are operational gates, not evidence for the substantive projection.

A joint `syn+sem` representation can be reported only if each classification independently clears its reliability gate. Pooling cannot let an easier grammar-facing judgement conceal failure of the semantics-facing one. Confirmatory coding retains the stronger lower-confidence-bound gates from the protocol after design calculations establish an adequate number of dossiers and events.

The negligible and useful predictive regions are frozen from scientific utility and coding burden before pilot outcomes are inspected. Pilot-derived variance components may inform whether the confirmatory design is feasible; they cannot move the decision regions.

If grouping, blinding, reliability, yield, or design identifiability fails, stop the CABNC route and activate the predeclared semantic-repetition experiment. Do not recover the corpus study by changing membership rules or excluding failed families after outcome inspection.

## Files and audit trail

The schema templates in this directory define the allowed joins and coding fields. Generated packets, transcript excerpts, audio, keys linking pseudonymous packet IDs to corpus occurrences, and completed coder files remain local and outside version control unless their licensing and privacy status has been explicitly cleared.

Every freeze records:

- corpus commit and subtree object;
- parser and alias-table hashes;
- grouping-rule version;
- fold-map version;
- dossier-evidence-mask version;
- packet-generation code and random seed;
- coder assignment manifest;
- adjudication history; and
- output hashes.

The lead owns theoretical interpretation and manuscript prose. Automated tools may validate schemas, hashes, masking, and joins; they may not assign final category membership or post-offset trajectories.

## Fold-integrity rule

Every retrieval bin belongs to exactly one principal outer block. Every sign-type inherits its retrieval bin's block. A strict variant block is wholly contained within one principal outer block.

For a held-out principal block, the primary fold removes that block and every training bin sharing a directly declared content-bearing lexical atom or unresolved audio-confusability relation with it. Expansion stops after that direct comparison: exclusions are not recursively followed through other excluded bins. The weaker ordinary outer-block fold is reported only as a diagnostic.

A pathway-blocked sensitivity fold additionally removes forms connected by an independently documented recruitment, substitution, or descent relation. This tests the paper's own path-dependence concern rather than assuming form families are exchangeable. Pathway relations are frozen from diachronic evidence before target coding.

The pathway relation graph over the sixteen declared pilot blocks is published before packet generation. A pathway-blocked fold is interpreted only if at least ten training outer blocks remain, including at least four blocks on each side of the frozen primary `sem` contrast. Otherwise the sensitivity is reported as structurally unidentified rather than fitted after relaxing the graph.

This distinction supports two claims of different strength:

- the primary analysis tests generalization without exposure to the held-out form's declared lexical material;
- the ordinary outer-block analysis estimates how much the result depends on component exposure; and
- the pathway-blocked analysis estimates how much it depends on historically related families.

All relations and exclusions are frozen before post-offset trajectory coding. Pronouns, determiners, and high-frequency function words cannot become blocking atoms merely because they occur inside a formula.
