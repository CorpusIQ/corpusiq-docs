---
title: resolving-merge-conflicts - Matt Pocock Merge Resolution Protocol for Hermes Agents
description: "Install and use mattpocock/skills@resolving-merge-conflicts (457K+ installs) - a 5-step protocol for resolving in-progress git merge/rebase conflicts: state, sources, hunks, checks, finish. Always resolve, never abort."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/resolving-merge-conflicts-setup/"
robots: "index,follow"
last_updated: "2026-09-09"
tags: ["hermes skill", "agent skill", "skill setup", "git", "merge conflicts"]
---

# resolving-merge-conflicts - Setup Guide

**Source:** [mattpocock/skills](https://skills.sh/mattpocock/skills/resolving-merge-conflicts) (457,159 installs)
**Skill:** `mattpocock/skills@resolving-merge-conflicts`
**Installs:** 457,159
**Category:** Software Engineering / Git Workflow
**First Seen:** Sep 9, 2026

`resolving-merge-conflicts` gives Hermes agents a strict 5-step protocol for resolving in-progress git merge/rebase conflicts. Its core rule: understand intent before touching hunks, preserve both intents where possible, and **always resolve - never `--abort`**. For an autonomous agent this is the difference between a merge that preserves everyone's intent and one that silently drops a co-author's work.

---

## Installation

```bash
npx skills add mattpocock/skills --skill resolving-merge-conflicts
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Hermes Agent** | Any recent version with skill support |
| **Node.js 18+** | For the `npx skills` CLI |
| **Git repo with an active conflict** | The skill activates on any in-progress merge/rebase |

---

## What It Provides

| Step | Action | Why |
|---|---|---|
| 1. See the current state | Check git history and the conflicting files | Baseline before any edit |
| 2. Find primary sources | Read commit messages, PRs, issues/tickets behind each side | Understand why each change was made and its original intent |
| 3. Resolve each hunk | Preserve both intents where possible; where incompatible, pick the one matching the merge's stated goal and note the trade-off; never invent new behaviour | Intent-preserving merges |
| 4. Run automated checks | Typecheck, then tests, then format - fix anything the merge broke | No regressions smuggled in |
| 5. Finish | Stage everything, commit; if rebasing, continue until all conflicts clear | Complete the operation |

**Hard rules:** Always resolve; never `--abort`. Do not invent new behaviour.

## Quick Start

1. Install: `npx skills add mattpocock/skills --skill resolving-merge-conflicts`
2. Trigger: any in-progress `git merge` or `git rebase` with conflicts - the skill activates automatically via its description ("Use when you need to resolve an in-progress git merge/rebase conflict")
3. The agent follows the 5-step protocol and commits the finished merge/rebase

## Limitations / Verification

```bash
# Verify skill installed
hermes skills list | grep resolving-merge-conflicts

# Functional test
git merge feature-branch   # create a conflict, then invoke the skill
```

- Short protocol skill (no scripts) - pairs naturally with `git-guardrails-claude-code` and `setup-pre-commit` from the same publisher for a complete git hygiene stack

## Security

- [skills.sh listing](https://skills.sh/mattpocock/skills/resolving-merge-conflicts) - Pass
- [GitHub repo](https://github.com/mattpocock/skills) - Pass
- [Publisher](https://github.com/mattpocock) - Pass

## Related

- [codebase-design Setup](/docs/hermes/skills/catalog/codebase-design-setup)
- [Matt Pocock Agent Workflow Suite - 20-Skill Setup](/docs/hermes/skills/catalog/mattpocock-agent-workflow-suite-setup)
- [Matt Pocock Engineering Skills Setup](/docs/hermes/skills/catalog/matt-pocock-engineering-setup)
