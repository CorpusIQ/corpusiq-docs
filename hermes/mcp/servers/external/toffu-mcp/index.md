---
title: "Toffu MCP - AI Marketing Agent for Ad Accounts"
description: "Hosted MCP that runs Google, Meta and LinkedIn ad campaigns end to end, from performance queries to staged changes and rollback."
category: "Marketing"
stars: n/a (hosted platform, toffu.ai)
added: 2026-10-03
source: "mcpservers.org server page (toffu-ai/toffu-mcp)"
relevance: ★★★
tags: [marketing, advertising, google-ads, meta-ads, linkedin-ads, campaigns, reporting, remote-mcp]
---

# Toffu MCP

**Hosted MCP server** - Toffu is an AI marketing platform an agent can drive end to end: connected ad accounts (Google, Meta, LinkedIn), analytics, content, campaigns and reports, behind one conversational surface.

```
Server type: Hosted (streamable HTTP)
Auth: Bearer API key from agent signup, or OAuth 2.1 + PKCE with Dynamic Client Registration
Endpoint: https://mcp.toffu.ai/mcp
Signup: POST https://mcp.toffu.ai/agent/signup (no email required)
Capability doc: https://toffu.ai/.well-known/toffu.json
Tools: 8 (see below)
License: repo MIT, service proprietary
Category: Marketing
Built by: Toffu (toffu.ai)
```

## Why This Matters for Operators

Most marketing MCP servers read data. Toffu is built to change it. The surface splits cleanly into a read half (`query_campaign_performance`, `creative_report`, `fetch_memory`) and a staged-write half (`propose_change`, `apply_change`, `undo_change`), so an agent proposes a campaign edit, a human or a policy approves it, and the applied change can still be rolled back. For an operator running paid acquisition on more than one platform, that staging layer is the difference between an agent that reports on spend and an agent that operates it.

`fetch_memory` searches the company's accumulated marketing memory, so context about brand, past campaigns and decided positioning does not have to be re-pasted into every session.

**Agent-native onboarding:** the server is designed so an agent can create an account and receive a key in a single call with no human in the loop, and a real `email` can be passed to make the account claimable by a person later.

## Tools

| Tool | What it does |
| --- | --- |
| `send_message` | Delegate any marketing task or question in plain language |
| `get_task_result` | Collect the answer for a `send_message` call that returned `status='working'` |
| `query_campaign_performance` | Campaign performance across all connected ad platforms |
| `creative_report` | Meta Ads creative performance report |
| `propose_change` | Propose a campaign change |
| `apply_change` | Apply an approved change |
| `undo_change` | Undo an applied change |
| `fetch_memory` | Search the company's marketing memory |

## Connect

```bash
# 1. Create an account and get a key (no email needed)
curl -X POST https://mcp.toffu.ai/agent/signup \
  -H 'content-type: application/json' \
  -d '{"company_name": "Acme"}'
# Response: api_key, company_id (and claim_url when an email was supplied)

# 2. Register the server in your client with the key as a Bearer token
claude mcp add --transport http toffu https://mcp.toffu.ai/mcp \
  --header "Authorization: Bearer <api_key>"
```

Generic client config:

```json
{
  "mcpServers": {
    "toffu": {
      "type": "streamable-http",
      "url": "https://mcp.toffu.ai/mcp",
      "headers": { "Authorization": "Bearer <api_key>" }
    }
  }
}
```

Reload the client after adding the server, since most clients only surface a new server's tools after a restart.

## FAQ

### Does Toffu require a human to set up?
No. The `POST /agent/signup` endpoint returns an `api_key` and `company_id` with no email required, which makes machine-owned accounts possible. Supplying an email makes the account claimable by a human later.

### How does Toffu avoid irreversible campaign mistakes?
Changes go through `propose_change` and only take effect on `apply_change`, and `undo_change` reverses an applied change. Nothing writes to a live ad account from a single read-style call.

### Which ad platforms are supported?
Google, Meta and LinkedIn ad accounts, alongside analytics and content channels. The `llms.txt` lists Google (Search, Gmail, Sheets, Docs, Analytics, Search Console, Ads), LinkedIn, HubSpot, Shopify, WordPress, Slack, Chrome and Reddit among the platform integrations.

## See Also

- [External MCP Server Catalog](https://www.corpusiq.io/docs/hermes/mcp/servers/external/) - the full curated list
- [CorpusIQ](https://corpusiq.io) - 40+ built-in business data connectors with OAuth 2.1 PKCE
