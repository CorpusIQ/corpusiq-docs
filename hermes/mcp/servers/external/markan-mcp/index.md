---
title: "Markan MCP - Steam Sales Estimates You Can Recompute"
description: "Steam market data over 200,000 games, with a revenue coefficient that is exactly five stated deductions multiplied out."
category: "Games / Market Research"
stars: "0 (hosted Streamable HTTP at https://api.markan.games/mcp, keyless, no account; four tools and one prompt, all four tools driven)"
added: 2026-11-17
source: "the mcp.so submission queue entry #7511 filed 2026-11-17T14:39:42Z, and a driven session on 2026-11-17 in which eighteen tools/call requests were run against the live endpoint with no credential"
relevance: ★★★
tags: [games, steam, market-research, indie, sales-estimates, boxleiter, keyless, remote, mcp]
last_updated: "2026-11-17"
---

# Markan MCP

**An indie studio asking how much a comparable game earned gets a confident number from an assistant, and that number is invented.** The unit economics of a game release are not in the model's context: how many reviews turn into how many sales, what the store keeps, and how the answer changes with the release year. Every part of that is arithmetic with an assumption inside it.

Markan puts the assumption where it can be read. It is Steam data on roughly 200,000 games and DLC, and the part worth a page is that its most consequential tool publishes its own formula, so the estimate can be checked instead of believed.

```
Server type:   remote Streamable HTTP (hosted)
Endpoint:      https://api.markan.games/mcp
Server:        markan, title "Markan: Steam market data"
Protocol:      2025-06-18
Auth:          none
Tools:         4 (find_games, search_games, get_games, estimate_sales)
Prompts:       1 (reference_analysis)
Website:       https://markan.games/developers
Listed on:     the mcp.so submission queue as #7511
```

## The evidence tier

Keyless and driven. `initialize` answered **200** with no credential and no session id, `tools/list` returned four schemas, `prompts/list` returned one prompt, and **eighteen** `tools/call` requests were run across the four tools including three deliberate mis-calls. Every figure quoted below is the server's own output; every arithmetic check beside it was worked here independently.

## The tool surface

| Tool | Arguments | What it returns |
|---|---|---|
| `find_games` | tags, price band, review band, release window, type, sort, limit | Matching games with Steam ID, release date, price, review count and score, and the total that matched |
| `search_games` | query (title or Steam ID) | Up to 5 matches, most-reviewed first |
| `get_games` | up to 50 Steam IDs, optional field list | Full record: tags, genres, developers, publishers, short description, price in cents |
| `estimate_sales` | up to 50 Steam IDs | Low, medium and high lifetime sales, plus net revenue in the same three bands, with an `assumptions` string on every response |

The filter set on `find_games` is the useful part for research. This call asked for every game tagged both Cozy and Farming Sim, released since 2022, priced between 10 and 25 dollars, with at least 100 reviews:

```text
find_games(tags=["Cozy","Farming Sim"], released_after="2022-01-01",
           min_price_usd=10, max_price_usd=25, min_reviews=100, sort="price")
total_matches: 55, returned: 50
first prices:  10.46, 10.77, 10.99, 11.40, 11.99, 11.99, 11.99, 12.99 ...
```

The sort honoured the price band, the tag filter required both tags rather than either, and the review and date windows held. That is a filter surface an agent can actually use, which is not the default in this category.

## The revenue formula, taken apart

`estimate_sales` states its own method in the `assumptions` field: sales are the review count times a multiplier that depends on the **release year**, and net revenue is list price times sales times **0.3478**, described as 10 percent refunds, 20 percent regional pricing, 25 percent average discount, 8 percent sales tax, and Steam's 30 percent cut.

That description is a multiplication, so it can be checked:

```text
0.9  x 0.8  x 0.75  x 0.92  x 0.70  =  0.34776
```

The stated **0.3478** is that product rounded to four decimals. Using the rounded figure does not reproduce the server's own numbers, and the exact product reproduces every one of them to the cent:

| Game | Price | Medium sales | Server net revenue | Recomputing at 0.34776 |
|---|---|---|---|---|
| Stardew Valley | 14.99 | 57,039,192 | 297,340,881.65 | 297,340,881.65 |
| Luma Island | 19.99 | 431,300 | 2,998,277.87 | 2,998,277.87 |
| I Am Future | 19.99 | 153,748 | 1,068,813.42 | 1,068,813.42 |
| Roots of Pacha | 24.99 | 145,160 | 1,261,516.23 | 1,261,516.23 |

