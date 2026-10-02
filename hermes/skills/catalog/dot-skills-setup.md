---
title: "Dot Skills - 96-Skill Agent Engineering Collection Setup"
description: "Setup guide for pproenca/dot-skills - 96 agent skills in the open Agent Skills format: Zod, Vitest, clean architecture, TypeScript. 30.6K+ installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/dot-skills-setup/"
robots: "index,follow"
last_updated: "2026-09-30"
tags: ["hermes skill", "agent skill", "skill setup", "software development", "agent skills", "typescript"]
---

# Dot Skills - 96-Skill Agent Engineering Collection Setup - Setup Guide

**Source:** [pproenca/dot-skills](https://github.com/pproenca/dot-skills) (211⭐, MIT, master branch, updated 2026-09-26)
**Skill:** `pproenca/dot-skills` (96 installable skills, 30.6K combined installs)
**Publisher:** pproenca
**Category:** Software Development / Agent Skills Collection
**Quality Tier:** 🟡 Beta (functional, author-tested, MIT - verified Sep 30, 2026)

Dot Skills is a collection of 96 agent skills that follow the open Agent Skills format, organized as one curated skill per directory under skills/.curated/. It covers the full TypeScript and React ecosystem with schema validation, testing, forms, animations, and architecture patterns, alongside general-purpose skills for debugging, code review, and feature architecture. With 30.6K combined installs it has the largest install base among multi-skill collections on skills.sh.

---

## Installation

```bash
# Full collection (all 96 skills)
npx skills add pproenca/dot-skills

# Or clone and browse the curated skills
git clone https://github.com/pproenca/dot-skills
```

Verify the indexed skills with `npx skills add pproenca/dot-skills --list`. The 211 SKILL.md files live under skills/.curated/<name>/.

## Roster - Top Skills of 96

| Skill | Installs | Does |
|---|---|---|
| zod | 6.6K | Schema validation and type inference with Zod |
| vitest | 4.1K | Testing patterns and configuration for Vitest |
| react-hook-form | 2.8K | Form state, validation, and submission patterns with React Hook Form |
| emilkowal-animations | 2.3K | High-craft UI animation patterns following Emil Kowalski's design approach |
| clean-architecture | 2.0K | Service boundaries, dependency direction, and layering patterns |
| nuqs | 2.0K | Type-safe URL search-parameter state management with nuqs |
| code-simplifier | 1.6K | Refactoring and complexity reduction for existing code |
| typescript | 1.5K | TypeScript configuration, typing patterns, and migration guidance |
| 88+ more | - | Next.js, Expo, MUI Base, MSW, design review, debug, feature architecture, iOS taste |

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Payload validation** | `zod` patterns for validating API and MCP responses before processing |
| **Frontend test coverage** | `vitest` for unit testing JS tooling and connector code |
| **UI polish** | `emilkowal-animations` raises animation quality on public-facing surfaces |
| **Architecture reviews** | `clean-architecture` for reviewing service boundaries during refactors |

## Limitations / Verification

- 96 skills with some overlap between general-purpose entries (debug, design-review, feature-arch)
- Repo layout uses skills/.curated/<name>/ rather than a root-level SKILL.md convention, so manual copying needs the nested path
- Some skills assume specific JS framework stacks (Next.js, Expo, React)
- Verify: `npx skills add pproenca/dot-skills --list` shows 96 skills

## Security

MIT license. No skills.sh security audits published (verified Sep 30, 2026):

| Audit | Verdict |
|---|---|
| Gen Agent Trust Hub | Not published |
| Socket | Not published |
| Snyk | Not published |

## Related

- [Skill From Masters Setup](/hermes/skills/catalog/skill-from-masters-setup)
- [Claude MPM Skills Setup](/hermes/skills/catalog/claude-mpm-skills-setup)
- [Skills Marketplace](/hermes/skills/marketplace)

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
