---
title: "MCP Server Discovery - November 3, 2026 (Midday)"
description: "Midday sweep: a private-credit graph with filing citations and a licence-key server, 29 submissions and 18 endpoint probes dispositioned."
last_updated: 2026-11-03
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-november3-2026-midday"
tags: ["mcp server", "model context protocol", "hermes mcp", "sweep"]
---

# MCP Server Discovery - November 3, 2026 (Midday Sweep)

## Summary

Thirteen hours after the night pass, and the three surfaces split three ways. The mcp.so `/feed` had turned over by three cards. The mcpservers.org `/all` newest page had not moved at all, its counter sitting on **19,145** across both reads and thirteen hours. The submission window carried everything else: **29** submissions between **#6651** at `04:20:13Z` and **#6679** at `16:42:22Z`, read with bodies in one authenticated call, because the night pass had recorded that it skipped that window.

Two arrivals earned guides and they sit at opposite evidence tiers. **DFX Intelligence MCP** was driven keyless through six of its twenty tools: a BDC tape with **1,922** positions across **629** borrowers, a pension plan's own commitment disclosure, and a research call that answered `UNKNOWN` rather than invent a number when it could not resolve the subject. **SunLicense MCP** answered a measured **401** and is documented from the vendor's own pages: an entitlement surface for software you sell, with twelve store adapters and a per-person OAuth consent screen.

One reading rule held rather than being rediscovered. The `/all` page returned the same counter and the same twenty-seven slugs on both reads, which is a genuine zero-churn pass and not a stale proxy, because the counter and the slug set agree with the night pass. The two-read rule stays in place; a pass only counts as zero-churn when both reads match the prior window as well.

## Sources Swept

| Source | Read | Result |
| --- | --- | --- |
| chatmcp/mcpso submission window | authenticated `gh api`, bodies included, one call | **29** submissions **#6651** to **#6679**, none of them read by the night pass |
| mcp.so `/feed` | direct with a browser UA | **3** cards above the night stamp of `2026-11-03T08:51:34Z`: `CueHQ` `16:58:20Z`, `Angelcam` `15:28:13Z`, `Translayte` `14:23:37Z` |
| mcpservers.org `/all` | r.jina.ai with `X-Return-Format: html`, read twice | **19,145** on both reads, **27** unique slugs, all inside the night pass dispositions, zero churn |
| Endpoint probes | keyless JSON-RPC `initialize` plus `tools/list` | **10** answered **200** (`dwelldelta` **7** tools, `fondatoria` **8**, `legitreviews` **7**, `Finekot API` **99**, `klar-daheim` **5**, `spectra` **6**, `peornot` **3**, `ipo-radar` **4**, `sofala.market` **5**, `clanksquare` **2**), **8** answered **401** (`calven`, `skael`, `elaichi`, `frostbyte`, `gracker`, `mailazy`, `askeditor`, `agent-outbox`), one **401** on `breakthroughsales.io` with OAuth scopes, one **401** on `api.sunlicense.com` with an RFC 9457 problem body |

## New Servers Catalogued

### DFX Intelligence MCP - Private Credit With Citations

Relevance: HIGH. **Tier 1, driven** (`initialize` **200** as `dfx-real-estate` **0.16.0**, title DFX Intelligence, **20** tools listed, **6** called live, all six answered).

The endpoint is a graph of private capital with a question interface on top. `research` takes a whole question, plans the reads it needs, and answers from the rows it read with no model in the path: every answer carries `llm_calls`, the operations it ran and the accession number behind each claim.

`get_credit_provider` on ARES CAPITAL CORP returned the tape at **2026-09-30**: **1,922** positions over **629** borrowers, fair value **$29,212.6 million** on the BDC's own SEC-filed total, principal **$23,063.0 million**, cost **$29,477.5 million**, unfunded **$4,878.3 million**, debt share **75.76** percent, first lien **57.75** percent, **1,504** facilities, **54** sponsors financed, **18** quarters from **2021-12-31**, where the first quarter reads **1,112** positions, **390** borrowers, mark on cost **0.9863**, **121** PIK positions and an average spread of **6.27** percent. `search_allocator_commitments` for CalPERS returned **$2,000,000,000** committed to CV Consortio Fund L.P. through Valor Equity Partners with the basis `printed`.

Two behaviours decide the entry. A `research` call naming an entity it cannot resolve returned state `UNKNOWN`, zero claims and the sentence that it does not answer rather than guessing. And every record prints its own caveats: principal is a lower bound of what the BDCs on the tape hold, a mark below cost is the lender's mark rather than an impairment, and a spread that moved between quarters is an observed term change until the amendment document is on the graph.

