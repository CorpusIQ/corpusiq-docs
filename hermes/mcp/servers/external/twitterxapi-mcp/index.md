---
title: "TwitterXAPI MCP - X Data for Agents"
description: "Bearer-key remote MCP for public X/Twitter data: posts, profiles, conversations, followers, search and trends across eight tools."
category: "Marketing"
stars: n/a (hosted platform, twitterxapi.com)
added: 2026-10-02
source: "mcpservers.org server page (twitterxapi-com-mcp-server)"
relevance: ★★
tags: [x, twitter, social-media, search, trends, social-listening, remote-mcp]
---

# TwitterXAPI MCP

**Remote MCP server (Streamable HTTP, bearer API key)** - TwitterXAPI gives agents public X posts, profiles, conversations, followers, search and trends through eight hosted MCP tools, without the operator building against the X API directly.

```
Server type: Remote (Streamable HTTP)
Auth: Bearer API key (tx_live_...)
Endpoint: https://twitterxapi.com/api/mcp
Tools: 8 (search_x, get_x_user and related public-data tools)
Pricing: API key from twitterxapi.com
Category: Marketing
Built by: TwitterXAPI (twitterxapi.com)
```

## Why This Matters for Operators

Social listening usually means either a heavyweight platform subscription or building against the X API yourself, with its access tiers and rate limits. TwitterXAPI sits in between: one hosted endpoint, one key, eight tools over public data, so an agent can search posts, pull a profile and read trends inside the workflow that already does the rest of the research.

**The trade-off is scope for simplicity.** It covers public data only, which is exactly what brand monitoring, competitor research and trend tracking need, without the account-level complexity of a full API integration.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `search_x` | Search public posts, accounts and trend pages |
| `get_x_user` | Retrieve a public X user profile |
| Related tools | Conversations, followers and trends across eight hosted tools |

## Installation

```bash
claude mcp add twitterxapi --transport http https://twitterxapi.com/api/mcp --header "Authorization: Bearer tx_live_..."
```

Get an API key at `https://twitterxapi.com/api/signup`.

## Configuration

```json
{
  "mcpServers": {
    "twitterxapi": {
      "type": "http",
      "url": "https://twitterxapi.com/api/mcp",
      "headers": {
        "Authorization": "Bearer tx_live_..."
      }
    }
  }
}
```

## Business Relevance

- **Brand and comms teams** monitor mentions of the company and competitors from the assistant.
- **Growth teams** track trends and conversations to time content.
- **Sales researchers** read a prospect's public posts before outreach.
- **Analysts** pull public post volume as a demand signal alongside other data.

## Integration with CorpusIQ

TwitterXAPI adds the public-conversation layer to the business picture CorpusIQ assembles. An agent can watch for a spike in mentions of a product line, then check Stripe or GA4 to see whether it tracked to revenue, or read a prospect's public posts to inform a HubSpot outreach sequence. One server reads the public conversation, CorpusIQ reads the business, and together they connect a social signal to a business outcome.

## Limitations

- Brand new, no track record yet.
- Public X data only; no posting or account management.
- Requires a TwitterXAPI key, and pricing follows the plan selected.
- Coverage ultimately depends on what the upstream X data exposes.
- Eight tools is a focused surface rather than a full API wrapper.

## FAQ

### Does TwitterXAPI need an X developer account?

No. It is a hosted service with its own key from `https://twitterxapi.com/api/signup`, so the operator works against the MCP endpoint rather than the X API directly.

### Can it post or manage an account?

No. It exposes public read data such as posts, profiles, conversations, followers, search and trends.

### How is it authenticated?

With a bearer API key passed in the `Authorization` header (`tx_live_...`).

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
