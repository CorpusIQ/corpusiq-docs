---
title: "Sumi - UX/UI Design Intelligence Skills Setup Guide"
description: "phazurlabs/sumi: UX/UI design intelligence skills for Claude Code - 4.0K combined installs across 47 listings for desktop apps, components and Figma."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/phazurlabs-sumi-setup/"
robots: "index,follow"
last_updated: "2026-11-20"
tags: ["hermes skill", "agent skill", "skill setup", "ux design", "ui design", "design systems"]
---

# Sumi - UX/UI Design Intelligence Skills Setup Guide

**Source:** [phazurlabs/sumi](https://www.skills.sh/phazurlabs/sumi) via skills.sh - 4.0K combined installs across 47 indexed listings; first seen Nov 20, 2026 (Nov 20, 2026 evening sweep)
**GitHub:** [phazurlabs/sumi](https://github.com/phazurlabs/sumi) - 59 stars, Apache-2.0 license, main branch, last pushed Oct 24, 2026; 45 skills under `skills/<name>/SKILL.md`, 38 `/sumi` slash commands and four agents (scout, art-director, ux-architect, critic) shipped as a Claude Code plugin.
**Category:** UX/UI Design
**Quality Tier:** 🟡 Yellow - 7 of the 8 parsed sampled skills are Pass across all three scanners, with a single Snyk Warn on figma-design-tool-workflows; the other 12 sampled listings were not parsed and no Fail appears.

`sumi` is a design-intelligence skill set from Phazur Labs that gives Claude Code measurable design judgment. It scopes the visual craft of shipping software: desktop and mobile app patterns, cognitive psychology and UX heuristics, component code with full state matrices, Figma design-to-code workflows, and a designer-grade visual scoring engine. The suite ships as a Claude Code plugin with a four-agent studio (scout, art-director, ux-architect, critic) that looks at real shipped work first, then builds and grades against it.

The repository indexes 47 skills on skills.sh, driven from a `/sumi:start` entry point that routes plain-language requests to the right skill so users never have to learn the names. Every fix is tied to a citable principle, and the README ships a before/after receipt that lifts a generic AI landing page from a Design Quality Score of 43 to 82 against four Awwwards winners.

## Installation

```text
/plugin marketplace add phazurlabs/sumi
/plugin install sumi@sumi-marketplace
/sumi:start
```

Pick a scope at install: user (all your projects), project (shared through `.claude/settings.json`), or local (yours, gitignored). `/sumi:start` asks what you are working on and picks the play. Restart Claude Code if the slash commands do not appear.

To hack on it:

```bash
git clone https://github.com/phazurlabs/sumi.git && claude --plugin-dir ./sumi
```

The `/inspo` capture flow adds a local Chrome and `puppeteer-core` (`npm i -D puppeteer-core`); Mobbin results need a Mobbin account and its MCP.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| desktop-app-design | 311 | desktop and enterprise app patterns: data-dense interfaces, dashboards, data tables, keyboard-first flows |
| cognitive-psychology-ux | 233 | Laws of UX, Gestalt principles, cognitive biases and mental models for grounded design decisions |
| component-patterns-code | 155 | production component code in React, SwiftUI and modern CSS with state matrices and ARIA |
| design-critique-case-studies | 149 | structured critique via the Liz Lerman process plus shipped-product deep-dives |
| figma-design-tool-workflows | 100 | Figma Auto Layout, variable modes, Dev Mode handoff and design-to-code pipelines |
| data-visualization-mastery | 53 | 50+ chart types, dashboards, data tables and accessible data presentation |
| icon-illustration-systems | 51 | icon grids, library selection, SVG optimization and accessible iconography |
| visual-design-mastery | 50 | visual quality scoring, canonical design rules, color science and composition |

The remaining 25 indexed listings range from 25 to 49 installs.

## Why This Matters for Hermes Agents

Agent-built interfaces ship with visible defaults: five font weights, pure black on white, a purple gradient, and one easing curve borrowed from nowhere. Sumi replaces those defaults with measured judgment, so an agent that would otherwise emit another generic landing page can instead ground each decision in a type scale, a palette, a rhythm and a curve. The scout agent pulls real references from Awwwards, Mobbin and MotionSites instead of working from memory, and the critic scores the build against those references, so quality becomes a comparison rather than a feeling. The skills span the full surface of interface work, from cognitive load and accessibility to data-dense dashboards, Figma design-to-code pipelines and a 10-dimension visual scoring rubric. Because every fix cites a principle, the guidance is auditable rather than hand-waved, which matters when an agent hands work to a client or a reviewer. The suite is a Claude Code plugin, so the same skills travel with the agent across projects without a separate install path.

## Usage

| You say | What happens |
|---|---|
| /sumi:start for a new landing page | Routes you to the right play without needing to learn the 45 skill names |
| /sumi:fix Card.tsx | Finds the AI tells and rewrites the design layer, citing a principle per fix |
| /sumi:inspo "landing page for a coffee roaster" | Scouts Awwwards and Mobbin references and builds a Reference Board |
| /sumi:grade | Scores the build against the references with a Design Quality Score from 0 to 100 |
| /sumi:audit src/ | Runs heuristics, cognitive load, flow, ethics and AI-tell checks |
| /sumi:figma | Converts a Figma design into code through a design-to-code pipeline |
| /sumi:a11y | Checks accessibility before shipping |

## Verification

```bash
# confirm the plugin is active inside Claude Code
/sumi:status
# review one skill before relying on it
curl -sL https://raw.githubusercontent.com/phazurlabs/sumi/main/skills/desktop-app-design/SKILL.md
```

The raw SKILL.md URL above was probed Nov 20, 2026 and returned HTTP 200. The canonical tree lives under `skills/<name>/SKILL.md`; 45 skills ship alongside 38 `/sumi` slash commands and four agents.

## Security

skills.sh verdicts for sampled skills (verified Nov 20, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| desktop-app-design | Pass | Pass | Pass |
| cognitive-psychology-ux | Pass | Pass | Pass |
| Mobile UX Design | not parsed | not parsed | not parsed |
| NNG UX Heuristics | not parsed | not parsed | not parsed |
| UI Visual Design System | not parsed | not parsed | not parsed |
| Interaction & Motion Design | not parsed | not parsed | not parsed |
| Design Systems Architecture | not parsed | not parsed | not parsed |
| Accessibility & Inclusive Design | not parsed | not parsed | not parsed |
| component-patterns-code | Pass | Pass | Pass |
| UX Research Methods | not parsed | not parsed | not parsed |
| design-critique-case-studies | Pass | Pass | Pass |
| Agentic AI & Generative UX | not parsed | not parsed | not parsed |
| UX Metrics & Measurement | not parsed | not parsed | not parsed |
| UX Ethics & Content Strategy | not parsed | not parsed | not parsed |
| figma-design-tool-workflows | Pass | Pass | Warn |
| Cross-Cultural & Internationalization UX | not parsed | not parsed | not parsed |
| Ambient Computing & Calm Technology | not parsed | not parsed | not parsed |
| data-visualization-mastery | Pass | Pass | Pass |
| icon-illustration-systems | Pass | Pass | Pass |
| visual-design-mastery | Pass | Pass | Pass |

## Limitations

- Snapshot data, verified Nov 20, 2026: 4,030 combined installs across 47 indexed listings; 59 GitHub stars; Apache-2.0 license; last pushed Oct 24, 2026. Counts drift over time.
- skills.sh indexes 47 listings, but 14 appear under Title Case display names (such as Mobile UX Design and NNG UX Heuristics) rather than their kebab-case directory names, so only 33 rows parse as plain skill slugs; the display-name listings map to the same skills under `skills/<name>/SKILL.md`.
- Only 8 of the 20 sampled listings carry skills.sh verdict cells; the other 12 read "not parsed" on that platform, so verdict coverage is partial and worth re-checking before production use.
- The README counts 45 skills, 38 commands and 195 reference files, while the skills.sh listing description says 43 skills, 168 references and 37 commands; the tree shows 45 skill directories and 38 command files, so the skills.sh description reads slightly stale.
- The repo's own AUDIT.md notes 54 of 84 extracted claims are not yet triaged, with conversion-optimization-patterns carrying the most risk; check its figures against a primary source before quoting them.

## Related

- [Design Review - UI Critique Setup](/hermes/skills/catalog/design-review-setup)
- [Design Judge Skills - Design Quality Scoring Setup](/hermes/skills/catalog/design-judge-skills-setup)
- [Cuellarfr Design Skills - Product Design Setup](/hermes/skills/catalog/cuellarfr-design-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run `/sumi:start` first on any task; it routes plain-language requests so you never need to learn the 45 skill names.
- Commit the `.sumi/` folder so the whole team inherits the direction, but keep `.sumi/refs` captures out of git (they are study material, not shipping assets).
- The `/inspo` capture flow needs a local Chrome and `puppeteer-core` (`npm i -D puppeteer-core`); Mobbin results need a Mobbin account and its MCP.
- Treat a `/sumi:grade` as a critique, not a verdict: the measurements are reproducible, the category scores are judgment.
- Before quoting figures from conversion-optimization-patterns, check them against a primary source; the repo's own audit flags that skill as the least triaged.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
