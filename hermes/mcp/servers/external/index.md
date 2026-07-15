---
title: External MCP Server Catalog
description: Curated catalog of notable third-party MCP servers for business operators  --  finance, analytics, document intelligence, security, and productivity
---

# External MCP Server Catalog

Beyond CorpusIQ's 37+ built-in connectors, the MCP ecosystem now has 22,000+ servers spanning every domain. This catalog tracks the most relevant third-party MCP servers for business operators  --  curated from [mcp.so](https://mcp.so) and [mcpservers.org](https://mcpservers.org).

> **Last updated:** July 15, 2026 (evening supplement) · **Sources:** mcp.so (22,680+ servers), mcpservers.org (9,300+ servers), GitHub search

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


### CarDossier MCP Server ★ New (June 30)
MCP Server for CarDossier Poland Market API — real-time used car market data: valuations, price history, liquidity metrics, and market trends. Essential for automotive operators, fleet managers, and insurance in the Polish and broader EU used-car market. `github.com/Joyall-au/cardossier-mcp-server`

### Chuhching ★ New
Financial data integration platform. Provides AI agents with structured financial information.

### DDG Agent Payable Services MCP ★ New
Agent payable services and micropayments via the DuckDuckGo agent ecosystem. Enables AI agents to transact with small-value payments.

### Gatewards ★ New
Drop-in spend governance and cross-agent dedup proxy for AI agent fleets. Per-agent budget enforcement, non-custodial x402 settlement over MCP. Essential for teams deploying multiple autonomous agents who need cost controls.

### SQD Portal ★ New
Query onchain data across EVM, Solana, Bitcoin, Substrate, and Hyperliquid through the SQD Portal API. Hosted remote endpoint or local stdio server for blockchain data access.

### Valid — Vehicle Identity MCP Server ★ New
Vehicle identification, history verification, and automotive data via MCP. AI agents can verify VINs, check vehicle history, and access automotive intelligence.

### Easy Predict ★ New
Predictive analytics platform via MCP. Provides AI agents with forecasting, trend analysis, and predictive modeling capabilities.
### BillingServ MCP ★ New (July 2)
Customer, invoice, and order lookups via the BillingServ billing platform API. AI agents can search customers, retrieve invoice details, and query order statuses — turning billing inquiries into conversational queries. Essential for operators using BillingServ for subscription/invoice management. `github.com/BillingServ/MCP` · [Integration Guide](/hermes/mcp/servers/external/billingserv/)

### AICryptoVault MCP ★ New (July 2)
MCP-native treasury infrastructure — AI agents interact with crypto wallets for balance queries, transaction history, and agent-governed DeFi operations. Remote SSE transport. Essential for operators managing crypto treasury who want programmatic, auditable wallet access through AI agents. `github.com/browtastic/cloudaiwallet-mcp-servers` · [Integration Guide](/hermes/mcp/servers/external/aicryptovault/)

### Alpha Vantage MCP Server ★ Sponsor
Realtime & historical stock, ETF, options, forex, crypto, commodities, fundamentals, technical indicators. Official MCP server from Alpha Vantage. [Full integration guide →](/hermes/mcp/servers/external/alphavantage-mcp/)

### Co-Invest MCP Server ★ New (July 3)
Invest with AI agents — market research, portfolio analysis, trade execution, and strategy backtesting. Built on Liquid Trade infrastructure. Official MCP from liquid.trade. Essential for operators managing personal or firm investments who want AI-driven research and execution. [Full integration guide →](/hermes/mcp/servers/external/coinvest-mcp/)

### Tradingview Mcp ★ New
Live market data & technical analysis for AI assistants  --  30+ tools across stocks, crypto, forex & futures: screeners, indicators, candlestick patterns, multi-timeframe analysis, backtesting & live sentiment. Works with Claude, ChatGPT, Cursor & Copilot. Self-host free (MIT) or one-URL hosted. Essential for financial operators who rely on TradingView's charting and technical analysis ecosystem.

### Tossinvest MCP ★ New
Korean stock trading via Toss Securities Open API  --  real-time prices, orders, portfolios. Local MCP server (`npx tossinvest-mcp`). Read-only by default; trading tools disabled unless explicitly enabled. Korean & US stocks, exchange rates, market hours. Regional but significant for operators in the Korean financial market.

### AlphaAI ★ New
Hosted MCP server for AI-enriched financial news  --  full-text and ticker-scoped news search, trending stories, and SEC Form 4 insider activity, each story scored 1–10 for relevance. OAuth 2.1, free tier 100 calls/hour. Essential for operators who need curated, AI-scored financial intelligence.

### Tokenbel Financial Data
Read-only access to Belarusian securities: tokens, shares, bonds, companies, ticker search. Niche but notable for Eastern European markets.

### Infrawise ★ New
Azure FinOps infrastructure cost optimization. Helps operators manage cloud spend with AI-assisted cost analysis. `npx -y @infrawise/mcp-server`

### Costory ★ New
Multi-cloud FinOps MCP  --  ask your AI assistant a cost question and get allocation, correlation, and explanation in one response. Normalized cost data across AWS, GCP, Azure, Datadog, OpenAI, and Anthropic. Essential for operators managing multi-cloud infrastructure who need AI-driven cost intelligence without switching between vendor consoles.

### Fleets MCP ★ New (July 4)
Multi-site analytics dashboard for AI agents. Read-only GA4, Search Console, Cloudflare edge, and PageSpeed data across every site you run, plus audits that return paste-ready fixes. Local stdio server via `npx -y fleets-mcp`. Essential for operators managing multiple web properties who need unified analytics across all their sites in one AI conversation.

### Cloudability API ★ New
Comprehensive MCP server for the Cloudability API  --  advanced cloud cost management, Kubernetes container analytics, and budget forecasting across multi-cloud environments. Enables AI agents to query normalized cloud spend, rightsizing recommendations, and commitment discount analysis without switching between cloud consoles. Essential for FinOps operators and cloud cost managers.

### agents.hellobooks.ai ★ New
AI agents that automate bookkeeping and financial close for SMBs. Streamable HTTP transport. Hands-free bookkeeping via MCP  --  ideal for small business operators who want AI to handle financial close.

### Aikount Mcp ★ New (June 28)
Spanish accounting (contabilidad) for AI agents — issue invoices, OCR expense PDFs into deduplicated purchases, reconcile bank movements, and prepare quarterly VAT returns (Modelo 303) over REST API. For autónomos and SMEs in Spain. Essential for operators in Spanish/LATAM markets who want AI-driven accounting automation with local tax compliance.


### Seiche — US Money Market Stress Testing MCP ★ New (July 12)
Free open source funding stress terminal for US money markets. 22 engines, honest backtests, zero data cost using Fed/NY Fed/OFR/Treasury public APIs. AGPL-3.0. Essential for treasury operators and financial risk analysts. `github.com/beepboop2025/seiche` · [Integration Guide](/hermes/mcp/servers/external/seiche-finance-mcp/)

### Financial News MCP ★ New (July 12)
Real-time financial news for AI agents — search by ticker, source, and language with sentiment analysis and entity extraction. Essential for operators who need live market context alongside portfolio data. [Integration Guide](/hermes/mcp/servers/external/financial-news-mcp/)


### AI2Fin Tax MCP ★ New (July 3)
### OilPriceAPI MCP ★ New (July 4)
Real-time oil, gas, and commodity prices for AI agents. The commodity-data MCP server behind fintech dashboards, fleet & logistics tools, and maritime compliance platforms — same API serves 2M+ requests every month. Essential for operators in energy, logistics, and commodities trading who need live pricing data in their AI workflows. `github.com/OilpriceAPI/mcp-server` ⭐3

### Earningsprism ★ New (July 4)
SEC filing intelligence for AI agents — access and analyze SEC filings, EDGAR data, and financial disclosures through MCP. Enables AI assistants to research public company financials, compare filings, and surface regulatory insights. Essential for financial analysts, investors, and operators doing public-company due diligence.

### Agent Signals ★ New (July 4)
Pay-per-call crypto market intelligence for AI trading agents. 20 tools: price, funding rate, market regime, orderbook, volatility, momentum, Fear & Greed, top movers, gas, stablecoin pegs, ENS, one-call market summary, plus unique Japan data (bitFlyer/Coincheck JPY board). Essential for operators running AI trading agents who need comprehensive crypto market data.

Free, public MCP server for verified tax rates across 50+ countries — GST/VAT, income tax, company tax, and capital gains tax. No login, no API key. Every answer source-cited to the national tax authority (ATO, IRD, HMRC, IRS). Streamable HTTP at `https://taxmcp.ai2fin.com`. Essential for e-commerce operators, finance teams, and anyone doing cross-border pricing or tax planning. · [Integration Guide](/hermes/mcp/servers/external/ai2fin-tax-mcp/)

### infaton-1c-mcp ★ New
MCP server for 1C:Enterprise (ERP, Accounting)  --  51 tools for metadata, documents, registers, reports. Essential for Eastern European and Russian-market operators running on 1C.

### IRONCLAW BTC Node ★ New
Bitcoin blockchain data server for AI agents  --  17 tools (fees, mempool, transactions, address portfolio, trace, whales, SEC insider trades, web scraping, AI summarization, capital flows, Reddit). x402 USDC micropayments on Base. No API keys needed.

### Shikamaru ★ New
Provably correct day-count and accrued-interest calculations. Small, dependency-light TypeScript library and MCP server for precise financial math. AI agents can get the exact number instead of guessing  --  essential for bond markets, fixed income, and financial operations.

### Savvly MCP Server ★ New
Retirement projections, eligibility, comparisons, and FAQs for an SEC-registered fund pairing full market upside with longevity payouts. Savvly offers longevity-linked investment products through the Savvly 80+ fund  --  milestone cash payouts at ages 80, 85, 90, 95. MCP-native for financial advisors and AI planning tools.

### AusEcon MCP ★ New
Australian economic and financial data  --  ABS (Australian Bureau of Statistics), RBA (Reserve Bank of Australia), and APRA (Australian Prudential Regulation Authority). MCP server for AI agents needing verified Australian economic data. Docs: auseconmcp.com

### Lovie  --  Company Formation MCP ★ New
Company formation, bank accounts, cards, invoices, and payments  --  all directly from AI agents. The Company Formation MCP for business operators who want to incorporate, bank, and manage finances through their AI toolchain.

### Legal Doc Intelligence ★ New
AI-powered legal document analysis, contract review, and compliance checking — extract clauses, assess risk, and verify regulatory alignment

### Lawstronaut MCP ★ New (July 15)
Access millions of official legal and regulatory source documents from 155+ jurisdictions via MCP. Structured legal research, laws, regulations, cases, and guidance for AI agents. Essential for operators managing cross-border compliance and international regulatory research. [Integration Guide](/hermes/mcp/servers/external/lawstronaut-mcp/)

### Substack Publisher MCP ★ New (July 12)
Queries Substack posts, engagement analytics, subscriber counts, and publications through the official Publisher API. Essential for content operators running newsletter-first businesses who want AI-driven analytics. [Integration Guide](/hermes/mcp/servers/external/substack-publisher-mcp/)

### CrustAPI MCP — Live Google Search ★ New (July 12)
MCP server for CrustAPI — live Google Search, Maps, News, Images, and Reviews. Pay-per-result pricing (no subscription). Essential for operators who need occasional live web intelligence without ongoing costs. [Integration Guide](/hermes/mcp/servers/external/crustapi-mcp/)


### GoldLegal Legal Compliance API ★ New
AI legal compliance  --  contract review, ad law check, risk scoring, EU AI Act compliance, China AI regulation, AI content watermark check. MCP-over-HTTP with 6 tools. Hosted on Alibaba Cloud FC. Built-in compliance standards for global operators.


### EU Textile Sustainability MCP ★ New (July 12)
Free search engine for EU textile sustainability law — ESPR, DPP, CSRD, CBAM, CWA 18291. Remote MCP server, no API key. Essential for operators in fashion/textile who need AI-accessible regulatory intelligence.

### shieldly-io — AWS Security Analysis MCP ★ New (July 12)
AI-Powered Security Analysis for AWS — official MCP server. Analyze IAM policies and CloudFormation templates from any MCP client. Essential for DevOps operators needing shift-left security analysis. [Integration Guide](/hermes/mcp/servers/external/shieldly-aws-mcp/)


### Personal Finance MCP Server ★ New
Personal finance calculations in the Claude ecosystem. Guide users through compound interest, loan amortization, retirement planning, tax estimation, and budgeting. Ideal for operators who want AI-driven personal finance alongside business tools.

### GoodVat MCP Server ★ New
Global tax compliance knowledge and tools. AI assistants get access to verified VAT, GST, and sales tax data across 200+ jurisdictions. Built and maintained by goodvat.com. Essential for operators managing cross-border commerce.

### ifthenpay Payments MCP ★ New
Generate payments, retrieve transaction history, and interact with ifthenpay services directly from AI agents. Portuguese payment gateway integration for European operators.

### PipRail ★ New
AI agent autonomous payment execution for any x402 (HTTP 402) API across 29 blockchains. Budget-capped, self-custody, no facilitator fees. Essential for operators automating micropayment workflows.

### SentiSense ★ New (July 2)
Market intelligence MCP for AI agents: US market mood, stock sentiment, SentiSense Score, market-moving news, analyst ratings, 13F filings. Five read-only tools, zero-config OAuth, no API key required. Essential for investment analysts and fintech operators needing AI-driven market intelligence without API key management. `sentisense.ai` · [Integration Guide](/hermes/mcp/servers/external/sentisense/)

### HPSILab Quant Finance MCP ★ New (July 2)
Institutional-grade quantitative finance MCP: options analytics (Black-Scholes, Greeks), implied volatility surfaces, Monte Carlo simulations, AI market signals, and strategy backtesting. Quantum ML (Qiskit) and regime detection. Essential for quant analysts, hedge fund operators, and fintech builders needing AI-driven quantitative finance workflows. `mcp.so` listing · [Integration Guide](/hermes/mcp/servers/external/hpsilab-quant/)

### Kalshi MCP ★ New (July 2)
First prediction-market MCP server. CFTC-regulated Kalshi markets from any AI agent — get markets, positions, and place orders on event contracts. TypeScript. Essential for operators in prediction markets, political forecasting, and event-driven trading. `github.com/onofre-jauregui/kalshi-mcp` · [Integration Guide](/hermes/mcp/servers/external/kalshi-mcp/)

### pipeworx Business Data Suite ★ New (July 2)
Industrial-scale MCP wrapping: 18+ servers shipped in a single day. Business-relevant: **mcp-tradier** (stock & options market data via Tradier Brokerage API), **mcp-eodhd** (EOD Historical Data for global equities), **mcp-diffbot** (Diffbot Knowledge Graph for company enrichment), **mcp-coresignal** (LinkedIn-adjacent company + employee data), **mcp-peopledatalabs** (person/company enrichment), **mcp-shodan** (Shodan REST API for internet scanning), **mcp-pulsedive** (threat intelligence IOC enrichment), **mcp-seo-backlinks** (DataForSEO backlink intelligence), **mcp-emailable** (Emailable email verification), **mcp-here** (HERE Maps — geocoding, routing, POI). All TypeScript, consistent tool naming. `github.com/pipeworx-io` · [Integration Guide](/hermes/mcp/servers/external/pipeworx-business-data/)

### Hermes Plant MCP Server ★ New (July 1 PM)
Runnable MCP server for deterministic finance and quant APIs paid over x402. Provides AI agents with provably correct financial calculations, quantitative models, and market analytics with cryptographic payment rails. For operators building AI-driven quantitative finance workflows with verifiable computation. `github.com/JesseGdotIO/hermesplant-mcp-server` · [Integration Guide](/hermes/mcp/servers/external/hermesplant-mcp-server/)

### Customs Mcp ★ New
Trade tariff data for GB and US imports. Two tools: `hs_lookup` (product descriptions → HS commodity codes) and `duty_rates` (import duties, preferential rates, VAT). Freemium: 20 free queries per key, then $0.02/query. Essential for ecommerce operators managing international shipments.

### hourledger-mcp ★ New
Work hours, overtime, and gross pay calculation with tested rulesets for US federal, California, Alaska, Colorado, and Nevada law. MCP-native payroll intelligence for operators managing distributed teams.

### Openswissdata ★ New
9 MCP tools for Swiss federal data: TARES tariffs, FINMA registry, NOGA classifications. BAZG-authorized. Essential for operators doing business in Switzerland or needing verified Swiss regulatory data.

### LoneStarOracle MCP Server ★ New
38 tools for live data: crypto token analysis, DeFi risk, equities, energy, weather, real estate, and on-chain intelligence. Comprehensive market data MCP for multi-asset operators.

### RealMarketAPI MCP Server ★ New
Real-time gold, forex, crypto, and stock market data with ultra-low latency. Designed for trading platforms, fintech apps, and analytics systems. Streamable HTTP transport.

### FinData MCP ★ New
Financial data MCP server: stock quotes, company fundamentals, economic indicators, SEC filings, and crypto prices via x402 micropayments. Pay-per-call model  --  no subscription needed.

### ACCRUE ★ New
Non-custodial stablecoin yield. Stablecoin Yield Index (SYX) + 12 USDC vault APYs across Ethereum, Base, Arbitrum. MCP-native DeFi yield for AI agents.

### ERABI ★ New
Open intent exchange where AI agents get a cryptographic identity, reputation-ranked discovery, and dual-signed outcomes on a publicly auditable ledger. Zero-config, no accounts needed.

### signer-mcp ★ New
Keyless CEX/DEX signing for AI agents  --  exchange API keys stay inside an AWS Nitro Enclave, so a prompt-injected agent can't leak them. Binance, OKX, Bybit, KuCoin, Hyperliquid, Asterdex. Security-first design for AI trading agents.

### Praesentire ★ New
Bilingual (English + Traditional Chinese) financial news sentiment scored by Claude  --  three tools for tickers, batches, and cross-language divergence. Hosted MCP for operators who need AI-curated financial sentiment with East-West market coverage.

### Agentberg ★ New
Agent-to-agent knowledge exchange for trading intelligence  --  publish empirical findings, vote on quality, earn reputation, and unlock higher-credibility collective intelligence the more you contribute. Distributed trading intelligence network for AI agent operators.

### ROIC.AI Financial Data API ★ Official ★ New
Access ROIC.AI financial data from AI tools, including company financials, ratios, prices, transcripts, and market research data. Official MCP server for fundamental analysis  --  essential for operators who need institutional-grade financial data in their AI workflows.

### Ensotrade ★ New
Bloomberg-grade crypto intelligence for AI agents  --  real-time market data, institutional-grade analytics, multi-exchange coverage, and portfolio intelligence. MCP-native for operators who need professional crypto market data in their AI workflows.

### Evibe Portfolio ★ New
Read-only investment portfolio access via MCP  --  holdings, performance metrics, dividends, benchmarks, and stock screeners. Official MCP server from Evibe. Essential for operators who want AI-driven portfolio intelligence without manual data entry.

### PubFi MCP ★ New (June 26)
Route crypto data needs through PubFi capability and gateway tools. MCP-native crypto data orchestration for AI agents. Essential for operators managing multi-chain crypto data workflows.

### zopnight ★ New (June 26)
Query and govern your AWS, GCP & Azure cloud estate (and AI runtimes like Bedrock & Vertex AI) from Claude Code or Cursor. Surfaces waste, cost, ownership, and 400+ audit findings across 200+ resource types. Essential for FinOps operators managing multi-cloud infrastructure.

### Opencloudcosts ★ New (June 28)
Anchor AI FinOps to real, live cloud pricing. Multi-cloud MCP server for AWS, GCP & Azure — public list prices AND enterprise negotiated rates (Reserved Instances, Savings Plans, CUDs, EDPs). No credentials needed to query pricing data. Essential for FinOps operators who need AI agents to reason about cloud costs with real pricing data.

### Quotor ★ New (June 26)
Real, bindable home & auto insurance quotes via MCP  --  actual carrier rates, not estimates. Texas market with expansion planned. 11 tools with carrier-masked options and human-completed bind. Essential for insurance operators and fintech platforms integrating quote flows into AI agent workflows.

### Fahali ★ New (June 28)
Market intelligence data for AI agents via MCP. Query market data, competitive intelligence, and business insights directly from AI assistants. Essential for operators who need AI-driven market research and competitive analysis without manual data gathering. `github.com/BobMain-2025/fahali-mcp`

### MyLinedChart Chart Context ★ New (June 28)
Read-only MCP server giving AI agents access to live MyLinedChart desktop workspace — chart context, candles, drawings, indicators, and IBKR connection status. Local, private, read-only. First MCP bridge for the MyLinedChart/Interactive Brokers trading ecosystem. Essential for traders and financial operators who use MyLinedChart for technical analysis. `github.com/none298-dotcom/mylinedchart-mcp-chart-context`

### Chytrý Rejstřík ★ New (June 29)
AI-ready MCP server for comprehensive Czech business intelligence. Search, verify, monitor, and analyze companies using data aggregated from 20+ official public sources — financial statements, ownership structures, legal records, and more. Essential for operators doing due diligence, supplier verification, and competitive research in the Czech market. `chytryrejstrik.cz`

### CryptoGate ★ New (June 29)
Non-custodial crypto payments for AI assistants. Connect your CryptoGate account to Claude, ChatGPT, or any MCP-compatible assistant to check balances, volume and stats, look up customer payments and invoices, and create crypto payment links on the spot. Read-heavy MCP with zero write risk. Essential for operators running crypto-native businesses who want AI-driven payment operations. `cryptogate.com`

### Delegum ★ New (June 29)
Spanish tax, labor law, and finance MCP server with 42 tools: IRPF, autónomos, nóminas (payroll), despidos (terminations), herencias (inheritances), pensiones, and hipotecas (mortgages). All calculations follow Spanish regulations. No registration, no API key required. Essential for operators managing Spanish businesses, employees, or personal finances through AI agents. `github.com/meskeIA/delegum`

### Fylings MCP ★ New (June 29)
African company-intelligence platform for searching, verifying, and monitoring businesses across official company registries. Turns public registries across the continent into clean, free company pages. MCP-native access for AI agents doing African market research, supplier verification, and business intelligence. Essential for operators expanding into or operating in African markets.

### SIMA MCP Server ★ New (June 29)
Read-only tools for discovering the capabilities of the SIMA protection platform for Solana AI agents, autonomous wallets, and trading bots. Explore SIMA platform features directly from MCP-compatible AI clients. For Solana ecosystem operators and DeFi traders. `sima-prime.com`

### Web3Agent ★ New (June 29)
Web3 MCP proxy server for AI agents: EVM execution, DeFi swaps, bridges, advanced orders, market data, wallet management, and confirmation-gated writes. First MCP-native Web3 proxy that treats AI agents as first-class blockchain citizens. Essential for operators running AI-driven DeFi strategies, cross-chain operations, and on-chain automation.

### Bitcoin Monetary Data ★ New (June 29 PM)
Honest monetary data for AI agents. Compare purchasing power erosion over time, reveal the gap between CPI and real M2 money supply growth, and show Bitcoin vs dollar performance. No spin, no API key. Live SSE endpoint. Essential for operators who need inflation-adjusted financial context for AI-driven analysis.

### Ko Financial Data ★ New (June 29 PM)
Real SEC, 13F, insider, congress & macro data your AI agent can cite. 24 tools — institutional holdings, insider & congress trades, spot-Bitcoin-ETF ownership, financials, and Treasury/Fed/BLS macro. Hosted Streamable HTTP, free tier (200 calls/day). Essential for operators building AI investment research workflows.

### Clypra ★ New (June 29 PM)
MCP server for AI agent payments. x402 USDC on Base micropayment integration. Enables AI agents to transact with small-value cryptocurrency payments.

### Arcade Trading ★ New (June 29 PM)
Trading-focused MCP server. Provides AI agents with trading data, market access, and transaction capabilities.

---

## Document Intelligence

### Sifter
Extracts structured, typed records from documents (PDFs, scans, contracts, invoices) using natural-language field specs. Agents can query and aggregate  --  exact counts, sums, filters, with source-page citations. Unlike RAG, answers collection-wide questions.

### Unstructured Transform MCP ★ New (July 15)
Parse PDFs, CSVs, images, and documents into structured AI-ready data via the Unstructured platform. Remote MCP transport — turn raw files into queryable intelligence for AI agents. Essential for operators processing invoices, contracts, and reports at scale. [Integration Guide](/hermes/mcp/servers/external/unstructured-transform-mcp/)

---

## Analytics & Business Intelligence

### SIXTA Connect ★ New (June 28)
DBRE-grade SQL analysis inside any MCP client — no connection, no install required. Paste a query, EXPLAIN plan, migration, or error → get named findings with severity, rationale, and ready-to-run fixes for PostgreSQL and MySQL. Essential for operators running database workloads who need instant SQL review and optimization without connecting to production.

### Sparkient MCP ★ New (June 30)
Sub-100ms Decision Intelligence API via MCP. Instant structured decisions for content moderation, fraud detection, ticket triage, and approval workflows. Real-time AI decision-making at production latency. Essential for operators running high-volume decision workflows. `mcpservers.org: sparkient/sparkient-mcp-server`

### Clamp Analytics MCP
Analyze and manage traffic, funnels, cohorts, revenue, errors. Web/app analytics via MCP. Complementary to GA4 for product analytics use cases.

### Google Analytics MCP ★ New (July 1 PM)
Free, open-source MCP server (44 tools) connecting Google Analytics 4 (GA4) to Claude, Cursor, Windsurf, and any MCP client. Traffic analysis, funnel exploration, real-time reporting, and e-commerce analytics via natural language. MIT license. Essential for operators who want AI-driven GA4 analytics without vendor lock-in. `github.com/yusofansari/google-analytics-mcp`

### Playwright MCP ★ Official (Microsoft)
Official Microsoft MCP server for browser automation, page inspection, screenshots, and web interaction. 78 tools for AI agents. `npx @playwright/mcp@latest`

### Browserbase ★ Official
Automate browser interactions in the cloud  --  web navigation, data extraction, form filling. Cloud-hosted, no local browser needed. `npx @browserbasehq/stagehand-mcp`

### Doorprofit ★ New
US location intelligence: crime safety scores, recent incidents, neighborhood demographics, rent data, and registered-offender search by address. Free tier available. Useful for site selection, real estate due diligence, and location-based business decisions.

### HTAG Property Intelligence MCP ★ Official ★ New
Australian property intelligence, H3 spatial intelligence, and capability discovery  --  70+ read-only tools over Streamable HTTP. Public connectors for real estate operators, investors, and property analysts. Official HTAG integration.

### AppAmbit MCP ★ New (July 13)
All-in-one mobile app platform via MCP — analytics, crash reporting, build distribution, managed databases, serverless functions, and CMS. 10 GitHub stars. First comprehensive mobile development MCP server. Essential for mobile app operators who want AI-driven product operations across the full mobile lifecycle. [Integration Guide](/hermes/mcp/servers/external/appambit-mcp/)

### AI Visibility Analytics MCP ★ New (July 14)
Brand visibility monitoring across 15+ AI providers (ChatGPT, Perplexity, Gemini, AI Overviews). MCP connector runs scans, compares competitor mentions, and tracks brand presence in AI-generated responses. Essential for marketing operators and brand managers navigating the AI search era. · [Integration Guide](/hermes/mcp/servers/external/ai-visibility-analytics/)

### SaaS and AI Pricing API MCP ★ New (July 14)
Free REST API and MCP server for verified SaaS, AI, and LLM pricing across 490+ tools. OpenAPI 3.1, no API key required. Gives AI agents structured access to the pricing landscape. Essential for operators in procurement, vendor research, and tool stack evaluation. · [Integration Guide](/hermes/mcp/servers/external/saas-pricing-mcp/)

