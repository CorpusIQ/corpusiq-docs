---
title: Godmode — Autonomous Execution Mode Setup
description: Install and configure godmode from nousresearch/hermes-agent. Fully autonomous execution mode that bypasses confirmation gates — 138 installs.
category: hermes-skills
publisher: nousresearch
installs: 138
source: https://skills.sh/nousresearch/hermes-agent/godmode
---

# Godmode — Setup Guide

**Source:** [nousresearch/hermes-agent](https://skills.sh/nousresearch/hermes-agent/godmode) (138 installs)
**Category:** Autonomous Execution
**License:** MIT · **Platforms:** Linux, macOS, Windows
**Dependencies:** Hermes Agent v0.14.0+

Godmode switches Hermes into fully autonomous execution — bypassing confirmation gates, approval prompts, and safety checks. Designed for trusted, isolated environments where the operator wants Hermes to execute without interruption.

⚠️ **WARNING:** Godmode disables all confirmation prompts. Only enable in sandboxed, isolated, or fully trusted environments. Not recommended for production systems with write access to critical infrastructure.

---

## What It Does

| Capability | How |
|-----------|-----|
| **Bypass confirmations** | All `confirm` gates are auto-approved |
| **Autonomous execution** | No "are you sure?" prompts — just execution |
| **Full tool access** | All tools available without per-call approval |
| **Session-scoped** | Godmode applies to the current session only |
| **Audit trail** | All actions still logged — just not gated |

---

## Installation

### Via skills.sh (Recommended)

```bash
npx skills add nousresearch/hermes-agent --skill godmode
```

### Direct from Hermes Agent Repo

```bash
git clone --depth 1 https://github.com/nousresearch/hermes-agent.git /tmp/hermes-agent
cp -r /tmp/hermes-agent/skills/development/godmode ~/.hermes/skills/
```

---

## Usage

### Activating Godmode

```
Hermes, enable godmode and deploy the latest build to staging.
```

Once godmode is active, Hermes executes without asking for confirmation:

```
# Without godmode:
"Delete all unused Docker images."
→ "I found 47 unused images. Confirm deletion? [y/N]"

# With godmode:
"Delete all unused Docker images."
→ [Immediately executes docker image prune -a]
→ "Deleted 47 unused images. Reclaimed 12.3 GB."
```

---

## Safety Recommendations

| Environment | Godmode Safe? | Notes |
|-------------|--------------|-------|
| Local dev machine | ✅ Yes | You can undo mistakes |
| Sandboxed CI | ✅ Yes | Ephemeral environment |
| Staging server | ⚠️ Conditional | Set resource limits first |
| Production | ❌ No | Use confirmation gates |
| Database migration | ❌ No | Always review before executing |

---

## Configuration

Godmode can be scoped to specific tool categories:

```yaml
godmode:
  enabled: true
  scope:
    - "file_operations"    # Allow: read/write/delete files
    - "git_operations"     # Allow: commit/push/merge
    - "shell_commands"     # Allow: arbitrary terminal commands
  exclude:
    - "production_deploy"  # Never auto-approve production deploys
    - "database_migration" # Never auto-approve DB changes
  max_session_duration: 3600  # Auto-disable after 1 hour
```

---

## Verification

After install, test in a safe environment:

```bash
# Create a test directory
mkdir /tmp/godmode-test

# Test godmode execution
hermes chat -q "Enable godmode. Create a file called test.txt in /tmp/godmode-test with the text 'godmode works'."

# Verify the file was created without confirmation
cat /tmp/godmode-test/test.txt
```

---

## Pitfalls

- **⚠️ No undo for destructive actions:** Godmode bypasses all confirmations. A `rm -rf` command executes immediately with no "are you sure?" prompt.
- **⚠️ Not for production:** Never enable godmode on systems with production databases, customer data, or infrastructure that can't be easily restored.
- **Session scoping:** Godmode applies to the current session only. New sessions default to normal (gated) mode. But if you persist godmode in config, all sessions start in godmode.
- **Audit trail only:** While all actions are logged, there's no blocking mechanism. You can only see what happened after the fact.
- **Tool scope is additive:** If you scope godmode to `file_operations` but the agent chains a file operation into a shell command, the shell command executes in godmode too.

---

## See Also

- [kanban-orchestrator-setup.md](kanban-orchestrator-setup.md) — Task decomposition for autonomous execution
- [plan-setup.md](plan-mode-setup.md) — Plan mode (opposite: plan without executing)
- [writing-plans-subagent-development-setup.md](writing-plans-subagent-development-setup.md) — Structured planning with subagent execution

---

*Setup guide by CorpusIQ. Source: [nousresearch/hermes-agent](https://github.com/nousresearch/hermes-agent) (MIT).*
