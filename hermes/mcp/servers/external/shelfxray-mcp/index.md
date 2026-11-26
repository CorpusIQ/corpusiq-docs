---
title: "ShelfXray MCP - Quick-Commerce Shelf Share for Brands"
description: "Keyless shelf reads from Blinkit, Zepto and Swiggy Instamart: brand coverage, ranks, sponsored slots and prices for two Indian cities, to August 2026."
category: "Retail"
stars: "n/a (vendor-hosted; dataset on darkstoreindex.com, CC BY 4.0)"
added: 2026-11-26
source: "official registry `in.shelfxray/shelf-data`; keyless initialize 200 as `in.shelfxray/shelf-data` 0.1.0 on https://mcp.shelfxray.in/mcp with a 5-tool tools/list and all five tools driven on 2026-11-26 (get_dataset_info, brand_shelf_snapshot on Sleepy Owl in Bengaluru, category_benchmark on Coffee in Delhi, search_rank_summary on protein bar, sponsored_slot_leaders on Coffee); dataset facts and licence read from the same payload and from darkstoreindex.com/data"
relevance: "★★"
tags: [retail, quick-commerce, shelf-share, india, brand-analytics, keyless, cc-by, remote-mcp]
last_updated: "2026-11-26"
---

# ShelfXray MCP

**Shelf share is the number every consumer brand argues about and almost none of them can produce for quick commerce.** A model asked which protein bar wins on Blinkit in Bengaluru will guess, or will repeat a press release. This server answers with a brand's rank per keyword, the share of stores it appeared in, how many paid placements it held, and the price band on the shelf, for Blinkit, Zepto and Swiggy Instamart in Bengaluru and Delhi NCR. It needs no key, it is honest that the data is a cached snapshot rather than a live read, and it ships under CC BY 4.0.

```
Server type:  Remote (Streamable HTTP)
Endpoint:     https://mcp.shelfxray.in/mcp     keyless, no account
Registry:     in.shelfxray/shelf-data
Server name:  in.shelfxray/shelf-data 0.1.0
              title "ShelfXray quick-commerce shelf data"
Tools:        5, read from a keyless tools/list and all five driven
Data:         cached public shelf reads, latest 2026-08-01, not live
Licence:      CC BY 4.0, The Dark Store Index
```

The `instructions` block sets the boundary before the first call: read-only, free, three platforms, two cities, three categories, and *"the data is a CACHED public snapshot, latest read 2026-08-01; it is not live. Always state the as-of date when quoting numbers."* That sentence is the difference between a citable figure and a made-up one, and it is the reason this guide leads with the date rather than the rankings.

## The five tools

| Tool | Arguments | What comes back |
| --- | --- | --- |
| `get_dataset_info` | none | as-of dates per read, row counts, platform and city coverage, licence, citation, download links, method |
| `brand_shelf_snapshot` | `brand`, optional `platform`, `city`, `keyword`, `category` | per-search rows for one brand: stores present, stores read, coverage percent, best and lowest rank, sponsored slots, read date |
| `category_benchmark` | `category`, optional `city`, `platform` | per platform: average distinct brands per search, result depth, share of store reads carrying an ad, sponsored slots among the top-8 brands, price median and range |
| `search_rank_summary` | `keyword`, optional `city`, `platform` | per platform and city: stores read, distinct brands, depth, ad presence, price band, ranked top brands |
| `sponsored_slot_leaders` | optional `category`, `city`, `platform`, `keyword` | brands ranked by paid placements owned, with each brand's share of the listed sponsored slots |

## The dataset, as it describes itself

`get_dataset_info` returned a payload that reads like a data card rather than a pitch:

