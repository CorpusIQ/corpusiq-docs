---
title: "Herdr Skills — Terminal Workspace Orchestration Setup"
description: "herdrdev/herdr — 5 skills, 28.1K installs: terminal workspaces, tabs, panes, and agent-aware session control exposed through the herdr CLI. 29.7K GitHub stars, 3/3 security audit passes."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/herdr-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-17"
tags: ["hermes skill", "agent skill", "skill setup", "terminal", "orchestration", "herdr"]
---

# Herdr Skills — Setup Guide

**Source:** [herdrdev/herdr](https://skills.sh/herdrdev/herdr)
**GitHub:** [herdrdev/herdr](https://github.com/herdrdev/herdr)
**Skills:** 5 skills · 28.1K total installs
**Category:** Terminal Orchestration
**First Seen:** catalogued August 17, 2026 sweep (herdr on skills.sh since April 7, 2026)
**Quality Tier:** 🟢 Production — Gen Agent Trust Hub Pass, Socket Pass, Snyk Pass (3/3)

Herdr organizes terminals into workspaces, tabs, and panes, recognizes coding agents running inside panes, and exposes the current session through the `herdr` CLI. An agent running inside a Herdr pane can inspect neighboring work, create layouts, start commands, and wait for state changes — turning a pile of terminals into one queryable session.

---

## Installation

```bash
npx skills add herdrdev/herdr
```

Individual skills install with the explicit repo form:

```bash
npx skills add https://github.com/herdrdev/herdr --skill herdr
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Herdr runtime** | The `herdr` CLI manages panes; the skill verifies it is running inside a managed pane |
| **Environment check** | Skill refuses to act unless `test "${HERDR_ENV:-}" = 1` passes |

## What It Provides

| Skill | Installs | Purpose |
|---|---|---|
| herdr | 27.6K | Core session control: inspect neighboring panes, create layout, start agents/commands, read output, wait for state |
| herdr-pre-release-audit | 160 | Pre-release audit workflow |
| herdr-throwaway-repro | 151 | Throwaway reproduction environments |
| triage | 146 | Issue triage workflow |
| writing-commit-messages | 17 | Commit-message drafting |

The core skill treats the installed `herdr` binary as the authority for command syntax — it learns the current CLI before issuing control commands, and refuses to inspect or control sessions from outside a Herdr-managed pane.

## Quick Start

1. Install: `npx skills add herdrdev/herdr`
2. Open a Herdr-managed pane, then ask: "inspect the other panes and summarize what's running"
3. For agent orchestration: ask the agent to start a command in a new tab and wait for completion

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Multi-agent sessions** | One pane per agent, with each able to see its neighbors through `herdr` — matches our multi-agent workflow patterns |
| **Spark terminal hygiene** | Workspace/tab structure for the DGX Spark's long-lived terminal sessions |
| **Sub-agent supervision** | Inspect what a background agent is doing without joining its pane |

## Limitations / Verification

- Security audits on herdr: Gen Agent Trust Hub Pass, Socket Pass, Snyk Pass — clean across all three
- Publisher-page install counts verified (27.6K + 160 + 151 + 146 + 17 = 28.1K); GitHub 29.7K stars on the repo
- Skill is inert outside Herdr-managed panes by design — the `HERDR_ENV` check blocks out-of-session control
- Companion skills are early content (sub-200 installs each)

```bash
npx skills add herdrdev/herdr   # verify install works
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Skills Marketplace](/hermes/skills/marketplace/)

*Powered by CorpusIQ*