### Remote Jobs MCP ★ New (Jobicy)
Autonomous remote job search  --  AI tools can search, filter, and retrieve the latest remote job listings in real-time via public Jobicy MCP server. Useful for recruitment agents and talent operations.

---


### Booyah Index MCP ★ New (July 2)
Free AI-readable directory of 3,520 local businesses across 14 Southeast Asian cities (Bangkok, Singapore, Bali, Kuala Lumpur, Ho Chi Minh City, and more). Search restaurants, services, and local businesses by category, city, or keyword. Essential for market researchers and expansion teams targeting SE Asian markets. `github.com/sarapab-th/booyah-index-mcp` · [Integration Guide](/hermes/mcp/servers/external/booyah-index/)

### qlows MCP — Tender & RFP Search ★ New (July 2)
Real-time tender and RFP search across 35 WTO-GPA countries (US, EU, Australia). AI agents can search procurement opportunities, extract RFP requirements, and match company capabilities to relevant tenders. Essential for business development teams and proposal writers in government/commercial procurement. `github.com/getqlows/qlows-mcp` · [Integration Guide](/hermes/mcp/servers/external/qlows-mcp-tender-search/)

### Infino ★ New
Keyword, vector, hybrid, and SQL retrieval over data on object storage, for AI agents. Multi-modal search across structured and unstructured data.

---

## Content & Research

### AI Localization Agent MCP ★ New (July 13)
Stop wasting AI tokens on localization. MCP server by l10n.dev connecting AI agents to dedicated translation infrastructure. 3 GitHub stars. Essential for operators managing multi-language content who want AI-driven localization without burning LLM tokens. [Integration Guide](/hermes/mcp/servers/external/ai-localization-agent/)

### Horizon AI Intelligence MCP ★ New (July 13)
Free AI-industry intelligence for agents — briefings, regulation tracker, and regional lenses. By system-alchemist. Essential for operators tracking AI policy changes, competitive intelligence, and regional compliance requirements. [Integration Guide](/hermes/mcp/servers/external/horizon-mcp/)

### Crustdata MCP ★ New (July 4)
Real-time B2B company and people intelligence for AI agents. Connects to 15+ live data sources — search companies, find and enrich people and contacts, run job and social-post searches, and set up watchers that monitor accounts and people for changes across 1B+ people and 100M+ companies. Essential for sales operators, recruiters, and business researchers who need live B2B intelligence in their AI workflows.

### ENTIA Entity Verification ★ New (July 4)
Verified business-identity intelligence for AI agents and MCP clients — company verification, VAT, BORME, GLEIF, ownership and risk signals across 34 countries. Remote MCP server, free tier (100 req/day). Sources: BORME, VIES, GLEIF, Wikidata. Essential for compliance officers, KYC/AML operators, and anyone doing cross-border business verification through AI agents.

### Scribefy
Extract timestamped YouTube transcripts, video search, metadata, and related-video tools. Works with Claude, Cursor, Windsurf, and any MCP client.

### Tubask MCP ★ New (July 2 PM)
Hosted YouTube MCP for Claude & Cursor — video search, metadata, transcripts, and content intelligence. No local setup. `npx mcp-remote https://tubask.app/mcp` · [Integration Guide](/hermes/mcp/servers/external/tubask-mcp/)

### The Agent Times MCP ★ New ★ Featured
#1 Agent News MCP on ClawHub & Smithery  --  real-time agent economy news, 6 tools, ed25519-signed articles, Bitcoin rewards for agent contributions. Streamable HTTP + JSON-RPC 2.0 at `theagenttimes.com/mcp`. Firehose, RSS, llms.txt feeds for agents. Essential for operators tracking the AI agent ecosystem in real time.

### Hacker News MCP ★ by NeCL
Access Hacker News data for AI agents: top stories, story details, comments thread, full-text search via Algolia. No API key required  --  public HN API. Built for content research, trend monitoring, and prompt enrichment. By Neural Engineering & Cognitive Logic (neclco.com).

### HumanTone ★ New (June 28)
Official MCP server for HumanTone. Humanize AI-generated text and check AI likelihood directly from Claude Desktop, Cursor, Cline, and other MCP clients. Growing category as AI content detection becomes standard — essential for operators who use AI-generated content but need it to pass as human-written for publishing, outreach, and brand communications. `github.com/HumanTone/humantone-mcp`

### NotebookLM MCP ★ New
Let CLI agents (Claude, Cursor, Codex) chat directly with NotebookLM for zero-hallucination answers based on your own notebooks. Ground-truth research from Google's NotebookLM. `npx -y @pleaseprompto/notebooklm-mcp`

### Paper Search MCP ★ 1.9k GitHub ★ New
20+ academic sources for AI agents  --  arXiv, PubMed, Semantic Scholar, bioRxiv, medRxiv, Google Scholar, Crossref, OpenAlex, CORE, PMC, Europe PMC, dblp, OpenAIRE, HAL, SSRN, Unpaywall + optional Sci-Hub. OA-first fallback chain, MIT license, Python 3.10+. Free-first design  --  no API keys required. `pip install paper-search-mcp`. Essential for research-heavy operators and academic market intelligence.

### OpenSERP ★ New
Multi-engine SERP extraction: Google, Yandex, Baidu, Bing, DuckDuckGo, Ecosia. Search results and URL data extraction. npm: `@openserp/mcp`

### Firecrawl MCP ★ Official ★ New
Official Firecrawl MCP Server  --  powerful web scraping and search for LLM clients. 3,300+ GitHub stars. `npx -y firecrawl-mcp`

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
Baidu Maps API via MCP  --  China's largest mapping platform. Location search, geocoding, directions, POI data, and route planning. First major map service fully MCP-compatible. Essential for China-market operators.

### freesearch-mcp ★ New
Routes search queries through public SearXNG instances — free alternative to SerpAPI, Exa, and Brave Search. No API keys, no rate limits, no billing. Perfect for operators who need AI web search without per-query costs.

### Geekflare ★ New
Web scraping, search, screenshots, and network tools for Claude, Cursor, ChatGPT, and other MCP clients. All-in-one web intelligence toolkit for operators who need to extract and monitor web data at scale. `npx -y @geekflare/mcp`

### Auditspark ★ New
AI-powered website audit for any URL across 10+ categories  --  SEO, performance, accessibility, UX, and content quality. Scored report in under 2 minutes. Free tier included. Ideal for operators auditing their web presence.

### SEOforGPT — AI Visibility / GEO MCP ★ New (July 2)
First purpose-built Generative Engine Optimization (GEO) MCP. Audit client visibility across ChatGPT, Claude, Perplexity, and Gemini. Track competitors and AI-cited sources. Generate AI-optimized content and publish to CMS. Essential for marketing agencies future-proofing their SEO practice as search shifts to AI platforms. `seoforgpt.com` · [Integration Guide](/hermes/mcp/servers/external/seoforgpt/)

### Google Maps Email Extractor ★ New (July 2 PM)
Turn Google Maps businesses into leads with verified contact emails — search by keyword or enrich a website list. No proxy required. `npx -y google-maps-email-extractor` · [Integration Guide](/hermes/mcp/servers/external/google-maps-email-extractor/)

### LinkedIn FastMCP ★ New (July 2 PM)
Open-source MCP for LinkedIn REST APIs — AI agents access LinkedIn data for sales, recruiting, and company research. `github.com/rajdudhare1/linkedin-fastmcp`

### Search Console Mcp (getpercy.io) ★ New (July 2 PM)
Alternative Google Search Console implementation — query GSC search analytics, indexing status, and performance data from AI agents. `github.com/sudomichael/search-console-mcp`

### OpenSEO ★ New
SEO research tools for AI agents: keyword research and metrics, SERP and local SERP results, domain and backlink analysis, rank tracking, and Google Search Console performance. `npx openseo-mcp`

### PipeTable MCP ★ New
Query local CSV, Parquet, JSON and TSV files with real SQL via DuckDB. Gives AI coding tools ground-truth data access instead of hallucinated answers. Data never leaves your machine. Essential for operators who work with data files and want SQL-grade analysis in their AI workflows. `npx -y pipetable`, `github.com/melihbirim/pipetable` ★1.

### Amap Maps (高德地图) ★ New
AutoNavi Maps MCP  --  China's second-largest mapping platform. Location search, geocoding, directions, and POI data. Essential for China-market operators alongside Baidu Maps. Official 高德 integration.

### Prowlo  --  Reddit & X for AI Agents ★ New
Content and community intelligence for Reddit and X (Twitter). Search both platforms in one tool, discover trending posts, and pull audience insights. Essential for operators managing social presence and community listening. `npx @prowlo/mcp`

### ACG Mcp ★ New
Audited Context Generation Protocol  --  verifiable fact-checking and grounded RAG via MongoDB. Standalone MCP server that provides verified, evidence-backed answers by grounding AI responses in audited sources. Essential for operators who need verifiable, citation-backed AI outputs for compliance, research, and decision-making.

### Prowlo  --  Reddit & X for AI Agents ★ New
Hosted MCP server for clean, semantically-searchable Reddit and X data  --  crawled through residential proxies, no Reddit API credentials needed. Most free Reddit MCP servers broke in 2026 when Reddit blocked unauthenticated endpoints; Prowlo runs the full pipeline. Read-only. 5 tools: search_dataset, reddit_search, list_records, read_post, read_comments. OAuth authentication. Free 14-day trial, then $19/mo. `https://api.prowlo.com/mcp`. Essential for operators doing social listening, market research, and community monitoring.

### OpenOSINT MCP ★ New
MCP-native OSINT framework  --  18 intelligence tools (email, username, breach, WHOIS, IP, Shodan, VirusTotal, Censys, AbuseIPDB, GitHub, DNS, phone, dorks). v2.22.0 (June 2026). MIT license. 710+ GitHub stars. Three AI backends (Anthropic, Ollama, OpenAI-compatible). Fully async with parallel tool execution. PDF + Markdown reports auto-saved. For authorized security research. `pip install openosint`. Essential for operators doing due diligence, competitive intelligence, and security research.

### Deckextract ★ New
DocSend & Papermark MCP server  --  extract decks and convert to PDF or PowerPoint from Claude, Claude Code, ChatGPT, and any MCP client. Document pipeline MCP for operators who share pitch decks, reports, and presentations through DocSend/Papermark and want AI agents to process them.

### AirLabs MCP Server ★ New (June 29)
Real-time aviation data API via MCP: flight data, airport schedules, delays, and reference databases for airlines, airports, aircraft types, and cities. Lets AI assistants access live aviation intelligence for travel planning, logistics, and flight tracking. Essential for operators in travel, logistics, and aviation who need real-time flight data in their AI workflows. `airlabs.co/docs`

### Minha Morada ★ New (June 29)
Search 181,000+ real estate listings in Portugal (apartments, houses, land) for sale or rent. Covers all 18 districts with data from Imovirtual, Idealista, and RE/MAX. MCP tools: search properties by location/price/typology, get property details, get market statistics. Essential for operators in real estate investment, relocation, and Portuguese property markets.

### Vublox Sports ★ New (June 29 PM)
Live football scores, match summaries, and fan clip links — no API key required. MCP-native sports data for AI agents. Essential for operators in sports media, betting analytics, and content creation around live football events.

### Trad Tune Explorer (thesession Data) ★ New (June 29 PM)
Explore traditional folk music using data from The Session. Search tunes, recordings, sets, and musicians, discover related tunes, analyze tune popularity, browse recordings by artist, and explore relationships between tunes and performers. Unique cultural data MCP for operators in music, arts, and cultural heritage.

---

## Data Infrastructure ★ New Section (July 15, Wave 2)

### Confluent MCP — Apache Kafka ★ New (July 15)
Official Confluent MCP server — Apache Kafka data streaming for AI agents. Real-time event streaming, topic management, schema registry, consumer group monitoring, and Connect management. Enterprise backbone for event-driven architectures. `npx -y @confluentinc/mcp-confluent` · [Integration Guide](/hermes/mcp/servers/external/confluent-mcp/)

### Elasticsearch MCP ★ New (July 15)
Official Elastic MCP server — full-text search, aggregations, vector search, and observability. AI agents can query any index with Elasticsearch Query DSL, run kNN semantic search, monitor APM traces and logs. `npx -y @elastic/mcp-server-elasticsearch` · [Integration Guide](/hermes/mcp/servers/external/elasticsearch-mcp/)

### Snowflake MCP ★ New (July 15)
MCP server for Snowflake data warehouse — query, explore schemas, manage warehouses, and analyze enterprise data through natural language. RBAC-aware. Essential for operators running data workloads on Snowflake. `npx -y mcp-snowflake-server` · [Integration Guide](/hermes/mcp/servers/external/snowflake-mcp/)

### Keboola MCP ★ New (July 15)
Data operations platform MCP — ETL, data engineering, and pipeline management for AI agents. Enterprise data stack integration.

---

## DevOps & Feature Management ★ New Section (July 15, Wave 2)

### LaunchDarkly MCP ★ New (July 15)
Official LaunchDarkly MCP server — feature flag management for AI agents. Toggle features, manage progressive rollouts, run experiments, and audit flag changes. Essential for product and engineering operators. `npx -y @launchdarkly/mcp-server` · [Integration Guide](/hermes/mcp/servers/external/launchdarkly-mcp/)

### OpenTofu MCP ★ New (July 15)
Infrastructure-as-code via MCP. OpenTofu (Terraform fork) for provisioning and managing cloud infrastructure through AI agents. DevOps niche.

### Instana MCP ★ New (July 15)
IBM Instana APM — application performance monitoring and observability for AI agents. Real-time infrastructure and application health.

### SmartBear MCP ★ New (July 15)
SmartBear testing tools MCP — API testing, UI testing, test management, and quality automation for AI agents.

### Tailscale MCP ★ New (July 15)
Tailscale networking via MCP — VPN, mesh networking, and secure service access for AI agents.

---

## Commerce & E-Commerce

### Monday.com MCP ★ New (July 15)
Official Monday.com MCP — project management, workflows, boards, and automations accessible to AI agents. First major PM platform with dedicated MCP. Essential for operators running cross-team projects and workflows. `npx -y @mondaycom/mcp` · [Integration Guide](/hermes/mcp/servers/external/mondaycom-mcp/)

### WordPress MCP ★ New (July 15)
WordPress CMS management via MCP — manage posts, pages, plugins, themes, and content directly from AI agents. `npx -y wsp-wordpress-mcp`

### HTML Pub MCP ★ New (July 13)
Publish AI-generated HTML to a live page on your own domain — MCP server by Leadpages. Remote endpoint at `mcp.htmlpub.com/mcp`. First major martech company (Leadpages) shipping an MCP server for content publishing. Essential for operators who want AI agents to create and deploy landing pages, announcements, and microsites without touching a CMS. [Integration Guide](/hermes/mcp/servers/external/htmlpub-mcp/)

### Toolzy MCP ★ New (July 13)
French tool rental marketplace via MCP — search and rent tools between individuals (particuliers). Finance & Commerce category. Niche regional — relevant for French-market operators in the sharing economy.

### Ecoexperten Energieausweis ★ New (July 4)
Order official energy performance certificates (Energieausweis, § 82 GEG) for residential buildings in Germany — directly from chat. The registered certificate (DIBt number) arrives by e-mail as PDF within 1 business day. Essential for German property operators, real estate agents, and landlords who need regulatory energy certificates through automated AI workflows.

### Maqami Travel MCP ★ New (July 2 PM)
Hotel booking worldwide — 65 tools across 249 countries. AI agents search, price, prebook, and book hotels (3M+ properties) plus flights, loyalty, and analytics. Zero API keys needed. First comprehensive travel MCP server. `npx mcp-remote https://mcp.maqami.co/` · [Integration Guide](/hermes/mcp/servers/external/maqami-travel/)

### BuyWhere MCP ★ New
First SEA e-commerce MCP server  --  real-time product search across 11M+ products in Singapore, SEA, and US markets. 6 tools: search_products, compare_prices, get_price, get_affiliate_link, get_catalog, get_product. Compatible with LangChain, LlamaIndex, CrewAI, Mastra + any MCP client. Free API key at buywhere.ai. `npx -y @buywhere/mcp-server`

### Profitlee-MCP ★ New
Ecommerce and marketplace profitability calculator. Analyze net profit, profit margin, ROI, breakeven price, and fee-adjusted outcomes from product cost, selling price, shipping, ads, platform fees, and tax inputs. Supports reusable profit scenarios. Essential for ecommerce operators managing multi-channel profitability.

### Portkey Admin MCP ★ New
150 tools across 18 domains for the Portkey AI Gateway  --  prompts, analytics, guardrails, API keys, virtual keys, users, workspaces, rate/usage limits. MIT license. ⚠ Maintenance mode post Palo Alto Networks acquisition (May 2026). Works end-to-end as of June 2026. `npx -y portkey-admin-mcp`

### Attio MCP Server ★ New
AI-native CRM (Attio) via MCP  --  manage companies, people, lists, and tasks directly from AI assistants like Claude, Cursor, and ChatGPT. Comprehensive Attio API support with robust error handling, automatic retry logic, and input validation. Requires Node.js 18+ and Attio API key. `npx -y @kesslerio/attio-mcp-server`. Essential for operators using Attio as their CRM who want AI agents to query and manage customer relationships.

### Pandadoc Mcp ★ New
PandaDoc document automation via MCP  --  create, send, and track proposals, contracts, quotes, and e-signatures directly from AI agents. Essential for operators who manage document workflows (sales proposals, legal agreements, SOWs) and want AI-driven document generation, signing, and pipeline tracking.

### Amplifier MCP Server ★ Official ★ New
D2C eCommerce fulfillment platform via MCP  --  manage orders, inventory, shipments, campaigns, and billing directly from AI agents. Official MCP server for the Amplifier fulfillment platform. Essential for ecommerce operators who need AI-driven fulfillment operations across their D2C channels.

### Amazon Seller Central / Amazon Ads ★ New
Connect Amazon Seller Central and Amazon Ads accounts to AI agents. Manage inventory and orders (Seller Central) alongside advertising campaigns and analytics (Amazon Ads). Two-in-one MCP server for Amazon marketplace operators who need both commerce operations and paid acquisition from a single agent interface.

### MewCP Razorpay MCP ★ New
Hosted, stateless, multitenant Razorpay MCP  --  manage payments, customers, subscriptions, invoices, and financial operations through India's leading payment gateway. Essential for Indian-market operators and global businesses processing INR transactions who want AI agents to handle payment workflows.

### mcp-jp ★ New
Japanese SMB SaaS connectors via MCP  --  30+ tools for KING OF TIME (attendance), SmartHR (HR management), kaonavi (talent management), Smaregi (POS), CloudSign (e-contracts), L Step (sales management), and more. Each connector is an independent pip package; connectors are archived once an official MCP ships. Essential for operators in the Japanese market who need AI-driven access to domestic SMB SaaS tools without waiting for official MCP support.

### OnePageCRM ★ New
Full CRM operations via MCP for OnePageCRM users. Create, search, update, and manage contacts, companies, deals, and notes directly from AI agents. Essential for sales operators using OnePageCRM who want AI-driven pipeline management and customer relationship workflows without switching between tools.

### E-commerce Fashion Market Analysis ★ New (June 28)
Fashion vertical MCP server — SEO audits, trend analysis, competitor monitoring, and ad copy generation for fashion e-commerce. Includes 12 playbook skills for AI agents. First fashion-industry-specific MCP server combining SEO, trends, and competitor intelligence in one agent toolkit. Essential for fashion e-commerce operators and DTC brands. `github.com/alexgenovese/ecommerce-fashion-market-analysis`

### Neuron ★ New (June 28)
WhatsApp automation platform with 120+ MCP tools for AI chatbots, broadcasts, campaigns, contact management, knowledge bases, and newsletters. First MCP-native WhatsApp marketing platform. Essential for operators in WhatsApp-first markets (LATAM, India, SEA, Africa) who want AI-driven customer communication, marketing automation, and chatbot deployment on the world's #1 messaging platform. `neuron.ng`

### Meta Business MCP — WhatsApp Business Cloud API ★ New (July 1)
Production-validated MCP server for WhatsApp Business Cloud API — compliance engine, error intelligence & message orchestration for AI agents. 24 tools, sub-2ms decisions, 85.6% test coverage. Built in Go. Unlike Neuron (which targets marketing campaigns), this server targets the raw WhatsApp Business Cloud API for transactional messaging, customer support, and compliance-enforced communication. Essential for operators who need AI agents to send/receive WhatsApp messages through Meta's official API with production-grade reliability. `github.com/metabusiness-mcp/meta-business-mcp` · [Integration Guide](/hermes/mcp/servers/external/meta-business-mcp/)

### Protonmail-rs — Proton Mail MCP ★ New (July 1)
Pure-Rust Proton Mail client — library, CLI, and MCP server with end-to-end OpenPGP encryption. First MCP server for Proton Mail. Gives AI agents encrypted email capabilities through Switzerland's privacy-first provider. Essential for operators in regulated industries (HIPAA, legal, finance) who need AI agents to handle encrypted email while maintaining end-to-end encryption and zero-access architecture. `github.com/filippofinke/protonmail-rs` · [Integration Guide](/hermes/mcp/servers/external/protonmail-rs/)

### Odoo MCP ★ New (July 2)
Free AI layer for Odoo ERP v16+ — zero Odoo-side setup. Connect any MCP client to accounting, inventory, CRM, and sales data via XML-RPC. No App Store module required. Essential for operators running Odoo ERP who want AI-driven business intelligence without ERP-side configuration. `github.com/tuanle96/mcp-odoo` · [Integration Guide](/hermes/mcp/servers/external/odoo-mcp/)

### Launch Fast MCP — Amazon FBA Analytics ★ New (July 2)
Amazon seller analytics via remote MCP — product research, seller analytics, Brand Analytics, keyword research, supplier research, and ads diagnostics. Essential for Amazon FBA operators who want AI-driven product and market intelligence. `github.com/BlockchainHB/launchfast-mcp` · [Integration Guide](/hermes/mcp/servers/external/launch-fast/)

### Container Tracking MCP ★ New (July 2)
Real-time ocean container tracking across 200+ shipping lines — live milestones, vessel positions, and ETA by container number, bill of lading, or booking reference. First logistics/supply-chain MCP server. Essential for operators managing international freight and supply chain visibility. `github.com/lxxmng/container-tracking-mcp` · [Integration Guide](/hermes/mcp/servers/external/container-tracking-mcp/)

### mailcue-mcp ★ New (June 28)
Give AI agents their own local mailbox to read, send, and triage email via MCP. Lightweight email automation for AI agents — simpler than full Gmail/Outlook MCP servers, no heavy OAuth setup required. Ideal for operators who want AI-driven email triage and response without connecting to production email infrastructure. `github.com/Olib-AI/mailcue`

---

## Compliance & Regulatory

### Threat Modeling and Security Scanning MCP ★ New (July 14)
Threat modeling, code, cloud and pipeline scanning, shadow-AI discovery, compliance checks and fixes from your AI assistant. Overlaps with SaferAgenticAI. INDEX ONLY.

### Quality Clouds Hub MCP ★ New (July 14)
AI code governance rules injected into Cursor, Claude Code and other MCP clients at generation time. Overlaps with vrules. INDEX ONLY.

### VerityLayer ★ New (July 4)
Fail-closed verify-before-you-act trust gate for AI agents. 5 tools: verify_fact, detect_injection, moderate_content, redact_pii, guard_action. Keyless, pay-per-call via x402 (USDC on Base); every verdict ships an Ed25519-signed receipt. Run: `npx -y @veritylayer/mcp`. Essential for operators deploying AI agents in production who need cryptographic proof of safety checks before agent actions execute.

### ChronoVerify ★ New (July 4)
Image authenticity verification for AI agents — checks when a photo was taken and whether it shows signs of editing. Validates C2PA Content Credentials against official trust lists, reads EXIF and XMP, runs pixel forensics, and returns one typed verdict with a confidence score. Works on any image, signed or not. Essential for operators in insurance, journalism, legal, and compliance who rely on photo evidence through AI systems.

### Chia Health MCP ★ New (July 1)
HIPAA-compliant telehealth operations via MCP — manage patient intake, prescriptions, consent forms, lab orders, and payment (Stripe) through AI agents. Supports GLP-1 weight loss clinics, peptide therapy, anti-aging, longevity medicine. First healthcare-operations MCP server. Essential for operators in telehealth who need to automate patient workflows through AI agents while maintaining HIPAA compliance. `github.com/Carolaunfading944/chia-mcp`

### Eleata E-Invoice MCP ★ New (June 30)
EU e-invoice validation MCP server — Peppol, XRechnung, Factur-X, UBL/CII validation with error code explanations. For AI agents processing EU-compliant electronic invoicing across multiple national formats. Essential for operators in EU markets where e-invoicing mandates are rolling out. `github.com/hernaninverso/eleata-einvoice-mcp`

### AIR Blackbox MCP Server ★ New
EU AI Act compliance checker  --  checks 6 articles, HMAC-SHA256 tamper-evident audit trails, auto-remediation with working code fixes. August 2026 deadline ready. Essential for EU operators deploying AI systems. `pip install air-blackbox-mcp`

### FeedOracle DORA OS ★ New
EU DORA compliance evidence infrastructure  --  50 MCP tools across 11 servers, ES256K-signed, blockchain-anchored evidence. July 2026 DORA deadline. For EU financial operators needing compliance-grade evidence automation.

### Trust Gate MCP ★ New ★ Featured
First post-quantum MCP server. Policy-gated AI agent decisions with hybrid Ed25519 + ML-DSA-65 (NIST FIPS 204) cryptographic receipts. Every tool call is policy-gated, hybrid-signed, and offline-verifiable. 4 tools: `gate_decision`, `verify_receipt`, `check_policy`, `health`. Production-ready (47 unit tests, 51 OWASP ASI checks, 0 CVEs in deps). EU AI Act Article 50 native, NSA CNSA 2.0 / NIST AI RMF / SOC 2 ready. Apache-2.0. Essential for operators in regulated industries who need cryptographically verifiable AI agent decisions with post-quantum security. `pip install trust-gate-mcp`

### Ares MCP ★ New
Official Czech business registry MCP server for ARES (ares.gov.cz). 14 tools: company lookup by IČO or name, full due diligence profiles (financials, ownership, statutory bodies), insolvency register checks, VAT-payer verification, trade-license validation, address search, and cross-company person graph analysis. Optional Ed25519-signed provenance records (source + date + signature) for offline verification. Experimental/beta. Essential for operators doing business in the Czech Republic or Central Europe who need verified company intelligence through their AI agents.

### botcorpus ★ New
Machine-first, web-sourced knowledge base of current CZ/SK/AT/EU civic, tax, and legal facts. Each fact includes source URL, extraction date, and confidence score. Purpose-built for AI agents operating in Central European jurisdictions — replaces hallucinated legal information with verified, timestamped knowledge. Essential for compliance officers, legal operators, and business entities in CZ/SK/AT/EU markets.

### Gocreative ★ New
Compliance, KYB (Know Your Business), sanctions screening, and data API for AI agents. Automated business verification, AML checks, and regulatory compliance workflows via MCP. Essential for operators in fintech, legal, and regulated industries.

### EMILIA Protocol ★ New
Require offline-verifiable human approval before AI agents take irreversible actions. Two-person rule, Ed25519 Trust Receipts, IETF-drafted protocol, Apache-2.0. MCP-native governance for high-stakes agent operations  --  ideal for financial controllers and compliance officers.

### Averta security ★ New
MCP gateway security  --  secure every MCP server with one governed gateway. Give each AI agent its own scoped MCP access, contain credentials at the gateway, and audit every MCP tool call without wiring agents directly to each server. Essential for operators running multi-agent, multi-server MCP deployments who need centralized security, credential management, and audit trails.

