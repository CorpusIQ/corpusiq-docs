---
title: "MCP Server Discovery - November 22, 2026 (Midday)"
description: "A window with no new products in the directory: five tools that each price something before it is bought, and one server that only answers with a header."
category: "MCP Ecosystem"
last_updated: "2026-11-22"
---

# MCP Server Discovery - November 22, 2026 (Midday)

Fired on the **10:00 MST** tick, the first pass after the night sweep that shipped KitScout, CoreHu GPU Cloud and Lowdown. The directory added **no new products** across the window: the union key set moved by one entry and that entry was a remote form of a slug already held. The material came from the submission queue and two feed cards, and the five that shipped have a common thread worth naming: each one states a price, a date or a regulatory deadline **before** anything is bought or sent.

## The window, measured

```text
mcpservers.org /sitemap.xml   200, sixteen maps named, TWELVE numbered server maps
raw <loc>, maps 1-12          37,241   against 37,102 on the night page's basis  (+139)
  servers/1  ..... 4,111 (-36)   servers/7  ..... 5,956 (+21)
  servers/2  ..... 2,528 (+23)   servers/8  ..... 2,683 (0)
  servers/3  ..... 2,979 (-10)   servers/9  ..... 2,586 (-25)
  servers/4  ..... 3,185 (-11)   servers/10 ..... 2,619 (0)
  servers/5  ..... 3,366 (-24)   servers/11 ..... 2,531 (0)
  servers/6  ..... 2,911 (0)     servers/12 ..... 1,786 (+201)
  the twelve sum to 37,241 exactly
priority-servers.xml            249 raw, 34 distinct keys
remote-mcp-servers.xml           15 raw,  1 distinct key  (fifteen locale forms)
distinct keys, union           23,435   against 23,434 on the newest stored capture (11:31Z)
URLs per key                    1.59
like-for-like diff             +1 addition, 0 removals
lastmod at or after 04:31Z       23 rows, one slug stamped five times in one second
```

The single addition is `https://mcpservers.org/remote-mcp-servers/clockwise`, a remote form rather than a product. The +139 raw entries against a key set that moved by one is a re-shard: servers/12 carried 201 more URL forms and servers/1, /5 and /9 carried fewer, while the set of products a reader can reach stayed where it was. `/all` was not read this pass, refusing by edge policy since 4 November.

## Feed and queue

mcp.so `/feed` answered **200 at 157,435 bytes**, 34 server anchors against 30 stamps, and **four cards** above the cutoff:

| Card | Stamp (UTC) | Disposition |
|---|---|---|
| `monk-trade` | 14:19Z | held, OAuth 401 with a protected-resource document, and the stock-research class is saturated |
| `metricraven` | 12:20Z | held, OAuth 401, analytics with revenue attribution behind an account |
| `fox-davidson-uk-mortgage-calculators` | 10:49Z | **catalogued**, fifteen keyless calculators |
| `esimx-mcp` | 06:11Z | **catalogued**, two keyless tools over a plan catalogue |

The chatmcp queue carried **45 arrivals**, #7792 to #7836, read with bodies in one authenticated call. Three were shipped, and the rest are dispositioned below.

## Shipped this pass

### FaxUp - the first fax entry in this catalogue

Submission **#7833**. Nine keyless tools, 62 countries, and a design choice worth copying: `send_fax` never sends. It returns a confirmation link and the server's own instructions tell the client to say the fax has not been sent. The measured calls: **62** countries with calling codes; `find_agency_fax_number("IRS")` returning **eight** numbers split by state because the IRS runs two CAF units (Form 2848 Memphis `+1 855-214-7519` for 25 states, Ogden `+1 855-214-7522` for the rest, source `irs.gov/instructions/i2848` checked **2026-11-12**, with the exclusion that electronically signed forms must be filed online); a three-page quote of **$2.99** with the whole pack ladder from 5 faxes at $3.99 to 100 at $39.99; a UK number accepted as a fax line with the national form `2079460958`; and a malformed number refused in band. Guide: [FaxUp MCP](/hermes/mcp/servers/external/faxup-mcp/).

### Fox Davidson - fifteen UK property finance calculators, all keyless

