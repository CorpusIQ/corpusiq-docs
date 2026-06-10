---
title: External MCP Server Catalog
description: Curated catalog of notable third-party MCP servers for business operators — finance, analytics, document intelligence, security, and productivity
---

# External MCP Server Catalog

Beyond CorpusIQ's 54 built-in connectors, the MCP ecosystem now has 22,000+ servers spanning every domain. This catalog tracks the most relevant third-party MCP servers for business operators — curated from [mcp.so](https://mcp.so) and [mcpservers.org](https://mcpservers.org).

> **Last updated:** June 9, 2026 · **Sources:** mcp.so (22,054 servers), mcpservers.org

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

---

## Document Intelligence

### Sifter
Extracts structured, typed records from documents (PDFs, scans, contracts, invoices) using natural-language field specs. Agents can query and aggregate — exact counts, sums, filters, with source-page citations. Unlike RAG, answers collection-wide questions.

---

## Analytics & Business Intelligence

### Clamp Analytics MCP
Analyze and manage traffic, funnels, cohorts, revenue, errors. Web/app analytics via MCP. Complementary to GA4 for product analytics use cases.

---

## Content & Research

### Scribefy
Extract timestamped YouTube transcripts, video search, metadata, and related-video tools. Works with Claude, Cursor, Windsurf, and any MCP client.

### Hacker News MCP ★ by NeCL
Access Hacker News data for AI agents: top stories, story details, comments thread, full-text search via Algolia. No API key required — public HN API. Built for content research, trend monitoring, and prompt enrichment. By Neural Engineering & Cognitive Logic (neclco.com).

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

### Scrapling MCP
High-performance Python web scraping via Playwright. Proxy support, captcha solving, intelligent navigation. Speed-optimized alternative to Playwright/Puppeteer.

---

## Productivity

### Cal.com MCP ★ Official
Connect AI clients to Cal.com scheduling. Hosted endpoint at `mcp.cal.com` or local instance.

### Chipp MCP ★ Official
Build, deploy, and monetize AI agents — "What Shopify did for ecommerce, Chipp does for AI agents."

---

## Communication

### Granola MCP ★ Official
AI-powered meeting notes and summaries. Connect your meeting data to AI agents.

### Superlist MCP Server ★ Official
Task and project management via MCP. Connect AI agents to your Superlist workspace.

---

## Memory & Knowledge

### Anki MCP ★ Official
Enable AI assistants to interact with Anki spaced-repetition flashcards.

### XMemo
Persistent memory for AI agents across sessions.

---

## New This Week (June 9, 2026 — mcp.so Latest)

| Server | Category | Description |
|--------|----------|-------------|
| Hacker News MCP | Content | Hacker News API: stories, comments, search (by NeCL) |
| Bright Data | Dev Tools | Enterprise web scraping and data extraction (Sponsor) |
| Scrapling MCP | Dev Tools | High-performance web scraping via Playwright |
| Onlinecybertools MCP | Dev Tools | 280+ free dev/security tools, no auth required |
| Scribefy | Content | YouTube transcripts, video search, metadata |
| Secure Calendar MCP | Data Firewall | AI-safe Google Calendar & Outlook access |
| Secure Email MCP | Data Firewall | AI-safe Gmail & Outlook access |
| Secure Google Drive | Data Firewall | AI-safe Google Drive access |
| Secure Google Docs | Data Firewall | AI-safe Google Docs editing |
| Secure Google Sheets MCP | Data Firewall | AI-safe Google Sheets operations |
| Sifter | Document AI | Structured record extraction from documents |
| Tokenbel Financial Data | Finance | Belarusian securities data |
| Voyei | Travel | Collaborative travel planning, 78 tools |
| Deepsite.site | Dev Tools | AI code agent powered by DeepSeek |
| ShipAny | Dev Tools | AI SaaS startup boilerplate |
| CopyWeb | Dev Tools | Screenshot/URL to code components |
| ThinkAny | Search | New Era AI search engine |
| HeyBeauty | AI | AI-powered virtual try-on |

---

## Ecosystem Stats

- **Total MCP servers tracked:** 22,037+ (mcp.so)
- **Official servers:** 30+ (from Google, GitHub, Cloudflare, Anthropic, etc.)
- **CorpusIQ connectors:** 54 (the most comprehensive business data MCP server)
- **Categories represented:** 20+ (Finance, Analytics, CRM, Commerce, Dev, etc.)

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
    "alphavantage": {
      "command": "npx",
      "args": ["-y", "@alphavantage/mcp-server"]
    }
  }
}
```

Check each server's documentation for specific transport type (streamable HTTP, stdio, SSE) and authentication requirements.

---

*← [MCP Servers Home](/hermes/mcp/servers/) | [Connector Catalog](/hermes/mcp/connectors/) →*

*↑ [MCP Documentation](/hermes/mcp/)*

*Powered by CorpusIQ — monitoring the MCP ecosystem for business operators*
