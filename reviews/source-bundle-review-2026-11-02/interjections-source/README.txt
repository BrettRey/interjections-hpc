BUILD NOTES — REVISED INTERJECTIONS MANUSCRIPT

This source package contains the revised manuscript, the exact cited subset of
the recovered bibliographies, four original figure PDFs, the author's house
preamble with two documented portability changes, and langsci-gb4e.sty.

Build from the directory containing interjections-revised.tex:

  xelatex -interaction=nonstopmode -halt-on-error interjections-revised.tex
  biber interjections-revised
  xelatex -interaction=nonstopmode -halt-on-error interjections-revised.tex
  xelatex -interaction=nonstopmode -halt-on-error interjections-revised.tex

The delivered proof was built with XeLaTeX (TeX Live 2023/Debian) and Biber 2.19.
Do not use pdfLaTeX: the house preamble uses fontspec. The source uses \today;
the delivered proof is dated 2 November 2026. Its build used TZ=America/Toronto.
Subsequent builds will ordinarily show their own compilation date.

FONTS AND PACKAGES

The rendered manuscript uses the author's EB Garamond main font, Charis SIL
for IPA, and Inconsolata for monospaced text. These fonts must be installed.
The build uses biblatex with Biber, including the APA bibliography style.
Normal TeX Live packages are required, including TikZ, ulem, xurl, microtype,
fancyhdr, fontspec, and the other packages named in the preamble.

For this Debian environment the additional packages installed were:
texlive-bibtex-extra, texlive-humanities, texlive-plain-generic, biber,
fonts-ebgaramond, fonts-sil-charis, and fonts-inconsolata.
This list supplements the existing TeX installation; it is not a standalone
minimal package list for all operating systems.

PORTABLE PREAMBLE

The manuscript source itself is unchanged between the supplied source and the
compiled proof. Two adjustments are confined to .house-style/preamble.tex:

1. The unavailable Hiragino Mincho ProN CJK fallback is replaced by DejaVu Sans.
   The manuscript never invokes the \cjk macro, so this affects no rendered
   manuscript text. DejaVu Sans is not presented as a general-purpose CJK font.
2. xurl is loaded after hyperref to allow long repository filenames to wrap.
   This removes two otherwise overfull lines in the Appendix B file inventory.

Original-preamble compilation stopped on the absent Hiragino font. No main-font,
IPA-font, bibliography-processor, or example-numbering substitutions were made.

BIBLIOGRAPHY

references-standalone.bib contains 68 exact records recovered from the author's
central bibliography and the verified supplementary records. The records were
extracted without inventing bibliographic content. Existing ids aliases are
retained. All 68 citekeys used by the revised manuscript resolve. The preamble
automatically prefers this standalone bibliography when it is present.

FIGURE AND STYLE PROVENANCE

The four figure files are original assets retrieved from BrettRey/interjections-hpc
at commit 074dfb44cef5b18d292ac176ba5acbfedc76e3b1. Their Git blob hashes were
verified against the retrieved bytes:

country-variation.pdf        28e4f9f7c95e8b1fec1871a6f4061b7628307bb1
fie-raw-proportions.pdf      683c683b5e70773e78030aca3e55c59db3e23b8b
fie-tau-posteriors.pdf       579be424d3ac6df78bad962a0fa0af57a183c32f
interjection-turnover.pdf   4d435529761ce5e7748f7ca8b689b875fee525b7

langsci-gb4e.sty was recovered from the official langsci/langscibook repository:
https://github.com/langsci/langscibook/blob/master/langsci-gb4e.sty
Git blob hash: eec32c548947d8b40a0d385a3f176db564936eb0
Its original license and copyright notices are retained inside the file.

VALIDATION AND REMAINING NONFATAL WARNINGS

The proof was compiled successfully with no LaTeX errors, missing glyphs,
overfull boxes, undefined citations or references, duplicate labels, or Biber
warnings. All pages were rendered and visually reviewed in contact sheets;
tables, figures, title page, bibliography, and affected appendix layouts were
also reviewed at readable size. These are typesetting and internal-reference
checks, not a claim that every quotation or empirical assertion has been
independently verified.

The inherited preamble emits two fancyhdr notices because even-page header and
footer options are unused in one-sided mode, one microtype footnote-patch notice,
and 402 microtype notices about unknown font protrusion slots. These notices do
not report missing printed glyphs; no visible rendering defect was found.

The two fie plots are intentionally retained as archived outputs of an analysis
whose measurement audit failed. Their revised captions and Appendix C explain
that they provide no valid test of linguistic property loss or its ordering.
Their inclusion should not be read as reinstating the withdrawn inference.
