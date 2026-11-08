---
title: "ImageGen Skills - Design Images for Coding Agents"
description: "leonxlnx/imagegen-skills on skills.sh: 5.0K combined installs; image-first website comps, mobile screens, brand kits and an image-to-code pipeline."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/imagegen-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-08"
tags: ["hermes skill", "agent skill", "skill setup", "image generation", "design direction", "frontend"]
---

# ImageGen Skills - Setup Guide

**Source:** [leonxlnx/imagegen-skills](https://www.skills.sh/leonxlnx/imagegen-skills) via skills.sh - 5,046 combined installs across 4 indexed listings; first seen 2026-11-08 (Nov 8 2026 morning sweep, first documentation)
**GitHub:** 72 stars, MIT LICENSE at the repo root, last pushed 2026-10-19, 4 SKILL.md directories under `skills/`
**Category:** Design imagery for agents: website comps, mobile screens, brand kits and an image-to-code handoff pipeline
**Quality Tier:** 🟢 Recommended - MIT, Pass on all three scanners for all four skills, no executable content, and a clear split between image-only skills and the one that closes the loop into code.

These four skills do not generate images themselves. They are art direction documents, between 843 and 1,465 lines each, that reshape how an image-capable model composes a design frame. The problem they address is the default distribution: centred dark hero, purple and blue glow, floating blobs, generic dashboard cards, repeated left-text right-image layouts, unreadable body copy. Each skill replaces that default with an explicit, countable brief.

The repository is small and single-purpose: `LICENSE`, `README.md`, `skills/` and `tests/`. It is the same author as `taste-skill`, and the README says these skills lived there until October 2026, when they were split out so each repo does one job. Install names did not change in the move.

The split inside the collection is the useful part. Three skills produce images and stop: `imagegen-frontend-web`, `imagegen-frontend-mobile`, `brandkit`. The fourth, `image-to-code`, is a pipeline that generates the design images, analyses them, then implements the page to match. That one needs an agent that can both generate images and write code. The other three work with any image generator, and the frames get handed to a coding agent afterwards.

## Installation

The README's install takes one skill at a time by install name:

```bash
npx skills add https://github.com/Leonxlnx/imagegen-skills --skill "imagegen-frontend-web"
```

Swap in `imagegen-frontend-mobile`, `brandkit` or `image-to-code`, or drop `--skill` entirely to install all four. For Claude Code the README also documents the plugin marketplace route:

```text
/plugin marketplace add Leonxlnx/imagegen-skills
/plugin install imagegen-skills@imagegen-skills
```

And for Codex:

```bash
codex plugin marketplace add Leonxlnx/imagegen-skills
codex plugin add imagegen-skills@imagegen-skills
```

Start a new Codex session afterwards, or the skills will not be loaded. If you installed these from `taste-skill` before the split, install them again from here; the README states the install names are unchanged, so the old copies and the new ones resolve to the same skill names.

## What It Provides

The table threshold for this pack is zero, so all four indexed listings appear below. No rows fall below the threshold and there is no tail.

| Skill | Installs | Use For |
|---|---|---|
| image-to-code | 2,185 | The full pipeline: generate section images, analyse them, extract the design system, then build the frontend to match |
| brandkit | 1,072 | Brand guideline boards: logo directions, symbol systems, palettes, type and applications on one presentation grid |
| imagegen-frontend-web | 982 | Landing page comps, one horizontal image per section, with enforced composition variety |
| imagegen-frontend-mobile | 807 | iOS, Android and cross-platform app screens and flows, consistent across a set, inside a phone mockup |

What each one actually enforces is concrete enough to audit:

`imagegen-frontend-web` opens with a hard output rule: one separate horizontal image per section, always. One section requested produces one image; a bare "landing page" request defaults to six sections and six images; "full website template" defaults to eight. It explicitly forbids the single tall image containing the whole page. It then biases away from the left-text right-image hero with ten named alternatives and requires at least three different composition anchors across a site, plus exactly four signature components and exactly two motion-implied cues.

`imagegen-frontend-mobile` is scoped hard to app screens: onboarding, auth, home, profile, settings, chat, ecommerce, fintech, health, productivity, social, utilities and multi-screen concepts. It lists what it is not for, websites and landing pages included, and it names the failure modes it exists to prevent: phone-sized websites, no safe-area awareness, too many floating cards, weak navigation logic. Its baseline dials carry a text readability priority of 10 out of 10.

`brandkit` defaults to a 3x3 board at 4:3 or 16:10, with alternative layouts for a 2x3 deck overview, a 2x2 concept board, a 1x3 horizontal strip and a 4x2 contact sheet. It runs a brand intake before generating: create from scratch, build on an existing identity, or refresh. On an existing identity it reuses supplied logos and colours and forbids inventing replacements. It also handles the awkward case honestly, telling the model to report the actual output size rather than promise pixel dimensions the generator cannot produce.

`image-to-code` is the only one with an ordering rule that changes a build. Generation first, deep analysis second, implementation third, and the skill states that the generated image is the design source while the code is the translation layer. Its baseline configuration is published as numbers: design variance 8, visual density 3, art direction 8, implementation clarity 9, image usage priority 9, spacing generosity 9, analysis precision 10, image generation eagerness 10, UI simplicity discipline 9.

## Why This Matters for Hermes Agents

The usual way an agent designs a page is to write CSS from a verbal description and iterate on the rendered result. That converges on the average of its training data, which is why agent-built sites share a look. These skills invert the order: the visual reference exists before any markup, so the agent has something to match instead of something to invent. For an operator that is also the review point, because a generated comp is easier to reject than a diff.

The other reason to load one is that the constraints are countable. "Generate one image per section" and "at least three different anchors" are instructions an agent can follow and a reviewer can check, which is rare in design prompting. If you already run a mockup or spec workflow, the frames become the deliverable and the code becomes the second step.

For CorpusIQ work the natural pairing is with the visual deliverable pipeline: `imagegen-frontend-web` for section comps, `brandkit` for a logo direction board, and `image-to-code` only when the build itself matters and the harness has both an image tool and a code tool available.

## Usage

| You say | What happens |
|---|---|
| "Design comps for a pricing page" | One image per section, with an announced section count and varied anchors |
| "A hero for a fintech product, not the usual left text right image" | The composition bias picks from the ten alternatives before falling back to the default |
| "Mobile onboarding flow, four screens" | Four app-native screens inside a phone mockup, safe areas respected, one palette across the set |
| "Brand board for a developer tool called X" | A 3x3 identity board with logo direction, palette, type and applications |
| "Build the pricing page from your own design images" | Image-to-code generates the frames, analyses them, then implements to match |
| "Make it more premium" | The dials move: density down, spacing and clarity up, variance stays high |
| "One big image showing the whole homepage" | Refused. The hard rule splits it into per-section frames |

## Verification

Read the pipeline skill before installing it. This path returned 200 on `main`:

```bash
curl -fsSL https://raw.githubusercontent.com/leonxlnx/imagegen-skills/main/skills/image-to-code/SKILL.md | head -40
```

It should open with frontmatter carrying only `name: image-to-code` and a description scoped to Codex website image-to-code work, then the heading "CORE DIRECTIVE: IMAGE-FIRST WEBSITE DESIGN TO CODE" and the mandatory order: image generation first, deep image analysis second, implementation third. If the file opens with a licence or version block instead, you are looking at a different skill.

The repository also ships a frontmatter test, which is worth running if you plan to load these in more than one harness:

```bash
npm install --no-save --no-package-lock yaml@2.6.1
node tests/frontmatter.mjs
```

It parses each `SKILL.md` with a strict YAML parser and fails loudly, because Claude Code and Codex silently drop a skill whose frontmatter does not parse. A clean run prints `ok - 4 skills load` and exits zero; any problem exits 1 with the offending file and a YAML message. After install, confirm the directory exists and holds one file:

```bash
ls ~/.claude/skills/imagegen-frontend-web
```

## Security

skills.sh verdicts for sampled skills (verified 2026-11-08) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| image-to-code | Pass | Pass | Pass |
| brandkit | Pass | Pass | Pass |
| imagegen-frontend-web | Pass | Pass | Pass |
| imagegen-frontend-mobile | Pass | Pass | Pass |

Clean across all three scanners, and the clean verdict is easy to justify. The repository contains markdown skills plus one Node test file that reads and parses them. There is no install script, no network call, no credential access and no executable path in the reasoning loop. The skills instruct a model; they do not run anything.

The risks here are content risks, not code risks. `brandkit` is designed to reproduce existing brand systems and to place real logos and names into generated boards, so an output can carry a trademark into material you would not want it in. Treat generated identity work as reference until a human signs off. Image generation also costs money per call, and the web skill's hard rule multiplies calls by section count: an eight-section landing page is eight images, not one.

## Limitations

- Snapshot data, verified 2026-11-08: 5,046 combined installs across 4 indexed listings; 72 stars; MIT; last pushed 2026-10-19; 4 SKILL.md directories. Counts drift.
- 72 stars is a small adoption signal for a design collection, so the install counts are doing most of the work of recommending it. There is no issue tracker history of any depth to read for failure reports.
- The repository has no example gallery. It ships `LICENSE`, `README.md`, `skills/` and `tests/` and nothing else, so every claim about output quality comes from reading the skill text, not from looking at results.
- Three of the four skills produce images only. Without an image-capable model or tool in your harness they do nothing at all, and the README is explicit that `image-to-code` needs an agent that can both generate images and write code.
- Legibility is a model problem the prompt fights rather than solves. The skills demand readable type, large per-section frames and generous spacing, but no instruction guarantees a small label will render correctly, and the mobile skill's readability priority exists precisely because that failure is common.
- Frontmatter carries only `name` and `description`. There is no version, no licence field per skill, no changelog and no dated release, so there is no way to tell from the file whether a copy is current.
- The `tests/` directory needs Node and a manually installed `yaml` package; there is no `package.json`, so `npm install` does not exist as a one-liner and CI has to replicate the documented command.
- I could not verify generated output quality, because that requires an image-generation run; only the raw skill paths and the file layout above were confirmed.

## Related

- [taste-skill - Setup Guide](/hermes/skills/catalog/taste-skill-setup)
- [Unlazy - Completion Gates and Depth Tree Setup](/hermes/skills/catalog/unlazy-setup)
- [UI/UX Pro Max - 19-Skill Design System Pack Setup](/hermes/skills/catalog/ui-ux-pro-max-setup)

## Pro Tips

- Install by skill name, not by repo. `image-to-code` changes how the agent works, while the other three only change what it generates; if your harness has no code tool, taking all four just adds context weight.
- Ask for the section count explicitly. "Eight-section landing page" makes the hard rule produce exactly eight frames, and it stops the model from quietly collapsing the page into one board.
- Keep the frames. In the image-to-code flow the generated images are the design source of truth, so writing them to a dated folder gives you a diffable record of what the build was supposed to match.
- For brand work, supply the real logo and palette up front. The brand intake flow reuses supplied assets and refuses to reinterpret them, which is exactly the behaviour you want and only triggers when the assets are attached.
- Run the frontmatter test after editing any skill. These files are long, and one unquoted colon in a description is enough for a strict parser to drop the whole skill silently in Claude Code or Codex.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
