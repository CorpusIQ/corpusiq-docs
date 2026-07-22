---
title: Multi-Agent Orchestration — PM-style parallel worker management for Hermes Agents
description: PM-style multi-agent orchestration with worktree isolation, tmux sessions, and Wave-based task dispatch. 32+ installs from cat-xierluo/legal-skills.
---

# Multi-Agent Orchestration — Setup Guide

**Source:** [cat-xierluo/legal-skills](https://skills.sh/cat-xierluo/legal-skills/multi-agent-orchestration) (32+ installs)
**Category:** Engineering / Agent Orchestration
**Quality Tier:** 🔵 Community

A comprehensive PM-style multi-agent orchestration framework for running parallel agent workers with isolated worktrees, tmux sessions, and structured Wave-based dispatch. Supports Claude Code, Codex, OpenCode, and custom CLI workers with provider-aware model routing, escape-prevention gates, and checkpoint-based monitoring.

---

## Installation

```bash
npx skills add cat-xierluo/legal-skills --skill multi-agent-orchestration
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Git** | Worktree support for isolation |
| **tmux** | Session management for parallel workers |
| **Agent CLI** | Claude Code, Codex, OpenCode, or custom CLI |
| **Bash** | Script execution environment |

---

## Key Capabilities

### PM-Worker Architecture
Current session acts as PM (Project Manager): reads task sources, groups work, spawns isolated workers, monitors progress via checkpoint files, and merges results. Workers execute in isolated worktrees with their own branches.

### Wave-Based Dispatch
Tasks are grouped into Waves — sets of parallel workers running against the same base ref. PM plans provider slots, concurrency limits, and risk tiers before launching. Supports 4-6 parallel workers for independent tasks, 1-3 for shared-dependency work.

### Escape Prevention Gate
When user requires tmux/independent sessions, PM must pass a startup gate before touching business code: create worktree → start tmux → verify session alive → confirm STATUS.json appears → only then proceed.

### Provider-Aware Routing
Worker backends include Claude Code (with provider registry for multi-provider routing), Codex, OpenCode, WorkBuddy/CodeBuddy, QoderWork CN, and custom CLI. Per-worker model selection, provider slot allocation, and concurrency management.

### Checkpoint Protocol
Workers write `STATUS.json`, `RESULT.md`, and `PATCH_SUMMARY.md` to a Session Context directory. PM monitors via `pm-monitor.sh` or `sentinel.sh` for stale workers, blocked tasks, and completion signals.

---

## Quick Start

```bash
# 1. Preflight dependency check
bash scripts/check-dependencies.sh

# 2. Create worktree and session
bash scripts/spawn-worker.sh \
  --project /path/to/repo \
  --branch feat/my-feature \
  --session my-worker-1 \
  --worker-backend claude-code \
  --model "your-model" \
  --verify-cmd 'npm run typecheck' \
  --command "claude --permission-mode auto"

# 3. Verify worker alive (30-second postflight)
tmux has-session -t my-worker-1
tmux capture-pane -t my-worker-1 -p | tail -5

# 4. Send worker prompt via tmux
tmux send-keys -t my-worker-1 -l -- "Your task prompt here..."
tmux send-keys -t my-worker-1 Enter

# 5. Monitor progress
bash scripts/pm-monitor.sh --project /path/to/repo --once
```

---

## Verification

```bash
# Check skill installed
npx skills list | grep multi-agent-orchestration

# Verify tmux available
tmux -V

# Check worktree support
git worktree list
```

---

## Notes

- Comprehensive 8-section SKILL.md covering: boundaries, execution modes, role/backend selection, Wave orchestration, naming conventions, session context, worker prompt templates, and monitoring/intervention
- Personal routing preferences via `config/orchestration-personal.json` (gitignored, not committed)
- Default: same-host workers (Claude Code PM → Claude Code workers). Cross-tool only with explicit justification
- Supports lightweight mode (`--no-worktree`) for non-git targets or folder-isolated workers
- Worker prompt template at `templates/worker-prompt.md` with Bootstrap-only and Full variants
- Built-in sentinel monitoring with harness re-invoke on worker completion
- Quality tier 🔵 Community: 32 installs, but extremely comprehensive (v1.18.4) with extensive production battle-testing
