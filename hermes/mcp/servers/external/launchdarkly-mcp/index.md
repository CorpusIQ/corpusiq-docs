---
title: "LaunchDarkly MCP — Feature Flag Management for AI Agents"
description: "Connect AI agents to LaunchDarkly via the official MCP server. Toggle features, manage progressive rollouts, run experiments, and audit flag changes."
category: mcp
tags: [mcp-server]
last_updated: 2026-07-15
---

# LaunchDarkly MCP — Feature Flag Management for AI Agents

## What It Is

LaunchDarkly MCP exposes feature flag management over the Model Context Protocol. AI agents can toggle features on/off, check flag statuses, manage progressive rollouts, run A/B experiments, and audit every flag change — bringing feature management into the agent workflow.

## Tools Available

| Tool | Description |
|------|-------------|
| Flag management | List, get, toggle, and update feature flags |
| Targeting rules | Manage user segments and targeting rules |
| Experiments | Create, monitor, and conclude A/B experiments |
| Audit log | Review flag change history and who toggled what |

## Quick Start

```bash
npx -y @launchdarkly/mcp-server
```

## Business Use Cases

1. Incident response: "Disable the new checkout flow feature flag in production"
2. Release verification: "Is the dark mode flag at 100% rollout for all users?"
3. Experiment analysis: "What's the conversion rate for the new onboarding experiment?"

## Limitations

- LaunchDarkly account and API key required. Flag toggles in production should still follow change management processes.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [CorpusIQ Connector Catalog](/hermes/mcp/connectors/)
