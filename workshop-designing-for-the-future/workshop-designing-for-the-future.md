# DESIGN THE FUTURE TODAY

*A workshop on speculative design, preferable futures, and what AI image tools are actually good and bad at*

> Working title, matching the original 2023 session name. Alternates at bottom.

---

## The pitch

A preferable future is unique to each person — the point isn't to predict what's coming, it's to decide what you'd actually want, then ask whether what you're making now belongs in it. Students write a description of their own preferable future, then spend the rest of the session turning that description into images: writing prompts, running them through text-to-image tools, seeing what the tools get right, what they flatten, and what they can't do at all.

This isn't a workshop about AI as a shortcut. It's a workshop about using AI tools as a fast, cheap way to visualize and argue about the future — and getting specific enough, through iteration, to see where the tools' own limits are. One thing that reliably holds up across runs: big, broad prompts about "the future" return generic sci-fi tropes, or worse. A specific object that does one particular thing in that future is much easier to actually get something usable out of the tools with — that shift, from scene to object, is where the workshop earns its keep.

---

## The lecture

A full delivered version of this lecture is transcribed in [2023-Fall-FutureCone-DesignForTheFuture.md](2023-Fall-FutureCone-DesignForTheFuture.md) (MICA Senior Seminar, Aug 29 2023) — use it as the working script.

**Opening.** Ask the room what they picture when they hear "the future." Answers come back as *The Jetsons*, *Blade Runner*, neon, wasteland, robots. Name what they have in common: these are other people's visions, and most of them are white. That observation is the setup for the Afrofuturism section later, and for the training-data section after that — don't drop it.

"The future" is a word that only means what you want it to mean in the moment. It's like calling a plant a weed: that just means an unwanted plant. Calling something "the future" only means it hasn't happened yet — not that it's real, not that it's fake.

**Building the cone.** Time as an arrow, then a now, then a past that reads as linear in hindsight, then a *range* ahead that widens the further out you go. Bridge into it through the light cone from relativity — the cone of places a photon could have come from, and the cone of places it could still go. Then Joseph Voros's Futures Cone: futures graded by likelihood from where we stand (Projected, Probable, Plausible, Possible, Preposterous) versus how *wanted* they are (Preferable). "Preferable" is doing real work here as a category, not just a mood.

Stuart Candy's "Four Generic Futures" (Continuation, Limits and Discipline, Decline and Collapse, Transformation) is a complementary lens for seeing different *kinds* of future rather than degrees of one. *(Not in the Fall 23 delivery — added since.)*

**Speculative and critical design.** Dunne & Raby, *Speculative Everything*. Design that critiques the status quo rather than serving it; design that speculates about other futures rather than extending this one. The reason design is a good vehicle for it: the language of design is already familiar to everybody, so a designed object is an easier window into an unfamiliar idea than an art piece or an experimental score. Simplest framing: it's design that provides options for people.

Murray Bookchin's 1978 talk, "Utopia, not futurism," makes the case for why this workshop insists on preferable futures instead of merely probable ones: doing the impossible, he argues, is the rational response to a crisis, not a naive one. He's also careful to distinguish a critique of technocracy from a rejection of technology itself — a useful distinction to name directly here, since the workshop uses AI tools in service of a personal, non-technocratic vision rather than treating the tools themselves as the future. *(Not in the Fall 23 delivery — added since.)*

### The four worked examples

These carry the lecture. Each one shows the cone moving, by a different mechanism.

1. **The iPhone, 2007.** Onstage it didn't work yet — the demos were hacked together backstage. In January 2007 it sat in the *possible*: buildable, but nobody knew if anyone wanted it. The naysayers were right that it didn't fit the projected future. Then it shipped, and the old projected line truncated and a whole new cone opened behind it — things that had been impossible were now merely possible. This is the example that explains the *mechanism* of a shifting cone, so it should come first.
2. **Curry Hackett.** Midjourney-generated scenes of Black leisure, architecture and history — floating gardens in Detroit, farms on scaffolding in Baltimore, grills in the Georgetown canal. The move here is different: he's not designing a future, he's fabricating a *past and present* that would have led somewhere else. Asked whether the photos are real, he says they aren't — but what if they were? Alternate pasts reposition the whole cone.
3. **Graham Coreil-Allen / Graham Projects (Baltimore).** Painted crosswalks and intersections, made with the neighborhood or school that uses them. The counterweight to the other three: no technology, no speculation, buildable this month, and it still asserts a preferable future — one where walking is prioritized over driving.
4. **CopenHill vs. Baltimore's incinerator.** Bjarke Ingels Group's Copenhagen waste-to-energy plant is clean enough to be a public park and a ski slope, and it's built, not rendered. Then show Baltimore's incinerator. Same object, two futures. The neighborhoods due south of it have the city's highest rates of asthma, lung cancer, and heart disease — so the question "which of these futures would you rather live in" isn't rhetorical. This is the pairing that lands hardest; end on it.

