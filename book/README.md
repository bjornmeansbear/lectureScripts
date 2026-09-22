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
hand-tagging each chapter.* Three things actually do that:

**Mood** (`data-mood="essay"` or `"lecture"`) — computed per chapter from
second-person pronoun density and question-mark density (`assemble.py:analyze`).
High direct-address / high question density reads as spoken delivery
("lecture"); low reads as written prose ("essay"). Calibrated against
this booklet's own nine chapters, not guessed at: most of them still
carry their lecture-delivery voice and land as "lecture"; the polished
introduction and an unwritten placeholder land as "essay." The two moods
get different h1 rules (double vs. single), different paragraph shape
(indented run-in vs. block-with-air), and a raised cap on essay openings —
real book-typography registers, not decoration.

**Density** (`data-density="brisk"/"measured"/"dense"`) — from average
sentence length. Shifts leading and paragraph spacing. A chapter written
in short declaratives gets more air; one built from long sentences gets
tighter leading, because it needs the density to keep momentum.

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
3. **Chapter** — the mood/density-driven template above. Running head
   shows the chapter title (left) and mood (right, small mono tag) via
   CSS `string-set`, so flipping through the printed book tells you at a
   glance which register you're in.

Recto/verso margins alternate so the gutter (bound edge) stays the wider
margin on both sides — real print-production detail, not just centered
margins.

## What the pipeline deliberately doesn't do

- **No invented typefaces.** The kit's rule (self-hosted OFL fonts only,
  system stack otherwise) applies here too. Mood/density differentiation
  comes from weight, spacing, and paragraph structure — not swapping in a
  display font nobody's licensed yet. `book.css` has the same commented
  `@font-face` hook as the kit's `print/print.css` for whenever one is
  chosen.
- **No auto-resolving "canonical-elsewhere" chapters.** `04-copyright-and-the-commons.md`
  in the source booklet explicitly flags an unresolved editorial decision
  (trim the workshop framing vs. keep it, which of three overlapping
  drafts wins). The build renders a placeholder naming where the real
  text lives rather than guessing at edits that are the author's call.
- **No hand-picked chapter styling.** If a chapter's mood/density looks
  wrong, the fix is to look at why the text scores that way, or move the
  thresholds in `assemble.py:analyze` — not to special-case that one file.

## Files

- `build-book.sh` — orchestrates: `assemble.py` -> pandoc -> weasyprint.
- `assemble.py` — parses chapter frontmatter, computes mood/density,
  tags cross-references, builds the title page / TOC / part dividers /
  chapter wrappers into one Markdown file. Prints its analysis to stderr
  on every run — the procedural decisions are meant to be visible, not a
  black box.
- `book.css` — the print stylesheet. Restates a token subset from
  `~/Code/color-system-and-guidelines/kit.css` rather than importing it,
  same reasoning as that repo's own `print/print.css`.
- `book-template.html` — minimal pandoc HTML5 shell; all styling lives in
  `book.css`.
- `themes.txt` — the recurring-idea vocabulary. Edit this to change what
  gets cross-referenced.
- `output/` — gitignored. Built PDFs land here by default.

## Extending this

Point `build-book.sh` at any other chapter directory that follows the
frontmatter convention — a different booklet, a set of essays pulled from
`sentence-a-day`, a future lecture writeup. The mood/density/cross-reference
machinery doesn't know or care where the chapters came from.
