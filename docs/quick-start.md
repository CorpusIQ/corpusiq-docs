# Quick Start

Get your first CorpusIQ query running in under five minutes.

## Prerequisites

- A [CorpusIQ account](https://corpusiq.io/signup)
- At least one connected business tool (Gmail, Google Drive, Slack, Shopify, etc.)
- A terminal with `curl` installed (for API usage)

## Step 1: Sign Up

Create an account at [corpusiq.io/signup](https://corpusiq.io/signup). You can sign up with Google, Microsoft, or email. No credit card is required for the free tier.

## Step 2: Connect Your Tools

1. After signing in, go to the [Dashboard](https://corpusiq.io/dashboard)
2. Click **Connections** in the sidebar
3. Click **Add Connection** on any service you want to connect
4. Complete the OAuth authorization flow

CorpusIQ uses **read-only OAuth scopes** — it can search your data but never modify it. The exact permissions are displayed on the authorization screen.

Popular first connections:
- **Gmail** — Search your email history
- **Google Drive** — Query across documents and spreadsheets
- **Slack** — Search messages and threads
- **HubSpot** — Look up deals and contacts

## Step 3: Get Your API Token

1. In the Dashboard, go to **Settings → API**
2. Click **Generate Token**
3. Copy the token — it will only be displayed once

Store the token securely. Never embed it in client-side code or commit it to version control.

```bash
# Store in an environment variable
export CORPUSIQ_TOKEN="your_token_here"
```

## Step 4: Make Your First Query

Once your tools are connected and you have a token, you can query your data from the terminal, your backend, or any HTTP client.

### Basic cURL Example

```bash
curl -X POST https://api.corpusiq.io/v1/query \
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
          "content": "Re: Q3 Budget Review — Sarah from Finance shared the updated budget spreadsheet. Please review by Friday.",
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
curl -X POST https://api.corpusiq.io/v1/query \
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
curl -X POST https://api.corpusiq.io/v1/query \
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

See the [MCP Integration Guide](https://corpusiq.io/docs/mcp) for setup instructions.

## Next Steps

- [API Overview](/docs/api/overview) — Understand the full API surface
- [Endpoints Reference](/docs/api/endpoints) — Detailed request/response schemas
- [Connectors](/docs/connectors) — Browse all 37+ integrations
- [Authentication](/docs/api/authentication) — Token management and best practices
- [Rate Limits](/docs/api/rate-limits) — Understand quotas and how to stay within them
