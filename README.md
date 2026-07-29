# CorpusIQ — Stop building reports by hand. Just ask your AI.

[![MCP Toplist](https://mcptoplist.com/badge/glama%2FCorpusIQ%2Fcorpusiq-docs.svg)](https://mcptoplist.com/server/glama%2FCorpusIQ%2Fcorpusiq-docs)

[![MCP Platform](https://img.shields.io/badge/MCP-Platform-0a2540?style=flat-square&logo=anthropic&logoColor=white)](https://www.corpusiq.io)
[![Connectors](https://img.shields.io/badge/Connectors-37+-c9a961?style=flat-square)](https://www.corpusiq.io/connectors)
[![Stars](https://img.shields.io/github/stars/CorpusIQ/corpusiq-docs?style=flat-square&color=c9a961)](https://github.com/CorpusIQ/corpusiq-docs)
[![Contributors](https://img.shields.io/badge/Contributors-welcome-0a2540?style=flat-square)](https://github.com/CorpusIQ/corpusiq-docs/blob/main/CONTRIBUTING.md)
[![License](https://img.shields.io/badge/License-MIT-627d98?style=flat-square)](LICENSE)

**CorpusIQ is the live-data brain you plug into ChatGPT, Claude, or any AI assistant.** Connect the tools you already use — QuickBooks, Shopify, Stripe, HubSpot, GA4, Klaviyo, Slack, and 30+ more — then ask plain-English questions and get answers grounded in your actual business data. No dashboards. No reports. No waiting on someone to pull the numbers.

> "How much did we make last month across Shopify and Stripe?" — answered in seconds.

---

## What makes it different

| Instead of... | CorpusIQ lets you... |
|---------------|---------------------|
| Building dashboards nobody checks | Ask questions in plain English, get real data |
| Exporting CSVs from 5 different tools | Query everything at once — cross-source, live |
| Waiting on someone to "pull the numbers" | Get answers in seconds, not days |
| Learning SQL or hiring a data team | Your AI assistant becomes your analyst |
| Static reports that are outdated by lunch | Live data, every time you ask |

---

## How it works — 3 steps

1. **Connect** — Plug in your existing tools (30-second OAuth, read-only, no data leaves your control)
2. **Ask** — Type a question in ChatGPT, Claude, or any MCP-compatible assistant
3. **Get answers** — Live data flows directly into the AI's response. No middleman.

**Read the full docs:** [corpusiq.io/docs](https://www.corpusiq.io/docs/) — Quickstart, API reference, connector guides, troubleshooting.

---

## 37+ live-data connectors

| Category | What you can query |
|----------|-------------------|
| **Commerce** | Shopify orders, Stripe charges, Amazon Seller, eBay |
| **Marketing** | GA4 traffic, Google Ads spend, Meta Ads ROAS, LinkedIn Ads, TikTok |
| **CRM** | HubSpot deals, LeadConnector pipelines, Close CRM, Monday.com |
| **Finance** | QuickBooks P&L, invoices, balance sheet |
| **Email/SMS** | Klaviyo campaigns, Mailchimp lists, ActiveCampaign automations |
| **Communication** | Slack messages, Gmail, Outlook, Calendly events |
| **SEO** | Ahrefs rankings, Semrush keywords, Google Search Console |
| **Databases** | PostgreSQL, MSSQL, Cosmos DB, MongoDB |
| **Files** | Google Drive, OneDrive, Dropbox, Airtable, Notion |

[Browse all 37+ connectors →](https://www.corpusiq.io/connectors)

---

## Who uses CorpusIQ

- **SaaS founders** — Revenue across Stripe + QuickBooks, churn from HubSpot, GA4 traffic — one question.
- **Ecommerce operators** — Shopify orders, Klaviyo campaign ROAS, Meta Ads spend — side by side.
- **Agencies** — Pull live data from 5+ client platforms, deliver answers without building reports.
- **Accountants** — Ask QuickBooks questions in plain English instead of running reports.
- **AI agents** — 24/7 autonomous agents querying live business data via MCP protocol.

---

## This repo: Everything you need

| Section | What's inside |
|---------|---------------|
| **[Quickstart](https://www.corpusiq.io/docs/quick-start/)** | Create account → connect AI → first query in 5 minutes |
| **[Prompt Library](/hermes/prompts/)** | Battle-tested prompts for executives, marketers, operators |
| **[Connector Guides](/connectors/)** | Setup walkthroughs for all 37+ integrations |
| **[How It Works](https://www.corpusiq.io/docs/how-it-works/)** | MCP architecture, privacy, rate limits, skills system |
| **[Hermes Community Hub](/hermes/)** | 130+ pages: autonomous agents, skills catalog, infrastructure |
| **[Troubleshooting](https://www.corpusiq.io/docs/troubleshooting/)** | Common issues, error codes, OAuth fixes |
| **[Recipes](/recipes/)** | Copy-paste workflows for common business operations |
| **[API Reference](https://www.corpusiq.io/docs/api/)** | REST API, endpoints, OpenAPI spec |

---

## For developers: MCP-native from day one

CorpusIQ is built on the [Model Context Protocol (MCP)](https://modelcontextprotocol.io) — the open standard for connecting AI assistants to external tools and data.

```json
{
  "mcpServers": {
    "corpusiq": {
      "url": "https://mcp2.corpusiq.io/mcp",
      "transport": "streamable-http"
    }
  }
}
```

Your AI assistant gets 37+ live data tools instantly. No SDK. No custom integration. Just works.

---

## Contributing

This docs repo is open for contributions:

- **Content gaps** — See open issues tagged [`good first issue`](https://github.com/CorpusIQ/corpusiq-docs/issues)
- **New recipes** — Share workflows that combine 2+ connectors
- **Connector requests** — [Open an issue](https://github.com/CorpusIQ/corpusiq-docs/issues/new)
- **Docs fixes** — PRs welcome for typos, clarifications, improvements

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full guide.

---

## Stay connected

- **Website:** [corpusiq.io](https://www.corpusiq.io)
- **Affiliate program:** [25% recurring for 3 years](https://www.corpusiq.io/affiliate)
- **GitHub Discussions:** [Ask questions, share ideas](https://github.com/CorpusIQ/corpusiq-docs/discussions)
- **MCP directory:** Listed on [mcp.so](https://mcp.so), [Smithery.ai](https://smithery.ai), and the [Official MCP Registry](https://registry.modelcontextprotocol.io)

---

## Topics

`mcp` `model-context-protocol` `ai-connectors` `business-intelligence` `claude` `chatgpt` `perplexity` `shopify` `quickbooks` `google-analytics` `hubspot` `stripe` `ai-agents` `llm-tools` `saas` `business-analytics` `data-integration` `autonomous-agents` `ai-assistant` `mcp-server`

---

*CorpusIQ — Stop building reports by hand. Just ask your AI.*
