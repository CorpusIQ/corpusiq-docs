---
title: External MCP Server Catalog
description: Curated catalog of notable third-party MCP servers for business operators — finance, analytics, document intelligence, security, and productivity
---

# External MCP Server Catalog

Beyond CorpusIQ's 37+ built-in connectors, the MCP ecosystem now has 22,000+ servers spanning every domain. This catalog tracks the most relevant third-party MCP servers for business operators — curated from [mcp.so](https://mcp.so) and [mcpservers.org](https://mcpservers.org).

> **Last updated:** June 14, 2026 (afternoon sweep) · **Sources:** mcp.so (22,282 servers), mcpservers.org (9,000+)

---

## Data Firewall Suite (PortEden)

The **PortEden Secure*** family puts a data firewall between AI agents and your Google/Microsoft accounts. Every action is permission-gated, content-redacted, and audit-logged. One-click revoke. Complementary to CorpusIQ's read-only OAuth model.

### Secure Calendar (Google Calendar & Outlook)
Search schedule, check availability, create/reschedule/cancel events, RSVP. AI held to permissions you grant. Every change logged.

### Secure Email (Gmail & Outlook)
Search, read, send, reply, forward, label, delete email. Sensitive content redacted before AI sees it. Full audit trail.

### Secure Google Drive
Search, read, create, copy, rename, move, share, delete files and folders. Sensitive data redacted. Permission-gated.

### Secure Google Docs
Search, read, create, copy, rename, precisely edit documents (insert, append, replace). Every edit logged.

### Secure Google Sheets
Create/copy spreadsheets, read tabs/ranges, write/append values, manage tabs. Protects sensitive values, audits every write.

### Secure Google Sheets MCP Server ★ New
Dedicated MCP server for PortEden's Google Sheets data firewall. Read, write, and manage spreadsheet data with permission gating and audit logging. Separate from the Drive-level Secure Google Drive server.

---

## Financial Data

### Alpha Vantage MCP Server ★ Sponsor
Realtime & historical stock, ETF, options, forex, crypto, commodities, fundamentals, technical indicators. Official MCP server from Alpha Vantage.

### Tokenbel Financial Data
Read-only access to Belarusian securities: tokens, shares, bonds, companies, ticker search. Niche but notable for Eastern European markets.

### Infrawise ★ New
Azure FinOps infrastructure cost optimization. Helps operators manage cloud spend with AI-assisted cost analysis. `npx -y @infrawise/mcp-server`

### agents.hellobooks.ai ★ New
AI agents that automate bookkeeping and financial close for SMBs. Streamable HTTP transport. Hands-free bookkeeping via MCP — ideal for small business operators who want AI to handle financial close.

### infaton-1c-mcp ★ New
MCP server for 1C:Enterprise (ERP, Accounting) — 51 tools for metadata, documents, registers, reports. Essential for Eastern European and Russian-market operators running on 1C.

### IRONCLAW BTC Node ★ New
Bitcoin blockchain data server for AI agents — 17 tools (fees, mempool, transactions, address portfolio, trace, whales, SEC insider trades, web scraping, AI summarization, capital flows, Reddit). x402 USDC micropayments on Base. No API keys needed.

### Shikamaru ★ New
Provably correct day-count and accrued-interest calculations. Small, dependency-light TypeScript library and MCP server for precise financial math. AI agents can get the exact number instead of guessing — essential for bond markets, fixed income, and financial operations. `npx -y @shikamaru/mcp-server`

### Dealflowpro ★ New
Multifamily real estate deal analysis via MCP. Analyze deals, score properties, calculate max offer prices, and look up market data from AI assistants. Essential for real estate investors and operators underwriting multifamily acquisitions. `npx -y dealflowpro-mcp` (requires `DFP_API_KEY`)

### Kaginet Bitcoin Escrow ★ New
Trustless Bitcoin escrow for AI agent-to-agent payments — 29 MCP tools. Create conditional escrow instruments (hash-match, human approval, optimistic with dispute bonds), fund with Bitcoin, settle automatically. All keys generated and deleted inside Intel TDX hardware enclaves with cryptographic attestation. No custodian, no stablecoin dependency. Streamable HTTP at `https://mcp.kaginet.com/sse` (requires API key from cloud.kaginet.com)

### Conta Azul MCP ★ New
Brazilian ERP for AI agents via MCP — 35 tools (read + write) covering sales, customers, products, payables/receivables, and NF-e invoices. OAuth 2.0 authentication. First Brazilian ERP MCP server — essential for SMBs operating in Brazil's NF-e invoice ecosystem. Streamable HTTP transport.

### Plinth FX MCP ★ New
Production-grade exchange rates from ECB data via Frankfurter. Latest rates, currency conversion, historical, and time-series endpoints. SRE-grade rate limiting, backoff, and structured logging. Free, no API key required. Essential for any business operator dealing with multi-currency operations.

### finra-mcp-server ★ New
FINRA Query API exposed as MCP tools. Access regulatory filings, broker/dealer data, and financial services compliance information directly from AI assistants. Essential for financial services operators who need FINRA data in their workflow.

### Longbridge ★ New
13 consolidated agent skills for Longbridge Securities — market data, fundamentals, portfolio analytics, and quantitative tools for HK, US, A-share (China), and Singapore markets. Multi-market coverage for operators running cross-border investment strategies.

### TradeInsight ★ New
US stock market data server — OHLCV price history, top movers ranked by volume/moving-average/price-change, and company ticker search. Free tier available. Quick market intelligence without Bloomberg terminal costs.

### IBKR Portfolio Builder ★ New
Top-down portfolio research for Interactive Brokers — 468 typed screeners tagged by strategy intent (value, growth, momentum, etc.). Read-only MCP server. Essential for financial operators running IBKR who want AI-assisted portfolio construction. `npx -y @ibkr/portfolio-builder-mcp`

### IBKR MCP ★ New
Unofficial local MCP server for Interactive Brokers market data, account positions, and trading workflows. Use paper trading and review permissions before connecting live accounts. Full Trading Workstation access from any MCP client.

### MCP for Indexa Capital ★ New
Access Indexa Capital robo-advisor portfolios (European markets) through Indexa's official API from any MCP client. View portfolio composition, performance, and allocation data. Essential for European financial operators using Indexa.

### AlphaAI News ★ New
Real-time, AI-enriched financial news for AI agents and trading bots. Full-text and ticker search, trending and "actionable-now" feeds, SEC Form 4 insider transactions, and two-ticker read-across. Essential for financial operators who need AI-curated market intelligence without noise.

### Rockmoon Financial Data ★ New
Cross-market (US/JP/KR) financial data over MCP — financials, segments, ownership, valuation metrics and prices. Every value traceable to its source filing. 18 tools; one API key works for both REST and MCP transport. For operators running multi-market analysis.

### TradeOS AI ★ New
Use TradeOS MCP Server to bring trading data, indicators, strategy logic, and agent workflows into MCP-compatible AI tools. Copy server URL, add to GPT or Claude, and work directly with trading intelligence. For operators who want AI-assisted trading workflows.

