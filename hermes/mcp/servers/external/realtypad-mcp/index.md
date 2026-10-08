---
title: "RealtyPad MCP - Real Estate Deal Research for Agents"
description: "Real-estate deal research for investors: listings in, researched deal file out - comps, rent, taxes, scenarios - plus pipeline and matching."
category: Finance
stars: n/a (new listing)
added: 2026-10-07
source: "mcpservers.org /all page 1 (Oct 7, 2026 evening sweep)"
relevance: ★★
tags: [real-estate, deal-research, comps, underwriting, investors]
---

# RealtyPad MCP

**Hosted MCP server that turns your agent into a deal analyst** - give it a listing and it returns a researched deal file: comps, rent, taxes, market trends and cashflow scenarios, written into the same workspace you use in the browser.

```
Server type: Remote (Streamable HTTP at https://app.realtypad.ai/mcp)
Auth: Account sign-in (30-day trial on your first workspace)
Docs: https://realtypad.ai/mcp
Clients: Claude, ChatGPT, Cursor and any Streamable HTTP client
Category: Finance
Built by: RealtyPad
```

## Why This Matters for Operators

Deal research is where small real-estate investors lose their weekends: pull the listing, hunt comps, guess the rent, rebuild the same spreadsheet, then do it again for the next address. RealtyPad keeps one deal file per property - address, ask, photos and listing copy - and gives your agent built-in tools to fill it: public listing sites, HUD and auction inventory and distressed-property records where available, or any URL or address you already have. If the listing is already in the workspace, the record updates instead of duplicating. The numbers your agent reads and writes are the same numbers the browser shows.

## Tools & Capabilities

| Area | What the agent can do |
|---|---|
| Find and research deals | search public listing sites, HUD and auction inventory and distressed records; paste a URL or address; write results into one deal file |
| Scoring | update deal scores from chat |
| Scenarios | run scenarios and hold projections |
| Matching | match deals and reply to investors |
| Evidence | manage comps and appraisal history |
| Trends | read and refresh market trends |
| Notes | attach observations and comments |

## Installation

Add the connector URL to the client you already use:

```json
{
  "mcpServers": {
    "RealtyPad": { "url": "https://app.realtypad.ai/mcp" }
  }
}
```

ChatGPT: Settings, then Apps, then Developer mode, then create a connector with the same URL. Cursor and Claude work with the JSON above.

## Business Relevance

- **Investors and small funds:** turn a paste-in listing into a researched file with comps, rent, taxes, trends and cashflow scenarios before deciding where to spend diligence time.
- **Realtors and brokers:** keep every deal, comp and appraisal in one pipeline your assistant can read and update.
- **Teams:** buyer matching and investor replies from the same workspace, with observations and comments attached to the record.

## Integration with CorpusIQ

CorpusIQ reads the rest of the business - banking, accounting, CRM and analytics - and keeps those answers consistent across AI clients. RealtyPad handles the deal side: check your cash position and portfolio numbers through CorpusIQ, then size the next deal in RealtyPad in the same conversation.

## Limitations

- An account is required (30-day trial on your first workspace); every number lives in your RealtyPad workspace, not in the chat.
- Discovery tools focus on public listing sites and government inventory (HUD, auctions, distressed records) where available; coverage varies by market.
- Deal research output is a starting file to verify, not an appraisal.

## FAQ

### Does it duplicate deals I already have?

No - if a listing is already in the workspace, RealtyPad updates the record instead of creating a duplicate.

### What do I need to start?

An account with a 30-day trial on your first workspace, and any MCP client (Claude, ChatGPT, Cursor or another Streamable HTTP client).

### Is this a homebuyer tool?

It is built for deal research: investors, Realtors, brokers and teams working comps, scenarios, pipeline and buyer matching.

### Where does the data come from?

Public listing sites and government inventory (HUD, auctions, distressed-property records where available), plus anything you paste in; all of it lands in the same workspace as the browser app.

## See Also

- [DFX Real Estate Intelligence MCP - US Property, Parcel and Debt Data](/hermes/mcp/servers/external/dfx-real-estate-mcp)
- [UK Land Registry MCP - Sold Price Packs for Agents](/hermes/mcp/servers/external/uk-land-registry-mcp/)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
