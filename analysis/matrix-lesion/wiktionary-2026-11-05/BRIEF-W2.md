Thank you for taking this on. This is a short supplementary pass. A first pass over English Wiktionary for the bearers of an interjections study has been done, but its text file had lost template content: IPA, the source forms in etymologies, example sentences, quotations, and a few glosses. That was an extractor fault, now fixed. Your job is to extract only what the first pass couldn't read, for half the bearers. Another agent has the other half.

FILES (read-only):
- The rebuilt text: /Users/brettreynolds/projects/LLM-CLI-projects/papers/queue/english-interjections/analysis/matrix-lesion/wiktionary-2026-11-05/wiktionary-senses-v2.txt. Blocks start "=== W:<page>:E<k>:<section>:<n> ===". E<k> is the etymology number, so ids are unique. Blocks are senses (with QUOTATION and EXAMPLE lines), HEADWORD lines, and Pronunciation, Etymology and Usage notes sections.
- The first pass's reports, for which senses match each bearer (section 2 of each) and what was already extracted: REPORT-v1-interjection-rows.md and REPORT-v1-expressive-control-rows.md in the same folder. Don't repeat rows they already give.
- The bearers: /Users/brettreynolds/projects/LLM-CLI-projects/papers/queue/english-interjections/analysis/matrix-lesion/items-v4.csv (use_gloss is the use).
- The properties: /Users/brettreynolds/projects/LLM-CLI-projects/papers/queue/english-interjections/analysis/matrix-lesion/properties-v4.csv; use the rows of type "possibility". Y needs one admissible instance; N means never and needs an explicit statement. Silence is never N.

EXTRACT, for each of your bearers, only:
1. **P13 from the IPA**: say whether any transcription given for the bearer's page includes sounds outside ordinary English word phonology (a click, a syllabic fricative, a vowelless form, a nasal-only form, a non-English segment). Quote the transcription.
2. **NEW:HISTORICAL_SOURCE**: what the Etymology block says the form or use derives from, with the source form now readable. If the page has several etymologies, use the one governing the matched sense (E<k> in the id).
3. **Rows from EXAMPLE and QUOTATION lines** of the matched senses: an example showing the use in a position or construction (P01, P02, P03, P04, P05, P06, P12S/P12I if prosody is described) gives one admissible instance for Y. Note the quotation's year and source as given.
4. **Glosses the first pass found stripped** (for example sh, mm-hm, okay, the hell's Interjection and Pronoun senses, hell Noun "Used as an…", fucking Adjective 2, quickly Adverb 1): read them now and extract as in the first pass (P08, P07D, NEW: form properties).

RULES
- Match the use, as the first pass did; if you disagree with its match, say so in a note.
- Register and variety labels go in the note, never as values.
- Quote exactly from wiktionary-senses-v2.txt, at most 40 words per quotation, with the block id. Every quotation will be string-checked against that file.

RETURN (in your final message; don't write files)
1. A table: item_id | property | value (Y/N) | scope (item/page) | "quotation" | block id | note.
2. One line per bearer: what you added, or "nothing new".
3. Anything still unreadable.

STOPPING RULE
Use Grep to find your pages' blocks, read only the matched senses plus Pronunciation and Etymology, extract, report and stop. Aim for about 20 tool calls; if you run long, deliver what you have and list what you didn't reach.
