---
title: The Nineteen-Year Test
subtitle: What happened to pure content
status: draft — written 2026-08-27, never delivered
lineage: third version. "Towards Purer Content" was given twice — the Bunting Teaching Fellow presentation at MICA (spring 2015) and Web Archives 2015, University of Michigan (November 2015). This is the version you can only give now.
sources:
  - 2015-WebArchives-paper-proposal.md
  - 2014-medium-framing-note.md
  - CHRONOLOGY.md
  - compiled-from-tiddlers.md
note: Sections map to chunk tiddlers. Written that way on purpose — see sessions/NEXT-tiddler-migration.md.
---

# The Nineteen-Year Test

## I let a domain go

In 2026 I stopped paying for betterlivingthroughsustainability.com. I had paid for it for nineteen years.

The site was mine, roughly 2007 to 2010. It ran on Drupal. Later I archived it as flat HTML. The writing in it now lives in a wiki, where it gets pulled into pages that did not exist when I wrote it.

Drupal, then static HTML, then a wiki. Three systems. The content was written for none of them.

That is the whole talk. Everything else is how it happened and what it cost.

## What I said in 2015

I gave a paper called "Towards Purer Content" at a web archives conference at the University of Michigan. Before that I gave it at MICA, as a teaching fellow, and before that it was a pile of blog posts. The argument was short.

The end form should decide the style. Style should never be baked into the content.

Keep the content structured and keep it style-less. WYSIWYM instead of WYSIWYG — what you see is what you mean, not what you get. Add simple metadata. Imply the structure semantically. Then feed that content to whatever needs it, and let the destination decide what it looks like.

I wrote this at the time:

> The common tools we use are ill-suited for un-styled content creation. Word processors wrap text in formatting hard to remove for use in other contexts. Desktop publishing platforms lock content into layout files incompatible with other workflows. WYSIWYG tools bloat content with impure markup making content there hard to reuse or migrate. This impure content withers and dies, chained into a file format, storage method, or self-imposed style prison.

I was talking to a room of archivists and librarians. They already knew. They deal with content that has to outlive its system as a job, not as an opinion.

## The booklet

The problem that started it was dull.

A conference had a website with a database of sessions, speakers, and times. The same conference had a printed programme, which was an InDesign file. Every time the website changed, somebody re-typed the change into InDesign.

Two documents. Same event. Neither knew the other existed.

So we generated the booklet from the database. XML into InDesign, where the tags already carry the structure and the paragraph styles share the tag names. Change the website, re-run it, get a new booklet.

If a booklet can come out of the content instead of being copied from it, so can a web page, an email, a widget, a poster. The only requirement is that the content stops carrying assumptions about where it ends up.

## CAPE

Kai Curry and I built this for about a decade, starting in 2011, out of a company we ran that made biodiesel and websites. We called it CAPE: Create Anywhere, Publish Everywhere.

The idea was not that you should change how you work. Stay on Flickr. Keep the spreadsheet. Write in whatever you write in. We wanted a layer that would collect all of it and make it reusable.

Half of it searched across content feeds — anything with an API or an RSS feed. You defined sources, filtered, saved the query. A saved query was a live feed.

The other half turned those results into things. XML, JSON, templates, a page, a site, a booklet. It watched for changes and regenerated what was affected. Static files, no database at request time.

We used Markdown, XML, JSON, YAML — whichever suited the tool in front of us. The rule was to stay as close to plain text as we could, so the content was easy to edit and easy to move. Then we added metadata wherever we could attach it without wrapping the content in something, so a thing could be linked and adapted later.

Plain text is not a preference. It is the only format I have watched survive four migrations without anyone maintaining it.

The software was open source. The way we assembled it for a given client was not. The parts were free and the work was the assembly, which is how open source has always paid for itself.

In 2011 we thought we were geniuses.

## What happened

Most of this is ordinary now. Contentful sells content as an API. Drupal and WordPress run headless. Static generators pull from remote sources without anyone arguing about it.

We were early, which is a mixed thing to be. The ideas were right and we hand-built the tooling every time.

The part that did not become ordinary is print. Generating a press-ready document from the same source as the website is still unusual and still mostly hand-rolled. I have never understood why.

And then the ground moved.

CAPE ran on Flickr's API, Instagram's API, Dropbox, RSS. Instagram gutted its API. Twitter closed. RSS got quietly dropped by the platforms that had carried it. The system did not fail. The commons it stood on was fenced.

That is worth saying plainly, because it is the same story as everything else I talk about. Tools get enclosed. Images get enclosed. Materials get enclosed. The plumbing of the open web got enclosed too, and almost nobody called it that at the time.

## What survived

The domain is gone. The Drupal install is gone. The company is gone. The static site generator we customised is abandoned. Flickr's API is a shadow. I could not rebuild CAPE today from its original parts.

The writing is fine.

It has moved four times and it is still legible, still searchable, still reusable. Not because I was careful with backups. Because it was structured and not styled, and every move was therefore a rendering rather than a rescue.

That is the test. It takes nineteen years to run and you cannot shorten it.

## The same argument, four times

I have made this argument in four places without noticing it was one argument.

- **Pure content** — do not let the format own the writing.
- **CAPE** — do not let the tool own the content.
- **The libre designer** — do not let the vendor own the practice.
- **Signs signaling on substrates** — do not let the medium own the design.

Tool, format, medium, substrate. Four carriers, one instruction: do not be defined by the thing that happens to be carrying you.

Libre and CAPE look opposed. Libre says the tool matters, so choose one you can leave. CAPE says use whatever you like, we will get the content out. They want the same thing and they cover each other. Libre cannot help when a client hands you the tool. CAPE cannot help when the format has no exit.

CAPE only works if the formats are open, the APIs are documented, and the structures are published. It was a libre position the whole time. I just did not say so.

## What I would tell you to do

Write in something a text editor can open.

Put the structure in the content, not in the layout.

Publish where you control it, then syndicate, and make the copies point home. Do that even when it seems unnecessary. The originals are what disappear.

Assume every platform you use will close, get bought, or quietly stop caring about the thing you rely on. This is not pessimism. It is the observed behaviour of every platform I have used since 2007.

And check your work in twenty years. That is the only version of this talk that proves anything.

<!-- TO DO

DELIVERY
- Untested. Reads at roughly 12–15 minutes. Fine as a conference paper, thin for a full lecture slot — the obvious expansion is the print half, which is the one part still not commodified.
- Sections are chunk-sized on purpose. If this goes into bjornpaedia, each `##` becomes a tiddler and the lecture becomes an assembly tiddler with a `list:` field. See sessions/NEXT-tiddler-migration.md.

GAPS
- Formats now recorded (Markdown, XML, JSON, YAML, plain text, metadata wherever it would attach). Still unrecorded: the **implementation** — language, framework, host. Only you and Kai know that.
- The booklet is unnamed. Hopkins Conference Books, ICFP, and Print from the Browser are empty tiddlers referenced in These Gestures Are Undoubtedly Utopian, and are almost certainly the real examples. Name one and the print section gets teeth.
- rwdfoundation.org ran a custom Ruhoh. Worth checking whether it survives.

VOICE
- "In 2011 we thought we were geniuses" is yours, from the Medium note. Keep it. It is the only joke and it earns the section.
- The four-carriers list is the newest claim here and the least tested. It may be too neat. Say it to somebody before you say it to a room.
-->
