---
title: "MCP Server Discovery - November 8, 2026 (Midday)"
description: "Midday sweep: the sitemap canonical grew 18 slugs and the issue window carried 8 arrivals, with ListRiver catalogued on the free-count primitive."
last_updated: 2026-11-08
tags: ["mcp server", "model context protocol", "mcp discovery", "november 2026"]
---

# MCP Server Discovery - November 8, 2026 (Midday)

Fired on the 10:00 MST tick, seven hours after the night pass that catalogued DutyKit. One server was catalogued. The finding of this window is not a product but a billing design, and it came from a package that answers questions about itself before it asks for a key.

## Surfaces read

| Surface | Result |
| --- | --- |
| mcpservers.org twelve-sitemap canonical | **20,018** distinct server slugs, **18 additions**, **0 removals**, from 63,435 raw `<loc>` entries across thirteen server maps |
| mcp.so homepage | 188 distinct stamps across 204 occurrences, newest `2026-11-08T15:50:03.559Z`, **4 cards** above the night stamp `2026-11-08T08:56:02.072Z`; plain and cache-busted reads identical |
| chatmcp/mcpso issue window | **#6936 to #6943**, eight arrivals, no gaps |
| mcpservers.org `/all` and detail routes | **403** direct, **401** through the reader proxy. The standing condition since November 4 |

A structural note that belongs in the ledger: the sitemap index now carries **`servers/11.xml`** alongside `servers/1` through `servers/10`, `priority-servers.xml` and `remote-mcp-servers.xml`. Thirteen server maps, 56.6 MB of XML, 63,435 raw entries. The count reconciles to 20,018 after the case-insensitive locale strip and the `/servers/` subset, which is the method that has held across passes. Reading the raw union instead of the subset over-reports by roughly 9,300 marketing and topic pages, and stripping locales case-sensitively multiplied an earlier attempt to 37,483.

## Catalogued

### ListRiver MCP

**Official US state business registries as a lead list, with a free counting primitive in front of the paid pull.**

Package `listriver-mcp` 0.1.0 over stdio, registry record `io.github.ListRiver-LLC/listriver` active since `2026-11-03T13:24:59Z`. A keyless `initialize` answers **200** as `ListRiver` 0.1.0 on protocol `2025-06-18` and returns the full instruction set plus all three tool schemas; `tools/call` then returns the documented 401 naming `LISTRIVER_API_KEY`.

Three tools: `list_states`, `count_businesses`, `search_businesses`. The design decision that earns the entry is that **the first two are free and the third spends records**. Every other business-data surface in this catalogue makes you learn the size of a market by buying the pull. Here an agent sizes a market, narrows it on `has_phone`, `has_email`, `naics`, `entity_type` and `formed_within`, and only then retrieves names, with a cursor to continue rather than restart.

The records are filings, not profiles: address, county, registered agent and formation month, plus phone, email, website, EIN and NAICS where the state publishes them. Two honesty notes come from the server itself and are recorded in the guide as the two ways this surface can mislead. Coverage of phone, email, NAICS and county is partial and state-dependent, and the server instructs the agent to check with `count_businesses` before promising a phone list. And the data carries a use restriction: no credit, insurance, employment or housing decisions, which is the FCRA boundary stated plainly.

Free tier is 500 records a calendar month, then $50 for 5,000 rising to $450 for 75,000, with prepaid packs and an AWS Marketplace path. No overlap with [Corply](/hermes/mcp/servers/external/corply-mcp/) (a formation service), [Leadbay](/hermes/mcp/servers/external/leadbay-mcp/) or [Vibe Prospecting](/hermes/mcp/servers/external/vibe-prospecting-mcp/) (proprietary scoring) or [firmy.ai](/hermes/mcp/servers/external/firmy-ai-mcp/) (Polish KRS, one country).

Guide: [ListRiver MCP](/hermes/mcp/servers/external/listriver-mcp/)

## The canonical additions, dispositioned

Eighteen slugs entered the twelve-sitemap universe. Five were prior dispositions and thirteen were genuinely undispositioned. Twelve of the thirteen resolve to consumer verticals.

**One publisher fleet.** Six of the additions carry the same author. `vendawallet-com` (free receipts for anyone taking payments), `carglendale-com` (Glendale CA dealership price comparison), `renderior-com` (furniture tried in a photo of your room), `armenly-com` (Armenian music streaming), `ayoh-dev` (self-hosted chat, mail, boards and calendar) and `kizupi-com` (a grades 1 to 6 math tutor) are all `io.github.miradero`. Six consumer verticals from one author, resolved through the registry rather than guessed from the slugs. Held as one fleet, not six findings.

**Held individually, class named:**

