# Connectors

CorpusIQ connects to your business tools through read-only MCP connectors.
Each connector requires a one-time OAuth authentication — you click Connect,
approve the permission screen, and your AI tools can query live data immediately.

The external-source connectors in this directory are designed for read-only retrieval and do not write back to connected vendor accounts. Separately annotated CorpusIQ control-plane tools are outside this connector directory.

## Index

### Commerce & Payments
- [Shopify](shopify.md) — Orders, products, customers, inventory
- [Stripe](stripe.md) — Payments, subscriptions, invoices, refunds
- [eBay](ebay.md) — Listings, orders, marketplace data
- [Amazon Seller](amazon_seller.md) — Seller Central metrics
- [GunBroker](gunbroker.md) — Auctions, bids, inventory

### Marketing & Advertising
- [Google Ads](google_ads.md) — Campaigns, ad groups, keywords, performance
- [Meta Ads (Facebook & Instagram)](facebook_marketing.md) — Ad accounts, campaigns, ad sets
- [LinkedIn Ads](linkedin-ads.md) — Campaign performance, audience data
- [TikTok](tiktok.md) — Ad performance, audience insights

### Web Analytics & SEO
- [GA4 — Google Analytics 4](ga4.md) — Traffic, conversions, events
- [Google Search Console](search-console.md) — Rankings, clicks, impressions
- [Ahrefs](ahrefs.md) — Backlinks, keyword rankings, site audits
- [Semrush](semrush.md) — Keyword research, competitor analysis
- [IndexNow](indexnow.md) — Real-time search engine indexing
- [YouTube](youtube.md) — Channel analytics, video performance

### Email & SMS Marketing
- [Klaviyo](klaviyo.md) — Campaigns, flows, segments
- [Mailchimp](mailchimp.md) — Campaigns, audiences, reports
- [Constant Contact](constantcontact.md) — Email campaigns, contacts
- [ActiveCampaign](activecampaign.md) — Automations, deals, contacts
- [Postscript](postscript.md) — SMS campaigns, subscribers

### CRM & Pipeline
- [HubSpot](hubspot.md) — Deals, contacts, companies, tickets
- [GoHighLevel (LeadConnector)](gohighlevel.md) — Pipelines, contacts, opportunities
- [Close](close.md) — Sales pipeline, leads, sequences
- [Monday.com](monday.md) — Boards, items, workflows

### Finance & Accounting
- [QuickBooks](quickbooks.md) — P&L, balance sheet, invoices, bills
- [Odoo](odoo.md) — ERP: accounting, inventory, sales, CRM

### Communication & Productivity
- [Google Workspace](google_workspace.md) — Gmail, Calendar, Drive, Docs, Sheets
- [Microsoft Outlook](outlook.md) — Email, Calendar, OneDrive
- [Slack](slack.md) — Messages, channels, search
- [Dropbox](dropbox.md) — Files, folders, shared links
- [OneDrive](onedrive.md) — Files, folders, SharePoint libraries
- [Notion](notion.md) — Pages, databases, comments
- [Airtable](airtable.md) — Bases, tables, records
- [Calendly](calendly.md) — Events, scheduling, invitees
- [IMAP Email](imap.md) — Read email from any IMAP account

### Databases & Analytics
- [PostgreSQL](postgres.md) — Relational database queries
- [Microsoft SQL Server (MSSQL)](mssql.md) — SQL Server queries
- [MongoDB](mongodb.md) — Document database queries
- [Azure Cosmos DB](cosmosdb.md) — Multi-model database queries
- [PostHog](posthog.md) — Product analytics, feature flags

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
5. The tab returns to CorpusIQ — the connector shows **Connected**

That's it. Your AI assistant can now query live data from that service.

Connector-specific notes (required plans, admin roles, multi-account setups) are on each individual connector page.

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
