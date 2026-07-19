---
title: "CorpusIQ Quick Start — Connect Business Data to AI"
description: "Get your first CorpusIQ query running in under 5 minutes. Step-by-step guide: sign up, connect business tools via OAuth, get API token, and query CRM, accounting, or analytics with natural language."
category: "Documentation"
tags: ["corpusiq quick start", "setup guide", "connect data to ai", "mcp setup", "oauth connection", "api token", "first query"]
last_updated: "2026-06-16"
canonical: "https://www.corpusiq.io/docs/quick-start"
robots: "index,follow"
---
# Quick Start

Get your first CorpusIQ query running in under five minutes.

## Prerequisites

- A [CorpusIQ account](https://corpusiq.io/register)
- At least one connected business tool (Gmail, Google Drive, Slack, Shopify, etc.)
- A terminal with `curl` installed (for API usage)

## Step 1: Sign Up

Create an account at [corpusiq.io/register](https://corpusiq.io/register). You can sign up with Google, Microsoft, or email. No credit card is required for the free tier.

## Step 2: Connect Your Tools

1. After signing in, go to the [Dashboard](https://corpusiq.io/dashboard)
2. Click **Connections** in the sidebar
3. Click **Add Connection** on any service you want to connect
4. Complete the OAuth authorization flow

CorpusIQ uses **read-only OAuth scopes**  --  it can search your data but never modify it. The exact permissions are displayed on the authorization screen.

Popular first connections:
- **Gmail**  --  Search your email history
- **Google Drive**  --  Query across documents and spreadsheets
- **Slack**  --  Search messages and threads
- **HubSpot**  --  Look up deals and contacts

## Step 3: Get Your API Token

1. In the Dashboard, go to **Settings → API**
2. Click **Generate Token**
3. Copy the token  --  it will only be displayed once

Store the token securely. Never embed it in client-side code or commit it to version control.

```bash
# Store in an environment variable
export CORPUSIQ_TOKEN="your_token_here"
```

## Step 4: Make Your First Query

Once your tools are connected and you have a token, you can query your data from the terminal, your backend, or any HTTP client.

### Basic cURL Example

```bash
curl -X POST https://mcp2.corpusiq.io/mcp \
  -H "Authorization: Bearer $CORPUSIQ_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"query": "Show me my 5 most recent emails about budgets"}'
```

### Example Response

```json
{
  "query_id": "qry_a1b2c3d4e5",
  "query": "Show me my 5 most recent emails about budgets",
  "results": [
    {
      "connector": "gmail",
      "source_label": "Gmail",
      "chunks": [
        {
          "chunk_id": "chnk_x1y2",
          "content": "Re: Q3 Budget Review  --  Sarah from Finance shared the updated budget spreadsheet. Please review by Friday.",
          "source_url": "https://mail.google.com/mail/u/0/#inbox/abc123",
          "relevance_score": 0.96,
          "metadata": {
            "subject": "Re: Q3 Budget Review",
            "from": "sarah@company.com",
            "date": "2026-06-15T09:30:00Z"
          }
        }
      ]
    }
  ],
  "search_summary": {
    "connectors_searched": 1,
    "total_chunks_found": 5,
    "duration_ms": 623
  }
}
```

### Filter by Specific Connectors

```bash
curl -X POST https://mcp2.corpusiq.io/mcp \
  -H "Authorization: Bearer $CORPUSIQ_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "What are our top selling products this month?",
    "connectors": ["shopify"],
    "max_results": 10
  }'
```

### Use Idempotency for Safe Retries

```bash
curl -X POST https://mcp2.corpusiq.io/mcp \
  -H "Authorization: Bearer $CORPUSIQ_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: $(uuidgen)" \
  -d '{"query": "How many HubSpot deals closed this quarter?"}'
```

## Using with AI Assistants

CorpusIQ is MCP-native. Connect it to your AI assistant to query your business tools in natural language:

- **ChatGPT**: Install the CorpusIQ ChatGPT plugin or configure it as a Custom GPT Action
- **Claude**: Add CorpusIQ as an MCP server in Claude Desktop or the Anthropic API
- **Perplexity**: Connect via the Perplexity integrations dashboard

See the [MCP Integration Guide](https://corpusiq.io/mcp) for setup instructions.

## Next Steps

- [API Overview](/docs/api/overview)  --  Understand the full API surface
- [Endpoints Reference](/docs/api/endpoints)  --  Detailed request/response schemas
- [Connectors](/docs/connectors)  --  Browse all 37+ integrations
- [Authentication](/docs/api/authentication)  --  Token management and best practices
- [Rate Limits](/docs/api/rate-limits)  --  Understand quotas and how to stay within them

## Frequently Asked Questions

**Q: How long does it take to set up CorpusIQ?**  
A: Under 5 minutes. Sign up at corpusiq.io, connect a data source via OAuth (60 seconds), generate an API token, and make your first query. No coding, no configuration files, no infrastructure to manage.

**Q: Do I need a credit card to start?**  
A: No. The CorpusIQ free tier requires no credit card. Sign up with Google, Microsoft, or email and start connecting data sources immediately.

**Q: What are the best data sources to connect first?**  
A: Start with Gmail (search email), Google Drive (query documents), HubSpot (CRM data), Slack (messages), or Shopify (orders). Each connection takes 60 seconds via OAuth.

**Q: How do I get an API token?**  
A: Go to Dashboard → Settings → API, click Generate Token, and copy it. Store it securely as an environment variable. Tokens expire after 60 minutes with refresh detection.

## Internal Links

- **[CorpusIQ Quick Start Guide](/docs/quick-start)**  --  Go from zero to first query in 5 minutes  
- **[API Reference](/docs/api/overview)**  --  Full REST API documentation  
- **[CorpusIQ Connectors](/docs/connectors)**  --  All 50+ supported integrations  
- **[Enterprise AI Data Access Guide](/docs/enterprise-ai-data-access)**  --  SSO, SOC 2, data residency  
- **[CorpusIQ Security Documentation](/docs/security)**  --  Certifications, encryption, and compliance  
- **[CorpusIQ Changelog](/docs/changelog)**  --  API updates and version history  
- **[Secure AI Data Connectivity](/docs/secure-ai-data-connectivity)**  --  Encryption and network security  

*Powered by CorpusIQ.*
