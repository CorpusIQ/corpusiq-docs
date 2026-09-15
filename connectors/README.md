---
title: "CorpusIQ Connectors - 40+ Business Tools"
description: "CorpusIQ connects 40+ business tools to ChatGPT, Claude, and Perplexity with read-only OAuth. Browse every connector: Shopify, QuickBooks, Stripe, GA4, HubSpot, and more."
---
# Connectors

CorpusIQ connects to your business tools through read-only MCP connectors.
Each connector requires a one-time OAuth authentication - you click Connect,
approve the permission screen, and your AI tools can query live data immediately.

**Read-only by design.** CorpusIQ is not an AI agent. It cannot write,
modify, or execute anything in your connected systems, and it does not
retain raw customer files or full connector response payloads. Data
passes through on demand and returns to your AI client as read-only
information. No one at CorpusIQ can access your accounts.
See the full guarantee: [Security and Read-Only Access](/docs/hermes/security/read-only-and-security)

The external-source connectors in this directory are designed for read-only retrieval and do not write back to connected vendor accounts. Separately annotated CorpusIQ control-plane tools are outside this connector directory.

## What are CorpusIQ connectors?

CorpusIQ connectors are the integration layer between business data and AI assistants. Each connector maps to a SaaS application or database - QuickBooks, Shopify, Stripe, HubSpot, GA4, Salesforce, Slack, Gmail and 40+ others - and exposes its data through one MCP endpoint that ChatGPT, Claude and Perplexity can query in plain English. Every published operation declares whether it is read-only or write-capable, and each connection uses the provider's own OAuth authorization with the scopes shown on screen. CorpusIQ does not retain raw customer files or full connector response payloads; operational logs keep query text, per-user tool-call metadata and bounded outcome summaries for up to 30 days.

The connector model matters because the MCP ecosystem is large and uneven. Public registries count more than 9,400 MCP servers with 97M+ SDK downloads, yet many are unmaintained. CorpusIQ's approach is different: 40+ curated connectors to the tools businesses already run, each with documented operations, safety annotations and live status, so an AI assistant answers from a governed source instead of from a random server. For the full interactive connector list with real-time status indicators, visit [corpusiq.io/connectors](https://corpusiq.io/connectors).

## Index

### Commerce & Payments
- [Shopify](shopify.md) - Orders, products, customers, inventory
- [Stripe](stripe.md) - Payments, subscriptions, invoices, refunds
- [eBay](ebay.md) - Listings, orders, marketplace data
- [Amazon Seller](amazon_seller.md) - Seller Central metrics
- [GunBroker](gunbroker.md) - Auctions, bids, inventory

### Marketing & Advertising
- [Google Ads](google_ads.md) - Campaigns, ad groups, keywords, performance
- [Meta Ads (Facebook & Instagram)](facebook_marketing.md) - Ad accounts, campaigns, ad sets
- [LinkedIn Ads](linkedin-ads.md) - Campaign performance, audience data
- [TikTok](tiktok.md) - Ad performance, audience insights

### Web Analytics & SEO
- [GA4 - Google Analytics 4](ga4.md) - Traffic, conversions, events
- [Google Search Console](search-console.md) - Rankings, clicks, impressions
- [Ahrefs](ahrefs.md) - Backlinks, keyword rankings, site audits
- [Semrush](semrush.md) - Keyword research, competitor analysis
- [IndexNow](indexnow.md) - Real-time search engine indexing
- [YouTube](youtube.md) - Channel analytics, video performance

### Email & SMS Marketing
- [Klaviyo](klaviyo.md) - Campaigns, flows, segments
- [Mailchimp](mailchimp.md) - Campaigns, audiences, reports
- [Constant Contact](constantcontact.md) - Email campaigns, contacts
- [ActiveCampaign](activecampaign.md) - Automations, deals, contacts
- [Postscript](postscript.md) - SMS campaigns, subscribers

### CRM & Pipeline
- [HubSpot](hubspot.md) - Deals, contacts, companies, tickets
- [GoHighLevel (LeadConnector)](gohighlevel.md) - Pipelines, contacts, opportunities
- [Close](close.md) - Sales pipeline, leads, sequences
- [Monday.com](monday.md) - Boards, items, workflows

### Finance & Accounting
- [QuickBooks](quickbooks.md) - P&L, balance sheet, invoices, bills
- [Odoo](odoo.md) - ERP: accounting, inventory, sales, CRM

### Communication & Productivity
- [Google Workspace](google_workspace.md) - Gmail, Calendar, Drive, Docs, Sheets
- [Microsoft Outlook](outlook.md) - Email, Calendar, OneDrive
- [Slack](slack.md) - Messages, channels, search
- [Dropbox](dropbox.md) - Files, folders, shared links
- [OneDrive](onedrive.md) - Files, folders, SharePoint libraries
- [Notion](notion.md) - Pages, databases, comments
- [Airtable](airtable.md) - Bases, tables, records
- [Calendly](calendly.md) - Events, scheduling, invitees
- [IMAP Email](imap.md) - Read email from any IMAP account

### Databases & Analytics
- [PostgreSQL](postgres.md) - Relational database queries
- [Microsoft SQL Server (MSSQL)](mssql.md) - SQL Server queries
- [MongoDB](mongodb.md) - Document database queries
- [Azure Cosmos DB](cosmosdb.md) - Multi-model database queries
- [PostHog](posthog.md) - Product analytics, feature flags

