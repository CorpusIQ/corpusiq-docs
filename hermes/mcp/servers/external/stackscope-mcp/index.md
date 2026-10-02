---
title: "StackScope MCP - Technographic Sales Intelligence for Agents"
description: "Technographics for the new web: what technologies new websites launch with, adopter tracking for your product or competitors, and contact export across 10 MCP tools with OAuth sign-in at mcp.stackscope.dev. Operated by DATAFREAK LTD."
category: Lead Generation & Web Scraping
stars: "n/a (hosted service)"
added: 2026-09-01
source: "mcpservers.org /all page 1 - stackscope-dev-docs-mcp listing (Sep 1, 2026 morning sweep)"
relevance: ★★★
tags: [mcp-server, technographics, sales-intelligence, lead-generation, tech-stack, competitive-intelligence, adopters]
---

# StackScope MCP

**Technographic intelligence for the new web, callable from any MCP client.** StackScope detects what new websites are built with the week they launch, tracks who adopts your product or a competitor's, and exports the matching companies with published contacts. Ten tools over OAuth sign-in, priced on the same credit model as its HTTP API.

```
Server type: Hosted, remote (Streamable HTTP)
Endpoint: https://mcp.stackscope.dev
Auth: OAuth sign-in and approval on first connection; revoke from the API keys page
Pricing: Data plan credits - 1 credit per call, 1 site from the monthly allowance per site returned for the first time; repeats free; cost approval before large results
Operator: DATAFREAK LTD (UK company no. 17328826)
Website: stackscope.dev (docs at /docs/mcp)
Tools: 10 (account_status, lookup_site, list_technologies, find_sites, technology_sites, technology_trend, export_sites, list_watches, create_watch, delete_watch)
```

## Why This Matters for Operators

BuiltWith-style intelligence usually lives in a web dashboard nobody checks. StackScope puts the same data inside the agent that is already doing your prospecting and competitive work.

First, **adopter tracking as a standing workflow.** create_watch delivers new adopters of your product (or a competitor's) by email or webhook, so the agent can hand the sales team a fresh list every week instead of a stale export.

Second, **contacts come with the technographics.** find_sites filters by technology, category, country, dates and contact availability, and export_sites pulls up to 5,000 sites with optional CSV - the exact list a lead-gen workflow needs, with published contact data attached.

Third, **cost control is explicit.** Before a large result the server quotes the credit and allowance cost and waits for approval, so an autonomous agent cannot silently burn the data plan.

## Tools and Capabilities

All 10 tools are documented on the vendor's /docs/mcp page with descriptions, Sep 1, 2026.

| Tool | What it does |
|------|--------------|
| `account_status` | Plan, permissions and remaining allowance. Free |
| `lookup_site` | Everything known about one site |
| `list_technologies` | The technology catalogue with usage counts |
| `find_sites` | Search by technology, category, country, dates and contact availability |
| `technology_sites` | Sites using one technology, newest first |
| `technology_trend` | Weekly adoption of a technology over time |
| `export_sites` | Bulk export, up to 5,000 sites, with optional CSV |
| `list_watches`, `create_watch`, `delete_watch` | Standing watches delivered by email or webhook |

## Installation

Paste the endpoint into any MCP client and approve the sign-in once:

```json
{
  "mcpServers": {
    "stackscope": {
      "url": "https://mcp.stackscope.dev"
    }
  }
}
```

Claude Code: `claude mcp add --transport http stackscope https://mcp.stackscope.dev`, then run /mcp to sign in.

## Configuration

First connection opens a sign-in and approval flow; command-line tools receive the callback on the local machine, so keep the app running while approving. Reconnect or revoke any time from the API keys page. Pricing follows the Data plan: one credit per call and one site from the monthly allowance for each site returned for the first time in the period; repeats are free. account_status always reports what remains, and nothing is charged without approval.

## Business Relevance

- **Founders and GTM teams** answer "what sites launched in the UK with WordPress this week, only ones with a contact email" in one call.
- **Sales operations** get exported lists of technology adopters with published contacts, up to 5,000 per pull.
- **Competitive intelligence** watches which analytics, CDN or hosting stack is growing fastest each quarter.
- **Partner teams** set standing watches (email or webhook) for new launches in a target country or stack.

## Integration with CorpusIQ

StackScope composes with CorpusIQ as the top-of-funnel half of a pipeline loop. CorpusIQ answers from the systems you already run (HubSpot deals, Stripe customers, Gmail threads) while StackScope answers from the market: who just launched with a competing stack, who adopted your product, and which of them published a contact. An operator can ask "give me this week's new Shopify launches in Germany with emails, then check which are already in our HubSpot" and get the list and the dedupe in one workflow. Pairs naturally with Apollo.io for enrichment-heavy outreach and with Xverum for people-level search once a company is identified.

## Verification (Sep 1, 2026)

- **Live endpoint probed**: POST to `https://mcp.stackscope.dev` with a JSON-RPC initialize returned `{"error":"unauthorized"}` - the server is up and OAuth-gated, refusing anonymous enumeration while confirming liveness.
- GET on the endpoint returns a 302 (nginx) toward the sign-in flow, consistent with the OAuth-required posture.
- Full tool surface requires an authorized session; capability table per the official submission and docs.

## Limitations

- Credit-based: every new site returned consumes one site from the monthly allowance; heavy sweeps need plan capacity planning.
- OAuth sign-in required; no anonymous or API-key-only mode documented.
- Detection-only data: inclusion on stackscope.dev reflects technical detection, not endorsement or affiliation.
- No public repo; the hosted service and its docs are the source of record.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
- [Leadgen MCP - Romanian Business Registry & Contact Enrichment](/hermes/mcp/servers/external/leadgen-mcp)
- [Apollo.io MCP](/hermes/mcp/servers/external/apollo-io-mcp)
- [SalesTouch MCP: LinkedIn GTM Prospecting for AI Agents](/hermes/mcp/servers/external/salestouch-mcp)
- [Xverum MCP - People Search Across 750M Professional Profiles](/hermes/mcp/servers/external/xverum-mcp)
