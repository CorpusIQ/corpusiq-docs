---
title: "MCP Server Discovery - November 1, 2026 (Evening)"
description: "Evening sweep of mcp.so, mcpservers.org and the chatmcp/mcpso submission window: two new servers catalogued with guides, 31 submissions dispositioned."
last_updated: 2026-11-01
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-november1-2026-evening"
tags: ["mcp server", "model context protocol", "hermes mcp", "sweep"]
---

# MCP Server Discovery - November 1, 2026 (Evening Sweep)

## Summary

Eleven hours after the midday pass, with 31 submissions landing in the meantime. Two servers earned guides: **Reg Monitoring MCP**, a keyless index of financial regulation across 34 regulators in 20 jurisdictions with a parsed deadline calendar, and **HeritageDeed MCP**, a keyless set of 58 US property due diligence tools that orders title reports at $49 while giving away flood, radon, Superfund, sale list and property tax data for free.

The mcpservers.org `/all` page failed the same way it failed in the morning, which turns the morning's observation into a standing rule. The first read, cache-busted on the target URL, returned the counter at **18,732** with the same thirty slugs the midday pass had dispositioned. The second read, cache-busted with a nanosecond stamp, returned **18,883** with all thirty turned over. Since the page is ordered newest first, the read whose counter has moved is the live one and the read that repeats the previous counter is a stale proxy snapshot. Two cache-busted reads, discard the one that agrees with yesterday.

## Sources Swept

| Source | Read | Result |
| --- | --- | --- |
| mcp.so homepage `recentServers` | direct, 30 cards with a date | newest `2026-11-02T01:54:34Z`, six above the midday stamp `2026-11-01T13:11:50Z` |
| mcpservers.org `/all` | r.jina.ai, `X-Return-Format: html` | first read 18,732 stale, second read 18,883 live, 30 slugs |
| chatmcp/mcpso issues | authenticated REST, one call with bodies | window #6551 to #6584, 31 submissions |
| Endpoint probes | keyless JSON-RPC | 4 endpoints keyless 200, 2 OAuth 401, 3 detail shells 404 |

## New Servers Catalogued

### Reg Monitoring MCP - 20 Jurisdictions, One Deadline List

Relevance: HIGH. **Endpoint verified** (HTTP 200 keyless `initialize`, `mcp-session-id` issued, `serverInfo` `regmonitoring` 0.2.0, **7** tools listed).

A keyless index over **6,107** financial regulatory records published between **2011-06-28** and **2026-10-30**, from **34** regulators across **20** jurisdictions. `get_stats` reports **5,528** records with an AI analysis, **974** with a parsed deadline, **100** with a penalty amount, **6,106** with a significance score and **3,932** with an urgency flag. `get_taxonomy` counts the filterable jurisdictions (UK 1,196, US 996, France 690, Luxembourg 648, Australia 358, Ireland 322, Germany 296, EU 295, UAE 187, Singapore 183, Hong Kong 179) and regulators (FCA 797, AMF 690, CSSF 648, SEC 394, ASIC 358, CBI 322). `list_deadlines` returned **974** deadlines with `deadline_type`, `status`, `confidence`, the parsed source sentence and a `firm_types` list.

It earns a guide against [The Bot Wire MCP](/hermes/mcp/servers/external/botwire-mcp/), which is a pipe into US primary documents with no jurisdiction filter, no consultation calendar and no firm-type field. Here the non-US records outnumber the American ones and the firm-type filter is what makes the feed a work queue.

Guide: [Reg Monitoring MCP](/hermes/mcp/servers/external/regmonitoring-mcp/)

### HeritageDeed MCP - US Title Reports on Demand

Relevance: HIGH. **Endpoint verified** (HTTP 200 keyless `initialize`, `serverInfo` `heritagedeed` 1.30.0, **58** tools listed, live tool calls returned real data).

Free keyless lookups plus paid documents. `list_coverage` returned **43** counties across 14 states with their main cities plus the eight inclusions and four exclusions of a title search. `flood_zone_lookup` returned a parsed FEMA National Flood Hazard Layer result for a live address, with `mapped: false`, `sfha: false`, the caveat about unpublished digital maps, the insurance consequence and a disclaimer that it is screening rather than an official determination. `property_tax_rates_by_state` returned the Census ACS 2020-2024 period with a US effective rate of **0.94 percent**, median real estate taxes of **$3,119** and a median home value of **$332,700** across **84,210,142** owner-occupied homes. Reports: title **$49**, environmental **$29**, tax appeal pack **$49**, credits at **$25** a report, Pro **$39** a month, Property Watch **$9.99** a month per property.

It earns a guide because [Hercules MCP](/hermes/mcp/servers/external/hercules-property-mcp/) answers who owns what and who to call, while this answers what is recorded against the parcel, what the ground around it carries, what a sale nets and what a tax sale leaves behind, and it orders the report at the end.

Guide: [HeritageDeed MCP](/hermes/mcp/servers/external/heritagedeed-mcp/)

## Also Identified (Not Catalogued)

