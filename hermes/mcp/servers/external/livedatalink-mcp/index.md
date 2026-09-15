---
title: "LiveDataLink MCP - Live Public Data for AI Agents"
description: "Hosted Streamable HTTP MCP with 284 agent-ready tools across 59 public-data domains - stocks, options, crypto, SEC filings, sanctions, courts, healthcare, economic data, CVE, weather, real estate and more - behind one bearer key with a free tier. One endpoint, one bill, no per-vendor contracts."
category: Data & Analytics
stars: n/a (hosted)
added: 2026-08-27
source: "mcpservers.org /all page 2 (livedatalink-ai-tools)"
relevance: ★★★
tags: [public-data, market-data, sec-filings, sanctions, cybersecurity, real-estate, remote-mcp]
---

# LiveDataLink MCP

**Hosted remote MCP server (Streamable HTTP, Bearer API key) aggregating live public data for AI agents.** LiveDataLink runs 284 agent-ready tools across 59 data domains through one endpoint: stocks, options, crypto, SEC EDGAR filings, FRED macroeconomic series, EIA energy data, sanctions screening, federal court filings, CVE/cybersecurity, weather, vehicle VIN, package tracking, property records, FMCSA carrier safety and more. One bearer key, one bill, no per-vendor contracts. A free API key (1,000 calls/month, no card) is minted in-conversation by the server itself, and anonymous evaluation allows 25 lifetime data calls per network.

```
Server type: Remote (Streamable HTTP)
Auth: Bearer API key; 25 lifetime anonymous data calls per network at 10 req/min
Endpoint: https://livedatalink.ai/mcp
Tools: 284 across 59 catalog domains
Pricing: Free key 1,000 calls/month (no card); Starter $10/mo at 30 req/min; Pro at 120 req/min; $199 founder-assisted pilot credited to plan
Docs: https://livedatalink.ai/tools · machine-readable: https://livedatalink.ai/llms.txt
Category: Data & Analytics
```

## Why This Matters for Operators

Every operator research question - "what did this competitor file with the SEC", "is this vendor on a sanctions list", "what does the Fed's data say about this market" - currently means a different vendor, a different contract and a different API key. LiveDataLink collapses 59 public-data domains into a single endpoint with a single bearer key, so an AI assistant can answer across finance, compliance, courts, energy, weather and real estate without the operator maintaining a fleet of data contracts. **The free key is minted by the server itself from inside the conversation - no signup form, no browser - so an agent can go from zero to live public data in one prompt.**

The catalog is demand-driven: `search_available_datasets` is free, and logged searches steer what the vendor builds next, so coverage grows in the direction operators actually query.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `search_available_datasets` | Free-text search across the whole 284-tool catalog; returns exact tool names (free, no credits) |
| `list_tool_groups` | Lists every category with its domain and tool counts; load only needed groups via X-Tool-Groups |
| `get_free_api_key` | Mints a working free-tier key in-conversation from the user's email (free, no credits) |
| `stock_quote` / `stock_quote_batch` | Real-time price, volume, market cap, P/E, 52-week range (batch up to 10 tickers) |
| `options_chain` | Calls/puts with strikes, IV, open interest, expirations |
| `stock_history` | OHLCV history, 1-minute intraday up to 5-year daily |
| `company_info` / `stock_compare` | Financial fundamentals; side-by-side comparison of 2-5 tickers |
| `crypto_price` / `crypto_compare` / `crypto_info` | Coin prices, market data, profiles via CoinGecko |

The remaining ~270 tools span SEC EDGAR, FRED, EIA, sanctions, courts, CVE, weather, vehicles, property and more; the full live list mirrors `tools/list` at the endpoint.

## Installation

```bash
curl -X POST https://livedatalink.ai/mcp \
  -H "Accept: application/json, text/event-stream" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}'
```

Cursor and other header-capable clients use a bare URL with a Bearer header; stdio-only clients wrap the HTTP endpoint with `npx @modelcontextprotocol/server-fetch`.

## Configuration

```json
{
  "mcpServers": {
    "livedatalink": {
      "url": "https://livedatalink.ai/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_API_KEY"
      }
    }
  }
}
```

Invalid keys are rejected rather than downgraded to anonymous; anonymous evaluation is capped at 25 successful lifetime data results per network.

## Business Relevance

- **Founders and operators** get one key covering 59 public-data domains instead of a vendor per domain
- **Finance teams** pull live quotes, options chains and fundamentals alongside SEC and FRED data in one conversation
- **Compliance teams** run sanctions and court checks from the same endpoint that answers market questions
- **Researchers** call `search_available_datasets` first, free, so the model never guesses whether a domain is covered

## Integration with CorpusIQ

LiveDataLink is the public-data complement to CorpusIQ's 40+ private-business connectors. Where CorpusIQ pulls the operator's own books (QuickBooks, Stripe, Shopify, GA4, HubSpot), LiveDataLink supplies the external context around them: a competitor's SEC filings while Stripe revenue is being analyzed, sanctions screening on a vendor named in QuickBooks payables, weather and energy data feeding Shopify inventory planning. An agent wired to both can hold a private-number question and a public-data question in the same thread - CorpusIQ for "what did we sell", LiveDataLink for "what did the market do".

## Limitations

- Brand new - no public track record yet; catalog maturity claims are vendor-reported
- Anonymous evaluation capped at 25 lifetime results per network
- Paid plans raise rate limits (30/120 req/min) but have no automatic overages
- Public data only - no private business records
- Hosted commercial service - no self-host option

## See Also

- [MCP Servers Index](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
- [1Lookup MCP - Phone, Email and IP Verification](/docs/hermes/mcp/servers/external/1lookup-mcp)
