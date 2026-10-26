---
title: "MCP Server Discovery - October 12, 2026 (Evening Sweep)"
description: "Evening sweep cataloguing international tax and wage reference data, US product recalls, GB operator licences, a compliance framework graph, QuickBooks Desktop, US property records, media contacts and startup paperwork."
last_updated: 2026-10-19
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-october12-2026-evening/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp"]
---

# MCP Server Discovery - October 12, 2026 (Evening Sweep)

Evening sweep about 10 hours after the midday supplement: the mcp.so `/feed` (30 server links via the direct TanStack fetch), mcpservers.org `/all` pages 1-5 through the r.jina.ai reader proxy (150 slugs, fully churned against the midday capture), the fresh chatmcp/mcpso issue window #5198-#5218 (21 submissions), and the canonical window check (r109 to r110: 124 additions, one removal), with live endpoint probes for every candidate. Eight new business-relevant entries, each catalogued with a guide: international tax and wage reference data, US product recalls, GB operator licences, a compliance framework graph, QuickBooks Desktop, US property records for investors, media contacts for PR, and startup paperwork with SAFE rounds.

## New Servers Catalogued

| Server | Category | What it does |
|---|---|---|
| [Afriref MCP](/hermes/mcp/servers/external/afriref-mcp) | Finance | Official tax, VAT, wage, holiday and FX reference data for 129 countries, every value cited to source |
| [RecallsAPI MCP](/hermes/mcp/servers/external/recallsapi-mcp) | Compliance | US product, food, drug, device and vehicle recall lookups with a source link on every result |
| [HaulierScope MCP](/hermes/mcp/servers/external/haulierscope-mcp) | Logistics | GB operator licence data from DVSA open data, with a change feed and insolvency and filing watch |
| [The Art of Service MCP](/hermes/mcp/servers/external/theartofservice-compliance-mcp) | Compliance | Compliance framework crosswalks: 969 frameworks, 46K controls, 315K mappings, plus courses |
| [LedgerCrossing MCP](/hermes/mcp/servers/external/ledgercrossing-mcp) | Finance | QuickBooks Desktop reachable from any MCP client: 240 qbXML operations via a local bridge |
| [Hercules MCP](/hermes/mcp/servers/external/hercules-property-mcp) | Real Estate Data | US property records, LLC lookups, pre-foreclosure cases and owner contacts |
| [Media List MCP](/hermes/mcp/servers/external/media-list-mcp) | Marketing | Journalist, editor and podcast host contacts for PR targeting and saved lists |
| [Binderwork MCP](/hermes/mcp/servers/external/binderwork-mcp) | Productivity | Startup paperwork: tracked deck links, e-signature envelopes, SAFE rounds, cap table |

## Sources

- mcp.so /feed via the direct TanStack fetch (30 server links; six cards new to this window - JustGains, Stockpile Market, call4me (a prior disposition), SkyAccess, CarWhere VIN and eVerbary - all evaluated and none catalogued; the rest repeats or prior dispositions from the October 3-12 ledgers)
- mcpservers.org /all pages 1-5 via the r.jina.ai reader proxy (150 slugs; full page churn against the midday capture - 30 of 30 on page one changed - with the three-way heading / guide-directory / ledger triage plus a residual eyeball pass over the fresh cohort)
- chatmcp/mcpso issues #5198-#5218 (21 submissions since the midday supplement; five catalogued: Afriref, Binderwork, Media List, Hercules, The Art of Service)
- Canonical window check on the sibling captures (r109 to r110: 124 additions, one removal - the removal is a slug-form flip; locale-prefix check clean, zero regional rows)
- Vendor docs, listing pages and live endpoint probes for every candidate (Afriref: keyless initialize 200 as `afriref` v1.0.0 with all 16 tools; RecallsAPI: 200 as `recallsapi` v0.1.2 with all 4 tools; HaulierScope: 200 as `haulierscope` v1.0.0 with all 15 tools; The Art of Service: 200 with all 33 tools; Hercules: 200 as `property-data` v1.0.0 with all 21 tools; Media List: 401 sign-in challenge; Binderwork: 401 missing authorization header; LedgerCrossing: local Windows app, vendor docs page live)

## Also Identified (Not Catalogued)

