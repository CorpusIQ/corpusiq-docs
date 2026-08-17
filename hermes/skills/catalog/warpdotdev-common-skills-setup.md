---
title: "Warp Common Skills — Spec-Driven Development Workflow"
description: "Install warpdotdev/common-skills (411.2K combined installs) — 25 skills from the Warp terminal team: spec-driven implementation, PR review, CI diagnosis, merge conflict resolution, and spec validation."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/warpdotdev-common-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# Warp Common Skills — Setup Guide

**Source:** [warpdotdev/common-skills](https://www.skills.sh/warpdotdev/common-skills) (411.2K combined installs)
**GitHub:** [github.com/warpdotdev/common-skills](https://github.com/warpdotdev/common-skills)
**Category:** Development Workflow / Spec-Driven Development
**First Seen:** August 12, 2026
**Quality Tier:** 🟢 Production (Warp team, uniform ~20K installs per skill)

Warp (the terminal company) publishes the skills their own agents use daily. The cluster centers on spec-driven development: write product and tech specs, implement against them, then verify the implementation matches the spec. Around that core sit PR mechanics (`review-pr`, `create-pr`, `pr-walkthrough`), failure handling (`fix-errors`, `diagnose-ci-failures`, `reproduce-bug-report`), and meta-workflows (`council`, `saga`, `research`).

---

## Installation

```bash
# Install the full repo
npx skills add warpdotdev/common-skills

# Or install individually
npx skills add warpdotdev/common-skills --skill review-pr
npx skills add warpdotdev/common-skills --skill write-product-spec
npx skills add warpdotdev/common-skills --skill implement-specs
npx skills add warpdotdev/common-skills --skill fix-errors
```

---

## Core Skills

| Skill | Installs | Use For |
|---|---|---|
| `review-pr` | 20.3K | Thorough PR review |
| `spec-driven-implementation` | 20.3K | Implement from specs |
| `write-product-spec` | 20.2K | Product requirements docs |
| `write-tech-spec` | 20.1K | Technical design docs |
| `resolve-merge-conflicts` | 20.1K | Conflict resolution |
| `fix-errors` | 20.1K | Error triage and fixes |
| `implement-specs` | 20.1K | Turn specs into code |
| `create-pr` | 20.0K | PR creation |
| `update-skill` | 20.0K | Self-updating skills |
| `diagnose-ci-failures` | 20.0K | CI failure root-causing |
| `council` | 19.0K | Multi-perspective review council |
| `check-impl-against-spec` | 18.6K | Verify implementation matches spec |
| `reproduce-bug-report` | 18.4K | Bug reproduction |
| `validate-changes-match-specs` | 16.7K | Pre-merge spec validation |
| `research` | 13.4K | Structured research pass |
| `cross-critique` | 13.4K | Cross-skill critique |
| `saga` | 12.3K | Long-running task orchestration |
| `write-feature-docs` | 10.8K | Feature documentation |

Also included: `brandalf`, `pr-walkthrough`, `respond-to-pr-comments-in-blocklist`, `scan-new-specs`, `readout`, `complain`, `suggestion-box`.

---

## Prerequisites

| Requirement | Details |
|---|---|
| Node.js + npx | For the skills.sh CLI install path |
| Git + GitHub workflow | PR-centric skills assume GitHub |
| Agent runtime | Hermes/Claude Code-style agent with shell access |

---

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Docs & repo quality** | `review-pr` + `check-impl-against-spec` on every agent-driven commit |
| **Feature planning** | `write-product-spec` before agent build tasks |
| **CI health** | `diagnose-ci-failures` for the docs build and MCP server pipelines |
| **Long-running sweeps** | `saga` to orchestrate multi-step cron workflows |

---

## Limitations / Verification

- GitHub-centric — non-GitHub forges get partial coverage
- Verify install: `npx skills list | grep -E "review-pr|spec"`

---

## Related

- [Subagent-Driven Development Setup](/hermes/skills/catalog/subagent-driven-development-setup/)
- [Simplify Code Setup](/hermes/skills/catalog/simplify-code-setup/)
- [Skills Catalog](/hermes/skills/catalog/)

*Powered by CorpusIQ*
