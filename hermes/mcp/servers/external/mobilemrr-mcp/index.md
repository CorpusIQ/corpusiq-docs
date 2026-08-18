---
title: "MobileMRR MCP - CorpusIQ Docs - CorpusIQ Docs"
description: Search mobile app acquisition opportunities with provider-verified revenue data, side-by-side listing comparisons, and live valuation estimates from any MCP client.
category: Finance
stars: n/a (new listing)
added: 2026-08-16
source: mcp.so
relevance: ★★
tags: [acquisitions, marketplace, mrr, valuation, mobile-apps, saas, verified-revenue, remote-mcp]
---

# MobileMRR MCP

**Remote acquisition-data server (Streamable HTTP, no auth)** — MobileMRR is a marketplace and public database for mobile apps with verified revenue, exposed over MCP at `mobilemrr.com/mcp`. Founders can prove an app makes real money, and buyers can evaluate an acquisition using provider-backed revenue data instead of screenshots or self-reported claims. Five read-only tools cover search, detail, leaderboard, side-by-side comparison, and live valuation estimates.

```
Server type: Remote (Streamable HTTP)
Auth: None
Endpoint: https://mobilemrr.com/mcp
Tools: 5 (search_listings, get_listing, get_leaderboard, compare_listings, estimate_valuation)
Pricing: Free — listing an app is free; no agent-side billing
Category: Finance & Commerce
Built by: MobileMRR (mobilemrr.com)
```

## Why This Matters for Operators

App acquisitions have run on trust — screenshots of revenue dashboards and founder-claimed numbers. MobileMRR replaces that with verification: the seller connects their RevenueCat or Superwall account and MobileMRR reads MRR, subscriber counts, and revenue directly from the provider's API. An agent can then filter listings by verified MRR, asking price, category, and platform, and pull side-by-side comparisons with profit multiples.

**The key advantage: diligence that used to take a broker and a data room now starts with one agent query.** The valuation tool adds a live low-mid-high estimate from MRR, category, age, platform, and verification status — a first-pass filter before human negotiation.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `search_listings(category, platform, for_sale, min_mrr, max_mrr, min_price, max_price, sort, limit, page)` | Search and filter live app listings with sorting and pagination |
| `get_listing(slug)` | Full detail on one app: verification status, verified MRR, asking price |
| `get_leaderboard(limit)` | Apps ranked by verified monthly revenue, highest first |
| `compare_listings(slugs)` | Side-by-side comparison of price, MRR, profit multiple, verification status, platform, category, and active users |
| `estimate_valuation(mrr, category, age_months, platform, verified)` | Live low/mid/high acquisition value range for a hypothetical or real app |

Only revenue marked verified via RevenueCat or Superwall should be treated as confirmed; unverified figures are founder-claimed estimates. Listing creation is human-only for now — agent-side listing support is planned.

## Installation

```bash
claude mcp add mobilemrr --transport http https://mobilemrr.com/mcp
```

The vendor publishes connection snippets for Claude Code, Codex, Cursor, and VS Code on the listing page.

## Configuration

```json
{
  "mcpServers": {
    "mobilemrr": {
      "type": "http",
      "url": "https://mobilemrr.com/mcp"
    }
  }
}
```

No API key, no account — the server is public and read-only by design, so nothing can be created or modified through it.

## Business Relevance

- **Buyers** filter the for-sale pool by verified MRR and asking price, then compare finalists with profit multiples
- **Founders** benchmark their own app against the leaderboard before pricing an exit
- **Investors and PE scouts** screen mobile-app deal flow with provider-backed revenue instead of founder claims
- **Analysts** get a live valuation model with explicit inputs instead of rule-of-thumb multiples

## Integration with CorpusIQ

MobileMRR pairs naturally with CorpusIQ's revenue connectors as a comps layer. An operator can pull their own verified revenue from CorpusIQ's Stripe and GA4 connectors, then use MobileMRR's leaderboard and `estimate_valuation` to benchmark that number against the live mobile-app acquisition market — same MRR, different multiples, one comparison pass.

For an acquisition target, the composed workflow runs the other direction: MobileMRR supplies verified MRR, asking price, and valuation range, while CorpusIQ's Stripe and QuickBooks connectors model the target's revenue mechanics once the data room opens. CorpusIQ holds the deal's financial ground truth; MobileMRR supplies the market context.

## Limitations

- Brand new — submitted to mcp.so in mid-August 2026; marketplace liquidity is thin until listings accumulate
- Read-only — agents cannot create or edit listings; submission is a human flow
- Only RevenueCat and Superwall verification providers are supported today
- Unverified listings carry founder-claimed revenue; treat them accordingly
- The valuation model is a live estimate — outputs are not guaranteed identical across repeated calls
- No escrow or transactions — purchases complete off-platform between buyer and seller

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
