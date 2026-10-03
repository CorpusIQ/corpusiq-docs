---
title: "Connectors - CorpusIQ Docs - CorpusIQ"
description: "Complete directory of 40+ CorpusIQ connectors: QuickBooks, Shopify, Stripe, HubSpot, GA4, Google Ads, Meta Ads, Salesforce, Slack, Gmail, Notion, and more"
category: "Documentation"
tags: ["corpusiq connectors", "business tools ai", "chatgpt business data", "oauth connectors", "crm integration", "accounting integration", "analytics connectors", "connect business data to chatgpt", "mcp connectors"]
last_updated: "2026-09-29"
canonical: "https://www.corpusiq.io/docs/connectors"
robots: "index,follow"
---
# CorpusIQ Connectors - 40+ Business Tools, One MCP Endpoint

## What are CorpusIQ connectors?

CorpusIQ connectors are the integration layer between business data and AI assistants. Each connector maps to a SaaS application or database - QuickBooks, Shopify, Stripe, HubSpot, GA4, Salesforce, Slack, Gmail and 40+ others - and exposes its data through one MCP endpoint that ChatGPT, Claude and Perplexity can query in plain English. Every published operation declares whether it is read-only or write-capable, and each connection uses the provider's own OAuth authorization with the scopes shown on screen. CorpusIQ does not retain raw customer files or full connector response payloads; operational logs keep query text, per-user tool-call metadata and bounded outcome summaries for up to 30 days.

The connector model matters because the MCP ecosystem is large and uneven. Public registries count more than 9,400 MCP servers with 97M+ SDK downloads, yet many are unmaintained. CorpusIQ's approach is different: 40+ curated connectors to the tools businesses already run, each with documented operations, safety annotations and live status, so an AI assistant answers from a governed source instead of from a random server. For the full interactive connector list with real-time status indicators, visit [corpusiq.io/connectors](https://corpusiq.io/connectors).

## Email & Communication

| Connector | Description |
|-----------|-------------|
| **Gmail** | Search and read email messages from Gmail inboxes. Supports Gmail search syntax for filtering by sender, date, labels, and content. |
| **Outlook** | Access Microsoft 365 / Outlook email messages, folders, and mailbox metadata. Supports keyword search across inbox, sent items, and custom folders. |
| **Slack** | Query Slack workspace messages, channels, threads, and file attachments. Search across public channels and direct messages. |

## Calendar & Scheduling

| Connector | Description |
|-----------|-------------|
| **Google Calendar** | List upcoming events, search calendar entries by keyword, and check availability across multiple calendars. |
| **Calendly** | Retrieve scheduled events, event types, invitee lists, and user availability. Monitor booking volume and no-show rates. |

## File Storage & Documents

| Connector | Description |
|-----------|-------------|
| **Google Drive** | Search files, read document contents, and list folder structures. Supports Google Docs, Sheets, PDFs, and uploaded files. |
| **OneDrive** | Access Microsoft 365 OneDrive files, shared documents, and recently modified items. Reads Word, Excel, PowerPoint, and PDF content. |
| **Dropbox** | Browse and search Dropbox files, folders, and shared content. Supports full-text extraction from common document formats. |
| **AWS S3** | Query object metadata and list buckets. Read text-based objects stored in S3. |
| **Notion** | Search pages, query databases, read block content, and list workspace users across Notion workspaces. |

## Analytics & SEO

| Connector | Description |
|-----------|-------------|
| **Google Analytics 4 (GA4)** | Query web and app traffic metrics, user counts, sessions, conversions, real-time visitors, and ecommerce revenue. |
| **Google Search Console** | Retrieve search performance data, clicks, impressions, CTR, average position, sitemaps, and indexed URL status. |
| **[Google Ads](connectors/google-ads-for-agencies.md)** | Access campaign performance, ad groups, keywords, search terms, quality scores, device and geographic breakdowns, and spend metrics. Agencies can connect one MCC identity and automatically discover linked client accounts. |
| **Meta Ads (Facebook & Instagram)** | Query Facebook and Instagram ad account performance, campaigns, ad sets, individual ads, audience insights, and lead forms. |
| **LinkedIn Ads** | B2B paid-social reporting: sponsored ad accounts, campaigns, creatives, and daily performance analytics. |
| **Ahrefs** | Domain rating, backlink analysis, organic keywords, referring domains, competitor research, and keyword difficulty scores. Superior for backlink data. |
| **Semrush** | Domain overview, organic and paid keyword research, competitor analysis, backlink profiles, and domain history snapshots. |
| **PostHog** | Product analytics: events, person records, HogQL queries, and funnel conversion analysis. |

## CRM & Sales

