---
title: "OEDON MCP: Bitcoin On-Chain Intelligence for AI Agents"
description: "Hosted x402 MCP server for Bitcoin on-chain market data - fee pressure, mempool stats, address analytics, hashrate, difficulty, block tips, mining pool distribution, transaction lookups and whale alerts. Live-probed oedon v0.2.0, anonymous initialize, pay-per-call 0.005 USDC in USDC on Base."
category: Finance
stars: n/a (new listing)
added: 2026-08-23
source: "mcp.so GitHub issue #3706 + live endpoint probe"
relevance: ★★★
tags: [bitcoin, on-chain-data, crypto-market-data, x402, usdc, remote-mcp, trading-research]
---

# OEDON MCP

**Bitcoin on-chain market intelligence over MCP - fee pressure, mempool statistics, address analytics, hashrate trends, difficulty adjustments, block tips, mining pool distribution, transaction lookups and whale alerts - served as a single x402 pay-per-call tool in USDC on Base.** The hosted server at `https://oedon.dev/mcp` was live-probed this sweep: anonymous initialize succeeded (server `oedon` v0.2.0, protocol 2025-11-05) and `tools/list` returned the full schema. No API key, no signup - discovery is free and each data query costs 0.005 USDC via x402 on Base mainnet.

```
Server type: Remote (Streamable HTTP, hosted)
Auth: None (anonymous initialize); x402 pay-per-call for data
Endpoint: https://oedon.dev/mcp
Tools: 1 (live-probed; server v0.2.0, protocol 2025-11-05)
Payment: USDC on Base via x402, 0.005 USDC per query
Manifest: https://oedon.dev/.well-known/mcp.json
```

## Why This Matters for Operators

Bitcoin network conditions move money: settlement times, treasury transfers, miner economics and market sentiment all sit behind mempool and chain state. Normally that data lives in explorer UIs that nobody queries mid-decision. OEDON puts fee pressure, congestion signals and whale alerts inside the agent that is already analyzing the situation, so the agent can answer "what will it cost to settle this now" with live numbers instead of stale assumptions. The x402 model keeps costs proportional: free discovery, then fractions of a cent per query, so a screening agent can check many addresses but pay only for the checks it actually needs.

## Tools & Capabilities

1 tool confirmed by live probe. `chain_query_onchain_intelligence` takes a `query_type` and returns the corresponding data set:

| query_type | What it returns |
|---|---|
| fee_pressure | Current mempool fee tiers and congestion signal |
| mempool_stats | Mempool size, tx count, fee histogram |
| address_stats | Balance, tx count, total received/sent for a Bitcoin address |
| hashrate | Network hashrate and 30-day trend |
| difficulty | Epoch progress, estimated adjustment, retarget date |
| block_tip | Latest block height, hash, timestamp, tx count, fees, size |
| mining_pools | 7-day pool distribution, top miners, share percentages |
| tx_lookup | Transaction details by txid (value, fees, inputs, outputs, status) |
| whale_alert | Recent large mempool transactions (>1 BTC unconfirmed) |

All data is sourced from public chain data. The probe confirmed the exact enum values above, so agents can enumerate query types safely.

## Installation

```json
{
  "mcpServers": {
    "oedon": {
      "type": "http",
      "url": "https://oedon.dev/mcp"
    }
  }
}
```

For the Claude Code CLI: `claude mcp add --transport http oedon https://oedon.dev/mcp`

## Configuration

No API key and no signup. Initialize anonymously and the server responds with its tools capability. Each data query returns the x402 payment challenge (USDC on Base, 0.005 USDC), which the agent or its x402-enabled wallet client satisfies to receive the data. The server publishes its service catalog machine-readably at `https://oedon.dev/v1/services` and its model instructions at `https://oedon.dev/llms.txt`.

## Example Prompts

- "What are current Bitcoin mempool fee tiers, and is the network congested right now?"
- "Check the balance and total received for this Bitcoin address."
- "Any whale transactions over 1 BTC sitting unconfirmed in the mempool?"
- "What is the 7-day mining pool distribution and current network hashrate trend?"

## Business Relevance

- **Treasury and settlement teams** check fee pressure before timing a Bitcoin payment or payout batch
- **Trading desks** watch whale alerts and mempool congestion as short-term market signals
- **Compliance screening** pulls address stats and transaction details for due-diligence checks
- **Mining and infrastructure operators** track difficulty retargets and pool distribution

## Integration with CorpusIQ

CorpusIQ answers questions about the business's own data (revenue, campaigns, customers). OEDON adds the external Bitcoin market layer: an agent can pull live fee pressure or whale alerts from OEDON and cross-check the timing against commercial workflows held in CorpusIQ - for example, confirming settlement conditions before a payout run, or validating a counterparty's on-chain activity against their business history.

## Limitations

- Pay-per-call: every data query costs 0.005 USDC over x402 on Base, so bulk historical pulls add up - discovery and schema enumeration stay free.
- One tool with point-in-time queries; no historical time-series API and no account/portfolio management.
- Public-source data only: derived from public chain data, not proprietary order books or exchange feeds.
- Hosted-only service with no published GitHub repository (new listing, Aug 23, 2026).

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external) - curated third-party MCP servers for operators
- [CryptoStruct Market Data MCP](/hermes/mcp/servers/external/cryptostruct-mcp) - historical crypto and prediction-market data over MCP
- [Truth Bear GAUGE MCP](/hermes/mcp/servers/external/truth-bear-gauge) - verifiable government data with x402 pay-per-record
- [MCP Integration Guide](/hermes/mcp) - connecting MCP servers to Hermes Agent
