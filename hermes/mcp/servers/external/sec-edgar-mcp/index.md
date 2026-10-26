---
title: "SEC EDGAR MCP - Full-Text Filing Search for Agents"
description: "Apify-hosted MCP server exposing SEC EDGAR full-text search as tools: keyword search with every form filter, company lookup and filing document retrieval for agents doing diligence, competitive intelligence and public-company research."
category: Finance
stars: "n/a (Apify-hosted actor)"
added: 2026-08-31
source: "mcpservers.org /all (newest-first page, Aug 31 midday sweep)"
relevance: ★★★
tags: [mcp-server, sec, edgar, filings, finance, research, apify]
last_updated: "2026-10-19"
---

# SEC EDGAR Full-Text Search MCP

**Public-company filings, searchable from any MCP client.** This Apify-hosted actor wraps SEC EDGAR's full-text search as MCP tools: keyword search across every filing type, company lookup, and filing document retrieval. Ask an agent to find all 10-Ks mentioning a product line, pull the latest proxy statement for a competitor, or trace insider-ownership language across filings - without leaving the chat.

```
Server type: Hosted on Apify (community actor rl1987/sec-edgar-mcp)
Access: Apify actor MCP endpoint (run via Apify; API token or free-tier usage applies)
Search surface: SEC EDGAR full-text search (sec.gov/edgar/search) with all form-type filters
Tools: keyword search, company lookup, filing document retrieval
Built by: R.L. (community, via Apify)
```

## Why This Matters for Operators

Public-company research is a slow, tab-heavy workflow. SEC EDGAR's native search is powerful but not agent-friendly.

First, **the whole filing corpus becomes agent context.** Instead of a human reading PDFs one at a time, an agent can search every 10-K, 8-K and proxy statement for a phrase, filter by form type, and retrieve the matching documents on demand.

Second, **diligence gets faster.** Vendor checks, competitor monitoring and M&A screening all start with EDGAR. An agent with this server answers "what did they disclose about X in the last four quarters" in one query instead of a browser session.

Third, **it is standard EDGAR data.** Full-text search covers the same public records professionals already use, just exposed as tools an AI can call repeatedly.

## Tools and Capabilities

Per the mcpservers.org listing and the actor description:

| Capability | Description |
|-----------|-------------|
| Keyword search | Full-text search across all SEC EDGAR filings with every form-type filter |
| Company lookup | Resolve company names to EDGAR CIKs and filing sets |
| Filing retrieval | Fetch the filing documents behind a search hit |

## Verification (Aug 31, 2026)

- Listed on mcpservers.org /all page (newest-first) with official-style remote listing.
- Actor page: apify.com/rl1987/sec-edgar-mcp (community actor, sponsored-adjacent placement).
- Not endpoint-probed in this sweep: Apify actors require an account/API token to run, so liveness was confirmed from the directory listing and actor documentation rather than a direct JSON-RPC call.
