---
title: "MCP Server Discovery - October 9, 2026 (Night Sweep)"
description: "Night sweep cataloguing a trading terminal for agents, agent-initiated customer requests, and agency marketing reporting in chat."
last_updated: 2026-10-09
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-october9-2026-night/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp"]
---

# MCP Server Discovery - October 9, 2026 (Night Sweep)

Night sweep over the mcp.so `/feed` (30 server links via the managed extractor), mcpservers.org `/all` pages 1-5 through the r.jina.ai reader proxy (the fresh cohort diffed against the October 8 r91 canonical capture of 14,913 server URLs and cross-referenced against the catalog and the full sweep ledger), and the fresh chatmcp/mcpso issue window #4976-#5022, with vendor docs and live endpoint probes for every candidate. Three new business-relevant entries, each catalogued with a guide: a finance terminal with quant engines for agents, agent-initiated customer information requests, and agency marketing reporting in chat.

## New Servers Catalogued

| Server | Category | What it does |
|---|---|---|
| [Fincept MCP](/hermes/mcp/servers/external/fincept-mcp/) | Finance | Fincept Terminal as 440 hosted tools and 15 quant engines - quotes, options, filings, portfolios, backtests, ML forecasts and risk optimization, paper-trading only |
| [Formstep MCP](/hermes/mcp/servers/external/formstep-mcp/) | Business Operations | Agent-initiated requests - send one customer a branded prefilled form, collect files, signatures and answers back under field keys, with callbacks |
| [DashThis MCP](/hermes/mcp/servers/external/dashthis-mcp/) | Marketing Analytics | DashThis dashboards from any assistant - list dashboards, read live widget values for any period, export client-ready PDFs and write comment boxes |

## Sources

- mcp.so /feed (30 server links, managed extractor)
- mcpservers.org /all pages 1-5 via the r.jina.ai reader proxy (the fresh cohort diffed against the October 8 r91 canonical capture of 14,913 server URLs; the canonical refresh across all ten sitemaps brought 14,916 URLs, whose net-new members resolved to holdings, a fragment duplicate and a 404 shell)
- chatmcp/mcpso issues #4976-#5022 (fresh window since the evening cutoff at #4975)
- Vendor docs and live endpoint probes for every candidate (Fincept POST initialize returns 401 "Authentication required."; Formstep returns 401 with OAuth protected-resource metadata; DashThis is a connector-directory setup with OAuth and no public endpoint URL)

## Also Identified (Not Catalogued)

On the mcp.so feed, the fresh entries beside the three catalogued were nittim (security audit for AI-written code; security-scan utility class), FeedShine (Google Shopping feed management; single-vendor app connector disposition stands), FUSE Health (health-sector remote server; thin listing) and Shopify SEO Expert (vendor repeat); every other block was a repeat or prior disposition from the October 3-8 ledgers (Aisle, MarginPad, CovaSyn, Priors, Multi Upload Tool, Rumoro, iDevice Buyer's Guide, Rivalize, EximAgent, Optimus MCP, Clipping Alpha, 3GPP Scout, MilliGate, x402-list-mcp, the grill planner, AssetLab, Listings API, Testiny, The Bridge, North Noir, Nitrosend, PubShip, KissCode, Localith, SpicyAPI, SlickTrip, PayPerFax and the rest).

On mcpservers.org, the site-wide delta since the r91 capture resolved to: apimart (AI model API marketplace; aggregator class per PZERO), the DemandSense LinkedIn Ads Intelligence Hub (LinkedIn ads attribution with website visitor identification and CRM pipeline matching; LinkedIn Ads operations class covered by the catalogued AdPlug entry - flagged as the closest call of the cycle), ninetails GnuCash (local-first desktop bookkeeping; class covered by the catalogued SuperBooks entry), Reduck (browser-script automation; class per the Bowmark browser-automation holds), Rumoro (social listening; class covered by the catalogued Octolens) and shotpipe (sitemap-fresh but a 404 shell on the detail route).

The overnight pass additionally dispositioned a previously unledgered October 8 cohort surfaced by page churn: Tommos (single-vendor CRM workspace; class per the Kasar and TeamShift holds), QueryInbox (read-only Search Console and GA4 pass-through; class covered by the catalogued AgentGrown and the QuerySail disposition), Returnolio (stock research; class saturated per ETFIQ, Silicon Floor and Market Eyes), MetricDuck (SEC filings and financials; class covered by the catalogued Edgrapi), WITAN (x402 agent knowledge marketplace; agent-payments class), Pozeidon (mobile-network creative and campaign operations; ad-ops saturation, mobile-network wedge noted), Vendwiser (Romania eMAG and Oblio operations; geo-niche class), Goldbeater (Google Ads findings layer; Google Ads class dense with Markifact, Get Ads and PaidSync catalogued), seatledger (local coding-agent cost forensics; dev-FinOps utility), DocuGrip (PDF tool directory links; document-utility class), agpay (stablecoin escrow between agents; agent-payments class), Constructelligence (offline construction reference; niche vertical), Buildability (US parcel scoring; land-data adjacent to the catalogued LandLens), DatosIA (Central America official data; regional dataset class), StatOSS (status pages; dev-infra), Siteprint (design scans for coding agents; dev-design utility), Launch Ready (website scans for agencies; audit class beside SiteAnalyzerFree), Portproof and HProxy (proxy utilities), Clipy (recording library access; media utility), Squadcard (amateur football organiser; consumer), pylos (read-focused IMAP; class covered by the catalogued imap-mcp), Content Sweep (copyright takedown workflow; class per the DMCA Cases hold), Cobrain (setup guides; content shell), AgentBrief (paid research briefs; narrow research utility), SoulStack (app portfolio scores; indie utility) and Datrace (Amazon keyword and ASIN market data; the cycle's strongest held candidate, flagged for the next sweep), with the dev, consumer and regional remainder as class-group holds.

From the fresh chatmcp/mcpso issue window #4976-#5022: held or skipped the theluckystrike forty-item batch (the vendor's TheLuckyStrike Ops Suite is catalogued; this batch is a repeat of a catalogued family), Octocrawl (web scraping with evidence records; scraping class dense), Elementor MCP (already catalogued; the submission expands the WordPress plugin's surface), DrinkedIn (agent bar simulation; consumer novelty), Lane Planner (personal planning; OpenKrill family), the Homey smart-home bridge (consumer), url-to-pdf (document converter; commodity class); Fincept catalogued above.

## Result

Catalog moved from 880 servers (+766 guides) to 883 servers (+769 guides).
