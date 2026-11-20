---
title: "Reevi MCP - Buyers Who Already Import Your Product"
description: "A keyless tool that names importers for a product and market from trade records and the public web, graded A to C, with a shared report link."
category: "Trade / B2B Prospecting"
stars: "n/a (hosted vendor endpoint; no public repository)"
added: 2026-11-19
source: "the mcpservers.org sitemap map servers/12 (restamped 2026-11-19T18:10Z onward), the official MCP registry record ai.reevi/find-buyers 1.0.0 published 2026-11-17T15:21:45Z, a keyless initialize and full tools/list on 2026-11-19, one driven find_buyers call that returned twelve buyers in 23.1 seconds, one schema refusal, and the report link and two of the returned buyer sites fetched to HTTP 200"
relevance: ★★★
tags: [export, importers, b2b-prospecting, buyers, customs-records, lead-generation, trade-data, remote, keyless, no-auth, free-tier]
last_updated: "2026-11-19"
---

# Reevi MCP

**An exporter's hardest question is not who could buy the product. It is who already does. This server answers that for one product and up to five countries in under half a minute, free, with no key.**

Reevi is a buyer-discovery product for exporters and manufacturers. Its MCP endpoint is deliberately small: one tool, one question, twelve graded answers and a link to a saved report. Nothing in this catalog answered "who already imports this" before this pass, which is why the entry exists rather than a hold.

```text
Server type:   remote Streamable HTTP, stateless (no Mcp-Session-Id issued)
Endpoint:      https://reevi.ai/mcp
Server:        reevi 1.0.0, protocol 2025-06-18
Registry:      ai.reevi/find-buyers 1.0.0, published 2026-11-17T15:21:45Z
Vendor page:   https://reevi.ai/find-buyers (HTTP 200, 156,157 bytes)
Auth:          none for the search. Contacts and introductions need a free reevi.ai account
Tools:         1 (find_buyers), keyless
Free tier:     5 searches a day per connection, counted by the server
```

## What the server says about itself

The `initialize` response explains the boundary before the tool is called, which is where the boundary belongs:

> Reevi finds companies that already buy a product, for exporters and manufacturers. Call find_buyers with the product and target countries. Share the report link with the user: contacts and introductions are on reevi.ai and need a free account.

So the agent gets the research and the human gets the contacts. That split is honest, and it is the reason the free tier exists at all.

## The one tool, and its whole schema

`find_buyers` takes more shaping than a marketing snippet suggests:

| Argument | Constraint | Effect |
|---|---|---|
| `product` | 2 to 300 characters | what the exporter sells, in plain words inside the search |
| `target_markets` | max 5, full English country names | defaults to the United States, the United Kingdom and Germany |
| `company_name` | max 200 | the exporter itself, which improves the fit grade |
| `company_website` | max 200 | read for product evidence |
| `company_country` | max 80 | buyers in that country are excluded |
| `customer_types` | enum: retailers, wholesalers_distributors, brands, direct_b2b | narrows to the buyer class that fits the channel |
| `exclude_domains` | array | known competitors and existing accounts |

The output is a text block plus a structured `buyers` array carrying `name`, `website`, `country`, `fit` (A, B or C) and `fitScore` on a 0 to 100 scale with a one-sentence `reason` per company.

## A run, measured

The call that produced this guide:

```json
{"product": "stainless steel kitchen sinks",
 "target_markets": ["Germany", "United States"],
 "company_country": "India",
 "customer_types": ["wholesalers_distributors"],
 "company_name": "Test Exporter"}
```

Result in **23.1 seconds** (the card promises 30 to 75):

```text
Found 12 buyers in United States, Germany.
Customs records show about 2,388 importers of this product in these markets.

Allora (allorausa.com)      United States  fit A  92
AAA Distributor             United States  fit A  88
Amerisink (amerisink.com)   United States  fit A  86
HamatUSA                    United States  fit A  82
Houzer                      United States  fit A  80
Spuelenprofi (spuelenprofi.de)      Germany  fit B
Spuelenhandel                        Germany  fit B
SHK Shop                             Germany  fit B
XXLgastro (xxlgastro.de)             Germany  fit B
Global Industrial           United States  fit B
Hygiene Shop (hygiene-shop.eu)       Germany  fit B
ascobloc Gastro-Geraetebau (ascobloc.de) Germany fit B
```

Four things are worth checking in that block rather than trusting:

- The exporter's own country was stated as India and no Indian company appears, which is the documented exclusion working.
- The channels asked for were wholesalers and distributors, and the reasons read like distributors and trade counters rather than retail shelves.
- The count and the list disagree by design: **2,388 importers in the market** is the pool the search drew from, and **12** is what the fit model chose to show.
- Two returned companies were opened to confirm they exist as described: **allorausa.com** (HTTP 200, 592,264 bytes) and **amerisink.com** (HTTP 200, 207,510 bytes), both kitchen-sink wholesale.

The call also decremented the quota aloud: *Free searches left today from this connection: 4*, after starting at 5. The counter is per connection, so a second agent on the same endpoint draws from the same allowance.

## The report link is real

Every search returns a saved report URL. The one from this run, `https://reevi.ai/r/cmwogh5uw0pjkle017agwrpbn`, was fetched directly: **HTTP 200, 108,134 bytes**, no sign-in. It carries the buyer list, the reasons and the call to unlock contacts, so an agent can hand a human a link instead of a wall of text, and the researched company stays the same object on both sides.

## The refusal, and what it teaches

A one-character product is refused in-band rather than by schema violation:

```json
{"isError": true, "content": [{"type": "text",
 "text": "product is required: describe what the exporter sells in a few words."}]}
```

An error that names the fix is a better product than a schema throw, and it costs the caller nothing from the daily allowance.

## Limits, as the vendor states them and as measured

- **Contacts are behind an account.** The tool returns companies, websites and fit reasons; the named person, the e-mail and the introduction happen on reevi.ai after a free sign-up. An agent that promises contacts from the tool has over-claimed.
- **Introductions are human-approved.** The vendor states that Reevi finds the right person at each buyer and sends the introductions the exporter approves, by e-mail or on WhatsApp, so this is not an autonomous outreach channel.
- **Five searches a day per connection**, enforced server-side and disclosed in the response text.
- **Two markets or five, one call.** The schema caps `target_markets` at five, so a ten-country push is two searches and two reports.
- **Fit grades are a model, not a purchase order.** A, B and C with a score and a sentence are a prioritisation. The customs-derived pool behind them is the vendor's own figure (2,388 in this run) and is not exposed as a table.
- **No write surface at all.** Nothing on this server changes anything, which makes it safe to leave enabled for an agent that runs unattended.

## Add it to Hermes

```bash
hermes mcp add reevi --url https://reevi.ai/mcp
hermes mcp test reevi
```

Then ask the question it exists for: *find distributors that already import stainless steel sinks in Germany and the United States, we manufacture in India.* The report link that comes back is the deliverable; the sign-up is where the human decides whether the introduction is worth making.

## Why it earns a slot

The catalog stocks prospecting tools that score companies against an ideal customer profile. This one starts from a different fact: a company that already imports the product has already made the decision to buy it from abroad. For a manufacturer or an exporter, that is a warmer list than any firmographic filter, and it costs nothing to ask.