| Connector | Description |
|-----------|-------------|
| **HubSpot** | Contacts, deals, companies, and pipeline data. Search across CRM objects and retrieve full object details. |
| **LeadConnector (GoHighLevel)** | Contacts, opportunities, appointments, conversations, payments, forms, and calendar data from the GoHighLevel platform. |
| **Close** | Leads, opportunities (pipeline deals), activities (calls, emails, notes), and sales rep data. Full-text search across leads. |
| **Odoo** | ERP and CRM: partners, sale orders, CRM leads/opportunities, invoices, products, inventory, and projects. |
| **ActiveCampaign** | Contacts, campaigns, automations, deals, lists, and tags from ActiveCampaign email marketing and CRM. |
| **Monday.com** | Workspaces, boards, groups, columns, items, and column values from Monday.com project and work management. |

## Ecommerce

| Connector | Description |
|-----------|-------------|
| **Shopify** | Orders, products, customers, inventory, and store analytics. Query order history, revenue, and product performance. |
| **Amazon Seller Central** | Orders, inventory, sales metrics, financial events, and marketplace participations. |
| **eBay** | Seller orders, transactions, performance overview, seller standards, customer service metrics, traffic reports, and funds summary. |
| **Etsy** | Shop orders, listings, revenue data, and seller performance metrics. |
| **GunBroker** | Firearms marketplace: active listings, sold items, orders, inventory summary, feedback, and fraud claims. |

## Marketing Automation

| Connector | Description |
|-----------|-------------|
| **Klaviyo** | Email and SMS campaigns, flows, abandoned cart performance, list growth, subscriber health, forms, and revenue attribution. |
| **Mailchimp** | Campaigns, audiences, subscribers, open/click rates, automation workflows, templates, and ecommerce product activity. |
| **Constant Contact** | Contacts, email campaigns, lists, segments, tags, and engagement metrics (opens, clicks, bounces). |
| **PostScript** | SMS marketing subscribers, keywords, and shop analytics for Shopify merchants. |

## Financial

| Connector | Description |
|-----------|-------------|
| **QuickBooks** | Profit & loss, balance sheet, invoices, payments, accounts receivable/payable, vendors, customers, and chart of accounts. |
| **Stripe** | Charges, customers, payouts, balance transactions, refunds, disputes, and current balance. |

## Social Media

| Connector | Description |
|-----------|-------------|
| **YouTube** | Channel analytics, video performance, viewer geography, transcripts, comments, and search. |
| **TikTok** | Account analytics, video engagement metrics (views, likes, shares, comments), and profile data. |

## Databases

| Connector | Description |
|-----------|-------------|
| **PostgreSQL** | Execute read-only SQL queries, list tables, and describe schemas on PostgreSQL databases. |
| **SQL Server (MSSQL)** | Read-only SQL queries, table listing, and schema inspection on Microsoft SQL Server databases. |
| **MySQL** | Query MySQL databases with read-only SELECT statements. |
| **Azure Cosmos DB** | Read-only SQL queries on Cosmos DB containers, container insights, and distinct counts. |
| **MongoDB** | Query MongoDB collections with read-only access. |

## Collaboration & Productivity

| Connector | Description |
|-----------|-------------|
| **Google Sheets** | Read spreadsheet data from Google Sheets by sheet name and range. |
| **Airtable** | Browse bases, list tables, search records, and retrieve structured data from Airtable databases. |

## Connecting a New Service

Each connector requests the provider scopes needed for its documented operations. To connect a new service:

