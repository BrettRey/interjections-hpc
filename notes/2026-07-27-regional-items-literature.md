# The three regional items: what the literature says
<!-- SUMMARY: haba confirmed as a free-standing interjection by a JoP paper using the same GloWbE data; lah confirmed as prosodically integrated on both rival analyses; yaar source identified but not obtained · status: two of three resolved · updated: 2026-07-27 -->

## haba (Nigerian English) — resolved, and by the same corpus

**Unuabonah, Foluke Olayinka & Daniel, Florence Oluwaseyi (2020). "Haba!
Bilingual interjections in Nigerian English: A corpus-based study." *Journal
of Pragmatics* 163, 66–77.** Filed in `literature/`.

Studies five emotive bilingual interjections (*haba*, *kai*, *chei*, *chai*,
*mtchew*) borrowed into Nigerian English, using **the Nigerian component of
GloWbE** — the same data behind §4.5.4 and Appendix A.

The passage that settles the categorial question (p. 69):

> "The terms 'prospective' and 'retrospective' are used instead of
> utterance-initial or utterance-final to describe the position of the
> interjections because **they are free standing and are far more detached
> from the utterances than PMs**."

So specialists working on this variety, in this corpus, treat *haba* as
free-standing and more detached than a pragmatic marker, preferring the
prospective (utterance-initial) position. That corroborates the KWIC coding
independently and gives the *lah* / *haba* contrast published backing:

| form | prosodic/syntactic status | source |
|---|---|---|
| *lah* | carries the utterance's contour, or a weakly-stressed neutral-tone enclitic; not independent on either account | Lim 2007: 447, 463 |
| *haba* | free standing, detached, prospective | Unuabonah & Daniel 2020: 69 |

They also classify *haba* as an emotive interjection signalling "surprise,
shock, anger, disapproval, disgust, distress, despair, disbelief,
disappointment, and disagreement", from Hausa.

### A frequency discrepancy to resolve

They report (p. 69): "In the GloWbE corpus, haba occurs 248 times with a
relative frequency of 5.8 (pmw)", of which *haba* proper is 239 and the rest
are the spellings *habba*, *habaa*, *haaba*, *haabaa*.

`data/glowbe-interjection-frequencies.csv` gives **8.77 pmw** for Nigeria,
which on a 42.6M-word section implies about **374 tokens**. Their denominator
agrees (248 ÷ 5.8 ≈ 42.8M), so the gap is in the token count, not the
normalisation. Since `haba_uh` returns nothing, tagging is not the difference
either. Worth resolving before the appendix figure is defended: the corpus may
have been re-indexed since 2020, or our extraction may have used a different
query. **This is a check on our number, not theirs.**

## lah — resolved, see the companion note

`notes/2026-07-27-singlish-particle-prosody-leads.md`. Both rival analyses
agree it is not prosodically independent, so it fails \intj{syn} either way.

## yaar (Indian English) — source identified, not obtained

**Lange, Claudia (2009). "'Where's the party yaar': Discourse markers in
Indian English." In Thomas Hoffmann & Lucia Siebers (eds.), *World Englishes:
Problems, properties and prospects*, 207–225. Amsterdam: Benjamins (VEAW
G40).** Citation confirmed against Lange's own publication list at TU Dresden;
the Benjamins catalogue gives 207–226, so check the pagination on the copy.

Benjamins returns 403 to my fetcher. **Needed.**

Secondary lead, unverified: reporting suggests *yaar* is preferred in Pakistani
data and *na* in Indian data, with *yaar* more often clause-initial in
Pakistani usage. That would bear directly on the PK/IN difference in §4.5.4 and
on the positional split found in the KWIC samples, so it is worth confirming
from Lange rather than from search-result summary.

## Bearing on the paper

The three regional items are not one categorial kind, and this is now
citable rather than my inference:

- *haba* is a free-standing emotive interjection (Unuabonah & Daniel 2020)
- *lah* is prosodically integrated on any current analysis (Lim 2007)
- *yaar* sits between them on the corpus evidence; Lange 2009 should settle it

§4.5.4 currently lists all three as "plausible cases" of regional conditioning
without distinguishing them. That hedge is doing real work and should stay,
but the paper can now say *why* they differ instead of grouping them.

Unuabonah & Daniel is also a close neighbour paper the manuscript arguably
ought to cite regardless: corpus-based, GloWbE, interjections, World Englishes,
in a journal the paper was until recently aimed at.