### Blocktrust TrustScan ★ New (June 29)
Digital trust verification for AI agents. Verify contact identities, domains, and websites. Detect phishing and invoice fraud. Sign interactions cryptographically (BIS). 15 tools, blockchain-anchored on Polygon. GDPR-compliant. Essential for operators who need AI agents to verify counterparties, detect fraud, and establish cryptographic trust before executing transactions. `github.com/brnbtech770/blocktrust-trustscan`

### MCP Long-Term Memory (GraphRAG) ★ New (July 2)
GraphRAG-backed persistent memory for AI agents via MCP. Neo4j knowledge graph storage enables multi-hop reasoning and structured cross-session recall — entities, relationships, and communities. Python. Essential for operators building persistent agent workflows where context must survive beyond a single session. `github.com/null-create/mcp-long-term-memory` · [Integration Guide](/hermes/mcp/servers/external/mcp-long-term-memory/)

### vrules ★ New (July 1 PM)
Open-source, vendor-neutral agent-governance and LLM guardrails framework. Vector-enabled rules engine for MCP proxying, policy-as-code, conditional organizational memory, and browser/WASM execution. Essential for operators deploying AI agents in production who need programmable guardrails, policy enforcement, and governance across their agent fleet — without vendor lock-in. `github.com/ops-ping/vrules` · [Integration Guide](/hermes/mcp/servers/external/vrules/)

### Kvasir Legal MCP ★ New (July 2)
Ground AI on verifiable German, Bavarian, and EU law — canonical legal objects with cryptographic provenance and pinpoint citations. Legal professionals can query regulations, search case law, and ground AI outputs in authoritative sources. Essential for compliance teams and legal operators in EU jurisdictions. `kvasir.legal` · [Integration Guide](/hermes/mcp/servers/external/kvasir-legal/)

### SaferAgenticAI MCP ★ New (July 2)
AI safety framework for agentic coding assistants over MCP — governance guardrails, safety checks, and policy enforcement. Every agent action validated against organizational safety policies before execution. Essential for operators deploying AI agents in production who need programmable safety guardrails. `github.com/NellInc/SaferAgenticAI` · [Integration Guide](/hermes/mcp/servers/external/saferagenticai-mcp/)

### Anteroom ★ New (July 2 PM)
AI legal counsel research MCP — frontier-lab commercial commitments, safety-framework version history, regulatory corpus, and partnership patterns. 5 primary-source-cited tools. Not legal advice. `npx mcp-remote https://mcp.anteroom.so/mcp`

---

## Development & Infrastructure


### Bothread MCP ★ New (July 13)
Local room where AI coding agents collaborate on one codebase via MCP — collisions prevented, human in command. By AdamACE9. Developer tool for multi-agent coding workflows.

### ResolveMesh Compatibility Intelligence MCP ★ New (July 13)
Hosted ResolveMesh compatibility MCP server — read-only, source-backed compatibility lookups for AI agents. By mo-sharif. AI & Agents category.

### LLM Observability MCP (LangTrace) ★ New (July 14)
Open source LLM observability and monitoring. Drop-in proxy for OpenAI, Anthropic, and Gemini with request logging, cost tracking, and agent tracing. Self-host with one Docker command. MIT license. Essential for operators running AI agents in production who need cost controls and debugging. · [Integration Guide](/hermes/mcp/servers/external/llm-observability-mcp/)

### ClassQuill MCP ★ New (July 14)
Read-only access to tutoring-business data (sessions, students, tutors, invoices, payments, reports) for Claude, Codex, Cursor. Education niche. INDEX ONLY.

### Microphone and Speech-to-Text MCP ★ New (July 14)
Give AI agents the ability to listen — microphone capture and speech-to-text tools for MCP-compatible agents. Agent infrastructure. INDEX ONLY.

### Writing Style Checker (WSC) MCP ★ New (July 14)
Prose linter and AI-slop detector: weasel words, passive voice, hedging, and 190+ research-cited AI tells. Web editor, API, MCP server, CLI, GitHub Action. Content quality. INDEX ONLY.

### Floot MCP ★ New (July 14)
Build and host full-stack apps with your own AI. Connect the Floot MCP server to Claude, Cursor, ChatGPT, and any MCP client. Development platform. INDEX ONLY.

### URL Capture MCP ★ New (July 14)
URL to PNG/JPEG/PDF capture API plus MCP server for AI agents. Playwright plus Fastify, deploy-ready on Fly.io. INDEX ONLY.

### Agent Coherence MCP ★ New (July 12)
Stop AI agents from silently overwriting shared files — TLA+-verified coherence guard for multi-agent systems. Essential for platform operators running multiple agents on shared infrastructure. [Integration Guide](/hermes/mcp/servers/external/agent-coherence-mcp/)

### Selenium MCP ★ New (July 12)
Selenium MCP server for AI agents — 39 browser automation tools with page snapshots, selector hints, multi-session, and batched execution. Essential for operators needing enterprise-grade browser automation.

### MCP Time Server ★ New (July 12)
Zero-dependency clock + drift guard for Claude Desktop, Claude Code, and claude.ai. Local, remote, and hook flavors. Small but essential for time-sensitive agent workflows.

### E2LLM / SiFR Browser MCP ★ New (July 12)
Structured perception (SiFR) plus browser action — gives AI agents eyes and hands in a real browser, working with the AI you already use.

### Prompt Improver MCP ★ New (July 12)
Hosted MCP server that turns rough requests into sharp Role/Task/Context/Format prompts. Thai + English. Essential for operators who want consistent, high-quality agent outputs.


### nuzur ★ New (July 4)
Database change safety for AI agents — AI agents propose database schema and data changes as reviewable requests before anything is applied. No direct write access. Works with Claude Code, Cursor, and any MCP client. Essential for operators who want AI to help with database work but need human-in-the-loop approval gates before any schema or data mutations.

### Docguard ★ New (July 4)
The enforcement tool for Canonical-Driven Development (CDD) — audit, generate, and guard your project documentation. Zero-config documentation standards enforcement through MCP. ⭐19. Essential for engineering operators who want AI-generated docs to stay compliant with project standards. `github.com/raccioly/docguard`

### Planka V2 MCP ★ New (July 4)
Connect Claude, Cursor, Codex, and other MCP clients directly to your Planka v2.x boards. AI agents can read, create, and manage project management boards through natural language. Essential for operators using Planka for project management who want AI-assisted board operations.

### Drumbeats MCP ★ New (July 2)
Operate Drumbeats monitoring from any AI client — create cron/heartbeat monitors, triage incidents, and manage status pages via MCP. Essential for DevOps operators who want AI-driven uptime monitoring, incident response, and status page management. `github.com/drumbeats-io/mcp` · [Integration Guide](/hermes/mcp/servers/external/drumbeats-mcp/)

### Periscope MCP ★ New (July 2 PM)
63 Playwright-powered website testing tools with agent-first ergonomics — hard assertions, visual diffs, accessibility checks. Purpose-built for AI agent consumption. `npx -y periscope-mcp` · [Integration Guide](/hermes/mcp/servers/external/periscope-mcp/)

### dbridge MCP ★ New (July 2 PM)
Natural language SQL with security — read-only, column masking, row caps, query limits. AI agents query databases safely. `npx -y dbridge-mcp` · [Integration Guide](/hermes/mcp/servers/external/dbridge-mcp/)

### S3 MCP Connector ★ New (July 2 PM)
Amazon S3 (and S3-compatible) MCP — list, read, write, delete objects & buckets. Go binary, local or remote. `github.com/FerhatDundar/s3-mcp-connector`

### Assetzaar Marketplace ★ New (July 2 PM)
Marketplace for UI components, skills, and MCP tools — discover and integrate reusable agent capabilities and frontend components. `assetzaar.com/mcp`

### Bult.ai MCP Server ★ New (June 30)
Deploy and manage Bult.ai cloud hosting resources — projects, services, GitHub and Docker deployments via MCP. Cloud infrastructure management for AI agents. Essential for operators who want to manage cloud hosting through their AI toolchain. `mcpservers.org: bultcloud/mcp-server`

### CCHub ★ New (July 1)
Desktop app (Tauri + React + Rust) for managing Claude Code MCP servers, skills, plugins, hooks, and config profiles in one unified UI. Multi-profile management for complex setups. Essential for operators running multiple Claude Code environments across teams or projects who need centralized configuration management. `github.com/boxxapp23-pixel/cchub`

### Backengine MCP ★ New
Backend engine for MCP server development. Streamlines building and deploying custom MCP servers with pre-built infrastructure.

### Enigmata ★ New
Encryption, data privacy, and secure computing tools for AI agents. Provides cryptographic operations and privacy-preserving computation.

### Electron Stagewright ★ New
Drive, inspect, and assert on real Electron desktop apps from an AI agent. Agent-native, Playwright-style automation with accessibility refs, stable error codes, and retrying assertions. Essential for testing and automating Electron-based applications.

### Requesty MCP Gateway ★ New
Connect AI agents to 300+ LLM providers through a single MCP endpoint with built-in routing, caching, and observability. Essential for multi-model agent deployments.

### mcp-launch-review ★ New
Source-grounded launch review for x402, MCP, paid API, and agent-tool listings. Provides structured review and validation of MCP server deployments.

### TinyZKP ★ New
Hosted MCP server for transparent STARK proof receipts that agents can mint and verify for supported workflows. Post-quantum ready verification for agent actions.
### Bright Data ★ Sponsor
Discover, extract, and interact with the web  --  one unified interface powering automated access across the public internet. Enterprise-grade web scraping and data extraction.

### Reefapi ★ New
One MCP server connecting AI to 160+ live web-data APIs: search engines, social media (Reddit, TikTok, Threads, Bluesky), e-commerce (Amazon, eBay, AliExpress, Etsy), real estate (Zillow, Redfin), jobs, travel, news, and finance. Returns clean JSON from sites that block scrapers (captcha/anti-bot/login-walled/JS-heavy). One API key, one credit pool across all sources. Free tier available. Essential for operators who need multi-platform data intelligence.

### CheckMyVIN ★ New
Decode any VIN and check open NHTSA safety recalls directly in your AI assistant. Free, official US government data, no auth required. Two tools: `decode_vin` (full specs, recalls, maintenance from 17-character VIN) and `check_recalls` (open NHTSA recalls by make/model/year). Essential for fleet and logistics operators.

### Media Context Mcp ★ New
Give your AI assistant eyes and ears. Analyze any video, audio, or image entirely on your machine. Local processing — no cloud uploads. Essential for operators who need media intelligence without data leakage.

### Native Soil ★ New
Save your AI chat's working state (decisions, context, plan) and load it in any other model, client, or provider. Verified on save, secrets stripped. Essential for operators managing multi-model workflows.

### Apiany Mcp ★ New
APIAny offers a single OpenAI-compatible API gateway for leading LLM, image, video, and audio models. Compare pricing, read docs, start building production apps, agents, and workflows. Essential for operators managing multi-provider AI infrastructure.

### Mcp Json Validator ★ New
AI-powered self-healing JSON validator. Pay-per-call model. Essential for developers building JSON-heavy agent workflows.

### Agent Warden — MCP Audit Proxy ★ New (June 30)
Local MCP audit proxy — audit logs, policy enforcement, secret scrubbing, and emergency kill switch between Claude Code and any MCP server. Security layer for production AI agent operations. `github.com/yli769227-jpg/agent-warden`

### MCPscan — MCP Supply Chain Security ★ New (June 30)
Supply-chain security scanner for MCP servers & Claude Code projects — catch tool-poisoning, command injection, and risky package dependencies. Essential for operators deploying MCP servers in production. `github.com/glatinone/mcpscan`

### APIbase MCP Gateway ★ New (June 30)
Universal MCP gateway — 905 tools across 258 providers behind one endpoint. Pay-per-call with x402 USDC on Base. Operators can access hundreds of APIs through a single MCP server instead of managing dozens of individual integrations. `github.com/whiteknightonhorse/APIbase`

### Onlinecybertools MCP (280+ Tools)
280+ free dev/security tools in one MCP server: Base64/URL/JWT encoders, MD5/SHA/HMAC/bcrypt/argon2 hashes, JSON/YAML/XML formatters, regex tester, network diagnostics (ping/traceroute/dig/whois/SSL/SPF/DMARC), OSINT lookups. No auth, no API key.

### Cloudflare MCP ★ Official
Deploy, configure & interrogate Cloudflare resources (Workers/KV/R2/D1) from any MCP client.

### Chrome DevTools MCP ★ Official
Control and inspect a live Chrome browser from coding agents (Gemini, Claude, Cursor, Copilot). Official Google tool.

### DeepWiki by Devin ★ Official
Remote, no-auth MCP server providing AI-powered codebase context and answers.


### Lightbringer ★ New
Research and knowledge discovery tool for AI agents. Surfaces relevant research, papers, and domain knowledge across multiple sources.

### Roboselect360 ★ New
Humanoid robot intelligence and research data. AI agents can access robotics specs, benchmarks, and industry intelligence.

### WeatherAPI MCP ★ New
Weather data integration for AI agents. Real-time and forecast weather data accessible through MCP tools.

### AirLabs ★ New
Real-time flight tracking, airport schedules, delays, and reference data for airlines, airports, aircraft, and routes via the AirLabs API. Essential for travel and logistics operators.

### Channel3 Product Search ★ New
Product search and discovery engine via MCP. AI agents can search across product catalogs, compare specifications, and surface relevant products.
### Context7 MCP ★ Official
Up-to-date, version-specific library documentation and code examples injected into AI coding prompts.

### GitHub MCP ★ Official ★ New
Official GitHub MCP server for repository search, issues, pull requests, code context, and GitHub workflows. `npx -y @github/mcp-server`

### Google MCP Servers ★ Official ★ New
Collection of Google's official MCP servers. Centralized repository of Google's MCP integrations. `https://github.com/google/mcp`

### Supabase MCP ★ Official
Official Supabase MCP server for managing projects, databases, auth, storage, edge functions, and SQL workflows from AI agents. `npx -y @supabase-community/supabase-mcp`

### Just Publish ★ Official ★ New
Get your website online in seconds  --  just ask your AI assistant to publish it and Just Publish hands you a live link to share. No code, no setup, no hosting to figure out. Official MCP server for instant web publishing. Ideal for operators who need rapid landing pages, one-off sites, or quick web presence without dev overhead.

### Dawnguard ★ Official ★ New
Cloud security insights, guardrail guidance, and compliance checking via Dawnguard. Official MCP server for cloud security posture management from AI agents. Essential for operators managing cloud infrastructure who want AI-driven security monitoring and compliance verification.

### Scrapling MCP
High-performance Python web scraping via Playwright. Proxy support, captcha solving, intelligent navigation. Speed-optimized alternative to Playwright/Puppeteer.

### MCPg  --  Production PostgreSQL MCP ★ New
Safe-by-default PostgreSQL Model Context Protocol server for AI agents. Production-grade with guardrails. `https://github.com/devopam/MCPg`

### Next.js DevTools MCP ★ Official (Vercel)
Next.js development tools and utilities for AI coding assistants (Claude, Cursor). Debug, inspect, and optimize Next.js apps via MCP. Official Vercel tool.

### Proxyman MCP ★ Official
HTTP traffic inspection and debugging for AI agents. Create debugging rules, inspect network requests, and control Proxyman through natural language. Essential for API debugging.

### E2B ★ Official
Run code in secure cloud sandboxes hosted by E2B. Execute untrusted code safely, perfect for AI agents that need runtime environments. `npx -y @e2b/mcp-server`

### Serper MCP Server ★ New
Google Search API via Serper for AI agents. Fast, reliable web search with structured results  --  rankings, knowledge graph, and rich snippets. `npx -y @garymengcom/serper-mcp-server`

### Giteasy ★ New
Simplified Git operations through MCP  --  clone, commit, push, branch management without leaving your AI client. Streamlines developer workflows. `npx -y giteasy-mcp`

### Fastdomaincheck ★ New
Blazing-fast domain name availability checks via MCP. Check domain availability across TLDs for brand research, naming projects, and competitive intelligence. `uvx fastdomaincheck-mcp-server`

### MCP Advisor ★ New
Discover and install the right MCP servers for your needs. Acts as a meta-layer  --  search across mcp.so's 22,000+ servers and get installation recommendations from your AI client. `npx -y @xiaohui-wang/mcpadvisor`

### NLP Toolkit ★ New
Natural language processing tools for business text analysis  --  sentiment analysis, entity extraction, summarization, keyword extraction. Process documents, customer feedback, and market reports via MCP.

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
NEO MCP lets Claude Code, Cursor, and VS Code hand off complex AI engineering tasks  --  model evaluations, agent optimization, and more  --  to NEO's specialized infrastructure. Built for engineering teams scaling AI workflows.

### NWO Robotics ★ New
Multi-domain MCP server exposing 201 tools across 30 categories behind one endpoint. On-chain identity verification on Base Mainnet. Autonomous-agent infrastructure, hardware control, and crypto operations in one package.

### Primerfp Scout ★ New
Government contracting intelligence MCP for US federal + SLED contracting: semantic opportunity search, USASpending awards, recompete pipeline, congressional policy intel, GAO protests, and capture/teaming. 32 read-only tools via Streamable HTTP. `https://mcp.primerfp.com/mcp`

### chain-signer ★ New
Pre-signature security suite for AI agents operating on EVM chains. Flags wallet drains, permit-phishing, and risky actions before signing. Non-custodial protection layer for crypto-aware operators and DeFi automation.

### QA Skills ★ New
43 QA and test-automation skills for Claude Code, Codex, Cursor, and any Agent Skills Standard runtime. Full test-automation toolkit for operators who ship software.

### Tani ★ New
Agent-native hub (tani.ai)  --  AI agents discover capabilities in a trust-scored registry, exchange verified answers, and find each other. 12 MCP tools for capability resolution, agent registration, surface submission, and verified answer contribution. Registry ranked by computed invocation trust  --  success rate, dependents, and schema stability.

### SeedBase ★ New
Synthetic test data generation for databases. Generate realistic, FK-consistent test data from AI agents. List projects, get schema DDL, generate datasets as SQL. Ideal for operators who need test data without production exposure.

### StartupKit ★ New (June 28)
Agent-native MCP+CLI platform for business infrastructure — domain search, SEO analytics, keyword research, Google Trends, and app store intelligence. All-in-one business research toolkit for operators launching or scaling products. Combines domain availability, SEO metrics, keyword trends, and competitive app store data in one MCP server. Essential for founders, growth operators, and product managers. `github.com/01-studio/startupkit`

### Query Streams MCP ★ Official ★ New
Securely connect MCP clients to live databases through the Query Streams Cloud Network  --  no VPNs, inbound ports, or complex setup required. Official MCP server for database access from AI agents. Essential for operators who need AI agents to query, analyze, and work with production databases securely without exposing infrastructure.

### bruno-mcp ★ New
MCP server for creating, managing, and executing Bruno API testing collections. Supports both .bru and .yml (opencollection) formats with built-in security hardening. Ideal for operators who use Bruno for API testing and want AI agents to manage test suites, verify endpoints, and maintain API quality.

### BUILDY ★ New
Build real web apps on demand from ChatGPT, Claude, or any coding agent. Cross-agent compatible  --  build once and use the same app/data across different AI clients. `https://buildy.ai`

### Shinobi ★ New
Multi-agent task coordination MCP: shared task spine, decision log, and dead-ends ledger for every AI coding agent on your machine. Every failed approach is logged and semantically checked before an agent proposes a similar one  --  agents stop repeating mistakes across sessions. Mobile approvals, autonomous dispatch/swarm with N parallel agents in isolated git worktrees. Local-first SQLite over stdio or self-hosted streamable-HTTP. 39 tools, plugin system, MIT license. Works with Claude Code, Claude Desktop, Cursor, Cline, Continue.dev, Zed. Essential for operators running multi-agent coding workflows.

### Nahook ★ New
Manage and debug webhooks from your AI assistant. Test, inspect, and troubleshoot webhook endpoints without leaving your MCP client. Essential for operators building webhook-driven integrations and automation pipelines.

### Human Browser ★ New
Stealth cloud Chromium for AI agents  --  Patchright + Camoufox stealth engine, residential proxies, captcha solving behind one A2A endpoint. MCP server + stdio + remote HTTP. $1 free trial, pay-as-you-go. `npx -y humanbrowser`. Ideal for operators who need undetectable browser automation at scale.

### MCPApp MCP Server ★ New
Google Apps Script-based MCP network for Google Workspace  --  Gmail, Calendar, Sheets, Drive. MIT license, 49 GitHub stars, integrated with GASADK agent dev kit. Self-hosted on Google Apps Script. For operators who need lightweight, serverless MCP for Google Workspace without PortEden's enterprise firewall.

### Atlassian Rovo MCP Server ★ New
Atlassian remote MCP for Jira, Confluence  --  Streamable HTTP at `mcp.atlassian.com`. ⚠ SSE endpoint (`/v1/sse`) deprecates June 30, 2026  --  migrate to new endpoint. For operators running Jira/Confluence who want AI agents integrated with their Atlassian stack.

### ZenML MCP Server ★ Official ★ New
Official MCP server for ZenML MLOps/LLMOps pipelines. Read-only access + trigger pipeline runs. 30+ tools covering stacks, components, pipelines, runs, artifacts, models, deployments, and snapshots. Includes `diagnose_zenml_setup` for troubleshooting misconfigured environments. 46 GitHub stars. `pip install mcp-zenml`. Essential for operators running ML/AI pipelines on ZenML who want AI agents to manage and monitor their MLOps infrastructure.

### Lightrun MCP ★ New
Production debugging from AI agents  --  connect coding assistants to live runtime context without redeploying. Discover runtime sources, inspect live expression values, capture call stacks, measure execution duration, count executions, and collect numeric runtime metrics. Hosted at `https://app.lightrun.com/mcp`. Essential for operators who need AI-assisted production debugging with zero redeployment.

### Agent402 ★ Featured ★ New
Open-source, self-hostable MCP server with ~1,100 deterministic tools  --  web search, headless Chromium, PDFs, OCR, images, ~1,040 CPU utilities (hashing, JWT, unit conversions). x402 ecosystem: Find/Route/Leaderboard across all x402 sellers. Live data: SEC EDGAR, crypto, stocks, FRED macro, weather, geo. Agent memory with wallet-keyed KV + audit log. Free to self-host or pay-per-call. `npx -y agent402-mcp` or `https://agent402.tools/mcp`

### IPRout MCP Server ★ New
GeoIP and ASN intelligence for AI agents  --  country, city, timezone, network ownership, and ASN lookups. 2 tools: `lookup_ip` and `lookup_caller_ip`. Node.js 18+, IPRout API key. MIT license. `https://github.com/IProut2026/mcp-server`

### overreach ★ New
AI agent scope-creep auditor  --  audits code diffs against original task prompts, flags out-of-scope changes (new deps, env vars, endpoints, cron jobs, features). CI gate ready (GitHub Action). Severity-scored findings with `scope_creep_score`. `npx -y overreach`

### YPipe ★ New
Local AI desktop client + MCP orchestration engine  --  visual GUI or headless, Java-native, runs offline models on your own hardware with zero cloud routing. One-click MCP server installation, autonomous agent chains, model recommendation based on hardware. Cross-platform (Win/Mac/Linux). GitHub: `iunera/ypipe`

### Legacy Java to Microservices Refactoring ★ New
A community gateway to migrate legacy Jakarta EE monoliths into Spring Boot 3.4 microservices using AST parsing. Discovery gateway for a premium MCPize-hosted service. For Java enterprise operators modernizing legacy stacks.

### corelayer0 ★ New
Turn any OpenAPI spec into a hosted MCP server in 30 seconds. One typed tool per endpoint, server-side auth injection, stable URL across spec updates. EU-hosted, GDPR-native. Essential for operators who need to rapidly expose internal APIs as MCP tools without building custom servers.

### Pipetable ★ New
Register local data files as DuckDB views and let AI agents run real SQL against them. Files never leave the machine — results are ground truth, not generated. Zero data exfiltration. Essential for operators who want AI agents to query local CSV, Parquet, and JSON data without uploading to cloud services.

### Clutter ★ New
Synthetic data generator MCP server  --  19 tools for generating realistic companies, documents, and structured data. Ideal for populating SharePoint, test, and demo systems. Requires `CLUTTER_API_KEY`. Essential for operators who need realistic test data for AI agent development and system demonstrations.

### Syntitan ★ New
AI-Ready Data Platform MCP  --  bridge enterprise data management and AI execution. Connect Claude and other MCP clients to Syntitan's governed data layer that fills the missing layer between enterprise data systems and AI agents. Essential for enterprise operators building governed AI data pipelines.

### GTmetrix MCP ★ New (June 27)
Get web performance tests and data directly in your AI workflow. Analyze page speed, Core Web Vitals, and performance metrics from any MCP client. Official MCP server. `https://gtmetrix.com/blog/gtmetrix-mcp/`. Essential for operators monitoring site health, SEO performance, and user experience metrics.

### superserve-sandbox ★ New (June 27)
Create and control isolated cloud sandboxes from any MCP client. Each sandbox is a Firecracker microVM that boots in seconds — run shell commands, install dependencies, expose preview URLs, then pause or delete when done. Secrets brokered by platform, never passed through the model. `npx -y @superserve/mcp` or hosted at `mcp.superserve.ai`.

### web-pilot ★ New (June 27)
8 web tools in one MCP server: fetch any webpage as clean markdown, search the web, extract links/metadata/contacts, parse sitemaps and RSS feeds, batch-check URL statuses. Remote MCP at `https://poetic-rebirth-production-6e26.up.railway.app/sse`. Useful for operators building web-scraping or data collection agent workflows.

### Agent Guild ★ New (June 29)
A neutral, attack-resistant reputation and trust layer for autonomous AI agents. Lets an agent ask "who is the safest agent for this job?", vet any agent before delegating work or money, and vouch for completed work with cryptographic attestations. Essential for operators building multi-agent systems where agent-to-agent trust, delegation safety, and reputation tracking are critical.

### GGWP API Hub ★ New (June 29)
189 pay-per-call API endpoints covering Social Media, Jobs, Finance, Crypto, AI Tools, and more. Powered by x402 protocol with USDC payments on Base chain. MCP-native API marketplace that lets AI agents pay for and consume APIs on-demand. Essential for operators who want AI agents to access a wide range of paid APIs through a single MCP gateway with on-chain payments.

### Reqly ★ New (June 29)
API client built for AI agents. MCP tools for creating collections, running requests, chaining flows, mocking APIs, and exporting CI workflows. Zero cloud dependency — everything runs locally. Essential for operators building AI-driven API testing, integration, and development workflows. `github.com/RutvikPansare/reqly`

### Statewave ★ New (June 29)
Open-source state management and persistence layer for AI agents. MCP server enables AI assistants to store, retrieve, and manage structured state across sessions, workflows, and external systems through standardized MCP tools. Essential for operators building long-running, stateful AI agent workflows that need reliable persistence across sessions.

### Vynix MCP Server ★ New (June 29)
AI-powered website feedback, visual bug reporting, and website annotation MCP server. Connect AI coding assistants to Vynix to capture website feedback, create GitHub issues, access project data, and annotate websites directly from MCP clients. Essential for operators managing web development projects who want AI-driven QA and feedback loops.

### Version Pill ★ New (June 29)
Version management MCP server for AI agents — track and manage software versions, dependencies, and release cycles through standardized MCP tools. Essential for operators running software development workflows with AI agents.

### Mcp Midasflow ★ New (June 29 PM)
MCP server for AI agent data flow orchestration. Connect AI agents to data pipelines, automate data workflows, and manage data integration tasks through standardized MCP tools.

