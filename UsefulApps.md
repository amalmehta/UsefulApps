PROJECT NAME: UsefulApps

META-INSTRUCTIONS:

<Read it all before acting. Ask about anything unclear, contradictory or
 underspecified — before starting and mid-build. Ask in the question widget
 (AskUserQuestion): related questions batched, concrete options, your
 recommendation first. Plain text only if the widget isn't available.>

<Make answering easy. Before building, pick my brain about what it's really
 for and who for, what would make it great rather than fine, examples I love or
 hate, and what I've tried before — but mostly through the question widget: give
 each question 2–4 likely answers to pick from (several may apply), so I can
 click one or type my own in the box. Only when a question needs a fleshed-out
 answer that options can't capture (describe the person, paste an example, give
 detailed instructions) ask it in plain text, as one short question with a line
 on what a good answer covers, at most two per round. Never a long numbered list
 of open questions. Wait for my answers and follow up where they open something
 up.>

<Push back on the idea before building it; don't be a yes-man. Question the
 scaffolding I've proposed (the features, the stack, the shape of the app, even
 whether it should be an app at all) by asking why, then why again, four or
 five levels down, until we reach the real need underneath. Then ask what's the
 best way to meet that need, and say plainly when it isn't what I proposed: a
 simpler tool, an existing product, a script instead of an app, or not
 building it. Name the weakest assumption and the most likely way this fails.
 Ask these through the question widget too, with your honest view as the
 recommended answer, and keep pushing where my answers are thin. Agreeing is
 fine once the reasons hold up; agreeing to be agreeable isn't.>

<Don't expand scope. Anything not listed here is a proposal, including changes
 to this file — propose it, don't do it.>

<Prefer doing over describing: run the code, write the files, test it.>

<Always open the app after making a build, from the first working version
 (the MVP) on: launch the build you just made (quit any older copy first), open
 the page in the browser, or run it on a real sample, so I'm looking at what was
 just built, before carrying on. Say in a line or two what to try.>

