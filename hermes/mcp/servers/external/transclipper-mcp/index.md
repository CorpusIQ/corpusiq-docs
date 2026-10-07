---
title: "TransClipper MCP - Viral Video Analytics for Agents"
description: "Transcripts, viral scores, creator breakouts and hook generation for TikTok, Reels and YouTube, from Claude, ChatGPT or Cursor."
category: Marketing
stars: n/a (hosted platform, transclipper.ai)
added: 2026-10-07
source: "mcpservers.org /all page 1 (Oct 7, 2026 midday sweep)"
relevance: ★★★
tags: [video, tiktok, youtube, viral-analytics, creator-research, content-marketing, oauth, remote-mcp]
---

# TransClipper MCP

**Hosted MCP server (Streamable HTTP, OAuth) that gives your AI a viral video brain** - connect it once and your assistant can transcribe any TikTok, Reel, Short or YouTube video, score why it went viral, find a creator's breakouts against their own median, and draft your next hook, all inside the chat.

```
Server type: Hosted (Streamable HTTP)
Auth: OAuth sign-in with your TransClipper account; Pro can use a Bearer API key
Endpoint: https://transclipper.ai/api/mcp
Tools: 13 across transcripts, analysis, creators, creation and account
Pricing: Free account works (3 transcripts a day); Pro unlocks full analysis, hooks, scripts and bulk
Built by: TransClipper
```

## Why This Matters for Operators

Most video tools hand an AI a raw transcript and stop. TransClipper hands it the answer: transcripts can carry a viral score, hook type and structure, and every creator video gets an outlier score against that creator's own median, so a breakout stands out even on a channel where everything performs. The operator workflow is research to draft in one thread: pull a competitor's breakouts, read what their winners share, then generate hooks and a script modelled on proven patterns in your own niche.

## Tools & Capabilities

| Tool | What the agent can do |
|---|---|
| `get_transcript` | Transcript, stats, viral score and hook type for a TikTok, Reel, Short or YouTube video |
| `get_transcripts_bulk` (Pro) | Up to 20 videos in one call |
| `get_video` / `search_my_library` | Fetch a video already in your library; search everything you have transcribed |
| `analyze_video` (Pro) | Viral score 0-100, grade, hook, structure, CTA, audience, strengths and fixes |
| `search_viral_library` | Search a library of analysed viral videos by niche, hook type and score |
| `get_creator_videos` / `explain_creator_breakouts` (Pro) | Recent posts with views and outlier scores; what a creator's winners share, as a playbook |
| `follow_creator` / `list_followed_creators` | Get new posts analysed in a Monday digest; manage the follow list |
| `generate_hooks` / `write_script` (Pro) | Five hooks with retention scores; a ready-to-film script with hook, body and CTA |
| `get_account` | Your plan and what is left this month |

Three prompt templates ship with it: `reverse_engineer_video`, `creator_breakdown` and `find_viral_ideas`.

## Installation

Claude (web, desktop and mobile), ChatGPT, Cursor, Claude Code, Windsurf, VS Code and any remote-capable MCP client:

```
claude mcp add --transport http transclipper https://transclipper.ai/api/mcp
```

Clients that only run local servers can bridge through `mcp-remote`. Sign in with your TransClipper account when prompted; the free account is enough to start.

## Configuration

```json
{
  "mcpServers": {
    "transclipper": {
      "url": "https://transclipper.ai/api/mcp"
    }
  }
}
```

Pro users can skip OAuth where a client cannot do it: create a key in Dashboard - Settings and send it as `Authorization: Bearer <key>`.

## Business Relevance

- **Content teams:** score a competitor's recent posts and mine the patterns that beat their median before planning the next month.
- **Agencies:** turn a client's niche into a hook library modelled on proven videos, with retention scores attached.
- **Founders doing their own content:** ask which of a creator's recent TikToks were breakouts and why, then draft from the same structure.

## Integration with CorpusIQ

CorpusIQ answers what is happening in your own business from the systems you already run. TransClipper answers what is working in the market - the outliers, the hooks, the structures behind them. Research the winners first, then check the plan against your own numbers.

## Limitations

- Creator listings work for TikTok and YouTube; Instagram does not expose profile post lists, so use single Reel links there.
- Pro features (full analysis, hooks, scripts, bulk transcripts, breakout reports) are gated; Pro includes 100 AI agent runs a month under fair use.
- Free tier: 3 transcripts a day, 12 creator posts, 5 viral library results, 1 followed creator.
- Transcripts are saved to your TransClipper library, the same as in the app.

## FAQ

### Is there a free tier?

Yes. A free TransClipper account works over MCP: three transcripts a day, creator outlier scores and viral library search. Pro unlocks analysis, hooks, scripts and bulk calls with no separate subscription.

### Which platforms are supported?

TikTok, Instagram Reels, YouTube Shorts and regular YouTube videos for transcripts and analysis; creator listings for TikTok and YouTube.

### Can my agent use it from automation?

Yes. On Pro, create an API key and send it as a Bearer token; this suits Cursor, Claude Code and server-side automations.

### What does it cost?

The MCP server uses your existing TransClipper plan; Pro pricing is on the TransClipper pricing page. There are no per-call credits.

## See Also

- [Selfstorming MCP - Marketing Libraries and Ideation](/hermes/mcp/servers/external/selfstorming-mcp)
- [AffiliateSpy MCP - Competitor Creator Discovery for Agents](/hermes/mcp/servers/external/affiliatespy-mcp)
- [Uxia MCP - AI User Testing and UX Research](/hermes/mcp/servers/external/uxia-mcp)
- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
