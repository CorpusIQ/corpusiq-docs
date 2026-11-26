---
title: "Suppliers Net MCP - Wholesale Prices With the Seller"
description: "A keyless Australian food-supply directory that returns advertised wholesale prices per kilo, each with its seller, source link and the date it was read."
category: "Business Operations"
stars: "n/a (no public repository)"
added: 2026-11-25
source: "mcpservers.org arrival in the November 25 evening window, `servers/1..13` maps; official registry record io.github.Dragoonhawx/suppliers-net 1.0.0; keyless initialize, a four-tool tools/list and fourteen tools/call requests driven against https://suppliers.net/mcp on 2026-11-25"
relevance: "★★★"
tags: [procurement, wholesale, pricing, suppliers, food, australia, keyless, remote-mcp]
last_updated: "2026-11-25"
---

# Suppliers Net MCP

**Procurement questions fail on provenance, not on coverage.** A per-kilo figure with no seller is a rumour, a seller with no date is a price that may have moved, and a date with no source link cannot be checked. Suppliers Net answers all four fields at once, and the arithmetic that turns a pack price into a unit price is reproducible from the payload itself.

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://suppliers.net/mcp
Auth:        none, no key and no account
Registry:    io.github.Dragoonhawx/suppliers-net 1.0.0
Scope:       Australian food wholesale, AUD, GST excluded
Tools:       4, read from a keyless tools/list
```

`initialize` answers **200** at protocol **2025-06-18** with `Server: cloudflare` and capabilities `resources`, `extensions`, `tools`. The extension capability is unusual here and worth knowing before a client negotiates its feature set: the server advertises more than plain tools, so a client that only reads `tools` still works but leaves the resource surface unused.

## What the four tools answer

| Tool | Arguments | What comes back |
| --- | --- | --- |
| `search_prices` | `query`, `include_older`, `limit` | dated advertised prices, cheapest per unit first, each with seller, pack, per-unit value, source URL and `date_seen` |
| `market_rates` | `query` | a median per unit, **only** where three or more verified suppliers list the same product |
| `find_suppliers` | `category`, `state`, `limit` | seller name, categories, state, profile URL and a `status` of `verified`, `checked`, `claimed` or `listed` |
| `coverage` | none | the size of the catalogue: supplier counts by state and category, current price count, sellers with prices |

## The catalogue, in its own numbers

`coverage` on 2026-11-25 returned **24681** current advertised prices from **427** sellers, and states summing exactly to **804** suppliers:

```text
NSW 266   VIC 222   QLD 156   WA 74   SA 56   TAS 15   ACT 10   NT 5
```

266 + 222 + 156 + 74 + 56 + 15 + 10 + 5 = **804**, and `find_suppliers` with only a state returns **266** for NSW, which is the state row and not a coincidence. The top ten categories read Meat **159**, Produce **98**, Beverages **93**, Pantry **74**, Seafood **66**, Dairy **63**, Bakery **39**, Coffee & tea **33**, Oysters **22**, Fruit **20**. These overlap by design: a butcher that also sells oysters is counted in both, so the category column is a set of tags rather than a partition, and the ten do not sum to 804.

## Fourteen calls, and the arithmetic that verifies them

`search_prices` with `query: "beef"` returned `total: 804` and twelve rows. Every row states its price twice, once as the pack price a seller advertises and once as a per-kilo figure, and the division reproduces exactly on all twelve:

| Item | Pack | Advertised | Per kg | Seller | Seen |
| --- | --- | --- | --- | --- | --- |
| Beef Soup Bones | 5 kg | $7.09 | **$1.418** | AUSBD HALAL FOODS PTY LTD | 2026-11-25 |
| Pet Mince (chicken or beef) | 1 kg | $2.50 | **$2.50** | South Ulladulla Butchers | 2026-11-24 |
| Beef Topside Whole | 6 kg | $17.64 | **$2.94** | AUSBD HALAL FOODS PTY LTD | 2026-11-25 |
| Beef Mince, liver heart kidney 30% | 5 kg | $17.48 | **$3.496** | AUSBD HALAL FOODS PTY LTD | 2026-11-25 |
| Beef Marrow Bone, bulk | 10 kg | $35.00 | **$3.50** | KCS HEALTH PTY LTD | 2026-11-25 |
| Premium Beef Fat, bulk | 3 kg | $11.50 | **$3.8333** | KCS HEALTH PTY LTD | 2026-11-25 |
| Angus Beef Burger | 1 kg | $3.88 | **$3.88** | Chop Astisan Butchery | 2026-11-25 |
| Black Angus Rump Whole MB3-4+ | 7 kg | $29.46 | **$4.2086** | AUSBD HALAL FOODS PTY LTD | 2026-11-25 |
| Packer Cut Brisket, navel end | 4 kg | $18.35 | **$4.5875** | AUSBD HALAL FOODS PTY LTD | 2026-11-25 |
| Brisket Bone | 1 kg | $5.00 | **$5.00** | Lakeside Chicken | 2026-11-25 |
| Beef Conical Muscle | 4 kg | $21.05 | **$5.2625** | AUSBD HALAL FOODS PTY LTD | 2026-11-25 |
| Massel Ultracubes beef stock | 1.05 kg | $5.60 | **$5.3333** | IBEX FOODS PTY. LTD. | 2026-11-24 |

**The cheapest and dearest rows in the same answer are $1.418 and $5.3333 a kilo, and the ordering holds across pack sizes rather than only within them.** That is the useful property for procurement: a 1.05 kg pack of stock cubes and a 10 kg pack of marrow bone compare on one scale without the buyer doing unit conversion by hand, and every row carries the string it was derived from (`stated.basis` reads `per 5 kg`, `per 1.05 kg`), so the conversion is auditable rather than trusted. Currency is AUD on every row and `gst: "excluded"` is stated per price, which matters because a catering quote that mixes GST-inclusive and GST-exclusive figures is wrong by 10% before anyone argues about anything else.

## What the tool refuses to do, and why that is the design

Three refusals arrived in the same pass, and each one names its own limit:

- `market_rates` with `query: "beef"` returned `count: 0` and *"No product has three or more verified suppliers yet, so there is no market rate to quote. Use search_prices for dated seller prices."*
- `search_prices` with a nonsense query returned `total: 0` and *"No current advertised price matches. Try a shorter query, or set include_older. Suppliers Net does not guess a price."*
- `find_suppliers` with `category: "nonexistentcat"` returned `total: 0` rather than the full catalogue, so the filter fails closed instead of open.

**A zero from a price tool is usually indistinguishable from a broken query, and this server writes the difference in the note.** It also states what its prices are not: advertised seller prices read from the seller's own public page, not a purchase price, not a quoted trade rate, and not a market rate. An assistant that reports a `search_prices` row as "the wholesale price of beef" has overstated it by exactly one word.

`include_older: true` on the beef query changed nothing measurable: `total` stayed **804** and the returned rows were identical, because every row on that query was already `current: true`. The flag exists to reach stale rows, and this pass did not observe a stale row on which to test it.

## One defect, recorded rather than smoothed

**`category` is matched against product text, not against the seller's category field.** Two calls demonstrate it:

- `category: "Meat"`, `state: "NSW"` returned **60** sellers whose first two rows are `Claudio's Seafoods` (categories Oysters, Finfish, Crustacean & Mollusc, Prawns) and `COSTIS FRESH SEAFOOD PTY LTD` (Seafood). Both advertise items containing the word: *MUSSEL MEAT*, *Prawn Meat*, *Bug Meat*.
- `category: "Seafood"`, `state: "NSW"` returned **22**, including `PUKARA ESTATE PTY LTD` whose category is Pantry.