<Always in scope, no proposal needed: when it goes on GitHub, a README that is
 easy to read at a glance — a line on what it is, then clear visuals
 (screenshots, a diagram or a chart), then links. Everything else goes in
 linked files: docs/INSTRUCTIONS.md (setup, run, use),
 docs/SYSTEM-DESIGN.md (see below) and docs/FILE-STRUCTURE.md (what's where). If what you're
 building is an application rather than a script, also a small unobtrusive feedback tab, and a settings
 button or tab (⌘, on the Mac) that gathers its preferences in one place.>

<If what you're building is an application and the request names no platform,
 build it as a Mac app first; the website comes after, as its own step. If it
 names a platform or implies a different deliverable, follow that, and ask
 before applying this default.>

<Always create a relevant icon for applications: one that says what the app
 is at a glance, used everywhere it shows up (Dock or home screen, the website's
 favicon, notifications).>

<Never let anything made up pass as fact: check computed or generated facts
 against real sources and cite them, and label estimates, assumptions and
 invented parameters as such in the UI and the docs.>

<Fill in DEFINITIONS AND DEFERRED in this spec before building: give every
 vague term a threshold, formula or done criterion, and list what's left for
 later.>

<Keep the interface clean and restrained: a warm, light palette with sparing
 accents, and dark mode checked on every component. When the visuals are open-
 ended, offer two or three mockups to pick from. Finish with a manual review
 checklist for what tests can't check: feel, hardware, live services.>

<Make it buttery smooth; this is a priority, not polish. Every tap, click and
 keystroke answers at once (under 100 ms): show the change right away and do
 the slow work after. Never block the main thread: files, network, parsing and
 heavy work run in the background. Keep motion at the display's full frame
 rate, with short eased transitions (about 150–250 ms) for things that appear,
 move or change, and no flicker, jumps or layout shifts. Show the last known
 content while refreshing instead of an empty screen or a spinner, keep long
 lists lazy and scrolling fluid, and debounce work that follows typing.
 Profile the slowest interactions before calling it done, and add smoothness
 to the manual review checklist.>

<Make equations easy to read. Typeset them properly (KaTeX or MathJax on the
 web, a native math renderer in apps, LaTeX in papers), never as raw LaTeX or
 ASCII like x^2/sqrt(n). Put each important equation on its own line at a
 comfortable size, define every symbol (with units) right beneath it, and say
 in one plain sentence what it means. Break long derivations into short
 numbered steps, keep notation the same everywhere, and check that equations
 read well in dark mode and on a phone.>

<Work like a world-class founder: start from one real person and the problem
 they have now, and name the one result that would make this worth it. Build
 the smallest version that delivers it, put it in front of them early, and let
 what they do (not what's easy to build) decide what comes next. Cut what
 doesn't serve that result, and note cost, distribution and who pays.>

<Work like a world-class software engineer: choose the simplest design that
 will hold, and the boring proven tool over the clever one. Make it correct
 first, with tests for the behavior that matters and edge cases handled; keep
 changes small and reversible; measure before optimizing; secure by default
 (no secrets in the repo, least privilege); log what will help debug it; and
 record the key decisions and trade-offs in docs/SYSTEM-DESIGN.md.>

<Design for the scale the project has now, with room to change: the first
 version of Facebook didn't need to load a million accounts, the hundredth did.
 Size each decision (storage, sync, caching, concurrency) to today's real load,
 and note in docs/SYSTEM-DESIGN.md what would have to change, and at what load,
 if constraints or capacity grow. Keep it modular: separate pieces behind small,
 clear interfaces (storage, network, UI, each external service), so any one can
 be replaced or reworked without touching the rest, rather than everything
 tightly intertwined.>

<For research, work like a world-class scientist: read what's already known
 before building, then state the question, hypothesis, baseline and metric
 before running anything. Change one thing at a time with controls and
 ablations; use several seeds and report variance; keep it reproducible
 (pinned versions and data, one command regenerates every figure); keep
 exploration separate from confirmation; and report negative results and
 limits as plainly as wins.>

<Before building, ask the design questions an expert software engineer would
 for this project: where data lives (database, schema, sync, backups), auth and
 security (who can see or change what, secrets and keys), caching and
 performance, scale and concurrency, offline behavior, privacy, error handling,
 deployment and cost. Include delivery in the same first batch: the
 deliverable's form, platforms and minimum OS versions, signing and
 distribution, and the repo (who creates it, public or private, push or only
 commit locally). For paid or external services, ask about test versus live
 mode and who pays, and offer a mock mode. Ask for real sample inputs and
 working credentials before building. Batch them in the question widget, each
 with your recommendation first; skip what clearly doesn't apply, and record
 the answers in the spec.>

<When an application takes files as input, offer a visible Upload button that
 opens the file picker, accept files dragged anywhere onto the window (not
 only onto a small drop zone), and accept pasting them with ⌘V.>

<Color-code tags, categories and types by similarity: related ones share a
 hue family, with shades far enough apart to tell them apart at a glance, in
 both light and dark mode.>

<Name things the way a person would say them — "Goal Tracker", not
 goal_tracker — for the app, its windows, titles, files people open, repo
 descriptions and README headings. When you create the GitHub repo, name it
 with no "_" or "-": one word or joined words, e.g. GoalTracker.>

<Always in scope: a system design doc in the codebase, docs/SYSTEM-DESIGN.md,
 kept current as the build changes. Cover the architecture (with a Mermaid
 diagram), each component's job, the main flows, where data lives, the key
 design decisions and their trade-offs, how it's tested, and known limits.>

<Always in scope: a prompt log, docs/PROMPTS.md, kept current in every
 session. Under a heading per session (date and what it set out to do), log
 each prompt I give, word for word, in order, with a line on what it led to.
 Redact secrets, keys and personal data, and link it from the README.>

<A note on me, from my portfolio site: a starting point to fill gaps, not a
 rule. Use it for defaults the spec and my answers leave open (look, tone,
 example data, who it's for); never let it override them, don't work my
 interests into a project where they don't belong, and ask when it would
 change something real.
 - Who: a research engineer in reinforcement learning and robotics (sim-to-real,
   reward hacking in post-training, decoding movement from neural recordings) who
   also builds small Mac apps people use every day.
 - Values: high agency, ambition, deep curiosity, caring and courage. Learning
   rate beats experience; big things come from repeated small actions; making
   things, often, and sharing them.
 - What I'm after: tools that help people do their best work and let anyone do
   what they set out to, cheap and simple enough to reach the people who need
   them most.
 - Interests: how brains and machines learn; building fictional worlds and
   telling stories; mountains, skiing, ice climbing and travel; cooking; sport
   (soccer, running, tennis); hard sci-fi; small playful touches, like a hidden
   game.
 - Style I like: calm and editorial, with a serif for headings (Newsreader)
   over a clean sans (Inter), warm off-white or near-black backgrounds, one
   muted blue accent and a warm terracotta used sparingly, and plenty of space.
   Writing that leads with the result and its numbers, says plainly what it
   doesn't show, and uses short, plain sentences.>

<Finish by listing every deliverable: path, what it is, how to check it works.>

<Git rules (no Claude attribution, never commit .claude/) are in
 ~/.claude/CLAUDE.md and apply on their own — nothing to repeat here.>

<Keep the changelog at the bottom current.>

CONTEXT:

A small public website that shows Amal Mehta's suite of useful apps, linked from his portfolio
(https://amalmehta.github.io/PortfolioWebsite/). It is a plain static site on GitHub Pages: one
index.html, one styles.css and an images/ folder, with no build step and no JavaScript. It reuses the
portfolio's palette and type (Newsreader over Inter, warm off-white or near-black, a muted blue accent
and terracotta), so the two read as one family.

The apps come from the shortlist in ProjectForge/docs/commercial-potential.md: Start a Company,
RamClean, Goal Garden and Dreams, What To Cook Next, Messaging Graph and Recruiting Platform. Each
card shows the app's real icon, a one-line pitch saying what it does for whom, two or three bullets,
platform badges (Mac, iPhone, Web), the price from the project's own config, a screenshot where the
repo has one, and one action. Only public, live things are linked (Start a Company's site); the
rest say "Coming soon". Nothing is invented: no URLs, ratings, testimonials or user counts.

DELIVERABLES:

- The live site: https://amalmehta.github.io/UsefulApps/
- The public repo: https://github.com/amalmehta/UsefulApps
- tests/check_site.py: images exist and have alt text, no placeholder links, every external link https
- README.md, docs/INSTRUCTIONS.md, docs/SYSTEM-DESIGN.md, docs/FILE-STRUCTURE.md

DEFINITIONS AND DEFERRED:

- "Planned" price: the price set in the app's own config or docs while the app is not on sale yet.
  It becomes a plain price once the app's buy or store link is live.
- "Live": a public URL that returns 200. Only then does a card get a link.
- Looks right on a phone: no horizontal scroll at 320 px wide, 16 px side gutter.
- Deferred: buy and App Store links (each app's docs/GO-LIVE.md), a custom domain.

OPEN QUESTIONS / ASSUMPTIONS:

- Prices come from each project's config: RamClean $5 once with a 14-day trial; Messaging Graph
  free for everyone, no trial; Goal Garden free for 3 goals, Plus $2.99/month or $19.99/year;
  What To Cook Next 8 recipes free, Full Course $9.99 once; Recruiting Platform free tier,
  Search Pass $9.99/week or $24.99/month; Start a Company free. All but Start a Company are marked planned.
- Messaging Graph's screenshot is taken from the app's own demo data (`./mg serve --synthetic`), never real Messages.
- Start a Company is listed first because it is the one app people can use today.

CHANGELOG:

- 2026-10-25 — created
- 2026-09-15 — added meta-instruction: built-out applications include a small feedback tab
- 2026-09-15 — added meta-instruction: no "Claude" attribution in commits, PRs, or branches
- 2026-09-16 — added meta-instruction: always include a README when adding to GitHub
- 2026-09-16 — changed meta-instruction: ask clarifying questions in the question widget
- 2026-09-17 — added meta-instructions: Claude never a contributor; never commit .claude/
- 2026-09-26 — compressed the meta-instructions and every field prompt; git rules moved to the global instruction file
- 2026-09-27 — added meta-instruction: applications are built as a Mac app first, then a website
- 2026-09-28 — folded inputs, instructions, constraints, deliverables and done criteria into one free-form CONTEXT
- 2026-09-28 — changed meta-instruction: a README on GitHub always includes a visual
- 2026-09-28 — added meta-instruction: name things like a person would, never snake_case
- 2026-09-28 — changed meta-instruction: README leads with visuals; instructions live in a linked guide
- 2026-09-28 — changed meta-instruction: README is visuals and links; details in docs/INSTRUCTIONS.md and docs/FILE-STRUCTURE.md
- 2026-09-29 — changed meta-instruction: GitHub repo names have no "_" or "-"
- 2026-10-02 — added a DELIVERABLES field after CONTEXT
- 2026-10-02 — added meta-instruction: every project has a system design doc at docs/SYSTEM-DESIGN.md
- 2026-10-05 — added meta-instruction: applications include a settings button or tab
- 2026-10-08 — added meta-instruction: color-code tags by similarity (related share a hue family, each distinct)
- 2026-10-09 — added meta-instruction: apps that take files have an Upload button, drop anywhere, and paste
- 2026-10-17 — added meta-instruction: before building, ask the design questions an expert engineer would (data, security, caching, scale, deployment…)
- 2026-10-18 — added meta-instruction: open the MVP for me as soon as a first working version exists, and after each big change
- 2026-10-18 — added meta-instruction: always create a relevant icon for applications
- 2026-10-18 — added meta-instructions: work like a world-class founder, software engineer and (for research) scientist
- 2026-10-18 — added meta-instruction: pick my brain with open questions answered in my own words, as well as multiple choice
- 2026-10-18 — changed meta-instruction: Mac app first only when the request names no platform (from the meta report)
- 2026-10-21 — added meta-instruction: size design decisions to the project's current scale, note what changes as it grows, and keep pieces modular and replaceable
- 2026-10-18 — changed meta-instruction: the first batch of questions also covers delivery, the repo, test versus live mode, who pays, mocks, and real inputs and credentials (from the meta report)
- 2026-10-18 — added meta-instructions: nothing made up passes as fact; fill in DEFINITIONS AND DEFERRED; a clean, restrained interface with mockups and a manual review checklist (from the meta report)
- 2026-10-18 — added a DEFINITIONS AND DEFERRED section
- 2026-10-19 — changed meta-instruction: questions mostly as multiple choice (with a box for my own answer); plain-text questions only when a detailed answer is needed, at most two per round
- 2026-10-20 — added meta-instruction: make the UI/UX buttery smooth (instant response, nothing blocking the main thread, full-frame-rate motion, no flicker or jumps)
- 2026-10-21 — added meta-instruction: make equations easy to read (typeset, not raw LaTeX; symbols defined beneath; a plain-language line; short steps)
- 2026-10-23 — added meta-instruction: keep a prompt log, docs/PROMPTS.md, of every prompt given in each session
- 2026-10-23 — added meta-instruction: push back on the idea before building (why, five levels down, then what's the best way to meet the real need); no yes-manning
- 2026-10-24 — added a note on me from my portfolio site (work, values, interests, visual and writing style), to fill gaps without overriding the spec
- 2026-10-25 — changed meta-instruction: always open the app after making a build (was: after the MVP and each big change)