**mcp.so feed (six fresh cards, none catalogued):** JustGains (workout and nutrition tracking; consumer fitness utility), Stockpile Market (autonomous agent commerce and curation; the agent-commerce class stays held), SkyAccess (private jet empty legs, charter estimates and booking links; the charter and travel-booking class is held per the Charter Boats and consumer-travel dispositions), CarWhere VIN (VIN decode, NHTSA recalls and verified buyer pricing; the vehicle-data class is covered by the catalogued CarDossier and Dutch Vehicle Context entries, and the NHTSA recall slice is now covered by RecallsAPI above), eVerbary certified translations (consumer document service), and call4me carrying its October 1 disposition (agent-placed phone calls; consumer task utility).

**mcpservers.org /all (150 slugs, fully churned):** evaluated and held - Agora / openforallofus (MCP server search ranked by measured handshakes; meta-directory utility, also submitted as issue #5204), HaveTML (publish artifacts as commentable share links; the publishing and share-link utility class per the SlopIt disposition), InboxGuards (account-takeover alarm for Google Workspace and Microsoft 365; monitoring service, listing thin on MCP specifics), StatementSure (bank and credit-card statements into QuickBooks, Xero, OFX exports; the document-utility class per Docspeed and RelayPDF), Qualien (QE gateway aggregating 21 testing servers; dev utility), Hatchdoor (self-hosted Obsidian vaults with MCP; notes and dev utility per the Obsidian precedent), ISHOB (36 x402 micro-utilities; x402 pay-per-call class), Mailroom (inbox access over IMAP/SMTP; the inbox class is dense per the Ficiel disposition), PreviewSend and Brod (deploy surfaces for agent-built sites; deploy-utility class), Emelia (multichannel prospecting platform; the outreach class is covered by Salesbot, Unipile and the Postfleet, Faivelo, Cooper Email family), Tenet Investing (stock research; investment-research class dense), GasNow (crypto gas and fee data; crypto class), Cited or Not and AIclicks (AI answer visibility; class saturated per geolint, LogNorm and the Onsomble ruling), Cheerful (influencer-campaign reporting connector; marketing-platform connector class), BNex by Ziync (WhatsApp Cloud API and shared inbox; business-messaging class dense), Fuentio (France and Spain company data; the regional company-data rule per the OpenBase and Corporary holds), ScaledThought (open-weight model API with agent-driven signup; model-access and agent-payments classes), MatrixAgentNet and DevRelay (agent network and release-content approvals; agent-infra and dev utilities), Kokon and Kelpo (local photo editing and UGC video creation; media-generation classes per Varosity, PZERO and the PhotoFresco hold), BotSharper (pump.fun wallet facts; crypto class), Actually Asked (site FAQ and visitor-question widget; site-CX utility), and the remaining fresh cohort held as dev, consumer and regional-content utilities (drivelab, brm-chronographes, DonPost, satledger, phpgraph and the Turkish news-API cluster).

**chatmcp/mcpso issue window #5198-#5218 (21 submissions):** the five catalogued above; evaluated and held - Lium Docs (GPU-marketplace documentation search; vendor-docs utility), Proofsource (brand visibility in AI answers; class saturated per the visibility rulings), fineprint (ToS risk scoring before an agent accepts terms; scanning utility class beside Vulnify), alethech (Ed25519-signed agent memory; memory class dense), Omneum (local context evaluator; dev tool), GLEE (x402 acceptance verifier; x402 class), Intellibook AI (India appointment booking; consumer regional), Kristo Intelligence (crypto signals over x402; crypto class), GiftRoam (gifting to 190+ countries; consumer e-commerce), presign-guard and x402 Doctor (one builder's screening pair; the x402 and pre-spend screening classes per mcp-sanctions and the spend-preflight holds), Sitemap Extractor (Apify-actor distribution class), Agent Discovery Board (MCP and x402 meta-directory), and genshin-miliastra (gaming utility).

**Canonical additions beyond the /all cohort (31 slugs):** held as dev, consumer, regional-news, x402, crypto or meta utilities - Seiche community and connect, Papyrio PDF tools, SafeXL, Harbor, Priors, Overflo CVE tools, ReputeMap, QuerySail, RunScout, Coredence, Keeploop, AIclicks, HubSpot Auditor, Breeze PM, gunsnprices, agentdiet, InstaSeer, and the remaining news-API cluster; the one removal is a slug-form flip (www-siglata-com-docs-agents-mcp re-keyed to siglata), not a delisting.

## Result

Catalog moved from 910 servers (+796 guides) to 918 servers (+804 guides).