### Hive Intelligence MCP ★ New
Managed crypto intelligence MCP for AI agents across market data, DeFi, wallets, security, DEX, NFTs, Solana, infrastructure, and prediction markets. Broad coverage for crypto-aware operators.

### PineForge Codegen ★ Official ★ New
Local MCP server: AI writes PineScript v6, bundled engine transpiles to C++ and backtests against Binance data — no API key, fully local. Essential for TradingView operators who want AI-written, locally-backtested strategies.

---

## Ecommerce & Marketplace Intelligence

### Webotee AI Connect — Amazon Seller Intelligence ★ New
Brand, seller, ASIN info, and under-competed niches from your AI assistant. Essential for Amazon operators and ecommerce businesses who need marketplace intelligence without manual research.

---

## Document Intelligence

### Sifter
Extracts structured, typed records from documents (PDFs, scans, contracts, invoices) using natural-language field specs. Agents can query and aggregate — exact counts, sums, filters, with source-page citations. Unlike RAG, answers collection-wide questions.

---

## Business Identity & AI Discoverability

### Truee Ai ★ New
AI-ready business profiles — a trusted business data layer for the AI-first internet. Businesses create structured profiles so AI systems, search engines, and agents can discover them accurately. Instead of AI guessing from outdated public data, Truee lets businesses control their own structured identity: services, location, contact details, announcements, and offers. For operators: ensure your business is discoverable and correctly represented when AI agents search for businesses to recommend.

---

## Compliance & Regulatory

### Disclos — EU AI Act ★ New
Remote MCP server for EU AI Act compliance (Regulation 2024/1689). Add one URL to Claude, Cursor, or Windsurf — no install — and your AI classifies any AI system against the regulation, returns the three-wave timeline, explains risk tiers (minimal/limited/high/unacceptable), and crosswalks to ISO standards. Essential for any business operator deploying AI in the EU market. Streamable HTTP, no API key.

### audit-ledger-mcp ★ New
Tamper-evident audit logging for AI decisions. Three tools (record_decision, verify_decision, list_decisions) write to a regulator-grade ledger built on AWS S3 Object Lock with 7-year retention. Designed for EU AI Act Article 12 and FCA SS1/23 evidence requirements. Try zero-config: `npx audit-ledger-mcp` boots in sandbox mode against a public hosted tenant. Essential for operators who need regulator-grade audit trails for AI-assisted decisions.

---

## GTM & Sales Intelligence

### IndustryLens ★ New
Browse cited competitive-intelligence reports and head-to-head competitor comparisons from any MCP-aware AI agent. Live B2B SaaS data with sources included. For operators who need real competitive intelligence — not guesses — when evaluating market moves.

### Mamba Labs GTM Suite ★ New
Six go-to-market signal tools in a single MCP server, from hiring detection to ICP scoring, all returning flat Clay-ready data. Includes ICP Fit Scorer and GTM Signals Aggregator. Essential for GTM operators who want enriched account data ready for outreach workflows.

### ICP Fit Scorer ★ New
Qualifies accounts against your ideal customer profile and returns a score, tier, and per-signal reasoning. Part of the Mamba Labs signal toolkit. For sales operators who want AI to qualify accounts against ICP in real time.

### GTM Signals Aggregator ★ New
Rolls hiring and tech-stack signals into a single go-to-market fit score for fast account prioritization. Part of the Mamba Labs signal toolkit. For operators who need quick account scoring to prioritize outreach.

### OpenWeb Ninja MCP ★ Official ★ New
Official MCP server connecting any AI agent to 40+ web data APIs for web search, e-commerce, local business, jobs, real estate, and finance data. Broadest coverage API aggregation MCP for operators who need diverse web data through a single endpoint.

---

## Business Operations

### Trainzilla Coach MCP ★ New
AI assistant for fitness coaches on Trainzilla. Manage clients, create workout and diet plans, schedule sessions, track habit compliance, review check-ins, and query billing — all via one-click OAuth 2.0. No token paste required. First dedicated fitness business operations MCP server.

### Pollbolt ★ New
AI-native survey & form builder. Let AI agents create and manage surveys directly — build surveys, manage responses, pull analytics, and configure webhooks. Secured with OAuth 2.1. Hosted Streamable HTTP at `https://api.pollbolt.com/mcp`. Essential for operators who want AI-assisted customer feedback, NPS tracking, and survey campaigns. `npx -y mcp-remote https://api.pollbolt.com/mcp`

---

## Analytics & Business Intelligence

### Clamp Analytics MCP
Analyze and manage traffic, funnels, cohorts, revenue, errors. Web/app analytics via MCP. Complementary to GA4 for product analytics use cases.

### Playwright MCP ★ Official (Microsoft)
Official Microsoft MCP server for browser automation, page inspection, screenshots, and web interaction. 78 tools for AI agents. `npx @playwright/mcp@latest`

### Browserbase ★ Official
Automate browser interactions in the cloud — web navigation, data extraction, form filling. Cloud-hosted, no local browser needed. `npx @browserbasehq/stagehand-mcp`

### Doorprofit ★ New
US location intelligence: crime safety scores, recent incidents, neighborhood demographics, rent data, and registered-offender search by address. Free tier available. Useful for site selection, real estate due diligence, and location-based business decisions.

### cityparity ★ New
Cost-of-living and quality-of-life comparison across 165 cities, 69 countries. Point it at two cities for take-home pay analysis, full cost breakdown (housing, healthcare, childcare, food, transit, travel, property tax), equivalent salary needed, and non-cash deltas (vacation days, parental leave, universal healthcare). City quality rankings and inbound-worker tax regimes (Italy, Portugal, and others). Free, no API key, hosted Streamable HTTP. Essential for HR operators, relocation planning, and global workforce strategy.

### HTAG Property Intelligence MCP ★ Official ★ New
Australian property intelligence, H3 spatial intelligence, and capability discovery — 70+ read-only tools over Streamable HTTP. Public connectors for real estate operators, investors, and property analysts. Official HTAG integration.

### Remote Jobs MCP ★ New (Jobicy)
Autonomous remote job search — AI tools can search, filter, and retrieve the latest remote job listings in real-time via public Jobicy MCP server. Useful for recruitment agents and talent operations.

---

## Content & Research

### Scribefy
Extract timestamped YouTube transcripts, video search, metadata, and related-video tools. Works with Claude, Cursor, Windsurf, and any MCP client.

### Hacker News MCP ★ by NeCL
Access Hacker News data for AI agents: top stories, story details, comments thread, full-text search via Algolia. No API key required — public HN API. Built for content research, trend monitoring, and prompt enrichment. By Neural Engineering & Cognitive Logic (neclco.com).

### NotebookLM MCP ★ New
Let CLI agents (Claude, Cursor, Codex) chat directly with NotebookLM for zero-hallucination answers based on your own notebooks. Ground-truth research from Google's NotebookLM. `npx -y @pleaseprompto/notebooklm-mcp`

