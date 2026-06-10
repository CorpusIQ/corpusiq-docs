# CorpusIQ Documentation

![tokens saved (est.)](https://img.shields.io/endpoint?url=https%3A%2F%2Fmcp2.corpusiq.io%2Fapi%2Fv1%2Fusage%2Fpublic-counter%3Fformat%3Dshields&style=flat-square&logo=anthropic&logoColor=white)

CorpusIQ is the live-data brain you plug into Claude or ChatGPT. Connect the tools you already pay for — QuickBooks, Shopify, Klaviyo, Google Ads, GA4, HubSpot, Slack, Gmail, and 35+ more — then ask plain-English questions and get real answers grounded in your own data.

---

## Contents

### Getting Started
Everything needed to go from zero to first answer.

| Page | Description |
|------|-------------|
| [Quickstart Guide](/quickstart/) | Step-by-step: create account, connect AI, first connector, first prompt |
| [How It Works](/how-it-works/) | Architecture, MCP protocol, privacy, rate limits, skills, connectors explained |
| [Examples](/examples/) | Claude Desktop config, MCP starter kit |
| [What is CorpusIQ?](/how-it-works/what-is-corpusiq/) | Product overview and value proposition |

### Connectors
**37+ live-data connectors** across 11 categories. Each with setup guides, auth walkthroughs, and example prompts.

| Category | Connectors |
|----------|-----------|
| Marketing & Analytics | GA4, Google Ads, LinkedIn Ads, Meta Ads, Ahrefs, Semrush, GSC, PostHog, TikTok |
| Email & Automation | Klaviyo, Mailchimp, ActiveCampaign, Constant Contact, Postscript |
| CRM & Sales | HubSpot, LeadConnector, Close, Odoo, Monday.com |
| Commerce | Shopify, Stripe, Amazon Seller, eBay, GunBroker |
| Finance | QuickBooks |
| Communication | Slack, Gmail, Outlook, Calendly, Notion |
| Files | Google Drive, OneDrive, Dropbox, Airtable |
| Databases | PostgreSQL, MSSQL, Cosmos DB, MongoDB |

[Browse all 37+ connectors →](/connectors/)

### Prompt Library
**Battle-tested prompts** for business operators. Copy, paste, get answers.

| Page | Use Case |
|------|----------|
| [Executive Summary](/prompts/executive-summary/) | Multi-source business health overview |
| [Marketing & ROAS](/prompts/marketing-roas/) | Campaign performance across Google Ads, Meta, LinkedIn |
| [Ecommerce Ops](/prompts/ecommerce-ops/) | Shopify + Klaviyo + GA4 combined queries |
| [Revenue & Finance](/prompts/revenue-and-finance/) | QuickBooks P&L, Stripe revenue, overdue invoices |
| [Customer & CRM](/prompts/customer-and-crm/) | HubSpot pipeline, lead scoring, deal velocity |
| [Email & SMS](/prompts/email-and-sms/) | Klaviyo campaign performance, list health |
| [Multi-Source](/prompts/multi-source/) | Cross-source queries combining 2+ connectors |

[Browse all 10 prompt templates →](/prompts/)

### Recipes
**Copy-paste workflows** for common business operations.

| Recipe | Connectors Used |
|--------|----------------|
| [Shopify + QuickBooks Reconciliation](/recipes/shopify-quickbooks-reconciliation/) | Shopify, QuickBooks |
| [HubSpot + Klaviyo Pipeline](/recipes/hubspot-klaviyo-pipeline/) | HubSpot, Klaviyo |
| [Weekly Ad ROI Report](/recipes/weekly-ad-roi-report/) | Google Ads, Meta Ads, GA4 |
| [IndexNow Auto-Submit](/recipes/indexnow-auto-submit/) | GSC, IndexNow API |

[Browse all recipes →](/recipes/)

### How It Works
Understand the platform architecture.

| Page | Topic |
|------|-------|
| [What is CorpusIQ?](/how-it-works/what-is-corpusiq/) | Product overview |
| [MCP Architecture](/how-it-works/mcp-architecture/) | Model Context Protocol deep dive |
| [Connectors Explained](/how-it-works/connectors-explained/) | How live-data connectors work |
| [Skills Explained](/how-it-works/skills-explained/) | Cross-source runbook system |
| [Metric Specs](/how-it-works/metric-specs/) | Canonical KPI definitions and drift detection |
| [Privacy & Security](/how-it-works/privacy-and-security/) | Data handling, encryption, compliance |
| [Rate Limits](/how-it-works/rate-limits-and-quotas/) | API quotas and throttling |

[Browse how-it-works →](/how-it-works/)

### Docs
Platform reference for developers and operators.

| Page | Topic |
|------|-------|
| [Architecture](/docs/architecture/) | System architecture and design decisions |
| [Governance](/docs/governance/) | Operational rules, monitoring, safety |
| [Security](/docs/security/) | Auth, encryption, compliance |
| [Reporting](/docs/reporting/) | Usage stats, token savings, analytics |
| [Search](/docs/search/) | Cross-source search and retrieval |
| [AI Agent Users](/docs/ai-agent-users/) | Using CorpusIQ from autonomous agents |
| [AI Chat Users](/docs/ai-chat-users/) | Using CorpusIQ from Claude/ChatGPT |
| [ChatGPT Integration](/docs/chatgpt-integration/) | ChatGPT-specific setup |
| [Supported Agents](/docs/supported-agents/) | Compatible AI platforms |

[Browse docs →](/docs/)

### Hermes Community Hub
**The largest collection of Hermes resources on GitHub.** 39 pages covering architecture, MCP integration, deployment, skills catalog, governance, and production operations. Built from live experience running 24 autonomous agents across 37+ MCP connectors.

| Section | Content |
|---------|---------|
| [Architecture](/hermes/architecture/) | Six-layer autonomous agent design |
| [Setup](/hermes/setup/) | DGX Spark + Mac Mini deployment |
| [Orchestration](/hermes/orchestration/) | Hermes, CrewAI, LangGraph, Reflexion |
| [Skills Catalog](/hermes/skills/catalog/) | 133+ skills, single source of truth |
| [MCP Integration](/hermes/mcp/) | 37+ CorpusIQ connectors for agents |
| [Knowledge](/hermes/knowledge/) | GBrain, GraphRAG, Dream Cycle, Honcho |
| [Infrastructure](/hermes/infrastructure/) | DGX, Mac Mini, browser, auth, routing |
| [Governance](/hermes/governance/) | Rules, crons, monitoring, email ops |
| [Content Ops](/hermes/content-ops/) | Video, social, engagement automation |
| [Tools Index](/hermes/tools/) | 233+ tools with repo links |
| [Troubleshooting](/hermes/troubleshooting/) | Browser, OAuth, cron, model routing |

[Browse the Hermes Community Hub →](/hermes/)

### Troubleshooting
Common issues and fixes for CorpusIQ users.

| Page | Issue |
|------|-------|
| [Claude Can't See CorpusIQ](/troubleshooting/claude-cant-see-corpusiq/) | MCP connection failures |
| [ChatGPT Can't See CorpusIQ](/troubleshooting/chatgpt-cant-see-corpusiq/) | ChatGPT integration issues |
| [Connector Auth Failed](/troubleshooting/connector-auth-failed/) | OAuth and credential problems |
| [Connector Shows No Data](/troubleshooting/connector-shows-no-data/) | Empty results, permission gaps |
| [Error Codes Reference](/troubleshooting/error-codes-reference/) | All error codes and resolutions |

[Browse troubleshooting →](/troubleshooting/)

### Community & Contributing

| Page | Content |
|------|---------|
| [Contributing](/CONTRIBUTING.md) | Specific enhancement requests, recipes, examples, and bug reports |
| [Community](/community/) | Questions, early ideas, upvotes, and discussion paths |
| [Progress](/PROGRESS.md) | Documentation completion tracker |
| [Changelog](/changelog/) | What changed and when |
| [Roadmap](/roadmap/) | Upcoming features and docs |

---

## Quick Reference

| Question | Answer |
|----------|--------|
| How do I get started? | [Quickstart →](/quickstart/) |
| What connectors are available? | [All 37+ connectors →](/connectors/) |
| How do I write a good prompt? | [Prompt library →](/prompts/) |
| How does it work under the hood? | [How It Works →](/how-it-works/) |
| Can my autonomous agent use this? | [Hermes Community Hub →](/hermes/) |
| Something's broken. Help? | [Troubleshooting →](/troubleshooting/) |
| I want to contribute. | [Contributing →](/CONTRIBUTING.md) |
| I have a connector idea. | [Community →](/community/) |

---

## Repo Stats

| Metric | Value |
|--------|-------|
| Total pages | 130+ |
| Connector docs | 37+ |
| Prompt templates | 10 |
| Recipes | 5 |
| Troubleshooting guides | 6 |
| Hermes hub pages | 39 |
| Hermes tools indexed | 140+ |
| Total lines | 10,000+ |

---

## Topics

`mcp` `model-context-protocol` `ai-connectors` `business-intelligence` `claude` `chatgpt` `shopify` `quickbooks` `google-analytics` `hubspot` `stripe` `ai-agents` `llm-tools` `saas` `hermes`
