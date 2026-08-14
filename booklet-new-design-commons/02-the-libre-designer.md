---
title: The Libre Designer
part: One — The Tools Commons
status: drafting
sources:
  - theLibreDesigner.md                                                    # root — structured outline, the spine
  - workshop-open-source-design/The Libre Designer (transcript).txt
  - workshop-open-source-design/Libre Designing (transcript).txt
  - workshop-open-source-design/MICAGD Summer Camp Libre Graphics (transcript).txt
  - workshop-open-source-design/FLOSS Regularly.txt
---

# The Libre Designer

I got here through a budget problem.

I was designing publications with no art budget. Not a small art budget — none. No stock photos, no hiring a photographer. So I went looking, and found public domain and Creative Commons images scattered across the internet. That was a practical fix for a practical constraint, and it turned into an ideology later.

The other route in was Drupal, in 2006. People all over the world building modules together, free to download, free to use however I wanted. Later, thinking about sustainability, I read *How Buildings Learn* and noticed that Stewart Brand's account of vernacular architecture — small fixes, copied down the block, adapted over time — described how Drupal had evolved. Same process, different material.

The libre designer is a character I play. A utopian device, useful for showing another way. I don't fully live there. I'm writing this on an Apple laptop.

## Start with the pictures

Changing where your images come from is the easiest move available, for four reasons. It works with the tools you already have — nothing to install or reconfigure. You don't need anyone's permission. Often you don't even need new sources, just a different way of searching. And it clears a pile of copyright and contract problems you'd otherwise be carrying.

Places to start: Openverse, Flickr Commons, RawPixel's public domain section, the Public Domain Review, Archive.org and the Prelinger Archive inside it, the Noun Project, Undraw.

There's a design argument for this beyond cost and risk. Working from public domain material means you can't search "diverse office team high-fiving" and take the first result. Old material doesn't carry this month's visual clichés. It makes you build a meaning instead of borrowing one, and the work ends up looking like it came from somewhere.

## Then the type

A magnitude harder than images, but not much.

Some libre fonts are already on your machine. Adobe Fonts carries part of the Google Fonts library, so you can switch a few on without leaving the software you have. Google Fonts has gone hard at variable fonts, which means most newer families arrive with nine weights and italics. The old complaint that libre type means one thin weight and no italics is mostly out of date. Raleway launched from The League of Moveable Type with a single weight, got forked, and the version on Google Fonts now has nine weights, italics, and a display cut.

Where to look: Velvetyne, The League of Moveable Type, Open Font Library, UseModify, Badass Libre Fonts by Womxn.

The part designers underuse: you can get the source files. If the family you like is missing a character or a weight, download the UFOs and draw it. If a client needs a custom face, start from the closest libre thing and change it. SIL's fonts carry enormous character sets because SIL makes language materials for communities nobody else typesets for. That's a different set of priorities producing a different kind of quality.

## Then the software

This is the real chasm.

Frame it right or it won't work: these are not replacements. They are alternatives. They do things differently and you can arrive at the same place — a well-made graphic object.

Start with tools that have no proprietary equivalent, so you're gaining something instead of giving something up. Drawbot. Nodebox. Processing. OBS. There's no Adobe app that does what these do.

Then the rest, when you're ready: Inkscape, Scribus, GIMP, Krita, Blender, Darktable, FontForge, Audacity, LibreOffice. ImageMagick and Ghostscript run in the background and in the terminal — hand ImageMagick a PDF and get back a folder of JPGs.

## File formats are the sleeper argument

SVG is an open standard that works in print and on the web. Illustrator reads it. Figma reads it. It's also XML, so a text editor reads it.

That holds across the ecosystem. A Scribus document is XML. You can open it in a code editor, see what's happening, add a page by hand, save it, and reopen it in Scribus. Try opening an .ai file the same way.

This is what you're buying: the ability to fix your file without the company that made it.

## Machines, and the ones you already have

GNU/Linux runs on almost anything, from a Raspberry Pi to a mainframe. That means an old laptop that can't handle a current version of Windows is often perfectly good with a current Linux on it. My old ThinkPad is useless for contemporary Windows and completely usable otherwise.

You should be able to fix your computer. You should be able to change it. That's getting harder everywhere, and Apple is the worst offender — proprietary parts, trackpads that Linux kernels struggle to talk to, security chips that make the newest models nearly impossible to liberate.

And there's a design point buried here. A designer should have some say in how their studio works. On Linux you pick the desktop environment, the icons, the interface type. You can design the thing you design inside of.

## Liberate the practice

Images, type, tools, machine. Then the work itself.

1. **Share your process.** Successes and failures, and probably the failures more. Name who you took from.
2. **Share your source files.** Documentation is better. Files alone still let someone open them and learn.
3. **Use text-editable formats where you can.** Easiest to work with, easiest to version, easiest to preview on the real system.
4. **Collaborate.** Design keeps insisting on the singular visionary. That's partly design history's fault.
5. **Donate.** Work that didn't get used can go to the public domain instead of a dead folder.
6. **Contribute.** Make examples for a type designer whose font you use. Build a site for a project that needs one. Answer design questions in an issue tracker.

## Why designers don't

Won't get credit. Pride. Not wanting anyone to see how the sausage is made. File formats. Tooling. Fear of design by committee. Greed, sometimes — I might sell this. Mostly, no particular desire to.

None of these survive much scrutiny, and the benefits are good enough that staying out looks foolish.

Here's the part I'd rather leave you with. Desktop publishing was shaped by about eight people in the early 1980s, for a small Macintosh, and most of those decisions are still sitting in your dock. Designers are supposed to be the people who make interfaces. Almost all of us use the same software on the same machines, which gives us a very narrow sense of what an interface can be.

There are tools out here that don't exist on a Mac. That alone is worth the trip.

<!--
TO DO:
  - Cut the tool lists down further? Right now they're bare lists per the reference-cluster
    rule, but a booklet might want fewer names and more reasoning.
  - The content warnings from the source ("I will be derogatory towards neoliberalism")
    are funny live and don't survive on the page. Left out — check you agree.
  - The Knuth/TeX/Metafont anecdote is in the source and got cut for length. It's a
    genuinely good origin story for design people specifically. Reinstate?
  - "What's hard / what's bad" section in the source is honest and mostly missing here.
-->
