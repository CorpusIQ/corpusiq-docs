---
title: "Forency MCP - Website Technology Stack Detection for Agents"
description: "MCP server that lets an AI assistant investigate any website's technology stack: CMS, ecommerce platform, JavaScript frameworks, analytics, CRM, marketing automation, payments, chat widgets, CDN, and hosting, available as a hosted endpoint or a local stdio package with API key auth and a free tier of 100 scans per month."
category: Lead Generation & Web Scraping
stars: n/a (new listing, github.com/cheevahagadog/forency-mcp)
added: 2026-08-28
source: mcp.so homepage new arrivals
relevance: ★★
tags: [mcp-server, tech-stack, competitive-intelligence, prospecting, web-analysis, remote-mcp]
---

# Forency MCP

**MCP server that answers "what tech stack does this website run" for any URL.** It detects CMS, ecommerce platform, JavaScript frameworks, analytics, CRM, marketing automation, payments, chat widgets, CDN, and hosting, and ships two connection paths: a hosted endpoint at forency.io with a Bearer API key, or a local stdio package (npx forency-mcp) with the key in an environment variable. The free tier covers 100 scans a month with no credit card.

```
Server type: Remote (Streamable HTTP) and local stdio (npx forency-mcp)
Auth: API key (free tier: 100 scans/month, no credit card)
Endpoint: https://forency.io/api/mcp (hosted)
Pricing: Free tier; paid plans beyond 100 scans/month
Category: Lead Generation / Competitive intelligence
Built by: cheevahagadog (GitHub cheevahagadog/forency-mcp, MIT; Smithery nathan-cheever12/forency-mcp)
```

## Why This Matters for Operators

Sales and competitive teams already ask these questions; they just answer them manually, one browser tab at a time. The README's own examples are the pitch: "What tech stack does competitor.com run?" and "Which of these 15 prospects use HubSpot vs Salesforce?" A batchable tech-stack check turns prospecting lists into qualified lists, because a prospect's CRM, ecommerce platform, and payments stack signal both budget and integration fit before the first call.

For competitive intelligence, the analytics and CDN layer of a competitor's stack reveals what measurement and delivery infrastructure they run, and watching it change over time catches platform migrations early. The hosted endpoint means remote MCP clients use it with nothing installed, while the stdio package covers local-first setups.

**Prospect qualification and competitor stack tracking become one tool instead of fifteen manual lookups.**

## Tools & Capabilities

Capability-level table from the repository documentation; the hosted endpoint requires an API key (verified live, 401 with a clear error directing to the free-key signup).

| Area | Capability |
|---|---|
| Technology profile | Detect CMS, ecommerce platform, JavaScript frameworks, and hosting for a given URL |
| Marketing stack | Detect analytics, CRM, marketing automation, and chat widgets |
| Payments | Detect payment providers and checkout infrastructure |
| Batch checks | Evaluate lists of domains for stack comparison and prospecting |

## Installation

Hosted (remote clients):

```bash
claude mcp add forency --transport http https://forency.io/api/mcp
```

Local (stdio):

```bash
claude mcp add forency -- npx -y forency-mcp
```

Get a free key at forency.io (100 scans/month, no credit card).

## Configuration

```json
{
  "mcpServers": {
    "forency": {
      "type": "http",
      "url": "https://forency.io/api/mcp",
      "headers": {
        "Authorization": "Bearer fcy_your_key"
      }
    }
  }
}
```

For the local package, set the key as the FORENCY_API_KEY environment variable instead of a header.

## Business Relevance

- **Sales teams** qualify prospect lists by CRM, ecommerce, and payments stack before outreach.
- **Competitive intelligence** tracks competitor platform migrations and infrastructure changes over time.
- **Agencies** audit a client's marketing and analytics stack before taking over the account.
- **Partnership teams** find complementary-tool users (for example, every site on a given CRM) for joint-marketing targeting.
- **E-commerce operators** benchmark their stack against category leaders.

## Integration with CorpusIQ

Forency reads the prospect's stack; CorpusIQ reads the prospect's numbers once they convert. A composed workflow: the assistant screens a lead list with Forency, scores fit by detected CRM and platform, then tracks the winners through HubSpot pipeline and Stripe revenue via CorpusIQ connectors to close the loop from stack signal to closed revenue.

## Limitations

- Capability-level tool table: exact tool schemas need an authenticated session.
- Detection accuracy depends on the underlying analyzer (enthec/webappanalyzer lineage); cloaked or heavily custom stacks may underreport.
- Rate limited by plan tier; free tier caps at 100 scans a month.
- Brand new listing: repo created Aug 28, 2026, 1 star, MIT license.
- Hosted endpoint means scan data routes through forency.io rather than running fully locally.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external)
- [Xverum MCP - People Search Across 750M Professional Profiles](/hermes/mcp/servers/external/xverum-mcp)
- [Leadgen MCP - Romanian Business Registry & Contact Enrichment](/hermes/mcp/servers/external/leadgen-mcp)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
