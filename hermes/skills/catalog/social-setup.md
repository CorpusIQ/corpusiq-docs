---
title: Social Content — Multi-Platform Social Media Creation for Hermes
description: Create, schedule, and optimize social media content for LinkedIn, X/Twitter, Instagram, TikTok, Facebook. Covers carousels, threads, short-form video, social listening, and engagement. 38.5K+ installs.
---

# Social Content — Setup Guide

**Source:** [coreyhaines31/marketingskills](https://skills.sh/coreyhaines31/marketingskills/social) (38,500+ installs)
**Category:** Growth / Social Media
**Quality Tier:** 🟢 Production

Expert social media strategist skill covering content creation, repurposing, scheduling, short-form video scripting, and social listening across LinkedIn, X/Twitter, Instagram, TikTok, and Facebook. Provides platform-specific formats, audience growth tactics, and engagement strategies.

---

## Installation

```bash
npx skills add coreyhaines31/marketingskills --skill social
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Product marketing context** | Optional: `.agents/product-marketing.md` for brand-aware content |
| **Brand voice guidelines** | Tone, terminology, topics to avoid |
| **Platform accounts** | Active accounts on target platforms |

---

## Key Capabilities

### Platform Quick Reference

| Platform | Best For | Frequency | Key Format |
|---|---|---|---|
| **LinkedIn** | B2B, thought leadership | 3-5x/week | Carousels, document posts, stories |
| **X/Twitter** | Tech, real-time, community | 5-10x/week | Threads, hot takes, replies |
| **Instagram** | Brand, visual, culture | 4-7x/week | Reels, carousels, stories |
| **TikTok** | Viral, trends, education | 1-3x/day | Short-form video (15-60s) |
| **Facebook** | Community, events | 2-3x/week | Groups, events, video |

### Content Types by Goal

| Goal | Best Format | Platform |
|---|---|---|
| **Thought leadership** | Carousels, threads, long-form | LinkedIn, X |
| **Product education** | Video tutorials, carousels | YouTube, LinkedIn, TikTok |
| **Community building** | Replies, quote tweets, DMs | X, Reddit, Discord |
| **Lead generation** | Case studies, testimonials, lead magnets | LinkedIn, email |
| **Brand awareness** | Short-form video, trends | TikTok, Instagram Reels |

---

## Quick Start

When invoked, the skill guides through:

1. **Goal Setting** — Brand awareness, leads, traffic, or community?
2. **Audience Analysis** — Platform demographics, content preferences
3. **Brand Voice** — Professional, casual, witty, or authoritative?
4. **Content Creation** — Platform-optimized posts with hooks and CTAs
5. **Scheduling** — Optimal posting times per platform
6. **Social Listening** — Brand mentions, competitor monitoring, engagement opportunities

---

## Hermes Integration

For CorpusIQ growth operations:

### Content Repurposing Pipeline

```
Blog Post (long-form)
  ├─► LinkedIn Carousel (slide-by-slide)
  ├─► X Thread (key insights)
  ├─► TikTok Script (60-second explainer)
  ├─► Instagram Reel (visual summary)
  └─► Reddit Discussion (ask for opinions)
```

### Social Listening Commands

```bash
# Find people asking about problems CorpusIQ solves
tvly search "how to combine Shopify and Meta Ads data" --topic news --json

# Monitor competitor mentions
tvly search "competitor_name review OR alternative" --time-range week --json
```

### Optimal Posting Schedule (MST)

| Platform | Best Times (MST) | Why |
|---|---|---|
| LinkedIn | 7-8 AM, 12-1 PM, 5-6 PM | Business hours engagement |
| X/Twitter | 6-9 AM, 12-2 PM, 7-9 PM | Tech audience patterns |
| Reddit | 5-8 AM | Morning browse, EST overlap |
| TikTok | 7-9 PM | Evening scroll peak |

---

## Tips

- Hooks determine 80% of engagement — spend 50% of creation time on the first line
- Carousels and document posts outperform text-only on LinkedIn by 3-5x
- Reply to relevant conversations before posting — engagement earns reach
- One strong take per post — multiple ideas dilute the message
- Video content: first 3 seconds determine whether they keep watching

---

## Troubleshooting

| Issue | Solution |
|---|---|
| Low engagement | Audit hooks — are they specific, emotional, or counterintuitive? |
| Zero reach | Check for shadowbans, platform restrictions, or algorithm changes |
| Content fatigue | Repurpose top performers in new formats instead of creating from scratch |
| Inconsistent posting | Build a 2-week content buffer before starting daily posting |

---

## See Also

- [[content-strategy-setup]] — Content strategy planning (companion skill)
- [Postiz](https://postiz.com) — Open-source social media scheduling tool
- [Buffer Social Media Guide](https://buffer.com/library/social-media-strategy) — Social media strategy for brands
