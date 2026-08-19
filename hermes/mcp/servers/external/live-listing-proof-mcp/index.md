---
title: "Live Listing Proof MCP - Verify Listings Before Agents Rely on Them"
description: "Hosted verification MCP that checks public product, marketplace, classified, and auction listings before an agent cites them: fail-closed verdicts at $0.02 USDC per check via x402 on Base, no API key"
category: Verification
stars: n/a (new listing)
added: 2026-08-18
source: "mcp.so GitHub issue #3630"
relevance: ★★
tags: [verification, trust, commerce, marketplace, x402, agent-safety, fail-closed, remote-mcp]
---

# Live Listing Proof MCP

**Hosted verification service that checks a public listing before an agent relies on it.** Send a URL and a claim; get a fail-closed verdict with source-supported facts — or an explicit removed, blocked, unreachable, unsupported, or insufficient-evidence state. Designed for agents that recommend products, cite listings, monitor classifieds, or act on advertised prices. $0.02 USDC per verification on Base via x402, no API key and no account.

```
Server type: Remote (Streamable HTTP MCP)
Auth: None (x402 micropayment per call)
Endpoint: https://live-listing-proof.mattskowronis.workers.dev/mcp
Verify endpoint: https://live-listing-proof.mattskowronis.workers.dev/v1/verify
Pricing: $0.02 USDC per verification (Base mainnet)
Category: Verification / Trust
Registry: dev.workers.mattskowronis.live-listing-proof/verify-listing
Built by: Skowron Works (skowronworks.com)
```

## Why This Matters for Operators

The most expensive failure mode for commerce agents is confident hallucination: recommending a product that was delisted, citing a price that changed, or alerting on a classified that sold yesterday. Live Listing Proof converts that failure mode into a cheap, fail-closed check. Instead of an agent trusting its training-time memory of a listing, it verifies the live page and gets a structured verdict with evidence.

The fail-closed design is the point: the service returns explicit negative states (removed, blocked, unreachable, unsupported, insufficient-evidence) rather than inventing facts. Recommendation and citation workflows should proceed only on `verified` with `claim_supported: true`.

## Tools & Capabilities

| Tool | What it does |
|---|---|
| `verify_listing` | Checks a listing URL against a supplied claim: availability, price, and/or location |
| `source_status` | Fail-closed state: verified, removed, blocked, unreachable, unsupported, or insufficient-evidence |
| Structured output | `verdict`, `claim_supported`, `title`, `price`, `location`, `evidence`, `retrieval_method` — optional facts are null when unsupported |

## Installation

```bash
claude mcp add --transport http live-listing-proof https://live-listing-proof.mattskowronis.workers.dev/mcp
```

No key, no account. Payment is settled per call via x402 (HTTP 402 Payment Required) in USDC on Base mainnet.

## Configuration

```json
{
  "mcpServers": {
    "live-listing-proof": {
      "type": "http",
      "url": "https://live-listing-proof.mattskowronis.workers.dev/mcp"
    }
  }
}
```

## Business Relevance

- **Shopping agents** verify a product URL and advertised price before recommending
- **Classified monitors** check that an ad is still current before alerting
- **Auction agents** confirm a lot has not sold or been removed before bidding decisions
- **Research agents** cite only source-supported listing facts
- **Procurement agents** check a supplier or product page before continuing a workflow

## Integration with CorpusIQ

CorpusIQ tracks the outcome; Live Listing Proof guards the input. A procurement or research agent can verify a supplier's public listing with Live Listing Proof, then run the financial picture through CorpusIQ (payments history, invoices, vendor spend) before recommending action. Together they shrink the two biggest agent-commerce risks: acting on stale listing data and acting without a financial picture.

## Limitations

- One verification per paid call; not a search engine or price-history database
- Verifies public listing pages only; no merchant-owned inventory API access
- Results are not cached as fresh — each call is a live check
- Individual-developer service hosted on Cloudflare Workers; no SLA published
- x402 payment rails still early-adopter territory

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
