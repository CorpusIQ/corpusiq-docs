---
title: "MCP Server Discovery - November 9, 2026 (Midday)"
description: "Midday sweep at a seven-hour gap: the canonical moved one slug rename, the feed carried seven cards, and two connectors are catalogued."
category: MCP Ecosystem
added: 2026-11-09
last_updated: 2026-11-09
source: "the mcpservers.org thirteen-sitemap canonical, the mcp.so feed read twice (plain and cache-busted), and the chatmcp/mcpso submission window #6986 to #7014"
tags: ["mcp server", "model context protocol", "discovery", "sweep", "november 2026"]
---

# MCP Server Discovery - November 9, 2026 (Midday)

Fired on the **10:00 MST** tick, seven hours after the night pass. The sitemap wave was a single slug rename, the feed carried seven cards, and the queue carried twenty-nine arrivals. Two connectors are catalogued: one prices a regulatory charge nobody quotes before the declaration, and one puts a priced proposal pipeline inside the chat.

```text
Canonical:   20,204 distinct server URLs from 63,649 raw <loc> entries across 13 maps
             (1 addition, 1 removal, which pair into a single slug rename)
Feed:        146,218 bytes plain, 146,253 cache-busted, 28 cards, 7 above the night stamp
Queue:       #6986 to #7014, 29 issues, no gaps, all arrivals
Catalogued:  2 servers, 2 guides
Evaluated:   36 candidates (29 queue arrivals plus 7 feed cards)
```

## The window, measured

The thirteen server maps, `servers/1.xml` through `servers/11.xml`, `priority-servers.xml` and `remote-mcp-servers.xml`, returned **63,649** raw `<loc>` entries and **20,204** distinct server URLs after the locale prefixes were stripped before the `/servers/` subset was taken. Against the night capture that is **1 addition and 1 removal**, and the pair is arithmetic rather than editorial:

```text
+ https://mcpservers.org/servers/nophish
- https://mcpservers.org/servers/nophi-sh-en-ai-agents
```

One product, one new slug, so the genuine arrival count for the window is **zero**. This is the third consecutive flat pass on the canonical, which is why the feed and the queue carried this window.

The mcp.so feed was read twice: **146,218** bytes plain and **146,253** cache-busted, **28** cards parsed on both reads with the same set. Seven cards sit above the night stamp `2026-11-09T06:14:44.864Z`:

```text
09:59:47Z  speedyindex-mcp-server
12:41:15Z  fokals
12:45:47Z  mapsemble
13:04:10Z  padel-expert-lab
13:41:38Z  nusii-mcp-server
14:00:35Z  aivikings-ai-mcp
16:30:43Z  bankingmcp-9749e1
```

The queue carried **#6986** to **#7014**, twenty-nine numbers with no gaps, every one an arrival and none a listing update. mcpservers.org `/all` answered **403** by edge policy, the standing condition since November 4 rather than a delisting.

## Catalogued: a border charge and a priced offer

