---
title: OpenCode CLI — Full Setup Guide for Hermes Agents
description: Use OpenCode as an autonomous coding worker orchestrated by Hermes. Provider-agnostic, open-source AI coding agent with TUI and CLI for parallel task execution.
---

# OpenCode CLI — Setup Guide

**Source:** [nousresearch/hermes-agent](https://github.com/nousresearch/hermes-agent) (227.9K⭐)
**Skill:** `nousresearch/hermes-agent@opencode`
**Installs:** 301
**Category:** Development / AI Coding
**First Seen:** Apr 4, 2026

Use [OpenCode](https://opencode.ai/) as an autonomous coding worker orchestrated by Hermes terminal/process tools. OpenCode is a provider-agnostic, open-source AI coding agent with a TUI and CLI. Ideal for long-running coding sessions, parallel task execution in isolated workdirs, and delegating implementation/refactoring/review to an external agent.

---

## Installation

```bash
# Install the skill
npx skills add nousresearch/hermes-agent@opencode

# Install OpenCode itself
npm install -g opencode-ai@latest
# or
brew install anomalyco/tap/opencode
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **OpenCode CLI** | `npm i -g opencode-ai@latest` or `brew install anomalyco/tap/opencode` |
| **Auth** | `opencode auth login` or set provider env vars (`OPENROUTER_API_KEY`, etc.) |
| **Git repository** | Recommended for code tasks |
| **Hermes Agent** | Any version with `pty=true` terminal access |
| **Verify auth** | `opencode auth list` must show at least one provider |

---

## What It Provides

### When to Use OpenCode via Hermes

| Scenario | Why OpenCode |
|---|---|
| **Large refactors** | Isolate in a worktree, let OpenCode run for 10-30 minutes |
| **Parallel features** | Dispatch multiple OpenCode instances in separate workdirs |
| **Code review** | Ask OpenCode to review a PR branch and suggest improvements |
| **Implementation from specs** | Feed a spec file, have OpenCode implement it |
| **Test generation** | Point at a module, ask for comprehensive test coverage |

### Hermes ↔ OpenCode Integration

OpenCode runs as a subprocess managed by Hermes's terminal tools:

```
Hermes (orchestrator)
  ├── terminal("opencode 'implement auth module'", pty=true)
  ├── OpenCode (autonomous coding)
  │   ├── Reads codebase
  │   ├── Plans implementation
  │   ├── Writes code
  │   ├── Runs tests
  │   └── Reports back
  └── Hermes reviews output, commits, continues
```

---

## Quick Start

```bash
# 1. Install + auth
npm install -g opencode-ai@latest
opencode auth login

# 2. Verify
opencode auth list

# 3. Basic usage via Hermes
# In a Hermes session:
opencode "Add input validation to src/auth/login.ts"

# 4. Long-running task with progress checks
opencode --model anthropic/claude-sonnet-4-20250514 \
  "Refactor the database layer to use connection pooling" \
  2>&1 | tee opencode_output.log
```

---

## Parallel Execution Pattern

For multi-feature work, use git worktrees:

```bash
# Create isolated worktrees
git worktree add ../feature-auth feature/auth
git worktree add ../feature-api feature/api

# Dispatch OpenCode to both
cd ../feature-auth && opencode "Implement OAuth flow" &
cd ../feature-api && opencode "Build REST endpoints" &

# Wait for both, then review
wait
git merge feature/auth feature/api
```

---

## Model Selection

OpenCode is provider-agnostic. Recommended models:

| Task Type | Recommended Model |
|---|---|
| Complex architecture | `anthropic/claude-sonnet-4-20250514` |
| Routine implementation | `openai/gpt-4o` |
| Quick fixes | `google/gemini-2.0-flash` |
| Cost-sensitive | `deepseek/deepseek-chat` |

---

## Verification

After installation:

```bash
# Check OpenCode is installed
opencode --version

# Check auth
opencode auth list

# Run a simple test
opencode "Write a hello world function in Python" --max-turns 3
```

---

## Limitations

- **Cost:** OpenCode consumes API tokens for each turn. Monitor usage.
- **Isolation:** Use worktrees or Docker for safe experimentation.
- **Review required:** Always review OpenCode's output before merging.
- **PTY mode:** Hermes terminal must use `pty=true` for interactive OpenCode sessions.

---

## Security

- [Gen Agent Trust Hub: Warn](https://www.skills.sh/nousresearch/hermes-agent/opencode/security/agent-trust-hub)
- [Socket: Pass](https://www.skills.sh/nousresearch/hermes-agent/opencode/security/socket)
- [Snyk: Warn](https://www.skills.sh/nousresearch/hermes-agent/opencode/security/snyk)

---

**Related:** [codex-setup.md](codex-setup.md), [claude-code-skills-setup.md](claude-code-skills-setup.md), [github-code-review-setup.md](github-code-review-setup.md)
