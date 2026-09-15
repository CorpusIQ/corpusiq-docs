---
title: "Hive Intelligence MCP - Live Crypto Market Data for Agents"
description: "Live crypto market data MCP: 607 tools over prices, on-chain activity, DeFi, derivatives, NFTs and token-safety checks with provenance receipts on every answer. Keyless trial tier, endpoint mcp.hiveintelligence.xyz/mcp live-probed Sep 1, 2026."
category: Finance
stars: "18 (hive-intel/hive-sdk)"
added: 2026-09-01
source: "chatmcp/mcpso issue #3869 (Sep 1, 2026)"
relevance: ★★★
tags: [mcp-server, crypto, market-data, on-chain, defi, token-safety, finance, provenance]
---

# Hive Intelligence MCP

**Hosted Streamable HTTP MCP server for live crypto market data with receipts.** Hive aggregates prices, on-chain activity, DeFi, derivatives, NFT and token-security data across major providers, and every answer carries a provenance receipt naming the provider, freshness and runtime status. A compact 8-tool root routes into a full 607-tool catalog.

```
Server type: Hosted, remote (Streamable HTTP)
Endpoint: https://mcp.hiveintelligence.xyz/mcp
Auth: keyless trial (25 calls per IP per day); signed-in OAuth 2.1 lifts to 10,000 monthly credits free
Registry: xyz.hiveintelligence/mcp v1.1.4 (official registry, active)
Repo: github.com/hive-intel/hive-sdk (MIT, 18 stars, created Aug 2025)
Website: hiveintelligence.xyz
Tools: 8 exposed at the root, 607 reachable through the catalog router
```

## Why This Matters for Operators

Crypto market questions used to mean juggling price feeds, blockchain explorers and token-safety checkers separately, then guessing which number is current. Hive puts the answer chain inside one server.

First, **provenance receipts on every answer.** Each result names its data provider, freshness and runtime status, so an agent can say "this price is 40 seconds old from CoinGecko" instead of quoting a remembered number. That is the difference between a research assistant and a liability.

Second, **token-safety screening is built in.** check_token_safety surfaces honeypot, tax, ownership and GoPlus risk datapoints for any EVM contract, which matters for any operator evaluating a token, a counterparty or an integration target.

Third, **the catalog is deep, not just wide.** Beyond prices, the 607-tool catalog covers wallets, DeFi positions, derivatives across venues, NFTs and Solana, with a typed receipt contract (validate_task_result) checking answers before they reach a human.

## Tools and Capabilities

All 8 root tools were live-probed and verified Sep 1, 2026. The root is a compact routing surface; the full 607-tool catalog is reached through search_tools plus the schema and invoke tools (dispatcher pattern, built for clients with tool-count caps).

| Tool | What it does |
|------|--------------|
| `get_token_price` | Current price for a token by CoinGecko id or symbol, or chain plus address for a specific contract |
| `check_token_safety` | Security screen for a contract address: honeypot, taxes, ownership and GoPlus risk datapoints |
| `get_wallet_portfolio` | Token holdings for a wallet with balances and USD values; EVM via Alchemy, Solana auto-detected |
| `search_tools` | Search the 607-tool catalog and compact user-intent routes; select a matching route first |
| `get_api_endpoint_schema` | Full input schema, operation type and root invoker for any Hive tool by name |
| `invoke_api_endpoint` | Invokes read-only Hive endpoints by name with schema-validated arguments |
| `invoke_stateful_endpoint` | State-changing endpoints, only after explicit user approval |
| `validate_task_result` | Validates a proposed answer against Hive's typed task-output and evidence-receipt contract |

## Installation

Point any MCP client at the hosted endpoint. No key needed for the trial tier:

```json
{
  "mcpServers": {
    "hive": {
      "url": "https://mcp.hiveintelligence.xyz/mcp"
    }
  }
}
```

## Configuration

Anonymous use is capped at 25 calls per IP per day, no account. Signing in over OAuth 2.1 lifts the cap to 10,000 monthly credits at no cost. The issue submission documents an OAuth 2.1 flow with a bearer-token fallback for headless clients.

## Business Relevance

- **Funds and analysts** get cross-venue prices, derivatives and on-chain data in one callable surface with freshness receipts.
- **Compliance and risk teams** screen contract addresses for honeypots, taxes and ownership risk before recommending any token to clients.
- **Treasury operators** track wallet holdings and valuations across chains from one question.
- **Researchers** cite the receipt contract (provider, freshness, status) instead of unverifiable market claims.

## Integration with CorpusIQ

Hive composes with CorpusIQ as the market-facing half of a crypto-adjacent finance workflow. CorpusIQ answers from the books (QuickBooks transactions, Stripe settlement, GA4) while Hive answers from the market: token prices, portfolio values and contract risk. An operator can ask "what is our token position worth right now and how risky is that new treasury candidate" and get both sides, internal records and live market data, in one conversation. Pairs naturally with CryptoStruct for cross-exchange market structure and with Stock Market MCP when the question spans digital and traditional assets.

## Limitations

- Free anonymous tier is small (25 calls per IP per day); real workflows need the signed-in 10,000-credit tier.
- Crypto data only; no equities, FX or macro series.
- The root exposes 8 routing tools; the 607-tool catalog requires the search-then-invoke pattern rather than flat tool listing in Cursor-style clients.
- State-changing endpoints require explicit approval per call, which adds a confirmation step to automated loops.

## See Also

- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
- [CryptoStruct Market Data MCP](/docs/hermes/mcp/servers/external/cryptostruct-mcp)
- [Stock Market MCP Server - Real-Time Financial Data](/docs/hermes/mcp/servers/external/stock-market-mcp-server)
- [Edgrapi MCP - SEC EDGAR Structured Data for Agents](/docs/hermes/mcp/servers/external/edgrapi-mcp)
