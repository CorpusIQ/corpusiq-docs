---
title: "See Sight Tours MCP - Guided Tours With Live Seats"
description: "Eight keyless tools over guided tours in 20 cities: live seats, party totals that expire in minutes, and a checkout link that stops short of payment."
category: "Travel & Hospitality"
stars: n/a (vendor-hosted)
added: 2026-11-21
source: "the mcp.so feed on 2026-11-21 (card stamped 17:12Z); the official MCP registry record com.seesight-tours/booking 1.0.0 published 2026-11-18T00:58:15Z; keyless initialize and tools/list, then seven tools/call requests on 2026-11-21"
relevance: ★★★☆
tags: [travel, tours, booking, availability, commerce, remote-mcp, keyless]
last_updated: "2026-11-21"
---

# See Sight Tours MCP

**Remote MCP server (Streamable HTTP, no authentication)** - a tour operator's own booking surface: search day tours and multi-day trips, read live seats and a priced total for a party, plan an itinerary from a city, and hand the traveller a checkout link that does not pass payment data through the agent.

```
Server type: Remote (Streamable HTTP, no auth)
Endpoint:    https://www.seesight-tours.com/api/mcp
Tools:       8
Registry:    com.seesight-tours/booking 1.0.0
             (active, published 2026-11-18T00:58:15Z)
Server:      see-sight-tours 1.2.0
Coverage:    day and private tours in 20 cities in Canada and the US,
             plus multi-day small-group trips worldwide
```

## Why This Matters for Operators

Travel is where an assistant most often answers with a guess: a price from last season, a tour that no longer runs, a "book here" link that leads to a search page. This server answers from the operator's own inventory, with seats, a party total, an expiry and a handoff link.

- **Live, not cached.** `check_availability` reads seats and prices for a specific date and party and stamps the answer with an expiry, so the number the agent quotes is the number the traveller will see for the next few minutes.
- **A quote the operator will honour.** The response states its own price basis: per-person ticket prices for that departure, taxes and fees as shown at checkout, before any promo code.
- **A checkout link, not a payment.** `get_checkout_link` returns a short-lived URL on seesight-tours.com. The agent never touches card data, and the server says plainly that it cannot see whether a guest paid.

## Tools & Capabilities

Eight tools were listed keyless on 2026-11-21.

| Tool | Required arguments | What it returns |
|---|---|---|
| `search_products` | none (all optional) | matching day tours, private tours and multi-day trips with ids, links and from-prices |
| `get_product` | `id` | full product record: itinerary, hotels, inclusions, exclusions, meeting point, pickup, languages, price options, departures, booking terms |
| `plan_itinerary` | `start_city`, `days` | candidate multi-day trips and day-tour combinations from a starting city |
| `customize_itinerary` | `changes` | a changed multi-day trip and a shareable plan link |
| `check_availability` | `id`, `date`, `adults` | live departures with seats left, party total and a `quote_id` |
| `get_checkout_link` | `quote_id` | a short-lived checkout URL on the operator's own site |
| `get_quote_link` | `id` | a request-a-quote link for trips booked by request |
| `check_checkout_link` | `checkout_url` | whether a link is prepared, expired or invalid |

## Measured Behaviour

Seven `tools/call` requests were driven keyless on 2026-11-21. Every figure is quoted from a response.

| Call | Arguments | Result |
|---|---|---|
| `search_products` | `location: Toronto` | **31** products, from *Best of Toronto Small Group Tour* at **237 CAD** per adult down to a **110 CAD** night tour with a boat ride |
| `search_products` | `location: Nowhereville` | **0** products, stated as *"0 matching See Sight Tours products (page 1)."* with an empty results array rather than an error |
| `get_product` | Niagara Falls from Toronto | **30** structured fields, including day-by-day itinerary, price options, departures and booking terms |
| `check_availability` | that tour, `2026-12-05`, 2 adults | one departure at **07:00 America/Toronto**, **4 seats left**, **726.00 CAD** for the party, expiring **2026-11-21T18:17:13Z** |
| `plan_itinerary` | Toronto, 3 days | three options returned, including *Niagara Falls and Toronto (3 days, Toronto to Toronto)* |
| `get_checkout_link` | the returned `quote_id` | `state: prepared`, a URL on `/checkout/handoff/` expiring **2026-11-21T19:02:18Z** |
| `check_checkout_link` | that URL | *"The checkout link is ready. Whether the guest paid is only visible to them ... and to See Sight Tours support."* |
| `check_checkout_link` | a fabricated URL | *"This is not a See Sight Tours checkout link created by this app."* |
| `get_product` | an unknown id | `NOT_FOUND` with `isError: true`, and the advice to use `search_products` |

### The price that carries its own expiry

`check_availability` returned `total_minor: 72600` with one line item, Adult x2 at 36,300, eight minutes before the same figure would have to be re-read. The party total, the seats left and the expiry arrive together, which is what makes the answer quotable: an agent that repeats the number without the expiry is quoting a number the operator no longer stands behind.

## Installation

No credential, no account, no key.

```json
{"mcpServers":{"see-sight-tours":{"type":"http","url":"https://www.seesight-tours.com/api/mcp"}}}
```

```
claude mcp add see-sight-tours --transport http https://www.seesight-tours.com/api/mcp
```

## Business Relevance

- **Travel and hospitality operators** see how a supplier exposes inventory to agents: live seats, honest expiry, a handoff link and a stated price basis.
- **Agency and concierge workflows** can price a day or a multi-day trip for a specific party without a human opening a booking engine.
- **Itinerary work** is a first-class tool rather than a chat exercise: `plan_itinerary` and `customize_itinerary` return structure and a shareable link.
- **An honest boundary** on payments, which is what makes it safe to attach to an agent that a customer talks to.

## Integration with CorpusIQ

A CorpusIQ answer about a trip or a city can end in a live quote instead of a description. The pairing keeps the citation discipline: the quote carries the departure time, the seats and the expiry, and the checkout link is on the operator's own domain, so the traveller sees the same price the agent quoted.

## Limitations

- **One operator's inventory.** This is See Sight Tours' own catalogue, not a travel marketplace: 20 cities in Canada and the United States for day and private tours, plus multi-day small-group trips worldwide.
- **Most multi-day trips are booked by request.** The tool descriptions say so directly, and those paths return a quote link rather than a seat hold.
- **No payment visibility.** The server cannot see whether a guest paid, and says so in the same sentence that confirms the checkout link works.
- **Currency follows the operator.** Prices came back in CAD for Toronto; a US departure prices in its own currency.
- **Seats move.** A quote is good for minutes, so any answer that quotes a total without its expiry is stale by design.

## FAQ

### Does it need an API key?

No. `initialize` and `tools/list` answered 200 keyless and all seven driven calls returned data without a credential.

### Can an agent complete a booking?

No. `get_checkout_link` hands back a link on seesight-tours.com where the traveller reviews and pays. The agent never sees card data and cannot confirm that a booking was paid.

### How current is availability?

Live at call time. The response carries seats left, a party total and an `expires_at` stamp, and the example above expired seventeen minutes after it was issued.

### What happens for a city it does not serve?

`search_products` returns an empty result with `total_matches: 0` rather than an error, so an agent can say plainly that this operator does not run there instead of inventing a tour.

## See Also

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [djbnb MCP - Live Music and Event Calendars](/hermes/mcp/servers/external/djbnb-mcp)
- [TripWorks MCP](/hermes/mcp/servers/external/tripworks-mcp)