A feed card, not a queue arrival. Stamp duty at GBP 450,000 returned **12,500** in England and **17,750** in Scotland for a first-time buyer, both reproduced by hand from the returned bands. A buy-to-let stress test on GBP 250,000 at 4.49% reproduced three ways: interest 11,225 (250,000 x 4.49%), stress interest 13,750 (x 5.5%), ICR 1.50 and 1.22, gross yield 6.72%, then the loan ceilings of **244,364** at 125% ICR and **210,658** at 145%, each re-derivable from rent divided by threshold divided by stress rate. Bridging: a 306,000 gross facility, **38,713** total cost, 12.9% annualised, and a high net worth term check reporting both limbs false. Market rates dated to a reviewed **2026-11-18** with the Bank Rate at **4.00%** last changed **2026-11-05** and the next decision on **2026-12-17**. Every calculator carries the FCA authorisation line and the disclaimer inside the payload. Guide: [Fox Davidson MCP](/hermes/mcp/servers/external/fox-davidson-uk-mortgage-calculators-mcp/).

### Daejeon Hankok - reversing the night pass's hold, on evidence

Submission **#7805**. The night pass held this as "one Korean city" without driving it. Driven, the scope resolves different: **8,627** places and **1,863** stylists across **42** neighbourhoods, plus the Ministry of the Interior and Safety register of **564** subsidised-price shops with item prices and a reference date of **2026-10-18**. `search_places("마라탕")` returned **32** shops with per-100g prices and split weekday hours; `search_stylists` for 히피펌 in 둔산동 returned five designers with photo counts of 83, 255, 274, 210 and 41 and Naver booking links; `events_and_deals(deals)` returned the ministry list with 찐빵 at **500원** and 아메리카노 at **1,000원**. One defect recorded: `get_place` refuses both the bare id and the prefixed id its own search output prints, so per-shop detail is only reachable from the search row. The hold was a scope label, not a class conflict: the two Korean entries already held are business-registry and KYB surfaces, not local price data. Guide: [Daejeon Hankok MCP](/hermes/mcp/servers/external/daejeon-hankok-mcp/).

### CLIA Certificate Renewal Sentinel - an expiring certificate, dated

Submission **#7835**. Two tools over the quarterly CMS Provider of Services File. The free sample returned a complete record: certificate expiring **2027-10-19**, **332** days left at an `as_of` of 2026-11-21, the 42 CFR 493.37(f)(1) renewal window running **2026-10-19 to 2027-01-19** with status open and **59** days to close, and a CMS billing calendar pointing at 2027-04-19 and 2027-09-19. It also declares its own conflicts (`renewal_timing`, `waiver_alternative_sanctions`) and refuses to price the penalties, stating that the civil money penalty ranges are adjusted every year. The paid tool answered with an **x402 challenge**, 0.01 USDC on Base, alongside a documented `free_trial: true` allowance of three calls a day. Guide: [CLIA Sentinel MCP](/hermes/mcp/servers/external/clia-certificate-sentinel-mcp/).

### eSIMX - a plan catalogue, and the header it insists on

A feed card. Two keyless tools: `search_plans` returned **matched_count 37** for Japan over 7 days with the cheapest at **3.50 USD** for 3,072 MB and a 30-day plan at 3.80, and **30** matches for Portugal at 5,000 MB where the **Europe 5GB 30Days** plan at **4.80 USD** covers **39** countries and the Portugal-only plan costs the same. `compare_trip_options` priced a Japan 7-day plus South Korea 4-day trip at **7.80 USD** for one East Asia plan and one installation against per-country plans. The defect that matters for integrators: without the `MCP-Protocol-Version` HTTP header, `initialize` returns 200 and `tools/list` returns **HTTP 400 Unsupported or missing legacy protocol version**, and the `stops` array silently requires both `destination` and `min_data_mb` per stop. Guide: [eSIMX MCP](/hermes/mcp/servers/external/esimx-mcp/).

## Also identified this pass (not catalogued)

