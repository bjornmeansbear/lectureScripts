# Pure Content / CAPE

The idea underneath everything else in this repo, and the oldest thing in it. Listed as a lecture in `Lectures To Writeup.txt` under General. Delivered as **“Towards Purer Content”** at **Web Archives 2015: Capture, Curate, Analyze**, University of Michigan, **12–13 November 2015**.

**Pure content**, in Kristian's words (2026-08-27): the abstract concept powering CAPE. Publishing everywhere required clear, structured content *"that didn't try to imply too much (or at all) what it should look like or be used for."* Content that carries no presentation and no intended use. Style is applied later, per context, and can change infinitely without touching the source.

**CAPE** = Create Anywhere Publish Everywhere. The software and service built on that idea. Nearly a decade of work with developer **Kai Curry**.

## Chronology

Full dated sequence, 2006 to now, in `CHRONOLOGY.md`. Short version: CAPE built with Kai Curry 2011–2014, a lecture in 2014, the essay published at test.ookb.co on 14 May 2015 and on Medium 2 June 2015, then the paper at Web Archives 2015 in November.

## In this folder

- `CHRONOLOGY.md` — the dated sequence, with a source for every entry.
- `2014-medium-framing-note.md` — the dating and context for CAPE, plus evidence of an **earlier 2014 lecture**. The only part of the Medium essay not already in bjornpaedia.
- `2015-WebArchives-paper-proposal.md` — **the talk itself.** Title, abstract, and bio as submitted, recovered from email 2026-08-27. The only surviving document of the presentation.
- `compiled-from-tiddlers.md` — **generated, do not edit.** All nine source tiddlers rendered into one readable document, 5,272 words. Regenerate with `scripts/tiddlers-to-md.py`.

That's deliberate. The tiddlers are canonical; this folder holds a rendering. Editing the markdown would fork it from the source, which is precisely what the material argues against.

## The source

`~/Code/sentence-a-day/sad2021tw/tiddlers`, tagged `CAPE` / `[[Pure Content]]` / `Writing`:

| Words | Tiddler | |
|---|---|---|
| 2,264 | What is CAPE? | likely the conference talk itself |
| 872 | Content is King | |
| 472 | From Indesign to Pure Content | |
| 455 | Extra Thoughts on CAPE | |
| 432 | Decoupling content from its site | |
| 324 | Striving For Static Sites | |
| 240 | Create Anywhere Publish Everywhere | the definition |
| 206 | Towards Purer Content | also tagged `[[Utopian Gestures]]` |
| 11 | CAPE | hub; carries `url: https://www.ookb.co/cape/` |

`Towards Purer Content` being tagged into two lectures at once is the argument for chunking, demonstrated: one chunk, two talks, no duplicate.

## Elsewhere

- **are.na** — [CAPE / Pure Content](https://www.are.na/kristian-bjornard/cape-pure-content), 26 blocks
- **Published** — <https://www.ookb.co/cape/>, from the `url` field on the CAPE tiddler
- **No case study** on a.wjerk.shop. See below.

## Open

- ~~Which conference~~ **RESOLVED 2026-08-27.** *Towards Purer Content*, at **Web Archives 2015: Capture, Curate, Analyze**, University of Michigan, 12–13 November 2015.
  - The talk title is Kristian's recollection, and it matches an existing tiddler exactly — `Towards Purer Content`, 206 words, tagged `Essays [[Utopian Gestures]] [[Pure Content]] OnMedium`. **That tiddler is almost certainly the talk's abstract or its surviving text**, which makes it the most important of the nine rather than the smallest.
  - The two emails found are attendee mail — a registration confirmation, and a workshop assignment placing him in *Using Web Archives*, Friday 13 November, 10:40am, Hatcher Gallery. He attended that workshop as part of attending; it isn't evidence against presenting.
  - **The paper proposal itself has since been recovered** — see `2015-WebArchives-paper-proposal.md`. It carries **WYSIWYM over WYSIWYG** (*what you see is what you mean*), the sharpest phrasing of the idea, which appears nowhere else in the archive. Still unlocated: the deck and the programme listing.

- **Still to write up:** `Hopkins Conference Books`, `ICFP`, and `Print from the Browser` — referenced in `These Gestures Are Undoubtedly Utopian.tid`, all three tiddlers empty. These read as the print-from-database clients, which makes them the concrete proof for CAPE's print half. The case study currently claims that half with no named example.
- **This should probably be a Wjerk case study.** Nearly a decade of work with Kai Curry, and it's the only major body of work in the practice with no case study. It would also be the only one on `a.wjerk.shop` that's about process and infrastructure rather than an object — which is a gap in that set, not a mismatch. Kai should be credited the way Christopher Attenborough is on 3P.
- **It is also the architecture the rest of this work is heading toward.** `a.wjerk.shop` has `case-study-template.html` and `generate-case-studies.sh`; `connections.md` plans to stamp Elsewhere blocks from `connections.json` at build; `sentence-a-day` has `renderTiddlers.sh`. All CAPE, rebuilt. A case study could say so.
- **The symmetry with Signs Signaling on Substrates.** Both say the carrier is variable and the thing carried is fixed — rendering vs. content here, substrate vs. signalling intent there. A decade apart. See `SHARED-COMPONENTS.md`.
