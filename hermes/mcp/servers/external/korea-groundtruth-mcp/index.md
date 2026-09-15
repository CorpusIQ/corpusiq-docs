---
title: Korea Ground-Truth MCP - Official Korean Data for Agents
description: Official Korean business data for AI agents - NTS business registration checks, DART corporate profiles, MOLIT property prices and statute search through one hosted MCP server with a free API key.
category: Compliance
stars: n/a (new listing)
added: 2026-08-26
source: "mcp.so GitHub issue #3776"
relevance: ★★★
tags: [korea, business-verification, government-data, dart, corporate-registry, kyb, law, remote-mcp]
---

# Korea Ground-Truth MCP

**Remote MCP server (Streamable HTTP, free bearer-key)** - Korea Ground-Truth (KGT) unifies five Korean government data sources - National Tax Service, DART corporate filings, road-name addresses, MOLIT property transactions and the National Law Information Center - into one API and one MCP server with 8 tools. Agent-native billing is built in: prepaid credits (1 credit = 10 KRW, calls cost 1-3 credits), the cost shown in every tool description, the balance in every response, and a 402 with a top-up URL when credits run out. Hosted at `kr-groundtruth-mcp.vercel.app`, version 0.1.0, anonymous initialize verified live (stateless handshake answered).

```
Server type: Remote (Streamable HTTP)
Auth: Bearer key (free, 50 credits) - attach as the authorization header
Endpoint: https://kr-groundtruth-mcp.vercel.app/api/mcp
Tools: 8 (business registration, DART, addresses, property prices, statutes)
Pricing: Free 50-credit key, prepaid credits after (1 credit = 10 KRW)
Category: Compliance
Built by: ChloePark85 (repo github.com/ChloePark85/kr-groundtruth-mcp)
```

## Why This Matters for Operators

Doing business in or with Korea means five different government systems with five integration efforts: tax registration status, corporate registry data, property transaction prices, official addresses and current statutes. Most teams skip the integration and rely on stale or second-hand data.

**KGT replaces five government API integrations with one MCP endpoint an agent already knows how to use.** An operator can verify a Korean counterparty's business registration status, pull its DART corporate profile, check real MOLIT apartment transaction prices for a market view and confirm the current statute text - in one workflow, with cost visibility on every call and automatic refunds when an upstream government source fails.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `verify_business_registration` | Business registration status (active/suspended/closed) and validation via NTS |
| `search_address` | Road-name address normalization, postal code, legal-dong code |
| `search_corporation` | DART corp_code search |
| `lookup_corporation` | Company profile - CEO, corporate registration number, address |
| `apartment_trade_prices` | MOLIT apartment transaction prices |
| `search_law` | Current statutes with enforcement dates |
| `get_balance` | Remaining credit balance |
| `get_pricing` | Per-tool credit costs |

## Installation

```bash
claude mcp add kgt --transport http https://kr-groundtruth-mcp.vercel.app/api/mcp
```

## Configuration

```json
{
  "mcpServers": {
    "kgt": {
      "type": "http",
      "url": "https://kr-groundtruth-mcp.vercel.app/api/mcp"
    }
  }
}
```

Request a free 50-credit key with `POST https://kr-groundtruth-mcp.vercel.app/v1/accounts` (JSON body with your email), then attach it as the authorization header on MCP calls. OpenAPI spec and llms.txt are published alongside the endpoint.

## Business Relevance

- **KYB teams** verify Korean counterparty registration status and corporate details before onboarding.
- **Real estate and investment analysts** pull actual MOLIT transaction prices instead of listing data.
- **Legal teams** confirm current statutes with enforcement dates rather than cached copies.
- **Compliance officers** get official government data with an audit-friendly, cost-transparent API.

## Integration with CorpusIQ

KGT complements CorpusIQ's financial connectors for operators with Korean exposure. A CorpusIQ workflow reading QuickBooks or Stripe data can pull a Korean vendor or customer name, run KGT's business-registration verification and DART corporate lookup, and attach the official confirmation to the vendor record before any payment flows. It also pairs with the Korea Business Verify guide in this catalog for a full Korean due-diligence stack - KYB checks plus official registration data.

## Limitations

- Brand new - version 0.1.0, zero stars, no track record yet.
- Korean data only; property tool covers apartments specifically.
- Prepaid credits with a 402 stop when empty - billing is explicit but not subscription-style.
- No self-host option; the vendor's Vercel endpoint is the only deployment.
- Free tier is 50 credits, which covers roughly 15-50 calls depending on tool.

## See Also

- [Korea Business Verify MCP - Live KYB Checks for Korean Companies](/docs/hermes/mcp/servers/external/korea-business-verify)
- [1Lookup MCP - Phone, Email and IP Verification](/docs/hermes/mcp/servers/external/1lookup-mcp)
- [External MCP Server Catalog](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