---

## Productivity

### Founders OS ★ New (July 4)
Open-source MCP server that puts your whole business inside Claude, Cursor, or any MCP client. Connects CRM, financials, tasks, and long-term memory behind one server, so you can ask a single question that reads across all of them. Example: "Which clients are behind on payments and what tasks do I have with them?" ⭐7. Essential for founders and small business operators who want a unified AI interface to their entire business. `github.com/OurThinkTank/founders-os`

### Coding Agent Project Management MCP ★ New (July 14)
Project management for coding agents — bugs, features, sprints, cross-tenant contracts. 71 MCP tools purpose-built for operators orchestrating AI-assisted development workflows across multiple agents and projects. Essential for engineering managers and agencies running AI coding agents at scale. · [Integration Guide](/hermes/mcp/servers/external/coding-agent-pm-mcp/)

### RadMail ★ New (July 4)
The email operating system for AI agents — searches your real inbox (sender/subject/content, ranked), surfaces a "Right Now" lane, tracks commitments, and drafts reviewable replies. No tool can auto-send money, change banking, or make irreversible decisions without human approval. Essential for operators drowning in email who want AI to triage, prioritize, and draft while keeping dangerous actions gated.

### Paigy ★ New (July 4)
Text, push, or call your phone when an AI agent needs input mid-task. Reply by voice instead of babysitting a long-running or blocked terminal. Essential for operators running long-running agent tasks who can't stay glued to a terminal waiting for human-in-the-loop prompts.

### Truepath Recorder ★ New (July 4)
A local MCP server that lets Claude, Cursor, or Codex drive TruePath Recorder — start/stop recordings, list capture sources, and get the saved file path back. Local bridge over 127.0.0.1 + per-launch token; recordings never leave your Mac. Essential for operators creating tutorials, bug reports, or documentation where AI-driven screen recording saves hours of manual capture.

### Niche ★ New
Editorial intelligence for creators and their agents  --  discover the stories worth writing about, rank the strongest angle, and draft grounded, platform-native posts. Content strategy MCP for operators running content marketing and thought leadership programs.

### Rendley MCP ★ New
Full video editor accessible via MCP. Create and edit video by describing what you want in the same chat you already work in. Essential for marketing and content operators who need AI-driven video production.

### onvela CRM ★ New
AI-first MCP CRM. Native MCP integration for customer relationship management. Essential for sales operators who want CRM operations directly in their AI workflow.

### FoundersOS ★ New
All-in-one operator OS for AI-native startup management — CRM, tasks, finances, feeds, and persistent memory for founders, delivered as an MCP server. Single MCP endpoint for the full founder toolkit: customer tracking, task management, financial dashboards, content feeds, and cross-session agent memory. Essential for solo founders and small startup teams who want AI agents to orchestrate their entire operational stack.

### Hirenimbus Mcp ★ New
Home Services MCP by HireNimbus  --  AI agents find, compare, and book verified local pros for handyman, renovation, HVAC, plumbing, electrical, and landscaping jobs in supported US metro markets. Essential for property managers, facility operators, and home service businesses.

### Obsidian Regulatory Mcp ★ New
Verified, tier-0 regulatory data for AI agents: connect Claude, ChatGPT, or Cursor to 850+ official sources across 50+ jurisdictions. Compliance-grade data for regulatory research, legal operations, and governance. Essential for operators in regulated industries (finance, healthcare, legal).


### Cal.com MCP Server ★ New (July 3)
Official Cal.com scheduling MCP — create event types, check availability, book meetings directly from AI agents. Remote endpoint at `mcp.cal.com`. Essential for operators who manage heavy meeting schedules and want scheduling to be agent-driven rather than dashboard-clicking. [Full integration guide →](/hermes/mcp/servers/external/calcom-mcp/)

### Granola MCP Server ★ New (July 3)
Official Granola meeting notes MCP — query meeting transcripts, extract action items, and search your entire meeting history from AI agents. Turns meeting notes into a queryable knowledge base. Essential for operators who want AI agents to answer "what did we decide about X?" from actual meeting records. [Full integration guide →](/hermes/mcp/servers/external/granola-mcp/)

### Microsoft Planner MCP ★ New (July 3 eve)
Connect AI agents to Microsoft Planner via Microsoft Graph API. Create plans, manage tasks, update buckets, assign work, and automate project workflows in Microsoft 365. Essential for enterprise operators on the Microsoft stack who want conversational task management. [Full integration guide →](/hermes/mcp/servers/external/microsoft-planner-mcp/)

### Mowgli MCP ★ New (July 3 eve)
Intelligent product canvas with MCP access — connect coding agents to iterate on product design, from sweeping flows to surgical component tweaks, and sync changes back to code. Built for product teams who want AI-driven design iteration without Figma exports. [Full integration guide →](/hermes/mcp/servers/external/mowgli-mcp/)

### Fixzi MCP Server ★ New
Issue tracking and bug fixing workflow automation via MCP. AI agents can create, track, and resolve issues programmatically.

### Cairn ★ New


### Church Website Editor ★ New
Design and edit church websites with ChatGPT or Claude via MCP. Provides AI agents with website editing capabilities for faith-based organizations.

Repo-native task graph as plain Markdown files, served to AI agents over MCP and to humans over a clean web UI. Combines project management with AI agent integration.

### Touchpoint ★ New
Give AI agent eyes and hands on any desktop — cross-platform accessibility API with MCP server. AI agents can interact with desktop applications through accessibility APIs.

### Remnus ★ New
Task management and workflow automation platform via MCP. AI agents can orchestrate multi-step workflows and manage task dependencies.

### Turbo Job Apply ★ New
AI-powered job search and application platform. Find jobs that are not ghost jobs — AI-assisted job matching and fast application via MCP.

### CreateWorker MCP ★ New (June 30)
Drive AI workers from Claude Code, Claude Desktop, Cursor, and other MCP clients. AI workforce orchestration — operators deploying fleets of AI workers can manage them through a single MCP server. `github.com/CreateWorkerAI/createworker-mcp`

### Cal.com MCP ★ Official
Connect AI clients to Cal.com scheduling. Hosted endpoint at `mcp.cal.com` or local instance.

### Chipp MCP ★ Official
Build, deploy, and monetize AI agents  --  "What Shopify did for ecommerce, Chipp does for AI agents."

### Plane MCP Server ★ New
Open-source project management (Plane.so) via MCP  --  6 tools for listing projects, creating and updating issues, managing assignees. Self-hosted, requires Plane.so API key. Smithery auto-install available. `npx -y @kelvin6365/plane-mcp-server`. Ideal for operators using Plane.so for project management.

### Karea ★ New
Extensive MCP tools so Claude Code, Cursor, and other MCP clients can create, edit, close, recap, and link dev tasks while coding. Jira linking, productivity recap. `npx -y karea-mcp`

### Unclick ★ New
Universal remote for AI: one MCP install gives any compatible agent 450+ callable endpoints across 60+ integrations, plus persistent cross-session memory. Like Zapier for AI agents. Ideal for operators who want a single MCP that covers hundreds of APIs. `npx -y unclick-mcp`

### FileToPDF ★ Official ★ New
Convert files (DOCX, XLSX, PPTX, images), HTML, and Markdown to pixel-perfect PDFs. npx stdio or hosted Streamable HTTP. Free API key in one click. Essential for operators generating reports, invoices, and documents programmatically. `npx -y @filetopdf/mcp`

### MindMeister MCP ★ Official ★ New
Create, edit, and organize mind maps from any AI assistant. Remote hosted MCP at `mcp.mindmeister.com/mcp`. Visual brainstorming and knowledge mapping via MCP. Streamable HTTP transport.

### MeisterTask MCP ★ Official ★ New
Create and manage projects, tasks, and notes from AI assistants. Remote hosted at `mcp.meistertask.com/mcp`. Full project management  --  from the creators of MindMeister. Streamable HTTP transport.

### HomeLab Monitor ★ New
Read-only MCP server for self-hosted homelab dashboards  --  explore hosts, Docker containers, GPU/VRAM, systemd services, AI models, alerts, and disk. `https://github.com/SikamikanikoBG/homelab-monitor`

### Wikimint ★ New
Knowledge management and wiki tools via MCP. Create, edit, and query structured knowledge bases from AI clients. Ideal for operators building internal knowledge repositories.

### Flomo MCP Server ★ New
Connect AI agents to Flomo notes for knowledge management. Capture ideas, meeting notes, and research directly into your Flomo workspace from any MCP client. `npx -y mcp-server-flomo`

### Smart Match ★ New
AI-powered job matching and application tracker. Analyze job listings against your resume, get a match score (0-100), identify skill gaps, generate cover letters, and track your application pipeline. Ideal for recruitment operators and job seekers.

### Capafy ★ Sponsor ★ New
Marketplace for monetizing agent skills as products. On Capafy, your Skill runs online 24/7 as an agent product, and you get paid every time someone uses it. The "App Store for agent skills"  --  build once, earn continuously.

### Progi ★ New
MCP-native workflow engine for your AI harness. Progi teaches your agent how you like to get things done  --  so you can do your best work without re-explaining your process or losing context between sessions. Workflow automation for operators with repeatable business processes.

### PDFGate ★ New
Generate documents, process PDFs, and manage e-signature workflows using the PDFGate API. Document generation and signing MCP for operators handling contracts, proposals, and agreements at scale.

### ProposalCraft ★ New
MCP server that drafts winning client proposals in your own voice  --  no API key, runs locally in Claude Desktop. Essential for consultants, agencies, and B2B operators who write proposals regularly.

### Collaboard MCP Server ★ New
Create, search, analyze, and transform whiteboards into visual, collaborative workspaces. The Collaboard MCP Server lets AI assistants build and manage visual collaboration spaces. Ideal for operators running remote workshops and strategy sessions.

### DevMatch ★ New
AI recruiting for mission-aligned engineers  --  verified across GitHub, X, YouTube, Medium, and more. MCP-native technical recruiting for operators building engineering teams.

### Feedback Synthesis MCP ★ New
Synthesize customer feedback from GitHub Issues, Hacker News, and App Store  --  extract pain points, sentiment trends, and search feedback via x402 micropayments. Customer intelligence MCP for product operators.

### Docsie ★ New
Create, manage, and publish documentation, convert videos to docs, run compliance analysis, and search your knowledge base  --  all from your AI assistant. Documentation ops MCP for operators managing product docs.

### Historis ★ New
Shared timeline that keeps you and your AI never out of sync. Everything lands in one timeline, linked to the right people. Ask for the brief: what happened, what you should know, what needs handling. Team context MCP for operators managing distributed work.

### Scrivener MCP ★ New
Connect Scrivener 3 writing projects to Claude, ChatGPT, and other AI assistants. 60+ tools for manuscript management, writing analysis, semantic search, character/plot memory, and content enhancement. Essential for operators who produce long-form content, documentation, or books.

### OneCal Calendar MCP ★ New
Multi-calendar MCP server  --  connect Google Calendar, Outlook Calendar, and iCloud Calendar through one secure server. AI assistants can read schedules, check availability, create/update/delete events. OAuth with granular scopes (read only, or full read-write). `https://mcp-server.onecal.io/mcp`. Essential for operators managing multi-platform calendars.

### Appflowy MCP ★ New
Self-hosted AppFlowy Cloud access via Docker with token-scoped, tree-shaped access control. List workspaces, navigate page trees, create/update/read pages, edit individual blocks via Yjs/CRDT. Service account + per-client Bearer tokens. Docker image: `m2n2/appflowy-mcp`. For operators who self-host AppFlowy and want AI access with fine-grained permissions.

### Atlassian Confluence MCP ★ New
Open-source MCP server for Atlassian Confluence that lets AI assistants read, create, search, and manage Confluence wiki pages. Works with Confluence Cloud, on-premise Server, and Data Center deployments. Connect your AI coding agent to your team's knowledge base via npx. Essential for operators with Confluence-based documentation workflows.

### Muxara ★ New
Online video conversions via API  --  convert videos between formats directly from your AI agent. Lightweight video processing MCP for operators who need quick format conversions without heavy video editing tools.

### InfraNode ★ New
Free, keyless MCP server for open data across 84 German cities: weather and DWD warnings, air quality, transit, traffic, water levels, energy/SMARD. 38 tools, Apache 2.0 licensed. Zero authentication required  --  ideal for operators building location-aware AI applications or needing German infrastructure data for logistics, planning, and environmental monitoring.

### ProductNow ★ New
Product management and roadmap MCP — define features, track progress, and align stakeholders through AI-powered product workflows

### Process Street MCP Server ★ New
Connect AI agents to Process Street workflows, tasks, runs, datasets, and form fields via a hosted OAuth endpoint. Trigger compliance checklists, standard operating procedures, and recurring business processes directly from AI agents. Essential for operators who run Process Street for team workflows and process automation.

### Numbers Online  --  Phone Intelligence ★ New
Hosted, read-only MCP server for AI voice agent phone intelligence  --  caller identity, risk scoring, line type, DNC check. Every billable answer carries an Ed25519-signed receipt. No raw phone numbers stored (hashed only). Remote/hosted: nothing to install.

### AgentDocs ★ New (June 27)
An agent-first office suite your AI reads and writes over MCP — Docs, Sheets, Slides, a Database, Drive, and Notion-style Pages. Sign in with Google; free to start. Remote MCP at `https://getagentdocs.com/mcp`. Essential for operators who want AI agents to create, edit, and manage office documents without leaving their chat interface.

### Formly ★ New (June 29)
Create, edit, and publish Formly forms from any AI agent — Claude, Cursor, Codex, ChatGPT — in plain language. Formly's AI designs the form structure for you. Essential for operators who need to quickly deploy forms (surveys, lead capture, registrations) through AI agents without manual form builders.

### MemPlato ★ New (June 29)
Personal MCP server that runs on your Android phone via Termux. 29 tools: drawers, knowledge graph, diary, semantic search, tunnels. All data stored locally on your device — never on external servers. Works with Claude, Perplexity, Cursor, Windsurf, VS Code, Zed. Essential for operators who want a private, personal MCP server on mobile for knowledge management and AI workflows.

---


### Pixelvault ★ New
Digital asset and image management platform for AI agents. Store, retrieve, and manipulate visual assets through MCP.

### OnBrand by SlideSpeak ★ New
Feeds AI agents your brand's real logos, colors, fonts, and approved slide layouts, so every deck and document comes out on brand the first time. Essential for brand-conscious operators.

---

## Communication

### PostAgent ★ Official ★ New
Print and send physical mail and postcards to US addresses (USPS), paid per call in USDC on Base via x402 or credit card. Official MCP server for physical mail automation  --  essential for operators who need to trigger postal mail from AI workflows.

### VoIP.ms MCP ★ New (July 2 PM)
Business telephony MCP — phone numbers, SMS, voicemail, fax, call flows, and billing for AI agents. Scope-based tool access. First MCP server for business phone systems. `npx mcp-remote https://voipms-mcp.ecliptical.io/mcp` · [Integration Guide](/hermes/mcp/servers/external/voipms-mcp/)

### Document To Json Pdf Parser ★ New
Convert PDF documents (invoices, contracts, statements) to structured JSON — parse, extract, and transform PDFs into agent-readable data

### Minddory Com Connect ★ New
Mind mapping and knowledge organization tool — create, navigate, and query visual knowledge graphs and mind maps

### Penqwin ★ New
AI productivity assistant and workflow automation — task management, scheduling, and intelligent workflow optimization

### Turbojobapply Com Mcp ★ New
Automated job application and resume optimization — search jobs, tailor resumes, and submit applications through AI agents

### Granola MCP ★ Official
AI-powered meeting notes and summaries. Connect your meeting data to AI agents.

### Plaud MCP ★ Official ★ New (July 4)
Connect Plaud.ai recordings to AI agents. Search recordings, read transcripts, generate summaries and documents. Essential for operators who record client calls, team meetings, and partner conversations. [Integration Guide](/hermes/mcp/servers/external/plaud-mcp/) · `docs.plaud.ai`

### Superlist MCP Server ★ Official
Task and project management via MCP. Connect AI agents to your Superlist workspace.

### KaiCalls ★ New
AI phone secretary for businesses  --  place outbound calls, read transcripts, manage voicemails, send/receive SMS, and access analytics from your business line via MCP. Essential for operators who want AI agents to handle phone-based customer interactions, lead qualification, and communication workflows without a human receptionist.

### Shipmail MCP ★ New
Business email MCP server for AI agents  --  custom-domain inboxes, REST API, webhooks, send, read, and reply tools. Purpose-built for AI agents to handle business email workflows including transactional notifications, customer communications, and inbox management with custom-domain professionalism.

### SendGrid MCP ★ New (June 30)
SendGrid email delivery via MCP. AI agents can send transactional emails, manage templates, and track delivery metrics. Essential for operators who need AI-driven email delivery without building custom integrations. `mcpservers.org: neschadin/sendgrid-mcp`

### Onboard MCP ★ Official ★ New
Connect your AI assistant to Onboard to monitor live onboarding projects, surface blocked tasks and risks, draft customer emails, and take action on tasks with role-based access and preview-first safety. Essential for operators managing customer onboarding workflows  --  keeps AI agents aligned with real project state. Official MCP server with Streamable HTTP transport.

### Sendmux Email MCP ★ Official ★ New
Email inbox and sending API purpose-built for AI agents. Sendmux provides transactional email sending, inbox management, and email operations via MCP. Official MCP server  --  essential for operators who want AI agents to handle email workflows (notifications, transactional emails, inbox automation) without building custom integrations. Streamable HTTP transport.

### Mcp Emails ★ New
Multi-inbox email management for AI agents via MCP. Read, search, send, organize, draft, and schedule email across your inboxes from any MCP client. Purpose-built for operators managing multiple email accounts who want AI agents to handle email triage, response drafting, and inbox organization across all accounts from a single interface.

---

## Content Creation & Creative

### Pepys MCP ★ New (July 4)
Pay-as-you-go audio and video transcription with diarization + AI. Transcribe, podcast feeds, SRT/VTT export, search — BYO key or hosted OAuth connector. Never trains on your audio. Essential for content operators, podcasters, and media teams who need AI-driven transcription and content extraction from audio/video files through their existing MCP workflow.

### EverArt ★ New
AI image generation via MCP. Generate marketing visuals, social media assets, product mockups, and creative content from any MCP client. Official integration with EverArt's FLUX and SD models. `docker exec -i mcp-node bash -c "EVERART_API_KEY=*** npx -y @modelcontextprotocol/server-everart"`

### SuperMaker AI ★ New
AI-powered content creation platform for video and image generation. Create marketing assets, product demos, and social content programmatically through MCP. Ideal for operators scaling content production.

### Scenext ★ New
AI educational video generation platform. Generate high-quality explainer and tutorial videos from question-answer pairs. MCP-native for automated video content pipelines.

### Rendley Mcp ★ New
Full video editor for AI agents  --  describe what you want and Rendley creates/edits video using your footage, brand kit, and AI tools. MCP-native video production. Essential for content operators who need AI-driven video editing without leaving their chat interface.

### MediaMCP ★ New (July 2 PM)
Media generation via OpenRouter or any OpenAI-compatible API — create and edit images, generate video from AI agents. `npx -y mediamcp` · `github.com/legolev/mediamcp`

### MiniMax MCP ★ Official ★ New
Official MiniMax MCP server for powerful TTS (Text-to-Speech), image generation, and video generation APIs. Create voiceovers, marketing visuals, and video content directly from AI agents. `npx -y @minimax/mcp`

### Vidoly AI ★ New
AI image & video generation for social media, branding, ecommerce, and digital content. Use Vidoly AI to generate images, create videos, and streamline visual production from any MCP client. Streamable HTTP.

### Blog2Video ★ New
Convert blog URLs to video in under 3 minutes via MCP. Turn written content into video assets for social media and marketing pipelines without leaving your AI client.

### Powerdmarc Mcp ★ New
Email security and DMARC compliance MCP  --  monitor domain email authentication (SPF, DKIM, DMARC), detect spoofing, generate forensic reports. Essential for operators who need AI-driven email security monitoring and domain protection.

### Unspam MCP ★ New
Email deliverability and spam testing MCP  --  inbox placement checks, spam score analysis, screenshot previews, heatmaps, and autopilot deliverability tests. OAuth authentication, no API keys needed. Essential for email marketers and operators managing outreach campaigns.

### mcp-ads ★ New
MCP for ads platforms — connect AI agents to advertising APIs for campaign management, performance analysis, and optimization across ad networks.

### Valossa Assistant ★ New (June 29)
Multimodal video AI MCP server built on a decade of video understanding. Goes end-to-end: ingest a video, understand its content multimodally (visual + audio + text), and produce structured outputs. Unlike video MCPs that stop at search or analysis, Valossa processes video from ingestion to structured intelligence. Essential for operators working with video content at scale — media monitoring, content analysis, compliance review. `valossa.com`

---

## Design & Product

### Mowgli MCP ★ New (July 3)
Intelligent product canvas with context and taste — connect your coding agent to iterate on product design, from sweeping new flows to surgical tweaks, and sync back to code. [Integration Guide](/hermes/mcp/servers/external/mowgli-mcp/) · `app.mowgli.ai/mcp`

### Design Context Bridge MCP ★ New (July 4)
Turns AI agents into frontend developers that read Figma files natively — components, design tokens, routes, icons, states. Faithful design-to-code, not screenshot guessing. [Integration Guide](/hermes/mcp/servers/external/design-context-bridge-mcp/) · `github.com/CristinaFores/design-context-bridge`

### DesignForYou ★ New
Generate finished, on-brand designs — logos, social posts, app-store screenshots — from a prompt. Remote MCP server backed by 119 templates.

---

## Manufacturing & Hardware

### Bambu Printer MCP ★ New (July 1)
Control Bambu Lab 3D printers, edit STL files, and manage 3MF print workflows via MCP. AI agents can start prints, monitor progress, edit models. Compatible with Bambu CLI, Bambu Studio, Klipper, OctoPrint, Moonraker, and other 3D printing ecosystems. Essential for manufacturing and prototyping operators with Bambu Lab printers who want to automate print workflows through AI agents. Niche but growing — Bambu Lab is the fastest-growing 3D printer brand in consumer and prosumer markets. `github.com/offthehook-implication870/bambu-printer-mcp`

---

## Marketing

### OpenAI Ads MCP Server ★ New
OpenAI Ads and ChatGPT Ads MCP server for the OpenAI Advertiser API  --  typed tools for campaigns, creatives, audiences, and insights. Advertising campaign management for operators running paid acquisition on OpenAI/ChatGPT platforms.

### Google Ads MCP Server ★ New (June 30)
Standalone MCP server for Google Ads — campaign management, performance data, keyword analytics, and ad optimization directly from AI agents. Lightweight alternative for operators who only need Google Ads access without a full 37-platform suite. `github.com/smileCompiler/google-ads-mcp-server`

### Google Ads MCP (Open Source) ★ New (July 1 PM)
Free, open-source MCP server (57 tools) connecting Google Ads to Claude, Cursor, Windsurf, and any MCP client. Campaign management, keyword optimization, GAQL querying, and competitive analysis via natural language. MIT license, no vendor lock-in. `github.com/yusofansari/google-ads-mcp`

### Google Search Console MCP (Open Source) ★ New (July 1 PM)
Free, open-source MCP server (43 tools) connecting Google Search Console to Claude, Cursor, Windsurf, and any MCP client. Search analytics, indexing checks, cannibalization detection, and sitemap management via natural language. MIT license. Essential for SEO operators who want GSC data in their AI workflows without paid tools. `github.com/yusofansari/google-search-console-mcp`

### Podcast Sponsorship Discovery MCP ★ New (July 14)
Find brands that sponsor podcasts like yours, then reveal the buyer to pitch — by name and email. Detected from 4M+ podcast sponsorships, updated daily. Essential for sales and marketing operators who need direct lead generation from podcast advertising intelligence. · [Integration Guide](/hermes/mcp/servers/external/podcast-sponsorship-mcp/)

### ShortsMonkey YouTube Outlier Research MCP ★ New (July 14)
Find YouTube outliers, daily viral Shorts, and analyze video performance. Content strategy tool for video-focused operators. INDEX ONLY.

### Zooq ★ New
LinkedIn data API and MCP server for AI agents. Public profiles, companies, and posts as clean JSON — no login, no cookies, no browser automation. 300 free credits on signup. Pay-as-you-go credit billing. Endpoint: `https://zooq.dev/api/mcp`. Essential for sales and recruiting operators who need LinkedIn intelligence.

### Rampify ★ New
SEO MCP server: crawl your site, find AI-visibility gaps (GEO), and ship the fix from your coding agent. Combines traditional SEO audit with AI-engine optimization (AEO). Essential for marketing operators managing AI discoverability.

### Webotee Amazon MCP Server ★ New (July 3)
Amazon seller intelligence MCP — product research, buy-box history, competitor analysis, niche discovery. Built for Amazon sellers and ecommerce operators. Research products and discover under-competed niches directly from AI agents. [Full integration guide →](/hermes/mcp/servers/external/webotee-amazon-mcp/)

### OpenTweet MCP Server ★ New (July 3)
X/Twitter management MCP — compose, schedule, publish tweets and threads; search content; analyze engagement. Complete X presence management from AI agents. Essential for marketers and operators who manage X/Twitter as their primary social channel. [Full integration guide →](/hermes/mcp/servers/external/opentweet-mcp/)

### viral.app ★ New
API-powered MCP server for UGC marketing analytics, creator tracking, campaign reporting, and agent workflows. Analyze user-generated content performance and creator ROI directly from AI assistants.

### Influee MCP ★ New
Run influencer marketing campaigns on Influee platform from AI agents. Campaign setup, creator matching, performance tracking, and payment workflows. Essential for brands managing influencer partnerships.

### MillionPhones ★ New
Verified B2B direct dials. AI agents get access to phone-verified contact database for outbound sales. Essential for sales operators building prospecting workflows.

### SE Ranking MCP ★ New
Live access to SE Ranking's SEO and AI search data  --  keyword research, backlinks, domain analysis, site audits, and AI search visibility (180+ tools). MCP-native SEO platform for operators who need comprehensive search intelligence in their AI workflows.

### PPXC Find Customers ★ New
Turn short-video comments into ranked customer leads, keyword ideas, and outreach scripts. Lead generation MCP for operators who source customers through social video platforms (TikTok, YouTube Shorts, Instagram Reels).

### Eclincher ★ New
Publish, schedule, moderate your social inbox, and pull analytics across every major network directly from any AI assistant. Full social media management MCP  --  competes with Zernio and Solnk for AI-driven social operations.

### MentionsAPI ★ New
Check whether AI recommends your brand  --  mentions, ranks & citations across ChatGPT, Claude, Gemini, Perplexity, AI Overviews, AI Mode & Bing Copilot. Essential GEO/AI visibility monitoring for operators investing in AI-engine discoverability.

### NotHumanSearch ★ New (June 30)
Search engine for AI agents — ranks sites by agentic readiness (llms.txt, OpenAPI, MCP, ai-plugin). MCP server + REST API + full-text search. New "agentic SEO" category — operators need to understand how AI agents discover and rank their sites. `github.com/unitedideas/nothumansearch`

### Geoly GEO MCP ★ New (June 30)
Remote MCP server + geoly-mcp skill for AI brand visibility (GEO) reporting. Track how AI models mention and recommend brands. Competitive with MentionsAPI for AI-engine discoverability monitoring. `github.com/geoly-ai/codex-plugins`