### Afrofuturism

Screen the Vox mini-documentary on Afrofuturism (~4 min). Mark Dery coining the term in 1994; Sun Ra's *Space Is the Place*; Parliament's *Mothership Connection* flipping the Underground Railroad into a spaceship; André 3000 on *ATLiens*; Janelle Monáe's *Q.U.E.E.N.*

This is not a detour. It closes the loop opened by the Jetsons question — only 8% of the 100 top-grossing sci-fi and fantasy films had a protagonist of color, and half of those were Will Smith. It also sets up the training-data section directly: if the culture has overwhelmingly imagined one kind of future, a model trained on that culture will return one kind of future. Afrofuturism is the century-old version of the move students are about to attempt with a prompt box.

## How the tools actually work

The part that makes this more than a design-theory workshop. The goal is that students leave able to explain *why* the tools failed them, not just that they did — and the explanation turns out to be the same as the design lesson.

**Diffusion is denoising, not drawing.** The model starts from a field of pure noise and iteratively removes noise toward something it judges to match the text. Nothing is retrieved, nothing is collaged. Step count is the visible knob: too few and it's mush, past a point it stops improving.

**Your prompt becomes a vector, and that's the bottleneck.** The text encoder turns the prompt into a position in a high-dimensional space; nearby positions produce similar images. This is the mechanical reason the workshop's central finding happens: **"the future" lands in one of the densest, most heavily-trafficked regions of that space** — a region built out of movie posters, concept art, and stock renders — so everyone in the room gets the same chrome-and-neon mush. A specific object doing one particular job lands somewhere sparse and particular, and the model has to actually work with your idea. The scene-to-object shift isn't a prompting trick; it's a consequence of the geometry.

**Seed and guidance make it legible.** Same prompt plus same seed gives the identical image every time — proof that nothing "creative" is happening. Change *only* the seed and watch a student's carefully-described future become a completely different picture: the model has no commitment to their idea. Guidance scale (CFG) is how hard the model is pushed toward the prompt versus toward generic plausibility; crank it and outputs go fried and over-literal, which is a decent live metaphor for over-constraining a brief. Use a tool that exposes these (see below) for at least one demo, even if students spend the rest of the session in something friendlier.

**The training distribution is the whole argument.** A model can only recombine what it was trained on, weighted by how often it appeared. So the generic sci-fi it hands back isn't a malfunction — it's an accurate readout of what the culture has already imagined loudly and often. That makes the failure *diagnostic*: when the tool gives you a cliché, it's telling you which futures are over-represented and which have no purchase at all. Curry Hackett's work is the direct counter-move — prompting hard against the distribution to get something it wasn't built to give you.

**One note on LLMs**, since students conflate them: text models predict the next token, image models denoise; different mechanisms, but the same limitation. Both reproduce their training distribution, and neither can produce something genuinely absent from it. As put in the original lecture: *they can't make an image that doesn't exist already, because they don't know what that is.* Warn the room that this will be a problem for the exercise — the exercise is partly designed to make them hit that wall.

**Ethics and disclosure, modeled not lectured.** Make the slides with these tools and say so on the slides — the prompt and the tool that produced each image. Students copy what you do faster than what you tell them. Rights and training-data provenance are worth naming here too, and the tool choice below makes that concrete.

## The workshop

1. **Recap and framing** (~20 min) — the preferable future is unique to each person; if something doesn't fit in your preferable future, should you make it at all in the present?
2. **Write a preferable future** (~10 min) — a paragraph or less, individually, "alone together" on laptops. If a whole future feels too big, narrow to your own longer-term future: what world do you want to live in, what work do you want to do. Stuart Candy's four futures and Project Drawdown (the 100 most effective tools for reducing atmospheric CO2) are there if anyone needs a starting point.
3. **Prompt it** (~20–30 min) — turn the description into prompts for text-to-image tools. Try the whole description, then just keywords, then rewritten chunks. Save at least four outputs, tracking the tool and prompt used for each.
4. **Share and diagnose** (~15 min) — as a group, look at what didn't work and why. Brainstorm ways to improve both the prompts and the group's expectations of the tools. The shared canvas usually does this work before you have to: everyone can see that half the room got the same chrome-and-neon city. Two demos land hardest here — run one student's prompt with only the **seed** changed (the model has no commitment to their idea), and run the same prompt across **two different tools** (the futures come back visibly different, which is the training-data point arriving as evidence rather than assertion).
5. **Reflect** (~15 min) — what would it take to be more specific? What did historical futurists do to articulate their futures clearly that a prompt alone doesn't capture? What stories are these tools actually drawing from when they render "the future"? This is usually where the broad-scene-vs-specific-object problem surfaces — worth naming directly if it hasn't come up yet, and pointing at Julian Bleecker and Near Future Laboratory's design fiction work as the model: a single, specific object implies a whole world far better than a wide shot of one does. This is also the moment to give the mechanical explanation (see *How the tools actually work*): the cliché isn't the tool failing, it's an accurate readout of which futures the culture has already imagined loudest — which is the same point the Afrofuturism section made from the other direction.
6. **Find shared themes** (~10 min) — group students by the futures they wrote, not at random.
7. **Render together** (~20–50 min) — each student renders their own *object* within the shared theme — not a scene, not "the future" in general — then the group assembles their images into one more legible picture of a shared future. This is the step that actually produces usable results with the tools. Discuss what worked, what the tools were and weren't useful for, and where they could be more useful.
8. **Close** — futures literacy, practice with text-to-image tools, a critique of their limitations, and a discussion of how design's own semiotic tools (signs, signals) can point culture toward better futures.

