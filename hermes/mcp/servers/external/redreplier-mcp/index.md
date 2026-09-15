---
title: "RedReplier MCP - Social Lead Monitoring and Reply Drafts for Agents"
description: "Remote MCP server that watches Reddit, Facebook, Hacker News, X and Bluesky for posts mentioning your product. Mentions are scored 0-100 for lead relevance, with reasoning and a drafted reply for each, so agents can triage opportunities and manage tracked keywords and alert digests."
category: Sales & Outreach
stars: n/a (new listing)
added: 2026-09-11
source: mcp.so feed
relevance: ★★★
tags: [social-listening, lead-generation, reddit, monitoring, sales, remote-mcp]
---

# RedReplier MCP

**Remote MCP server (Streamable HTTP, OAuth or API key)** - a hosted connector that turns social listening into an agent workflow. RedReplier watches Reddit, Facebook, Hacker News, X and Bluesky for posts that mention your product or keywords, scores each mention 0-100 for lead relevance, and gives your agent the reasoning behind the score plus a drafted reply, so it can surface opportunities before anyone else notices them.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth sign-in, or API key (redreplier_ prefix) via Authorization header
Endpoint: https://mcp.redreplier.com/mcp
Tools: 6 documented (list_keywords, add_keyword, search_threads, get_thread, get_relevance_score, list_subreddits)
Pricing: Free tier with paid keyword slots; keyword cost preview before activation
Category: Sales & Outreach
Built by: RedReplier
```

## Tools

| Tool | Purpose |
|---|---|
| list_keywords | List the keywords RedReplier is tracking for you |
| add_keyword | Start tracking a new keyword, optionally scoped to specific subreddits |
| search_threads | Find Reddit threads matching your keywords, filtered by subreddit, score and recency (minScore, since, limit, offset) |
| get_thread | Fetch the full details and comments of a single thread |
| get_relevance_score | Return the relevance score for a thread so you can prioritize which opportunities to review |
| list_subreddits | List the subreddits available for tracking and filtering |

The listing also documents capabilities beyond the six-tool reference - mentions from all five networks in one list filterable by website, source, status or score, a count-before-paging helper, per-mention score reasoning with a saved drafted reply, mention statuses (new, approved, rejected), monitored websites and keywords with cost previews, and email alert digest controls. Connect to discover the full live tool list.

## Connection

1. Create a RedReplier account and add at least one website or keyword set to track.
2. Add the endpoint to any MCP client. Claude Code one-liner - `claude mcp add redreplier --transport http https://mcp.redreplier.com/mcp`
3. Sign in when the OAuth browser window opens. For headless agents or clients without OAuth, create an API token at redreplier.com/api-tokens and send it as `Authorization: Bearer redreplier_...` (with or without the Bearer prefix).
4. Ask for today's high-scoring threads about your product, or have the agent triage the mention inbox and draft replies. A packaged Agent Skill is also published at github.com/redreplier/agent.

## Verification (Sep 11, 2026 midday sweep)

Endpoint live-probed over JSON-RPC: anonymous initialize returned HTTP 401 with `{"error":"invalid_token","error_description":"Authentication required"}` - live and auth-gated as designed (OAuth sign-in or API key). The mcp.so listing carries the verified and featured badges, submitted by the vendor, and the vendor docs at redreplier.com/features/agents/docs document the endpoint, Streamable HTTP transport, OAuth flow and the six-tool reference above.

## See Also

- [Reach MCP - Operate a Real LinkedIn Account from Your Agent](/docs/hermes/mcp/servers/external/reach-mcp)
- [GramClaw MCP - Telegram Outreach Workflow for Agents](/docs/hermes/mcp/servers/external/gramclaw-mcp)
