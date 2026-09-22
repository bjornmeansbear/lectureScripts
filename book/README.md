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
`pip install weasyprint` if it's missing.

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

The brief this was built against: *typeface and page template should
shift essay to essay, driven by the content itself, not by a person
hand-tagging each chapter — and every chapter should get its own numbers,
not one of a few presets.* So every axis below is continuous: assemble.py
normalizes each metric against this book's own min/max (`compute_visual_params`)
and writes the resulting value straight into the chapter's `<section
style="...">` as a literal CSS custom property — `--leading: 1.251`, not
`data-density="measured"`. book.css only does `var()` lookups; there's no
`calc()` combining two `var()`s anywhere (WeasyPrint's calc() silently
no-ops on that — hit it once, see the comment on `h1_size_rem`), so every
number in the PDF traces back to one line in `compute_visual_params`.

Five axes, each owning a channel the others don't touch:

**Direct address** — second-person pronoun density + question density.
Blends paragraph shape continuously between indent-run (written) and
block-with-air (spoken) — a chapter halfway between gets half the indent
*and* half the paragraph gap, not a switch between the two. Also sets the
h1 rule weight (heavier for written) and feeds the drop-cap size.

**Sentence rhythm** — average sentence length. Drives leading (line-height)
alone.

**Chapter length** — word count relative to the book's own range. Drives
h1 size and, jointly with direct address, drop-cap size: short chapters
get the biggest opening gesture, on the theory that a device this loud
would wear out over a long chapter.

**Instructional density** — `**Bold-lead**` paragraphs (ch. 08's "Require
libre fonts.", "Constrain the image sources.") per 1000 words. Colors and
underlines that leading bold phrase, continuously, from barely-there to
fully accented. Known limitation: the regex can't tell a short label from
a long bolded thesis sentence — ch. 07 has one of the latter and it gets
label-styled too. Text-only heuristic; live with it or refine the regex,
not worth NLP for this.

**Apparatus density** — footnote references per 1000 words *plus*
blockquote share of the chapter (both signal "this chapter leans on
outside material"; footnotes alone are too sparse in this still-drafting
booklet to mean much on their own — most citations are still marked
`[CITE — ...]` in the source). Drives the **page geometry itself**, not
paragraph styling: sparse-apparatus chapters that are also long enough get
two columns and a tight outer margin (maximize type per page); dense ones
get a single, narrower column with a wide outer margin held in reserve —
Tufte-style apparatus space, not filled in yet, but the room is there.
This is the one axis that reaches `@page` rather than the chapter
`<section>` — margins aren't a property an element's `style` can set, so
assemble.py writes a second file, `OUTPUT.md.pages.css`, with one named
`@page ch-page-NN` per chapter, and `build-book.sh` passes it to
weasyprint as a second `--stylesheet` after `book.css`.

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

## The three page templates

1. **Title page** — book title, author. Full-bleed-free, centered.
2. **Part divider** — a quiet page whenever `part:` changes between
   consecutive chapters. No running head (there's no "current chapter"
   on a divider).
3. **Chapter** — the five-axis template above, one or two columns.
   Running head shows the chapter title (left) and a discrete `WRITTEN`/
   `SPOKEN` register tag (right, small mono, from the same direct-address
   score but read at a fixed threshold rather than the continuous value —
   a running head has to be a short label, not a number) via CSS
   `string-set`, so flipping through the printed book tells you at a
   glance which register you're in.

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
