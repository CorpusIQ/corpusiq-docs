---
title: "Setell MCP - Quote-to-Cash Agent for Small Service"
description: "Setell MCP server - vertical AI agent for quote-to-cash workflows in small service businesses (machine shops, contractors, field services). Generate quotes"
category: mcp
tags: [mcp-server, finance, quote-to-cash, service-business, smb, operations]
last_updated: 2026-10-30
canonical: "https://www.corpusiq.io/docs/hermes/mcp/servers/external/setell-mcp/"
robots: "index,follow"

---

# Setell MCP Server

Setell is a vertical quote-to-cash agent purpose-built for small service businesses - machine shops, contractors, field service providers, and trades. The MCP server exposes the full Setell platform to AI agents, enabling quote generation, order management, and payment tracking from any MCP-compatible client.

**Source:** awesome-mcp-servers PR #9531 (discovered July 19, 2026)
**Category:** Finance & Fintech / Operations
**Author:** Setell AI
**Repo:** https://github.com/Setell-AI/setell-mcp
**Platform:** https://go.setell.ai
**Status:** Active

## Why This Matters for Operators

Service businesses run on quotes and invoices. The gap between "a client asks for a quote" and "the invoice is paid" is where most small operators lose time and money. Setell closes this loop with AI-native tooling - your agent can receive a service request, generate a quote from historical pricing data, send it to the client, and track through to payment, all within the MCP ecosystem.

## Installation

```bash
# Via npm
npm install -g setell-mcp

# Or run directly
npx setell-mcp
```

## Claude Desktop / Hermes Configuration

```json
{
  "mcpServers": {
    "setell": {
      "command": "npx",
      "args": ["setell-mcp"],
      "env": {
        "SETELL_API_KEY": "your-api-key"
      }
    }
  }
}
```

## Key Tools

25 tools, all prefixed `setell_`.

| Tool | Description |
|------|-------------|
| `setell_get_health` | Setell connection health |
| `setell_find_jobs` | Find Setell jobs |
| `setell_get_quote` | Get a Setell quote |
| `setell_find_customer` | Find Setell customers |
| `setell_get_morning_brief` | Setell morning brief |
| `setell_get_pricing_signal` | Setell pricing signal |
| `setell_propose_parts_list` | Setell parts-list proposal |
| `setell_get_autonomy` | Setell autonomy modes |
| `setell_set_autonomy` | Set autonomy mode |
| `setell_get_shop_profile` | Setell shop profile |
| `setell_update_shop_profile` | Update shop profile |
| `setell_get_customer_baseline` | Customer pricing baseline |
| `setell_get_customer_memory` | Customer memory list |
| `setell_save_customer_memory` | Save customer memory |
| `setell_get_learning_coverage` | Learning-loop coverage |
| `setell_get_pricing_calibration` | Pricing report card |
| `setell_get_quote_tiers` | List quote tiers |
| `setell_generate_quote_tiers` | Generate quote tiers |
| `setell_select_quote_tier` | Select a quote tier |
| `setell_compose_quote` | Compose a quote email |
| `setell_send_quote` | Send a quote |
| `setell_schedule_send` | Schedule a quote send |
| `setell_cancel_scheduled_send` | Cancel a scheduled send |
| `setell_get_job_margin` | Realized job margin |
| `setell_get_margin_summary` | Margin summary |

## Authentication

Requires a Setell account and API key. Sign up at [go.setell.ai](https://go.setell.ai).

## CorpusIQ Angle

Setell's quote-to-cash workflow mirrors what CorpusIQ operators do daily - but focused on service businesses rather than e-commerce/DTC. Worth monitoring as a potential partnership target or competitive signal. The vertical AI agent model (specialized MCP servers for industry verticals) is a pattern CorpusIQ can replicate for e-commerce operators.

## See Also

- [[sweeps/sweep-july19-2026]]
- SignWell MCP
