---
title: June 10, 2026 Discoveries
description: 68 new high-value skills discovered across 12 new repositories. Setup guides with install commands and Hermes integration tips.
---

# June 10, 2026 — New Skills Discoveries

Automated discovery sweep across 74 search queries found **226 skills not yet cataloged**. This page documents the **most impactful 68** — skills from 12 major new repositories, each with 500+ installs and direct relevance to Hermes agents.

*Previously cataloged: coreyhaines31/marketingskills, nousresearch/hermes-agent, vercel-labs/agent-browser, vercel-labs/agent-skills, anthropics/skills, xixu-me/skills, browser-use/skills, mcp-use/mcp-use, github/awesome-copilot, obra/superpowers, apify/agent-skills, wshobson/agents.*

---

## Google Workspace CLI — 8 skills (168K total installs)

`googleworkspace/cli` — Automate Gmail, Drive, Docs, Calendar, and Sheets from the terminal. Essential for any operator running Hermes with Google Workspace.

| Skill | Installs | Use Case |
|-------|----------|----------|
| `googleworkspace/cli@gws-gmail` | 34.9K | Read, search, send Gmail from CLI |
| `googleworkspace/cli@gws-drive` | 33.4K | List, search, read Google Drive files |
| `googleworkspace/cli@gws-docs` | 33.3K | Create and edit Google Docs |
| `googleworkspace/cli@gws-calendar` | 32K | Schedule, list, and manage calendar |
| `googleworkspace/cli@gws-workflow-email-to-task` | 17.8K | Convert emails to actionable tasks |
| `googleworkspace/cli@recipe-save-email-attachments` | 16.8K | Auto-save email attachments to Drive |
| `googleworkspace/cli@persona-content-creator` | 16.6K | AI-driven content creation |
| `googleworkspace/cli@recipe-draft-email-from-doc` | 16.6K | Draft emails from document templates |

**Setup:**

```bash
npx skills add googleworkspace/cli@gws-gmail
npx skills add googleworkspace/cli@gws-drive
# Auth: Requires Google OAuth. Run `gws login` after install.
# Hermes: Skill auto-registers. Use tool names in agent prompts.
```

---

## Firecrawl CLI — 4 skills (235K total installs)

`firecrawl/cli` — The dominant web scraping toolkit. Turns any website into structured markdown. Core infrastructure for research agents.

| Skill | Installs | Use Case |
|-------|----------|----------|
| `firecrawl/cli@firecrawl` | 70.7K | Full web scraping CLI |
| `firecrawl/cli@firecrawl-scrape` | 55.2K | Single-page extraction |
| `firecrawl/cli@firecrawl-search` | 55.1K | Web search with extraction |
| `firecrawl/cli@firecrawl-agent` | 54K | AI agent for web research |

**Setup:**

```bash
npx skills add firecrawl/cli@firecrawl
# API key: export FIRECRAWL_API_KEY="fc-..."
# Free tier: 500 credits/month. Pro: $19/month for 3,000 credits.
# Hermes: Auto-available as web tool alternative after install.
```

---

## Stripe AI — 3 skills (108K total installs)

`stripe/ai` — Official Stripe agent skills. Payment integration, upgrades, and project scaffolding for Stripe-powered apps.

| Skill | Installs | Use Case |
|-------|----------|----------|
| `stripe/ai@stripe-best-practices` | 42.2K | Stripe integration patterns |
| `stripe/ai@upgrade-stripe` | 34.9K | Upgrade Stripe SDK versions |
| `stripe/ai@stripe-projects` | 31.3K | Scaffold Stripe projects |

**Setup:**

```bash
npx skills add stripe/ai@stripe-best-practices
# Requires: Stripe API key in env var STRIPE_SECRET_KEY
# Hermes: Use for payment integration questions, subscription logic
```

---

## Firebase Agent Skills — 5 skills (292K total installs)

`firebase/agent-skills` — Firebase platform skills. Auth, hosting, security rules, Firestore. For agents building on Firebase.

