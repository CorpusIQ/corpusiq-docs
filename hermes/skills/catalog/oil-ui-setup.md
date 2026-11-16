---
title: "Oil UI - Interface Design Skill for Agents"
description: "oil-oil/oil-ui - 4.7K combined installs across 1 indexed listing: design skill that recommends one direction or explores three distinct directions."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/oil-ui-setup/"
robots: "index,follow"
last_updated: "2026-11-15"
tags: ["hermes skill", "agent skill", "skill setup", "ui design", "design", "frontend"]
---

# Oil UI - Setup Guide

**Source:** [oil-oil/oil-ui](https://www.skills.sh/oil-oil/oil-ui) via skills.sh - 4.7K combined installs across 1 indexed listing; first seen Nov 15, 2026 (Nov 15 evening sweep)
**GitHub:** 3,422 stars, MIT license, `main` branch, last pushed 2026-11-15, `SKILL.md` at the repository root
**Category:** Interface and UI/UX design for AI coding agents
**Quality Tier:** 🟡 Yellow - Socket reports a warning on the sampled skill; re-check before production use.

Oil UI is a single-skill publisher that gives coding agents a working design process. The one indexed skill recommends a single clear visual direction and refines it against real-browser screenshots, or explores three genuinely distinct directions side by side when asked to compare.

The skill ships with a 117-example live gallery at ui.oiloil.org and is compatible with Claude Code, Cursor, Codex, Windsurf and any SKILL.md-compatible agent. A separate paid Oil UI Pro edition exists, and the README warns against installing both editions because they compete for the same requests.

## Installation

```bash
npx skills add oil-oil/oil-ui
```

It works immediately with no configuration. If Oil UI Pro is already installed, skip the open-source edition. For DeepSeek Harness the README lists a native plugin, dsh-oil-ui.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| oil-ui | 4,724 | Interface and UI/UX design: recommends one visual direction and refines it against real screenshots, or explores three distinct directions side by side. |

No indexed listings fall below the threshold; the one indexed listing appears above.

## Why This Matters for Hermes Agents

Generic models default to AI slop patterns such as glowing eyebrow pills, triple-nested cards and invented KPI metrics. Oil UI's process counteracts that by starting from something concrete (a material, a setting, an object) instead of vague adjectives like "minimal" or "bold".

The skill also forces real comparison. When asked for three directions, layout, typography, color and imagery may share at most one trait between any two, so the agent cannot quietly return the same design three times.

Finally, it trusts the real screen rather than the code. It opens desktop and mobile viewports, inspects screenshots, dispatches an isolated reviewer, and ends with a subtraction pass. That loop matters for Hermes agents because UI quality is judged on what renders, not what compiles.

## Usage

| You say | What happens |
|---|---|
| "Explore a few design directions for this course booking product" | The skill produces candidate directions and pages you can preview side by side. |
| "Create three designs with different typography and color" | It returns three genuinely distinct directions on a comparison page so you can choose. |
| "Polish this page using the project's existing design guidelines" | It refines the layout against the stated guidelines rather than imposing a new style. |
| "Review this homepage and explain what to change" | It inspects desktop and mobile screenshots and reports what to fix without editing files. |
| "Recreate this page from the screenshot and add a mobile layout" | It rebuilds the design from the image and adds the mobile viewport. |

## Verification

```bash
curl -fsSL https://raw.githubusercontent.com/oil-oil/oil-ui/main/SKILL.md | head -40
npx skills add oil-oil/oil-ui
```

The SKILL.md lives at the repository root, so the raw URL is the place to review the process before installing.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-15) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| oil-ui | Pass | Warn | Pass |

The skill runs a version check at most once every 10 minutes: it reads the public version list at ui.oiloil.org and uploads nothing from the project. Set OIL_NO_UPDATE_CHECK=1 to disable it. The Socket warning is the reason this guide carries a Yellow tier.

## Limitations

- Snapshot data, verified 2026-11-15: 4,724 combined installs across 1 indexed listing; 3,422 GitHub stars; MIT; last pushed 2026-11-15. Counts drift over time.
- Oil UI Pro is a separate paid edition; installing both editions makes them compete for the same requests.
- The open-source edition covers a new page from a blank start to a distinct design; existing-project renovation, deep polish and design-system consolidation are Pro features.
- The version check needs Python 3 and outbound access to ui.oiloil.org.
- One skill is a narrow surface: there is no motion or copy-editing coverage here (those live in separate oil-motion and oil-tone repos).

## Related

- [Emil Kowalski Skills - Design Engineering Suite Setup](/hermes/skills/catalog/emilkowalski-skills-setup)
- [Uizze UI Skills - Anti-UI-Slop Design Quality Setup](/hermes/skills/catalog/uizze-ui-skills-setup)
- [Bergside Design Skills - Design Systems Setup](/hermes/skills/catalog/bergside-awesome-design-skills-setup)
- [design-review - Visual UI Audit & Fix Setup](/hermes/skills/catalog/design-review-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Ask for directions explicitly when you want options; the default behavior recommends one direction for confirmation.
- Share brand assets, screenshots or the existing codebase up front so the skill starts from concrete material.
- Use the built-in comparison page to open candidates at actual size and switch between desktop and mobile before choosing.
- Keep .oil-ui out of version control; intermediate candidates and caches live there while final code writes to the project.
- Disable the update check with OIL_NO_UPDATE_CHECK=1 in air-gapped environments.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
