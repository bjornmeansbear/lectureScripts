# Session — 26/27 August 2026

Started with one question about a stray Notion export. Ended with the root emptied, a bookable menu written, and eight workshop sheets sized for print.

24 commits, `febb839` → `402bb62`. All pushed except the last.

---

## What changed structurally

**The root is empty.** It held ~25 loose drafts. Now it holds `README.md`, `MENU.md`, `SHARED-COMPONENTS.md`, `SURFACES.md`, and `Lectures To Writeup.txt`. Everything else went into a named directory.

New folders: `lecture-signs-signaling-on-substrates/`, `lecture-utopian-gestures/`, `lecture-climate-design/`, `lecture-time-speed-motion/`, `lecture-new-design-commons/`, `lecture-professional-practice/`, `lecture-what-is-sustainable-graphic-design/`, `lecture-bauerden/`. `DesignThinking/` and `EthnographicResearch/` renamed to `lecture-*` to match.

All moves used `git mv`, so history survived. Every path reference across the booklet essays, `OUTLINE.md`, `review.html`, and internal cross-links was rewritten to match, and every relative link in every tracked `.md` was audited afterward.

**Two duplicate/misfiled things resolved.** The two `NDC lecture script.txt` files were never different content — the diff is one blank line. `OUTLINE.md` had carried that as an open "verified by hash" mystery since the booklet was outlined. Duplicate deleted. And four NDC source files were living in `workshop-open-source-design/`, including booklet essay 00's primary source; they're now in `lecture-new-design-commons/`.

---

## The intellectual thread — worth not losing

This ran alongside the cleanup and is the more interesting half.

**"Signs signaling on substrates" is from 2019, and it started as a materials question.** `~/Code/sentence-a-day/SAD2019.md`: `:151` papermaking and clay tablets, `:179` carbon capture, `:186` *"Okay, Signs on Substrates. Carbon capture. What the hell am I going to do?"*, then `:230` turning theoretical — *"Every graphic design problem's answer is not a book; or a poster; or an identity… Can it always be framed as signs on substrates?"* — and `:463` holding both branches at once: *"pragmatic utopian. signs on substrates signalling sustainability. how to put that together?"*

So booklet essay 07 ("Signs Signaling **Sustainability**") and the new lecture ("Signs Signaling on **Substrates**") are not a name collision. They're one phrase that forked, and `:463` is the unfinished attempt to fuse them.

**The 2022 AIGA CFP is the missing middle.** Conference theme was SURFACE; underneath it, a title brainstorm — "Signs Signaling on Surfaces," "Signs on Surfaces Signaling Sustainably." Those sit directly under *"do I pitch free culture as a paper/lecture… or a workshop???"*, so they were titles for the **commons** talk. As late as 2022 the phrase was doing triple duty: sustainability, commons, definition. Also explains why Ben Duvall matters — his line is literally *surface + sign = a work of graphic design*, so the conference handed KB the exact frame he was arguing against. Filed in `lecture-new-design-commons/`.

**The broad definition of design was already written, in 2021.** `sad2021tw/tiddlers/020211102222602 Ideas.tid`, a reply to a Nico Chilla are.na block: *"how do you translate your interests and desires and intentions into things — these things can be posters, websites, apps, books, zines, dances, songs, flags, chairs, gardens, whatever."* KB confirmed this is the definition. Not form-giving (silent on ideology, and defines by output). Not problem-solving (rejected in that entry itself).

**The discriminator is intent, not medium.** Corrected mid-session — I first argued signaling doesn't scale to chairs without flattening function, and KB rejected that correctly: a chair's form denotes chairness and connotes comfort or status, which *is* signaling, and Krippendorff and Barthes support it rather than warn against it. The real question was never "does this cover all design," it's "is this medium-agnostic enough to cover a graphic designer making a chair." It is. Graphic design is what you're doing when the purpose is to signal a meaning, whatever the substrate.

Consequences: it strengthens the automation argument (define by output, Canva wins; define by intent, the practice is portable), and it makes 3P, Spontaneous Lamp, and the Drawdown diptychs *graphic design with unusual substrates* rather than departures.

**Product design, and the overlap.** Product design = affordance-first, same axis. But Norman had to add "signifier" in 2013 because an affordance nobody can perceive is inert — so affordance-first still needs a signaling layer. KB pushed further and was right: the overlap isn't a layer one discipline owns, it's that the disciplines are historical bundles of *intent + medium + toolset + guild*, and signaling intent ran across all of them the whole time. Checkable: SEGD, product semantics, and interaction design are all institutions founded in that intersection.

Full reasoning, with the retracted versions kept visible: `lecture-signs-signaling-on-substrates/sources-and-pointers.md`.

**Still undrafted:** the genus half — "translating intention into things." Material is the 2021 tiddler, the silverware-roll/hobo-knife cluster at `SAD2019.md:174–178`, and the Simon sentence already unpacked in `lecture-design-thinking/`.