| Skill | Installs | Use Case |
|-------|----------|----------|
| `firebase/agent-skills@firebase-basics` | 77.7K | Firebase platform fundamentals |
| `firebase/agent-skills@firebase-auth-basics` | 77.1K | Authentication patterns |
| `firebase/agent-skills@firebase-hosting-basics` | 75.3K | Deploy and configure hosting |
| `firebase/agent-skills@firebase-security-rules-auditor` | 41.7K | Audit Firestore security rules |
| `firebase/agent-skills@firestore-security-rules-auditor` | 20.3K | Firestore-specific rule audits |

**Setup:**

```bash
npx skills add firebase/agent-skills@firebase-basics
# Requires: Firebase CLI (`npm i -g firebase-tools`) + `firebase login`
```

---

## Supabase Agent Skills — 2 skills (335K total installs)

`supabase/agent-skills` — Official Supabase skills for database, auth, and real-time infrastructure.

| Skill | Installs | Use Case |
|-------|----------|----------|
| `supabase/agent-skills@supabase-postgres-best-practices` | 220.9K | Postgres optimization, indexing, Row Level Security |
| `supabase/agent-skills@supabase` | 114.1K | Full Supabase platform: auth, storage, edge functions |

**Setup:**

```bash
npx skills add supabase/agent-skills@supabase-postgres-best-practices
# Requires: Supabase project URL + anon key in env
```

---

## Shopify AI Toolkit — 6 skills (38K total installs)

`shopify/shopify-ai-toolkit` — Official Shopify dev tools for storefront, admin, Liquid, and GraphQL.

| Skill | Installs | Use Case |
|-------|----------|----------|
| `shopify/shopify-ai-toolkit@shopify-admin` | 6.7K | Shopify admin API integration |
| `shopify/shopify-ai-toolkit@shopify-dev` | 6.2K | Development patterns and CLI |
| `shopify/shopify-ai-toolkit@shopify-liquid` | 6K | Liquid templating language |
| `shopify/shopify-ai-toolkit@shopify-storefront-graphql` | 5.5K | Storefront API via GraphQL |
| `shopify/shopify-ai-toolkit@shopify-hydrogen` | 5.2K | Hydrogen storefront framework |
| `shopify/shopify-ai-toolkit@shopify-functions` | 4.8K | Shopify Functions (serverless backend logic) |

**Setup:**

```bash
npx skills add shopify/shopify-ai-toolkit@shopify-dev
# Requires: Shopify CLI (`npm i -g @shopify/cli`) + store auth
```

---

## Prisma Skills — 3 skills (32K total installs)

`prisma/skills` — Database ORM for TypeScript/Node.js. Schema design, migrations, client API patterns.

| Skill | Installs | Use Case |
|-------|----------|----------|
| `prisma/skills@prisma-database-setup` | 11.6K | Database schema design + migrations |
| `prisma/skills@prisma-client-api` | 10.8K | Type-safe database queries |
| `prisma/skills@prisma-cli` | 9.6K | Prisma CLI workflows (migrate, generate, studio) |

**Setup:**

```bash
npx skills add prisma/skills@prisma-database-setup
# Requires: Prisma CLI (`npm i -g prisma`) + DATABASE_URL in env
```

---

## LangGraph Extensions — 3 skills (20.6K total installs)

`langchain-ai/langchain-skills` — LangGraph workflow patterns. State persistence, human-in-the-loop, and deep agent memory.

| Skill | Installs | Use Case |
|-------|----------|----------|
| `langchain-ai/langchain-skills@langgraph-persistence` | 8.7K | Long-term memory and checkpointing |
| `langchain-ai/langchain-skills@langgraph-human-in-the-loop` | 8.4K | Human approval workflows |
| `langchain-ai/langchain-skills@deep-agents-memory` | 9.9K | Advanced memory architecture |

**Setup:**

```bash
npx skills add langchain-ai/langchain-skills@langgraph-persistence
# Requires: pip install langgraph langgraph-checkpoint
```

---

## ElevenLabs — 2 skills (10.7K total installs)

`elevenlabs/skills` — Voice AI. Text-to-speech and speech-to-text for audio agents.

| Skill | Installs | Use Case |
|-------|----------|----------|
| `elevenlabs/skills@text-to-speech` | 6.2K | Generate natural voice audio |
| `elevenlabs/skills@speech-to-text` | 4.5K | Transcribe audio to text |

