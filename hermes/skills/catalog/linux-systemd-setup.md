---
title: Linux Systemd Agent Deployment — Setup Guide
description: Deploy OpenClaw/Hermes agents as Linux systemd services with supervision, logging, restart policies, and resource limits.
---

# Linux Systemd Agent Deployment — Setup Guide

## Prerequisites
- **Linux** system with systemd (Ubuntu 20.04+, Debian 11+, Fedora 35+)
- **OpenClaw / Clawdbot / Hermes** agent installed
- **sudo** access (for system-level services) or **user systemd** (`systemctl --user`)

## Capabilities

| Capability | Description |
|-----------|-------------|
| **Unit File Generation** | Create systemd `.service` files for agent processes |
| **Restart Policies** | `on-failure`, `always`, `no` — with RestartSec delay |
| **Journald Logging** | stdout/stderr automatically captured to journald |
| **Resource Limits** | MemoryMax, CPUQuota, TasksMax for agent processes |
| **Environment Variables** | Inject API keys, tokens, config paths via Environment= |
| **User vs System Services** | Choose user-level (`systemctl --user`) or system-level |

## Installation

```bash
npx skills add alphaonedev/openclaw-graph/linux-systemd
```

## Quick Start

### User-Level Service (Recommended for Agents)

Create `~/.config/systemd/user/hermes-gateway.service`:

```ini
[Unit]
Description=Hermes Agent Gateway
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
ExecStart=/usr/local/bin/hermes gateway run --profile corpusiq
Restart=on-failure
RestartSec=30
MemoryMax=4G
CPUQuota=200%
Environment=HERMES_HOME=/home/hermes/.hermes/profiles/corpusiq
Environment=PATH=/home/hermes/.hermes/node/bin:/usr/local/bin:/usr/bin:/bin

[Install]
WantedBy=default.target
```

Enable and start:

```bash
systemctl --user daemon-reload
systemctl --user enable hermes-gateway.service
systemctl --user start hermes-gateway.service
systemctl --user status hermes-gateway.service
```

### System-Level Service

For agents that need to start at boot before user login:

```ini
[Unit]
Description=Hermes Agent Gateway (System)
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
User=hermes
Group=hermes
ExecStart=/usr/local/bin/hermes gateway run --profile corpusiq
Restart=on-failure
RestartSec=30
MemoryMax=4G
CPUQuota=200%
Environment=HERMES_HOME=/home/hermes/.hermes/profiles/corpusiq

[Install]
WantedBy=multi-user.target
```

Install to `/etc/systemd/system/hermes-gateway.service` and:

```bash
sudo systemctl daemon-reload
sudo systemctl enable hermes-gateway.service
sudo systemctl start hermes-gateway.service
```

## Key Configuration Patterns

### Restart Policy Selection

| Policy | Use When |
|--------|----------|
| `no` | One-shot tasks, cron jobs |
| `on-failure` | Long-running agents (prevents death loops from clean exits) |
| `always` | Critical services that must never stop (use with caution) |

### Resource Limits

```ini
MemoryMax=4G          # Hard memory cap — agent gets OOM-killed if exceeded
MemoryHigh=3G         # Soft limit — agent gets throttled
CPUQuota=200%         # Max 2 CPU cores
TasksMax=512          # Max threads/processes
```

### Viewing Logs

```bash
# User service
journalctl --user -u hermes-gateway.service -f

# System service
journalctl -u hermes-gateway.service -f --since "10 minutes ago"
```

## CorpusIQ Use Cases

1. **Gateway Service:** The CorpusIQ Hermes gateway runs as `hermes-gateway-corpusiq.service` on DGX Spark. `Restart=on-failure` prevents death loops from CLI `--replace` conflicts.

2. **Cron Workers:** Long-running monitor workers (email, social) can run as systemd services instead of cron, giving better logging and restart behavior.

3. **Multi-Agent Deployments:** Each agent profile gets its own systemd unit — isolation via MemoryMax and separate environment variables.

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| Service in `activating (auto-restart)` loop | Gateway crashing on start | Check `journalctl --user -u <service> -n 50` for error |
| `ExecStartPost` exits code 1 | Post-start script failing | Add `|| true` guard or fix the script |
| OOM kill in logs | MemoryMax too low | Raise MemoryMax or investigate memory leak |
| Service stops after SSH disconnect | Using system service without `linger` | Run `loginctl enable-linger <user>` |

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace](/hermes/skills/marketplace/) →*
*↑ [Skills Home](/hermes/skills/)*

---

*Curated by CorpusIQ — one MCP endpoint, all your business tools.*
