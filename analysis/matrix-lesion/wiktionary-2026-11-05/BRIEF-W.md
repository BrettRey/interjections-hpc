Thank you for taking this on. Brett Reynolds, a linguist, is deciding which properties to add to a study of English interjections and expressives. Its EXPRESSIVE grouping has too few diagnostics, all of them meaning properties. Four linguistics sources have already been extracted. Now he wants to see what English Wiktionary records for each bearer, in one vocabulary that applies to every bearer alike, controls included. Your job is one half of the bearers; another agent has the other half.

FILES (read-only):
- The Wiktionary text: /Users/brettreynolds/projects/LLM-CLI-projects/papers/queue/english-interjections/analysis/matrix-lesion/wiktionary-2026-11-05/wiktionary-senses.txt. Each block starts with a line "=== W:<page>:<section>:<n> === (revid …; bearers sharing this page: …)". A block is one sense of one part of speech (with its QUOTATION and EXAMPLE lines), or a Pronunciation, Etymology or Usage notes section, or a HEADWORD line. The block id is your locator.
- The bearers: /Users/brettreynolds/projects/LLM-CLI-projects/papers/queue/english-interjections/analysis/matrix-lesion/items-v4.csv. Each row is one conventional use (use_gloss), e.g. DAMN_DEGREE is the degree use (*damn good*), DAMN_PRENOM the prenominal attributive use, DAMN_REACT the standalone reaction.
- The properties: /Users/brettreynolds/projects/LLM-CLI-projects/papers/queue/english-interjections/analysis/matrix-lesion/properties-v4.csv. Use the rows whose type is "possibility" (P07D, P11E, P12S and P12I replace P07, P11N and P12, which are superseded). Every property is a possibility: Y needs one admissible instance (a sense gloss, a label, or a quotation showing the use doing it); N means never, so it needs an explicit statement or label (a headword marked not comparable, a label such as "attributive" meaning attributive only, a sense saying the use cannot do something). Silence is never N.

WHAT TO EXTRACT, for each of your bearers:
1. Which Wiktionary sense(s) correspond to the bearer's use. Give the block id and the part-of-speech heading. If no sense matches, say so; that is a result.
2. Every statement the matched senses (and the page's Pronunciation, Etymology and Usage notes) make about:
   (a) the schema's possibility properties;
   (b) Potts's six properties of expressives (independence, nondisplaceability, perspective dependence, descriptive ineffability, immediacy, repeatability), if a gloss or note states one;
   (c) form properties Wiktionary records: comparability (from the HEADWORD template: `{{en-adj|-}}` or `{{en-adv|-}}` means not comparable; `er` or `more` means comparable), grammatical labels (attributive, predicative, chiefly in the negative, with superlatives, transitive, and so on), infixation, plural or inflected forms. Give each a short NEW:NAME;
   (d) roots: what the Etymology block says the use derives from (for example a source word, a minced oath, a clipping). Record as NEW:HISTORICAL_SOURCE with the source form in the note;
   (e) pronunciation: whether the IPA given includes sounds outside ordinary English word phonology (P13).
3. The part-of-speech heading the matched sense sits under, in the note column only. It is Wiktionary's classification: record it, but never as a property value.

RULES
- Match the use. A headword's comparability applies to every sense under it, so say when the matched sense is not the one that makes the headword comparable (bloody's adjective headword is comparable because of "covered in blood", which says nothing about the intensifier sense).
- Register and variety labels (vulgar, informal, slang, Britain, dated) are a field, not a value: put them in the note.
- Quote exactly from wiktionary-senses.txt, at most 40 words per quotation, and give the block id as the locator. The parent will string-check every quotation, so don't tidy or paraphrase inside quotation marks.
- One row per statement. scope is "item" for a sense matched to the bearer; "page" for a Pronunciation, Etymology or Usage notes statement that covers the whole page.

RETURN (in your final message; don't write files)
1. A table: item_id | property | value (Y/N) | scope (item/page) | "quotation" | block id | note.
2. For each of your bearers, one line: the matched block id(s), or "no matching sense".
3. The NEW: properties you introduced, each with a one-line definition.
4. Anything you could not match or read.

STOPPING RULE
Read the blocks for your bearers' pages (search the file for their forms), extract, report, and stop. Don't read other files or the web. A short table, or "no matching sense" for several bearers, is a successful result.
