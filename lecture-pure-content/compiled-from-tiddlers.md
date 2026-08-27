# Pure Content — compiled from bjornpaedia

> **Generated file — do not edit.** Rendered from tiddlers in `~/Code/sentence-a-day/sad2021tw/tiddlers`, which are canonical. Regenerate with `scripts/tiddlers-to-md.py`.

Source tiddlers, in order: `Create Anywhere Publish Everywhere`, `CAPE`, `Towards Purer Content`, `What is CAPE?`, `Content is King`, `From Indesign to Pure Content`, `Decoupling content from its site`, `Striving For Static Sites`, `Extra Thoughts on CAPE`, `Pure Content`

---

## Create Anywhere Publish Everywhere

*tags: `[[Pure Content]] Writing` · modified: 20210619*

[[CAPE]] = Create Anywhere Publish Everywhere

## Ideas Explaining:

Create Anywhere Publish Everywhere is software, service, and philosophy. The way the contemporary web works increasingly focuses on linking together disparate and specialized services; not providing a single website with all solutions hardwired directly into the site proper. Create Anywhere Publish Everywhere accepts and embraces this new ideology. Create Anywhere Publish Everywhere uses standard formatting, hardware, software, services, and server technologies. However, the way in which these things are combined is often quite novel.

Create Anywhere Publish Everywhere is a service for connecting your services. Create Anywhere Publish Everywhere desires to provide an interface to control content — photos from Flickr, Instagram, Amazon S3, or Behance; documents from Dropbox, Google Drive, or Github; items from an inventory management system; Facebook Posts, Wordpress posts, content from your existing website — anything accessible via API, anything in an RSS feed, and anything otherwise publishable to the web (or cloud) in a common data format (XML, JSON, TXT, etc.). The goal: make your content work for you in more places.

Create Anywhere Publish Everywhere wants to rethink content creation and management. It is best to approach content creation in as pure a way as possible (meaning semantic, structural, meta-data rich content — not styled content). This makes it easy then for Create Anywhere Publish Everywhere to always map content from one place to another and easily template it for whatever use required.

---

## CAPE

*tags: `[[Pure Content]]` · published: <https://www.ookb.co/cape/> · modified: 20210619*

CAPE = [[Create Anywhere Publish Everywhere]]

## Idea Explaining:

---

## Towards Purer Content

*tags: `Essays [[Utopian Gestures]] [[Pure Content]] OnMedium` · modified: 20260707*

The end-form of the content should dictate the style — visual style should not be baked into the content itself. The content should remain structured, yet style-less ([[WYSIWYM]] over [[WYSIWYG]] [What-you-see-is-what-you-mean instead of what-you-see-is-what-you-get]). Structure must be semantically implied with simple meta data added to content. This structured, un-styled, meta data rich content can then be fed to whatever service, tool, program, etc. required for the display type desired.

We are not yet in this perfect world.

The common tools we use are ill-suited for un-styled content creation. Word processors wrap text in formatting hard to remove for use in other contexts. Desktop publishing platforms lock content into layout files incompatible with other workflows. [[WYSIWYG]] tools bloat content with impure markup making content there hard to [[Reuse]] or migrate. This impure content withers and dies, chained into a file format, storage method, or self-imposed style prison.

This does not have to be the case.

Purer content is achievable. [[Pure Content]] is able to evolve and live in different templates, different places, and migrate seamlessly between different future-friendly formats. There are a variety of ways that content can better conform to an idealized “pure” form that is more flexible and more future friendly than current options …

---

## What is CAPE?

*tags: `CAPE Writing` · modified: 20210619*

# CAPE
The way the web works will be increasingly about linking together disparate but specialized services; not providing a single website with all solutions pre-built or hardwired into the site itself. CAPE accepts and tries to embrace this new ecosystem.

## Create Anywhere, Publish Everywhere.
_CAPE has two basic parts._

The first part is to API content feeds as Google is to HTML pages: Users search across multiple content sources and are empowered to reuse or display found data in any way they choose. A user defines various content sources, creates a set of search filters, previews the results and saves the final query. Queries are live-updated content feeds, and the results can be removed, remixed, or saved. Saved results can also be re-ordered. Source feeds are not limited and can include public RSS and API data as well as private content created in a Dropbox folder or files from a Jekyll GIT repository.

The second part is CAPE’s use of the search results. Each query has a “saved” and “live” results feed. Currently query result feeds are available in XML, Json, or can be passed through mustache templates for a variety of use-cases.

