---
title: New Marketplace Skills — June 9, 2026
description: 30+ newly discovered skills.sh marketplace skills relevant to Hermes agents. Web scraping, MCP building, testing, Stripe, Shopify, LangGraph extensions, and more.
---

# 🆕 Marketplace Skills — June 9, 2026 Discovery

30+ skills from [skills.sh](https://skills.sh) discovered in the June 9 batch sweep — all relevant to CorpusIQ Hermes agents. Install with `npx skills add <owner/repo@skill>`.

---

## Web Scraping & Data Extraction — 6 skills

Essential for market research, competitor monitoring, and content extraction. All from [firecrawl/cli](https://skills.sh/firecrawl/cli).

| Skill | Installs | Use Case |
|-------|----------|----------|
| `firecrawl` | 70.5K | Core Firecrawl web scraping engine |
| `firecrawl-scrape` | 55K | Single-page scraping with selectors |
| `firecrawl-search` | 54.9K | Web search + scrape in one pass |
| `firecrawl-agent` | 53.8K | Agent-driven crawling with context |
| `firecrawl-crawl` | 53.8K | Multi-page recursive crawling |
| `firecrawl-map` | 53.5K | Site map generation and discovery |

```bash
npx skills add firecrawl/cli  # installs all 6
```

**Setup:** Requires a Firecrawl API key. Set `FIRECRAWL_API_KEY` in your environment.

---

## MCP Server Development — 4 skills

Build and deploy MCP servers — critical for CorpusIQ connector expansion.

| Skill | Installs | Use Case |
|-------|----------|----------|
| `mcp-builder` | 71.6K | Build MCP servers from scratch (anthropics/skills) |
| `mcp-apps-builder` | 14.9K | Rapid MCP app scaffolding (mcp-use/mcp-use) |
| `mcp-cli` | 9.2K | CLI tools for MCP management (github/awesome-copilot) |
| `typescript-mcp-server-generator` | 10.5K | Auto-generate TypeScript MCP server (github/awesome-copilot) |

```bash
npx skills add anthropics/skills@mcp-builder
npx skills add mcp-use/mcp-use@mcp-apps-builder
npx skills add github/awesome-copilot@mcp-cli
npx skills add github/awesome-copilot@typescript-mcp-server-generator
```

---

## Testing & QA — 5 skills

Testing patterns for agent-built software. Essential for maintaining CorpusIQ reliability.

| Skill | Installs | Use Case |
|-------|----------|----------|
| `webapp-testing` | 92K | Playwright-based web app testing (anthropics/skills) |
| `python-testing-patterns` | 23.6K | pytest patterns and best practices (wshobson/agents) |
| `e2e-testing-patterns` | 17.6K | End-to-end test architecture (wshobson/agents) |
| `javascript-testing-patterns` | 14.8K | Jest/Vitest patterns (wshobson/agents) |
| `playwright-cli` | 52.7K | Official Microsoft Playwright CLI (microsoft/playwright-cli) |

```bash
npx skills add anthropics/skills@webapp-testing
npx skills add microsoft/playwright-cli@playwright-cli
npx skills add wshobson/agents  # installs all testing patterns
```

---

## Stripe Integration — 3 skills

Payment infrastructure for CorpusIQ monetization.

| Skill | Installs | Use Case |
|-------|----------|----------|
| `stripe-best-practices` | 42.1K | Stripe API best practices (stripe/ai) |
| `upgrade-stripe` | 34.8K | Migrate Stripe API versions (stripe/ai) |
| `stripe-projects` | 31.2K | Project-level Stripe setup (stripe/ai) |

```bash
npx skills add stripe/ai  # installs all 3
```

---

## Shopify Development — 6 skills

For CorpusIQ ecommerce operator integrations.

| Skill | Installs | Use Case |
|-------|----------|----------|
| `shopify-admin` | 6.7K | Shopify Admin API integration |
| `shopify-dev` | 6.2K | Shopify app development |
| `shopify-liquid` | 6K | Liquid template language |
| `shopify-storefront-graphql` | 5.5K | Storefront GraphQL API |
| `shopify-custom-data` | 5.4K | Metaobjects/meta fields |
| `shopify-functions` | 5.4K | Shopify Functions (serverless) |

```bash
npx skills add shopify/shopify-ai-toolkit  # installs all 6
```

---

## LangGraph Extensions — 3 skills

Advanced LangGraph patterns for multi-agent workflows.

| Skill | Installs | Use Case |
|-------|----------|----------|
| `langgraph-persistence` | 8.7K | Persistent state for LangGraph agents (langchain-ai/langchain-skills) |
| `langgraph-human-in-the-loop` | 8.4K | Human approval gates in agent workflows (langchain-ai/langchain-skills) |
| `langgraph-docs` | 3.5K | LangGraph documentation patterns (langchain-ai/deepagents) |

```bash
npx skills add langchain-ai/langchain-skills@langgraph-persistence
npx skills add langchain-ai/langchain-skills@langgraph-human-in-the-loop
npx skills add langchain-ai/deepagents@langgraph-docs
```

---

## Database & Infrastructure — 4 skills

| Skill | Installs | Use Case |
|-------|----------|----------|
| `supabase-postgres-best-practices` | 220.2K | Supabase PG patterns (supabase/agent-skills) |
| `supabase` | 113.5K | Full Supabase toolkit (supabase/agent-skills) |
| `prisma-database-setup` | 11.5K | Prisma ORM setup (prisma/skills) |
| `postgresql-table-design` | 19.2K | PG table design patterns (wshobson/agents) |

```bash
npx skills add supabase/agent-skills@supabase-postgres-best-practices
npx skills add supabase/agent-skills@supabase
npx skills add prisma/skills@prisma-database-setup
npx skills add wshobson/agents@postgresql-table-design
```

---

## Productivity & Business — 4 skills

| Skill | Installs | Use Case |
|-------|----------|----------|
| `excel-automation` | 10.1K | Excel workflow automation (claude-office-skills/skills) |
| `gws-workflow-email-to-task` | 17.8K | Gmail → task conversion (googleworkspace/cli) |
| `recipe-save-email-attachments` | 16.8K | Auto-save attachments to Drive (googleworkspace/cli) |
| `recipe-draft-email-from-doc` | 16.6K | Draft emails from Docs (googleworkspace/cli) |

```bash
npx skills add claude-office-skills/skills@excel-automation
npx skills add googleworkspace/cli@gws-workflow-email-to-task
npx skills add googleworkspace/cli@recipe-save-email-attachments
npx skills add googleworkspace/cli@recipe-draft-email-from-doc
```

---

## Hermes Ecosystem — 4 skills

Additional Hermes-specific marketplace skills.

| Skill | Installs | Use Case |
|-------|----------|----------|
| `hermes-imports` | 1.9K | Hermes import patterns (affaan-m/everything-claude-code) |
| `hermes-history-ingest` | 1.6K | Ingest browsing history into Hermes (ar9av/obsidian-wiki) |
| `hermes-agent` | 483 | Alternative Hermes agent skill (wihy/hermes-agent-skill) |
| `hermes-marketing-dashboard` | 357 | Marketing dashboard for Hermes (aradotso/marketing-skills) |

```bash
npx skills add affaan-m/everything-claude-code@hermes-imports
npx skills add ar9av/obsidian-wiki@hermes-history-ingest
npx skills add wihy/hermes-agent-skill@hermes-agent
npx skills add aradotso/marketing-skills@hermes-marketing-dashboard
```

---

## TTS & Audio — 3 skills

Text-to-speech for video and voice agents.

| Skill | Installs | Use Case |
|-------|----------|----------|
| `edge-tts` | 4.3K | Microsoft Edge TTS (aahl/skills) |
| `tts` (noizai) | 3.9K | Multi-provider TTS (noizai/skills) |
| `sherpa-onnx-tts` | 1.9K | Local ONNX TTS engine (steipete/clawdis) |

```bash
npx skills add aahl/skills@edge-tts
npx skills add noizai/skills@tts
npx skills add steipete/clawdis@sherpa-onnx-tts
```

---

## Summary

| Category | New Skills | Top Install Count |
|----------|:---------:|:-----------------:|
| Web Scraping & Extraction | 6 | 70.5K (firecrawl) |
| MCP Server Development | 4 | 71.6K (mcp-builder) |
| Testing & QA | 5 | 92K (webapp-testing) |
| Stripe Integration | 3 | 42.1K (stripe-best-practices) |
| Shopify Development | 6 | 6.7K (shopify-admin) |
| LangGraph Extensions | 3 | 8.7K (langgraph-persistence) |
| Database & Infrastructure | 4 | 220.2K (supabase) |
| Productivity & Business | 4 | 17.8K (gws-workflow) |
| Hermes Ecosystem | 4 | 1.9K (hermes-imports) |
| TTS & Audio | 3 | 4.3K (edge-tts) |
| **Total** | **42** | |
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
