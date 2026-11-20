---
title: "NestJS Skills - Seven Agent Skills for NestJS Setup"
description: "Setup guide for amirtaherkhani/nestjs-skills: 3.6K combined installs across 7 listings; NestJS skills for architecture, OOP, audits and performance."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/amirtaherkhani-nestjs-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-19"
tags: ["hermes skill", "agent skill", "skill setup", "nestjs", "typescript", "code audit"]
---

# NestJS Skills - Setup Guide

**Source:** [amirtaherkhani/nestjs-skills](https://www.skills.sh/amirtaherkhani/nestjs-skills) via skills.sh - 3.6K combined installs across 7 indexed listings; first seen Nov 19, 2026 (Nov 19, 2026 evening sweep)
**GitHub:** 26 stars, Apache-2.0, `main` branch, last pushed 2026-11-19. Seven skills under `skills/`, each a SKILL.md with `references/` plus `evals/` and, for some, `agents/` and `scripts/`; a VitePress docs site, runnable examples, and an opt-in evaluation harness sit alongside.
**Category:** NestJS and TypeScript backend engineering
**Quality Tier:** 🟡 Yellow - Apache-2.0 license, no Fail cells; 3 Snyk Warn cells among 7 sampled verdicts (nestjs-professional-software-engineering, nestjs-features-performance, nestjs-git-commit-pr-message).

amirtaherkhani/nestjs-skills ships seven focused skills for working on real NestJS codebases. Each skill owns a distinct engineering decision: architecture, object design, professional implementation, runtime features and performance, whole-repo code audit, single-feature roadmap audit, and intentional Git publication. The suite is built on the Agent Skills open standard and targets Claude Code and Codex.

A defining design choice is the pre-execution conflict guard: every skill reconciles ownership before mutation, so when two active skills want incompatible file changes or architecture, the agent assigns one owner or stops for clarification. The three audit and architecture skills are read-only by design, while the implementation and Git skills are the mutation paths.

## Installation

Install the collection with the skills CLI:

```bash
npx skills add amirtaherkhani/nestjs-skills
```

Install one skill for both Claude Code and Codex:

```bash
npx skills add amirtaherkhani/nestjs-skills \
  --skill nestjs-professional-software-engineering \
  --agent claude-code \
  --agent codex
```

Preview available skills without installing:

```bash
npx skills add amirtaherkhani/nestjs-skills --list
```

The CLI installs project skills into `.claude/skills/` for Claude Code and `.agents/skills/` for Codex; add `--global` for a user-level install. Optional project rules can be copied into a checkout and merged with existing instructions:

```bash
cp integrations/codex/AGENTS.md ./AGENTS.md
cp integrations/claude/CLAUDE.md ./CLAUDE.md
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| nestjs-architecture-principles | 587 | Design and review NestJS architecture: feature modules, modular monoliths, layered or hexagonal boundaries, dependency inversion, and CQRS or microservices decisions. |
| nestjs-oop-design-patterns | 555 | Apply pragmatic OOP, SOLID, and design patterns to NestJS and TypeScript: controllers, providers, use cases, entities, repositories, and factories. |
| nestjs-professional-software-engineering | 551 | Implement, refactor, debug, review, and verify production-quality NestJS and TypeScript with version-compatible syntax and proportionate verification. |
| nestjs-features-performance | 545 | Select and implement runtime features: error contracts, security, testing, DevOps, performance, queues, caching, observability, and safe scale. |
| nestjs-code-audit | 509 | Read-only audit of a whole NestJS repo, returning one prioritized, evidence-backed quality report without changing code. |
| nestjs-feature-audit | 449 | Audit one feature against its documented roadmap on a branch, returning an evidence-backed implementation, gap, legacy, bug, and blocker report. |
| nestjs-git-commit-pr-message | 406 | Prepare and publish intentional Git changes: inspect the diff, scan for secrets, match commit conventions, run checks, and push safely. |

All 7 indexed listings appear in the table above.

## Why This Matters for Hermes Agents

A Hermes agent working on NestJS has the same failure mode as any agent on a large backend: it prescribes Clean Architecture, CQRS, or microservices before reading the repository that is actually in front of it. These skills push the opposite direction, starting from the existing code, the installed versions, and the real runtime constraints before choosing the smallest safe design.

The two audit skills are the standout for review-heavy work. nestjs-code-audit turns TypeScript, lint, module-boundary, security, testing, and performance evidence into one prioritized report without modifying anything, and nestjs-feature-audit does the same for a single feature against a documented roadmap. Both stop rather than guess when the evidence or the roadmap is missing.

The Git skill matters for any agent that commits: it inspects the complete diff, preserves unrelated work, scans staged content for secrets, and performs only the explicitly requested remote actions. That is a concrete guardrail against an agent pushing or force-pushing more than it was asked to.

## Usage

| You say | What happens |
|---|---|
| "Review this module graph and remove the cycle" | nestjs-architecture-principles recommends the smallest change that removes the dependency cycle. |
| "Audit this NestJS repository without changing anything" | nestjs-code-audit returns one evidence-backed report across syntax, lint, boundaries, security, testing, and performance. |
| "Audit the payments feature against its roadmap" | nestjs-feature-audit compares the feature on a branch with its documented roadmap and classifies implemented, missing, legacy, bug, and blocker items. |
| "Trace this slow endpoint and propose a fix" | nestjs-features-performance identifies the limiting resource (event loop, database, network, memory) and proposes a measured fix. |
| "Refactor this provider using SOLID" | nestjs-oop-design-patterns applies a pattern only if the observed variation justifies it, without over-engineering. |
| "Commit and push this verified change" | nestjs-git-commit-pr-message stages the diff, scans for secrets, writes the commit and PR, and reports CI and Pages status. |

## Verification

Confirm skills landed in the agent skills directory after install, and probe one SKILL.md on the `main` branch before reviewing (returns 200):

```bash
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/amirtaherkhani/nestjs-skills/main/skills/nestjs-architecture-principles/SKILL.md
```

```bash
npx skills add amirtaherkhani/nestjs-skills --list
```

## Security

skills.sh verdicts for sampled skills (verified Nov 19, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| nestjs-architecture-principles | Pass | Pass | Pass |
| nestjs-oop-design-patterns | Pass | Pass | Pass |
| nestjs-professional-software-engineering | Pass | Pass | Warn |
| nestjs-features-performance | Pass | Pass | Warn |
| nestjs-code-audit | Pass | Pass | Pass |
| nestjs-feature-audit | Pass | Pass | Pass |
| nestjs-git-commit-pr-message | Pass | Pass | Warn |

The sample covers all 7 indexed listings; three skills carry a Snyk Warn and every other cell passes.

## Limitations

- Snapshot data, verified Nov 19, 2026: 3,602 combined installs across 7 indexed listings; 26 GitHub stars; Apache-2.0; last pushed 2026-11-19. Counts drift over time.
- Version 2 renamed two skills (professional-software-engineering to nestjs-professional-software-engineering, git-commit-pr-message to nestjs-git-commit-pr-message); reinstall the renamed skills and update explicit commands.
- The skills do not force Clean Architecture, CQRS, repositories, microservices, or Kubernetes into a project; the repository and its constraints come first.
- nestjs-code-audit uses installed local ESLint and `tsc --noEmit` only; it does not install dependencies, fix files, run migrations, build images, or deploy.
- nestjs-feature-audit stops before code comparison when no clear roadmap is available in `docs/` or supplied by the user.

## Related

- [NestJS Best Practices - 40-Rule Agent Skill Setup Guide](/hermes/skills/catalog/agent-nestjs-skills-setup)
- [Solid Skills - SOLID and TDD Coding Standards](/hermes/skills/catalog/solid-skills-setup)
- [Ejiro Agent Skills - Svelte, Vue, NestJS and Exa Setup](/hermes/skills/catalog/ejirocodes-agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with nestjs-code-audit on an unfamiliar repo; it is read-only and returns one prioritized report before you change anything.
- Invoke skills explicitly when you know the decision: `/nestjs-code-audit` in Claude Code or `$nestjs-code-audit` in Codex.
- Merge the optional `integrations/claude/CLAUDE.md` and `integrations/codex/AGENTS.md` into existing rules files instead of overwriting project instructions.
- The feature audit needs a real roadmap in `docs/`; supply one or expect the skill to stop rather than guess.
- Prefer the narrowest owning skill for a focused problem, and add another only when the decision crosses boundaries.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
