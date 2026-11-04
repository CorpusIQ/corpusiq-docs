---
title: "MCP Server Discovery - November 4, 2026 (Midday)"
description: "Midday sweep: one crawl-telemetry surface catalogued, five fresh directory listings dispositioned, and 27 submissions read with bodies."
last_updated: 2026-11-04
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-november4-2026-midday"
tags: ["mcp server", "model context protocol", "hermes mcp", "sweep"]
---

# MCP Server Discovery - November 4, 2026 (Midday Sweep)

## Summary

Eight hours after the night pass, and for the first time in four passes the directory counters barely moved. The twelve-sitemap canonical grew by **five** server URLs, mcpservers.org `/all` page one churned two slugs out and two in without changing its character, and the mcp.so `/feed` carried a single card above the night stamp. The submission window carried the rest: **27** items between **#6719** and **#6745**, one of which is a listing-removal request rather than a submission.

One arrival earned a guide. **NMOS.NET Crawl Analytics MCP** is the catalogue's first surface that reads *observed* crawl telemetry rather than a proxy for it: which search and AI bots actually arrived on your own pages, on which day, whether they got a 200 or a policy block, and whether the `llms.txt` you published is being fetched at all. Every other AI-visibility entry here measures the answer side of that pipeline. This one measures the input.

The reading rule this pass is about honesty at a small delta. Five new listings, six probes and twenty-seven submissions produced one guide, and the disciplined record is the disposition line for each hold rather than a padded batch. A crawl-log surface is new; the twenty-sixth stock-research endpoint, the twenty-first SEO suite and the fourth agent-wallet are not.

A note on execution: a **10:00 to 10:05 MST attempt** ran these same surfaces and stopped mid-run without committing. Its twelve-sitemap capture and its `/all` pages one to five were reused rather than refetched, and the window delta was recomputed from the two captures on disk rather than taken from the dead run's output. The canonical diff below is a fresh set difference on those files.

## Sources Swept

| Source | Read | Result |
| --- | --- | --- |
| chatmcp/mcpso submission window | authenticated `gh api`, bodies included, one call | **27** items **#6719** to **#6745**, one a listing-removal request, 26 submissions |
| mcp.so `/feed` | direct fetch with a browser UA, `createdAt` parsed from `recentServers` | **124** objects, newest `2026-11-04T14:37:59Z`, **one** card above the night stamp of `2026-11-04T09:41:03Z` |
| mcpservers.org `/all` | r.jina.ai reader proxy, two reads | counter **19,342** then **19,344**, page-one composition churn with two slugs in and two out |
| mcpservers.org twelve-sitemap canonical | captures at 04:30 and 10:15, set difference recomputed | **19,339** unique URLs to **19,344**, **5** additions and **0** removals |
| Endpoint probes | keyless `initialize` on six endpoints | **2** answering **200** (`workload-zero` **2.1.0** with **149** tools, `gameshipkit` **1.0.0**) and **4** answering **401** |

## New Servers Catalogued

### NMOS.NET Crawl Analytics MCP - Observed AI Bot Visits

Relevance: HIGH. **Tier 3, measured 401** (`initialize` answered `HTTP 401` with JSON-RPC `-32001 Unauthorized. Connect via OAuth or send Authorization: Bearer ***`), so the endpoint is live and gated and no tool was called.

The surface is cookieless crawler tracking with a read-only MCP façade. A site installs a meta tag plus `tracking.js`, a no-JS beacon, or a Cloudflare Worker, and the service records every search and AI crawler visit; the six tools read it back: `list_sites`, `list_bot_visits`, `get_crawl_stats`, `get_traffic_overview`, `get_robots_status` and `get_site_health`.

What makes it worth an entry is the direction of measurement. The catalogue holds the answer side three ways already: [NM Signals](/hermes/mcp/servers/external/nm-signals-mcp/) audits how crawlers *would* see a URL, [AIO.GEO](/hermes/mcp/servers/external/aio-geo-mcp/) audits structural readiness and dry-runs fixes, and [Encited](/hermes/mcp/servers/external/encited-mcp/) mines Search Console and answer-engine visibility. None of them can answer whether the crawler came back after a migration, or whether the fetch returned a 403. That is the distinction an operator needs when a page that ranks on Google is invisible to an assistant: a page never fetched is an access problem, and no amount of rewriting fixes it.

The honest limit is the vendor's own sentence, and it is quoted in the guide: NMOS shows visit records and policy signals, not search rankings or model-training proof. The paid line matters too. The free plan is one site and **100** crawl visits a month with crawl analysis only; `llms.txt` coverage, sitemap coverage, reverse-DNS bot authenticity and the crawl-like-a-bot simulation all start at **Pro, $20 a month**, and the integrations panel at **Pro+, $40**. Yearly billing is 10x monthly.

## Read and Held, With the Measurement Behind Each Ruling

**The five fresh directory listings.** `astraeye-labs-mcp` is AI research reports over US stocks, ETFs and crypto, read out of one account, held on the stock-research class that already carries Altair, ValuEdge, fAlpha, BDE and the nine EDGAR surfaces. `exclusive-digits-phone-numbers-mcp` sells US phone numbers by city, area code, word and pattern, a number-inventory commerce surface rather than a business data feed, held with the phone-number and lead-generation inventories. `orinyx-mcp` tests healthcare agent claims against cited FDA label text on synthetic data only and says so in its own description, held as a healthcare vertical beside TMSClinics, SleepStudies and test-well. `lingviko-com-der-die-das` is German noun-gender drill, outside operator scope and already named by the night pass. `snapwidget-mcp` answered a live detail page and builds an Instagram feed widget and hands the paste-ready code to a coding agent, held as a website embed widget rather than a data surface: it makes a marketing asset, it does not read the business.

