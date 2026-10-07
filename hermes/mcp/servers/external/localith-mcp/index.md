---
title: "Localith MCP - Google Business Profile Data for Agents"
description: "Google Business Profile data for AI agents: locations, listings, reviews and performance metrics, with review-trend analysis and location comparisons."
category: Marketing
stars: n/a (new listing)
added: 2026-10-06
source: "mcp.so feed (Oct 6, 2026 evening sweep)"
relevance: ★★
tags: [local-seo, google-business-profile, reviews, marketing, analytics, remote-mcp]
---

# Localith MCP

**Remote MCP server (Streamable HTTP, account sign-in)** - connects Claude and ChatGPT to your Google Business Profile data: connected locations, listing details, customer reviews and performance metrics, worked into review trends, location comparisons, listing audits and reports through natural-language prompts.

```
Server type: Remote (Streamable HTTP)
Auth: Account sign-in (Google Business Profile connected)
Endpoint: https://embedsocial.com/app/api/mcp
Tools: enumerated after sign-in
Pricing: see Localith / EmbedSocial plans
Built by: EmbedSocial team (Localith)
Listing: mcp.so (submitted Oct 6, 2026)
```

## Why This Matters for Operators

For any business with a physical presence, the Google Business Profile is the storefront: listings, hours, photos and reviews are what customers see before they ever reach the website. Managing that surface across locations is normally dashboard work - open the GBP tab, click through each location, export screenshots into a report.

Localith puts that data behind an MCP endpoint: an agent can read the connected locations, pull listing details and customer reviews, compare locations side by side and turn review trends into a report. For agencies running local clients and multi-location brands, it turns the monthly "how are our locations doing" pull into a question rather than a tab-tour.

## Tools & Capabilities

| Area | What the agent can read |
|---|---|
| Locations | Connected Google Business Profile locations |
| Listings | Listing details for each location, for audits |
| Reviews | Customer reviews across locations |
| Performance | Profile performance metrics |
| Analysis | Review trends, location comparisons and generated reports through prompts |

The public listing does not expose a tool list before sign-in, so the exact tool set is enumerated once your account is connected.

## Installation

```bash
claude mcp add localith --transport http https://embedsocial.com/app/api/mcp
```

Sign in with your Localith (EmbedSocial) account with a Google Business Profile connected. The endpoint returns 401 until authenticated - that is expected, not an outage.

## Configuration

```json
{
  "mcpServers": {
    "localith": {
      "url": "https://embedsocial.com/app/api/mcp"
    }
  }
}
```

## Business Relevance

- **Local operators** read their own reviews and listing status without opening the GBP dashboard.
- **Multi-location brands** compare locations and spot review-trend drift per market.
- **Agencies** fold location audits and review reports into their client workflow from chat.
- **Marketing teams** prep reports with the underlying profile data already in the conversation.

## Integration with CorpusIQ

CorpusIQ's read-only connectors cover the business's own numbers - revenue, orders, ad spend, analytics. Localith covers the local presence layer that sits in front of those numbers: what customers see and say on Google before they convert. An operator can ask one question and get both halves - the business data and the local-market view.

## Limitations

- New product (first submitted to mcp.so Oct 6, 2026); no track record in this catalog yet.
- Requires a Localith (EmbedSocial) account with a Google Business Profile connected; the public endpoint returns 401 without sign-in.
- The tool list is not public before authentication; capabilities above follow the published listing.
- Scoped to the Google Business Profile surface; it is not a general web-analytics or social tool.

## FAQ

### What can I ask it for?

Locations, listing details, customer reviews and performance metrics for your connected profiles - and analyses built from them: review trends, location comparisons, listing audits and reports.

### Do I need my own account?

Yes. Connect with a Localith (EmbedSocial) account that has your Google Business Profile linked. The endpoint requires sign-in (a bare probe returns 401).

### Which AI clients does it work with?

Claude and ChatGPT are the stated clients, and the endpoint is plain Streamable HTTP, so any MCP client that supports remote HTTP servers with a sign-in flow can connect.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [MisarSEO MCP - SEO Research for AI Agents](/hermes/mcp/servers/external/misarseo-mcp/)
- [Sitegoalie MCP - WordPress Operations for Agencies](/hermes/mcp/servers/external/sitegoalie-mcp/)