### AI Integration Guides
- [ChatGPT Business Data Connector](chatgpt-business-data-connector.md)
- [Perplexity Business Data via MCP](perplexity-business-data-mcp.md)
- [AI MCP Server for Business Data](ai-mcp-server-for-business-data.md)
- [MCP Server: Shopify + QuickBooks](mcp-server-shopify-quickbooks.md)
- [Connect Airtable to Claude](connect-airtable-to-claude.md)
- [Connect GA4 to Claude](connect-ga4-to-claude.md)
- [Connect Google Ads to Claude](connect-google-ads-to-claude.md)
- [Connect HubSpot to Claude](connect-hubspot-to-claude.md)
- [Connect Klaviyo to ChatGPT](connect-klaviyo-to-chatgpt.md)
- [Connect Klaviyo to Claude](connect-klaviyo-to-claude.md)
- [Connect LinkedIn Ads to Claude](connect-linkedin-ads-to-claude.md)
- [Connect Meta Ads to Claude](connect-meta-ads-to-claude.md)
- [Connect QuickBooks to Claude](connect-quickbooks-to-claude.md)
- [Connect Shopify to Claude](connect-shopify-to-claude.md)
- [Connect Slack to Claude](connect-slack-to-claude.md)
- [Connect Stripe to Claude](connect-stripe-to-claude.md)

### Alternatives & Comparisons
- [Windsor.ai Alternative](windsor-ai-alternative.md)
- [Adzviser Alternative](adzviser-alternative.md)

## How to connect any connector

1. Open the CorpusIQ **Connectors** page
2. Click **Connect** next to the tool you want
3. A browser tab opens to the vendor's login page
4. Sign in, review the read-only permissions, click **Authorize**
5. The tab returns to CorpusIQ - the connector shows **Connected**

That's it. Your AI assistant can now query live data from that service.

Connector-specific notes (required plans, admin roles, multi-account setups) are on each individual connector page.

## Frequently Asked Questions

### How many connectors does CorpusIQ support?

CorpusIQ supports 40+ native connectors spanning CRM, accounting, payments, analytics, marketing, ecommerce, file storage, communication, databases, and more. External-source retrieval and write-capable management/control-plane operations are separately named and annotated.

### How do I connect a new data source?

Open the CorpusIQ Connectors page, click Connect next to the tool you want, approve the vendor's read-only permission screen, and the connector shows Connected. Each connection takes under 60 seconds.

### Are CorpusIQ connectors read-only?

External-source retrieval tools are marked read-only. CorpusIQ is not an AI agent. It cannot write, modify or execute anything in your connected systems, and it does not retain raw customer files or full connector response payloads. Data passes through on demand. No one at CorpusIQ can access your accounts. Operational query text, per-user tool-call metadata and bounded outcome summaries may be retained for up to 30 days; optional indexed search keeps embeddings and minimal metadata until connector revocation or account deletion. Write-capable connector-management and CorpusIQ control-plane tools are separately named and annotated.

### Does CorpusIQ support database connections?

Yes. CorpusIQ supports PostgreSQL, MSSQL (SQL Server), MySQL, Azure Cosmos DB, and MongoDB, all with read-only SQL/query access.

### What if I need a connector that isn't listed?

CorpusIQ adds new connectors regularly. You can request new connectors through the Dashboard or connect custom databases via the database bridge. For proprietary APIs, contact CorpusIQ about custom MCP connector development.

### How do I check which connectors are active?

Visit the CorpusIQ Dashboard to see connector status (active, paused, needs re-auth). Each connector shows real-time status indicators.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "How many connectors does CorpusIQ support?", "acceptedAnswer": {"@type": "Answer", "text": "CorpusIQ supports 40+ native connectors spanning CRM, accounting, payments, analytics, marketing, ecommerce, file storage, communication, databases, and more. External-source retrieval and write-capable management/control-plane operations are separately named and annotated."}},
    {"@type": "Question", "name": "How do I connect a new data source?", "acceptedAnswer": {"@type": "Answer", "text": "Open the CorpusIQ Connectors page, click Connect next to the tool you want, approve the vendor's read-only permission screen, and the connector shows Connected. Each connection takes under 60 seconds."}},
    {"@type": "Question", "name": "Are CorpusIQ connectors read-only?", "acceptedAnswer": {"@type": "Answer", "text": "External-source retrieval tools are marked read-only. CorpusIQ is not an AI agent. It cannot write, modify or execute anything in your connected systems, and it does not retain raw customer files or full connector response payloads. Data passes through on demand. No one at CorpusIQ can access your accounts. Operational query text, per-user tool-call metadata and bounded outcome summaries may be retained for up to 30 days; optional indexed search keeps embeddings and minimal metadata until connector revocation or account deletion. Write-capable connector-management and CorpusIQ control-plane tools are separately named and annotated."}},
    {"@type": "Question", "name": "Does CorpusIQ support database connections?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. CorpusIQ supports PostgreSQL, MSSQL (SQL Server), MySQL, Azure Cosmos DB, and MongoDB, all with read-only SQL/query access."}},
    {"@type": "Question", "name": "What if I need a connector that isn't listed?", "acceptedAnswer": {"@type": "Answer", "text": "CorpusIQ adds new connectors regularly. You can request new connectors through the Dashboard or connect custom databases via the database bridge. For proprietary APIs, contact CorpusIQ about custom MCP connector development."}},
    {"@type": "Question", "name": "How do I check which connectors are active?", "acceptedAnswer": {"@type": "Answer", "text": "Visit the CorpusIQ Dashboard to see connector status (active, paused, needs re-auth). Each connector shows real-time status indicators."}}
  ]
}
</script>

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
