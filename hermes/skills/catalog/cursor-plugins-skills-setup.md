---
title: "Cursor Plugins Skills — Engineering Discipline Suite Setup"
description: "cursor/plugins — 79 skills, 72.0K installs: thermo-nuclear code review, CI loop tools, and engineering-principle skills from the Cursor team."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/cursor-plugins-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-16"
tags: ["hermes skill", "agent skill", "skill setup", "code review", "cursor", "engineering"]
---

# Cursor Plugins Skills — Setup Guide

**Source:** [cursor/plugins](https://skills.sh/cursor/plugins)
**GitHub:** [cursor/plugins](https://github.com/cursor/plugins)
**Skills:** 79 skills · 72.0K total installs
**Category:** Code Review & Engineering Discipline
**First Seen:** catalogued August 16, 2026 sweep (top skill on skills.sh since May 21, 2026)
**Quality Tier:** 🟢 Production — official Cursor org; top skill passes all three security audits

The largest single engineering-discipline cluster catalogued to date: 79 skills covering unusually strict code review, PR hygiene, CI failure loops, and a "principles" series encoding engineering judgment. The flagship thermo-nuclear-code-quality-review pushes agents toward ambitious restructurings that preserve behavior while making the code dramatically simpler.

---

## Installation

```bash
npx skills add cursor/plugins
```

Individual skills install with the explicit repo form:

```bash
npx skills add https://github.com/cursor/plugins --skill thermo-nuclear-code-quality-review
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js + npx** | For the skill installer |
| **Git repository** | Most skills operate on a branch's diff |
| **CI access** | For loop-on-ci and fix-ci skills |

## What It Provides

| Skill | Installs | Purpose |
|---|---|---|
| thermo-nuclear-code-quality-review | 10.3K | Deep code-quality audit of branch changes, "code judo" restructurings |
| deslop | 3.6K | Remove AI-slop patterns from code |
| fix-merge-conflicts | 1.6K | Resolve conflicts autonomously |
| make-pr-easy-to-review | 1.5K | PR hygiene for reviewers |
| review-and-ship | 1.5K | End-to-end review-to-merge flow |
| what-did-i-get-done | 1.5K | Session work recap |
| pr-review-canvas | 1.5K | Structured PR review workspace |
| fix-ci / get-pr-comments / loop-on-ci | 1.4K | CI failure recovery loop |
| weekly-review | 1.4K | Periodic engineering review |
| check-compiler-errors | 1.4K | Build verification |
| new-branch-and-pr / run-smoke-tests | 1.4K | Branch and test workflow |
| control-ui / control-cli / verify-this | 1.3K | Plugin control surface |
| unslop / thermo-nuclear-review | 1.0K | Additional slop-removal passes |

Plus a 24-skill "principles" series (foundational thinking, boundary discipline, guard-the-context-window, prove-it-works, and more) and 40+ additional utilities — 79 skills total.

## Quick Start

1. Install: `npx skills add cursor/plugins`
2. Start with `thermo-nuclear-code-quality-review` — it carries 10.3K of the suite's installs
3. Ask: "run a thermo-nuclear review of this branch before I open the PR"

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **PR quality gate** | Thermo-nuclear review pairs with our GitHub workflow before merging |
| **CI self-healing** | loop-on-ci and fix-ci automate the retry loop we do manually today |
| **Slop removal** | deslop/unslop match our AI-writing audit doctrine, applied to code |
| **Branch hygiene** | make-pr-easy-to-review and new-branch-and-pr standardize our contribution flow |

## Limitations / Verification

- Security audits on thermo-nuclear-code-quality-review: Gen Agent Trust Hub Pass, Socket Pass, Snyk Pass — 3/3
- Publisher-page install counts verified (72.0K total); GitHub 2.9K stars on the repo
- Long tail is shallow: most skills beyond the top five are sub-1.5K installs — treat as early content
- Review skills are opinionated; they will propose large restructurings. Pair with a human gate on high-stakes repos

```bash
npx skills add cursor/plugins   # verify install works
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Skills Marketplace](/hermes/skills/marketplace/)

*Powered by CorpusIQ*
