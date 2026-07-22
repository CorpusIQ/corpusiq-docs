# Connectors

CorpusIQ connects to 37+ business tools through a single MCP server. Each connector is read-only — we pull data into your AI tools, never write back.

## How Connectors Work

You authenticate once. After that, CorpusIQ keeps a read-only token and your AI tools can query live data from all your connected services simultaneously. No data warehouses, no ETL pipelines, no copies of your data anywhere.

## Available Connectors

### Commerce & Payments
- [Shopify](connectors/shopify.md) — Orders, products, customers, inventory
- [Stripe](connectors/stripe.md) — Payments, subscriptions, invoices, refunds
- [eBay](connectors/ebay.md) — Listings, orders, marketplace data
- [GunBroker](connectors/gunbroker.md) — Auctions, bids, inventory
- [Amazon Seller](connectors/amazon_seller.md) — Seller Central metrics

### Marketing & Advertising
- [Google Ads](connectors/google_ads.md) — Campaigns, ad groups, keywords, performance
- [Meta Ads](connectors/facebook_marketing.md) — Facebook and Instagram ad data
- [LinkedIn Ads](connectors/linkedin-ads.md) — Campaign performance and audience data
- [TikTok Ads](connectors/tiktok.md) — Ad performance and audience insights
- [Klaviyo](connectors/klaviyo.md) — Email campaigns, flows, segments
- [Mailchimp](connectors/mailchimp.md) — Campaigns, audiences, reports
- [Constant Contact](connectors/constantcontact.md) — Email marketing data
- [ActiveCampaign](connectors/activecampaign.md) — Marketing automation
- [Postscript](connectors/postscript.md) — SMS marketing
- [SEMrush](connectors/semrush.md) — SEO and competitive research
- [Ahrefs](connectors/ahrefs.md) — Backlinks, keywords, site audits

### Analytics & Reporting
- [Google Analytics 4](connectors/ga4.md) — Web analytics and traffic
- [Google Search Console](connectors/search-console.md) — Search performance and indexing
- [PostHog](connectors/posthog.md) — Product analytics
- [Search Console](connectors/search-console.md) — SEO performance
- [IndexNow](connectors/indexnow.md) — Real-time search engine indexing

### CRM & Sales
- [HubSpot](connectors/hubspot.md) — CRM, deals, contacts, tickets
- [GoHighLevel](connectors/gohighlevel.md) — All-in-one sales platform
- [Close](connectors/close.md) — Sales CRM
- [Monday.com](connectors/monday.md) — Work OS and project management

### Accounting & Finance
- [QuickBooks](connectors/quickbooks.md) — Accounting, invoices, P&L, balance sheet

### Productivity & Collaboration
- [Google Workspace](connectors/google_workspace.md) — Drive, Docs, Sheets, Calendar
- [Slack](connectors/slack.md) — Messages, channels, users
- [Notion](connectors/notion.md) — Databases, pages, wikis
- [Airtable](connectors/airtable.md) — Spreadsheet-database hybrid
- [Outlook](connectors/outlook.md) — Email, calendar, contacts
- [OneDrive](connectors/onedrive.md) — Cloud storage
- [Dropbox](connectors/dropbox.md) — Cloud storage
- [Calendly](connectors/calendly.md) — Scheduling and availability
- [IMAP](connectors/imap.md) — Email inbox access
- [Odoo](connectors/odoo.md) — ERP and business apps

### Databases
- [PostgreSQL](connectors/postgres.md) — Direct database queries
- [MongoDB](connectors/mongodb.md) — NoSQL document queries
- [MSSQL](connectors/mssql.md) — SQL Server
- [CosmosDB](connectors/cosmosdb.md) — Azure NoSQL

### Video & Media
- [YouTube](connectors/youtube.md) — Channel analytics, video performance

## AI Platform Integrations

Once your connectors are active, you can access them from any MCP-compatible AI tool:

- [ChatGPT](connectors/chatgpt-business-data-connector.md)
- [Claude](connectors/ai-mcp-server-for-business-data.md)
- [Perplexity](connectors/perplexity-business-data-mcp.md)

## Alternatives to CorpusIQ

See how we compare:
- [CorpusIQ vs Windsor.ai](connectors/windsor-ai-alternative.md)
- [CorpusIQ vs Adzviser](connectors/adzviser-alternative.md)

## Adding New Connectors

We ship new connectors regularly based on user demand. If you need a connector that's not listed here, reach out at https://corpusiq.io.
