# Source reading: erosheva-etal-2007-gom
<!-- SUMMARY: subagent reading report on erosheva-etal-2007-gom for the matrix-lesion plan and the working paper, saved verbatim by the parent session · status: received; every source quotation string-checked by the parent against the PDF text, all found · updated: 2026-11-04 -->

Saved verbatim by the parent Claude session from the subagent's final report (agent a0a6c6b682e6d7df6). Model output, not a source. The parent string-checked every quotation attributed to the source against the PDF text (2026-11-04) and found all of them; page numbers were not rechecked, and quoted phrases from FREEZE-v4 or the paper, and the agent's own proposed wording, are not source quotations.

**Verdict.** A two-profile grade-of-membership (GoM) model would be easy to add to the current EM. It uses the same per-item machinery plus one extra hyperparameter. But at 46 rows it can't deliver what FREEZE-v4 wants: the degree-of-membership result would mostly reflect the prior, and the lesion scores would barely change. It's worth using as a sensitivity analysis and as a fake-data world, not as the membership model.

Source: Elena A. Erosheva, Stephen E. Fienberg & Cyrille Joutard, "Describing disability through individual-level mixture models for multivariate binary data", *Annals of Applied Statistics* 1(2): 502–537 (2007), https://doi.org/10.1214/07-AOAS126. Page numbers below are the arXiv reprint's (0712.2124), not the journal's.

**1. The model**

Each individual has a membership vector g, "a latent partial membership vector of K nonnegative random variables that sum to 1" (§3, p. 5). Extreme profile k gives the item probabilities λkj for "a complete member of extreme profile k" (p. 9). Given g, item j's probability is "a convex combination of the extreme profiles' conditional response probabilities" (eq. 2, pp. 5–6). Local independence "says that latent variables fully account for associations among the observed responses" (p. 6).

The two formulations nest in both directions. A K-class latent-class model is a K-profile GoM with g restricted to 0/1 vectors (eq. 4). In the other direction, Theorem 3.2 says "any individual-level mixture model with K components can be represented as a constrained population-level mixture model with K^J components" (p. 8). Each of those classes assigns every item to one profile (eqs 5–8), so individuals "may move between extreme profiles when they respond to different items on the questionnaire" (§5, p. 14).

The authors read g in two ways. Admixed individuals "do not simply belong to one of the original subpopulations with some degree of uncertainty" (§1.1, p. 2). But in GoM's medical origin, "when a diagnosis is uncertain, partial membership reflects this uncertainty" (§3, p. 4).

**Priors and estimation (§4).** g follows a Dirichlet(α) distribution, split into proportions ξ and a spread parameter α0. "The closer α0 is to zero, the more probability is concentrated near the mixture categories; similarly, the larger α0 is, the more probability is concentrated near the population average membership score" (p. 10).
- Priors: Beta(1,1) on λ, ξ uniform, and α0 "a proper diffuse gamma distribution" (p. 10).
- In the application α0 gets Gamma(2,10), because "We expected individual vectors of membership scores to be dominated by one component" (§8.1, p. 22).
- Sampling: Gibbs over the per-item indicators zij, λ and g (eqs 11–13), with Metropolis–Hastings steps for α0 and ξ. Variational EM is offered as an alternative (§4.2).
- The extended GoM (§5) adds a deterministic "stayer" compartment of all-zero respondents.

**Choosing K (§§6–7).** They use truncated Pearson residuals, variational BIC, DIC, AICM and BICM. In simulation, "BICM underestimates and DIC overestimates the true number of profiles in both cases" (p. 20). For a true K of 3, the criteria chose anywhere from 2 to 5 (Table 1). In the application they settle on K = 9 for the basic model and 8 for the extended one. They dropped K = 2 because it is "a monotone unidimensional latent structure model" (p. 22).

**Data size.** The real data are 21,574 records pooled over four survey waves, with 16 binary items; "About 80% of cells in the contingency table have observed counts that are less than 5" (p. 20). The simulations used 5,000 × 16 and 5,000 × 10. In the second, "the number of items and the sample size … were too small to provide reliable distinction among different grades of membership" (§7, p. 19).

