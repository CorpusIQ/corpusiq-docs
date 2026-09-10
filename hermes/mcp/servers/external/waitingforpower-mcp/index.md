---
title: WaitingForPower MCP - US Energy Permitting Tracker for Agents
description: Keyless remote MCP server over the WaitingForPower dataset of U.S. energy projects stuck in permitting, sourced live from 41 state utility commissions plus EIA, LBNL, ORNL and the Federal Permitting Dashboard.
category: Data & Analytics
stars: 0
added: 2026-09-10
source: "chatmcp/mcpso issue #4011"
relevance: ★★★
tags: [energy, permitting, infrastructure, policy, public-data, remote-mcp, keyless]
---

# WaitingForPower MCP

**Live U.S. energy permitting intelligence as a keyless remote MCP** - generation, transmission, storage, LNG and pipeline projects currently stuck waiting on permitting approval, with every project citing its real public source, its normalized permitting stage, why it is delayed, and how long it has been waiting. Live-verified over JSON-RPC during the Sep 10, 2026 sweep (server v1.0.0, no auth).

```
Server type: Remote (hosted, Streamable HTTP, stateless)
Auth: None - public, no API key
Endpoint: https://waitingforpower.com/mcp
Registry: com.waitingforpower/energy-permitting-tracker (Official MCP Registry)
License: MIT
Tools: 6, all read-only
Built by: waitingforpower.com
```

## Why This Matters for Operators

Anyone developing, financing, supplying or siting around U.S. energy infrastructure needs the same question answered: which projects are waiting on what, and where is the queue moving. **WaitingForPower turns that into a queryable dataset** - 41 state utility/siting commissions plus EIA, LBNL, ORNL and the Federal Permitting Dashboard, normalized into project records with cited sources. For operators the value is scouting and diligence: a site selector can filter by state and bottleneck category, a supplier can track pipeline stages for target customers, and a policy analyst can pull the aggregate stats on capacity waiting by cause. Every claim in the data carries a public citation, so an agent can cite primary sources instead of paraphrasing.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `search_projects` | Search the project dataset with filters including USPS state codes |
| `get_project` | Full detail for one project: cited sources, milestone timeline, capacity, wait duration |
| `get_stats` | Headline aggregates - project count, capacity waiting, clean-energy capacity waiting |
| `list_causes` | The fixed structural bottleneck categories (interconnection queue backlog, NEPA review, and more) |
| `list_policies` | Six bipartisan permitting-reform policy proposals, one per cause category |
| `list_states` | USPS state codes and full names for use as filter values |

## Installation

```bash
claude mcp add waitingforpower https://waitingforpower.com/mcp
```

No key, no sign-up, no rate-limit headers. The server also publishes a plain-text site index at waitingforpower.com/llms.txt for documentation-aware clients.

## Configuration

```json
{
  "mcpServers": {
    "waitingforpower": {
      "url": "https://waitingforpower.com/mcp"
    }
  }
}
```
