# CABNC pre-pilot amendment after construct-validity review
**Date:** 2026-07-27 **Status:** Fully approved and implemented **Scope:** Operational study design only; the approved three-category architecture is unchanged
## Why there is a second checkpoint
The approved census report authorized a bounded pre-pilot, not a specific set of annotation instruments. Building those instruments exposed decisions that would be difficult or impossible to repair after coding. A Claude Code/Claude 5 construct-validity audit identified seven such gaps, and the independent corpus and fold audits supplied two further corrections.

The right response is to amend the protocol before any event is sampled or any outcome is coded. `main.tex` remains untouched.
## Resolutions from the first review
The first review supplied three corrections that materially improve the design:

1. Published studies should guide the interaction-structure decision.

2. The `syn` and `sem` comparisons should be symmetrical where the scientific question is symmetrical.

3. There is no available ten-person human coding team; the study should exploit LLM annotation and local acoustic measurement instead of pretending otherwise.


The consequences are incorporated below. Because they change the annotation architecture and the interpretation of Gate A, this document returns for one bounded second review before the operational schemas are rewritten.
## Gate A result: interaction structure
Published precedent guides this decision but does not supply a ready-made CABNC turn boundary. All eight papers cited in this section were retrieved into the linked central `literature/` holdings before implementation; their titles and DOIs were checked against the downloaded copies. No cited paper remains inaccessible.

