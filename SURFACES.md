# Surfaces

> **⚠ Read `~/Code/a.wjerk.shop/connections.md` first.** That file is the canonical cross-property map and it is further along than this one — it models **the concept, not the project, as the connecting unit**, gives every are.na channel a *role* (`sourcing` / `bibliography` / `archive` / `working` / `moodboard`), and is meant to become `connections.json` that the build stamps onto pages automatically. Its companion `arena-inventory.md` has all 518 channels with visibility counts and fuller prefix semantics than the table below.
>
> This file was written 2026-08-26/27 without knowing that existed, so parts of it duplicate that work by hand. **Where they disagree, `connections.md` wins.** What's still worth keeping here is the lecture-channel → repo-folder mapping and the loop/coverage table, neither of which that file has. Merge these two rather than maintaining both.

The same work lives in more than one place. This file maps each project across all of them, so material already written somewhere doesn't get rewritten here.

`SHARED-COMPONENTS.md` tracks reuse *inside* this repo — one idea appearing in two workshops. This tracks the same work across *different surfaces*: raw material here, a polished case study on `a.wjerk.shop`, research and notes on `bjornpaedia.wjerk.shop`, visual research on are.na, a pitch line in `MENU.md`.

Local sibling repos, browsable directly: `~/Code/a.wjerk.shop`, `~/Code/bjornpaedia`, `~/Code/sentence-a-day` (the TiddlyWiki source behind bjornpaedia).

---

## Figma (added 2026-09-02)

All slide decks live in one file, **AY26 Lectures and Presentations**
(`ltomqlGJOWEk1NEu0T9LSr`), one page per talk — 19 pages, ~2,100 frames.

`scripts/figma-slides.py` dumps a page to markdown so a deck can be grepped,
diffed, and cross-referenced from `SHARED-COMPONENTS.md` without opening Figma.
Needs `FIGMA_TOKEN` in `.env`. `--list-pages` enumerates the file.

Dumps live beside the lecture they support (`lecture-*/slides.md`), or in
`decks/` when there is no folder for them yet. They are dated snapshots —
regenerate, don't edit.

Worth knowing: **the decks run ahead of the scripts.** Three times on
2026-09-02 the deck already contained material the script was missing —
finished Clarke and Dator slides benched in the futures deck, seven built
Parsons & Charlesworth slides with no script text, and a semiotics
icon/symbol demonstration sitting two sections earlier than the section that
needed it. Check the dump before writing new material for a lecture.

The visual rules for these decks are **not** here — they live in
`~/Code/color-system-and-guidelines/RULES.md`, nine `## Presentations:`
sections plus `## Presentations: how the Figma file is built`.

## The loop

The goal, in Kristian's words (2026-08-27): **lectures** on things; **shirts** that condense a lecture into a semiotic gesture that goes out and lives in the world; **workshops** that make people do it. Each of the three tied back to a case study on `a.wjerk.shop` or to research and writing on `bjornpaedia.wjerk.shop`, so the whole thing reads as loops rather than as scattered outputs — a real picture of how the practice works.

That is a coherent model, and most of the parts already exist. What's missing is almost never the material. It's the link.

### The six surfaces