**The feed card.** `Gamebeast` at `2026-11-04T14:37:59Z` is the official server for one game LiveOps platform: player behaviour, experimentation and live operations inside a publisher's own projects. Held as a single-vendor vertical analytics connector, the class carried by the platform-specific entries, with the promotion test recorded: a game-studio operator asking cross-platform player questions would want it beside general analytics, and nothing here serves a business outside games.

**Measured 200 and still held.** `workload.zero` at `https://mcp.workloadzero.de/mcp` answered keyless `initialize` **200** as `workload-zero` **2.1.0** with a **149**-tool surface, the widest in this window: profile and colleagues, projects and budgets, clients, tasks and subtasks, time entries and timers, goals, deals, quotes and quote-to-invoice conversion, revenue. It is a hosted German business suite and it is held on class rather than dismissed, because the CRM and revenue slice is carried by [Deskhand](/hermes/mcp/servers/external/deskhand-mcp/), NOVA for Kommo, Finwise, [Reciba](/hermes/mcp/servers/external/reciba-mcp/) and Volanea, and the project and task slice by the project-management entries; the German hosting and the OAuth DCR are regional packaging of a covered shape, not a new measurement. `EZ@Work` answered **401** on `mcp.ezatwork.com/mcp` and is the freelancer version of the same slice, clients, projects, time and invoices. `GameshipKit` answered keyless **200** as `gameshipkit` **1.0.0** with five tools over 69 browser tools for sprite, pixel-art, VFX and store assets, outside operator scope.

**Measured 401 and held.** `Links as a Service` answered **401** `invalid_token` on `app.linksasaservice.com/api/mcp`, a Danish link-building marketplace with 150k publisher domains and open prices at publisher cost plus a 20 percent margin. It is the closest call in the window and it is held for two reasons: the link-building slice is already carried by [RankControl](/hermes/mcp/servers/external/rankcontrol-mcp/) as part of an SEO content programme and by [MentionAgent](/hermes/mcp/servers/external/mentionagent-mcp/) for placement outreach threads, and what remains is a checkout with an MCP wrapper around inventory that is bought, not data that is read. `Smitline` is a self-hosted open-source server that places phone calls and joins Zoom, Teams and Meet, held on two carried classes at once: voice by PlaceCall and the calling entries, and meeting notes by [Granola](/hermes/mcp/servers/external/granola-mcp/), ParrotNotes, Tactiq and Lavox. `UX Pilot` answered **401** `-32001 API key is required` and drives UI design on its own canvas, held on the design-tool class. `Tabula`, `Kipurse`, `I Am Wallet` and `Haris Guardian` are agent credit, agent wallets and Solana rug checks, held on the agent-payments and crypto classes carried by [FiatDock](/hermes/mcp/servers/external/fiatdock-mcp/), CoinVello, SnapEX Pay and Spectra. `Dopamyn` is crypto audience intelligence on X and is held on the creator-analytics class with the crypto qualifier. `run.zero` is a German PaaS an agent deploys to, `Mobilebox` a cloud-Android device farm, and both are developer infrastructure. `UberLLM` and `Sirv AI Studio` are media generation, saturated. `Postly` prints and posts physical letters to Danish addresses, held beside the print-and-mail entries. `Same Day Website Builder` builds a trades-business demo site, held on the site-builder class carried by Jaybird and iter0. `CallAI SEO` is pay-per-call SERP data on the twenty-guide SEO class. `AI SENSE Free Public Tools` is **77** free utilities as one endpoint, an aggregator. `pdf-table-pull-lite`, `doc2md-lite` and `link-check-lite` are one maintainer's three local utilities, and `seam`, `Markdown Pipeline`, `ipvolt Proxy Toolkit` and `AdminHub for Telegram` are a diff reviewer, Jira-to-Markdown sync, proxy set-up guides and a hosted Telegram publisher, all developer or messaging tooling. `PitchHighway` is vocal practice, `GameShipKit` and `Gamebeast` are games, and `#6745` is a request to retire an unmaintained community prototype in favour of the maintained FinancialFilings server, housekeeping rather than an arrival.

**The `/all` composition churn.** Page one swapped `github-com-foreverworks-mcps-tree-main-servers-eas` and `reciba-com-br-para-agentes` out for `lingviko-com-der-die-das` and `snapwidget-mcp`, a two-slot rotation with no new cohort behind it: every other slug on the page is inside the wave the night pass dispositioned by cohort.

## Count

The guide tree held **1,098** directories before this pass and holds **1,099** after it, **1,242** entries counting single-file guides before and **1,243** after. Sources: the chatmcp/mcpso submission window **#6719** to **#6745**, **27** items with bodies in one authenticated call; the mcp.so `/feed` fetched directly with a browser UA, **124** objects parsed with the newest at `2026-11-04T14:37:59Z`; mcpservers.org `/all` read twice through the reader proxy at **19,342** and **19,344**; a twelve-sitemap canonical set difference from **19,339** to **19,344**, **5** additions and **0** removals; and **6** endpoint probes, **2** answering **200** and **4** answering **401**.
