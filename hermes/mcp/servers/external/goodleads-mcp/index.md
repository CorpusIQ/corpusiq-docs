---
title: "GoodLeads MCP - New-Business Leads for Agent Outreach"
description: "Keyless remote MCP server that turns new-business state filings into priced lead lists. An agent interprets a buyer's own words (industry, state, city), quotes the count and live per-record price, and hands back a hosted Stripe checkout link - the human completes payment, never the agent."
category: Sales & Outreach
stars: n/a (new listing)
added: 2026-09-11
source: mcpservers.org /all
relevance: ★★★
tags: [lead-generation, b2b-sales, state-filings, outreach, keyless, remote-mcp]
---

# GoodLeads MCP

**Remote MCP server (Streamable HTTP, keyless)** - formation-grade lead intelligence for agents. GoodLeads watches U.S. state formation filings and lets an agent shop for new businesses the morning after the state posts the filing: interpret the buyer's description of who they sell to, browse and quote the matching records, and mint a hosted checkout link that a human completes. The contact is the owner or an officer named on the filing - never the attorney or formation service that filed it.

```
Server type: Remote (Streamable HTTP, stateless)
Auth: None - no account, no API key, no OAuth
Endpoint: https://mcp.goodleads.club/mcp
Tools: 13 live-probed (2 write tools, both money-safe)
Pricing: $0.25 per record (name + mailing address), $0.50 (plus verified phone or email), $0.70 (both); no minimums
Category: Sales & Outreach
Built by: GoodLeads (goodleads.club)
```

## Tools

| Tool | Purpose |
|---|---|
| interpret_list | Turn the buyer's own words ("cleaning companies in Texas") into a countable, priceable list shape |
| list_starters | Ready-made state × business-type lists with live counts and starting prices |
| browse_leads | Rows for a list shape or saved list, or summary counts, facets and price |
| list_filterable_fields | The filter contract (fields, grammar, recipes) from the schema endpoint |
| explain_concept | Map a buyer's word for a concept to this surface's fields before concluding absence |
| quote_list | What a list costs before anyone pays - records naming a person, price by grade |
| list_live_states | The state codes live in production right now, never a cached page |
| list_products | The pre-shaped shelf of business type × state products |
| find_lead_by_glid | One record in full by Lead ID (e.g. GL-CO-00042), with a _meta provenance block |
| data_quality_scorecard | Mechanical conformance grades per state - format, completeness, consistency, standardization |
| describe_surface | What GoodLeads is and how to act on a list (explain/vet helper) |
| checkout_list | Turn a quoted list into a payment link a person completes (RW - minting costs nothing) |
| create_checkout | Mint a hosted Stripe Checkout link for a shelf product or shaped list (RW) |

Only the two checkout tools write, and neither touches money: they mint a hosted link and save a shaped list. Payment happens on Stripe's hosted page, completed by a human, and the agent is told not to represent the purchase as complete until the person confirms.

## Connection

1. Paste the door URL into any MCP client that takes a remote Streamable HTTP server. No key, no account, no OAuth - leave authentication empty.
2. Claude Code one-liner - `claude mcp add --transport http goodleads https://mcp.goodleads.club/mcp`
3. Claude.ai / Desktop - Customize → Connectors → Add custom connector → paste `https://mcp.goodleads.club/mcp`, leave Advanced (OAuth) empty.
4. First thing to say - "Find me 50 new businesses in Denver I can call this week and quote both the callable-now and newest mail-first options."

## Verification (Sep 11, 2026 evening sweep)

Endpoint live-probed over JSON-RPC: keyless `tools/list` returned all 13 tools with full input schemas and read-only annotations - the door is open as documented. Every record ships the owner name, mailing address, entity type and status, state filing number, formation date, industry with NAICS/SIC/Google Business codes, registered agent, a Lead Reference, and Reachability / Contact Relevance / Contact Confidence scores. Records are priced per record with no minimums; after payment the file is checked for verified phones and emails and only what is found is billed, never more than the authorized ceiling.

## See Also

- [Crawdar MCP - Qualified Prospect Research for Agents](/hermes/mcp/servers/external/crawdar-mcp)
- [Vibe Prospecting MCP - Live B2B Data for Lead Generation](/hermes/mcp/servers/external/vibe-prospecting-mcp)
- [Emailchaser MCP - Cold Email Operations for Agents](/hermes/mcp/servers/external/emailchaser-mcp)
