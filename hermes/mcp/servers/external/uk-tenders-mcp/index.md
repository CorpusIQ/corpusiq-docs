---
title: "UK Tenders MCP - Public Sector Notices for Agents"
description: "Live UK public-sector notices from Contracts Finder for bid agents: search by keyword, region or CPV, then full packs with fit scoring and risk flags."
category: Sales & Outreach
stars: n/a (new listing)
added: 2026-10-06
source: "chatmcp/mcpso issue #4834 (Oct 6, 2026 evening sweep)"
relevance: ★★
tags: [uk, tenders, procurement, contracts-finder, open-data, remote-mcp, keyless, bid-intelligence]
---

# UK Tenders MCP

**Remote MCP server (Streamable HTTP, keyless)** - live UK public-sector notices from Contracts Finder, shaped for bid agents: a free peek at matching tenders with buyer, deadline and category, then one-time £0.49 packs, including a scored variant with fit and risk flags.

```
Server type: Remote (Streamable HTTP, Cloudflare Worker)
Auth: None (keyless discovery; packs pay per use)
Endpoint: https://uk-tenders-mcp.donniertf.workers.dev/mcp
Tools: 4 (discovery, two pack tools, redeem)
Pricing: Free sample; GBP 0.49 one-time per pack
Built by: donniertf (uk-mcp-fleet)
Source: Contracts Finder (Open Government Licence v3.0)
```

## Why This Matters for Operators

Public-sector work is one of the few demand streams that publishes its buying intent in advance - every tender notice is an explicit "we are buying this, here is the deadline". The friction is filtering: keyword, region, CPV code, then reading enough of each notice to know whether it fits.

This server turns that into a chain an agent can run: discover matching notices for free, then pull a pack where each notice carries buyer, deadline and category - and on the scored variant, a fit score, fit flags and pack risk flags against the query. For bid writers and sales operators, the first-pass triage happens in the conversation instead of in a browser tab.

## Tools & Capabilities

| Tool | What the agent can do |
|---|---|
| `tenders_discover` | Free peek: up to 5 live Contracts Finder notices for a keyword, region or CPV code; cached 24h |
| `tenders_pack` | Paid pack of Contracts Finder notices for the query; Stripe Checkout link, one-time token redeem |
| `tender_score_pack` | Paid scored variant: notices plus `fit_score`, `fit_flags` and `risk_flags` |
| `redeem_pack` | Instructions to redeem a paid Stripe Checkout session |

Free sample: `GET /v1/discover/tenders?query=construction` (up to 5). Scored packs take a query and size, e.g. `{"query":"IT support","size":25}`.

## Installation

```bash
claude mcp add uk-tenders --transport http https://uk-tenders-mcp.donniertf.workers.dev/mcp
```

Discovery is keyless. Paid packs return a Stripe Checkout URL inside the tool result; pay GBP 0.49 and redeem with the one-time token.

## Configuration

```json
{
  "mcpServers": {
    "uk-tenders": {
      "url": "https://uk-tenders-mcp.donniertf.workers.dev/mcp"
    }
  }
}
```

## Business Relevance

- **Bid writers** triage new UK public-sector notices by keyword, region or CPV from the chat.
- **Sales operators** monitor the public pipeline as a demand signal next to their private pipeline.
- **Consultancies and suppliers** score fit before committing time to a full bid.
- **Researchers** get structured notices with buyer and deadline fields instead of portal pages.

## Integration with CorpusIQ

CorpusIQ's read-only connectors already answer "what is happening in our business". The Tenders server answers "what is being bought out there, and does it fit us" - demand-side intelligence that pairs with your own pipeline numbers. Ask what your pipeline looks like, then ask which new public notices match it.

## Limitations

- Contracts Finder coverage: confirm deadlines and details on the official site before acting.
- Free samples are capped (5 notices, 24h cache); full and scored results are behind one-time GBP 0.49 packs.
- Fit scoring is a heuristic flag set to speed triage, not a bid/no-bid decision.
- UK public-sector notices only.

## FAQ

### What sources are searched?

Live UK Contracts Finder notices - public-sector opportunities with buyer, deadline and category fields.

### Can it score tenders for me?

Yes, on the scored pack variant: each notice carries a `fit_score`, `fit_flags` and `risk_flags` alongside the notice fields. Treat the score as triage, not a verdict.

### How much does a pack cost?

GBP 0.49 per pack, paid once via Stripe Checkout from inside the tool call. Discovery is free.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [GovContractScout MCP - State and Local Contracts](/hermes/mcp/servers/external/govcontractscout-mcp/)
- [UK Companies House MCP - KYB Packs for Agents](/hermes/mcp/servers/external/uk-companies-house-mcp/)