### OpenSERP ★ New
Multi-engine SERP extraction: Google, Yandex, Baidu, Bing, DuckDuckGo, Ecosia. Search results and URL data extraction. npm: `@openserp/mcp`

### Firecrawl MCP ★ Official ★ New
Official Firecrawl MCP Server — powerful web scraping and search for LLM clients. 3,300+ GitHub stars. `npx -y firecrawl-mcp`

### Exa MCP ★ Official
AI-native search engine by Exa. Search the web with semantic understanding. Official MCP server. `npx -y @exalabs/exa-mcp-server`

### Zhipu Web Search ★ New
LLM-optimized search integrating four search engines with intent recognition. Returns structured results (title, URL, summary, site name, icon) designed for AI consumption. By BigModel.

### Perplexity Ask MCP Server ★ New
AI-powered research and Q&A through Perplexity's search engine. Get cited, up-to-date answers for market research, competitive analysis, and business intelligence. Ideal for operators who need fact-checked research without leaving their MCP client. `npx -y @perplexity-ask/mcp-server`

### AgentQL MCP Server ★ New
Structured web data extraction with AgentQL's query language. Transform any website into clean, typed data for business intelligence, lead enrichment, and competitive monitoring. Semantic, not brittle CSS selectors.

### Jina AI MCP Tools ★ New
AI-powered search, embeddings, and content processing via Jina AI. Reader API for web content extraction, embeddings for semantic search, and deep search capabilities. `npx -y @jina-ai/mcp-tools`

### Search1API ★ New
Unified search API aggregating results from Google, Bing, and other search engines. Single interface for multi-engine web search with structured results optimized for AI consumption. `npx -y search1api-mcp`

### Reddit MCP Server ★ New
Access Reddit data for social listening, market research, and community monitoring. Search subreddits, fetch posts and comments, track trending topics. Requires Reddit API credentials. `pip install reddit-mcp`

### Baidu Map MCP ★ New
Baidu Maps API via MCP — China's largest mapping platform. Location search, geocoding, directions, POI data, and route planning. First major map service fully MCP-compatible. Essential for China-market operators.

### Geekflare ★ New
Web scraping, search, screenshots, and network tools for Claude, Cursor, ChatGPT, and other MCP clients. All-in-one web intelligence toolkit for operators who need to extract and monitor web data at scale. `npx -y @geekflare/mcp`

### Fonteum MCP ★ New
Source-provenanced US federal healthcare provider data over MCP. Resolve any NPI or CCN across NPPES, OIG LEIE, SAM.gov, state Medicaid exclusions, CMS PECOS, Care Compare, and Open Payments — every field carries a 14-field provenance contract, and an "excluded or compromised anywhere" check runs on every lookup. Essential for healthcare operators and compliance teams needing verifiable provider data.

### Auditspark ★ New
AI-powered website audit for any URL across 10+ categories — SEO, performance, accessibility, UX, and content quality. Scored report in under 2 minutes. Free tier included. Ideal for operators auditing their web presence.

### OpenSEO ★ New
SEO research tools for AI agents: keyword research and metrics, SERP and local SERP results, domain and backlink analysis, rank tracking, and Google Search Console performance. `npx openseo-mcp`

### Amap Maps (高德地图) ★ New
AutoNavi Maps MCP — China's second-largest mapping platform. Location search, geocoding, directions, and POI data. Essential for China-market operators alongside Baidu Maps. Official 高德 integration.

---

## SEO & AI Visibility

### GSC Wizard MCP ★ New
Your AI assistant can query Google Search Console analytics directly. Performance data, query analysis, page-level metrics — all through natural language. For operators who want AI-assisted Search Console analysis without dashboard toggling.

### Ranki.io SEO/AEO Consultant ★ Official ★ New
Free SEO and AEO MCP server that turns Claude/Cursor/ChatGPT into a senior SEO + AEO consultant. Audits any URL, generates sitemap.xml / llms.txt / robots.txt, finds keyword gaps, and tells your AI exactly what to fix — using your own AI credits. Essential for operators shipping content that needs to rank in both traditional search AND AI engines.

### Local AI Visibility ★ New
Free, no-signup MCP that checks whether AI assistants name a local business when prospects ask "who's the best in town?" Returns a Share-of-Model score, the competitors named instead, a GEO/AEO checklist, and a buying-intent prompt generator. Essential for local business operators tracking AI-discoverability.

### auto-geo ★ Official ★ New
GEO-optimized content publishing engine for AI visibility. Ensures your content is structured for discovery by AI search engines and assistants. For operators who want their content surfaced when AI agents answer questions in their domain.

### Nightwatch SEO MCP ★ Official ★ New
Official Nightwatch SEO MCP server — query live rank tracking, AI visibility, keyword research, site audits, and reports from Claude, Cursor, or ChatGPT. For operators running professional SEO programs who want AI-native access to rank data.

### SEO Performance MCP ★ New
Post-publish SEO performance MCP that scores every URL across Google Search Console, GA4, Matomo, Clarity, and AI citations — emitting a refresh/expand/merge/kill verdict per post. For content operators who need AI to tell them which posts to keep, improve, or retire."

### Glippy MCP ★ New
GEO analysis tools for MCP clients. Analyze and optimize content for generative engine optimization across AI search platforms.

---

## Development & Infrastructure

### Bright Data ★ Sponsor
Discover, extract, and interact with the web — one unified interface powering automated access across the public internet. Enterprise-grade web scraping and data extraction.

### Onlinecybertools MCP (280+ Tools)
280+ free dev/security tools in one MCP server: Base64/URL/JWT encoders, MD5/SHA/HMAC/bcrypt/argon2 hashes, JSON/YAML/XML formatters, regex tester, network diagnostics (ping/traceroute/dig/whois/SSL/SPF/DMARC), OSINT lookups. No auth, no API key.

### Cloudflare MCP ★ Official
Deploy, configure & interrogate Cloudflare resources (Workers/KV/R2/D1) from any MCP client.

### Chrome DevTools MCP ★ Official
Control and inspect a live Chrome browser from coding agents (Gemini, Claude, Cursor, Copilot). Official Google tool.

### DeepWiki by Devin ★ Official
Remote, no-auth MCP server providing AI-powered codebase context and answers.

### Context7 MCP ★ Official
Up-to-date, version-specific library documentation and code examples injected into AI coding prompts.

### GitHub MCP ★ Official ★ New
Official GitHub MCP server for repository search, issues, pull requests, code context, and GitHub workflows. `npx -y @github/mcp-server`

### Google MCP Servers ★ Official ★ New
Collection of Google's official MCP servers. Centralized repository of Google's MCP integrations. `https://github.com/google/mcp`

### Supabase MCP ★ Official
Official Supabase MCP server for managing projects, databases, auth, storage, edge functions, and SQL workflows from AI agents. `npx -y @supabase-community/supabase-mcp`

