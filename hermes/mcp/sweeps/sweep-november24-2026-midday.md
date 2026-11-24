---
title: "MCP Server Discovery - November 24, 2026 (Midday)"
description: "A directory that moved 113 entries and not one key, and three queue arrivals that were all driven: an exchange calendar, a statutory workday table and a China data API."
category: "MCP Ecosystem"
last_updated: "2026-11-24"
---

# MCP Server Discovery - November 24, 2026 (Midday)

Fired on the **10:00 MST** tick, seven hours after the night capture stored at **10:01Z**. The directory moved and did not grow: **113** fewer raw entries across the twelve numbered server maps with the distinct key set identical at **23,894** on both captures, which is the definition of a re-shard and not of a purge. The feed and the queue carried the window, all three ships came from the queue, and all three could be driven without a credential - a calendar with six keyless tools, a statutory workday table with two, and a China data API that opens its whole price list before it asks for a key.

## The window, measured

```text
mcpservers.org /sitemap.xml   sixteen maps named, TWELVE numbered server maps
raw <loc>, maps 1-12         37,656   night capture 37,769  (-113, composition)
  servers/1  ..... 4,165     servers/7  ..... 5,871
  servers/2  ..... 2,525     servers/8  ..... 2,736
  servers/3  ..... 2,946     servers/9  ..... 2,604
  servers/4  ..... 3,186     servers/10 ..... 2,584
  servers/5  ..... 3,287     servers/11 ..... 2,528
  servers/6  ..... 2,902     servers/12 ..... 2,322     sum 37,656 exact
distinct keys, maps 1-12     23,894   IDENTICAL to the night capture
URLs per surviving key       1.576    night 1.580
union with priority + remote 23,928   night 23,943
priority-servers.xml         252 raw, 34 keys
remote-mcp-servers.xml       15 raw, 1 key
lastmod, server maps         34,203 stamped rows
  at or after 10:30Z         147 rows -> 52 distinct keys
  repeats                    7 keys stamped 13-15 times inside one second
  newest stamp anywhere      2026-11-24T13:03:28Z
mcp.so /feed                 200, 160,797 bytes, 36 anchors, 30 stamps
  pairs                      30, 29 unique slugs
  above the cutoff           7
submission queue             #7966 - #8001, 36 filings
```

The re-shard reads cleanly once the keys are counted. Seven listings were stamped **13 to 15 times inside one second** (`browserstack/mcp-server`, `keboola/keboola-mcp-server`, `makeplane/plane-mcp-server`, `rad-security/mcp-server`, `kubeshark-mcp`, `GoogleCloudPlatform/cloud-run-mcp`, `mcp-server-qdrant`), the same signature this surface has shown on every re-shard since the locale forms were consolidated, and the raw fall of **113** with a held key set is that consolidation finishing, not a delisting. No removals are recorded because none were observed: every key in the previous capture is still present.

## Shipped (3, all from the queue, all driven keyless)

