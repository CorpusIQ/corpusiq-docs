---
title: "Magento 2 Agent Skills - Adobe Commerce Suite"
description: "maxnorm/magento2-agent-skills: 7.5K combined installs across 30 listings, a Magento 2 and Adobe Commerce domain-skill suite for agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/magento2-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-14"
tags: ["hermes skill", "agent skill", "skill setup", "magento", "adobe commerce", "php"]
---

# Magento 2 Agent Skills - Setup Guide

**Source:** [maxnorm/magento2-agent-skills](https://www.skills.sh/maxnorm/magento2-agent-skills) via skills.sh - 7.5K combined installs across 30 indexed listings; first seen Nov 14, 2026 (this sweep)
**GitHub:** 32 stars, MIT license, `main` branch, last pushed 2026-01-24, 30 `SKILL.md` files in `skills/<name>/` folders
**Category:** Magento 2 / Adobe Commerce domain skills
**Quality Tier:** 🟢 Green - all six sampled verdicts pass; MIT license. Last pushed 2026-01-24.

Magento 2 Agent Skills is a suite of 30 specialized skills that give an agent domain expertise across the whole Magento 2 / Adobe Commerce workflow: core module development, frontend theming, performance, security, infrastructure and e-commerce data analysis. The skills are based on rubenzantingh's claude-code-magento-agents repository, adapted to the Cursor agent-skills format, and can run independently or delegate to each other when a generalist task needs a specialist.

The tree holds 30 `SKILL.md` files under `skills/<name>/`, one per listing, so the index and the repo agree exactly. The README documents each skill's domain with a "Use when" clause, which makes the whole set easy to reason about before installing.

## Installation

The README does not document a `npx skills` install command; it describes skills that Cursor's agent system invokes automatically when a task matches a skill's domain. Install them explicitly with the skills CLI:

```bash
npx skills add maxnorm/magento2-agent-skills --skill 'magento-hyva-specialist' -g
```

Install the full set of 30 with `--skill '*'` instead of a single name.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| magento-hyva-specialist | 875 | Build high-performance Magento 2 storefronts with the Hyva theme framework, Alpine.js and Tailwind CSS. |
| magento-code-reviewer | 496 | Review Magento 2 code for quality, security, performance and PSR-12 plus Magento coding-standard compliance. |
| magento-module-developer | 455 | Build maintainable, extensible Magento 2 modules following enterprise architecture patterns. |
| magento-performance-analyst | 447 | Run Magento 2 performance analysis and optimization across all system layers. |
| magento-frontend-developer | 418 | Build Magento 2 storefront frontends: layout XML, templates, JavaScript and CSS. |
| magento-xml-specialist | 392 | Write Magento 2 XML configuration: layout XML, dependency injection, system.xml and module definition. |

The remaining 24 indexed listings range from 148 to 272 installs.

## Why This Matters for Hermes Agents

Magento 2 is a sprawling framework where a single change touches PHP, XML configuration, layout, frontend JavaScript and cache/index state. A generic coding agent rarely carries the full map. These skills encode that map: module structure and service contracts, dependency injection in `di.xml`, layout XML, cron configuration, indexers and caches, and the storefront's Hyva, Alpine.js, KnockoutJS and RequireJS layers.

The suite is also opinionated about correctness. The code-reviewer and security-analyst skills push PSR-12, Magento coding standards and security hardening, so an agent that loads them produces pull requests that survive review rather than bounce on standards. The performance and cache skills turn a slow storefront investigation into a repeatable checklist instead of guesswork.

The hierarchical design is a third point: generalist skills delegate to specialists, so an agent does not have to hold all 30 in context at once. It loads the right specialist for the task and follows its process documentation and best practices.

## Usage

| You say | What happens |
|---|---|
| "Review this Magento 2 module" | Runs magento-code-reviewer over the code for quality, security and standards compliance. |
| "Build a new module from scratch" | Runs magento-module-developer for structure, service contracts and repository patterns. |
| "Why is the storefront slow?" | Runs magento-performance-analyst to find bottlenecks across the stack. |
| "Add a REST and GraphQL endpoint" | Runs magento-api-developer for service contracts, DTOs and authentication. |
| "Set up this module's di.xml and layout XML" | Runs magento-xml-specialist for dependency injection and layout configuration. |
| "Build a Hyva storefront" | Runs magento-hyva-specialist for Alpine.js and Tailwind CSS patterns. |

## Verification

Probe skills on the `main` branch before installing. All return 200:

```bash
curl -fsSL https://raw.githubusercontent.com/maxnorm/magento2-agent-skills/main/skills/magento-hyva-specialist/SKILL.md | head -12
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/maxnorm/magento2-agent-skills/main/skills/magento-code-reviewer/SKILL.md
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/maxnorm/magento2-agent-skills/main/skills/magento-xml-specialist/SKILL.md
```

Skills live at `skills/<name>/SKILL.md` on the `main` branch; keep the name exactly as listed when constructing raw URLs.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-14) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| magento-hyva-specialist | Pass | Pass | Pass |
| magento-code-reviewer | Pass | Pass | Pass |
| magento-module-developer | Pass | Pass | Pass |
| magento-performance-analyst | Pass | Pass | Pass |
| magento-frontend-developer | Pass | Pass | Pass |
| magento-xml-specialist | Pass | Pass | Pass |

All six sampled skills pass all three auditors. The sample covers 6 of the 30 indexed listings, so it says little about the remaining 24, which publish no verdict on skills.sh.

## Limitations

- Snapshot data, verified 2026-11-14: 7,538 combined installs across 30 indexed listings; 32 GitHub stars; MIT; last pushed 2026-01-24. Counts drift over time.
- The repo was last pushed 2026-01-24, roughly ten months before this snapshot; the guidance is stable but not actively refreshed, so pair it with current Adobe Commerce documentation for version-specific changes.
- The README documents Cursor auto-invocation but no `npx skills` command; the install line above is a fallback rather than a documented command.
- The security sample covers only 6 of 30 listings; the rest publish no verdict on skills.sh.
- The skills are prompt-only markdown with process documentation and references; verify any code they suggest against Adobe Commerce and Magento coding standards.

## Related

- [Hyva AI Tools - Magento Front-End for Agents](/hermes/skills/catalog/hyva-ai-tools-setup)
- [Adobe Skills - PDF, Document and Creative Suite Setup](/hermes/skills/catalog/adobe-skills-setup)
- [Awesome Ecommerce Skills - Commerce Index](/hermes/skills/catalog/awesome-ecommerce-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the full set with `--skill '*'` once, then let Cursor auto-invoke the right specialist per task.
- Start with magento-code-reviewer on an existing module to learn the review style before adopting the broader workflow.
- Pair the performance and cache skills when diagnosing a slow storefront; they cover different layers of the same investigation.
- The frontend skills overlap (Hyva, Luma, Alpine.js, KnockoutJS, RequireJS); pick the one matching your theme stack rather than loading all five.
- Keep the skills' "Use when" clauses in mind when delegating; the generalist-to-specialist handoff assumes each skill stays in its domain.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