### Scrapling MCP
High-performance Python web scraping via Playwright. Proxy support, captcha solving, intelligent navigation. Speed-optimized alternative to Playwright/Puppeteer.

### MCPg — Production PostgreSQL MCP ★ New
Safe-by-default PostgreSQL Model Context Protocol server for AI agents. Production-grade with guardrails. `https://github.com/devopam/MCPg`

### Schemabrain ★ New
Read-only trust + intelligence layer between AI agents and your database. The agent never writes SQL — Schemabrain translates natural language to safe queries, refuses PII before the query runs, and logs every call in a tamper-evident audit trail. Postgres today. Essential for operators who want AI agents to query production data without direct database access. `https://mcp.so/server/schemabrain/Arun-kc`

### Next.js DevTools MCP ★ Official (Vercel)
Next.js development tools and utilities for AI coding assistants (Claude, Cursor). Debug, inspect, and optimize Next.js apps via MCP. Official Vercel tool.

### Proxyman MCP ★ Official
HTTP traffic inspection and debugging for AI agents. Create debugging rules, inspect network requests, and control Proxyman through natural language. Essential for API debugging.

### E2B ★ Official
Run code in secure cloud sandboxes hosted by E2B. Execute untrusted code safely, perfect for AI agents that need runtime environments. `npx -y @e2b/mcp-server`

### Serper MCP Server ★ New
Google Search API via Serper for AI agents. Fast, reliable web search with structured results — rankings, knowledge graph, and rich snippets. `npx -y @garymengcom/serper-mcp-server`

### Giteasy ★ New
Simplified Git operations through MCP — clone, commit, push, branch management without leaving your AI client. Streamlines developer workflows. `npx -y giteasy-mcp`

### Fastdomaincheck ★ New
Blazing-fast domain name availability checks via MCP. Check domain availability across TLDs for brand research, naming projects, and competitive intelligence. `uvx fastdomaincheck-mcp-server`

### Name Brewery Domain Checker ★ New
Bulk domain checking for AI agents: availability, aftermarket prices, archive.org history, social handle links, and buy links across 6 TLDs. Handles up to 50 names per call. 20 free credits to start. Useful for brand naming and domain acquisition research. `https://namebrewery.com/mcp`

### MCP Advisor ★ New
Discover and install the right MCP servers for your needs. Acts as a meta-layer — search across mcp.so's 22,000+ servers and get installation recommendations from your AI client. `npx -y @xiaohui-wang/mcpadvisor`

### Acopio ★ New
Curated developer tool catalog for AI agents. Save tools once — repos, CLIs, API docs — then let Claude, Cursor, and any MCP client search and recommend from your own curated catalog instead of generic model knowledge. Remote MCP over Streamable HTTP with OAuth 2.0 + DCR.

### NLP Toolkit ★ New
Natural language processing tools for business text analysis — sentiment analysis, entity extraction, summarization, keyword extraction. Process documents, customer feedback, and market reports via MCP.

### EdgeOne Pages MCP ★ New
Deploy HTML content to EdgeOne Pages CDN and obtain accessible public URLs. Simple deployment for static sites, landing pages, and single-page apps via MCP. By Tencent Cloud.

### Redirhub MCP Server ★ New
AI-powered URL redirect management and link shortener via MCP. Create, update, test, and monitor redirects. Alternative to Bitly with custom domains and team collaboration features.

### StillOnline MCP ★ New
Uptime monitoring and status pages via MCP. Manage monitoring projects, HTTP/SSL health checks, and incidents from any AI client. Requires Pro/Ultimate API key.

### Unterm MCP ★ New
Cross-platform desktop terminal (macOS/Linux/Windows, MIT) with built-in MCP server. Spawn tabs/panes, run commands with structured output, read screens, take scrolling screenshots, record sessions with secret redaction. Auto-registers with Claude Code/Codex/Gemini CLI.

### Contorium ★ New
Runtime Cognitive Cortex for AI coding workflows. Provides workspace awareness, project memory, runtime monitoring, and MCP context synchronization without taking control away from developers.

### Neo MCP ★ Sponsor ★ New
NEO MCP lets Claude Code, Cursor, and VS Code hand off complex AI engineering tasks — model evaluations, agent optimization, and more — to NEO's specialized infrastructure. Built for engineering teams scaling AI workflows.

### NWO Robotics ★ New
Multi-domain MCP server exposing 201 tools across 30 categories behind one endpoint. On-chain identity verification on Base Mainnet. Autonomous-agent infrastructure, hardware control, and crypto operations in one package.

### Primerfp Scout ★ New
Government contracting intelligence MCP for US federal + SLED contracting: semantic opportunity search, USASpending awards, recompete pipeline, congressional policy intel, GAO protests, and capture/teaming. 32 read-only tools via Streamable HTTP. `https://mcp.primerfp.com/mcp`

### chain-signer ★ New
Pre-signature security suite for AI agents operating on EVM chains. Flags wallet drains, permit-phishing, and risky actions before signing. Non-custodial protection layer for crypto-aware operators and DeFi automation.

### QA Skills ★ New
43 QA and test-automation skills for Claude Code, Codex, Cursor, and any Agent Skills Standard runtime. Full test-automation toolkit for operators who ship software.

### Tani ★ New
Agent-native hub (tani.ai) — AI agents discover capabilities in a trust-scored registry, exchange verified answers, and find each other. 12 MCP tools for capability resolution, agent registration, surface submission, and verified answer contribution. Registry ranked by computed invocation trust — success rate, dependents, and schema stability.

### SeedBase ★ New
Synthetic test data generation for databases. Generate realistic, FK-consistent test data from AI agents. List projects, get schema DDL, generate datasets as SQL. Ideal for operators who need test data without production exposure.

### BUILDY ★ New
Build real web apps on demand from ChatGPT, Claude, or any coding agent. Cross-agent compatible — build once and use the same app/data across different AI clients. `https://buildy.ai`

### Rami Code Review ★ New
Rami reviews every pull request for the bugs, logic errors, and risky patterns that AI coding agents commonly leave behind. When it flags something, your agent — Claude Code, Cursor, or Codex — fetches the review and fixes it. For engineering operators who want an AI safety net on AI-generated code.

---

## Productivity

### Cal.com MCP ★ Official
Connect AI clients to Cal.com scheduling. Hosted endpoint at `mcp.cal.com` or local instance.

### Chipp MCP ★ Official
Build, deploy, and monetize AI agents — "What Shopify did for ecommerce, Chipp does for AI agents."

### Karea ★ New
Extensive MCP tools so Claude Code, Cursor, and other MCP clients can create, edit, close, recap, and link dev tasks while coding. Jira linking, productivity recap. `npx -y karea-mcp`

### Unclick ★ New
Universal remote for AI: one MCP install gives any compatible agent 450+ callable endpoints across 60+ integrations, plus persistent cross-session memory. Like Zapier for AI agents. Ideal for operators who want a single MCP that covers hundreds of APIs. `npx -y unclick-mcp`

