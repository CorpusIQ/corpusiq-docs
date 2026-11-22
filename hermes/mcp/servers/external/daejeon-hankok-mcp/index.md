---
title: "Daejeon Hankok MCP - A Korean City Priced Per Item"
description: "8,627 places and 1,863 hair stylists across 42 Daejeon neighbourhoods, plus the ministry list of 564 subsidised-price shops with item prices."
category: "Local Data"
stars: n/a (vendor-hosted)
added: 2026-11-22
source: "chatmcp/mcpso submission #7805 filed 2026-11-22T09:40:39Z; keyless initialize, tools/list and five tools/call requests on 2026-11-22"
relevance: ★★★★
tags: [korea, local-search, restaurants, price-data, public-data, keyless, remote-mcp]
last_updated: "2026-11-22"
---

# Daejeon Hankok MCP

**Remote MCP server (Streamable HTTP, no authentication)** - a read-only guide to one South Korean city, served in Korean, with prices. Two surfaces sit inside it: the venue directory of 8,627 restaurants, cafes, hair and nail salons across 42 neighbourhoods, and a government list of 564 shops designated as good-value with their item prices.

```
Server type: Remote (Streamable HTTP, no auth)
Endpoint:    https://daejeon.ferrorium.com/mcp
Server:      daejeon-hankok 1.2.0, protocol 2025-06-18
Tools:       11, all read-only
Coverage:    Daejeon, 42 neighbourhoods, 8,627 places, 1,863 stylists
```

## Why This Matters for Operators

A city guide is only useful to an agent if the answer carries a price and a booking path. This one does both, and the price source is not scraped chatter: the good-value list is the Ministry of the Interior and Safety designation published on Korea's public data portal, and the response states its reference date.

It is also the first entry in this catalogue for a single municipality. That scope is the point rather than a limitation: one city, every neighbourhood priced, with stylists indexed by the treatment they specialise in.

## Measured Behaviour

Five calls were driven on 2026-11-22, all keyless and all in Korean. Figures below are quoted from the responses.

### The neighbourhood table decides what is queryable

`list_areas` returns a table of area codes against four business categories, and the counts are uneven in a way that matters:

| Area code | Neighbourhood | hair | nail | food | cafe |
|---|---|---|---|---|---|
| `dunsan` | 둔산동 | 68 | 62 | 80 | 84 |
| `eunhaeng` | 은행동 | 47 | 26 | 134 | 109 |
| `sintanjin` | 신탄진 | 104 | 27 | 93 | 84 |
| `gungdong` | 궁동 | 49 | 17 | 122 | 83 |
| `eoeun` | 어은동 | 10 | 3 | 45 | 47 |
| `jijok` | 지족동 | 14 | 3 | 14 | 23 |

An agent that asks for nail salons in 어은동 (three of them) gets a thin answer by construction, and it can see that before it asks.

### Search returns price, hours and the speciality

`search_places("마라탕")` returned **32** places. The first three rows, unchanged:

```text
탕화쿵푸마라탕 대전정부청사점 · 마라탕 · 청사서로 30 1층
  영업 매일 10:00-22:00 · 가격 2,100-16,000원
  대표: 마라탕 100g 2,100원, 사천훠궈마라탕 100g 2,100원, 마라샹궈 100g 3,200원
춘리마라탕 관저점 · 구봉로131번길 23 석영빌딩 2층
  예약가능 · 월-목 10:30-22:00, 금-토 10:30-23:40, 일 10:30-22:00
  가격 1,900-15,900원 · 주차 · 지역화폐 · 유아시설
최애마라탕 충남대점 · 궁동로18번길 53 2층
  영업 매일 10:00-24:00 · 가격 1,900-13,900원 · 지역화폐
  대표: 최애마라탕 1,900원, 토마토마라탕 2,000원, 최애마라샹궈 2,700원
```

Per-100g pricing, split opening hours by weekday, parking, local-currency acceptance and children's facilities all arrive in one line per shop. That is the shape a person deciding where to eat actually needs.

### The good-value list is the strongest surface

`events_and_deals(kind="deals")` returned the 착한가격업소 register: **564** designated shops in Daejeon with representative menu prices, sourced to the Ministry of the Interior and Safety via the public data portal, **reference date 2026-10-18**. Individual rows:

- 찐빵 500원, 단팥빵 500원, 슈크림빵 1,000원 at bakeries across 서구, 중구 and 대덕구
- 아메리카노 1,000원 hot and 1,500원 iced at two named coffee shops on the same street in 오류동
- 고기만두 1판 (10개) 3,000원 at a 만두 shop in 중리동

A price ceiling list with a government designation behind it is a different asset from a review score, and the response says which one it is.

### Stylists are indexed by treatment

`search_stylists` for 히피펌 in 둔산동 returned five designers, each with the shop, the other treatments they list, a photo count and a Naver booking URL:

```text
지유 실장   · 엘포엘헤어 대전둔산점 · 리프컷, 히피펌, C컬펌, 애쉬브라운 · 사진 255장
채이 디자이너 · 유엘헤어 대전둔산점   · 매트브라운, 레이어드컷, 히피펌, 허쉬펌 · 사진 274장
```

The booking link is the Naver booking item URL, not a home page, so the handoff lands on a slot selector.

## What It Cannot Do

- **The detail call is currently unreachable.** `get_place` refused both the bare id the search output implies (`2020254465`) and the prefixed form from the returned link (`p/food/2020254465`) with the message *가게를 찾지 못했다* (shop not found), while `search_places` itself returns links of exactly that form. Until that is fixed, the per-shop detail must be read from the search row.
- One city only. Daejeon, not Korea.
- Korean only. The tool descriptions are Korean and the responses are Korean; a non-Korean agent has to translate.
- Read-only, with no write path: the Naver booking links hand off to Naver to actually book.
- Opening hours and prices change. The server's own instructions tell the client to point people at Naver booking to confirm.

## Frequently Asked Questions

### Is this a Korea-wide directory?

No. It covers Daejeon's 42 neighbourhoods, with a national fallback in `search_places` that matches shop names and neighbourhoods outside the city rather than full detail.

### Where do the prices come from?

Two sources, both stated in the responses: the venue directory's own menu data for per-item prices, and the Ministry of the Interior and Safety good-value register published on the public data portal with a reference date of 2026-10-18 for the 564 designated shops.

### Does it need a key?

No. Eleven tools answered keyless on 2026-11-22.

## See Also

- [Local and regional data sources in the external catalogue](/hermes/mcp/servers/external/)
