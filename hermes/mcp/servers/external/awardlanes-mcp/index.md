---
title: "Awardlanes MCP - USDA Freight Awards by Territory"
description: "Read-only USDA food-purchase award lanes scoped to a freight broker's territory, each result linked to the USDA record."
category: Logistics
stars: "n/a (hosted; OAuth, 14-day trial from the consent screen)"
added: 2026-11-08
source: "chatmcp/mcpso submission #6969 filed 2026-11-09T03:48:57Z; the official MCP registry record com.awardlanes/awardlanes; the connector documentation at awardlanes.com/docs/mcp; and the endpoint itself, where a keyless initialize answered 401 with a protected-resource pointer"
relevance: ★★★
tags: [logistics, freight, usda, government-data, territory, oauth, remote-mcp, read-only]
last_updated: "2026-11-08"
---

# Awardlanes MCP

**A freight broker's day starts by asking which awarded lanes are open in the states they cover. That answer lives in USDA purchase records and in a spreadsheet most brokers rebuild by hand every morning.** awardlanes reads the USDA food-purchase awards, keeps them attached to an account territory of up to three states, and exposes the search, the award and the vendor behind each one as read-only tools.

```text
Server type: Remote (Streamable HTTP)
Endpoint:    https://awardlanes.com/mcp
Auth:        OAuth 2.1, authorization code with PKCE (S256), DCR and Client ID Metadata Documents
Tools:       5, read-only
Registry:    com.awardlanes/awardlanes
Docs:        awardlanes.com/docs/mcp
Trial:       14 days, started from the consent screen
```

## What the endpoint says about itself

A keyless `initialize` answers **401** with a resource pointer rather than a login wall:

```text
www-authenticate: Bearer resource_metadata="https://awardlanes.com/.well-known/oauth-protected-resource/mcp", scope="awardlanes"
```

The JSON-RPC body is a `-32001` with the same message a person sees: sign in to awardlanes to use this connector. That is the tier this entry rests on: **live, gated, documented by the vendor, not driven.**

## The five tools, and what each is for

- `search_lanes` finds USDA award lanes by place, direction, equipment, delivery window, commodity or vendor. The vendor's own example is the whole use case: reefer award lanes from Texas to Oklahoma that are open.
- `get_award` opens one award by its finding id or contract number with every lane detail and the source record.
- `state_summary` summarises the honest totals for the account's territory, plus the visible statistics.
- `vendor_awards` returns one vendor's USDA awards with the published plant contact details.
- `my_account` reports trial or plan status, the territory and the billing link.

## The design decisions worth recording

Two limits are stated by the vendor and both are the right kind of honesty. **Equipment is inferred from the commodity name where USDA does not state it**, which is the sort of derived field that should be labelled and is. And the territory rule is explicit: during the trial and on a paid plan the connector reads the full territory, while after a trial ends without a plan, or for a state outside the account territory, it returns **the same first 20-lane sample** the web page shows, with an upgrade link in the response. A model reading that answer can tell a person the difference between "no lanes" and "not in your plan", which is not true of most gated data endpoints in this catalogue.

Every result links to the USDA record and to the matching awardlanes view, so a broker quoting off it can hand a customer the source rather than a screenshot.

## The class it enters, with the owners named

Freight is already represented here twice, at different points of the workflow. [Plain Freight](/hermes/mcp/servers/external/plainfreight-mcp/) quotes China to US freight keylessly. [SpendQuery](/hermes/mcp/servers/external/spendquery-mcp/) runs query plans over federal award data, USAspending, SAM.gov and the FAR, and returns the SQL beside the answer. awardlanes is neither a quote engine nor a contract search: it is the awarded-lane view a broker lives in, in their own territory, with the USDA notice behind each lane. For a small brokerage that bids USDA food freight, that is the difference between an assistant that can talk about freight and one that can answer today's question.

## Limits, stated as limits

Five tools, one country's agricultural purchase data, and a territory of at most three states, which is a deliberate narrow product rather than a general freight database. Nothing is written back: there is no way to bid, book or update a lane. The trial starts on the consent screen, so connecting is also subscribing to a clock, and a broker should know the 14 days begin there.

## Frequently asked questions

### Which lanes can an assistant see?

The USDA food-purchase award lanes inside the account's territory, up to three states, filtered by place, direction, equipment, delivery window, commodity or vendor. Outside the territory, or after a trial lapses, the same first 20-lane sample is returned with the upgrade path attached.

### Is it read-only?

Yes. All five tools read. There is no booking, no bid and no write path, which makes it safe to leave connected to an assistant that only asks questions.

### How does it get the data?

From USDA purchase awards, with each result linked to the USDA record it came from. Equipment is inferred from the commodity name where the source does not state it, which the vendor labels as an inference rather than a fact.

### Does a small brokerage need a plan?

The trial runs 14 days from the consent screen and reads the full territory. Whether that is enough depends on how many lanes the territory actually carries, which `state_summary` answers before the trial ends.
