---
title: x-use MCP — Browser-Native X (Twitter) Automation
description: "Setup and usage guide for x-use MCP — Browser-Native X (Twitter) Automation. Part of the Hermes resource directory."
last_updated: 2026-08-12
---

# x-use MCP — Browser-Native X (Twitter) Automation

**Priority:** HIGH | **Category:** Social Media / Marketing  
**Transport:** stdio (pip) | **Auth:** Cookie-based (no X API key)  
**Repository:** [ihuzaifashoukat/x-use](https://github.com/ihuzaifashoukat/x-use) (MIT)  
**Package:** `pip install x-use-mcp`  
**Discovered:** July 27, 2026 (chatmcp/mcpso #3301)

## What It Does for Operators

Multi-account X (Twitter) automation that drives a real Chrome session with your own cookies — no X API key or developer account required. 32 tools for posting, replies, keyword search, engagement, single-tweet reads (images returned as MCP content), per-account personas, proxy pools, and a persistent scheduled-action queue.

**The killer feature:** Draft-approval mode is ON by default. Write tools return a draft — nothing publishes until `approve_draft` is called. This is the safety rail that most social-media MCP servers lack.

## Installation

```bash
pip install x-use-mcp
# Start with:
x-use mcp
```

## Claude Desktop / Hermes Config

```json
{
  "mcpServers": {
    "x-use": {
      "command": "x-use",
      "args": ["mcp"],
      "env": {
        "OPENAI_API_KEY": "sk-... (optional, for auto-replies)"
      }
    }
  }
}
```

## Tools (32)

Key tool categories:
| Category | Tools | Description |
|----------|-------|-------------|
| Content | `post_tweet`, `reply_to_tweet`, `quote_tweet` | Publishing with draft-approval gate |
| Discovery | `search_tweets`, `get_trending`, `get_user_tweets` | Keyword and trend monitoring |
| Engagement | `like_tweet`, `retweet`, `follow_user` | Interaction management |
| Reading | `read_tweet`, `read_thread` | Images returned as MCP content |
| Management | `list_drafts`, `approve_draft`, `reject_draft` | Draft queue with approval workflow |
| Personas | `set_persona`, `list_personas` | Multi-account identity management |
| Scheduling | `schedule_post`, `list_scheduled`, `cancel_scheduled` | Persistent action queue |

## Operator Use Cases

1. **Help-first community presence:** Agent monitors X for questions about your product category, drafts helpful replies (never mentioning your product unless directly relevant), queues for operator approval
2. **Competitive intelligence:** Agent searches competitor mentions daily, summarizes sentiment, surfaces actionable insights
3. **Multi-account brand management:** One agent manages founder account + company account + support account with different personas per account
4. **Content distribution:** Agent schedules technical content across accounts at optimal engagement times, using draft-approval so operator reviews before publish
5. **Crisis monitoring:** Agent watches for negative brand mentions, drafts measured responses, flags for immediate review

## CorpusIQ Angle

**Direct integration path.** CorpusIQ's social-cadence engine (already supports X via Postiz/API) could route through x-use for cookie-based access, bypassing X API rate limits and costs. The draft-approval mode aligns with CorpusIQ's pre-flight gate doctrine.

## Limitations

- Requires Chrome and logged-in X session (cookie-based)
- X may detect and block automation patterns — rotate proxies and respect rate limits
- Cookie expiry requires periodic re-authentication
- New package, early community adoption
- Python-only (no Node.js distribution)
