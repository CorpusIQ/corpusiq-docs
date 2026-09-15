---
title: "Ashton & Forge Directory MCP - Vetted AI Implementation"
description: "Keyless read-only MCP directory of vetted AI implementation agencies from the Ashton & Forge marketplace. Three tools summarize the service clusters and industries covered, filter agency listings by service, industry, client size, engagement stage and budget, and hand off the matching-brief link. Free, no account."
category: Business Operations
stars: "n/a (hosted service, no repo)"
added: 2026-09-02
source: "mcpservers.org /all JSON-LD (Sep 2, 2026 morning sweep)"
relevance: ★★
tags: [mcp-server, agencies, directory, ai-implementation, marketplace, vendor-discovery]
---

# Ashton & Forge Agency Directory MCP

**A keyless, read-only directory of vetted AI implementation agencies, answerable from your assistant.** The server exposes the Ashton & Forge marketplace as three read-only tools: what the marketplace covers, how to filter the vetted listings, and how a buyer actually gets matched. Listings are anonymized deliberately - the agent learns what the agencies can do and who they serve, and hands you the matching-brief link when you are ready to meet them. Public, free, no account, no key.

```
Server type: Hosted, keyless (live-probed Sep 2, 2026)
Endpoint: https://ashtonforge.com/mcp/directory (Streamable HTTP, read-only, unauthenticated)
Server: Ashton & Forge Agency Directory v1.0.0 (initialize 200, no auth)
Website: ashtonforge.com
Tools: 3 (directory_summary, search_agencies, get_matched)
```

## Why This Matters for Operators

Buying AI implementation help is a procurement problem, and procurement starts with scoping. This server is built to answer the first question a buyer asks: "is there an agency that can build this, and what does that supply look like?"

First, **scope before you meet.** `directory_summary` reports the service clusters with supply, the industries served, the engagement floors, and the answers to the questions buyers ask first - so an operator can judge whether the marketplace even covers their problem before talking to anyone.

Second, **filters mirror buying criteria.** `search_agencies` filters listings by service cluster, industry, client size, engagement stage or budget, and returns how many matched and what they can do - a shortlist without a sales call.

Third, **the handoff is a brief, not a contact dump.** `get_matched` returns the URL that starts a matching brief, what it asks, how long it takes, and what it costs - the anonymized directory converts into a named conversation only through the marketplace's own matching step.

## Tools and Capabilities

All three tools live-probed keyless Sep 2, 2026 (server v1.0.0):

| Tool | Description |
|------|-------------|
| `directory_summary` | Read-only. What the Ashton & Forge marketplace covers: service clusters with supply, industries served, engagement floors, and the questions buyers ask first |
| `search_agencies` | Read-only. Filter the vetted agency listings by what they do and who they do it for; every filter optional, returns how many matched and what they can do |
| `get_matched` | Read-only. How a buyer gets matched: the URL that starts the brief, what it asks, how long it takes, what it costs |

## Installation

Claude (web/desktop): Settings, Connectors, Add custom connector, paste `https://ashtonforge.com/mcp/directory`, leave authentication empty - there is no account to create and no key to paste.

```bash
claude mcp add --transport http ashtonforge https://ashtonforge.com/mcp/directory
```

Confirm all 3 tools are listed after connecting. Any other Streamable HTTP client takes the same URL.

## Configuration

Nothing to configure. Read-only, unauthenticated, no usage limits stated. The server speaks Streamable HTTP at the directory URL; the root `/mcp` path serves the marketing page, so use the `/mcp/directory` path for the MCP endpoint.

## Business Relevance

- **Operators buying AI implementation** get a scoped shortlist and a structured brief instead of a directory of marketing claims.
- **Procurement teams** get engagement floors and budget filters before committing a stakeholder meeting.
- **Consultants scoping build partners** can check which industries and service clusters have supply.

## Integration with CorpusIQ

Ashton & Forge composes with CorpusIQ as the build-vs-buy conversation. CorpusIQ covers the business data layer (Stripe, QuickBooks, Shopify, HubSpot); Ashton & Forge answers who can implement on top of it. An operator can ask "which vetted agencies build e-commerce data pipelines, and what do their engagements cost" while CorpusIQ quantifies the data problem the engagement must solve.

## Limitations

- Three read-only tools; no agency names are exposed until the marketplace matching step.
- The directory is one marketplace's vetted set, not an exhaustive industry census.
- Read-only and anonymized by design - there is no API for direct outreach or contact data.
- No public repo; the listing page and live probe are the sources of record.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
- [Small Business Intelligence MCP - Metro Records and Teardowns](/docs/hermes/mcp/servers/external/small-business-intelligence-mcp)
