---
title: "hermoso MCP Server — AI Ad Studio for Agents"
description: "Integration guide for hermoso-ai/hermoso: 52-tool AI ad studio that generates video/image/UGC ads and researches competitor ad libraries across Meta, Google, LinkedIn, TikTok, Instagram, and YouTube."
category: marketing
tags: [mcp, advertising, video-generation, ugc, competitor-research, meta-ads, google-ads, linkedin-ads]
source: awesome-mcp-servers
repo: hermoso-ai/hermoso
stars: 0
discovered: 2026-07-23
last_updated: 2026-07-23
---

# hermoso MCP Server — AI Ad Studio

**Repo:** [hermoso-ai/hermoso](https://github.com/hermoso-ai/hermoso)
**Install:** `npx -y hermoso mcp`
**Hosted endpoint:** `app.hermoso.ai/mcp`
**Pricing:** Free signup grant, no card required
**Tools:** 52
**Category:** Marketing / Advertising

## Overview

hermoso is an AI ad studio built for agents. It enables AI assistants to generate finished video, image, and UGC avatar ads for any brand — complete with script writing, voiceover, music, and brand end cards — plus research competitor ads across the Meta, Google, and LinkedIn ad libraries, as well as TikTok, Instagram, and YouTube organic content.

## Why Business Operators Need This

For a business operator running growth, marketing, and competitive intelligence, hermoso is transformative:

1. **Competitor Ad Research** — Your agent can research what ads competitors are running across Meta, Google, and LinkedIn ad libraries, then synthesize insights about messaging, creative angles, and spend patterns.
2. **UGC Video Generation** — Turn competitive insights into finished UGC-style video ads with AI avatars, voiceover, and branding — all through agent conversation, no editing software needed.
3. **Cross-Platform Analysis** — Analyze organic content performance on TikTok, Instagram, and YouTube alongside paid ads for a complete competitive picture.

**Example operator workflow:** "Research what ads our top 3 competitors are running on Meta and Google this month. Find the highest-performing creative angles. Generate 5 UGC-style video ads for our product using those insights. Include a brand end card with our logo and website."

## Installation

### Local (stdio)

Add to your MCP client configuration:

```json
{
  "mcpServers": {
    "hermoso": {
      "command": "npx",
      "args": ["-y", "hermoso", "mcp"]
    }
  }
}
```

### Hosted (remote HTTP)

Connect directly to the hosted endpoint:

```json
{
  "mcpServers": {
    "hermoso": {
      "url": "https://app.hermoso.ai/mcp",
      "transport": "streamable-http"
    }
  }
}
```

## Key Tools (52 total)

| Tool Group | Count | Key Capabilities |
|-----------|-------|-----------------|
| Video Ad Generation | ~15 | Script writing, AI avatar UGC, voiceover, music, brand end cards |
| Image Ad Generation | ~10 | Static ads, carousel, product showcase |
| Competitor Research | ~12 | Meta Ad Library, Google Ads Transparency, LinkedIn Ad Library |
| Organic Content Analysis | ~8 | TikTok, Instagram, YouTube content performance |
| Brand Asset Management | ~5 | Logo upload, brand kit, end card templates |
| Campaign Analytics | ~2 | Cross-platform performance aggregation |

## Common Queries

### Competitor Ad Research

```
"Search the Meta Ad Library for ads from [competitor] running in the last 30 days. Focus on video ads."
"Find the top-performing Google Ads from [industry] brands this quarter."
"Analyze LinkedIn Sponsored Content from [competitor] — what messaging angles are they using?"
```

### UGC Ad Generation

```
"Generate a 30-second UGC-style video ad for our product. Use a casual, testimonial tone. Include our logo as an end card."
"Create 3 variations of a Facebook image ad for our summer promotion. A/B test friendly."
"Make a TikTok-style UGC ad with an AI avatar explaining our value prop in 15 seconds."
```

### Cross-Platform Analysis

```
"Compare our organic Instagram content performance against [competitor]'s last 20 posts."
"What YouTube ad formats are working best in our category? Search 10 competitor channels."
```

## Best Practices

1. **Start with research before generation** — Use the ad library tools to understand competitor creative before generating your own.
2. **Batch generate variations** — Generate 5-10 UGC variations at once for A/B testing on Meta/Google.
3. **Use brand end cards consistently** — Upload your brand assets once, then all generated ads include your branding automatically.
4. **Combine organic + paid insights** — Cross-reference ad library data with organic content performance for complete competitive intelligence.
5. **Iterate fast** — The free signup grant lets you generate multiple rounds without cost concern. Test, learn, regenerate.

## Limitations

- New server (created July 2026) — API stability and tool coverage may evolve rapidly
- Video generation quality depends on AI model capabilities — review outputs before publishing
- Ad library data availability varies by platform (Meta most comprehensive, LinkedIn limited)
- Free tier may have usage caps — check current limits at `app.hermoso.ai`

## For Operators: Integration with CorpusIQ

hermoso complements CorpusIQ's existing MCP connectors:

- **CorpusIQ Meta Ads connector** + hermoso = Pull your own ad performance data via CorpusIQ, research competitor creative via hermoso
- **CorpusIQ Google Analytics** + hermoso = Attribute website traffic to specific ad campaigns while monitoring competitor creative
- **CorpusIQ TikTok/YouTube connectors** + hermoso = Compare your organic content benchmarks against competitor creative approaches

## See Also

- [Meta Ads MCP Guide](/hermes/mcp/#meta-ads)
- [TikTok MCP Guide](/hermes/mcp/#tiktok)
- [YouTube MCP Guide](/hermes/mcp/#youtube)
- [External MCP Server Catalog](/hermes/mcp/servers/external/)

---

*Discovered: July 23, 2026 · Source: awesome-mcp-servers PR #10414 · Category: Marketing/Advertising*
