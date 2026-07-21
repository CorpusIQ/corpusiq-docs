---
title: Hermes Labyrinth — Observability Dashboard Plugin for Hermes Agent
description: Read-only observability plugin that maps agent journeys, crossings, guideposts, and cron runs. Exportable reports. 187+ installs.
---

# Hermes Labyrinth — Setup Guide

**Source:** [aradotso/trending-skills](https://skills.sh/aradotso/trending-skills/hermes-labyrinth-observability) (187+ installs)
**Category:** Agent Infrastructure / Observability
**Quality Tier:** 🔵 Community

A read-only observability dashboard plugin for Hermes Agent. Turns autonomous agent runs into a navigable map of crossings (prompts, tool calls, tool results, failures, model switches, subagents, approvals, memory hits, redactions, context compression, cron runs) with exportable evidence.

---

## Installation

### Plugin Directory Install

```bash
mkdir -p ~/.hermes/plugins
git clone https://github.com/stainlu/hermes-labyrinth.git ~/.hermes/plugins/hermes-labyrinth
```

Start or restart the Hermes dashboard:

```bash
hermes dashboard
```

If the dashboard is already running, rescan plugins:

```bash
curl http://127.0.0.1:9119/api/dashboard/plugins/rescan
```

Open the dashboard in your browser and select the **Labyrinth** tab.

### Optional Theme

```bash
mkdir -p ~/.hermes/dashboard-themes
cp ~/.hermes/plugins/hermes-labyrinth/theme/hermes-labyrinth.yaml ~/.hermes/dashboard-themes/
```

---

## What Labyrinth Tracks

| View | Contents |
|---|---|
| **Journey index** | Recent CLI, dashboard, gateway, cron, and delegated work |
| **Labyrinth map** | Ordered crossings through a selected agent journey |
| **Inspector** | Input, output, duration, status, evidence, guideposts per crossing |
| **Guideposts** | Generated observations backed by local evidence |
| **Skill atlas** | Bundled, optional, external, and user skill inventory |
| **Cron gate** | Scheduled autonomy, next runs, last failures, workdirs |
| **Model ferry** | Model/provider transitions across sessions |
| **Reports** | Redacted Markdown and JSON exports for one journey |

---

## API Reference

All endpoints are read-only. The plugin API is served at:

```
http://127.0.0.1:9119/api/plugins/hermes-labyrinth/
```

### Endpoints

```
GET /health
GET /journeys
GET /journeys/{journey_id}
GET /journeys/{journey_id}/crossings
GET /skills
GET /cron
GET /guideposts
GET /reports/{journey_id}.json
GET /reports/{journey_id}.md
```

### Example: Fetch All Journeys

```bash
curl http://127.0.0.1:9119/api/plugins/hermes-labyrinth/journeys | jq .
```

### Example: Export a Journey Report

```bash
JOURNEY_ID="your-journey-id"
curl "http://127.0.0.1:9119/api/plugins/hermes-labyrinth/reports/${JOURNEY_ID}.md" > report.md
```

### Health Check

```bash
curl http://127.0.0.1:9119/api/plugins/hermes-labyrinth/health
```

---

## Python API Client

```python
import urllib.request
import json

BASE = "http://127.0.0.1:9119/api/plugins/hermes-labyrinth"

def get_journeys():
    with urllib.request.urlopen(f"{BASE}/journeys") as r:
        return json.loads(r.read())

def get_crossings(journey_id: str):
    with urllib.request.urlopen(f"{BASE}/journeys/{journey_id}/crossings") as r:
        return json.loads(r.read())

def get_report_json(journey_id: str):
    with urllib.request.urlopen(f"{BASE}/reports/{journey_id}.json") as r:
        return json.loads(r.read())
```

---

## Verification

```bash
# After installing plugin and starting dashboard
curl http://127.0.0.1:9119/api/plugins/hermes-labyrinth/health

# Should return: {"status": "ok"}

# Check journeys endpoint
curl http://127.0.0.1:9119/api/plugins/hermes-labyrinth/journeys | jq '. | length'
```

---

## Notes

- **Read-only by design** — no write operations, safe to run in production
- **Black-box recorder** — not a chat UI, designed for post-hoc analysis
- **Exportable evidence** — JSON and Markdown reports for sharing findings
- From the [ara.so](https://ara.so) Daily 2026 Skills collection
- Complements `openclaw-control-center` for agent monitoring