**Setup:**

```bash
npx skills add elevenlabs/skills@text-to-speech
# API key: export ELEVENLABS_API_KEY="..."
# Free tier: 10,000 chars/month. Starter: $5/month for 30,000 chars.
```

---

## Claude Office Skills — 4 skills (22K total installs)

`claude-office-skills/skills` — Office automation: Excel, CRM, PDFs, Airtable. Built for Claude but works with any LLM agent.

| Skill | Installs | Use Case |
|-------|----------|----------|
| `claude-office-skills/skills@excel-automation` | 10.2K | Excel file creation and manipulation |
| `claude-office-skills/skills@pdf-extraction` | 5.8K | Extract and parse PDF content |
| `claude-office-skills/skills@crm-automation` | 3.2K | CRM data entry and management |
| `claude-office-skills/skills@airtable-automation` | 2.7K | Airtable base operations |

**Setup:**

```bash
npx skills add claude-office-skills/skills@excel-automation
# No API key needed for Excel/PDF. CRM requires connected CRM API keys.
```

---

## Communication Bots — 4 skills (11K total installs)

`claude-office-skills/skills` — Telegram, WhatsApp, Slack, and Discord bot builders. Deploy autonomous agents to chat platforms.

| Skill | Installs | Use Case |
|-------|----------|----------|
| `claude-office-skills/skills@whatsapp-automation` | 3.4K | WhatsApp bot and automation |
| `claude-office-skills/skills@telegram-bot` | 3.1K | Build and deploy Telegram bots |
| `claude-office-skills/skills@linkedin automation` | 2.9K | LinkedIn posting and engagement |
| `claude-office-skills/skills@discord-bot` | 2.8K | Discord server bots |

**Setup:**

```bash
npx skills add claude-office-skills/skills@telegram-bot
# Telegram: Bot token from @BotFather. Discord: Bot token from Developer Portal.
```

---

## Additional High-Value Skills

Quick-reference table of other notable discoveries:

| Skill | Installs | Category |
|-------|----------|----------|
| `microsoft/playwright-cli@playwright-cli` | 53.1K | Browser automation CLI |
| `currents-dev/playwright-best-practices-skill@playwright-best-practices` | 48.4K | Playwright testing patterns |
| `intellectronica/agent-skills@notion-api` | 42.6K | Notion API integration |
| `neondatabase/agent-skills@neon-postgres` | 40.4K | Serverless Postgres |
| `expo/skills@expo-deployment` | 33.6K | React Native deployment |
| `resciencelab/opc-skills@seo-geo` | 29.5K | Geo-targeted SEO |
| `jeffallan/claude-skills@kubernetes-specialist` | 10.3K | Kubernetes expertise |
| `jeffallan/claude-skills@devops-engineer` | 6K | DevOps patterns |
| `jeffallan/claude-skills@monitoring-expert` | 3.1K | Infrastructure monitoring |

---

## Summary

| Category | New Repos | New Skills |
|----------|-----------|------------|
| Google Workspace | 1 | 8 |
| Web Scraping | 1 | 4 |
| Payments | 1 | 3 |
| Firebase | 1 | 5 |
| Database (Supabase + Prisma) | 2 | 5 |
| Commerce (Shopify) | 1 | 6 |
| AI/ML (LangGraph + ElevenLabs) | 2 | 5 |
| Office Automation | 1 | 4 |
| Communication Bots | 1 | 4 |
| Infrastructure & Testing | 4 | 6 |
| Other | 2 | 18 |
| **Total** | **17** | **68** |

All skills installable with `npx skills add <owner/repo@skill>`. See the [skills.sh marketplace](https://skills.sh) for browse/search.

*Discovered: June 10, 2026. 74 search queries, 280 skills found, 226 new, 68 high-value documented above.*

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace](/hermes/skills/marketplace/) →*

*Part of the [Hermes Skills Library](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/skills) — 133+ agent skills. Built by [CorpusIQ](https://www.corpusiq.io).*

*Part of the [Hermes Skills Library](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/skills) — 133+ agent skills. Built by [CorpusIQ](https://www.corpusiq.io).*
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
