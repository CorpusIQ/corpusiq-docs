---
title: Reelier MCP Server
subtitle: Agent workflow recording and deterministic replay at zero tokens
source: mcp.so
github: https://github.com/maximehoule/reelier
created: 2026-07-22
category: AI Operations
stars: 0
tags: [agent-workflow, replay, deterministic, testing, audit, developer-tools]
---

# Reelier MCP Server

MCP server for **recording agent tool-call workflows and replaying them deterministically at zero tokens**. Agents make claims — Reelier writes receipts. Record an agent's workflow once, replay it exactly, and diff runs to catch drift.

## What It Does

- **Workflow Recording** — Capture every tool call, parameter, and response in an agent session
- **Deterministic Replay** — Replay recorded workflows exactly — no LLM, no tokens, no variation
- **Drift Detection** — Diff current runs against recorded baselines to detect changes
- **Zero Token Cost** — Replay costs nothing because it's purely deterministic

## Business Operator Use Cases

| Use Case | Value |
|----------|-------|
| **QA Automation** | Record a successful agent workflow once, replay for every deployment |
| **Agent Auditing** | "What exactly did the agent do during that incident?" → full replay |
| **Cost Optimization** | Replay deterministic workflows instead of burning tokens on repeated tasks |
| **Compliance** | Immutable record of every agent action for SOC2/ISO audits |

## Installation

```bash
git clone https://github.com/maximehoule/reelier
cd reelier
npm install
```

## Configuration

Add to your MCP client config:

```json
{
  "mcpServers": {
    "reelier": {
      "command": "node",
      "args": ["path/to/reelier/index.js"],
      "env": {
        "REELIER_STORAGE_PATH": "/path/to/workflow-recordings"
      }
    }
  }
}
```

## Tools Provided

- `start_recording` — Begin capturing agent workflow
- `stop_recording` — End capture and save workflow
- `replay_workflow` — Deterministically replay a saved workflow
- `diff_workflows` — Compare two workflow runs, identify drift
- `list_recordings` — Browse saved workflow recordings

## Limitations

- **0 stars, brand new** — Created July 22, 2026. Experimental.
- **Deterministic only** — Replay is exact. Can't adapt to changed environments or APIs.
- **Storage growth** — Long workflows with large responses consume disk space.
- **No scheduling** — Manual trigger only. No cron/CI integration yet.

## Operator Verdict

★★★ **Critical infrastructure for agent operations at scale.** This is one of the first MCP servers addressing the "how do we know what our agents are doing" problem. Deterministic replay for compliance and cost savings is genuinely innovative. Watch for CI/CD integration and scheduling features. This could become standard equipment for any team running >3 agents in production.