| Surface | Lives at | Local repo | Holds |
|---|---|---|---|
| Lectures & workshops | this repo | `~/Code/lectureScripts` | scripts, pitch sheets, transcripts |
| Shirts | `stuff.wjerk.shop` | `~/Code/shirts` | the store |
| Case studies | `a.wjerk.shop` | `~/Code/a.wjerk.shop` | 10 finished projects |
| Research & writing | `bjornpaedia.wjerk.shop` | `~/Code/sentence-a-day` | 1,400+ tiddlers |
| Visual research | are.na | — | 518 channels |
| Drafts | Notion | — | bios, essays, project pages |
| Syndication | [Medium](https://medium.com/@bjornmeansbear) | — | **deliberately downstream.** Publish to a site he controls, syndicate to Medium for reach, link back. POSSE. Every post should carry an "originally published at" line — which makes Medium a dating index for essays whose original host is gone |
| Old studio | `ookb.co` / `test.ookb.co` | — | The Office of Kristian Bjørnard. Original publication venue for the 2015 Pure Content essay; also hosts `ookb.co/cape` |

### Where the loops are complete, and where they break

L = lecture · S = shirt · W = workshop · C = case study · A = are.na · B = bjornpaedia

| Topic | L | S | W | C | A | B |
|---|---|---|---|---|---|---|
| Signs Signaling on Substrates | ✓ draft | **✓** | — | — | ✓ 11 | ✓ |
| Form, Content, Context | listed | **✓** | ✓ | — | ✓ | ✓ |
| The Libre Designer / open source | ✓ | — | ✓ | ✓ | ✓ 874 | ✓ |
| The Sustainabilitist Principles | ✓ | — | ✓ | ✓ | ✓ 2,957 | ✓ |
| Semiotic commons / Make It Mean Something | ✓ | — | ✓ | — | ✓ 94 | ✓ |
| Copyright & the commons | ✓ | — | ~ #4 | — | ✓ 224 | ✓ |
| A New Design Commons | ✓ | — | — | — | ✓ 309 | ✓ |
| What is Sustainable Graphic Design | ✓ | — | — | — | ✓ 514 | ✓ |
| Climate design | ✓ | — | — | — | ✓ ×3 | ✓ |
| Futures / speculative design | ✓ | — | ✓ | — | ✓ 111 | ✓ |
| Utopian gestures | ✓ | — | — | — | ✓ 46 | ✓ |
| Time, speed, motion | thin | — | — | — | ✓ ×5 | ✓ |
| BauErden | ✓ | — | — | — | ✓ 10 | ✓ |
| Chair-ness | — | — | ~ | ✓ | ✓ 485 | ✓ |
| 3P plastic | — | — | ✓ off-menu | ✓ | ✓ 124 | ✓ |
| Spontaneous Lamp | — | — | ✓ | ✓ | ✓ 6 | ✓ |
| Entropy | listed ×2 | — | — | — | ✓ 5 | ✓ |
| Solarpunk | listed | — | — | ✓ | — | ✓ |
| Carbon sequestering book | — | — | — | ✓ | — | ? |
| Green Acres → Ecovention | — | — | — | ✓ | — | ✓ |
| MICA grad zine | — | — | — | ✓ | — | ? |
| Repair — Kintsugi, Mending Nets | — | — | — | — | ✓ ×2 *images only* | ? |
| Drawing on tempered glass | — | — | — | ✓ | — | ? |

### What the table says

**The shirt leg is almost entirely missing.** Two shirts map to ideas — *Signs Signaling on Substrates* and *form content context*. Both happen to be the two most abstract, most definitional things in the practice, which suggests the shirt is doing exactly the job intended: it's the compression test. If an idea can't survive being a shirt, it may not be finished. Eight shirt channels exist; six are about type, music, or jokes rather than about the work.

**Nothing has all six.** The Libre Designer and the Sustainabilitist Principles have five — everything but a shirt. They're the closest to a complete loop, and each is one shirt away.

**Five case studies are orphans.** Solarpunk Boombox, Carbon Sequestering Book, Green Acres → Ecovention, MICA Grad Zine, Drawing on Tempered Glass have a finished public case study and no lecture, workshop, or shirt pulling from them. Two of those are things the booklet says it still needs.

**Two lectures exist only as are.na channels.** Kintsugi and Mending Nets, both private, both updated 20 August 2026 — the most recently active thing in this map.

Checked their contents 2026-08-27, and they are **image collections, not argument research**. Kintsugi: 22 blocks of tea bowls and golden repair from Wikimedia Commons, the Met, the Walters, LACMA, Britannica, rawpixel. Mending Nets: 21 blocks of the same subject in painting — Winslow Homer, Sorolla, Israëls, Avercamp, Utamaro, Kuniyoshi — from WikiArt, Artsy, the British Museum, Artvee.

Two things follow. **The effort is larger than "write it up"** — what's gathered is pictures, at the stage `Lecture: Signs Signaling Substrates Slide Images` is at, not the stage `Lecture: Utopian Gestures` is at (that one holds essays, talks, and notes for a lecture that exists). There is no argument yet.

**But the sourcing is already right.** Every block in both channels is public domain or open-licensed, from museum and commons collections — the same discipline the semiotic workshop teaches. Whatever these become, they were gathered the way the practice says to gather.

The pair is thematically tight: kintsugi makes the break visible in gold; mending nets is repair as ordinary labour, painted over and over across four centuries. Repair made visible rather than hidden. That connects to the circular-economy material (repair against replacement) and to the Signs Signaling Sustainability argument that form should declare its values.

**Time/speed/motion is inverted.** Five are.na channels feeding a folder with two text files. The research is done; the lecture isn't.

### Closing loops, cheapest first

1. **Link what exists.** Chair-ness alone is a channel, a case study, a repo, a Notion page, and a file here — five surfaces, no cross-references until today. No new work, just links.
2. **Two shirts.** *The Libre Designer* and *The Sustainabilitist Principles* each complete a five-of-six loop with one gesture.
3. **Two booklet essays** adopt the orphaned case studies instead of drafting from nothing.
4. **The repair lecture.** Two channels of research already gathered, nothing written.
5. **Time/speed/motion** — assemble from five channels plus the GD3 material.

---

## Linked already

| Project | Here | Case study |
|---|---|---|
| The Libre Designer | `workshop-open-source-design/` | [libre-designer](https://a.wjerk.shop/case-study-libre-designer.html) |
| 3P: People Processing Plastic | `workshop-circular-economy-design/workshop-3p-plastic.md` | [3p](https://a.wjerk.shop/case-study-3p.html) |
| Spontaneous Lamp | `workshop-circular-economy-design/workshop-spontaneous-lamp.md` | [spontaneous-lamp](https://a.wjerk.shop/case-study-spontaneous-lamp.html) |
| The Sustainabilitist Principles | `workshop-sustainabilitist-principles/` | [sustainabilitist-principles](https://a.wjerk.shop/case-study-sustainabilitist-principles.html) |

## Published, but nothing here points at it

Five of the nine case studies aren't referenced anywhere in this repo. Two of them are things the booklet says it still needs.

| Case study | What it is | Where it belongs here |
|---|---|---|
| [twobooks](https://a.wjerk.shop/case-study-twobooks.html) — "Green Acres → Ecovention Europe" | The exhibition catalog designed with curator Sue Spaid, and the 100%-ink-coverage palette | **`booklet-new-design-commons/OUTLINE.md` lists this as a case study that "still needs a home."** It has a finished, published home. Essay 06 or 07. |
| [micagradadmissions](https://a.wjerk.shop/case-study-micagradadmissions.html) | The pandemic die-cut zine that unfolds into a poster; one plate, print, flip the stack, re-run | **The other one OUTLINE.md says still needs a home.** Same fix. |
| [chairness](https://a.wjerk.shop/case-study-chairness.html) | Chair-ness | `workshop-circular-economy-design/chair-case-studies.md` covers the same ground and doesn't link to it. See also the unconfirmed Oka Terra overlap flagged in `SHARED-COMPONENTS.md`. |
| [solarpunk-boombox](https://a.wjerk.shop/case-study-solarpunk-boombox.html) | Solarpunk Boombox | "Solarpunk" is a listed but unwritten lecture in `Lectures To Writeup.txt`. This is the object that would anchor it. |
| [carbon-sequestering-book](https://a.wjerk.shop/case-study-carbon-sequestering-book.html) | A Carbon Sequestering Book | Fits the SGD lecture and the climate-design material. No link either way. |
| [drawing-on-tempered-glass](https://a.wjerk.shop/case-study-drawing-on-tempered-glass.html) | Drawing on Tempered Glass | No obvious match in this repo yet. Possibly nothing — worth a look. |

## are.na — 518 channels, now mapped

Recovered 2026-08-27 via `scripts/arena-channels.py` (v3 API, personal access token in a gitignored `.env`). Before that, no index existed anywhere and channels were named out loud in workshops and never written down.

**There is a naming taxonomy already in use.** It maps onto this repo more closely than anything here anticipated:

| Prefix | Means | Example |
|---|---|---|
| `Lecture:` | one per talk | Lecture: Utopian Gestures |
| `Workshop:` | one per workshop | Workshop: Copyright & a New Design Commons |
| `Project:` | one per assignment/brief | Project: Speed and Speculation |
| `§` | sustainability research | § The Sustainabilitist — **2,957 blocks** |
| `£` | libre / open source | £ FLOSD Free Libre Open Design — 874 blocks |
| `Shirt:` | one per shirt | Shirt: Signs Signaling on Substrates |
| `Wjerk:` / `Ω Wjerk:` | studio and client work | Wjerk: Precious Plastics |
| `BRN:` | book reading notes | BRN: Ways of Seeing |
| `://` | web, interface | :// what is an interface? |

### Lecture channels → this repo

| Channel | Blocks | Here |
|---|---|---|
| [Lecture: What is Design?](https://www.are.na/kristian-bjornard/lecture-what-is-design) | 67 | **Nothing.** `Lectures To Writeup.txt:33` has this slot empty. 67 blocks of research already exist. |
| [Lecture: Signs Signaling Substrates Slide Images](https://www.are.na/kristian-bjornard/lecture-signs-signaling-substrates-slide-images) | 11 | `lecture-signs-signaling-on-substrates/` |
| [Lecture: Signs Signaling Sustainability (Art, etc.)](https://www.are.na/kristian-bjornard/lecture-signs-signaling-sustainability-art-etc) | 99 | `booklet-new-design-commons/07-…` |
| [Lecture: Surface — A New Design Commons](https://www.are.na/kristian-bjornard/lecture-surface-a-new-design-commons) | 309 | `lecture-new-design-commons/` — note "Surface," confirming the AIGA CFP link |
| [Lecture: Utopian Gestures](https://www.are.na/kristian-bjornard/lecture-utopian-gestures) | 46 | `lecture-utopian-gestures/` |
| [Lecture: The Libre Designer](https://www.are.na/kristian-bjornard/lecture-the-libre-designer) | 74 | `workshop-open-source-design/` |
| [Lecture: Why Designer's Don't F/LOS](https://www.are.na/kristian-bjornard/lecture-why-designer-s-don-t-f-los) | 18 | same |
| [Lecture: What Does Sustainable Graphic Design Look Like](https://www.are.na/kristian-bjornard/lecture-what-does-sustainable-graphic-design-look-like) | 20 | `lecture-what-is-sustainable-graphic-design/` |
| [Lecture: WDSGDLL-20200316](https://www.are.na/kristian-bjornard/lecture-wdsgdll-20200316) | 24 | same, dated 16 March 2020 |
| [Lecture: Carbon Cycle](https://www.are.na/kristian-bjornard/lecture-carbon-cycle) · [Climate Change Notes](https://www.are.na/kristian-bjornard/lecture-climate-change-notes) · [CD→SSS](https://www.are.na/kristian-bjornard/lecture-cd-sss) | 29 / 19 / 57 | `lecture-climate-design/` |
| [Lecture: Some Semiotics](https://www.are.na/kristian-bjornard/lecture-some-semiotics) · [Semiotics, Building, Speed?](https://www.are.na/kristian-bjornard/lecture-semiotics-building-speed) | 94 / 8 | `workshop-semiotic-commons/` |
| [Lecture: Design for the Future Today](https://www.are.na/kristian-bjornard/lecture-design-for-the-future-today) | 111 | `lecture-design-for-the-future-today/` (2026 transcript + references) and `workshop-designing-for-the-future/` (2023 versions, facilitator guide) |
| [Lecture: Intro to Motion](https://www.are.na/kristian-bjornard/lecture-intro-to-motion) · [What is Time?](https://www.are.na/kristian-bjornard/lecture-what-is-time) · [Newton vs Aristotle](https://www.are.na/kristian-bjornard/lecture-newton-vs-aristotle-motion) · [Everything is a Motion Graphic](https://www.are.na/kristian-bjornard/lecture-everything-is-a-motion-graphic) · [Slowing down graphic design](https://www.are.na/kristian-bjornard/lecture-slowing-down-graphic-design) | 84 / 32 / 8 / 3 / 19 | `lecture-time-speed-motion/` — five channels for a folder holding two text files |
| [Lecture: Entropy](https://www.are.na/kristian-bjornard/lecture-entropy) | 5 | Listed twice in `Lectures To Writeup.txt`, unwritten |
| [Lecture: Remix](https://www.are.na/kristian-bjornard/lecture-remix) · [Design as a common good](https://www.are.na/kristian-bjornard/lecture-design-as-a-common-good) | 1 / 10 | booklet 03, NDC |
| [Lecture: Mending Nets](https://www.are.na/kristian-bjornard/lecture-mending-nets) · [Lecture: Kintsugi](https://www.are.na/kristian-bjornard/lecture-kintsugi) | 21 / 22 | **Nothing here at all.** Both private. Repair as a subject — not in `Lectures To Writeup.txt` either. |

### The two channels that were lost

Both named aloud in the January 2025 workshop transcripts with no URL recorded. Found:

- **"my own collection on Arena of open source fonts"** → [£ LibreType](https://www.are.na/kristian-bjornard/libretype), 232 blocks. Same channel already cited in `theLibreDesigner.md:195`.
- **"a whole arena board of information about copyright and book references"** → [Workshop: Copyright & a New Design Commons](https://www.are.na/kristian-bjornard/workshop-copyright-a-new-design-commons), 224 blocks. Belongs to `workshop-semiotic-commons/copyright-and-the-commons.md` and to workshop #1's Day One.

**Stale URL:** `Why Libre Design.txt:1165` cites `are.na/kristian-bjornard/free-libre-open-design`. The channel is now at [`flosd-free-libre-open-design`](https://www.are.na/kristian-bjornard/flosd-free-libre-open-design), 874 blocks. The old link is likely dead.

### The big research collections

Not lecture-specific. These are where the thinking accumulates.

- [§ The Sustainabilitist](https://www.are.na/kristian-bjornard/the-sustainabilitist) — **2,957 blocks.** Largest by far, and the throughline of the whole practice.
- [§ @ ¬ Sustainable Aesthetics.](https://www.are.na/kristian-bjornard/sustainable-aesthetics) — 1,093
- [£ FLOSD Free Libre Open Design](https://www.are.na/kristian-bjornard/flosd-free-libre-open-design) — 874
- [Wjerk: Use This For Something](https://www.are.na/kristian-bjornard/wjerk-use-this-for-something) — 520
- [§ SGD](https://www.are.na/kristian-bjornard/sgd) — 514
- [Chair-ness](https://www.are.na/kristian-bjornard/chair-ness) — 485
- [Wjerk](https://www.are.na/kristian-bjornard/wjerk) — 400
- [3P: People Processing Plastic](https://www.are.na/kristian-bjornard/3p-people-processing-plastic) — 124

### Four surfaces for one project

**Chair-ness** is the clearest case of the same work living everywhere and connecting nowhere: an are.na channel (485 blocks), a published [case study](https://a.wjerk.shop/case-study-chairness.html), `workshop-circular-economy-design/chair-case-studies.md` here, and a "Chair project w/ Chris Attenborough" page in Notion. None of the four referenced any of the others before today.

### Gaps

- **No Drawdown Diptychs channel.** The workshop is built on visual research from open sources and has no collection.
- **No Solarpunk channel**, though the lecture is listed and a [case study](https://a.wjerk.shop/case-study-solarpunk-boombox.html) exists.
- `Shirt: Signs Signaling on Substrates` (13 blocks) — the phrase became a shirt. Another surface for `lecture-signs-signaling-on-substrates/`.

### Naming new channels

The taxonomy already works. The gap is that only one `Workshop:` channel exists, so workshop research has nowhere consistent to go. Convention going forward, so a channel and a folder find each other later:

**`Workshop: <exact title from MENU.md>`** — matching the menu means the channel, the pitch sheet, and the folder all carry the same name.

| Menu title | Folder | Channel |
|---|---|---|
| Make It Mean Something | `workshop-semiotic-commons/` | — |
| Drawdown Diptychs | `workshop-semiotic-commons/` | — |
| The Libre Designer | `workshop-open-source-design/` | `Lecture:` exists, no `Workshop:` |
| The Sustainabilitist Principles | `workshop-sustainabilitist-principles/` | — |
| Design the Future Today | `workshop-designing-for-the-future/` | `Lecture:` exists, no `Workshop:` |
| Structured Creativity | `workshop-structured-creativity/` | — |
| Form, Content, Context | `workshop-form-content-context/` | `Shirt:` exists, no `Workshop:` |
| Spontaneous Lamp | `workshop-circular-economy-design/` | — |
| *(off menu)* 3P | `workshop-circular-economy-design/` | `3P: People Processing Plastic`, 124 blocks |
| *(not on menu)* Copyright & the Commons | `workshop-semiotic-commons/copyright-and-the-commons.md` | **[Workshop: Copyright & a New Design Commons](https://www.are.na/kristian-bjornard/workshop-copyright-a-new-design-commons)**, 224 blocks — the only one that exists |

Three of these already have a `Lecture:` or `Shirt:` channel holding overlapping research. Those don't need merging; a workshop and its lecture are different collections. But when a workshop channel gets made, cross-link it to the lecture one in are.na so the pair is visible from either side.

**When a workshop names a channel out loud in the room, add the URL to this file the same week.** That's the failure that lost two channels for a year — they were findable by everyone who attended and by nobody afterward.

Worth noting: `Workshop: Copyright & a New Design Commons` is research for a workshop that doesn't formally exist yet. `copyright-and-the-commons.md` is currently workshop #1's Day One lecture *and* the leading candidate for a standalone #4 (see `SHARED-COMPONENTS.md`). The channel having its own name suggests it was already being treated as its own thing.

### Re-running this

```
python3 scripts/arena-channels.py           # all 518
python3 scripts/arena-channels.py libre     # filter by title or slug
```

## bjornpaedia — barely connected

Referenced in exactly two files: `workshop-sustainabilitist-principles/sustainabilitist-principles-source.md:3` and `workshop-semiotic-commons/variations-pitch-booklet.md:148`. The wiki has far more in it than that — see the `sentence-a-day` finds logged throughout `SHARED-COMPONENTS.md`.

---

## How to use this

- Before writing anything new, check whether a polished version already exists on `a.wjerk.shop`. Twice now, finished prose has been sitting there while this repo treated the topic as unwritten.
- When a workshop or lecture names an are.na channel out loud, **record the URL here**. That's the failure this file exists to stop.
- Links stay one-directional — this repo points out at the published surfaces. The case studies are their own thing and don't need to point back.
- Add a row when a new case study goes up on `a.wjerk.shop`.
