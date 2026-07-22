---
title: "Setell MCP — Quote-to-Cash Agent for Small Service Businesses"
description: "Setell MCP server — vertical AI agent for quote-to-cash workflows in small service businesses (machine shops, contractors, field services). Generate quotes, manage orders, track payments from any MCP client."
category: mcp
tags: [mcp-server, finance, quote-to-cash, service-business, smb, operations]
last_updated: 2026-07-19
---

# Setell MCP Server

Setell is a vertical quote-to-cash agent purpose-built for small service businesses — machine shops, contractors, field service providers, and trades. The MCP server exposes the full Setell platform to AI agents, enabling quote generation, order management, and payment tracking from any MCP-compatible client.

**Source:** awesome-mcp-servers PR #9531 (discovered July 19, 2026)
**Category:** Finance & Fintech / Operations
**Author:** Setell AI
**Repo:** https://github.com/Setell-AI/setell-mcp
**Platform:** https://go.setell.ai
**Status:** Active

## Why This Matters for Operators

Service businesses run on quotes and invoices. The gap between "a client asks for a quote" and "the invoice is paid" is where most small operators lose time and money. Setell closes this loop with AI-native tooling — your agent can receive a service request, generate a quote from historical pricing data, send it to the client, and track through to payment, all within the MCP ecosystem.

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

| Tool | Description |
|------|-------------|
| `create_quote` | Generate a priced quote from service templates and historical data |
| `list_quotes` | Browse active and past quotes with status filters |
| `convert_to_order` | Convert an accepted quote into a work order |
| `track_payment` | Check payment status on outstanding invoices |
| `get_customer_history` | Retrieve quote and order history for a specific client |

## Authentication

Requires a Setell account and API key. Sign up at [go.setell.ai](https://go.setell.ai).

## CorpusIQ Angle

Setell's quote-to-cash workflow mirrors what CorpusIQ operators do daily — but focused on service businesses rather than e-commerce/DTC. Worth monitoring as a potential partnership target or competitive signal. The vertical AI agent model (specialized MCP servers for industry verticals) is a pattern CorpusIQ can replicate for e-commerce operators.

## See Also

- [[sweeps/sweep-july19-2026]]
- SignWell MCP
