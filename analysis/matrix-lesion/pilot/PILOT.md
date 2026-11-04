# P02 pilot report

Date: 2026-11-03

Status: feasibility pilot only. These 40 pilot cells are not study data and must not be reused in the full matrix.

## Design run

- Property: P02 SUPPLEMENT.
- Items: OUCH, WOW, GEE, DAMN_PRENOM, BANG_DEPICT, MMHM, BLOODY_PRENOM, COFFEE, STOP, BLACK.
- Packets: form-based scripted excerpts from Ameka (1992), Wilkins (1992), Dingemanse (2023, 2024), Heine (2023), Stange (2016), Libert (2019), Norrick (2009), Gehweiler (2008), CGEL, and Quirk et al. (1985). Packet sizes were 1,440 to 6,947 characters, except that most items received roughly 5.7 to 6.9k characters.
- Independent coder families: Agy, Copilot, and local Qwen3.8-27b. A fresh-context Muse subagent also coded the column, and is reported separately because Muse is the orchestrating family and is not an independent model family.
- Claude and Codex routes were unavailable and were not used.

## Route and completion results

All four routes eventually returned ten parseable cells.

| Coder | Working call pattern | Time | Y | N | U | Quote result |
|---|---|---:|---:|---:|---:|---|
| Agy | 10 per-item print-mode calls, tools explicitly disabled in prompt | 568.2 s | 3 | 0 | 7 | 3/3 verified |
| Copilot | 1 column-wide prompt | 31.9 s harness time; 5.46 AI credits; 35.2k input and 2.1k output tokens | 1 | 0 | 9 | 1/1 verified |
| Qwen3.8-27b | 10 per-item Ollama API calls, temperature 0, JSON mode, 16,384 context | 360.8 s | 0 | 0 | 10 | no quoted cells |
| Muse (non-independent) | 1 fresh-context subagent call | not instrumented | 3 | 0 | 7 | 3/3 verified |

Route defects and fixes encountered during the pilot:

1. Agy's first column-wide call returned empty stdout after 45.9 s. Per-item calls with an explicit no-tools instruction worked, but cost about 57 s per item.
2. The initial analysis script failed to load the Muse output because its family label was spelled “Muse” rather than “Muse”. This was an orchestration bug, not a coder failure.
3. Agy and Copilot did not return model identifiers in the JSON output. A full run must log the CLI version and configured model separately for every call.

## Values and agreement

| Item | Agy | Copilot | Qwen | Muse (reported separately) | Independent consensus |
|---|---|---|---|---|---|
| OUCH | Y | U | U | Y | U |
| WOW | Y | U | U | Y | U |
| GEE | Y | Y | U | Y | Y |
| DAMN_PRENOM | U | U | U | U | U |
| BANG_DEPICT | U | U | U | U | U |
| MMHM | U | U | U | U | U |
| BLOODY_PRENOM | U | U | U | U | U |
| COFFEE | U | U | U | U | U |
| STOP | U | U | U | U | U |
| BLACK | U | U | U | U | U |

- No coder returned an N.
- Unknown rates were 70% for Agy, 90% for Copilot, 100% for Qwen, and 70% for Muse.
- Raw pairwise agreement among the independent families was 8/10 (Agy-Copilot), 7/10 (Agy-Qwen), and 9/10 (Copilot-Qwen).
- Fleiss's kappa for Agy, Copilot, and Qwen was 0.135. The low kappa coexists with high raw agreement because U dominates the marginal distribution and the few informative disagreements concern whether indirect class-level evidence is enough for Y.
- Only GEE reached the drafted independent consensus rule. The consensus column is therefore 90% unknown.
- All seven Y quotes were verified verbatim, after whitespace normalization, in both the item packet and the cited source markdown. There were no fabricated quotes, missing quotes on Y cells, or U cells carrying a quote.

## What the disagreements actually show

The disagreements are systematic rather than random. Every Y comes from one Ameka passage saying that primary interjections, with “Ouch!, Wow!, Gee!, Oho!, Oops!, etc.” as examples, “could be used as co-utterances with other units”, followed by the example “Gee. you look like you had it!” Agy and Muse treated that class-level co-utterance statement as sufficient for OUCH, WOW, and GEE. Copilot required the item-specific GEE example. Qwen did not accept the passage as sufficient.

