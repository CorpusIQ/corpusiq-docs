---
title: "VoiceMoat MCP - Voice-Matched Social Publishing"
description: "Remote MCP that scores drafts against your own voice, improves and schedules them, then publishes to X and LinkedIn after a two-step confirmation."
category: "Marketing"
stars: n/a (hosted platform, voicemoat.com)
added: 2026-10-03
source: "mcpservers.org server page (prateeks367/voicemoat-mcp)"
relevance: ★★★
tags: [marketing, social-media, twitter, linkedin, content, publishing, voice, remote-mcp]
---

# VoiceMoat MCP

**Hosted MCP server** - VoiceMoat is a personal brand system for X and LinkedIn an agent can drive directly: it learns a voice profile from your published posts, scores new drafts against it, improves them, and schedules or publishes on your behalf.

```
Server type: Hosted (streamable HTTP, remote)
Auth: OAuth (sign-in, no API keys)
Endpoint: https://app.voicemoat.com/api/mcp
Requires: VoiceMoat Pro or Enterprise plan for writing tools
Tools: 15 (see below)
Registry: com.voicemoat/voicemoat
Category: Marketing
Built by: VoiceMoat (voicemoat.com)
```

## Why This Matters for Operators

Most social MCP servers are schedulers. VoiceMoat carries a per-platform voice profile built from your own posts, so the agent's drafts are measured against how you actually write, not a generic marketing tone. For a founder or operator posting consistently, that closes the gap between an agent that drafts volume and an agent that drafts volume you would actually sign off on.

The write path is also gated: publishing always asks twice. The first call returns the exact text, the destination account and a one-time confirmation code and posts nothing. Only a second call carrying that code publishes. The code is bound to the exact text and account, so a changed draft is refused and a fresh preview returned.

## Tools (15)

| Tool | What it does | Read only |
| --- | --- | --- |
| `get_me` | Which account is connected, and its plan | Yes |
| `list_profiles` | Connected X and LinkedIn profiles | Yes |
| `get_voice_profile` | Your trained voice profile for a platform | Yes |
| `get_voice_insights` | Voice Lab analysis, when run | Yes |
| `get_analytics` | Totals and top post for a window, up to 30 days | Yes |
| `list_posts` | Best posts in a window | Yes |
| `get_post` | One post in full with its numbers | Yes |
| `list_creators` | Creators you study in VoiceMoat | Yes |
| `search_inspiration` | Public LinkedIn posts from tracked creators | Yes |
| `score_voice_match` | Score text against your voice, 0 to 100 | No (uses credits) |
| `get_post_ideas` | Post ideas on a topic | No (uses credits) |
| `improve_post` | Improve a draft | No (uses credits) |
| `suggest_hooks` | Three opening lines for a topic | No (uses credits) |
| `publish_post` | Publish now, after a preview and a second confirmed call | No |
| `schedule_post` | Schedule for later, same preview and confirmation | No |

Reading costs no credits. Scoring, ideas, hooks and improving spend credits from the same pool as the web dashboard. Voice Match is a similarity score against your past posts, not a performance prediction.

## Connect

```
claude mcp add -t http voicemoat https://app.voicemoat.com/api/mcp
```

Any client that supports remote MCP over Streamable HTTP with OAuth connects with the same address. Works on any plan, but writing tools need Pro or Enterprise and refuse with an explanation until then.

## Limitations

- Works only with your own account and the profiles you connected.
- Cannot attach images, delete posts, reply to others, or send messages.
- LinkedIn analytics are as fresh as your last sync.

## FAQ

### Does VoiceMoat publish without me confirming?

No. Every publish or schedule call returns a preview with a one-time code first. Only a second call with that exact code posts, and the code works once.

### Do I need an API key?

No. Authentication is OAuth sign-in. There are no keys to store in prompts or config.

### Can it post to platforms other than X and LinkedIn?

No. VoiceMoat covers Twitter/X and LinkedIn only, with a separate voice profile per platform.

## Related

- [External MCP Server Catalog](/hermes/mcp/servers/external/) - the curated catalog
- [MCP Ecosystem Sweeps](/hermes/mcp/sweeps/) - all sweep reports
