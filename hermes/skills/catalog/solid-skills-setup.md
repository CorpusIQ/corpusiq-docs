---
title: "Solid Skills - SOLID and TDD Coding Standards"
description: "ramziddin/solid-skills - 3.7K combined installs across 1 indexed listing: SOLID, TDD, clean code, code smells, design patterns and clean architecture."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/solid-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-15"
tags: ["hermes skill", "agent skill", "skill setup", "solid", "tdd", "typescript", "code quality"]
---

# Solid Skills - Setup Guide

**Source:** [ramziddin/solid-skills](https://www.skills.sh/ramziddin/solid-skills) via skills.sh - 3.7K combined installs across 1 indexed listing; first seen Nov 15, 2026 (Nov 15 evening sweep)
**GitHub:** 634 stars, no LICENSE file, `main` branch, last pushed 2026-09-03, `skills/solid/SKILL.md`
**Category:** Software engineering discipline for TypeScript and NestJS
**Quality Tier:** 🟡 Yellow - the repository ships no license file.

Solid Skills is a single-skill publisher that packages one `solid` skill carrying reference files for SOLID principles, TDD, clean code, code smells, design patterns and clean architecture. It aims primarily at TypeScript and NestJS projects but applies to any object-oriented codebase.

The skill enforces a TDD workflow (write the failing test first), detects and fixes code smells, and applies SOLID principles to every class and function. It also keeps methods under 10 lines and classes under 50 lines.

## Installation

```bash
npx skills add ramziddin/solid-skills
```

The skill is available automatically once installed; the agent uses it when relevant tasks are detected.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| solid | 3,673 | SOLID, TDD, clean code, code smells, design patterns and clean architecture reference files for TypeScript and NestJS. |

No indexed listings fall below the threshold; the one indexed listing appears above.

## Why This Matters for Hermes Agents

The skill turns "write clean code" from a vague instruction into concrete checks: red-green-refactor, single responsibility, meaningful names, value objects for IDs and money. Agents respond to those specifics better than to a general ask.

The reference files cover the whole review cycle, so one skill supports writing, refactoring, reviewing and designing. A Hermes agent can apply the same standard when adding a feature, cleaning a service or sketching an architecture.

The TDD emphasis is the highest-leverage part: an agent that writes the failing test first produces code with a built-in safety net, which matters when the work runs unattended.

## Usage

| You say | What happens |
|---|---|
| "Implement a user registration feature" | The agent applies TDD and SOLID principles while building the feature. |
| "Refactor this service to follow SOLID principles" | It restructures the code against single responsibility and dependency inversion. |
| "Review this code for quality issues" | It flags code smells and suggests fixes from the reference files. |
| "Add tests for this module" | It writes tests first, following the red-green-refactor cycle. |
| "Design the architecture for a payment system" | It applies clean architecture, vertical slicing and the dependency rule. |

## Verification

```bash
curl -fsSL https://raw.githubusercontent.com/ramziddin/solid-skills/main/skills/solid/SKILL.md | head -40
npx skills add ramziddin/solid-skills
```

The SKILL.md sits under `skills/solid/`; the reference files live alongside it in `references/`.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-15) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| solid | Pass | Pass | Pass |

The skill is Markdown reference material with no runtime dependencies, and all three auditors pass it. The license is the open concern: the repository ships no LICENSE file even though the README states MIT (see Limitations).

## Limitations

- Snapshot data, verified 2026-11-15: 3,673 combined installs across 1 indexed listing; 634 GitHub stars; no LICENSE file; last pushed 2026-09-03. Counts drift over time.
- The repository has no LICENSE file even though the README states MIT: treat it as unlicensed until the maintainer adds one.
- Guidance targets TypeScript and NestJS; other ecosystems get the principles with fewer concrete examples.
- One skill covers a wide surface, so depth comes from the nine reference files rather than per-domain specialists.

## Related

- [Matt Pocock Engineering Skills - Setup Guide for Hermes Agents](/hermes/skills/catalog/matt-pocock-engineering-setup)
- [Actionbook Rust Skills - Rust Guidelines Setup](/hermes/skills/catalog/actionbook-rust-skills-setup)
- [AI Dev Standards Skills - Design Setup](/hermes/skills/catalog/ai-dev-standards-skills-setup)
- [Cursor Plugins Skills - Engineering Discipline Suite Setup](/hermes/skills/catalog/cursor-plugins-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Ask for the failing test first when generating new code; the skill's TDD workflow depends on it.
- For TypeScript and NestJS projects the examples in the reference files apply directly.
- Use the same skill for review as for writing so the standard stays consistent across the team.
- Re-check the license status before any commercial use; the repository ships no LICENSE file.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
