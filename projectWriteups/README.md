# Project pointers

One file per project, saying where its pieces live. A file here is a pointer, not a write-up: a line per location, no prose copied in. The writing lives where it will be published.

## What goes here, and what doesn't

The other maps track **finished, public** things:

- `~/Code/a.wjerk.shop/connections.json` — the published links (live, shop, essay, are.na) that the build stamps onto each case study
- `~/Code/a.wjerk.shop/connections.md` — the concept map, and why each link exists
- `../SURFACES.md` — which of the six surfaces each topic reaches

A pointer file tracks the **working** state those don't: drafts, notes, half-gathered research, decisions made along the way, and what's next. When something gets published, record it in `connections.json` and replace the line here with “see connections.json”. Don't keep the same fact in two places.

## Naming

`<slug>.md`, using the same slug as the case study (`case-study-<slug>.html`) and its key in `connections.json`. A project with no case study yet gets a descriptive kebab-case slug, which the case study should then take.

## Shape

```
# Title
slug · status in one line · updated YYYY-MM-DD

## Where things are
- what — path or URL (repo-relative paths are prefixed with the repo: `sentence-a-day/otherIdeas/…`)

## Decided
- one line each, dated

## Next
- the next concrete step, not a wish list

## Log
- YYYY-MM-DD — what was put where, newest last
```

## The rule

Whenever a session creates, moves, or publishes something for a project, update its pointer in the same session: add the location, append a log line, bump `updated`. If there isn't a pointer yet, make one.
