---
title: "MCP Server Discovery - November 27, 2026 (Midday)"
description: "A 302-slug shard backfill with no stamp inside the window, ten feed cards, twenty filings, and two guides."
category: "MCP Ecosystem"
last_updated: "2026-11-27"
---

# MCP Server Discovery - November 27, 2026 (Midday)

Fired on the **10:00 MST** tick, **five and a half hours** after the baseline capture on disk, into a window whose size had to be measured twice because the two usual arrival signals disagreed. The thirteen numbered server maps returned **38,769** raw `<loc>` entries against **38,251** at the night read, the per-map distinct counts held on maps **1** through **12** and rose only in `servers/13` (**528** to **830**), and the keyed union moved **24,528** to **24,830**: **302 additions and 0 removals**, all of them inside the newest shard. The `lastmod` window returned **one** row and it is not one of them.

## The window, measured

```text
mcpservers.org /sitemap.xml   200, 17 maps named, 13 numbered server maps
raw <loc>, maps 1..13         38,769   (night read 38,251)
  servers/1  ..... 4,120      servers/8  ..... 2,791
  servers/2  ..... 2,525      servers/9  ..... 2,616
  servers/3  ..... 2,957      servers/10 ..... 2,578
  servers/4  ..... 3,181      servers/11 ..... 2,497
  servers/5  ..... 3,356      servers/12 ..... 2,424
  servers/6  ..... 2,878      servers/13 .....   947
  servers/7  ..... 5,899      sum ............ 38,769 exact
distinct keys per map        1,987 / 1,990 / 1,994 / 1,999 / 1,996 / 2,000 x7 / 830
server-map distinct slugs    24,796   (night 24,494, +302)
priority-servers.xml         250 raw / 34 keys
remote-mcp-servers.xml        15 raw /  0 matched server keys
union of keyed slugs         24,830   (baseline 24,528)
set diff vs 20261127_0435    +302 additions, 0 removals
lastmod rows, server maps    35,230
  at or after 11:35:00Z            1 row, a held slug, stamped 11:52:23Z
  newest anywhere            2026-11-27T11:52:23Z
```

**The 302 are a shard backfill, and the stamps say so.** Every one of the 302 arrival slugs carries a `lastmod` of **2026-11-27**, and **265** of them sit inside a single hour, **00:19Z to 00:59Z**, with a thin tail from **01:00Z** to **11:05Z**. Not one is at or after the baseline capture's **11:35Z**, so a detector keyed on the stamp cutoff reports **zero arrivals** against a shard that gained **302 products**. The signal that held is the one that has held through the last six shapes: the **per-map distinct count**, here `servers/13` moving **528 to 830** while maps **1** to **12** did not move at all, and the raw count inside the same shard rising **528 to 947**. Raw and distinct rising together is a shard filling; raw rising while distinct falls is a re-shard; a raw fall with a key rise is a locale prune. This pass is the first.

## The feed turned over ten cards

`mcp.so/feed` answered **200** at **157,756** bytes with **35** anchors, **35** distinct slugs and **28** paired stamps, the bottom seven anchors being the unstamped popular block rather than cards.

| Card | Stamp (UTC) | What it is | Disposition |
|---|---|---|---|
| `corsair` | 16:59 | One MCP URL for Gmail, Slack, GitHub, Notion and 700+ apps with rules on every action | Held, agent-gateway class |
| `my-job-fleet` | 16:11 | Job search tooling | Held, job-search class |
| `tekyous` | 16:00 | Tech stack diagrams, developer tools catalogue, stack recommendations | Held, developer tooling |
| `aperiodic-market-data-for-tokenized-assets-crypto` | 15:13 | Market data for tokenised assets | Held, crypto market data (saturated) |
| `oylist` | 13:45 | Directory listing | Held, directory class |
| `mailmergic` | 12:59 | Agent mail | Held, email class (postkeep, Voidmail precedent) |
| `outscraper-mcp-google-maps-business-data` | 12:16 | Business data across Google Maps, reviews and enrichment | **Catalogued** |
| `urldone` | 12:04 | Link utility | Held, utility class |
| `quantbloc` | 10:57 | Quantitative data | Held, finance data class |
| `abwatcher` | 10:55 | Monitoring | Held, monitoring class |