**Futures Clock** (#7990) at `https://mcp.futuresclock.com/mcp`, `initialize` **200** keyless as `china-futures` **0.1.0** on protocol **2025-06-18** with **six** tools. The answer that makes it worth an entry is the night-session attribution: SHFE on **2026-11-24** returns `night_session.civil_date 2026-11-24` against `trading_date 2026-11-25`, sourced to the SHFE holiday calendar with `last_verified 2026-09-29` and `rights_status approved_public_reference`. HKEX on **2026-12-25** returns `closed`, `Christmas Day`, `圣诞节`, sourced to an HKEX circular PDF. `trading_hours` on **shfe-cu** returns four sessions with an explicit `day_offset`, `offset_unit` and `anchor` on every open and close, and `contract_expiry` for **202612** returns `cu2612` with a last trading day of **2026-12-15** verified from `ContractBaseInfo20261120.dat` while leaving the first-notice day `unknown` rather than estimating it. Two gaps are recorded in the guide: `next_closure` answers `outside_coverage` for SHFE and CFFEX while **LME** resolves Christmas Day, and a product slug on `trading_day` resolves the night session but reports the day `not_published`.

**China Workday Calendar** (#7991) at the AWS `execute-api` endpoint, `cn-calendar` **1.0.0**, **two** keyless tools, **20** free calls per IP per day and a per-call x402 price after that. Every refusal is free and instructive: `invalid_arguments` names `date` or `from`/`to`, `range_too_large` enforces the **366-day** ceiling. The answers were checked against the State Council notice **国办发明电〔2025〕7号** of **2025-11-04**, fetched independently: **2026-02-14** to **2026-02-28** is **15** calendar days and **6** workdays around a nine-day Spring Festival, **2026-10-01** to **2026-10-10** is **3** workdays, and **2026-02-17** answers `春节` with the gov.cn URL. Its second tool answers package advisories from OSV: **lodash 4.17.20** returns **4** advisories with `fixed 4.17.21`, **requests 2.31.0** returns **6**. The defect recorded is that range answers carry `data_updated` but no `source_url`, while single-date answers do.

**Silkline** (#7983) at `https://api.silklinedata.com/mcp`, `silkline` **1.0.0**, **three** tools, and the cleanest discovery-open split in the catalogue: `search_endpoints` answers with no key and returns the whole **285-endpoint**, **34-platform** catalogue with its prices, while `call_endpoint` and `get_balance` refuse with `no_api_key` and the two ways to fix it, charging nothing. Prices are visible per endpoint: **$0.0018** per Xiaohongshu note with a **$0.025** page minimum, **$0.0092** per Xiaohongshu blogger, **$0.008** per Taobao product, a **$0.00023** floor, **$0** for a request that fails on their side and **$0.30** of trial balance on **212 of 285** endpoints. The free demo route returned a live Weibo hot-search board, which proves the pipeline reaches a platform with no public API before anyone pays.

## Also identified this pass (not catalogued)

Thirty-six queue filings and seven feed cards, held with the class or gate named. **ItalyCheck** (#7972) is the strongest: a keyless IndicePA lookup by codice fiscale with a **$0.01** x402 counterparty call, held because **Korea Business Verify** already carries the country KYB slot and **imperio-mcp** the Italian tax surface. **StickerByVIN** (#7994) on the VIN class (**CarDossier**, **Valid**, **CheckMyVIN**). **Signing for agents** (#7996) on e-signatures. **Sanchara** (#7992) on social publishing (**SocialBu**, **Sociality**) despite **13** networks. **Booking for agents** (#7995) on booking (**MainBook**). **E-Invoicing** (#7978) on the EU e-invoice shelf already carrying **Eleata**, **BeeL**, **gofact**, **Factur-X Orvel** and **Rechnungslotse**. **FiveSocket MT5** (#7973) and **AlphaSift** (#7987) on the crowded market-data and stock-screening class. **CiteAura GEO** (#7967) on the AEO class. **agent402** (#7989) and **tactica** (#7966) on the x402 lane. **Hearl** (#7998) on the **Octolens** listening class, now partly reachable through Silkline. **Great Work Labs** (#7999) on multi-model task hubs. **NoctHost** (#7986), **Gregale** (#7968), **Mergestorm** (#7970), **Lyriks** (#7979), **repomap** (#7977), **lockdocs** (#7976), **Inplain** (#7997), **IceScreen Touch** (#7982), **autologin-mcp** (#7975), **vwatch** (#7974), **claude-codex-orca-bridge** (#7988) and **LONG AI** (#7981) in the developer-tooling lane. **Train My AI** (#7971) on agent memory, **FreeMusic** (#7969) on music generation, **Brik** (#7980) on design tools, **Cupday** (#7984) as a sports-tournament vertical, **Connecty** (#8001) as a five-site status page and **Floppy** (#8000) as file sharing with read receipts. From the feed: **figment-mac-hosting** on mac hosting, **zerobounce** on the **MailTester** email-verification trio, **vibecode** (and its queue twin **#7993**) on app builders, **fatesign-bazi** as an astrology vertical, **ai-certificates** as exam preparation and **persado-mcp** on marketing copy generation. **dealmachine** re-entered the feed and already carries `external/dealmachine-mcp`, so it is a relisting.

## Listings

Re-measured on the five surfaces this pass. **mcpservers.org LISTED**: `servers/corpusiq-io` and `servers/corpusiq/corpusiq-docs` both sit in `servers/5.xml`, which is the evidence that matters because the detail page answers **403** by edge policy. **mcp.so LISTED**: `/servers/corpusiq-docs` answered **200** at **856,054** bytes with **59** corpusiq mentions, and the four guessed product slugs remain 404s, which is not a listing verdict. **Glama LISTED**: `/mcp/connectors/io.corpusiq/multi-source-mcp` answered **200** with the product name on the page. **Smithery LISTED**, on the narrowest route that still answers: the search surface `?q=corpusiq` returned HTTP **500** `{"error":"An unexpected error occurred"}` on three spaced attempts and both page routes (`/server/...` and `/servers/...`) returned **404**, but the direct record `GET https://registry.smithery.ai/servers/@benoit-p/Cprusiq` returned the object with `qualifiedName benoit-p/Cprusiq` and `displayName CorpusIQ`, read today at 17:12Z. A 500 on search is a provider error and the 404s are a route change, not a delisting; the record route is the evidence. **Anthropic** is still not listed: `scripts/anthropic_directory_watch.py` scanned **1,217** pages across **3**, zero hits, exit **0**.

### Why ship three of thirty-six?

Because each of the three answers a question the catalogue could not answer before, and each was measured rather than described. The exchange calendar names the trading date a night session belongs to. The workday table carries the make-up Saturdays that decide whether a delivery lands. The China data API is the first entry here that can return a Taobao or JD.com record, and it publishes its price list before it asks for a key. Everything else on the list either duplicated a class already carried or could not be driven from this egress.

### What did this pass not do?

No keyed call was made to Silkline, so no returned record was checked for accuracy or freshness; the guide says so. No Chinese exchange's `next_closure` answer could be tested for correctness because the tool declines to answer for those exchanges at all. The five listing surfaces were measured but no submission was made: nothing here was unlisted, so there was nothing to submit.
