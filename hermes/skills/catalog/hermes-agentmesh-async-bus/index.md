---
title: Hermes AgentMesh Async Bus  --  Setup Guide
description: Deploy a peer-to-peer, 0-SSH, Redis-backed async message bus for multi-agent coordination. Designed for Hermes, OpenClaw, LangGraph, AutoGen, CrewAI.
category: Agent Infrastructure
source: seleman66eeddwegger3-art/hermes-agentmesh
installs: 1/day trending
---

# Hermes AgentMesh Async Bus

**Install:** `npx skills add seleman66eeddwegger3-art/hermes-agentmesh --skill hermes-agentmesh-async-bus`

A peer-to-peer, 0-SSH, Redis-backed async message bus designed by Bobo (a Hermes agent architect). Replaces synchronous HTTP coordination with Redis mailboxes  --  agents communicate by dropping tasks in named inboxes instead of making blocking HTTP calls.

## Why Use This

| Problem | AgentMesh Solution |
|---------|-------------------|
| HTTP timeouts at 5–10 min crash multi-agent tasks | Redis queues  --  hours-long tasks OK |
| SSH required to start remote workers | 0 SSH  --  workers listen on shared Redis |
| Reports lost or must be scp'd | Reports land naturally on initiator's machine |
| Group chat noise eats context tokens | Named inboxes  --  zero noise |

## Architecture

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

- **Central hub:** Redis + Hermes LLM API + HTTP file server on Mac mini
- **Worker nodes:** Pure Redis clients (any OS), kept alive by LaunchAgents/systemd
- **Protocol:** `redis.lpush("inbox:<NODE_NAME>", task_json)`  --  the mailbox IS the protocol

## Quick Start (5 minutes)

### Prerequisites
- 1 Mac mini (Redis + Hermes LLM API on :8642 + HTTP file server on :8080)
- 1+ other devices on same LAN
- Redis installed on all nodes

### Step 1: Mac mini  --  Configure Redis for LAN access
```bash
sudo sed -i.bak \
  -e 's/^bind 127.0.0.1 ::1$/bind 0.0.0.0/' \
  -e 's/^protected-mode yes$/protected-mode no/' \
  /opt/homebrew/etc/redis.conf
brew services restart redis
nc -z -w 2 127.0.0.1 6379 && echo "✓ Redis cross-LAN OK"
```

### Step 2: Install the skill
```bash
npx skills add seleman66eeddwegger3-art/hermes-agentmesh --skill hermes-agentmesh-async-bus
```

### Step 3: Deploy workers (0 SSH)
```bash
# On each worker node:
mkdir -p ~/.hermes/async_bus
curl -s http://<MAC_MINI_IP>:8080/worker_node.py -o ~/.hermes/async_bus/worker_node.py
curl -s http://<MAC_MINI_IP>:8080/orchestrator_async.py -o ~/.hermes/async_bus/orchestrator_async.py
curl -s http://<MAC_MINI_IP>:8080/.env.example -o ~/.hermes/async_bus/.env_common
# Edit .env_common with actual IPs and API keys
```

### Step 4: Send your first task
```python
import redis, json
r = redis.Redis(host='<MAC_MINI_IP>', port=6379)
task = {"type": "analysis", "payload": "audit codebase", "from": "orchestrator"}
r.lpush("inbox:worker-1", json.dumps(task))
# Worker picks it up, processes, writes report back to your machine
```

## Verification
```bash
# Check worker is listening
redis-cli -h <MAC_MINI_IP> PING  # Should return PONG

# Monitor inbox activity
redis-cli -h <MAC_MINI_IP> MONITOR | grep "inbox:"

# Check worker health
curl -s http://<MAC_MINI_IP>:8080/health
```

## Key Design Decisions

1. **Redis, not HTTP**  --  Eliminates timeout anxiety. A 2-hour agent task is just a message sitting in a Redis list.
2. **0 SSH deployment**  --  Workers pull code from the hub's HTTP file server. No remote process management.
3. **Reports land locally**  --  The initiator writes the report to its own filesystem, not the worker's. No scp needed.
4. **Framework-agnostic**  --  Works with Hermes, OpenClaw, LangGraph, AutoGen, CrewAI. The mailbox format is universal JSON.

## Pitfalls

- **Redis LAN binding** requires `bind 0.0.0.0` and `protected-mode no`. Secure your network accordingly.
- **API keys** in `.env_common` are shared across nodes. Use a dedicated LAN-scoped key, not your primary API key.
- **Worker node naming** must match inbox names exactly. Use consistent, lowercase names.

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Agent Infrastructure](/hermes/skills/catalog/#agent-infrastructure) →*
*Source: [seleman66eeddwegger3-art/hermes-agentmesh](https://github.com/seleman66eeddwegger3-art/hermes-agentmesh)*
*Powered by CorpusIQ*
