# MCP Integration Guide

Model Context Protocol (MCP) servers extend Hermes with structured, type-safe tools. Here's every integration pattern we've tested in production.

## The CorpusIQ MCP — One OAuth, 53 Tools, 37+ Platforms

The biggest pain point in agent operations: managing 37 different API keys across 37 different platforms. The CorpusIQ MCP server solves this with a single OAuth flow.

### Quick Start

```bash
# Add to Hermes
hermes mcp add corpusiq -- url https://mcp2.corpusiq.io/mcp

# Authenticate (device login flow)
hermes mcp auth corpusiq
# → Opens browser: Enter code "ABCD-1234"
# → Authenticate with Google
# → Done. 53 tools available.
```

### Available Tools

#### CRM & Sales
```
mcp_corpusiq_crm_connector
├── list_hubspot_contacts
├── search_hubspot_contacts
├── list_hubspot_deals
├── get_hubspot_contact
├── list_leadconnector_contacts
├── get_leadconnector_opportunity
├── close_list_leads (Close CRM)
├── activecampaign_get_contacts
└── odoo_search_partners
```

#### Analytics & SEO
```
mcp_corpusiq_ga4_connector
├── list_properties
├── run_report (dimensions + metrics + date ranges)
└── get_realtime

mcp_corpusiq_ahrefs_connector
├── get_domain_overview
├── get_organic_keywords
├── get_backlinks_overview
└── get_competitors

mcp_corpusiq_semrush_connector
├── get_domain_overview
├── get_organic_keywords
├── get_paid_keywords
└── get_keyword_overview

mcp_corpusiq_search_console_connector
├── get_sites
├── get_performance
└── inspect_url

mcp_corpusiq_posthog_connector
├── list_events
├── list_persons
├── run_query (HogQL)
└── get_funnel
```

#### Email & Marketing
```
mcp_corpusiq_email_connector
├── list_gmail_messages
├── search_gmail
└── get_gmail_message

mcp_corpusiq_klaviyo_connector
├── get_campaigns
├── get_email_metrics_summary
├── get_flows
└── get_campaign_revenue

mcp_corpusiq_mailchimp_connector
├── get_campaigns
├── get_lists
├── get_campaign_report
└── search_members
```

#### Advertising
```
mcp_corpusiq_google_ads_connector
├── get_account_summary
├── list_campaigns
├── get_keyword_performance
└── get_search_terms

mcp_corpusiq_meta_ads_connector
├── get_facebook_account_insights
├── list_facebook_campaigns
├── get_facebook_campaign_insights
└── get_instagram_account_insights

mcp_corpusiq_linkedin_ads_connector
├── get_account_info
├── list_ad_accounts
├── list_campaigns
└── get_campaign_analytics
```

#### Ecommerce & Payments
```
mcp_corpusiq_stripe_connector
├── get_account
├── list_charges
├── list_customers
├── list_payouts
└── get_balance

mcp_corpusiq_amazon_seller_connector
├── list_amazon_orders
├── get_amazon_sales_metrics
└── list_amazon_inventory

mcp_corpusiq_ebay_connector
├── get_orders
├── get_seller_performance_overview
└── get_traffic_report
```

#### Finance
```
mcp_corpusiq_quickbooks_connector
├── get_profit_loss
├── list_invoices
├── get_balance_sheet
├── get_overdue_invoices
└── get_ar_aging
```

#### Social & Content
```
mcp_corpusiq_tiktok_connector
├── get_account_analytics
├── list_videos
└── get_video_analytics

mcp_corpusiq_youtube_connector
├── get_my_youtube_analytics
├── get_youtube_transcript
└── search_youtube

mcp_corpusiq_slack_connector
├── list_channels
├── search_messages
└── get_workspace_analytics
```

#### Storage & Productivity
```
mcp_corpusiq_drive_connector
├── search_drive (Google Drive)
├── list_my_onedrive_files
├── search_my_dropbox
└── read_sheet

mcp_corpusiq_notion_connector
├── notion_search
├── notion_query_database
└── notion_get_page

mcp_corpusiq_calendar_connector
├── list_my_calendar_events
├── list_my_outlook_events
└── search_my_calendar
```