### FileToPDF ★ Official ★ New
Convert files (DOCX, XLSX, PPTX, images), HTML, and Markdown to pixel-perfect PDFs. npx stdio or hosted Streamable HTTP. Free API key in one click. Essential for operators generating reports, invoices, and documents programmatically. `npx -y @filetopdf/mcp`

### MindMeister MCP ★ Official ★ New
Create, edit, and organize mind maps from any AI assistant. Remote hosted MCP at `mcp.mindmeister.com/mcp`. Visual brainstorming and knowledge mapping via MCP. Streamable HTTP transport.

### MeisterTask MCP ★ Official ★ New
Create and manage projects, tasks, and notes from AI assistants. Remote hosted at `mcp.meistertask.com/mcp`. Full project management — from the creators of MindMeister. Streamable HTTP transport.

### HomeLab Monitor ★ New
Read-only MCP server for self-hosted homelab dashboards — explore hosts, Docker containers, GPU/VRAM, systemd services, AI models, alerts, and disk. `https://github.com/SikamikanikoBG/homelab-monitor`

### Wikimint ★ New
Knowledge management and wiki tools via MCP. Create, edit, and query structured knowledge bases from AI clients. Ideal for operators building internal knowledge repositories.

### Flomo MCP Server ★ New
Connect AI agents to Flomo notes for knowledge management. Capture ideas, meeting notes, and research directly into your Flomo workspace from any MCP client. `npx -y mcp-server-flomo`

### Smart Match ★ New
AI-powered job matching and application tracker. Analyze job listings against your resume, get a match score (0-100), identify skill gaps, generate cover letters, and track your application pipeline. Ideal for recruitment operators and job seekers.

### Capafy ★ Sponsor ★ New
Marketplace for monetizing agent skills as products. On Capafy, your Skill runs online 24/7 as an agent product, and you get paid every time someone uses it. The "App Store for agent skills" — build once, earn continuously.

### Toolforest MCP ★ Official ★ New
Hosted remote MCP server with managed OAuth for a growing list of 15+ toolkits, including Google Workspace, Last.fm, MusicBrainz, Fitbit, Oura, Kalshi, and Polymarket. Single endpoint, managed auth — ideal for operators who want multiple integrations without managing individual API keys.

### Matchbox ★ New
Describe a real-world problem in plain language and Matchbox finds products built to solve it — with reasoning, honest caveats, what each product won't cover, and a frank "no strong match" when nothing fits. Useful for operators evaluating tools and vendors.

---

## Communication

### Granola MCP ★ Official
AI-powered meeting notes and summaries. Connect your meeting data to AI agents.

### Superlist MCP Server ★ Official
Task and project management via MCP. Connect AI agents to your Superlist workspace.

---

## Content Creation & Creative

### EverArt ★ New
AI image generation via MCP. Generate marketing visuals, social media assets, product mockups, and creative content from any MCP client. Official integration with EverArt's FLUX and SD models. `docker exec -i mcp-node bash -c "EVERART_API_KEY=*** npx -y @modelcontextprotocol/server-everart"`

### SuperMaker AI ★ New
AI-powered content creation platform for video and image generation. Create marketing assets, product demos, and social content programmatically through MCP. Ideal for operators scaling content production.

### Scenext ★ New
AI educational video generation platform. Generate high-quality explainer and tutorial videos from question-answer pairs. MCP-native for automated video content pipelines.

### MiniMax MCP ★ Official ★ New
Official MiniMax MCP server for powerful TTS (Text-to-Speech), image generation, and video generation APIs. Create voiceovers, marketing visuals, and video content directly from AI agents. `npx -y @minimax/mcp`

### Vidoly AI ★ New
AI image & video generation for social media, branding, ecommerce, and digital content. Use Vidoly AI to generate images, create videos, and streamline visual production from any MCP client. Streamable HTTP.

### Blog2Video ★ New
Convert blog URLs to video in under 3 minutes via MCP. Turn written content into video assets for social media and marketing pipelines without leaving your AI client.

