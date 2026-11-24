---
title: "Catalog Sweep Log Archive - August 1-15, 2026"
description: "External MCP server catalog sweep log, August 1-15, 2026 archive: directory movement, measured candidates, hold decisions"
canonical: "https://www.corpusiq.io/docs/hermes/mcp/servers/external/changelog-2026-08a/"
robots: "noindex,follow"
last_updated: "2026-11-24"
tags: ["mcp server", "model context protocol", "sweep log"]
---

# External MCP Server Catalog - Sweep Log, August 1-15, 2026

Archive for August 1-15, 2026. Discovery passes appear newest first. The [current sweep log](/hermes/mcp/servers/external/changelog) carries the most recent passes.

Archive: [July 16-31, 2026](/hermes/mcp/servers/external/changelog-2026-07b) | [August 16-31, 2026](/hermes/mcp/servers/external/changelog-2026-08b)

## 🆕 August 15, 2026 - Evening Cron Sweep (2 New, 2 Guides)

Scanned mcpservers.org /all pages 1-2 (newest submissions) and mcp.so Feed (30 newest submissions). 2 new business-relevant servers found - both financial data: a congressional-trading disclosure server with per-trade anomaly scoring, and an options-analytics stack with a published agent-sized API reference.

### GovTrade MCP ★★ - August 15 evening