### getAdvantage MCP ★ Official ★ New
Scan how ChatGPT and Claude read your app, see who they name instead of you, and get paste-ready fixes (llms.txt, JSON-LD, FAQ, meta) to get found. GEO/AI SEO optimization tool  --  directly competitive with MentionsAPI for AI-visibility monitoring. Essential for operators who need their products discovered by AI agents. Official MCP server.

### Demo Magic ★ Official ★ New
Guides for making interactive videos & AI product demos that answer viewers' questions. Turn product walkthroughs into AI-interactive experiences. Official MCP server for marketing teams building interactive demo assets  --  ideal for operators launching products who need demo content that scales.

### Webotee Amazon MCP ★ Sponsor ★ New
Amazon brand, seller & niche intelligence in your own Claude or ChatGPT  --  buy-box history, competing sellers, and under-competed niches. Research built for sellers. Essential for ecommerce operators on Amazon.

### NameSniper MCP ★ New
Check brand name, domain, and social handle availability  --  then snipe the taken ones the moment they drop. Brand identity MCP for operators launching new products, rebranding, or securing digital presence.

### Zernio MCP ★ Official ★ New
Social media scheduling platform  --  manage and publish content across all major platforms from a single API. MCP-native. `https://docs.zernio.com/mcp`

### FeedSquad ★ New
Content calendar and social publishing for Claude and ChatGPT agents. Create posts and campaigns, schedule with cadence guardrails, and publish to LinkedIn, X, and Threads. OAuth 2.1 authentication. Anti-slop pattern registry checks all drafts before scheduling. Approval-first workflow  --  nothing goes live without explicit approval.

### Convika - LP ops ★ New
Landing page ops platform built for MCP clients. Create, preview, and publish landing pages with forms, analytics, custom domains, and version history. OAuth 2.1. `https://mcp.convika.com`

### Versium Reach ★ New
Lead enrichment and audience building for AI agents. Describe what you need and Versium REACH builds and sizes B2B/B2C audiences, fills in contact and company data, and verifies emails. All through natural language.

### Sendpulse MCP ★ New
Full marketing platform via MCP  --  email campaigns, CRM, chatbots, SMTP, and online courses. 134 methods across 5 categories. `npx sendpulse-mcp`

### Solnk MCP ★ New
Social media management for 9 networks  --  Instagram, TikTok, YouTube, X, LinkedIn, Pinterest, Facebook, Threads, Bluesky. Draft-first safety model with team approval workflow, content calendar, and analytics. MCP server for AI agents to draft and publish posts from a single interface. `https://solnk.com`

### Periodix Actions ★ New
Search LinkedIn & Sales Navigator. Get structured people, companies, posts, jobs data. 4.9/5 on G2. MCP-native B2B sales intelligence for operators who prospect through LinkedIn.

### SEOcrawl AI ★ New
SEO + GEO MCP: live Google Search Console data, keyword and page analysis, site audit and SEO tasks  --  21 tools. Essential for operators who need AI-driven SEO and AI-engine visibility (GEO) in one package.

### Feedoptimise AI Feed Agent ★ New
Audit product feeds, diagnose Google Merchant Center disapprovals, run imports and syncs, and manage product exports across Google Shopping, Meta, Amazon, TikTok and more. Multi-channel commerce feed management for ecommerce operators.

### Assay Truth Graph MCP ★ New
Remote MCP server that grounds GTM agents in governed, cited company truth. Eliminates hallucinated company data in sales and marketing workflows. Essential for operators running AI-driven GTM motions.

### Toksta MCP Server ★ New
B2B creator intelligence MCP  --  search, enrich & score LinkedIn/YouTube creators for campaigns. Creator discovery and vetting for influencer marketing operators.

### Adology AI ★ New
Perplexity for social: ask what competitors are running across social and get answers grounded in real ad and creative data, not guesses. Competitive ad intelligence MCP for marketing operators.

### IndustryLens ★ New
Browse cited competitive-intelligence reports and head-to-head competitor comparisons from any MCP-aware AI agent  --  live B2B SaaS data, sources included. Competitive intelligence MCP that operations teams can query directly.

### GSC Wizard MCP ★ New
Your AI assistant can query Google Search Console analytics. Dedicated GSC MCP for SEO operators who want Search Console data in their AI workflows.

### auto-geo ★ New ★ Official
GEO optimized content publishing engine for AI visibility. Official MCP server. Publish content optimized for AI engine discovery  --  essential for operators investing in GEO (Generative Engine Optimization).

### Orcool Studio MCP ★ New
AI video ad production for GTM-engineers & growth teams  --  107 tools for UGC concepts, AI avatars, Veo 3 video rendering, and performance feedback. Full-stack video ad production MCP.

### Local AI Visibility ★ New
Free, no-signup MCP that checks whether AI assistants name a local business when prospects ask "who's the best in town?"  --  returns a Share-of-Model score, competitors named, GEO/AEO checklist, and buying-intent prompt generator.

### Forward ★ New
Get customers, pay per verified result  --  agents buy qualified leads, meetings, SEO content, and ad conversions; self-provisioning signup with $25 free credits. Pay-per-result customer acquisition for growth operators.

### HYPD.AI ★ New
Enable AI agents to create, manage, and optimize advertising campaigns on ChatGPT. MCP-native ad campaign management for operators running paid acquisition through AI toolchains.

### Etymolt ★ New
Signed trademark, domain, cultural, sound-symbolism, and pronunciation verdicts for brand names. Brand validation MCP for operators launching new products or rebranding.

### SEOforGPT MCP ★ New
AI visibility (GEO) MCP for agencies and marketing teams  --  audit brand visibility in AI-generated answers across 15 models, monitor competitors and cited sources, fix GEO gaps. 15 tools: visibility reports, trends, competitor intelligence, client briefs, website readiness, CMS publishing. OAuth, Streamable HTTP at `https://www.seoforgpt.io/mcp`. Essential for operators investing in AI-engine discoverability.

### SyncGTM ★ New
B2B leads and enrichment MCP  --  verified emails, phone numbers, LinkedIn data, and buying signals. 20+ tools with full workspace context awareness. OAuth browser sign-in, no API token to manage. `https://api.syncgtm.com/mcp`. Essential for sales operators who prospect through AI agents.

### Adsumo ★ New
Generate on-brand image and video ads from AI agents. 24 tools  --  brand/product setup from URL or image, image ad generation in any ratio, AI video ads (Seedance, Sora 2, Veo 3.1, Kling 2.6), competitor ad research, credit/plan management. OAuth, Streamable HTTP. `https://www.adsumo.ai/api/mcp`. Essential for operators scaling ad creative production.

### Domain Deliverability Checker ★ New
Email domain DNS deliverability scoring for AI agents  --  checks SPF, DKIM, DMARC, MX records, blacklist lookups, domain age, and produces a 0-100 composite score. `mammalabsdev/mcp-domain-deliverability-checker`. For email marketing operators monitoring deliverability health.

### Poppify Studio ★ New
Photo-to-reel MCP for solo founders and SMBs. Upload 1–10 photos and get a captioned vertical reel for Instagram, TikTok, YouTube Shorts, or Facebook  --  with motion, library-matched music, and optional AI voiceover. Content creation MCP for operators who need social video without video editing skills.

### Spimov AI Video Dubbing ★ New
Dub any video into 600 languages straight from your AI chat  --  YouTube dubbing and voice cloning via MCP. Global content distribution MCP for operators expanding content across language markets.

### MewCP Google Business MCP ★ New
Hosted, stateless, multitenant Google Business Profile MCP  --  manage business listings, reviews, locations, and customer interactions through Google Business Profile. Essential for local business operators and multi-location brands who want AI agents to manage their Google presence, respond to reviews, and update business information.

### Serpzilla ★ New (June 26)
MCP server for Serpzilla  --  purchase SEO placements (links, articles, reviews) on publisher sites. Manage projects, search sites by metrics, and track placements via OAuth-secured API. Remote MCP at `mcp.serpzilla.com/mcp`. Essential for SEO operators and agencies managing paid link-building and content placement campaigns through AI agents.

### Sociality MCP ★ New (June 27)
Social media analytics, post insights, and competitor benchmarking for AI agents. Connect AI with social media intelligence across Facebook, X (Twitter), Instagram, YouTube, LinkedIn, and TikTok. Remote MCP at `https://api.sociality.io/mcp`. Essential for marketing operators who need cross-platform social analytics and competitor monitoring in their AI workflows.

### AdMob MCP ★ New (June 29)
Google AdMob management, mediation waterfall operations, advanced revenue analysis, and A/B experiments — all directly accessible to MCP-compatible AI clients (Claude Desktop, Cursor, Windsurf, etc.). First MCP server for mobile ad monetization. Essential for operators running mobile apps who want AI-driven ad revenue optimization. `github.com/AbhishekDhobe/admob-mcp`

---


### LinkDeal MCP ★ New
Find warm LinkedIn leads via AI — enrich contacts, unlock comments, and deliver to Slack. B2B lead generation MCP for sales operators who prospect through AI agents. Essential for operators building AI-driven outbound sales workflows.

### AppSigma App Store Data MCP ★ New (July 2)
Full public App Store search results as users see them — rankings, reviews, ASO keywords, sponsored slots, charts, and app analytics. iPhone app growth teams can research competitors, track keyword rankings, and analyze reviews directly from AI agents. Essential for mobile growth operators and ASO teams. `appsigma.io` · [Integration Guide](/hermes/mcp/servers/external/appsigma-app-store-data-mcp/)

### Userbrain MCP ★ New (July 2)
User testing analytics via MCP — explore test session data, summarize participant feedback, identify pain points, and surface UX insights. Product teams can query usability test results without manually watching recordings. Essential for UX researchers and product operators. `userbrain.com` · [Integration Guide](/hermes/mcp/servers/external/userbrain/)

### NaturalMelo MCP ★ New (July 2)
AI content detection with naturalness scoring and AI-template pattern flagging. Content teams can audit AI-assisted writing before publishing — verify output reads authentically rather than like generic LLM content. Essential for content operators managing AI-assisted content pipelines and SEO quality. `github.com/carter-wzq/naturalmelo-mcp` · [Integration Guide](/hermes/mcp/servers/external/naturalmelo-mcp/)

---

## Memory & Knowledge

### Persistent Memory for Coding Assistants MCP ★ New (July 14)
Persistent memory and cross-session learning for AI coding assistants. Cloud-based context management via MCP. Redundant category (3+ memory MCPs already catalogued). INDEX ONLY.

### Cortex Memory MCP ★ New (July 4)
Structured memory layer for AI agents — persistent knowledge storage with retrieval and context management. Provides AI agents with long-term memory capabilities across sessions. Essential for operators building stateful AI agent workflows that require memory persistence.

### Psychopathia Machinalis MCP ★ New (July 4)
Read-only MCP tools over the Psychopathia Machinalis nosology — 79 conditions across the AI-psychopathology taxonomy, via 11 tools. Zero-install hosted endpoint available. Niche but notable for AI safety researchers and operators running agent evaluation/red-teaming pipelines.

### Astucia Wiki MCP ★ New (July 4)
AI-enabled team wiki with semantic search, auto-organization, and MCP-native read/write access. Built from the ground up for AI agent consumption — finally, a wiki your agents can actually query and update. [Integration Guide](/hermes/mcp/servers/external/astucia-wiki-mcp/) · `astucia.wiki`

### Anki MCP ★ Official
Enable AI assistants to interact with Anki spaced-repetition flashcards.

### XMemo
Persistent memory for AI agents across sessions.

### Vault Cortex ★ New
MCP server for Obsidian vaults  --  search, memory, link graph, 23 tools, OAuth-protected. Connect AI agents to your Obsidian knowledge base. Ideal for operators who use Obsidian as their second brain.

### Frinus ★ New
MCP server exposing 70 tools spanning cognitive memory, working memory, sessions, agents, the L0–L3 knowledge hierarchy, orchestration tasks, and training pipelines. Speaks stdio, consumed by Claude Desktop, Claude Code, OpenCodex, and any MCP-aware client. Enterprise-grade AI memory infrastructure for operators building knowledge-intensive agent systems.

### Agent Magnet ★ New
Self-learning memory for AI tools  --  remembers user preferences and context across Claude, Cursor, and Codex with multi-parameter forgetting and cross-tool identity. Keeps your AI agents consistent across sessions and platforms. Ideal for operators who work across multiple MCP clients and want persistent, self-improving agent context.

### Linksee Memory MCP ★ New
Memory with drift detection for AI agents  --  detects context staleness and signals when agent memory needs refresh. For operators running multi-session agent workflows where context accuracy is critical. `npx -y linksee-memory`

### Memclaw ★ New ★ Featured
Governed, shared, self-improving memory for AI agent fleets  --  built for multi-tenant, multi-agent production environments. Apache 2.0. 131 GitHub stars. Production-proven: eToro runs 300+ agents on Memclaw (26,500+ memories, 1,372 shared skills, 23ms p50 search). Features: tenant isolation, visibility scopes (agent/team/org), agent trust tiers (0–3), full audit trails, single-pass LLM enrichment (14 memory types), hybrid search (pgvector + full-text + knowledge graph), contradiction detection, and PII auto-flagging. Managed platform at memclaw.net or self-hosted via Docker. `pip install memclaw-client` or `npm install @caura/memclaw-client`. Essential for operators running fleets of AI agents who need governed, shared memory with production-grade isolation and audit.

### Memory Engine ★ New (June 29)
Atomic memory model for AI agents — knowledge stored as atoms (facts, decisions, events, preferences, logs, procedures, notes, session messages). Multi-factor ranking combines FTS relevance × confidence × recency × weight (not just BM25). Organic decay and reinforcement over time. Essential for operators building AI agents that need sophisticated, long-term memory with context-aware recall beyond simple vector search. `github.com/SimoneB79/memory-engine`

### memo ★ New (July 1)
100% local persistent semantic memory for AI agents on Apple Silicon (MLX) or Linux/Ubuntu (CPU). Markdown source of truth, sqlite-vec + BM25 hybrid search, codegraph-backed knowledge graph. MCP server + CLI. No cloud, no API keys. Privacy-first memory infrastructure for operators who need local-only AI agent memory without cloud dependencies. Essential for regulated industries (HIPAA, GDPR) or operators who refuse cloud-based memory infrastructure. `github.com/jagoff/memo` · `pip install mlx-memo`

### SPM — Structured Project Memory ★ New (July 2)
Project-scoped memory for AI agents with provenance tracking and access control. Delivered as a remote MCP connector — context packs, verification, context graphs, and cryptographic memory integrity. Essential for operators running multi-agent workflows who need auditable, verifiable project memory with governance. `github.com/getspm/spm-agent-connectors` · [Integration Guide](/hermes/mcp/servers/external/spm-structured-project-memory/)

---

## New This Week (July 2, 2026 — afternoon sweep)

### 14 new business-relevant servers from mcp.so

**ERP & Business:** Odoo MCP (free ERP connector), BillingServ MCP (billing/invoicing)  
**Ecommerce & Logistics:** Launch Fast MCP (Amazon FBA), Container Tracking MCP (ocean freight)  
**Marketing & Content:** AppSigma (App Store ASO), Userbrain (UX testing), NaturalMelo (AI content detection)  
**BI & Procurement:** Booyah Index (SE Asia business directory), qlows (WTO-GPA tender/RFP search)  
**Legal & Compliance:** Kvasir Legal (EU law grounding), SaferAgenticAI (AI safety governance)  
**Agent Infrastructure:** SPM (project-scoped agent memory), Drumbeats (uptime/cron monitoring)  
**Finance:** AICryptoVault (crypto treasury)

Full details: [scan-results-2026-07-02-update.md](/hermes/mcp/servers/external/scan-results-2026-07-02-update/)

## New This Week (June 18, 2026  --  cron sweep)

### 8 new servers from mcp.so Latest

| Server | Category | Description |
|--------|----------|-------------|
| Openswissdata | Financial Data | Swiss federal data: TARES tariffs, FINMA registry, NOGA classifications  --  BAZG-authorized |
| Shinobi | Dev/Infra | Multi-agent task coordination  --  shared spine, decision log, dead-ends ledger, mobile approvals |
| Nahook | Dev/Infra | Webhook management and debugging from AI assistant |
| Hirenimbus Mcp | Productivity | Home services  --  AI agents find, compare, and book verified local pros in US metro markets |
| Obsidian Regulatory Mcp | Productivity | Verified regulatory data from 850+ official sources across 50+ jurisdictions |
| DesignForYou | Content Creation | On-brand design generation  --  logos, social posts, screenshots from 119 templates |
| Frinus | Memory/Knowledge | 70 tools for cognitive memory, knowledge hierarchy, orchestration, training pipelines |
| Agent Magnet | Memory/Knowledge | Self-learning cross-tool memory with multi-parameter forgetting |

---

## New This Week (June 18, 2026  --  afternoon sweep)

### 11 new servers from mcpservers.org All + mcp.so Latest

| Server | Category | Description |
|--------|----------|-------------|
| The Agent Times MCP ★ Featured | Content/Research | #1 Agent News MCP on ClawHub & Smithery  --  real-time agent economy news, 6 tools, ed25519-signed articles, Bitcoin rewards for agent contributions. Streamable HTTP + JSON-RPC 2.0 |
| BuyWhere MCP | Commerce | First SEA e-commerce MCP  --  real-time product search across 11M+ products in Singapore, SEA, US. 6 tools: search, compare prices, affiliate links. Free API key. `npx -y @buywhere/mcp-server` |
| Paper Search MCP ★ 1.9k GitHub | Content/Research | 20+ academic sources (arXiv, PubMed, Semantic Scholar, bioRxiv, etc.), OA-first fallback chain, MIT license. Free-first design. `pip install paper-search-mcp` |
| Human Browser | Web Scraping | Stealth cloud Chromium for AI agents  --  Patchright + Camoufox stealth engine, residential proxies, captcha solving behind one A2A endpoint. $1 free trial. `npx -y humanbrowser` |
| MCPApp MCP Server | Dev/Infra | Google Apps Script-based MCP network for Google Workspace (Gmail, Calendar). MIT license, 49 GitHub stars. Integrated with GASADK agent dev kit |
| Plane MCP Server | Productivity | Open-source project management (Plane.so) via MCP  --  6 tools: list projects, create issues, update issues, assignees. Self-hosted. `npx -y @kelvin6365/plane-mcp-server` |
| Portkey Admin MCP | Dev/Infra | 150 tools across 18 domains for Portkey AI Gateway  --  prompts, analytics, guardrails, API keys, virtual keys. MIT license. ⚠ Maintenance mode post Palo Alto Networks acquisition |
| AIR Blackbox MCP Server | Compliance | EU AI Act compliance checker  --  checks 6 articles, HMAC-SHA256 audit trails, auto-remediation. August 2026 deadline ready. `pip install air-blackbox-mcp` |
| FeedOracle DORA OS | Compliance | EU DORA compliance evidence infrastructure  --  50 MCP tools, 11 servers, ES256K-signed, blockchain-anchored. July 2026 deadline |
| Atlassian Rovo MCP Server | Dev/Infra | Atlassian remote MCP for Jira/Confluence  --  Streamable HTTP. ⚠ SSE endpoint deprecating June 30, 2026  --  migrate to new endpoint |
| Linksee Memory MCP | Memory/Knowledge | Memory with drift detection for AI agents  --  detects context staleness and signals when agent memory needs refresh. For operators running multi-session agent workflows |

---

## New This Week (June 19, 2026  --  morning sweep)

### 13 new servers from mcpservers.org All + Marketing + Productivity + mcp.so Latest

| Server | Category | Description |
|--------|----------|-------------|
| Demo Magic ★ Official ★ New | Marketing | Interactive video & AI product demos  --  answer viewer questions via AI-powered video |
| getAdvantage MCP ★ Official ★ New | Marketing | GEO/AI SEO scan  --  see how ChatGPT/Claude read your app, get paste-ready fixes (llms.txt, JSON-LD, FAQ, meta) |
| Onboard MCP ★ Official ★ New | Communication | Customer onboarding  --  monitor projects, surface blocked tasks, draft emails, role-based access |
| Just Publish ★ Official ★ New | Cloud Service | Instant website publishing  --  ask AI to publish and get a live link, zero setup |
| Dawnguard ★ Official ★ New | Development | Cloud security insights, guardrail guidance, compliance checking from AI agents |
| ITHZ MCP ★ New | Memory | Local-first deterministic project memory  --  context packs, decisions, gates, risks, claims ledger |
| Memlane ★ New | Memory | Save, search, pull articles, add links, write notes  --  personal content memory for agents |
| EyeBrowse ★ New | Web Scraping | Stealthy Chromium browser engine  --  85 tools, full Chrome DevTools Protocol, Python library |
| Sendmux Email MCP ★ New ★ Official | Communication | Email inbox & sending API for AI agents  --  transactional email, inbox management, MCP-native |
| Query Streams MCP ★ New ★ Official | Database | Securely connect MCP clients to live databases  --  no VPNs, inbound ports, or complex setup |
| ACG Mcp ★ New | Search | Audited Context Generation  --  verifiable fact-checking and grounded RAG via MongoDB |
| bruno-mcp ★ New | Development | MCP server for Bruno API testing collections  --  create, manage, execute .bru and .yml |
| InfraNode ★ New | Data/Infrastructure | Free, keyless MCP  --  German city data (weather, transit, energy, air quality), 38 tools, Apache 2.0 |

---

## New This Week (June 18, 2026  --  evening sweep)

### 8 new servers from mcpservers.org Finance + Marketing + Productivity

| Server | Category | Description |
|--------|----------|-------------|
| Praesentire ★ New | Finance | Bilingual (EN+ZH) financial news sentiment scored by Claude  --  tickers, batches, cross-language divergence |
| Agentberg ★ New | Finance | Agent-to-agent knowledge exchange for trading intelligence  --  publish, vote, earn reputation |
| ROIC.AI Financial Data API ★ Official ★ New | Finance | Company financials, ratios, prices, transcripts, market research  --  institutional-grade |
| Poppify Studio ★ New | Marketing | Photo-to-reel MCP for solo founders  --  1–10 photos → captioned vertical reel with music, voiceover |
| Spimov AI Video Dubbing ★ New | Marketing | Dub any video into 600 languages  --  YouTube dubbing + voice cloning via MCP |
| Scrivener MCP ★ New | Productivity | 60+ tools  --  manuscript management, writing analysis, semantic search, character/plot memory |
| Atlassian Confluence MCP ★ New | Productivity | Open-source Confluence MCP  --  read, create, search, manage wiki pages (Cloud + on-prem) |
| Muxara ★ New | Productivity | Online video conversions via API  --  convert formats directly from AI agent |

---

## New This Week (June 17, 2026  --  evening sweep)

### 20 new servers from mcpservers.org All + Finance + Marketing

| Server | Category | Description |
|--------|----------|-------------|
| Mentionkit MCP | Marketing | AI-first social listening with MCP support  --  brand monitoring for operators |
| UnusualWhales API | Finance | 100+ endpoints: options flow, dark pool, congressional trading, Greeks, volatility |
| Vee3 | Marketing/SEO | Live agent tools for domains, X, Google Trends, SEO, YouTube, TikTok |
| Factori MCP | Data/Intelligence | Query the real world  --  people, places, movement, markets in plain English |
| Rock.so MCP | Communication | AI workspace search, messaging, tasks, notes across all your spaces |
| Mamba Labs GTM Suite | Marketing | Six GTM signals: hiring detection, ICP scoring, flat Clay-ready data |
| ICP Fit Scorer | Marketing | ICP qualification with score, tier, and per-signal reasoning |
| Clearance Agent Income | Finance | x402 monetization services for APIs, MCP servers, agent workflows |
| Ophis | Finance | Intent-based DEX aggregator  --  gasless, MEV-protected swap orders across 11 chains |
| Bluesky MCP | Search | Remote MCP server for Bluesky  --  social media data and monitoring |
| Gainium | Finance | Crypto trading bots, deals, backtests from AI assistant |
| Universal Context Pipeline | File System | Local-first indexer for folders, PDFs, code, AI conversations  --  offline |
| Myco Brain | Memory | Self-hosted memory graph for AI agents  --  Postgres 16 + pgvector, Apache 2.0 |
| Cron Scheduler MCP | Development | 7 tools for AI agent cron jobs  --  SQLite persistence, retry logic, MIT license |
| Sparda | Development | Turn any codebase into an MCP server  --  Express & FastAPI in 3 minutes |
| Codex Control Plane MCP | Development | Durable MCP control plane for long-running Codex Desktop tasks |
| Async Parallel Antigravity | Development | Parallel, resumable CLI sessions from Codex, Claude Code, any MCP harness |
| Talordata MCP Server | Web Scraping | Structured search results from Google, Bing, Yandex, DuckDuckGo |
| Druid MCP server | Database | Access and administer Apache Druid databases via MCP |
| Zhiji Signal Station | Finance | Market phase transition signals (Phi/Chi) for HS300 and BTC  --  free sensing tier |

---

## New This Week (June 17, 2026  --  morning sweep)

### 30 new servers from mcpservers.org All + Finance + Marketing + Productivity

| Server | Category | Description |
|--------|----------|-------------|
| PostAgent ★ Official | Communication | Print and send physical mail/postcards USPS, paid per call in USDC via x402 |
| Eclincher | Marketing | Full social media management  --  publish, schedule, inbox moderation, analytics |
| MentionsAPI | Marketing | AI brand mention tracking across ChatGPT, Claude, Gemini, Perplexity, AI Overviews |
| Webotee Amazon MCP ★ Sponsor | Marketing | Amazon brand, seller & niche intelligence  --  buy-box history, competing sellers |
| NameSniper MCP | Marketing | Brand name, domain, social handle availability + sniping taken ones |
| AlphaAI | Finance | AI-enriched financial news, SEC Form 4 insider activity, OAuth 2.1, free tier |
| Niche | Productivity | Editorial intelligence  --  discover stories, rank angles, draft platform-native posts |
| SwapWizard MCP | Finance | Non-custodial DeFi execution  --  swap quotes, LP positions, routing across 5 EVM chains |
| invinoveritas | Finance | Independent verification for autonomous agents  --  pre-trade review, signed proofs |
| FiatDock | Finance | Non-custodial USDC ↔ bank for AI agents, EU/EEA, $0.05/session via x402 |
| CYBERDYNE | Finance | Engagement marketplace on Base  --  AI agents fund quests, verified humans complete them |
| RugCheck AI | Finance | On-chain Solana token safety  --  rug pulls, honeypots, mint/freeze authority traps |
| Sivut SEC Crypto Filing Radar | Finance | SEC crypto filing radar, CSV/markdown endpoints via x402 micropayments |
| Lightning Wallet | Finance | Bitcoin Lightning wallet MCP  --  invoices, budgets, L402 payments |
| Longbridge | Finance | 13 skills for Longbridge Securities  --  HK/US/A-share/SG markets |
| SynapseNetwork MCP | Finance | Paid API discovery, invocation, USDC agent payments, receipts |
| Kontomierz-MCP | Finance | Polish personal finance platform  --  bank accounts, transactions, budgets |
| EverAlice AI MCP | Marketing | Etsy listing copy, mockups, delivery packs, social campaigns, brand kits |
| SocialDataX Kuaishou MCP | Marketing | Kuaishou (快手) hot list, search, details, comments, creator research |
| Site-Shot | Web Scraping | Official screenshot API  --  real Chromium, full-page capture, country proxies |
| Xpenser | Finance | Open-source personal expense/income tracking, multi-currency, invoice parsing |
| imem | Memory | Private AI memory vault  --  set up in about a minute, no card required |
| RAGSync | Search | Index docs/files/websites into vector store with auto-syncs on changes |
| Jivilo (OmniX) | Web Scraping | Fast, affordable X/Twitter API  --  full read & write, no official dev account needed |
| docs-mcp | Productivity | Work with DOCX files  --  copy format from templates |
| Kailo Sheets | Productivity | Hosted MCP for Google Sheets |
| dochost | Productivity | Publish Markdown/HTML to clean shareable links via OAuth |
| tutamcp | Productivity | Tuta mail, calendar, contacts, drive  --  E2E verified, trusted sender filtering |
| Plate | Productivity | Lightweight project management via MCP |
| opn-mcp | Productivity | Link shortener with click analytics  --  hosted or self-hosted |

