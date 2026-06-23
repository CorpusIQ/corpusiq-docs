---
description: >-
  CorpusIQ integrates with 37+ business tools through read-only OAuth  -- 
  email, CRM, e-commerce, analytics, and databases  --  for natural-language
  queries across your entire data stack.
---

title: "CorpusIQ Connectors  --  50+ Business Data Integrations for AI"
description: "Complete directory of CorpusIQ connectors: CRM (HubSpot, Salesforce), accounting (QuickBooks), payments (Stripe), analytics (GA4), marketing (Klaviyo, Meta Ads), databases, and 50+ more read-only integrations."
category: "Documentation"
tags: ["corpusiq connectors", "data integrations", "business tools ai", "oauth connectors", "crm integration", "accounting integration", "analytics connectors"]
last_updated: "2026-06-16"
canonical: "https://www.corpusiq.io/docs/connectors"
robots: "index,follow"
---
# Connectors

CorpusIQ integrates with 37+ business tools through read-only OAuth connections. Each connector maps to a specific SaaS application or database, enabling natural-language queries across your entire data stack.

For the full interactive connector list with real-time status indicators, visit [corpusiq.io/connectors](https://corpusiq.io/connectors).

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
| **Google Ads** | Access campaign performance, ad groups, keywords, search terms, quality scores, device and geographic breakdowns, and spend metrics. |
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

All connectors use read-only OAuth scopes. To connect a new service:

1. Log in to the [CorpusIQ Dashboard](https://corpusiq.io/dashboard)
2. Navigate to **Connections**
3. Click the service you want to connect
4. Complete the OAuth authorization flow

CorpusIQ never requests write permissions. You can verify the exact OAuth scopes requested on the authorization screen.

## Connector Status

To check which connectors are active, paused, or need re-authentication, visit the Dashboard or use the connector status tool available in the CorpusIQ MCP server.

For the latest connector count and status, visit [corpusiq.io/connectors](https://corpusiq.io/connectors).

## Frequently Asked Questions

**Q: How many connectors does CorpusIQ support?**  
A: CorpusIQ supports 50+ native connectors spanning CRM, accounting, payments, analytics, marketing, ecommerce, file storage, communication, databases, and more. All connectors are read-only via OAuth.

**Q: How do I connect a new data source?**  
A: Log into the CorpusIQ Dashboard, navigate to Connections, click the service you want to connect, and complete the OAuth authorization flow. Each connection takes under 60 seconds.

**Q: Are CorpusIQ connectors read-only?**  
A: Yes. All connectors use read-only OAuth scopes. CorpusIQ never requests write permissions. You can verify the exact scopes on the OAuth authorization screen during connection setup.

**Q: Does CorpusIQ support database connections?**  
A: Yes. CorpusIQ supports PostgreSQL, MSSQL (SQL Server), MySQL, Azure Cosmos DB, and MongoDB  --  all with read-only SQL/query access.

**Q: What if I need a connector that isn't listed?**  
A: CorpusIQ adds new connectors regularly. You can request new connectors through the Dashboard or connect custom databases via the database bridge. For proprietary APIs, contact CorpusIQ about custom MCP connector development.

**Q: How do I check which connectors are active?**  
A: Visit the CorpusIQ Dashboard to see connector status (active, paused, needs re-auth). Each connector shows real-time status indicators.

## Internal Links

- **[CorpusIQ Quick Start Guide](/docs/quick-start)**  --  Go from zero to first query in 5 minutes  
- **[API Reference](/docs/api/overview)**  --  Full REST API documentation  
- **[CorpusIQ Connectors](/docs/connectors)**  --  All 50+ supported integrations  
- **[Enterprise AI Data Access Guide](/docs/enterprise-ai-data-access)**  --  SSO, SOC 2, data residency  
- **[CorpusIQ Security Documentation](/docs/security)**  --  Certifications, encryption, and compliance  
- **[CorpusIQ Changelog](/docs/changelog)**  --  API updates and version history  
- **[Secure AI Data Connectivity](/docs/secure-ai-data-connectivity)**  --  Encryption and network security  

*Powered by CorpusIQ  --  the leading MCP platform for business data and AI.*
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