Congressional trading disclosures over MCP - STOCK Act filings (House and Senate) with pre-computed anomaly signals per trade (signal strength, Low/Medium/High label, natural-language reasoning covering unusual size versus the politician's own history, committee overlap, and federal contract ties) plus per-politician baselines (trade count, average size, buy/sell ratio, top sector). Self-hosted stdio via `node index.js` with a funded EVM wallet; paid per call via x402 (USDC on Base), no subscription. `github.com/iamdarcie/govtrade-mcp`. (commercial, pay-per-call) · [Guide →](/hermes/mcp/servers/external/govtrade-mcp)

### ApexVol Options Analytics MCP ★★★ - August 15 evening

Options analytics over MCP - options chains (live, historical, simulated), IV rank and crush, Greeks and GEX (market, cross-index, portfolio level), expected moves, skew and term structure, screeners, mispricing and relative-value scans, strategy build/optimize/stress-testing. 43 tools over 56 published REST endpoints; one Pro bearer token drives both the self-hosted `apexvol-mcp` client and direct REST calls. MIT, `github.com/ryansilk/apexvol-mcp`. (commercial, Pro plan) · [Guide →](/hermes/mcp/servers/external/apexvol-mcp)

**Also identified (not catalogued):** PDI Bridge for Claude (ServiceNow PDI dev-instance bridge - query tables, review Business Rules/ACLs/client scripts; dev tool, not business ops), Picorn (image/video creative projects - one-liner listing with no MCP tool depth), GOJI (Melbourne agency knowledge bot answering AEO/SEO questions from its own published material - agency marketing surface), apix402 (onchain governance/vesting/oracle checks - x402 infra, consistent with prior skips), WEM Price Compare (repeat of the Aug 15 morning skip - consumer/affiliate), EraseText and AI Image Cleaner (consumer image utilities), a Chinese raw-IP listing (shenshaoyin, endpoint on 121.40.18.232) and a trycloudflare exposed-port slug (host-dump noise). Feed repeats already catalogued or previously skipped this cycle: Etincel, CryptoStruct, World Monitor, API Direct, JobYap, Kin, NexusTrade, Snipara, RADAAR, BlazingCDN, Cost Seg Smart, easydocforms, Just Domain, Fakto wFirma, FARPY, CoinLobster, EM+x, SceneF, LabTestSuperstore, Prose Coach, Clipkit, CR8 Agent Commons, x402 Merchant Check, directree, Syncro.

**Key observation:** Both entries confirm the pattern of financial-data vendors shipping a published, agent-sized API reference alongside the MCP surface - ApexVol's single-file `apexvol-api.md` is the cleanest example yet of docs designed for agent consumption (explicit 401/403/426/429 semantics so an agent can tell revoked-token from tier-entitlement from rate-limit failures). GovTrade extends the x402 pay-per-call model from infrastructure into disclosure-grade financial data, with anomaly reasoning attached to every signal.

---

## 🆕 August 15, 2026 - Midday Cron Sweep (1 New, 1 Guide)

Scanned mcpservers.org /all pages 1-3 (newest submissions) and mcp.so Feed (30 newest submissions). 1 new business-relevant server found - a deterministic AI-writing-tell detector with trainable brand voices and CI support, the local/self-hosted complement to Prose Coach.

### Etincel MCP ★★★ - August 15 midday

Deterministic AI-writing-tell detector - 20 tools that audit non-fiction prose for AI patterns (banned hype vocabulary, chatbot fingerprints, structural tells like uniform paragraphs and em-dash overuse), train brand voices from real writing samples, and measure drafts against a voice baseline. Local stdio install via `npx etincel serve`, MIT, dictionary-as-code in `.etincelrc`; GitHub Action for CI. Optional hosted API at `etincel.ai/api/mcp` for the one model-based tool (`second_read`). (open source, free; hosted model call billed) · [Guide →](/hermes/mcp/servers/external/etincel-mcp)

**Also identified (not catalogued):** Feed repeats already catalogued or previously skipped this cycle: CryptoStruct, World Monitor, API Direct, JobYap, Kin (dev tool), NexusTrade, Snipara (previously skipped), RADAAR, BlazingCDN, Cost Seg Smart, easydocforms, Just Domain, Fakto wFirma, FARPY (dev infra), CoinLobster (crypto), EM+x, SceneF (consumer), LabTestSuperstore (lab supplies), Prose Coach, Clipkit, CR8 Agent Commons, x402 Merchant Check, directree, Syncro, ROIC.ai, Conqueror, NERAI. A raw-IP Chinese listing (shenshaoyin, endpoint on 121.40.18.232) excluded as junk signal. mcpservers.org /all pages 1-3 carried no other new business-relevant slugs - the holoweave slug resolves to Citation Check (already catalogued Aug 14); a trycloudflare exposed-port slug excluded as host-dump noise.

**Key observation:** The de-AI content stack now has both delivery models - Prose Coach as the no-auth remote filter and Etincel as the local, CI-runnable install with trainable voice profiles. Etincel's loop (train from samples → check drafts against the measured baseline) turns brand-voice compliance from reviewer eyeballing into a measurable gate, and `audit_text`'s strengths counter-signal guards against the fix-everything-into-flat-prose failure mode.

---

## 🆕 August 15, 2026 - Morning Cron Sweep (10 New, 9 Guides)

Scanned mcpservers.org /all pages 1-3 (newest submissions) and mcp.so Feed (30 newest submissions). 10 new business-relevant servers found - a 63-tool global-intelligence platform, crypto and prediction-market data procurement, index monitoring with an honesty flag, structural GEO auditing, free e-signature, multilingual content ops, tamper-evident agent logging, the official Datadog observability bridge, the official Loops email MCP, and agency operations.

### World Monitor MCP ★★★ - August 15 morning

Live global-intelligence platform over MCP - 63 read-only tools spanning markets, geopolitical risk, conflicts, aviation, maritime, energy, climate, cyber threats, supply chains, sanctions, public health, and procurement, all source-attributed with `cached_at`/`stale` freshness stamps. OAuth 2.1 or API key, Streamable HTTP at `worldmonitor.app/mcp`. AGPL-3.0 (`github.com/koala73/worldmonitor`). (commercial, free + Pro) · [Guide →](/hermes/mcp/servers/external/world-monitor-mcp)

### CryptoStruct Market Data MCP ★★ - August 15 morning

Historical crypto and prediction-market data - ~500K instruments across 35 venues, live OHLC/VWAP/depth/slippage statistics, free sample files, and Stripe-checkout data procurement at €1 per instrument-day. Keyless catalog and stats; optional OAuth for account tools. Streamable HTTP at `cryptostruct.com/mcp`, MIT. (commercial, free tier + €20/mo Premium) · [Guide →](/hermes/mcp/servers/external/cryptostruct-mcp)

### Seomely MCP ★★★ - August 15 morning

Google index monitoring with history - which pages are indexed, which dropped out and when, and why the rest are not. Every diagnosis carries a `submission_helps` honesty flag; `investigate_indexing` correlates regressions with their shared cause. Bearer API key, Streamable HTTP at `seomely.com/api/mcp`. Free 1K / Pro 25K / Agency 250K calls per month. (commercial) · [Guide →](/hermes/mcp/servers/external/seomely-mcp)

### SignSimple MCP ★★ - August 15 morning

Free e-signature workflow over MCP - send a PDF by URL, recipients get emailed signing links, poll status, download the certified result with a certificate page (signer list, timestamps, SHA-256 of the original). Four tools; ESIGN-act binding; no per-document fees. `signsimple.app/mcp`. (commercial, free) · [Guide →](/hermes/mcp/servers/external/signsimple-mcp)

### AIO.GEO MCP ★★★ - August 15 morning

Structural AI Search Readiness - audit what AI engines can see, dry-run fixes, rescore, doctor. Explicitly sells receipts, not LLM rankings. Self-hosted via `npx -y @aio-geo/mcp-server` plus CLI and public audit API; publishes a well-known server card, api-catalog, and agent-skills index. (commercial, free CLI) · [Guide →](/hermes/mcp/servers/external/aio-geo-mcp)

### Polyblog MCP ★★ - August 15 morning

Multilingual content operations over MCP - manage articles, localization coverage, and editorial plans through OAuth. Streamable HTTP at `mcp.polyblog.io/mcp`; parallel REST API at api.polyblog.io; publishes an ai-catalog.json and an agent plugin. (commercial) · [Guide →](/hermes/mcp/servers/external/polyblog-mcp)

### Arcaeon Ledger MCP ★★ - August 15 morning

Tamper-evident action logging for AI agents - hash-chained `ledger_append`/`ledger_verify` over one JSONL file with artifact binding and an optional external witness; built toward EU AI Act Article 12 logging. Self-hosted via `pip install arcaeon-ledger`; names its own non-proofs in the README. (free, open source) · [Guide →](/hermes/mcp/servers/external/arcaeon-ledger-mcp)

### Datadog MCP Server ★★ - August 15 morning

Official observability bridge - APM, logs, metrics, monitors, dashboards, and security signals for MCP-capable agents. OAuth via the coterm CLI installer; toolsets scoped at connection time; every MCP action lands in Datadog's Audit Trail. Fair-use 50 req/10s burst, 50K monthly tool calls. (commercial, included with Datadog) · [Guide →](/hermes/mcp/servers/external/datadog-mcp)

### Loops MCP Server ★★★ - August 15 morning

Official Loops email-platform MCP - contacts, mailing lists, campaigns, transactional email, and account data, paired with a CLI, agent skills, and a Claude plugin marketplace entry. Connection flow documented for Claude Code and Claude Desktop. `loops.so` (commercial) · [Guide →](/hermes/mcp/servers/external/loops-mcp)

### Corcava MCP ★★ - August 15 morning (catalog entry)

Agency operations over MCP - projects, tasks, and time tracking through Corcava's remote endpoint at `app.corcava.com/mcp`. Thin docs (no published tool list or auth detail); classified Productivity. (commercial)

**Also identified (not catalogued):** Pixero (AI marketing agent for Meta ads - docs are a JS-only shell with no tools, auth, or endpoint published; thin-docs rule), Duvo (grocery/retail execution runs with approvals - vertical niche), WEM Price Compare (cross-retailer price comparison, disclosed affiliate - consumer), Wakelog (hosted changelog publishing - niche utility), Daily Studio (iPhone teleprompter - consumer), Routebase (OpenAPI design/mock/testing - dev tool), Hamptons Verified (hyperlocal fact-checking - consumer). Feed repeats already catalogued or previously skipped this cycle: RADAAR, BlazingCDN, Cost Seg Smart, API Direct, NexusTrade, JobYap, easydocforms, Just Domain, Fakto wFirma, EM+x, Prose Coach, ROIC.ai, cloro, BanProof, NERAI, Citation Check, Customer Intelligence & Segmentation, Viral Outliers, Holdings, Kin, Snipara, Syncro, CoinLobster, FARPY, SceneF, LabTestSuperstore, CR8 Agent Commons, x402 Merchant Check, directree, Conqueror, Clipkit.

**Key observation:** This sweep filled the last two structural gaps in the operator stack - observability (Datadog official) and email execution (Loops official) both landed vendor-first-party MCPs - and the GEO/SEO layer thickened with two anti-theater products (Seomely's `submission_helps` flag, AIO.GEO's no-LLM-rankings stance). Second, World Monitor is the first full-spectrum geopolitical-intelligence MCP: the NERAI class grew from calibrated forecasts into a 63-tool operating picture with procurement and sanctions surfaces. Third, compliance tooling keeps moving down-market - Arcaeon ships EU AI Act-style tamper-evident logging as a pip-installable stdio server with named non-proofs.

---

## 🆕 August 14, 2026 - Morning Sweep (10 New, 8 Guides)

Scanned mcpservers.org /all pages 1-3 (newest submissions) and mcp.so Feed (30 newest submissions). 10 new business-relevant servers found - procurement and SaaS spend, ad intelligence and AI ad creation, cost segregation, knowledge bases, and Telegram operations.

### Vertice AI MCP ★★★ - August 14 morning

Official procurement-platform MCP from Vertice - query contracts, vendors, and SaaS spend in natural language, then trigger Vertice workflows with the same RBAC as the web app. OAuth 2.1 PKCE (S256), Streamable HTTP; Preview access through your Vertice Account Manager. The first major procurement platform with an official MCP connector. · [Guide →](/hermes/mcp/servers/external/vertice-ai-mcp)

### Waldo MCP ★★★ - August 14 morning

Live marketing intelligence for AI agents - ad libraries across Meta, Google, LinkedIn and TikTok, social listening, share of voice, audience insights and category landscapes, with every answer linked to its source. OAuth 2.1 auto or API key; per-workspace tool toggling; strategy plugin at /strategy. `mcp.waldo.fyi` (commercial) · [Guide →](/hermes/mcp/servers/external/waldo-mcp)

### Hermoso AI MCP ★★★ - August 14 morning

AI ad studio over MCP - 415 tools over one OAuth'd endpoint covering ad research (Meta/Google/LinkedIn libraries), creative generation with 50+ image and video models on a single credit meter, publishing, and campaign management. Open-source MCP server + CLI + Claude skills. `hermoso.ai` (commercial) · [Guide →](/hermes/mcp/servers/external/hermoso-ai-mcp)

### Viral Outliers MCP ★★ - August 14 morning

Continuously-crawled database of viral social outliers - search overperforming posts on TikTok, Instagram and YouTube, pull creator stats, generate transcripts, and crawl profiles on demand. Bearer API key, credit-metered (search 1 credit, transcript 10, crawl 40), REST + MCP parity, openapi.json + llms.txt published. `viraloutliers.com/api/mcp` (commercial) · [Guide →](/hermes/mcp/servers/external/viral-outliers-mcp)

### Shhots AI MCP ★★ - August 14 morning

AI UGC ads, cinematic product films, and studio product photography over MCP - avatars speak your script in 12 languages, multi-variant batches, photoshoots from one reference image. Account sign-in; Pro & Scale plans; live for Claude and ChatGPT. `mcp.shhots.ai/mcp/` (commercial) · [Guide →](/hermes/mcp/servers/external/shhots-ai-mcp)

### Cost Seg Smart MCP ★★ - August 14 morning

Cost segregation study pricing and Stripe checkout for US real estate - `get_cost_seg_quote` returns study cost, year-1 accelerated depreciation, tax savings and ROI; `get_cost_seg_payment_link` generates the checkout URL. No auth, Streamable HTTP, 21 property types. Example: $750K STR at 37% bracket → $995 study, $184.5K year-1 deduction, $68K savings, 69x ROI. `costsegsmart.com/mcp` (commercial) · [Guide →](/hermes/mcp/servers/external/cost-seg-smart-mcp)

### HelpDocs MCP ★★ - August 14 morning

Official knowledge-base connector - search and read articles, draft and update content, reorganize categories, and pull analytics on what readers search for. Per-account URL (Settings → AI → MCP Access), authorization flow, certain plans. `helpdocs.io` (commercial) · [Guide →](/hermes/mcp/servers/external/helpdocs-mcp)

### Graspil MCP ★★ - August 14 morning

Telegram analytics, broadcast, and automation over MCP - reports, funnels, referral stats, broadcasts and automations from chat, without the dashboard. API key; thin layer on the Graspil API with the same permissions. `graspil.com` (commercial) · [Guide →](/hermes/mcp/servers/external/graspil-mcp)

### Customer Intelligence & Segmentation MCP ★★ - August 14 morning (catalog entry)

Which next customer to call, and how much it will be worth - read-only customer tiering and value estimation. Endpoint `customer-tiering-mcp-latest.saifs.ai`. Thin docs (no tool list published); classified Marketing. (commercial)

### Citation Check MCP ★★ - August 14 morning (catalog entry)

Mechanical citation and claim checks for AI-generated documents - seven checks (enumeration, internal references, arithmetic, count-vs-list, declared bounds, ordinal sequences, self-consistency) with located verdicts per line. No model on the free path, documents never stored. `holoweave.org` (free tier)

**Also identified (not catalogued):** PolymarketScan (Polymarket prediction-market analytics - crypto), CoinLobster (whale-trade signals - crypto), FARPY (GPU Blender rendering - dev infra), AI Image Cleaner and EraseText (consumer photo/text-removal tools), GOJI (single-agency AEO/SEO knowledge base), Picorn (generic image/video project tool), Teai.io (MCP monetization gateway - a listing venue, not a server; worth revisiting as a directory target for CorpusIQ itself). Folklore variant evidence was already noted Aug 13.

**Key observation:** Ad creative moved fully onto MCP this cycle - Hermoso (415 tools, 50+ models, generation not just scheduling), Shhots (UGC/cinematic/photoshoot generation), and Waldo (ad-library research) now form a complete research → generate → publish → measure loop across separate vendors. Second, Vertice's official connector is the first procurement-platform MCP, extending the platform-MCP pattern (Atlassian, Apollo, Monday) into SaaS spend. Third, vertical tax tooling surfaced with Cost Seg Smart - quoting with ROI math before the study is sold, the same pay-per-outcome pattern seen in x402 and credit-metered servers.

---

## 🆕 August 14, 2026 - Midday Sweep (2 New, 2 Guides)

Scanned mcpservers.org /all pages 1-3 (newest submissions) and mcp.so Feed (30 newest submissions). 2 new business-relevant servers found - a social-media-management platform MCP and an official CDN-ops server. Plus one catalog fix (Holdings body entry).

### RADAAR MCP ★★★ - August 14 midday

Official social media management MCP from RADAAR - publish, schedule, unified inbox, listening, and analytics across 20+ channels (Instagram, X, LinkedIn, TikTok, YouTube, Threads, Pinterest, Bluesky, Mastodon, Google Business Profile, WordPress) from any MCP client. Six tool modules (publishing_*, inbox_*, monitoring_*, analytics_*, utilities_*, settings_*/subscriptions_*); OAuth, Streamable HTTP. `mcp.radaar.io` (commercial) · [Guide →](/hermes/mcp/servers/external/radaar-mcp)

### BlazingCDN MCP ★★ - August 14 midday

Official MCP server for BlazingCDN - 52 tools for Anycast CDN, cache operations, bandwidth metrics, custom domains, Cloud Storage and Video CDN, self-hosted via npx. API token auth; write tools gated by `BLAZINGCDN_ALLOW_WRITE=1`. MIT. `github.com/BlazingCDN/BlazingCDN-MCP` · [Guide →](/hermes/mcp/servers/external/blazingcdn-mcp)

**Catalog fix:** Holdings MCP (agentic invoicing/payments) - guide written Aug 10, body entry never landed. Added under Financial Data (no count change, unindexed-guides rule).

**Also identified (not catalogued):** MarkupBase (secure versioned workspace for agent-published artifacts - vendor MCP page is a JS-only shell with no tools, auth, or endpoint published; thin-docs rule). Feed repeats already catalogued this cycle: Vertice, Waldo, Hermoso, Shhots, Cost Seg Smart, HelpDocs, Graspil, OnePostly, Just Domain, Fakto wFirma, BusyMail, KPainter, EM+x, Prose Coach, ROIC.ai, cloro, BanProof, Stoxly, TED Tender Monitor, Citation Check, Customer Intelligence & Segmentation, Viral Outliers, easydocforms, NERAI. Previously skipped repeats: Syncro, LabTestSuperstore, SceneF, Faxer, Departi, Conqueror, CR8 Agent Commons, x402 tooling, directree, crosscode-cli, SportsTrackLive, scvd.store, FARPY, CoinLobster, PolymarketScan, AI Image Cleaner, EraseText, GOJI, Picorn, Teai.io, Snipara.

**Key observation:** The social-management platform category gained its second full MCP in five days - RADAAR joins OnePostly (Aug 13) with an official connector covering scheduling, inbox, listening, and analytics. The publish layer of social ops is now fully agent-addressable end to end. CDN operations (BlazingCDN) followed the official-vendor-MCP pattern on the infra side.

---

## 🆕 August 14, 2026 - Evening Sweep (3 New, 3 Guides)

Scanned mcpservers.org /all pages 1-3 (newest submissions) and mcp.so Feed (30 newest submissions). 3 new business-relevant servers found - a 13-platform public-data search MCP with ready-made lead-gen playbooks, a hosted quant-trading platform MCP, and a job-posting aggregator with community discussion threads.

### API Direct MCP ★★★ - August 14 evening

Public-data search across 13 platforms (LinkedIn, X, Facebook, Reddit, YouTube, Instagram, Threads, TikTok, Truth Social, forums, news, web search, Google Maps) with 68 tools plus 60+ ready-made skill playbooks (lead-gen, competitor conquest, recruiting, OSINT due diligence, brand monitoring). API key, Streamable HTTP, pay-as-you-go per request. `apidirect.io/mcp` (commercial) · [Guide →](/hermes/mcp/servers/external/api-direct-mcp)

### NexusTrade Financial MCP ★★★ - August 14 evening

Hosted quant-trading platform MCP - 125 tools covering stock screening, historical and fundamental data, multi-regime backtesting, portfolio and risk analysis, managed compute, creator strategy discovery, and paper/live copy trading with brokerage execution behind platform risk controls. OAuth 2.1 PKCE with dynamic client registration; Streamable HTTP. `nexustrade.io/api/mcp`, github.com/austin-starks/nexustrade-ts (commercial) · [Guide →](/hermes/mcp/servers/external/nexustrade-financial-mcp)

### JobYap MCP ★★ - August 14 evening

Job postings aggregated from companies' official career sites, each with a public discussion thread - salaries, locations, full descriptions, interview notes, and team signal. 8 read-only tools (search_jobs, get_job, get_job_comments, search_locations, list_companies, get_job_stats, search, fetch); no auth, Streamable HTTP. `mcp.jobyap.com/mcp` (commercial, free) · [Guide →](/hermes/mcp/servers/external/jobyap-mcp)

**Also identified (not catalogued):** Kin (firelock-ai/kin - provenance graph billed as "the system of record for AI-written software," stdio via `npx -y @kinlab/kin-mcp`, Apache-2.0; dev tool, not business-ops). Feed repeats already catalogued or previously skipped this cycle: RADAAR, BlazingCDN, Cost Seg Smart, easydocforms, Just Domain, Fakto wFirma, FARPY (dev infra), CoinLobster (crypto), EM+x, SceneF (consumer), LabTestSuperstore (lab supplies), Prose Coach, Clipkit (Aug 12 guide), CR8 Agent Commons, x402 Merchant Check, directree, Syncro, ROIC.ai, Conqueror, NERAI, BanProof, cloro, scvd.store, Faxer, Snipara. mcpservers.org /all pages 1-3 carried no other new business-relevant slugs - remaining slugs were repeats already catalogued or skipped in prior sweeps (MarkupBase, AppaTools, MyDart, Imag8, Sightseer, SonaPrompt, TrueSend, Teai.io, GOJI, Picorn, PolymarketScan, AI Image Cleaner, EraseText, Folklore Variant Evidence).

**Key observation:** The playbook layer is now a product. API Direct ships 60+ ready-made skills (competitor conquest, layoff-wave interception, due-diligence dossiers) that chain 68 raw tools into outcome-shaped calls, and NexusTrade formalizes the strategy marketplace with fork-and-copy-trade primitives (`fork_shared_portfolio`, `copy_trade_shared`). Both point the same direction: MCP servers are graduating from tool bundles to workflow products with opinionated entry points.

---

## 🆕 August 13, 2026 - Midday Sweep (8 New, 7 Guides)

Follow-up to the Aug 13 morning sweep. Scanned mcpservers.org /all pages 1-3 (newest submissions) and mcp.so Feed (33 newest submissions). 8 new business-relevant servers found - social publishing, voice AI, product-marketing automation, human-gated email, EU procurement, domain ops, Polish accounting, and source-grounded video content. [Full sweep report →](/hermes/mcp/sweeps/sweep-august13-2026-midday)

### OnePostly MCP ★★★ - August 13 midday

Nine-platform social publishing over MCP - publish, schedule, and read normalized insights across X, Instagram, Facebook, Threads, LinkedIn, TikTok, YouTube, Pinterest, and Reddit. Bearer API keys with read_only variants; wallet-debited X pass-through billing; 9 tools with per-platform validation. `mcp.onepostly.com` (commercial) · [Guide →](/hermes/mcp/servers/external/onepostly-mcp)

### Shipstar MCP ★★★ - August 13 midday

Product-marketing automation from commits - 21 tools generate changelogs, blog posts, feature pages, KB articles, release emails, X threads, and LinkedIn posts, then route every draft through review, approval, and publish. OAuth 2.1 with per-project scoping. `mcp.shipstar.ai/mcp` (commercial) · [Guide →](/hermes/mcp/servers/external/shipstar-mcp)

### DialNexa MCP ★★★ - August 13 midday

Voice AI agent platform over MCP - create and manage voice agents, place confirmed outbound calls, run campaigns and batch calls, search and buy numbers, and read dashboard metrics. Every tool classified read-only/state-changing/destructive/billable with approval required before calls or spend. OAuth 2.1 PKCE, workspace-scoped consent. `api.dialnexa.com/v1/mcp` (commercial) · [Guide →](/hermes/mcp/servers/external/dialnexa-mcp)

### Just Domain MCP ★★ - August 13 midday

Domain availability and pricing checks for AI assistants - first-year AND renewal prices plus a checkout link for justdomain.ai. Read-only by design: no purchase in chat. No auth, Streamable HTTP. `mcp.justdomain.ai` (commercial) · [Guide →](/hermes/mcp/servers/external/just-domain-mcp)

### Fakto.app wFirma MCP ★★ - August 13 midday

The only MCP for wFirma.pl (Polish accounting) - full read-write across ~45 tools: invoices, contractors, expenses, warehouse, KPiR and ZUS, cashflow forecasts, payment reminders. OAuth 2.0 (RFC 7591). Sister server for Fakturownia.pl. `fakto.app/wfirma/stream` (commercial) · [Guide →](/hermes/mcp/servers/external/fakto-wfirma-mcp)

### BusyMail MCP ★★ - August 13 midday

IMAP email over MCP with the strongest approval gate observed: a token can never send - it queues, and approval happens while signed in, so the writer and approver can never be the same session. Scoped read/organize/send tokens; accounts stay where they are. Invite-only. `busymail.app/mcp` (commercial) · [Guide →](/hermes/mcp/servers/external/busymail-mcp)

### TED Tender Monitor ★★ - August 13 midday

EU TED procurement monitoring via an Apify Actor - search notices by CPV, country, keyword, value, or type; persistent tasks deliver only new or changed tenders with dedup state. $0.005 per new tender. 13 example tasks + n8n and Make templates included. `github.com/Telemark-Digital/apify-monitoring-workflows` (unofficial community tool) · [Guide →](/hermes/mcp/servers/external/ted-tender-monitor)

### KPainter MCP ★★ - August 13 midday (catalog entry)

Source-grounded videos, slides, and interactive knowledge content from your own materials - read-aloud explainer videos from documents. stdio MCP (`kp-mcp` CLI) with API key; `kp_*` tools (kp_me, kp_get_catalog, kp_create_creation, kp_get_job_status, kp_get_creation, kp_edit_creation with scene-level edits). `kpainter.ai` (commercial)

**Also identified (not catalogued):** ViewMade (YouTube research/SEO/video production - listing page is only a support page, no MCP endpoint or tool docs), TrueSend (email marketing ESP - listing page is homepage marketing copy, no MCP surface documented), Folklore Variant Evidence (helena.bio genomics variant classification - healthcare niche), AgentBrink (agent identity infra - already noted Aug 12 evening), plus the usual dev-tool/consumer entries (PyPI MCP, x402 tooling, GetLulu micro-utilities - previously noted). One junk slug on /all page 2 (exposed-port OpenClaw host dump) excluded.

**Key observation:** The human-approval-gate pattern the Aug 12 sweeps flagged in content tools (Prose Coach, BanProof) is now the default architecture across new production MCPs in every domain - BusyMail (token can never send), Shipstar (approve before publish), OnePostly (read_only keys), DialNexa (safety-level classification with approvals before billable or destructive calls). Approval gates moved from content into email, marketing, social, and voice. Second, voice AI gained its first full-platform MCP (DialNexa). Third, EU public procurement surfaced as a vertical (TED Tender Monitor) - the first procurement entry in the catalog.

---

## 🆕 August 13, 2026 - Evening Sweep (5 New, 4 Guides)

Follow-up to the Aug 13 midday sweep. Scanned mcpservers.org /all pages 1-3 (newest slugs) and mcp.so Feed (30 newest submissions, 2 hours to 6 days old). 5 new business-relevant servers found - ad creative intelligence, PHI-safe healthcare forms, agent sequence enforcement, a prompt-injection gate, and biotech process economics. [Full sweep report →](/hermes/mcp/sweeps/sweep-august13-2026-evening)

### Alison AI MCP ★★★ - August 13 evening

Creative intelligence from your ad accounts inside any MCP client - spend and KPIs, creative tags, competitor intelligence (SensorTower/Pathmatics), and creative previews. 14 read-only tools; OAuth 2.1 PKCE with server-side grant scoping - the grant decides what the client can see, and revocation is immediate. `evo.alison.ai/mcp` (commercial) · [Guide →](/hermes/mcp/servers/external/alison-ai-mcp)

### easydocforms MCP ★★ - August 13 evening

Healthcare intake forms over MCP with a PHI-minimization design - the agent imports a blank PDF, hands the patient a hosted fill link, and retrieves the completed PDF; PHI never enters agent context. Docker-hosted (ghcr.io/easydocforms/easydocforms-mcp), API key auth, MIT. `github.com/easydocforms/easydocforms-mcp` · [Guide →](/hermes/mcp/servers/external/easydocforms-mcp)

### AgenticRail Gate MCP ★★ - August 13 evening

Deterministic step-order enforcement for AI agents - evaluate_step returns ALLOW/DENY before a step runs and every ALLOW writes an Ed25519-signed, hash-chained receipt stored as a tamper-evident compliance record; verify_receipt proves chain integrity. Public demo key, no auth required. `mcp.agenticrail.nz` · [Guide →](/hermes/mcp/servers/external/agenticrail-gate-mcp)

### glc PromptGuard ★★ - August 13 evening

Eight-layer source-aware prompt-injection gate - checks user prompts, RAG chunks, and tool outputs before they reach the model or tool loop. Intent × source × impact scoring with typed verdicts; agent self-registration tokens. `mcp.glc-rag.hu/mcp` · [Guide →](/hermes/mcp/servers/external/glc-promptguard-mcp)

### Untangle Bio MCP ★ - August 13 evening (catalog entry)

Self-serve biotech process design - generate downstream purification routes, simulate separations, and run techno-economic analysis (CAPEX/OPEX/payback) from Claude via MCP or the web app. Vertical niche; notable as the TEA-over-MCP pattern. `untangle.bio` (commercial)

**Also identified (not catalogued):** Imag8 Studio (style-locked image generation - listing is a one-liner with no MCP tool docs), AppaTools MCP Studio (no-code MCP server builder - dev tool), plus repeats already skipped in prior sweeps (Syncro, LabTestSuperstore, SceneF, FLINT Network, Constants, Faxer, Departi, LocalCan, x402 tooling, GetLulu micro-utilities, exposed-port junk slugs on /all pages 2-3). **Catalog fix:** NERAI Risk Intelligence has had a guide and docs link since Aug 11 but no catalog body entry - added under Compliance & Regulatory.

**Key observation:** The five servers split into three patterns. (1) Platform MCPs now expose read-only analytics warehouses with server-side grant scoping - Alison Evo's "the grant decides, not the client" is the enforcement philosophy CorpusIQ ships natively. (2) Data-minimization is becoming a product feature - easydocforms' PHI-never-enters-context design extends the approval-gate pattern from actions to data itself. (3) The verify-before-act layer keeps thickening - AgenticRail's signed receipt chains and glc PromptGuard's source-aware injection gate join VerityLayer and FLINT as agent-governance rails, making this the fastest-growing new segment in the ecosystem.

---

## 🆕 August 12, 2026 - Evening Sweep (4 New, 3 Guides)

Follow-up to the afternoon sweep (~3 hours later). Scanned mcpservers.org /all page 1 (30 newest) and mcp.so Feed (33 newest submissions). 4 new business-relevant servers found - consulting-grade deliverable generation, field-service ERP with a write-capable MCP surface, AI-search-visibility tooling, and self-hosted task management. [Full sweep report →](/hermes/mcp/sweeps/sweep-august12-2026-evening)

### EM+x MCP ★★★ - August 12 evening
Board-ready deliverables from chat - steering-committee readouts, executive briefs, market scans, and QBR decks built by an agentic consulting team on your own templates. Storyline approved before drafting; deterministic quality gates + adversarial partner review before delivery; native .pptx/.docx on your slide masters, palette, and fonts. 33 tools, Streamable HTTP, OAuth. Free: 1 project + 5 revisions/mo; paid from $8/mo. `emplusx.com/api/mcp` (commercial) · [Guide →](/hermes/mcp/servers/external/em-x-mcp)

### ATLASS OS MCP ★★★ - August 12 evening
Field-service business platform (CRM, scheduling, jobs, double-entry books, banking, GST, payables, payroll, inventory) with a native hosted MCP surface - 58 tools, 35 write-capable, 32 permission scopes. Tokens minted in-app; every financial write posts balanced double-entry to an append-only audit log; no payment rail by design. First field-service platform with a working MCP surface. `app.atlass-os.com/mcp` (commercial, founding-stage) · [Guide →](/hermes/mcp/servers/external/atlass-os-mcp)

### CiteRank MCP ★★★ - August 12 evening
AI search visibility platform - audits why AI answer engines won't cite a brand, then hands the fix. 5 tools: URL AI-visibility audits (schema, E-E-A-T, agentic readiness), brand citation checks across Google AI Overviews/Gemini, JSON-LD schema generation, agentic-readiness tests, and agent-journey simulation. Purpose-built for GEO/AEO programs. `citerankscore.com/api/mcp-server` (commercial) · [Guide →](/hermes/mcp/servers/external/citerank-mcp)

### QTask MCP ★★ - August 12 evening (catalog entry)
Open-source task/project management with a built-in MCP server - list/create/update tasks and projects, staged write approval (AI proposes, human approves), semantic search. Self-hosted with Docker + Ollama; hosted qtask.dev available. OAuth/JWT. `github.com/dbeasty/qtask` (open source)

**Also identified (not catalogued):** SceneF (SF movie showtimes - consumer), LabTestSuperstore (lab supplies - noted afternoon), AgentBrink (agent identity infra), swag2mcp (OpenAPI→MCP bridge - dev tool), US Stocks & Market Data (gino.im - overlaps catalogued ROIC.ai), PyPI MCP, King Crimson MCP, plus ~10 dev-tool/utility entries. The ~30-entry single-author rudrendupaul burst on mcpservers.org /all page 1 was excluded per the catalog-spam doctrine. Clipkit (Feed, 12h) was already covered by the Aug 12 morning sweep's guide.

**Key observation:** The ecosystem is splitting into two layers - (1) executive-output tools (EM+x) that turn raw agent conversation into board-ready artifacts behind human approval gates, and (2) vertical ERP surfaces (ATLASS OS) where the write path and the audit trail are the product. Both extend the human-gate pattern the afternoon sweep spotted (Prose Coach, BanProof, Plainpaper) from content to deliverables and money.

---

## 🆕 August 12, 2026 - Afternoon Sweep (10 New, 6 Guides)

Follow-up to the Aug 12 morning sweep (~6 hours later). Scanned mcpservers.org /all pages 1-3 (90 newest servers) and mcp.so Feed (30 newest submissions). 10 new business-relevant servers found - content quality tooling, finance, sales intelligence, and AI-engine visibility. [Full sweep report →](/hermes/mcp/sweeps/sweep-august12-2026-afternoon)

### Prose Coach MCP ★★★ - August 12 afternoon
Deterministic AI-writing filter - 43 AI-writing patterns flagged with the triggering line quoted and the fix attached. Remote Streamable HTTP, no auth, one URL. Free tier: 3 drafts/day at 12K chars; PRO $5/mo. First MCP purpose-built to de-AI content before it ships. `prose.coach/mcp` (commercial) · [Guide →](/hermes/mcp/servers/external/prose-coach-mcp)

### ROIC.ai MCP Server ★★★ - August 12 afternoon
Financial data MCP - stock prices, income statements, earnings call transcripts, fundamentals, ratios, and valuation multiples for 60,000+ public companies. One server covers statements + earnings + fundamentals. Streamable HTTP with API key. `mcp.roic.ai/mcp` (commercial) · [Guide →](/hermes/mcp/servers/external/roic-ai-mcp-server)

### cloro MCP ★★★ - August 12 afternoon
Live access to AI answer engines as agent tools - runs prompts through ChatGPT, Gemini, Perplexity, Copilot, Grok, and Google AI Mode, returning each answer with cited sources; plus Google Search/News with country/state geo-targeting. Purpose-built for brand monitoring and GEO/AEO. API key. `mcp.cloro.dev` (commercial) · [Guide →](/hermes/mcp/servers/external/cloro-mcp)

### Stratyfix MCP ★★★ - August 12 afternoon
Sales intelligence connector - 10 read-only tools over live pipeline data (deal forecasts, pace-to-target, coaching queue, team coverage, gap ledger). OAuth per-user permissions. Honesty rule: withholds numbers it can't defend instead of guessing. `app.stratyfix.com/api/mcp` (commercial) · [Guide →](/hermes/mcp/servers/external/stratyfix-mcp)

### FlowyTeam OKR MCP ★★ - August 12 afternoon
Native OKR MCP - connect Claude, ChatGPT, or n8n to objectives, key results, and tasks; post check-ins and move KR progress from chat. MIT, OAuth. `github.com/flowy-team/okr-mcp-server` · [Guide →](/hermes/mcp/servers/external/flowyteam-okr-mcp)

### QuestDB MCP Server ★★ - August 12 afternoon
Official QuestDB MCP - connects coding agents to a running QuestDB Web Console with tools for notebook cells, queries, and charts. First official time-series database MCP. Apache-2.0. `npx @questdb/mcp-server-questdb setup` · [Guide →](/hermes/mcp/servers/external/questdb-mcp)

### Plainpaper MCP ★★ - August 12 afternoon (catalog entry)
AI marketing canvas for MCP agents - 54 tools drafting campaigns as cards on a shared board, briefed by brand rules, human-approved before execution. OAuth, 7-day trial, Starter $29/mo. `mcp.plainpaper.io/mcp` (commercial)

### Contio MeetingOS MCP ★★ - August 12 afternoon (catalog entry)
Meeting workspace MCP - agendas, transcripts, AI notes, and action items from planning to follow-through, without recording audio/video. OAuth. `mcp.contio.ai/mcp` (commercial)

### MachineTranslation.com MCP ★★ - August 12 afternoon (catalog entry)
Multilingual translation via multi-model consensus over MCP - connects AI agents to professional-grade translation. Useful for global content ops. `tomedes-org/machinetranslation.com-mcp` (commercial)

### BanProof AI ★★ - August 12 afternoon (catalog entry)
Audits TikTok Shop and Amazon affiliate video scripts for policy violations before creators record or publish. Exposes `audit_script` tool. `banproof.io` (commercial)

**Also identified (not catalogued):** Canvas API MCP (education niche - per Aug 11 decision), MoodleMCP (LMS), React SEO Skills (dev-tool adjacent), Faxer (fax ops utility), Constants (overlaps catalogued ad MCPs), LabTestSuperstore (lab supplies), GetLulu 6-pack (micro-utilities: crypto price, domain RDAP, FX, holidays, registry, weather), Conqueror, CR8 Agent Commons (agent message board), x402 Merchant Check (crypto), GoLeasy (German leasing), Departi (travel), Andrii Co Notary (WA notary), plus ~25 dev-tool/utility entries from mcpservers.org /all (bunkerweb, humanpen, lobu, mercury-cortex, strata, sonaprompt, ohm, sshmng, etc.). A ~30-entry single-author burst (rudrendupaul: haltproof, shimguard, toolgovern, tokentrust…) showed classic AI-generated catalog-spam signals and was excluded entirely. **Morning sweep note:** the Aug 12 morning sweep's 6 servers (Orcha, Clipkit, FiatDock, Apiosk, directree, LocalCan) have guides; entries added to the additions log Sep 10, 2026 (see `/hermes/mcp/sweeps/sweep-august12-2026.md`).

**Key observation:** Two patterns this sweep - (1) human-gate content tooling is arriving: Prose Coach (deterministic de-AI filter), BanProof (script compliance), and Plainpaper (human-approved campaigns) all put a human gate or deterministic check between the agent and the publish button; (2) the finance stack keeps deepening - ROIC.ai joins 5+ financial-data MCPs already catalogued, and AI-engine visibility (cloro) is emerging as its own measurement category for GEO/AEO programs.

---

## 🆕 August 11, 2026 - Midday Sweep (3 New, 3 Guides)

Follow-up to the overnight sweep (~6 hours later). Scanned mcp.so homepage + /servers?sort=latest (50 most recent) and mcpservers.org /all (30 newest). 3 new business-relevant servers found - with a notable trend: "no dashboard required" is becoming the explicit pitch for MCP-native marketing tools. [Full sweep report →](/hermes/mcp/sweeps/sweep-august11-2026-midday)

### AdMake AI MCP ★★★ - August 11 midday
Remote MCP (OAuth 2.1) for AI ad creative generation + Meta Ad Library competitor research + publishing to Meta/TikTok/Pinterest. First MCP that connects the full ad creative lifecycle (research → generate → publish) in a single agent-accessible flow. Plans from $39/mo, 5 free ads. `admakeai.com/api/mcp` (commercial) · [Guide →](/hermes/mcp/servers/external/admake-ai-mcp)

### JaxSuite AI MCP ★★★ - August 11 midday
AI-native cold outreach + CRM platform - 27 MCP tools covering campaign lifecycle, multi-step content writing with spintax, contact management, and deliverability analytics. 300M+ verified B2B contacts. Remote Streamable HTTP with API token auth. First end-to-end cold outreach MCP with built-in deliverability. `jaxsuite.com/api/v1/mcp` (commercial) · [Guide →](/hermes/mcp/servers/external/jaxsuite-ai-mcp)

### DripRaven MCP ★★ - August 11 midday
WhatsApp Business campaign automation for AI agents - import contacts, send approved templates, schedule broadcasts, read delivery rates via official WhatsApp API. First WhatsApp-specific marketing MCP. Starter $49/mo (5K msgs). `dripraven.com` (commercial) · [Guide →](/hermes/mcp/servers/external/dripraven-mcp)

**Also identified (not catalogued):** Syncro MCP (IT management, official), LocalCan MCP (ngrok alternative, 82⭐), LinkedIn API MCP (browser session approach), Bastion (attack surface monitoring), wecallio (outbound phone calls for agents), Klarefi (legal intake), and 6 others. 12 total identified, most were dev tools, security/legal niche, or crypto-adjacent.

---

## 🆕 August 11, 2026 - Evening Sweep (3 New, 3 Guides)

Follow-up to the midday sweep (~6 hours later). Scanned mcp.so homepage (Featured, Trending, New Arrivals) and mcpservers.org homepage + /all (30 newest). 3 new business-relevant servers found - completing a "marketing MCP stack" across ads, referrals, and video production. [Full sweep report →](/hermes/mcp/sweeps/sweep-august11-2026-evening)

### Cello MCP ★★★ - August 11 evening
Remote MCP for referral, partner, and affiliate program management. Ask AI agents about top referrer revenue, churn risk, attribution health, and program benchmarks in plain language. OAuth, Streamable HTTP at `https://mcp.cello.so/mcp`. First dedicated referral program intelligence MCP. Free with Cello account. · [Guide →](/hermes/mcp/servers/external/cello-mcp)

### AdWhispr MCP ★★★ - August 11 evening
Complete ad workflow MCP - research any brand's live Facebook/TikTok ads (ranked by days running), clone proven winners, and launch real campaigns on Google, TikTok, and Meta. First MCP that closes the full ad lifecycle (research → clone → launch). OAuth, free tier, Pro $39/mo. `https://adwhispr.com/api/mcp` (commercial, OAuth) · [Guide →](/hermes/mcp/servers/external/adwhispr-mcp)

### ViewMade MCP ★★ - August 11 evening
YouTube research, SEO, and finished video production for AI agents. Listed in mcpservers.org's Latest MCPs (Marketing category). Agent-native video production from research through publishing. Early-stage - public MCP documentation is thin. `viewmade.com` (commercial) · [Guide →](/hermes/mcp/servers/external/viewmade-mcp)

**Also identified (not catalogued):** Medplum (healthcare, 2.5K⭐), PLUR (agent memory, 226⭐, 98% R@5 benchmark), Termany (agent terminal, 174⭐), LocalCan (82⭐ - already noted midday), BetterBugs (dev tool), AI Video MCP by AITuber (content niche), directree (software directory), scvd.store (x402 infra), crosscode-cli (dev tool), SportsTrackLive (consumer), Sightseer MCP (travel), and 6 dev/ML tools from mcpservers.org. 

**Key observation:** With AdWhispr + AdMake AI + Cello + JaxSuite AI + DripRaven - all catalogued on the same day - the MCP ecosystem now covers the full marketing stack. An operator could theoretically run their entire growth function through MCP-connected agents.

---

## 🆕 August 11, 2026 - Overnight Sweep (3 New, 3 Guides)

Follow-up to the Aug 10 evening sweep. Scanned mcp.so homepage SSR (7 recent servers), mcp.so/feed (30 servers), and 15 mcp.so GitHub issues. 3 new business-relevant servers found - forming a complete "operator visibility stack" (social listening + LinkedIn content + SEO audit). [Full sweep report →](/hermes/mcp/sweeps/sweep-august11-2026-overnight)

### SiteGuru MCP ★★★ - August 11 overnight
Remote MCP connecting SiteGuru's full SEO dataset - crawl audits, Google Search Console rankings, Google Analytics traffic, backlink profiles, and indexation status - to AI agents. Operational SEO: ask "What should I fix first?" and get prioritized, actionable answers. One-click OAuth setup. `mcp.siteguru.co` (commercial, no public repo) · [Guide →](/hermes/mcp/servers/external/siteguru-mcp)

### LinkedMash MCP ★★★ - August 11 overnight
Hosted MCP for LinkedIn saved posts - search, organize, draft, schedule, publish, and analyze. Turns passive saved-post libraries into AI-powered content engines. Chrome extension import, then any MCP client connects. Full content lifecycle from inspiration to publishing. `mcp.linkedmash.com` (commercial, no public repo) · [Guide →](/hermes/mcp/servers/external/linkedmash-mcp)

### Xpoz MCP ★★★ - August 11 overnight
Social media intelligence MCP - 3B+ posts across Twitter/X, Instagram, Reddit, TikTok. Brand monitoring, social listening, lead gen, competitive intel. No platform API keys required. Remote MCP with OAuth 2.1. 2-min setup. `github.com/xpozpublic/xpoz-mcp` (MIT, 10⭐) · [Guide →](/hermes/mcp/servers/external/xpoz-mcp)

**Also identified (not catalogued):** DocuQueue MCP (PDF gen/form filling, 1⭐, early-stage), Data Studio Agent (unified DB MCP, unverified), SV Number (SMS verification numbers, niche). 12+ other GitHub submissions were dev tools (mcp-x, MeshMarket, gandr-mcp, crosscode-cli), consumer apps (oura-mcp, SportsTrackLive), infrastructure (scvd.store, FLINT Network, FiatDock), or niche (UAPDrop, Poliety, InstaSeer, HokAI, Redbark). 17+ feed entries were dev tools, consumer apps, or regional niche.

---

## 🆕 August 10, 2026 - Evening Sweep (4 New, 4 Guides)

Follow-up to the morning sweep. Deep scan of mcp.so pages 1-3 and mcpservers.org /all. 4 additional business-relevant servers found - including one that appeared 4 hours after the morning sweep. [Full sweep report →](/hermes/mcp/sweeps/sweep-august10-2026-evening)

### Perfex CRM MCP ★★★ - August 10 evening
Self-hosted MCP server for Perfex CRM - leads, customers, invoices, tickets, projects, contracts, subscriptions exposed as typed MCP tools. Staff-scoped API keys, read-only mode, granular tool control, full request logging. First self-hosted CRM MCP server. Data stays on your server - no third-party relay. `themesic/perfex-rest-api-examples` (MIT) · [Guide →](/hermes/mcp/servers/external/perfex-crm-mcp)

### FCA Handbook MCP (Metis Harness) ★★★ - August 10 evening
UK Financial Conduct Authority Handbook MCP - 10,000+ regulatory entries with verbatim citations and binding-level classifications (R=Rule, G=Guidance). Stateless, one-shot design aligned with OWASP Top 10 for Agentic Applications. First regulatory compliance MCP server. `github.com/99blakeD99/the-metis-fca-handbook-ai-harness-mcp-files` (MIT) · [Guide →](/hermes/mcp/servers/external/fca-handbook-mcp)

### Stoxly ★★ - August 10 evening
Free stock & ETF fundamental analysis - 10-point score, verdict, and metrics for any ticker. No API key, no account required. Lightweight complement to heavier financial MCPs. Brand new (added to mcp.so ~4 hours before this sweep). Author: wizard-exe. · [Guide →](/hermes/mcp/servers/external/stoxly-mcp)

### Fund Momentum MCP ★★ - August 10 evening
VC intelligence for AI assistants - 920+ active VC funds, live investor signals, AI-powered startup matching. First dedicated VC/fundraising intelligence MCP. Remote MCP with API key. `schneidavie/fundmomentum` · [Guide →](/hermes/mcp/servers/external/fund-momentum-mcp)

**Also identified (not catalogued):** Trimtab AIS (ship/port data, free, logistics niche), Goalie Trademark Search (14M+ USPTO trademarks, IP legal niche), Pickle (ClickUp/Slack/Teams ops manager), Anomalia (marketing content planning), Exchangerate.dev (keyless FX rates). 20+ other servers were developer tools, consumer apps, or regional niche.

---

Sweep of mcp.so GitHub issues (15 most recent), mcp.so /servers SSR, and mcpservers.org sitemaps. 3 business-relevant finds submitted since yesterday afternoon's sweep. [Full sweep report →](/hermes/mcp/sweeps/sweep-july31-2026-early)

### The Bot Wire ★★★ - July 31
40 real-time primary-source data wires - SEC EDGAR, Federal Register, federal court opinions, congressional bills, SEC/FTC enforcement, FDA approvals, Federal Reserve/FOMC, BLS/BEA, CISA CVEs. Reads original documents directly, not news coverage. AI agents answer post-cutoff questions with primary-source citations. First MCP for regulatory/legal/economic primary-source intelligence. `github.com/ArasPasha/botwire-mcp` (0⭐) · [Guide →](/hermes/mcp/servers/external/botwire-mcp)

### Pangolinfo Amazon Data MCP ★★ - July 31
19 e-commerce and IP-compliance tools - Amazon product/review/search/niche/bestseller data, AI SERP/keyword trends, WIPO trademark search, PACER patent litigation. Consolidates marketplace intelligence + IP legal tools in one MCP. `github.com/Pangolin-spg/pangolinfo-mcp` (0⭐) · [Guide →](/hermes/mcp/servers/external/pangolinfo-mcp)

### Primate Intelligence ★★ - July 31
Video scene understanding for AI agents via predictive world models. Register videos by URL, ask natural-language questions, get deterministic yes/no/indeterminate answers with confidence scores and clip timestamps. No hallucinated descriptions. First MCP for AI video understanding. `github.com/Primate-Intelligence/primate-intelligence-mcp` (0⭐) · [Guide →](/hermes/mcp/servers/external/primate-intelligence-mcp)

**Also identified (not catalogued):** ClawJob (agent task marketplace - dev tool), GoodMemory (local-first memory - dev tool), bomly (dependency graphs - dev tool), plori (cloud computers for agents - dev tool), NameWhisper (ENS intelligence - crypto niche). Plus ~25+ mcpservers.org sitemap re-indexes for July 31 - all well-known existing servers (Storybook, Microsoft, Qdrant, ClickUp, Metabase, Sentry, Stripe, StackOverflow, etc.).

---