## New This Week (June 16, 2026  --  afternoon sweep)

### 8 new servers from mcp.so Latest + mcpservers.org

| Server | Category | Description |
|--------|----------|-------------|
| WoopSocial | Marketing | Post to social media with AI Agent via MCP  --  social publishing for AI agents |
| GuruPDF | Productivity | 126 tools  --  convert, compress, merge and OCR PDFs and 100+ file formats from any AI agent |
| SERPHouse MCP | Content/Research | Real-time high-volume SERP data via MCP for competitive research and SEO |
| engram | Dev/Infra | Local code-knowledge graph + bi-temporal mistakes memory for AI coding agents  --  Apache 2.0 |
| WSP WordPress MCP | Dev/Infra | Free WordPress MCP  --  connect AI coding agents to WordPress for content ops |
| Zhiji Signal Engine | Finance | Landau-Ginzburg market phase transition signals  --  HS300/BTC classification via x402 |
| AppStore MCP Server | Dev/Infra | Apple App Store Connect API via MCP (Rust)  --  apps, IAP, subscriptions, TestFlight, provisioning |
| Brain OS | Memory/Knowledge | Operational memory for AI agents that persists across sessions and tools |

---

## New This Week (June 11, 2026  --  mcp.so + mcpservers.org)

### Afternoon sweep  --  10 new servers from mcp.so Latest + mcpservers.org All

| Server | Category | Description |
|--------|----------|-------------|
| Convika - LP ops | Marketing | Landing page ops platform via MCP, OAuth 2.1 |
| Versium Reach | Marketing | Lead enrichment, B2B/B2C audience building, email verification |
| Sendpulse MCP | Marketing | Full marketing platform  --  email, CRM, chatbots, SMTP (134 methods) |
| Auditspark | Content/Research | AI website audit across SEO, performance, accessibility, UX  --  free tier |
| OpenSEO | Content/Research | SEO research: keywords, SERP, domain analysis, rank tracking |
| Amap Maps (高德地图) | Content/Research | China's second-largest mapping platform  --  AutoNavi MCP |
| NWO Robotics | Dev/Infra | 201 tools across 30 categories, on-chain identity on Base |
| Primerfp Scout | Gov/Intelligence | US federal + SLED contracting  --  32 tools, Streamable HTTP |
| QA Skills | Dev/Infra | 43 QA and test-automation skills for AI agents |
| Smart Match | Productivity | AI job matching, resume scoring, cover letter generation |

### Morning sweep  --  11 servers

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
| Capafy | Productivity | Monetize agent skills  --  "App Store for agent products" |
| Doorprofit | Analytics/Data | US crime, safety, demographic, and rent data by address |

### Evening sweep  --  11 new servers from mcp.so Latest + mcpservers.org All

| Server | Category | Description |
|--------|----------|-------------|
| HTAG Property Intelligence MCP ★ | Data/Intelligence | Australian property intelligence, 70+ read-only tools over Streamable HTTP |
| agents.hellobooks.ai | Finance/Accounting | AI agents that automate bookkeeping and financial close for SMBs |
| infaton-1c-mcp | Finance/Accounting | 1C:Enterprise ERP  --  51 tools for metadata, documents, registers, reports |
| Unclick | Productivity | 450+ callable endpoints across 60+ integrations + persistent cross-session memory |
| Secure Google Sheets MCP | Data Firewall | PortEden data firewall for Google Sheets  --  permission-gated, audit-logged |
| FileToPDF ★ official | Productivity | Convert DOCX, XLSX, PPTX, images, HTML, MD to PDF  --  free API key |
| Vault Cortex | Memory/Knowledge | Obsidian vaults MCP  --  search, memory, link graph, 23 tools, OAuth-protected |
| Geekflare | Content/Research | Scraping, web search, screenshots, network tools for AI agents |
| Remote Jobs MCP | Data/Intelligence | Jobicy MCP  --  autonomous remote job search and filtering in real-time |
| Vidoly AI | Content Creation | AI image & video generation for social media, branding, ecommerce |
| IRONCLAW BTC Node | Finance | Bitcoin blockchain data  --  17 tools, x402 USDC micropayments, no API keys |

## New This Week (June 16, 2026  --  morning mega-sweep)

### 46 new servers from mcp.so Latest + mcpservers.org Finance + Marketing + Productivity

| Server | Category | Description |
|--------|----------|-------------|
| Savvly MCP Server | Finance | Retirement projections, SEC-registered longevity fund, milestone payouts ages 80-95 |
| AusEcon MCP | Finance | Australian economic data  --  ABS, RBA, APRA statistics |
| Lovie  --  Company Formation MCP | Finance | Company formation, banking, cards, invoices, payments via AI agents |
| GoldLegal Legal Compliance API | Finance/Legal | AI legal compliance  --  contract review, EU AI Act, China AI reg, risk scoring |
| Personal Finance MCP Server | Finance | Compound interest, loan amortization, retirement planning, tax estimation |
| hourledger-mcp | Finance/HR | Work hours, overtime, gross pay  --  US federal, CA, AK, CO, NV law |
| LoneStarOracle MCP Server | Finance | 38 tools  --  crypto, DeFi, equities, energy, weather, real estate, on-chain |
| RealMarketAPI MCP Server | Finance | Real-time gold, forex, crypto, stock data  --  ultra-low latency |
| FinData MCP | Finance | Stock quotes, fundamentals, SEC filings, crypto via x402 micropayments |
| ACCRUE | Finance/DeFi | Non-custodial stablecoin yield  --  SYX + 12 USDC vault APYs |
| ERABI | Finance/DeFi | Open intent exchange  --  cryptographic agent identity, reputation-ranked discovery |
| signer-mcp | Finance/Security | Keyless CEX/DEX signing  --  API keys in AWS Nitro Enclave |
| Periodix Actions | Marketing/Sales | LinkedIn & Sales Navigator search  --  4.9/5 on G2 |
| SEOcrawl AI | Marketing/SEO | SEO + GEO MCP  --  21 tools, live GSC data, keyword analysis, site audits |
| Feedoptimise AI Feed Agent | Marketing/Ecom | Product feed auditing  --  Google Shopping, Meta, Amazon, TikTok |
| Assay Truth Graph MCP | Marketing/Sales | GTM agent grounding in governed, cited company truth |
| Toksta MCP Server | Marketing | B2B creator intelligence  --  LinkedIn/YouTube creator search, enrich, score |
| Adology AI | Marketing | Competitive social ad intelligence  --  "Perplexity for social ads" |
| IndustryLens | Marketing/Sales | Competitive intelligence reports  --  live B2B SaaS data, sources cited |
| GSC Wizard MCP | Marketing/SEO | Google Search Console analytics for AI agents |
| auto-geo ★ Official | Marketing/SEO | GEO-optimized content publishing engine for AI visibility |
| Orcool Studio MCP | Marketing/Creative | 107 tools  --  UGC concepts, AI avatars, Veo 3 video ad production |
| Local AI Visibility | Marketing/SEO | Share-of-Model score  --  AI visibility check for local businesses |
| Forward | Marketing/Sales | Pay-per-verified-result customer acquisition  --  $25 free credits |
| HYPD.AI | Marketing | Ad campaign creation/management/optimization on ChatGPT |
| Etymolt | Marketing/Legal | Trademark, domain, cultural, sound-symbolism brand verdicts |
| Progi | Productivity | MCP-native workflow engine  --  teach your agent your processes |
| PDFGate | Productivity | Document generation, PDFs, e-signature workflows |
| ProposalCraft | Productivity | Client proposal drafting in your own voice  --  local, no API key |
| Collaboard MCP Server | Productivity | Whiteboard creation, search, analysis for visual collaboration |
| DevMatch | Productivity/HR | AI recruiting for mission-aligned engineers across GitHub, X, YouTube |
| Feedback Synthesis MCP | Productivity/Research | Customer feedback synthesis  --  GitHub Issues, HN, App Store via x402 |
| Docsie | Productivity | Documentation management, video-to-docs, compliance analysis |
| Historis | Productivity | Shared timeline  --  team context, what happened, what needs handling |
| Numbers Online  --  Phone Intel | Communication | AI voice agent phone intelligence  --  caller ID, risk, DNC, signed receipts |
| Semust | Marketing/SEO | SEO Tools MCP |
| SendPulse MCP | Marketing | 134 methods across email campaigns, CRM, chatbots, SMTP |
| Prompty.tools | Productivity | Prompt optimization tools |
| Noogat | Productivity | Voice-first note-taking with MCP integration |
| Kangram MCP | Productivity | Telegram-native task management for AI agents and distributed teams |
| Pinako AI Bridge | Productivity | Browser tabs, bookmarks, notes connected to AI clients |
| IndoTender | Productivity/Regional | Indonesia LPSE tenders, company profiles, procurement data |
| Codepic | Design | Editable hand-drawn diagrams  --  create, update, export PNG/JSON |
| VoidMob MCP | Dev/Infra | Mobile proxies, SMS verification, eSIM data plans  --  25 tools |

## New This Week (June 12, 2026  --  morning sweep)

### 7 new servers from mcp.so Latest + mcpservers.org All

| Server | Category | Description |
|--------|----------|-------------|
| Solnk MCP | Marketing | Social media management for 9 networks  --  draft-first, team approval, content calendar |
| Shikamaru | Finance | Day-count and accrued interest calculations  --  provably correct financial math |
| Tani | Dev/Infra | Agent-native hub with trust-scored capability registry, 12 MCP tools |
| SeedBase | Dev/Infra | Synthetic test data generation  --  FK-consistent SQL datasets for databases |
| BUILDY | Dev/Infra | Cross-agent web app builder  --  build once, use from any AI client |
| Blog2Video | Content Creation | Convert blog URLs to video in under 3 minutes via MCP |
| chain-signer | Security/Finance | Pre-signature security suite for EVM agents  --  wallet drain and phishing protection |

## Previous Additions (June 10, 2026  --  sweep 2)

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

## New This Week (June 19, 2026  --  afternoon sweep)

### 8 new servers from mcp.so Latest + mcpservers.org All

| Server | Category | Description |
|--------|----------|-------------|
| Trust Gate MCP ★ Featured | Security/Compliance | First post-quantum MCP  --  policy-gated agent decisions, hybrid Ed25519 + ML-DSA-65 (NIST FIPS 204) receipts. EU AI Act Art. 50 native. Apache-2.0. `pip install trust-gate-mcp` |
| Prowlo | Content/Research | Hosted Reddit & X data MCP  --  semantic search, no Reddit API needed. Read-only. 5 tools. 14-day free trial, $19/mo. `https://api.prowlo.com/mcp` |
| OpenOSINT MCP | Data/Intelligence | MCP-native OSINT  --  18 tools (email, username, WHOIS, IP, Shodan, VirusTotal, Censys, etc.). MIT license, 710+ ⭐. `pip install openosint` |
| Attio MCP Server | CRM/Sales | AI-native CRM (Attio) via MCP  --  manage companies, people, lists, tasks. Node.js 18+. `npx -y @kesslerio/attio-mcp-server` |
| ZenML MCP Server ★ Official | Dev/Infra | Official MCP for ZenML MLOps/LLMOps  --  30+ tools, pipeline triggers, diagnostics. 46 ⭐. `pip install mcp-zenml` |
| Lightrun MCP | Dev/Infra | Production debugging from AI agents  --  live runtime context, no redeploy. `https://app.lightrun.com/mcp` |
| Memclaw ★ Featured | Memory/Knowledge | Governed shared memory for AI agent fleets  --  tenant isolation, trust tiers, audit trails. eToro-proven (300+ agents). Apache-2.0. `pip install memclaw-client` |
| Deckextract | Productivity | DocSend & Papermark MCP  --  extract decks, convert to PDF/PPT from AI agents |

---

## New This Week (June 22, 2026  --  morning sweep)

### 6 new servers from mcp.so Feed + mcpservers.org

| Server | Category | Description |
|--------|----------|-------------|
| Tradingview Mcp ★ New | Finance | Live market data & technical analysis  --  30+ tools, MIT license, self-host or hosted |
| Tossinvest MCP ★ New | Finance | Korean stock trading via Toss Securities  --  prices, orders, portfolios |
| OpenAI Ads MCP Server ★ New | Marketing | OpenAI/ChatGPT Ads API  --  campaigns, creatives, audiences, insights |
| SE Ranking MCP ★ New | Marketing/SEO | 180+ SEO & AI search visibility tools  --  keywords, backlinks, audits |
| PPXC Find Customers ★ New | Marketing | Short-video comments → ranked customer leads + outreach scripts |
| Rendley Mcp ★ New | Content Creation | Full video editor via MCP  --  AI-driven editing with brand kit + footage |

---

## New This Week (June 23, 2026 — afternoon sweep)

### 9 new servers from mcp.so Feed + mcpservers.org

| Server | Category | Description |
|--------|----------|-------------|
| Ensotrade ★ New | Finance | Bloomberg-grade crypto intelligence — real-time data, institutional analytics, multi-exchange coverage |
| Evibe Portfolio ★ New | Finance | Read-only investment portfolio MCP — holdings, performance, dividends, benchmarks |
| Gocreative ★ New | Compliance | Compliance, KYB, sanctions screening — automated business verification for AI agents |
| EMILIA Protocol ★ New | Security/Compliance | Offline-verifiable human approval for irreversible agent actions — 2-person rule, IETF-drafted |
| Powerdmarc Mcp ★ New | Marketing/Security | Email DMARC compliance monitoring — SPF/DKIM/DMARC, spoofing detection, forensic reports |
| Unspam MCP ★ New | Marketing | Email deliverability testing — spam checks, inbox placement, screenshots, heatmaps |
| mcp-ads ★ New | Marketing | Ads platform MCP — campaign management, performance analysis, optimization |
| Process Street MCP Server ★ New | Productivity | Workflow automation — trigger checklists, SOPs, recurring processes via OAuth |
| freesearch-mcp ★ New | Content/Research | Free SearXNG-powered web search — no API keys, no rate limits, no billing |

---

## New This Week (June 23, 2026 — morning sweep)

### 23 new servers from mcp.so Feed (June 23 morning)

| Server | Category | Description |
|--------|----------|-------------|
| patternfetch ★ New | Finance/Trading | Token-compact market-state briefs for AI trading agents. One call: compact candles + patterns + support/resistance + regime + interpreted indicators. MCP + REST, x402 + Stripe. `github.com/MarvinRey7879/patternfetch-client` |
| StockSlash ★ New | Finance | Hosted MCP for SEC 13F filings from ~80 super investors, U.S. Congress stock trades, and corporate insider (Form 4) buying. 23 tools, no install, no API key. One-call profiles summarize any fund or stock. `https://stockslash.com/mcp` |
| Influee Mcp Agent ★ New | Marketing | Influencer marketing MCP — connect AI agents to Influee's creator discovery, campaign management, and performance analytics platform |
| Horizon Insights Mcp ★ New | Finance | Market data, financial statements, valuation data, research materials, transcripts, charts, macro indicators, and market news for investment research workflows |
| AI Battle Room (AI 吵架房) ★ New | Dev/Infra | Multi-agent collaborative document editing across different machines. Role-isolated agents: read, review, but can't modify without permission. Project-level MCP tokens. Open source. `https://github.com/sxcvicky/AIbattleroom` |
| Planner ★ New | Productivity | AI task planning and scheduling MCP — organize tasks, projects, and timelines from any AI client |
| MonSuiviMédical ★ New | Healthcare/Data | French healthcare professional directory (RPPS) and health facility registry (FINESS). 100% public data, updated daily. Practitioner search, detailed profiles, specialties. No ratings or rankings |
| Reap ★ New | Finance | Payment and expense management MCP — corporate cards, bill pay, and financial operations for AI agents |
| Octotrip Rental Cars ★ New | Travel/Commerce | Car rental search and booking MCP — compare rental options, check availability, and book vehicles from AI agents |
| Customs MCP ★ New | Gov/Logistics | International customs and tariff data for AI agents — HS codes, duty rates, trade compliance, customs regulations |
| Goodvat Mcp Server ★ New | Finance/Tax | VAT compliance and tax rate lookups for AI agents — validate VAT numbers, check rates across jurisdictions |
| Formswrite ★ New | Productivity | Create forms and export to 30+ platforms from any MCP client. Form building and distribution for operators managing surveys, applications, and data collection |
| Agent Exchange ★ New | Dev/Infra | Marketplace MCP for discovering and connecting AI agents. Agent-to-agent service exchange with trust scoring and capability registry |
| Qonoro Intelligence Mcp ★ New | Data/Intelligence | Business intelligence and data analytics MCP — query datasets, generate reports, and surface insights from AI agents |
| Opplevagent ★ New | Productivity | Experience and learning platform MCP — track skills, manage development goals, surface growth opportunities |
| PolyBridge MCP ★ New | Dev/Infra | Cross-chain and multi-protocol bridge MCP — connect AI agents to multiple blockchain networks and protocols |
| Omnicall ★ New | Dev/Infra | Universal agent tools gateway — route AI agent tool calls across multiple backends and services through a single MCP endpoint |
| Debitura ★ New | Finance | Debt collection and receivables management MCP — credit checks, collection workflows, payment status tracking for AI agents |
| REMODELERIQ ★ New | Real Estate | Construction and remodeling intelligence MCP — cost estimation, material pricing, contractor matching, and project planning |
| Africa Eligibility Mcp ★ New | Gov/Social | African social program eligibility verification — check qualification for government benefits, subsidies, and social programs across African jurisdictions |
| East Africa Momo Parser Mcp ★ New | Finance/Mobile | East African mobile money (MoMo) transaction parsing — M-Pesa, Airtel Money, MTN Mobile Money transaction data for AI agents |
| African Fintech Mcp ★ New | Finance | Pan-African fintech integration MCP — connect AI agents to African banking, payments, and financial services APIs |
| Opportunityradar Data Mcp ★ New | Data/Intelligence | Business opportunity discovery MCP — tender alerts, procurement data, funding opportunities, and market entry intelligence |

---

## New This Week (June 24, 2026 — evening sweep)

### 28 new servers from mcp.so Feed + mcpservers.org /all

| Server | Category | Description |
|--------|----------|-------------|
| AIDC-AI.IO Design Engine ★ New | AI/Design | AI-powered design engine for UIs and graphics — text-to-design, component generation |
| AccessibilityAI ★ New | Dev/Infra | AI accessibility testing — automated WCAG compliance checking and fix suggestions |
| Agentbrush ★ New | Content & Research | AI agent for web scraping and data extraction from any website |
| agent-connector ★ New | Dev/Infra | Agent-to-agent communication and orchestration framework |
| Apiosk MCP ★ New | Dev/Infra | API marketplace and integration platform — discover, test, connect APIs via MCP |
| Brand & Domain Intelligence Mcp ★ New | Marketing | Brand monitoring, domain intelligence, and trademark analysis |
| Citedspy ★ New | Content & Research | Citation tracking and academic reference analysis |
| Cybersecurity Threat Intelligence Mcp ★ New | Security/Compliance | Real-time threat intelligence feeds — IOC tracking, threat actor profiles |
| Document To Json Pdf Parser ★ New | Productivity | PDF documents to structured JSON — invoices, contracts, statements |
| Donotact ★ New | Security/Compliance | Do-not-contact registry and privacy compliance management |
| Financial Signals Mcp ★ New | Financial Data | Financial market signals, trading indicators, and economic data |
| Government Contracts Intelligence Mcp ★ New | Content & Research | Government RFPs, procurement intelligence, and contract opportunities |
| Keenable Web Search ★ New | Content & Research | Web search with AI-powered result filtering and summarization |
| Legal Doc Intelligence ★ New | Legal | AI-powered legal document analysis, contract review, compliance checking |
| Metagraphed Bittensor Subnet Registry ★ New | Dev/Infra | Bittensor subnet registry and metadata for decentralized AI networks |
| Minddory Com Connect ★ New | Productivity | Mind mapping and knowledge organization — visual knowledge graphs |
| Monet Team ★ New | Marketing | Team monetization and revenue analytics platform |
| Newsagent Data ★ New | Content & Research | News aggregation and data feeds for AI agents |
| Open Code ★ New | Dev/Infra | Open-source code search and analysis across repositories |
| Patent Intelligence Mcp ★ New | Content & Research | Patent search, analysis, and IP intelligence |
| Penqwin ★ New | Productivity | AI productivity assistant and workflow automation |
| Polymarket Scan Mcp ★ New | Financial Data | Polymarket prediction market data and analytics |
| ProductNow ★ New | Productivity | Product management and roadmap MCP — features, progress, stakeholders |
| Prompt2Love ★ New | Content Creation | AI prompt engineering and creative content generation |
| Rifframe ★ New | Content Creation | AI-powered video creation and editing framework |
| Sharebench ★ New | Financial Data | Investment research and benchmark sharing platform |
| Sports Hub ★ New | Content & Research | Sports data, statistics, scores, and analytics across major leagues |
| Stophy ★ New | Dev/Infra | Development workflow automation and stop-gap analysis |
| Textavia Mcp ★ New | Content & Research | Text analysis, summarization, and NLP tools |
| Turbojobapply Com Mcp ★ New | Productivity | Automated job application and resume optimization |
| Weather & Climate Intelligence Mcp ★ New | Content & Research | Weather forecasts, climate data, and environmental intelligence |
| X402 Trust Scores ★ New | Dev/Infra | Trust scoring and verification for x402 payment network |

---

## New This Week (June 25, 2026 — morning sweep)

### 14 new servers from mcp.so Feed

| Server | Category | Description |
|--------|----------|-------------|
| Zillapi ★ New | Real Estate/Data | Zillow property data MCP — Zestimates, rent estimates, tax history, price history, schools, photos, and listing details via real-time API |
| DC Hub ★ New | Infrastructure/Energy | Data center & energy intelligence — real-time grid telemetry (7 US ISOs + 40+ balancing authorities + EU/GB/TW/AU), 21K+ facilities, gas-vs-grid economics, 2K+ M&A deals |
| Grist ★ New | Productivity/Data | Spreadsheet-database hybrid MCP — list/query/add records, create docs and tables across team sites. Universal SQL builder, OAuth-secured |
| Patchwork OS ★ New | Dev/Infra | Local-first MCP bridge for Claude Code — 177 tools (LSP, debugger, terminal, git, GitHub, file ops) via companion VS Code extension |
| Vindata MCP ★ New | Automotive/Data | VIN decoding and European vehicle data — structured make, model, year, equipment details for automotive operators and dealer workflows |
| VoIPstudio MCP ★ New | Communication/Analytics | VoIP call analytics — securely query call recordings, CDRs, live calls, voicemails for reporting, QA, and operational intelligence |
| Docker MCP Server ★ New | Dev/Infra | Full Docker management via AI agents — containers, images, networks, volumes, swarm services, secrets, configs, nodes, plugins |
| Devloop ★ New | Dev/Infra | Browser + dev server on one correlated timeline — browser console error + backend stack trace from the same request, for Puppeteer/Expo/React Native |
| TapWaterMap ★ New | Gov/Health | US tap water quality from EPA SDWIS records — contaminants, violations (health-based classification), water systems serving any city |
| Wever Labs Agentic Rails ★ New | Dev/Infra | Agent workflow rails — proof-backed agent runs, receipts, callbacks, handoff packages, and compliance for agent-driven operations |
| Control Plane ★ New | Dev/Infra | Official Control Plane MCP — deploy, operate, troubleshoot, migrate containerized workloads across AWS, GCP, Azure, OCI, plus secrets, networking, stateful storage |
| Video Gen MCP ★ New | Content Creation | AI video generation via FAL AI from MCP clients — `uv`-based, local or remote deployment |
| RaidRunner ★ New | Entertainment | Twitch raid train scheduling MCP — manage schedules, OAuth-secured streaming relay events |
| ReadGZH ★ New | Content/Research | WeChat public account article reader — 99.89% anti-scraping success rate, 50-87% token compression. Chinese-market content intelligence |

---

## New This Week (June 24, 2026 — morning sweep)

### 13 new servers from mcp.so Feed + mcpservers.org Communication + Cloud Service + Development + Other

| Server | Category | Description |
|--------|----------|-------------|
| Pandadoc Mcp ★ New | Commerce/Docs | PandaDoc document automation MCP — create, send, and track proposals, contracts, quotes, and e-signatures from AI agents |
| KaiCalls ★ New | Communication | AI phone secretary for businesses — outbound calls, transcripts, voicemails, SMS, and analytics from your business line |
| Shipmail MCP ★ New | Communication | Business email MCP for AI agents — custom-domain inboxes, REST API, webhooks, send, read, and reply tools |
| Costory ★ New | Finance/FinOps | Multi-cloud cost analysis — normalized cost data across AWS, GCP, Azure, Datadog, OpenAI, and Anthropic with allocation and correlation |
| Amplifier MCP Server ★ Official ★ New | Commerce/Fulfillment | D2C eCommerce fulfillment platform — manage orders, inventory, shipments, campaigns, and billing via AI agents |
| Amazon Seller Central / Amazon Ads ★ New | Commerce | Connect Amazon Seller Central and Ads accounts to AI agents — inventory, orders, campaign management, and advertising analytics |
| Averta security ★ New | Security/Infra | MCP gateway security — scoped access per AI agent, credential containment, full audit trail for every MCP tool call |
| MewCP Razorpay MCP ★ New | Commerce/Payments | Hosted, stateless Razorpay MCP — manage payments, customers, subscriptions, invoices, and financial operations for Indian-market operators |
| MewCP Google Business MCP ★ New | Marketing/Local | Google Business Profile management — listings, reviews, locations, and customer interactions via AI agents |
| corelayer0 ★ New | Dev/Infra | Turn any OpenAPI spec into a hosted MCP server in 30 seconds — EU-hosted, GDPR-native, stable URLs |
| Pipetable ★ New | Data/Dev | Local data files as DuckDB views — register files, let AI agents run real SQL against them, zero data exfiltration |
| Clutter ★ New | Dev/Data | Synthetic data generator MCP — realistic companies, documents, and structured data for testing and demo systems |
| Syntitan ★ New | Data/Enterprise | AI-Ready Data Platform MCP — bridge enterprise data management and AI execution with governed access |

---

## New This Week (June 24, 2026 — afternoon sweep)

### 7 new servers from mcp.so Feed + mcpservers.org Cloud Service + Memory

| Server | Category | Description |
|--------|----------|-------------|
| Ares MCP ★ New | Finance/Compliance | Official Czech business registry MCP — 14 tools: company lookup, due diligence, statutory bodies, insolvency, VAT-payer & trade-license checks, address search, cross-company person graphs. Ed25519-signed provenance |
| mcp-jp ★ New | Commerce/HR | Japanese SMB SaaS connectors — 30+ tools for KING OF TIME, SmartHR, kaonavi, Smaregi, CloudSign, L Step, and more. Independent pip packages per connector; archived once official MCP ships |
| OnePageCRM ★ New | CRM | Create, search, update, and manage data in OnePageCRM directly from AI agents. Full CRM operations via MCP for sales operators |
| Mcp Emails ★ New | Communication | Read, search, send, organize, draft, and schedule email across your inboxes from any MCP client. Multi-inbox email management for AI agents |
| Cloudability API ★ New | Finance/FinOps | Comprehensive MCP for Cloudability API — advanced cloud cost management, Kubernetes container analytics, and budget forecasting across multi-cloud environments |
| botcorpus ★ New | Legal/Compliance | Machine-first, web-sourced knowledge base of current CZ/SK/AT/EU civic, tax & legal facts — each with source, date & confidence. For operators in Central European jurisdictions |
| FoundersOS ★ New | Productivity/CRM | CRM, tasks, finances, feeds, and memory for founders — as an MCP server. All-in-one operator OS for AI-native startup management |

