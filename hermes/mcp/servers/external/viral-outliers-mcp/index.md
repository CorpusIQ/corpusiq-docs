---
title: "Viral Outliers MCP - CorpusIQ Docs"
description: Search a continuously-crawled database of viral social media outliers, pull creator stats, generate transcripts, and crawl TikTok, Instagram or YouTube profiles on demand.
category: Content
stars: n/a (new listing)
added: 2026-08-14
source: mcpservers.org
relevance: ★★
tags: [creator-intelligence, viral-content, social-research, tiktok, instagram, youtube, content-strategy, remote-mcp]
---

# Viral Outliers MCP

**Remote MCP server (Streamable HTTP, Bearer API key)** — a continuously-crawled database of viral social media outliers exposed to AI agents. Search overperforming posts by query and platform, pull profile stats, generate transcripts, and crawl new profiles on demand, with no scraping infrastructure on your side.

```
Server type: Remote (Streamable HTTP)
Auth: Bearer API key
Endpoint: https://viraloutliers.com/api/mcp
Tools: 9+ (search, profiles, stats, transcripts, crawls, jobs, credits)
Pricing: Credit-based subscriptions (per-call credits)
Category: Content
Built by: Viral Outliers (viraloutliers.com)
```

## Why This Matters for Operators

Finding what is actually working on social usually means opening each platform and scrolling. Viral Outliers replaces that with scored search: outlier posts ranked by how far they overperform their baseline, retrievable by query and platform filter in one call.

**Content teams get the signal without the scroll.** Every capability exists as both a REST endpoint and an MCP tool, billed from one credit system, so an assistant can run the full loop — find the post, read its stats, transcribe it, compare profiles — inside one conversation.

## Tools & Capabilities

| Tool | Credits | Purpose |
|---|---|---|
| Search Viral Outlier Posts | 1 | Find overperforming posts by query, platform, min outlier score |
| Search Social Media Profiles | 1 | Discover creators matching a niche |
| Get Post Details | 1 | Full post metadata |
| Get Profile Stats | 1 | Creator performance stats |
| Transcribe a Post | 10 | Speech-to-text for video content |
| Crawl a New Profile | 40 | On-demand TikTok, Instagram, YouTube profile crawl |
| Check Job Status | Free | Poll async crawl/transcribe jobs |
| Check Credit Balance | Free | Credit meter for the workspace |
| Compare Profiles | — | Side-by-side creator comparison |

Async skills return a job reference you poll for free. The full REST contract is published in `openapi.json` and a machine-readable summary at `/llms.txt`.

## Installation

```bash
claude mcp add --transport http viral-outliers https://viraloutliers.com/api/mcp --header "Authorization: Bearer <key>"
```

Create an API key in Settings → API Keys. Subscriptions include monthly credits.

## Configuration

```json
{
  "mcpServers": {
    "viral-outliers": {
      "type": "http",
      "url": "https://viraloutliers.com/api/mcp",
      "headers": {
        "Authorization": "Bearer <key>"
      }
    }
  }
}
```

## Business Relevance

- **Content strategists** mine outlier posts for formats worth replicating
- **Creator-adjacent brands** identify partners by real performance, not follower count
- **Agencies** build competitor content benchmarks without scraping tooling
- **UGC teams** transcribe and analyze winning creative in chat

## Integration with CorpusIQ

Viral Outliers pairs with CorpusIQ's content stack: Postiz handles publishing and scheduling, while Viral Outliers feeds the research phase — which formats are overperforming, which creators to watch. A composed workflow searches outlier posts for a topic, transcribes the top hits, and hands a content brief to the publishing pipeline. The credit-metered, read-only posture matches CorpusIQ's read-only connector philosophy.

## Limitations

- Commercial credit system — heavy transcription and crawling burn credits fast
- No self-host path
- Coverage limited to TikTok, Instagram, and YouTube
- Brand new — no track record yet

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
