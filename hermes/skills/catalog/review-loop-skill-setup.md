---
title: "Review Loop Skill — Continuous Code Review Discipline"
description: "2dmurali/review-loop-skill — 24.6K installs, #1 on the skills.sh hot leaderboard. A self-contained review-loop discipline skill: review code changes, produce actionable feedback, verify fixes. Complements agent coding workflows."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/review-loop-skill-setup/"
robots: "index,follow"
last_updated: "2026-08-14"
tags: ["hermes skill", "agent skill", "skill setup", "code review", "workflow"]
---

# Review Loop Skill — Setup Guide

**Source:** [2dmurali/review-loop-skill](https://skills.sh/2dmurali/review-loop-skill)
**GitHub:** [2dmurali/review-loop-skill](https://github.com/2dmurali/review-loop-skill)
**Skills:** 1 skill (`review-loop`, 24.6K installs)
**Category:** Code Quality / Agent Workflow
**First Seen:** August 14, 2026 afternoon sweep
**Quality Tier:** 🟢 Production (24.6K installs, #1 on the skills.sh hot leaderboard at sweep time — fastest-rising skill, +399 installs in 1 hour)

A focused discipline skill: run a continuous review loop over code changes — review the diff, produce specific actionable feedback, verify the fixes land, repeat. It is the smallest of the "agent workflow discipline" skills (compare Caveman's evidence review and commit hygiene), useful where a full workflow suite is more than the task needs.

---

## Installation

```bash
npx skills add 2dmurali/review-loop-skill
```

No configuration or API keys required.

## What It Provides

- A structured **review → feedback → verify → repeat** loop for code changes
- Review triggers on diffs, PRs, and working-tree changes
- Feedback is scoped to actionable items — not style noise
- Verification step confirms each flagged issue is actually resolved before the loop closes

## Quick Start

1. `npx skills add 2dmurali/review-loop-skill`
2. "Run a review loop on the changes in this repo since the last commit"
3. "Review this PR diff and give me only actionable feedback"
4. "Verify the fixes from the last review actually landed"

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Docs repo hygiene** | Review each corpusiq-docs change set before push — catches broken links, frontmatter drift, and stale references |
| **Script review** | Review cron wrapper scripts and automation edits before deployment |
| **Agent self-review** | Pair with `caveman` and `verify-and-stop` from the Caveman suite for a full discipline stack |

## Limitations / Verification

- Single-purpose: review-loop discipline only — no commit hygiene, context compression, or test generation (see Caveman for those)
- No external services; works entirely on local diffs and PR context

```bash
# Verify install
npx skills list 2>/dev/null | grep -i review-loop || ls ~/.agents/skills 2>/dev/null | grep -i review-loop
```

## Related

- [Caveman Skills — Agent Coding Workflow Suite Setup](/hermes/skills/catalog/caveman-skills-setup/)
- [Self-Improving Agent Setup](/hermes/skills/catalog/self-improving-agent-setup/)
- [GitHub workflow skills catalog section](/hermes/skills/catalog/)

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace](/hermes/skills/marketplace/) →*

*Powered by CorpusIQ*
