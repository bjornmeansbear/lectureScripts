# Pure Content / CAPE

The idea underneath everything else in this repo, and the oldest thing in it. Listed as a lecture in `Lectures To Writeup.txt` under General, delivered once at a library and archive conference around 2012–2014.

**Pure content**, in Kristian's words (2026-08-27): the abstract concept powering CAPE. Publishing everywhere required clear, structured content *"that didn't try to imply too much (or at all) what it should look like or be used for."* Content that carries no presentation and no intended use. Style is applied later, per context, and can change infinitely without touching the source.

**CAPE** = Create Anywhere Publish Everywhere. The software and service built on that idea. Nearly a decade of work with developer **Kai Curry**.

## In this folder

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

- **Which conference, and what year?** Still unknown. Searched 2026-08-27 — **don't repeat these:**
  - Gmail: `kbjornard@mica.edu` has **nothing before 2015**. A c.2012–14 talk would have been on another address (ookb.co, sundaysenergy, or a personal account). Dead end unless an old mailbox is still reachable.
  - All of `~/Code` grepped for the obvious venue names — MARAC, Code4Lib, LITA, DLF Forum, Museums and the Web, MCN, THATCamp, SAA, ACRL, Personal Digital Archiving. **No hits anywhere.**
  - `Hopkins Conference Books`, `ICFP`, and `Print from the Browser` are referenced in `These Gestures Are Undoubtedly Utopian.tid` but the tiddlers are **empty**. Those look like print-from-database *clients* rather than the speaking venue — worth writing up either way, since they're the concrete proof for the print half of CAPE.
  - Not yet tried: Google Drive (a deck from then would name it on the title slide), the `sundaysenergy` GitHub org, and the live `ookb.co/cape` page.
  - Baltimore-area candidates worth a memory jog: **MARAC** (Mid-Atlantic Regional Archives Conference) is the most plausible given the region; then Code4Lib, LITA Forum, DLF Forum, MCN, Museums and the Web, Maryland Library Association.
- **This should probably be a Wjerk case study.** Nearly a decade of work with Kai Curry, and it's the only major body of work in the practice with no case study. It would also be the only one on `a.wjerk.shop` that's about process and infrastructure rather than an object — which is a gap in that set, not a mismatch. Kai should be credited the way Christopher Attenborough is on 3P.
- **It is also the architecture the rest of this work is heading toward.** `a.wjerk.shop` has `case-study-template.html` and `generate-case-studies.sh`; `connections.md` plans to stamp Elsewhere blocks from `connections.json` at build; `sentence-a-day` has `renderTiddlers.sh`. All CAPE, rebuilt. A case study could say so.
- **The symmetry with Signs Signaling on Substrates.** Both say the carrier is variable and the thing carried is fixed — rendering vs. content here, substrate vs. signalling intent there. A decade apart. See `SHARED-COMPONENTS.md`.
