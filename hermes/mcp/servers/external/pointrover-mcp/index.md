---
title: "PointRover MCP - The Supply Chain Board for One Business"
description: "Builds a per-business board of what moves upstream of a small business, with an official receipt on every figure."
category: Supply Chain & Market Intelligence
stars: n/a (vendor-hosted; no public repository)
added: 2026-11-07
source: "The mcpservers.org twelve-sitemap addition `pointrover-com-docs` in the November 7 evening window; the official MCP registry record `com.pointrover/pointrover` active on four published versions 2026.10.31 to 2026.11.6 with the remote `https://pointrover.com/mcp`; the vendor's own guide at pointrover.com/docs; and the endpoint itself, where a keyless initialize answered 401 and the protected-resource document it named answered 200"
relevance: ★★★★
tags: [supply-chain, input-prices, tariffs, local-market, wage-data, permits, business-records, oauth, remote-mcp]
last_updated: "2026-11-07"
---

# PointRover MCP

**Every accounting system answers the same question: what already happened. The question an owner actually loses money on is the one that has not reached the books yet, because what they buy, what they pay, the duties on what they import and the rules they answer to all move upstream first, by weeks or by months.** PointRover is built for that gap and only that gap: name one business, and it assembles a board of the official records that touch it.

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://pointrover.com/mcp
Auth:        OAuth 2.1, authorization code with PKCE and dynamic client registration
Scope:       read:tenant (the only scope advertised)
Tenancy:     one connection reads one business
Tools:       9, all read-only
Refresh:     board rebuilt as figures publish, checked every 12 hours
Price:       $79 per business per month after a 14-day trial
```

## What the endpoint says about itself

A keyless `initialize` on `https://pointrover.com/mcp` answers **401** with a pointed error rather than a bare refusal:

```json
{"error":"invalid_token",
 "error_description":"Sign in to PointRover in your MCP client to use this tool. This endpoint takes an OAuth 2.1 access token issued by https://pointrover.com. Discover how to obtain one at https://pointrover.com/.well-known/oauth-protected-resource/mcp"}
```

That discovery document answers **200**:

```json
{"resource":"https://pointrover.com/mcp",
 "authorization_servers":["https://pointrover.com"],
 "scopes_supported":["read:tenant"],
 "bearer_methods_supported":["header"],
 "jwks_uri":"https://pointrover.com/oauth/jwks"}
```

One scope, read-only, and the tenant is the unit. There is no write path to misuse and no catalogue-wide read: a connection is approved for one business, so an agency running ten clients approves ten connections rather than one credential that can see everything.

## The nine tools

Every tool reads. The vendor documents all nine, with parameters and examples, in its own guide.

| Tool | What it returns |
| --- | --- |
| `whoami` | Which business the connection reads, whether its figures are ready, and the industry, decided or still provisional |
| `pointrover_brief` | One summary: what moves upstream of what the business buys, open tariff alerts, events reaching it, rules with a date coming up |
| `pointrover_changes_since` | What moved since a `board_version` or a check id: newly published figures, and recalls, storms or trade actions that opened, changed or ended |
| `pointrover_events` | Recalls, weather alerts, disaster declarations and trade actions at the business's locations or on what it buys, in the publisher's words, scored for how closely they touch it |
| `search` | Inputs, published index series, tariffs, wages, locations, rules and events matching a few words, `limit` 1 to 25, scoped `business`, `industry` or `all` |
| `fetch` | One record by id |
| `pointrover_series` | A published index series over time |
| `pointrover_receipt` | The source record behind a single figure |
| `pointrover_graph` | Walk the links between a business, its inputs and the records behind them |

Three of those are what separate this from a search box. `pointrover_changes_since` makes the board incremental, so a returning agent asks what moved instead of re-reading everything. `pointrover_receipt` returns the record behind a number, which is the difference between a figure an owner can act on and one they have to double-check. `pointrover_events` filters on `min_exposure`, `min_coverage`, `min_weight` and `kinds`, so "a storm" becomes "a storm within reach of two of your three sites".

## What is actually on the board

The coverage is stated as six surfaces, each tied to a decision an owner makes:

- **Inputs and what is upstream of them.** How far the materials, food, fuel and parts a business buys have moved over twelve months, whether the move is unusual, and how much of it reaches the business and when. The framed example is an auto shop still pricing an oil-change special on last quarter's oil cost while refined petroleum is up 60.7 percent and lubricating oil only 15.4 percent, with history showing the rest of the gap still in transit to the supplier's sheet.
- **Duties on what it imports.** Import duty by product and country, Section 232 and Section 301 included, with the date each took effect.
- **Permits, licences and rules.** Federal and state regulations for that kind of business in that state, OSHA and EPA requirements, licences to hold, filings with a date on them, each in the regulator's own words.
- **What the work pays.** Average wage for a role in the owner's own town rather than the national figure, minimum wage at each location, and how employment in the trade swings through the year.
- **The local market.** Who lives around each place and who works there in the daytime, by age and income bracket, how far customers travel, the trade's own index, and how many businesses like it operate in the county and what they sell.
- **Disruption at the door.** Recalls on products sold or used, weather watches, warnings and disaster declarations at the locations, and trade actions on imports, each tied to the part of the business it touches.

## Why it is not a duplicate of the tariff entries

The catalog carries [Tariff Monitor](/hermes/mcp/servers/external/tariff-monitor-mcp/) and a procurement entry, and neither is this. Tariff Monitor is a local stdio calculator: you give it an HTS code and a country of origin, it stacks MFN, Section 301 and 232 and returns the duty rate and the annual exposure. PointRover is the opposite shape. It is a hosted, per-business state whose job is to decide which inputs, duties, rules and events apply to one business, keep that mapping current, and hand the agent a receipt for each. A duty calculator answers "what is the rate on heading 6404.11"; PointRover answers "the duty on what this shop imports changed last month, here is the Federal Register record, and here is what it costs you".

## Limits worth writing down

- **A snapshot every twelve hours, not a live feed.** Figures are refreshed as new releases publish and the board is checked every twelve hours, so an intraday move is not visible until the next check.
- **No published tool count on the site to reconcile against.** The nine tools come from the vendor's own documentation, not from a keyless `tools/list`, which the endpoint refuses.
- **One business per connection.** Useful for an agency, awkward for an assistant being asked about a second client in the same conversation.
- **No writes and no exports.** It is a read surface; the model still drafts the decision, and the owner still makes it.
- **The trial needs a card at checkout**, stated on the pricing page, so the free path is fourteen days rather than a keyless tier.

## Pricing, read off the page

**$79 per business per month**, after a **14-day trial** that charges nothing until it ends. From the third business the rate drops to **$59 each**, and from the tenth to **$49 each**. No setup fee and no platform fee. The board is built in about an hour after the business name and address are entered, which is the real gate: the connection is useless until the board exists.

## Frequently asked questions

### What does PointRover MCP cost?

**$79** per business per month after a **14-day** trial that takes a card at checkout. From the third business the rate is **$59** each and from the tenth **$49** each, with no setup or platform fee.

### Does PointRover need an API key?

No. It uses OAuth 2.1 with the authorization code flow, PKCE and dynamic client registration, and the only scope it advertises is `read:tenant`, so there is nothing to paste into a client and nothing to paste into a chat.

### How current is the board?

The board is refreshed as new figures publish and checked every **twelve hours**, and `pointrover_changes_since` takes a `board_version` from an earlier answer so a returning agent reads only what moved.

### Can one connection read several businesses?

No. A connection is approved for one business, which is the tenancy boundary; an agency approves one connection per client.
