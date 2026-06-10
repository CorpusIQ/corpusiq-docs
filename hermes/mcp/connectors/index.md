---
title: CorpusIQ MCP Connectors
description: Complete catalog of all available CorpusIQ MCP connectors for Hermes agents. Updated as connectors are added.
---

# CorpusIQ MCP Connectors

Every MCP connector available through the CorpusIQ platform. Hermes agents discover these automatically when connected.

To connect a new source, run `get_connector_status` to check availability, then follow the OAuth link or enter credentials.

---

## Marketing & Analytics

| Connector | What It Provides | Status |
|-----------|-----------------|--------|
| **GA4** | Web/app traffic, sessions, users, conversions, real-time visitors | Active |
| **Google Ads** | Campaigns, ad groups, keywords, search terms, quality scores, spend | Active |
| **Meta Ads** | Facebook/Instagram campaigns, ad sets, ads, impressions, ROAS | Active |
| **LinkedIn Ads** | B2B ad accounts, campaigns, creatives, daily performance | Active |
| **PostHog** | Product analytics, events, persons, HogQL queries, funnels | Active |
| **Ahrefs** | Domain rating, backlinks, organic keywords, competitors, top pages | Active |
| **Semrush** | Domain overview, organic/paid keywords, backlinks, keyword research | Active |
| **Search Console** | Clicks, impressions, CTR, position, sitemaps, URL inspection | Active |
| **Cross-Source Ads** | Correlate Google Ads spend with GA4 sessions, conversions, revenue | Active |

## Email & Marketing Automation

| Connector | What It Provides | Status |
|-----------|-----------------|--------|
| **Klaviyo** | Email/SMS campaigns, flows, abandoned cart, list growth, revenue attribution | Active |
| **Mailchimp** | Email campaigns, lists, subscribers, open/click rates, audience growth | Active |
| **ActiveCampaign** | Contacts, campaigns, automations, deals, tags, lists | Active |
| **Constant Contact** | Contacts, email campaigns, lists, segments, engagement metrics | Active |
| **PostScript** | SMS subscribers, keywords, shop analytics for Shopify merchants | Active |
| **Cross-Source Email** | Correlate Klaviyo with web traffic, ecommerce revenue, ad spend | Active |

## CRM & Sales

| Connector | What It Provides | Status |
|-----------|-----------------|--------|
| **HubSpot** | Contacts, deals, companies, pipelines, sales opportunities | Active |
| **Close CRM** | Leads, opportunities (pipeline deals), activities, full-text search | Active |
| **LeadConnector** | Contacts, opportunities, calendars, appointments, conversations, forms | Active |

## Commerce & Payments

| Connector | What It Provides | Status |
|-----------|-----------------|--------|
| **Stripe** | Account, charges, customers, payouts, balance transactions, refunds, disputes | Active |
| **Shopify** | Orders, products, customers, inventory, financials (via REST Admin API) | Active |
| **QuickBooks** | Profit & loss, invoices, balance sheet, AR/AP aging, payments, expenses | Active |
| **Amazon Seller** | Orders, inventory, sales metrics, catalog items, finances | Active |
| **eBay** | Orders, transactions, seller standards, traffic reports, funds summary | Active |
| **GunBroker** | Listings (active/sold/unsold), orders, FFL lookup, feedback, billing | Active |
| **Odoo** | Partners, sale orders, CRM leads, invoices, products, inventory, projects | Active |

## Communication & Collaboration

| Connector | What It Provides | Status |
|-----------|-----------------|--------|
| **Slack** | Channels, messages, threads, files, workspace analytics | Active |
| **Notion** | Pages, databases, blocks, users, workspace search | Active |
| **Airtable** | Bases, tables, records, search across structured data | Active |
| **Monday** | Workspaces, boards, columns, items, project status tracking | Active |
| **Calendly** | Scheduled events, event types, invitees, user availability | Active |

## Email & Calendar

| Connector | What It Provides | Status |
|-----------|-----------------|--------|
| **Gmail** | Messages, search, full message content | Active |
| **Outlook Mail** | Inbox, folders, full email content | Active |
| **Google Calendar** | Events, search, availability | Active |
| **Outlook Calendar** | Events, search, Microsoft 365 calendar access | Active |

## File Storage

| Connector | What It Provides | Status |
|-----------|-----------------|--------|
| **Google Drive** | Files, search, Sheets read access, file content | Active |
| **OneDrive** | Files, storage info, recent, shared files, file content | Active |
| **Dropbox** | Files, storage info, recent files, file content | Active |

## Content & Social

| Connector | What It Provides | Status |
|-----------|-----------------|--------|
| **TikTok** | Account analytics, video performance, engagement metrics | Active |
| **YouTube** | Channel analytics, video performance, viewer geography, transcripts | Active |

## Databases

| Connector | What It Provides | Status |
|-----------|-----------------|--------|
| **PostgreSQL** | Direct SQL queries, table listing, schema inspection | Active |
| **Microsoft SQL Server** | Direct SQL queries, table listing, schema inspection | Active |
| **Azure Cosmos DB** | SQL queries, container listing, partition-aware queries | Active |
| **MongoDB** | Document queries, collection listing | Active |

## Platform Management

| Tool | What It Does | Status |
|------|-------------|--------|
| **Connector Status** | Dashboard showing every connector's auth status with OAuth links | Active |
| **Resolve Connector** | AI-powered: maps natural language to the right connector + action | Active |
| **Enable/Disable** | Show or hide connector tools from active tool list | Active |
| **Reset Token** | Clear stale tokens for re-authentication | Active |
| **Logout All** | Disconnect from all sources at once | Active |
| **Usage Stats** | Personalized usage dashboard (calls, skills, connectors, tokens saved) | Active |

## Knowledge & Governance

| Tool | What It Does | Status |
|------|-------------|--------|
| **Canonical Facts** | User-declared business facts (pricing, taglines, team) | Active |
| **Canonical Decisions** | Decision log with context | Active |
| **Truth Sources** | Authoritative document pointers (KPI workbooks, contracts) | Active |
| **Metric Specs** | Live computed KPIs (MRR, AOV, etc.) with cross-source drift detection | Active |
| **Skills/Runbooks** | Pre-built multi-step analysis runbooks for common business questions | Active |

---

## Summary

| Category | Connector Count |
|----------|:--------------:|
| Marketing & Analytics | 9 |
| Email & Marketing Automation | 6 |
| CRM & Sales | 3 |
| Commerce & Payments | 7 |
| Communication & Collaboration | 5 |
| Email & Calendar | 4 |
| File Storage | 3 |
| Content & Social | 2 |
| Databases | 4 |
| Platform Management | 6 |
| Knowledge & Governance | 5 |
| **Total** | **37+** |

---

## Adding New Connectors

New connectors are added through CorpusIQ platform updates. When a connector is added:

1. It appears in `get_connector_status` with an OAuth link or credential form
2. The Hermes agent discovers tools automatically
3. This page should be updated to reflect the addition

To request a connector, contact CorpusIQ: [corpusiq.io](https://corpusiq.io)

---

*← [MCP Overview](/hermes/mcp/) | ↑ [Home](/hermes/)*
