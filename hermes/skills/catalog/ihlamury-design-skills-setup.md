---
title: "UI Design Skills - Design System Constraints Setup"
description: "ihlamury/design-skills - 25.3K combined installs: 87 UI constraint skills distilled from leading design systems for pixel-accurate interfaces."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/ihlamury-design-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-24"
tags: ["hermes skill", "agent skill", "skill setup", "design system", "ui constraints", "frontend"]
---

# UI Design Skills - Setup Guide

**Source:** [ihlamury/design-skills](https://www.skills.sh/ihlamury/design-skills) via skills.sh - 25.3K combined installs across 87 indexed listings; first catalogued Nov 24, 2026 (Nov 24, 2026 evening sweep)
**GitHub:** [ihlamury/design-skills](https://github.com/ihlamury/design-skills) - 108 stars, no LICENSE file (GitHub license metadata is empty; the README's License section states MIT), last pushed Feb 10, 2026, main branch; 87 skill directories under skills/<company>/SKILL.md, each with a metadata.json.
**Category:** UI Design System Constraints
**Quality Tier:** 🟢 Green - all 15 sampled skills pass the Gen Agent Trust Hub, Socket, and Snyk checks.

ihlamury/design-skills publishes 87 opinionated UI constraint skills, one per well-known product (Linear, Stripe, Figma, Apple, and 83 more), each distilled into a SKILL.md that an AI agent reads to match that product's exact colors, typography, spacing, borders, and component patterns. Every skill bundles semantic color tokens, font scales, a spacing grid, border radii, component specifications, interactive states, and animation timing, plus a MUST/SHOULD/NEVER hierarchy that makes the strength of each constraint explicit.

skills.sh indexes 87 listings at 25.3K combined installs and publishes no per-skill descriptions, but the repository README's Available Skills table lists a style and one-line description for all 87, which grounds the Use For cells below. All 87 indexed listings have a matching skills/<company>/ directory in the current tree. The repository also ships a Python extraction pipeline (scripts/extract_ui.py, then ui-skills/generate_skills.py) that turns any website into a new skill using the Codia and ScreenshotOne APIs.

## Installation

Install everything for Claude Code, Cursor, or Copilot with the Skills CLI:

```bash
npx skills add ihlamury/design-skills
```

Manual install: clone the repository and copy a single skill into the agent's skills directory:

```bash
git clone https://github.com/ihlamury/design-skills.git
cp -r design-skills/skills/linear ~/.claude/skills/
```

For Cursor or Copilot, fetch one SKILL.md directly into the project and reference it with an @-mention:

```bash
curl -o .cursor/skills/linear.md https://raw.githubusercontent.com/ihlamury/design-skills/main/skills/linear/SKILL.md
```

You can also download individual SKILL.md files straight from the skills/ directory, or paste a skill's contents into any agent's prompt. To generate a new skill from a website, the extraction pipeline needs Python 3.8+ and Codia plus ScreenshotOne API keys.

## What It Provides

skills.sh publishes no per-skill descriptions for ihlamury/design-skills; each Use For cell below is grounded in the README's Available Skills table. All 87 indexed listings have a counterpart directory in the current tree.

| Skill | Installs | Use For |
|---|---|---|
| awwwards-ui-skills | 609 | applying award-winning web design patterns |
| apple-ui-skills | 582 | applying Apple's consumer design standard |
| linear-ui-skills | 440 | building Linear-style project interfaces with the Inter font and 4px grid |
| dribbble-ui-skills | 435 | applying Dribbble-style designer showcase aesthetics |
| airbnb-ui-skills | 424 | building Airbnb-style travel interfaces with warm tones |
| notion-ui-skills | 420 | building clean, minimal Notion-style productivity interfaces |
| figma-ui-skills | 375 | building Figma-style collaborative design tool interfaces |
| vercel-ui-skills | 373 | building minimal black-and-white Vercel-style developer interfaces |
| framer-ui-skills | 353 | applying Framer-style website builder aesthetics |
| anthropic-ui-skills | 341 | applying Anthropic's warm cream aesthetic |
| superhuman-ui-skills | 326 | building premium Superhuman-style email interfaces |
| stripe-ui-skills | 316 | building Stripe-style payment interfaces with blue accents |

The remaining 75 indexed listings range from 258 to 312 installs.

## Why This Matters for Hermes Agents

Design-skills gives a Hermes agent a catalog of concrete, product-specific design constraints instead of vague style guidance. Each skill pins exact color tokens, font families and sizes, a spacing grid, border radii, component specs, interactive states, and animation timing, with a MUST/SHOULD/NEVER hierarchy that makes the constraint strength explicit. For a builder who wants an agent to produce pixel-accurate UI without hand-feeding a design spec each time, dropping the relevant SKILL.md into the project is a lightweight, dependency-free way to lock a target look. The skills are plain Markdown, so they work with Claude Code, Cursor, Copilot, or any agent that reads a prompt, and they compose per screen: build a dashboard with Linear's grid, a pricing page with Stripe's tokens, a player with Spotify's palette. The tradeoff is that they encode specific brands' aesthetics, so an agent reproduces that look rather than inventing a novel one, and the repository itself carries no LICENSE file. Read it as a style-shortcut library, not a component kit.

## Usage

| You say | What happens |
|---|---|
| Build a project management dashboard | Uses linear-ui-skills constraints: sidebar navigation, project list, and task cards |
| Create a pricing page | Uses stripe-ui-skills constraints: three tier cards, feature comparison, and CTA buttons |
| Build a music player interface | Uses spotify-ui-skills constraints: album art, playback controls, and a playlist sidebar |
| Build a banking dashboard | Uses mercury-ui-skills constraints: balance cards, transaction history, and a transfer modal |
| Build a database management interface | Uses supabase-ui-skills constraints: table explorer, query editor, and schema viewer |
| Match a design system for my settings page | Copies the SKILL.md into .cursor/skills/ and references it with @linear.md |

## Verification

Confirm the README and a representative skill body resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/ihlamury/design-skills/main/README.md | head -40
curl -sL https://raw.githubusercontent.com/ihlamury/design-skills/main/skills/linear/SKILL.md | head -40
```

Both URLs return 200. Review any SKILL.md you plan to adopt, since the constraints inside are what the agent will follow verbatim.

## Security

skills.sh verdicts for sampled skills (verified Nov 24, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| awwwards-ui-skills | Pass | Pass | Pass |
| apple-ui-skills | Pass | Pass | Pass |
| linear-ui-skills | Pass | Pass | Pass |
| dribbble-ui-skills | Pass | Pass | Pass |
| airbnb-ui-skills | Pass | Pass | Pass |
| notion-ui-skills | Pass | Pass | Pass |
| figma-ui-skills | Pass | Pass | Pass |
| vercel-ui-skills | Pass | Pass | Pass |
| framer-ui-skills | Pass | Pass | Pass |
| anthropic-ui-skills | Pass | Pass | Pass |
| superhuman-ui-skills | Pass | Pass | Pass |
| stripe-ui-skills | Pass | Pass | Pass |
| discord-ui-skills | Pass | Pass | Pass |
| raycast-ui-skills | Pass | Pass | Pass |
| shopify-ui-skills | Pass | Pass | Pass |

All 15 sampled skills pass all three checks; 15 of the 87 indexed listings were sampled, and the rest were not.

## Limitations

- Snapshot data, verified Nov 24, 2026: 25,329 combined installs across 87 indexed listings; 108 GitHub stars; no LICENSE file (GitHub reports no license, though the README's License section states MIT); last pushed Feb 10, 2026. Counts drift over time.
- skills.sh publishes no per-skill descriptions, so every Use For cell above is grounded in the README's Available Skills table rather than an indexed description.
- The repository has no LICENSE file and GitHub reports no license, while the README states MIT; treat the license status as unresolved rather than assuming MIT terms.
- The install index and the repo tree agree: all 87 indexed listings map to a skills/<company>/ directory, with no index-vs-tree drift.
- Skills pin exact color tokens, typefaces, and component specs from specific products, so they constrain style, not functionality; the constraints follow a MUST/SHOULD/NEVER hierarchy.
- Generating new skills with the bundled extraction pipeline requires Python 3.8+ plus Codia and ScreenshotOne API keys, an external dependency beyond the Markdown skills themselves.

## Related

[Emil Kowalski Skills - Design Engineering Suite Setup](/hermes/skills/catalog/emilkowalski-skills-setup) | [UI Skills - Design Engineer Skill Registry Setup](/hermes/skills/catalog/ibelick-ui-skills-setup) | [UI/UX Agent Skill System - Vendor-Neutral Skill Suite Setup](/hermes/skills/catalog/ui-ux-agent-skill-system-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install everything with npx skills add ihlamury/design-skills, then name the product in your prompt: "Build a dashboard using the Linear UI skills".
- Copy only the one or two SKILL.md files your current project needs into ~/.claude/skills/ instead of all 87.
- In Cursor or Copilot, reference a fetched SKILL.md with an @-mention (for example @linear.md) so the agent reads the constraints directly.
- Treat MUST and NEVER lines as hard rules the agent must not break, and SHOULD lines as defaults it can override with reason.
- Extract new skills only if you have Codia and ScreenshotOne API keys; otherwise contribute a SKILL.md and metadata.json manually.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
