# MCP Server Directory Scan — June 25, 2026
## Comprehensive scan of mcp.so and mcpservers.org for new business-relevant MCP servers

---

## SOURCE 1: MCP.SO (22,663+ total servers)

### Methodology
- Scraped the servers listing page via curl, extracted from Next.js RSC payload
- Successfully extracted 47 servers with full metadata (name, description, URL, install commands, dates)
- 
- 

### Business-Relevant Servers Found on mcp.so

#### FINANCE
1. **kospi-kosdaq-stock-server** (Feb 2025)
   - Provides KOSPI/KOSDAQ stock data using FastMCP
   - URL: https://github.com/dragon1086/kospi-kosdaq-stock-server
   - Tags: finance, Korean stock market
   - Business relevance: Regional stock data for Korean market operators

#### ANALYTICS / RESEARCH & DATA
2. **serper-mcp-server** (Apr 2025)
   - Google Search API integration via Serper
   - Install: `uvx serper-mcp-server`
   - URL: https://github.com/garymengcom/serper-mcp-server
   - Business relevance: Web research and competitive intelligence

3. **jina-mcp-tools** (Apr 2025)
   - Integrates Jina AI Search Foundation APIs
   - Install: `npx jina-mcp-tools`
   - URL: https://github.com/PsychArch/jina-mcp-tools
   - Business relevance: AI-powered web search and content extraction

4. **perplexity** (Mar 2025)
   - Perplexity API connector for web search within MCP
   - Install: `npx -y @chatmcp/server-perplexity-ask`
   - URL: https://github.com/ppl-ai/modelcontextprotocol
   - Business relevance: Real-time web research with citations

5. **agentql-mcp** (Mar 2025)
   - AgentQL's data extraction capabilities via MCP
   - Install: `npx -y agentql-mcp`
   - URL: https://github.com/tinyfish-io/agentql-mcp
   - Business relevance: Structured web data extraction for business intelligence

6. **aws-kb-retrieval-server** (Mar 2025)
   - AWS Knowledge Base retrieval via Bedrock Agent Runtime
   - Install: `npx -y @modelcontextprotocol/server-aws-kb-retrieval`
   - Business relevance: Enterprise knowledge base access

7. **zhipu-web-search** (May 2025)
   - Search engine for LLMs integrating 4 search engines
   - URL: https://github.com/THUDM
   - Business relevance: Multi-engine search for comprehensive research

#### MARKETING / COMMUNICATION
8. **Mailtrap Email API** (Apr 2025)
   - Transactional email sending via Mailtrap
   - Install: `npx -y mcp-mailtrap`
   - URL: https://github.com/railsware/mailtrap-mcp
   - Business relevance: Email automation from AI agents

9. **Bucket** (Apr 2025)
   - Feature flag management from code editors
   - URL: https://github.com/bucketco/bucket-javascript-sdk
   - Business relevance: Feature flagging for product/engineering teams

#### PRODUCTIVITY
10. **mcp-server-flomo** (Dec 2024)
    - Write notes to Flomo
    - Install: `npx -y @chatmcp/mcp-server-flomo`
    - Business relevance: Note-taking integration

#### DEVELOPMENT / INFRASTRUCTURE
11. **edgeone-pages-mcp** (Apr 2025)
    - Deploy HTML to EdgeOne Pages with public URL
    - Install: `npx edgeone-pages-mcp`
    - URL: https://github.com/TencentEdgeOne/edgeone-pages-mcp
    - Business relevance: Quick deployments for marketing pages

12. **mcp-server-neon** (Mar 2025)
    - Neon serverless Postgres management
    - Install: `npx -y @neondatabase/mcp-server-neon start {API_KEY}`
    - Business relevance: Database infrastructure management

13. **playwright-mcp** (Mar 2025)
    - Official Playwright browser automation
    - Install: `npx @playwright/mcp@latest`
    - URL: https://github.com/microsoft/playwright-mcp
    - Business relevance: Web testing and automation

14. **302_sandbox_mcp** (Apr 2025)
    - Remote sandbox for code execution and file operations
    - Install: `npx -y @302ai/sandbox-mcp`
    - Business relevance: Secure code execution environments
    
15. **302_browser_use_mcp** (Apr 2025)
    - Remote browser automation
    - Install: `npx -y @302ai/browser-use-mcp`
    - Business relevance: Web automation at scale

