---
title: VenuNite Events MCP - US Live Events Data for Agents
description: Hosted, read-only MCP connector for 400,000+ source-verifiable US live events from independent venues and community calendars in all 50 states - keyless fair-use trial, Builder key for authenticated setup.
category: Location Data
stars: n/a (new listing)
added: 2026-09-09
source: mcp.so
relevance: ★★
tags: [events, local-marketing, venue-data, entertainment, location-data, remote-mcp]
---

# VenuNite Events MCP

**US live events as an agent-ready data source** - 400,000+ source-verifiable events from independent venues and community calendars across all 50 states, exposed through a single read-only search tool over Streamable HTTP. No key required for an instant trial under shared fair-use limits; the connector cannot modify events or calendars and returns the original event source when one is available.

```
Server type: Remote (Streamable HTTP, read-only)
Auth: Keyless trial under fair-use limits; "Builder key" for client-specific authenticated setup
Endpoint: https://mcp.venunite.com/v1/mcp/ (general)
ChatGPT variant: https://mcp.venunite.com/v1/chatgpt/mcp/ (drops explicit location args)
Trial budget: 5 calls/min and 100 tool calls/day per account (keyed to source IP), 20 events per search, 30 days ahead
Built by: VenuNite (venunite.com)
```

## Why This Matters for Operators

Local marketing, venue intelligence and event-driven campaigns normally start from scraping or manual research. **VenuNite gives an agent a clean, read-only events surface**: search by place name, coordinates, state or timezone, get up to 20 events per search with dates and sources, and let the agent reason about local demand - without any write access to the underlying calendars. Every response carries applied_filters so the agent can state exactly what was searched, and quota states (row_budget_exhausted, location_unavailable) are explicit rather than silent.

## Tools & Capabilities

| Capability | Purpose |
|---|---|
| Event search (single read-only tool; name not published in docs) | Search events near a place or point, ahead of a date range |
| `place_name` / `center_lat` / `center_lng` / `state_hint` / `timezone` | Location arguments (general endpoint) |
| `date_start` / `horizon_end` / `limit` | Date window and result cap (up to 20 events per search, 30 days ahead) |
| `applied_filters` | Every response reports the filters actually applied |
| `row_budget_exhausted` / `location_unavailable` | Explicit quota and location states instead of silent empty results |

The ChatGPT variant drops the five location arguments and takes the search center from the coarse location ChatGPT supplies, returning rounded distances and `location_unavailable` when no US location is sent.

## Installation

```bash
claude mcp add --transport http venunite https://mcp.venunite.com/v1/mcp/
```

## Configuration

```json
{
  "mcpServers": {
    "venunite": {
      "type": "http",
      "url": "https://mcp.venunite.com/v1/mcp/"
    }
  }
}
```

Use the keyless trial for instant evaluation; choose "Use a Builder key" for client-specific authenticated setup (Codex, Cursor, VS Code examples are on the developer page). Call and search details plus quota telemetry are logged as described in the privacy policy.