---

## MENU.md — the à la carte menu

New at root. Eight workshops, nine lectures, numbered 1–17. Intro, who it's for, the bare list, short descriptions, booking, and a back-page third-person bio. Written to be letter-sized and riso-printed.

Two deliberate moves: it says which workshops have never been run (#4, #7) and which lecture is a draft (#13); and it leads with the materials being free, so what's sold is facilitation.

**3P came off the menu** — the grinding rig doesn't travel and a two-day slot has no troubleshooting time. Sheet kept, flagged at the top, still pitchable to anyone who can come to MICA.

**Facts confirmed during the session:** Undergraduate Design Chair Fall 2022 → summer 2026, now faculty in Graphic Design and Design and Innovation (**not** product design). Kalamazoo 1999–2003 BA Studio Art; MICA GDMFA 2007–09. Hixson-Lied Visiting Artist Lecture, 14 April 2021, UNL School of Art, Art History & Design, over Zoom. Drawdown first ran at Utah in 2021 over five weeks, **entirely remotely**. Christopher Attenborough credited as collaborator. Always spell it **Bjørnard**.

**Still open on the menu:** images (KB is sourcing), contact details go in at layout not in the repo, and whether the fees are current.

---

## Sheet lengths — all eight now fit front/back letter

| Sheet | Words |
|---|---|
| Make It Mean Something | 524 |
| Spontaneous Lamp | 618 |
| Sustainabilitist Principles | 679 |
| Structured Creativity | 857 |
| Drawdown Diptychs | 862 |
| Design the Future Today | 865 |
| The Libre Designer | 874 |
| Form, Content, Context | 901 |

Three were fixed, for two different reasons. **Design the Future Today** (3,264) and **The Libre Designer** (1,453) were carrying running material inside a pitch — 959 words of AI tooling in one, three full origin stories in the other. Both split into a `facilitator-guide.md`. **Form, Content, Context** (1,170) was never over-described; its bibliography was 29% of the sheet with an annotation per entry, now in `reading-list.md`. Nothing deleted in any of the three.

The three shortest have room for an image. The four in the 850–900 band don't.

---

## SURFACES.md — new, and the loose end worth chasing

Maps each project across its other homes: case studies on `a.wjerk.shop`, the wiki, are.na.

**are.na was never connected.** Two channel URLs recoverable from the material (`free-libre-open-design`, `libretype`). Two more are named out loud in the January 2025 transcripts with no URL recorded — including a copyright/book-references board that belongs to workshop #1. Those need retrieving from the account; nothing in the repo can recover them.

**Four of nine case studies are linked.** The unlinked five include the two the booklet has been waiting on — `OUTLINE.md` says Ecovention Europe and the MICA Grad Zine "still need a home," and both are finished published case studies (`twobooks`, `micagradadmissions`). That note now points at them. Also unlinked: Chair-ness (despite `chair-case-studies.md` existing), Solarpunk Boombox (the object that would anchor the unwritten Solarpunk lecture), and Carbon Sequestering Book.

---

## Day two — are.na, and the loop model

Wrote `scripts/arena-channels.py` against the v3 API (spec: `~/Code/sentence-a-day/openapi`; token in a gitignored `.env`; Cloudflare rejects urllib's default UA with error 1010, so the script sets its own).

**518 channels**, already organized in a taxonomy nobody had written down: `Lecture:`, `Workshop:`, `Project:`, `Shirt:`, `§` sustainability, `£` libre, `Wjerk:`, `BRN:`.

Found: `Lecture: What is Design?` with 67 blocks, for the slot with no material here. Both lost channels — the fonts one is `£ LibreType`, the copyright one is `Workshop: Copyright & a New Design Commons` (224 blocks). Two lectures existing only as private channels, Kintsugi and Mending Nets, both about repair. Five channels feeding `lecture-time-speed-motion/`. `§ The Sustainabilitist` at 2,957 blocks. A stale URL in `Why Libre Design.txt`, corrected.

Then the model Kristian described: lecture → shirt → workshop, each tied to a case study or to bjornpaedia, forming loops. Six surfaces total, including `stuff.wjerk.shop` (the `~/Code/shirts` repo). Coverage table for 23 topics is in `SURFACES.md`.

Headline: **the shirt leg is nearly absent**, and the two that exist are the two most definitional ideas — the shirt is functioning as a compression test. Nothing has all six surfaces; Libre Designer and Sustainabilitist Principles have five and are one shirt short.

## Started, then stopped — the tiddler migration

Chunking lectureScripts material into bjornpaedia tiddlers. Converter written and dry-run tested; **nothing written to `sentence-a-day`**, which is still clean.

The question — small reusable chunks vs. one long essay — is answered by Kristian's own 2021 work: chunks, assembled by transclusion, 100–200 words each. 92 tiddlers already use the pattern.

Full plan, the format spec, the collision problem, and the recommended order: `sessions/NEXT-tiddler-migration.md`.

## Day two, later — Pure Content, and a case study shipped

**"Pure Content" turned out to be the biggest thing in the archive, and this repo knew nothing about it.**

`Lectures To Writeup.txt` listed it under General. I first marked it "nothing anywhere." Wrong twice over. It is (a) the organising principle behind everything else here, and (b) already written — **~5,300 words across nine tiddlers** in bjornpaedia, tagged `CAPE` / `[[Pure Content]]` / `Writing`, chunked and hub-linked in exactly the pattern the migration plan proposes. `What is CAPE?` at 2,264 words is probably the conference talk itself — **Web Archives 2015: Capture, Curate, Analyze**, University of Michigan, 12–13 November 2015.

Kristian's definition, in his words: pure content is the abstract concept powering CAPE — publishing everywhere required structured content *"that didn't try to imply too much (or at all) what it should look like or be used for."*

**The symmetry worth writing up:** Pure Content and Signs Signaling on Substrates are the same claim in two domains. Both say the carrier is variable and the thing carried is fixed — rendering vs. content in one, substrate vs. signalling intent in the other. A decade apart, neither written as a lecture. Logged in `SHARED-COMPONENTS.md`.

### What got built

- **`scripts/tiddlers-to-md.py`** — inverse of the md-to-tiddlers converter. Renders a set of tiddlers into one markdown document.
- **`lecture-pure-content/`** — README plus `compiled-from-tiddlers.md`, all 5,272 words. **Marked generated, do not edit.** The tiddlers stay canonical; this is a rendering. Copying the prose in would have been the exact drift this repo spent two days documenting, and the material argues against it.
- **`a.wjerk.shop/case-study-cape.html`** — written, built, and pushed. 1,127 words, text-first, slotted into the case-study ring between The Libre Designer and Drawing on Tempered Glass with both neighbours rewired and an index tile added. Build verified before pushing: assembles clean, tokens resolve, 1.11 MB.

### Two facts that made the case study

**Sunday's Energy was their own company, not a client.** Kristian went looking in 2006 for a way to run a car on something other than diesel, found a Minneapolis group running biodiesel workshops and engine conversions, ended up working there, then ran it with Kai Curry. They made biodiesel, websites, and assorted eco-things. The websites paid for the biodiesel, and building sites for organisations with no CMS budget is what produced CAPE. Constraint first, philosophy afterward.

**The nineteen-year test.** `Better Living Through Sustainability`, his own site c.2007–2010, was built on Drupal, later archived as static HTML, and now lives as tiddlers in bjornpaedia transcluded into pages that didn't exist when it was written. Three platforms, none of which the content was written for. He let the domain expire in 2026 after nineteen years. The writing outlived the database, the site, and the address — the only test of pure content that means anything, and not one you can run quickly. It was sitting in a tiddler.

### Duplication found

Four separate inventories of are.na now exist: `a.wjerk.shop/arena-inventory.md`, `a.wjerk.shop/connections.md`, `sad2021tw/tiddlers/All Are.na Channels.tid`, and this repo's `SURFACES.md`. **`connections.md` is the best of them** — it models the concept rather than the project as the connecting unit, gives channels a role, and is headed for `connections.json` stamped at build. SURFACES.md now defers to it at the top. Consolidate to one before adding anything else.

## Threads left open

- The genus half of "What is design?" — undrafted, material located.
- ~~are.na URLs~~ recovered, both. See `SURFACES.md`.
- The shirt leg: two shirts would complete five-of-six loops (Libre Designer, Sustainabilitist Principles).
- **The tiddler migration** — see `sessions/NEXT-tiddler-migration.md`. Tool is built, order is decided, nothing written to the wiki yet. Read the nine CAPE tiddlers first; they're the finished example.
- ~~Which conference~~ **FOUND**: Web Archives 2015: Capture, Curate, Analyze, University of Michigan, 12–13 November 2015.
- **Screenshots for the CAPE case study** — one hero, one index tile (`i/cape-dither.png`, 800×450). Two marked TODOs in the HTML with the SPEC.md §3 requirements inline.
- **Consolidate the four are.na inventories** into `connections.md`.
- A repair lecture — Kintsugi and Mending Nets are **image collections**, not argument research. Sourcing is already all public domain. No argument written yet.
- Five orphaned case studies with nothing drawing on them.
- Images for the menu and sheets.
- Fees — confirm current.
- The **"Chair project w/ Chris Attenborough"** Notion doc KB mentioned and didn't finish pointing at. Not looked at. Relates to `chair-case-studies.md` and the Chair-ness case study.
- `variations-pitch-booklet.md:120` and the Notion bio both still say "graphic and product design."
- Older files in the repo are still hard-wrapped; new writing isn't. Unwrapping them is one pass if wanted.