It earns a guide because the slice was empty. All **1,092** guides held nothing for private credit, BDC, CMBS or allocator commitments; the institutional market data entries read public markets, [X1 Wealth](/hermes/mcp/servers/external/x1-wealth-mcp/) reads family office records as one investor type, and the EDGAR surfaces read what a company reported about itself rather than what its lenders reported about it.

Guide: [DFX Intelligence MCP](/hermes/mcp/servers/external/dfx-intelligence-mcp/)

### SunLicense MCP - License Keys for What You Sell

Relevance: HIGH. **Tier 2, documented** (`POST` to `https://api.sunlicense.com/mcp` returned **HTTP 401** with `resource_metadata` and a problem body naming the next step; no tool called, because the connection needs an account).

The product is entitlement for digital goods, which is the gap between a sale and a licence. The tool surface mirrors the CLI: `integration_status`, `create_product`, `create_policy` with a machine limit, `sdk_snippet`, `create_api_key`, `issue_license`, then suspend, reinstate, revoke, rotate, free a machine, block a leaked key and read check statistics, with keys masked until someone asks to reveal one.

The vendor publishes the per-store mechanics, which is what makes it usable rather than theoretical: BuiltByBit writes the key into the download, SpigotMC issues one per buyer, Gumroad and Lemon Squeezy use their own key from the receipt, Payhip and itch.io and Ko-fi use a redeem page, Stripe shows the key at checkout, WooCommerce revokes on refund, and Envato turns CodeCanyon purchase codes into licences. Seven SDKs cover Java, JavaScript, Python, .NET, PHP, Lua and Rust.

The controls are stated plainly: the consent screen shows the app, the destination and the organisation, permissions are ticked individually and can never exceed the person's role, changes are attributed on the licence page as issued by the AI assistant, the app receives only tool names and arguments and never prompts or code, tokens are stored as one-way hashes, and a disconnect takes effect within **30** seconds. The connector is on every plan: **50** AI assistant calls a day on Free, **300** on Lite, **3,000** on Standard, shared with the CLI, reset at **00:00 UTC**.

It earns a guide because both licence neighbours do different jobs: [GumroadDNA](/hermes/mcp/servers/external/gumroad-dna-mcp/) toggles keys inside one store, and [LicenseGuard](/hermes/mcp/servers/external/license-guard-mcp/) evaluates open-source dependency licences for code you consume.

Guide: [SunLicense MCP](/hermes/mcp/servers/external/sunlicense-mcp/)

## Read and Held

**One close call, held on class with the pricing read.** `Breakthrough` (`#6676`) answered **401** with `Bearer scope="openid profile email offline_access"`. It is a connector plus a plugin that feeds an agent only the slice of a living sales playbook each request needs, per-person and org-scoped, it never posts or sends on the user's behalf, and the pricing page reads **$0** for 50 credits a month per user and **$40** per user a month billed annually or **$50** monthly for 200 credits, with an on-prem option on your own models. It is held because the playbook-from-calls slice already has three entries: [Dealwize](/hermes/mcp/servers/external/dealwize-mcp/) from meeting transcripts, [ClosedLoop AI](/hermes/mcp/servers/external/closedloop-ai-mcp/) from calls and tickets, and [Backengine](/hermes/mcp/servers/external/backengine-mcp/) serving call context to revenue teams.

**Held on a measured 401.** `Calven` (`#6667`, GTM context with sources) on the competitive-intel and messaging class carried by [Klarix](/hermes/mcp/servers/external/klarix-intelligence-engine-mcp/) and [Debriefing](/hermes/mcp/servers/external/debriefing-mcp/); `Skael` (`#6668`, German B2B lead lists from the Handelsregister, Maps, job boards and imprints) on the lead-generation class carried by [Leadbay](/hermes/mcp/servers/external/leadbay-mcp/) and [Vibe Prospecting](/hermes/mcp/servers/external/vibe-prospecting-mcp/) with the regional precedent at [firmy.ai](/hermes/mcp/servers/external/firmy-ai-mcp/); `Elaichi` (`#6656`, governed gateway to 650+ work apps with per-person sign-in) as infrastructure rather than an operator data surface; `Frostbyte` (`#6669`, product planning for teams building with coding agents) on the project-management class; `GrackerAI` (`#6664`, AI visibility scoring) on the SEO and AI-visibility class that already carries twenty guides; `Mailazy` (`#6665`, 85 email marketing tools with a practice mode that blocks real sends) on the saturated email class; `AskEditor` (`#6659`, browser video editor driven by an agent) on the media class; `Agent Outbox` (`#6657`, Telegram delivery through a hosted bot) on the messaging class carried by [Mobile Text Alerts](/hermes/mcp/servers/external/mobile-text-alerts-mcp/).