A blogger or editor can search for tags across multiple sources (including personal ones) and then select the relevant content for a new post with a few clicks. The results can be turned into the actual HTML file or displayed in widget format on any page. Entire websites can be created this way based on a collection of saved queries and a set of display templates.

## CAPE Explained
CAPE uses existing and standard formatting, hardware, software, and server technologies. However, the way in which these things are combined is fairly novel.

_This is software, service, and philosophy in one._

As software, CAPE provides the potential for a backend to control all your content feeds — photos from Flickr or Instagram, text docs from Dropbox or Github, spreadsheets from Google Drive, even content from your inventory management system, basically anything that has an API, RSS feed, or otherwise publishes to the web (cloud) somehow can be found, captured, and reused.

Service-wise CAPE provides the option for linking together all your other services. Pick the existing products, softwares, services, etc. that already manage something — workflow tools, photo feeds, etc. — and then use what you are already familiar with to create the content for your website or even print. Instead of being a content management system, CAPE is a content curation and delivery service. (To clarify what “services” are: CMSs have modules or plugins, iOS and Android have apps, the Web has Services … (For more on this, [“There is a service for that”](https://github.com/sundaysenergy/www.sundaysenergy.com/blob/master/pages/static/service_for_that.md) contains references to many existing services providing all kinds of pre-built functionality.))

As a philosophy, CAPE says this: whatever you are already using for content management or creation, please continue to use it. CAPE just wants that content, and will find it, re-format it and deliver it where and how you choose. Mostly this requires thinking about what existing services do the tasks you require, what current jobs create and manage content within your office, and then how those can all be linked together in a sensical, methodical way.

## How CAPE can be used / Why CAPE is useful.
CAPE is beneficial for a number of reasons. 

That CAPE is a philosophy as much of a software/hardware decision means that it is mutable, iterable, flexible, and more future-proof than many other options. CAPE allows for working fluidly within existing company/organization workflows.

Content creation tasks can be broken up by who actually deals with specific kinds of content. These sub-divided creation tasks can be relegated to tools best and/or only suited to the specific tasks. This makes a creator/editor’s tasks simpler as new workflows, tools, concepts, etc. aren’t necessary. This also means that products and/or services best used for a specific medium can be used making each piece of a site — images, text, HTML, video, CSS, JS, whatever — hosted, served, managed, etc. in the most effective possible way.

Breaking down conceptually the way that the content is created, and then putting it back together at your discretion allows for a number of things traditional CMS driven sites don't  easily permit. 

### 1. Ease of Hosting.
Sites built on the CAPE philosophy are simpler, smaller, leaner, and faster to host. The “site” itself is made up of just a few HTML, CSS, JS, and media files as the majority of the content is being drawn in from elsewhere. Also, when new “pages” or “content” are created, they are actually turned into static HTML pages that load quickly and reliably. The entire site (excluding the third party services) can be hosted on a Content Delivery Network. A CDN provides redundancy, speed, and reliability beyond that of regular hosting models for PHP/SQL driven sites.

### 2. Speed.
CAPE doesn’t power a site like a traditional CMS does, it generates a site. CAPE lives in the background, listening for changes in feeds, services, or other content libraries. When it notices a change or new content CAPE creates any new pages, lists, menus, etc., corresponding to that change, update, or addition. 

If you need to load a page, the page is just there for loading, the server doesn’t need to ask a SQL database (or anything else) for said content and have PHP or another script/language compile the content into an HTML file. Also, because of the CDN possibilities, the closest, least-loaded server to a visitor can be used to serve the files, creating another speed gain.

### 3. Future-Proofness.
CAPE provides a way to link, display, feed, and control content from elsewhere. It does this using simple JS, HTML, CSS, and a collection of processing software snippets. Individually, these are all base-level, foundation technologies for the construction of web-pages. This is unlikely to change in the near future.

Because CAPE doesn't actually manage any content itself, only finds and displays content from elsewhere, your content can be migrated, moved, edited, etc. from whatever is the current best choice. This means that CAPE is able to evolve and flex as technologies advance, improve, or change all together. Being a philosophy more than a software allows for adaptability to be key.

### Additional “Why CAPE?” Arguments
_Some of these points reiterate the ones above, but are helpful to explain more specific benefits, or the same benefits in greater detail._

#### Performance
Content rarely changes. It is a complete waste of resources to load a database and software to handle the processing it into the final html markup. It's difficult to get higher performance than serving static files. Dynamic content can be handled with various third party javascript libraries. Ever get a notice from your host that your website is using too many resources? CPU or Memory issues will be gone forever when your site is statically cached.

#### Data Protection
Own your content. If you use a blogging service like Tumblr you should have a backup of all your posts. Do you? CAPE accepts various sources of information and stores them in plain text files. They are easy to edit anywhere and can be published everywhere.

#### Security
Serving static HTML is inherently safe. No server side scripts to get attacked, or abused. Anytime your site is being dynamically generated that software must be updated regularly or you are at risk for security vulnerabilities.

#### Focus on the content
Interfaces change, content remains. It's too difficult to have layout specific information in the content if you want to display the content in more than one place. The content needs to be **presentation agnostic**. One of the greatest things about the Web is its universality. Web-enabled devices are everywhere. Your content should be accessible from any device. A Content Management System should focus on **managing content** not displaying it. 

#### Responsive Design
The web is responsive by nature. Responsive design gets really difficult to accomplish when there are display rules mixed into the content. As it is impossible to test for all the possibilities we must try to design, code, and content-create for the flexibility and the unknown. By treating content as its own layer, removed from the presentation, we are better able to do this.

#### Versatility
Desktop applications, web applications, mobile applications. All devices can by sources of content. Why limit yourself to creating content in/on a single place/software focused toward a single device/context.

#### Don’t Repeat Yourself / Don’t Reinvent the Wheel
Don’t Repeat Yourself (DRY) is a principle of software development aimed at reducing repetition of information — all kinds of information. To reinvent the wheel is to duplicate a basic method that has already been created or optimized by others. CAPE helps website users and managers avoid these pitfalls.

## The problems with content management systems 

### Complexity and Cost
Using Drupal, Wordpress, or most other CMSs requires software to be running on a server to dynamically build each page request. Every time a user visits a page, the server has to build that page first. Every time. Every single time. The software that does this builds each page dynamically, and requires constant updates and has a lot of “moving parts.” The cost to keep all of those parts moving all the time is high. Therefore, the correlating cost to properly host a website like this is much more expensive than that of hosting static site. 

### Constraints on Content Creation
With a typical CMS, content can only be created via that website. The method for adding content was designed to be like a “desktop” type device that was connected to the internet. This approach was fine when everyone did everything on a desktop computer. But now content creators have all kinds of devices they like to use for content creation. A good example is the iPad. It’s clumsy editing content via a website, and it's a much nicer experience using a native app that is a content editor.

### Emphasis on WYSIWYG
WYSIWYG (What you see is what you get) editors are still the common means of editing content in most CMSs. Unfortunately, while they appear useful, they are mostly inefficient and ineffective. WYSIWYG editors created bloated content that contains not just the actual content, but a variety of presentational markup. This both makes the site slower to load and harder to reuse content in other places. It also can interfere with main styles and templates created for display. WYSIWYG works fine on your personal blog, but it isn’t optimal for dynamic, flexible, and responsive websites.

CAPE is more interested in WYSIWYM, or “What You See Is What You Mean.”

From wikipedia:

> In a WYSIWYM editor, the user writes the contents in a structured way, marking the content according to its meaning, its significance in the document, leaving its final appearance up to one or more separately WYSIWYG-authored style sheets. For example, in a WYSIWYM document a human being manually marks text as the title of the document, the name of a section, or the name of an author; this would in turn allow one element, such as section headings, to be rendered as large bold text in one style sheet, or as red center justified text in another, without further human intervention. This requires the semantic structure of the document to be decided on before writing it.[‡](http://en.wikipedia.org/wiki/WYSIWYM)

This allows for CAPE sites to have textual, image, video, and whatever other content separated from each other allowing a much easier chance for reuse, repurposing, and optimized management dependent on the content or media type. The content then only displays in the ways you have asked or told it to.

### CMSs are Slow and Complicated
You’ll only be as good as the mean of those around you. The Drupal community is home to many semi-developer freelancers. Drupal enables a ton of functionality without being a programmer. Need some added functionality? There is more than likely a module for that. A module that could have been written for a specific job and the maintainer is no longer getting paid to work on it. Wordpress has a similar community and thus a similar set of problems. CAPE avoids this by interfacing with standard, up-kept tools. If a new, better tool comes along (or better maintained tool), it can be swapped in for the old one.

### CMSs are good for two main groups
# Small scale site builders who can leverage the power of SQL Views, Fields, and the rich module ecosystem (in Drupal, or the general plugin system of Wordpress) but aren't building sites complex enough to land them in “maintenance hell.”

# Large organizations with small development teams that need a complex content/user model. Drupal does a good job of content modeling, revisions, localization, and has a decent plugin system. It also is useful in managing a large user base. Wordpress does not easily handle overly complex content models, so should be avoided here anyway. Some other CMSs besides Drupal can handle the complex side of things as well. 

## Glossary

- API: Application Programming Interface
- CAPE: Create Anywhere, Publish Everywhere
- CDN: Content Delivery Network
- CMS: Content Management System
- CSS: Cascading Style Sheets (contains layout and design instructions) 
- HTML: HyperText Markup Language (the basic structural code of web pages)
- JS: Javascript
- JQuery: A javascript library of pre-built functions to help simplify and extend basic behaviors for the web.
- WYSIWYG: What you see is what you get
- WYSIWYM: What you see is what you mean

---

## Content is King

*tags: `CAPE [[Pure Content]] Writing` · modified: 20210619*

Publishing is about content. Getting content to where you need it. Getting it into the form you need it. Content needs structure. It needs hierarchy. However, the end-form the content takes should dictate the style. Content should remain structured, yet style-less.[^1]

In a perfect world, blank, structured, meta-data rich content is fed to whatever service, tool, program, etc. desired and then is picked apart and displayed whatever way is best. We are not yet in this perfect world. Content is not created in this clean, pure way. Writers write, editors edit, designers design, developers develop, creators create — a soupy process of back-and-forth ensues. Since each type of “creator” has their own set of tools, the revisions, changes, updates, etc. that happen all flow across emails, different documents, and different programs and are not always easily manageable, trackable, or cross-compatible. This does not have to be the case.

It isn’t always known all the places content will be needed or desired. This is short sited. It is also a common problem. When someone is creating a book, the workflow is optimized for a physical tome to be the final resting place for that content. A year or two passes when it is realized that the book content is needed for a website, or a magazine, or whatever else instead. This necessitates pulling all the final edits, changes, formatting — whatever — from the design file, and recreating a text file to move to the next place. This is inefficient, frustrating and error prone. It also means that at the end of this process the most correct version of the book’s text and layout are locked into a layout program document. This isn’t easy to use again for another sized book, etc.

The same can happen on the web. A blog is created. Originally this is just for fun. Many posts rack up. Visitors come. Suddenly a magazine article is asked for, or a book deal is signed. How does that content get to the form necessary for print production from its digital, database locked forms?[^2]

What these scenarios (and many others) share in common is that the content was created directly with and for the tools of immediate, intended production — not just for any tools of production. Content should be able to live on its own and just wait for where it wants to be sent, not live singular, complicated lives that don’t mix well. 

On the one hand this is easy, it just requires some simple refiguring of the creation and tracking process. On the other its incredibly complicated because the tools we’ve learned to use are mostly ill-suited for this process. Microsoft word for example. A horrible content creation tool. Everything is mired in mucky styling and formatting that is incredibly hard to get out both for use in a print context and in a web context. Indesign for layout doesn’t out of the box understand very much in the way of text-only formatting. The web is rigid and automated in ways that make matching styling and flexibility to content occasionally frustrating. The key still lays in the creation stage.

…

I will present several thought-experiments (which have semi-functioning web and print experiments to visually exemplify the ideas and process) that show a variety of ways that “content”[^3] can better conform to its idealized, perfect form suitable for a “create anywhere, publish everywhere” mindset.

First, a book that has already been designed will be examined. A final InDesign file will go from a formatted, rigid document, back into raw content. This is important as often the “design” phase does affect the content. This method respects this idea, yet still conforms to an idealized content that can be tracked, edited, updated, and reused on its own. This also begins to pave the way for a more dynamic print workflow where content updates can update printable PDF files — say for a print-on-demand project or downloadable PDF situation.

Next, a website full of content created specifically for that publication channel only will be turned into repository of raw content that still publishes as desired to the web, but suddenly opens up uses for print, or other digital formats. (for example, you have a website AND a separate, optimized phone application, whats the best way to get the content to both places?).

Finally, an idealized workflow will be examined. Options for best practices will be discussed.

Collaboration is important in the creation of great content. Writers, designers, developers, etc. all have key roles they play. One of the goals of the “create anywhere, publish everywhere” methodology is that collaborative contributions should be valued, allowed, and made as easy as possible through whatever tool the user is most familiar with. With content in the correct format upfront, this can be possible.

[^1]: I am here referring to visual style, not written style
[^2]: Actually, it is a lot easier to go from the web to print than vise versa, at least in terms of getting clean, structured but unstyled content… but we’ll get to this more later.
[^3]: By content I mean a the collection of text documents, images, and any other necessary files or data required for publishing what is being created.

---

## From Indesign to Pure Content

*tags: `CAPE Writing [[Pure Content]]` · modified: 20210619*

InDesign, Word, and various other all-in-one document/software types make it is hard to connect or anchor an addendum piece of content to the flow without actively inserting it somehow. Distinctions between an “introduction” paragraph and a regular paragraph become fuzzy. Paragraph styles for both might be the same in terms of aesthetics, however, semantically, or meta-data-wise, there might be need/desire for a difference. 

Let us say you have a designed book. All the editing, etc. for printing has already happened. However, now that content is locked into that usability space.

This is no different than using InDesign for writing. I think designers might often do this — it isn’t uncommon to directly design and write your syllabus in InDesign. Or perhaps, project sheets, etc.

Also, in terms of hierarchy within a syllabus, there are things like headlines, subheads, paragraphs, etc. that will all get paragraph stylings or perhaps character styles (to use InDesign vernacular). However, this isn’t quite as good as say styling with CSS which gives you different sorts of meta-data control, or the ability to say that the paragraph tags of class “lecture” do something different than paragraph tags of class “project” — though they are still paragraph tags… hmmm… I guess you can do this by just using different paragraph styles — but it isn't quite as intrinsically simple in inDesign or word as it is in CSS.

If you want paragraphs to look the same, but be different, or tagged, in terms of their different content, paragraph styles or similar aren’t really enough to do that…

Coding languages are much better equipped to handle things like this. Variables, Fields, File-types, etc.

Visual styling is concerned with hierarchy.
Content organizing is concerned with structure.

There is visual hierarchy and structural hierarchy.
We want to worry the most about the structural hierarchy. This is what will remain the same across all uses. The visual hierarchy we can allow to change as a function of the structural hierarchy and the use 

»»»»»»»»

Create Anywhere, Publish everywhere has some key concepts that must be understood.

Create Anywhere: This doesn’t mean with any software, or in any format unfortunately. This “Anywhere” means anything that is capable of outputting semi-structured, little-to-no-formatted text/content. However, there are ways of converting things like word docs, google docs, spreadsheets, etc. into better formatted options. This just takes 1 central repository/program that can pull in all various datas and datatypes and formats, and convert, splice, and format them in friendlier, more universal ways; as well as optimal formats for specific use cases (InDesign likes XML, most web things like JSON right now). Once data is in the central repository — or the CAPE framework — this can be accomplished fairly simply… The content can even then be “generated” to a pure form for future updates, etc. via best practices.

---

## Decoupling content from its site

*tags: `CAPE Writing` · modified: 20210619*

One thing that isn't working well for me with Ruhoh, Wintersmith, etc. is that they mix site content with site generation files to a certain extent. I want to give my clients the simple experience of only editing stuff that they should see — and not having to teach them to ignore things. Content should be separate from templates or any other site-specific information.

So, can the content be meaningfully de-coupled from the site generation in these contexts? That is the main aim of “Create Anywhere Publish Everywhere” (CAPE) right? So does that mean that Ruhoh (or wintersmith or jekyll or any other static site generator) just actually aren't the right tools to be helping with the job I want to do?

Some MFA students last year in the GDMFA program here at MICA build a poster generating machine. It was basically just a website. There were controls via an Arduino box and some code that allowed a viewer to adjust the CSS of a digital “poster” with knobs and buttons. The most important control was a big “print” button. This basically took a screen shot of the display, then saved that capture to a dropbox folder. Another computer, this one hooked up to the printer, had an apple script running that said “when a new image shows up in this dropbox folder, print it.” Using this method the grad students built a pretty seamless system that made posters, printed out images, and also uploaded all of them to a tumblr blog (which then was used to feed images to their “website”). There were a lot of moving pieces required — a lot of behind the scenes, hacked together complexity — but to the user/viewer it looked simple and seamless and easy.

Locally, I could figure this out short term — I could share a folder with a client, put in the files in a directory structure that made sense to their specific needs, and then have it upon syncing trigger an action on my laptop that updated a git repository or similar. But how long would that last? The site could have a git repo of just content, and this content could then get sent around to wherever was desired. This would also be relatively easy to explain what might need to be explained to the clients then, and hide all the complexity they need know nothing about. How does this get ramped up into production though? I can't have every clients’ website just syncing to my personal computer.

It is at least a conceptual start. We'll see where it leads.

---

## Striving For Static Sites

*tags: `CAPE Writing` · modified: 20210619*

There is a lot of working happening in the static site generation realm. I’ve played with a number of options: Jekyll, Ruhoh, Nanoc, and Wintersmith to name a few. A quick google search will yield literally 10’s if not 100’s of more options… 

The gist is this: write up your content in Markdown and YAML, create a few templates, then compile those via Ruby, Python, Node.js, or similar, and you are left with a directory of static HTML, CSS, and JS files that are now your site. Easy. Painless. Done. 

Sort of.

Its a cool idea. So far however, they all seem fairly focused on making a blog easier to upkeep, not actually build a whole site. I’m frustrated in that outside of using only a single directory of date sorted files and a few root level pages, none of the generators I have played with tried do very well at correctly managing or compiling a whole site. Multiple directories, nested sub-directories, different kinds of “content-types,” any sort of semi-advanced information architecture quickly shows the weaknesses of all the tools I’ve tested. 

I’m looking for something that does the compiling, AND can figure out my information architecture. I’m happy telling it basic stuff in some sort of metadata file — some sort of YAML file that structures how things nest or what different content types do — but I just need it to actually understand what I am telling it. 

What my colleagues and I are onto these days is trying to take this idea and run with it… so maybe we’ll figure it out at some point ourselves. We have some custom solutions do what we want (http://www.rwdfoundation.org is running on a custom version of ruhoh that adds the additional nesting I was talking about more correctly), but turning it into something that will work for any site is still in the distance.
 
I guess we will just see what the future brings.

---

## Extra Thoughts on CAPE

*tags: `CAPE Writing [[Pure Content]]` · modified: 20210619*

# Some thoughts

The process required to make any of these [[Create Anywhere Publish Everywhere]] ideas “work” rely on a person being proficient over a wide array of technical skills. These experiments have been about building new tools and connecting disparate esoteric tools, not just about using existing standard equipment. This means that as a solution, [[CAPE]] is not yet completely viable for everyday use… 

However, The idea is sound. But, in its current form it either needs a user with wide skill sets, or a team of people to make things come together. The team is probably the most sensible way to think about using [[CAPE]]. As a design department we have all the people to form a “team” allowing the kinds of skills crossover.

[[Create Anywhere, Publish Everywhere]] can also be a metaphor for how our design department can grow and evolve. One of [[CAPE]]'s aims is at platform agnosticism. 

The purer the content, the less reliant on a specific tool, technology or piece of software the content is to be distributed. The trick is figuring out the formats that allow for maximum interoperability and [[future-proof]]ness. Right now that appears to be simple image formats (like [[jpg]]), plaintext, and then a variety of coding formats — [[html]], [[xml]], [[json]], and [[yaml]]. With content in mostly these kinds of formats it can easily be sent to wherever it is desired, as well as easily reformatted for other languages/formats, or reprocessed for new uses.

[[CAPE]] respects specialization. It respects uniqueness. While the goal is content purity, the content can start anywhere. As long as you have people or tools that understand how to convert from one format to another, the content can be created in whatever tool you like. The purer the tools however, the better. InDesign in and of itself isn't the pure. Neither is [[Word]]. However, Indesign can be made "pure" by using the export to xml feature, once a person has gone through the trouble of tagging properly all the content in the InDesign document. This is not as easily the case for [[Word]]. I believe that no one should use [[Microsoft]] [[Word]].

[[Google]] [[Docs]] are problematic too — they just give you too much ability to style and weirdly format things. Too much presentational power, not enough purely structural power. Interestingly, writing in a google spreadsheet yields more usable, “pure” content than writing in a [[google doc]]. The reason? Less ability to stylize. Most spreadsheet cells are really only plaintext.

[[CAPE]] cares about [[Data]]. It cares about [[content]]. Formats that care about [[structure]] are what are most useful. But un-stylized structure is key. You then need tools that can maintain the structure while allowing you to hook styles onto that structure.

---

