---
title: "TripLedger MCP - Travel Day Counts for Tax and Schengen"
description: "Track tax-residency day counts and Schengen 90/180 status from your own travel history: log trips once in Claude, ChatGPT or any agent."
category: Compliance
stars: n/a (new listing)
added: 2026-10-11
source: "mcp.so /feed (Oct 11, 2026 evening sweep)"
relevance: ★★★
tags: [travel, tax-residency, schengen, day-counts, expenses, compliance, remote-mcp]
last_updated: "2026-10-24"
---

# TripLedger MCP

**Remote MCP server (Streamable HTTP, OAuth 2.1 or API key)** - a personal travel ledger built for AI assistants: connect Claude, ChatGPT, Cursor or any MCP client to log journeys, stays and travel expenses, then ask for tax-residency day counts per country, rolling Schengen 90/180 status, your current country and gaps in your travel history.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth 2.1 (ledger:read and ledger:write scopes) or API key; reads always stay available
Endpoint: https://my.tripledger.app/mcp
Tools: 31 (18 read, 13 write)
Pricing: 14-day free trial, then $97 once per ledger (no subscription)
Registry: app.tripledger/tripledger (official MCP Registry)
Built by: Pianosa Labs (github.com/pianosa-labs/tripledger-mcp)
Listing: mcp.so /feed and mcpservers.org /all (Oct 2026)
```

## Why This Matters for Operators

Day counting is the part of travel that bites quietly. A consultant who works from Lisbon, Dubai and Bangkok is running a tax-residency calculation in every country they sleep in, and a frequent visitor to Europe is running a rolling 90/180 day Schengen calculation whether or not they track it. Overstay penalties and surprise tax residency are expensive precisely because the underlying record was reconstructed from memory at the wrong time.

TripLedger keeps the record where the counting happens: log trips once, and the assistant answers questions from the same history - days per country this year and the last 365 days, remaining Schengen days if a planned trip runs its course, or the exact exit date the rolling window implies. Both counting methods (Any Presence and Midnight Rule) are built in and switched per country, so the number matches local tax rules instead of a spreadsheet formula.

**The ledger is the point: journeys, stays and costs stay connected to the totals they came from.** Gap detection flags untracked days so the record is complete before it goes to an accountant, and booking emails can be logged as trips without retyping anything.

## Tools & Capabilities

| Tool group | Purpose |
|---|---|
| Journeys (read and write) | Log, update, list and delete journeys, including from booking emails |
| Status (read) | Tax-residency day counts per country, rolling Schengen 90/180 status, current country, travel summary |
| Records (read and write) | Stays and travel expenses attached to the trip they belong to |
| Integrity (read) | Gap detection for missing days, plus the documented counting methodology |

18 read tools cover journeys, stays, expenses, summaries, residency status, Schengen status, current country, gap detection and the methodology; 13 write tools cover logging, updating and deleting. Day counting spans 180+ countries with timezone data for 140,000+ cities, so a late-night flight that lands the next day is counted as one day or two the way the rules say.

## Installation

```bash
claude mcp add tripledger --transport http https://my.tripledger.app/mcp
```

Claude web and desktop use Settings, Connectors, Add custom connector with the same URL; any MCP client that accepts a remote server works the same way. The vendor publishes per-client setup snippets on the listing and at tripledger.app.

## Configuration

```json
{
  "mcpServers": {
    "tripledger": {
      "type": "http",
      "url": "https://my.tripledger.app/mcp"
    }
  }
}
```

First connect opens the browser sign-in (OAuth 2.1); an API key works for scripted clients. The two scopes are `ledger:read` and `ledger:write`, and read access stays available even when writes are not granted.

## Business Relevance

- **Founders and consultants who travel** get a defensible day count per country for tax-residency reviews, from their own records
- **Frequent Europe visitors** see when they must leave to stay inside the Schengen 90/180 window, and can check a planned trip before booking
- **Second-home owners and snowbirds** keep one continuous history instead of reconstructing years from calendars at tax time
- **Accountants' clients** can hand over a complete travel record with gaps flagged before it is reconstructed from memory

## Integration with CorpusIQ

TripLedger covers a record the usual business stack does not hold: where the operator physically was. CorpusIQ answers questions from connected sources such as Gmail, Calendar and Drive, and the Gmail connector can supply the booking emails that TripLedger logs as trips - the same source that already feeds document questions.

Used together: ask CorpusIQ for the business view (spend on travel from connected accounting, meeting load from calendar) and ask TripLedger for the compliance view (days per country, Schengen headroom, next exit date). The counts stay in TripLedger as the source of record; CorpusIQ remains the place the rest of the business question is answered alongside.

## Limitations

- Brand new - no track record yet (registry v1.0.0)
- One-time paid licence after the trial ($97 per ledger); some household and cost features sit in Pro
- Personal-scale ledger, not corporate travel management or booking
- Write tools require the OAuth grant; counts come from your own entries, not from immigration or tax authorities
- Day counts are informational - not tax or legal advice

## FAQ

### Does it handle multiple countries and counting methods?

Yes. It tracks residency for 180+ countries with both the Any Presence and Midnight Rule methods built in, switched per country to match local tax rules, plus rolling Schengen totals for all 29 Schengen countries in one place.

### Where do the records come from?

Your own entries: quick trip logs, stays and expenses, including logging from booking emails. Gap detection flags missing days so the history stays complete. Totals are computed from your records with a documented methodology.

### What does it cost?

A 14-day free trial, then a one-time $97 lifetime licence per ledger - no subscription. Pro adds household and cost tracking for partners and family.

### What can an agent actually do with it?

Read tools answer residency, Schengen, current-country and gap questions; write tools log, update and delete journeys, stays and expenses. Both run behind OAuth 2.1 with scoped consent (`ledger:read`, `ledger:write`).

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/) - all catalogued business-relevant servers
