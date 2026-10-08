---
title: "MCP Server Discovery - October 8, 2026 (Midday Sweep)"
description: "Midday sweep cataloguing sourced competitor teardowns and an official LinkedIn data API for people, company, job and post lookups."
last_updated: 2026-10-08
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-october8-2026-midday/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp", "sweep"]
---

# MCP Server Discovery - October 8, 2026 (Midday Sweep)

Midday sweep over the mcp.so `/feed` (30 server links, direct fetch), mcpservers.org `/all` pages 1-3 through the r.jina.ai reader proxy (the fresh cohort diffed against the night sweep's dispositions and the full sweep ledger), and the fresh chatmcp/mcpso issue window #4936-#4951, with vendor docs and live checks for every candidate. Two new business-relevant entries, each catalogued with a guide: sourced competitor teardowns and an official LinkedIn data API for people, company, job and post lookups.

## New Servers Catalogued

| Server | Category | What it does |
|---|---|---|
| [Rivalize MCP](/hermes/mcp/servers/external/rivalize-mcp/) | Competitive Intelligence | One-call competitor teardowns (positioning, pricing, ads, social, reviews, hiring, momentum) plus a universe of tracked companies, projects, reports, battlecards, timelines and evidence - thirteen read-only tools and an opt-in write, stdio via `npx -y @rivalize/mcp` v0.3.2 with an `rk_live_` API key |
| [EnvoAPI LinkedIn Data MCP](/hermes/mcp/servers/external/envoapi-linkedin-data-mcp/) | Sales & Outreach | 40 read-only tools over public LinkedIn data - profiles (13), companies (6), search (11), jobs (2), posts (3), emails (`find_email`, `verify_email`) and websites (3) - hosted at `api.envoapi.com/mcp` with OAuth or an API key, 100 free credits and one balance shared with the REST API |

## Sources

- mcp.so /feed (30 server links, direct TanStack fetch)
- mcpservers.org /all pages 1-3 via the r.jina.ai reader proxy (the fresh cohort diffed against the night sweep's Oct 8 dispositions; the page counter moved from 14,651 to 14,770 servers)
- chatmcp/mcpso issues #4936-#4951 (fresh window since the night sweep cutoff at #4935)
- Vendor docs and live checks for every candidate (EnvoAPI POST initialize returns HTTP 401 "The access credential is missing or invalid."; Rivalize verified through its npm package v0.3.2, the MIT repo with its MCP Registry manifest, and the published changelog - it ships as a local stdio server, so there is no remote endpoint to probe)

## Core Listing Verification

- mcpservers.org: LISTED (`/servers/corpusiq-io` 200 via the reader proxy, title "CorpusIQ MCP Server | Awesome MCP Servers")
- glama.ai: LISTED (title "corpusiq MCP Servers | Glama", `io.corpusiq` connector references present)
- smithery.ai: LISTED (registry serves `Cprusiq` / displayName CorpusIQ; direct slug 200)
- PulseMCP: LISTED ("Official CorpusIQ MCP Server | PulseMCP")
- mcp.so: NOT LISTED (search payload carries no server object; quarantine holds, no resubmit)
- No submissions this cycle: every automatable target is either listed or in its established hold state. Directory watch: JFrog Universal MCP Registry and Prefect Horizon registry surfaced as enterprise-governance registries, not public listing targets.

## Also Identified (Not Catalogued)

On the mcp.so feed, the fresh entries beside the two catalogued were Priors (on-chain credit records for ERC-8004 agents on Robinhood Chain; agent-payments class per the steward-mcp and Mekler dispositions, held), Multi Upload Tool (video publishing and scheduling across nine platforms; social-publishing class at saturation with Antwork, Sprkly and Blog2Social), Rumoro (social listening across Reddit, X, Hacker News and GitHub; class covered by the catalogued Octolens per the Mentio disposition) and iDevice Buyer's Guide (consumer device buying guide per the iDevice Wearables hold); every other block was a repeat or prior disposition from the October 3-7 ledgers (EximAgent catalogued in the night sweep; Optimus MCP, Clipping Alpha, 3GPP Scout, MilliGate, x402-list-mcp, the grill planner, AssetLab, Listings API, Testiny, The Bridge, North Noir, Nitrosend, PubShip, KissCode, Localith, SpicyAPI, SlickTrip, PayPerFax, mxHERO, Snov.io, AdvisorIQ, ETFIQ, Gastrosync, Leverage, Ybug, AskOne, Chalet-Montagne, Snipzr and Heard).

On the mcpservers.org /all pages 1-3, the fresh top cohort resolved to LinkedIn Data MCP and Rivalize catalogued above, looot and RealtyPad and Booksmate as already catalogued, Bitculator as a prior hold, and the remainder of the three pages as the October 6-7 disposition cohorts (UK fleet reruns, Voidmail, Kasar CRM, OperStack, APEX Faucet, Kvickd, Ta Rodando, Brasil Data, OlaChill, CPFHub, Datalake-mcp, Checkbox, Fresh402, Rein Agent Risk Scale, Chatpack, conv2pdf, Teleloom, Endzone, ibara, Ball Ranks, Dreamwork, Steward, Bilbop and the rest).

From the fresh chatmcp/mcpso issue window #4936-#4951: the two catalogued above; held or skipped: Costory (already catalogued June 24 - the mcp.so submission is packaging, not a new class), guard-core-mcp (Python security-config analysis; dev-utility class), the theluckystrike five-server relistings at mcp.zovo.one (quotes, invoice, time-tracker, spreadsheet, pdf; the vendor's TheLuckyStrike Ops Suite is already catalogued and prior single-server relistings were disposed - held as repeats of a catalogued family), Haulest (licensed-mover quote requests; consumer services class per the OnArrival and Kirah dispositions), Global FinReg (LEI register lookups; class covered by the catalogued Prometiam Risk and ENTIA entity-verification entries), NEXUS AGI (agent memory and knowledge graph; agent-memory class), Shinjuku Shielded (shielded x402 payments on Solana; crypto class), Landbot (single-vendor conversion-agent platform connector; class per the Kasar CRM and TeamShift holds), Tanod (prior disposition stands), Layout Debug (dev tool) and LayerMap (prior disposition, dev utility).

## Result

Catalog moved from 876 servers (+762 guides) to 878 servers (+764 guides).
