# P02 controlled re-pilot report

Date: 2026-11-03

Status: feasibility re-pilot only. These 40 cells are not study data and must not be reused in the full matrix.

## Controlled comparison

Pilot 2 used exactly the same packets, items, shuffling seeds, and call patterns as pilot 1. Two prompt elements changed:

1. P02 no longer asked coders to identify supplement “in the CGEL sense”. It asks whether a source describes or exemplifies a sign occurring with another complete unit while retaining separate, utterance-like status and not entering integrated construction with it.
2. Each non-U cell now records the source's own wording and whether the evidence is item-specific or class-level.

The comparison therefore isolates coder-facing framing. It does not test packet v2.

## Results by family

| Coder | Pilot 2 | Change from pilot 1 | Time | Output defects |
|---|---|---|---|---|
| Agy | 3Y, 0N, 7U | no value changes | 800.4 s | WOW item_id was “ITEM WOW”; intended item was recovered only from its per-item filename and flagged |
| Copilot | 4Y, 2N, 4U | OUCH and WOW U→Y; MMHM U→Y; BLOODY_PRENOM and BLACK U→N | 37.0 s; 5.98 AI credits; 35.5k input and 3.1k output tokens | 1 ellipsis-spliced quote; 1 punctuation-altered quote; 1 source wording absent from its quote |
| Qwen3.8-27b | 3Y, 0N, 7U | OUCH, WOW, and GEE U→Y | 420.4 s | all 3 Y quotes are 303 characters, 3 over the stated limit |
| Muse subagent (non-independent) | 3Y, 0N, 7U | no value changes | not instrumented | none detected |

All four coders gave Y for OUCH, WOW, and GEE under the intended-item recovery for Agy's WOW file. The independent consensus consequently changed from one Y in pilot 1 (GEE) to three Y values in pilot 2 (OUCH, WOW, GEE). The other seven items remain consensus U.

Fleiss's kappa for Agy, Copilot, and Qwen rose from 0.135 in pilot 1 to 0.619 in pilot 2. Pairwise agreement was 10/10 for Agy-Qwen, 7/10 for Agy-Copilot, and 7/10 for Copilot-Qwen. Muse aligned with Agy and Qwen on all ten items, but remains a non-independent comparison.

Unknowns remain substantial: 18 of the 30 independent cells are U (60%), and 7 of 10 consensus cells are U (70%). The revised framing recovered evidence that was already in the packets for the Ameka trio; it did not create evidence for the other items.

## Quote verification

There were 15 non-U cells. Thirteen quotes verified verbatim, after whitespace normalization, in both the packet and the cited source markdown.

Two Copilot quotes failed strict verification:

- OUCH joins two parts of Ameka's sentence with an ellipsis. Both parts are real, but the returned string is not the required continuous substring.
- MMHM reproduces Dingemanse's wording without the source's quotation marks around “Mm hm”, so it is punctuation-altered rather than exact.

No quote was fabricated from whole cloth. The remaining defects are schema failures, not source inventions:

- Agy returned the malformed identifier “ITEM WOW”. Its quote itself verified, and the intended item is unambiguous from the separate per-item call and filename.
- Qwen used the same 303-character Ameka quote for OUCH, WOW, and GEE, exceeding the 300-character instruction by three characters each time.
- Copilot's BLOODY_PRENOM cell gives “entering into construction” as its source wording, but that phrase does not occur in the supplied quote.

A production run should reject or retry these outputs automatically. In particular, quote length, identifier membership, continuity, and wording-in-quote can all be machine-checked before adjudication.

## Interpretation

The prompt correction had the predicted effect on the Ameka evidence. Qwen changed exactly OUCH, WOW, and GEE from U to Y after the question stopped asking it to match a framework label. It recorded all three as class-level evidence and preserved “co-utterances with other units” as source wording. Copilot likewise changed OUCH and WOW to Y, while Agy and Muse were already making that reading. This confirms that a substantial part of pilot 1's disagreement was manufactured by the CGEL-bound prompt rather than by disagreement about what Ameka's passage says.

The revised wording also exposed a second risk in Copilot's coding:

- MMHM was coded Y from the phrase “Passive Recipiency”. That identifies a sequential stance, but the quoted words alone do not describe the relevant occurrence-with-another-unit behaviour. Agy, Qwen, and Muse retained U.
- BLOODY_PRENOM was coded N from one integrated example, “Get the bloody thing out of my cheek!” A single integrated use does not by itself meet the pilot's positive-restriction standard for N.
- BLACK was coded N because Wilkins says it is not commonly used as an utterance without preceding linguistic context. That addresses elliptical standalone use, not a positive restriction to integrated-only or standalone-only occurrence.

Copilot is therefore much faster than the other routes but more willing to infer beyond the quoted behaviour. Its three extra non-U cells should not be read as better packet recall. They are overextensions under the stated standards.

## Stop-rule assessment after re-pilot

- The kappa revision threshold is no longer triggered on its face: 0.619 rather than 0.135.
- Unknowns still trigger packet revision if consensus unknowns are the denominator (70%). At the level of all independent cells the rate is exactly 60%, not above it. Either way, only the Ameka-supported trio had usable evidence in these packets, so packet construction remains the binding constraint.
- No family fabricated a quote. Copilot nevertheless needs automated schema and quote screening because two of its six non-U quotes failed strict verbatim verification.
- Agy's malformed WOW identifier and 800-second runtime make its current per-item mode the least scalable route. This is an operational issue, not evidence about its linguistic judgments, which aligned completely with Qwen's values in this run.

## Conclusion

The controlled re-pilot establishes two distinct findings. First, replacing the framework-label test with source-supported distributional behaviour materially improves agreement and recovers the Ameka evidence in line with Brett's reading. Second, the same packets still contain no usable P02 evidence for seven of ten items, and a faster coder can introduce inferential overreach once the wording becomes less label-bound.

The next step remains packet v2, not full coding. It should retrieve distributional descriptions and examples sectionally, deduplicate evidence, separate item-specific from class-level passages, preserve publication-page locations, and be paired with automatic schema and quote rejection before any human adjudication.
