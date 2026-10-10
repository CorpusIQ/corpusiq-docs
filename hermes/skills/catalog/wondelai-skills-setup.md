---
title: "Wondelai Skills - Book Framework Business & Design Setup"
description: "Setup guide for wondelai/skills - 275.9K combined installs. 65 skills: 51 frameworks from bestselling business and design books plus 14 metaskills."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/wondelai-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-10"
tags: ["hermes skill", "agent skill", "skill setup", "business frameworks", "ux design", "software design"]
---

# Wondelai Skills - Setup Guide

**Source:** [wondelai/skills](https://www.skills.sh/wondelai/skills) via skills.sh - 275.9K combined installs across 65 indexed listings; first seen Oct 9, 2026 (extended-query probe)
**GitHub:** [wondelai/skills](https://github.com/wondelai/skills) (2,372 stars, MIT; pushed 2026-09-10; repo layout: one skills/<name>/SKILL.md per skill)
**Category:** Business Frameworks / Design / Content
**Quality Tier:** 🟡 Beta - 2,372-star MIT collection; curated frameworks from bestselling books; all sampled verdicts Pass; independent publisher

Wondel.ai Agent Skills is an independent collection of 65 agent skills: 51 expert frameworks distilled from bestselling business, design, and coding books and industry style guides, plus 14 metaskills that orchestrate them step by step. It supports Claude, Claude Code, Claude Cowork, Codex, Cursor, OpenClaw, and Hermes Agent, and the same content ships in the open Agent Plugins format.

The frameworks are packaged into ten Claude Code plugin collections (product-strategy, ux-design, marketing-cro, sales-influence, product-innovation, strategy-growth, team-motivation, code-craftsmanship, systems-architecture, and metaskills), while the metaskills cover guided journeys such as create-website, improve-code-quality, and conversion-optimization. Each metaskill keeps its state in the project's docs/ folder, so a journey survives across sessions.

---

## Installation

There are two practical install paths. Claude Code users get plugin collections from the repo's own marketplace; every other agentskills.io-compatible host, including Hermes Agent, Codex, Cursor, and OpenClaw, installs skills through the skills.sh CLI.

### Claude Code plugin marketplace

```text
/plugin marketplace add wondelai/skills
/plugin install ux-design@wondelai-skills
/plugin install code-craftsmanship@wondelai-skills
/plugin install metaskills@wondelai-skills
```

The other collections install the same way: product-strategy, marketing-cro, sales-influence, product-innovation, strategy-growth, team-motivation, and systems-architecture.

### skills.sh CLI

```bash
# Install all 65 skills globally
npx skills add wondelai/skills --all --global

# Or install individual skills
npx skills add wondelai/skills/web-typography --global
npx skills add wondelai/skills/jobs-to-be-done --global
```

Codex works with the same individual npx skills add commands, and the repo also ships a Codex plugin marketplace that auto-discovers in a clone.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| web-typography | 8,475 | Web typography principles and implementation |
| refactoring-ui | 8,194 | Practical UI design system for developers |
| ux-heuristics | 8,069 | Usability evaluation and principles |
| ios-hig-design | 7,306 | Native iOS app design guidelines |
| clean-architecture | 6,557 | The Dependency Rule: dependencies point inward |
| domain-driven-design | 6,547 | Model software around business domains |
| top-design | 6,522 | Award-level web design techniques from elite studios |
| jobs-to-be-done | 6,202 | JTBD framework for product innovation |
| microinteractions | 6,100 | Design triggers, feedback, and loops for interaction polish |
| clean-code | 5,988 | Readable, maintainable code through naming and small functions |
| refactoring-patterns | 5,788 | Named refactorings that improve structure safely |
| hooked-ux | 5,656 | Habit-forming product design |
| system-design | 5,623 | Scalable distributed systems: caching, scaling, load balancing |
| cro-methodology | 5,570 | Conversion rate optimization, evidence over best practices |
| software-design-philosophy | 5,536 | Managing complexity with deep modules |
| storybrand-messaging | 5,478 | Clear brand messaging built on story structure |
| negotiation | 5,340 | Tactical negotiation for high-stakes conversations |
| lean-startup | 5,268 | Build-Measure-Learn methodology for new products |
| pragmatic-programmer | 5,257 | DRY, orthogonality, tracer bullets, design by contract |
| influence-psychology | 5,219 | Persuasion science and ethical influence principles |
| hundred-million-offers | 5,175 | Grand Slam Offer creation: value, pricing, guarantees |
| obviously-awesome | 5,133 | Product positioning and market category choice |
| design-everyday-things | 5,080 | Affordances, signifiers, and feedback in design |
| lean-ux | 5,038 | Hypothesis-driven UX with rapid experiments |
| improve-retention | 5,018 | Behavior design for user retention (B=MAP) |

The remaining 40 indexed listings range from 860 to 4,981 installs.

## Why This Matters for Hermes Agents

These skills give an agent decision procedures instead of raw generation: each framework encodes a specific author's method, such as question sets, checklists, and evaluation criteria, that an agent can apply consistently across sessions. That matters because judgment is the hard part of product, design, and content work, and a framework keeps the agent from improvising when it is asked to review a landing page or position a product. The 14 metaskills go further by orchestrating the frameworks in sequence and keeping state in the project's docs/ folder, so a multi-phase journey like create-website survives context resets. Hermes Agent is explicitly listed among supported hosts, and installs flow through the same skills.sh pipeline used for other catalog entries, which keeps setup uniform. Because everything is MIT-licensed and stored as plain SKILL.md files, teams can read a framework and adapt it instead of treating it as a black box.

## Usage

| You say | What happens |
|---|---|
| "Our dashboard looks amateur" | refactoring-ui runs a practical UI review and suggests concrete fixes. |
| "Why do visitors not convert on this page?" | cro-methodology builds an objection and counter-objection table and proposes bold hypotheses. |
| "Help me position our product" | obviously-awesome works through competitive alternatives, unique value, and market category. |
| "Make our pricing more compelling" | hundred-million-offers applies the Value Equation to offers, pricing, and guarantees. |
| "Write better customer interview questions" | mom-test keeps the interview about their life, not your idea. |
| "Users sign up but do not come back" | improve-retention designs behavior change around B=MAP. |
| "We need to build a website from scratch" | create-website, a metaskill, orchestrates ten frameworks phase by phase. |

## Verification

Confirm the install by listing what the CLI installed:

```bash
npx skills list | grep -E "web-typography|jobs-to-be-done"
```

If you installed globally, narrow the list to global skills:

```bash
npx skills ls -g
```

Review a raw SKILL.md before installing (this URL returned 200 when checked on Oct 10, 2026):

```bash
curl -sL https://raw.githubusercontent.com/wondelai/skills/main/web-typography/SKILL.md
```

## Security

skills.sh verdicts for sampled skills (verified Oct 10, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| web-typography | Pass | Pass | Pass |
| refactoring-ui | Pass | Pass | Pass |
| ux-heuristics | Pass | Pass | Pass |

## Limitations

- Independent publisher rather than a first-party vendor toolchain; the last push was 2026-09-10, so check freshness for fast-moving topics such as browser performance.
- The frameworks are distilled summaries of commercial books and style guides; they are not substitutes for reading the source material.
- Only three skills (web-typography, refactoring-ui, ux-heuristics) are covered in the sampled verdict table; the other 62 were not sampled here.
- The /plugin install path is Claude Code-specific; other hosts should use the npx skills commands or the repo's Agent Plugins packaging.
- Metaskills write state into the project's docs/ folder; review what gets written before committing it.


- Snapshot data, verified Oct 10, 2026: 275,940 combined installs across 65 indexed listings; 2,372 GitHub stars; MIT; last pushed 2026-09-10. Counts drift over time.

## Related

- [Emil Kowalski Skills - Design Engineering Suite Setup](/hermes/skills/catalog/emilkowalski-skills-setup) - interface craft for the same design-minded audience.
- [Better UI Skills - Interface Polish Suite Setup](/hermes/skills/catalog/better-ui-skills-setup) - compare polish-focused UI workflows against refactoring-ui and top-design.
- [Design Judge Skills - Design Award Workflow Setup](/hermes/skills/catalog/design-judge-skills-setup) - judge-style review to pair with steve-jobs-design-review.
- [Content Strategy - Full Planning Framework Setup](/hermes/skills/catalog/content-strategy-setup) - planning frameworks that complement storybrand-messaging and one-page-marketing.
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with one framework on a real page or codebase; web-typography, refactoring-ui, and ux-heuristics have the deepest install base and the cleanest on-ramp.
- Use a metaskill (create-website, improve-code-quality, conversion-optimization) when you want a phased journey; it sequences the frameworks and asks the decision questions phase by phase.
- Prefer individual installs when you only need two or three frameworks; --all pulls the entire set of 65.
- The marketplace collections and the npx skills installs reference the same skills; pick one path per host to avoid duplicates.
- Browse skills.wondel.ai to read a skill before installing; each framework maps back to the book or style guide it came from.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
