**Assessment of the revised interjections bundle — 2 November 2026**

My judgment is that this revision substantially improves the paper's evidential and logical accuracy. I would keep its central corrections. I wouldn't adopt it wholesale as the finished paper: the positive contribution needs clearer emphasis, and one part of the empirical withdrawal needs qualification.

The revision has corrected claims that the evidence couldn't support. The editorial task is now to make the resulting, narrower argument worth reading on its own terms. Restoring the stronger claims would undo the most valuable work in this bundle.

I read the complete revised source and its appendices, compared its principal claims with the current draft, checked its new source on *lah*, and commissioned a focused independent verification of the two empirical audits. I also checked citation-key resolution and selected PDF pages. The complete empirical checks and their input hashes are in [the verification report](empirical-check/findings.txt). No existing manuscript, bibliography, analysis input, or project-status file was changed.

**The corrections I would retain**

- **Withdraw the original derivative result.** The local [primary coding script](../../analysis/morphgain-confirmatory-code-primary.py) assigns `verbal_syntax = 1` and `semantic_residue = 1` to every retained row (lines 287–294). All 969 retained rows consequently receive both confirmatory outcomes. Selecting verbal uses was legitimate; counting the automatically assigned semantic outcome as an independent finding wasn't. The revision gets that distinction right.
- **Withdraw the substantive interpretation of the *fie* curves.** The model retains the cited *He* → *FIe* OCR substitutions as observations with three zero codes. The 616-row denominator, 350 prediction-labelled notes, and separate 141-row exclusion file all check out. Reading the saved model reproduces the ordering probability, 0.127875, without refitting. Reproducible arithmetic doesn't repair the denominator. The revised treatment as an invalid test is warranted.
- **Leave the usefulness of the intersection open.** [Revised §5.3](interjections-source/interjections-revised.tex:874) repairs a real argument error. Derivability from component memberships doesn't rule out useful compression, pooling, or interactions under limited evidence. The original claim that overlap supplies no independent projective force was too strong. This is a substantive improvement to the thesis, not merely softer wording.
- **Keep external integration separate from internal complementation.** [Revised §2.3](interjections-source/interjections-revised.tex:175) handles *damn these mosquitoes!* much better. An expression can be externally detached while having internal dependents. The disputed lexical analysis remains a distinct question.
- **Keep the identity discipline and the distinction between semantic continuity and expressive meaning.** A failed prediction can't automatically create a new sign-type; a verb describing a source-related response needn't itself contribute expressively. These corrections address two ways the previous account could protect itself from counterevidence.
- **Keep the fairer treatment of alternatives.** The revision acknowledges what constructional and diachronic prototype accounts can already explain. It also separates frequency variation from category boundaries, inventory turnover from profile stability, and historical recruitment from synchronic maintenance.

**The changes I would make before adopting the revision**

1. **Major: make the positive linguistic contribution govern the article.** The revised opening with three uses of *damn* is effective. But the article then spends extensive space specifying what a network would have to establish, while its conclusion acknowledges that no complete network or category-level stability has been established ([lines 936–944](interjections-source/interjections-revised.tex:936)). Sections 3 and 4 still present the framework and causal structure as the centre of the paper.

   The strongest contribution is the separation of grammatical, expressive, and interactional judgments about particular conventional uses. The historical material then shows why some combinations are intelligible in light of recruitment. I would organize the paper around that claim, with the network as a proposal whose status is stated once and maintained consistently. The reader needs a clear account of what these distinctions resolve now. A conceptual contribution can be worthwhile without a new predictive experiment, but it must explain more than why further tests would be desirable.

   A related question remains at [lines 475–487](interjections-source/interjections-revised.tex:475): what does naming the latter two groupings `interjection_sem` and `interjection_prag` accomplish beyond using *expressives* and *interactional resources*? The revision honestly raises this question but doesn't yet give a compact, convincing answer. The contribution may be a disciplined reconciliation of competing uses of *interjection*, rather than three newly established categories. That choice needs to be explicit.

2. **Major: narrow the audit's claim about absent independent measurement.** Appendix B correctly withdraws the primary confirmatory result, but [lines 1077 and 1118](interjections-source/interjections-revised.tex:1077) can be read as saying there is no independent semantic coding anywhere in the record.

   There is a distinct 97-row recoding file. The existing [RESULTS.md](../../analysis/morphgain-confirmatory/RESULTS.md:69) attributes it to Brett and describes it as blind. It contains 22 nonblank notes and secondary judgments differing from the primary record. Those facts establish a distinct recorded pass; they don't independently authenticate the claimed human/blind provenance. If that provenance and the application of the rubric are sound, the sample may supply limited descriptive evidence of source-content continuity among retained derivatives.

   Undefined kappa doesn't make the observations worthless. It means this chance-corrected statistic is uninformative when both margins are constant. Equally, the 97 positive codes don't justify calling the procedure fully reliable. The sample covers only **3 of the 54 confirmatory-window observations**, including none for *ooh*, and includes no rejected rows. It cannot rescue the original early-window claim.

   Suggested correction: scope the absence of independent measurement to the primary pipeline and full confirmatory result; acknowledge the separately recorded sample and its unresolved provenance. Preserve the withdrawal. No replacement confirmatory claim follows from this qualification.

