---
title: "MisarSEO MCP - SEO Research for AI Agents"
description: "Keyword research, live SERP data, backlinks, rank tracking and Search Console performance for SEO work, from one hosted MCP server."
category: SEO
stars: n/a (new listing)
added: 2026-10-06
source: "chatmcp/mcpso issue #4797"
relevance: ★★
tags: [seo, keywords, serp, backlinks, rank-tracking, search-console, marketing, remote-mcp]
---

# MisarSEO MCP

**Remote MCP server (Streamable HTTP, OAuth sign-in or API key)** - SEO research for agents on open, verifiable data. MisarSEO brings keyword research, live SERP inspection, domain and page research, backlinks, rank tracking and first-party Search Console performance into any MCP client, and it ships companion SEO skills that tell the agent how to run each workflow. It is part of the Misar family alongside MisarReach, MisarMail and Misar.Blog, all catalogued in this index.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth sign-in on first connect, or an API key minted from a signed-in session
Endpoint: https://seo.misar.io/mcp
Tools: keywords, SERP, domain research, local business, backlinks, rank tracking, Search Console, URL inspection
Pricing: Free plan includes 25 keyword lookups/day, 5 tracked keywords and 1 audit/month; paid plans add limits
Built by: MisarSEO
Registry: via seo.misar.io (login flow)
```

## Why This Matters for Operators

SEO research normally lives in a web dashboard: you export keyword lists, paste SERPs into spreadsheets, and hand-carry Search Console numbers into reports. MisarSEO moves the whole loop into the conversation your agent is already having - research a keyword, pull the live SERP, hydrate the opportunity list with volume, difficulty, CPC and intent, check what a domain already ranks for, then read the first-party Search Console numbers to see what actually happened.

**The research and the performance data meet in one place.** Most keyword tools sell estimates; MisarSEO pairs its research surface with the operator's own Search Console property, so an agent can compare "what we could win" against "what we already show for". The hosted endpoint means no scraping babysitting, and the free plan is usable on day one: 25 keyword lookups a day, five tracked keywords and one audit a month at no cost.

The companion skills are the sharpest part: instead of asking an agent to "do SEO", you point it at a specific workflow - SEO project setup, keyword research, competitive landscape, competitor analysis, keyword clustering or link prospecting - each defined in a `SKILL.md` the vendor maintains alongside the server.

## Tools & Capabilities

| Area | What the agent can do |
|---|---|
| Keyword research | Volume, difficulty, CPC and trends; hydrate keywords with intent and traffic |
| SERP inspection | Live Google organic results for a keyword, competitor comparison across a keyword set |
| Domain research | Exact keyword, page, rank, volume, CPC, intent and traffic rows for a domain or page |
| Local business | Search businesses near a coordinate, read a Maps or Local Finder SERP, pull Google Business Q&A |
| Backlinks | Backlink and referring-domain overview data for a domain |
| Rank tracking | Read rank tracker configs and latest keyword positions; save useful keywords back to the project |
| Search Console | First-party GSC performance (clicks, impressions, CTR, position) and URL inspection for index status, crawl and canonical, up to 10 URLs per call |

## Installation

```bash
claude mcp add --transport http --scope user misarseo https://seo.misar.io/mcp
```

Approving the MisarSEO login when prompted. Cursor, Codex and Claude Desktop have published walkthroughs, and the AI & MCP page in MisarSEO has a copyable endpoint plus the current setup UI. Use user scope to make the server available across projects.

## Configuration

```json
{
  "mcpServers": {
    "misarseo": {
      "url": "https://seo.misar.io/mcp"
    }
  }
}
```

If authorization fails, disconnect the server in the client, add it again and repeat the login. If the agent cannot find a project, ask it to list MisarSEO projects first and pass the returned project ID into later calls.

## Business Relevance

- **Marketing leads** run keyword and competitor research in the same conversation as the campaign plan, without a dashboards tab.
- **Agencies** put client projects behind one connection and read GSC performance next to the research backlog.
- **SEO specialists** batch URL inspections (up to 10 per call) and read index status without opening Search Console.
- **Founders** get a usable free tier: 25 keyword lookups a day, five tracked keywords, one audit a month.

## Integration with CorpusIQ

CorpusIQ reads the business's own Google Search Console property through the Search Console connector, so the performance side of the picture is already available, read-only, alongside GA4, Google Ads and the rest of the stack. MisarSEO adds the outside view: which keywords exist, what the SERPs look like, which domains link where, and what competitors rank for. Together an operator can ask one question and get both halves - what our site already earns, and what the market around it looks like.

## Limitations

- Brand new listing: no track record from this catalog yet.
- Hosted only; there is no self-host path.
- Every call needs the connected account; there is no anonymous mode.
- Free-plan caps are real: 25 keyword lookups a day, 5 tracked keywords, 1 audit a month.
- Rank tracking and audits refresh on the provider's schedule, not on every call.

## FAQ

### Do I need an API key?

Either sign in through the OAuth flow on first connect, or mint an API key from a signed-in session (the endpoint answers `POST /api/keys`). The key path suits headless agents.

### What does the free plan include?

MCP access with 25 keyword lookups per day, 5 tracked keywords and 1 audit per month. Paid plans raise the limits.

### Can it read my Search Console data?

Yes, as a first-party connection: GSC performance (clicks, impressions, CTR, position) plus URL inspection for index status, crawl and canonical.

### Is it related to MisarReach and MisarMail?

Yes, same vendor family. The siblings cover outbound sales and email operations; MisarSEO covers search research.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [MisarReach MCP - Outbound Sales and Lead Pipeline for AI Agents](/hermes/mcp/servers/external/misarreach-mcp/)
- [Seomely MCP - Google Index Monitoring for Agents](/hermes/mcp/servers/external/seomely-mcp/)