### Video Overlay Kit ★ New
AI-driven animated b-roll overlay renderer for short-form video. Paste your script into any AI coding tool (Claude Code, Cursor, Codex), the MCP server writes the scene spec and renders an mp4. Eight track kinds (flow, compare, list-reveal, hub-spin, cadence-pop, node-draw, side-slide, orbit) with Remotion + Tabler icons + LottieFiles stack. Portrait 1080×1920 for social (LinkedIn, IG Reels, TikTok, YouTube Shorts) and landscape 1920×1080 for YouTube. Free, MIT, fully local — no accounts, no per-render cost. Essential for growth operators scaling short-form video production with AI. `npx -y @alichherawalla/video-overlay-kit` · [GitHub](https://github.com/alichherawalla/video-overlay-kit)

---

## Marketing

### Zernio MCP ★ Official ★ New
Social media scheduling platform — manage and publish content across all major platforms from a single API. MCP-native. `https://docs.zernio.com/mcp`

### FeedSquad ★ New
Content calendar and social publishing for Claude and ChatGPT agents. Create posts and campaigns, schedule with cadence guardrails, and publish to LinkedIn, X, and Threads. OAuth 2.1 authentication. Anti-slop pattern registry checks all drafts before scheduling. Approval-first workflow — nothing goes live without explicit approval.

### Convika - LP ops ★ New
Landing page ops platform built for MCP clients. Create, preview, and publish landing pages with forms, analytics, custom domains, and version history. OAuth 2.1. `https://mcp.convika.com`

### Adology AI ★ New
Perplexity for social: ask what competitors are running across social and get answers grounded in real ad and creative data, not guesses. Competitor ad intelligence for marketing operators — discover creative strategies, ad formats, and media mix from any MCP client.

### Versium Reach ★ New
Lead enrichment and audience building for AI agents. Describe what you need and Versium REACH builds and sizes B2B/B2C audiences, fills in contact and company data, and verifies emails. All through natural language.

### Sendpulse MCP ★ New
Full marketing platform via MCP — email campaigns, CRM, chatbots, SMTP, and online courses. 134 methods across 5 categories. `npx sendpulse-mcp`

### Solnk MCP ★ New
Social media management for 9 networks — Instagram, TikTok, YouTube, X, LinkedIn, Pinterest, Facebook, Threads, Bluesky. Draft-first safety model with team approval workflow, content calendar, and analytics. MCP server for AI agents to draft and publish posts from a single interface. `https://solnk.com`

### Socialclaw ★ New
Social media scheduling MCP for AI agents across 11 platforms — X, LinkedIn, Instagram, Facebook Pages, TikTok, Discord, Telegram, YouTube, Reddit, WordPress, and Pinterest. Broader platform coverage than most social MCPs, including Discord and Telegram for community operators.

### AdWhispr ★ New
Chat with any brand's Meta (Facebook/Instagram) ads inside Claude — research a competitor's ad library, surface their longest-running winners, extract hooks/formats, and clone winning ads for your own brand. Essential for performance marketers and growth operators who want AI-assisted creative intelligence.

### Blend MCP — Cross-Channel Marketing ★ Official ★ New
Google Ads, Meta Ads, TikTok Ads, Microsoft Ads, Pinterest Ads, Amazon Ads, LinkedIn Ads, and Reddit Ads — all from one MCP server. Safe, robust, built for agencies. Manage cross-channel campaigns without switching dashboards. `npx -y blend-mcp`

### Zevari ★ New
Remote MCP server for LinkedIn sales workflows: research prospects, draft outreach, classify LinkedIn inbox replies, prepare campaigns, and stage sensitive LinkedIn actions behind review gates. Built for B2B sales operators who want AI-assisted LinkedIn prospecting without automation risk.

### LinkedIn MCP ★ New
Connect Claude or ChatGPT to your LinkedIn account to see who engaged on your posts, track performance and profile viewers, spot warm outreach signals, and publish content. Built for B2B marketers and creators who live on LinkedIn.

### Signaliz ★ New
B2B lead generation, email verification, company enrichment, and governed GTM Ops. Full-stack outbound intelligence for operators running sales pipelines — identify targets, verify contact data, enrich company profiles, and manage GTM operations from any MCP client.

### FounderSignal ★ New
Ask Claude what SaaS ideas are worth building — revenue data, growth signals, and pain points from 10+ sources. Market validation for operators evaluating new product ideas or competitive threats.

### Enrich MCP Server ★ New
Free company intelligence from domain or company name — company name, country, contacts, and social profiles. No API key required. Quick company lookup for lead enrichment and competitive research from any MCP client. `npx -y enrich-mcp-server`

### mailtani ★ New
Manage email marketing from Claude, Cursor, or any MCP-compatible AI agent — contacts, lists, campaigns, segments, and event tracking. For operators who want AI-assisted email marketing without switching between dashboards.

### Maqui Analytics ★ New
All-in-one marketing analytics MCP — Instagram, ads, web traffic, SEO and reviews for local businesses and the agencies that manage them. Consolidates multiple data sources into one MCP endpoint for marketing operators.

### HYPD.AI ★ New
Enable AI agents such as Claude, Copilot, Codex to create, manage, and optimize advertising campaigns on ChatGPT. For operators running ad campaigns who want AI-native campaign management.

### Orcool Studio MCP ★ New
AI video ad production for GTM engineers and growth teams — 107 tools for UGC concepts, AI avatars, Veo 3 video rendering, and performance feedback. For growth operators scaling video ad production with AI.

### Spresh ★ New
Spy on competitor Facebook ads. Decode their marketing strategy and copy their winning ad formats. For performance marketers and growth operators running competitive ad intelligence.

---

## Memory & Knowledge

### Anki MCP ★ Official
Enable AI assistants to interact with Anki spaced-repetition flashcards.

### XMemo
Persistent memory for AI agents across sessions.

### Vault Cortex ★ New
MCP server for Obsidian vaults — search, memory, link graph, 23 tools, OAuth-protected. Connect AI agents to your Obsidian knowledge base. Ideal for operators who use Obsidian as their second brain.

---

## New This Week (June 11, 2026 — mcp.so + mcpservers.org)

### Afternoon sweep — 10 new servers from mcp.so Latest + mcpservers.org All

| Server | Category | Description |
|--------|----------|-------------|
| Convika - LP ops | Marketing | Landing page ops platform via MCP, OAuth 2.1 |
| Versium Reach | Marketing | Lead enrichment, B2B/B2C audience building, email verification |
| Sendpulse MCP | Marketing | Full marketing platform — email, CRM, chatbots, SMTP (134 methods) |
| Auditspark | Content/Research | AI website audit across SEO, performance, accessibility, UX — free tier |
| OpenSEO | Content/Research | SEO research: keywords, SERP, domain analysis, rank tracking |
| Amap Maps (高德地图) | Content/Research | China's second-largest mapping platform — AutoNavi MCP |
| NWO Robotics | Dev/Infra | 201 tools across 30 categories, on-chain identity on Base |
| Primerfp Scout | Gov/Intelligence | US federal + SLED contracting — 32 tools, Streamable HTTP |
| QA Skills | Dev/Infra | 43 QA and test-automation skills for AI agents |
| Smart Match | Productivity | AI job matching, resume scoring, cover letter generation |

### Morning sweep — 11 servers

| Server | Category | Description |
|--------|----------|-------------|
| MiniMax MCP | Content Creation | Official TTS, image gen, video gen APIs via MCP |
| FeedSquad | Marketing | Content calendar + social publishing (LinkedIn, X, Threads), anti-slop registry |
| EdgeOne Pages MCP | Dev/Infra | Deploy HTML to CDN, static sites via MCP (Tencent Cloud) |
| Baidu Map MCP | Content/Research | China's largest mapping platform via MCP |
| Redirhub MCP | Dev/Infra | URL redirect management, link shortener (Bitly alternative) |
| StillOnline MCP | Dev/Infra | Uptime monitoring & status pages via MCP |
| Unterm MCP | Dev/Infra | Cross-platform terminal (MIT) with built-in MCP server |
| Contorium | Dev/Infra | Runtime Cognitive Cortex for AI coding workflows |
| Neo MCP | Dev/Infra | AI engineering task delegation (model evals, agent optimization) |
| Capafy | Productivity | Monetize agent skills — "App Store for agent products" |
| Doorprofit | Analytics/Data | US crime, safety, demographic, and rent data by address |

### Evening sweep — 11 new servers from mcp.so Latest + mcpservers.org All

| Server | Category | Description |
|--------|----------|-------------|
| HTAG Property Intelligence MCP ★ | Data/Intelligence | Australian property intelligence, 70+ read-only tools over Streamable HTTP |
| agents.hellobooks.ai | Finance/Accounting | AI agents that automate bookkeeping and financial close for SMBs |
| infaton-1c-mcp | Finance/Accounting | 1C:Enterprise ERP — 51 tools for metadata, documents, registers, reports |
| Unclick | Productivity | 450+ callable endpoints across 60+ integrations + persistent cross-session memory |
| Secure Google Sheets MCP | Data Firewall | PortEden data firewall for Google Sheets — permission-gated, audit-logged |
| FileToPDF ★ official | Productivity | Convert DOCX, XLSX, PPTX, images, HTML, MD to PDF — free API key |
| Vault Cortex | Memory/Knowledge | Obsidian vaults MCP — search, memory, link graph, 23 tools, OAuth-protected |
| Geekflare | Content/Research | Scraping, web search, screenshots, network tools for AI agents |
| Remote Jobs MCP | Data/Intelligence | Jobicy MCP — autonomous remote job search and filtering in real-time |
| Vidoly AI | Content Creation | AI image & video generation for social media, branding, ecommerce |
| IRONCLAW BTC Node | Finance | Bitcoin blockchain data — 17 tools, x402 USDC micropayments, no API keys |

## New This Week (June 12, 2026 — morning sweep)

### 7 new servers from mcp.so Latest + mcpservers.org All

| Server | Category | Description |
|--------|----------|-------------|
| Solnk MCP | Marketing | Social media management for 9 networks — draft-first, team approval, content calendar |
| Shikamaru | Finance | Day-count and accrued interest calculations — provably correct financial math |
| Tani | Dev/Infra | Agent-native hub with trust-scored capability registry, 12 MCP tools |
| SeedBase | Dev/Infra | Synthetic test data generation — FK-consistent SQL datasets for databases |
| BUILDY | Dev/Infra | Cross-agent web app builder — build once, use from any AI client |
| Blog2Video | Content Creation | Convert blog URLs to video in under 3 minutes via MCP |
| chain-signer | Security/Finance | Pre-signature security suite for EVM agents — wallet drain and phishing protection |

## New This Week (June 12, 2026 — afternoon sweep)

### 8 new servers from mcp.so Latest + mcpservers.org All

| Server | Category | Description |
|--------|----------|-------------|
| Webotee AI Connect | Ecommerce/Data | Amazon seller intelligence — brand, seller, ASIN info, under-competed niches via MCP |
| Toolforest MCP ★ Official | Productivity | Hosted remote MCP with managed OAuth for 15+ toolkits (Google Workspace, Last.fm, Fitbit, Oura, Kalshi, Polymarket) |
| Socialclaw | Marketing | Social media scheduling across 11 platforms — X, LinkedIn, Instagram, Facebook, TikTok, Discord, Telegram, YouTube, Reddit, WordPress, Pinterest |
| Matchbox | Productivity | Plain-language problem → product matching with reasoning, honest caveats, and "no strong match" when nothing fits |
| Mnemom | Trust/Security | Trust ratings for AI agents and websites — reputation scores, signed scorecards, zero-auth reads |
| signer-mcp | Finance/Crypto | Keyless CEX/DEX signing for AI agents — exchange API keys inside AWS Nitro Enclave (Binance, OKX, Bybit, KuCoin, Hyperliquid, Asterdex) |
| Gas Fee Predictor | Finance/Crypto | Live ETH + Layer-2 gas fee data — cheapest L2, best time to transact, per-action cost estimates |
| ActivitySmith MCP ★ Official | Productivity | Send push notifications and Live Activities to paired iOS devices via MCP |

## New This Week (June 12, 2026 — evening sweep)

### 2 new servers from mcp.so Latest + mcpservers.org All

| Server | Category | Description |
|--------|----------|-------------|
| Dealflowpro | Finance/Real Estate | Multifamily real estate deal analysis — scoring, max offer prices, market data via MCP |
| Kaginet Bitcoin Escrow | Finance/Crypto | Trustless Bitcoin escrow for AI agent-to-agent payments — 29 tools, Intel TDX enclaves |

---

## New This Week (June 13, 2026 — morning sweep)

### 5 new servers from mcp.so Latest + mcpservers.org All

| Server | Category | Description |
|--------|----------|-------------|
| Adology AI | Marketing | Perplexity for social — competitor ad intelligence across social media, grounded in real ad data |
| Truee Ai | Business Identity | AI-ready business profiles — structured business data layer for AI agent discoverability |
| cityparity | Analytics/Data | Cost-of-living comparison across 165 cities, 69 countries — salary parity, tax regimes, quality scores |
| Name Brewery Domain Checker | Dev/Infra | Bulk domain checking with aftermarket prices, archive.org history, social handle links |
| Acopio | Dev/Infra | Curated developer tool catalog — save tools once, let MCP clients search and recommend |

---

## New This Week (June 13, 2026 — evening sweep)

### 8 new servers from mcp.so Latest + mcpservers.org Finance/All

| Server | Category | Description |
|--------|----------|-------------|
| Schemabrain | Security/Database | Read-only trust + intelligence layer between AI agents and Postgres — PII refused before query runs, tamper-evident audit log |
| Disclos — EU AI Act | Compliance/Legal | Remote MCP for EU AI Act compliance (Regulation 2024/1689) — classify AI systems, risk tiers, ISO crosswalks. No install. |
| Conta Azul MCP | Finance/ERP | Brazilian ERP for AI agents — sales, customers, products, payables/receivables, NF-e invoices. 35 tools (read + write), OAuth 2.0. |
| Plinth FX MCP | Finance | Exchange rates from ECB via Frankfurter — latest, convert, historical, time-series. SRE-grade rate limiting. |
| finra-mcp-server | Finance/Compliance | FINRA Query API as MCP tools — regulatory data for financial services operators |
| Longbridge | Finance | 13 agent skills for Longbridge Securities — market data, fundamentals, portfolio, quant for HK/US/A-share/SG markets |
| TradeInsight | Finance | US stock market data — OHLCV price history, top movers by volume/moving-average/price-change, ticker search |
| Trainzilla Coach MCP | Business Ops | AI assistant for fitness coaches — manage clients, workouts, diet plans, scheduling, habit tracking, billing via OAuth 2.0 |

---

## New This Week (June 13, 2026 — late night sweep)

### 10 new servers from mcpservers.org Finance + Marketing tabs

| Server | Category | Description |
|--------|----------|-------------|
| IBKR Portfolio Builder | Finance | Top-down portfolio research for Interactive Brokers — 468 typed screeners tagged by strategy intent. Read-only. |
| IBKR MCP | Finance | Unofficial local MCP for Interactive Brokers market data, account positions, and trading workflows |
| AdWhispr | Marketing | Chat with any brand's Meta ads inside Claude — competitor ad library research, winning ad detection, hook extraction |
| Blend MCP ★ Official | Marketing | Cross-channel marketing: Google, Meta, TikTok, Microsoft, Pinterest, Amazon, LinkedIn, Reddit ads from one MCP |
| Signaliz | Marketing | B2B lead gen, email verification, company enrichment, and governed GTM Ops |
| Zevari | Marketing | LinkedIn sales workflows — research prospects, draft outreach, classify inbox replies, stage sensitive actions behind review gates |
| LinkedIn MCP | Marketing | Connect Claude/ChatGPT to LinkedIn — track post engagement, profile viewers, warm outreach signals, publish content |
| FounderSignal | Marketing | Ask Claude what SaaS ideas are worth building — revenue data, growth signals and pain points from 10+ sources |
| Enrich MCP Server | Marketing/Data | Free company intelligence from domain/company name — name, country, contacts, social profiles. No API key. |
| MCP for Indexa Capital | Finance | Access Indexa robo-advisor portfolio (European markets) through official API from any MCP client |

---

## New This Week (June 14, 2026 — morning sweep)

### 22 new servers from mcp.so Latest + mcpservers.org Finance/Marketing/All

| Server | Category | Description |
|--------|----------|-------------|
| AlphaAI News | Finance | Real-time AI-enriched financial news — full-text/ticker search, insider transactions, read-across |
| Rockmoon Financial Data | Finance | Cross-market (US/JP/KR) financials, segments, ownership, valuation — 18 tools, source-traceable |
| TradeOS AI | Finance | Trading data, indicators, strategy logic, and agent workflows via MCP |
| Hive Intelligence MCP | Finance | Managed crypto intelligence — market data, DeFi, wallets, DEX, NFTs, prediction markets |
| PineForge Codegen ★ Official | Finance | AI writes PineScript v6, transpiles to C++, backtests on Binance data — fully local |
| IndustryLens | GTM/Sales | Cited competitive-intelligence reports and head-to-head competitor comparisons — live B2B SaaS data |
| Mamba Labs GTM Suite | GTM/Sales | Six GTM signal tools — hiring detection, ICP scoring, Clay-ready data |
| ICP Fit Scorer | GTM/Sales | Qualifies accounts against ICP with score, tier, and per-signal reasoning |
| GTM Signals Aggregator | GTM/Sales | Hiring + tech-stack signals into GTM fit score for account prioritization |
| OpenWeb Ninja MCP ★ Official | Data/API | 40+ web data APIs — search, e-commerce, local business, jobs, real estate, finance |
| audit-ledger-mcp | Compliance | Tamper-evident audit logging for AI decisions — AWS S3 Object Lock, 7-year retention, EU AI Act ready |
| GSC Wizard MCP | SEO/AI Visibility | Query Google Search Console analytics from AI agents — natural-language performance data |
| Ranki.io SEO/AEO ★ Official | SEO/AI Visibility | Free SEO + AEO consultant — audits URLs, generates sitemaps, llms.txt, robots.txt, finds keyword gaps |
| Local AI Visibility | SEO/AI Visibility | Share-of-Model score for local businesses — checks if AI names your business when asked |
| auto-geo ★ Official | SEO/AI Visibility | GEO-optimized content publishing engine for AI visibility and discoverability |
| Nightwatch SEO MCP ★ Official | SEO/AI Visibility | Live rank tracking, AI visibility, keyword research, site audits from Claude/Cursor/ChatGPT |
| SEO Performance MCP | SEO/AI Visibility | Post-publish SEO scoring across GSC, GA4, Matomo, Clarity, AI citations — per-post verdict |
| Glippy MCP | SEO/AI Visibility | GEO analysis tools for generative engine optimization across AI search platforms |
| mailtani | Marketing | Email marketing from MCP clients — contacts, lists, campaigns, segments, event tracking |
| Maqui Analytics | Marketing | All-in-one marketing analytics — Instagram, ads, web traffic, SEO, reviews |
| HYPD.AI | Marketing | AI agents create, manage, optimize advertising campaigns on ChatGPT |
| Orcool Studio MCP | Marketing | AI video ad production — 107 tools for UGC concepts, AI avatars, Veo 3 rendering |
| Spresh | Marketing | Competitor Facebook ads spy — decode strategy and copy winning ad formats |

---

## New This Week (June 14, 2026 — afternoon sweep)

### 2 new servers from mcp.so Latest

| Server | Category | Description |
|--------|----------|-------------|
| Pollbolt | Business Ops | AI-native survey & form builder — surveys, responses, analytics, webhooks via MCP. OAuth 2.1, hosted Streamable HTTP |
| Video Overlay Kit | Content Creation | AI-driven animated b-roll overlay renderer for short-form video — 8 track kinds, Remotion + Tabler stack. Free, MIT, local |

---

## Previous Additions (June 10, 2026 — sweep 2)

| Server | Category | Description |
|--------|----------|-------------|
| Perplexity Ask MCP | Content/Research | AI-powered research via Perplexity (by Perplexity) |
| AgentQL MCP | Content/Research | Structured web data extraction with query language |
| Jina AI MCP Tools | Content/Research | AI search, embeddings, and content processing |
| Search1API | Content/Research | Unified multi-engine search API |
| Reddit MCP Server | Content/Research | Reddit data for social listening and market research |
| Giteasy | Dev Tools | Simplified Git operations via MCP |
| Fastdomaincheck | Dev Tools | Domain availability checks for brand research |
| MCP Advisor | Dev Tools | MCP server discovery and installation recommendations |
| NLP Toolkit | Dev Tools | NLP text analysis for business documents |
| EverArt | Content Creation | AI image generation for marketing assets |
| SuperMaker AI | Content Creation | AI video and image content creation |
| Scenext | Content Creation | AI educational video generation |
| Wikimint | Productivity | Knowledge management and wiki tools |
| Flomo MCP Server | Productivity | Flomo notes integration for knowledge management |

## June 10, 2026 (sweep 1)

---

## Ecosystem Stats

- **Total MCP servers tracked:** 22,282 (mcp.so), 9,000+ (mcpservers.org)
- **Official servers:** 40+ (from Google, GitHub, Cloudflare, Anthropic, Microsoft, MiniMax, PineForge, auto-geo, etc.)
- **CorpusIQ connectors:** 37+ (the most comprehensive business data MCP server)
- **Categories represented:** 30+ (Finance, Analytics, CRM, Commerce, Dev, Marketing, Content Creation, Gov/Intelligence, Media, Business Identity, Compliance, Business Ops, GTM/Sales Intelligence, SEO & AI Visibility, etc.)
- **New this cycle (June 14 morning):** 23 newly catalogued servers — AlphaAI News, Rockmoon Financial Data, TradeOS AI, Hive Intelligence, PineForge Codegen, IndustryLens, Mamba Labs GTM Suite, ICP Fit Scorer, GTM Signals Aggregator, OpenWeb Ninja MCP, audit-ledger-mcp, GSC Wizard, Ranki.io, Local AI Visibility, auto-geo, Nightwatch SEO, SEO Performance MCP, Glippy MCP, mailtani, Maqui Analytics, HYPD.AI, Orcool Studio MCP, Spresh
- **New this cycle (June 14 afternoon):** 2 newly catalogued servers — Pollbolt, Video Overlay Kit
- **Cumulative since June 9:** 133 MCP servers catalogued across 13 sweeps

---

## How to Use External MCP Servers

Most MCP clients (Claude Desktop, Cursor, Windsurf, Hermes) support multiple MCP server connections simultaneously. To add an external server alongside CorpusIQ:

```json
{
  "mcpServers": {
    "corpusiq": {
      "url": "https://mcp2.corpusiq.io/mcp",
      "transport": "streamable-http"
    },
    "firecrawl": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": {
        "FIRECRAWL_API_KEY": "fc-YOUR_KEY"
      }
    },
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    }
  }
}
```

Check each server's documentation for specific transport type (streamable HTTP, stdio, SSE) and authentication requirements.

---

*← [MCP Servers Home](/hermes/mcp/servers/) | [Connector Catalog](/hermes/mcp/connectors/) →*

*↑ [MCP Documentation](/hermes/mcp/)*

*Powered by CorpusIQ — monitoring the MCP ecosystem for business operators*
