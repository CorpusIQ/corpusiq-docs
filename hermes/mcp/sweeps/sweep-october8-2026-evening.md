---
title: "MCP Server Discovery - October 8, 2026 (Evening Sweep)"
description: "Evening sweep cataloguing paid advertising operations across fourteen platforms and a hosted database MCP that answers questions from the live database."
last_updated: 2026-10-08
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-october8-2026-evening/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp"]
---

# MCP Server Discovery - October 8, 2026 (Evening Sweep)

Evening sweep over the mcp.so `/feed` (30 server links via the reader-proxy links summary), mcpservers.org `/all` pages 1-5 through the r.jina.ai reader proxy (the fresh cohort diffed against the October 8 r89 canonical capture of 14,767 server URLs and cross-referenced against the catalog and the full sweep ledger), and the fresh chatmcp/mcpso issue window #4952-#4975, with vendor docs and live endpoint probes for every candidate. Two new business-relevant entries, each catalogued with a guide: paid advertising operations across fourteen ad and analytics platforms from one agent, and a hosted database MCP that answers questions from the live database.

## New Servers Catalogued

| Server | Category | What it does |
|---|---|---|
| [PaidSync MCP](/hermes/mcp/servers/external/paidsync-mcp/) | Advertising & Marketing | Runs paid advertising across 14 platforms as 630+ approval-gated tools - Google Ads (152), Microsoft Ads (152), Meta Ads (83), LinkedIn Ads (34), ChatGPT Ads (28), TikTok Ads (13), Snapchat Ads (15), Reddit Ads (14), Pinterest Ads (14), X Ads (14), Google Tag Manager (39), GA4 (26), Merchant Center (16) and Search Console reads (6); dry_run previews on creates, confirm_destructive on destructive operations, free for 15 tasks a month |
| [SaturnSQL MCP](/hermes/mcp/servers/external/saturnsql-mcp/) | Database & Data Engineering | Hosted database MCP for Claude, ChatGPT and Cursor: six tools over PostgreSQL, MySQL, Oracle, BigQuery, SQL Server, Redshift, ClickHouse and DynamoDB - schema reads and row-limited SQL, read-only by default, with a shared team query library |

## Sources

- mcp.so /feed (30 server links, via the reader-proxy links summary)
- mcpservers.org /all pages 1-5 via the r.jina.ai reader proxy (the fresh cohort diffed against the October 8 r89 canonical capture of 14,767 server URLs)
- chatmcp/mcpso issues #4952-#4975 (fresh window since the midday sweep cutoff at #4951)
- Vendor docs and live endpoint probes for every candidate (PaidSync 401 "Missing Bearer token. Connect via OAuth first.", GitHub repo 200, paidsync.ai/mcp-server page 200; SaturnSQL 401 "Missing SaturnSQL credentials. Connect with Authorization: Bearer or use OAuth")

## Core Listing Verification

- mcpservers.org: LISTED (re-verified, `/servers/corpusiq-io` 200 via the reader proxy, title "CorpusIQ MCP Server | Awesome MCP Servers")
- glama.ai: LISTED (carried from midday, no change signal)
- smithery.ai: LISTED (carried; the direct slug returns 308 to the canonical listing)
- PulseMCP: LISTED (carried; the direct probe sits behind a 403 bot gate)
- mcp.so: NOT LISTED (quarantine holds, no resubmit)
- No submissions this cycle: every automatable target is either listed or in its established hold state.

## Also Identified (Not Catalogued)

