# Session — 2 September 2026

Started as "anything else good in my are.na channel?" for the futures lecture. Ended with a Figma extraction pipeline, twelve deck dumps tracked, a new section in the design-system repo, and one genuinely new idea.

Commits `48edd4d` → `fd1de0c` here, plus one in `~/Code/color-system-and-guidelines`.

---

## The idea worth not losing

**Peirce's index is why greenwashing works, and costly signalling is the mechanism.**

Peirce sorts signs by how they relate to their object: an icon resembles it (a leaf), a symbol means it by convention (the recycling triangle), an index is physically caused by it (smoke, a footprint). You can draw an icon of anything and assign a symbol to anything — both cost an afternoon. An index costs whatever the thing costs, because the thing has to have happened.

So greenwashing runs on icons and symbols. The recycling triangle is the whole case in one mark: a Möbius loop meaning *recyclable* wrapped around a resin code meaning *what plastic this is*. Nothing on the container is false, almost nobody reads it correctly, and a #6 clamshell nothing will ever recycle still gets to wear it. That is a connotation hardened into a fact — Barthes's **myth**, from the same lecture, arriving in a second place.

Two corrections that came out of pressure-testing it. Indices *can* be faked — distressed jeans, a molded weld seam, a stamped "handmade" — but that is forgery, a different act than design. And underneath sits **costly signalling**, reached independently by biology (Zahavi's handicap principle) and economics (Spence, Nobel 2001): a signal is trustworthy in proportion to what it costs to fake. So this is not an analogy between two lectures; it is a design-specific instance of a mechanism two other fields found separately.

Why it is a connection rather than a citation: `07-signs-signaling-sustainability.md` already ended its greenwashing section on *"a trope can be stolen, a value has to be enacted"* — the index argument without the vocabulary. The lecture gives the claim a name; the essay gives the lecture a payoff beyond a taxonomy of cats.

Written into three places: `lecture-some-semiotics/deck-outline.md` (§11), `booklet-new-design-commons/07-signs-signaling-sustainability.md` (Greenwashing), `SHARED-COMPONENTS.md`.

---

## What changed in the futures script

`2026-09-design-for-the-future-today-script.md`, roughly 18k → 23k:

- **Fisher moved to §1**, before Foster rather than after. Order now runs pictures → "basically mythologies and sci fi movies" → Fisher → Foster's three principles. §11 pays him off without restating, the same way Faulkner works.
- **Clarke swapped in for Dator in §3** — laws 1 and 2, dropped law 3. Law 2 is the edge-of-the-cone line stated as method; law 1 is aimed at whoever tells a student their project isn't feasible.
- **Dator relocated to §10**, next to the degree-project question where it actually lands. The four archetypes cut.
- **Kyle Whyte in §9**, after Prado & Oliveira. The dystopia already happened, and Whyte's Lawrence Gross citation — *Indians survived the apocalypse*.
- **Blauvelt in §4**, whose description of defuturing (a future that is only the present, extended) turns out to be §3's Projected band arriving from another direction.
- **Futurama opening §8** — GM's 1939 pavilion handed out buttons reading I HAVE SEEN THE FUTURE. Brand's 1966 button asked a question instead. Same object, opposite politics.
- **The cone mirrored in §3.** Physics draws a double cone; foresight kept the top half. Closes a hole §2 opens with Faulkner, and gives Hackett's plural pasts somewhere to live. Ends on *in physics you can't move the edge of the cone; in design that's the job.*
- **Physics distributed, not collected** — one sentence in §3 (the mirror), one in §4 (mixing is the second law, "entropy isn't advice"), one in §9 (everyone agrees on the cone, nobody agrees on where *now* is, so the vertex is yours). Quantum indeterminacy left out; it is interpretation-dependent and the other two are settled.
- **§9 Hackett rewritten** to make him and Bleecker one practice. Bleecker puts the artifact ahead of you, Hackett puts it behind you.

The §9 rewrite came out of KB's own correction: Hackett's images are **not** an alternate history, they are speculative pasts, fabricated now. Which means the cone drawing's second apex is *drawn, not found* — and the fake past never travelled through the present, it was manufactured at it. All the causation runs through the vertex, which is also what §10 says.

---

## The Figma pipeline

`scripts/figma-slides.py` — stdlib only, same shape as `arena-channels.py`. Dumps a Figma page to markdown: frames in canvas order grouped into section rows, every text run, `[hidden]` flagged. `--list-pages` enumerates a file. Retry with backoff, because Figma throttles a loop over 19 pages and four dumps silently vanished before that existed. Needs `FIGMA_TOKEN` in `.env`.

Default output shows the **delta** per frame rather than every text run, since these decks build by duplication and printing the carried-over lines buries the build. `--full` disables it.

**The finding that justifies the whole thing: the decks run ahead of the scripts.** Three times in one evening the deck already held what the script was missing — finished Clarke and Dator slides benched in the futures deck, seven built Parsons & Charlesworth slides with no script text at all, and a semiotics icon/symbol demonstration (slides 503/505, "cat" in a grotesque then "Cat" whose C *is* a cat) sitting two sections earlier than the section that needed it. None of that was findable until something enumerated the frames.

Twelve of nineteen pages now tracked: five into the folder they belong to, seven into `decks/` with a README, two already placed earlier. Four administrative pages and a 330-frame scrap canvas deliberately skipped. `SURFACES.md` got a Figma section, which it had never had.

---

## `~/Code/color-system-and-guidelines`

Went in expecting to write `SLIDE-STYLE.md`. Didn't, because **RULES.md already has ~560 lines across nine `## Presentations:` sections** derived from 25 lecture PDFs 2010–2026 — full-bleed as a hard rule, the tilted opaque quote card, the `TYPE:` credit line, the talk-vs-teaching-support genre split. Nearly everything read off Figma was already documented, in more detail. (I had only read to line 200 and said otherwise; the correction is the useful part.)

What was actually missing was the **production layer**, now added as `## Presentations: how the Figma file is built` — canvas rows as sections, build-by-duplication, and **two** frame-naming schemes rather than one (`2 Future Cone 09` in three decks; bare numbers whose leading digits are the section, `000`/`100`/`2000`, in two others). Build-by-duplication appears in 15 of 19 pages and is absent from exactly the four administrative ones, which is a third genre beyond the existing split.

Also: the border-radius rule was **wrong as written** and got rewritten — it is about chrome (panels, buttons, dividers), not about scale, since the talk decks have always used large rounded quote cards. Roster gained Overpass and Pilowlava (both OFL) and **PicNic, which is not OFL** — it is under Velvetyne's CUTE licence, an ethical-use licence with conditions. Flagged rather than filed alongside, on a roster whose stated constant is the licence. NOTES.md logged the unreconciled deck-vs-kit colour question (kit says pink on warm gray; decks are black/white/grayscale with green marking "preferable").

Hidden frames deliberately left out of that section: per KB, hiding a slide means benching it from the current cut, not losing it.

---

## What's next

**Blocked on Kristian — one question.** Parsons & Charlesworth: which of their pieces *actually function* versus which are convincing props? That contrast is the entire reason they are not just more Dunne & Raby, and it blocks drafting the §7 passage. Everything else about them is researched and written into `lecture-design-for-the-future-today/examples-and-references.md`.

**Kristian's to do.** Record a test run of the semiotics lecture. Whisper it to a transcript (see the `reference-whisper-setup` memory — transcripts go to scratchpad, not the repo), then build the script against `lecture-some-semiotics/deck-outline.md`, which already carries the 13-section structure and the §11 work.

**Unbuilt in Figma.** The mirrored cone. §3 now describes a double cone the deck doesn't draw — one added frame in the existing `2 Future Cone` run.

**Open, low priority.**

- The Lost Cause sentence in futures §9 — whether the speculative-history-vs-revisionism distinction earns a line.
- `ham-kb-work-and-workshop` (149 frames) and `hopkins-mar-30-jana-s-class` (256) are full talks appearing nowhere in `Lectures To Writeup.txt`. Either they are versions of listed talks under other names, or the backlog is missing two.
- Eight reviewed-but-unused are.na candidates for the futures lecture, ranked at the bottom of `examples-and-references.md`.
- The futures band definitions are near-verbatim from the Christophilopoulos JFS paper in the are.na channel, uncredited. Same file has the fuller cone lineage (Taylor 1990 → Hancock & Bezold → Voros 2003).
