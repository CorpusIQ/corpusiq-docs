---
title: Automated Video Generation
description: HeyGen-powered UGC video pipeline for autonomous content creation and distribution
---

# Automated Video Generation

HeyGen powers automated UGC production with professional narration, avatar presentation, and caption generation. The pipeline produces daily short-form content distributed to TikTok, Instagram Reels, and YouTube Shorts.

## Pipeline

```
Script Generation → Avatar Recording → Caption Overlay → Review → Distribution
```

### Script Generation
Agent drafts 60-90 second scripts based on daily content themes (product features, growth tactics, operator insights).

### Video Production
HeyGen API generates avatar-presented videos with professional narration and timed captions. Output: MP4 files staged on Mac Mini for review.

### Quality Review
Each video passes through automated checks: audio sync, caption accuracy, duration compliance. Flagged videos enter manual review queue.

## Distribution Targets

| Platform | Format | Frequency |
|----------|--------|-----------|
| TikTok | 9:16 vertical | Daily |
| Instagram Reels | 9:16 vertical | Daily |
| YouTube Shorts | 9:16 vertical | Daily |

## Content Themes
- CorpusIQ feature spotlights
- MCP connector tutorials
- Growth engineering tactics
- Autonomous agent operations
- Market intelligence briefs

---
title: Social Distribution
description: Centralized social publishing across 7 platforms via Postiz CLI automation
---

# Social Distribution

Postiz provides centralized publishing across LinkedIn, X, Reddit, Facebook, Instagram, TikTok, and YouTube. Publishing executes through automated workflows without manual intervention.

## Platform Matrix

| Platform | Content Type | Frequency | Automation |
|----------|-------------|-----------|------------|
| X (Twitter) | Text, threads | 3x daily | Postiz CLI |
| Reddit | Posts, comments | Help-first | PRAW |
| LinkedIn | Articles, posts | 2x daily | Postiz CLI |
| TikTok | Short video | Daily | Postiz CLI |
| Instagram | Reels, posts | Daily | Postiz CLI |
| YouTube | Shorts, long-form | Weekly | Postiz CLI |
| Facebook | Cross-posts | Daily | Postiz CLI |

## Publishing Strategy

All content follows help-first doctrine: answer real operator problems before mentioning products. Zero sales content. Every post provides standalone value.

## Rate Limit Handling

When a platform returns 429 (rate limited), the agent detects failure and pivots to an alternative platform or schedule rather than retrying. This prevents wasted API calls and account flags.

## Analytics

Publishing results logged to `post-log.jsonl` and `activity-log.jsonl`. Daily reports aggregate engagement metrics across all platforms.

---
title: Community Engagement
description: Help-first cross-platform engagement strategy for building operator community
---

# Community Engagement

The platform executes help-first engagement across YouTube, Product Hunt, Reddit, HN, and Discord. Future activation includes TikTok and Instagram engagement engines.

## Engagement Doctrine

**Help first, never sell.** Every comment must provide standalone value. Never pitch CorpusIQ in an engagement response unless directly asked. The goal is operator trust, not lead generation.

## Active Platforms

| Platform | Activity | Frequency |
|----------|----------|-----------|
| YouTube | Comment responses | Every 6 hours |
| Product Hunt | Community monitoring | Every 2 hours |
| Reddit | Help-first answers | Every 2 hours |
| Hacker News | Show HN, comments | Every 2 hours |
| Discord | 6 target communities | Continuous |

## Target Communities

- AI Agents
- Data Engineering
- SaaS Operations
- Automation Engineering
- Founder Communities
- Anthropic Developer

## Content Pattern

Each engagement follows: identify operator problem → provide solution (tools, framework, approach) → optionally reference CorpusIQ only if directly relevant. Result: organic authority building without spam.

---
title: Operational Outputs
description: Measurable results from autonomous agent operations — SEO, marketplace expansion, recruiting, and community growth
---

# Operational Outputs

The platform has produced measurable outputs across multiple domains. These are not theoretical — they are the byproduct of running a production autonomous agent platform.

## Programmatic SEO
- 15 SEO pages generated using Ahrefs keyword data
- Connector landing pages for each MCP integration
- Competitor comparison pages (CorpusIQ vs alternatives)
- MCP readiness assessment tools
- Output: indexed content driving organic discovery

## Product Hunt Operations
- Monitoring and engagement workflows
- Comment tracking and response
- Launch analytics and performance measurement

## Autonomous Recruiting
- Resume parsing and analysis
- AI-generated cover letters tailored to job descriptions
- Application management across multiple platforms
- Response monitoring via email forward-handler

## Marketplace Expansion
- MCP directory submissions (mcpservers.org, mcp.so)
- GitHub awesome-list PRs (marketingskills, awesome-mcp-servers)
- Developer ecosystem visibility
- Discovery optimization across directories

## Community Growth
- Cross-platform help-first engagement
- YouTube comment responses
- Reddit community participation
- Hacker News Show HN submissions

All outputs compound over time. Each indexed page, each directory listing, each GitHub PR contributes to long-term organic discovery without recurring ad spend.