At the rounded 0.3478, Stardew's medium revenue computes 34,200 dollars above the server's figure. The gap is not an error in the server: it is the cost of quoting a rounded deduction chain as if it were the one that ran. Anyone re-deriving these numbers for a business case should use the exact product.

## The year bands, measured

The multiplier is not a single constant, which is the detail a studio actually needs. Sampling one game per release year and dividing the reported sales by the review count gives clean integers:

| Release year | Low | Medium | High |
|---|---|---|---|
| 2015 | 36 | 64 | 92 |
| 2016 | 35 | 63 | 90 |
| 2017 | 30 | 53 | 75 |
| 2018 to 2019 | 25 | 43 | 60 |
| 2020 to 2025 | 20 | 38 | 55 |

The decay is monotone and it says something real: older games carry more lifetime sales per review, so a 2020 release needs a smaller multiplier than a 2016 one to produce the same estimate. Quoting a single reviews-to-sales ratio across a catalogue is wrong by a factor of nearly two between the ends of that table.

## A free game is handled honestly

The strongest single response in the session is the one for a title with no price. Tom Clancy's Rainbow Six Siege returned a price of **0.0**, sales of 56.6 to 144.7 million, revenue of **0.0** at all three bands, and this note:

> Free (or not for sale): 'sales' means players, and in-game purchases are not estimated, so revenue is 0.

A tool that could have multiplied by zero and said nothing volunteered the reason instead. Five other free-to-play titles in the sample (PUBG, Apex Legends, NARAKA) behaved the same way.

## What it refuses, and how

Three deliberate mis-calls, all answered at HTTP 200 with `isError: true` and a named reason:

- A tag that does not exist: `unknown tags: 'NotARealTagXYZ'`.
- An invented sort key, `reviews_desc`: `sort must be one of reviews, newest, oldest, price`. The enum is printed, so the retry is a single correction. With `sort` set to `price`, the band came back ascending from 10.46.
- A Steam ID that does not exist: it lands in a `not_found` array (`[999999999]`) rather than poisoning the batch, and the valid IDs in the same request still return.

**One real friction point, measured.** `get_games` and `estimate_sales` take `steam_ids`, and passing the camelCase `steamIds` returns `steam_ids must be a non-empty list of Steam IDs`. The refusal is accurate and does not name the key that was actually sent, so the first retry after that message is a guess. Three of the eighteen calls were spent on it.

## One inconsistency worth knowing before you build on it

The price unit is not the same across tools. `get_games` returns `basePrice: 1499` and documents cents; `find_games` and `estimate_sales` return `priceUsd: 14.99` and `19.99` in dollars. A pipeline that reads a price from `get_games` and compares it to a `find_games` band without converting will be wrong by two orders of magnitude, silently.

## The prompt

`reference_analysis` takes one required argument, `game` (genre, features, target price, platform, scope), and is built for the comparison workflow the instructions recommend: find comparable titles, confirm them with the user, and end with a `Steam IDs: <id>, <id>` line that pastes into the vendor's Excel and Google Sheets add-ins. The add-ins are the vendor's real product; the MCP surface is the discovery half of it, which is worth stating because the instructions say so plainly rather than pretending the server is the whole tool.

### Does a review count really predict sales?

Not by itself. The Boxleiter method is a heuristic, the server says so in the same string that carries the numbers, and the low-to-high spread inside a single band is about 2.75 times at every year tested. The useful reading is the ordering and the ratio between comparable titles, not the absolute figure. An agent asked to value a studio should quote the medium band and say it is an estimate.

### Can it be used without an account?

Yes, completely. There is no key, no OAuth, no sign-up and no rate limit hit across eighteen calls in one session. That is unusual for a Steam data surface and it is the reason this one is usable inside a chat client without a setup step.

## Why it earns a page

Steam data has been reachable through undocumented scraping and through paid market-intelligence suites; the catalog held no guide for it, and `steam` appeared here only in a product that gives coding agents achievement badges. What makes Markan an entry rather than a listing is that the arithmetic behind its headline number is published, one deduction chain resolves exactly, and the year bands can be measured from the answers instead of taken on trust.

The server is also honest about its ceiling in the one place it matters most: a free game gets a zero revenue, with a written reason, instead of a plausible number.
