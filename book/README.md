# Book pipeline

Turns a directory of chapter `.md` files into a print-ready book PDF —
6in x 9in trim, no bleed. Started from `booklet-new-design-commons/` (nine
lecture-derived essays already sitting in this repo) but works on any
directory that follows the same convention.

```
./build-book.sh CHAPTERS_DIR "Book Title" "Author Name" [output.pdf]

./build-book.sh ../booklet-new-design-commons "A New Design Commons" \
    "Kristian Bjornard"
```

Requires `pandoc` and `weasyprint` — same toolchain as
`~/Code/color-system-and-guidelines/print/md2pdf.sh`, same reasoning
(see that repo's `RULES.md`, "PDF generation"): plain text in git,
diffable, rebuilds without a browser, no page-layout GUI to fight with.

On macOS: `brew install pandoc pango` then `pip install weasyprint`.
`build-book.sh` already sets the `DYLD_FALLBACK_LIBRARY_PATH` WeasyPrint
needs to find Homebrew's pango (same fix as that sibling `md2pdf.sh`),
so you shouldn't have to touch your shell env yourself.

One real visual difference to expect: `--font-text` is Liberation
Serif, which is preinstalled on Linux but *not* on macOS (it's not an
Apple system font), so the body copy will silently fall back to Georgia
there instead — the next name in the stack, and a perfectly good serif,
just a different one than what any PDF built on Linux shows you. Not a
bug, just a font-availability gap. Fixed permanently by self-hosting a
chosen OFL serif via `@font-face` in `book.css` (same hook the kit's own
`print/print.css` uses) — worth doing once you've picked one, rather
than living with whatever's on a given machine.

Optional: `brew install poppler` gets you `pdfinfo`, which
`build-book.sh` uses only to print the page count at the end — the build
works fine without it, that line just goes blank.

## What a chapter directory needs

Each chapter is `NN-slug.md` (numeric prefix sets reading order) with the
frontmatter this repo's essay directories already use:

```
---
title: Chapter Title
part: One — Some Part Name
status: drafted
---

# Chapter Title

Prose...
```

`status: canonical-elsewhere` (with a `canonical: path/to/real/file.md`
field) renders as a short, honest placeholder instead of guessing at
content — see "What the pipeline deliberately doesn't do" below.

## What's procedural here, and why

First version of this made every axis continuous — a chapter's numbers
came from lerping between two invented endpoints, and no chapter fell
into a named bucket. That was wrong in a specific way: a continuous dial
can only ever produce dial-sized differences. Turning a knob doesn't
make a different machine. What actually reads as "different and
meaningful" — the actual brief — is a different *system*: different grid
logic, different alignment, different relationship between type and
page. Brockmann and Manutius don't differ by a margin setting; they
differ by everything.

So the top-level choice is now discrete, and it isn't invented: every
chapter gets assigned one of two real, historically-grounded typesetting
systems (`compute_visual_params` in assemble.py), built out in book.css:

- **Manutius** (the Aldine press, Venice, ~1495-1515) — justified,
  hyphenated, tight, serif, single narrow column, every paragraph
  indented with no added vertical margin. This booklet's default: mostly
  discursive essay.
- **Brockmann** (Swiss International Typographic Style — Emil Ruder,
  Josef Müller-Brockmann, ~1950s-60s) — strict grid, flush-left/
  ragged-right (no justification, no hyphenation — Ruder and
  Müller-Brockmann both argued justification distorts natural word
  rhythm), sans-serif, hierarchy from weight alone, a large pink
  grid-module numeral as the one structural flourish. Picked for chapters
  that read as more instructional/enumerable than quotation-or-citation-
  laden — ch. 08's "Require libre fonts.", "Constrain the image sources."
  is the clear case; see `data-template` selection logic below.

Five metrics still modulate *within* whichever template a chapter gets —
this is where "the content decides the details" from the first version
still holds, it just no longer decides the system itself. assemble.py
normalizes each metric against this book's own min/max and writes the
resulting value straight into the chapter's `<section style="...">` as a
literal CSS custom property — `--leading: 1.251`, not `data-density="measured"`.
book.css only does `var()` lookups; there's no `calc()` combining two
`var()`s anywhere (WeasyPrint's calc() silently no-ops on that — hit it
once, see the comment on `h1_size_rem`), so every number in the PDF
traces back to one line in `compute_visual_params`.

Five axes, each owning a channel the others don't touch:

**Direct address** — second-person pronoun density + question density.
Drives the h1 rule weight (heavier for written) within Manutius (Brockmann
has no rule at all). Does *not* touch paragraph indent or spacing —
indent-run and block-with-air are two different, mutually exclusive ways
of marking a new paragraph, not two ends of a dial, and blending them
continuously used to leave a paragraph with both a partial indent and a
partial gap at once, which is neither convention, just wrong. Manutius
paragraphs always indent with zero extra margin; Brockmann paragraphs
never indent and are always separated by a full line (margin-bottom
equal to leading, not a fraction of it — see Sentence rhythm).

**Sentence rhythm** — average sentence length. Drives leading
(line-height); in Brockmann, also sets the exact paragraph gap (one full
line-height, so it reads as a real line-return rather than a sliver).

**Chapter length** — word count relative to the book's own range. Drives
h1 size: short chapters get a bigger title treatment than long ones.

**Instructional density** — `**Bold-lead**` paragraphs (ch. 08's "Require
libre fonts.", "Constrain the image sources.") per 1000 words. This is
also half of the **template decision**: a chapter scoring higher on
instructional density than apparatus density (below) gets the Brockmann
template. Within a chapter, it also colors and underlines that leading
bold phrase, continuously, from barely-there to fully accented — on
Manutius chapters only; Brockmann's own rule (bold, no color) overrides
it, because a colored label is a classical-register flourish, not a
Swiss one. Known limitation: the regex can't tell a short label from a
long bolded thesis sentence — ch. 07 has one of the latter and it gets
label-styled too. Text-only heuristic; live with it or refine the regex,
not worth NLP for this.

**Apparatus density** — footnote references per 1000 words *plus*
blockquote share of the chapter (both signal "this chapter leans on
outside material"; footnotes alone are too sparse in this still-drafting
booklet to mean much on their own — most citations are still marked
`[CITE — ...]` in the source). This is the other half of the template
decision (see above). Within a Manutius chapter, it also still drives
outer margin width: sparse-but-not-quite-Brockmann apparatus gets a
tighter margin, denser gets a wider one held in reserve for that
apparatus — Tufte-style marginalia space, not filled in yet, but the room
is there. Brockmann's margin is fixed instead (the grid is structural,
not content-driven, and a Brockmann chapter is low-apparatus by
construction anyway). Margins are a page-box property, not something a
CSS custom property on an element can reach, so this is the one axis
that needs a second generated file — assemble.py writes
`OUTPUT.md.pages.css` with one named `@page ch-page-NN` per chapter, and
`build-book.sh` passes it to weasyprint as a second `--stylesheet` after
`book.css`.

**Recurring ideas** — `themes.txt` lists phrases known to recur across
chapters (grounded in `OUTLINE.md`'s own cross-reference notes, plus
terms confirmed by grep to actually repeat — not invented). The first
time a phrase appears anywhere in the book it's left alone; every later
chapter that uses it again gets **one** marked recurrence, turned into a
link back to the chapter where it started. `book.css` renders that as a
small arrow plus the *actual printed page number* of the origin, computed
at render time via WeasyPrint's `target-counter()` — not hardcoded, not
approximated. Same mechanism drives the table of contents.

None of this needs a knob per chapter. Add a chapter file with the usual
frontmatter and it gets analyzed and slotted in.

## The page templates

1. **Title page** — book title, author. Full-bleed-free, centered.
2. **Part divider** — a quiet page whenever `part:` changes between
   consecutive chapters. No running head (there's no "current chapter"
   on a divider).
3. **Chapter, Manutius** — serif, justified, single column, every
   paragraph indented. This booklet's default register.
4. **Chapter, Brockmann** — sans, ragged-left, two-column grid, a pink
   grid-numeral, paragraphs separated by a full line instead of an
   indent. The instructional-chapter exception.

Both chapter templates still carry a running head: chapter title (left)
and a discrete `WRITTEN`/`SPOKEN` register tag (right, small mono, from
the direct-address score read at a fixed threshold rather than its
continuous value — a running head has to be a short label, not a number)
via CSS `string-set`. That tag is independent of which of the two
templates the chapter got; it's a second, orthogonal readout, not a
duplicate of `data-template`.

Recto/verso margins alternate so the gutter (bound edge) stays the wider
margin on both sides — real print-production detail, not just centered
margins. Apparatus density can widen the *outer* margin further still on
top of that (see above).

## What the pipeline deliberately doesn't do

- **No invented typefaces.** The kit's rule (self-hosted OFL fonts only,
  system stack otherwise) applies here too. Body text is Liberation Serif
  (OFL, already installed everywhere WeasyPrint runs — no fetch, no
  setup); the five axes above differentiate chapters through weight,
  spacing, margin, and column count, not by swapping in a display font
  nobody's licensed yet. `book.css` has the same commented `@font-face`
  hook as the kit's `print/print.css` for whenever one is chosen.
