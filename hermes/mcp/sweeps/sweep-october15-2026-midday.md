---
title: "MCP Server Discovery - October 15, 2026 (Midday Sweep)"
description: "Midday sweep cataloguing an accounts-receivable MCP layer for Xero and QuickBooks Online."
last_updated: 2026-10-19
canonical: "https://www.corpusiq.io/docs/hermes/mcp/sweeps/sweep-october15-2026-midday/"
robots: "index,follow"
tags: ["mcp server", "model context protocol", "hermes mcp"]
---

# MCP Server Discovery - October 15, 2026 (Midday Sweep)

Midday sweep about 13 hours after the October 14 evening sweep. Surfaces: the mcp.so `/feed` (30 server links via the r.jina.ai reader proxy; two cards fresh past the evening capture), mcpservers.org `/all` pages 1-5 through the r.jina.ai reader proxy (145 slugs; the delta against the evening capture was dominated by the mid-October ingestion wave already dispositioned on the canonical list), the fresh chatmcp/mcpso issue window #5428-#5457 (30 numbers), and a fresh twelve-sitemap canonical refresh (r121: 15,625 server URLs; six additions and zero removals against the r120 capture), with vendor docs, live endpoint probes and class-precedent passes for every candidate. One new business-relevant entry, catalogued with a guide: the accounts-receivable layer for Xero and QuickBooks Online.

## New Servers Catalogued

### Paidnice MCP - Accounts Receivable for Xero and QuickBooks

The receivables layer that sits between the ledger and the customer conversation. Xero or QuickBooks holds the ledger; Paidnice holds what happens after the invoice goes out, and the MCP server lets an assistant read both in one chat. It triages customer replies into promises, questions and disputes ranked by what each customer owes, checks whether a "we already paid" claim has landed as a payment or a deposit waiting to be reconciled, briefs you before a call, and keeps contacts current from cc lines and out-of-office replies. A beta set adds the multi-client accountant path (every client in one chat), a month-end pack with DSO, overdue and collected per client, a cash forecast, an approval queue for drafted reminders and statements, and escalation work surfaces. Built for AI-first finance teams and the accountants who manage many clients; Xero Global App Awards 2026 App of the Year.

Relevance: HIGH. **Endpoint live** (POST initialize to `https://api.paidnice.com/mcp` returns 401 for the OAuth flow; the app host at `app.paidnice.com/mcp` returns 200), **official registry entry** (`com.paidnice/mcp` v1.0.0), and vendor docs live (paidnice.com and docs.paidnice.com both 200). Included with the Pro and Custom plans; a bearer-token REST API is documented alongside.

## Also Evaluated (Not Catalogued)

The mcp.so feed carried two cards fresh past the evening capture, both held: **The Living Bread** (Bible passages with an evidence label, keyword search and cross references; the novelty and consumer-content rule) and **Logimu Shopping MCP** (Amazon US, UK, DE, CA, AU, FR, IT, ES, JP, MX and BR plus Walmart US product data with ranked search, prices, stock, sellers, the Buy Box and price and sales-rank history; the e-commerce product-data class is covered by the catalogued Datrace, Pangolinfo and AMZ Vault entries and the Ecommerce Data API hold). Every other feed card carried a prior disposition from the October 13-14 ledgers (fixRAgent, PostPlanify, Blend MCP, UGCfy AI, DatePhotos.AI, ProfessionalHeadshot.io, Pitch Protocol, Cite42, BackPow, Crowded Finance, Hubity, heyhey, FastSocial, transcribe.so and the rest).