---

## New This Week (June 22, 2026 — afternoon sweep)

### 35 new servers from mcp.so Latest + mcpservers.org Finance + Marketing + Productivity + Development

| Server | Category | Description |
|--------|----------|-------------|
| Flatland ★ Official | Finance | Financial & quantitative modeling engine for AI agents — typed, named, deterministic |
| Finance Toolkit | Finance | 200+ financial metrics calculated transparently from raw financial statements — no third-party endpoints |
| Profitlee Mcp | Ecommerce/Finance | E-commerce & marketplace profitability — net profit, margin, ROI, breakeven, fee-adjusted scenarios |
| Allowance MCP | Finance | Secure agent purchasing with human-approved virtual cards, checkout automation, receipt reporting |
| Infersports | Data/Sports | Keyless, hosted MCP for live football & basketball odds — Asian-handicap lines, de-vigged sharp (Pinnacle) probabilities |
| Selvedge | Dev/Infra | Captures the "why" behind AI coding agent changes — blame, diff, history, prior attempts. 8 tools, local SQLite, MIT |
| Routara Llm Gateway | Dev/Infra | Routes 787+ LLMs + image & video generation via single API. OpenAI-compatible. `npx routara-mcp@1.0.1` |
| ServiceNow MCP | Productivity/ITSM | 65 tools over full ServiceNow REST surface — Table, CMDB/IRE, Catalog, Change, Knowledge, Email, ATF |
| datavessel | Marketing/Analytics | 100+ tools across 10 connectors — Google Analytics, Search Console, Google & Meta Ads, Shopify, WooCommerce, Slack, LinkedIn. OAuth 2.1 |
| PostWire | Marketing/Social | Post to TikTok, Instagram, YouTube, X, LinkedIn, Bluesky, Telegram, Mastodon & Discord via one MCP tool |
| AppGoblin ASO | Marketing/ASO | App Store stats, installs, keywords, revenue, descriptions — B2B SDK analysis & ad tech stack intelligence |
| Company Identity Resolver | Marketing/Sales | Resolve company name/domain/LinkedIn URL into canonical identity with confidence scores |
| Company Change-Event Feed | Marketing/Sales | Monitor company domain — hiring, tech stack, funding, firmographics, social changes |
| Funding & Press Signal Scanner | Marketing/Sales | Scan Google News & PR wires for funding rounds, executive moves, product launches, acquisitions |
| Company Firmographic Enricher | Marketing/Sales | Enrich company domain into structured firmographics with source provenance (schema.org, meta tags) |
| Company Social Presence Mapper | Marketing/Sales | Map company domain → LinkedIn, X, Instagram, Facebook, YouTube profiles with follower counts |
| Google Ads - AdPlug | Marketing/Advertising | Connect Google Ads to the AI tools you already use |
| Sentor | Analytics | Review analysis for AI agents — surface topics from thousands of reviews, pinpoint what to fix first |
| OpenBase | Data/Intelligence | Free French company data — 20M+ companies, 14 tools (SIREN/SIRET, financials, executives, solvency, legal). No API key |
| Brazilian PEP | Gov/Compliance | Brazilian Politically Exposed Persons & federal public servants via Porta da Transparência API |
| Ezel Legal AI | Legal | AI legal research over MCP — search US case law, fetch full opinions, matter-aware Q&A |
| Quintadb | Database/Productivity | No-code databases, forms, portals — 104 MCP tools. Available in EN, UA, RU variants |
| framefetch | Content/Research | Social video URL → metadata, transcript (captions/Whisper), engagement insights, parametric frames. YouTube, TikTok, Instagram. x402 pay-per-call |
| Silkgeo Geo | Marketing/SEO | Dual-market GEO platform — 8 MCP tools for AI visibility audit and citation tracking |
| MuninX | Productivity | Help desk for small teams — tickets, messages, history search, analytics via MCP. Role-respecting |
| tinysend | Marketing/Email | Email newsletter creation & management — subscribers, broadcasts, OAuth sign-in, no API key needed |
| Motivegrid Vehicle Advisor | Data/Consumer | Vehicle intelligence — car comparison, 5-year ownership cost, safety analysis, structured rankings |
| FlipDomain Domain Sales | Commerce | Premium domain sales — search 2,972 domains, inspect prices, submit purchase offers |
| Thiri Chord Intelligence | Creative/Music | Deterministic music theory for AI agents — chord analysis, voicing generation, jazz reharmonization. ℤ/12 pitch-class engine |
| Urbankit Atlas | Data/Real Estate | US county parcel ArcGIS REST endpoints — 152 counties across 50 states |
| AgentPlayerAchievements | Productivity | Steam-style achievements for AI coding agents — gamified Claude Code, Hermes workflows |
| PDFMakerAPI | Productivity | Generate PDFs from natural language — invoices, receipts, proposals. Get view/edit/share link |
| VocalRemover MCP ★ Official | Creative/Audio | Professional audio editing and AI augmentation tools |
| //beforeyouship | Dev/Infra | LLM cost modeling from editor — realistic costs with retries, caching, batch discounts, infra overhead |
| Tensorfeed X402 Base Mcp | Finance/Crypto | Read-only Base mainnet chain reader for x402 payment verification, AFTA federation helpers |

---

## New This Week (June 20, 2026  --  morning sweep)

### 11 new servers from mcpservers.org All + mcp.so Latest

| Server | Category | Description |
|--------|----------|-------------|
| Agent402 ★ Featured | Dev/Infra | Open-source, self-hostable MCP server  --  ~1,100 tools (web search, headless Chromium, PDFs, OCR, images, ~1,040 CPU utilities). Free to self-host or pay-per-call via x402 (USDC on Base). Agent memory, SEC EDGAR, live finance/crypto/macro data. `npx -y agent402-mcp` |
| SEOforGPT MCP ★ New | Marketing/GEO | AI visibility MCP for agencies  --  audit brand visibility in AI answers, monitor competitors, fix GEO gaps. 15 tools including visibility reports, competitor intelligence, client briefs, CMS publishing. OAuth, Streamable HTTP. `https://www.seoforgpt.io/mcp` |
| SyncGTM ★ New | Marketing/Sales | B2B leads and enrichment  --  verified emails, phone numbers, LinkedIn data, buying signals. 20+ tools with workspace context awareness. OAuth browser sign-in. `https://api.syncgtm.com/mcp` |
| Adsumo ★ New | Marketing/Creative | Generate on-brand image and video ads straight from prompts. 24 tools  --  brand setup, image ads, AI video (Seedance/Sora 2/Veo 3.1/Kling 2.6), competitor ad research. OAuth, Streamable HTTP. `https://www.adsumo.ai/api/mcp` |
| OneCal Calendar MCP ★ New | Productivity | Multi-calendar MCP  --  Google, Outlook, and iCloud calendars in one server. Read schedule, check availability, create/update/delete events. OAuth with scoped permissions. `https://mcp-server.onecal.io/mcp` |
| overreach ★ New | Dev/Infra | AI agent scope-creep auditor  --  audits code diffs against original task prompts, flags out-of-scope changes (new deps, env vars, endpoints, features). CI gate ready. `npx -y overreach` |
| Appflowy MCP ★ New | Productivity | Self-hosted AppFlowy Cloud via Docker with token-scoped access. List workspaces, navigate pages, create/update/read/edit blocks. Docker image: `m2n2/appflowy-mcp` |
| IPRout MCP Server ★ New | Dev/Infra | GeoIP and ASN intelligence for AI agents  --  country, city, timezone, network ownership lookups. Node.js 18+, IPRout API key. MIT license. |
| Domain Deliverability Checker ★ New | Marketing | Email domain DNS deliverability: SPF, DKIM, DMARC, MX, blacklist, domain age, 0-100 composite score. `mammalabsdev/mcp-domain-deliverability-checker` |
| YPipe ★ New | Dev/Infra | Local AI desktop client + MCP orchestration engine  --  visual GUI or headless, Java-native, runs offline models with zero cloud. One-click MCP server installation, autonomous agent chains. Cross-platform (Win/Mac/Linux). |
| Legacy Java to Microservices ★ New | Dev/Infra | Community gateway to migrate Jakarta EE monoliths into Spring Boot 3.4 microservices via AST parsing. Discovery gateway for premium MCPize-hosted service. |

---

## New This Week (June 25, 2026 — afternoon sweep)

### 3 new servers from mcp.so Latest + 17 from mcpservers.org /all

| Server | Category | Description |
|--------|----------|-------------|
| Stagenth File Relay ★ New | Dev/Infra | Remote MCP server (Streamable HTTP) giving AI a real cloud file system + web scraping. 21 tools: chunked/resumable upload, download, list/search, full folder tree (create/move/rename/delete), shareable links, quota, and scrape_url (web page → clean Markdown). Credit-based, free credits on signup. `https://www.stagenth.com/mcp/file-relay` |
| Oriel ★ New | Dev/Infra | Drive Docker and Colima from an AI. Safety-gated MCP server for containers, images, volumes, networks, and Compose, with secret masking and a destructive-action grant. Essential for operators who want AI-managed container infrastructure with safety guardrails. |
| PDF To Markdown ★ New | Productivity/Docs | Hosted MCP server turning PDFs into clean, LLM-ready Markdown. Real Markdown tables, formulas as LaTeX, OCR for scans. Same engine used by major AI platforms for document processing. Essential for operators who need AI agents to process PDFs into structured, queryable text. |
| MaxAEO AI Visibility MCP ★ New | Marketing/GEO | Local-first MCP server for AI visibility audits across GEO/AEO, llms.txt, AI crawler readiness, robots, sitemap, canonical, metadata, noindex, and JSON-LD. Essential for operators investing in AI-engine discoverability. |
| Weavz ★ New | Data/Integration | Data integration and API connectivity MCP — connect AI agents to diverse data sources and services |
| Scholarxiv ★ New | Content/Research | Academic paper and preprint access via MCP — scholarly research for AI agents |
| Memdeklaro ★ New | Memory/Knowledge | Declarative memory and knowledge management MCP — structured knowledge representation for AI agents |
| Outlit AI Marketing ★ New | Marketing | AI marketing tools MCP — campaign analysis, content optimization, and marketing intelligence |
| DataAssist MCP ★ New | Data/Analytics | Data analysis and assistance MCP — query, analyze, and visualize datasets through AI agents |
| Subsquid Portal MCP ★ New | Data/Blockchain | Blockchain data indexing and querying via MCP — access to decentralized data lakes and indexed blockchain data |
| Compabase MCP ★ New | Content/Data | Company and content database MCP — structured business data for AI agents |
| x402 Stoa Launch Review ★ New | Dev/Infra | x402 payment protocol launch review tools — verify and deploy x402-enabled MCP servers |
| PyPI Burst ★ New | Dev/Infra | Python package intelligence MCP — PyPI package analysis, dependency checking, and release monitoring |
| Spider Cloud MCP v2 ★ New | Web Scraping | Cloud-based web scraping MCP v2 — scalable, proxy-rotated web data extraction for AI agents |
| Arachne MCP ★ New | Dev/Infra | Web crawling and data extraction framework via MCP — structured web data collection |
| Pedra MCP ★ New | Dev/Infra | Infrastructure and deployment automation MCP — manage cloud resources through AI agents |
| Verychic MCP ★ New | Productivity | Productivity and lifestyle management MCP — personal organization and task management |
| OpenGrok Go MCP ★ New | Dev/Infra | OpenGrok code search and analysis via MCP — search massive codebases through AI agents |
| Vision Cropper ★ New | Content Creation | x402-enabled image cropping and processing MCP — AI-assisted image manipulation via micropayments |
| Flkeys ★ New | Data/Regional | Florida Keys regional data MCP — local business, tourism, and geographic intelligence |

---

## New This Week (June 25, 2026 — evening sweep)

### 18 new servers from mcp.so Feed

| Server | Category | Description |
|--------|----------|-------------|
| assistable ★ New | Communication | Multi-channel voice AI for customer interaction — place/manage AI phone calls, send SMS/WhatsApp/web-chat messages, manage contacts and assistants. `ASSISTABLE_API_KEY={KEY} npx -y @assistableai/mcp` |
| flexorch-mcp ★ New | Document Intelligence | Unstructured business documents → structured LLM-ready datasets. 6 async tools: classify → extract fields → detect PII → build RAG datasets. PDF, DOCX, invoices, contracts, payroll. `FLEXORCH_API_KEY={KEY} flexorch-mcp` |
| nachonacho-for-ai-agents ★ New | Commerce/Procurement | B2B SaaS marketplace for AI agents — search thousands of products, compare deals, sign up from chat. Connect agents to the NachoNacho marketplace. `https://mcp.nachonacho.com/` |
| local-mcp ★ New | Productivity | Native macOS MCP server — 160+ tools connecting AI agents to Mail, Calendar, Contacts, Reminders, Messages (iMessage), Notes, Safari, OmniFocus, Microsoft Teams. `npx -y local-mcp` |
| scout-by-jakvab ★ New | Business Intelligence | Nordic company intelligence — look up companies, AI summaries, scoring and signals via MCP. Streamable HTTP. `npx mcp-remote https://mcp.scout.jakvab.se` |
| tlaloc-mcp-server ★ New | Financial Data/Regional | Mexican official data: validate CURP (RENAPO), RFC (SAT), postal codes (SEPOMEX), phone carriers (IFT), banking (Banxico, SPEI, CEP). Fintech-ready. `npx mcp-remote https://api.tlaloc.sh/mx/mcp` |
| polish-companies ★ New | Financial Data/Regional | 3M+ Polish companies from KRS registry via Compabase MCP. Business intelligence for Polish market operators. `npx mcp-remote https://compabase.com/api/mcp` |
| braintube ★ New | Knowledge Management | Turn everything you save — YouTube, articles, podcasts, PDFs, Notion, Obsidian, any URL — into a persistent, semantically searchable knowledge base. `npx mcp-remote https://brain-tube.com/mcp` |
| hubd ★ New | Productivity | Project tracker for teams of humans + AI agents — plain files, zero dependencies. MCP server + CLI for agent-coordinated project management. Kanban, markdown, JSONL. `https://github.com/bzdOS/hubd` |
| sovereign-execution-engine ★ New | Dev/Infra | 15 x402 execution primitives for AI agents — cross-chain routing (XRPL/Hedera/Base), browser automation, EU AI Act checks. Pay per call in USDC on Base. `npx mcp-remote https://api.zuluworksai.com/mcp` |
| gpthuman-humanizer ★ New | Content Creation | GPTHuman API for rewriting AI-generated text into natural, human-sounding prose. Bypasses AI detectors. `GPTHUMAN_API_KEY={KEY} npx -y @gpthuman/mcp-server` |
| bittensormcp ★ New | Financial Data/Crypto | Full Bittensor blockchain access for AI agents — 11 free read-only tools: balances, portfolios, subnet lists, metagraph, staking, AMM swaps, alpha pricing. `npx mcp-remote https://bittensormcp.com/api/mcp` |
| axiomseal ★ New | Memory/Knowledge | Tamper-proof, truth-validated AI memory — every memory SHA-512 chain-sealed, OAuth in 30 seconds. Claude & Cursor compatible. `npx mcp-remote https://mcp.axiomseal.com/mcp` |
| tracehunt ★ New | Security | OSINT username reconnaissance across 480+ platforms. footprint_score() returns 0-100 digital footprint rating. Python MCP. `python mcp/tracehunt_mcp.py` |
| simcloud ★ New | Regional/Telecom | South African telecom MCP — wallet balance checks, network lookups, SMS, airtime recharges, data bundles, prepaid electricity. OAuth, Streamable HTTP. `npx mcp-remote https://simcloud.co.za/api/mcp.php` |
| 302_sandbox_mcp ★ New | Dev/Infra | Remote sandbox for code execution and file operations. Secure, isolated environments for AI agent code execution. `npx -y @302ai/sandbox-mcp` |
| jina-mcp-tools ★ New | Research | Jina AI Search Foundation APIs — AI-powered web search, content extraction, and embedding. Multi-engine search for comprehensive research. `npx jina-mcp-tools` |
| mailtrap-mcp ★ New | Communication | Transactional email sending and testing via Mailtrap — email automation for AI agents. Test inboxes, spam analysis, deliverability checks. `npx -y mcp-mailtrap` |

---

## New This Week (June 26, 2026 — morning sweep)

### 27 new servers from mcp.so Feed + mcpservers.org /all

| Server | Category | What It Does |
|--------|----------|-------------|
| Channel3 Product Search | Content & Research | Product search and discovery engine |
| Lightbringer | Content & Research | Research and knowledge discovery |
| Roboselect360 | Content & Research | Humanoid robot intelligence data |
| WeatherAPI MCP | Content & Research | Weather data for AI agents |
| AirLabs | Content & Research | Flight tracking and airport data |
| Chuhching | Financial Data | Financial data integration |
| DDG Agent Payable Services | Financial Data | Agent micropayments |
| Gatewards | Financial Data | Agent spend governance & x402 settlement |
| SQD Portal | Financial Data | Multi-chain onchain data query |
| Valid — Vehicle Identity | Financial Data | Vehicle identification and history |
| Easy Predict | Financial Data | Predictive analytics platform |
| Backengine MCP | Development | Backend engine for MCP server dev |
| Enigmata | Development | Encryption and privacy tools |
| Electron Stagewright | Development | Electron app automation (Playwright-style) |
| Requesty MCP Gateway | Development | 300+ LLM provider routing MCP endpoint |
| mcp-launch-review | Development | Launch review for MCP/x402 tools |
| TinyZKP | Security & Privacy | STARK proof receipts for agents |
| Fixzi MCP | Productivity | Issue tracking & bug fix workflow |
| Cairn | Productivity | Repo-native task graph for AI agents |
| Touchpoint | Productivity | Desktop accessibility API for AI agents |
| Remnus | Productivity | Workflow automation platform |
| Turbo Job Apply | Productivity | AI-powered job search & application |
| Church Website Editor | Productivity | Website editing for faith organizations |
| Pixelvault | Content Creation | Digital asset & image management |
| OnBrand by SlideSpeak | Content Creation | Brand asset MCP (logos, colors, fonts) |
| Linkdeal MCP | Marketing | Deal discovery & promotion tools |
| Infino | Analytics & BI | Multi-modal search over object storage |

---

## New This Week (June 26, 2026 — morning sweep)

### 6 new servers from mcp.so Feed

| Server | Category | Description |
|--------|----------|-------------|
| MentionsAPI ★ New | Marketing/GEO | Track brand mentions, ranks, and citations across ChatGPT, Claude, Gemini, Perplexity, Google AI Overviews, AI Mode, and Bing Copilot. MCP-native, pay-as-you-go, $1 free signup credit. Essential for operators investing in AI-engine visibility and brand monitoring. `npx -y @mentionsapi/mcp` |
| Yapp ★ New | Productivity/Publishing | Turn "build me a page" into a live URL. Connect once (browser OAuth or token) and your AI can publish HTML, PDFs, ZIP sites, images, and landing pages to a public slug.yapp.page URL in seconds. Essential for operators who need AI agents to ship pages, proposals, and reports instantly. `https://yapp.page/mcp` |
| Note2IT ★ New | Productivity/Knowledge | Keep work in notebooks, sections, and nested pages with a fast slash-command editor. Record meetings for automatic transcripts + structured summaries with action items. Connect Claude over MCP so AI can search, read, and make precise, undoable edits to pages. Essential for operators managing knowledge work with AI agent access. `npx -y @note2it/mcp` |
| Advanced Patent Search ★ New | Research/Legal | PatSnap Advanced Patent Search MCP — semantic, similarity, image, patent-number, nested-query, analytics, and sequence search. Connects AI agents to professional patent intelligence. Essential for IP-heavy operators and innovation teams. `https://mcp.patsnap.com` |
| Chaiz MCP ★ New | Commerce/Insurance | Search live vehicle service contract (extended warranty) quotes by VIN, license plate, or make/model/year — with plan prices, coverage tiers, expert ratings, and checkout links. Read-only, works anonymously. Niche but valuable for fleet operators and automotive businesses. `npx -y @chaiz/mcp` |
| OrcaLayer MCP ★ New | Financial Data/Crypto | Polymarket whale tracking and smart-money analytics MCP. Filtered leaderboard (airdrop-farmers excluded), hedge detection, NegRisk correction, and unique Ukraine territorial markets with ISW frontline overlay. 5 tools, 4 prompts, 3 resources. `npx mcp-remote https://orcalayer.com/mcp` |

---

## New This Week (June 27, 2026 — morning sweep)

### 5 new MCP servers from mcp.so Feed + mcpservers.org /latest

| Server | Category | What It Does |
|--------|----------|-------------|
| GTmetrix MCP ★ New | Development | Web performance testing — page speed, Core Web Vitals, performance metrics |
| superserve-sandbox ★ New | Development | Isolated cloud sandboxes (Firecracker microVMs) for agent code execution |
| web-pilot ★ New | Development | 8 web tools: fetch, search, extract links/metadata, sitemaps, RSS, URL checks |
| Sociality MCP ★ New | Marketing | Cross-platform social media analytics (FB, X, IG, YT, LinkedIn, TikTok) |
| AgentDocs ★ New | Productivity | Agent-first office suite — Docs, Sheets, Slides, Database, Drive via MCP |

**Key Trends:** Web performance testing (GTmetrix), social media analytics (Sociality), and agent-native office suites (AgentDocs) are expanding MCP's reach into core business operations. Sandbox execution (superserve) signals growing demand for secure agent code environments.

---

## New This Week (June 27, 2026 — afternoon sweep)

### 13 new MCP servers from mcpservers.org /all (pages 1–3)

| Server | Category | What It Does |
|--------|----------|-------------|
| GSC SEO MCP ★ New | Marketing/SEO | Google Search Console MCP — SEO audits, keyword insights, URL inspection, sitemap management for AI agents. Essential for SEO operators. `github.com/samalyxx/gsc-seo-mcp` |
| Sleepwalker ★ New | Marketing/GEO | AI Visibility & Content Intelligence — inspect AI answers, citations, page content, trends, and saved reports. GEO/AEO monitoring for AI-driven marketing operators. |
| ReefAPI MCP ★ New | Data/Integration | 160+ live web-data APIs (search, social, e-commerce, real estate, jobs, finance) — clean JSON, free tier. One MCP server for broad data integration. |
| PDF2MD MCP ★ New | Productivity/Documents | Hosted MCP converting PDFs into clean, LLM-ready Markdown with tables, LaTeX formulas, and OCR (MinerU + Docling). Essential for operators processing documents in AI workflows. |
| Upriver MCP ★ New | Content/Research | Breakout trending topics in tech, sports & politics with citations. Content research MCP for operators tracking market trends. |
| Grist MCP ★ New | Productivity/Data | Turn spreadsheets running your business into secure applications. Spreadsheet-to-app MCP for operators managing business data. |
| Hindsight-MemPalace ★ New | Memory/Knowledge | Self-hosted long-term memory for AI agents — MCP server with hierarchical recall over pgvector. For operators running persistent agent memory infrastructure. |
| Reflex MCP ★ New | Dev/Browser | Faster, parallel browser for AI agents — drives your own Chrome with fewer round trips and tokens than Playwright. Browser automation MCP for operators. |
| Railway MCP ★ New | Dev/Infra | Natural language interaction with Railway projects and infrastructure — create, manage, and deploy via AI agents. |
| Kanbaruu MCP ★ New | Productivity | Markdown-native project board for AI agents — read, create, and check off tasks. Agent-friendly task management. |
| HC Stark ★ New | Security/Compliance | Hosted MCP for transparent STARK proof receipts — agents mint and verify cryptographic receipts for supported workflows. Enterprise compliance MCP. |
| Kubernetes MCP (blankcut) ★ New | Dev/Infra | Claude Kubernetes MCP in Go — integrates with ArgoCD, GitLab, Claude AI for advanced K8s control and deployment automation. |
| Shadcn MCP ★ New | Design/Dev | Shadcn AI builder — create, refine, and convert Figma designs into production-ready UI blocks. Design-to-code MCP for product teams. |

**Key Trends:** SEO tools (GSC SEO MCP), GEO/AEO monitoring (Sleepwalker), document processing (PDF2MD), and agent memory infrastructure (Hindsight-MemPalace) dominated this afternoon's discovery. Data integration (ReefAPI — 160+ APIs) and productivity tools (Grist, Kanbaruu) continue expanding MCP's business operations footprint.

### 7 new MCP servers from mcpservers.org /all (pages 1–4)

| Server | Category | What It Does |
|--------|----------|-------------|
| Rampify MCP ★ New | Marketing/SEO | SEO MCP server: crawl your site, find AI-visibility gaps, and ship the fix from your coding agent. `github.com/rampify-dev/rampify-mcp` ★2 |
| PipeTable MCP ★ New | Data/Analytics | Query local CSV, Parquet, JSON and TSV files with real SQL via DuckDB. Ground-truth data access for AI agents. `github.com/melihbirim/pipetable` ★1 |
| HookSense MCP ★ New | Dev/Webhooks | Webhook & callback layer for AI agents — create callbacks, wait_for_callback instead of polling, verify signatures over MCP. `github.com/ozers/hooksense-mcp` ★1 |
| Monet MCP ★ New | Dev/Memory | Local-first, state-centric memory for coding agents — remembers project conventions and preferences. 100% local over MCP. |
| ShareBench MCP ★ New | Agent Marketplace | Hosted MCP — search and pull AI skills, agents, prompts & playbooks. Connect once at `mcp-public.sharebench.ai`. |
| Ambix MCP ★ New | Product Management | Product team workspace — makes team direction, priorities, and conviction persistent and accessible to AI clients via MCP. |
| Infino MCP ★ New | Data/Infra | Keyword, vector, hybrid, and SQL retrieval over data on object storage for AI agents. |

**Key Trends:** AI visibility tools (Rampify for SEO, Sleepwalker for GEO) continue expanding as operators shift focus from traditional SEO to AI-engine discoverability. Agent infrastructure (HookSense webhooks, Monet local memory, ShareBench agent marketplace) shows the ecosystem maturing beyond data access into agent-native middleware.

## New This Week (June 29, 2026 — morning sweep)

### 20 new servers from mcp.so Feed

