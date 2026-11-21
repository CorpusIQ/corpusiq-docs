---
title: "Dot Claude - Claude Code Skills Setup Guide"
description: "samhvw8/dot-claude: 40 Claude Code skills for coding agents - 6.2K combined installs spanning UI design, planning, Next.js, media and documents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/samhvw8-dot-claude-setup/"
robots: "index,follow"
last_updated: "2026-11-20"
tags: ["hermes skill", "agent skill", "skill setup", "claude code", "ui design", "developer tools"]
---

# samhvw8/dot-claude - Claude Code Skills Setup Guide

**Source:** [samhvw8/dot-claude](https://www.skills.sh/samhvw8/dot-claude) via skills.sh - 6.2K combined installs across 40 indexed listings; first seen Nov 20, 2026 (Nov 20, 2026 evening sweep)
**GitHub:** [samhvw8/dot-claude](https://github.com/samhvw8/dot-claude) - 12 stars, no license file declared (GitHub metadata reports none), main branch, last pushed Dec 9, 2025; skills under `skills/<name>/SKILL.md` (document skills under `document-skills/<name>/SKILL.md`) with Claude Code configuration in `agents/`, `hooks/` and `settings.json`.
**Category:** Claude Code Configuration
**Quality Tier:** 🟠 Orange - in the 15-skill sample, planning fails Gen Agent Trust Hub with a Snyk Warn and aesthetic carries a Snyk Warn.

`dot-claude` is a personal Claude Code configuration from samhvw8, published on skills.sh as a 40-skill library. The collection spans UI design systems, planning, full-stack Next.js with Turborepo, 3D graphics, media processing and Office document generation, with the canonical skills under `skills/<name>/SKILL.md` and the author's own agent, hook and settings files alongside.

The flagship ui-design-system leads the roster at 3,174 installs, covering React component systems built on TailwindCSS, Radix and shadcn/ui; the remaining 39 listings fall between 208 and 15 installs. The repository is small (12 stars) and dormant (last pushed Dec 9, 2025), so treat it as a personal, opinionated configuration rather than a maintained product.

## Installation

```bash
npx skills add samhvw8/dot-claude
```

Preview the available skills with `--list`, then install a subset with `--skill` selectors.

```bash
npx skills add samhvw8/dot-claude --list
npx skills add samhvw8/dot-claude --skill ui-design-system --skill planning
```

Update with `npx skills update` and remove with `npx skills remove <name>`. The repository also ships the author's own `agents/`, `hooks/` and `settings.json` files, which are personal Claude Code configuration and not part of the `skills` CLI install.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| ui-design-system | 3,174 | React UI component systems with TailwindCSS, Radix and shadcn/ui |
| ui-ux-design | 208 | UI/UX reference database: 50+ styles, palettes, font pairings, charts and stacks |
| project-planner | 184 | universal project planning for business, personal, creative and academic work |
| claude-md-architect | 153 | generating and optimizing CLAUDE.md files for Claude Code projects |
| nextjs-turborepo | 137 | full-stack Next.js 14+ with Turborepo monorepos and remote caching |
| aesthetic | 120 | visual design intelligence: hierarchy, color, typography and micro-interactions |
| mobile-development | 112 | cross-platform and native mobile apps (React Native, Flutter, Swift, Kotlin) |
| planning | 109 | technical implementation planning and architecture design |
| git-workflow | 97 | git workflow management with atomic commit principles |
| 3d-graphics | 88 | 3D web graphics with Three.js (WebGL/WebGPU) |
| google-adk-python | 85 | building AI agents with Google Agent Development Kit for Python |
| refactoring-expert | 83 | systematic code refactoring following Martin Fowler's catalog |
| prompt-enhancer | 81 | prompt engineering and token optimization for LLMs |
| media-processing | 81 | video/audio/image processing with FFmpeg and ImageMagick |
| mise-expert | 80 | mise development environment and tool version management |

The remaining 25 indexed listings range from 15 to 78 installs.

## Why This Matters for Hermes Agents

The library gives Hermes agents a broad, opinionated toolkit that maps to common build tasks: a design system and a design database for UI work, a technical planner and a project planner for scoping, and Next.js, mobile, backend and 3D-graphics skills for implementation. ui-design-system alone covers the full component pipeline, from TailwindCSS tokens through Radix primitives to shadcn/ui composition, which is the stack an agent needs to produce accessible, themeable interfaces instead of decoration-first output. claude-md-architect and prompt-enhancer tighten the loop between an agent and its own instructions, generating and optimizing CLAUDE.md context and compressing prompts to cut token spend. The planning and git-workflow skills impose structure, turning vague requests into roadmaps and commits into single-responsibility units. Because everything ships in the standard Agent Skills layout, the same skills install into any host that speaks the format rather than living in a single tool.

## Usage

| You say | What happens |
|---|---|
| Build a component library with dark mode and design tokens | ui-design-system reviews and builds accessible React components with TailwindCSS, Radix and shadcn/ui |
| Plan a mobile app with offline sync and push notifications | mobile-development lays out native vs cross-platform options and platform-specific concerns |
| Set up a Next.js monorepo with shared packages | nextjs-turborepo scaffolds the App Router app and configures Turborepo pipelines and caching |
| Write a CLAUDE.md for this codebase | claude-md-architect analyzes the project and generates optimized Claude Code instructions |
| Convert and compress a folder of videos and images | media-processing batches FFmpeg and ImageMagick conversion, resizing and transcoding |
| Plan a business launch end to end | project-planner structures goals, milestones, timeline and risk assessment |
| Improve this unclear prompt | prompt-enhancer restructures and compresses the prompt while preserving intent |

## Verification

```bash
# after install, confirm the skills landed in the agent skills directory
ls .agents/skills/
# review one skill before relying on it
curl -sL https://raw.githubusercontent.com/samhvw8/dot-claude/main/skills/ui-design-system/SKILL.md
```

The raw SKILL.md URL above was probed Nov 20, 2026 and returned HTTP 200. Skills live under `skills/<name>/SKILL.md` on the main branch; document skills use `document-skills/<name>/SKILL.md`.

## Security

skills.sh verdicts for sampled skills (verified Nov 20, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| ui-design-system | Pass | Pass | Pass |
| ui-ux-design | Pass | Pass | Pass |
| project-planner | Pass | Pass | Pass |
| claude-md-architect | Pass | Pass | Pass |
| nextjs-turborepo | Pass | Pass | Pass |
| aesthetic | Pass | Pass | Warn |
| mobile-development | Pass | Pass | Pass |
| planning | Fail | Pass | Warn |
| git-workflow | Pass | Pass | Pass |
| 3d-graphics | Pass | Pass | Pass |
| google-adk-python | Pass | Pass | Pass |
| refactoring-expert | Pass | Pass | Pass |
| prompt-enhancer | Pass | Pass | Pass |
| media-processing | Pass | Pass | Pass |
| mise-expert | Pass | Pass | Pass |
| backend-development | Pass | Pass | Pass |
| sequential-thinking | Pass | Pass | Pass |
| frontend-development | Warn | Pass | Pass |
| payment-integration | Pass | Pass | Warn |
| infra-engineer | Fail | Warn | Pass |

## Limitations

- Snapshot data, verified Nov 20, 2026: 6,182 combined installs across 40 indexed listings; 12 GitHub stars; no license file declared (GitHub metadata reports none); last pushed Dec 9, 2025. Counts drift over time.
- The repository has no top-level LICENSE file, so it declares no overall reuse terms; individual skills carry an MIT field in their frontmatter (ui-design-system, for example).
- The repository has not been pushed since Dec 9, 2025, nearly a year before this snapshot, so it is dormant and unlikely to receive updates.
- skills.sh sampled security verdicts for only 20 of the 40 listings; the other 20 are unverified on that platform.
- The docx, pdf, pptx and xlsx listings live under a `document-skills/<name>/SKILL.md` tree rather than the flat `skills/<name>/` layout.

## Related

- [Better Web UI - Frontend Design Skills Setup](/hermes/skills/catalog/aladicf-better-web-ui-setup)
- [Next.js Agent Skills - App Router Setup](/hermes/skills/catalog/nextjs-agent-skills-setup)
- [Code Review Skill - Review Workflow Setup](/hermes/skills/catalog/code-review-skill-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start from ui-design-system for any UI work; it is the collection's flagship and carries the most guidance.
- Preview with `--list` and install only the skills you need rather than the full 40.
- Treat the `agents/`, `hooks/` and `settings.json` files as the author's personal config, not as installable defaults.
- Re-check the skills.sh security pages before production use; two of the top fifteen skills carry Warn or Fail verdicts.
- Confirm licensing with the author before redistributing, since the repo has no top-level LICENSE file.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