Without a category the same state returns **266**, so the filter is reducing the set rather than being ignored. The reduction is coming from matchable text somewhere in the record, which means a category-shaped question is answered with sellers that stock the word rather than sellers tagged with the category. For an agent, the practical consequence is that `find_suppliers` is a discovery tool and `search_prices` is the precise one: to answer "who sells beef", read the `seller` field off priced rows instead of trusting a category filter to have done it.

## Limits measured this pass

- **Australia only.** Every seller, every state and every currency is Australian; there is no other market on the surface.
- **Advertised, not transacted.** The vendor states this in the tool descriptions, and no order, quote or availability tool exists to contradict or confirm a listed price.
- **Freshness is per row, not per catalogue.** `date_seen` ran **2026-11-24** to **2026-11-25** on this read, but there is no tool that returns the age distribution, so an agent quoting a single row should read `current` and `date_seen` on that row rather than assume the catalogue is current.
- **`status` is a claim hierarchy, not a trust score.** `verified` means claimed with an ABN match, `listed` means found in public records and never claimed; the tool says so in its note, and a procurement answer that omits the status is quoting an unclaimed listing as if it were verified.
- **No phone numbers or emails** are returned by `find_suppliers`, deliberately. The profile URL is the contact path.

## Where it fits a business-answer system

Suppliers Net is the cleanest example in this catalog of the pattern CorpusIQ is built around: **one number, one seller, one date, one link**. The figure is only usable when all four travel together, and the server returns them as a single object rather than as prose an assistant can paraphrase into something vaguer. For a food-service operator comparing chicken suppliers, or a cafe owner checking whether a quoted price is in line with what the market advertises today, the answer arrives with the receipt attached.

## See also

- [BestPrice Shopping MCP](/hermes/mcp/servers/external/bestprice-shopping-mcp/) for retail price comparison rather than wholesale.
- [Bullion Price Check MCP](/hermes/mcp/servers/external/bullion-price-check-mcp/) for the same dated-price discipline on dealer metal pricing.
- [Invoices to Spreadsheets MCP](/hermes/mcp/servers/external/invoices-to-spreadsheets-mcp/) for getting a supplier invoice into structured data before comparing it.
- [External MCP Server Catalog](/hermes/mcp/servers/external/) for the full index.
