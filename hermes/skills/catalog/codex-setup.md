---
title: "Codex — Delegate Coding Tasks to OpenAI Codex CLI"
description: "Install and configure the Codex skill to delegate coding tasks from Hermes to OpenAI Codex CLI. Offload features, PRs, and complex refactors."
category: catalog
---

# Codex — OpenAI Codex CLI Delegation Setup Guide

Delegate coding tasks from your Hermes agent to OpenAI Codex CLI. This skill enables your Hermes agent to spawn Codex subprocesses for feature development, PR creation, and complex refactoring — leveraging Codex's specialized coding capabilities while Hermes handles orchestration.

**Source:** [nousresearch/hermes-agent](https://github.com/nousresearch/hermes-agent) via [skills.sh](https://www.skills.sh/nousresearch/hermes-agent/codex)

## Installation

```bash
npx skills add nousresearch/hermes-agent --skill codex
```

## Prerequisites

- Hermes Agent installed and running
- OpenAI Codex CLI installed: `npm install -g @openai/codex`
- OpenAI API key configured in Codex: `export OPENAI_API_KEY=sk-...`
- Node.js 18+

## Configuration

After installation, the skill auto-discovers Codex CLI. Verify:

```bash
# Check Codex is accessible
codex --version

# Test basic delegation
hermes codex test
```

## Usage Patterns

### 1. Delegate a Feature

```bash
# From Hermes, delegate a feature to Codex
hermes codex delegate "Add rate limiting middleware to the API server"
```

Hermes will:
1. Pass the task description to Codex
2. Codex reads the codebase, plans the change, and implements it
3. Results (diffs, test results) are returned to Hermes
4. Hermes can review, approve, or request changes

### 2. Create a PR

```bash
hermes codex pr "Fix the pagination bug in /api/users endpoint"
```

### 3. Refactor with Constraints

```bash
hermes codex delegate \\
  --constraints "Keep backward compatibility, add deprecation warnings" \\
  "Refactor the auth module to use the new token format"
```

## Integration with Hermes Workflows

### Autonomous PR Pipeline

Create a cron job that picks up issues and delegates to Codex:

```yaml
# In Hermes config
codex:
  auto_pr: false          # Set true for fully autonomous PR creation
  review_required: true   # Hermes reviews before pushing
  max_files_per_pr: 10    # Safety limit
```

### Pair Programming Mode

```bash
# Codex works on a task while Hermes monitors
hermes codex pair "Implement the GraphQL resolver for User type"
# Hermes watches Codex output, can interrupt if it goes off-track
```

## Safety & Guardrails

| Setting | Default | Description |
|---------|:------:|-------------|
| `review_required` | true | Hermes must approve changes before they're committed |
| `max_files_per_pr` | 10 | Hard limit on files changed per PR |
| `blocked_operations` | `rm -rf, drop table, truncate` | Patterns that Codex cannot execute |
| `test_required` | true | Tests must pass before PR can be opened |

## Comparison with Hermes Native Coding

| Aspect | Hermes Native | Codex Delegation |
|--------|:------------:|:----------------:|
| Best for | Orchestration, ops, config | Feature dev, refactors |
| Code generation quality | Good | Specialized (Codex tuned for code) |
| Context window | Smaller | Codex has its own context |
| File operations | Direct | Via Codex sandbox |
| Review workflow | Manual | Hermes reviews Codex output |

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `codex: command not found` | Install: `npm install -g @openai/codex` |
| Codex returns empty | Check `OPENAI_API_KEY` is set and valid |
| Delegation times out | Increase timeout: `hermes codex config --timeout 600` |
| Codex makes unwanted changes | Tighten constraints: add more specific instructions |
| PR creation fails | Check GitHub token: `gh auth status` |
