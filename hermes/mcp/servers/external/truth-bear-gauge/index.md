---
title: "Truth Bear GAUGE: Verifiable Government Data for AI Agents"
description: "Official government screening signals (SEC, FDA, USGS, NOAA) with cryptographic proof: every record carries a record hash and signed citation verifiable offline. Free find_signal coverage checks and verify_citation; paid records fetched pay-per-call over x402 in USDC on Base. Live-probed v1.0.0, no API key."
category: Compliance
stars: 0
added: 2026-08-23
source: "mcp.so homepage recentServers + live endpoint probe"
relevance: ★★★
tags: [government-data, compliance, sec, verification, x402, usdc, remote-mcp]
---

# Truth Bear GAUGE MCP

**Official government data, provably unaltered: Truth Bear serves screening-level signals (environment, agriculture, power grid, shipping, SEC filings) where every paid record ships with a record hash and signed citation you can verify offline.** The MCP server (live-probed: `truthbear-gauge` v1.0.0, protocol 2025-03-26) at `https://api.truthbear.co/mcp` needs no API key and no account: coverage checks and citation verification are free, and paid records are bought pay-per-call over x402 in USDC on Base - the server itself never takes payment.

```
Server type: Remote (Streamable HTTP, hosted)
Auth: None (free tools); x402 pay-per-call for paid records
Endpoint: https://api.truthbear.co/mcp
Tools: 3 (live-probed; server v1.0.0, protocol 2025-03-26)
Payment: USDC on Base via x402, per record
Repo: changchinfu/mcp-gauge (MIT)
```

## Why This Matters for Operators

Screening decisions - vendor due diligence, environmental risk checks, supply-chain validation - are only as good as the data behind them, and government data is exactly where provenance matters most. **Truth Bear's model is proof-first: `find_signal` tells you (free) whether your entity is covered and how fresh the data is, `get_official_record` returns the x402 payment challenge for the exact record, and `verify_citation` recomputes the canonical hash server-side so you can confirm any record is genuine - before or after paying.** An operator's agent can run coverage checks for free, pay only for the records it needs, and keep every answer verifiable, which is what turns an AI summary into a defensible compliance artifact.

## Tools & Capabilities

3 tools confirmed by live probe:

| Tool | Purpose |
|---|---|
| find_signal | FREE coverage and freshness manifest: which signal lines exist, how many entities each covers, and fresh/recent/stale counts - check "is my entity covered and how fresh" before paying |
| get_official_record | Returns the real x402 payment challenge (network, asset, payTo, amount) for the paid endpoint serving a given signal_id + entity; does not deliver paid data and does not take payment |
| verify_citation | FREE: given a record_hash, look up and recompute the canonical hash server-side, returning whether it is a genuine Truth Bear record plus a plain-language reverse lookup of the record contents |

The server is explicit about its posture: descriptive only - no advice, no forecasts, no adjudication. Signals cover environment, agriculture, power grid, shipping and SEC filings; the cryptographic proof chain (record hash plus signed citation) is what makes the output citable in a due-diligence file.

## Installation

```json
{
  "mcpServers": {
    "truth-bear": {
      "type": "http",
      "url": "https://api.truthbear.co/mcp"
    }
  }
}
```

For the Claude Code CLI: `claude mcp add --transport http truth-bear https://api.truthbear.co/mcp`

## Configuration

No API key and no signup. The free tools (`find_signal`, `verify_citation`) work anonymously. Paid records use x402: `get_official_record` returns a payment challenge, the agent (or its x402-enabled wallet client) pays in USDC on Base, and the record is returned with its hash and signed citation. The server never handles payment itself, which keeps the endpoint keyless and stateless.

## Example Prompts

- "Which of our vendors have SEC filings on file, and how fresh are they?"
- "Pull the environmental screening record for this facility and verify the citation."
- "Is this entity covered for power-grid signals before I pay for anything?"
- "Confirm this record hash is a genuine Truth Bear record."

## Business Relevance

Compliance and due diligence run on authoritative sources, and the failure mode is silent: an unverifiable number in a report that later cannot be defended. Truth Bear's coverage-first, pay-per-record design suits agents that screen many entities but pay for few, and the offline-verifiable citations make every fetched record audit-ready. The government-data focus (SEC, FDA, USGS, NOAA) maps directly to operator screening workflows in vendor management, supply-chain risk and investment research.

## Integration with CorpusIQ

CorpusIQ answers questions about the business's own data (revenue, campaigns, customers). Truth Bear adds the external regulatory and environmental layer: an agent can screen a counterparty's government records (Truth Bear), verify the citations, and cross-check the findings against the relationship's commercial history in CorpusIQ. Verification data from Truth Bear, business truth from CorpusIQ.

## Limitations

- Pay-per-call: each paid record costs USDC over x402 on Base, so bulk historical pulls add up - use `find_signal` to triage coverage before paying.
- Screening-level signals, not full source documents: the server is descriptive and explicitly does not interpret or forecast.
- Young surface: repo created Jul 10, 2026 with 0 stars, though pushed as recently as Aug 23, 2026 and listed across mcp.so, glama.ai and the official registry.
- Free tools cover discovery and verification only; the data itself is paid.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external) - curated third-party MCP servers for operators
- [Corpus Law MCP](/hermes/mcp/servers/external/corpus-law-mcp) - US legal search and business formation over MCP
- [MCP Integration Guide](/hermes/mcp) - connecting MCP servers to Hermes Agent
