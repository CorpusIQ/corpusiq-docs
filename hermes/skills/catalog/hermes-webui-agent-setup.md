---
title: "Hermes WebUI Agent — Browser-Based Hermes Agent Interface Setup"
description: "240+ installs. Deploy, configure, and use Hermes WebUI — a web interface for Hermes Agent with persistent memory, scheduled jobs, and multi-platform messaging."
---

# Hermes WebUI Agent — Setup Guide

**Source:** [aradotso/hermes-skills](https://skills.sh/aradotso/hermes-skills/hermes-webui-agent) (240+ installs)
**Category:** Hermes Agent / UI & Deployment
**Quality Tier:** 🟡 Beta

Expert skill for deploying, configuring, and using Hermes WebUI — a lightweight web interface for Hermes Agent built on Flask. Provides browser-based access with three-panel layout (sessions sidebar, chat center, workspace file browser), persistent memory, scheduled cron jobs, and 10+ messaging platform integrations.

---

## Installation

```bash
npx skills add aradotso/hermes-skills --skill hermes-webui-agent
```

### Native Python (Recommended)

```bash
git clone https://github.com/nesquena/hermes-webui.git
cd hermes-webui
python3 bootstrap.py
# Auto-detects Hermes Agent, creates venv, starts on http://localhost:8787
```

### Docker

```bash
git clone https://github.com/nesquena/hermes-webui
cd hermes-webui
cp .env.docker.example .env
docker compose up -d
# Open http://localhost:8787
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Python** | 3.10+ for native install |
| **Docker** | For containerized deployment |
| **Hermes Agent** | Installed or auto-detected by bootstrap |
| **Model Provider** | OpenAI, Anthropic, DeepSeek, OpenRouter, or local Ollama |

---

## Key Capabilities

### Browser-Based Agent Access
Full three-panel WebUI with sessions sidebar, chat center with markdown + syntax highlighting, and workspace file browser. Supports real-time SSE streaming, tool call rendering, and multi-session management.

### Scheduled Jobs Dashboard
Create, view, and manage cron-style jobs from the WebUI Control Center. Jobs run offline and deliver results via Telegram, Discord, Slack, Signal, or email.

### Messaging Platform Integration
Configure 10+ messaging platforms directly from WebUI. Supports Telegram bots, Discord webhooks, Slack webhooks, Signal (via signal-cli), and email delivery for scheduled job output.

### Self-Hosted with Security
Password protection, SSH tunneling for remote access, and reverse proxy support (Nginx example included). All conversations and memory stay on your hardware.

### Daemon Lifecycle Management
Full `ctl.sh` daemon control: start, stop, restart, status, and log viewing. Writes logs to `~/.hermes/webui.log` and PID to `~/.hermes/webui.pid`.

---

## Quick Start

```bash
# Clone and bootstrap (one-command setup)
git clone https://github.com/nesquena/hermes-webui.git && cd hermes-webui
python3 bootstrap.py

# Or Docker
docker compose up -d

# Access at http://localhost:8787
```

### Remote Access via SSH Tunnel

```bash
# On your local machine
ssh -L 8787:localhost:8787 user@your-server.com
# Then open http://localhost:8787
```

### Password Protection (Required for Network Exposure)

```bash
echo "HERMES_WEBUI_PASSWORD=your-strong-password" >> .env
docker compose up -d --force-recreate
```

---

## Verification

```bash
# Check health endpoint
curl http://localhost:8787/health

# Check daemon status (if using ctl.sh)
./ctl.sh status

# Check logs
./ctl.sh logs --lines 50
```

---

## Notes

- Bootstrap auto-detects Hermes Agent installation — no manual path configuration needed
- Docker supports single-container, two-container (agent+webui isolated), and three-container (agent+dashboard+webui) setups
- Supports Podman with some limitations (known issue with shared `.hermes` in Podman 3.4 — upgrade to Podman 4+)
- Workspace file browser mirrors `HERMES_WEBUI_DEFAULT_WORKSPACE` directory
- For production, use reverse proxy (Nginx) with HTTPS and password protection enabled

---
