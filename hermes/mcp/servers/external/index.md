---
title: External MCP Server Catalog
description: Curated catalog of notable third-party MCP servers for business operators — finance, analytics, document intelligence, security, and productivity
---

# External MCP Server Catalog

Beyond CorpusIQ's 37+ built-in connectors, the MCP ecosystem now has 22,000+ servers spanning every domain. This catalog tracks the most relevant third-party MCP servers for business operators — curated from [mcp.so](https://mcp.so) and [mcpservers.org](https://mcpservers.org).

> **Last updated:** June 11, 2026 · **Sources:** mcp.so (22,135+ servers), mcpservers.org

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

---

## Financial Data

### Alpha Vantage MCP Server ★ Sponsor
Realtime & historical stock, ETF, options, forex, crypto, commodities, fundamentals, technical indicators. Official MCP server from Alpha Vantage.

### Tokenbel Financial Data
Read-only access to Belarusian securities: tokens, shares, bonds, companies, ticker search. Niche but notable for Eastern European markets.

### Infrawise ★ New
Azure FinOps infrastructure cost optimization. Helps operators manage cloud spend with AI-assisted cost analysis. `npx -y @infrawise/mcp-server`

---

## Document Intelligence

### Sifter
Extracts structured, typed records from documents (PDFs, scans, contracts, invoices) using natural-language field specs. Agents can query and aggregate — exact counts, sums, filters, with source-page citations. Unlike RAG, answers collection-wide questions.

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

### MCP Advisor ★ New
Discover and install the right MCP servers for your needs. Acts as a meta-layer — search across mcp.so's 22,000+ servers and get installation recommendations from your AI client. `npx -y @xiaohui-wang/mcpadvisor`

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

---

## Productivity

### Cal.com MCP ★ Official
Connect AI clients to Cal.com scheduling. Hosted endpoint at `mcp.cal.com` or local instance.

### Chipp MCP ★ Official
Build, deploy, and monetize AI agents — "What Shopify did for ecommerce, Chipp does for AI agents."

### Karea ★ New
Extensive MCP tools so Claude Code, Cursor, and other MCP clients can create, edit, close, recap, and link dev tasks while coding. Jira linking, productivity recap. `npx -y karea-mcp`

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

### Capafy ★ Sponsor ★ New
Marketplace for monetizing agent skills as products. On Capafy, your Skill runs online 24/7 as an agent product, and you get paid every time someone uses it. The "App Store for agent skills" — build once, earn continuously.

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

---

## Marketing

### Zernio MCP ★ Official ★ New
Social media scheduling platform — manage and publish content across all major platforms from a single API. MCP-native. `https://docs.zernio.com/mcp`

### FeedSquad ★ New
Content calendar and social publishing for Claude and ChatGPT agents. Create posts and campaigns, schedule with cadence guardrails, and publish to LinkedIn, X, and Threads. OAuth 2.1 authentication. Anti-slop pattern registry checks all drafts before scheduling. Approval-first workflow — nothing goes live without explicit approval.

---

## Memory & Knowledge

### Anki MCP ★ Official
Enable AI assistants to interact with Anki spaced-repetition flashcards.

### XMemo
Persistent memory for AI agents across sessions.

---

## New This Week (June 11, 2026 — mcp.so + mcpservers.org)

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

- **Total MCP servers tracked:** 22,135+ (mcp.so)
- **Official servers:** 33+ (from Google, GitHub, Cloudflare, Anthropic, Microsoft, MiniMax, etc.)
- **CorpusIQ connectors:** 37+ (the most comprehensive business data MCP server)
- **Categories represented:** 22+ (Finance, Analytics, CRM, Commerce, Dev, Marketing, Content Creation, Media, etc.)
- **New this cycle (June 11):** 11 newly catalogued servers for business operators
- **Cumulative since June 9:** 47 MCP servers catalogued across 3 sweeps

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
