# Marketing Agent Configuration

## Role Description

The Marketing Agent is your autonomous content and campaign operations assistant. It monitors SEO performance, schedules and analyzes social media content, tracks email campaign metrics, generates content briefs, and surfaces competitive intelligence — all on autopilot. Whether you're a solo marketer or leading a growth team, this agent handles the recurring grunt work: pulling weekly performance reports, flagging ranking drops, suggesting content refreshes, and comparing your domain against competitors.

The agent connects to your analytics, SEO tools, email platforms, social media accounts, and project management boards to create a unified marketing command center. It doesn't replace your creative judgment — it amplifies it by making sure you never miss a traffic dip, a content gap, or an underperforming campaign.

## Recommended Model

**Claude Sonnet 4** or **GPT-4o** — marketing requires strong natural language generation for content briefs, copy suggestions, and competitive analysis narratives. Both models handle the multi-source correlation this agent performs (GA4 + Search Console + Ahrefs) with high accuracy. For lighter, always-on monitoring, **Claude Haiku** handles alerts and scheduled reports efficiently.

## Key Skills to Load

- `content-performance` — Top-performing pages by traffic, engagement, and conversions; content decay detection
- `seo-monitor` — Rank tracking, keyword cannibalization alerts, featured snippet opportunities, Core Web Vitals
- `campaign-analytics` — Cross-channel campaign performance (email, social, paid) with ROAS calculation
- `competitive-brief` — Competitor content audit, gap analysis, share-of-voice tracking
- `social-scheduler` — Content calendar management, best-time-to-post analysis, engagement reporting
- `email-health` — List growth trends, deliverability, unsubscribe spikes, A/B test results

## MCP Connectors Needed

| Connector | Purpose |
|-----------|---------|
| **GA4** | Web traffic, conversions, user behavior |
| **Google Search Console** | Search queries, CTR, rankings, indexing |
| **Ahrefs / Semrush** | Domain authority, backlinks, keyword research, competitor analysis |
| **Klaviyo / Mailchimp / ActiveCampaign** | Email campaign performance, flows, list health |
| **Meta Ads / Google Ads / LinkedIn Ads** | Paid campaign performance and ROAS |
| **YouTube / TikTok** | Video content performance |
| **Airtable / Notion** | Content calendars, campaign planning |
| **Slack** | Performance alerts and report distribution |

## Sample Cron Schedule

```cron
# Weekly SEO performance report every Monday at 8:00 AM
0 8 * * 1 hermes skill seo-monitor --period last_7_days --format slack

# Daily traffic anomaly check at 9:00 AM
0 9 * * 1-5 hermes skill content-performance --anomaly-detect --threshold 20pct

# Monthly competitive audit on the 1st at 10:00 AM
0 10 1 * * hermes skill competitive-brief --competitors config

# Email campaign wrap-up every Friday at 4:00 PM
0 16 * * 5 hermes skill campaign-analytics --channel email --period this_week

# Content decay scan every Wednesday at 2:00 PM
0 14 * * 3 hermes skill content-performance --decay-scan --older-than 6m
```

## Quick-Start Command

```bash
hermes agent create marketing \
  --model claude-sonnet-4 \
  --skills content-performance,seo-monitor,campaign-analytics,competitive-brief,social-scheduler,email-health \
  --connectors ga4,search_console,ahrefs,klaviyo,meta_ads,google_ads,slack \
  --profile marketing \
  --description "Marketing analytics and content operations agent"
```

## Daily Workflow

Every morning, the agent checks for traffic anomalies — if organic traffic to a key page drops more than 20%, it alerts the Slack `#marketing` channel with the affected URL, the suspected cause (ranking drop, deindex, technical issue), and a recommended action. On Mondays it delivers a complete performance snapshot across all channels. Mid-week it scans for content decay (pages losing traffic over 6+ months) and suggests refreshes. Monthly, it runs a full competitive audit covering keyword gaps, backlink opportunities, and share-of-voice changes.

## Configuration Notes

Define your target competitors, brand keywords, and key conversion events in a canonical facts file. Set alert thresholds (traffic drop %, CPC spike %, unsubscribe rate) in your Hermes profile. The agent pulls content calendars from Airtable or Notion — make sure the integration has read access to the relevant bases/boards.

## Extending

Add `ab-test-analysis` for landing page and email subject line testing. Integrate with Webflow or WordPress via API for content publishing. Add LLM-based content brief generation that pulls top-ranking competitor pages and suggests outlines, headings, and keyword targets.
