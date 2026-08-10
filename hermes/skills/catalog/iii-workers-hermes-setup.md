---
title: III Workers Hermes Bridge — Full Setup Guide for Hermes Agents
description: Put the Hermes agent on the iii bus — omnichannel front door wiring Hermes's 27+ messaging platforms to the entire iii function registry.
---

# III Workers Hermes Bridge — Setup Guide

**Source:** [iii-hq/workers](https://github.com/iii-hq/workers) (90⭐)
**Skill:** `iii-hq/workers@hermes`
**Installs:** 5
**Category:** Agent Infrastructure / Multi-Agent
**First Seen:** Jun 29, 2026

The `hermes` worker puts the Hermes agent on the iii bus. `hermes::run` runs one headless Hermes turn carrying the iii runtime context, so the agent discovers and drives the whole engine live. `hermes::send` delivers to any of Hermes's 27+ messaging platforms. Inbound platform messages and webhook events arrive on the worker's HTTP sink (`hermes::inbound`) and republish so any iii worker can react.

Hermes becomes iii's omnichannel front door: chat-platform reach wired to the entire function registry.

---

## Installation

```bash
npx skills add iii-hq/workers@hermes
```

Or install from the monorepo:

```bash
npx skills add https://github.com/iii-hq/workers --skill hermes
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Hermes Agent** | Installed and configured with `~/.hermes/.env` |
| **III Runtime** | The iii bus engine running locally or remotely |
| **Hermes Credentials** | Pre-provisioned — the worker reads from `~/.hermes/.env` |
| **Node.js** | For the iii runtime |

---

## Architecture

```
┌─────────────────────────────────────────────────┐
│                  iii Bus                         │
│  ┌──────────┐  ┌──────────┐  ┌──────────────┐  │
│  │ worker A │  │ worker B │  │ hermes worker │  │
│  └──────────┘  └──────────┘  └──────┬───────┘  │
│                                      │           │
│                          ┌───────────▼────────┐  │
│                          │  hermes::run        │  │
│                          │  hermes::send       │  │
│                          │  hermes::inbound    │  │
│                          └────────────────────┘  │
└─────────────────────────────────────────────────┘
         │                    │
         ▼                    ▼
┌─────────────────┐  ┌──────────────────┐
│ 27+ Messaging   │  │ Function Registry │
│ (Telegram,      │  │ (any iii worker   │
│  Slack, Discord,│  │  can react to     │
│  WhatsApp...)   │  │  inbound events)  │
└─────────────────┘  └──────────────────┘
```

---

## Worker API

### `hermes::run`

Runs one headless Hermes turn carrying the iii runtime context. The agent discovers the full iii engine and can call any function in the registry.

```
iii → hermes::run(context) → Hermes Agent executes → result returned to bus
```

### `hermes::send`

Delivers messages to any of Hermes's 27+ messaging platforms. Target platform is specified in the message payload.

```
iii → hermes::send(platform="telegram", chat="topic_2", message="...") → delivered
```

### `hermes::inbound`

HTTP sink that receives inbound platform messages and webhook events. These are republished on the iii bus so any worker can react.

```
Telegram/Slack/Discord → hermes::inbound → iii bus → any worker reacts
```

---

## Quick Start

```bash
# 1. Verify Hermes is running
hermes gateway status

# 2. Install the skill
npx skills add iii-hq/workers@hermes

# 3. Load in your agent
skill_view(name="hermes")

# 4. Register with iii runtime (varies by setup)
# The worker auto-discovers the iii bus via environment variables
```

---

## Use Cases

| Use Case | Flow |
|---|---|
| **Customer support triage** | Telegram message → `hermes::inbound` → classify worker → Hermes responds |
| **Multi-platform command bot** | Slack slash command → `hermes::run` → Hermes executes → result back to Slack |
| **Event-driven automation** | Webhook fires → `hermes::inbound` → trigger worker → Hermes takes action |
| **Cross-agent coordination** | Worker A completes task → `hermes::send` notifies user on preferred platform |

---

## Limitations

- **Requires iii runtime:** The iii bus must be running for the worker to function.
- **Headless turns:** `hermes::run` executes one turn at a time — not a persistent conversation.
- **Pre-provisioned credentials:** Hermes must already be configured before the worker can use it.
- **Experimental:** 5 installs, first seen June 2026. Ecosystem is young.

---

## Verification

After setup:

```bash
# Check iii worker registration
curl -s http://localhost:IIIPORT/workers | jq '.[] | select(.name=="hermes")'

# Test hermes::run with a simple query
iii invoke hermes::run '{"message": "What is the current time?"}'

# Test hermes::send
iii invoke hermes::send '{"platform": "telegram", "message": "Test from iii bus"}'
```

---

## Security

- [Gen Agent Trust Hub: Pass](https://www.skills.sh/iii-hq/workers/hermes/security/agent-trust-hub)
- [Socket: Pass](https://www.skills.sh/iii-hq/workers/hermes/security/socket)
- [Snyk: Warn](https://www.skills.sh/iii-hq/workers/hermes/security/snyk)

---

**Related:** [hermes-agent-framework-setup.md](hermes-agent-framework-setup.md), [blueprint-orchestration-setup](blueprint-orchestration-setup)
