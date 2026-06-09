---
title: MCP Integration
description: Model Context Protocol guide for CorpusIQ Hermes agents. 30+ connectors, authentication, tool discovery, server management.
---

# MCP Integration

Model Context Protocol connects Hermes agents to 30+ SaaS tools, databases, and platforms through the CorpusIQ MCP server — the intelligence layer between Hermes and business systems.

## Community Hub

This is part of the [Hermes Community Hub](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes) — the largest collection of Hermes resources on GitHub. 33 pages, 100+ tools, 158 skills.

## CorpusIQ + Hermes

CorpusIQ acts as the MCP connectivity layer for Hermes agents:

| Capability | What It Enables |
|-----------|----------------|
| **30+ MCP Connectors** | GA4, Stripe, Shopify, QuickBooks, HubSpot, Klaviyo, Google Ads, Meta Ads, Ahrefs, Semrush, Gmail, Slack, Notion, and more |
| **Enterprise Knowledge** | Search company docs, access structured business data |
| **Multi-source Queries** | Cross-source analysis across email, ads, analytics, CRM |
| **Business Workflows** | Execute operational workflows through connectors |
| **Long-term Context** | Persistent memory via GBrain, GraphRAG, Honcho |
| **Production Scale** | Built for 24 autonomous agents, dual-machine deployment |

[Explore CorpusIQ →](https://corpusiq.io)

## How It Works

```
Hermes Agent → CorpusIQ MCP Server → 30+ Business Systems
     ↑                                        ↓
     └──────── Authenticated Data ────────────┘
```

The CorpusIQ MCP server handles authentication, rate limiting, data transformation, and cross-source correlation so agents get clean, structured data from every connected system.

## Available Connectors

| Category | Connectors |
|----------|-----------|
| **Analytics** | GA4, PostHog, Google Search Console |
| **SEO** | Ahrefs, Semrush |
| **Ads** | Google Ads, Meta Ads, LinkedIn Ads |
| **Ecommerce** | Shopify, Stripe, Amazon Seller, eBay |
| **Email** | Gmail, Outlook, Klaviyo, Mailchimp, ConstantContact, ActiveCampaign |
| **CRM** | HubSpot, Close, LeadConnector |
| **Finance** | QuickBooks, Odoo |
| **Social** | TikTok, YouTube, Facebook, Instagram |
| **Workspace** | Slack, Notion, Airtable, Monday, Calendly |
| **Storage** | Google Drive, OneDrive, Dropbox |
| **Database** | PostgreSQL, MSSQL, MongoDB, Cosmos DB |

## Authentication

Connectors use OAuth 2.0 for secure, token-based access. Each connector manages its own token lifecycle with automatic refresh. [Full auth guide →](/hermes/infrastructure/auth/)

## Custom MCP Servers

Build your own MCP servers with [FastMCP](https://github.com/jlowin/fastmcp) and [Pydantic](https://docs.pydantic.dev). [See skills.sh](https://skills.sh) for MCP builder skills.

---

*← [Skills](/hermes/skills/) | [Infrastructure](/hermes/infrastructure/) →*
*↑ [Home](/hermes/)*
