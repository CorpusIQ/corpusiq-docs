---
title: ContHunt MCP - Viral Short-Form Content Research
description: "Remote MCP server for viral content research: search keywords, hashtags and creators across TikTok, YouTube Shorts, Instagram Reels and LinkedIn, run a deep research agent that analyzes hooks, pacing and script structure, and get Hook Score, Virality Index and reach metrics per video. OAuth sign-in, hosted endpoint, companion agent skill."
category: Social Media Management
stars: n/a (new listing)
added: 2026-09-15
source: "chatmcp/mcpso issue #4156 (submitted Sep 15) + vendor docs at conthunt.app and conthunt.app/mcp"
relevance: ★★★
tags: [tiktok, instagram, youtube-shorts, linkedin, viral-content, content-research, trend-hunting, oauth, remote-mcp]
---

# ContHunt MCP

**A research engine for short-form virality that lives in the agent.** ContHunt aggregates viral videos across TikTok, YouTube Shorts, Instagram Reels and LinkedIn, then analyzes every frame so an assistant can answer why a video worked, what a niche is doing, and what to make next. The vendor positions it as "the third eye for your marketing": search, reverse-engineer, and act on trends without scrolling feeds by hand.

```
Server type: Remote (Streamable HTTP)
Auth: OAuth (browser sign-in on first connect; the server issues bearer tokens and instructs clients to re-register when they expire)
Endpoint: https://mcp.conthunt.app (root path)
Tools: Live tool list served from the endpoint after sign-in (the submission lists search, creator lookup, boards, analysis and research)
Pricing: Not published on the public site (login-gated; no public price page found at sweep time)
Category: Social Media Management / Content research
Built by: Synthenova Enterprises LLP (conthunt.app, Chennai, India)
```

## Why This Matters for Operators

Content teams burn hours manually hunting for ideas, watching competitor videos, and guessing why some posts blow up. ContHunt turns that into a repeatable pipeline: the agent searches thousands of short-form videos in minutes, filters noise, flags high-potential content, and then runs a deep analysis that names what made a video work - the hook, the pacing, the visuals, the script structure. Each analyzed video comes back with scored metrics (Hook Score, Virality Index, estimated reach), so content decisions rest on numbers instead of gut feel.

The Niche Hunter is the operator unlock: instead of chasing saturated topics, the agent identifies low-competition, high-velocity topics matched to a specific brand, with velocity metrics that show which videos are growing faster than the creator's own average. That is early-signal detection: catch a trend while it is still cheap to ride.

## Tools & Capabilities

The exact tool names are served from the endpoint after sign-in, and the vendor's MCP docs describe the capability surface:

| Area | What it covers |
|---|---|
| Multi-platform search | Keywords, hashtags and creators across TikTok, YouTube Shorts, Instagram Reels and LinkedIn simultaneously |
| Creator lookup | Profile-level research on specific creators |
| Boards | Save videos to boards for organized review and comparison |
| Deep research agent | Per-video analysis of hooks, pacing, visuals and script structure ("NotebookLM for short-form") |
| Metrics | Hook Score, Virality Index and estimated reach per analyzed video |
| Niche Hunter | Low-competition, high-velocity topics tailored to a brand |
| Velocity metrics | Videos growing faster than the creator's average, flagged as early signals |

## Installation

```bash
claude mcp add --transport http conthunt https://mcp.conthunt.app
```

Then run `/mcp` and sign in when asked. Other clients from the vendor's docs:

```bash
codex mcp add conthunt --url https://mcp.conthunt.app
codex mcp login conthunt

gemini mcp add --transport http -s user conthunt https://mcp.conthunt.app
# then /mcp auth conthunt

npx add-mcp https://mcp.conthunt.app --name conthunt
```

The vendor also ships an agent skill that teaches the assistant when and how to use ContHunt:

```bash
npx skills add https://conthunt.app
```

## Configuration

```json
{
  "mcpServers": {
    "conthunt": {
      "type": "http",
      "url": "https://mcp.conthunt.app"
    }
  }
}
```

Cursor users can add the same block to `~/.cursor/mcp.json`; Claude users add a custom connector named ContHunt with the URL above; Grok users add a custom connector at grok.com/connectors. The first connection opens a browser sign-in; an expired token returns an invalid_token error that instructs the client to clear its tokens and re-register.

## Business Relevance

- **Content marketers** replace manual feed scrolling with agent-run searches across four short-form platforms.
- **Agencies** research competitor content per client niche and cite Hook Score and Virality Index in reports.
- **Brands** use Niche Hunter to find low-competition topics before they saturate.
- **Founders** get reverse-engineered breakdowns of winning scripts to brief creators and editors.

## Integration with CorpusIQ

ContHunt answers what is working; CorpusIQ answers what is happening in the business. A content workflow pairs them: the agent finds the trending format and the winning hook through ContHunt, drafts the post, then pulls the brand's Shopify or GA4 numbers through CorpusIQ to attach real product and audience data before publishing. The loop closes on verification: after the post ships, CorpusIQ connectors report the traffic and revenue effect, so the next ContHunt research pass knows which formats actually converted rather than which ones just trended.

## Limitations

- Tool list is account-gated: exact tool names are served after sign-in, so the capability surface above is derived from the vendor docs.
- Pricing is not published on the public site (login-gated).
- The submission links a GitHub repo that returns 404 at sweep time (likely private); the live endpoint and vendor docs are the verifiable surface.
- Not yet listed on the MCP directories: the mcp.so submission (chatmcp/mcpso issue #4156) is pending review.
- Hosted service only; no self-host option published.

## See Also

- [MCP Servers Index](/docs/hermes/mcp/servers/external)
- [CorpusIQ Connectors](/docs/hermes/mcp/connectors)
- [ViralHunt MCP - Trending Discovery and Social Publishing for Agents](/docs/hermes/mcp/servers/external/viralhunt-mcp)
- [Genviral MCP - Social Media Creation and Publishing for AI Assistants](/docs/hermes/mcp/servers/external/genviral-mcp)
- [TikTok Transcript MCP - AI Transcriptions of Public TikTok Videos](/docs/hermes/mcp/servers/external/tiktok-transcript-mcp)
