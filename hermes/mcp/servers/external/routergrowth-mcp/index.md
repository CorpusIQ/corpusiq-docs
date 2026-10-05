---
title: RouterGrowth MCP - GTM Data and Actions for Agents
description: "One balance for SEO, B2B contact and company enrichment, social scraping, ads and outbound as native MCP tools with spending rules."
category: Sales & Outreach
stars: n/a (new listing)
added: 2026-10-05
source: mcpservers.org /all (Oct 5, 2026 midday sweep)
relevance: ★★★
tags: [gtm, seo, lead-enrichment, serp, backlinks, outbound, pay-per-call, remote-mcp, oauth]
---

# RouterGrowth MCP

**Remote MCP server (stateless Streamable HTTP, OAuth or API key)** - RouterGrowth puts go-to-market capabilities into any agent as native tools on one balance: SERP, backlink and keyword data, B2B contact and company enrichment, social scraping, ads and outbound. Nothing to install, one key, an exact quote before the first paid run of any call.

```
Server type: Remote (Streamable HTTP, stateless - POST in, JSON out)
Auth: OAuth 2.1 (PKCE, dynamic client registration, scope "mcp") or an rg_live_ API key
Endpoint: https://api.routergrowth.com/mcp
Tools: discover, inspect, run, batch_run, runs, get_run, history, watch, watches, events, feedback, balance (+ tables and table_write when enabled)
Billing: pay-per-call from the workspace balance; $1 of credit once your email is verified
Rate limit: 300 requests per minute per key, 3,000 per minute per IP
```

## Why This Matters for Operators

Growth and sales data normally arrives as four vendor accounts and a pile of wrapper code: an SEO suite for SERP, keywords and backlinks, a contact database for enrichment, a scraper for social, an outbound tool for sequences. RouterGrowth collapses that stack into one MCP surface - a discover, inspect, run loop where the agent finds the capability by job description, reads the exact price and billing conditions, then runs it inside a stated cost cap.

The spending model is the notable part for agents: the server's initialize response instructs the model to inspect before the first run of a call, set `max_cost` on every item and `max_total_cost` on a batch, stop and ask before a batch over about $1 unless the user asked for that volume, and never present simulated (`rg_test_`) data as real. Paid runs are idempotency-keyed, so a retry does not get charged twice.

## Tools & Capabilities

| Group | Tools | What they do |
|---|---|---|
| Loop | `discover`, `inspect`, `run`, `batch_run` | Search the catalog by job description; read schema, providers, exact price and billing conditions for one capability; execute a capability with `max_cost`, routing and `idempotency_key`; run one capability for 1 to 200 inputs concurrently with per-item receipts and a total cost cap |
| Tracking | `runs`, `get_run`, `history` | Run history with attempts, charges and routing reasons; one run by id with long-polling; everything already done to one subject (email, domain, LinkedIn URL, handle, phone, name) with results to reuse |
| Change watch | `watch`, `watches`, `events`, `feedback` | Save a query and refresh it to get back only new and changed records plus disappeared keys; list watches with last changes; new replies, bounces and messages across connected channels; report a bug or missing capability from the call site |
| Workspace | `tables`, `table_write`, `balance` | List, describe and query tables by status, due date and data fields; upsert and update rows with `if_status` claims; read wallet balance, reserved and available |
| Catalog routes | `seo.serp`, `seo.keywords`, `seo.ranked_keywords`, `seo.backlinks`, `contact.find`, `contact.verify`, `company.enrich`, `people.search`, plus social, ads, creative and outbound routes | No DataForSEO, Semrush or Ahrefs account of your own - the agent inspects the price and runs the call |

## Installation

Claude Code (OAuth on first use, or a key header):

```bash
claude mcp add --transport http routergrowth https://api.routergrowth.com/mcp
```

Chat apps (claude.ai, ChatGPT developer mode, Claude Desktop, mobile) add it as a custom connector with the same URL; API-key clients send `Authorization: Bearer rg_live_...`. For Hermes Agent, add the server to the profile's `config.yaml` under `mcp_servers` with the URL and `auth: oauth`. Full setup pages for every client, including no-code builders and agent frameworks, live on the RouterGrowth quickstart.

## Business Relevance

- **One balance, many vendors**: SEO data, enrichment and outbound priced per call instead of four subscriptions.
- **Quote before spend**: `inspect` returns the exact price and billing conditions; `max_cost` and `max_total_cost` cap every run.
- **Batch that behaves**: `batch_run` covers 1 to 200 inputs with per-item receipts and retry-safe idempotency keys.
- **Change-only refresh**: `watch` returns just the new and changed records since the last run, so recurring monitoring stays cheap.
- **Agent-safe defaults**: the spending rules travel in the handshake, and `rg_test_` keys return clearly labeled simulated data.

## Integration with CorpusIQ

CorpusIQ answers questions about the business's own systems, read-only and cited; RouterGrowth supplies the outside data a growth operator needs next to those answers - the SERP positions, the enriched contacts, the outbound state. An operator can ask CorpusIQ what the site's traffic did and RouterGrowth which keywords moved and which prospects replied, in the same assistant, with each paid call quoted before it runs.

## Limitations

- Paid by design: only `discover`, `inspect`, `runs`, `get_run`, `history`, `watches`, `events`, `tables`, `feedback` and `balance` are free; `run`, `batch_run` and `watch` spend from the balance.
- Stateless server: GET and DELETE answer 405; there is no stream and no session to keep.
- `tables` and `table_write` appear only when the workspace enables tables.
- A test key (`rg_test_...`) returns simulated data by design - the tools are labeled, never to be presented as real.
- Hosted by RouterGrowth and governed by its terms; a live POST initialize returns 401 unauthenticated, confirming it is auth-gated.

## FAQ

### What is RouterGrowth?

A pay-per-call API platform that bundles GTM capabilities - SEO (SERP, keywords, backlinks), B2B contact and company enrichment, social scraping, ads and outbound - behind one wallet and exposes them through MCP for agents.

### Does the agent need an account with each data vendor?

No. RouterGrowth routes the call to its own providers; you hold one balance and the agent quotes the exact price with `inspect` before the first paid run.

### How do cost controls work?

Every run takes `max_cost`; batches take `max_total_cost` and per-item receipts; the handshake's spending rules tell the agent to stop and ask before a batch over about $1 unless the volume was explicitly requested.

### Which clients are supported?

claude.ai, Claude Desktop, Claude mobile, ChatGPT (developer mode), Claude Code, Codex, Cursor, VS Code, Gemini CLI, other IDE clients, no-code builders (n8n, Make, Zapier, Copilot Studio, Dify) and major agent frameworks - OAuth where supported, an API key everywhere else.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [Listar MCP - Verified B2B Contact Data](/hermes/mcp/servers/external/listar-mcp/)
