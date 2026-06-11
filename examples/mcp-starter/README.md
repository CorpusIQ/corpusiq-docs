# CorpusIQ MCP Starter

Connect your AI agent to real business data in 60 seconds. No API keys. No dashboards. Just one MCP endpoint.

## Quick Start

```bash
# 1. Clone this template
git clone https://github.com/corpusiq/corpusiq-docs.git
cd corpusiq-docs/examples/mcp-starter

# 2. Add your CorpusIQ MCP endpoint to your agent
# Claude Code:
claude mcp add corpusiq --url https://mcp2.corpusiq.io/mcp --header "Authorization: YOUR_API_KEY"

# Cursor / Windsurf:
# Add to .cursor/mcp.json or .windsurf/mcp.json:
{
  "mcpServers": {
    "corpusiq": {
      "url": "https://mcp2.corpusiq.io/mcp",
      "headers": { "Authorization": "YOUR_API_KEY" }
    }
  }
}

# 3. Your agent now has 64+ business data tools
# Try: "What was our revenue last month?"
# Try: "Show me all Shopify orders over $500 this week"
# Try: "Compare Stripe MRR vs QuickBooks expenses"
```

## No-Code Path (n8n, Make, Zapier)
```bash
# n8n users: install the Postiz node then add CorpusIQ as an MCP tool node
# Point it at https://mcp2.corpusiq.io/mcp with your API key
```

## What You Get

64+ tools across 37+ data sources. Your AI agent can query:
- **Ecommerce**: Shopify, Amazon Seller, eBay, WooCommerce
- **Marketing**: Google Ads, Meta Ads, Mailchimp, Klaviyo, SEMrush
- **CRM**: HubSpot, GoHighLevel, ActiveCampaign, Monday
- **Finance**: Stripe, QuickBooks, Odoo
- **Data**: PostgreSQL, MongoDB, Google Analytics, Airtable

## How It Works

```
Your AI Agent (Claude, ChatGPT, Cursor)
     │
     │ MCP Protocol (JSON-RPC)
     ▼
CorpusIQ MCP Server (mcp2.corpusiq.io)
     │
     │ Live queries, no ETL
     ▼
Your Business Apps (Shopify, Stripe, HubSpot, etc.)
```

No data warehouse. No ETL pipelines. Direct queries to live data.

## Try It Free

30-day trial. No credit card. Sign up at [corpusiq.io](https://corpusiq.io).

## Community

- [GitHub Discussions](https://github.com/corpusiq/corpusiq-docs/discussions)
- [Discord](https://discord.gg/corpusiq)
- [r/mcp on Reddit](https://reddit.com/r/mcp)

## License

MIT — use this template for anything.