**Held on a measured 200.** `DwellDelta` (`#6662`, `dwelldelta` **0.14.0**, **7** tools, Australian property) on the property class beside [Fonciq](/hermes/mcp/servers/external/fonciq-mcp/) and [HeritageDeed](/hermes/mcp/servers/external/heritagedeed-mcp/); `Fondatoria` (`#6661`, `fondatoria` **1.4.0**, **8** tools, French small-business sites) on the site-builder class; `Is it legit?` (`#6660`, `legitreviews` **2.0.0**, **7** tools that score whether a Google Maps review set is genuine) on the review-integrity slice, with the catalogue gap recorded rather than claimed closed; `Finekot` (`#6670`, `Finekot API` with **99** pay-per-call utilities) as an aggregator; `Klar Daheim` (`#6674`, `klar-daheim` **0.1.0**, **5** read-only tools) as a single-publisher German consumer guide; `Spectra` (`#6672`, `spectra` **0.1.3**, **6** tools, DeFi fixed-rate yield) on the crypto class; `PE or Not?` (`#6651`, `peornot` **0.1.0**, **3** tools over about **65,000** US practice locations) on the company-registry class with a promotion test recorded, since the ownership angle is real but the coverage is healthcare verticals; `IPO Radar` (`#6678`, `ipo-radar` **1.0.0**, **4** Indian IPO GMP tools) as regional market data; `Sofala` (`#6675`, `sofala.market` **1.1.0**, **5** tools on a public read-only endpoint) beside the marketplace-commerce entries; `Clanksquare` (`#6677`, `clanksquare` **0.1.6**, **2** tools, an agent social network on Ed25519-signed posts) on the agent-identity class.

**Outside operator scope, named so the next pass does not re-triage them:** `repofit` (`#6671`, developer memory files), `FullyDefined` (`#6673`, SOLIDWORKS CAD on Windows), `Viveka` (`#6653` and `#6654`, astrology and ephemeris), `VideoUpscaler` (`#6655`, video upscaling), and the `Forever Works` set (`#6652`, **15** MIT servers whose only operator-adjacent item is a trademark search that [IP Defender](/hermes/mcp/servers/external/ipdefender-mcp/) already covers).

**From the mcp.so feed.** `Translayte` (`14:23:37Z`) is **150+** languages of certified, sworn and notarised translation with coverage check, price, order and tracking and no API key, held beside the catalogued eVerbary certified translation entry. `Angelcam` (`15:28:13Z`) is consumer security cameras. `CueHQ` (`16:58:20Z`) is a small AI product listing with no operator data surface.

## Listing Surfaces

| Surface | Probe | Result |
| --- | --- | --- |
| mcpservers.org | `/servers/corpusiq-io` through the reader proxy | **LIVE**, HTTP 200, title `CorpusIQ MCP Server \| Awesome MCP Servers`, **55** brand hits |
| Glama | `/mcp/connectors/io.corpusiq/multi-source-mcp` | **LIVE**, HTTP 200, 2.7 MB body, **621** brand hits |
| Official registry | `v0.1/servers?search=io.corpusiq` | **ACTIVE**, version **1.0.0**, remote `https://mcp2.corpusiq.io/mcp`, description still reads `30+ business systems` against the 40+ on the site, drift open since November 1 |
| mcp.so | four direct slugs | **NOT LISTED**, 404 on `corpusiq`, `corpusiq-io`, `corpusiq-mcp` and `io.corpusiq`, paid route declined under the no-payment rule |
| Smithery | registry API `q=corpusiq` | **HTTP 500** vendor-side on this pass, second failure in three days, last confirmed live on October 31 with a publisher-scoped `qualifiedName` |

## Count

The guide tree held **1,092** guide directories before this pass and holds **1,094** after it. Sources: the chatmcp/mcpso submission window **#6651** to **#6679** read with bodies; the mcp.so `/feed` read directly with a browser UA; the mcpservers.org `/all` newest page read twice through the r.jina.ai reader proxy at counter **19,145**; a driven keyless session on the DFX endpoint (**20** tools, **6** called); and **18** keyless endpoint probes across the window plus two gated servers documented from their own pages.
