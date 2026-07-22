---
title: "Hermes Workspace AI Agent UI — Native Web Workspace for Hermes Agent Setup"
description: "196+ installs. Full-featured web workspace for Hermes Agent with chat, terminal, memory browser, skills catalog, swarm mode, and multi-agent orchestration. Setup guide for Hermes agents."
---

# Hermes Workspace AI Agent UI — Setup Guide

**Source:** [aradotso/hermes-skills](https://skills.sh/aradotso/hermes-skills/hermes-workspace-ai-agent-ui) (196+ installs)
**Category:** Hermes Agent / UI & Workspace
**Quality Tier:** 🟡 Beta

Hermes Workspace is a native web interface for Hermes Agent that goes beyond chat — it's a complete workspace with file browsing, persistent sessions, role-based agent dispatch, swarm mode for managing multiple Hermes Agent workers, a 2,000+ skill catalog browser, and full MCP integration. Built with Next.js, Monaco editor, and PTY terminal support.

---

## Installation

```bash
npx skills add aradotso/hermes-skills --skill hermes-workspace-ai-agent-ui
```

### One-Line Install

```bash
curl -fsSL https://raw.githubusercontent.com/outsourc-e/hermes-workspace/main/install.sh | bash
```

### Docker Compose (Recommended)

```bash
git clone https://github.com/outsourc-e/hermes-workspace.git
cd hermes-workspace
docker-compose up -d
# Access at http://localhost:3000
```

### Manual

```bash
git clone https://github.com/outsourc-e/hermes-workspace.git
cd hermes-workspace
pnpm install
cp .env.example .env
echo 'HERMES_API_URL=http://127.0.0.1:8642' >> .env
pnpm dev
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js** | 22+ required |
| **pnpm** | Package manager |
| **Hermes Agent Gateway** | Running on port 8642 (`hermes gateway run`) |
| **Hermes Dashboard** | Optional, port 9119 for enhanced features |

---

## Key Capabilities

### Complete Agent Workspace
- **Chat Interface**: Real-time SSE streaming, tool call rendering, multi-session with markdown + syntax highlighting
- **Terminal & Files**: Monaco-powered file browser with cross-platform PTY terminal
- **Memory Browser**: Search, edit, and manage agent memory with live markdown editor
- **Skills Catalog**: Browse 2,000+ skills with origin badges, filters, and source paths
- **MCP Integration**: Full Model Context Protocol catalog, marketplace, and source management

### Swarm Mode (Multi-Agent)
Persistent tmux-backed agent workers with role-based dispatch:
- `builder`: Code implementation
- `reviewer`: PR review and validation
- `docs`: Documentation
- `research`: Investigation
- `ops`: Operations and deployment
- `triage`: Issue classification
- `qa`: Quality assurance
- `lab`: Experiments

### Conductor Mission Dispatch
Mission decomposition and dispatch with fallback to native swarm orchestration. Supports auto-decomposition mode and Kanban task board.

### PWA Support
Install as native app, access over Tailscale. Works on mobile devices.

---

## Quick Start

```bash
# Terminal 1: Start gateway
hermes gateway run

# Terminal 2: Start dashboard (optional)
hermes dashboard

# Terminal 3: Start workspace
cd ~/hermes-workspace && pnpm dev

# Access at http://localhost:3000
```

### Swarm Mode

```bash
cd ~/hermes-workspace
pnpm swarm:start
# Configure roles in UI: Settings → Swarm → Configure Roles
```

### Remote Access via Tailscale

```bash
echo 'HERMES_API_URL=http://100.x.y.z:8642' >> .env
# Gateway must bind to 0.0.0.0
echo 'API_SERVER_HOST=0.0.0.0' >> ~/.hermes/.env
```

---

## Verification

```bash
# Verify gateway
curl http://127.0.0.1:8642/health

# Verify workspace
curl http://localhost:3000

# Check swarm workers
pnpm swarm:status

# Check connection in Settings → Connection → Test Connection
```

---

## Notes

- Supports local models (Ollama, LM Studio, Atomic Chat) by pointing `HERMES_API_URL` to their endpoints
- Multi-container Docker setup available for production with gateway, dashboard, and workspace orchestration
- Custom themes configurable in `src/styles/themes/` with full color/font customization
- Workspace caches build artifacts — clear `.next` and rebuild if memory issues occur
- Swarm workers use tmux sessions — check `tmux ls` to verify worker processes

---
