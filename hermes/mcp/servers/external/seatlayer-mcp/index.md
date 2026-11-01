---
title: "SeatLayer MCP - Seating Charts Built by an Agent"
description: "Venue seating charts and reserved-seat ticketing as agent tools. Build from a description, price it, publish on human approval, then run the live event."
category: Operations
stars: n/a (commercial platform, no public repo)
added: 2026-11-01
source: "The chatmcp/mcpso submission issue #6534 filed on 2026-11-01 at 09:45:20Z; a measured 401 on https://mcp.seatlayer.io/mcp; a keyless JSON-RPC initialize, tools/list, product_overview, pricing and capabilities on https://docs.seatlayer.io/mcp; and Markdown reads of the SeatLayer MCP guide, the connect page and the documentation index"
relevance: ★★★
tags: [ticketing, seating-charts, venues, events, venue-designer, oauth, human-approval, remote-mcp, streamable-http]
last_updated: "2026-11-01"
---

# SeatLayer MCP

**A seating chart is the one business document where an agent's mistake is public: a wrong price shows at checkout, a blocked seat shows at the door. SeatLayer exposes the chart, the event and the prices as 63 tools behind an OAuth grant that a human approves per capability, and it publishes a keyless read-only server so the first question can be answered before anyone connects anything.**

```
Server type: Remote (Streamable HTTP), two servers
Endpoint:    https://mcp.seatlayer.io/mcp          (OAuth 2.1, 63 tools)
             https://docs.seatlayer.io/mcp         (public, read-only, 11 tools)
Auth:        OAuth with PKCE and dynamic client registration, per-administrator consent
Tools:       63 in the build toolset, 11 on the public knowledge server
Pricing:     $0 to start, 100 free sold-seat credits a month, then prepaid credits
Category:    Operations / ticketing and venues
Built by:    SeatLayer (seatlayer.io)
```

## What it does

SeatLayer is seating chart software and reserved-seat ticketing on one account. A chart is venue geometry, sections, rows, seats, tables, booths and standing areas, reused across events, with event-specific free, held, sold and blocked inventory. The MCP server lets an agent build that chart from a description or a floor plan image, price it, validate it, preview it on desktop and mobile, and publish it, then run the event on it: open and close sections, block and release seats, change prices and releases, work sales channels, read orders and reports.

The boundary is written into the product rather than left to the prompt. The agent cannot sell a seat, cannot hold one for a buyer, and cannot refund or charge anyone: a refund is a request an administrator approves in Orders. Chart changes stay reviewable revisions, publication stays a human action, and an agent's publish can be undone in one click.

## What this pass measured

Two servers, and the split between them is the practical story.

`https://mcp.seatlayer.io/mcp` answered a keyless `initialize` with **HTTP 401** in 0.28 seconds and the body `{"error":"unauthorized","code":"bad_designer_session"}`, which is the normal state for an OAuth-only surface: live, and closed without a grant.

`https://docs.seatlayer.io/mcp` is the second server, and it answered **HTTP 200** keyless with `serverInfo` name `seatlayer-knowledge` at version **0.109.1**, **11** tools, and instructions that tell a client to call `product_overview` first and to quote the canonical URLs each result returns. Three calls were made in 0.06 to 0.08 seconds each.

`product_overview` returned the product in its own words, including the split between the two doors: Hosted Ticketing, where buyers pay into the organizer's own payment account at **$0.50** per confirmed ticket, and the Platform SDK, where a platform keeps its own checkout and embeds the seating engine, live at **$0** with **100** free confirmed-sold-seat credits per organization each month and prepaid credits from **$0.10**. It also records the scale claim as fixtures rather than adjectives: public demos at a **200,000** seat stadium and a **100,000** seat arena, and a readiness observation dated **2026-09-14** on a **53,018** seat chart.

`pricing` returned the meter and the ladder: one prepaid credit per confirmed sold seat, designing, rendering, browsing, temporary holds, releases and unsold inventory consume nothing, the first production payment is **$0**, purchased credits do not expire, and the ladder runs **500** credits at **$50** (**10** cents a seat) down to **100,000** at **$5,000** (**5** cents), with no subscription and no minimum. Hosted ticket sales are a separate wallet at **$0.50** per confirmed ticket. Enterprise terms begin above **100,000** sold seats a month.

`capabilities`, reviewed **2026-09-27**, separates what is released from what is not, in the vendor's own matrix, which is the single most useful result for anyone deciding whether the agent path covers their event: released seating, released managed ticketing across 14 payment gateways, buyer 3D released and optional with a 2D fallback, **51** starting templates with **35** carrying 3D relief, and SDKs across web, seven server languages, four mobile platforms and a REST OpenAPI 3.1 surface.

The OAuth designer surface is documented rather than driven here: **63** tools in the `?tools=build` toolset, `?tools=build,trace` to add floor-plan tracing, `?tools=events` for live events, each toolset carrying less than half the definitions of the full set on every turn.

## Why This Matters for Operators

**Ticketing is one of the few small-business systems where an agent's error is measured in customers standing in a doorway.** That is why the consent screen is the feature, not the tool count.

Three mechanisms carry the design:

