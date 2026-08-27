# Next up — migrating lectureScripts into bjornpaedia tiddlers

Written 2026-08-27, stopping mid-task. Everything needed to restart is here. **Nothing has been written to `sentence-a-day` yet.**

---

## The question that started it

Should a lecture in bjornpaedia be small reusable chunks assembled by transclusion, or is a 2,000-word essay fine as one tiddler if it interlinks?

**Answered, and the answer is Kristian's own.** He built the chunk-and-assemble pattern in August 2021 and it's used in **92 tiddlers**. Chunks, not essays — on his own evidence: every long thing he's written has been quarried afterward (`WhatIsSGD.md` → booklet essays 05, 06, 07; the Notion Substrates essay → a lecture plus a pointer file). A 2,000-word tiddler can't be transcluded in three places; a 156-word one can.

## The pattern to replicate

The model is `sad2021tw/tiddlers/Lecture_ What Is Sustainable Graphic design_ (April 2021).tid`. The parent tiddler carries **no prose of its own** — only headings and transclusions:

```
created: 20210828025855258
list: [[Define Sustainability]] [[The Sustainabilitist Principles]] [[...]]
modified: 20210828034918110
tags: Lecture Nebraska
title: Lecture: What Is Sustainable Graphic design? (April 2021)
type: text/vnd.tiddlywiki

{{Define Sustainability}}

!! Good Formalism

{{Good Formalism}}
```

And each chunk is tagged back to its parent:

```
created: 20210828031544380
modified: 20210828034918079
tags: [[Lecture: What Is Sustainable Graphic design? (April 2021)]]
title: Good Formalism
type: text/vnd.tiddlywiki

<body>
```

**Chunk size is 100–200 words.** Measured: Define Sustainability 104, Good Formalism 108, Example: Green Acres 156, An Idea: Signs Signaling Sustainability 166, Example: MICA Grad Zine 201. A paragraph or two — the smallest thing you'd cite somewhere else.

**Naming taxonomy already in use:** `Define X` · `Good X` · `Example: X` · `An Idea: X` · `Lecture: X`. Same discipline as the are.na prefixes.

**Filename escaping:** `/ \ : ? " < > | *` all become `_`. So `Lecture: Foo?` → `Lecture_ Foo_.tid`.

**Markup:** `!!` for h2, `!!!` h3, `<<<` … `<<<` for blockquote, `''bold''`, `//italic//`, `[[text|url]]`, `* ` for bullets.

## The tool

`scripts/md-to-tiddlers.py` in this repo. Written and dry-run tested; **never overwrites** — it reports collisions and skips them.

```
python3 scripts/md-to-tiddlers.py <file.md> --title "Lecture: Foo" [--tags "Lecture Bar"] [--prefix "Example: "]
python3 scripts/md-to-tiddlers.py <file.md> --title "Lecture: Foo" --write
```

