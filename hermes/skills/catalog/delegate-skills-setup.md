---
title: Delegate Skills — Background Agent Delegation Setup Guide
description: Install and configure delegate-skills to spawn background agent workers with git worktree isolation and self-healing monitoring. Works with Hermes and any AI with shell access.
---

# Delegate Skills — Setup Guide

**Source:** [bassemZohdy/delegate-skills](https://github.com/bassemZohdy/delegate-skills)
**Category:** Agent Infrastructure / Multi-Agent Orchestration
**License:** MIT · **Published:** June 28, 2026

Delegate long-running coding tasks to background agent workers with full git worktree isolation. The parent agent spawns a worker in a separate worktree, the worker does the task, and the parent gets a summary — without polluting the main working directory or context window. Self-healing monitoring restarts failed workers automatically.

---

## Architecture

```
Parent Agent (Hermes)
  │
  ├─ spawns → Worker Agent (isolated git worktree)
  │              │
  │              ├─ runs task in background
  │              ├─ self-healing monitor watches for failures
  │              └─ returns summary + artifacts
  │
  └─ continues other work while worker runs
```

---

## Key Capabilities

| Feature | Description |
|---------|-------------|
| **Git worktree isolation** | Each worker gets its own worktree — no collisions |
| **Self-healing monitoring** | Crashed workers are detected and restarted |
| **Summary return** | Workers return structured results, not raw logs |
| **Multi-agent support** | Claude Code, Hermes, any agent with shell access |
| **Artifact handoff** | Workers can produce files, branches, or PRs |

---

## Installation

```bash
npx skills add bassemZohdy/delegate-skills
```

Direct clone:

```bash
git clone https://github.com/bassemZohdy/delegate-skills.git
cp -r delegate-skills/skills/* ~/.hermes/profiles/corpusiq/skills/
```

### Prerequisites

```bash
# Ensure git worktree support
git config --global core.worktreeConfig true

# The background agent CLI (choose one)
npm install -g @anthropic-ai/claude-code   # Claude Code
# or: Hermes Agent is already your runtime
```

---

## Usage with Hermes Agent

```
"Delegate the payment refactoring to a background agent"
"Spawn a worker to fix all the lint errors in the api/ directory"
```

The skill handles:
1. Creating an isolated git worktree
2. Spawning the background agent with the task
3. Monitoring for completion or failure
4. Returning a summary when done

---

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| Parallel feature work | Delegate independent tasks to concurrent workers |
| Code cleanup sprints | Spawn workers for linting, formatting, dead code removal |
| Test suite expansion | One worker per test module |
| Multi-repo operations | Workers operate in isolated worktrees across repos |

---

## Pitfalls

- Workers consume additional disk space (one worktree per task)
- Large monorepos may have slow worktree creation
- Background agents need their own API keys configured
- Check `git worktree list` periodically to clean up stale workers

---

*This guide is part of the [Hermes Skills Catalog](/hermes/skills/catalog/). Discovered June 29, 2026. Powered by CorpusIQ.*
