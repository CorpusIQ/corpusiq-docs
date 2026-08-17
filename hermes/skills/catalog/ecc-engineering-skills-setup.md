---
title: "ECC Engineering Skills — Enterprise Engineering Suite"
description: "affaan-m/ecc — 292 skills, 466.2K total installs. Enterprise engineering suite: frontend-patterns, backend-patterns, security-review, api-design, coding-standards, tdd-workflow, docker-patterns, postgres-patterns, deep-research, article-writing, seo, brand-voice, architecture-decision-records, living-docs-governance."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/ecc-engineering-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-14"
tags: ["hermes skill", "agent skill", "skill setup", "engineering standards", "code quality", "security review"]
---

# ECC Engineering Skills — Setup Guide

**Source:** [affaan-m/ecc](https://skills.sh/affaan-m/ecc)
**GitHub:** [affaan-m/ecc](https://github.com/affaan-m/ecc)
**Skills:** 292 skills · 466.2K total installs
**Category:** Engineering Standards & Full-Stack Development
**First Seen:** August 14, 2026 evening sweep
**Quality Tier:** 🟡 Beta (community suite, very large install base)

The ECC suite is one of the largest engineering skill collections on skills.sh. It encodes repeatable engineering practice across the full stack: pattern libraries for frontend and backend work, security review discipline, API design, coding standards, TDD workflows, Docker and Postgres patterns, database migrations, end-to-end testing, codebase onboarding, and architecture decision records. It also carries content and research skills (deep-research, literature-review, article-writing, seo, brand-voice, video-editing, market-research) and an agent governance layer (dev-team, council-multi-model, living-docs-governance, prompt-optimizer). Top skills run 2.0K to 2.3K installs each; the repo totals 466.2K installs.

---

## Installation

```bash
npx skills add affaan-m/ecc
```

The suite installs all 292 skills. Because the collection is large, install it in a dedicated workspace or review the skill list on the publisher page first and import only the skills you need.

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js + npx** | Required for the `skills add` installer |
| **Hermes Agent** | Any recent version; skills are plain markdown + scripts and work with any agent |
| **GitHub** | Optional — some skills reference repo workflows (codebase-onboarding, code-review tooling) |

## What It Provides

| Area | Representative Skills | Installs |
|---|---|---|
| Frontend | frontend-patterns, frontend-design-direction, frontend-slides, design-system | 2.0K–2.3K |
| Backend | backend-patterns, api-design, postgres-patterns, docker-patterns, database-migrations | 1.9K–2.2K |
| Quality & Security | security-review, coding-standards, tdd-workflow, python-testing, e2e-testing, accessibility | 1.9K–2.2K |
| Architecture | architecture-decision-records, nextjs-turbopack, codebase-onboarding | ~1.9K |
| Research & Content | deep-research, literature-review, article-writing, seo, brand-voice, video-editing, market-research | 1.9K–2.1K |
| Agent Governance | prompt-optimizer, dev-team, council-multi-model, living-docs-governance, orch-runtime, claude-api | 0–2.0K |

## Quick Start

1. `npx skills add affaan-m/ecc`
2. Try one skill end-to-end first, e.g. ask Hermes to apply the `coding-standards` skill to a small repo
3. Use `security-review` before merging auth- or payment-touching changes
4. Use `deep-research` + `market-research` for competitive and market analysis passes

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Docs & frontend work** | frontend-patterns, design-system, and accessibility on docs.corpusiq.io UI changes |
| **MCP server hardening** | security-review and coding-standards applied to mcp2.corpusiq.io code paths |
| **Content pipeline** | article-writing, seo, and brand-voice for docs and blog content |
| **Research sweeps** | deep-research and literature-review for the nightly ecosystem discovery cadence |
| **Decision hygiene** | architecture-decision-records for infra changes, living-docs-governance for runbook upkeep |

## Limitations / Verification

- Large install footprint (292 skills) — review the publisher page before installing everything
- Community-maintained: no vendor SLA; verify each skill against your own repo conventions before adopting
- Some governance skills (orch-runtime, evalview-agent-testing, claude-api) show near-zero installs — treat as experimental

```bash
# Verify install
npx skills list | grep -c ecc
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Firecrawl Skills Setup](/hermes/skills/catalog/firecrawl-skills-setup/) — research workflows
- [Review Loop Skill Setup](/hermes/skills/catalog/review-loop-skill-setup/) — review discipline

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace](/hermes/skills/marketplace/) →*

*Powered by CorpusIQ*