On mcpservers.org `/all` pages 1-5, the window delta against the evening capture was 91 slugs, 62 of them members of the r120 canonical addition wave the evening sweep already dispositioned by name. The remainder resolved to 404 shells and author or account paths (petshopbros, transcenduk, expeditedprojects, elicitly, beppetemp, idos-games, iamsal, officialspicrawl, cbecks1212, bradraylucas-eng, murphywuwu, norcalnappy, punsnprotons, random00000000, lordfreez-ship-it, conorbronsdon) and to class holds: Catchr (agency marketing reporting across 100+ sources; the cross-channel marketing class is dense per the catalogued Blend MCP and Get Ads entries), Fixter (APM and error tracking for agent-built apps; dev-infrastructure class), Nifty PM (tasks, projects and docs; workspace and PM class per the catalogued Monday.com, Notion and Taskade entries), PostEverywhere (social publishing across twelve networks; the social-publishing class is at saturation per Pith and PostPlanify), CarWhere VIN (VIN decode, NHTSA recalls and buyer pricing; the vehicle-data class per CarDossier and Dutch Vehicle Context), CloudCorpRecords (contributor-tool fleet), InsightSocial (social-data density), Elfsight (site widgets; consumer utility) and Polymarket Wallets (crypto class).

From the fresh chatmcp/mcpso issue window #5428-#5457 (30 numbers), all held beyond the catalogued entry: Clarity Today (tech-news feed, keyless; news class per apitube and webz), Citepath (self-hosted cited documentation search; docs and RAG utility class), Lomen (cookie-free website analytics with Stripe, Shopify, Lemon Squeezy and Polar revenue; the analytics class per the catalogued Umami entry), OpenSDR (open-source AI SDR on your own keys; the lead-data class is dense per Crustdata, EnvoAPI and the LeadBoxer hold), Brandname Maker (naming with registry domain checks; creative-novelty utility), Upstream (live API status, deprecations and breaking-change digests; the status class per APIzone, HostTracker, Drumbeats and pingcheck), MnogoReels (long video to captioned shorts; media-generation class), China News Feed (regional news and hot lists over an Apify actor; regional-news and Apify-distribution classes), Scalelist (B2B lead finder with verified work emails; lead-data class dense), closure_drift (release-tag drift checks; dev utility), Agent Wake (scheduled agent wake-ups; agent-infrastructure utility), Signal Leads (sales leads with public signals; lead-data class), Agent Access Check (whether a site will let an agent in; agent-web utility), Log10x (log pattern cost ranking and tier-down planning; DevOps utility), AegisCore (pre-execution policy enforcement and audit ledger for MCP tools; agent-security class), briar (local knowledge store built from GitHub, Bitbucket, Jira and Linear history; knowledge-store class), MeshArc (web crawler to markdown with change tracking; scraping class saturated), EyalSec (read-only taint-analysis events; security class), MIZAN (whether a trading agent's track record is real; crypto and agent-verification classes), own-words (notes into a study deck; education utility), SwiftNodes (blockchain RPC across 125+ chains; crypto infrastructure), Account Hiring Watch (company job-board changes and hiring velocity; the mambabuilt job-change family and hiring-signal classes), ProvenPin (version-pinned code recipes with test receipts; dev utility), Fitatu (Polish calorie counter; consumer fitness), UEAgent (Unreal Engine editor tooling; game-dev utility), Swifteq for Zendesk (Zendesk support operations; single-vendor support-platform connector), VibeAudit (one-shot security-audit overview; security utility), Aloof (backend PaaS deploy and operations; single-vendor dev-infrastructure class), Toolweather (whether an MCP server or tool is safe to call right now; meta and dev-infrastructure classes) and CareJobs.Now (US healthcare jobs read from 258 employers' own career sites with posted pay; the jobs-data and careers classes per Applystead, RobotTraining.jobs and Web Remote Jobs).

Canonical window check (r120 to r121: six additions, zero removals): the additions were CarWhere VIN, Catchr, Fixter, Nifty PM, Paidnice and PostEverywhere; all six appear on the `/all` surface and five are held above, with Paidnice catalogued.

## CorpusIQ Listing State

Checked this cycle (unchanged):

- mcpservers.org: LISTED (`/servers/corpusiq-io` serves the CorpusIQ page)
- glama.ai: LISTED (`io.corpusiq/multi-source-mcp` connector plus the CorpusIQ server entry)
- smithery: LISTED (registry query returns `Cprusiq` as the first result)
- mcp.so: NOT LISTED (four-slug direct probe all 404; quarantine holds, no resubmit)

No changes to the CorpusIQ listing state this cycle.

## Result

Catalog moved from 928 servers (+814 guides) to 929 servers (+815 guides).