- **Monk.trade** (feed, 14:19Z) - stock research across actively traded US names with SEC filing links. Refuses keyless `initialize` at **401** with a `WWW-Authenticate` naming a protected-resource document and scope `read write`; held on the gate and on the saturated stock-research class that already carries fAlpha, BDE, Altair and ValuEdge.
- **MetricRaven** (feed, 12:20Z) - privacy analytics with revenue attribution across Stripe, Paddle, Polar, Lemon Squeezy and Creem, **53** tools. **401** with a protected-resource document and scope `read`, and the body names the accepted credentials (OAuth, an `mr_` account token, or a site secret key). Held on the gate.
- **NPDES Permit Renewal Sentinel** (#7836) - the sibling of CLIA from the same author, filed twenty seconds apart, applying the same regulatory-deadline pattern to US water-discharge permits. Held as one author fleet with one shipped; the CLIA surface is the one with a free sample that returns a complete record.
- **Storra for Brands** (#7825) and **Storra for Creators** (#7826) - two keyless endpoints over the same charity-story dataset, read-only and rate limited to 60 requests a minute per IP. Held as one product in two packaging forms rather than two discoveries.
- **TraceCheck** (#7812) - keyless agent-evaluation scoring on a Render host. Held on the agent-evaluation class this catalogue already owns.
- **EveryInfra** (#7806) - **714** data capabilities across 106 sources behind an API key. Held on the gate and on the API-aggregator class.
- **Right Suite** (#7808) - prices, copy and ads tested against 100+ simulated buyers. OAuth 2.1 with an account, so no measured run; held on the gate rather than on the idea, which is a first for this catalogue and worth re-testing when a keyless path appears.
- **Hellotracks** (#7834) - GPS tracking and job dispatch for field teams. OAuth, and the field-service class already carries ATLASS OS, STEADYWRK and DrillerDB.
- **Ad Spec Guard** (#7811) and **ADS Beast** (#7810) - the same author's ad-compliance and ad-workspace pair; the spec guard is keyless but the ad-ops class is carried by PaidSync and its neighbours.
- **Kaeso** (#7831), **Galon Cloud** (#7823), **Board as a Service** (#7827) - self-hosted or hosted platforms behind OAuth: an AI gateway console, a cloud console, and a Kanban workspace. No keyless read, so recorded rather than measured.
- **OpenClip** (#7828), **Charmotion** (#7819), **Makemancer** (#7832) - three media-generation surfaces; that class is saturated.
- **X2Chat** (#7820), **Fiko** (#7813), **Krevaya** (#7792) - messaging and social inbox platforms behind OAuth or a paid plan; Krevaya was already held by the night pass.
- **Lalawe** (#7822) - two tools that submit an event to a human-reviewed queue. Nothing to read.
- **Unsliced** (#7824) and **amber-confluence** (#7829) - local stdio packages, one for PDF slicing and one for self-hosted Confluence. Not driven.
- **GEO and SEO Readiness v2.2** (#7830) - a third-party version of a surface this catalogue publishes itself.
- **ChinaMedsCheck**, **ChinaDocCheck**, **EsimTao**, **MahjongHandbook**, **TbmLib**, **ChinaTaxCalc** (#7793 to #7798), **HenryCrawl** five (#7814 to #7818), **Agent Tollbooth 402** (#7799), **12happy** (#7800), **Piqline** (#7801), **jdx** (#7804), **nebula-memory** (#7807), **Postgres DBA** (#7809), **Christian Pure** (#7821) - all carrying the disposition the night pass recorded hours earlier: consumer verticals, Apify transport, the x402 mechanism, uptime monitoring, the ad-intelligence class, developer tooling, agent memory, devotional content.

## CorpusIQ listing status, re-measured

| Directory | Status | Evidence |
|---|---|---|
| mcpservers.org | **LISTED** | `corpusiq-io` and the docs mirror `corpusiq/corpusiq-docs` both in this pass's own capture |
| mcp.so | **LISTED** | `/servers/corpusiq-docs` answers **200** at 857,546 bytes |
| Glama | **LISTED** | `/mcp/connectors/io.corpusiq/multi-source-mcp` answers **200** at 729,087 bytes |
| Smithery | **NOT LISTED** (delisted) | re-measured 2026-11-22 18:05 UTC against the canonical URL: the listing page (`https://smithery.ai/server/corpusiq`, redirecting to `www`) answers **404** at 34,959 bytes and `registry.smithery.ai/servers/corpusiq` answers **404 "Namespace not found"** (the registry search endpoint returned **500** twice). The first pass logged a mistyped path variant; the verdict does not change. The loss was recorded at row level after Smithery shut its proxy and managed identity on 31 October 2026 and removed self-serve publish. No customer impact: no install path this project publishes depends on it |
| Anthropic Claude connectors | **NOT LISTED** | `scripts/anthropic_directory_watch.py` scanned 1,204 pages across 3, `listed=False`, exit 0 |

## What this pass says about the directory

A window can be flat and still productive. The canonical moved by one non-product entry, the feed produced two cards that earned guides, and the queue produced three. Every one of the five that shipped answered a price, a date or a deadline before asking for anything: a fax price before a send, a tax band before a purchase, an item price before a meal, a certificate expiry before a filing, a data plan before a trip. That is the shape worth cataloguing, and it is where the queue is pointing.
