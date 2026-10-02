---
title: "Glasser MCP - Pay-Per-Use Data APIs for AI Agents"
description: "Glasser gives AI agents one hosted MCP endpoint in front of paid data APIs: company and person enrichment, email verification, SEO research and web search, run from a shared Workspace balance with OAuth or key auth. Seven static tools cover search, price inspection, runs and balance."
category: Data & Analytics
stars: n/a (new listing)
added: 2026-09-15
source: "mcp.so feed (Sep 15 midday) + vendor docs at glasser.ai/docs/mcp-server"
relevance: ★★★
tags: [data-apis, enrichment, email-verification, seo, web-search, lead-generation, pay-as-you-go, remote-mcp]
---

# Glasser MCP

**A pay-per-use data marketplace your agent can price before it spends.** Glasser wraps paid data APIs behind one hosted MCP server: the agent searches the catalog of runnable endpoints, inspects an endpoint's input schema and exact price with its charge clauses, then runs the request from a shared Workspace balance. Company and person enrichment, email verification, SEO research and web search are the documented starting points.

```
Server type: Remote (stateless Streamable HTTP)
Auth: OAuth (sign in from the client and it gets a Key of its own) or API key in the Authorization header
Endpoint: https://api.glasser.ai/mcp
Tools: 7 (search, inspect, run, runs_get, runs_list, runs_stop, balance)
Pricing: pay per request from a Workspace balance; prices and charge clauses published per endpoint
Category: Data & Analytics
Built by: Glasser (glasser.ai)
```

## Why This Matters for Operators

Data tasks usually mean a new vendor contract, a new key and a new invoice. Glasser collapses that into the agent session: one connection, one balance, and a catalog the agent can shop at runtime. **The inspect tool is the trust mechanism**: it returns the input schema and the exact price with every charge clause before run executes, so spend is deliberate rather than surprising.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `search` | Find runnable paid endpoints; results are filtered to what the Key may run |
| `inspect` | One endpoint's input schema, exact price and charge clauses |
| `run` | Execute a selected request against the endpoint |
| `runs_get` | Fetch one past run |
| `runs_list` | List runs for the Workspace |
| `runs_stop` | Stop a run |
| `balance` | Check the Workspace balance |

The data sources themselves stay behind `search`: endpoints are data the agent discovers at runtime, never one tool each.

## Installation

```bash
claude mcp add glasser --transport http https://api.glasser.ai/mcp
```

## Configuration

```json
{
  "mcpServers": {
    "glasser": {
      "type": "http",
      "url": "https://api.glasser.ai/mcp"
    }
  }
}
```

Two ways in: sign in from the client and it gets a Key of its own, or supply a Key you already have. Requests are stateless (no session): each one is authenticated with the Key in the Authorization header or with the access token issued at sign-in. The authorization server is discovered from the 401 challenge (`resource_metadata` in `WWW-Authenticate`), so OAuth clients need nothing beyond the URL.

## Business Relevance

- **Sales and GTM teams** enrich company and person records and verify emails before outbound, without a second vendor login and contract.
- **SEO and content operators** pull search and SEO data into the same session where the content is drafted.
- **Founders** run one-off data tasks (enrichment, verification, lookups) without committing to subscriptions.
- **RevOps** keeps spend visible per request through inspect-before-run and a single Workspace balance.

## Integration with CorpusIQ

CorpusIQ's connectors are the systems of record (HubSpot, Stripe, Shopify, QuickBooks, GA4 and more); Glasser is the on-demand enrichment layer for the session. A worked pattern: pull a customer or lead list through CorpusIQ, enrich and verify it through Glasser inside the same conversation, then write back or act. Because Glasser prices each endpoint up front, you can see exactly what a batch will cost before running it, which keeps ad-hoc data work inside a known budget.

## Limitations

- Paid per request: every run draws from the Workspace balance; no flat allowance is described.
- The catalog is third-party data sources; coverage, freshness and price vary per endpoint.
- Requests are stateless, so multi-step workflows must pass context explicitly.
- The Key is the spend credential; treat it like a billing secret.
- Brand new to this catalog; no track record in the sweep data yet.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