A first version of this report called that a problem of matching Ameka to a supposed technical definition of supplement function. Brett's correction (2026-11-03) rejects that framing: there is no technical definition against which source descriptions are to be measured. The pilot prompt itself invited the error by specifying supplement “in the CGEL sense”. Read in context, Ameka's loose phrasing is nevertheless plainly distributional and syntactic. He says the items can constitute utterances “in terms of their distribution”, do not normally “enter into construction with other word classes”, and can serve as co-utterances; the following *Oh, I have another suit* / *Oh!* comparison concerns the same structural territory. That is quite close to what CGEL treats as supplement function, without either description needing to define or authorize the other. Agy's and Muse's Y codings are therefore well supported on Brett's reading. Copilot's insistence on an item-specific example and Qwen's non-acceptance reflect the prompt's framework-bound wording more than a deficiency in Ameka's evidence. The consensus U outcomes for OUCH and WOW should be read as artifacts of those thresholds, not as evidence against the property.

## Packet diagnosis

Packet construction is the binding constraint, not model willingness:

- No pilot packet contains the word “supplement”. That fact alone is not a defect: evidence need not arrive under CGEL's label. The real retrieval defect is variability in whether packets contain relevant distributional descriptions or examples at all. Ameka's co-utterance passage was present and relevant for OUCH, WOW, and GEE, while several other packets offered no usable evidence about how the sign combines, or does not combine, with other units.
- Whole-grammar sources contributed little relevant distributional evidence under the current “form near generic distribution vocabulary” query. Retrieval should target descriptions and examples of standalone use, clause-adjacent or co-utterance use, integration, dependents, and construction with other expressions, whatever terminology a source uses.
- COFFEE received only one irrelevant excerpt. STOP and several other packets contain topically adjacent but non-probative passages.
- Overlapping windows duplicated substantially the same Ameka passage for GEE and across OUCH/WOW/GEE, spending the character cap on repeated text.
- No packet produced evidence meeting the drafted negative standard. That explains the complete absence of N values. Silence in these packets is primarily retrieval failure, not evidence that the property is unknowable from the literature.

## Stop-rule assessment

The drafted pilot rules are triggered:

- Fleiss's kappa of 0.135 is below the 0.40 threshold for revising operational definitions and re-piloting once.
- The unknown rate is far above the 60% packet-revision threshold, whichever denominator is used.
- No coder is suspended for quote fabrication, because no fabricated or materially misattributed quote was found.

Kappa alone understates the raw agreement in this highly imbalanced column, but the substantive threshold disagreement and the 90% consensus-unknown result independently justify stopping before a full run.

## Recommended revisions before any re-pilot

1. Recast P02 so coders extract source-supported distributional behaviour rather than test sources against a supposed definition of supplement. Relevant observations include a described or exemplified contrast among standing alone, occurring with another complete unit without entering its construction, and occurring as an integrated constituent. Preserve the source's own wording (for example, Ameka's *co-utterances*) in the coding record, and distinguish item-specific examples from generalizations over a class that explicitly includes the item. Any mapping from those observations to the analyst's P02 column must be explicit and revisable.
2. Build packet v2 around distributional behaviour as well as forms, without requiring the word “supplement”. Retrieve passages in which sources describe occurrence alone, occurrence with other units, entry into constructions, integration, and dependents, including CGEL's relevant sections. Deduplicate overlapping windows and preserve stable publication pages where available rather than relying only on markdown line numbers.
3. Split packets into item-specific evidence and explicitly labelled class-level evidence. This makes the current disagreement codable and auditable instead of leaving each model to invent its own bridge.
4. Record provider, configured model, CLI version, timing, and token or credit use for every call. Decide in advance whether Agy remains viable at roughly 57 seconds per item if column-wide calls cannot be made reliable.
5. Re-pilot the revised P02 once. If it remains overwhelmingly unknown, run the drafted second feasibility column, P05 INFLECTS, before deciding whether a literature-only matrix can pass the fill gate.

Bottom line: the multi-model route is operationally feasible and quotation discipline was excellent, but the framework-bound P02 prompt and form-first packet builder do not yet produce a dependable evidence base. The pilot succeeds by showing that before 490 cells are commissioned.
