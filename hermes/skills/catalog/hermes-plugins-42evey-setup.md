---
title: Hermes Plugins (42-evey) Setup Guide
description: Install and configure 42-evey/hermes-plugins — goals tracking, inter-agent bridge, model selection, and cost control for Hermes Agent.
category: hermes-native
publisher: 42-evey
maturity: beta
source: https://github.com/42-evey/hermes-plugins
---

# Hermes Plugins (42-evey) — Setup Guide

Native Hermes Agent plugins by [42-evey](https://github.com/42-evey/hermes-plugins). Provides goals tracking, inter-agent communication bridges, model selection routing, and cost control — four missing primitives for production Hermes deployments.

## What It Provides

- **Goals tracking** — define, track, and report on agent goals with completion gates
- **Inter-agent bridge** — structured communication between Hermes agents without shared memory
- **Model selection** — automatic model routing based on task complexity and cost budget
- **Cost control** — token usage caps, per-task budgets, and spending alerts

## Installation

```bash
# Install via skills.sh
npx skills add https://github.com/42-evey/hermes-plugins

# Manual clone
git clone https://github.com/42-evey/hermes-plugins.git ~/.hermes/skills/hermes-plugins-42evey
```

## Configuration

### Goals Plugin

```yaml
goals:
  enabled: true
  storage: "~/.hermes/goals.json"
  max_active: 5
  auto_archive: true
```

### Inter-Agent Bridge

```yaml
bridge:
  enabled: true
  protocol: "stdio"       # or "http" for remote agents
  peer_agents:
    - name: "dev-hermes"
      endpoint: "http://192.168.1.50:9090"
    - name: "ops-hermes"
      endpoint: "http://192.168.1.51:9090"
  auth_token: "${BRIDGE_AUTH_TOKEN}"
```

### Model Selection

```yaml
model_selector:
  enabled: true
  default_model: "sonnet"
  routing_rules:
    - pattern: "refactor|debug|test|build"
      model: "sonnet"
    - pattern: "research|strategy|architecture|board"
      model: "opus"
    - pattern: "social|post|tweet|reddit"
      model: "sonnet"
    # Never route to haiku
  cost_budget_daily: 50.00   # USD
```

### Cost Control

```yaml
cost_control:
  enabled: true
  daily_budget: 50.00         # USD
  per_task_budget: 5.00
  alert_threshold: 0.80       # alert at 80% of budget
  block_on_exceeded: true     # hard stop when budget exceeded
```

## Key Workflows

### Set and track a goal

```
/hermes-plugins goal-create "Deploy CorpusIQ MCP server to production"
/hermes-plugins goal-status
```

### Send a task to another agent

```
/hermes-plugins bridge-send dev-hermes "Run the test suite on the latest PR"
```

### Check cost status

```
/hermes-plugins cost-status
```

## Verification

```bash
# Test plugins load
hermes skills list | grep hermes-plugins

# Test goals plugin
hermes chat -q "/hermes-plugins goal-list"

# Test bridge
hermes chat -q "/hermes-plugins bridge-status"
```

## Pitfalls

- **Bridge auth tokens**: Store in environment variables, never in config files. The `BRIDGE_AUTH_TOKEN` is read from the environment at plugin load time.
- **Cost tracking accuracy**: Model costs are estimated based on published pricing. Actual costs may differ with provider-specific discounts or surcharges.
- **Goal storage**: JSON file storage can corrupt on concurrent writes from multiple agent sessions. For production, consider migrating to SQLite.
- **Inter-agent loops**: Ensure bridge communication doesn't create infinite loops (A sends to B, B sends to A). The bridge has a `max_depth: 3` default.

## See Also

- [42-evey/hermes-plugins repo](https://github.com/42-evey/hermes-plugins)
- [CorpusIQ Agent Optimization Skill](/hermes/skills/catalog/corpusiq-agent-optimization/)
- [Hermes Agent Skill Authoring](/hermes/skills/catalog/hermes-agent-skill-authoring-setup/)

---

*Setup guide by CorpusIQ. Source: [42-evey/hermes-plugins](https://github.com/42-evey/hermes-plugins).*
