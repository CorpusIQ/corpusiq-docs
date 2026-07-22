# Connect ChatGPT to Your Business Data

CorpusIQ lets ChatGPT query your business tools directly — no CSV exports, no copy-paste, no data warehouses.

## How It Works

1. Connect your data sources in CorpusIQ (30 seconds each, read-only)
2. Add CorpusIQ as an MCP server in ChatGPT
3. Start asking questions that pull live data

## Setup

### Step 1: Connect Your Data

Sign up at [corpusiq.io](https://corpusiq.io) and connect the tools you want ChatGPT to access. Each connector takes about 30 seconds — just click Connect and approve read-only access.

### Step 2: Add to ChatGPT

In ChatGPT settings, add an MCP server with this URL:

```
https://mcp2.corpusiq.io/mcp
```

Follow the OAuth flow to authenticate. Once connected, ChatGPT can query your data.

### Step 3: Ask Questions

Try questions like:
- "What was our revenue last month across all channels?"
- "Show me open HubSpot deals sorted by value"
- "Which Shopify products had the highest return rate?"
- "Pull up the QuickBooks P&L for Q2"

## What You Can Query

All 37+ connectors are available through ChatGPT:
- Accounting (QuickBooks)
- Ecommerce (Shopify, Stripe, eBay)
- CRM (HubSpot, Monday.com, Close)
- Marketing (Google Ads, Meta Ads, Klaviyo)
- Analytics (Google Analytics, Search Console)
- And more

## Security

CorpusIQ is read-only. ChatGPT can query your data but cannot modify anything. No data is stored or copied — queries run live and results pass through.

See our [ChatGPT connector guide](connectors/chatgpt-business-data-connector.md) for detailed setup.
