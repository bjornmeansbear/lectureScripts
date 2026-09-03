# Decks without a home

Markdown dumps of Figma pages that don't correspond to a folder in this repo —
teaching sessions, program talks, and guest lectures that were delivered but
never written up. Generated with `scripts/figma-slides.py`; Figma is source of
truth, so regenerate rather than edit.

A dump belongs in the lecture or workshop folder it supports (see
`lecture-design-for-the-future-today/slides.md`). These land here because there
is nothing to sit next to yet. **If one of them becomes a lecture folder, move
its dump in.**

| File | Frames | What it is |
| --- | --- | --- |
| `di-what-is-di-what-are-co-majors.md` | 50 | The DI program and co-majors, for students choosing one |
| `di-degree-plan-co-majors-too.md` | 87 | Degree planning, same audience |
| `gfd-file-types-and-how-to-use-them.md` | 43 | Teaching support — file formats and when to use which |
| `gfd-type-image-posters.md` | 45 | Teaching support — type and image in poster work |
| `ham-kb-work-and-workshop.md` | 149 | Visiting artist talk: own work plus a workshop |
| `hopkins-mar-30-jana-s-class.md` | 256 | Guest lecture, Johns Hopkins, Jana's class |
| `micawknd-risograph-workshop.md` | 20 | MICA Weekend risograph workshop |

Two of these look like the largest unwritten talks in the file. `ham-kb-work-and-workshop`
is a whole visiting-artist lecture; `hopkins-mar-30-jana-s-class` is 256 frames.
Neither appears in `Lectures To Writeup.txt` — worth checking whether they should.

## Not dumped

Four administrative pages in the same Figma file are not lectures and aren't
tracked here: `FEC: Jan 16 Faculty Meeting` (14 frames), `FEC: Feb 13 Strategic
Plan` (25), `FEC: Aug 21 Faculty Meeting` (32), and `CMP: Jan 29 Design and Media
Ideas` (248). Also skipped: `Pile of spreads, extras...` (330), which is a scrap
canvas rather than a deck.

Regenerate any of them:

```
python3 scripts/figma-slides.py "https://www.figma.com/design/ltomqlGJOWEk1NEu0T9LSr/x" --list-pages
python3 scripts/figma-slides.py "ltomqlGJOWEk1NEu0T9LSr <NODE-ID>" -o decks/<name>.md
```