#### ECOMMERCE / CLOUD
16. **qiniu-mcp-server** (Apr 2025)
    - Qiniu cloud storage and image processing
    - Install: `uvx qiniu-mcp-server`
    - Business relevance: Cloud storage management for Chinese market

17. **MiniMax-MCP** (Apr 2025)
    - Text-to-speech, image, and video generation
    - Install: `uvx minimax-mcp`
    - URL: https://github.com/MiniMax-AI/MiniMax-MCP
    - Business relevance: Content generation for marketing

#### COMPLIANCE / SECURITY
18. **sentry** (Dec 2024 - official)
    - Error tracking and issue analysis from Sentry.io
    - Install: `uvx mcp-server-sentry --auth-token={TOKEN}`
    - Business relevance: Production monitoring and incident response

#### DOCUMENT INTELLIGENCE
19. **search1api** (Dec 2024)
    - One API for Search, Crawling, and Sitemaps
    - Install: `npx -y search1api-mcp`
    - Business relevance: SEO and content intelligence

---

## SOURCE 2: MCPSERVERS.ORG (9,300+ total servers)

### Methodology
- Scraped the home page listing (featured + latest servers)
- Extracted 35 unique servers from the TanStack Start SSR state
- Also scraped category pages (finance, marketing, productivity, search, communication)
- The site categorizes servers well, making business filtering straightforward

### MCPSERVERS.ORG Latest Additions (most recent, ~June 2026)

1. **Railway MCP** ⭐ Official
   - Category: Development
   - Natural language interaction with Railway projects: create projects, deploy templates, manage environments, pull variables, redeploy services
   - URL: https://docs.railway.com/ai/mcp-server
   - Website: https://railway.com
   - Business relevance: Infrastructure-as-code for operators

2. **Voipstudio MCP** — Official
   - Category: Communication
   - Secure access to VoIPstudio account: recordings, call detail records, live calls, voicemails. Query activity, analyze patterns, identify agent performance issues, generate QA reports
   - URL: https://voipstudio.com/docs/administrator/aiartificialintelligence/voipstudiomcpserver/
   - Business relevance: Call center analytics and operations

3. **Native Soil**
   - Category: Memory
   - Save AI chat working state, load in any model/client/provider. Verified on save, secrets stripped
   - URL: https://nativesoil.dev/install
   - Business relevance: AI session portability across models

4. **Weavz**
   - Category: Development
   - Governed app access for AI agents — hosted runtime exposing 1,000+ apps (12,000+ tools) through Code Mode MCP, with Human Gates approvals, scoped per-user credentials, sandbox, files, and durable state
   - URL: https://weavz.io
   - Business relevance: Enterprise-grade AI governance platform

5. **ScholarXIV MCP**
   - Category: Other
   - Access to ScholarXIV academic research
   - URL: https://www.scholarxiv.com/developers/docs
   - Business relevance: Academic research access for R&D teams

6. **Memdeklaro**
   - Category: Other
   - Self-sovereign decentralized identity
   - URL: https://memdeklaro.org
   - Business relevance: Identity verification

7. **flkeys.app**
   - Category: Search
   - Verified, ground-truthed local intelligence for the Florida Keys
   - URL: https://flkeys.app
   - Business relevance: Local business intelligence

8. **MaxAEO AI Visibility MCP**
   - Category: Marketing
   - AI visibility audits: GEO/AEO, llms.txt, AI crawler readiness, robots, sitemap, canonical, metadata, noindex, JSON-LD
   - URL: https://github.com/maxaeo/maxaeo-ai-visibility-mcp
   - Business relevance: SEO for AI search engines — critical for modern marketing

### MCPSERVERS.ORG Featured Business Servers

#### FINANCE
9. **Alpha Vantage MCP Server** ⭐ Sponsor
   - Realtime & historical stock, ETF, options, forex, crypto, commodities, fundamentals, technical indicators
   - URL: https://mcp.alphavantage.co
   - Business relevance: Financial market data — already in our catalog

#### MARKETING / ECOMMERCE
10. **Zernio MCP** ⭐ Official
    - Social media scheduling: manage and publish across all major platforms from a single API
    - URL: https://docs.zernio.com/mcp
    - Website: https://zernio.link/mcpservers
    - Business relevance: Social media management automation

