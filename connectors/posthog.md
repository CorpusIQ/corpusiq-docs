---
title: "PostHog - Product Analytics - CorpusIQ Docs"
description: "Connect PostHog to CorpusIQ and ask plain-English questions about user behavior, product events, funnels, and retention - inside Claude or ChatGPT.."
last_updated: "2026-10-30"
---
# PostHog - Product Analytics

Connect PostHog to CorpusIQ and ask plain-English questions about user behavior, product events, funnels, and retention - inside Claude or ChatGPT.

## What it unlocks

- **Event analysis** - what events are firing, how often, from which users
- **Funnel performance** - conversion rates between key product steps
- **User profiles** - search and inspect person records across your product
- **Feature adoption** - which features are being used by which segments
- **Custom HogQL queries** - run SQL-style queries against your PostHog data

## Example prompts

```
How many users completed the onboarding funnel this week?
```

```
What is the conversion rate from signup to first data connector connected?
```

```
Which events are firing most frequently in the last 24 hours?
```

```
Show me the top 10 users by event count this month.
```

```
What percentage of users who signed up last week are still active today?
```

## How to connect

1. Go to **corpusiq.io** → Dashboard → Connectors
2. Click **PostHog**
3. Enter your PostHog Personal API Key (from PostHog → Settings → Personal API Keys)
4. Enter your PostHog Project ID
5. Done

## What data CorpusIQ can see

| Data | Available |
|------|-----------|
| Events and event definitions | ✅ |
| Person/user records | ✅ |
| Funnel conversion data | ✅ |
| Custom HogQL queries | ✅ |
| Session recordings | ❌ |
| Feature flags | ❌ |

## See also

- [Connect PostHog to Claude](../connect-posthog-to-claude.md) - the Claude Desktop setup, the questions worth asking and the read-only boundary.
- [Connect PostHog to ChatGPT](../connect-posthog-to-chatgpt.md) - the ChatGPT setup, the questions worth asking and the read-only boundary.
---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
