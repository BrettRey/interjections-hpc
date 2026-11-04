from pathlib import Path
p=Path('inquiry-relative-evidence-supplement.tex');s=p.read_text()
def replace(a,b):
 global s
 if a not in s: raise ValueError(a[:100])
 s=s.replace(a,b,1)
replace('Neither measure identifies the three worked sign-type classifications independently.', 'Neither measure independently identifies the grammatical, expressive, depictive, or interactional groupings discussed in the main paper.')
replace('The tagger\'s training on inner-circle English limits its treatment of regional forms, but recognized items aren\'t necessarily clean.', 'The tagger misses relevant regional uses, and even recognized items can contain false positives.')
start=s.index('Coding tagged concordances across all twenty sections shows the sensitivity.')
end=s.index('Spelling variants introduce another country-dependent error.',start)
s=s[:start]+r'''The fuller twenty-section audit uses a deterministic regular-expression
screen, implemented in \path{analysis/filter-ha-concordance.py}. Its rules
inspect reduplication, laughter words, punctuation, units, numbers, names,
and typography. All twenty rows of \path{data/ha-validity-rates.csv}
reproduce those automated assignments. The precision estimates below are
conditional on that screen; they aren't independently adjudicated
country-wide proportions of genuine interjections.

The screen was checked and tuned against forty previously labelled
Kenyan and Tanzanian examples. The adding commit records changes to
the rules after inspecting errors on those examples. Its 39/40 agreement
concerns the binary interjection decision; exact agreement across the
five labels is 37/40. These are development-set comparisons. They don't
establish held-out accuracy or comparable error rates across all twenty
sections, and the archive doesn't establish the initial labeller's identity.

Under the screen, laughter accounts for 51.5\% of sampled US tagged
\mention{ha} and 63.0\% of sampled British tagged \mention{ha}. Table~\ref{tab:ha-sensitivity}
separates six treatments of laughter and unclear cases
\citep[cf.][]{gelman2014statcrisis}. Here \term{unpooled} means rates adjusted
using each section's screen-derived proportion without shrinkage; it
doesn't mean the original tagged rates. The original uncorrected
coefficient of variation is approximately 0.412.

\begin{table}[htbp]
\centering
\small
\caption{Sensitivity of adjusted \mention{ha} rates to screen-based inclusion rules.
Unclear cases receive weight 0, 0.5, or 1. CV is the standard deviation
divided by the mean of the twenty section rates.}
\label{tab:ha-sensitivity}
\begin{tabular}{@{}llrrrr@{}}
\toprule
 & Unclear & \multicolumn{2}{c}{CV} & \multicolumn{2}{c}{Kenya rank} \\
\cmidrule(lr){3-4}\cmidrule(l){5-6}
Laughter & weight & Unpooled & Pooled & Unpooled & Pooled \\
\midrule
Included & 0   & 0.396 & 0.395 & 15 & 15 \\
Included & 0.5 & 0.420 & 0.419 & 15 & 14 \\
Included & 1   & 0.446 & 0.445 & 15 & 15 \\
Excluded & 0   & 0.793 & 0.778 & 15 & 15 \\
Excluded & 0.5 & 0.810 & 0.796 & 15 & 15 \\
Excluded & 1   & 0.828 & 0.817 & 16 & 16 \\
\bottomrule
\end{tabular}
\end{table}

Kenya falls from fifth in the original tagged rates to fifteenth or
sixteenth across the six unpooled specifications; pooled ranks range
from fourteenth to sixteenth. The downward movement survives these
choices, but its exact rank doesn't. The laughter-inclusive adjusted
CVs also differ from the original uncorrected 0.412.

With laughter included and unclear cases excluded, the screen retains
34.5\% of sampled hits in Bangladesh and 84.0\% in Great Britain.
It identifies \term{hectare} as a major contaminant in East Africa and
South Asia, and names as relevant in Singapore, where it assigns 6.1\%
to \term{hectare}. These percentages describe the screen's output.
Their accuracy as linguistic measurements requires separate validation.

Pooling uses the exported sample sizes: 1,000 US rows and 200 Ghanaian
rows, compared with corpus totals of 8,016 and 420 tagged occurrences.
The twenty exports contain 16,197 rows. Shrinkage changes the proportions
by about 0.6 percentage points at most across the six specifications.
The small change reflects estimated binomial sampling variation under
the pooling model; it doesn't bound classification error or uncertainty
about the representativeness of the exported contexts.

Between-section differences in screen-derived proportions exceed the
binomial variation represented by that calculation. Whether they exceed
all measurement error is unknown. The sensitivity choices also don't
cover every possible screen error, and false-negative retrieval remains
unmeasured. The relevant code and output are
\path{analysis/pool-ha-rates.py} and
\path{analysis/hand-extracted/ha-pooled-multiverse.csv}.

'''+s[end:]
replace('Models m0--m2 use exact reloo for leave-one-out cross-validation; exploratory m3 is assessed through Pareto-smoothed importance sampling (PSIS) diagnostics only.', 'Models m0--m2 request pointwise leave-one-out cross-validation (LOO), with \texttt{reloo} enabling exact refits for problematic observations; this is not a record of 360 exact refits. Exploratory m3 is assessed through Pareto-smoothed importance sampling (PSIS) diagnostics only.'.replace('\texttt','\\texttt'))
# Explicit prediction target, with no refit.
needle='The country intercept in m1 estimates an overall frequency shift across items, not an item-specific country effect.'
replace(needle,r'''The held-out observation is one country--item aggregate from the 18-item
by 20-country design. Its training data retain the same item in nineteen
other countries and seventeen other items in the same country. The target
is an omitted cell within that observed design, with its corpus-size
offset supplied. It isn't an unseen country, an unseen item, a later
period, or a newly categorized sign-type.

'''+needle)
replace('Exact leave-one-out comparisons for the confirmatory models are:', 'The archived pointwise LOO comparisons for models m0--m2 are:')
replace('Adding item type doesn\'t improve the point estimate.', 'Adding item type doesn\'t improve the point estimate for this omitted-cell task. Item intercepts already receive information from the same items elsewhere; the comparison therefore doesn\'t settle whether type helps predict an unfamiliar item.')
replace('not replacement of the exact-reloo results above. Precision correction leaves recall unidentified.', 'not replacement of the pointwise LOO results above. The draws represent binomial uncertainty in screen-derived proportions; they don\'t propagate unknown screen errors or establish sample representativeness. Precision correction leaves recall unidentified.')
replace('not continued \\intj{sem} membership.', 'not continued membership in an expressive category.')
start=s.index('The archive contains a separate recorded recode, internally attributed to')
end=s.index('The recode covers only three',start)
s=s[:start]+r'''The archive contains a separate 97-row recode whose secondary codes and
notes differ from the primary file. I cannot reconstruct who performed
that recode or what information was concealed. The archive's attribution
to a blind human pass by me is therefore unsubstantiated and isn't
retained as a provenance claim. The GPT-Pro-authored source bundle
reports on this older record; authorship of that report doesn't establish
authorship of the underlying coding file.

The recorded judgments remain inspectable, but they supply no verified
independent human validation. Their possible descriptive value depends
on the coding's validity and independence, which the available record
doesn't establish. Undefined $\kappa$ is a separate statistical issue:
it neither validates nor erases the content of those judgments.

'''+s[end:]
replace('This ordered-erosion hypothesis was an additional historical commitment; it doesn\'t follow merely from distinguishing three worked sign-type classifications.', 'This ordered-erosion hypothesis was an additional historical commitment. The archived labels below identify the original syntactic, semantic, and interactional coding dimensions; distinguishing those dimensions doesn\'t entail ordered erosion or one category per field.')
p.write_text(s)
print('Corrected measurement, CVs, sample denominators, ranks, prediction target, and provenance wording.')