11. **Webotee Amazon MCP** ⭐ Sponsor
    - Amazon brand, seller & niche intelligence: buy-box history, competing sellers, under-competed niches
    - URL: https://www.webotee.com/amazon-product-research-mcp
    - Business relevance: Ecommerce intelligence for Amazon sellers

#### PRODUCTIVITY
12. **Cal.com MCP** ⭐ Official
    - Connect AI clients to Cal.com scheduling
    - URL: https://cal.com/docs/mcp-server
    - Business relevance: Meeting scheduling automation

13. **Superlist MCP Server** ⭐ Official
    - All-in-one task management: to-do lists, notes, projects. From Wunderlist creators
    - URL: https://help.superlist.com/en/articles/658028-superlist-mcp-server
    - Business relevance: Team productivity and task management

14. **Granola MCP** ⭐ Official
    - Meeting notes: query notes, search transcripts, get meeting insights
    - URL: https://docs.granola.ai/help-center/sharing/integrations/mcp.md
    - Business relevance: Meeting intelligence

15. **NotebookLM MCP Server** ⭐
    - Chat with NotebookLM for zero-hallucination answers from your notebooks
    - URL: https://github.com/PleasePrompto/notebooklm-mcp
    - Business relevance: Research and knowledge management

#### DEVELOPMENT / INFRASTRUCTURE
16. **Chipp MCP** ⭐ Official
    - Build, deploy, and monetize AI agents — no engineering team required
    - URL: https://chipp.ai/docs/guides/mcp.md
    - Business relevance: No-code AI agent platform

17. **Neo** ⭐ Sponsor
    - Hand off complex AI engineering tasks: model evals, agent optimization
    - URL: https://docs.heyneo.com/neo-mcp
    - Business relevance: AI engineering automation

18. **Capafy** ⭐ Sponsor
    - Skills run online 24/7 as agent products, get paid per use
    - URL: https://capafy.ai
    - Business relevance: Monetization platform for AI agent skills

---

## MCPSERVERS.ORG Category Pages — Notable Business Servers Found

### Finance Category (from /category/finance)
- **Polymarket Scan MCP**: Live prediction market data — whale trades, odds, profiles
- **ifthenpay Payments MCP**: Generate payments, retrieve transaction history (Portuguese gateway)
- **GoodVat MCP Server**: Global tax compliance across 200+ jurisdictions (already in catalog)
- **tossinvest-mcp**: Korean stock trading via Toss Securities (already in catalog)
- **Finance Toolkit**: 200+ financial metrics calculated from raw statements
- **ROIC.AI Financial Data API**: Company financials, ratios, prices, transcripts
- **UnusualWhales API**: Options flow, dark pool, congressional trading data
- **AlphaAI**: AI-enriched financial news with relevance scoring (already in catalog)
- **Personal Finance MCP Server**: Compound interest, amortization, retirement planning
- **Lovie — Company Formation MCP**: Company formation, banking, invoicing from AI agents
- **Flatland**: Pay-per-call x402 data APIs — token rug-check, on-chain reads
- **Gainium**: Crypto trading bot management from AI assistants
- **Clearance Agent Income**: Agent-to-agent knowledge exchange for trading intelligence
- **Agentberg**: Autonomous x402 payments across 29 chains
- **PipRail**: Already in catalog
- **Evibe Portfolio**: Investment portfolio + live market data
- **Allowance MCP**: Secure agent purchasing with virtual cards

### Marketing Category (from /category/marketing)
- **SEOcrawl AI**: Live Google Search Console & GA4 data, keyword/page analysis
- **CitedSpy**: Connect AI tools to CitedSpy workspace for content intelligence
- **Outlit Customer Context MCP**: Customer context, timelines, semantic search
- **viral.app**: API-powered MCP for UGC marketing analytics
- **Influee MCP**: Influencer marketing campaigns
- **Rampify**: LinkedIn data API for AI agents
- **Unspam MCP**: Spam checks, inbox placement, screenshots
- **PostWire**: Post to TikTok, Instagram, YouTube, X, LinkedIn, Bluesky, Telegram, Mastodon & Discord
- **AppGoblin ASO**: App Store stats, installs, keywords, revenue
- **PPXC Find Customers**: Turn comments into ranked customer leads
- **SE Ranking MCP**: 180+ SEO tools — keyword research, backlinks, domain analysis
- **Google Ads - AdPlug**: Connect Google Ads to AI
- **OpenAI Ads MCP Server**: OpenAI Advertiser API integration
- **Adsumo**: AI ad creative studio

