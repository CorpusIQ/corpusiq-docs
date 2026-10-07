---
title: ddmarketer MCP - Validated SaaS Opportunity Intelligence
description: Hosted, keyless MCP server that surfaces validated SaaS opportunities mined from real user complaints across eight public sources and scored 0-100 for commercial intent. Four tools cover gap search by keyword, weekly top opportunities, idea validation against the complaint corpus, and full dossiers with source links, MVP scope and suggested pricing.
category: Data & Analytics
stars: n/a (new listing)
added: 2026-09-04
source: "mcp.so GitHub issue #3932"
relevance: ★★★
tags: [saas-opportunities, market-research, product-gaps, customer-complaints, product-validation, remote-mcp, streamable-http]
---

# ddmarketer MCP

**Remote MCP server (Streamable HTTP, keyless)** - a hosted research service that mines real, recurring user complaints from eight public sources (Reddit, Hacker News, GitHub, Stack Exchange, Trustpilot, app store reviews, product forums, X) and turns them into scored SaaS opportunities. No account, no API key, read-only and rate limited. Four tools confirmed by live probe in this sweep.

```
Server type: Remote (Streamable HTTP)
Auth: None (public, read-only, rate limited)
Endpoint: https://www.ddmarketer.com/api/mcp
Tools: 4 (search_gaps, get_top_gaps, validate_idea, get_dossier)
Pricing: Free
License: MIT (client repo CodePhantom-1/ddmarketer-mcp)
```

## Why This Matters for Operators

"Decide what to build" is the most expensive decision a product team makes, and the standard inputs are vibes, competitor feature lists and analyst reports. ddmarketer inverts that: it starts from complaints real users have already written, then scores each gap 0-100 for commercial intent (willingness to pay signals inside the complaint language). **An operator deciding between two product ideas can run both through `validate_idea` and get a corpus-backed comparison instead of a whiteboard debate.**

The `get_dossier` tool is the stand-out: for one validated gap it returns the source complaints with links, a suggested MVP scope, suggested pricing and the competitors already serving the space. That is a one-call competitive brief for a build decision.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `search_gaps` | Find validated software opportunities by keyword |
| `get_top_gaps` | This week's highest-commercial-intent opportunities across all categories |
| `validate_idea` | Score an idea you already have against the complaint corpus - how many real complaints match, how commercial, how confident |
| `get_dossier` | Full dossier for one gap: source complaints and links, MVP scope, suggested pricing, competitors already serving it |

## Installation

```bash
claude mcp add --transport http ddmarketer https://www.ddmarketer.com/api/mcp
```

No key and no account. The endpoint answers anonymous initialize and tools/list (verified live this sweep), so the agent can explore the full surface before the first query.

## Configuration

```json
{
  "mcpServers": {
    "ddmarketer": {
      "url": "https://www.ddmarketer.com/api/mcp"
    }
  }
}
```

Read-only by design; there are no write tools. Rate limits apply to the public endpoint.

## Business Relevance

- **SaaS founders and product teams** validate build decisions against real complaint data instead of intuition.
- **Agencies and studios** use `get_top_gaps` as a weekly opportunity radar for client pitches.
- **Growth teams** mine complaint language for positioning and landing-page copy.
- **Competitive analysts** use dossiers to see which competitors already serve a gap and how.

## Integration with CorpusIQ

CorpusIQ answers "what is happening in my business"; ddmarketer answers "what should the product do next". A CorpusIQ-connected agent researching a vertical can pull the top complaint gaps for that vertical and cross-check the dossier's competitor list against CorpusIQ's own competitive research. For an early-stage operator running both, ddmarketer is the idea-validation layer upstream of the product analytics CorpusIQ already provides.

## Limitations

- Indie project: client repo has 0 stars and the corpus sources and scoring methodology are described, not audited.
- Public endpoint is rate limited; bulk corpus export is not offered through MCP.
- Scoring reflects complaint language, not revenue data - treat dossiers as directional evidence, not market sizing.
- No historical API to compare gaps across time yet.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
- [Klarix Intelligence Engine MCP - B2B Competitive Intelligence](/hermes/mcp/servers/external/klarix-intelligence-engine-mcp)
- [Neonjelly MCP - Shopify Store Intelligence for Agents](/hermes/mcp/servers/external/neonjelly-mcp)