- The closest corpus-specific precedent, [Mertens and de Ruiter (2021)](https://doi.org/10.5210/dad.2021.102), identifies the relevant TCU and transition-relevance point manually from CABNC audio, measures timing in Praat, and checks exceptional multi-TCU cases in sensitivity analysis.

- [Heldner and Edlund (2010)](https://doi.org/10.1016/j.wocn.2010.08.002) bridge within-speaker silences below 180 ms to construct inter-pausal units, while distinguishing those acoustic units from interactional turns.

- [Roberts, Torreira, and Levinson (2015)](https://doi.org/10.3389/fpsyg.2015.00509) likewise approximate Switchboard turns by joining same-speaker words across gaps under 180 ms and discard recordings with unreliable timing.

- The direct AudioBNC study by [Rühlemann and Gries (2020)](https://doi.org/10.1016/j.wocn.2020.100976) uses BNC sentence-like units, speaker, and file identifiers, but notes that the sentence-like units only generally match turns.

- [Corps, Knudsen, and Meyer (2022)](https://doi.org/10.1016/j.cognition.2022.105037) show directly that automatically derived speech segments need not be turns and that same-speaker self-continuations require independent linguistic adjudication.

- In a much larger but cleaner dyadic corpus, [Cooney and Reece (2025)](https://doi.org/10.1038/s41598-025-24381-1) find that same-speaker thresholds of 2 seconds or more tend to overmerge turns. Their full procedure cannot be imported because it treats brief interjections and backchannels as secondary speech, which would leak the present target classification.

- [Stivers et al. (2009)](https://doi.org/10.1073/pnas.0903616106) sample across separately identified interactions, cap the contribution of any one interaction, and model responses within interactions rather than treating transcript fragments as independent conversations.


The proposed correction is therefore sharper than the first amendment. The parser constructs **IPU-style analytic spans**, not “analytic turns,” by joining adjacent same-speaker tiers only when the speaker is known and listed, both boundary times are present, and the gap is under 180 ms. Unknown identities, missing timing, speaker changes, and longer gaps force a split. Every span retains the original same-speaker chain and a boundary-reason code. The validated version 0.6.0 run yields 244,922 spans while leaving the 255,211 retrieved occurrences unchanged. The count is sixteen above the provisional dry run because the corpus contains exactly sixteen otherwise eligible boundaries at precisely 180 ms; the frozen strict `< 180` rule splits them.

For sampled material, target-bearing TCU boundaries and same-speaker self-continuations are adjudicated separately from these acoustic spans using source-label-blind packets. The three-character BNC collection prefix remains the conservative corpus-wide dependence block. Transcript files, tape sides, and tapes are not called conversations; sampled interaction identities are separately resolved where the metadata and permitted audio support them.

The 2.5-second value is retained only as the right edge of the outcome window, not as a turn or conversation boundary. Continuous signed latency is retained, and the 1.5-, 2.0-, and 2.5-second summaries are all reported. [Kendrick and Torreira (2015)](https://doi.org/10.1080/0163853X.2014.955997) further show that conclusions can depend on whether timing begins at the first audible component, first word or particle, or base-TCU onset. The revised audio layer therefore records those boundaries separately rather than silently choosing one.
## Required design amendments
### 1. A symmetrical four-model comparison
The `syn` and `sem` analyses are symmetric, paired contrasts within one predeclared multilevel predictive model family, not independent passes or separate votes. They use the same component-blocked form holdouts because shared cases permit paired estimation of predictive-score differences and their covariance, as recommended by [Vehtari, Gelman, and Gabry (2017)](https://doi.org/10.1007/s11222-016-9696-4). The amended comparison set is:

| Contrast | Question | Status |
| --- | --- | --- |
| `B` vs `B + sem` | Does `INTERJECTION_sem` improve transport beyond the category-free baseline? | co-primary, edge-specific |
| `B` vs `B + syn` | Does `INTERJECTION_syn` improve transport beyond the same baseline? | co-primary, edge-specific |
| `B + syn` vs `B + syn + sem` | Does `sem` add useful distinctions conditional on `syn`? | complementarity diagnostic |
| `B + sem` vs `B + sem + syn` | Does `syn` add useful distinctions conditional on `sem`? | complementarity diagnostic |

`B` contains matched immediate cues, independently assigned neighbouring classifications, and symmetrically available form covariates, but no interjection-category label. The conclusions remain edge-specific: success on `syn` cannot rescue failure on `sem`, and success on `sem` cannot rescue failure on `syn`. The paper cannot announce that “interjection categories predict” merely because one of two comparisons succeeds. The conditional contrasts measure non-redundancy, not category legitimacy; two correlated categories may both be useful even if neither contributes much after the other is supplied in full.

The four predictive-score contrasts are reported jointly at the held-out form-block level. Any claim that one category cut contributes more than the other is evaluated as a direct paired difference, not inferred from one edge crossing a decision threshold while the other does not—the error diagnosed by [Gelman and Stern (2006)](https://doi.org/10.1198/000313006X152649). The outcome model partially pools sparse speaker, collection-block, form-family, and trajectory-specific effects under regularizing priors. The `syn` and `sem` coefficients are jointly estimated but are not forced into a two-member exchangeable hierarchy merely to invoke partial pooling; [Gelman, Hill, and Yajima's (2012)](https://doi.org/10.1080/19345747.2011.618213) advice is to model defensible relations among parameters, not to manufacture exchangeability.

If the paper-level claim is that both cuts have projective standing for this target, support is conjunctive: the joint uncertainty distribution must clear both frozen minimum-useful-gain thresholds. No confirmatory `syn × sem` interaction is fitted, because that would invite the false suggestion that the overlap is a fourth category.

The pre-pilot cannot itself count as evidence that either edge is projectible. Before confirmatory outcomes are inspected, design simulations must freeze the predictive score, a minimum practically useful improvement, the simultaneous lower-bound procedure, and a calibration tolerance. A co-primary edge fails if its held-out lower bound does not clear the practical margin, if its calibration is worse than the baseline beyond tolerance, or if any apparent advantage depends systematically on a small set of supposedly central members. Such failure is reported as failure of that declared edge, not redescribed after inspection as support for a nearby target.
### 2. A mechanical primary outcome
“Recipient treatment” required an annotator to decide whether the next contribution was a fitted response. That judgement could import the annotator's own semantic or interactional analysis of the source.

The revised primary outcome is four-way post-offset **floor-transfer trajectory**, with every level bounded at 2.5 seconds:

1. a different speaker produces the first new vocal onset within 2.5 seconds;

2. the source speaker produces the first new vocal onset within 2.5 seconds;

3. no new vocal onset occurs within 2.5 seconds; or

4. valid audio shows simultaneous or competitively overlapping onsets that cannot be uniquely ordered.


Recipient status, minimal versus non-minimal entry, fittedness, same-trajectory continuation, and uptake are separately coded secondary outcomes. They cannot determine the primary label. The immediate-cue model receives TCU completeness and syntactic packaging; if those local properties already determine floor transfer, the category edge fails rather than taking credit for them. The exact signed latency and the first-audible, first-vocal, and first-word-or-particle onsets remain available for audit and threshold sensitivity.

The primary boundary is the first participant-produced vocal onset, excluding an isolated inbreath or non-vocal handling noise. A uniquely ordered onset may begin in overlap with the target TCU and receives a negative signed latency; overlap enters the fourth level only when valid competing onsets cannot be ordered. Speaker ambiguity, corrupt or insufficient audio, and other technical failures produce an `uncodable` record and are handled as attrition, not as a substantive trajectory. “Different speaker” is deliberately not glossed as “recipient” or “response.”
### 3. Audio is a real gate
Every timing field records its source and resolution. Before sampling, Gate 0 requires Humber's written REB determination, authenticated AudioBNC access under an approved storage workflow, and a 40-event audit spanning at least eight pilot blocks.

Each permitted clip is converted locally to a fixed-format lossless PCM WAV. Frozen local code produces a time-scaled waveform, spectrogram, and 10-ms voice-activity proposals. These are measurement aids paired with listening, not ground truth: monophonic AudioBNC material can contain overlap, noise, laughter, clicks, and breaths that a waveform alone cannot identify. A source-label-blind expert audit corrects the proposed boundaries and records separate first-audible, first-vocal, and first-word-or-particle onsets. The audited subset must show median absolute algorithm–expert difference no greater than 50 ms and a 95th percentile no greater than 100 ms for the boundary used in the primary derivation.

Raw audio, waveforms, and spectrograms remain local unless the REB determination and AudioBNC conditions explicitly permit hosted processing. Hosted LLMs receive transcript or evidence-card packets only. If authority, access, alignment, or measurement quality fails, the CABNC route stops. We will not retrofit a transcript-timed outcome after seeing data. The semantic-repetition experiment is the predeclared fallback.
### 4. The missing token-to-sign-type layer
Dossiers classify sign-types, while target packets contain tokens. The original schemas had no blinded judgement connecting the two, especially for homographs such as _well_, _right_, and _what_.

The amended design adds a pre-offset token-to-sign-type assignment using opaque frozen sign-type rules. Each model-family run sees neither category membership nor the following sequence. Assignment has its own agreement and audit gates, and token uses cannot be reclassified because of their outcomes.
### 5. Eligibility is split
Pre-offset annotation alone determines intelligibility, participant identity, potential-recipient availability, timing adequacy, quotation, mention, and reading aloud. Frozen code separately checks clipping, duplication, corruption, and packet boundaries. No pre-offset packet contains the following sequence.

This prevents an annotator from excluding an event for “no potential recipient” after seeing that nobody responded.
### 6. Source and rival classifications use isolated passes
`INTERJECTION_syn`, `INTERJECTION_sem`, and each neighbouring category are annotated in separate randomized, one-shot passes. No conversation state, response, rationale, or output carries from one pass to another. Declaration-specific cards precede full-profile cards. Form masking, form guesses, presentation order, decisive evidence IDs, and prohibited-evidence exposure are recorded.

Agreement is assessed separately for `syn` and `sem`; an easier grammar-facing judgement cannot conceal failure of the semantics-facing classification. Neighbouring labels cannot be generated in the same prompt or context as interjection membership. Source passes never see post-offset material, and target passes never see source labels. This is information separation, not the fiction that model outputs are independent human observers.
### 7. A frozen multi-model annotation panel
The ten-human-coder gate is removed. The subjective fields are instead annotated by a three-family panel:

- one Claude-family model;

- one Gemini-family model; and

- one GPT/Codex-family model.


The exact checkpoints, provider routes, system prompts, decoding settings, JSON schemas, and invocation dates are frozen before annotation. Claude 5 is routed through Claude Code; Claude 4.6 and Gemini models may be routed through Agy when available; the GPT-family run uses Codex. A local open-weight model may be added as a portability stress test, but it does not create another chance for the declared panel to pass. If a provider changes or withdraws a frozen checkpoint during an annotation layer, that entire layer is rerun under one newly frozen checkpoint before outcomes are inspected; old and new versions are not silently pooled.

Each critical source card is sent twice to every family in fresh, stateless contexts with tools, browsing, memory, and manuscript access disabled. The two runs use the same frozen rubric but independently randomized card order. Raw responses, evidence-span references, refusals, parse failures, prompt hashes, and model/version identifiers are retained. A model output that cites unavailable evidence or violates the schema is invalid rather than repaired by hand.

Stateless prompting cannot erase information acquired during model pretraining. Evidence-card grounding, prohibited-evidence checks, and recorded form guesses constrain and diagnose that risk; they do not justify claiming that a familiar form was psychologically unknown to the model.

For source-category labels, a family contributes a vote only when its two runs agree. Confirmatory `yes` or `no` requires three stable family votes in agreement plus Brett's source-only, outcome-blind confirmation. Anything else remains `uncertain`; Brett does not turn panel disagreement into confirmatory consensus after seeing outcomes. For token assignment, immediate cues, and secondary fittedness, a frozen consensus rule is piloted before use.

Brett audits every source-category and principal-neighbour dossier, every token-assignment disagreement, every model instability, a frozen random sample of consensus cue assignments, and every acoustic boundary used in the primary outcome. He is not treated as a ten-person substitute. The audit for a source field never exposes its outcomes, and the audit for a target field never exposes its source labels.

Published work shows that LLMs can equal or outperform crowd workers on bounded text-annotation tasks, including [Gilardi, Alizadeh, and Kubli (2023)](https://doi.org/10.1073/pnas.2305016120) and [Törnberg (2025)](https://doi.org/10.1177/08944393241286471). That precedent justifies a direct pilot; it does not establish validity for these linguistic judgements in advance. Cross-family agreement is therefore reported as **inter-model agreement**, not human intercoder reliability, and the author audit plus evidence grounding remains a separate validity check.
### 8. Stronger holdout protection
The census's retrieval identifier no longer doubles as sign-type or evaluation family. The operational tables now distinguish surface aliases, retrieval bins, sign-types, strict variants, principal outer blocks, component relations, and pathway relations.

The primary evaluation removes both the held-out outer block and every training bin sharing a directly declared lexical component. A weaker ordinary outer-block result is diagnostic only. A pathway-blocked sensitivity also removes independently documented recruitment or descent relatives, since the paper itself argues that such relatives share residues.

For each co-primary edge, a block counts as positive or negative only when its retained sign-types are unanimous under the final declaration-specific panel judgement. Mixed or uncertain blocks count toward neither side minimum. The pathway sensitivity is interpreted for an edge only if at least ten training blocks remain, including at least four on each side of that edge's frozen contrast.
### 9. Frozen pre-pilot selection and composition
The pre-pilot begins with 240 pre-offset candidates: fifteen from each of sixteen blocks selected without post-offset outcomes. Each pre-offset pool is built by scanning its frozen SHA-256 rank while applying the within-block concentration caps. Target selection then proceeds round-robin by within-block rank and frozen block order. Candidates that would breach a global cap are logged and skipped, and scanning continues until ten are admitted per block or the pool is exhausted, for at most 160 target packets:

_oh_, _ooh_, _ah_, _eh_, _ha_, _cor_, _ugh_, _gosh_, _mm_, _er/erm_, _yes_, _no_, _well_, _right_, _mum_, and _thanks/thank you_.

`Mum` is deliberately a kinship-term vocative-NP control, not a presumed negative member of either interjection category. Its source-only sign-type assignment distinguishes standalone summonses, supplementary vocatives within larger TCUs, and referential nominal uses. It tests whether the `syn` edge adds anything beyond supplement function, prosodic isolation, and standalone packaging; for `sem`, it is an adversarial neighbour whose polarity remains to be adjudicated. Addressivity, summons status, TCU completeness, and projected source continuation therefore belong in the category-free immediate-cue layer.

The sixteen blocks span expressive candidates, responses, fillers, discourse markers, a vocative-NP rival, and a routine formula. They test source-side variation and annotation feasibility; they are not preassigned to positive or negative `syn`/`sem` cells. If a declared block cannot supply ten eligible assigned events from its fifteen candidates, that is a feasibility failure. At least eight of the ten selected targets per retained block must yield a primary-codable trajectory. Feasibility is evaluated once, after all 240 pre-offset packets and every selected target packet reach their declared stages. Selection never uses post-offset information.

Within a pilot block, no speaker or collection block supplies more than two candidates. Globally, no speaker supplies more than 5% and no collection block more than 10% of selected targets. Every pilot occurrence is excluded from confirmatory training and scoring; fresh occurrences from the same outer blocks may enter confirmation.
### 10. Pilot reliability gates match pilot size
The pilot replaces human-intercoder gates with four distinct checks:

1. **Inter-model agreement.** `syn` and `sem` each require nominal alpha at least .80 and raw agreement at least .85; principal neighbours require .75 and .80; token-to-sign-type assignment requires .80 and .85; and each principal categorical immediate cue requires .70 and .80.

2. **Within-model stability.** Every critical source card is run twice. Each family must achieve raw repeat agreement of at least .90 on `syn` and `sem` and .85 on the other principal categorical fields. A concealed, hash-selected 15% duplicate set supplies the corresponding check for high-volume token and cue fields.

3. **Expert audit.** Brett reviews all source-category and principal-neighbour dossiers, plus the masked token/cue subsets specified above. Panel–audit raw agreement must reach .85 for `syn` and `sem` and .80 for the remaining subjective fields. Disagreements are reported by field and form block; the audit is a validity check, not another model vote.

4. **Mechanical timing audit.** The waveform/VAD proposal is compared with Brett's masked boundary audit under the 50-ms median and 100-ms 95th-percentile gates above.


The primary four-way trajectory is derived by code from the audited first-entry timing and speaker identity; it does not depend on panel-coded minimality and does not receive an inter-model alpha of its own. No required subjective primary field may exceed 15% combined uncertain and uncodable values, no more than 15% of derived primary outcomes may be uncodable, and source-cell attrition rates may differ by at most 10 percentage points. Confidence intervals are reported but do not gate this small pilot. Stronger confirmatory lower-bound requirements are frozen only after design calculations establish adequate dossier and event counts.

Agreement across Claude, Gemini, and GPT is evidence of cross-family robustness, not three independent samples from a human annotator population. Family-specific stable-label yields and disagreements are reported as diagnostics, but they cannot replace or rescue the declared consensus analysis.
### 11. Auditable schemas rather than prose promises
The implemented packet contains 45 validated schema templates, a populated controlled-value codebook, a 47-item leakage checklist, 29 reliability gates, 14 feasibility gates, prospective failure classes, timing provenance, and frozen packet/fold/evidence hashes.

The approved schema revision adds:

- a model registry with provider route, family, exact checkpoint, settings, and date;

- prompt, packet, response, and evidence-card hashes;

- one-shot pass and duplicate-assignment manifests;

- inter-model agreement and expert-audit tables;

- WAV conversion, waveform, spectrogram, VAD, and onset-measurement provenance;

- separate first-audible, first-vocal, and first-word-or-particle boundaries;

- both co-primary and both conditional model comparisons; and

- deterministic derivation of floor-transfer trajectory at 1.5, 2.0, and 2.5 seconds, with 2.5 seconds retained as the declared primary summary.


The strongest possible positive interpretation remains modest: calibrated compression and transport within the CABNC sampling frame. It would not show that the label adds information after its complete diagnostic basis, establish `INTERJECTION_prag`, or prove causal network order.

One instrument task intentionally remains open: `clause_type` and `prior_action_type` value sets must be developed from practice packets and frozen before Gate C. The leakage checklist treats an incomplete immediate-cue codebook as a halt condition. No pilot reliability or target coding can begin while that item is open.
## Approved decision
The amended pre-pilot protocol has the following consequences:

1. `INTERJECTION_sem` and `INTERJECTION_syn` receive symmetrical, edge-specific co-primary comparisons against one category-free baseline; neither can rescue the other;

2. the two conditional `sem | syn` and `syn | sem` comparisons are complementarity diagnostics, not independent projectibility tests;

3. the outcome is four-way floor-transfer trajectory at 2.5 seconds, with continuous signed timing, shorter-horizon summaries, and minimality, fittedness, and uptake retained separately;

4. the ten-human-coder gate is replaced by a frozen Claude/Gemini/GPT panel, isolated annotation passes, author audit, and local waveform/VAD measurement;

5. corpus-wide parser units are IPU-style spans rather than turns, and sampled TCU/conversation boundaries are separately adjudicated;

6. component-blocked evaluation is primary and pathway blocking is a sensitivity analysis; and

7. the 240-candidate, at-most-160-target pilot is evaluated once, without outcome-driven selection or replacement.


The protocol, schemas, validators, tests, 180-ms span parser, census rerun, and local acoustic-preparation utility are implemented. The next empirical step is Gate 0: obtain the written REB determination, confirm authenticated audio access and storage conditions, and run the 40-event waveform/alignment audit. Retrieval, variant, component, pathway, and sign-type dossier tables can then be frozen in the declared order. No annotation-packet generation, post-offset outcome coding, or manuscript reconstruction begins before the applicable REB/audio, model-panel, agreement/audit, and leakage gates are satisfied.
