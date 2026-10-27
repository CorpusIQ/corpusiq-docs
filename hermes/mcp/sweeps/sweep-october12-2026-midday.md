---
title: "MCP Server Discovery - October 12, 2026 (Midday Sweep)"
description: "Midday sweep cataloguing US parcel and zoning due-diligence data, rental turnover and deposit settlement, and ISO 20022 payment code reference servers."
last_updated: 2026-10-24
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-october12-2026-midday/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp"]
---

# MCP Server Discovery - October 12, 2026 (Midday Sweep)

Midday sweep over the mcp.so `/feed` (30 server links via the r.jina.ai reader proxy), mcpservers.org `/all` pages 1-5 through the same reader proxy (150 slugs cross-referenced three-way against the catalog headings, guide directories and the October ledgers), the fresh chatmcp/mcpso issue window #5161-#5196 (36 submissions), and the canonical window check on the existing captures (r106 to r109: one addition, zero removals). Three new business-relevant entries, each catalogued with a guide: US parcel and zoning due-diligence data, rental turnover and deposit settlement estimates, and ISO 20022 payment code reference.

## New Servers Catalogued

| Server | Category | What it does |
|---|---|---|
| [Placestack MCP](/hermes/mcp/servers/external/placestack-mcp) | Real Estate Data | Parcel, owner, assessment, sales, permit and zoning records for any U.S. address: 14 tools for due diligence at the speed of a conversation |
| [Tektolo MCP](/hermes/mcp/servers/external/tektolo-mcp) | Property Management | Free keyless engines for the move-out: what a turnover costs, what to return from a deposit under the state statute, and whether the deposit came back on time |
| [ISO 20022 Navigator MCP](/hermes/mcp/servers/external/iso20022-navigator-mcp) | Finance | Grounded answers on ISO 20022 bank transaction codes and legacy mappings (MT103 to pacs.008), with a provenance block on every response |

## Sources

- mcp.so /feed via the r.jina.ai reader proxy (30 server links; the fresh cards were Sprite Fusion, 42min and Placestack (catalogued), with every other block a repeat or prior disposition from the October 3-11 ledgers)
- mcpservers.org /all pages 1-5 via the r.jina.ai reader proxy (150 slugs; the window delta against the October 11 evening snapshot was two slugs (geoapify-mcp-server, photoshoot-si), both held, and the previously unledgered carryover cohort was dispositioned with ISO 20022 Navigator catalogued)
- chatmcp/mcpso issues #5161-#5196 (36 fresh submissions since the evening cutoff at #5160; Tektolo catalogued, the rest held or prior dispositions)
- Canonical window check on the existing captures (r106 to r109: one genuine addition (geoapify-mcp-server) and zero removals; no locale-prefix artifacts; no fresh twelve-sitemap refresh this cycle)
- Vendor docs, listing pages and live endpoint probes for every candidate (Placestack: POST initialize returns 401 "Authentication required" behind OAuth; Tektolo: keyless initialize returns 200 as `Tektolo` v0.1.0 and `tools/list` returns all 5 tools; ISO 20022 Navigator: keyless initialize returns 200 as `iso20022-navigator` v0.1.0 and `tools/list` returns all 3 tools)

## Also Identified (Not Catalogued)

**mcp.so feed:** the fresh cards beside Placestack were Sprite Fusion (pixel-art sprite generation for game projects; creative-utility class per the Uwear and 3DLogo precedents), 42min (official meeting-scheduling server, 43 tools covering availability, booking, polls, routing forms and contacts; the scheduling class is covered by the catalogued Cal.com, Secure Calendar and OneCal entries per the Caly ruling) and Localscreenshot (local screenshot utility; dev utility, thin docs), with every other block a repeat or prior disposition from the October 3-11 ledgers (TripLedger, Gamedev Tavern, FlexQueries SEO, Lochless, DeFade, Nullprint, Kinetune, UXKIN, Your Move Exercise Video API and the rest).

