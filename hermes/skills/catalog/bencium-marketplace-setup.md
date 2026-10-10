---
title: "Bencium Marketplace - Design & Product Skills Suite Setup"
description: "Setup guide for bencium/bencium-marketplace - 53.1K combined installs. 17 design, UX, marketing, and productivity skills from bencium.io."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/bencium-marketplace-setup/"
robots: "index,follow"
last_updated: "2026-10-10"
tags: ["hermes skill", "agent skill", "skill setup", "design skills", "ux design", "claude code plugins"]
---

# Bencium Marketplace - Setup Guide

**Source:** [bencium/bencium-marketplace](https://www.skills.sh/bencium/bencium-marketplace) via skills.sh - 53.1K combined installs across 17 indexed listings; first seen Oct 9, 2026 (extended-query probe)
**GitHub:** [bencium/bencium-marketplace](https://github.com/bencium/bencium-marketplace) (446 stars, MIT; pushed 2026-10-04; per-skill plugin dirs: `<name>/skills/<name>/SKILL.md`, 16 SKILL.md files in the tree)
**Category:** Design / Product / Marketing
**Quality Tier:** 🟡 Beta - 446-star MIT marketplace; all sampled verdicts Pass; broad design/product/marketing scope

Bencium Marketplace is a Claude Code plugin marketplace by bencium.io carrying 17 skills and tools for design, marketing, architecture, and productivity. It was built around the Anthropic Skills guide plus bencium's own design and development philosophy, and its strongest entries attack a specific problem: AI-generated interfaces that all look the same.

The suite is organized into four families - Design (6), Marketing (1), Productivity (6 plus tools), and Development (4). Each plugin follows the standard Claude Code plugin layout, so skills install individually or as a set. A common starting point: pick one of the three UX designer variants for the job, then add design-audit and ui-typography to keep generated output sharp.

---

## Installation

### skills.sh (recommended)

```bash
# Browse all available skills
npx skills add bencium/bencium-marketplace --list

# Install all skills globally
npx skills add bencium/bencium-marketplace -g --all

# Install a specific skill
npx skills add bencium/bencium-marketplace -g --skill design-audit
```

### Claude Code plugin

Add the marketplace once, then install individual plugins:

```bash
/plugin marketplace add bencium/bencium-marketplace
/plugin install bencium-controlled-ux-designer@bencium-marketplace
```

### Other agents and editors

The SKILL.md format works with 40+ coding tools that support markdown skill files, including OpenAI Codex, Gemini CLI, Cursor, and Windsurf. For the Claude.ai Cowork app, copy a plugin's `skills/` directory into your project's `.claude/skills/` folder; for other tools, copy the skill files into the tool's prompt or context directory.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| bencium-innovative-ux-designer | 6,918 | Bold creative UX that commits to a distinctive direction; landing pages and campaigns |
| bencium-impact-designer | 5,005 | Production-grade frontend interfaces that avoid generic AI aesthetics |
| bencium-controlled-ux-designer | 4,384 | Systematic UX for enterprise and regulated products; WCAG 2.1 AA, mathematical scales, always-ask-first protocol |
| design-audit | 3,914 | Phased, implementation-ready visual UI/UX audit plans (visual only, functionality untouched) |
| ui-typography | 3,692 | Typography rules for generated code: correct quote marks, dashes, spacing, hierarchy |
| human-architect-mindset | 3,182 | Domain modeling, systems thinking, and AI-aware problem decomposition |
| bencium-aeo | 3,179 | Answer Engine Optimization for visibility in ChatGPT, Claude, Gemini, and AI Overviews |
| adaptive-communication | 3,133 | Adapting agent responses to high-context vs low-context communication styles |
| bencium-code-conventions | 3,124 | Code style and stack conventions for React/Next.js/TypeScript, TailwindCSS, Supabase |
| renaissance-architecture | 3,121 | First-principles software architecture, beyond derivative work |
| negentropy-lens | 3,095 | Decision support through an entropy (decay) vs negentropy (growth) lens |
| vanity-engineering-review | 3,030 | Reviewing code, architectures, PRs, and plans for ego-driven engineering |
| insurgent-campaign | 1,847 | Grassroots campaign design for teams outspent by incumbents; lift-test plans, no fabricated names |
| hungarian-humanizer | 1,143 | Removing AI-generated markers from Hungarian text (26 patterns plus 4 style markers) |
| eu-ai-act-reviewer | 612 | EU AI Act review workflows |
| organic-first-campaign | 603 | Organic-first campaign planning |

The remaining 1 indexed listing is Agentic UX Design - Relationship-Centric Interfaces (3,166 installs).

## Why This Matters for Hermes Agents

Agent builders increasingly generate frontend work, and the default failure mode of an LLM-built interface is sameness: interchangeable layouts, safe gradients, generic cards. This suite attacks that directly. bencium-innovative-ux-designer pushes a model to commit to a distinctive direction, while bencium-controlled-ux-designer does the opposite job for regulated products, holding output to WCAG 2.1 AA, mathematical scales, and an always-ask-first protocol. design-audit turns an existing UI into a phased, implementation-ready remediation plan an agent can execute step by step. ui-typography auto-applies correct quotes, spacing, and hierarchy inside generated HTML, CSS, and React. Because each plugin ships plain SKILL.md files under an MIT license, the same instructions load into any agent that reads markdown skill files.

## Usage

| You say | What happens |
|---|---|
| Make our landing page feel distinctive | bencium-innovative-ux-designer commits to a bold direction with shadows, gradients, and experimental typography |
| This healthcare flow must pass an accessibility review | bencium-controlled-ux-designer applies WCAG 2.1 AA, mathematical scales, and an always-ask-first protocol |
| Audit our dashboard's visual design before the next build phase | design-audit returns a phased, implementation-ready plan without touching functionality |
| Fix the typography in this generated React component | ui-typography enforces correct quote marks, spacing, and hierarchy automatically |
| Review this PR for over-engineering | vanity-engineering-review flags code built for ego rather than user value |
| Make our docs more citable by AI assistants | bencium-aeo optimizes content for answer-engine visibility |
| Plan a launch with no paid budget | insurgent-campaign audits spend asymmetry and assembles a grassroots channel stack with a lift-test plan |

## Verification

Confirm the install from the CLI or the skills directory:

```bash
npx skills list | grep bencium
```

In Claude Code, run `/plugin` and confirm the plugins you added appear (for example `bencium-controlled-ux-designer@bencium-marketplace`). Before installing, review the exact instructions the agent will read: each plugin ships its skill at `<plugin-name>/skills/<skill-name>/SKILL.md`. For example, fetch the controlled UX designer skill file at `https://raw.githubusercontent.com/bencium/bencium-marketplace/main/bencium-controlled-ux-designer/skills/bencium-controlled-ux-designer/SKILL.md` (verified reachable Oct 10, 2026).

## Security

skills.sh verdicts for sampled skills (verified Oct 10, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| bencium-innovative-ux-designer | Pass | Pass | Pass |
| bencium-impact-designer | Pass | Pass | Pass |
| design-audit | Pass | Pass | Pass |

## Limitations

- Verdicts cover three sampled skills only; the rest of the suite is unaudited here, so re-check each skill's security page on skills.sh before production use.
- Claude Code plugin extras (commands, hooks, the emotion-statusline hook, and the spinner-verbs bonus) are not SKILL.md skills and only travel with the full plugin install.
- The README and the indexed listings do not fully overlap: bencium-loop, relationship-design, and emotion-statusline appear in the README but not in the measured rows, while eu-ai-act-reviewer and organic-first-campaign appear in the listings.
- The marketplace is young (446 stars) and tracked as Beta; expect renames and layout churn between releases.
- MIT license per the repo; re-check the LICENSE and pin a revision when vendoring.

- Snapshot data, verified Oct 10, 2026: 53,148 combined installs across 17 indexed listings; 446 GitHub stars; MIT; last pushed 2026-10-04. Counts drift over time.

## Related

- [Emil Kowalski Skills - Design Engineering Suite Setup](/hermes/skills/catalog/emilkowalski-skills-setup) - motion and interaction craft that pairs with the bencium visual design skills
- [Better UI Skills - Interface Polish Suite Setup](/hermes/skills/catalog/better-ui-skills-setup) - finishing passes for generated interfaces
- [Design Judge Skills - Design Award Workflow Setup](/hermes/skills/catalog/design-judge-skills-setup) - evaluation-focused counterpart to design-audit
- [Uizze UI Skills - Anti-UI-Slop Design Quality Setup](/hermes/skills/catalog/uizze-ui-skills-setup) - another anti-slop quality layer for UI output
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Preview before installing: `npx skills add bencium/bencium-marketplace --list` shows everything; `-g --all` installs the whole set globally.
- Choose the UX variant by job: innovative for campaigns and landing pages, controlled for enterprise and regulated products, impact for production polish.
- Install ui-typography even if you never invoke it by name - it auto-applies to generated HTML, CSS, and React.
- In Claude Code, add the marketplace once and install plugins one at a time so each can be updated independently.
- The spinner-verbs JSON and the statusline hook are cosmetic extras; skip them if you only want skill content.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