- The grant is per capability, not per application. An administrator ticks manage live events, create and run events, set prices and releases, manage sales channels, look after orders, read reports or change seat categories, and can narrow the whole grant to one chart instead of a workspace. Every call that uses one of the event capabilities re-checks that the person who connected the agent still holds a role that allows it in the dashboard.
- Writing to an event on sale takes a plan first. The agent shows the plan and waits for a yes, a yes covers that plan only, and if the seats change first it plans again.
- Publishing a chart needs approval of a review, history names the agent, an administrator gets one email about agent changes at most every 15 minutes per agent, and a publish can be undone in one click.

## Tools & Capabilities

The 63 designer tools group by area, per the vendor's own guide:

| Area | What the agent can do |
|---|---|
| Chart building | Sections, rows, seats, tables, booths, GA areas, floors, zones, text, shapes, categories and theme |
| Tracing | Build a chart from a reference image with confirmed counts and labels (`?tools=build,trace`) |
| Validation and preview | Validate the chart, render buyer previews on desktop and mobile, 3D structure and sightline scores |
| Review and publish | Submit a revision for review, and publish only an approved revision |
| Event configuration | Create, review and publish configurations, and bind them to an event |
| Event setup | Create, edit and duplicate events, open, close and reopen sales, archive and delete |
| Live controls | Block and reserve seats, hide or open sections, change seat categories, move an event to the latest chart |
| Prices and releases | Event prices, ticket releases, when sections go on sale, checkout hold time, how tables sell |
| Sales channels | Allocations, channel prices and sale routes, pause and archive, buyer links, partner report links |
| Orders | Find and read orders, resend tickets, ask an admin to refund or cancel |
| Reports | Sales, money, door counts and the event log |

The public knowledge server's 11 tools are a different job: `product_overview`, `compare_with`, `why_seatlayer`, `pricing`, `capabilities`, `renderer_evidence`, `search_docs`, `get_page`, `sdks`, `faq` and `chart_types`. Every result carries a `sources` array of canonical URLs with the date each claim was verified, which makes it the rare vendor surface that expects to be quoted with a citation.

## Installation

```bash
claude mcp add --transport http seatlayer https://mcp.seatlayer.io/mcp
```

For chat hosts such as Claude and ChatGPT, narrow the toolset on the URL:

```
https://mcp.seatlayer.io/mcp?tools=build
https://mcp.seatlayer.io/mcp?tools=build,trace
https://mcp.seatlayer.io/mcp?tools=events
```

The read-only knowledge server needs no account:

```
https://docs.seatlayer.io/mcp
```

## Configuration

The administrator approves each connection on a consent screen. Choose one chart or the workspace, tick the capabilities, then sign the client in. Tokens expire hourly and refresh on their own. Do not paste a SeatLayer secret key into a client: this connector takes OAuth only, and the vendor says so explicitly.

A safe first prompt, from the vendor's own guide, is to call `get_capabilities`, name the chart or workspace that is authorized, and summarize the chart without changing anything. If the answer names a chart you did not approve, disconnect and reconnect.

## Business Relevance

The commercial shape is unusual for a vertical SaaS and it is worth stating plainly: the Platform door has no subscription, starts at **$0**, gives **100** sold-seat credits a month and sells credits that never expire, and the Hosted door charges **$0.50** per confirmed ticket with the money landing in the organizer's own gateway. Nothing here is priced per agent or per AI feature.

That means an operator can test the agent path on one real event without a platform decision. If the chart builds and the prices hold, the cost of the exercise is a credit balance; if it does not, the loss is a chart revision.

## Integration with CorpusIQ

The two answer different questions and they meet at the report. SeatLayer knows what sold, at what price, through which channel, and how many came through the door; CorpusIQ reads the systems around it, the payment processor, the ad account, the inbox, and answers why a number moved. A promoter asking which channel actually filled the room needs the SeatLayer report joined to spend, and that join is the part neither surface does alone.

The containment holds on both sides: SeatLayer grants the agent no payment authority, and CorpusIQ reads without writing.

## Limitations

- The OAuth surface was measured only to its 401. No grant exists, so all **63** tools are the vendor's documentation rather than a driven list, and the 63 count itself was not returned by a `tools/list`.
- Chart building, tracing, validation, publishing and every live event control are unexercised.
- The pricing ladder, the free credit allowance and the **$0.50** hosted rate were read from the vendor's own MCP server, which is an authoritative statement of list price but not an invoice.
- The **200,000** and **100,000** seat demos and the **53,018** seat readiness observation are the vendor's fixtures; nothing here loaded them.
- The capability matrix is dated **2026-09-27**, so anything shipped after that date is outside what this pass read.
- `compare_with` and `renderer_evidence` were not called, so the competitive and performance claims are unread.

## FAQ

### Can an agent sell tickets through this connector?

No. Selling stays with the Server API and your checkout. The connector builds and publishes the map buyers use and can run the event, but it cannot sell a seat, hold one for a buyer, or charge anyone.

### Is there a free way to test it?

Yes, two. The public knowledge server at `https://docs.seatlayer.io/mcp` is keyless and read-only, and the Platform door starts at `$0` with **100** confirmed-sold-seat credits per organization each month.

### What happens if the agent changes a chart that is already on sale?

It has to show a plan first and wait for a yes, and that yes covers that plan only. If the inventory changed in the meantime it plans again, held and sold seats never change, and an administrator gets a digest of agent changes at most every 15 minutes.

### Does it work only with Claude?

The vendor documents connection guides for Claude, ChatGPT and Codex, and the server is a standard remote MCP endpoint reachable from any Streamable HTTP client.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [MCP Server Discovery Sweeps](/hermes/mcp/sweeps/)