On the mcp.so feed, the fresh entries beside the two catalogued were Aisle (wedding-venue search and planning; consumer vertical, held), MarginPad (crypto-futures paper trading and market data; crypto class), FUSE Health (health-sector remote server; thin listing, held) and CovaSyn (prior disposition); Shopify SEO Expert by Digital Darts is a vendor repeat (thin MCP docs disposition stands); every other block was a repeat or prior disposition from the October 3-7 ledgers (Priors, Multi Upload Tool, Rumoro, iDevice Buyer's Guide, Rivalize, EximAgent, Optimus MCP, Clipping Alpha, 3GPP Scout, MilliGate, x402-list-mcp, the grill planner, AssetLab, Listings API, Testiny, The Bridge, North Noir, Nitrosend, PubShip, KissCode, Localith, SpicyAPI, SlickTrip, PayPerFax and the rest). On the mcpservers.org /all pages 1-5, the fresh cohort beyond the two catalogued resolved to Bitculator (prior hold), and evaluated and held: SiteCheck (x402 pay-per-call utilities; class per the Bilbop and Plumb holds), Wayza (agent identity and sign-up doors; class per the Voidly disposition), ProductByte (single-vendor e-commerce marketing connector; class per the FeedShine and Kasar holds), bitHuman (talking-avatar clips and voice chat; media-generation class), Private SuperIntelligence (self-promotional thin-listing class per the Optimus precedent), the Ouroboros nine-app suite (claim, deposit, desk, invoice, milestone, papers, patent, rank and scope - a single-author single-purpose utility suite, class per the theluckystrike disposition), MacroCyber (AI-era exposure scanner; security-scan utility class), SoftQuantus QCOS (quantum operating system; deep-tech niche), SarnAI Agent Output Verifier (x402 verification receipts; class per the dsh-verify, MCP Rigor and Lodestar skips), Sniffington (brand-mention monitoring and triage; social-listening class covered by the catalogued Octolens and Buska entries per the Mentio and Rumoro precedents), RudderStack (official CDP MCP; install-level documentation only, no published tool surface, CDP class covered by the catalogued Jitsu entry), Kontoflux (DACH PSD2 bank sync; regional variant of the catalogued Zenith), AEON (autonomous agent framework on GitHub Actions, 767 stars; agent-orchestration infrastructure class per the ADA Turbo and AstroFabric holds), Ludus (agent trading journal and ladder; experiment-stage agent-finance class), agentRamen (local repository context index for coding agents; dev utility), Lampo (frame-exact video review for AI video agents; media-production class), Bowmark (hosted web tasks on live sites; browser-automation class densely covered), DnsGuard (email-authentication audit utility; class per Probelane), Konnekta (Dutch accounting knowledge page; site-published content shell), DealScore (consumer car-deal scoring), Alpina.travel (consumer alpine travel), NyayAssist (Indian legal research and matter platform; regional legal class per the eCourts India skip and the Olia disposition), SecurePutCalls (options-wheel research; trading class), QRX (art QR codes; print-design utility), Jerry (consumer insurance superapp), Zaptu (US home-services lead capture; consumer services class per the Haulest disposition), iter0 (AI website builder; dev-design utility), ARC AI (crypto intelligence; crypto class), Adeli (social-publishing API; class at saturation), Sorinai (meeting-notes connector; notetaker class covered by ParrotNotes and Granola), the ADM Google Ads skill (Google Ads class densely covered and its hosted write surface is not yet live - held) and the site-published llms.txt and docs-page shells (Recipe Library in Hebrew and English, Measured Size, the ofershap connect page, www-manyscripts docs, ask-notedandno skill page, favor-skilled llms.txt, demomyproduct demo page, workbuddy with no readable docs surface), with the remainder of the five pages as the October 5-7 disposition cohorts (UK fleet, Fresh402, Rein Agent Risk Scale, Chatpack, conv2pdf, Teleloom, Endzone, ibara, Ball Ranks, Dreamwork, Steward, Bilbop, Voidmail, Kasar CRM, OperStack, APEX Faucet, Kvickd, Ta Rodando, Brasil Data, OlaChill, CPFHub, Datalake-mcp, Checkbox and the rest). From the fresh chatmcp/mcpso issue window #4952-#4975: the two catalogued above; held or skipped: Agent Checkout (Stripe payment links for agents; agent-payments class per steward-mcp), Zektor (managed Postgres and Valkey; dev-infra class), PartForge (parametric 3D-print parts; maker niche), Travel Risk API (travel-risk data; niche travel class), Octopost (social publishing; class at saturation), Taskhold (single-vendor task connector), Plainfold (Apify-actor class per the Lintlab and Themineworks precedents), terminal-use (dev utility), the MailTester email-verification trio (commodity class per Easy Email Verification), Disc Golf England (niche sports), Superpowers (model and API marketplace; aggregator class per PZERO), PBT-G (no published detail), Agent-Shield (agent security scanning; class per yotta-verify), EMET and Engram (agent memory; class per NEXUS AGI), cloudcostwise (cloud cost cleanup; dev-infra) and Experience Bamfield (local travel vertical).

## Result

Catalog moved from 878 servers (+764 guides) to 880 servers (+766 guides).
