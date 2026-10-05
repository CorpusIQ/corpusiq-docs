---
title: GovContract Radar MCP - Federal Contract Alerts
description: "AI-native MCP server for U.S. federal contract opportunities: filter SAM.gov solicitations by NAICS code and set-aside, with deadlines and agency details."
category: Sales & Outreach
stars: n/a (new listing)
added: 2026-10-05
source: mcpservers.org /all (Oct 5, 2026 morning sweep)
relevance: ★★
tags: [sales-outreach, government-contracts, sam-gov, prospecting, search, remote-mcp]
---

# GovContract Radar MCP

**Remote MCP server (Streamable HTTP)** - an AI-native server from PixHarvest that brings U.S. federal contract opportunities into any MCP client. It filters new SAM.gov solicitations by NAICS code and set-aside status (8(a), SDVOSB, WOSB, HUBZone) and surfaces response deadlines and agency details the day they post. Built on public U.S. government data (SAM.gov and USAspending); the live initialize handshake identifies the server as "PixHarvest GovContract Radar" v1.2.0, syncing hourly through GovConAPI with a SAM fallback every 6 hours.

```
Server type: Remote (Streamable HTTP)
Auth: open keyless initialize; paid plans unlock filtering and alerts (7-day free trial)
Endpoint: https://gov.pixharvest.com/mcp
Tools: search_opportunities, get_opportunity
Pricing: Starter $19/mo, Pro $49/mo, Radar+ $149/mo (card or invoice)
Package: gov-contract-radar-mcp (npm, MIT) | Product: pixharvest.com/gov
```

## Why This Matters for Operators

Government contracting is a pipeline business with unforgiving clocks: solicitations post, deadlines move, and the advantage goes to whoever sees the opportunity first. Watching SAM.gov by hand is a search session nobody keeps up with; this server turns it into a monitored feed filtered to the NAICS codes and set-aside programs your business actually qualifies for, with the response deadline on every card.

That reframes the assistant as a capture desk. Instead of "are there any contracts for us?", the operator asks which of this week's matches are worth a bid, which need a partner, and which deadlines collide with current delivery capacity. The data layer carries early signals too: presolicitations and special notices that precede formal solicitations.

## Tools & Capabilities

| Capability | What it does |
|---|---|
| `search_opportunities` | Query federal contract opportunities by NAICS, keyword or set-aside |
| `get_opportunity` | Full detail for a specific solicitation |
| Daily digest | Optional email digest of new matches (subscription) |

Beyond the two tools, the substance sits in the data: set-aside flags (8(a), SDVOSB, WOSB, HUBZone) on every opportunity, response deadlines surfaced first, agency details, and the synced SAM.gov feed with special notices as early signals.

## Installation

```json
{
  "mcpServers": {
    "gov-contract-radar": {
      "type": "streamable-http",
      "url": "https://gov.pixharvest.com/mcp"
    }
  }
}
```

Point any MCP client (Claude, Cursor, others) at the endpoint. The initialize handshake is open and keyless; the listing's plans carry NAICS filtering, the daily digest and set-aside alerts, with a 7-day free trial and no card required.

## Business Relevance

- **Set-aside targeting**: filter to the programs your business actually qualifies for instead of reading the full feed.
- **Deadline-first triage**: each opportunity carries its response deadline and agency, so the assistant can rank what needs attention this week.
- **Early signals**: presolicitations and special notices surface ahead of formal solicitations, giving capture time.
- **Pipeline reporting**: fold opportunity data into the same assistant that reads revenue and capacity through CorpusIQ, so "can we staff this?" has an answer next to "should we bid this?".

## Integration with CorpusIQ

CorpusIQ reads the business itself (revenue systems, ads spend, site demand) read-only; GovContract Radar adds the demand source on the government side. An operator can ask one assistant to cross the two: which NAICS categories are producing solicitations while free capacity exists, which agencies' deadlines cluster in the weeks after a slow season. Each system answers what the other cannot, and neither writes into the other.

## Limitations

- U.S. federal opportunities only (SAM.gov and USAspending data).
- Two documented tools; deeper workflows (digest, alerts) sit in the subscription plans.
- Paid from $19/mo after the trial; Radar+ adds priority data, custom filters and team access.
- Vendor-operated; governed by PixHarvest terms. The npm package `gov-contract-radar-mcp` (MIT) is verified at v1.0.0.

## FAQ

### What is GovContract Radar?

An MCP server that filters new U.S. federal contract opportunities from SAM.gov by NAICS code and set-aside status, with deadlines and agency details, delivered as they post.

### Does the server need an API key?

The keyless initialize handshake works out of the box (verified live); the filtering plans start with a 7-day free trial, and paid tiers run $19 to $149 per month.

### What set-asides are covered?

8(a), SDVOSB, WOSB and HUBZone flags on every opportunity.

### Where does the data come from?

Public U.S. government data: SAM.gov and USAspending, synced hourly through GovConAPI with a SAM fallback every 6 hours and posted-to-radar latency under 60 minutes.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [RestoSignals MCP - Scored Restaurant Opening Leads](/hermes/mcp/servers/external/restosignals-mcp/)
- [The Company Atlas MCP - Trade Data and Company Registries](/hermes/mcp/servers/external/company-atlas-mcp/)
