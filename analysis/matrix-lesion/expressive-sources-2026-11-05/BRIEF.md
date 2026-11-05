Thank you for taking this on. Brett Reynolds, a linguist, is deciding which properties to add to a study of English interjections and expressives. The study's EXPRESSIVE grouping has too few diagnostics, and all of them are meaning properties. He wants to know, source by source, which properties the expressive literature states for which particular bearers. Your job is one source. Three other agents are doing the other sources.

FILES (read-only):
- The source, as page-marked text: the file named in your task. Each page starts with a line "=== PDF page N ===". Convert to printed page numbers with the offset given in your task, and check it against the running heads.
- The bearers: /Users/brettreynolds/projects/LLM-CLI-projects/papers/queue/english-interjections/analysis/matrix-lesion/items-v4.csv (item_id, form, use_gloss: each row is one conventional use, e.g. DAMN_DEGREE is the degree use, DAMN_PRENOM the prenominal attributive use, DAMN_REACT the standalone reaction).
- The current properties: /Users/brettreynolds/projects/LLM-CLI-projects/papers/queue/english-interjections/analysis/matrix-lesion/properties-v4.csv (P01 to P14, with what counts as Y and as N).

WHAT TO EXTRACT
Every statement or example in the source that says a particular bearer (one of the 46 uses) has or lacks a property. Properties are:
(a) the P01 to P13 schema properties, judged by their positive and negative standards in properties-v4.csv;
(b) Potts's six properties of expressives: independence, nondisplaceability, perspective dependence, descriptive ineffability, immediacy, repeatability;
(c) any other property the source uses to characterize or distinguish expressive items, especially form properties (position, which words it can modify, predicative use, infixation, gradability, co-occurrence, prosody). Give each one a short NEW:NAME and say what the source treats as having it.

RULES
- Silence is not N. Record N only where the source states the bearer lacks the property, or marks an example with the bearer unacceptable.
- Match the use. If the source's example of *damn* is the prenominal use, it bears on DAMN_PRENOM, not DAMN_DEGREE. If you can't tell which use, say so in the note.
- Distinguish scope. "item" means the source states it of that bearer or gives an example with that bearer. "class" means the source states it of a class ("expressives", "slot fillers", "epithets"). For a class statement, write ONE row with item_id = CLASS:<the class's name>, and list in the note the bearers the source names as members. Don't copy a class statement onto each member.
- Quote exactly, at most 40 words per quotation, with the printed page. The parent will string-check every quotation against the text, so don't tidy or paraphrase inside quotation marks.
- Bearers not in the 46 (e.g. *shit*, *goddamn*, Japanese items) can be noted briefly at the end if the source uses them to establish a property, but don't extract them row by row.

RETURN (in your final message; don't write files)
1. A table, one row per statement: item_id | property | value (Y/N) | scope (item/class) | "quotation" | printed page | note.
2. The NEW: properties you introduced, each with a one-line definition from the source and the page.
3. Anything in the source that warns against using a property as a diagnostic, with page.
4. What you did not read, if anything.

STOPPING RULE
Read the sections named in your task, plus anything else in the source that names one of the 46 bearers (search for their forms). Then report and stop. If the source says little about these bearers, a short table is a successful result; say so. If a page is unreadable, note it and carry on. Don't search the web or read other files.
