---
title: "Claude MPM Skills - 96-Skill Dev Toolchain Collection Setup"
description: "Setup guide for bobmatnyc/claude-mpm-skills - 96 curated dev skills with progressive loading: Drizzle, Playwright, tRPC, LangChain. 26K+ installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/claude-mpm-skills-setup/"
robots: "index,follow"
last_updated: "2026-09-30"
tags: ["hermes skill", "agent skill", "skill setup", "software development", "toolchains", "claude code"]
---

# Claude MPM Skills - 96-Skill Dev Toolchain Collection Setup - Setup Guide

**Source:** [bobmatnyc/claude-mpm-skills](https://github.com/bobmatnyc/claude-mpm-skills) (76⭐, MIT, main branch, updated 2026-09-29)
**Skill:** `bobmatnyc/claude-mpm-skills` (96 installable skills, 26.1K combined installs)
**Publisher:** bobmatnyc
**Category:** Software Development / Toolchains
**Quality Tier:** 🟡 Beta (functional, author-tested, MIT license; wide coverage but low stars - verified Sep 30, 2026)

Claude MPM Skills is a curated library of 96 development skills spanning AI frameworks, databases, web toolchains, and testing. It uses progressive loading with toolchain detection, so agents pull in only the skills relevant to the stack they are working on instead of loading the full catalog. Coverage includes Drizzle and tRPC for TypeScript stacks, Playwright end-to-end testing, Tailwind CSS, Docker, and AI frameworks such as LangChain, LangGraph, and DSPy. With 26.1K combined installs it is one of the most widely adopted multi-skill collections on skills.sh.

---

## Installation

```bash
# Full collection (all 96 skills)
npx skills add bobmatnyc/claude-mpm-skills

# Or clone and pick the toolchain directories you need
git clone https://github.com/bobmatnyc/claude-mpm-skills
```

Verify the indexed skills with `npx skills add bobmatnyc/claude-mpm-skills --list`. The 174 SKILL.md files live under toolchains/, universal/, and data-science/.

## Roster - Top Skills of 96

| Skill | Installs | Does |
|---|---|---|
| drizzle | 4.4K | SQL schema design, queries, and ORM usage patterns for Drizzle |
| playwright-e2e-testing | 2.8K | End-to-end browser test authoring and debugging with Playwright |
| drizzle-migrations | 1.3K | Drizzle migration workflows: generate, apply, and roll back schema changes |
| tailwind-css | 1.2K | Tailwind utility-first styling patterns and class composition |
| trpc-type-safety | 1.1K | Type-safe tRPC client/server contracts and input validation |
| docker | 1.0K | Dockerfile authoring, compose setup, and container debugging |
| vitest | 907 | Unit and integration testing with Vitest |
| 88+ more | - | AI frameworks (LangChain, LangGraph, DSPy), databases (MongoDB, Elixir Ecto), OpenRouter, LinkedIn, session compression, vector search |

Note: `drizzle` appears twice in the skills.sh index (4.4K plus 1.6K installs) as a duplicate listing; the combined total counts both entries.

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **TypeScript stack work** | `drizzle` and `drizzle-migrations` cover schema and migration work when agents touch Postgres-backed services |
| **End-to-end verification** | `playwright-e2e-testing` guides browser-based verification of user-facing flows |
| **Frontend consistency** | `tailwind-css` and `trpc-type-safety` keep styling and API contracts consistent across projects |
| **AI framework patterns** | LangChain, LangGraph, and DSPy skills for agent-internal AI tooling evaluations |

## Limitations / Verification

- 76-star repo with 96 skills: coverage is wide but individual skills have limited community vetting
- `drizzle` appears twice in the skills.sh index (4.4K + 1.6K), a duplicate listing that inflates the combined total
- Progressive loading relies on toolchain detection; a stack the detector misses means relevant skills never load
- Verify: `npx skills add bobmatnyc/claude-mpm-skills --list` shows 96 skills

## Security

MIT license. No skills.sh security audits published (verified Sep 30, 2026):

| Audit | Verdict |
|---|---|
| Gen Agent Trust Hub | Not published |
| Socket | Not published |
| Snyk | Not published |

## Related

- [Skill From Masters Setup](/docs/hermes/skills/catalog/skill-from-masters-setup)
- [Dot Skills Setup](/docs/hermes/skills/catalog/dot-skills-setup)
- [Skills Marketplace](/docs/hermes/skills/marketplace)

---

*← [Skills Catalog](/docs/hermes/skills/catalog) | [Skills Marketplace](/docs/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
