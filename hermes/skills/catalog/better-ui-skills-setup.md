---
title: Better UI Skills — Interface Polish Suite Setup Guide for Hermes Agents
description: "jakubkrehel/skills — 13 skills, 51.3K total installs. better-ui (8.6K), better-typography (8.3K), better-colors (8.0K), better-interface (6.2K), better-layout (6.2K), better-accessibility (6.1K), better-writing (6.1K), interface-review (1.6K), oklch color skills."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/better-ui-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-14"
tags: ["hermes skill", "agent skill", "skill setup", "ui design", "typography", "accessibility", "design polish"]
---

# Better UI Skills — Setup Guide

**Source:** [jakubkrehel/skills](https://skills.sh/jakubkrehel/skills)
**GitHub:** [jakubkrehel/skills](https://github.com/jakubkrehel/skills)
**Skills:** 13 skills · 51.3K total installs
**Category:** UI Design & Interface Polish
**First Seen:** August 14, 2026 evening sweep
**Quality Tier:** 🟡 Beta (community suite, hot on the leaderboard)

The Better UI suite encodes interface-polish discipline: better-ui (8.6K installs), better-typography (8.3K), better-colors (8.0K), better-interface (6.2K), better-layout (6.2K), better-accessibility (6.1K), and better-writing (6.1K), plus interface-review (1.6K) and OKLCH-based color skills. All six core skills were rising on the hot leaderboard during the sweep hour (+6 to +11 installs each). The suite is a focused alternative to heavyweight design systems — take an existing UI and make it genuinely better across type, color, layout, accessibility, and copy.

---

## Installation

```bash
npx skills add jakubkrehel/skills
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js + npx** | For the `skills add` installer |
| **A codebase or design to polish** | Skills apply to existing UI work |

## What It Provides

| Skill | Installs | Purpose |
|---|---|---|
| better-ui | 8.6K | General interface improvement pass |
| better-typography | 8.3K | Type hierarchy, measure, spacing, contrast |
| better-colors | 8.0K | Color palettes and contrast discipline |
| better-interface | 6.2K | Component-level interface refinement |
| better-layout | 6.2K | Spacing, alignment, grid structure |
| better-accessibility | 6.1K | A11y passes on existing UI |
| better-writing | 6.1K | Interface copy and microcopy |
| interface-review | 1.6K | Structured review of an interface |
| oklch-colors / oklch-skill / great-typography / great-interfaces / make-interfaces-feel-better | 1–3 | OKLCH color space workflows and polish meta-skills |

## Quick Start

1. `npx skills add jakubkrehel/skills`
2. "Run better-typography on the docs.corpusiq.io landing page styles"
3. "Apply better-accessibility to the signup flow"
4. "Do an interface-review of the dashboard and list the top 10 fixes"

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Docs site polish** | better-typography and better-colors on MkDocs theme overrides |
| **Frontend QA** | interface-review as a pre-deploy design pass on www.corpusiq.io |
| **Accessibility compliance** | better-accessibility for WCAG passes on public pages |
| **Marketing page copy** | better-writing for landing page microcopy |

## Limitations / Verification

- Guidance-oriented: the skills direct the agent's design judgment rather than generating assets
- Community-maintained; results vary by agent model — always review diffs before merge

```bash
npx skills list | grep -i better
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Emil Design Engineering](/hermes/skills/catalog/) — design engineering standards
- [Animation Vocabulary](/hermes/skills/catalog/) — motion design companion

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace](/hermes/skills/marketplace/) →*

*Powered by CorpusIQ*