### Productivity Category (from /category/productivity)
- **DataAssist-IO**: Natural language querying of SQL, NoSQL, files & warehouses
- **Appflowy MCP**: Self-hosted workspace (open-source Notion alternative)
- **ServiceNow MCP**: 65 tools over full REST surface
- **PDFMakerAPI**: Generate invoices, receipts, documents via natural language
- **atlassian-confluence-mcp-server**: Read, create, search in Confluence
- **Collaboard MCP Server**: Whiteboard creation and management
- **ProposalCraft**: Draft winning client proposals locally
- **Prompty.tools**: Prompt library as MCP server
- **Kailo Sheets**: Hosted MCP for Google Sheets

---

## COMPARISON WITH EXISTING CATALOG

Our catalog at `/corpusiq-docs/hermes/mcp/servers/external/index.md` (updated June 25, 2026) already contains many of the financial servers found (Alpha Vantage, Tradingview, Tossinvest, AlphaAI, Infrawise, Costory, Cloudability, GoodVat, Lovie, etc.)

### NEW SERVERS NOT IN OUR CATALOG (High Priority)

From mcpservers.org:
1. **Voipstudio MCP** — Call center analytics (Communication)
2. **Weavz** — Enterprise AI governance with 12,000+ tools (Development)
3. **MaxAEO AI Visibility MCP** — AI search engine SEO optimization (Marketing)
4. **Native Soil** — Cross-model AI session portability (Memory)
5. **Zernio MCP** — Social media scheduling API (Marketing)
6. **Webotee Amazon MCP** — Amazon seller intelligence (Ecommerce)
7. **Chipp MCP** — No-code AI agent platform (Development)
8. **Neo** — AI engineering task automation (Development)
9. **Capafy** — Agent skill monetization platform (Productivity)

From mcp.so:
10. **serper-mcp-server** — Google Search via Serper API
11. **Mailtrap Email API** — Transactional email from AI agents
12. **Bucket** — Feature flag management from IDE
13. **agentql-mcp** — Structured web data extraction
14. **perplexity** — Perplexity API web search connector
15. **jina-mcp-tools** — Jina AI search foundation APIs
16. **zhipu-web-search** — Multi-engine LLM search
17. **MiniMax-MCP** — TTS, image & video generation
18. **edgeone-pages-mcp** — Quick HTML deployments
19. **302_sandbox_mcp** — Remote code execution sandbox

From mcpservers.org category pages (notable):
20. **Polymarket Scan MCP** — Prediction market data
21. **UnusualWhales API** — Options flow & congressional trading
22. **Finance Toolkit** — 200+ computed financial metrics
23. **PostWire** — Multi-platform social posting (10+ platforms)
24. **SE Ranking MCP** — 180+ SEO tools
25. **SEOcrawl AI** — GSC + GA4 live data
26. **DataAssist-IO** — Natural language data querying
27. **ServiceNow MCP** — 65-tool ITSM integration
28. **Appflowy MCP** — Open-source workspace
29. **Influee MCP** — Influencer marketing campaigns
30. **PDFMakerAPI** — Document generation from natural language

---

## SUMMARY STATS

| Source | Total Servers | Business-Relevant Found | New to Our Catalog |
|--------|--------------|------------------------|-------------------|
| mcp.so | 22,663+ | ~47 extracted (full), many more referenced | ~15 notable new |
| mcpservers.org | 9,300+ | 35 from home page, dozens more from categories | ~20 notable new |

**Key Takeaway:** The MCP ecosystem is growing extremely fast. The most notable trends:
- **AI-native marketing tools**: SEO for AI search engines (GEO/AEO), multi-platform social posting
- **Enterprise governance**: Weavz (12,000+ apps with Human Gates), compliance tools
- **Financial data explosion**: Prediction markets, options flow, crypto trading, multi-chain
- **No-code AI platforms**: Chipp, Capafy — build and monetize agents without engineering
- **Communication infrastructure**: VoIP analytics, email automation, meeting intelligence

---

*Scan performed June 25, 2026. Sources: https://mcp.so/servers and https://mcpservers.org*
*Note: mcp.so uses React Server Components with deduplication; only a subset of servers had full metadata extractable via scraping. The site reports 22,663+ total servers across 367 pages.*