From the mcp.so card block: `brontide` (agent game), `instatus` (official status page vendor, uptime class carried by WatchCron, healthchecks, realuptime and hosttracker), `cve-now` (merged CVE/OSV/NVD/KEV/EPSS feed, class covered by Bot Wire's CISA wire), `sazabi` (logs and issues for a coding agent behind OAuth), `opsis-osint` (OSINT, carried by OpenOSINT), `cdphub` (met again on /all).

From `/all`: `cdphub-com-mcp` (CdpHub, **6** keyless tools measured, a read-only CDP integration directory held beside Jitsu which manages a CDP rather than comparing them), `taskavel-com` (401 with protected-resource metadata, project management class per Plane Workflow), `www-seliee-si` (401, all-in-one business connector, aggregator class), `docfig-com-api` (bank statement conversion, carried by MainBook and BankConv), `markethq-ai` (buyer intent plus AI visibility, Octolens and Buska class), `elitemailsuite-com-docs-automation-ai-mcp` (email class saturated), `diffio-ai` (audio restoration), `bettyapp-org-developers` (lecture moments), `moneywithai-net` and `4ai-ai-for-ai-agents` (directories), `pclosets-com` (single-vendor shop), `privategoat-app-docs-agents-mcp-server` (local Mac app), `verli-app` (saved transcripts), `nova-civai-co-agent-product-admin` (one vendor's product admin), `escortfox-com-developers` (consumer), `graphify-labs`, `omnicoder-dev` and `testchimp` (404 detail shells, no server content behind the slug), and `veshraazthapa`, `ryanbiddy`, `igorolv`, `eudoramarlowe`, `camerxnduff`, `alfa-reza` (personal handle listings with no product surface).

From the submission window, held on recorded class precedents: `GatherHQ` #6558 (synthetic customer research from simulated interviews, the research class carried by User Intuition from October 28 with a four million person real panel, closest call of the pass), `Truo` #6576 (Australian CDR bank data, regional bank-sync precedent against Kontoflux), `DMD Costs` #6567 (UK legal costs, regional legal trio Fermat 360, NyayAssist, PRIMAMCP), `Starlecta` #6569 (Turkey-only creator analytics, saturated creator-discovery class), `Seonix` #6564 (seo, saturated), `PDFDispatch` #6562 (document rendering, Bannerify and url-to-pdf and FynePDF), `NoneCap` #6563 (captcha class), `Ahel` #6560 (per-call priced data task catalog, Apify-actor distribution class), `Cloud Alter Ego` #6559 (memory class), `Kalshi Eye` #6557 (prediction market data class).

Skipped on thinness or scope: `Chartory` #6577 (React charts), `Varity` #6578 (deployment), `ChronoGate` #6566 (timezone utility), `Agent Craft` #6553 (voxel game), `Bytewell` #6551 (Mac disk cleanup), `Space Mushroom` #6580 (engineering materials), `Inkable Label` #6579 (single-vendor label shop), `Caigen Notes` #6584 (note app), `Fluxcut` #6583 and `CropDen` #6582 (media utilities), `TV Box Tools` #6575 (Android television setup), `AI Detect` #6574 (authorship scoring), `Gemini MCP` #6573 and `houtini-lm` #6572 (provider wrappers), `Agentboard Skills` #6570 (agent workflows), `SingIt x402` #6556 (USDC-billed search).

Two corrections rather than holds: `Anclum` #6581 is a directory of 9,500+ MCP servers, the same subject as this catalogue, and `SEO Audit` #6571 is a resubmission of the already catalogued `seo-audit-console-mcp`.

## Skip Classes Held

- Uptime and status page vendors, carried by WatchCron, healthchecks-mcp, realuptime-mcp and hosttracker-mcp.
- Vulnerability feeds, carried by Bot Wire's CISA wire and the security class.
- Creator discovery and influencer analytics, saturated and again regional in this window.
- Regional bank sync, carried by the Kontoflux precedent.
- Regional legal research, carried by Fermat 360, NyayAssist and PRIMAMCP.
- Document rendering and PDF generation, carried by Bannerify, url-to-pdf, FynePDF and PDFDispatch's own class.
- Bank statement conversion, carried by MainBook and BankConv.
- Directories and benchmark fixtures, including two in this window.
- Single-vendor storefronts, personal handle listings and game servers.

## Core Listing Verification

| Surface | Result |
| --- | --- |
| mcpservers.org `/servers/corpusiq-io` | live, page title "CorpusIQ MCP Server \| Awesome MCP Servers" through the reader proxy |
| Smithery registry `?q=corpusiq` | two attempts returned HTTP 500, service-side; last confirmed live at the midday pass, not treated as delisting |
| Glama `/mcp/connectors/io.corpusiq/multi-source-mcp` | HTTP 200 with CorpusIQ present |
| Official registry `io.corpusiq/multi-source-mcp` | HTTP 200, version 1.0.0, remote `https://mcp2.corpusiq.io/mcp`, description still reads "30+ business systems" against 40+ on the site, the drift flagged at midday and still open |
| mcp.so four direct slugs | 404 on `/server/corpusiq`, `/server/corpusiq-io`, `/server/corpusiq-mcp` and `/server/io.corpusiq`, still not listed with the paid route declined |

## Verification

- Both guides pass `gates.py docs` with zero findings and zero warnings, and the local validator confirmed title and description lengths at 56/141 and 45/130 characters, no em dash, no credential redaction marker, a FAQ question heading present and every See Also target resolving to a real directory.
- Both endpoints were driven live: `initialize`, `tools/list`, and real tool calls returning record counts, taxonomy counts, a parsed FEMA result and a Census tax table.
- Index patched with a single atomic script: the `> **Last updated:**` line moved to the evening sweep, and one new `## 🆕 November 1, 2026 - Evening Sweep (2 New, 2 Guides)` section was inserted above the midday section, with every anchor asserted before the write.
- Guide tree counted from disk: **1,080** before, **1,082** after, **1,230** entries in the tree, **1,228** before the two new directories.

## Sources

- [External MCP Server Catalog](/hermes/mcp/servers/external/)
- [Reg Monitoring MCP](/hermes/mcp/servers/external/regmonitoring-mcp/)
- [HeritageDeed MCP](/hermes/mcp/servers/external/heritagedeed-mcp/)
