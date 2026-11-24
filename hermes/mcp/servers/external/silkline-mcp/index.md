---
title: "Silkline MCP - 34 China Platform Data Endpoints"
description: "Public data from 34 Chinese social and e-commerce platforms as JSON, 285 endpoints, priced per record with the price shown before the call."
category: "Marketing"
stars: "n/a (vendor-hosted; no public repository)"
added: 2026-11-24
source: "Submission chatmcp/mcpso #7983 filed 2026-11-24T12:59:01Z; a keyless initialize on https://api.silklinedata.com/mcp answering 200 as silkline 1.0.0 with three tools; endpoint searches and the two keyless refusals driven 2026-11-24; the free demo route GET /v1/demo/weibo/hot called the same day; silklinedata.com, /pricing and /llms.txt read the same day"
relevance: "★★★"
tags: [china, xiaohongshu, douyin, weibo, taobao, e-commerce, social-data, market-research, pay-per-record, remote-mcp]
last_updated: "2026-11-24"
---

# Silkline MCP

**The Chinese internet is where a third of the world's product and purchase conversation happens, and almost no data tool reaches it: the APIs are closed, the pages are app-native, and the vendors that do sell access sell a subscription to a dashboard nobody can query.** Silkline sells the data as records over one HTTP API, with 285 endpoints across 34 platforms, and its MCP server puts the same catalogue in front of an agent: search the endpoints, read the price, then fetch.

```
Server type: Remote (Streamable HTTP)
Endpoint:    https://api.silklinedata.com/mcp
Auth:        Bearer API key, or the key in the path: /mcp/<your key>
Server name: silkline 1.0.0, protocol 2025-06-18
Tools:       3 (search_endpoints, call_endpoint, get_balance)
Pricing:     per record returned, per-record price printed per endpoint
```

## Discovery is open, execution is keyed

This is the cleanest version of that split in the catalogue, and it was measured rather than assumed:

- `initialize` and `tools/list` answer **200** with no credential.
- `search_endpoints`, the whole catalogue with prices, answers with **no key**.
- `call_endpoint` and `get_balance` refuse with `isError: true` and a message that is a remedy, not a wall:

> `no_api_key: No API key was sent, so nothing was run or charged. Add the header "Authorization: Bearer <your key>" to this MCP server's settings, or use the address https://api.silklinedata.com/mcp/<your key>. Create a key at https://silklinedata.com/keys. Searching endpoints works without a key.`

Nothing was charged for either refusal, and the refusal says so. That means an operator can evaluate the entire product (every endpoint, every price, every parameter) before creating an account, which is the opposite of the trial-then-learn pattern most directories carry.

## The platform list, from the server itself

Douyin, Weibo, Douyin Analytics, TikTok, Zhihu, Instagram, Xiaohongshu (RedNote), WeChat, Xingtu, Bilibili, YouTube, Pugongying, Huahuo, Reddit, TikTok Creative Center, Threads, TikTok Shop, JD.com, Kuaishou, Taobao, Douban, TikTok LIVE, Amazon, Douyin Shop, Telegram, Toutiao, Youku, IMDb, WeChat Index, X, 1688, AliExpress, China web search and Xianyu.

The commercial half of that list is the part this catalogue had nothing for. There is no other entry here that returns **Taobao**, **1688**, **JD.com** or **Xianyu** data, and no other that covers Xiaohongshu, Douyin, Weibo, Bilibili, Zhihu and the creator-marketplace platforms (Xingtu, Pugongying, Huahuo) in one interface.

## Prices are in the search result, not in a sales call

`search_endpoints` returns the rate card with the schema. Three measured examples:

| Endpoint | What it returns | Price |
|----------|-----------------|-------|
| `xiaohongshu/search` | Notes by keyword with title, body, author, likes, collects, comments, shares, cover, link | **$0.0018** per result, **$0.025** minimum per page |
| `pugongying/search` | Xiaohongshu bloggers with follower count, price quotes, median reads and engagements | **$0.0092** per result, **$0.0375** minimum per page |
| `taobao/search` | Products by keyword with title, price, discount price, sales text, shop, ratings, location | **$0.008** per result, **$0.036** minimum per page |

The vendor's pricing page agrees and adds the two facts a buyer needs: the lowest price per record is **$0.00023**, a request that fails on their side costs **$0**, and a new account gets **$0.30** of trial balance that works on **212 of the 285** endpoints. A 100-record Xiaohongshu keyword pull is **$0.18**; a 50-record Taobao search is **$0.40**. No subscription renews.

## Try it without a key at all

The vendor publishes one free demo route, and it answered:

```
GET https://api.silklinedata.com/v1/demo/weibo/hot   ->   200
{"data":[{"type":"hot","rank":2,"keyword":"129万一针抗癌药进医保","hotness":828298,
          "url":"https://s.weibo.com/weibo?q=..."}, ...]}
```

A live Weibo hot-search board with rank, keyword, heat and the source link, no account and no charge. It is the right demo for this product: it proves the pipeline reaches a platform that has no public API before anyone pays for a record.

## How does the billing actually work?

Each answer is `{ data, cursor, meta }`. While `cursor` is present there is more, and it goes back with the same request. The charge is the records returned times the endpoint's price, or the endpoint's minimum per page when that is higher, so a call that returns two records can cost the page minimum. `meta.charged_usd` carries what was actually billed, and the instructions say to keep `limit` small while exploring, a warning that reads like it was written after someone learned it the expensive way.

## Two details that will cost you a call if you assume

1. **The parameter is `endpoint`, not `endpoint_id`.** The instructions say "each result has the endpoint id to pass to `call_endpoint`", and the result field is `endpoint`, while the call's argument is also `endpoint` in `platform/mode` form (`xiaohongshu/search`). Sending `endpoint_id` returns `bad_input: endpoint is required` and charges nothing.
2. **`price_usd` changes its key by billing unit.** Some endpoints price per `result`, others per `item`, and each carries a separate `min_per_page_usd`. Read the key rather than assuming `result`.

## Who is behind it

Silkline publishes an OpenAPI spec, an `llms.txt` of 51 KB describing every endpoint for agents, a public status page per endpoint, a changelog of listed endpoints and price changes, and an on-site free demo. That is more transparency than most vendors in this catalogue offer, and for a pay-per-record seller it is the right kind: you can audit the price list without a conversation.

## How to connect

```
claude mcp add --transport http silkline https://api.silklinedata.com/mcp --header "Authorization: Bearer $SILKLINE_KEY"
```

The key goes in the header, or use the per-key path form `https://api.silklinedata.com/mcp/<your key>` if your client cannot send headers.

## What this guide can and cannot certify

Verified on 2026-11-24: the keyless handshake and all three schemas, the keyless catalogue search and the exact per-record prices quoted above, both refusal messages, the free Weibo demo response, and the vendor pricing and `llms.txt` claims about 285 endpoints and the $0.30 trial. Not verified: the accuracy or freshness of any returned record, because no keyed call was made; whether all 285 endpoints answer as documented; and how the platform terms of service treat resale, which is the operator's question to ask before building a product on it.

## Verdict

Most China data access is sold as a seat in a dashboard, which is useless to an agent and to anyone who needs the numbers inside their own system. **A per-record price with the price printed before the call is what makes a closed platform usable, and 285 endpoints behind one key is the first time this catalogue could answer a question about a Taobao listing.**
