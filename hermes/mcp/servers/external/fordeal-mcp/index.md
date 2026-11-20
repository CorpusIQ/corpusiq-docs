---
title: "Fordeal MCP - Shop Prices Across Central Europe"
description: "Compares shop prices in six Central European countries with price history, shop trust and a wait-or-buy verdict on every offer."
category: "E-Commerce / Price Intelligence"
stars: "n/a (hosted vendor endpoint; MCP wrapper published at github.com/banbosh/fordeal-mcp)"
added: 2026-11-20
source: "the mcp.so submission queue entry #7697 filed 2026-11-20T11:31:57Z, a keyless initialize the same day, the full tools/list, and eight driven tools/call requests (find, get, history, variants, abroad, trending, most_searched and a text search) plus two refusal paths, with the commission disclosure read from the responses"
relevance: ★★
tags: [price-comparison, retail, ecommerce, price-history, central-europe, shopping, remote, keyless, commission-funded]
last_updated: "2026-11-20"
---

# Fordeal MCP

**A price is not a number until you know what it was last week and which shop is behind it. This server answers both, for six countries at once.**

```text
Server type:   remote Streamable HTTP, keyless (SSE responses, event: message)
Endpoint:      https://fordeal.ai/mcp
Server:        fordeal 0.1.0, title "Fordeal.ai", protocol 2025-06-18
Vendor:        https://fordeal.ai (HTTP 200), docs at github.com/banbosh/fordeal-mcp
Auth:          none for the public tools; an optional free agent key raises the rate limit
Tools:         2, both read-only, both action-switched
Countries:     CZ, SK, PL, DE, AT, HU (the enum the server enforces)
```

## What the server is

Fordeal is a shopping comparison engine built for the Central European market: it tracks shop offers per product, keeps a daily lowest price per day, and answers with a verdict rather than a list. The `initialize` instructions state the job in one line:

> Fordeal answers one question: where to buy a product cheapest today in Czechia or Slovakia (more countries coming), by the real product price with the shipping shown separately for every offer, and whether the shop can be trusted.

Read past the marketing sentence and note the three claims it commits to: **goods price separated from shipping**, **a trust signal per shop**, and a **capture timestamp per offer**. All three are in the response body, which is what makes the surface worth a guide.

## The two tools

Both tools are a single entry point with an `action` switch - the shape is unusual and it matters, because the arguments change per action.

| Tool | Actions | Key arguments |
|---|---|---|
| `search` | `search`, `trending`, `most_searched`, `rows` | `query`, `category`, `country`, `locale`, `limit`, `offset`, `sort`, `price_min`, `price_max`, `brand`, `in_stock`, `on_sale`, `detail` |
| `product` | `find`, `get`, `variants`, `history`, `abroad` | `query` or product slug, `country`, `detail` |

The declared `outputSchema` on `search` promises `total`, `returned`, `limit`, `offset`, `more`, `commission_disclosure` and `cross_border_note`. The declared schema is not what comes back - see the drift note below.

## One product, measured

`product` with `action: find` and the query *iPhone 16* for **CZ** returned a complete verdict, not a table:

```text
verdict:      "wait"
headline:     "Wait. The recommended offer today is CZK 19,990 at Mobil Pohotovost,
               and the price has been lower recently."
explanation:  "In the last 51 days the goods sold for CZK 18,015 without shipping;
               today's price sits well above that. Price checked 20/11, 11:54."
best:         Mobil Pohotovost  goods 19,990  shipping 0  total 19,990  CZK
              trust "rated", rating 0.82, 2,882 ratings, price_status "verified"
price_verdict lowest 18,015.06 · percentile 40 · days 51 · current 19,990
captured_at:  2026-11-20T10:54:58Z
```

`action: history` on the same product gives the series behind that verdict:

```text
window 365 days · 21 points · CZK
first  2026-10-01   21,260.09
last   2026-11-20   19,990
min    2026-11-08   18,015.06
max    2026-10-03   22,990
summary_of "daily lowest prices"
```

Every number in the verdict reconciles against the series: the **18,015.06** low is the **2026-11-08** point, the **51** days is the distance from that low to today, and the **40th** percentile follows from 21 points of which the current price sits above the minimum. The verdict is arithmetic on its own data, which is the test most "AI shopping" surfaces fail.

### Can it tell me whether today is a good price?

That is the product. It returns **wait**, **buy at the low**, or a caveat, plus `reasons` (`above_recent_low` here) and `advice` (`recently_cheaper`). The basis is stated verbatim: `own_daily_lowest_90d` - the vendor's own daily lowest, not a market index, so the verdict is only as good as their shop coverage in that country.

