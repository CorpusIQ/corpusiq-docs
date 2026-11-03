---
title: "Stageshow - Faux Product UI Skill Setup"
description: "benjitaylor/skills: 7.2K combined installs. One skill for faux product UI: stills, cursor demos and bento grids in React, with a kit and a film gate."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/benjitaylor-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-02"
tags: ["hermes skill", "agent skill", "skill setup", "product ui", "react", "motion design", "design engineering"]
---

# Stageshow - Setup Guide

**Source:** [benjitaylor/skills](https://www.skills.sh/benjitaylor/skills) via skills.sh - 7.2K combined installs across 1 indexed listing; first documented 2026-11-02 (evening sweep)

**GitHub:** [benjitaylor/skills](https://github.com/benjitaylor/skills) - 996 stars, no license file at the repository root (the skill folder carries its own MIT license), branch main, last pushed 2026-10-31; one skill living in its own top-level `stageshow/` directory, with `SKILL.md` at that directory's root, its own `README.md`, 15 reference pages, 69 example folders, a portable `kit/` of 42 component files and 12 Node verification scripts

**Category:** Product UI illustration for agents: faux app screens, cursor walkthroughs and bento grids built in React and filmed for review

**Quality Tier:** 🟡 Yellow - Socket returns a Warn on the single indexed listing and the repository has no license file at its root, so the MIT grant covers the skill folder and nothing beside it

Benji Taylor's repository is a personal collection of design and motion skills, and today it holds exactly one: `stageshow`, in a top-level folder of its own, described by that folder's `README.md` rather than by the root. The root README is twenty lines and points at it. The folder is the substance: a 149-line `SKILL.md`, 15 reference pages, 69 example folders, a portable React kit of 42 component files with their CSS, a Vite playground that previews everything, nine bad and good teaching pairs, and 12 Node scripts that film a running demo and assert things about the result.

The premise is narrow and well chosen. Agents asked for a product illustration produce something that reads as generated, so `SKILL.md` opens with five named failure modes (too much, wireframe, boxed, flat, bland) and their fix, then treats the job as a design review rather than a generation task: find the closest gold example, film it, copy its folder, replace its content with the brief's product, compare yours to it at two widths, and only then choreograph motion. The whole thing is authored illustration rather than browser automation, so a scripted `a.click()` draws the cursor pressing and `a.set()` changes the scene.

## Installation

The repository README gives one command, scoped to the skill:

```bash
npx skills add benjitaylor/skills --skill stageshow
```

The `--skill` flag matters here. The repository is laid out so each skill keeps its instructions, references, examples and tools together in its own folder, which the root `AGENTS.md` states as the rule for adding more, so a bare install of the repository is not the right unit.

For a Hermes profile the manual copy is a folder copy, because the skill is self-contained and its references are local:

```bash
git clone --depth 1 https://github.com/benjitaylor/skills.git /tmp/benjitaylor-skills
mkdir -p ~/.hermes/profiles/corpusiq/skills/stageshow
cp -R /tmp/benjitaylor-skills/stageshow/. ~/.hermes/profiles/corpusiq/skills/stageshow/
```

Copy the folder contents. `SKILL.md` links every reference and every example by relative path, so a copy holding only the Markdown leaves the agent with rules and no kit to build them with.

To run the playground, which is how you see the gold examples and film anything, the folder needs Node 20.19 or later:

```bash
cd stageshow
npm install
npm run dev
```

On macOS and Linux that serves **http://stageshow.localhost:1355**; on Windows open the Vite URL it prints, normally 127.0.0.1:5173. If npm skipped optional dependencies, the README says to re-run with `npm install --include=optional`. Filming uses `playwright-core` and a locally installed Chrome, or a `CHROME_PATH` if Chrome lives somewhere unusual; neither is a runtime dependency of the illustration you build.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| stageshow | 7,243 | Building faux product UI that reads as a real product: browser and app windows, dashboards, phones with lock screens and notifications, chat threads, terminals, bento grids and cursor walkthroughs, as a still, a feature card or a 10 to 16 second animated demo. Covers the framing rules (one gutter, bleed off an edge, no plate under a hero, crop to the panel the story happens in), a restraint budget of 3 to 7 real strings with filler only at the edges, the kit of `Stage`, `Window`, `Phone`, `Keyboard`, `Thread`, `Bubble` and the motion primitives (`Collapse`, `Roll`, `Swap`, `Count`, `Fly`, `Follow`, `States`, `Stream`, `Popover`, `Scroll`, `Camera`, `Expand`), 69 worked examples split into gold scenes, product studies and specimen sheets, nine teaching pairs for diagnosing a bad frame, and a film-and-check loop (`typecheck`, `check:css`, `film.mjs --gate` at the shown width, at 390 and across states). |

All 1 indexed listings clear the threshold and appear in the table above.

The 15 references are the judgment layer and each maps to a task: `framing.md` for the layout table and crop rules, `craft.md` for the still frame (restraint, type, spacing, icons, color, chrome), `motion.md` for story, loops, pace and drags, `kit.md` for every component's props, `rehearse.md` for how to film and which frames are never intentional, `verify.md` for the checklist and the hand-over template, plus `bento.md`, `annotations.md`, `backgrounds.md`, `brands.md`, `looks.md`, `choreography.md`, `products.md`, `review.md` and `teaching.md`.

## Why This Matters for Hermes Agents

The default agent output for "make a picture of our product" is a purple gradient, a sparkle icon, and a letter in a colored square. Stageshow names that failure and replaces it with constraints an agent can follow: count the real strings and keep the budget to 3 to 7, put words where the eye lands and bars only beside it, keep the window bleeding off at least one edge instead of floating with even margins, and never draw a status bar or a phone frame by hand when the kit already has one.

The second thing it fixes is the comparison step. Most design guidance asks an agent to be tasteful, which is not checkable. This skill asks it to film the closest gold example first, then film its own still at the same two widths, and answer whether its version is the emptier, flatter or smaller one. That converts a taste argument into a measured difference, and it is the single most transferable idea in the pack.

The third is verification as artifact. `film.mjs` drives a real browser, captures the loop and a contact sheet, and can step beats at 40 to 80 milliseconds so a press or a morph is inspected at the frame where it happens, with a `--gate` run that ends only on `rehearsal passed`. The skill is explicit that a passing gate is necessary and not sufficient and that no automated clean result replaces watching the motion, which is the right way to ship a judgment tool to an agent.

Finally the output is editable. The kit is React and plain CSS with no third-party animation runtime, so what an agent produces is a component a developer can keep, re-theme and re-render, not a screenshot that has to be redone by hand.

## Usage

| You say | What happens |
|---|---|
| "Make a hero image of our app that looks like a real product" | Picks the closest gold example from the table, copies its folder, maps your product's tokens onto the kit's look, and films a still at the hero width and at 390 before showing you anything. |
| "I need a feature card with a dashboard in it" | Starts from the static card gold, keeps a hard crop with one satellite object, puts real words only on the subject row and the total, and fills the panes so no corner is empty. |
| "Animate a cursor clicking through onboarding" | Copies a cursor gold, writes three to five beats with a payoff inside 10 to 16 seconds, marks what the cursor touches with `data-target` and `data-cursor`, and drives it from the `Act` script. |
| "This looks AI generated, fix it" | Names the fault against the five failure modes (too much, wireframe, boxed, flat, bland), then fixes the largest visible one first: framing, then hierarchy, then motion, then polish. |
| "Make a bento grid of our features" | Plans the grid with the bento reference, gives each tile one specific moment with its own words, and makes one tile clearly lead by size or depth. |
| "Film it and tell me what is wrong" | Runs the type check and CSS clash check, films the loop with `--gate` at the shown width and at 390 and across states, and reads the contact sheet frame by frame. |
| "It has to work as a phone-sized tile" | Uses the `compact` design at the column width of 358 as a redesign rather than a squeeze, and crops the phone so it bleeds off an edge instead of shrinking whole. |

## Verification

The raw path below returned 200 on branch main on 2026-11-02. The file sits at the root of the skill folder, not at the repository root:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/benjitaylor/skills/main/stageshow/SKILL.md
```

After a clone, confirm that the skill arrived with its references, examples and kit, because the folder is the unit and a partial copy is the common failure:

```bash
git clone --depth 1 https://github.com/benjitaylor/skills.git /tmp/benjitaylor-skills
find /tmp/benjitaylor-skills -name SKILL.md | wc -l
ls /tmp/benjitaylor-skills/stageshow/references | wc -l
ls -d /tmp/benjitaylor-skills/stageshow/examples/*/ | wc -l
head -3 /tmp/benjitaylor-skills/stageshow/SKILL.md
```

The first count should print 1, the second 15, the third 69, and `head` should show `name: stageshow` with the description the runtime routes on. On the installed copy:

```bash
ls ~/.hermes/profiles/corpusiq/skills/stageshow | head
grep -c 'references/' ~/.hermes/profiles/corpusiq/skills/stageshow/SKILL.md
```

You should see `SKILL.md`, `README.md`, `kit`, `examples`, `references`, `teaching`, `scripts` and `playground`, and a non-zero pointer count. If you want the film gate to work, `npm install` and `npm run typecheck` in that folder are the next check.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-02) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| stageshow | Pass | Warn | Pass |

The code in this repository is React and TypeScript, with CSS modules per component and a set of Node scripts. `package.json` in the skill folder declares only `dev`, `typecheck`, `build` and `check:css`, so there is no install hook, no postinstall download and nothing that runs on load. The one thing an agent will execute on purpose is `scripts/film.mjs`, which launches Chrome through `playwright-core` and films a URL you give it. That is the same action a screenshot tool performs, and it is worth reading once before you let it point at anything other than localhost.

The Warn is easier to understand from the tree than from the report: the folder vendors a lot of third-party artwork. `kit/brands/` holds 44 SVG brand marks drawn from SVGL, payment-icons, Cryptocurrency Icons and official sources, each with its own licence file and a `SOURCES.md` recording per-file origins, plus app icons and two CC0 photographs. `NOTICE.md` states plainly that the MIT licence does not extend to those marks or to the trademarks they represent. If you ship an illustration built from a kit brand or a product study, that is your licensing decision, not the skill's.

The repository root has no licence file at all, so the README and the root `AGENTS.md` carry no explicit reuse grant. The MIT text exists only inside `stageshow/LICENSE`, and it names Benji Taylor as the copyright holder.

## Limitations

- Snapshot data, verified 2026-11-02: 7,243 combined installs across 1 indexed listing; 996 GitHub stars; no license file at the repository root; last pushed 2026-10-31. Counts drift over time.
- Socket returns a Warn on the only sampled listing and the pack records no rule for it. The code is small and readable, but the verdict is not clean.
- The licence is per folder, not per repository. `stageshow/LICENSE` is MIT; anything the root of the repository gains later has no stated terms, so check before reusing non-skill files.
- The gate is a floor, not a verdict. `SKILL.md` says a `film.mjs --gate` run ending `rehearsal passed` is necessary and not sufficient, and that no automated clean result replaces watching the motion, so an agent that only reads the gate can still hand over a frame a designer would reject.
- It is a heavy install for a skill: 69 example folders, a package lock, 42 components with their CSS, a Vite playground, and Node 20.19 or later plus a local Chrome for filming. All of it is optional for reading the guidance and required for using the kit well.
- `SKILL.md` compresses each workflow step into a single dense paragraph with parenthetical cross-references. It is efficient and hard to skim, and the references are not optional reading if the task is a still.
- Product studies bundle recognizable interfaces (Figma, Linear, Slack, Raycast, Finder, Spotify, Notion, Gmail, Office, Wikipedia, Telegram, iMessage). The guidance is to borrow the interaction and not another product's identity, which is a judgment call an agent can get wrong.

## Related

- [remotion-best-practices - Video Production Setup](/hermes/skills/catalog/remotion-best-practices-setup)
- [PowerPoint - Create, Read, Edit .pptx Decks Setup](/hermes/skills/catalog/powerpoint-setup)
- [JEO Skills - Presentation and Document Suite](/hermes/skills/catalog/jeo-skills-setup)
- [Jwynia Agent Skills - Presentation and Writing Suite](/hermes/skills/catalog/jwynia-agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Film the closest gold example before you write a line. The skill's own command is `node scripts/film.mjs "<preview>/?capture=<gold>" --select '#example' --still --out gold.png`, and holding your still next to it is the fastest way to see that yours is emptier.
- Read `references/craft.md` in full even when a gold example matches your task. It holds the still-frame rules the gold cannot show you, including the cases your chosen example happens not to contain.
- Set the poster frame first. Most people see only that frame, as a thumbnail or under reduced motion, so it has to tell the story on its own, with the result left on screen rather than tidied away.
- Run the 390 pass every time, then the `--states` pass. A demo that holds at 900 and breaks at phone width is the most common defect in a feature card.
- Leave a `REHEARSAL.md` beside the component using the template in `references/verify.md`: the gold you copied, what you changed, what you did not check. It gives the next run an honest starting point.
- Use `teaching/` for diagnosis only. The bad halves are deliberately broken, and copying them as a starting point reproduces the fault.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
