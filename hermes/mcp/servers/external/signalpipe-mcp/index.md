---
title: "SignalPipe MCP - Buying-Intent Lead Detection"
description: "Three-judge swarm scores posts, emails and tickets for buying intent, drafts replies you approve, and nurtures prospects with objection memory."
category: Sales & Outreach
stars: 0 (MIT plugin, AbYousef739/signalpipe)
added: 2026-09-30
source: "mcpservers.org server page (abyousef739/signalpipe)"
relevance: ★★★
tags: [lead-generation, buying-intent, sales-intelligence, prospect-nurturing, reddit, outreach, approval-gated, remote-mcp]
---

# SignalPipe MCP

**Agentic sales pipeline: buying-intent detection, swarm-scored qualification and prospect nurturing.** SignalPipe judges whether the author of a post, email or ticket wants to buy. Your agent brings text from anywhere it reads, an optional scout reads the RSS, subreddit or HN feeds you choose, three independent judges rule on borderline signals, each kept lead gets a drafted reply, and only real leads reach you for approval. Works through any MCP client or as an OpenClaw plugin.

```
Server type: Remote (Streamable HTTP)
Auth: Bearer operator key
Endpoint: https://api.signalpipe.io/mcp
Tools: 29 across signal acquisition, nurture, sender and reader
Pricing: $29/mo (3,000 judgements) or $79/mo (9,000)
Category: Sales & Outreach
Built by: signalpipe.io (plugin MIT licensed)
```

## Why This Matters for Operators

Social mining by hand means reading hundreds of posts to find the three people who want to buy, then writing each reply from scratch. SignalPipe moves the reading, scoring and drafting to a managed brain and leaves the human only the approval step. Competitor-switch posts are hard-floored and always reach the queue, and borderline posts go to a three-judge panel (Skeptic, Analyst, Optimist) so split verdicts are visible instead of hidden.

The nurture engine makes follow-up consistent. Every prospect carries a temperature score across 14 signal types, an intent-based mode (Nurture, Sales, Closing, Recovery, Dead), and permanent objection memory: if someone said the price is too high, that angle is never repeated. One-directional mode transitions mean no oscillation and no spam.

## Tools & Capabilities

| Area | Representative tools |
|---|---|
| Signal acquisition | get_missions, approve_mission, reject_mission, scout_now, add_station, suggest_anchors |
| Nurture engine | track_prospect, record_reply, get_pipeline, score_signal (paste any text for a score) |
| Sender | start_sender, stop_sender, sender_status (posts pre-approved missions with your own Reddit creds) |
| Reader | read_feeds, preview_station (check a feed for buyers before adding it) |

Scoring is multilingual (English, Spanish, French, German, Portuguese, Finnish), sarcasm-aware with fail-open behavior, and reinforcement-learned: every approve or reject adjusts the source feed's weight, so one noisy subreddit gets demoted without dragging down the rest of the product.

## Installation

```bash
claude mcp add --transport http signalpipe https://api.signalpipe.io/mcp
```

Subscribe at signalpipe.io, create the operator key in the console (shown once), and attach it as the Authorization header with the Bearer scheme. OpenClaw users can install the plugin instead; the plugin and daemon are MIT licensed while the managed brain is a subscription.

## Configuration

```json
{
  "mcpServers": {
    "signalpipe": {
      "type": "http",
      "url": "https://api.signalpipe.io/mcp"
    }
  }
}
```

The optional in-plugin Reddit sender needs a Reddit script app's credentials, which stay on your machine and are never sent to SignalPipe. Public comments and DMs are never sent without a person approving each one.

## Business Relevance

- **Founders and growth operators** turn Reddit, HN and RSS feeds into a reviewed lead queue instead of a reading backlog
- **Outbound teams** get drafts that answer what the person actually asked, mentioning the product only when they asked for a tool
- **Sales leads** track prospect temperature and objections across the pipeline without a CRM
- **OpenClaw and Claude Code users** keep the scoring hosted while the sending runs on their own credentials

## Integration with CorpusIQ

SignalPipe finds the demand; CorpusIQ serves the product data. A composed workflow: SignalPipe flags a buying-intent post and drafts the reply, and CorpusIQ supplies the live revenue, churn or support numbers the reply should reference, pulled from Stripe, HubSpot and GA4 connectors. For agencies running both, lead research and business data answers sit in the same agent session.

## Limitations

- Brand new listing with no track record yet (0 GitHub stars at catalog time)
- The managed brain is a hosted subscription; only the plugin and daemon are open source
- Judgements are metered: 3,000 to 9,000 per month by plan
- X sending needs a separate daemon and a paid X API account; Reddit sending needs a Reddit script app

## FAQ

### Does SignalPipe auto-send DMs or replies?

No. Private messages and X replies always wait for your approval, and Reddit and X require recipient consent before an app sends anything.

### What is a judgement?

One three-judge panel run. Clear noise and clear buyers are decided without convening the panel and spend nothing.

### Can I use it without OpenClaw?

Yes. All 29 tools are exposed as a standard MCP server at api.signalpipe.io/mcp and work from Claude Code, Cursor or Windsurf.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
- [MediaFast MCP - Reddit Marketing for AI Agents](/hermes/mcp/servers/external/mediafast-mcp/)
- [AffiliateSpy MCP - Competitor Creator Discovery for Agents](/hermes/mcp/servers/external/affiliatespy-mcp/)
- [Deeplead MCP - Verified B2B Contacts for AI Agents](/hermes/mcp/servers/external/deeplead-mcp/)
- [HeyLead MCP - LinkedIn Outreach from Your Own Account](/hermes/mcp/servers/external/heylead-mcp/)
