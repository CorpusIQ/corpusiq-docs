---
title: Agent Pulse Skill — Local AI Agent Activity Monitor Setup
description: "jane-o-o-o-o/agent-pulse-skill — agent-pulse (32.4K installs): CLI source of truth for local AI-agent activity via the agentpulse-cli PyPI package; monitors agent runs, sessions, and activity."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/agent-pulse-skill-setup/"
robots: "index,follow"
last_updated: "2026-08-15"
tags: ["hermes skill", "agent skill", "skill setup", "monitoring", "cli", "observability"]
---

# Agent Pulse Skill — Setup Guide

**Source:** [jane-o-o-o-o/agent-pulse-skill](https://skills.sh/jane-o-o-o-o/agent-pulse-skill)
**GitHub:** [jane-o-o-o-o/agent-pulse-skill](https://github.com/jane-o-o-o-o/agent-pulse-skill)
**Skills:** 1 skill (`agent-pulse`) · 32.4K installs
**Category:** Agent Observability & Monitoring
**First Seen:** May 27, 2026 (catalogued August 15, 2026 sweep; +218 installs in the sweep hour on the hot leaderboard)
**Quality Tier:** 🟢 Production (all three security audits pass)

agent-pulse teaches the agent to use the installed `agent-pulse` CLI as the source of truth for local AI-agent activity. The PyPI package is `agentpulse-cli` while the command remains `agent-pulse`. The skill prefers running the CLI and summarizing its output over reading Agent Pulse source code, and handles platform quirks (emoji and box-drawing output requires UTF-8 mode on Windows). It was the fastest-rising new skill on the hot leaderboard during this sweep.

---

## Installation

```bash
npx skills add jane-o-o-o-o/agent-pulse-skill --skill agent-pulse
```

CLI dependency:

```bash
pip install agentpulse-cli
```

On Windows, enable UTF-8 before running because Agent Pulse output contains emoji and box drawing:

```powershell
$env:PYTHONUTF8='1'
$env:PYTHONIOENCODING='utf-8'
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Python + pip** | For the `agentpulse-cli` package |
| **Node.js + npx** | For the skill installer |
| **Local agent environment** | Agent activity to monitor |

## What It Provides

| Capability | Notes |
|---|---|
| Activity source of truth | `agent-pulse` CLI as the canonical view of local agent activity |
| Run summaries | Summarize agent runs from CLI output |
| Cross-platform support | Windows (with UTF-8 mode), macOS, Linux |
| Lightweight install | Single PyPI package |

## Quick Start

1. `pip install agentpulse-cli`
2. `npx skills add jane-o-o-o-o/agent-pulse-skill --skill agent-pulse`
3. Ask: "show me recent local agent activity and summarize what has been running"

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Agent fleet visibility** | Monitor local agent activity across the Spark and worker nodes |
| **Cron run audits** | Verify scheduled agent runs actually executed |
| **Debugging aid** | Correlate agent activity with reported outcomes during incident triage |
| **Observability reference** | CLI-first monitoring pattern for our own agent telemetry |

## Limitations / Verification

- Monitors local machine activity only — no remote fleet aggregation documented
- Output includes emoji/box drawing; pipe through UTF-8-aware terminals

```bash
agent-pulse --help   # verify CLI is installed and working
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Sentry Dev Skill Setup](/hermes/skills/catalog/sentry-dev-skills-setup/) — error monitoring
- [Hermes Stack Doctor](/hermes/skills/) — Hermes health audits

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace](/hermes/skills/marketplace/) →*

*Powered by CorpusIQ*
