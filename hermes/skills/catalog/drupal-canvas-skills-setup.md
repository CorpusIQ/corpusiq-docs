---
title: "Drupal Canvas Skills - Code Components Setup"
description: "drupal-canvas/skills - 2.8K combined installs: agentic skills for developing Drupal Canvas Code Components."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/drupal-canvas-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-26"
tags: ["hermes skill", "agent skill", "skill setup", "drupal", "canvas", "code components"]
---

# Drupal Canvas Skills - Setup Guide

**Source:** [drupal-canvas/skills](https://www.skills.sh/drupal-canvas/skills) via skills.sh - 2.8K combined installs across 17 indexed listings; first catalogued Nov 26, 2026 (Nov 26, 2026 morning sweep)
**GitHub:** [drupal-canvas/skills](https://github.com/drupal-canvas/skills) - 3 stars, MIT license, last pushed Sep 25, 2026, main branch; 14 skill folders under skills/<name>/SKILL.md.
**Category:** Drupal Canvas Code Components
**Quality Tier:** 🟡 Yellow - 13 of 17 listings sampled: twelve pass all three checks, and canvas-navigation-components carries a single Socket Warn.

drupal-canvas/skills is the official collection of agentic skills for developing Drupal Canvas Code Components, the React/JSX component model for Drupal's Canvas page builder. Each skill encodes one part of the Canvas workflow: the canonical component contract, component.yml metadata, JSON:API data fetching, Tailwind styling, and the push path into Drupal Canvas.

All 14 skills with a matching skills/<name>/SKILL.md in the current tree follow the Agent Skills format. The install index lists 17 listings; three of them (canvas-component-upload, canvas-slots-for-repeatable-content, and canvas-component-naming) carry install counts but have no matching directory in the current tree.

## Installation

The README documents a single command via the skills CLI:

```bash
npx skills add drupal-canvas/skills
```

Skills follow the Agent Skills format and live under skills/<name>/SKILL.md, several with a references/ subdirectory (for example canvas-component-definition/references/naming.md and canvas-design-decomposition/references/granularity.md). The repository is MIT-licensed.

## What It Provides

skills.sh publishes per-skill install counts for all 17 indexed listings. The 8 most-installed skills are listed below; the remaining 9 are summarized under the table.

| Skill | Installs | Use For |
|---|---|---|
| canvas-component-metadata | 260 | define valid component.yml metadata for Canvas components, including props, slots, and enums |
| canvas-component-definition | 260 | start here for any Canvas component task to enforce the canonical component contract |
| canvas-data-fetching | 239 | fetch and render Drupal content with JSON:API and SWR patterns |
| canvas-component-composability | 237 | design Canvas-ready components with slots and decomposition-first patterns |
| canvas-styling-conventions | 234 | style components with Tailwind CSS 4 theme tokens and approved utility patterns |
| canvas-component-utils | 226 | use utility components to render formatted text and media correctly |
| canvas-component-push | 205 | push validated component changes to Drupal Canvas and recover from push failures |
| canvas-workbench | 201 | verify work in local Canvas Workbench and run component mocks and page previews |

The remaining 9 indexed listings range from 7 to 198 installs.

## Why This Matters for Hermes Agents

This suite hands an agent the full contract for a component-driven Drupal frontend instead of leaving it to improvise. canvas-component-definition and canvas-component-metadata pin down the exact component.yml shape, prop/slot structure, and enum mappings, so generated components validate on first push rather than failing on a "not a valid choice" error. canvas-data-fetching encodes the JSON:API and SWR patterns for fetching Drupal content, including the rule that every generated request must be executed and verified before rendering logic is written against it. canvas-component-composability and canvas-design-decomposition enforce decomposition-first structure, and canvas-component-push plus canvas-workbench close the loop by validating changes locally before pushing to Drupal Canvas. The suite is narrow in scope: it is Canvas-only, not a general Drupal toolkit, and its 3-star GitHub footprint means it is young and lightly community-tested.

## Usage

| You say | What happens |
|---|---|
| Build a new Canvas component | Uses canvas-component-definition to enforce the component contract, then canvas-component-metadata for the component.yml |
| Add data to a component | Uses canvas-data-fetching with JSON:API and SWR patterns to fetch and render Drupal content |
| Style this component | Uses canvas-styling-conventions with Tailwind CSS 4 theme tokens and CVA variants |
| Decompose this screen into components | Uses canvas-design-decomposition to plan props/slots and component granularity |
| Push my component to Canvas | Uses canvas-component-push to push validated changes and recover from push failures |
| Check it in the Workbench | Uses canvas-workbench to start the local dev server and verify mocks and previews |
| Render text and images correctly | Uses canvas-component-utils for the FormattedText and Image utility components |

## Verification

Confirm the README and a representative skill body resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/drupal-canvas/skills/main/README.md | head -40
curl -sL https://raw.githubusercontent.com/drupal-canvas/skills/main/skills/canvas-component-definition/SKILL.md | head -40
```

Both URLs return 200. After installing, review each skills/<name>/SKILL.md before relying on it, and re-check the security pages on skills.sh for the Warn verdict noted below.

## Security

skills.sh verdicts for sampled skills (verified Nov 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| canvas-component-metadata | Pass | Pass | Pass |
| canvas-component-definition | Pass | Pass | Pass |
| canvas-data-fetching | Pass | Pass | Pass |
| canvas-component-composability | Pass | Pass | Pass |
| canvas-styling-conventions | Pass | Pass | Pass |
| canvas-component-utils | Pass | Pass | Pass |
| canvas-component-push | Pass | Pass | Pass |
| canvas-workbench | Pass | Pass | Pass |
| canvas-page-definition | Pass | Pass | Pass |
| canvas-design-decomposition | Pass | Pass | Pass |
| canvas-navigation-components | Pass | Pass | Warn |
| canvas-content-templates | Pass | Pass | Pass |
| canvas-regions | Pass | Pass | Pass |

Across the 13 sampled skills there are 38 Pass, 1 Warn, and 0 Fail cells. Twelve skills pass all three checks; canvas-navigation-components carries the single Warn (Socket).

## Limitations

- Snapshot data, verified Nov 26, 2026: 2,805 combined installs across 17 indexed listings; 3 GitHub stars; MIT license; last pushed Sep 25, 2026. Counts drift over time.
- The install index outruns the tree: canvas-component-upload, canvas-slots-for-repeatable-content, and canvas-component-naming carry install counts but have no matching skills/<name>/SKILL.md in the current tree.
- skills.sh sampled only 13 of the 17 indexed listings; canvas-headless, canvas-component-upload, canvas-slots-for-repeatable-content, and canvas-component-naming carry no published verdict.
- The suite is Canvas-only and carries 3 GitHub stars; it is young and narrowly scoped to Drupal Canvas Code Components, not a general Drupal toolkit.
- Installs cluster around 200-260 for the core skills and drop sharply to single digits for the newest listings.

## Related

[WordPress Agent Skills - Audit and Optimize Setup](/hermes/skills/catalog/agent-skills-wordpress-setup) | [Drupal Claude Skills - Drupal Development Setup](/hermes/skills/catalog/drupal-claude-skills-setup) | [Drupal AI - Drupal 11 Toolkit Setup](/hermes/skills/catalog/drupal-ai-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with canvas-component-definition for any new component, then add canvas-component-metadata before writing the implementation.
- Run canvas-design-decomposition before building so props/slots and granularity are decided up front.
- Treat canvas-data-fetching's rule literally: execute and verify every generated JSON:API request before writing rendering logic against it.
- Use canvas-workbench to validate locally before canvas-component-push, which is only for explicit push/publish/sync requests.
- The region APIs are deprecated; prefer page variants and composed page trees via canvas-page-definition instead of canvas-regions.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
