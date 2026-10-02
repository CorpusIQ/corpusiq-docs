---
title: Nexlab MCP - Cited Data Intelligence Across 23 Servers
description: A cited-data suite of 23 MCP servers and 200 tools behind one endpoint and one key. Corporate ownership and due-diligence trails, court records, EU policy watch, trade tariffs, vulnerability intelligence and more, with every answer naming its sources. Free tier of 50 calls per month per server.
category: Data & Analytics
stars: n/a (no public repo)
added: 2026-09-06
source: mcpservers.org
relevance: ★★★
tags: [data-intelligence, citations, regulatory, legal-research, corporate-research, due-diligence, api, remote-mcp]
---

# Nexlab MCP - Cited Data Intelligence Across 23 Servers

**Remote MCP server (HTTP, single API key)** - a hosted suite of 23 MCP servers and 200 tools behind one endpoint and one key, covering corporate ownership trails, court records, EU policy, trade tariffs, vulnerability intelligence, Shodan search, research papers, public health and more. Every answer names the sources behind it and states their limits, so what the agent reports can be checked. Every server starts free at 50 calls per month.

```
Server type: Remote (HTTP)
Auth: single API key for all 23 servers
Endpoint: https://mcp.nexlab.net
Tools: 200 across 23 servers
Pricing: free tier 50 calls/mo per server, then per-server plans from about 9 to 19 EUR/mo
Category: Data & Analytics
Built by: Nexlab (mcp.nexlab.net)
```

## Why This Matters for Operators

The gap in most agent data tooling is not access - it is accountability. A model that answers from scraped or unstated sources produces confident wrong answers, and operators making decisions on those answers cannot verify them. Nexlab's design rule is that every answer names the sources behind it and states their limits, and the errors it returns are structured so the agent can act on them instead of guessing.

**The operator-relevant servers are the ones that normally take three separate subscriptions: Corporate Money Trail (public corporate ownership, filings, identity records and due-diligence links), Court Records, EU Policy Watch, Trade Tariffs and Vulnerability Intel - plus Shodan search for exposure work.** One key covers all of them, which collapses the credential and billing sprawl of assembling the same stack vendor by vendor. The 50 free calls per month per server mean the whole suite can be evaluated before any card exists.

Warm responses land in about 0.2 seconds, so the suite works inside an interactive agent session rather than as a batch API you babysit.

## Tools & Capabilities

| Server | What it covers |
|---|---|
| Corporate Money Trail MCP | Public corporate ownership, filings, identity records and due-diligence links for large companies |
| Court Records MCP | Court record search and retrieval |
| EU Policy Watch MCP | European Union policy documents and regulatory tracking |
| Trade Tariffs MCP | Tariff and trade data for compliance and sourcing questions |
| Vulnerability Intel MCP | Vulnerability intelligence for security exposure checks |
| Shodan Search MCP | Internet-facing asset and service discovery via Shodan |
| Peer Research Papers MCP | Peer-reviewed literature search |
| Wikipedia Retrieval MCP | Cited Wikipedia lookups |
| Public Health Watch MCP | Public health data and monitoring |
| Air Route Atlas, Flight Watch, Europe Rail Watch, Maritime AIS MCP | Transport and logistics data (routes, connections, live traffic) |
| Grid Carbon, Planet Watch, Sky Watch, Weather MCP | Environmental and earth observation data |
| Launch Watch MCP | Rocket and launch activity tracking |
| Sacred Texts, Sports Events Results, Scientific Math Calculator MCP | Reference and domain utilities |

The full 200-tool list is served live from the endpoint after key setup; the table above follows the vendor's published server catalog. Every tool answer carries source attribution and stated limits.

## Installation

```bash
claude mcp add --transport http nexlab https://mcp.nexlab.net
```

Sign up for one key that unlocks all 23 servers, then attach it as the authorization header for the client. Each server stays at 50 free calls per month until a paid plan is chosen per server.

## Configuration

```json
{
  "mcpServers": {
    "nexlab": {
      "type": "http",
      "url": "https://mcp.nexlab.net",
      "headers": {
        "X-API-Key": "your-nexlab-key"
      }
    }
  }
}
```

The single key authenticates the whole suite. Per-server plan selection happens in the Nexlab dashboard, and the free tier never expires - no trial clock.

## Business Relevance

- **Due-diligence and BD teams** run corporate ownership and filing checks from the Corporate Money Trail server with cited sources
- **Legal and compliance operators** track EU policy and trade tariffs in the same surface as court record search
- **Security teams** pair Vulnerability Intel with Shodan search for exposure checks
- **Supply-chain and logistics operators** use the transport servers for route, flight and maritime questions

## Integration with CorpusIQ

Nexlab complements CorpusIQ's governed business-data read layer with cited external intelligence. CorpusIQ answers what is happening inside the business (Stripe, QuickBooks, HubSpot, GA4); Nexlab answers what is happening around it - ownership, policy, tariffs, exposure - with sources the agent can cite back to the operator. A composed workflow: an agent researches a target company's ownership trail through Corporate Money Trail, checks the regulatory posture with EU Policy Watch and Trade Tariffs, and cross-references the target's financial health with CorpusIQ's data connectors, producing a sourced briefing where every claim is checkable.

## Limitations

- New listing (September 2026) - no long track record or public repository to inspect
- Hosted only; there is no self-host option for the suite
- 50 free calls per month per server is a thin free tier for production use
- Some servers (transport, earth observation) are consumer or niche rather than business-critical
- Attribution quality depends on each server's upstream sources, which the vendor discloses per answer

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/hermes/mcp/connectors)
