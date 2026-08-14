---
title: Caveman Skills — Agent Coding Workflow Suite Setup Guide for Hermes Agents
description: "Install juliusbrussee/caveman (2.2M combined installs) — 23 skills for caveman-style agent coding: commits, reviews, context compression, stats, multi-agent crews, and evidence-driven fixes."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/caveman-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# Caveman Skills — Setup Guide

**Source:** [juliusbrussee/caveman](https://www.skills.sh/juliusbrussee/caveman) (2.2M combined installs)
**GitHub:** [github.com/juliusbrussee/caveman](https://github.com/juliusbrussee/caveman)
**Category:** Code Quality / Agent Workflow
**First Seen:** August 12, 2026
**Quality Tier:** 🟢 Production (seven skills above 250K installs)

Caveman is a blunt-instrument agent coding workflow: keep it simple, commit everything, compress the context, review with evidence. The flagship `caveman` skill alone has 431K installs, backed by a full toolchain — `caveman-commit`, `caveman-review`, `caveman-compress`, `caveman-stats`, and the multi-agent `cavecrew`.

---

## Installation

```bash
# Install the full repo
npx skills add juliusbrussee/caveman

# Or install the core individually
npx skills add juliusbrussee/caveman --skill caveman
npx skills add juliusbrussee/caveman --skill caveman-commit
npx skills add juliusbrussee/caveman --skill caveman-review
npx skills add juliusbrussee/caveman --skill caveman-compress
```

---

## Core Skills

| Skill | Installs | Use For |
|---|---|---|
| `caveman` | 431.1K | Main workflow — simple, direct coding loops |
| `caveman-commit` | 303.1K | Disciplined commit cadence |
| `caveman-review` | 301.0K | Evidence-based code review |
| `caveman-compress` | 298.8K | Context compression between steps |
| `caveman-help` | 293.1K | Self-help and usage discovery |
| `cavecrew` | 250.6K | Multi-agent crew orchestration |
| `caveman-stats` | 250.3K | Progress and usage statistics |
| `compress` | 46.6K | General context compression utility |

Smaller but useful additions: `caveman-explore`, `caveman-optimize`, `investigate-first`, `verify-and-stop`, `caveman-learn`, `surgical-patch`, `safe-refactor`, `caveman-discover`, `lean-build`, `caveman-manage`, `caveman-evidence-review`, `caveman-setup`, `migration`, plus `caveman-es` (Spanish) and `caveman-cn` (Chinese) localizations.

---

## Prerequisites

| Requirement | Details |
|---|---|
| Node.js + npx | For the skills.sh CLI install path |
| Git repo | Workflow is commit-centric |
| Any agent runtime | Skills are runtime-agnostic; Hermes/Claude Code-style agents work |

---

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Docs repo maintenance** | `caveman-review` + `caveman-commit` for sweep-driven doc updates like this catalog |
| **Context discipline** | `caveman-compress` pattern matches the token-optimization doctrine for long agent sessions |
| **Multi-agent builds** | `cavecrew` when parallel workers need a shared coding protocol |
| **Safe refactors** | `surgical-patch` + `safe-refactor` for production repo edits |

---

## Limitations / Verification

- Opinionated workflow — best adopted whole, not piecemeal
- Verify install: `npx skills list | grep caveman` shows installed entries
- `caveman-es` / `caveman-cn` are localizations of the core skill

---

## Related

- [Simplify Code Setup](/hermes/skills/catalog/simplify-code-setup/)
- [Code Quality & Review category](/hermes/skills/catalog/)
- [Skills Catalog](/hermes/skills/catalog/)

*Powered by CorpusIQ*
