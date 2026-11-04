# P02 packet-v2 pilot report

Date: 2026-11-03

Status: feasibility pilot only. These 40 cells are not study data and must not be reused in the full matrix.

## Controlled comparison

Pilot 3 kept the pilot-2 behaviour-based P02 prompt, item set, shuffling seeds, and coder-call patterns. Retrieval changed to packet v2:

- candidate windows were relevance-ranked instead of accepted in source order;
- windows centred on distributional-behaviour expressions as well as the item form;
- overlapping windows were merged;
- bibliography-like passages were penalized;
- selection round-robined across sources;
- item-form passages were separated from class/context passages;
- locations included the nearest markdown section heading as well as the source-file line.

Most packets grew from roughly 5.7 to 6.9k characters in pilots 1 and 2 to roughly 8.4 to 9.8k in pilot 3. COFFEE remained sparse at 3,557 characters from CGEL only. Every packet now contains passages using “supplement”, and OUCH and WOW both receive CGEL's direct class-level statement that central members including them occur “on their own, or as supplements with clausal anchors”.

## Results

| Coder | Pilot 3 | Change from pilot 2 | Time | Main defects |
|---|---|---|---|---|
| Agy | 3Y, 0N, 7U | none | 787.3 s | none detected this run |
| Copilot | 4Y, 0N, 6U | BLOODY_PRENOM and BLACK N→U | 32.6 s; 6.73 AI credits; 43.5k input and 2.6k output tokens | OUCH quote has an ellipsis and is not a continuous verbatim substring |
| Qwen3.8-27b | 3Y, 1N, 6U | BLACK U→N | 624.3 s | GEE quote is 303 characters, three over the limit |
| Muse subagent (non-independent) | 3Y, 0N, 7U | none | not instrumented | none detected |

Independent consensus is unchanged from pilot 2: OUCH, WOW, and GEE are Y; the other seven are U. All four families agree on the three Y items.

Fleiss's kappa for Agy, Copilot, and Qwen is 0.726 in pilot 3, compared with 0.619 in pilot 2 and 0.135 in pilot 1. Independent pairwise agreement is 9/10 for Agy-Copilot, 9/10 for Agy-Qwen, and 8/10 for Copilot-Qwen. The increase is driven by Copilot withdrawing its two pilot-2 N values, partly offset by Qwen introducing an N for BLACK. The same high-prevalence caveat applies: 19 of 30 independent cells (63%) and 7 of 10 consensus cells (70%) remain U.

## Quote verification

Fourteen cells are non-U. Thirteen quotes verify verbatim, after whitespace normalization, in both packet v2 and the cited source markdown.

Copilot's OUCH cell again splices Ameka's sentence with an ellipsis. The component words are real, but a non-continuous quotation violates the output rule and should be rejected automatically in a production run. Qwen's GEE quote verifies exactly but exceeds the 300-character limit by three characters.

No fabricated source or invented quotation was found. The remaining two problematic positive/negative judgments are semantic rather than textual:

- Copilot alone codes MMHM Y from “Continuer between turns during a telling-in-progress”. That is direct evidence of a separate turn in an ongoing telling. Whether it belongs in the intended P02 territory depends on whether sequential co-presence is being conflated with a non-integrated element accompanying a clausal or nominal anchor. The pilot prompt's broad phrase “another complete ... utterance unit” leaves that boundary underspecified.
- Qwen alone codes BLACK N from Wilkins's observation that *black* is not commonly used as an utterance without preceding linguistic context. The quote concerns conventional standalone use. It does not positively restrict the specified adjective use to integrated-only or standalone-only occurrence, as the negative standard requires.

Both cells are isolated and do not affect consensus. They identify the next manual clarifications needed: distinguish turn-sequential accompaniment from anchor-linked non-integration, and keep absence of conventional standalone use separate from a negative P02 value.

## Did packet v2 work?

Packet v2 materially improved retrieval for the already-supported items. OUCH and WOW received the highly relevant CGEL passage at the head of their packets, and all coders used direct CGEL or Ameka evidence consistently. GEE, which is not in CGEL's central-member list, continued to be supported by Ameka's item-specific example. Deduplication worked in the limited sense that no normalized duplicate excerpts were selected within a packet.

Packet v2 did not solve sparse evidence. DAMN_PRENOM still produced no non-U vote even though CGEL evidence for supplementary *damn* was present; coders correctly kept the specified prenominal use separate. BANG_DEPICT, BLOODY_PRENOM, COFFEE, and STOP remained U across all four coders. MMHM and BLACK each attracted one semantically contestable non-U vote, but no second independent vote.

The class/context component has a foreseeable risk. It makes supplement discussions available even where the item is absent, which can clarify the behavioural territory but can also invite transfer from a class discussion to an item that the passage does not include. In this run, that did not change consensus, but full-run packets should retain the explicit item-form versus class/context separation and the requirement that class evidence explicitly include the item (possibly across linked passages only under a separately stated rule).

## Operational implications

Copilot remains by far the fastest route, but this is its second consecutive run with a non-verbatim ellipsis quote and with isolated semantic overreach. It needs automatic rejection for quote continuity and a later semantic screen.

Agy was clean in pilot 3, including its item identifiers, but took about 79 seconds per item. Qwen took about 62 seconds per item. Naive linear extrapolation to 490 cells gives roughly 10.7 sequential hours for Agy and 8.5 hours for Qwen, before retries. Those extrapolations are only scale indicators; batching, concurrency, properties with smaller packets, and provider behaviour could change them. Copilot's single-call time cannot be extrapolated the same way because 35-item columns will require checking context limits and batching.

Quote locations now add nearby section headings, but they are still primarily markdown line addresses. Publication-page resolution remains incomplete and should not wait until after full coding.

## Conclusion

The sequence of pilots now separates the constraints cleanly:

1. Pilot 1 showed that coders can follow quotation rules but that a CGEL-label prompt suppresses relevant source-described behaviour.
2. Pilot 2 showed that behaviour-based instructions recover the Ameka evidence and substantially improve agreement.
3. Pilot 3 shows that relevance-ranked retrieval can surface direct class evidence reliably, but cannot create evidence where the held literature is silent or only adjacent.

Packet v2 is an improvement, not a solution to fill. Before any full run, the remaining decisions are conceptual and procedural: settle the turn-sequential boundary case represented by MMHM, tighten the negative standard illustrated by BLACK, finish source-page locations, and test how these packets and standards behave on at least one property unlike P02. FREEZE approval and registration should still wait.