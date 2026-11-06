Thank you for taking this on. Brett Reynolds, a linguist, is looking for form properties (distribution, position, morphology, prosody) that would help identify an EXPRESSIVE grouping of English uses. Four expressive sources and Wiktionary supply almost only meaning properties. The one form property found so far that recurs across expressive forms is insertion inside a word or phrase: the OED gives it for damn, bloody and fucking. Your job is one reference grammar: extract what it states about the bearers' form, so that each candidate property can be checked against rows of every kind, not only against same-slot controls.

FILES (read-only):
- Your grammar, as page-marked text (the file named in your task). Each page starts "=== PDF page N ===". Use the page conversion given in your task, and check it against the running heads.
- The bearers: /Users/brettreynolds/projects/LLM-CLI-projects/papers/queue/english-interjections/analysis/matrix-lesion/items-v4.csv (item_id, form, use_gloss). Each row is one conventional use: DAMN_DEGREE is the degree use, DAMN_PRENOM the prenominal attributive use, DAMN_REACT the standalone reaction, and so on.
- The properties: /Users/brettreynolds/projects/LLM-CLI-projects/papers/queue/english-interjections/analysis/matrix-lesion/properties-v4.csv. Use the rows of type "possibility". Y needs one admissible instance; N means never and needs an explicit statement or a starred example. Silence is never N.

WHAT TO EXTRACT
1. Statements or examples about particular bearers: the expressive uses (DAMN_*, BLOODY_*, FUCKING_PRENOM, BASTARD_SUPP, YOU_BASTARD, THE_HELL_WH), the interjections (AH, OH, OUCH, WOW, SH, TUTTUT, GEE, HEY, YES, NO and the rest), and the controls (VERY_INTENS, EXACTLY_WH, MAIN_PRENOM, PROBABLE_PRENOM, QUICKLY, BLACK, COFFEE, STOP).
2. Form properties the grammar states for a class the bearers belong to: expletives, intensifying or emphasizing adjectives, attributive-only adjectives, degree adverbs, interjections, epithets, wh-intensifiers such as on earth and the hell, tmesis or infixation. Record these once as CLASS rows, naming the members the grammar lists. Pay special attention to properties that would hold of several expressive uses and fail for the other rows:
   - attributive only (no predicative use);
   - no comparison or grading;
   - no modification;
   - insertion inside words or phrases;
   - occurrence after wh-words;
   - restriction to particular hosts;
   - stress or intonation;
   - position at clause edges.
3. Meaning properties only where the grammar ties them to a form property.

RULES
- Match the use: prenominal damn is DAMN_PRENOM, not DAMN_DEGREE. If you can't tell which use, say so.
- Quote exactly, at most 40 words per quotation, with the printed page (and section number for Quirk). The parent will string-check every quotation against your file, so don't tidy or paraphrase inside quotation marks.
- Starred, question-marked or # examples count as N for the construction shown. Give the example exactly.

RETURN (in your final message; don't write files)
1. A table: item_id (or CLASS:<name>) | property | value (Y/N) | scope (item/class) | "quotation" | printed page | note.
2. The form properties the grammar gives that hold of two or more expressive uses. For each: which bearers it holds of, and whether the grammar says anything about it for the interjections and controls.
3. Anything that warns against using a property as a diagnostic.
4. What you searched for and didn't find (the search strings), and the sections you didn't reach.

STOPPING RULE
Search your file for the bearers' forms and the class terms above, read those passages, extract, report and stop. Aim for about 25 tool calls. If you run long, deliver what you have, with what you didn't reach. A short table is a successful result.