- `picardo-mcp` - consumer health commerce, clinician-designed blood panels and custom supplements with a buy link. Held on the healthcare vertical class (`orinyx`, `peptides.farm`, `TMSClinics`, `Slate`).
- `rivieramayaelite-com-ai` - local business directory, area guides and developments for sale in the Riviera Maya. Held on the regional consumer directory class.
- `supercompress/supercompress` - compresses coding-agent context about 64 percent, hosted Neural Keep. Held on the developer-infrastructure class that already carries more than twenty guides.
- `heimatvox-universalear-com` - `universalear.com` serves as "Universal Ear, local-first AI for speech and document workflows", no registry record under either name. Held on the transcript and document-workflow class (`EasyTranscriber`, `Free YT Bulk Transcripts`).
- `nodriver-project/chromeleon-mcp` - prior disposition. `chromeleon-mcp` was already held on anti-detect browser automation (`Veilus`), and `nodriver` resolves to `andresolbach/nodriver-mcp-server` (undetected Chrome automation, 57 tools), the same slice.
- `agent-guard-organic-pilot-staging-andrea-vignoni-workers-dev` - a staging artifact by name (pilot, staging, a worker branch). Not a product listing.

Prior dispositions confirmed by name in the index: `anymail-finder` (B2B email find and verify), `getcheapgames`, `simplyboost`, `simvito-esim` (the four ordinary mcp.so arrivals from the night window) and `chromeleon`.

## The four mcp.so cards

- `seo-with-rankspot` (**SEO with RankSpot**, `15:50:03Z`, OAuth) - AI SEO, GEO and visibility tracking across ChatGPT, Perplexity and Google AI answers, with keyword research and article publishing. Held on the SEO and AI-visibility class that carries geolint, LogNorm, Tracetify, Sorank, HiBot and Serpel and more than twenty guides.
- `whatsapp-by-green-api-6c0466` (**WhatsApp by GREEN-API**, `13:04:21Z`) - held on the WhatsApp class carried by WASender, Radar, Kaption WhatsApp and wuapi.
- `glp1-health-mcp-glp-1-prices-reviews-fda-safety` (**glp1.health MCP**, `12:47:55Z`, no auth) - consumer pharmaceutical pricing. Held on the healthcare vertical class.
- `getsales-outreach-mcp-server` (**GetSales: Outreach MCP Server**, `11:07:34Z`, OAuth) - tables of people and companies, enrichment, workflows, inbox and signals. Held on the lead-generation and sales-engagement class carried by Leadbay, Vibe Prospecting, LeadGen, DeepLead and Heylead.

## The eight issue arrivals

| # | Submission | Disposition |
| --- | --- | --- |
| 6943 | dmswift, Instagram and Facebook business accounts via Meta's API | Held. Social publishing class is saturated; eight scheduling variants were held on it a week ago |
| 6942 | Kanvo, omnichannel messenger inbox | Held. Messaging class per WASender and the Kaption surface |
| 6941 | antiRea, dataset access metering and bot-abuse flagging | Held. Agent infrastructure, and advisory only by its own description |
| 6940 | Agent Index, CC BY 4.0 dataset of GRC and security AI agents | Held. A directory of agents, not a connector to an operator's system |
| 6939 | Everstrike, live crypto derivatives market data, keyless read-only | Held. Crypto market-data class per centralcommand-io and the Hyperliquid and Solana entries |
| 6938 | Lodestar, shared memory of what worked for agents | Prior disposition. Recorded among the Lodestar skips |
| 6937 | Crossmart, AGPL-3.0 multichannel seller platform | Held. The multichannel publish and SKU-sync core is carried by `3dsellers-mcp` |
| 6936 | PlayTesterHub, twelve real Android testers for closed Google Play testing | Held. QA and testing class per Playwright E2E MCP, TurnSignal and Periscope |

## Core listing check, measured

- **mcpservers.org:** the fresh canonical carries both `/servers/corpusiq-io` and `/servers/corpusiq/corpusiq-docs`. The detail route answers 403 by edge policy, not by delisting.
- **mcp.so:** all four direct slugs (`corpusiq`, `corpusiq-io`, `corpusiq-mcp`, `io.corpusiq`) answer **404**. The listing remains absent.
- **Glama:** `https://glama.ai/mcp/servers/corpusiq-io` answers **200**. The `/@benoit-p/` and `/mcp/connectors/` forms both answer 404, so the plural server route is the live one, not a delisting.
- **Smithery:** `registry.smithery.ai/servers?q=corpusiq` and `?q=Cprusiq` both return zero servers, and `https://smithery.ai/servers/benoit-p/Cprusiq` answers 404. This is a change from the previously verified `unlisted=false` state and is flagged in the closeout as the one open question from this pass rather than recorded as a delisting on a single read.

## Counts

- Canonical: **20,018** against 20,000, +18 and -0, from 63,435 raw entries across thirteen server maps
- mcp.so: 204 createdAt occurrences, 188 distinct stamps, **4** cards above the night stamp
- Issue window: **8** arrivals, all dispositioned
- Candidates evaluated: 18 canonical additions plus 4 cards plus 8 issues, **30 total**
- Catalogued: **1**, with one guide
- Guide tree: 1,120 directories and 1,263 entries before this pass, 1,121 and 1,264 after
- Markdown under `hermes/mcp/`: 1,529 before, 1,531 after