The Outscraper card is the same product the shard carried, which is worth noting because it is the first time this window has produced two independent surfaces pointing at one entry: the canonical slug arrived on the backfill, and the feed card stamped **12:16Z** confirmed it twelve minutes after the capture. Its endpoint, its twenty-nine tools and the gate that refuses every call without a token are the subject of the guide below.

## The queue carried twenty filings

`chatmcp/mcpso` issues **#8226** to **#8245**, the newest filed at **16:44:48Z**, read with titles and bodies. The distribution is the usual one: two fleet publishers, a handful of single-tool wrappers, and one product that became a guide.

| Issue | Product | Disposition |
|---|---|---|
| #8226 | Cadabra AI (30+ media engines behind one credit balance) | Held, media-generation aggregator class |
| #8227 | TruceHQ (AI mediator, free for agents, per-side fee for people) | Held, legal and dispute class |
| #8228 | Fuel (integration layer) | Held, integration class |
| #8229 | Creafex Lab, four remote servers | Held, publisher fleet |
| #8230 | alephlo (classifieds) | Held, classifieds class |
| #8231 | BPMN-Pilot (process modelling) | Held, workflow modelling |
| #8232 | SimOwl travel eSIM | Held, consumer travel |
| #8233 to #8237 | mambalabsdev five: Spain company directory, Europages suppliers, SEC Form 4 insider trades, sanctions list screening, HubSpot and Salesforce partner directory | Held, one-tool-per-actor fleet (now five waves) |
| #8238 | RBAi CLI | Held, local CLI package |
| #8239 | Vulnpocalypse | Held, security scanning |
| #8240 | VektorScan | Held, vector and embedding tooling |
| #8241 | Sway (AI visibility with live WordPress and GitHub fixes, undo built in) | Held, AI-visibility class |
| #8242 | EQVector | Held, vector and embedding tooling |
| #8243 | **IRS Mileage Rates** | **Catalogued** |
| #8244 | Checkers Sixty60 shopping | Held, regional retail |
| #8245 | Internal Systems Gateway | Held, internal gateway |

## Two guides

- [Outscraper MCP - 29 Business-Data Tools, One OAuth Gate](/hermes/mcp/servers/external/outscraper-mcp/) - **discovery open, every call gated.** `initialize` answers **200** as `outscraper` **1.0.0** on protocol **2025-03-26** and a **29-tool** `tools/list` answers with no credential, covering Google Maps places, reviews, photos and chain data, contact and email enrichment, phone validation, company firmographics, Yellow Pages, Trustpilot, Tripadvisor, Booking.com, Indeed, Google Search and BuiltWith. Four `tools/call` attempts, on a read tool, a preview tool, the service router and the pricing tool, each answered **200 with `isError: true`** and *"Authentication required: provide a valid OAuth access token."* The protected-resource document names **four scopes**, `businesses.read`, `profile.read`, `requests.read` and `services.run`, which is the split that lets an assistant research while a person keeps the right to spend. **Two defects recorded:** the registry publishes the remote as `mcp.outscraper.com/mcp`, which answers **404** HTML to a JSON-RPC initialize, while `api.outscraper.com/mcp` answers **200** with the same request, so a client following the record literally reports a dead server; and five tool descriptions advertise a **free masked preview** that refused without a token exactly like the billable tools, so the free tier is either allowance-based inside an account or written for the paid path and reads as anonymous to anyone browsing. The design worth carrying is the router: `discover_services` then `get_service_schema` then `run_service`, with `pricing_get` able to price a scenario and `balance_get` to read the account, so an assistant can answer "what would this cost" before spending.
- [Ogarnio Mileage Rates MCP - IRS Rates Priced by Date](/hermes/mcp/servers/external/ogarnio-mileage-rates-mcp/) - **the first tax-rate surface here, keyless and fully driven.** Four tools, all `readOnlyHint: true`: `get_mileage_rate`, `list_mileage_rates`, `calculate_deduction` and `mileage_log_requirements`. **Eight calls were made** and the arithmetic reproduces by hand: two entries of **100 miles**, on **2026-06-15** and **2026-07-15**, returned **72.50** and **76.00** for a total of **148.50**, because the business rate moved from **0.725** to **0.76** on **1 July 2026** and each drive is priced on its own date, where a single annual rate would have answered **145.00** or **152.00**. **The charity rate is the detail that proves the data is read rather than interpolated:** **0.14** with `in_force` from **2023-01-01**, because 26 U.S.C. 170(i) sets it by statute rather than annually. A date past the last published period returns the latest rate marked **`provisional`** with the reason attached (*"it usually announces the next year's rates in mid to late December"*), and every answer carries a `source` block naming the IRS, the URL and a **verified** date. The vendor ships a second, account-scoped connector on the same host for reading a real mileage log with read-only or read-and-sort grants, previews before any change and a connected-agent history, so the address is the product: the free rate table and the account log are different endpoints.

