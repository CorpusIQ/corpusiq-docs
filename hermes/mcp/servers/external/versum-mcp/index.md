---
title: "Versum MCP - The Local Shop Shelf an Agent Can Quote"
description: "Keyless read-only index of US local businesses read from their own websites: hours, items, published prices and order links, with unknown stock labelled."
category: Commerce & Retail
stars: ★★★ (keyless, 13 tools, 5,398 cards measured across 128 trades)
added: 2026-11-02
source: "the chatmcp/mcpso submission window on 2026-11-02 (issue #6603), and a driven keyless session on https://versum.suverse.io/mcp: initialize HTTP 200, 13 tools listed, and live calls to list_niches, search_catalog, find_business, get_card, get_offering and quote_order"
relevance: ★★★
tags: [local-business, commerce, pricing, storefront, read-only, keyless, remote-mcp, us]
last_updated: "2026-11-02"
---

# Versum MCP

**Every local business already publishes its prices. The problem is that no agent can read them, so the answer to "what does that shop charge" is still a phone call at eleven in the morning.**

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://versum.suverse.io/mcp
Auth:        none for reads
Tools:       13 measured, all read-only
Coverage:    128 trades, 5,398 cards, 9,300 businesses
Writes:      none. No order is placed, nothing is reserved
```

## What it does

Versum is a free index of real local businesses in the United States, built by reading each business's own public website rather than a directory feed. The point is not the listing. The point is the shelf: what each business sells, at what published price, with the link that goes back to the shop.

The thirteen tools split by the question being asked.

| Question | Tool |
| --- | --- |
| What trades exist, and how deep is each one | `list_niches` |
| Surf the shelf | `list_cards`, `search_catalog` |
| The user named a business | `find_business` |
| One business in full | `get_card`, `get_business` |
| One item, with a live price request | `get_offering`, `get_product` |
| What would this cost delivered | `quote_order` |
| Stock | `check_availability` |
| Act | `place_order`, `book_slot`, `order_status` |

`get_product` and `get_business` are synonyms of `get_offering` and `get_card`, kept so an agent that already knows the other name does not have to relearn it.

The contract is written for an agent rather than for a human reader, which is the part worth copying. Ask `search_catalog` for pizza without a location and it refuses to guess: `needs.missing: location`, a stated reason that no distance was measured so nothing was narrowed, and an instruction to ask the user for a city or a 5-digit postcode before quoting any of it back. It also states what the answer is not: the order of the results says nothing about proximity.

## What this pass measured

A keyless session against the live endpoint, not a documentation read.

`initialize` answered **HTTP 200** with `serverInfo` `versum-catalog` **1.6.0** on protocol `2025-06-18`, `tools/list` returned all **13** tools with schemas in 50,179 bytes, and no credential was used at any point.

`list_niches` returned the whole index in one object: **128** trades, **5,398** cards and **9,300** businesses, with per-trade coverage and the city zones behind it. The depth is uneven and the index says so. Restaurant carries **783** cards over **1,042** businesses, coverage `partial`, with the reason printed as `Tampa, FL: 10 cell(s) still answer the cap`. Florist is **183** cards over **316** businesses and `complete`. Pizza is **95** over **202** and `complete`. Each zone carries the date it was last passed, `2026-11-01` and `2026-11-02` in the samples read.

`search_catalog` for pizza in Tampa returned **12** matches in a **15** mile radius and the first three businesses with their items. The top card is a real shelf with real prices:

- Green Bench Brewing Co., **0.3** miles away, `(813) 867-8804`, platforms `skytab` and `squarespace`, `checked: 2026-11-01`
- FOUR CHEESE PIZZA at **$12.95**, `price_type: fixed`, `availability: unknown`
- Pepperoni Pizza at **$14.50**, same terms

`get_offering` on the first item returned the price as a claim with its evidence attached rather than as a number: `price_state: {state: confirmed, basis: published, source: semantic_html, read_at: 2026-11-01T01:28:53}`, `evidence: {url: http://thepintandbrew.com/menu, quote: "$ 12.95"}`, `currency: USD`. The stock line is the honest half: `availability_state: {state: unknown, basis: not published}`, and the card says `availability not published for any offering shown`. Somebody can be told what a pizza costs and cannot be told whether it is in stock, and both facts arrive labelled.

`get_card` returned the full business: address, latitude and longitude, e-mail, website, platform `squarespace`, timezone `America/New_York`, hours for all seven days as `11:30` to `00:00` with a `quote` field written as a person would say it, and `niche_decided_by: {source: catalog, reason: "catalog: 100% restaurant (dish 25, drink 8) of 33 classified, 46 on the shelf"}`. The classification carries its arithmetic, so a trade assignment can be argued with instead of trusted.

`find_business` is the operational tool. Asked for Green Bench Brewing near `33602` with `intent: order` and `needed_by: 2026-11-06T19:00:00-05:00`, it read the timestamp as `open_at` on `Fri 2026-11-06`, matched at **0.9** on `part`, and returned a task card: the phone number, the hours for that day with `state: confirmed` and the reasoning `open at 19:00 by the published hours (11:30 AM - 12:00 AM)`, and the five cheapest items with prices, `Bottle Water` at **$3.00**, `Iced Tea` at **$3.95**, `Lemonade` at **$3.95** and two more. That is the whole answer an operator needs before sending someone: open then, this is what it costs, here is the number.

`quote_order` on the **$12.95** pizza delivered to postcode `33602` came back `placed: false`, `status: not_available`, `reason: no_public_cart`, and stated its own limits: the shop's public cart priced the order in a session of its own which was emptied afterwards, only the delivery address was sent, no name, e-mail or phone, and nothing about it was kept. The quote path failing is worth knowing before anybody builds on it: this shop publishes a menu but not a cart.

## Where it fits, and where it does not

Nothing else in this catalogue reads a local shop's own shelf. [GBPly MCP](/hermes/mcp/servers/external/gbply-mcp/) manages your own Google Business Profile and keeps every write behind an approval that expires in fifteen minutes; [Listings API MCP](/hermes/mcp/servers/external/listings-api-mcp/) publishes a business out to 80 plus directories and maps; [GoodLeads MCP](/hermes/mcp/servers/external/goodleads-mcp/) turns new-business state filings into priced lead lists. All three act on business identity. None answers what a shop on the next block charges for a pizza. [Undercart MCP](/hermes/mcp/servers/external/undercart-mcp/) is the nearest neighbour and covers online Shopify stores; this covers the shop with a Squarespace menu and a phone number.

The limit is stated by the server itself rather than by this guide. Coverage is partial and city-bounded: Tampa is deep, and a query in a city with no passed cells has nothing to return. There is no write path a buyer should rely on until a card shows a connected platform, and the one shop measured here has a menu but no public cart. The index is US only.

## Integration notes for CorpusIQ

- Add it as a read-only source beside a commerce or Shopify connector and the answer stops being a link: a price, a distance, a phone number and an honest unknown.
- `find_business` with `needed_by` is the pattern worth reusing on our own side. A timestamp that resolves to `open_at` with the reasoning printed is a citation an operator can check, which is the difference between an answer and a guess.
- No key, no account, nothing to configure. The call that costs nothing is also the one that says what it does not know.

## Links

- Server: `https://versum.suverse.io/mcp`
- Website: https://versum.suverse.io
- Public design notes: https://github.com/sudzikcoin/versum-agent-assistant
- Registry: `io.github.sudzikcoin/versum-agent-assistant`

## Verification

- Endpoint driven keyless on 2026-11-02: `initialize` **200**, `versum-catalog` **1.6.0**, **13** tools, 50,179 bytes of schema.
- Six tools called live: `list_niches` (**128** trades, **5,398** cards, **9,300** businesses), `search_catalog` (**12** matches, **3** cards), `find_business` (task card with a confirmed open state), `get_card`, `get_offering` (price with evidence quote, stock unpublished and labelled), `quote_order` (`placed: false`, `no_public_cart`).
- Two argument-shape corrections found by driving it: `get_card` and `get_offering` take `id`, not `business_id` or `offering_id`, while `quote_order` and `place_order` take `offering_id` and `business_id`. The schema is strict, `additionalProperties: false`, and a wrong field name returns JSON-RPC `-32602`.
- Numbers in this guide are what the server returned on the day, not the counts in the submission issue. The issue states **7,415** cards over **128** trades; the live `list_niches` answered **5,398** cards over **9,300** businesses across the same **128** trades.
