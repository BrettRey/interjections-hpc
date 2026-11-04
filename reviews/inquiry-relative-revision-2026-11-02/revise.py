from pathlib import Path
p=Path('reviews/inquiry-relative-revision-2026-11-02')
s=(p/'before/inquiry-relative-categories.tex').read_text()
head=s[:s.index('\\begin{abstract}')]
# Local bibliographic correction, scoped to the two working documents.
doi=r'''% Publisher-verified correction without changing the shared bibliography.
\DeclareSourcemap{
  \maps[datatype=bibtex]{
    \map[overwrite=true]{
      \step[fieldsource=entrykey, match=\regexp{\Aunuabonahdaniel2020\Z}, final]
      \step[fieldset=doi, fieldvalue={10.1016/j.pragma.2020.04.004}]
    }
  }
}
'''
head=head.replace('\\newif\\ifblind',doi+'\n\\newif\\ifblind')
# Keep the archival diagnostic macros only in the supplement.
mainhead=head.replace('\\newcommand{\\intj}[1]{\\textsc{interjection\\textsubscript{#1}}}\n','').replace('\\newcommand{\\intjshort}[1]{Intj\\textsubscript{#1}}\n','')
middle=s[s.index('\\section{Phonological organization'):s.index('\\section{What the corpus evidence bears on}')]
middle=middle.replace(r'\intj{syn}', 'grammatical interjections').replace(r'\intj{sem}', 'expressive signs').replace(r'\intj{prag}', 'interactional resources').replace(r'\intj{phon}',r'\term{phonological interjection}').replace(r'\intj{x}',r'\term{interjection}')
middle=middle.replace('cross the three classifications developed earlier','cross the grammatical, semantic, and interactional groupings developed earlier')
middle=middle.replace('including the relations among different bearers.','including the relations among different bearers.')
start=middle.index('\\textcite[112--113]{ameka1992}')
end=middle.index('An account of the stratum',start)
middle=middle[:start]+r'''\textcite[112--113]{ameka1992} diagnoses a specific inference: unusual
phonology shared with interjections has been used to include onomatopoeic
words in the grammatical interjection category. His alternative is to
recognize a phonological grouping whose members can belong to different
grammatical categories. The following assessment develops the evidential
consequence of that distinction.

The grammatical claim concerns membership in a lexical category. The
evidence offered concerns sounds or sound patterns unusual elsewhere in
the language. That evidence supports a comparison of phonological
possibilities across independently identified signs. It doesn't answer
whether a particular use has nominal, verbal, or interjectional grammar.
Nor does sound depiction itself entail phonological anomaly: resemblance
and distribution within the sound system are different relations.

For English \mention{Bang!}, the competing grammatical analysis is a
standalone nominal fragment, supported as a possibility by the independently
available noun in \mention{a loud bang}. A depictive interpretation leaves
that analysis open. Even if an occurrence had unusual phonation, the
additional observation would concern its realization. Choosing between
nominal and interjectional analyses would still require distributional
and constructional evidence about the selected conventional use.

The strongest alternative retains one broad descriptive class and records
phonology and grammar as separate attributes. For organizing known cases,
that can preserve the same information. It becomes inadequate only if
membership in the broad class is used to infer a grammatical assignment
without the relevant evidence. The completed assessment therefore rejects
that inference while retaining the cross-grammatical phonological
comparison. It doesn't establish a single projectible phonological stratum.

'''+middle[end:]
middle=middle.replace('a classification based on independently\nestablished segmental possibilities','a class based on independently\nestablished segmental possibilities')
middle=middle.replace('and\nenter membership intersections.','and\nenter membership intersections.')
# Historical evidence remains a case explanation, not a category-level success.
needle='route predictable.\n'
middle=middle.replace(needle,needle+r'''
This is an explanation of a particular outcome. It doesn't yet establish
that a class of signs with religious ancestry outperforms alternatives
or supports a common projection. That comparison would require independently
documented histories and outcomes across more than this one route.

Hill's considerations clarify a tempting stronger claim. If newly acquired
prosodic isolation were proposed as a cause of the semantic change, the
already peripheral invocation would fail to supply the required change
in exposure. The cited history doesn't independently measure a prosodic
innovation preceding the semantic transition. Plausibility of a
prosody--syntax connection cannot supply that missing temporal comparison.
Gehweiler's proposed roles for invited inference and taboo-motivated
clipping remain distinct historical claims with their own evidence.
''')
middle=middle.replace('Historical classification has two kinds of payoff. It can','Historical classes can have two kinds of payoff. They can')
middle=middle.replace('and it can compare processes across developments. These are legitimate','and they can compare processes across developments. These are legitimate')
middle=middle.replace('contributions without a universal demand for an additional predictive\neffect. Where a historical category is advertised as projective,\nits claimed expectations require evidence beyond the histories used\nto construct it.', 'descriptive and explanatory contributions. An empirical ancestry category,\nin the stronger usage adopted here, additionally needs support for the\ninductions it licenses. The documented history of one sign cannot supply\nthat support for an entire source class.')
middle=middle.replace('Their categories\ncan\'t be intersected directly', 'Their classes\ncan\'t be intersected directly')
middle=middle.replace('An open family of classifications needn\'t become an\never-expanding list of technical senses of \\term{interjection}.', 'Several classes can serve one inquiry, and one supported category can\nserve several inquiries. Neither relation requires additional technical\nsenses of \\term{interjection}.')
Path('inquiry-relative-categories.tex').write_text(mainhead+(p/'parts/opening.tex').read_text()+(p/'parts/assessment.tex').read_text()+middle+(p/'parts/ending.tex').read_text())
# Preserve appendix content verbatim initially; corrections follow in a separate script.
appendix=s[s.index('\\appendix'):s.index('\\end{document}')]
turnover=s[s.index('The COHA inventory illustrates'):s.index('\\subsection{Withdrawn confirmatory interpretations}')]
turnover=turnover.replace('The COHA inventory illustrates a different descriptive result','The Corpus of Historical American English (COHA) inventory supplies a descriptive result')
supphead=head.replace('Inquiry-Relative Categories: English Interjections as a Worked Case','Inquiry-Relative Categories: Evidence Supplement').replace('\\title{Inquiry-Relative Categories:\\\\English Interjections as a Worked Case}','\\title{Inquiry-Relative Categories:\\\\Evidence Supplement}')
intro=r'''
This supplement preserves the measurement records accompanying
\href{inquiry-relative-categories.pdf}{Inquiry-Relative Categories: English
Interjections as a Worked Case}. It distinguishes retained descriptions
from invalid confirmatory interpretations. No new corpus coding or model
fit is reported. The older diagnostic labels in Section~C are retained
to identify archived outputs; they don't allocate one category to each
field in the main paper.

Sections~A--C document the GloWbE, derivative, and \mention{fie} analyses.
Section~D preserves the COHA inventory comparison. Numerical outputs from
invalid analyses remain solely as records of what the pipelines produced.
The audit is tied to repository revision
\texttt{074dfb44cef5b18d292ac176ba5acbfedc76e3b1}.

'''
supp= supphead+intro+appendix+'\n\\clearpage\n\\section{Turnover in the tagged COHA inventory}\n\\label{app:turnover}\n\n'+turnover+'\n\\clearpage\n\\printbibliography\n\\end{document}\n'
supp=supp.replace('\\section[Supplementary materials]{Supplementary materials: GloWbE conditioning analysis}', '\\section[GloWbE measurement and models]{GloWbE measurement and model comparisons}')
supp=supp.replace('Supplementary materials: audit of the semantic-residue analysis in COHA','Audit of the semantic-residue analysis in COHA').replace('Supplementary materials: audit of the \\mentionhead{fie} analysis in COHA','Audit of the \\mentionhead{fie} analysis in COHA')
Path('inquiry-relative-evidence-supplement.tex').write_text(supp)
bib=Path('inquiry-relative-categories.bib')
bibtext=(p/'before/inquiry-relative-categories.bib').read_text()
bibtext+='\n'+(p/'source-check/candidate-references.bib').read_text()
bibtext+=r'''
% Issue year verified against the publisher; first online publication was 2015.
@article{wharton2016expressives,
  author = {Wharton, Tim},
  title = {That bloody so-and-so has retired: Expressives revisited},
  date = {2016},
  journaltitle = {Lingua},
  volume = {175--176},
  pages = {20--35},
  doi = {10.1016/j.lingua.2015.08.004}
}
'''
bib.write_text(bibtext)
print('Assembled revised main document and separate evidence supplement.')