---

## Who it's for

Undergraduate studio, any level — has run with both graphic design seniors (MICA, thesis-framing context) and juniors (WMU). Graduate seminar. Works for a single class section (12–25 students); needs laptops and a shared collaborative canvas (Figma or equivalent) for the "alone together" exercises.

Especially good as a **thesis-framing session**: at MICA it opened Senior Seminar, and "does this thing exist in my preferable future?" doubles as a test for choosing a degree project.

## What they leave with

Multiple AI-generated images testing their own vision of a preferable future, with prompts and tools logged for each. A working knowledge of at least one futures-studies framework. A tested, specific sense of what current text-to-image tools handle well and where they fall apart — **and a mechanical explanation for why**, in terms of denoising, prompt embeddings, and training distribution, rather than just "the AI is bad at this." For students new to it, practice with a real-time multiplayer design canvas.

## What you need

- A single afternoon at minimum (the original ran 4:15–7:00pm, tight but workable). Can expand to two or three days for real reflection time between rounds and actual iterative improvement on the images, rather than one pass straight through all eight steps. Also runs as a short format — see *Formats* below.
- Laptops/Computer station for all students
- A shared real-time collaborative canvas — Figma originally, and worth treating as part of the teaching, not just plumbing (see below)
- Access to at least one text-to-image tool — see *Picking the tools* below
- A projector/large TV for group share-outs

### The shared canvas is part of the workshop

At WMU, Figma itself was new to a lot of the students, and the real-time-everyone-sees-everything quality of it did work the workshop depends on. It's what makes the "alone together" steps function: students are heads-down on their own prompts but can watch everyone else's results appear, which is where the "wait, we all got the same chrome city" realization actually happens — collectively and on its own, before it gets named from the front of the room.

Set up the file in advance with duplicable components for logging image + prompt + tool, and separate pages per phase. Any real-time multiplayer canvas works (FigJam, Miro), but pre-built templates matter more than which tool — students shouldn't spend the session building layout.

### Picking the tools

The 2023 runs happened in a window that's closed: Midjourney, Mage.space, Stable Diffusion demos, and half a dozen others were free and effectively unlimited. Nearly all of that is now metered. Current thinking, and it needs re-checking the week before running since this space evolves and changes so rapidly now:

**Start by asking who already has Adobe Creative Cloud.** At most art schools it's a site license, and Firefly credits come with it (All Apps includes a large monthly credit allotment; the standalone free tier is a much smaller ~25 credits/month). Advantages beyond access: it's trained on Adobe Stock and licensed content, so the provenance conversation has a concrete anchor, and its outputs are noticeably blander than competitors' — which is itself a live demonstration of training-distribution effects. Downside for this workshop: **it hides seed, steps, and guidance**, so it can't carry the "how it works" section.