- **Rows:** 430 brand-shelf rows, 54 search-summary rows, 96 distinct brands.
- **Platforms:** Blinkit, Swiggy Instamart, Zepto. **Cities:** Bengaluru, Delhi NCR.
- **Categories:** Baby care, Coffee, Protein & energy bars. **Keywords:** nine, from `baby lotion` to `protein bar`.
- **Reads:** rows were read on 2026-07-23, 2026-07-24 and 2026-08-01, and the read date is per city and platform rather than per dataset. Bengaluru on Swiggy Instamart was read 2026-07-23 while Delhi NCR across all three platforms was read 2026-07-24 and Bengaluru on Blinkit and Zepto was read 2026-08-01.
- **Licence and citation:** CC BY 4.0, *Source: The Dark Store Index, 23 July 2026 - 1 August 2026*, with CSV and JSON downloads published beside it.

Three statements in the method are worth repeating to any client who asks whether a missing brand is absent from the shelf: only the top 8 brands by store coverage per search are recorded, ranks are a floor because platforms cap result lists, and unread stores are excluded rather than counted as absent.

## One brand, read in one city

`brand_shelf_snapshot` with `brand: "Sleepy Owl"` and `city: "Bengaluru"` returned six rows over three platforms, with a summary of 6 searches present, best rank seen 1, average coverage 98.2 percent and 37 sponsored slots owned:

| Platform | Keyword | Stores present / read | Coverage | Best rank | Lowest seen | Sponsored | Read date |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Swiggy Instamart | cold brew coffee | 9 / 9 | 100% | 1 | 41 | 0 | 2026-07-23 |
| Blinkit | cold brew coffee | 9 / 9 | 100% | 2 | 36 | 1 | 2026-08-01 |
| Zepto | cold brew coffee | 9 / 9 | 100% | 2 | 26 | 0 | 2026-08-01 |
| Zepto | instant coffee | 9 / 9 | 100% | 5 | 30 | 25 | 2026-08-01 |
| Swiggy Instamart | instant coffee | 9 / 9 | 100% | 9 | 39 | 0 | 2026-07-23 |
| Blinkit | instant coffee | 8 / 9 | 89% | 10 | 36 | 11 | 2026-08-01 |

The six coverage values are five 100s and one 89, which averages 98.17 against the summary's 98.2, and the sponsored total of 37 is the sum of the `sponsored_slots_owned` column exactly (0, 1, 0, 25, 0, 11). **The row that matters is the fourth one:** a brand ranked 5th organically on Zepto's instant coffee search held 25 paid placements, more than it held on every other search in the city combined. That is the finding a brand team pays for, and it comes from one call.

## The category benchmark, and a rupee figure that needs a second look

`category_benchmark` on Coffee for Delhi NCR, read 2026-07-24:

| Platform | Avg distinct brands per search | Avg result depth | Store reads with any ad | Sponsored slots among top-8 | Median price | Price range |
| --- | --- | --- | --- | --- | --- | --- |
| Swiggy Instamart | 21.7 | 66.5 | 100% | 643 | 252 | 24 to 2,330 |
| Blinkit | 17.3 | 22.5 | 96.3% | 115 | 155 | 28 to 1,165 |
| Zepto | 14.0 | 13.7 | 77.8% | 176 | 99 | 2.16 to 819 |

The payload is careful about the median: it is the median of per-search medians in rupees of listed shelf prices, *"a shelf-price guide, not a market average"*. The figure that does not survive a sanity check is **Zepto's minimum of 2.16 rupees**, which is roughly two and a half cents for a coffee product. It is either a sachet sold at a near-zero promotional price or a parsing artefact, and the dataset gives no product-level row to settle it. Treat that cell as unverified, and note that the same call reports Zepto with the shallowest result depth of the three platforms at 13.7 against Instamart's 66.5.

## Sponsored placements, ranked

`sponsored_slot_leaders` on Coffee returned 1,982 sponsored slots among the listed brands and a leaderboard that reproduces to one decimal:

