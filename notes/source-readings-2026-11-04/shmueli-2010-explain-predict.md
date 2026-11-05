# Source reading: shmueli-2010-explain-predict
<!-- SUMMARY: subagent reading report on shmueli-2010-explain-predict for the matrix-lesion plan and the working paper, saved verbatim by the parent session · status: received; every source quotation string-checked by the parent against the PDF text, all found · updated: 2026-11-04 -->

Saved verbatim by the parent Claude session from the subagent's final report (agent a2500d16c130e895c). Model output, not a source. The parent string-checked every quotation attributed to the source against the PDF text (2026-11-04) and found all of them; page numbers were not rechecked, and quoted phrases from FREEZE-v4 or the paper, and the agent's own proposed wording, are not source quotations.

**Pagination.** The local PDF and .md are the arXiv reprint, which "differs from the original in pagination and typographic detail" (reprint p. 1). Pages below are reprint pages; the journal's pages (289–310) can't be recovered from this copy. Shmueli isn't in the central bib, the project, the HPC book or `lit`, so she needs a `references-local.bib` entry: Galit Shmueli, "To Explain or to Predict?", *Statistical Science* 25(3): 289–310 (2010), https://doi.org/10.1214/10-STS330.

## 1. Her argument

**Definitions (p. 3).**
- Explanatory modelling: "the application of statistical models to data for testing causal hypotheses about theoretical constructs".
- Predictive modelling: "the process of applying a statistical model or data mining algorithm to data for the purpose of predicting new or future observations".
- Descriptive modelling: "aimed at summarizing or representing the data structure in a compact manner", where "the focus is at the measurable level rather than at the construct level".

**Sources of the difference.** "measurable data are not accurate representations of their underlying constructs" (p. 5). She names four aspects (pp. 5–6): causation–association, theory–data, retrospective–prospective, and bias–variance. On the last: "In explanatory modeling the focus is on minimizing bias to obtain the most accurate representation of the underlying theory. In contrast, predictive modeling seeks to minimize the combination of bias and estimation variance" (p. 6).

**How the modelling steps differ.**
- Goal: "a priori determination of the main study goal as either explanatory or predictive is essential to conducting adequate modeling" (p. 7).
- Data: in explanation "statistical power is the main consideration"; prediction needs more data because "f itself is often determined from the data" (p. 7).
- Missing data: missingness dummies are "considered unsatisfactory in explanatory modeling, but can produce excellent predictions". For prediction, "the important distinction is whether the missingness depends on Y or not" (p. 8).
- Variables: a predictor needs "ex-ante availability" (p. 10).
- Methods: explanation "requires interpretable statistical models f that are easily linked to the underlying theoretical model F" (p. 11).
- Validation: prediction targets "generalization, which is the ability of f̂ to predict new data" (p. 11).
- Evaluation: "A common misconception in various scientific fields is that predictive power can be inferred from explanatory power" (p. 12).
- Selection: she quotes Berk on repeated fitting: "Some unjustified optimism remains" (p. 13).

**Prediction in theory testing.** Prediction can "compare competing theories" and supply "benchmarks of predictive accuracy" (p. 4). But "the “wrong” model can sometimes predict better than the correct one" (p. 6). She endorses Hagerty and Srinivasan's conclusion that "the practice in applied research of concluding that a model with a higher predictive validity is “truer,” is not a valid inference" (p. 20).

## 2. Bearing on FREEZE-v4

**What kind of study it is.** In her terms, FREEZE-v4 fits a descriptive model and scores it with a predictive technique; none of it is explanatory. Section 2 calls the latent-class model "the simplest summary of co-occurrence the record can support". The one-cell lesion is leave-one-out cross-validation over cells.

**Where the design fits her.**
- M1 is her predictive benchmark, and M2 is the theory-constrained model whose distance from it she'd want reported (the compression cost). M0 is a floor she doesn't discuss.
- Comparing INTJ with EXPRESSIVE is comparing competing accounts by predictive power.
- Concealing dependent evidence (section 2 step 3) is the nearest analogue to ex-ante availability.
- Berk's warning bears on the v1–v4 development record and the section 9 firewall.

**Where it doesn't.**
- **Record reconstruction isn't prediction in her sense.** Section 3 calls the summary "exact for the frozen inventory and coding", and an exact quantity on a fixed record doesn't estimate performance on "new data". The projective-warrant claim is the predictive one, and her missingness criterion governs it: if documentation depends on the target value, gains on documented cells won't transfer. The "documentation diagnostics" (section 1) should test that dependence.
- **The concealment rule can create missingness that depends on the target.** Section 4 conceals a source cell when the source entails the target value or the reverse. Entailment is specific to values: a covering statement such as "takes no dependents" makes P04 and P06 both N, so a concealed P04 signals that P06 is probably N. M1's missingness indicators can learn that signal (her p. 8 condition, built in by design), and M2 can't. So M1 has to be reported without the indicators as well. Separately, section 4 says applying the rule to reference rows "remains a Brett decision", whereas section 2 step 3 already applies it.
- **Variance confounds the compression and sufficiency contrasts.** An underspecified model predicts better "when the data are very noisy", "when the predictors are highly correlated", and "when the sample size is small" (p. 20). All three hold here, which explains section 2's hub-world result (M2 beat M1 by 0.04–0.06). A near-zero loss(M2) − loss(M3) may mean only that the extra signal in the sources is smaller than the variance of estimating their coefficients. Sufficiency should be read from the residual-dependence checks, with the gap reported as predictive sufficiency at this n.

**Limits.** The study can't show that a grouping is the right carving because it predicts better (p. 20). She has nothing on mechanism or cliquish stability, so on the HPC question itself she bears less than suggested.

## 3. For the paper

Both halves of lines 158–159 are supported (pp. 3, 12; p. 17: "Predictive models for auction price cannot provide direct causal explanations"), and the converse supports lines 1226–1231. A possible sentence:

> \textcite[PAGES]{shmueli2010} draws the same line among models built to summarize data, to predict new observations, and to test causal hypotheses: predictive success isn't evidence of a correct causal account, and a correctly specified model can predict worse than a misspecified one.

Supporting reprint pages: 3, 6, 17, 20. The journal pages are needed.

## 4. Conflicts

- **Projective warrant falls between her categories.** For her, prediction is instrumental ("Direct interpretability ... is not required", p. 5), so a black box that predicts well would satisfy her. Brett's warrant asks whether the *grouping* licenses the expectation, which is why the plan compares M2 with M1. That's a gap in her account, not a contradiction.
- **Converging diagnostics.** Her nearest analogue is factor analysis, whose "factors are expected to correspond to the underlying constructs" (p. 10). She files that under explanatory modelling, as instrument validation. FREEZE-v4 keeps the latent class descriptive and treats posteriors as epistemic, which is the right placement. Reading membership as the construct the diagnostics converge on would move it into her explanatory column.
