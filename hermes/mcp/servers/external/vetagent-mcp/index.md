---
title: "VetAgent MCP - Pre-Trade Token Risk Intelligence for Agents"
description: "VetAgent MCP is a free, keyless pre-trade safety check for AI agents: before an agent buys, holds or recommends a crypto token it gets one actionable verdict (low, medium, high, unknown) plus the signals behind it - sell simulation, taxes, liquidity depth, pair age, impersonation and owner powers read from contract bytecode. Ethereum, BSC, Base, Solana."
category: Finance
stars: 0
added: 2026-09-07
source: "chatmcp/mcpso issue #3987"
relevance: ★★★
tags: [crypto, token-risk, due-diligence, keyless, remote-mcp, finance]
---

# VetAgent MCP - Pre-Trade Token Risk Intelligence for Agents

**Remote MCP server (Streamable HTTP, keyless)** - VetAgent answers the question every token-touching agent should ask before acting: can I actually get out of this position? It returns one actionable verdict - low, medium, high or unknown - plus the specific signals behind it, instead of forty raw fields to interpret.

```
Server type: Remote (Streamable HTTP, Cloudflare Worker)
Auth: None; free, no signup, no API key
Endpoint: https://vetagent.dev/mcp (probe-verified; anonymous tools/list served 3 tools)
Tools: 3 (assess_token_risk, get_token_liquidity, find_new_hot_pools)
Pricing: Free
Category: Finance
Built by: VetAgent (vetagent.dev); repo github.com/jakegu1/vetagent
```

## Why This Matters for Operators

Token risk tools usually answer with data dumps and let the agent draw its own conclusions - and a confident wrong conclusion is the worst outcome. VetAgent's two design decisions are the reason it stands out: it fails closed (when a critical check cannot run, the answer is unknown, never "low risk"), and it publishes its own measured error rate, including the unflattering figures, with the benchmark harness in the repository for anyone to reproduce.

**The checks are the ones that actually matter for a position: sell simulation (can you actually exit), buy and sell tax, liquidity depth, trading-pair age, same-ticker impersonation, and owner powers read from contract bytecode - across Ethereum, BSC, Base and Solana.**

## Tools & Capabilities

| Tool | What it returns |
|---|---|
| assess_token_risk | Full risk verdict (low, medium, high, unknown) with the specific signals behind it |
| get_token_liquidity | Liquidity snapshot: price, 24h volume, pair count, chains traded |
| find_new_hot_pools | Newest and most active pools by chain (discovery only) |

Plain-HTTP access exists for non-MCP callers: GET https://vetagent.dev/assess/<address>.

## Installation

No keys, no signup - point any Streamable HTTP client at the endpoint. The registry name is dev.vetagent/vetagent.

```json
{
  "mcpServers": {
    "vetagent": {
      "type": "http",
      "url": "https://vetagent.dev/mcp"
    }
  }
}
```

## Configuration

None required. The anonymous probe returned serverInfo and all 3 tools, confirming the keyless design.

## Business Relevance

- **Trading operations** gate every token decision on a fail-closed risk verdict.
- **Payments teams** screen token acceptance and treasury exposure before onboarding a new asset.
- **Analysts** use liquidity snapshots and pool discovery as market-structure inputs.
- **Agent builders** wire the verdict into trading and recommendation workflows as a mandatory pre-check.

## Integration with CorpusIQ

VetAgent screens the token; CorpusIQ screens the business. A composed workflow: the agent vets any token a counterparty proposes via VetAgent, then evaluates the counterparty's actual financials through CorpusIQ's Stripe, QuickBooks and bank connectors - two independent diligence layers before capital moves.

## Limitations

- Brand new listing (issue #3987, Sep 7, 2026); 0-star repo, MIT, Cloudflare Worker deployment.
- Crypto scope only; no traditional-finance risk surface.
- Risk verdicts are measured, not guarantees; the vendor's own error-rate publication is part of the contract.
- Pool discovery is a new-listing signal, not investment advice.

## See Also

- [Hive Intelligence MCP - Live Crypto Market Data](/hermes/mcp/servers/external/hive-intelligence-mcp/)
- [CryptoStruct Market Data MCP - Real-Time Crypto Market Data](/hermes/mcp/servers/external/cryptostruct-mcp/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