3. **Major: distinguish declaration templates from completed test specifications.** The revised §5 is clearer about leakage, baselines, and the difference between predictive success and representational advantage. Its tables nevertheless remain templates. For example, [Table 4](interjections-source/interjections-revised.tex:844) refers to source and target frames without selecting them, and the surrounding prose says that identity rules and assessment criteria still need to be supplied.

   The hardest practical question is still how to identify the same conventional use in a withheld environment without using the outcome to decide identity. Requiring an independent rule is correct; it isn't yet such a rule. I would either call these prospective templates throughout, or develop one genuinely worked declaration with named environments, the identity rule, an opportunity denominator, a comparison, and a failure criterion. This is a request for a concrete exposition, not a demand to launch another corpus study before the paper can proceed.

4. **Medium: the added *lah* citation supports the example, but the category inference needs another step.** [Line 668](interjections-source/interjections-revised.tex:668) accurately cites Lee's confirmation-seeking example. [Lee (2022), §1 example 3 and §5](https://www.mdpi.com/2226-471X/7/3/203), documents the exchange and derives different pragmatic effects from the particle's not-at-issue contribution together with the utterance's speech act.

   My concern is the inference from an affirmative response to the whole utterance to a conventional sequential job for the particle. That inference may be defensible, but the response alone doesn't establish it. State what *lah* contributes beyond the host's confirmation-seeking action and why that meets the adopted criterion. Otherwise keep this assignment explicitly provisional. Leaving its expressive-category membership unresolved is appropriate.

5. **Medium: consolidate repeated qualifications.** The distinction between predictive success, representational advantage, and causal explanation recurs in the introduction, §3.3, the opening of §5, §5.4, the discussion, and the conclusion ([lines 117, 459, 810, 890, 924, 942](interjections-source/interjections-revised.tex:117)). The sign-identity safeguard also receives several full explanations. These repetitions repeatedly interrupt the linguistic argument.

   I would preserve one clear account of the evidential distinctions, one audit summary with detailed appendices, and local qualifications where they change the interpretation of a specific case. The revised source is actually about 2% longer than the current source: 22,175 versus 21,742 whitespace-delimited tokens, including TeX. Removing unsupported results has not yet reduced the expository load.

   The abstract has the same problem in miniature: it devotes much of its space to limits and future evaluations. It also remains two paragraphs, whereas the [current house-style default](/Users/brettreynolds/projects/LLM-CLI-projects/.house-style/style-guide.md:486) is one concise explanatory paragraph. I would lead with the classificatory problem, the concrete contrasts the analysis preserves, and the resulting claim. The audit's consequence still needs stating clearly.

**Smaller points**

The decade-label versus decade-midpoint discrepancy in [Appendix C](interjections-source/interjections-revised.tex:1160) is real, but centring cancels a common offset in the predictor. It affects the conversion back to calendar years by about five years; it doesn't explain the ordering probability. Treat it as a reporting convention/error, separately from the denominator failure.

All 68 citation keys resolve. *Lee (2022)* is the sole added citation, and *Seifart (2010)* is removed. The standalone bibliography is useful for portability, but it should not replace the live bibliography wholesale: for example, its Poggi chapter record omits editors already present locally. Many other differences are equivalent BibLaTeX field choices. The Linux font substitution likewise supplies no reason to replace the project's native preamble.

The style and terminology scripts produced triage flags, including false positives for terms that the prose does explain. I would not mechanically apply them. Actual clarity fixes include expanding COHA at first use and introducing ELPD before the main-text numerical comparison. These are secondary to the article's structure.

**Projectibility check**

| Check | Status | Evidence and implication |
|---|---|---|
| Declaration | YELLOW | §5 separates source and target, but provides templates with several design fields still open. |
| Inquiry, warrant plan, revision rule | YELLOW | Comparators and kinds of failure are named; useful reach, thresholds, and concrete identity rules remain unspecified. |
| Non-trivial projection | YELLOW | Targets are withheld in principle. No new warranted forward projection is demonstrated, and the text now admits this. |
| Warrant versus world-side claims | GREEN | Descriptive contrast, predictive performance, representation, and causal explanation are separated. |
| Stability versus causal order | GREEN | Neither is inferred merely from the other; turnover is no longer treated as profile stability. |
| Stabilizer versus controller | GREEN | Maintenance hypotheses are qualified and homeostatic control is not claimed. |
| Level and mereology | GREEN | Occurrence, sign-type, inventory, and analyst/participant claims are distinguished. |
| Scope and field relativity | GREEN | Inquiry selects the question; it doesn't determine whether the prediction succeeds. |
| Prospective revision | YELLOW | Post hoc conversion and exclusion are explicitly disallowed, but the operational identity rule remains to be shown. |
| Positioning and conclusion | YELLOW | The conclusion is accurately qualified; the positive payoff receives too little emphasis. |

Projectibility is structurally important here, but principally as a standard for future evaluation. The current evidence supports descriptive contrasts and some historically grounded explanations. It does not establish the whole profile as stable, the proposed synchronic network as causally identified, or maintenance/control across inventory turnover. The revision generally respects those limits.

**Recommendation**

Use this as the basis for the next draft, after correcting the treatment of the 97-row sample. Preserve the empirical withdrawals and the logical repairs. Then make a substantial cut and reorganization around the positive linguistic argument. Keep the causal and predictive proposals where they clarify that argument, and concentrate their methodological requirements in one place. The next step is editorial; this review doesn't require another round of data collection or model fitting.
