# Complete MCP Connector Directory — 37+ Live Business Data Sources

This is the definitive directory of business data connectors available through MCP. Every connector listed here is live, read-only, and connects in 30 seconds via OAuth.

## By Category

### Commerce & Payments
| Connector | What You Can Query |
|-----------|-------------------|
| **Stripe** | Charges, customers, subscriptions, MRR, churn, payouts |
| **Shopify** | Orders, products, customers, inventory, refunds |
| **Amazon Seller** | Listings, orders, inventory, sales metrics |
| **eBay** | Orders, transactions, seller performance, traffic |
| **GunBroker** | Listings, orders, feedback, inventory |

### Accounting & Finance
| Connector | What You Can Query |
|-----------|-------------------|
| **QuickBooks** | P&L, balance sheet, invoices, AR/AP, chart of accounts |
| **Stripe** | Revenue, charges, disputes, balance |

### CRM & Sales
| Connector | What You Can Query |
|-----------|-------------------|
| **HubSpot** | Contacts, deals, pipeline, companies, tickets |
| **LeadConnector** | Contacts, opportunities, calendars, conversations |
| **Close** | Leads, opportunities, activities, search |
| **Odoo** | Partners, sales orders, CRM leads, invoices, inventory |
| **Monday.com** | Workspaces, boards, items, columns, status |

### Marketing & Analytics
| Connector | What You Can Query |
|-----------|-------------------|
| **GA4** | Traffic, sessions, conversions, users, real-time |
| **Google Ads** | Campaigns, keywords, spend, impressions, conversions |
| **Meta Ads** | Campaigns, ad sets, ROAS, reach, frequency |
| **LinkedIn Ads** | Campaign performance, account analytics |
| **TikTok** | Account analytics, video performance, engagement |
| **PostHog** | Events, persons, funnels, HogQL queries |
| **Ahrefs** | Domain rating, backlinks, organic keywords, competitors |
| **Semrush** | Domain overview, organic/paid keywords, backlinks |
| **Google Search Console** | Clicks, impressions, CTR, position, sitemaps |
| **Bing Webmaster** | Rank, traffic, query stats, crawl stats |

### Email & SMS Marketing
| Connector | What You Can Query |
|-----------|-------------------|
| **Klaviyo** | Campaigns, flows, revenue, lists, segments, forms |
| **Mailchimp** | Campaigns, lists, subscribers, open/click rates |
| **ActiveCampaign** | Contacts, campaigns, automations, deals, tags |
| **Constant Contact** | Contacts, campaigns, lists, engagement metrics |
| **Postscript** | SMS subscribers, keywords, analytics |

### Communication & Scheduling
| Connector | What You Can Query |
|-----------|-------------------|
| **Slack** | Channels, messages, threads, files, analytics |
| **Gmail** | Messages, search, threads |
| **Outlook** | Emails, calendar, contacts |
| **Calendly** | Events, event types, invitees, availability |
| **Notion** | Pages, databases, blocks, search, users |

### File Storage & Databases
| Connector | What You Can Query |
|-----------|-------------------|
| **Google Drive** | Files, search, sheets, docs |
| **OneDrive** | Files, search, storage |
| **Dropbox** | Files, search, storage |
| **Airtable** | Bases, tables, records, search |
| **PostgreSQL** | Direct SQL queries |
| **MSSQL** | Direct SQL queries |
| **Cosmos DB** | NoSQL queries |
| **MongoDB** | Document queries |

## What Makes These Connectors Different

**Read-only by design:** Every connector is read-only. The AI can query data but cannot create, modify, or delete anything.

**OAuth-native:** No API keys to manage. Each connector uses OAuth — 30 seconds to connect, instant to revoke.

**Cross-tool queries:** Ask across any combination of connectors. "Compare Shopify revenue to Meta Ads spend" queries both simultaneously.

**Single endpoint:** All 37+ connectors available through one MCP endpoint:
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

**Free trial — no credit card:** [corpusiq.io](https://www.corpusiq.io)

---

*This directory is maintained by CorpusIQ. Last updated: July 8, 2026. All connectors verified live.*
