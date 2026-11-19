---
title: "Oakoss Agent Skills - Curated Web Dev Skills Setup"
description: "oakoss/agent-skills: 15.7K combined installs across 96 listings; curated web development and DevOps skills hand-written against official documentation."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/oakoss-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-18"
tags: ["hermes skill", "agent skill", "skill setup", "web development", "devops"]
---

# Oakoss Agent Skills - Setup Guide

**Source:** [oakoss/agent-skills](https://www.skills.sh/oakoss/agent-skills) via skills.sh - 15.7K combined installs across 96 indexed listings; first seen Nov 18, 2026 (Nov 18, 2026 evening sweep)
**GitHub:** 25 stars, no LICENSE file, `main` branch, last pushed 2026-08-17. Each skill is one `SKILL.md` per directory under `skills/`.
**Category:** Web development and DevOps tooling
**Quality Tier:** 🟠 Orange - 5 Warns among 12 sampled verdicts (playwright, find-skills, brand-designer, content-humanizer, knowledge-graph-builder); no LICENSE file.

Oakoss Agent Skills is a curated collection of hand-written skills for the web stack: TanStack, React, Tailwind, shadcn/ui, Playwright, Vitest, Zod, and Drizzle, plus security, DevOps, and deployment skills. The README describes 112 skills while the skills.sh index carries 96 listings.

Each skill is hand-written and enriched against official documentation rather than auto-generated from docs. The highest-install skills concentrate in UI polish and Playwright browser automation, with a long tail spanning validation, logging, database security, and TypeScript patterns.

## Installation

The README installs through the `skills` CLI via pnpm:

```bash
# Browse and select skills interactively
pnpm dlx skills add oakoss/agent-skills

# Install all skills
pnpm dlx skills add oakoss/agent-skills --all

# Install specific skills
pnpm dlx skills add oakoss/agent-skills -s react-patterns tanstack-query shadcn-ui

# Install to a specific agent
pnpm dlx skills add oakoss/agent-skills -a claude-code

# Install globally (user-level)
pnpm dlx skills add oakoss/agent-skills -g
```

Preview the catalog with `pnpm dlx skills add oakoss/agent-skills --list`. Each skill is a plain `SKILL.md` under `skills/`, so any harness that loads skill files can consume them directly.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| ui-ux-polish | 572 | Iterative UI and UX polishing for web apps, including glassmorphism, bento grids, and WCAG accessibility audits. |
| playwright | 472 | Playwright browser automation, scraping, and tooling with locator strategies, assertions, stealth mode, and MCP integration. |
| coolify | 381 | Coolify self-hosted PaaS for deploying applications, databases, and services via REST API and Git integration. |
| application-security | 284 | Application security covering STRIDE threat modeling, OWASP Top 10, secure coding review, and compliance. |
| find-skills | 275 | Discover and install agent skills from the open ecosystem, enriching results with descriptions from skills.sh. |
| drizzle-orm | 260 | Drizzle ORM for type-safe SQL with PostgreSQL, MySQL, and SQLite, covering schemas, queries, relations, and migrations. |
| brand-designer | 239 | Create cohesive brand identities: logos, color palettes, typography systems, and brand guideline documents. |
| tailwind | 229 | Tailwind CSS v4 patterns and design systems: themes, components, dark mode, container queries, and shadcn/ui. |
| vitest-testing | 223 | Vitest unit, component, and integration testing with mocking, React Testing Library, and coverage. |
| content-humanizer | 223 | Make AI-generated prose sound natural by removing hedging, filler words, and over-qualification. |
| tanstack-form | 220 | TanStack Form v1 headless form state management for React with sync and async validation. |
| knowledge-graph-builder | 220 | Implement knowledge graphs for AI: ontology design, graph database selection, and hybrid graph-vector architecture. |
| zod-validation | 219 | Zod v4 schema validation for TypeScript covering objects, arrays, unions, coercion, transforms, and refinements. |
| pino-logging | 214 | Pino high-performance JSON logging for Node.js with transports, child loggers, redaction, and framework integrations. |
| database-security | 205 | Database security auditing with Row Level Security enforcement, zero-trust architecture, and forensic audit trails. |
| typescript-patterns | 200 | Advanced TypeScript patterns for strict mode: utility types, generics, discriminated unions, and modern JS idioms. |

The remaining 80 indexed listings range from 89 to 199 installs.

## Why This Matters for Hermes Agents

These skills cover the tooling an agent actually reaches for when building and shipping web apps: forms, queries, tests, logging, and deployment. What sets them apart is that each one is hand-written against the library's official documentation, so the guidance reflects current majors instead of a model's remembered API surface.

For Hermes agents, the security and QA skills are the most reusable: application-security, database-security, and vitest-testing encode real standards such as OWASP, Row Level Security, and React Testing Library that can be wired in as validation steps. The set is plain SKILL.md files, so any harness that loads skill files can use them directly.

## Usage

| You say | What happens |
|---|---|
| "Polish this UI to Stripe-level quality" | ui-ux-polish runs iterative enhancement cycles and audits accessibility and WCAG compliance. |
| "Scrape this site" | playwright handles locators, assertions, stealth mode, and authenticated sessions. |
| "Set up structured logging in Fastify" | pino-logging configures transports, request IDs, and redaction. |
| "Write a Zod schema for this API" | zod-validation covers objects, arrays, unions, coercion, and transforms. |
| "Audit my Postgres Row Level Security" | database-security reviews RLS policies and audit trails. |
| "Design a brand identity" | brand-designer produces logos, color palettes, and typography systems. |

## Verification

Probe one skill on the `main` branch before installing. It returns 200:

```bash
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/oakoss/agent-skills/main/skills/ui-ux-polish/SKILL.md
```

Then install:

```bash
pnpm dlx skills add oakoss/agent-skills
```

For a subset, use `-s` with skill names; for a single agent, use `-a claude-code`.

## Security

skills.sh verdicts for sampled skills (verified Nov 18, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| ui-ux-polish | Pass | Pass | Pass |
| playwright | Pass | Warn | Pass |
| coolify | Pass | Pass | Pass |
| application-security | Pass | Pass | Pass |
| find-skills | Warn | Warn | Warn |
| drizzle-orm | Pass | Pass | Pass |
| brand-designer | Pass | Pass | Warn |
| tailwind | Pass | Pass | Pass |
| vitest-testing | Pass | Pass | Pass |
| content-humanizer | Pass | Pass | Warn |
| tanstack-form | Pass | Pass | Pass |
| knowledge-graph-builder | Pass | Warn | Pass |

The sample covers 12 of the 96 indexed listings; find-skills warns in all three scanners, and playwright, brand-designer, content-humanizer, and knowledge-graph-builder each carry one Warn. The repo has no LICENSE file, so treat the skills as unlicensed until you confirm terms with the author.

## Limitations

- Snapshot data, verified Nov 18, 2026: 15,684 combined installs across 96 indexed listings; 25 GitHub stars; no LICENSE file; last pushed 2026-08-17. Counts drift over time.
- The README describes 112 skills while the skills.sh index carries 96 listings, so the index and the README do not agree on the full set.
- With no LICENSE file, the licence is unstated; treat the repo as all-rights-reserved unless you confirm terms with the author.
- The sample carries 5 Warns across playwright, find-skills, brand-designer, content-humanizer, and knowledge-graph-builder, with find-skills warning in all three scanners.
- The install uses pnpm dlx skills rather than npx skills.

## Related

- [Uncodixfy - Anti AI UI Pattern Skill](/hermes/skills/catalog/uncodixfy-setup)
- [Dembrandt Skills - Design System Judgment for Agents](/hermes/skills/catalog/dembrandt-skills-setup)
- [Claude Code Skills - Agentic Coding & Skill Development Setup](/hermes/skills/catalog/claude-code-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install a subset with -s instead of --all; the set is large and most projects only need a few skills.
- Use ui-ux-polish as an iterative loop rather than a one-shot pass.
- Preview the catalog with --list before committing to an install.
- For find-skills, note it warns in all three scanners; review what it installs before trusting it.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
