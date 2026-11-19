---
title: "Cuellar Design Skills - UX and Design Skills Setup"
description: "cuellarfr/design-skills: 4.3K combined installs across 12 listings; UX research, critique, accessibility, and design systems for coding agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/cuellarfr-design-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-19"
tags: ["hermes skill", "agent skill", "skill setup", "ux design", "accessibility", "design systems"]
---

# Cuellar Design Skills - Setup Guide

**Source:** [cuellarfr/design-skills](https://www.skills.sh/cuellarfr/design-skills) via skills.sh - 4.3K combined installs across 12 indexed listings; first seen Nov 19, 2026 (Nov 19, 2026 morning sweep)
**GitHub:** 127 stars, MIT licence, `main` branch, last pushed 2026-09-30. Ten skills under `skills/`, each a standalone `SKILL.md` plus `references/`, `templates/`, and `examples/` directories, and a single Claude Code plugin under `.claude-plugin/`.
**Category:** UX and product design
**Quality Tier:** 🟢 Green - no Warn or Fail among 12 sampled skills; MIT licence.

Cuellarfr Design Skills is a collection of ten UX and design skills for Claude Code, Cursor, Codex, and other agents. Each skill encodes an established framework with opinionated defaults: UX research, design critique, accessibility auditing, journey mapping, design systems, UX strategy, interaction design, design ops, UX writing, and design elevation.

The skills.sh install index reports 12 listings against the 10 skill directories: two listings carry display names rather than directory names. "Design Critique & Evaluation" (198 installs) is the README's display name for `design-critique`, and "Journey Mapping & Service Design" (184 installs) is the display name for `journey-mapping`, so those two are duplicates of the corresponding kebab-case listings, not additional skills.

## Installation

Install with npx skills:

```bash
npx skills add cuellarfr/design-skills
```

Install a single skill, list first, or install globally:

```bash
npx skills add cuellarfr/design-skills --list
npx skills add cuellarfr/design-skills --skill design-critique
npx skills add cuellarfr/design-skills -g
npx skills add cuellarfr/design-skills -a claude-code
```

All ten skills also ship as a Claude Code plugin:

```
/plugin marketplace add cuellarfr/design-skills
/plugin install design-skills@design-skills
```

Skills are model-invoked; call one directly with its namespace, for example `/design-skills:accessibility-audit`.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| ux-research | 450 | Plan, conduct, and analyze UX research: interview scripts, test plans, recruiting, qualitative analysis, and synthesis into personas and journey maps. |
| interaction-design | 443 | Design microinteractions, state machines, motion, and error prevention; specify how products respond to input across states. |
| ux-writing | 431 | Write user-centered, accessible interface microcopy (buttons, labels, errors, empty states) and voice-and-tone guidelines. |
| design-elevation | 427 | Elevate functional visual outputs (dashboards, decks, reports, web pages) into polished designs using Tailwind tokens and perceptual patterns. |
| accessibility-audit | 420 | Audit pages, components, and flows against WCAG 2.2 at A, AA, and AAA with severity assessment, code fixes, and audit reports. |
| ux-strategy | 417 | Connect design decisions to business outcomes: competitive analysis, opportunity mapping, Jobs to Be Done, and UX metrics. |
| design-systems | 401 | Build and document design systems: tokens, component specs, pattern libraries, naming conventions, and governance. |
| design-ops | 378 | Run design sprints, handoff, team rituals, documentation standards, and design QA processes. |
| design-critique | 323 | Evaluate UI designs against usability heuristics, UX laws, and interaction principles for structured, actionable critiques. |
| journey-mapping | 237 | Create customer journey maps, service blueprints, experience maps, and empathy maps with diagram-type guidance. |

The remaining 2 indexed listings range from 184 to 198 installs (Journey Mapping & Service Design at 184 and Design Critique & Evaluation at 198).

## Why This Matters for Hermes Agents

These skills give an agent deep knowledge of design frameworks instead of a generic assistant's taste. The consistent architecture matters for a harness like Hermes: each `SKILL.md` works standalone and pulls `references/`, `templates/`, and `examples/` on demand, so the agent gets frameworks, checklists, and fillable templates without a monolithic prompt.

The accessibility and critique skills are the highest-leverage pair for agent-authored UI. AI-generated interfaces are inaccessible by default; `accessibility-audit` covers automated, keyboard, screen reader, visual, and flow testing plus generation-time prevention, and `design-critique` returns feedback grounded in named principles rather than subjective opinion.

## Usage

| You say | What happens |
|---|---|
| "Audit this page for accessibility" | accessibility-audit runs the 5-layer WCAG 2.2 audit and generates a report with severity and code fixes. |
| "Critique this UI" | design-critique evaluates against heuristics, UX laws, and interaction patterns and returns specific, actionable feedback. |
| "Write the empty state and error copy for this form" | ux-writing produces purposeful, concise interface copy with voice and tone guidance. |
| "Make this dashboard look polished" | design-elevation applies Tailwind tokens and perceptual patterns to elevate the visual output. |
| "Map the customer journey for onboarding" | journey-mapping selects the diagram type and structures the map or service blueprint. |
| "Set up a design system for this app" | design-systems defines tokens, component specs, and governance. |

## Verification

Probe one skill on the `main` branch before installing. It returns 200:

```bash
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/cuellarfr/design-skills/main/skills/ux-research/SKILL.md
```

Then install the pack and ask your agent to run a critique or an accessibility audit.

## Security

skills.sh verdicts for sampled skills (verified Nov 19, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| ux-research | Pass | Pass | Pass |
| interaction-design | Pass | Pass | Pass |
| ux-writing | Pass | Pass | Warn |
| design-elevation | Pass | Pass | Pass |
| accessibility-audit | Pass | Pass | Pass |
| ux-strategy | Pass | Pass | Pass |
| design-systems | Pass | Pass | Pass |
| design-ops | Pass | Pass | Pass |
| design-critique | Pass | Pass | Pass |
| journey-mapping | Pass | Pass | Pass |
| Design Critique & Evaluation | not parsed | not parsed | not parsed |
| Journey Mapping & Service Design | not parsed | not parsed | not parsed |

skills.sh publishes no verdict for the two display-name listings (Design Critique & Evaluation, Journey Mapping & Service Design); the ten kebab-case skills are sampled Pass except one Warn on ux-writing.

## Limitations

- Snapshot data, verified Nov 19, 2026: 4,309 combined installs across 12 indexed listings; 127 GitHub stars; MIT licence; last pushed 2026-09-30. Counts drift over time.
- The install index outruns the repo tree: 12 indexed listings against 10 skill directories. "Design Critique & Evaluation" and "Journey Mapping & Service Design" are display-name duplicates of design-critique and journey-mapping with no separate directory.
- The two display-name listings carry no skills.sh security verdict (not parsed).
- Skills are model-invoked under the plugin, so a direct call needs the `design-skills:` namespace prefix.

## Related

- [UX UI Agent Skills - Design Gates for Coding Agents](/hermes/skills/catalog/ux-ui-agent-skills-setup)
- [UX Writing Skill - Interface Copy Setup](/hermes/skills/catalog/ux-writing-skill-setup)
- [Interface Design Skill - Non-Templated Product UI Setup](/hermes/skills/catalog/interface-design-skill-setup)
- [design-review - Visual UI Audit & Fix Setup](/hermes/skills/catalog/design-review-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the whole pack with `-g`; the ten skills are independent and the agent loads the right one per task.
- Run accessibility-audit before shipping any agent-generated UI; it is the highest-risk gap for AI-authored interfaces.
- Use design-critique for a structured second opinion: it cites the heuristic or law behind each finding.
- Reach for design-elevation for non-product artifacts (decks, dashboards, reports), not just web pages.
- The ux-writing skill traces back to content-designer's ux-writing-skill, so it complements the standalone UX Writing catalog entry rather than replacing it.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
