---
title: "Product Skills - UX Design & Product Management Setup"
description: "uxcel-lab/product-skills: 7.8K combined installs across 59 listings; UX design and product management skills built from the Uxcel learning library."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/product-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-18"
tags: ["hermes skill", "agent skill", "skill setup", "ux design", "product management", "design audit"]
---

# Product Skills - Setup Guide

**Source:** [uxcel-lab/product-skills](https://www.skills.sh/uxcel-lab/product-skills) via skills.sh - 7.8K combined installs across 59 indexed listings; first seen Nov 18, 2026 (this sweep)
**GitHub:** 42 stars, MIT licence, `main` branch, last pushed 2026-07-02. The 59 skills live as one `SKILL.md` per directory under `ux/` and `pm/`, split across six UX categories and five product management categories.
**Category:** UX design and product management
**Quality Tier:** 🟢 Green - all 60 sampled verdict cells pass; MIT licence.

Product Skills is a toolkit of 59 UX design and product management skills for AI assistants, built from the Uxcel learning library. Each skill is a single `SKILL.md` of decision rules that changes how an assistant handles a design or product task: gating decisions on context, leading with prevention, auditing against real standards, and refusing to over-apply best practices.

The set splits into generative skills that build or modify work, evaluative audit skills that review existing work against a standard such as WCAG or Nielsen heuristics, and workflow skills that compose the other two into a full review or a build from scratch. Every skill links back to the Uxcel lessons it came from.

## Installation

The README offers three ways to install. As a Claude plugin, since the repo doubles as a plugin marketplace:

```bash
/plugin marketplace add Uxcel-Lab/product-skills
/plugin install uxcel@product-skills
```

With npx skills into Claude Code, Cursor, Codex, and other agents:

```bash
npx skills add Uxcel-Lab/product-skills
```

Or one skill at a time by copying its `SKILL.md` into your tool's skills directory (for example `ux/audits/heuristics/SKILL.md`), or by downloading the latest release archive.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| ux-heuristics-audit | 180 | Audit any UI against Nielsen's 10 usability heuristics and return a severity-rated issue list with concrete fixes. |
| ux-design-review | 176 | Run a holistic review of a screen, flow, or component that composes the relevant audit lenses into one prioritized report. |
| ux-mobile-responsiveness-audit | 168 | Audit a design for viewport reflow, touch targets, thumb reach, and mobile input ergonomics, with a severity-rated issue list. |
| ux-dashboard | 164 | Design or critique a dashboard, deciding which metrics earn a place and which chart fits each one. |
| ux-microcopy-audit | 157 | Audit interface copy such as labels, buttons, errors, and empty states against UX-writing standards, with concrete rewrites. |
| ux-inputs-and-forms | 154 | Design or critique forms and inputs: field selection, labels, layout, validation, error states, and submission. |
| ux-information-architecture-audit | 154 | Audit a sitemap, navigation tree, or category structure and return severity-rated findings on labeling and hierarchy. |
| ux-navigation | 153 | Design or critique navigation systems, matching the nav pattern to the information architecture and wayfinding needs. |
| ux-accessibility-audit | 153 | Run a structured WCAG 2.1 AA audit and return a prioritized issue list citing each violated criterion and a fix. |
| ux-layout-spacing-grids | 151 | Lay out a screen with disciplined spacing, sizing, and grids on one base unit, replacing arbitrary pixel values with a system. |

The remaining 49 indexed listings range from 114 to 148 installs.

## Why This Matters for Hermes Agents

For an agent that generates screens and product artifacts, the default failure mode is plausible output that is not actually good: flat lists of generic suggestions, every metric crammed onto a dashboard, arbitrary pixel spacing, and best practices applied everywhere. These skills replace that with judgment. Generative skills gate: they establish context, apply the always-true core, then surface context-dependent decisions with trade-offs.

Evaluative audit skills review work against a named standard and return severity-rated findings with concrete fixes, so they can be wired in as validation steps after any generation. Because every rule traces back to Uxcel course material, the guidance is grounded in documented craft rather than a model's defaults.

The skills are plain `SKILL.md` files, so any harness that loads skill files, including Hermes, can use them directly even though the one-line installers target the Claude plugin and npx skills.

## Usage

| You say | What happens |
|---|---|
| "Audit this dashboard for usability problems" | ux-heuristics-audit returns a severity-rated issue list tagged with the violated Nielsen heuristic and a fix. |
| "Review my signup flow" | ux-design-review establishes context once, runs the always-relevant lenses, and returns one prioritized report. |
| "Check this screen against WCAG" | ux-accessibility-audit returns findings that cite each violated WCAG criterion with severity and a fix. |
| "Design a checkout form" | ux-inputs-and-forms applies the always-true core: minimal fields, one column, labels outside inputs, inline validation. |
| "Lay out this settings screen with a spacing scale" | ux-layout-spacing-grids places every value on one base unit and aligns content to a grid. |
| "Review the labels and button copy on this page" | ux-microcopy-audit returns concrete rewrites against UX-writing standards. |
| "Does this screen work on phones?" | ux-mobile-responsiveness-audit checks viewport reflow, touch targets, thumb reach, and mobile readability. |

## Verification

Probe one skill on the `main` branch before installing. It returns 200:

```bash
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/uxcel-lab/product-skills/main/ux/audits/heuristics/SKILL.md
```

Then install the whole set as a Claude plugin, or with npx skills:

```bash
/plugin marketplace add Uxcel-Lab/product-skills
/plugin install uxcel@product-skills

npx skills add Uxcel-Lab/product-skills
```

For a single skill, add `--skill` by name:

```bash
npx skills add Uxcel-Lab/product-skills --skill ux-heuristics-audit
```

After install, ask your agent to review or build something and check the next response changes.

## Security

skills.sh verdicts for sampled skills (verified Nov 18, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| ux-heuristics-audit | Pass | Pass | Pass |
| ux-design-review | Pass | Pass | Pass |
| ux-mobile-responsiveness-audit | Pass | Pass | Pass |
| ux-dashboard | Pass | Pass | Pass |
| ux-microcopy-audit | Pass | Pass | Pass |
| ux-inputs-and-forms | Pass | Pass | Pass |
| ux-information-architecture-audit | Pass | Pass | Pass |
| ux-navigation | Pass | Pass | Pass |
| ux-accessibility-audit | Pass | Pass | Pass |
| ux-layout-spacing-grids | Pass | Pass | Pass |
| ux-tables | Pass | Pass | Pass |
| ux-landing-page | Pass | Pass | Pass |
| ux-aesthetics-audit | Pass | Pass | Pass |
| ux-iconography | Pass | Pass | Pass |
| ux-typography | Pass | Pass | Pass |
| ux-color | Pass | Pass | Pass |
| ux-microcopy | Pass | Pass | Pass |
| ux-dark-patterns-audit | Pass | Pass | Pass |
| ux-error-recovery | Pass | Pass | Pass |
| pm-product-spec | Pass | Pass | Pass |

The sample covers 20 of the 59 indexed listings; every cell in all three columns passes.

## Limitations

- Snapshot data, verified Nov 18, 2026: 7,762 combined installs across 59 indexed listings; 42 GitHub stars; MIT licence; last pushed 2026-07-02. Counts drift over time.
- The ten skills shown above carry most of the install volume; the other 49 indexed listings sit between 114 and 148 installs and are long-tail.
- Each skill compresses Uxcel course material into decision rules and links back to the courses for the full reasoning, so the deeper context lives on Uxcel rather than inside the `SKILL.md`.
- The one-line install commands target the Claude plugin and npx skills; outside those tools you copy individual `SKILL.md` files into your agent's skills directory.

## Related

- [Bergside Design Skills - Design Systems Setup](/hermes/skills/catalog/bergside-awesome-design-skills-setup)
- [Design Judge Skills - Design Award Workflow Setup](/hermes/skills/catalog/design-judge-skills-setup)
- [Impeccable Design Setup](/hermes/skills/catalog/impeccable-design-setup)
- [Ant Design Skills - Official antd Agent Suite Setup](/hermes/skills/catalog/ant-design-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start a broad request with ux-design-review; it composes the right audit lenses instead of forcing you to run each one by hand.
- Run the audit skills as a validation step after generating UI; they are safe to auto-run and return severity-rated fixes.
- Try one skill first by copying a single SKILL.md (for example ux/audits/heuristics/SKILL.md) into your skills directory.
- For forms, trust the always-true core (minimal fields, one column, labels outside inputs) before adding multi-step splitting or floating labels.
- Install a subset with npx skills add Uxcel-Lab/product-skills --skill <name> instead of pulling all 59 at once.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
