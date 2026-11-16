---
title: "GoGiga MCP - Polish Concerts, Dated Prices and Sellers"
description: "A keyless MCP server for Polish concerts with dated prices and named ticket sellers, plus a price filter that still returns concerts carrying no price."
category: "Events / Local Data"
stars: "0 (remote Streamable HTTP, keyless; four tools, all four driven)"
added: 2026-11-16
source: "the mcp.so submission queue entry #7460 filed 2026-11-16T14:59:51Z, and a driven session on 2026-11-16 in which all four tools were called over Streamable HTTP, 23 tools/call requests in total"
relevance: ★★★
tags: [events, concerts, poland, ticketing, local-data, keyless, remote, mcp]
last_updated: "2026-11-16"
---

# GoGiga MCP

**An assistant asked what is on in a city this weekend will answer from its training data, which is to say it will answer from a summer that has already ended.** The failure is not subtle: the model names a festival that finished in August, quotes a venue that closed, and puts a price on a ticket that no longer exists. The fix is not a better model. It is a lookup against a list that is regenerated from the ticket shops.

GoGiga is a small, free, keyless server that answers that question for **400+ Polish towns**, and the property worth recording is that every answer carries the concert's own page, a Polish-time date and time, and, where the seller publishes one, a **from** price with the shops that sell it. The pass below drove all **four** tools through **23** `tools/call` requests and found the arithmetic of the listing consistent, the refusals clean, and one filter that does not do what its own schema says.

```
Server type:   remote Streamable HTTP
Endpoint:      https://gogiga.pl/mcp
Server:        pl.gogiga/koncerty, version 1.0.0, title GoGiga
Protocol:      2025-06-18
Auth:          none (no key, no account, no OAuth)
Tools:         4 (search_concerts, get_concert, band_concerts, list_festivals)
Website:       https://gogiga.pl
Listed on:     the mcp.so submission queue as #7460
```

## The evidence tier

**Keyless and driven.** No credential was needed at any point. `initialize` answered **200** as `pl.gogiga/koncerty` **1.0.0** on protocol **2025-06-18**, `tools/list` returned **four** closed schemas, and every one of the four tools was called: `search_concerts` on seven argument shapes, `get_concert` on a URL, a bare slug and an invalid slug, `band_concerts` on three names, and `list_festivals` on two filters and an out-of-range page. Six of the calls were deliberate failures, run to see whether the server refuses or invents.

## The tool surface

| Tool | Arguments | What it returns |
|---|---|---|
| `search_concerts` | `city`, `radius_km` (0 to 50), `query`, `genre`, `date_from`, `date_to`, `price_max`, `page` (1 to 50) | A page of **12** concerts with title, date, time, venue and address, performers, genre, a **from** price where one is known, and the concert's GoGiga URL, beside `totalConcerts` and `totalPages`. |
| `get_concert` | `concert` (GoGiga URL or slug) | One concert with ticket sellers, each seller's own price, a `resale` flag, and the band records behind it. |
| `band_concerts` | `band` (2 to 100 characters) | Every band the name resolves to, with genre, subgenre, URL, `totalUpcomingConcerts` and the upcoming list. |
| `list_festivals` | `query`, `type` (festival or tour), `page` (1 to 50) | Festivals and tours, soonest first, **10** a page, with date range, towns and a concert count. |

## What the city search returns, and the arithmetic that checks it

`search_concerts` for Kraków answered **522** upcoming concerts across **44** pages, and 522 divided by the 12 rows a page carries gives 43.5, which is 44 pages rounded up. The two filters that narrow the set behave the way the counts say they should:

| Call | `totalConcerts` | `totalPages` | Reading |
|---|---|---|---|
| city Kraków | 522 | 44 | 44 x 12 = 528, the ceiling of 522 |
| city Kraków, `radius_km` 30 | 552 | 46 | 46 x 12 = 552, and the extra 30 are the neighbouring towns |
| city Kraków, `genre` Jazz | 35 | 3 | 36 is the ceiling of 35 |
| city Kraków, 2026-11-20 to 2026-11-22 | 51 | 5 | 60 is the ceiling of 51 |
| city Kraków, `price_max` 100 | 192 | 16 | see the defect below |

The first page opened on the day of the pass: Julia Pietrucha at **19:00** at Kino Kijów Centrum at **od 129 zł**, Carpenter Brut at Klub Studio at **od 179 zł**, and Korn at TAURON Arena on 17 November, which carries no price at all. A listing that omits the price rather than printing a zero is the right shape, and the schema says so in as many words: a concert without a price has no known price.

## One concert, three numbers that have to agree

`get_concert` on a URL and on the bare slug returned the identical object, which is the behaviour a caller wants from an identifier that appears in two forms in its own search results.

```text
title          Julia Pietrucha
date / time    2026-11-16, 19:00 Polish time
venue          Kino Kijów Centrum, Al. Krasińskiego 34, Kraków
price          od 129 zł
ticket sellers Adria Art   od 129 zł
               AleBilet    od 149,50 zł  resale = true
band           Julia Pietrucha, Rock & Alternative, /band/julia-pietrucha
```