## Also identified this pass (not catalogued)

The **302-slug backfill** decomposes before it triages: **101** are namespaced `owner/repo` slugs and **201** are single-segment vendor or product slugs of the `domain-form` shape, with **eight** `github-com-...-tree-main` route captures inside that second group; the fleets are broken out below. Every candidate was checked against the catalog index in both slug and space form before a hold was written.

- **ColdIQ** (`com.coldiq/mcp` **1.0.0**, `https://mcp.coldiq.com/mcp`) is held on **documentation, not merit**: the server answers **401** with a complete `resource_metadata` pointer, the protected-resource document names three scopes (`coldiq:read`, `coldiq:write`, `coldiq:execute`), and the RFC 8414 document is complete, with code as the only response type, S256 only, refresh tokens, and `client_id_metadata_document_supported: true` plus the authorization-response `iss` parameter. But `docs.coldiq.com` returns **NXDOMAIN** and the reader proxy refused the marketing path with a **401 bad-IP** notice, so no substantive capability claim could be sourced and none was written. It is a first target for a pass with a documented path.
- **Corsair** (`dev.corsair/mcp`, `https://mcp.corsair.dev/mcp`) answers **401** with `{"error":{"code":"unauthorized","message":"sign in to Corsair"}}` and a `resource_metadata` pointer whose document names a **separate authorization server** at `hub.corsair.dev/mcp-auth`, a WorkOS-shaped grant list that includes `urn:workos:agent-auth:grant-type:claim` beside authorization code, refresh and JWT bearer. Held on the **agent-gateway class**: one URL for 700+ apps with per-action rules is a gateway, and the catalog has carried gateways as holds since Switchyard and agents-room.
- **Sway** (`ai.getsway/sway`) is the strongest hold of the queue and it is held on the **AI-visibility class** already carried here by geolint, LogNorm, Agitech and 1Alexander. Its distinguishing feature is that it does not stop at measurement: `ship_fix` and `undo_ship` make text changes live on a connected WordPress or GitHub site, and `fix_results` re-measures whether the change moved the answer. Recorded for the class owner's benefit, not catalogued tonight.
- **gscdump** (`com.gscdump/mcp` **1.1.0**, `https://gscdump.com/mcp`) is the third Search Console surface to arrive and the class is already carried by two: scopes `mcp:read`, `feedback:write`, `sites:connect`, `indexnow:write`, `annotations:write`, so the interesting part (an IndexNow write scope beside a read scope) is noted and the entry held.
- **united-compute/gpu-price-tracker** is held on the **GPU pricing class**, which `gpufinder-mcp` and the November 26 GPU Cloud Prices entry already carry, and **`zillodata/zillow-mcp-server`** on the **real estate class** carried by Zillapi.
- **`usefulapi-io`** shipped **ten** connectors in this wave (Buildium, eDesk, Follow Up Boss, Hostaway, Housecall Pro, JobNimbus, Less Annoying CRM, Recruitee, Teamleader Focus, Wincher), which is one publisher wrapping one SaaS per server: held as a **publisher fleet**, with the CRM and property-management classes already covered.
- **`cotlet-connect`** shipped **three** (`gentu`, `nookal`, `semble`) on top of the **Cotlet MCP** already catalogued, so the fleet is an extension of a catalogued product rather than three arrivals.
- **`mambalabsdev`** appears twice in one window, five on the shard and five in the queue, for ten wrappers covering Spain's company directory, Europages suppliers, SEC Form 4 filings, sanctions screening, HubSpot and Salesforce partner data, UK Companies House, India MCA records, US building permits, BBB business search and a Discord server directory. Held under the standing **one-tool-per-actor** ruling, now in its fifth wave; the sanctions-screening and SEC Form 4 items remain the two worth a future probe if the ruling is ever relaxed.
- **`scorematic`** shipped **three** (`mcp-us-tariff`, `mcp-sec-edgar`, `mcp-uspto-trademark`): tariff codes are carried by Codixio and the customs-tariff entry, and SEC filings by the holdings already recorded, so all three are class-covered.
- **`apimodels`** (`api.apimodels.app/mcp`, with sibling design and transcribe routes) is a media-model marketplace, held on the **media-generation aggregator class** alongside Varosity and Superpowers; **`mcpcheck`** and **`mcpcheckup`** are MCP trust-scanning tools, held on the **meta-tooling class**; **`tekyous`** is developer tooling; **`koru`** arrives as three distinct products under one word (a DNS filter, a team AI layer and an open-source notes app), held on the **notes and knowledge class**.
- **`apex-engine-dev/apex-verify`**, **`cipherweave/cavalry-mcp`**, **`adepoco/clearrun`** and **`handlesapi/mcp`** are read from the slug only, with no registry record found for `clearrun`, so nothing is claimed about them; **`signalcheckerhq/mcp-server`** resolves through the registry as `org.signalcheckerhq/signalcheckerhq` **1.0.1** and is a crypto signal checker rather than a business surface, so it is class-held. **`founden-bot`** shipped two healthcare price indexes (GLP-1 and TRT clinic pricing), both held on the health vertical, and **`tjldc`** shipped three consumer tools held together.

## Listings re-measured

- **mcp.so** `/servers/corpusiq-docs` answers **200** at **857,333** bytes with **175** `corpusiq` occurrences, against **856,208** at the night read.
- **mcpservers.org** `/servers/corpusiq-io` answers **403** with the Cloudflare interstitial, the edge policy recorded since November 4 rather than a delisting.
- **Official registry** `io.corpusiq/multi-source-mcp` carries four records to **1.0.3**, all `active`, with a streamable HTTP remote at `https://mcp2.corpusiq.io/mcp`.
- **Glama** answers **200** and the listing resolves at `/mcp/connectors/io.corpusiq/multi-source-mcp`, the connector route that replaced the old encoded server path.
- **Smithery** is **unmeasured this pass**: `registry.smithery.ai/servers?q=corpusiq` returned **HTTP 500** with an error body on two attempts, and `smithery.ai/server/@benoit-p/Cprusiq` answered **404** with a 34,959-byte body. A refused API and a client-rendered 404 are not evidence of a delisting and are recorded as unmeasured.
- **Anthropic Claude connectors directory**: the watch script scanned **1,227** pages across three result pages and found **zero** matches, unchanged. The submission filed on November 16 is still in review; status lives only in the portal at `claude.ai/directory/manage`.
