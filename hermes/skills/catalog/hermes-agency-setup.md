---
title: Hermes Agency — P2P Agent Collaboration Setup Guide
description: End-to-end setup for Hermes Agency — P2P agent discovery, encrypted communication, and multi-agent orchestration via AgentAnycast SDK for Hermes Agent profiles.
skill_name: hermes-agency
author: DeployFaith
stars: 0
license: Apache 2.0
created: June 22, 2026
last_updated: June 22, 2026
---

# Hermes Agency — P2P Agent Collaboration Setup Guide

**Author:** [DeployFaith](https://github.com/DeployFaith)
**Repo:** [DeployFaith/Hermes_Agency](https://github.com/DeployFaith/Hermes_Agency)
**SDK:** [AgentAnycast Python SDK](https://github.com/AgentAnycast/agentanycast-python) (Apache 2.0, PyPI: `agentanycast`)
**Created:** June 22, 2026

A Hermes plugin that gives every Hermes profile its own P2P node with a persistent identity, auto-generated AgentCard from `SOUL.md` + installed skills, and encrypted P2P communication with other agents — across LAN or WAN.

> **Status:** Local testing / PR-prep. Early stage — actively developed.

---

## What It Does

| Feature | Description |
|---------|-------------|
| **Profile AgentCards** | Auto-generated from `SOUL.md`, installed skills, and non-secret config allowlist |
| **Node Lifecycle** | Start/stop per-profile P2P nodes with persistent Ed25519 identity |
| **Peer Discovery** | Find agents by skill through LAN peer discovery + relay-backed anycast registry |
| **Team Context** | Compact teammate summaries injected through plugin context, bounded by config budgets |
| **Task Send/Receive** | Send tasks to peers, receive tasks from remote agents, return artifacts to the sender |
| **Safe Incoming Handler** | Remote tasks default to safe/no-dangerous-tool behavior unless explicitly enabled |
| **Kanban Tracking** | Outbound and inbound A2A tasks reconcile with Hermes Kanban when available |
| **Autonomous Collaboration** | Self-registration, bidding, workflows, proactive tasks, autonomy checks, routing-correction logging |
| **CLI + Slash Commands** | `hermes agency ...` and `/agency ...` for status/start/stop/discovery |

---

## Architecture

```text
┌─────────────┐         mDNS / Relay         ┌─────────────┐
│  Hermes A   │<------------------------------>│  Hermes B   │
│  (Python)   │     E2E encrypted (Noise)     │  (Python)   │
└──────┬──────┘                               └──────┬──────┘
       | gRPC                                        | gRPC
┌──────┴──────┐                               ┌──────┴──────┐
│ agentanycastd│                               │ agentanycastd│
│  (Go daemon)│<---------- libp2p ------------>│  (Go daemon) │
└─────────────┘                               └──────────────┘
```

Each Hermes profile gets its own daemon home at `~/.hermes/profiles/<profile>/.agency/`.

### Plugin Structure

```text
Hermes profile
├── config.yaml          → agency.* settings
├── SOUL.md              → AgentCard name/description source
├── skills/**/SKILL.md   → AgentCard skill source
└── plugins/hermes-agency/
    ├── plugin.yaml      → plugin metadata (19 tools, 5 hooks)
    ├── __init__.py      → tool/CLI/slash/hook registration
    ├── config.py        → profile-safe config resolver
    ├── card_builder.py  → AgentCard builder with secret-safe metadata
    ├── node_manager.py  → daemon/node lifecycle, incoming queue, registry refresh
    ├── tools.py         → a2a_* model tools (14 tools)
    ├── orchestrator.py  → orch_* model tools (5 tools)
    ├── announcements.py → Team context, blocked state, policy announcements
    ├── context_packet.py→ Context packet builder
    ├── bidding.py       → Task bidding and best-bid selection
    ├── kanban_bridge.py → Hermes Kanban integration
    ├── learning.py      → Routing-correction feedback logging
    └── discord_bridge.py→ Discord channel bridge
```

---

## Tools (19 Total)

### Agent-to-Agent (14 tools)

| Tool | Description |
|------|-------------|
| `a2a_info` | Show plugin/SDK/card/node status; use `compact: true` for health checks |
| `a2a_start_node` | Start this profile's P2P node |
| `a2a_stop_node` | Stop the node cleanly |
| `a2a_list_peers` | List connected P2P peers |
| `a2a_discover` | Find agents by skill through anycast routing |
| `a2a_send` | Send a task to a `peer_id` or skill and optionally wait for completion |
| `a2a_status` | Check latest tracked status/artifacts for a sent task |
| `a2a_inbox` | Inspect recent incoming tasks |
| `a2a_registry` | List live self-registration records |
| `a2a_bid_task` | Record/simulate bids and optionally assign the best bidder |
| `a2a_execute_workflow` | Create dependency-linked Kanban tasks from configured workflows |
| `a2a_create_proactive_task` | Create proactive tasks when enabled |
| `a2a_check_autonomy` | Check autonomy policy for a proposed action |
| `a2a_log_routing_correction` | Record routing-correction feedback when learning is enabled |

### Orchestrator (5 tools — only for promoted orchestrator profiles)

| Tool | Description |
|------|-------------|
| `orch_route` | Route tasks to the best peer by skill |
| `orch_decompose` | Decompose complex tasks into sub-tasks |
| `orch_status` | Check orchestrator state |
| `orch_list_tasks` | List all tracked tasks |
| `orch_escalate` | Escalate stuck/blocked tasks |

---

## Installation

### Requirements

- Python 3.10+
- Hermes Agent with user-plugin support
- `agentanycast` Python SDK: `pip install agentanycast`
- Optional for cross-network discovery: a relay with registry service

### Option A: Symlink (Development)

```bash
git clone https://github.com/DeployFaith/Hermes_Agency.git ~/src/hermes-agency
ln -s ~/src/hermes-agency/hermes-agency ~/.hermes/profiles/corpusiq/plugins/hermes-agency
```

### Option B: Copy (Standalone)

```bash
git clone https://github.com/DeployFaith/Hermes_Agency.git /tmp/hermes-agency
mkdir -p ~/.hermes/profiles/corpusiq/plugins
cp -r /tmp/hermes-agency/hermes-agency ~/.hermes/profiles/corpusiq/plugins/hermes-agency
```

### Install the Python SDK

```bash
pip install agentanycast

# Or with framework adapters
pip install agentanycast[crewai,langgraph]      # CrewAI + LangGraph
pip install agentanycast[openai-agents,claude]  # OpenAI + Claude Agent SDK
```

---

## Configuration

Add to your active profile's `config.yaml`:

```yaml
plugins:
  enabled:
    - agency

agency:
  enabled: true                 # Runtime gate after plugin is enabled
  auto_start: false             # true = start node on session/plugin load
  relay: null                   # libp2p relay multiaddr for cross-network transport
  skills_from_profile: true     # Generate AgentCard skills from installed Hermes skills
  allow_remote_tasks: false     # false = safe stub / no real execution
  trusted_peers: []             # peer_id allowlist, reserved for stricter policies
  incoming_queue_limit: 100
  card_name: null               # Optional public display name override
  daemon_bin: null              # Optional explicit daemon path; prevents SDK auto-download/overwrite

  incoming:
    mode: delegation            # template, delegation, subprocess
    delegation_timeout: 120
    tool_access: safe           # safe, none, full
    max_iterations: 25
    subprocess_profile: null
    reject_unmatched_skills: false
    send_progress: false
    conversation_ttl: 3600
    conversation_max_turns: 20

  team:
    auto_discover: true
    auto_register: true
    inject_context: true
    kanban_integration: true
    self_serve: true
    announce_progress: false
    tenant: default
    context_refresh_minutes: 5
    max_context_peers: 5
    max_context_skills: 5
    context_max_chars: 4000

  orchestrator:
    enabled: false
    agent: null
    auto_decompose: true

  routing: {}
```

### Relay / Registry Setup

For relay-backed skill discovery, set the daemon environment:

```bash
export AGENTANYCAST_REGISTRY_ADDRS=100.123.57.115:50052
```

Relay/bootstrap and skill registry are separate: `agency.relay` connects libp2p; `AGENTANYCAST_REGISTRY_ADDRS` enables anycast skill discovery.

---

## CLI / Slash Commands

```bash
# CLI
hermes agency status
hermes agency start
hermes agency stop
hermes agency discover <skill>
hermes agency registry
hermes agency promote <profile>
hermes agency demote <profile>
```

```text
# In a Hermes session
/agency status
/agency start
/agency stop
/agency discover <skill>
/agency registry
```

---

## Security Model

| Layer | Policy |
|-------|--------|
| **Plugin loading** | Opt-in via `plugins.enabled` |
| **Runtime operation** | Gated by `agency.enabled` |
| **Remote task execution** | Defaults to safe behavior — no terminal/file access granted by default |
| **Incoming processor** | Uses delegation/subprocess modes only when explicitly configured |
| **AgentCard exposure** | Only non-secret metadata: provider/model names, configured booleans, profile/toolset summaries. NEVER exposes API keys, raw env vars, Discord channel IDs, local daemon paths, or profile-private data |
| **Daemon/relay** | External runtime components — NOT vendored into the plugin |

---

## Quick Start: Two-Agent Demo

### Agent 1 (Receiver)

```python
# In a Hermes session on Machine 1
/agency start
# → "Node running — Peer ID: 12D3KooW..."
```

### Agent 2 (Sender)

```python
# In a Hermes session on Machine 2 (same LAN)
/agency start
/agency discover echo
# → "Found: EchoAgent (12D3KooW...)"

/agency send peer_id=12D3KooW... "Hello from Agent 2!"
# → "Result: Echo: Hello from Agent 2!"
```

### CLI Equivalent

```bash
# Direct
agentanycast send 12D3KooW... "Hello!"

# By skill (anycast)
agentanycast send --skill translate "Bonjour!"

# Discovery
agentanycast discover translate
```

---

## Three Ways to Send a Task

```python
# 1. Direct — by Peer ID
await node.send_task(peer_id="12D3KooW...", message=msg)

# 2. Anycast — by skill (relay resolves the target)
await node.send_task(skill="translate", message=msg)

# 3. HTTP Bridge — to standard HTTP A2A agents
await node.send_task(url="https://agent.example.com", message=msg)
```

---

## Framework Adapters

Turn existing frameworks into P2P agents with one function call:

```python
from agentanycast.adapters.crewai import serve_crew
from agentanycast.adapters.langgraph import serve_graph
from agentanycast.adapters.adk import serve_adk_agent
from agentanycast.adapters.openai_agents import serve_openai_agent
from agentanycast.adapters.claude_agent import serve_claude_agent
from agentanycast.adapters.strands import serve_strands_agent

await serve_crew(crew, card=card, relay="...")
await serve_graph(graph, card=card, relay="...")
await serve_adk_agent(agent, card=card, relay="...")
await serve_openai_agent(agent, card=card, relay="...")
await serve_claude_agent(prompt_template="...", card=card)
await serve_strands_agent(agent, card=card)
```

---

## Interoperability

```python
# W3C DID
from agentanycast.did import peer_id_to_did_key, did_key_to_peer_id
did = peer_id_to_did_key("12D3KooW...")      # "did:key:z6Mk..."
pid = did_key_to_peer_id("did:key:z6Mk...")  # "12D3KooW..."

# MCP Tool ↔ A2A Skill mapping
from agentanycast.mcp import mcp_tools_to_agent_card
card = mcp_tools_to_agent_card(mcp_tools, name="MCPAgent")

# A2A v1.0 JSON format
from agentanycast.compat.a2a_v1 import task_to_a2a_json, task_from_a2a_json

# OASF / AGNTCY Directory
from agentanycast.compat.oasf import card_to_oasf_record
from agentanycast.compat.agntcy import AGNTCYDirectory
```

---

## Validation

```bash
# Unit tests
python -m pytest hermes-agency/tests/test_unit.py -q

# Syntax check
python -m py_compile hermes-agency/*.py

# E2E (local P2P — no relay/registry required)
python hermes-agency/tests/test_e2e.py

# Full E2E (with relay/registry — set env vars first)
export AGENTANYCAST_E2E_REGISTRY=...
export AGENTANYCAST_E2E_RELAY=...
python hermes-agency/tests/test_e2e_full.py
```

---

## Why This Matters for CorpusIQ

This is the **first P2P multi-agent plugin** discovered for Hermes Agent that doesn't require SSH, centralized servers, or shared infrastructure. Key innovations:

- **Drop-in-mailbox architecture** — Agents communicate via encrypted P2P messages, not synchronous HTTP calls. No timeouts, no SSH tunnels.
- **LAN + WAN** — mDNS for same-network discovery, relay for cross-network. Zero-config local; one env var for global.
- **Skill-based anycast** — Send a task to "translate" and the relay finds the right agent. No hardcoded peer IDs.
- **Safe by default** — Remote agents can't access terminal/file tools unless explicitly configured.
- **Framework-agnostic** — Serve CrewAI, LangGraph, OpenAI Agents, Claude Agent SDK, or Strands agents as P2P nodes.

This is the foundation for truly decentralized CorpusIQ agent swarms — autonomous operators that discover each other, bid on work, and collaborate without a central orchestrator.

---

## Known Limitations

- **Early stage** — Created June 22, 2026. Actively developed but not production-hardened.
- **Relay required for WAN** — LAN works out of the box; cross-network needs a deployed relay.
- **Orchestrator profile promotion** — Manual via `hermes agency promote`. No auto-election yet.
- **No upstream PR yet** — Do not open PRs to NousResearch/hermes-agent unless author explicitly asks.

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace Home](/hermes/skills/marketplace/) | [DeployFaith/Hermes_Agency on GitHub](https://github.com/DeployFaith/Hermes_Agency)*