**The seller block is the useful part, and it is readable without a salesperson.** The primary shop and the resale shop are separated by a flag rather than by a paragraph, and the resale price is **15.9%** above the primary one on the same seat inventory: **149.50 / 129 = 1.1589**. A caller that quotes the first price it sees quotes the cheaper one here, but the flag is what tells it whether it is looking at primary sale at all.

## What the filters actually do

Three of the four filters held on every call. `genre` accepts a main genre or a subgenre, and an unknown one comes back as a refusal naming the ten main genres rather than an empty set that reads as *no concerts*. `date_from` and `date_to` are inclusive of both ends in Polish time. `radius_km` widens the city set and the counts say by how much.

**The price filter does not hold, and it fails in two directions at once.** `price_max` is documented as *Only concerts with a known ticket price up to this many złoty*. Across the first three pages of the Kraków result at a **100** złoty cap, **36** rows came back of which **13** carried no price field at all (36% of the set) and one carried a price above the cap, Imperial Triumphant at **od 109 zł**. A caller that trusts the filter to mean *priced, and priced under the limit* is wrong on both counts, and the only safe reading is that the argument is a hint.

## A refusal is the property to test first

Six wrong calls, six answers that name the problem:

| Call | Answer |
|---|---|
| `get_concert` with `does-not-exist-xyz` | *No concert "does-not-exist-xyz". Use the url or the slug that search_concerts returns.* |
| `search_concerts` with `city: Zzzznotacity` | *Unknown town "Zzzznotacity". Give a Polish town name, e.g. "Kraków" or "Gdańsk".* |
| `search_concerts` with `genre: Polka` | *Unknown genre "Polka". Main genres: Rock & Alternative, Electronic & Dance, Hip-Hop & Rap, Reggae, Jazz, Classical, Metal & Punk, Pop, Blues, RnB & Soul.* |
| `list_festivals` with `page: 99` | *"page" must be a whole number from 1 to 50* |
| `band_concerts` with `band: "X"` | *"band" needs at least 2 characters* |
| `band_concerts` with `Zzqqxx` | An empty `bands` array, which is the honest answer to a band nobody has heard of |

The genre refusal is the one to copy. It does not merely reject the argument, it prints the enum, so a model that guessed *Polka* can correct itself on the next call without another round trip through a search.

## Two defects in the band and festival tools

**The band resolver returns a genre it cannot justify.** `band_concerts` for **Metallica** returned `totalUpcomingConcerts` **0**, which is plausible for a band between tours, and `genre` **Pop**, which is not a classification any reader of the catalogue would defend. A record that exists with the wrong genre is worse than a miss, because a caller filtering by genre will file the band in the wrong place. `Dżem` resolved correctly at **18** upcoming concerts with the genre *Blues, RnB & Soul*, so the resolver works and the record behind it does not.

**The festival filter returns a value outside its own enum.** `list_festivals` documents `type` as `festival` or `tour`, and a request with `type: tour` returns objects whose `type` field reads **`trasa`**, the Polish word. A client that branches on the returned field against the documented enum falls through both cases. The filter works; the label it round-trips does not.

## The listing itself, measured

`list_festivals` for the whole of Poland returned **92** entries across **10** pages, and the tour filter returned **66** across **7**, with the arithmetic consistent at 10 a page. The entries carry what a caller needs to answer a question rather than to browse: a date range, the towns in order, and a concert count. The longest single tour in the set was a **44** concert run across 43 towns from November 2026 into December 2027, which is the kind of row that is expensive to assemble by hand and cheap to return here.

**A date worth a caveat.** A `query` search for **Kult** returned **5** results, one of them at TAURON Arena Kraków stamped **2027-11-06**, twelve months out. That is a real announcement or a data error and this pass cannot tell which from outside; what it can say is that the server serves far-future dates without flagging them, so a caller answering *what is on this month* should still bound the window with `date_to` rather than trust the default.

## Is this worth a connection?

For an assistant that answers questions about live events, yes, and the reason is narrow. The server covers one country, it is free, and it carries the two things a language model cannot generate: a date that is still ahead and a price that a shop is currently asking. It is not a ticketing integration, it does not sell anything, and its strongest property is the one this pass tested hardest: the numbers agree with themselves.

## FAQ

### Does GoGiga need an API key or an account?

No. `initialize`, `tools/list` and all **23** `tools/call` requests were made with no credential of any kind, and the endpoint answered **200** throughout.

### How do I ask it what is on this weekend in a specific city?

Pass `city` with the Polish name and bound the dates with `date_from` and `date_to`, both `YYYY-MM-DD` in Polish time. The window from 2026-11-20 to 2026-11-22 in Kraków returned **51** concerts, and every row carried its own GoGiga URL.

### What does the price field mean when it is missing?

That no price is known for that concert, per the server's own instructions. A caller should say *no price published* rather than guess, because the row genuinely has no number in it and the seller list may still have one behind `get_concert`.

### Why did a concert priced above the limit come back from a price-capped search?

Because `price_max` behaves as a hint rather than a filter in the current build: **13** of **36** rows on the first three pages of a 100 złoty capped search carried no price at all, and one carried **od 109 zł**. Treat the argument as a ranking aid and re-check the price field in the response.