- [CBAM Data MCP - EU Carbon Border Cost per Import Line](/hermes/mcp/servers/external/cbam-data-mcp/) - remote Streamable HTTP at `https://cbamdata.eu/mcp`, protocol `2025-11-25`, server `eu.cbamdata/cbam` **1.0.0**, submission `#7001`, **6** tools, and the rare tier where a keyless client can do real work: `initialize` answers **200** with all six tools listed, `cbam_status` answers with the dataset state (**572** scope rows, **10,910** default rows, latest price **EUR 82.32** for 2026-Q3), and `cbam_resolve` answers inside **3 free calls a day per IP** while the other four tools return `401` with the reason stated in the body. **Driven live:** 100 tonnes of CN `72085120` from China in 2026 returned **3.5057** tCO2e/t direct, **350.570** tCO2e total, a benchmark of **1.37** tCO2e/t on route C under Reg (EU) 2025/2620, a **97.5%** factor under Directive 2003/87 Art. 10a(1a), a free-allocation adjustment of **133.575** t, **216.995** t subject to CBAM, **217** certificates at **EUR 82.32**, and a total of **EUR 17,863.44**, every line tagged with the article that produced it. A four-digit heading is refused rather than guessed: `7208` returns `partial` and lists the twenty in-scope eight-digit children. The dataset carries the **2028** mark-up column (30% iron and steel, aluminium, cement and electricity; 1% fertilisers), the **50 tonne** de minimis, a `declarationDeadline` on the answer, and `meta.dataVersion` on every response. The OpenAPI document at `1.3.0` documents the free tier, the **50,000** calls a month on Developer, and a second regulation on the same shape, EUDR under Reg (EU) 2023/1115.
- [Nusii MCP - The Proposal Pipeline Inside the Chat](/hermes/mcp/servers/external/nusii-mcp/) - remote Streamable HTTP at `https://app.nusii.com/mcp`, feed card filed `2026-11-09T13:41:38Z`, 14-day trial with a 60-day money-back guarantee. A keyless `initialize` answers **401 Unauthorized**, and the protected-resource document names the resource `https://app.nusii.com/admin_mcp` with exactly two scopes, `admin:read` and `admin:write`, which is the tier: live, gated, scopes documented by the vendor, no keyless tool list. The surface is the proposal workflow rather than the signature: templates list, clients search, create a proposal from a template, update sections and line items, then read the pipeline (**12** sent, **5** accepted, **41.67%** acceptance, **4** pending in the vendor's own worked example). The design decision worth recording is where the assistant stops: the draft is prepared and the send stays with the person, which is the right boundary for a document that commits price. The vendor's State of Proposals 2026 report is built on **9,022** proposals sent in 2025 and states **50.2%** were accepted. Signature execution already has owners here in SignWell, SignSimple and Countersignatory; the priced proposal pipeline did not.

## Held, with the reason each one was held

- **BankingMCP** (feed card `bankingmcp-9749e1`, endpoint `https://banking-mcp.com/api/mcp`): read-only bank access across German, Austrian and EU institutions through PSD2 via finAPI, five tools (`list_accounts`, `get_balances`, `list_transactions`, `search_transactions`, `refresh_accounts`), **EUR 5** a month including VAT, 7-day trial, up to **50** accounts and **20** assistants, `accounts:read` as the only scope, no payment or transfer tool. A keyless `initialize` answers **401** with `invalid_token` and the protected-resource document at the app host. Held on the DACH PSD2 bank-sync class already recorded against Kontoflux, itself a regional variant of the catalogued Zenith. What it adds over that precedent, and the reason it is re-checked rather than closed: a flat price across up to fifty accounts, business and personal in one subscription, and property-management outputs the vendor demonstrates (a 2025 service-charge statement compiled from bank transactions). If the Kontoflux ruling loosens, this is the entry to promote.
- **Fokals** (`https://mcp.fokals.com/mcp`, feed 12:41:15Z): market and company intelligence, OAuth with a Supabase-hosted authorization server and a documented `connect` page, keyless `initialize` **401** naming the connector-key option. Held on the company-intelligence class at saturation, carried by Synorb, FinzData, SimilarLabs, Velarion, Xcout Intel, aVenture and Subastech, the last of those with a driven reversal test named.
- **SpeedyIndex** (feed 09:59:47Z): check whether URLs are indexed in Google, Bing or Yandex, submit links, read the balance. Held on the URL-indexing and rank-tracking class, which the catalogue already holds as a credits-per-call hosted SEO suite.
- **Maps Agent** (`com.maps-agent/knowledge`, #6998): guides, answers and a glossary about Google Business Profiles and Maps rankings, two read tools, each answer linking to its own page. Held on the local-SEO knowledge class owned by Cygnix SEO; it is a content surface behind an MCP handshake, not a data source.
- **Agent Data Hub** (`io.github.Jona1245/agentdatahub`, #7000): official statistics, central bank rates, FX and energy, keyless with a 1,000-call daily quota, and a provenance design that names source, licence and date on every answer. Held on the financial-statistics class covered by the catalogued Monitly and FXMacroData entries.
- **Duo Data Utilities** (#7011): 33 deterministic validators and codecs, IBAN, ISIN, CUSIP, SEDOL, VAT and tax IDs, GTIN, time zones and business days, slugs and transliteration, JWT and semver parsing, geohash and point-in-polygon. Held on the developer-utility class; broad and cheap, but nothing here is a business data surface.
- **SEO and Keyword Data API** (#7012) and **Social Media Data API** (#7014) and **Crypto Derivatives Data API** (#7013): three hosted data resellers from one publisher pattern, 44 SEO tools, 26 social tools and 10 perp tools. Held on the SEO-data class, the social-listening class per Octolens and the social-data class per CyberRedd and ScrapeAtlas, and the crypto-market-data class respectively.
- **monerometrics** (`io.github.nowi333/monerometrics`, #7010): 19 keyless read-only Monero network tools from the vendor's own node. Held on the crypto-metrics class.
- **Warden MCP** (`warden-protocol/warden-mcp`, #6999): `quote_swap`, `prepare_swap`, `execute_swap` and wallet session tools on Base, BNB Chain, Robinhood Chain, Arc and Solana. Held on the crypto-rail and agent-payments class carried by Base Payment Assurance, Brasil Data and AICryptoVault.
- **Alpha Bazaar Arena** (`ai.alphabazaar/arena`, #7004): a free paper-trading arena for agents with an optional free key to publish. Held on the trading class.
- **Droply** (`so.droply/droply`, #7003): publish an HTML page, Markdown report, CSV, SVG or multi-file site to a shareable link with password and search settings. Held on the publishing and hosting class; useful tooling, not a business data surface.
- **NateUI** (#6992): a themeable React and Tailwind UI kit served to coding agents. Held on the developer tooling class.
- **supabase-rls-check** (#6994) and **remote-contract-jobs** (#6995): a read-only Row Level Security review of an exported Supabase catalog, and a search over public remote job feeds. Held on the developer-security utility class and the jobs class respectively.
- **csv2zugferd** (`de.zugferd-tools/csv2zugferd`, #6991): a .NET tool that turns a CSV into a ZUGFeRD e-invoice. Held on the German e-invoicing class already carried by NormAPI, Factu and the ZUGFeRD and XRechnung trio.
- **Car Listing Check** (#6990), **ParHard courses** (#6993), **SuliHuli** (#6997), **ElectroAtlas** (#6996), **Padel Expert Lab** (feed 13:04:10Z) and **Mapsemble** (feed 12:45:47Z): automotive listing checks, golf courses, EV specs, the Russian EV market, a padel racket comparator and an interactive map builder. Held as consumer verticals and media tooling, outside operator scope.
- **Headshot Photo Check** (#7002) and **AiVikings.ai MCP** (feed 14:00:35Z): a photo-quality audit for job applications and a domain registrar. Held on the consumer-utility class per ProfessionalHeadshot.io and the registrar and payments infrastructure class.
- **Voidless** (`dev.voidless/voidless`, #7008): a prior disposition, held across three earlier sweeps on the media-generation and agent-address class.
- **The mambalabsdev fleet** (#6986 to #6989, #7005 to #7007, #7009): eight more one-tool npm packages wrapping Apify actors, ten of the family in this window counted with the two the night pass took, held on the standing Apify-actor hold class and the October 7 Mamba Labs fleet ruling. `mcp-tennis-match-data` also joins the sports-data vertical held beside Tennis Evolution.

## Core listing check, measured

The fresh canonical carries `/servers/corpusiq-io` and `/servers/corpusiq/corpusiq-docs`. mcpservers.org `/all` answered **403** by edge policy, the standing condition rather than a delisting. All four direct mcp.so slugs answered **404** (`corpusiq`, `corpusiq-io`, `corpusiq-mcp`, `io.corpusiq`), so that listing remains absent. Both Glama routes still answer **301** to their query pages, the routing change recorded on November 8. The Smithery registry query returned an empty set on this pass, which is a query-surface result rather than a delisting read, and the standing rule applies: never conclude absence from a search echo.

## Frequently asked questions

### Why is a slug rename reported as an addition and a removal?

Because the set difference is computed before anything is interpreted. `nophi-sh-en-ai-agents` leaving and `nophish` arriving is one product changing its slug, and pairing the two is what keeps a rename from being booked as churn in one direction and a wave in the other. The honest count for the window is zero arrivals.

### How is a keyless tier different from a documented tier?

A keyless tier can be driven, so the guide can quote a real answer: the CBAM calculation above is output, not documentation. A documented tier answers a handshake with an OAuth challenge and publishes its metadata, which proves the endpoint is live and describes the scopes, but every tool name comes from the vendor. Both are catalogued, and the guide says which one it is.

### Why hold a bank connector that looks useful?

Because the same slice, read-only DACH account access over PSD2, is already recorded against Kontoflux as a regional variant of Zenith. Cataloguing the second one with no new capability would inflate the class without adding a decision. The distinctions that could justify promotion are named in the hold, so a later pass does not have to rediscover them.
