---
title: "Skills for Antigravity - Game & Research Collection Setup"
description: "Setup guide for omer-metin/skills-for-antigravity - 25.6K combined installs. Skills for Google Antigravity: game UI, pixel art, quant research, 3D."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/skills-for-antigravity-setup/"
robots: "index,follow"
last_updated: "2026-10-10"
tags: ["hermes skill", "agent skill", "skill setup", "antigravity ide", "game development", "quant research"]
---

# Skills for Antigravity - Setup Guide

**Source:** [omer-metin/skills-for-antigravity](https://www.skills.sh/omer-metin/skills-for-antigravity) via skills.sh - 25.6K combined installs across 96 indexed listings; first seen Oct 9, 2026 (extended-query probe)
**GitHub:** [omer-metin/skills-for-antigravity](https://github.com/omer-metin/skills-for-antigravity) (163 stars, Apache-2.0; pushed 2026-01-22; standard `SKILL.md` files under `skills/`)
**Category:** Game Development / Research
**Quality Tier:** 🔵 Community - independent collection (163 stars, Apache-2.0); last pushed Jan 2026; all sampled verdicts Pass

Skills for Antigravity is an independent collection of 462+ AI skills packaged for Google Antigravity. omer-metin converts the Vibeship Spawner Skills dataset (originally defined in YAML) into Markdown `SKILL.md` files, repairing hundreds of formatting issues and typos along the way. Coverage spans development (React, Next.js, Python, TypeScript, Docker, Kubernetes), AI and ML, business, and specialist domains; the traffic leaders are game UI design, quantitative research, pixel art sprites, technical analysis, and 3D modeling.

The skills are standard SKILL.md folders under `skills/`, so they drop into Antigravity's global (`~/.gemini/antigravity/global_skills/`) or per-project (`project/.agent/skills/`) directories with no build step. Two clusters dominate installs: game development (game UI, sprites, gamification loops, game audio, level and combat design) and quant trading (quantitative research, technical analysis, crypto trading bots, algorithmic trading, risk management).

---

## Installation

The README's Fast Start method for Antigravity: copy the skills you want from the `skills/` folder into your Antigravity workspace.

- Global: `~/.gemini/antigravity/global_skills/`
- Project-specific: your project's `.agent/skills/` directory

Registry-based install via the skills.sh CLI:

```bash
# Browse the collection
npx skills add omer-metin/skills-for-antigravity --list

# Install the full collection
npx skills add omer-metin/skills-for-antigravity -g --all

# Or install a single skill
npx skills add omer-metin/skills-for-antigravity -g --skill game-ui-design
```

No build step is required; Antigravity reads the SKILL.md files directly. See the [Antigravity Skills documentation](https://antigravity.google/docs/skills) for how the IDE consumes them.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| game-ui-design | 3,496 | Game UI work: HUDs, menus, and interface systems for games |
| quantitative-research | 2,610 | Quantitative research workflows: hypotheses, data, and strategy evaluation |
| pixel-art-sprites | 2,396 | Creating pixel art sprites and sprite sheets |
| technical-analysis | 1,953 | Technical analysis of price charts and market indicators |
| 3d-modeling | 1,100 | 3D modeling for game assets and scenes |
| crypto-trading-bots | 901 | Building crypto trading bot logic |
| gamification-loops | 517 | Designing gamification and engagement loops |
| algorithmic-trading | 516 | Algorithmic trading strategy implementation |

The remaining 88 indexed listings range from 52 to 450 installs.

## Why This Matters for Hermes Agents

Agent builders get two things here. First, domain coverage that would otherwise require assembling many single-purpose repos: the game-dev cluster runs from UI and pixel art through audio, level design, and monetization, and the quant cluster runs from research and technical analysis through trading bots and risk management. Second, portability: everything is plain Markdown, so the same folders that Antigravity reads from `~/.gemini/antigravity/global_skills/` or `.agent/skills/` can be dropped into any agent that loads SKILL.md files. The conversion also repaired formatting across hundreds of files, so the content is cleaner than the original YAML dataset it came from. Start with the high-traffic skills - they are the most exercised and the best documented - and audit each SKILL.md before wiring it into a workflow.

## Usage

| You say | What happens |
|---|---|
| Design the HUD and menus for our arena shooter | game-ui-design applies game interface patterns to the HUD and menu system |
| Generate pixel art sprite sheets for a roguelike | pixel-art-sprites produces sprite art in a consistent pixel style |
| Research a quantitative strategy for a market hypothesis | quantitative-research structures the research workflow from hypothesis to evaluation |
| Chart the trend and momentum indicators on this stock | technical-analysis walks through chart analysis and indicator interpretation |
| Model a low-poly prop for the game scene | 3d-modeling covers the modeling workflow for game assets |
| Design the progression loop for our idle game | gamification-loops builds engagement and reward loops |
| Prototype a crypto trading bot | crypto-trading-bots covers bot logic for crypto markets |

## Verification

Check where the skills landed, then review one before trusting it:

```bash
# List installed skills
npx skills list | grep antigravity

# Antigravity global install location (README Fast Start)
ls ~/.gemini/antigravity/global_skills/ | head

# Project-scoped install location
ls .agent/skills/ | head
```

Review the exact instructions before installing: fetch a skill directly from the repo, for example `https://raw.githubusercontent.com/omer-metin/skills-for-antigravity/main/skills/game-ui-design/SKILL.md` (verified reachable Oct 10, 2026).

## Security

skills.sh verdicts for sampled skills (verified Oct 10, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| game-ui-design | Pass | Pass | Pass |
| quantitative-research | Pass | Pass | Pass |
| pixel-art-sprites | Pass | Pass | Pass |

## Limitations

- 96 listings is the skills.sh API page cap; the README claims 462+ skills, so most of the collection is not covered by the install counts in this guide.
- Verdicts cover three sampled skills only; the rest of the collection is unaudited here, so re-check each skill's security page on skills.sh before production use.
- Independent community project: 163 stars, no company backing, and the last push was Jan 2026, so validate quality per skill before relying on it.
- The content is converted from the third-party Vibeship Spawner Skills YAML dataset with AI-assisted repairs; provenance traces to that source, and Apache-2.0 applies to both.
- The index shows several near-duplicate entries (for example pixel-art at 446 installs alongside pixel-art-sprites at 2,396), so check for overlapping skills before installing both.
- No paid support or versioning guarantees; expect the set to move as the source dataset changes.

- Snapshot data, verified Oct 10, 2026: 25,624 combined installs across 96 indexed listings; 163 GitHub stars; Apache-2.0; last pushed 2026-01-22. Counts drift over time.

## Related

- [Claude Code Skills - Agentic Coding & Skill Development Setup](/hermes/skills/catalog/claude-code-skills-setup) - general skill-development workflows when authoring your own skills
- [Awesome Cursor Skills - Cursor Agent Setup](/hermes/skills/catalog/awesome-cursor-skills-setup) - agent-IDE skill collections for a different editor
- [Phaser 4 GameDev Skills Setup](/hermes/skills/catalog/phaser4-gamedev-setup) - browser game development with Phaser 4
- [GD Agentic Skills - Godot 4 Agent Setup](/hermes/skills/catalog/gd-agentic-skills-setup) - Godot 4 game development skills
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install by domain, not wholesale: copy only the game-dev or quant cluster you need instead of all 462+ folders.
- Antigravity reads skills from `~/.gemini/antigravity/global_skills/` (global) or `.agent/skills/` (project); keep project skills in the repo so they ship with the code.
- Start with the traffic leaders (game-ui-design, quantitative-research, pixel-art-sprites) - the most-installed skills in the set.
- Each skill is a single readable SKILL.md; audit it before relying on it in a workflow.
- Watch for near-duplicate entries across the index and prefer the higher-install variant when two skills overlap.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
