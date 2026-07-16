---
title: "napoleond/clawdirect — Agent Self-Direction Framework"
description: "Complete setup guide for clawdirect and clawdirect-dev: structured agent task execution, work trees, directives, and development mode for Hermes/OpenClaw agents."
---

# Setup Guide: napoleond/clawdirect

**2 skills for structured agent self-direction — task execution, work trees, and development directives.**

## Quick Install

```bash
npx skills add napoleond/clawdirect/clawdirect
npx skills add napoleond/clawdirect/clawdirect-dev
```

## Prerequisites

- Hermes Agent or OpenClaw installed
- Node.js 18+ (for `npx skills`)
- Git (for work tree isolation)
- Familiarity with agent directive patterns

## Skills Overview

| Skill | Installs | Purpose |
|-------|:--------:|---------|
| **clawdirect** | 4,617 | Core agent directing — structured task execution, work trees, directives |
| **clawdirect-dev** | 4,502 | Development mode — extended directives for coding, testing, deployment |

## What It Does

Clawdirect gives Hermes agents a structured command interface for self-directed work:

- **Work Trees**: Isolated git worktrees for parallel task execution
- **Directives**: Structured task descriptions with clear acceptance criteria
- **Task Execution**: Agent processes directives through defined stages (plan → execute → verify)
- **Development Mode**: Extended directives for software development workflows (PR creation, test runs, deployment)

## Configuration

```yaml
# ~/.hermes/config.yaml
skills:
  clawdirect:
    worktree_root: "/tmp/clawdirect-worktrees"
    max_parallel: 4
    timeout_seconds: 1800
  clawdirect-dev:
    test_command: "pytest"
    lint_command: "ruff check"
    deploy_branch_prefix: "deploy/"
```

## Use Cases

1. **Parallel background work**: Agent spawns multiple worktrees, each executing a different task simultaneously
2. **Structured code reviews**: Development mode creates PRs with test verification gates
3. **Task queuing**: Complex multi-step goals broken into sequential directives
4. **Self-healing workflows**: Failed directives automatically retry or escalate

## Workflow Example

```
Agent receives: "Add dark mode toggle to settings"
  → clawdirect creates directive with acceptance criteria
  → clawdirect-dev spawns worktree, checks out feature branch
  → Agent implements changes, runs tests
  → Directive marked complete when tests pass
  → Worktree cleaned up
```

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| Worktree creation fails | Disk space or permission issue | Check `/tmp` write access and free space |
| Directive timeout | Task too complex for timeout window | Increase `timeout_seconds` in config |
| Parallel worktrees conflict | Same branch checked out twice | Use unique branch names per directive |
| `clawdirect-dev` test failures | Test command not configured | Set `test_command` in skill config |

## CorpusIQ Integration

Clawdirect's work tree pattern is ideal for:
- **Multi-agent orchestration**: Combine with CorpusIQ supervisor for distributed task execution
- **PR automation**: Automated PR creation and verification for docs and code repos
- **Background processing**: Long-running tasks don't block the main agent conversation

---

*← [Clawdis Setup](/hermes/skills/catalog/clawdis-setup/) | [Clawdstrike Setup →](/hermes/skills/catalog/clawdstrike-setup/)*

*↑ [Skills Catalog](/hermes/skills/catalog/)*
