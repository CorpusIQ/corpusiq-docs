---
title: Yandex Metrika MCP - Web Analytics for Agents
description: Full Yandex Metrika API coverage as MCP tools - 108 Management, Logs and Stat methods generated from the official docs, with a transparency contract and no silent query rewriting.
category: Data & Analytics
stars: n/a (new listing)
added: 2026-09-09
source: mcpservers.org
relevance: ★★
tags: [web-analytics, yandex-metrika, traffic-analysis, marketing-analytics, ecommerce-analytics, reporting, self-hosted]
---

# Yandex Metrika MCP

**Community MCP server (stdio, MIT, npm)** - the full Yandex Metrika API as MCP tools: all 108 Management, Logs and Stat methods generated from the official docs, ten sensible tools exposed by default with a transparency contract that shows exactly what the server added to every call.

```
Server type: Self-hosted (stdio via npx)
Auth: Yandex Metrika OAuth token (in environment)
Endpoint: npx -y yandex-metrika-mcp-server
Tools: 108 methods available (95 Management, 7 Logs, 6 Stat); 10 exposed by default
Pricing: Free (MIT), fork of atomkraft/yandex-metrika-mcp
Category: Data & Analytics
Built by: artgas1 (community), npm yandex-metrika-mcp-server
```

## Why This Matters for Operators

Analytics MCP servers tend to fail in two quiet ways: they answer a different question than the one asked, and they silently apply filters that change the numbers. **Yandex Metrika MCP was rebuilt around a no-silent-substitution contract** - every response carries a `_meta` block listing what the server applied, what it decided on your behalf, how many rows were returned versus truncated, and how many retries happened. If the server changed the query, you can see it.

For teams whose traffic reports include ad spend decisions, that transparency is the difference between trusting a number and double-checking it.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `metrika_counter_list` | List counters (sites) in the account |
| `metrika_goal_create` | Create a conversion goal |
| `metrika_segment_update` | Update an audience segment |
| `metrika_logs_create` / `metrika_logs_get` / `metrika_logs_download` | Raw Logs API jobs |
| `metrika_stat_data` / `metrika_stat_bytime` / `metrika_stat_pivot` | Stat API reports - data, by-time series, pivot tables |

Tool names map one-to-one to API resources, so `metrika_goal_list` is unambiguously GET /management/v1/counter/{id}/goals. The other ~98 methods enable with a single variable.

## Installation

```bash
npx -y yandex-metrika-mcp-server
```

## Configuration

```json
{
  "mcpServers": {
    "yandex-metrika": {
      "command": "npx",
      "args": ["-y", "yandex-metrika-mcp-server"]
    }
  }
}
```

The Yandex Metrika OAuth token goes in the environment; it travels only as a header and never appears in responses (the server redacts it from echoed request URLs).

## Business Relevance

- **Marketing teams running Yandex Metrika** get counter, goal and segment management plus Stat and Logs reports in one assistant.
- **E-commerce operators in RU/CIS and EU markets** ask "how did yesterday's traffic convert" and get the pivot table without tab-hopping.
- **Analysts who distrust silent filters** get a `_meta` contract that discloses robot filtering, truncation and server-side decisions.
- **Teams scaling beyond the defaults** enable the remaining 98 methods with one variable instead of building their own wrapper.

## Integration with CorpusIQ

Yandex Metrika MCP covers the analytics corner CorpusIQ's GA4 connector does not - Yandex-native counters for RU/CIS traffic. A composed workflow: CorpusIQ pulls GA4 for one region, Yandex Metrika MCP pulls the other, and the assistant merges both into one traffic-and-conversion view for operators running split-region analytics. Two analytics sources, one reporting loop.

## Limitations

- Community project forking an earlier community project - no official Yandex backing.
- 108-method surface means careful prompting; the default 10-tool profile exists precisely to avoid context flooding.
- Requires a Yandex Metrika account with OAuth access - value is zero without one.
- Russian-language primary documentation; English README is provided.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