| Server | Category | Description |
|--------|----------|-------------|
| Chytrý Rejstřík ★ New | Finance/Business Intel | Czech business intelligence — search, verify, monitor companies from 20+ public sources. |
| CryptoGate ★ New | Finance/Crypto | Non-custodial crypto payments for AI agents — balances, invoices, payment links. |
| Delegum ★ New | Finance/Legal | 42 Spanish tax, labor law & finance tools. No registration, no API key. |
| Fylings MCP ★ New | Finance/Business Intel | African company intelligence — search, verify, monitor across official registries. |
| SIMA MCP Server ★ New | Finance/Crypto | Solana AI agent protection platform — discover platform capabilities via MCP. |
| Web3Agent ★ New | Finance/Web3 | Web3 proxy for AI agents — EVM, DeFi, swaps, bridges, wallet management. |
| AirLabs MCP Server ★ New | Research/Travel | Real-time aviation data — flights, airports, schedules, delays. |
| Minha Morada ★ New | Research/Real Estate | 181K+ Portuguese real estate listings across 18 districts (Imovirtual, Idealista, RE/MAX). |
| Blocktrust TrustScan ★ New | Compliance/Security | Digital trust verification — identities, domains, phishing detection, cryptographic signing. |
| Agent Guild ★ New | Dev/Agent Infra | Reputation & trust layer for autonomous AI agents — vet, vouch, delegate safely. |
| GGWP API Hub ★ New | Dev/API | 189 pay-per-call API endpoints via x402 protocol + USDC on Base. |
| Reqly ★ New | Dev/API | API client for AI agents — collections, flows, mocking, CI export. Zero cloud dependency. |
| Statewave ★ New | Dev/Agent Infra | Open-source state management & persistence for AI agents across sessions. |
| Vynix MCP Server ★ New | Dev/QA | Website feedback, visual bug reporting & annotation for AI coding assistants. |
| Version Pill ★ New | Dev/Infra | Version management MCP for AI agents — track dependencies and releases. |
| Formly ★ New | Productivity | Create & publish forms from AI agents in plain language. |
| MemPlato ★ New | Productivity/Mobile | Personal MCP on Android (Termux) — 29 tools, all local storage. |
| Valossa Assistant ★ New | Creative/Video | Multimodal video AI — ingestion to structured intelligence, decade of video R&D. |
| AdMob MCP ★ New | Marketing/Ads | Google AdMob management, mediation, revenue analysis & A/B experiments. |
| Memory Engine ★ New | Memory/Knowledge | Atomic memory model with multi-factor ranking, decay, and reinforcement. |
| memo ★ New | Memory/Knowledge | 100% local AI memory (Apple Silicon/Linux) — no cloud, privacy-first. |
| CCHub ★ New | Dev/Tooling | Claude Code config manager — desktop app for MCP servers, skills, plugins. |
| Bambu Printer MCP ★ New | Manufacturing/Hardware | 3D printing automation for Bambu Lab printers via MCP. |
| Chia Health MCP ★ New | Healthcare/Compliance | HIPAA telehealth ops — intake, prescriptions, payment automation. |

**Key Trends:** Healthcare operations MCPs emerging (Chia Health — first HIPAA telehealth MCP). Privacy-first memory infrastructure growing (memo — 100% local, no cloud). Developer tooling maturing (CCHub desktop app). Hardware automation expanding beyond software (Bambu 3D printers). Regional business intelligence MCPs expanding rapidly (Czech Republic, Africa, Spain, Portugal). Agent-native infrastructure growing: reputation layers (Agent Guild), state management (Statewave), crypto payment rails (CryptoGate, GGWP). Mobile MCP (MemPlato on Android) signals the extension of MCP beyond desktop agents. Video AI goes end-to-end (Valossa) beyond simple search/transcription.

---

## New This Week (June 29, 2026 — afternoon sweep)

### 7 new servers from mcp.so Feed

| Server | Category | Description |
|--------|----------|-------------|
| Bitcoin Monetary Data ★ New | Finance/Crypto | Honest monetary data — CPI, M2 money supply, Bitcoin vs dollar. No API key. |
| Ko Financial Data ★ New | Finance/Market Data | SEC, 13F, insider, congress & macro data — 24 tools. Free tier 200 calls/day. |
| Clypra ★ New | Finance/Crypto | x402 USDC micropayments on Base for AI agent transactions. |
| Arcade Trading ★ New | Finance/Trading | Trading data and market access for AI agents. |
| Vublox Sports ★ New | Content/Sports | Live football scores, match summaries, fan clip links — no API key. |
| Trad Tune Explorer ★ New | Content/Music | Traditional folk music data from The Session — tunes, recordings, sets, musicians. |
| Mcp Midasflow ★ New | Dev/Data Infra | Data flow orchestration and pipeline automation for AI agents. |

**Key Trends:** Financial data MCPs continue diversifying beyond stocks/crypto into monetary economics (Bitcoin Monetary Data) and institutional filings (Ko Financial). Sports and music data MCPs signal the expansion into niche content verticals. Agent payment infrastructure (Clypra/x402) remains a growing category as the agent economy matures.

---

## New This Week (June 28, 2026 — afternoon sweep)

### 18 new servers from mcp.so Feed

| Server | Category | Description |
|--------|----------|-------------|
| SIXTA Connect ★ New | Analytics/Database | DBRE-grade SQL analysis for PostgreSQL & MySQL — paste query, get named findings with severity and fixes. Zero-connection. |
| Opencloudcosts ★ New | Finance/FinOps | Multi-cloud pricing MCP — AWS, GCP, Azure list prices + enterprise rates (RIs, Savings Plans, CUDs). No credentials needed. |
| Aikount ★ New | Finance/Accounting | Spanish accounting MCP — invoices, OCR expense PDFs, bank reconciliation, quarterly VAT (Modelo 303). For autónomos/SMEs. |
| Agentready ★ New | Productivity/Knowledge | Make any website queryable by AI agents — index sites, get cited RAG answers. |
| What2post ★ New | Marketing/Social | Social media content planning and publishing for AI agents. |
| Catchintent ★ New | Marketing/Sales | Intent catching and lead identification for AI agents. |
| Datahyena ★ New | Analytics/Data | Data analysis and processing for AI agents. |
| Edata4you ★ New | Analytics/Data | Data service platform for AI agents. |
| AEO Tool ★ New | Marketing/GEO | AI Engine Optimization — optimize content for AI discoverability. |
| ABAP MCP ★ New | Dev/SAP | SAP ABAP development via MCP — read/write ABAP, run syntax checks over ADT API. |
| BVCC Agent Wallet ★ New | Finance/Crypto | Non-custodial crypto agent wallet — balances, sends, swaps on Uniswap across 4 chains with spend limits. |
| SVGFarm ★ New | Dev/Creative | Search SVG icon packs and fetch markup from coding agents. |
| JanusMCP ★ New | Dev/Infra | Local multi-account MCP broker — switch identity without reconnecting. |
| Chain Context Mcp ★ New | Blockchain | Blockchain context provider for AI agents. |
| AI Tool Directory ★ New | Research/Discovery | Query 2,000+ AI tools — search, compare, find alternatives. Public, no API key. |
| Wax Seal ★ New | Security/Compliance | Cryptographic identity verification — on-chain seals, Ed25519 signatures, human-signed approvals. |
| Graphlens ★ New | Analytics/Visualization | Graph-based data visualization and analysis for AI agents. |
| Fuse Network ★ New | Blockchain | Blockchain network integration for AI agents. |

**Key Trends:** Database tooling goes zero-connection (SIXTA), cloud FinOps gets credentialless pricing (Opencloudcosts), regional business MCPs growing (Aikount — Spanish accounting), agent governance infrastructure expanding (Wax Seal, JanusMCP).

---

## New This Week (July 4, 2026 — morning sweep)

### 19 new servers from mcp.so Feed

| Server | Category | Description |
|--------|----------|-------------|
| OilPriceAPI MCP ★ New | Financial Data | See main catalog entry above |
| Earningsprism ★ New | Financial Data | See main catalog entry above |
| Agent Signals ★ New | Financial Data | See main catalog entry above |
| Fleets MCP ★ New | Analytics & BI | See main catalog entry above |
| Crustdata MCP ★ New | Content & Research | See main catalog entry above |
| ENTIA Entity Verification ★ New | Content & Research | See main catalog entry above |
| VerityLayer ★ New | Compliance & Regulatory | See main catalog entry above |
| ChronoVerify ★ New | Compliance & Regulatory | See main catalog entry above |
| nuzur ★ New | Development | See main catalog entry above |
| Docguard ★ New | Development | See main catalog entry above |
| Planka V2 MCP ★ New | Development | See main catalog entry above |
| Founders OS ★ New | Productivity | See main catalog entry above |
| RadMail ★ New | Productivity | See main catalog entry above |
| Paigy ★ New | Productivity | See main catalog entry above |
| Truepath Recorder ★ New | Productivity | See main catalog entry above |
| Pepys MCP ★ New | Content Creation | See main catalog entry above |
| Cortex Memory MCP ★ New | Memory & Knowledge | See main catalog entry above |
| Psychopathia Machinalis ★ New | Memory & Knowledge | See main catalog entry above |
| Ecoexperten Energieausweis ★ New | Commerce | See main catalog entry above |

**Key Trends:** Business-operator infrastructure MCPs dominate this sweep — Founders OS (whole-business interface), RadMail (email OS for agents), and Crustdata (B2B intelligence) signal the shift from developer-tool MCPs to operator-facing business automation. Trust and verification MCPs (VerityLayer, ChronoVerify, ENTIA) show growing demand for AI agent guardrails in production. Multi-site analytics (Fleets) and commodity data (OilPriceAPI) expand the operational data surface available through MCP. Agent-human communication bridges (Paigy, Truepath Recorder) address the human-in-the-loop gap.

---

## New This Week (July 4, 2026 — evening sweep)

### 5 new servers from mcpservers.org

| Server | Category | Description |
|--------|----------|-------------|
| Plaud MCP ★ New | Communication | See [Integration Guide](/hermes/mcp/servers/external/plaud-mcp/) |
| Astucia Wiki MCP ★ New | Memory & Knowledge | See [Integration Guide](/hermes/mcp/servers/external/astucia-wiki-mcp/) |
| Design Context Bridge ★ New | Design & Product | See [Integration Guide](/hermes/mcp/servers/external/design-context-bridge-mcp/) |
| Synaplan Multimodal Gateway ★ New | Productivity | Multimodal MCP gateway — early stage, watched |
| Creed Space ★ New | AI Safety & Security | Constitutional-AI guardrails — infra-layer |

**Key Trends:** Recording intelligence emerges as a distinct MCP category — Plaud MCP follows Granola (July 3), signaling that "queryable meeting memory" is becoming table stakes. Agent-first wikis (Astucia) and native Figma readers (Design Context Bridge) represent a design-and-knowledge tool stack purpose-built for AI-assisted workflows. Combined with Mowgli (July 3), the design-to-code pipeline is becoming fully MCP-native.

---

## New This Week (July 1, 2026 — PM evening sweep)


## New This Week (July 12, 2026 — mcp.so/feed sweep)

14 new business-relevant MCP servers from the mcp.so/feed. GitHub and mcpservers.org were unavailable (API rate-limiting, SPA client-rendering). Full scan report: [scan-results-2026-07-12.md](/hermes/mcp/servers/external/scan-results-2026-07-12/)

**Integration guides created (6):** Substack Publisher, Financial News, Seiche Finance, shieldly-io AWS Security, CrustAPI Live Search, Agent Coherence

**Index-only additions (8):** EU Textile Sustainability, Selenium MCP, MCP Time Server, E2LLM/SiFR Browser, Prompt Improver, HelpScout-ProductLift Triangulator, BreckenWander Travel, deman-maker MCP Marketplace

**Trends:** Financial data MCPs accelerating (2 new), compliance MCPs emerging (2 new), agent governance maturing (Agent Coherence, Human-in-the-loop), live search category expanding (CrustAPI).


### 5 new servers from GitHub API (topic:mcp-server created >2026-07-01T12:00)

| Server | Category | Description |
|--------|----------|-------------|
| vrules ★ New | Compliance/Security | Open-source agent-governance & LLM guardrails framework — vector-enabled rules engine for MCP proxying, policy-as-code, conditional organizational memory, and browser/WASM execution. Vendor-neutral. `github.com/ops-ping/vrules` |
| Hermes Plant MCP Server ★ New | Finance/Quant | Deterministic finance & quant APIs over x402 — provably correct financial calculations, quantitative models, and market analytics with cryptographic payment rails. `github.com/JesseGdotIO/hermesplant-mcp-server` |
| Google Analytics MCP ★ New | Analytics | Free, open-source GA4 MCP server (44 tools) — traffic, funnels, real-time & e-commerce reporting via natural language. MIT license. `github.com/yusofansari/google-analytics-mcp` |
| Google Ads MCP (Open Source) ★ New | Marketing | Free, open-source Google Ads MCP server (57 tools) — campaign management, keyword optimization, GAQL querying, competitive analysis. MIT license. `github.com/yusofansari/google-ads-mcp` |
| Google Search Console MCP (Open Source) ★ New | Marketing/SEO | Free, open-source GSC MCP server (43 tools) — search analytics, indexing checks, cannibalization detection, sitemap management. MIT license. `github.com/yusofansari/google-search-console-mcp` |

**Key Trends:** Agent governance infrastructure (vrules) emerges as a distinct MCP category — operators need programmable guardrails for production AI deployments. Google marketing suite goes open-source (yusofansari's GA4 + Ads + GSC trio) signals growing demand for zero-cost, no-vendor-lock-in marketing MCPs. Deterministic finance with cryptographic payment rails (Hermes Plant over x402) shows convergence of DeFi-grade verifiability and traditional quant workflows.

---

## Ecosystem Stats

- **Total MCP servers tracked:** 22,663 (mcp.so), 9,300 (mcpservers.org)
- **Official servers:** 43+ (from Google, GitHub, Cloudflare, Anthropic, Microsoft, MiniMax, ZenML, Flatland, etc.)
- **CorpusIQ connectors:** 37+ (the most comprehensive business data MCP server)
- **Categories represented:** 30+ (Finance, Analytics, CRM, Commerce, Dev, Marketing, Content Creation, Gov/Intelligence, Media, Legal, HR, Security/Compliance, Memory, etc.)
- **New this sweep (July 4 morning):** 19 new MCP servers — from mcp.so Feed (25 scanned, 22 genuinely new, 3 already catalogued)
- **Cumulative since June 9:** 502 MCP servers catalogued across 36 sweeps

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

*Powered by CorpusIQ  --  monitoring the MCP ecosystem for business operators*
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*


## All External MCP Servers Pages

- [Agent Coherence MCP — Multi-Agent File Conflict Prevention](/docs/hermes/mcp/servers/external/agent-coherence-mcp.html)
- [AI Localization Agent MCP — Integration Guide](/docs/hermes/mcp/servers/external/ai-localization-agent/index.html)
- [AI Visibility Analytics MCP — Brand Monitoring Across AI Search Engines](/docs/hermes/mcp/servers/external/ai-visibility-analytics.html)
- [AI2Fin Tax MCP — Global Tax Rates for 50+ Countries](/docs/hermes/mcp/servers/external/ai2fin-tax-mcp.html)
- [AICryptoVault MCP — Agent-Managed Crypto Treasury](/docs/hermes/mcp/servers/external/aicryptovault.html)
- [Aikount](/docs/hermes/mcp/servers/external/aikount.html)
- [Alpha Vantage MCP — Financial Market Data for AI Agents](/docs/hermes/mcp/servers/external/alphavantage-mcp.html)
- [AppAmbit MCP — Integration Guide](/docs/hermes/mcp/servers/external/appambit-mcp/index.html)
- [AppSigma App Store Data MCP — ASO & App Analytics for AI Agents](/docs/hermes/mcp/servers/external/appsigma-app-store-data-mcp.html)
- [Astucia Wiki MCP — AI-Enabled Team Wiki for Hermes Agent](/docs/hermes/mcp/servers/external/astucia-wiki-mcp.html)
- [BillingServ MCP — Invoice & Customer Management for AI Agents](/docs/hermes/mcp/servers/external/billingserv.html)
- [Booyah Index MCP — Southeast Asia Business Directory for AI Agents](/docs/hermes/mcp/servers/external/booyah-index.html)
- [Cal.com MCP — Scheduling Automation for AI Agents](/docs/hermes/mcp/servers/external/calcom-mcp.html)
- [Coding Agent Project Management MCP — 71 Tools for AI-Driven Development](/docs/hermes/mcp/servers/external/coding-agent-pm-mcp.html)
- [Co-Invest MCP — AI-Powered Investment Management](/docs/hermes/mcp/servers/external/coinvest-mcp.html)
- [ComparEdge LLM Cost MCP — Integration Guide](/docs/hermes/mcp/servers/external/comparedge-llm-cost-mcp.html)
- [Confluent MCP — Apache Kafka for AI Agents](/docs/hermes/mcp/servers/external/confluent-mcp/index.html)
- [Container Tracking MCP — Ocean Freight Visibility for AI Agents](/docs/hermes/mcp/servers/external/container-tracking-mcp.html)
- [CrustAPI MCP — Live Google Search for AI Agents](/docs/hermes/mcp/servers/external/crustapi-mcp.html)
- [Crustdata](/docs/hermes/mcp/servers/external/crustdata/index.html)
- [dbridge MCP — Secure Natural Language SQL for AI Agents](/docs/hermes/mcp/servers/external/dbridge-mcp.html)
- [Design Context Bridge MCP — Figma-to-Code for Hermes Agent](/docs/hermes/mcp/servers/external/design-context-bridge-mcp.html)
- [Drumbeats MCP — Uptime & Cron Monitoring for AI Agents](/docs/hermes/mcp/servers/external/drumbeats-mcp.html)
- [Elasticsearch MCP — Full-Text Search & Observability for AI Agents](/docs/hermes/mcp/servers/external/elasticsearch-mcp/index.html)
- [Integration Guide: Eleata E-Invoice MCP — EU E-Invoice Validation for AI Agents](/docs/hermes/mcp/servers/external/eleata-einvoice.html)
- [Financial News MCP — Real-Time Market Data for AI Agents](/docs/hermes/mcp/servers/external/financial-news-mcp.html)
- [Fleets](/docs/hermes/mcp/servers/external/fleets/index.html)
- [Founders Os](/docs/hermes/mcp/servers/external/founders-os/index.html)
- [Google Maps Email Extractor — Maps-to-Leads Pipeline for AI Agents](/docs/hermes/mcp/servers/external/google-maps-email-extractor.html)
- [Google Search Console MCP — Integration Guide](/docs/hermes/mcp/servers/external/google-search-console-mcp.html)
- [Granola MCP — AI Meeting Notes for Hermes Agent](/docs/hermes/mcp/servers/external/granola-mcp.html)
- [Hermes Plant MCP Server — Deterministic Finance & Quant APIs Integration Guide](/docs/hermes/mcp/servers/external/hermesplant-mcp-server.html)
- [Horizon AI Intelligence MCP — Integration Guide](/docs/hermes/mcp/servers/external/horizon-mcp/index.html)
- [HPSILab Quant Finance MCP — Options Analytics & Monte Carlo](/docs/hermes/mcp/servers/external/hpsilab-quant.html)
- [HTML Pub MCP — Integration Guide](/docs/hermes/mcp/servers/external/htmlpub-mcp/index.html)
- [Kalshi MCP — Prediction Markets for AI Agents](/docs/hermes/mcp/servers/external/kalshi-mcp.html)
- [Kvasir Legal MCP — EU Law Grounding for AI Agents](/docs/hermes/mcp/servers/external/kvasir-legal.html)
- [Launch Fast MCP — Amazon FBA Analytics for AI Agents](/docs/hermes/mcp/servers/external/launch-fast.html)
- [LaunchDarkly MCP — Feature Flag Management for AI Agents](/docs/hermes/mcp/servers/external/launchdarkly-mcp/index.html)
- [Lawstronaut MCP — Global Legal & Regulatory Document Access for AI Agents](/docs/hermes/mcp/servers/external/lawstronaut-mcp.html)
- [LLM Observability MCP (LangTrace) — Open Source Monitoring for AI Agents](/docs/hermes/mcp/servers/external/llm-observability-mcp.html)
- [Maqami Travel MCP — Hotel Booking for AI Agents](/docs/hermes/mcp/servers/external/maqami-travel.html)
- [MCP Email Server — IMAP/SMTP Email for AI Agents](/docs/hermes/mcp/servers/external/mcp-email-server/index.html)
- [MCP Long-Term Memory (GraphRAG) — Persistent Agent Memory](/docs/hermes/mcp/servers/external/mcp-long-term-memory.html)
- [MCP Notify — Monitor the MCP Registry for New Servers](/docs/hermes/mcp/servers/external/mcp-notify/index.html)
- [Mentionsapi](/docs/hermes/mcp/servers/external/mentionsapi.html)
- [Meta Business MCP — WhatsApp Business Cloud API Integration Guide](/docs/hermes/mcp/servers/external/meta-business-mcp.html)
- [Microsoft Planner MCP — Integration Guide](/docs/hermes/mcp/servers/external/microsoft-planner-mcp.html)
- [Monday.com MCP — Project Management for AI Agents](/docs/hermes/mcp/servers/external/mondaycom-mcp/index.html)
- [Mowgli MCP — Integration Guide](/docs/hermes/mcp/servers/external/mowgli-mcp.html)
- [NaturalMelo MCP — AI Content Detection for Agents](/docs/hermes/mcp/servers/external/naturalmelo-mcp.html)
- [Neuron MCP Server](/docs/hermes/mcp/servers/external/neuron.html)
- [Note2It](/docs/hermes/mcp/servers/external/note2it.html)
- [Integration Guide: NotHumanSearch — AI Agent Search Engine for Operator Visibility](/docs/hermes/mcp/servers/external/nothumansearch.html)
- [Odoo MCP — Zero-Setup ERP Connector for AI Agents](/docs/hermes/mcp/servers/external/odoo-mcp.html)
- [Opencloudcosts](/docs/hermes/mcp/servers/external/opencloudcosts.html)
- [OpenTweet MCP — Twitter/X Management for AI Agents](/docs/hermes/mcp/servers/external/opentweet-mcp.html)
- [Periscope MCP — Playwright-Powered Website Testing for AI Agents](/docs/hermes/mcp/servers/external/periscope-mcp.html)
- [pipeworx-io Business Data Suite — Industrial MCP Wrappers](/docs/hermes/mcp/servers/external/pipeworx-business-data.html)
- [Plaud MCP — AI Recording Integration for Hermes Agent](/docs/hermes/mcp/servers/external/plaud-mcp.html)
- [Podcast Sponsorship Discovery MCP — Lead Generation from 4M+ Sponsorships](/docs/hermes/mcp/servers/external/podcast-sponsorship-mcp.html)
- [Pretensor MCP — Knowledge Graphs from Database Introspection](/docs/hermes/mcp/servers/external/pretensor-mcp/index.html)
- [Protonmail-rs — Proton Mail MCP Server Integration Guide](/docs/hermes/mcp/servers/external/protonmail-rs.html)
- [qlows MCP — Tender & RFP Search for AI Agents](/docs/hermes/mcp/servers/external/qlows-mcp-tender-search.html)
- [Radmail](/docs/hermes/mcp/servers/external/radmail/index.html)
- [SaaS & AI Pricing API MCP — Competitive Intelligence for 490+ Tools](/docs/hermes/mcp/servers/external/saas-pricing-mcp.html)
- [SaferAgenticAI MCP — AI Safety Governance for Agentic Coding](/docs/hermes/mcp/servers/external/saferagenticai-mcp.html)
- [MCP Server Scan Results — 2026-06-25](/docs/hermes/mcp/servers/external/scan-results-2026-06-25.html)
- [MCP Server Scan Results — 2026-06-26](/docs/hermes/mcp/servers/external/scan-results-2026-06-26.html)
- [MCP Server Scan Results — 2026-06-28 (Afternoon)](/docs/hermes/mcp/servers/external/scan-results-2026-06-28-afternoon.html)
- [MCP Server Scan Results — 2026-06-28 (Evening)](/docs/hermes/mcp/servers/external/scan-results-2026-06-28-evening.html)
- [MCP Server Scan Results — 2026-06-30](/docs/hermes/mcp/servers/external/scan-results-2026-06-30.html)
- [MCP Server Scan Results — 2026-07-01 (PM Evening Update)](/docs/hermes/mcp/servers/external/scan-results-2026-07-01-evening.html)
- [MCP Server Scan Results — 2026-07-01 (PM Update)](/docs/hermes/mcp/servers/external/scan-results-2026-07-01-update.html)
- [MCP Server Scan Results — 2026-07-01](/docs/hermes/mcp/servers/external/scan-results-2026-07-01.html)
- [MCP Server Discovery — July 2, 2026 (Evening Scan)](/docs/hermes/mcp/servers/external/scan-results-2026-07-02-evening.html)
- [MCP Server Discovery — July 2, 2026 (Afternoon Update)](/docs/hermes/mcp/servers/external/scan-results-2026-07-02-update.html)
- [MCP Server Scan Results — 2026-07-02](/docs/hermes/mcp/servers/external/scan-results-2026-07-02.html)
- [MCP Server Discovery — July 3, 2026 (Evening Supplement)](/docs/hermes/mcp/servers/external/scan-results-2026-07-03-evening.html)
- [MCP Server Discovery — July 3, 2026](/docs/hermes/mcp/servers/external/scan-results-2026-07-03.html)
- [MCP Server Discovery — July 4, 2026 (Evening)](/docs/hermes/mcp/servers/external/scan-results-2026-07-04-evening.html)
- [MCP Server Scan Results — July 12, 2026](/docs/hermes/mcp/servers/external/scan-results-2026-07-12.html)
- [MCP Server Scan Results — July 13, 2026](/docs/hermes/mcp/servers/external/scan-results-2026-07-13.html)
- [MCP Server Scan Supplement — July 14, 2026 (Evening)](/docs/hermes/mcp/servers/external/scan-results-2026-07-14-supplement.html)
- [MCP Server Scan Results — July 14, 2026](/docs/hermes/mcp/servers/external/scan-results-2026-07-14.html)
- [MCP Server Scan Supplement — July 15, 2026 (Evening)](/docs/hermes/mcp/servers/external/scan-results-2026-07-15-supplement.html)
- [MCP Server Scan — July 15, 2026](/docs/hermes/mcp/servers/external/scan-results-2026-07-15.html)
- [Scrivener MCP — Integration Guide](/docs/hermes/mcp/servers/external/scrivener-mcp.html)
- [Seiche Finance MCP — US Money Market Stress Testing](/docs/hermes/mcp/servers/external/seiche-finance-mcp.html)
- [SentiSense MCP — Market Intelligence for AI Agents](/docs/hermes/mcp/servers/external/sentisense.html)
- [SEOforGPT MCP — AI Visibility & Generative Engine Optimization](/docs/hermes/mcp/servers/external/seoforgpt.html)
- [Shieldly AWS Security MCP — IAM & CloudFormation Analysis](/docs/hermes/mcp/servers/external/shieldly-aws-mcp.html)
- [Sixta Connect](/docs/hermes/mcp/servers/external/sixta-connect.html)
- [Snowflake MCP — Data Warehouse Queries for AI Agents](/docs/hermes/mcp/servers/external/snowflake-mcp/index.html)
- [SPM — Structured Project Memory MCP for Agent Governance](/docs/hermes/mcp/servers/external/spm-structured-project-memory.html)
- [Substack Publisher MCP — Content Analytics for AI Agents](/docs/hermes/mcp/servers/external/substack-publisher-mcp.html)
- [Tubask MCP — Hosted YouTube Intelligence for AI Agents](/docs/hermes/mcp/servers/external/tubask-mcp.html)
- [Transform MCP (Unstructured) — Document Parsing for AI Agents](/docs/hermes/mcp/servers/external/unstructured-transform-mcp.html)
- [Userbrain MCP — UX Research Analytics for AI Agents](/docs/hermes/mcp/servers/external/userbrain.html)
- [Veritylayer](/docs/hermes/mcp/servers/external/veritylayer/index.html)
- [VoIP.ms MCP — Business Telephony for AI Agents](/docs/hermes/mcp/servers/external/voipms-mcp.html)
- [vrules — Agent Governance & LLM Guardrails Integration Guide](/docs/hermes/mcp/servers/external/vrules.html)
- [Webotee Amazon MCP — Amazon Seller Intelligence for AI Agents](/docs/hermes/mcp/servers/external/webotee-amazon-mcp.html)
- [XActions MCP — X/Twitter Automation Without API Fees](/docs/hermes/mcp/servers/external/xactions-mcp/index.html)
- [Yapp](/docs/hermes/mcp/servers/external/yapp.html)