| Brand | Sponsored slots | Searches with sponsored | Share of listed slots |
| --- | --- | --- | --- |
| Continental | 347 | 12 of 12 present | 17.5% |
| Epigamia | 321 | 2 of 2 present | 16.2% |
| NOICE | 292 | 2 of 3 present | 14.7% |
| Maiva Fresh | 172 | 2 of 2 | 8.7% |
| Bru | 128 | 11 of 15 | 6.5% |
| TATA Coffee | 124 | 7 of 10 | 6.3% |
| Sleepy Owl | 105 | 9 of 15 | 5.3% |

Every share reproduces as the brand's slots over 1,982, for example 347 divided by 1,982 gives 17.51 percent against the payload's 17.5. The interesting structure is the pairing of slot count with the number of searches the brand actually appears in: Epigamia holds 16.2 percent of the category's sponsored placements while appearing in only two of the searches read, which is what a concentrated buy looks like, against Bru's 6.5 percent spread across eleven.

**A number that will confuse a reader if the filter is not stated:** `brand_shelf_snapshot` gave Sleepy Owl 37 sponsored slots for Bengaluru, while `sponsored_slot_leaders` gives it 105 for the category with no city filter. Both are correct and neither is comparable. Always print the filter beside the total.

## One keyword, three platforms

`search_rank_summary` on `protein bar` put The Whole Truth at rank 1 in Bengaluru on Blinkit with 100 percent coverage and 6 sponsored slots, RiteBite at rank 2 with 16, and Yoga Bar at rank 3 with 14, out of 9 distinct brands over 9 stores read, a result depth of 12 to 36 and a price band of 42 to 447 rupees around a median of 78. All nine stores carried at least one ad. On the same keyword, Swiggy Instamart's Bengaluru read covered 17 distinct brands at a depth of 87 to 94, which is the single clearest illustration of why a rank on one platform does not transfer to another: the same product competes in a list three times longer.

## Defects and limits, measured

1. **The dataset is four months old.** The newest read is 2026-08-01 and the tool says so on every response, but a reader who skips the `data_as_of` field will quote August shelf positions as current in late November.
2. **A brand summary is filter-dependent and does not say so in the summary block.** The `filters` object records the city, and the totals and the leaderboard will not reconcile when those differ.
3. **The Zepto coffee price floor of 2.16 rupees** is not explained by any field the tools expose.
4. **Only the top 8 brands per search are recorded**, so a brand's absence is never evidence of absence from the shelf, a limit the payload states in its own `limitations` array.

## Where it fits a business-answer system

Quick-commerce shelf position is a daily argument inside consumer brands, and the evidence usually lives in a screenshot someone took on their phone. This turns that into a dated, licensed, per-store table with the sponsored layer separated from the organic one, which is what makes a category review answerable in a chat window: "who leads, in which city, on which keyword, at what price, and who is buying the placements". Pair it with a marketplace or retail source and the same system can compare an online storefront's assortment against what actually reaches the dark-store shelf.

## Is this live shelf data?

No. It is a cached public snapshot whose newest read is 2026-08-01, spanning 2026-07-23 to 2026-08-01, and the server repeats that on every response. Quote the `data_as_of` date with any number.

## Can a missing brand be read as delisted?

No. Only the top 8 brands by store coverage per search are in the dataset, and unread stores are excluded rather than counted as absent, so absence from a row says nothing about the shelf.

## Is the sponsored count a spend figure?

No. It counts placements owned, not money spent, and the dataset says so twice. A brand's sponsored slot count says where it bought position, never what it paid.

## Connecting it

Add `https://mcp.shelfxray.in/mcp` as a remote MCP server. No key, no OAuth, no header. Call `get_dataset_info` first so the as-of date and the coverage are in the conversation before any ranking is quoted, then the tool that matches the question: `brand_shelf_snapshot` for one brand, `category_benchmark` for a category, `search_rank_summary` for a keyword, `sponsored_slot_leaders` for the paid layer.

## See also

- [External MCP server catalog](/hermes/mcp/servers/external/index.md) for the rest of the retail and data group
- [American Spend MCP](/hermes/mcp/servers/external/americanspend-mcp/) for the card-spending side of the same category question
