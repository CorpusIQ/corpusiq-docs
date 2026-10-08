---
title: "SV Atlas MCP - Find Startups That Will Buy Your Product"
description: "Hosted MCP server over sourced profiles of accelerator-backed startups: match a product website to its ideal customer, rank likely buyers, and work outreach lists - 19 tools over OAuth with a free tier."
category: Sales Intelligence
stars: n/a (new listing)
added: 2026-10-08
source: "chatmcp/mcpso issue #4934 (October 8, 2026 night sweep)"
relevance: ★★★
tags: [startups, sales, prospecting, lead-generation, investors, founders, research]
---

# SV Atlas MCP

**Hosted MCP server that answers "who would buy this?" for founder-led sales** - paste a website and Atlas writes its ideal-customer profile, then ranks accelerator-backed startups against it. Every fact links to its public source or stays blank. 17,250 startups, 16,655 founders and 402 investment firms, as 19 tools over OAuth.

```
Server type: Remote (Streamable HTTP at https://svatlas.io/mcp)
Auth: OAuth 2.1 with dynamic client registration and PKCE (Google sign-in; resource metadata at svatlas.io/.well-known/oauth-protected-resource/mcp)
Docs: https://svatlas.io
Tools: 19 across search, lists, and enrich and export
Directory: 17,250 startups, 16,655 founders, 402 investor firms (live counts)
Pricing: Free (5 URL matches and 20 meaning searches per month); Pro $69/mo; Team $249/team/mo
Category: Sales Intelligence
Built by: SV Atlas
```

## Why This Matters for Operators

Founders looking for first customers usually bounce between four tools: a startup database, a contact finder, an enrichment spreadsheet, and an outreach tool. SV Atlas takes over the first job - deciding who to sell to - with evidence instead of guesswork. The match reads your product site, writes the customer profile in plain words, ranks companies by semantic fit to that profile, and keeps every fact traceable to a public source. From there the same list carries an outreach angle, a per-company note, and a status column you work through, with CSV export for the tools that come next.

## Tools & Capabilities

| Area | Tools |
|---|---|
| Search | meaning-based search across companies, founders and investors, with sourced profile cards |
| Matching | match_companies_by_website reads a product site, writes its ideal-customer profile and ranks Atlas companies against it (counts toward the monthly URL-match limit) |
| Lists | build and manage outreach lists; each carries an angle, an importance value, a note per company and a status column; team plans share them |
| Enrich and export | company and founder detail with source links, suggested additions, CSV export for outreach on Pro |

## Installation

```bash
claude mcp add --transport http svatlas https://svatlas.io/mcp
```

```json
{
  "mcpServers": {
    "svatlas": {
      "url": "https://svatlas.io/mcp"
    }
  }
}
```

The first call opens the Google sign-in; no API key to manage.

## Configuration

The agent signs in as you and shares the same monthly limits as the site (free: 5 URL matches and 20 meaning searches a month; unlimited on Pro). Live probe: POST initialize returns 401 with a "Sign in to use the Silicon Valley Atlas MCP server" challenge plus OAuth resource metadata, confirming the endpoint is live and auth-gated.

## Example Prompts

- "Here is our product site. Rank the startups most likely to buy it and save the top 20 to a list called 'Q4 outbound'."
- "Which accelerator-backed companies in the email infrastructure market have raised recently and fit our ICP?"
- "Give me the founders behind the top 10 matches, with their X and LinkedIn profiles where public."
- "Export the 'early design partners' list as CSV for our outreach tool."

## Integration with CorpusIQ

CorpusIQ keeps your own numbers consistent across AI clients - revenue, customers and pipelines from Stripe, Shopify or your CRM arrive read-only and cited. SV Atlas sits in front of that: decide who to sell to with sourced startup data, then check the fits against your real revenue picture in the same conversation.

## Limitations

- Free tier is genuinely limited (5 URL matches a month); heavy matching needs Pro.
- Facts come with sources or stay blank; unknown data is not backfilled - treat empty fields as unknown, not false.
- Semantic fit is a ranking aid, not a buying signal; verify a target before high-effort outreach.
- New listing - no published third-party track record yet.

## FAQ

### How does the matching work?

It reads the product website, writes an ideal-customer profile, and ranks Atlas companies by semantic similarity to that profile. Scores are similarity, not purchase intent, and every row shows the sources behind its facts.

### Does it replace Apollo or Clay?

No - the vendor positions Atlas as step one: pick the right companies. Contact finding, enrichment and sequencing stay with whichever tools you already use, fed by the exported list.

### Is there a free plan?

Yes. Free includes 5 URL matches and 20 meaning searches per month, plus the whole directory with source links.

## See Also

- [AffiliateSpy MCP - Competitor Creator Discovery for Agents](/hermes/mcp/servers/external/affiliatespy-mcp/)
- [looot MCP - One Balance for 2,350 Data APIs](/hermes/mcp/servers/external/looot-mcp/)
- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