**Then use a knob-exposing tool for at least one demo.** [Hugging Face Spaces](https://huggingface.co/spaces) running FLUX.1-schnell is the pick ([try this!](https://huggingface.co/spaces/black-forest-labs/FLUX.1-schnell)) — free, no account, Apache-2.0, and it exposes seed and step count so the same-prompt-different-seed demo actually works. Expect queue waits at peak. Locally on a Mac, Draw Things or DiffusionBee give full parameter access with no credits at all. If you want the pipeline made visually explicit, ComfyUI's node graph *is* the diagram — good as an instructor demo, too much setup to ask of students.

**Have one high-quality general option as a comparison point.** Google's Gemini/Imagen free tier is generous and students may already have Google accounts.

The point of running two or three rather than one is comparison: the same prompt across Firefly, FLUX, and Imagen returns visibly different futures, and *that* difference is the training-data lesson landing without anyone having to assert it.

## Fee

Single afternoon: $1,500–$2,500 plus travel — shorter format than the two-day workshops, priced accordingly. Multi-day version, with real time for reflection and iteration between rounds: $2,500–$3,500 plus travel.

---

## Prior versions

- **MICA, August 29, 2023** — first run. Graphic design **seniors**, opening class of Senior Seminar (co-taught with Hayelin Choi). Short format: ~35-minute lecture to the full section, then the exercise in the existing discussion groups. Full lecture transcript: [2023-Fall-FutureCone-DesignForTheFuture.md](2023-Fall-FutureCone-DesignForTheFuture.md).
- **Western Michigan University, October 9, 2023** — "Design the Future Today," graphic design **juniors**, single afternoon workshop following a lecture. This is the version with the full run script: [2023-WesternMichigan-DesignForTheFuture.md](2023-WesternMichigan-DesignForTheFuture.md). Timing ran tight but worked out.

## Formats

- **Short (~90 min–2 hrs).** Lecture to a full section, then the write-and-prompt exercise in smaller breakout groups. This is what MICA got, and it's a much easier ask of a host than an entire afternoon — it drops into an existing class meeting. Cuts the shared-themes and collaborative-render steps.
- **Single afternoon (~3–4 hrs).** The WMU version. All eight steps, one pass, no time to iterate.
- **Multi-day.** Real reflection time between rounds, and actual iterative improvement on the images rather than one pass through.

---

## Bibliography

- Dr. Joseph Voros, [The Futures Cone, use and history](https://thevoroscope.com/2017/02/24/the-futures-cone-use-and-history/), *The Voroscope* (2017)
- Murray Bookchin, ["Utopia, not futurism: Why doing the impossible is the most rational thing we can do"](http://unevenearth.org/2019/10/bookchin_doing_the_impossible/) — 1978 speech at the Toward Tomorrow Fair, Amherst, MA (also featuring R. Buckminster Fuller and Ralph Nader); republished with permission of the Bookchin Trust
- Dunne & Raby, *Speculative Everything*
- Near Future Laboratory, *The Manual for Design Fiction*
- Julian Bleecker (AIGA 2022 Annual Conference)
- Stuart Candy
- Angela Oguntala, *Re-imagine the Future*
- Mille Bøjer, The Futures Cone
- [IKEA Home Futures](https://designmuseum.org/exhibitions/home-futures)
- Katie Patrick
- Curry J. Hackett — Midjourney-generated alternate pasts and presents of Black leisure, architecture, and history
- Vox, *Afrofuturism* (mini-documentary, ~4 min) — Mark Dery's 1994 coinage; Sun Ra, *Space Is the Place* (1973); Parliament, *Mothership Connection* (1975); André 3000 on *ATLiens*; Janelle Monáe, *Q.U.E.E.N.*
- [Graham Coreil-Allen / Graham Projects](https://grahamprojects.com/), Baltimore — participatory painted crosswalks and intersections
- Bjarke Ingels Group, [CopenHill](https://big.dk/projects/copenhill-2321) (Amager Bakke), Copenhagen — waste-to-energy plant as public park and ski slope; pair against Baltimore's incinerator and the asthma/lung cancer/heart disease rates in the neighborhoods due south
- The iPhone launch, January 2007 — worked example of a shifting futures cone
- [Arthur C. Clarke's third law](https://en.wikipedia.org/wiki/Clarke%27s_three_laws), “Any sufficiently advanced technology is indistinguishable from magic,” as the throwaway version of the same point

---

## Notes to self

- The original ran as a single afternoon paired with a separate lecture visit — this can be done in a single session, or can be explanded to multi-day offering.
- "Which AI tool(s)" is a genuinely moving target — the general category is "text-to-image diffusion," and I don't particularly care about a specific tool. But the *free-and-unlimited* era the 2023 runs relied on is over, so the tool question now has to be answered concretely for each host. Ask about their Creative Cloud license first. Re-verify every free tier the week before teaching; they change constantly (I have tried ideogram, google's stuff, chatGPT... there are so many options, its just what is easily useable for free temporarily in a workshop space).
- The teaching goal has widened: not just futures studies plus a tools exercise, but an actual explanation of how diffusion models work. The connective tissue is that the workshop's oldest finding (broad prompts → generic sci-fi, specific objects → usable results) turns out to be a fact about prompt-embedding density and training distribution. Design lesson and technical lesson are the same lesson — that's the version worth pitching.
- the models given just big broad prompts give you vague scienc-fictiony results; getting into actual more concrete objects, use cases, descriptions, etc. lead you to more usable, interesting imagery.
