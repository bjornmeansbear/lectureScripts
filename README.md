# Lecture Scripts

Lecture and workshop material, one directory per topic.

- `lecture-*` — a talk and its drafts, transcripts, and exports
- `workshop-*` — a pitchable workshop, its source material, and its license
- `booklet-new-design-commons/` — nine essays drawing on both; sources stay where
  they are and get cited by path, never copied in
- `SampleSlides/` — the NodeBox sketches behind the 2020 slide-title type tests (the
  rendered SVGs are in Dropbox, see below)
- `SHARED-COMPONENTS.md` — the ledger of what's reused across more than one of the
  above. Read it before starting a new write-up.
- `SURFACES.md` — where each project also lives: published case studies on
  `a.wjerk.shop`, notes on `bjornpaedia.wjerk.shop`, are.na channels. Check it before
  writing something that may already exist in finished form.
- `MENU.md` — the à la carte menu of bookable lectures and workshops.
- `projectWriteups/` — one pointer file per project: where its drafts, notes, and research live, and what's next. Update it whenever you put something somewhere. See its README.

Root used to be a flat pile of drafts. It isn't any more — if you add something,
put it in a directory.

## License

Writing and graphics are CC BY-SA 4.0. Code (NodeBox `.ndbx` files and the scripts) is GPLv3. See [LICENSE](LICENSE) for what that covers. The per-directory LICENSE files in the workshops match the CC BY-SA terms.

## Images and big files

Git holds text: scripts, notes, and deck source (HTML decks are text too). Big visual files go elsewhere, and the repo says where.

| Thing | Where |
|---|---|
| Scripts, notes, HTML deck source | here |
| Other people's images (Unsplash, Flickr, Are.na) | an Are.na channel per deck, plus the credit in the deck. The deck's `images/` folder is a gitignored cache, rebuilt with `commons` / `fetch_arena` in `color-system-and-guidelines/tools/`. |
| My own photos, artwork, big renders | `Dropbox/2 Teaching/lectureScripts-files/`, same folder names as here |
| Exported PDFs | one per talk, the current one. Old versions don't need keeping. |
| Old Scribus or PDF-only decks | leave them as they are. Rebuild one as an HTML deck only when giving that talk again. |

Images get credited where they're used. `lecture-systems-thinking/IMAGES.md` is the example.

## Open

- The old SVGs are still in git history (the reason `.git` is about 120 MB). Removing them means rewriting history and force-pushing. Do it once both computers have pushed everything, and re-clone on the other one after.
