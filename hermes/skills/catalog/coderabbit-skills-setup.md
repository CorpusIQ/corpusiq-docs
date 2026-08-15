---
title: CodeRabbit Skills — AI Code Review Setup Guide for Hermes Agents
description: "coderabbitai/skills — official CodeRabbit skills: code-review (9.7K installs) and autofix (6.2K). AI-driven code review and automatic fix application for pull requests."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/coderabbit-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-14"
tags: ["hermes skill", "agent skill", "skill setup", "code review", "pull requests", "automation"]
---

# CodeRabbit Skills — Setup Guide

**Source:** [coderabbitai/skills](https://skills.sh/coderabbitai/skills)
**GitHub:** [coderabbitai/skills](https://github.com/coderabbitai/skills)
**Skills:** 2 skills (`code-review`, `autofix`) · 15.9K total installs
**Category:** Code Review & Pull Request Automation
**First Seen:** August 14, 2026 evening sweep
**Quality Tier:** 🟢 Production (official CodeRabbit)

CodeRabbit — the AI code review platform — publishes its review methodology as installable skills. `code-review` (9.7K installs) encodes a structured review pass for pull requests; `autofix` (6.2K) applies fixes for the issues found. The code-review skill was on the hot leaderboard during the sweep (+7 in one hour). These skills give any agent CodeRabbit-style review discipline without the CodeRabbit SaaS subscription.

---

## Installation

```bash
npx skills add coderabbitai/skills
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js + npx** | For the `skills add` installer |
| **Git repo + PR workflow** | Skills operate on pull requests / diffs |

## What It Provides

| Skill | Installs | Purpose |
|---|---|---|
| code-review | 9.7K | Structured PR review: correctness, security, style, tests |
| autofix | 6.2K | Apply fixes for review findings, with diff verification |

## Quick Start

1. `npx skills add coderabbitai/skills`
2. In a repo with an open PR: "review this PR with the code-review skill"
3. "Apply the safe fixes from the review as a new commit"

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Docs repo PRs** | Review community and internal PRs before merge |
| **MCP server PRs** | code-review on mcp2.corpusiq.io changes touching connectors |
| **Frontend releases** | Pre-merge review pass before Vercel deploys |
| **Review discipline** | Standardize review criteria across agent-driven commits |

## Limitations / Verification

- The skills bring the methodology, not CodeRabbit's cloud analysis engine
- autofix output should still be reviewed by a human or a second pass before merge

```bash
npx skills list | grep coderabbit
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Review Loop Skill Setup](/hermes/skills/catalog/review-loop-skill-setup/) — review → feedback → verify loop
- [ECC Engineering Skills Setup](/hermes/skills/catalog/ecc-engineering-skills-setup/) — security-review companion

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace](/hermes/skills/marketplace/) →*

*Powered by CorpusIQ*
