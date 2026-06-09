---
title: MCP Server Integration
description: Complete MCP server integration guides for Hermes — 53+ servers, FastMCP patterns, CorpusIQ tools
---

# MCP Server Integration

Model Context Protocol (MCP) servers extend Hermes with structured tool access. This guide covers the 53+ MCP servers available through CorpusIQ plus integration patterns for any MCP-compatible server.

## CorpusIQ MCP

CorpusIQ provides 53 operational MCP tools directly to the Hermes agent environment:

| Connector | Tools | Use Case |
|-----------|-------|----------|
| Stripe | 12 | Payments, charges, customers, payouts |
| QuickBooks | 18 | Accounting, invoices, P&L, balance sheet |
| Shopify | 10 | Orders, products, inventory |
| Google Ads | 11 | Campaigns, keywords, performance |
| Meta Ads | 14 | Facebook/Instagram ad management |
| GA4 | 4 | Web analytics, traffic, conversions |
| Klaviyo | 18 | Email/SMS campaigns, flows, segments |
| Mailchimp | 20 | Email marketing, lists, subscribers |
| HubSpot | 5 | CRM, contacts, deals |
| Close CRM | 4 | Sales pipeline, leads |
| Stripe, Semrush, Ahrefs, TikTok, YouTube, Slack, Notion, Monday, Airtable, Calendly... | | |

53 tools total across marketing, finance, CRM, analytics, and operations.

## FastMCP + Pydantic

CorpusIQ MCP servers use FastMCP with Pydantic validation:

```python
from fastmcp import FastMCP
from pydantic import BaseModel, Field

mcp = FastMCP("corpusiq-connector")

class StripeQuery(BaseModel):
    customer_id: str = Field(..., description="Stripe customer ID")

@mcp.tool()
async def get_customer_subscriptions(query: StripeQuery):
    """Get active subscriptions for a Stripe customer."""
    ...
```

Type safety, schema enforcement, and reliable tool invocation.

## Integration Pattern

### Registering a New MCP Server

```yaml
# hermes config
mcp_servers:
  my-server:
    url: https://my-mcp.example.com
    auth: oauth
    tools: ["search", "create", "update"]
```

### Tool Discovery

```bash
# List all available MCP tools
hermes tools --source mcp

# Filter by server
hermes tools --source mcp --server corpusiq
```

## Common Patterns

### Cross-Source Queries

CorpusIQ MCP supports cross-source analysis — correlate Google Ads spend with GA4 traffic, Klaviyo revenue with Shopify orders, or Stripe charges with QuickBooks invoices:

```
"Compare our Google Ads spend to GA4 conversions this month"
"Show Klaviyo email revenue vs Shopify revenue by day"
"Reconcile Stripe payouts with QuickBooks deposits"
```

### Agent-Initiated Workflows

MCP tools are callable directly by agents through terminal execution. No human intervention required for routine operations.

---

*Next: [Architecture Overview](/architecture/) · [Skills Marketplace](/skills/)*
