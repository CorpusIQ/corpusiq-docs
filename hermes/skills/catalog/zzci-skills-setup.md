---
title: "PMA Skills - Project Lifecycle and Code Review Setup"
description: "Setup guide for zzci/skills: 3.4K combined installs across 16 listings; PMA project lifecycle, code review, and Go, Rust, Bun, and web baselines."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/zzci-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-19"
tags: ["hermes skill", "agent skill", "skill setup", "project management", "code review", "web development"]
---

# PMA Skills - Setup Guide

**Source:** [zzci/skills](https://www.skills.sh/zzci/skills) via skills.sh - 3.4K combined installs across 16 indexed listings; first seen Nov 19, 2026 (Nov 19, 2026 evening sweep)
**GitHub:** 2 stars, no LICENSE file, `main` branch, last pushed 2026-11-12. Ten skills under `skills/` (pma, pma-cr, pma-web, pma-rust, pma-go, pma-bun, bkd, gitea, react-spectrum-s2, spectrum-audit), each a SKILL.md with `references/` and `agents/openai.yaml`; pma-d2, pma-draw, and pma-mem live under `backup/`, and pma-design, ptask, and pma-code-review have no directory in the current tree.
**Category:** Project lifecycle, code review, and language implementation baselines
**Quality Tier:** 🟠 Orange - no LICENSE file; 2 Fail cells and 8 Warn cells across 16 sampled verdicts (pma fails the Gen Agent Trust Hub; react-spectrum-s2 fails Snyk).

zzci/skills is a collection of Claude Code skills centered on PMA, a complexity-tiered project development lifecycle. The suite spans the full delivery loop: plan, implement, review, and ship, with implementation and acceptance baselines for React + Vite web frontends, Go services and CLIs, Rust workspaces, and Bun backends. Around that core sit an evidence-based code review skill, a React Spectrum S2 component guide and a matching audit skill, plus REST API operators for Gitea and a BKD kanban board.

The defining design is the tiered PMA workflow: investigate, then propose, then implement, with trivial changes taking a fast path and everything else waiting for approval. The four language baselines all reference pma for lifecycle management and pma-cr for code review, so the suite is meant to be used as a coordinated system rather than a loose set of individual skills.

## Installation

```bash
# Install all skills globally
npx skills add zzci/skills --global
```

Install specific skills globally:

```bash
npx skills add zzci/skills --skill pma --global
npx skills add zzci/skills --skill pma-cr --global
npx skills add zzci/skills --skill pma-web --global
npx skills add zzci/skills --skill pma-rust --global
npx skills add zzci/skills --skill pma-go --global
npx skills add zzci/skills --skill pma-bun --global
npx skills add zzci/skills --skill react-spectrum-s2 --global
npx skills add zzci/skills --skill spectrum-audit --global
npx skills add zzci/skills --skill bkd --global
npx skills add zzci/skills --skill gitea --global
```

Install to the current project instead, or list what is available:

```bash
npx skills add zzci/skills
npx skills add zzci/skills --list
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| pma-web | 391 | Frontend implementation and acceptance baseline for React + Vite SPAs: quality gates, TanStack Router and Query, shadcn/ui base-nova, Tailwind theming, testing, i18n, and delivery rules. |
| pma | 388 | Project development lifecycle management: a complexity-tiered investigate, proposal, implement workflow with file-based plan and task tracking and claim-before-work multi-agent coordination. |
| bkd | 374 | Operate a BKD kanban board over its REST API: projects, issues, cron jobs, three-tier L1/L2/L3 coordination, multi-repo and multi-subtask orchestration, and the messages system. |
| pma-rust | 372 | Production-grade Rust implementation and acceptance baseline for services and CLIs: workspaces, Axum/Tokio, CI, release packaging, lint policy, testing, observability, and supply-chain controls. |
| pma-cr | 368 | Evidence-based code review for local diffs, pull requests, and repository audits across TypeScript, Go, Rust, and Python, with BLOCK, INCOMPLETE, WARNING, or PASS decisions. |
| pma-go | 366 | Go implementation and acceptance baseline for services and CLIs: cmd/internal layout, golangci-lint, sqlc + pgx or GORM, koanf config, Chi or Gin, and observability. |
| pma-bun | 364 | Bun implementation and acceptance baseline: Drizzle + SQLite-first data access, OpenAPIHono on Bun.serve, validated env config, and standalone binary compilation with embedded assets. |
| gitea | 189 | Operate a Gitea instance via its REST API with curl, including forced routing for any repository whose git remote host is not github.com. |
| pma-mem | 132 | Knowledge management: capture, classify, search, and sync project knowledge to the Memos storage backend. |
| pma-d2 | 110 | Generate D2 (d2lang.com) diagrams for architecture, workflow, sequence, and ERD from concepts or code. |
| pma-draw | 104 | Generate ReactFlow diagrams as .rfd.json files using a library of custom node types, edge presets, and layout templates. |
| pma-design | 77 | Listed on skills.sh with no directory in the current tree, so its behavior is not documented in the repository. |
| spectrum-audit | 63 | Audit a codebase for adherence to the Spectrum design system and React Spectrum S2 best practices: configuration, styling, accessibility, and component usage. |
| react-spectrum-s2 | 63 | Build UIs with React Spectrum S2 (Spectrum 2), Adobe's React component library, including React Aria Components docs for custom components on unstyled primitives. |
| ptask | 6 | Listed on skills.sh with no directory in the current tree, so its behavior is not documented in the repository. |
| pma-code-review | 1 | Listed on skills.sh with no directory in the current tree, so its behavior is not documented in the repository. |

All 16 indexed listings appear in the table above.

## Why This Matters for Hermes Agents

Most codebase work fails at the boundaries, not in the middle. PMA encodes the boundaries as phases: an agent investigates, proposes, and only then implements, and a trivial change takes a fast path while everything else waits for approval. That keeps a Hermes agent from rewriting a module when a one-line fix would do.

The implementation baselines are the other half. A generic agent that scaffolds a Go service, a Rust workspace, a Bun API, or a React SPA will invent idioms from memory; pma-go, pma-rust, pma-bun, and pma-web each pin a real stack (sqlc + pgx or GORM, Axum/Tokio, Drizzle + SQLite, TanStack Router and Query) with quality gates. An agent following them produces code that matches the project's conventions instead of approximating them.

The code review skill closes the loop. pma-cr returns evidence-backed decisions (BLOCK, INCOMPLETE, WARNING, or PASS) for local diffs, pull requests, and whole-repository audits, and it separates evidence from check results and coverage. That is the review discipline most autonomous agents lack.

## Usage

| You say | What happens |
|---|---|
| "Plan a feature in this codebase" | pma runs the investigate, proposal, and implement workflow and tracks plan and task files. |
| "Review my local diff before I commit" | pma-cr returns an evidence-backed review with a BLOCK, INCOMPLETE, WARNING, or PASS decision. |
| "Scaffold a Go service with a database" | pma-go applies the Go baseline: cmd/internal layout, golangci-lint, sqlc + pgx or GORM, koanf config. |
| "Build a React SPA with routing and server state" | pma-web applies TanStack Router and Query, shadcn/ui base-nova, Tailwind, and the required quality gates. |
| "Stand up a Rust service with CI" | pma-rust applies the Cargo workspace defaults, strict quality gates, and Axum/Tokio patterns. |
| "Build a Bun API with a SQLite database" | pma-bun applies Drizzle + SQLite, OpenAPIHono on Bun.serve, and validated env config. |
| "Build a UI with Adobe Spectrum components" | react-spectrum-s2 guides component selection and usage, or spectrum-audit audits an existing codebase. |

## Verification

Confirm skills landed in the agent skills directory after install, and probe one SKILL.md on the `main` branch before reviewing (returns 200):

```bash
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/zzci/skills/main/skills/pma/SKILL.md
```

```bash
npx skills add zzci/skills --list
```

## Security

skills.sh verdicts for sampled skills (verified Nov 19, 2026) - re-check the security pages on skills.sh before production use:

Two of the 16 sampled skills carry a Fail cell (pma on the Gen Agent Trust Hub; Snyk on react-spectrum-s2), and eight others carry Warn cells, so review those pages before relying on the skills in production.

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| pma-web | Pass | Pass | Pass |
| pma | Fail | Pass | Warn |
| bkd | Pass | Pass | Warn |
| pma-rust | Pass | Pass | Pass |
| pma-cr | Pass | Pass | Warn |
| pma-go | Pass | Pass | Pass |
| pma-bun | Pass | Pass | Pass |
| gitea | Pass | Pass | Warn |
| pma-mem | Pass | Pass | Warn |
| pma-d2 | Pass | Pass | Pass |
| pma-draw | Pass | Pass | Pass |
| pma-design | Pass | Warn | Pass |
| spectrum-audit | Warn | Pass | Pass |
| react-spectrum-s2 | Pass | Pass | Fail |
| ptask | Pass | Pass | Pass |
| pma-code-review | Pass | Pass | Warn |

The sample covers all 16 indexed listings.

## Limitations

- Snapshot data, verified Nov 19, 2026: 3,368 combined installs across 16 indexed listings; 2 GitHub stars; no LICENSE file; last pushed 2026-11-12. Counts drift over time.
- There is no LICENSE file, so treat the repository as all-rights-reserved rather than open source until terms are confirmed with the owner.
- Three indexed listings (pma-design, ptask, pma-code-review) have no directory in the current tree, so their behavior is not documented in the repository.
- pma-d2, pma-draw, and pma-mem are stored under `backup/` rather than `skills/`, so they may sit on a deprecation or relocation path.
- Two of 16 sampled verdicts carry a Fail cell (pma on the Gen Agent Trust Hub, react-spectrum-s2 on Snyk), so production use should wait on a closer review of those skills.

## Related

- [Kanban Orchestrator Setup](/hermes/skills/catalog/kanban-orchestrator-setup)
- [CodeRabbit Skills - AI Code Review Setup](/hermes/skills/catalog/coderabbit-skills-setup)
- [TanStack Skills - React Server State & Router Suite Setup](/hermes/skills/catalog/tanstack-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with pma for lifecycle and pma-cr for review; the four language baselines all reference both.
- Run pma first on any non-trivial change so investigate and proposal complete before implementation begins.
- Use `pma-cr audit` or `pma-cr --repo` for repository-wide review, and `pma-cr <PR-number-or-URL>` for pull request review.
- Keep `docs/plan/` and `docs/task/` files in the repository; the PMA workflow tracks state there.
- Re-check the two Fail skills (pma, react-spectrum-s2) on skills.sh before production use.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