It strips YAML frontmatter and HTML comments (so the TO DO blocks don't travel), splits on `##`, converts markdown to TiddlyWiki markup, writes one tiddler per section tagged to the parent, and builds the parent with a `list:` field and transclusions.

Verified dry run, `booklet-new-design-commons/07-signs-signaling-sustainability.md`:

```
chunks : 5
   194w  Beauty is a rendition of values
   140w  The obvious objection
   356w  Four that do it
   102w  Greenwashing
   146w  What I actually think now
```

Right size range, except "Four that do it" at 356 — that one is four case studies in one section and should be split into four `Example:` tiddlers by hand.

## Before writing anything — the collision problem

**The 2021 wiki already covers a lot of the SGD material.** `Good Formalism`, `Define Sustainability`, `An Idea: Signs Signaling Sustainability`, `Example: Green Acres`, `Example: MICA Grad Zine` all exist as tiddlers. Booklet essay 07 is a *rewrite* of that same material. Running the converter on it would create near-duplicates under slightly different names, which is the exact drift `SHARED-COMPONENTS.md` exists to prevent.

So the order matters:

1. **Convert what has no wiki presence at all.** `lecture-signs-signaling-on-substrates/` (2024–26 material, wiki is mostly 2021), `lecture-design-thinking/`, `lecture-ethnographic-research/`, `workshop-semiotic-commons/copyright-and-the-commons.md`.
2. **For material that already has tiddlers, update the existing tiddler rather than making a new one.** Booklet 07 vs `Good Formalism` is the test case — the booklet prose is better; the tiddler is the canonical location. Merge into the tiddler.
3. **Don't chunk anything already published on `a.wjerk.shop`.** Link to the case study. Two copies will drift.

## Recommended order

| Order | Source | Parent tiddler | Why |
|---|---|---|---|
| 1 | `lecture-signs-signaling-on-substrates/lecture-signs-signaling-on-substrates.md` | `Lecture: Signs Signaling on Substrates` | Newest, zero wiki presence, and the wiki already has the stub `Signs Signaling on Substrates` (2024) to link from |
| 2 | `workshop-semiotic-commons/copyright-and-the-commons.md` | `Lecture: Copyright and the Commons` | Finished prose, no tiddlers, feeds workshop #1 and possible #4 |
| 3 | `lecture-design-thinking/di200-wk1-design-thinking-lecture.md` | `Lecture: Design Thinking` | New course material, nothing in the wiki |
| 4 | `lecture-ethnographic-research/di200-wk1-ethnographic-research-lecture.md` | `Lecture: Ethnographic Research` | same |
| 5 | booklet essays 00–09 | one per essay | **Merge, don't create** — check each against 2021 tiddlers first |

## Open decisions

- **Where do workshop pitch sheets go, if anywhere?** They're sales documents, not thinking. Probably not tiddlers at all — or one `Workshop: X` tiddler per workshop that transcludes the concept chunks and links to `MENU.md`.
- **Tag vocabulary.** The 2021 tiddlers use `tags: Lecture Nebraska` — type plus occasion. Worth deciding the full set before bulk-writing, or the tag pane becomes noise.
- **Does the `Example:` prefix want to be its own thing?** There are already `Example: Green Acres` and `Example: MICA Grad Zine`, and both are also a.wjerk.shop case studies. A convention where `Example:` tiddlers are one-paragraph summaries that link out to the full case study would close that loop cleanly.
- **Should the converter also emit backlinks into `lectureScripts`?** Right now migration is one-directional; the markdown file won't know its tiddler exists.

## Restarting

1. `cd ~/Code/lectureScripts`
2. Dry-run the item at the top of the order table.
3. Check the collision list against `~/Code/sentence-a-day/sad2021tw/tiddlers`.
4. `--write`, then review in the wiki before committing — `sentence-a-day` is its own repo, currently clean on `master`.

---

## Correction, same day — this overlaps existing work

`~/Code/a.wjerk.shop` already contains `connections.md` and `arena-inventory.md`, both pulled 2026-08-27. They cover much of what `lectureScripts/SURFACES.md` covers, and are better in three ways:

- **The connecting unit is the concept, not the project.** "A project draws on concepts; a concept has a canonical tiddler, a research channel, and maybe a lecture and an object." That is the right model and SURFACES.md doesn't have it.
- **Channels have a `role`** — `sourcing` / `bibliography` / `archive` / `working` / `moodboard` — which says what a channel is *for* rather than what it holds, and determines how it should be rendered on a page.
- **It's headed for automation.** `connections.md` becomes `connections.json`; the build stamps an "Elsewhere" block onto each page from it and checks the links resolve. SURFACES.md is hand-maintained markdown, which will drift.

`arena-inventory.md` also has all 518 channels with visibility counts (231 closed / 173 public / 114 private) and fuller prefix semantics — including `mm-` (43) and the course-code prefixes (`di200-`, `di220-`, `gd-prd-223-`, `ad1/2-`, `gd1/2/3-`, `gd105-`) that SURFACES.md missed entirely.

**Next session: merge, don't maintain both.** SURFACES.md keeps two things that file doesn't have — the lecture-channel → repo-folder mapping, and the loop/coverage table across lecture / shirt / workshop / case study / are.na / bjornpaedia. Fold those into `connections.md` and leave a pointer behind.

## And this answers the "pure content" question

The machinery is already half-built on the case-study side:

- `case-study-template.html` with `{{TITLE}}`, `{{DESCRIPTION}}`, `{{IMAGE}}`
- `generate-case-studies.sh`
- `build.sh`, `SPEC.md`, `methodology.md`
- `renderTiddlers.sh` in `sentence-a-day`, which already renders every tiddler to static HTML

So: **yes, case studies should pull their text from tiddlers — at build time, not runtime.** Tiddler is canonical, the template is the styling, the build joins them. That's the same pattern as `connections.json`, applied to prose instead of links.

This is "Pure Content" from `Lectures To Writeup.txt`, and it isn't a lecture topic — it's the architecture. Kristian built it once already as **CAPE, "create anywhere publish everywhere"** (per his own bio: "treating content as a pure material that could move fluidly between platforms... generating print documents from custom server workflows"). The tiddler-chunking question is the same principle applied to prose.

**Open, and worth deciding before any migration:** if tiddlers become canonical for case-study prose, the markdown in `lectureScripts` stops being a source and becomes a *rendering* too. That's a bigger change than chunking, and it decides whether this repo holds content or only holds working drafts.

---

## The migration already happened once — look at Pure Content first

Found 2026-08-27, after the plan above was written. **Pure Content / CAPE is already chunked in bjornpaedia**, ~5,300 words across nine tiddlers, tagged `CAPE` / `[[Pure Content]]` / `Writing`, with a `<<list-links>>` hub. It is the finished example of everything this plan proposes, done years ago.

```
2264w  What is CAPE?                     ← likely the c.2012–14 library/archive conference talk
 872w  Content is King
 472w  From Indesign to Pure Content
 455w  Extra Thoughts on CAPE
 432w  Decoupling content from its site
 324w  Striving For Static Sites
 240w  Create Anywhere Publish Everywhere
 206w  Towards Purer Content             ← tagged Essays + [[Utopian Gestures]]
  11w  CAPE                              ← hub
```

**Read these before converting anything.** They show the tag vocabulary actually in use (`Writing`, `Essays`, `OnMedium`), how a hub tiddler works, and how a chunk gets cross-tagged into more than one lecture — `Towards Purer Content` belongs to both Pure Content and Utopian Gestures. Two lectures, one chunk, no duplication. That is the whole argument for chunking, demonstrated.

The direction of travel is also worth noting: for this topic the **wiki is ahead of `lectureScripts`**, not behind. The migration is not one-way. Some topics need pushing into tiddlers; this one needs pulling out, or just linking to.

Not recorded anywhere yet: **which conference**, and when. Worth asking Kristian and adding it — everything else about this body of work is documented except where it was delivered.

## Another duplication to fold in

`sad2021tw/tiddlers/All Are.na Channels.tid` already lists are.na channels. Along with `a.wjerk.shop/arena-inventory.md` and `connections.md`, that makes **three** places inventorying are.na, plus `SURFACES.md` as a fourth. Consolidate to one before adding anything else.