**mcpservers.org /all (150 slugs; the window delta was two slugs, both held, plus the previously unledgered carryover cohort):** evaluated and held - geoapify-mcp-server (official geocoding, routing and geospatial tooling with 11 tools; the geocoding and mapping class is covered by the catalogued PlaceRoot and HERE Maps entries plus the China maps surface), Photoshoot.si (AI photoshoots from 22 image models; media-generation aggregator class per Varosity and PZERO), LinkedNav (145 LinkedIn outreach tools across campaigns, unibox, enrichment and signals; the class is covered by the catalogued Salesbot and Unipile entries - the strongest hold of the cycle), Audo (audio and video cleanup for agents; media utility), Unl (decision-reason capture for agents; memory and context class dense), Vigilia (front-end monitoring script tag; dev utility), AsOf (wallet holdings at a date; crypto class) and BlazePhoenix (callable on-chain solver; crypto class), with the rest of the surface carrying prior dispositions from the October 3-11 ledgers.

**chatmcp/mcpso issue window #5161-#5196 (36 submissions):** Tektolo catalogued above. Evaluated and held - Is It Down API, PulseWatch Vendor Status, Dragons Eye Ransomware Claim Lookup and OrionCMD Site Checks (a coherent one-builder fleet of no-auth status and check endpoints with paid tools metered in x402 v2 USDC on Base; the x402 pay-per-call class per the toll402, sendcheck and Ni Biashara dispositions, with status utilities per the StatOSS precedent), PaidPilot Invoice Tools (invoice helpers; the invoice tooling class is covered by the catalogued LuckPanda and Eleata entries), RobotTraining.jobs (robot-training jobs data; jobs-data class covered by the catalogued OpenHire and Jobyap plus the Magnificent Jobs search), Ownkube (prior disposition; personal cloud deploys, dev infrastructure), Reasonbook (local decision records for coding sessions; dev and memory utilities dense), agentsvc.io (prior disposition; x402 pay-per-call scraping), Director's Lookbook (named style catalogs for image and music generation; media-generation class), Remember Me Bible Memory and Pour Picks (consumer utilities), KeyShortcuts (keyboard shortcut lookups; dev utility), 6Frame Verify (pre-launch website QA; site-scan class beside PageProofer and Pinthread), Jid (US business-registry verification before an agent acts; the KYB class is covered by the catalogued Company Identity Resolver, registry-mcp and Prometiam Risk entries, with the Global FinReg hold as precedent), Craft Quantities (construction material quantities from cited calculators; construction vertical held per Constructelligence, calculator class per the catalogued Octura tools), Vicem (AI phone answering; voice and telephony class covered by the DialNexa and KaiCalls holds and the Callflow disposition), Pineprompt (AI-search visibility tracking; visibility class saturated per geolint, LogNorm and the Onsomble ruling), nano-mcp-termux (device utility), Ficiel (AI inbox for coaches; communication and inbox classes dense), GuiaFlow (interactive product demos from screenshots; marketing and design tooling class), the QFactory trio AINDF, Unslop and QFactory (design-system serving, design and copy rule canon and workflow catalogs from one author; design and dev tooling class per the UXKIN, WunderUI and UIDiscovery holds), classifier.dev (batch text classification; dev utility), Reticle (in-app verification for web apps; dev and testing utility), SiteData (website rankings; web-data class dense per Vaneform), genealogy-mcp (family-history research; consumer research utility), PageLens Analytics (cookieless web analytics and AI visibility; visibility class saturated), SocialRobot (social publishing; same saturated class as the evening disposition), mcd-profile (personal archive; consumer utility), the Webcam, Windows-MCP and Obsidian-MCP Bot Bridge trio (forks and device utilities; fork-disposition class).

## Result

Catalog moved from 906 servers (+792 guides) to 909 servers (+795 guides).
