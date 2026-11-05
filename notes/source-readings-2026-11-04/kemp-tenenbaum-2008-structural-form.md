# Source reading: kemp-tenenbaum-2008-structural-form
<!-- SUMMARY: subagent reading report on kemp-tenenbaum-2008-structural-form for the matrix-lesion plan and the working paper, saved verbatim by the parent session · status: received; every source quotation string-checked by the parent against the PDF text, all found · updated: 2026-11-04 -->

Saved verbatim by the parent Claude session from the subagent's final report (agent a34232f35487e5ce2). Model output, not a source. The parent string-checked every quotation attributed to the source against the PDF text (2026-11-04) and found all of them; page numbers were not rechecked, and quoted phrases from FREEZE-v4 or the paper, and the agent's own proposed wording, are not source quotations.

No responsibility notice.

**Premise check.** The working paper (/Users/brettreynolds/projects/LLM-CLI-projects/papers/queue/english-interjections/inquiry-relative-categories.tex) never rejects a single scale "from less to more interjectional". I searched it, plus main.tex, notes/*.md, DECISIONS.md and STATUS.md, for "ordering", "less to more", "more interjectional", "single scale", "one scale", "single ordering", "continuum" and "cline". None matched. The closest passages are ll. 806–811 ("The number and rank of categories are outcomes of comparison") and ll. 1487–1489, where form alone "doesn't establish what it licenses". Neither bibliography has an entry for the paper.

**1. The model**
It works at two levels, form first, then structure: "The higher-level problem is to discover the form of the underlying structure" (10687).

- **Forms** (Fig. 2A, 10688): partition, chain, order, ring, hierarchy, tree, grid (chain ∏ chain) and cylinder (chain ∏ ring). Each of the first six comes from a single node-replacement production. Starting from one node, a parent node becomes two children, linked to each other and to the parent's neighbours (10687–10688). "A hierarchy has objects located internally, but a tree may only have objects at its leaves" (10688).
- **Score:** P(S, F|D) ∝ P(D|S)P(S|F)P(F) (Eq. 1, 10688). "P(F) is a uniform distribution over the forms under consideration". The nodes of S are clusters of entities. "P(S|F) ∝ θ^k if S is compatible with F, and P(S|F) = 0 otherwise" (10688), with θ fixed. The normalizer "ensures that simpler forms are preferred whenever possible" (10689), so "the grid form will only be chosen if the best grid is substantially better than the best chain" (10690).
- **Likelihood:** "P(D|S) will be high if the features in D vary smoothly over the graph S, that is, if entities nearby in S tend to have similar feature values"; "Even though Fig. 1 shows binary features, we treat all features as continuous features and capture the expectation of smoothness by assuming that these features are independently generated from a multivariate Gaussian distribution with a dimension for each node in graph S" (10690). The covariance is defined only in the SI appendix, which isn't held. A greedy search for each form returns the single best (S, F), not a posterior (10690).
- **Similarity data** are read as covariance. The likelihood needs "only two components that depend on D: the number of features observed and the covariance of the data" (10690).
- **Results:**
  - Synthetic data: the true form was recovered (10690).
  - Feature data: animals, 33 × 106, gave a tree; Supreme Court votes, 13 judges × 1,596 cases, gave a chain (10690).
  - Similarity data: 14 hues gave a ring; faces gave a grid (the main text gives no N); 35 cities gave a cylinder (10690).
  - Relational data: mangabeys gave an order; 13 Bush officials a hierarchy; prisoners a partition; 20 New Guinea communities the Kula ring (10691).
  - Fig. 5: "After observing only five features of each animal species, the model chooses a partition". By 20 features it chooses a tree (10690).

**2. Bearing on the paper**
It bears on the paper less than the brief suggests. K&T formalize the comparison at l. 811, and that's worth adopting. But they claim "Identifying the best form for a domain provides powerful constraints on inductive inference" (10691), while ll. 1487–1489 deny that form alone settles warrant. That difference should be logged as deliberately distinguished.

Limits:
- **One structure for all features.** Eq. 1 has a single S, so a fit to the whole matrix assumes what the paper denies. My inference: if INTJ's 6 diagnostics vary smoothly over one partition and EXPRESSIVE's 4 over another, the fit would follow the larger set and treat the other as noise.
- **Crosscutting can't be expressed.** Again my inference, from Fig. 2: ∏ is a graph product. Two partitions have no edges, so their product has none either and amounts to one four-cluster partition with no shared parameters. A 2 × 2 grid would share parameters, but only by making members and non-members neighbours expected to be alike. K&T concede that their inventory "does not exhaust the set of cognitively natural or scientifically important forms" (10691).
- **A chain is not graded membership.** It's an ordering of discrete clusters, each item assigned to one cluster. So "partition versus chain" isn't "categories versus gradient", and the model says nothing about graded epistemic access.

The legitimate use is to compare partition, chain and tree within one classification's diagnostics.

Suggested text after l. 811 (needs a new references-local.bib entry):
> \textcite{KEY} make this choice a matter of model comparison, scoring partitions, chains, trees and other forms by how smoothly the properties vary over each, with a penalty on the number of clusters. Their model fits one structure to every property in a dataset, so it can compare forms within one classification but can't represent several classifications of the same items.

**3. Bearing on the study**
The matrix in /Users/brettreynolds/projects/LLM-CLI-projects/papers/queue/english-interjections/analysis/matrix-lesion/FREEZE-v4.md is 46 × 14. Twelve properties are coded Y/N/U, P10 has 4 values and P14 has 8. The diagnostic sets are INTJ 6 and EXPRESSIVE 4.

- **Size:** a partition already wins at 5 features in Fig. 5. With 4–6 features, a partition result is close to the default and is weak evidence. Only a chain or tree win would tell you anything.
- **Missing cells:** the main text doesn't mention them. A Gaussian model could in principle integrate them out (my point; I can't confirm their implementation does). U must be treated as missing, not 0. K&T have nothing like N versus U ("Silence is U", FREEZE §6), testimony-unit weights or absence strength.
- **Other fit problems:** binary cells become Gaussian values, and P10 and P14 would need one-hot coding. The lesion firewall would need a refit on source columns only for each concealment. Because each row gets a single best assignment, there's nothing comparable to M2's membership posteriors.
- **Possible gain:** FREEZE says the latent-class model can't tell "genuine intermediacy or thin evidence" apart (ll. 306–308). A three-cluster chain makes the middle cluster resemble both ends. Comparing it with the three-class sensitivity run would test whether intermediates are real.
- **Prerequisite:** a fake-data recovery check at 46 × 6 using the yield audit's pattern of known cells, like K&T's synthetic test (10690). I expect it to fail at this size. The Round 7 two-feature model (ll. 313–323) fits the paper's thesis better than any K&T form.

**4. Conflicts with Brett's commitments**
- **Converging fallible diagnostics:** compatible, since no feature defines the structure, though all features are weighted alike.
- **Absences count:** 0 and 1 enter symmetrically, so it's compatible as long as U isn't coded 0.
- **Anchoring:** no counterpart. Anchoring could only be imposed by choosing which columns go in, and the model can't tell an anchor from another property in the cluster.
- **Plural crosscutting categories:** a direct conflict with the one-structure assumption. Cite K&T as the single-structure alternative the paper declines, not as support.