- **No auto-resolving "canonical-elsewhere" chapters.** `04-copyright-and-the-commons.md`
  in the source booklet explicitly flags an unresolved editorial decision
  (trim the workshop framing vs. keep it, which of three overlapping
  drafts wins). The build renders a placeholder naming where the real
  text lives rather than guessing at edits that are the author's call.
- **No hand-picked chapter styling.** If a chapter's numbers look wrong,
  the fix is to look at why the text scores that way, or adjust the lerp
  bounds in `assemble.py:compute_visual_params` — not to special-case
  that one file.

## Files

- `build-book.sh` — orchestrates: `assemble.py` -> pandoc ->
  `group_footnotes.py` -> weasyprint (with both `book.css` and the
  generated per-chapter `pages.css`).
- `assemble.py` — parses chapter frontmatter, computes the five axes
  (`analyze` for raw per-chapter metrics, `compute_visual_params` for the
  corpus-normalized, final CSS values), tags cross-references, builds the
  title page / TOC / part dividers / chapter wrappers into one Markdown
  file, and writes the `.notes.tsv` and `.pages.css` sidecars. Prints its
  analysis to stderr on every run — the procedural decisions are meant to
  be visible, not a black box.
- `group_footnotes.py` — splits pandoc's one flat endnotes list back into
  labeled per-chapter sections (see its own docstring for why pandoc's
  output needs this).
- `book.css` — the print stylesheet. Restates a token subset from
  `~/Code/color-system-and-guidelines/kit.css` rather than importing it,
  same reasoning as that repo's own `print/print.css`.
- `book-template.html` — minimal pandoc HTML5 shell; all styling lives in
  `book.css`.
- `themes.txt` — the recurring-idea vocabulary. Edit this to change what
  gets cross-referenced.
- `output/` — gitignored. Built PDFs (and the generated `*.pages.css`/
  `*.notes.tsv` sidecars, which are temp files cleaned up by
  `build-book.sh`'s trap) land here by default.

## Extending this

Point `build-book.sh` at any other chapter directory that follows the
frontmatter convention — a different booklet, a set of essays pulled from
`sentence-a-day`, a future lecture writeup. The five-axis/cross-reference
machinery doesn't know or care where the chapters came from — it renormalizes
against whatever corpus you point it at.
