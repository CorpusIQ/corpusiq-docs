---
title: "Orbiads GAM MCP — Google Ad Manager for AI Agents"
description: "Hosted MCP server for Google Ad Manager — 200+ tools across campaign management, line items, creatives (image/video/HTML5/native), interactive reporting, inventory exploration, and ad-ops compliance audits. OAuth on-behalf-of-user."
source: github.com/OrbiAds/Orbiads-GAM-MCP
stars: 3
language: Python
transport: Streamable HTTP (hosted)
auth: OAuth 2.0 (Google Ad Manager)
category: Marketing/AdTech
last_updated: 2026-07-20
---

# Orbiads GAM MCP — Google Ad Manager for AI Agents

**Hosted MCP server with 200+ tools for Google Ad Manager.** Manage campaigns, line items, creatives, inventory, and reporting from any MCP-compatible AI agent. OAuth on-behalf-of-user — your agent acts as you with the permissions you grant.

## What It Does for Operators

- **Campaign Management** — Create, update, pause, and archive GAM campaigns from natural language
- **Line Items** — Full line item lifecycle: create, target, traffic, and optimize
- **Creatives** — Upload and manage image, video, HTML5, and native ad creatives
- **Interactive Reporting** — Ask questions about performance in natural language, get formatted reports
- **Inventory Exploration** — Search ad units, placements, and inventory availability
- **Ad-Ops Compliance** — Audit campaigns against best practices (frequency caps, competitive exclusions, viewability thresholds)
- **Forecast** — Delivery forecasts, inventory availability predictions

## Installation

This is a **hosted** MCP server — no local installation required. Connect via Streamable HTTP:

```json
{
  "mcpServers": {
    "orbiads-gam": {
      "url": "https://api.orbiads.com/mcp/gam",
      "transport": "streamable-http"
    }
  }
}
```

First-time connection opens a browser for Google OAuth — authorize once, and the agent reuses credentials for future sessions.

## Claude Desktop / Hermes Config

```json
{
  "mcpServers": {
    "orbiads-gam": {
      "url": "https://api.orbiads.com/mcp/gam",
      "transport": "streamable-http"
    }
  }
}
```

## Free Trial

Orbiads offers a free trial: **5 credits, no credit card required.** Sign up at [orbiads.com](https://orbiads.com).

## Key Tools

| Tool | Description |
|------|-------------|
| `list_orders` | List all GAM orders with status |
| `create_line_item` | Create a new line item with targeting |
| `get_inventory` | Search ad units by name, size, or placement |
| `upload_creative` | Upload image/video/HTML5 creative assets |
| `run_report` | Generate and download GAM reports |
| `compliance_audit` | Audit a campaign against ad-ops best practices |
| `forecast_delivery` | Predict delivery for a line item or order |

## Operator Use Cases

1. **Ad Operations Teams** — Manage GAM campaigns from Claude/Cursor instead of the GAM dashboard. "Pause all underdelivering line items from yesterday" becomes one prompt.

2. **Media Buyers** — Pull inventory availability data directly into AI research workflows. Compare CPMs across placements without manual exports.

3. **Compliance Auditors** — Run automated audits against GAM setups. Flag missing frequency caps, broken competitive exclusions, and below-threshold viewability.

4. **Reporting Automation** — "Send me a report of top-performing line items by revenue, last 7 days" — get formatted reports without building GAM queries.

## Pricing

- **Free tier:** 5 credits (1 credit ≈ 1 tool call)
- **Paid:** Contact Orbiads for pricing

## CorpusIQ Angle

First Google Ad Manager MCP server — fills a gap in the marketing/adtech MCP ecosystem. Operators running ad operations alongside their business can now manage GAM from AI agents. Complementary to CorpusIQ's analytics connectors — GAM performance data alongside GA4, Stripe, and QuickBooks in one AI conversation.

## Limitations

- Hosted only — no self-hosted option (vendor dependency)
- OAuth requires a Google Ad Manager account with appropriate permissions
- New project (3⭐). API stability and uptime not guaranteed.
- GAM API v202602 — requires up-to-date GAM network
