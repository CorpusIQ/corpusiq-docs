---
title: "Shenton Brokers MCP - Singapore Insurance Prices in Chat"
description: "Twelve Singapore insurance lines priced live in S$ through fourteen tools, with a buy link per plan and the broker commission stated on every quote."
category: "Business Operations"
stars: n/a (vendor-hosted)
added: 2026-11-21
source: "chatmcp/mcpso submission #7747 filed 2026-11-21T05:23:31Z; the official MCP registry record com.shentonbrokers/quotes 1.0.0 published 2026-11-20T09:55:49Z; keyless initialize and tools/list, then nine tools/call requests on 2026-11-21"
relevance: ★★★★
tags: [insurance, singapore, quotes, travel, property, finance, remote-mcp, keyless]
last_updated: "2026-11-21"
---

# Shenton Brokers MCP

**Remote MCP server (Streamable HTTP, no authentication)** - Singapore insurance prices from a broker regulated by the Monetary Authority of Singapore. An agent asks for a quote in plain answers and gets back every featured insurer's plan, its price in Singapore dollars with GST, the date that price was last checked, the cover lines, and a buy link for the plan the buyer picks.

```
Server type: Remote (Streamable HTTP, stateless entry, no auth)
Endpoint:    https://shentonbrokers.com/mcp
Tools:       14 (12 quote tools, explain_product, create_buy_link)
Registry:    com.shentonbrokers/quotes 1.0.0, published 2026-11-20T09:55:49Z
Docs:        https://shentonbrokers.com/developers  (OpenAPI 3.1 at /api/v1/openapi.json)
Products:    travel, maid, car, motorcycle, home, personal accident, pet,
             personal cyber, overseas student, golf, bicycle, HDB fire
Quote state: a quoteId, quoted back by create_buy_link
```

## Why This Matters for Operators

Most "insurance" tools for agents return a marketplace listing or an affiliate table. This one returns a priced quote per insurer, and it does the two things an operator actually needs before a decision: it states the ranking rule, and it states who gets paid.

Two lines appear on every priced answer:

> Plans are listed by price, lowest first. At the same price the order is by insurer name. The order is not advice to buy any plan.

> Shenton Insurance Brokers is a registered insurance broker regulated by the Monetary Authority of Singapore. The insurer pays us commission when you buy through us. We charge the buyer no fee.

An agent can therefore hand a person a comparison without pretending to be an adviser, and the conflict of interest ships inside the payload instead of a footer somewhere.

## Measured Behaviour

Four quotes were driven on 2026-11-21, all keyless, every figure quoted from the response:

| Call | Answers given | Plans returned | Cheapest plan |
|---|---|---|---|
| `get_travel_quote` | Japan, 7 days, 2 adults | 49 | Income FlexiTravel Plus, **S$42** |
| `get_car_quote` | Toyota Corolla Altis 1.6, 5 years old, driver 35, 10 years licensed, NCD 30% | 22 | India International, **S$718.84** |
| `get_home_quote` | HDB flat, owner, S$60,000 contents | 29 | Sompo HomeVital, **S$67.85** |
| `get_pa_quote` | For myself, teacher, S$100,000 sum insured | 64 | UOI UniPA Value, **S$120.07** |

Every plan carries its own `priceCheckedOn` date, and they differ: the four cheapest plans above were last checked on 2026-11-21, 2026-11-20, 2026-11-20 and 2026-10-11. The travel quote listed UOI at S$47.60 with a 2026-10-19 date beside an Income plan checked the same morning. That is a staleness signal per plan, not per product, which is why the guide quotes the date next to every price instead of calling the whole table fresh.

The response also echoes how it read each answer, and it hedges the assumptions out loud:

```text
Destination (countries): Japan
Trip type (tripType): Single trip
Departure date (departDate): 2026-12-21
Return date (returnDate): 2026-12-27
COVID-19 cover (covid): Included (assumed: not given)
Going on a cruise (cruise): No (assumed: not given)
Japan read as JP.
7 read as a 7-day trip, 2026-12-21 to 2026-12-27.
```

Nothing silently defaults. The car quote turned `age: 35` into a date of birth of 1991-11-21 in its `notes` and said so, and every assumed field is marked `(assumed: not given)`.

## What a Wrong Answer Looks Like

`create_buy_link` with the travel quote `SB-WKN6MU` and plan `1` returned a live link and the commission line again:

```text
buyLink: https://shentonbrokers.com/go/q/SB-WKN6MU/1
reference: SB-WKN6MU-1
insurer: Income
priceSgd: 42
```

That link answers **HTTP 200**.

Validation is in band and readable. A destination of `Atlantis` returns `status: "problems"` with the reason rather than a quote, and a car registered three years in the future returns the same shape, so an agent can retry with a corrected answer instead of rendering an empty list. `explain_product` refuses anything outside its twelve-product enum with a one-line message naming the schema.

## Where It Stops

- **One country.** Prices are Singapore, in SGD, with HDB fire cover, Ministry of Manpower maid requirements and Monetary Authority of Singapore regulation. The product explanations are written for that market.
- **Quotes, not policies.** No claims, no endorsement, no renewal on an existing policy. The insurer takes payment and issues the policy through the broker's link.
- **A quoteId is the only state.** The server issues no session id on initialize; the quote itself is held server side behind `quoteId`, which is what `create_buy_link` reads. How long a quoteId stays resolvable was not tested on this pass.
- **An insurer can decline.** A plan that does not take the car, or the driver, is listed as declined with no price, and the instruction is to say "refer to insurer".
- **Twelve products, nothing bespoke.** No marine, no commercial property, no group employee benefits.

### How should an agent present the prices?

Give the plan, the insurer, the price with GST, and the `priceCheckedOn` date. Show the ranking rule and the commission disclosure from the response verbatim. Do not add a recommendation the payload does not make, because every priced answer says explicitly that the order is not advice.

### Does it need a key or an account?

No. `initialize` and `tools/list` answer 200 without a token, and all four quotes above were produced with no credential and no cookie. A buyer only meets an account when they follow a buy link to an insurer's checkout.

### Can it price a whole household in one call?

One product per call. The personal accident tool takes `who` (myself, couple, parent, family, children) and a spouse occupation, and the travel tool takes adult and child counts, but a car plus a home plus travel is three calls, each with its own quoteId.

## Catalogue Position

Insurance quotes already had one owner in this catalogue: **Quotor**, a Texas home and auto surface held as a catalogue row rather than a guide. Shenton is the second, and it earns its own slot on the envelope rather than on the category, because the jurisdiction, the currency, the product set, the disclosure regime and the quote lifecycle are all Singapore specific. It is the first entry here that prices twelve personal lines from one endpoint and returns the commission line inside the answer.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [MCP Server Discovery - November 21, 2026 (Night)](/hermes/mcp/sweeps/sweep-november21-2026-night)