1. Log in to the [CorpusIQ Dashboard](https://corpusiq.io/dashboard)
2. Navigate to **Connections**
3. Click the service you want to connect
4. Complete the OAuth authorization flow

You can verify the exact provider scopes requested on the authorization screen and inspect each MCP tool's safety annotations.

## Connector Status

To check which connectors are active, paused, or need re-authentication, visit the Dashboard or use the connector status tool available in the CorpusIQ MCP server.

For the latest connector count and status, visit [corpusiq.io/connectors](https://corpusiq.io/connectors).

## Frequently Asked Questions

### How many connectors does CorpusIQ support?

CorpusIQ supports 40+ native connectors spanning CRM, accounting, payments, analytics, marketing, ecommerce, file storage, communication, databases, and more. External-source retrieval and write-capable management/control-plane operations are separately named and annotated.

### How do I connect a new data source?

Log into the CorpusIQ Dashboard, navigate to Connections, click the service you want to connect, and complete the OAuth authorization flow. Each connection takes under 60 seconds.

### Are CorpusIQ connectors read-only?

External-source retrieval tools are marked read-only. Write-capable connector-management and CorpusIQ control-plane tools are separately named and annotated. Provider scopes vary by connector and are shown during authorization.

### Does CorpusIQ support database connections?

Yes. CorpusIQ supports PostgreSQL, MSSQL (SQL Server), MySQL, Azure Cosmos DB, and MongoDB  --  all with read-only SQL/query access.

### What if I need a connector that isn't listed?

CorpusIQ adds new connectors regularly. You can request new connectors through the Dashboard or connect custom databases via the database bridge. For proprietary APIs, contact CorpusIQ about custom MCP connector development.

### How do I check which connectors are active?

Visit the CorpusIQ Dashboard to see connector status (active, paused, needs re-auth). Each connector shows real-time status indicators.

## Connector setup guides

Each connector has a dedicated setup guide with required scopes, example questions, and a plain-English walkthrough. Jump straight to the tool you use:

[ActiveCampaign](/connectors/activecampaign) · [Adzviser (alternative)](/connectors/adzviser-alternative)
[Ahrefs](/connectors/ahrefs) · [Airtable](/connectors/airtable)
[Amazon Seller](/connectors/amazon_seller) · [Calendly](/connectors/calendly)
[Close](/connectors/close) · [Constant Contact](/connectors/constantcontact)
[Azure Cosmos DB](/connectors/cosmosdb) · [Dropbox](/connectors/dropbox)
[eBay](/connectors/ebay) · [Meta (Facebook, Instagram, Ads)](/connectors/facebook_marketing)
[GA4](/connectors/ga4) · [GoHighLevel (LeadConnector)](/connectors/gohighlevel)
[Google Ads](/connectors/google_ads) · [Google Workspace](/connectors/google_workspace)
[GunBroker](/connectors/gunbroker) · [HubSpot](/connectors/hubspot)
[IMAP Email](/connectors/imap) · [IndexNow](/connectors/indexnow)
[Klaviyo](/connectors/klaviyo) · [LinkedIn Ads](/connectors/linkedin-ads)
[Mailchimp](/connectors/mailchimp) · [Monday.com](/connectors/monday)
[MongoDB](/connectors/mongodb) · [Microsoft SQL Server (MSSQL)](/connectors/mssql)
[Notion](/connectors/notion) · [Odoo](/connectors/odoo)
[OneDrive](/connectors/onedrive) · [Outlook](/connectors/outlook)
[PostgreSQL](/connectors/postgres) · [PostHog](/connectors/posthog)
[Postscript](/connectors/postscript) · [QuickBooks](/connectors/quickbooks)
[Google Search Console](/connectors/search-console) · [Semrush](/connectors/semrush)
[Shopify](/connectors/shopify) · [Slack](/connectors/slack)
[Stripe](/connectors/stripe) · [TikTok](/connectors/tiktok)
[YouTube](/connectors/youtube)

Looking for something not in this list? See [how to connect a new data source](#how-do-i-connect-a-new-data-source) or browse the [full connector directory](https://corpusiq.io/connectors).

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "How many connectors does CorpusIQ support?", "acceptedAnswer": {"@type": "Answer", "text": "CorpusIQ supports 40+ native connectors spanning CRM, accounting, payments, analytics, marketing, ecommerce, file storage, communication, databases, and more. External-source retrieval and write-capable management/control-plane operations are separately named and annotated."}},
    {"@type": "Question", "name": "How do I connect a new data source?", "acceptedAnswer": {"@type": "Answer", "text": "Log into the CorpusIQ Dashboard, navigate to Connections, click the service you want to connect, and complete the OAuth authorization flow. Each connection takes under 60 seconds."}},
    {"@type": "Question", "name": "Are CorpusIQ connectors read-only?", "acceptedAnswer": {"@type": "Answer", "text": "External-source retrieval tools are marked read-only. Write-capable connector-management and CorpusIQ control-plane tools are separately named and annotated. Provider scopes vary by connector and are shown during authorization."}},
    {"@type": "Question", "name": "Does CorpusIQ support database connections?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. CorpusIQ supports PostgreSQL, MSSQL (SQL Server), MySQL, Azure Cosmos DB, and MongoDB, all with read-only SQL/query access."}},
    {"@type": "Question", "name": "What if I need a connector that isn't listed?", "acceptedAnswer": {"@type": "Answer", "text": "CorpusIQ adds new connectors regularly. You can request new connectors through the Dashboard or connect custom databases via the database bridge. For proprietary APIs, contact CorpusIQ about custom MCP connector development."}},
    {"@type": "Question", "name": "How do I check which connectors are active?", "acceptedAnswer": {"@type": "Answer", "text": "Visit the CorpusIQ Dashboard to see connector status (active, paused, needs re-auth). Each connector shows real-time status indicators."}}
  ]
}
</script>

## Internal Links

- **[CorpusIQ Quick Start Guide](/quickstart)**  --  Go from zero to first query in 5 minutes  
- **[API Reference](/api/overview)**  --  Full REST API documentation  
- **[CorpusIQ Connectors](/connectors)**  --  All 40+ supported integrations  
- **[Enterprise AI Data Access Guide](https://www.corpusiq.io/enterprise)**  --  SSO, SOC 2, data residency  
- **[CorpusIQ Security Documentation](/security)**  --  Certifications, encryption, and compliance  
- **[CorpusIQ Changelog](/blog)**  --  API updates and version history  
- **[Secure AI Data Connectivity](/security)**  --  Encryption and network security  

*Powered by CorpusIQ  --  the leading MCP platform for business data and AI.*
---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
