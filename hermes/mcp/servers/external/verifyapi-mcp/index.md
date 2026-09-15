---
title: VerifyAPI MCP - Fact-Checking with Signed Receipts
description: "Single-tool MCP server (npm stdio) that verifies factual claims against live web sources and returns a citable verdict with source URL, published date, verbatim quote and an Ed25519-signed JWS receipt - so downstream systems can prove the check actually happened."
category: Content & Research
stars: n/a (new listing)
added: 2026-09-11
source: mcp.so feed
relevance: ★★
tags: [fact-checking, verification, receipts, hallucination-prevention, compliance, stdio-mcp]
---

# VerifyAPI MCP

**stdio MCP server (npm)** - fact-checks claims before an agent acts on them. One tool takes a claim, checks it against live web sources, and returns a verdict (supported, contradicted or unverifiable) with the source URL, published date, a verbatim quote, reasoning, and an Ed25519-signed receipt. The signed receipt is the differentiator: a downstream system - compliance auditor, user, another agent - can cryptographically prove that a specific claim was verified against a specific source at a specific time.

```
Server type: stdio (npm @verify-api/mcp)
Auth: VERIFYAPI_API_KEY env var (csk_live_ prefix); keyless free trial without it
Tools: 1 (verify_claim)
Pricing: Free trial 3 calls/IP/24h; $0.02 per verified claim; fresh-fetch tier $0.05; unverifiable calls free
Verdicts: supported, contradicted, unverifiable
Category: Content & Research
Built by: Circuit Savers LLC (KyTheKitty/verifyapi-mcp)
```

## Tools

| Tool | Purpose |
|---|---|
| verify_claim | Check one factual claim against live web sources - returns verdict, confidence, source_url, exact_quote, reasoning, and a JWS receipt (kid + jws) |

Example output for a supported claim includes `confidence` (e.g. 0.99), the exact source URL, a verbatim quote, and a receipt object with the key id and compact JWS. Receipts are signed by keys served at api.verify-api.dev/.well-known/jwks.json, so verification is offline-checkable by anyone holding the public keys.

## Connection

1. Optional - get a free key at verify-api.dev/signup (no credit card). Without a key, the free trial allows 3 calls per IP per 24h, receipts included.
2. Add to any MCP client's config:
```json
{
  "mcpServers": {
    "verifyapi": {
      "command": "npx",
      "args": ["-y", "@verify-api/mcp@latest"],
      "env": { "VERIFYAPI_API_KEY": "csk_live_..." }
    }
  }
}
```
3. Use it whenever the agent is about to act on a claim it cannot cite - prices, dates, versions, quotes, statistics, product specs, event outcomes.

## Verification (Sep 11, 2026 evening sweep)

The mcp.so listing carries the verified and featured badges (submitter Circuit Savers LLC). The npm package metadata (v0.1.9) confirms the single-tool design, tiered freshness (default / recent / fresh), $0.02 base per verified claim and the free trial. The GitHub README documents the full verify_claim input/output contract, the three verdicts, and the JWKS endpoint for receipt verification. Note: the listing's tool count shows zero because it is a stdio package - tools surface only when the server runs inside a client.

## See Also

- [TrustScan MCP - Security Scanning for MCP Servers and AI Skills](/docs/hermes/mcp/servers/external/trustscan-mcp)
- [Ultralayer MCP - Realtime Market Intelligence for Agents](/docs/hermes/mcp/servers/external/ultralayer-mcp)
- [Nexlab MCP - Cited Data Across 23 Sources for Agents](/docs/hermes/mcp/servers/external/nexlab-mcp)