#### Database Direct
```
mcp_corpusiq_database_connector
├── query_database (PostgreSQL/MSSQL)
├── list_database_tables
├── query_cosmos_database
└── list_cosmos_containers
```

---

## Query Patterns

### Cross-Source Analysis

The real power comes from querying across platforms in a single session:

```python
# "How did our Meta ads perform vs Shopify revenue this week?"

# 1. Get ad spend
meta_ads = mcp_corpusiq_meta_ads_connector(
    action="get_facebook_account_insights",
    params={"start_date": "2026-06-09", "end_date": "2026-06-15"}
)

# 2. Get revenue (via cross-source connector)
roas = mcp_corpusiq_cross_source_ads_connector(
    action="correlate_spend_vs_ga4_revenue",
    params={"customer_id": "...", "property_id": "..."}
)

# 3. Get email attribution
email = mcp_corpusiq_cross_source_email_connector(
    action="get_channel_attribution_summary"
)
```

### Automated Reporting

```python
# "Generate a weekly business health report"

# 1. Revenue
profit_loss = mcp_corpusiq_quickbooks_connector(action="get_profit_loss")
stripe = mcp_corpusiq_stripe_connector(action="get_balance")

# 2. Traffic
ga4 = mcp_corpusiq_ga4_connector(action="run_report", params={
    "property_id": "...",
    "dimensions": ["date"],
    "metrics": ["sessions", "activeUsers", "conversions"],
    "date_ranges": [{"start_date": "7daysAgo", "end_date": "today"}]
})

# 3. Email
klaviyo = mcp_corpusiq_klaviyo_connector(action="get_email_metrics_summary")

# 4. SEO
ahrefs = mcp_corpusiq_ahrefs_connector(action="get_domain_overview", params={"domain": "corpusiq.io"})
```

---

## Adding Your Own MCP Server

### Option A: FastMCP (Python)

```python
# my_server.py
from fastmcp import FastMCP

mcp = FastMCP("My Server")

@mcp.tool()
def get_dashboard_metrics():
    """Return key business metrics"""
    return {"mrr": 12500, "users": 843, "churn": 0.02}

mcp.run()
```

```bash
hermes mcp add my-server -- python my_server.py
```

### Option B: TypeScript

```typescript
// my-server.ts
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";

const server = new McpServer({ name: "my-server" });

server.tool("get_metrics", async () => ({
  content: [{ type: "text", text: JSON.stringify({ mrr: 12500 }) }]
}));
```

```bash
hermes mcp add my-server -- npx tsx my-server.ts
```

### Option C: Remote HTTP MCP

```bash
hermes mcp add remote-server -- url https://my-mcp-server.com/sse
```

---

## MCP Server Monitoring

We run three daily monitors to discover new MCP servers:

| Monitor | Sources | Schedule |
|---------|---------|----------|
| mcp-server-monitor | mcp.so, mcpservers.org | 3 AM, 11 AM, 7 PM |
| hermes-release-monitor | GitHub releases | 2 AM, 10 AM, 6 PM |
| skills-monitor | skills.sh | 4 AM, 12 PM, 8 PM |

New discoveries are reported to Telegram Topic 2 for evaluation.

---

## Troubleshooting

### "MCP server connection failed"

```bash
# Test connectivity
hermes mcp test corpusiq

# Check auth
hermes mcp auth corpusiq --check

# View logs
journalctl --user -u hermes-gateway -n 50 | grep mcp
```

### "Tool not found"

```bash
# List all available tools
hermes mcp list

# Reload MCP config
hermes mcp reload
```

### "Token expired"

```bash
# Re-authenticate
hermes mcp auth corpusiq --reauth
```

---

## Architecture Note

MCP servers run as subprocesses managed by Hermes. Each server:

- **stdio transport:** Local, zero-latency, no network dependency (recommended for custom servers)
- **HTTP transport:** Remote, supports OAuth, good for shared servers (CorpusIQ, Honcho)
- **Tool registration:** Automatic — Hermes discovers tools on connect

**The CorpusIQ advantage:** 37+ business platforms through ONE MCP server. No managing 37 API keys, no 37 different auth flows. One OAuth, one server, 53 tools.

---

*Next: [Production Cron Reference](/hermes/governance/scheduling/) · [Skills Marketplace](/hermes/skills/) · [Memory Architecture](/hermes/knowledge/)*
