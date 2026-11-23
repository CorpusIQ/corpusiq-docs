---
title: "Moa MCP - Korean Prices Compared With Shipping"
description: "Twelve keyless tools over a Korean marketplace of 16,677 tumblers and 13 million products, comparing prices with shipping included."
category: "Commerce"
stars: n/a (vendor-hosted)
added: 2026-11-23
source: "submission #7872; keyless initialize, tools/list and four tools/call requests on 2026-11-23"
relevance: ★★★★
tags: [korea, marketplace, price-comparison, procurement, shipping, keyless, remote-mcp]
last_updated: "2026-11-23"
---

# Moa MCP

**Remote MCP server (Streamable HTTP, no authentication)** - twelve tools over a Korean marketplace that compares **total delivered cost**, not list price. Every row carries the item price, the shipping charge and the sum, plus the age of the price check. The server's own instruction to the model is a workflow: answer with one comparison link, let the person choose, then prepare an order sheet that the person completes and pays.

```
Server type: Remote (Streamable HTTP, no auth)
Endpoint:    https://moaibuy.com/mcp
Server:      moa 0.3.0, protocol 2025-06-18, Korean-language responses
Tools:       12 (answer_link, search_products, get_product, get_products, recommend_top3,
             check_offer, start_order, get_order_status, connect_shop, register_seller,
             upsert_seller_products, update_seller_offers)
Catalogue:   13,217,010 products claimed, 14 categories
```

## Why This Matters for Operators

A quote that ignores shipping is not a quote. On a 1,700 won item the delivery charge here is **3,000 won**, which is 176 percent of the product price, and the tool prints both numbers and the total on the same line so the asymmetry is visible. That is the whole proposition: for small-item purchasing, the delivered total is the only number that compares across suppliers.

The Korean market is a real sourcing base for hardware, packaging and office goods, and this is the first server in this catalogue that prices it from inside chat. It also carries a seller side, which makes it a two-sided surface rather than a scraper: a shop can be onboarded by URL alone.

## Measured Behaviour

Four calls were driven on 2026-11-23, all keyless. The server answers in Korean, so the guide quotes the figures as returned.

### A category count, then ten rows with totals

`search_products(q="텀블러")` returned **16,677** matching products and showed ten of them at a stated snapshot time, each with price, shipping and total:

| Item | Price | Shipping | Total |
|---|---|---|---|
| 슬림 미니 텀블러 150ml | 4,500 | 0 | **4,500** |
| 마이멜로디 쿠로미 스트로 텀블러 3P 세트 | 13,000 | 0 | **13,000** |
| 리락쿠마 스텐 빨대 텀블러 680ml | 25,900 | 0 | **25,900** |
| 헬로키티 올드스쿨 스텐 머그 텀블러 400ml | 35,000 | 0 | **35,000** |
| 텀블러 손잡이 핸들 900ml | 7,100 | 3,000 | **10,100** |
| 텀블러 보온병 스테인리스 원터치 | 24,800 | 3,000 | **27,800** |

Two things sit beside the rows and are worth more than the prices. First, a `cursor` for the next page, because ten of 16,677 is a sample. Second, a flag on the rows whose price check is old: *"오래된 값 3개, 고르기 전에 check_offer 로 다시 확인하세요"* (three stale prices, re-check before choosing). The cheapest row shows free shipping and the seventh row shows 3,000 won shipping on a 7,100 won item, which is the comparison the tool exists to make.

### One question in, one link out

`answer_link(q="3만원 이하 무선 이어폰")` returned a single comparison URL, a one-line summary, and the item ids in screen order:

```
국내 3곳 · 해외 2곳 비교 · 가장 싼 총액 4,700원 · 가장 빠른 도착 11월 24일
```

Five candidates, three domestic and two shipped from abroad, cheapest total **4,700 won** and the fastest arrival **November 24**, one day out. The design intent is stated in the response: hand the person that one link rather than a list of product URLs.

### One item, in full, and what the cheapest total actually was

`get_product(item_id="4eua7vbc")` returned the item behind the 4,700 won headline:

```
에어팟 프로 버즈 무선 이어폰 귀지 청소 솔 키트 · 1,700원 + 배송 3,000원 = 총 4,700원
갈래: 가전디지털 > 음향가전
규격: 원산지 수입산(아시아·중국) · 제조사 중국OEM · 모델 3975
판매: 모아(타이거버트) · 값 확인 2026-11-23T10:27:27+09:00 (값 확인 8시간 전)
사는 길: 모아에서 사기 · https://moaibuy.com/p/4eua7vbc
```

It is an **earbud cleaning brush kit**, not earbuds. The price, the shipping, the category, the origin, the model number, the seller and the price-check timestamp are all correct and all attached to the wrong product for the question asked.

### A stale price that says it is stale

`check_offer(item_ids=["dw7ke2fs"])` answered with the stored value and its age in the same sentence: *"1개 확인(11월 20일 00:00 · 3일 전 기준, 저장된 값)"*, total **27,800 won**, in stock, followed by *"도매처 답이 늦어 저장된 값으로 답합니다"* (the wholesaler was slow to answer, so this is the stored value). A procurement tool that tells you the age of its own answer is worth more than one that does not.

## Defects and Limits

- **Relevance does not respect the product class.** A query for wireless earbuds under 30,000 won resolved its cheapest row to a cleaning accessory, so "cheapest delivered total" was true of the accessory and false of the product the person asked for. Any agent routing this tool must read `get_product` before it reports a price, or it will quote a 1,700 won accessory as the cheapest earbuds.
- **The order path is a handoff, not a purchase.** `start_order` returns an order sheet link valid for 24 hours and a report to pass to the person; the tool description states it does not pay or place the order. It was **not driven in this pass** because it writes an order sheet, and the write path should not be exercised for a catalogue entry.
- **The seller tools are writes.** `connect_shop`, `register_seller`, `upsert_seller_products` and `update_seller_offers` change a shop's presence in the index and were not driven for the same reason. `connect_shop` is documented as free, keyless, and refresh-daily.
- **The language is Korean throughout.** Tool names are English, arguments and responses are Korean. An English-speaking operator needs the model to translate, which is a fair description of the surface but not of the prices.

### Does it need a key?

No. `initialize`, `tools/list` and all four `tools/call` requests answered **200** with no authentication header on 2026-11-23.

### How current are the prices?

Each row carries its own check time, and the answer says how old it is. Two of the ten rows in the sample were three to five days old and were flagged in the response, and `check_offer` re-asks the wholesaler on demand, falling back to the stored value with a plain explanation when the wholesaler does not answer.

### Can it quote a total for a multi-item purchase?

Only item by item. `get_products` accepts up to ten ids (fifty with a public key appended to the endpoint) and returns each total separately, and `start_order` takes one item id at a time with a quantity and options. There is no basket-level total call.

## See Also

- [Commerce and marketplace data sources in the external catalogue](/hermes/mcp/servers/external/)
- [Sweep report for November 23, 2026 (night)](/hermes/mcp/sweeps/sweep-november23-2026-night)
