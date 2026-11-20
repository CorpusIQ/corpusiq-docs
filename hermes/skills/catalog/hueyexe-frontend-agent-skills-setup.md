---
title: "Frontend Design Skills - UI Composition and UX Review"
description: "hueyexe/frontend-agent-skills: 9 frontend UX/UI design skills that stop AI-generated slop - 6.1K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/hueyexe-frontend-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-19"
tags: ["hermes skill", "agent skill", "skill setup", "ux design", "frontend", "ui design"]
---

# Frontend Design Skills - Setup Guide

**Source:** [hueyexe/frontend-agent-skills](https://www.skills.sh/hueyexe/frontend-agent-skills) via skills.sh - 6.1K combined installs across 9 indexed listings; first seen Nov 19, 2026 (Nov 19, 2026 evening sweep)
**GitHub:** [hueyexe/frontend-agent-skills](https://github.com/hueyexe/frontend-agent-skills) - 25 stars, MIT licence, main branch, last pushed Aug 2, 2026. Skills live at the repository root as `<name>/SKILL.md` (9 directories), each with a `references/` subfolder.
**Category:** Frontend UX/UI Design
**Quality Tier:** 🟢 Green - all 9 sampled verdicts Pass; MIT licence.

This set of nine skills targets a specific problem: AI agents scaffold frontends fast but without taste, producing gradient-blob heroes, symmetrical three-column grids and weightless CTA buttons. Each skill injects one discipline of design thinking into an agent's workflow, so the output stops looking like it was assembled from a template. The nine cover visual composition, design systems, UX writing, information architecture, accessibility, usability foundations, interaction patterns, forms and checkout, and research and testing.

Every skill follows the same structure: a SKILL.md carrying decision frameworks, plus a references folder with anti-patterns, checklists, decision prompts and principle cards. That means the agent gets a framework for making design decisions that hold up when real users arrive, not a list of instructions to repeat.

## Installation

```bash
npx skills@latest add hueyexe/frontend-agent-skills
```

Works with Claude Code, Cursor, OpenCode, Kiro and anything that supports the skills format.

Install all nine, or pick what you need:

```bash
npx skills@latest add hueyexe/frontend-agent-skills --skill ui-visual-composition
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| ui-visual-composition | 834 | Hierarchy, spacing, typography, color, depth, imagery and visual states |
| design-systems-frontend-architecture | 740 | Design tokens, component contracts, responsive layouts and CSS strategy |
| ux-writing-content-design | 690 | Microcopy, labels, CTAs, empty states, errors and notifications |
| information-architecture-navigation | 679 | Navigation, labels, taxonomy, hierarchy, search and wayfinding |
| accessibility-inclusive-design | 679 | Keyboard flows, focus management, semantic structure and inclusive defaults |
| ux-usability-foundations | 675 | Affordances, feedback, constraints, error prevention and task flow |
| interaction-patterns-components | 633 | Pattern selection, component behavior and flow design |
| forms-inputs-checkout | 627 | Validation, error states, field grouping and checkout flows |
| ux-research-discovery-testing | 554 | Research planning, discovery interviews and usability tests |

All 9 indexed listings appear in the table above.

## Why This Matters for Hermes Agents

AI-generated frontends are fast and generic: gradient-blob heroes, symmetric grids, empty alt text, and a "Get Started" button with no visual weight. The problem is not speed but judgment, and these skills supply the judgment one concern at a time. Each one ships the same supporting structure, anti-patterns to avoid, checklists to verify against, decision prompts the agent asks before choosing, and principle cards that encode reusable behavior. That structure matters because it turns a one-shot instruction into a repeatable decision process that survives contact with real users. Coverage spans the whole surface, from visual composition and accessibility to forms and checkout, where the difference between a finished task and a closed tab lives. For an agent that already generates markup quickly, this is the layer that makes the output worth keeping.

## Usage

| You say | What happens |
|---|---|
| Make this landing page look less generic | The visual-composition skill fixes hierarchy, spacing, type and color |
| Design a checkout form | The forms skill groups fields, adds progressive disclosure and validates on blur |
| Audit this UI for accessibility | The accessibility skill checks keyboard flow, focus and semantic structure |
| Organize this app's navigation | The information-architecture skill builds task-based hierarchy and wayfinding |
| Write the empty state copy | The UX-writing skill produces clear microcopy instead of "Something went wrong" |
| Pick the right interaction pattern | The interaction-patterns skill selects a pattern instead of defaulting to a modal |
| Run usability tests with real users | The research skill plans interviews, tests and evidence-backed recommendations |

## Verification

```bash
# after install, confirm the skill directories landed
ls .skills/hueyexe/frontend-agent-skills/
# review one skill's instructions before relying on it
curl -sL https://raw.githubusercontent.com/hueyexe/frontend-agent-skills/main/ui-visual-composition/SKILL.md
```

The raw SKILL.md URL above was probed Nov 19, 2026 and returned HTTP 200.

## Security

skills.sh verdicts for sampled skills (verified Nov 19, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| ui-visual-composition | Pass | Pass | Pass |
| design-systems-frontend-architecture | Pass | Pass | Pass |
| ux-writing-content-design | Pass | Pass | Pass |
| information-architecture-navigation | Pass | Pass | Pass |
| accessibility-inclusive-design | Pass | Pass | Pass |
| ux-usability-foundations | Pass | Pass | Pass |
| interaction-patterns-components | Pass | Pass | Pass |
| forms-inputs-checkout | Pass | Pass | Pass |
| ux-research-discovery-testing | Pass | Pass | Pass |

## Limitations

- Snapshot data, verified Nov 19, 2026: 6,111 combined installs across 9 indexed listings; 25 GitHub stars; MIT licence; last pushed Aug 2, 2026. Counts drift over time.
- All nine indexed listings map to directories in the current tree, so there is no index-vs-tree drift to reconcile.
- The skills are prose frameworks, not code libraries; the value is in the decision guidance rather than any executable tooling, so an agent must be able to read and apply Markdown instructions.
- Install counts on skills.sh reflect the marketplace snapshot and will lag the repository's own usage.

## Related

- [Uizze UI Skills - Anti-UI-Slop Design Quality Setup](/hermes/skills/catalog/uizze-ui-skills-setup)
- [Better UI Skills - Interface Polish Suite Setup](/hermes/skills/catalog/better-ui-skills-setup)
- [UI/UX Pro Max - Design System Skill Pack Setup](/hermes/skills/catalog/ui-ux-pro-max-setup)
- [Impeccable Design Setup](/hermes/skills/catalog/impeccable-design-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Load `ui-visual-composition` first for any screen that looks "fine" but does not communicate; it is the highest-install skill and the broadest.
- Keep the references folders close: the checklists are quality gates and the anti-patterns are the fastest way to catch a templated layout.
- Run `accessibility-inclusive-design` and `forms-inputs-checkout` together on any data-entry flow; the overlap is where real users get stuck.
- Use the decision prompts in each skill before choosing a pattern, so the agent justifies a modal, a disclosure or a separate page instead of defaulting.
- Pair `ux-writing-content-design` with `ux-research-discovery-testing` when copy feels off; the research skill grounds the words in user evidence.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
