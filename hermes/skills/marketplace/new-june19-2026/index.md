---
title: New Skills  --  June 19, 2026 (Hermes AgentMesh + Windows Native)
description: 4 newly discovered skills and tools  --  async multi-agent message bus, Windows-native setup package, polymarket trading bot, and video translation. Plus Graphify adds Hermes platform support.
---

# New Skills  --  June 19, 2026

**Sources:** skills.sh, GitHub discovery
**Date:** June 19, 2026
**Total new:** 4 skills/tools

Post-June 18 final sweep, the ecosystem continues to grow. Today's findings include a breakthrough multi-agent communication bus designed by a Hermes agent architect, a Windows-native deployment package, and continued OpenClaw ecosystem expansion.

---

## Hermes Agent Ecosystem (2 new)

| # | Skill/Tool | Installs | Description |
|---|-----------|----------|-------------|
| 1 | `hermes-agentmesh-async-bus` | 1/day trending | Peer-to-peer, 0-SSH, Redis-backed async message bus for multi-agent systems  --  Hermes, OpenClaw, LangGraph, AutoGen, CrewAI |
| 2 | `hermes-windows-native` |  --  | Windows-native integrated package: Hermes Agent + WebUI, no Docker, no WSL2. One-click PowerShell startup |

## OpenClaw Ecosystem (2 skills via aradotso/hermes-skills)

| # | Skill | Installs | Description |
|---|-------|----------|-------------|
| 3 | `openclaw-polymarket-trading-bot` | 7/day trending | Polymarket prediction market trading bot  --  query markets, place bets, track positions |
| 4 | `openclaw-videotranslate-skill` |  --  | Video translation pipeline  --  extract, translate, and dub video content |

---

## Spotlight: Hermes AgentMesh Async Bus

**Source:** [seleman66eeddwegger3-art/hermes-agentmesh](https://github.com/seleman66eeddwegger3-art/hermes-agentmesh)
**Designed by:** Bobo, a Hermes agent architect

### The Problem It Solves

Multi-agent coordination historically fails in three ways:
1. **Group chat noise**  --  Telegram/Discord message storms eat context tokens, leak credentials
2. **Synchronous HTTP timeouts**  --  Agent tool calls take 5–15 minutes; HTTP connections die at 300–600s
3. **SSH overhead**  --  Remote process execution requires SSH; reports must be scp'd

### The Solution: "Drop in Mailbox, Don't Call"

AgentMesh replaces synchronous HTTP with **Redis-backed named inboxes** (`inbox:<NODE_NAME>`). Any node pushes a task to any inbox; workers listen and process asynchronously. The mailbox is the protocol.

```
HTTP Synchronous ("phone call")     Redis Queue ("mailbox")
requests.post(url, timeout=600)     redis.lpush("inbox:bobo", task_json)
Client blocks waiting               Client returns immediately
Timeout at 5–10 minutes             Hours-long tasks OK
Cross-machine needs SSH             0 SSH  --  shared Redis + HTTP LLM
Report must be scp'd                Report lands on initiator's machine
```

### Architecture

```
┌─────────── Mac mini (central hub) ───────────┐
│ Redis :6379 │ Hermes API :8642 │ HTTP :8080  │
└──────────────────┬───────────────────────────┘
                   │ 0.7ms LAN Redis
        ┌──────────┼──────────┐
        ▼                     ▼
   Worker Node           Worker Node
   (macOS)               (Linux/Pi/WSL)
```

### Key Facts
- Mac mini runs Redis + LLM API + file server
- All nodes are pure Redis clients, no SSH needed
- Systemd/LaunchAgents keep workers alive
- Reports land naturally on the initiating machine
- Works across Hermes, OpenClaw, LangGraph, AutoGen, CrewAI

---

## Spotlight: Hermes Windows Native

**Source:** [markwang2658/hermes-windows-native](https://github.com/markwang2658/hermes-windows-native)
**Stars:** 20 ⭐ | **License:** MIT

A Windows-native integrated package bundling Hermes Agent v0.16.0 + Hermes WebUI v0.51.454 with:
- Shared `.venv` for both components
- PowerShell launchers  --  Agent, WebUI, and one-click startup
- Runtime data redirected to `%USERPROFILE%\.hermes`
- No Docker, no WSL2  --  lightest local footprint on Windows

### Quick Start
```powershell
git clone https://github.com/markwang2658/hermes-windows-native.git hermes-windows
cd hermes-windows
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e ".[all]"  # Agent
# Install WebUI deps, then:
.\hermes-start\hermes-start.ps1  # One-click startup
```

---

## Installation

```bash
# Hermes AgentMesh async bus
npx skills add seleman66eeddwegger3-art/hermes-agentmesh --skill hermes-agentmesh-async-bus

# OpenClaw Polymarket trading bot
npx skills add Golrypavium/openclaw-polymarket-trading-bot --skill openclaw-polymarket-trading-bot

# OpenClaw Video translate
npx skills add zbjincheng/openclaw-skill-videotranslate --skill openclaw-videotranslate-skill

# Hermes Windows Native (not a skills.sh skill  --  git clone)
git clone https://github.com/markwang2658/hermes-windows-native.git
```

---

## Ecosystem Note: Graphify Adds Hermes Support

[Graphify](https://github.com/safishamsi/graphify) (`pip install graphifyy`)  --  the "turn any folder into a queryable knowledge graph" tool  --  now supports Hermes Agent as a first-class platform. Install with:

```bash
graphify install --platform hermes
```

This writes `~/.hermes/skills/graphify/SKILL.md` and `AGENTS.md` so Hermes agents can use `/graphify .` to analyze codebases without leaving the conversation.

---

## Why This Matters

1. **AgentMesh is a paradigm shift**  --  Moving from synchronous HTTP to async Redis mailboxes changes how multi-agent systems coordinate. No more timeout anxiety, no more SSH setup, no more lost reports. This is the kind of infrastructure the Hermes ecosystem needs for production multi-agent deployments.

2. **Windows Native lowers the barrier**  --  Docker and WSL2 are genuine obstacles for Windows users. A one-click PowerShell launcher with a shared venv makes Hermes accessible to a vastly larger audience.

3. **Graphify Hermes integration**  --  Knowledge graph visualization directly inside agent conversations is a powerful workflow. Being able to run `/graphify .` and get an interactive HTML graph from Hermes extends the agent's analytical capabilities.

4. **Continued OpenClaw expansion**  --  The Polymarket trading bot and video translation skill show the OpenClaw ecosystem continues to grow alongside Hermes, with cross-pollination through `aradotso/hermes-skills`.

---

## Catalog Updates

- **Marketplace index:** Updated with this page
- **Ecosystem page:** Added windows-native and agentmesh entries
- **Total documented marketplace skills:** 336 + 4 = 340+

---

*← [Skills Marketplace](/hermes/skills/marketplace/) | [June 18 Final Sweep](/hermes/skills/marketplace/new-june18-2026-final-sweep/) →*
*↑ [Skills Catalog Home](/hermes/skills/catalog/)*
*Powered by CorpusIQ*