### Does it hide the commercial relationship?

No, and the wording is the best part of the surface. Every search response carries:

> When you buy through a Fordeal link, the shop pays Fordeal a commission. It does not raise your price and it never affects the order: offers are ranked by product price and shop trust only; shipping is shown separately for each offer.

An affiliate disclosure inside the tool response, before any purchase path, is the correct place for it, and most of this catalog's commerce servers omit it.

## Trust, and what it is worth

Every offer carries `shop.trust` as a word (`rated`), a `rating` as a decimal (**0.82**), and a `rating_count` (**2,882** for Mobil Pohotovost, **302** for Bscom.cz). Where the count is missing the tool warns instead of inventing one: the same response carried two warnings - *"The shop has customer ratings but no verified-shop badge"* and *"eBay.at has no verified reviews"*. The trust vocabulary is doing real filtering work rather than decorating the output.

The trending board for CZ returned **11** products, and it shows shipping separated exactly as promised:

```text
Apple AirPods 4                 3,190 + 69 shipping = 3,259 CZK   4 shops
Apple iPhone 18 Pro 256 GB     34,990 +  0 shipping = 34,990 CZK  4 shops
```

## Where it stops

- **The card says two countries; the server answers six.** The queue body and the instructions say Czechia and Slovakia with "more countries coming". The refusal path prints the real enum: `Pass one of: CZ, SK, PL, DE, AT, HU.` Ask for the United States and the answer is `Fordeal does not compare shops for "US"` with `isError: true` and a `fix` naming the six. Trust the error, not the card.
- **Text search expands the query and then reports partial matches.** A search for *robot vacuum* in CZ returned **28** matches whose first two rows are a Xiaomi mop pad (**299 + 89 = 388 CZK**) and a replacement brush (**219 + 89 = 308 CZK**), each with `match_note: "Partial match: the product's name lacks irobot from the query."` The engine rewrote the query to include a competitor brand and then returned accessories. An agent that forwards the top row reports a mop pad as a vacuum cleaner.
- **One product's `history` offers mix currencies without converting.** The same response that gives CZK 22,990 for Datart lists NAY at **1,029 EUR** in the `offers` array beside the CZK prices, with no `currency` normalisation and no FX conversion - the top-level `currency` says CZK and the row says EUR.
- **`history` rejects the argument the other actions accept.** `product` with `action: history` and `query` returns `Invalid arguments for price_history: product: Invalid input: expected string, received undefined` and a `fix` pointing at `help {topic:"price_history"}` - an internal action name the schema does not list. Pass the slug, not the query.
- **`most_searched` for SK returns an empty ranking with a broken next step.** The response was `count: 0`, `generated_at: null`, and a `next_actions` entry calling a tool named `search_products` with a parameter named `deliver_to_country` - neither exists in the tool list, which declares `search` with `action: search` and a `country` argument.
- **`abroad` can return nothing without a reason.** For the iPhone in CZ it returned `products: []`, `total: 0` and no note, so "no cheaper country" and "not tracked abroad" read the same.
- **Output keys drift from the declared schema.** `search` declares `total` and returns `total_matches`; `product` declares a `slug` and returns a per-query visit slug that differs between `find` (`v8pcan4mfe`) and `get` (`me7et3nfk8`) on the same product. Parse defensively.

## What it costs

The public tools need no account and no key. The vendor documents a free rate limit of **10 requests per minute per IP** for anonymous use and **60** with a free agent key - read from the queue entry rather than measured here, because this pass never came close to the ceiling. The business model is the affiliate commission the disclosure describes, so the data costs the caller nothing and the vendor is paid by the shop.

## Add it to Hermes

```bash
hermes mcp add fordeal --url https://fordeal.ai/mcp
hermes mcp test fordeal
```

Then ask the question a purchasing lead actually has: *is an iPhone 16 a good buy in Czechia today, and which shop has it?* The answer is a verdict, a shop with a rating count, and a timestamp - the three things a price scrape usually leaves out.

## Why it earns a slot

Price monitoring in this catalog has been marketplace-data shaped: scrapers that return listings. This is the first entry that returns a **judgement with a date on it** - a 51-day low, a percentile, a shop trust level, and an explicit statement that a commission is being paid. For a business buying in CZK, PLN or HUF that is the difference between a spreadsheet of prices and a decision, and the rejections it performs (six countries, honest refusals, warnings where a badge is missing) are as useful as the prices it returns.
