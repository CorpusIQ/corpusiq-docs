---
title: Hermes Skill (dandacompany) — Full Setup Guide for Hermes Agents
description: Install, configure, and use the dandacompany/hermes-skill — the most comprehensive third-party Hermes Agent operations guide. 69+ installs.
---

# Hermes Skill (dandacompany) — Setup Guide

**Source:** [dandacompany/hermes-skill](https://github.com/dandacompany/hermes-skill) (2⭐)
**Skill:** `dandacompany/hermes-skill@hermes`
**Installs:** 69
**Category:** Agent Infrastructure
**First Seen:** May 3, 2026

A comprehensive Hermes Agent self-hosting and day-to-day operation skill. Covers the entire lifecycle: install, setup, model/provider selection, gateway platforms, Slack channel setup, command discovery, updates, plugins, tools, skills, memory, profiles, MCP, cron, Kanban, `delegate_task` subagents, logs, dashboards, tutorials, and long-running tmux sessions.

This is the most complete third-party Hermes operations skill on skills.sh. Use it as your primary reference for Hermes Agent administration.

---

## Installation

```bash
npx skills add dandacompany/hermes-skill@hermes
```

Or install the full repo:

```bash
npx skills add https://github.com/dandacompany/hermes-skill --skill hermes
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Hermes Agent** | Any version. Skill auto-detects Hermes installation. |
| **Python 3** | For `hermes_check.py` script |
| **Node.js** | For npx skills CLI |

---

## What It Provides

### 1. Dynamic Command Discovery (`hermes_check.py`)

The skill ships with `scripts/hermes_check.py` — a Python script that introspects the live Hermes installation and returns JSON-structured status. Run at the start of every Hermes task:

```bash
python3 <skill-dir>/scripts/hermes_check.py --json
```

This returns:
- Hermes version and installation path
- Active profile and configuration
- Gateway status
- Available models and providers
- Installed plugins and tools
- MCP server connections
- Active cron jobs
- Memory/storage statistics

### 2. Command Map Generation

Refresh the local command reference snapshot:

```bash
python3 <skill-dir>/scripts/hermes_check.py --write-help <skill-dir>/references/command-map.generated.md
```

This keeps command documentation current even as Hermes ships updates.

### 3. Operational Coverage

| Area | What the Skill Covers |
|---|---|
| **Installation** | Fresh install on Linux, macOS, WSL |
| **Configuration** | `config.yaml`, profiles, environment variables |
| **Models** | Provider selection, model routing, fallback chains |
| **Gateway** | Systemd setup, health checks, death loop recovery |
| **Platform Integrations** | Slack, Telegram, Discord, 27+ messaging platforms |
| **Skills Management** | Install, create, update, delete skills |
| **Memory** | Session DB, Honcho, GBrain, Sibyl-Memory |
| **MCP** | Server configuration, tool discovery, OAuth |
| **Cron** | Schedule, manage, and monitor recurring jobs |
| **Subagents** | `delegate_task` patterns, parallel dispatch |
| **Monitoring** | Logs, dashboards, health checks |
| **Persistence** | Tmux sessions for long-running agent processes |

---

## Quick Start

```bash
# 1. Install the skill
npx skills add dandacompany/hermes-skill@hermes

# 2. Verify Hermes is healthy
python3 <skill-dir>/scripts/hermes_check.py --json

# 3. Load the skill in your agent
skill_view(name="hermes")

# 4. Follow the skill's guidance for your specific task
```

---

## Verification

After installation, verify the skill loaded correctly:

```bash
hermes skills list --marketplace | grep hermes
```

Then run the health check:

```bash
python3 $(find ~/.hermes -name "hermes_check.py" -path "*/dandacompany*" 2>/dev/null | head -1) --json
```

Expected output: JSON object with `version`, `profile`, `gateway_status`, `models`, `mcp_connections`, `cron_jobs_count`.

---

## Common Pitfalls

- **Stale command references:** Hermes CLI updates frequently. Always refresh with `--write-help` before relying on specific command flags.
- **Python path:** The script requires Python 3. On some systems, use `python3` explicitly.
- **Profile mismatch:** The skill detects the active profile automatically, but verify with `hermes profile current` if results seem wrong.

---

## Security

- [Gen Agent Trust Hub: Pass](https://www.skills.sh/dandacompany/hermes-skill/hermes/security/agent-trust-hub)
- [Socket: Pass](https://www.skills.sh/dandacompany/hermes-skill/hermes/security/socket)
- [Snyk: Warn](https://www.skills.sh/dandacompany/hermes-skill/hermes/security/snyk)

---

**Related:** [hermes-agent-framework-setup.md](hermes-agent-framework-setup.md), [hermes-agent-helm-setup.md](hermes-agent-helm-setup.md)