**Identifiability** gets no formal treatment; a search for "identifiab" finds only a title in the references. What they do mention:
- label switching, which they couldn't check for K ≥ 9 (pp. 23–24);
- duplicated profiles when the fitted K exceeds the true one (footnote 5, p. 29);
- "ridges in the likelihood function" in older maximum-likelihood methods (§9, p. 32).

**Missing data** isn't handled. I searched missing|nonresponse|incomplete|imput in both the .md and the PDF text. The one hit, "Imputation step", draws the latent z, not missing cells. Individual membership scores are never reported (p. 32).

**2. Bearing on FREEZE-v4**

Per grouping, the model sees six INTJ diagnostics or at most four EXPRESSIVE ones ("Membership model"), not twelve. The current rule that unknown cells contribute nothing carries over directly. That is valid only if missingness is at random; neither model helps if it isn't.

(a) α0 is the only thing a two-profile GoM adds, and 46 rows won't inform it. The paper's estimate is α̂0 ≈ 0.1, meaning "membership vectors are dominated by one component for a majority of individuals" (p. 32). That came from 21,574 records and a prior that already expected it. At 46 rows the posterior for α0 will follow the prior.

(b) This is my derivation from eq. 2, not the paper's. With K = 2, the covariance of two items equals ΔjΔk·Var(g), where Δ is the difference between the two profiles on that item.
- A two-class latent-class model with its profiles pulled inward reproduces every item mean and every pairwise association of any two-profile GoM.
- The two models differ only in three-way and higher associations (four-way when the two profiles have equal weight). Six sparse items on 46 rows can't estimate those.
- On three binary diagnostics, a two-profile GoM has 8 parameters against 7 degrees of freedom, so a three-diagnostic EXPRESSIVE record can't identify it at all.

(c) A concealed cell's predicted probability is E[g | visible]·λ1t + (1 − E[g | visible])·λ2t. That is the same form as M2 ("Probabilities"). One-cell lesion scores see g only through its posterior mean, so they can't separate degree of membership from uncertainty. Also, g's complete conditional (eq. 13) is Dirichlet(α plus the items assigned to each profile). That is a shrunk share of item votes, close to the unthresholded convergence score already in "Comparators".

(d) The confound between thin evidence and real intermediacy ("What the model is, and isn't") moves rather than disappears: a posterior mean of 0.5 can be tight or wide. By my rough arithmetic, six items with Δ = 0.6 leave g with a posterior SD near 0.3. That is about the SD of a uniform prior, so the data barely narrow it.

Telling GoM from latent-class on such data would need many more items and rows, judged on higher-order associations. Even then, by Theorem 3.2 the discrete K^J-class version "cannot possibly be distinguished from the continuous mixture GoM model on the basis of data" (§9, p. 33).

**Recommendation: supplement, don't replace.**
1. Fit a two-profile GoM at a few fixed α0 values, from strongly polarised (bathtub-shaped) to flat, and report it beside the three-class sensitivity. Never estimate α0. The variational E-step (eq. 18) slots into the current EM.
2. Add a two-profile GoM world with real intermediacy to the Round 7 harness ("Fake-data requirement"). Test whether the share of posteriors between 0.2 and 0.8, or the "Residual-dependence checks", can tell it apart from a two-class world.

**3. Fit with Brett's commitments**

These are compatible:
- Converging fallible diagnostics: local independence with item-specific λ, and no diagnostic required.
- Absences count: an observed 0 enters through 1 − λkj (eq. 10).
- No single property decides.

These conflict:
- **Ontic partial membership.** GoM can express it but not detect it (Theorem 3.2; p. 33), and its own authors read g both epistemically and ontically. In "What the model is, and isn't", "the closer match to HPC" should become "a parameterization in which partial membership is expressible".
- **Two profiles are one-dimensional.** With K = 2, g sums to 1, so INTJ degree is just one minus complement degree, and crosscutting categories can't be represented ("Round 7 candidate" already says this). Degree is also relative to how extreme the fitted profiles are, which by (b) trades off against how spread out the memberships are.
- **Local independence stays.** Given g, properties are still independent, so HPC's direct support between properties remains outside the model. The authors themselves say that assumption, for their items, "may be questionable" (§9, p. 33).
