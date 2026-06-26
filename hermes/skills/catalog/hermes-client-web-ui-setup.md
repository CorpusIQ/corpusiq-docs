---
title: Hermes Client Web UI — Full Setup Guide for Hermes Agents
description: Install, configure, and use the hermes-client-web-ui skill from aradotso/devtools-skills. Web-based chat dashboard for Hermes Agent with multi-profile management, SSE streaming, and terminal integration.
---

# Hermes Client Web UI — Setup Guide

**Source:** [aradotso/devtools-skills](https://skills.sh/aradotso/devtools-skills) (59 installs) | [GitHub](https://github.com/lotsoftick/hermes_client)
**Category:** interface, dashboard

A web-based chat interface for the Hermes Agent by Nous Research. Manages multiple Hermes profiles as separate "agents", runs conversations with full streaming via SSE, and provides an interactive terminal for setup commands. Each UI agent maps 1:1 to a Hermes profile with its own home directory, config, and sessions.

---

## Installation

```bash
# Install the skill
npx skills add aradotso/devtools-skills --skill hermes-client-web-ui

# Clone and start the web UI
git clone https://github.com/lotsoftick/hermes_client.git
cd hermes_client
npm start
```

`npm start` builds, deploys to `~/.hermes_client`, installs auto-start (LaunchAgent on macOS / Startup on Windows), and creates the global `hermes_client` command.

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js 18+** | Required for the web server |
| **Hermes Agent** | Must be installed with `hermes` on `PATH` |
| **Git** | Required for cloning and auto-update |
| **Build Tools** | Windows: Visual Studio Build Tools (for native modules) |

---

## Key Capabilities

### Core Features

| Capability | How to Trigger | Notes |
|---|---|---|
| Web chat interface | Open `http://localhost:18888` | Browser-based Hermes conversations |
| Multi-profile management | Select profile in UI dropdown | Each profile maps to `~/.hermes/profiles/<name>/` |
| SSE streaming | Automatic in chat | Real-time streaming of agent responses |
| Interactive terminal | Terminal tab in UI | Run `hermes` CLI commands directly |
| API access | `http://localhost:18889` | REST API for programmatic access |
| Auto-start service | `npm start` configures this | LaunchAgent (macOS) or Startup (Windows) |

### Service Management

```bash
hermes_client start      # Start the web server
hermes_client stop       # Stop the web server
hermes_client restart    # Restart the web server
hermes_client status     # Check if running
```

### Default Access

| Resource | URL | Credentials |
|---|---|---|
| Web Client | http://localhost:18888 | admin@admin.com / 123456 |
| API | http://localhost:18889 | Same credentials |

---

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Team dashboard** | Deploy on internal network for team access to shared Hermes profiles |
| **Multi-agent monitoring** | Manage separate profiles for Growth, Support, and Dev agents in one UI |
| **Remote access** | Tunnel via SSH or Tailscale to access Hermes from mobile/tablet |
| **Demo environment** | Use web UI for client demos — cleaner than terminal output |
| **Training/onboarding** | New team members interact with Hermes through familiar chat interface |

---

## Troubleshooting

| Issue | Fix |
|---|---|
| Port 18888 already in use | Change port in `~/.hermes_client/config.json` |
| "hermes not found" | Verify `hermes` is on PATH: `which hermes` |
| Blank page on load | Check Node.js version: `node --version` (needs 18+) |
| npm install fails (Windows) | Install Visual Studio Build Tools with "Desktop development with C++" |
| Auto-start not working | Re-run `npm start` to reconfigure LaunchAgent/Startup |
| Login fails | Default credentials: admin@admin.com / 123456 |

## Verification

```bash
# Verify skill installed
hermes skills list | grep hermes-client-web-ui

# Start the web server
hermes_client start

# Check it's running
curl -s http://localhost:18889/api/health

# Open in browser
open http://localhost:18888   # macOS
# Or: xdg-open http://localhost:18888  # Linux
```

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Discovery Page](/hermes/skills/marketplace/new-june25-2026-update/) →*
*Curated by CorpusIQ — one MCP endpoint, all your business tools.*
