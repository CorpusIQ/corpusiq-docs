---
title: Threads Growth Skill — Full Setup Guide for Hermes Agents
description: Install, configure, and use the threads-growth-skill from aradotso/marketing-skills. Automate Threads growth strategies, content publishing, and audience engagement with 745+ installs.
---

# Threads Growth Skill — Setup Guide

**Source:** [aradotso/marketing-skills](https://skills.sh/aradotso/marketing-skills) (745 installs)
**Category:** Social Media & Growth

A Threads growth and marketing automation skill for Hermes agents. Published by aradotso — the same organization behind the hermes-skills ecosystem (50+ Hermes-native skills). Enables agents to execute Threads growth strategies, content scheduling, audience engagement, and analytics — closing the Meta social stack gap alongside existing X/Twitter, LinkedIn, and Instagram skills.

---

## Installation

```bash
npx skills add aradotso/marketing-skills --skill threads-growth-skill
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Threads Account** | Meta Threads account with professional/creator dashboard access |
| **Meta Developer App** | For API-based automation: register at [developers.facebook.com](https://developers.facebook.com) |
| **Hermes Agent** | v0.16.0+ (for skill system compatibility) |
| **Instagram Account** | Threads is linked to Instagram — same credentials |

Environment variables (if using API mode):

```bash
export THREADS_ACCESS_TOKEN="<your-meta-access-token>"
export THREADS_USER_ID="<your-threads-user-id>"
```

Or in `~/.hermes/config.yaml`:

```yaml
env:
  THREADS_ACCESS_TOKEN: "<token>"
  THREADS_USER_ID: "<id>"
```

---

## Key Capabilities

### Core Features

| Capability | How to Trigger | Notes |
|---|---|---|
| Content publishing | "Post to Threads: [content]" | Supports text, images, and link posts |
| Growth analytics | "Analyze my Threads growth this week" | Follower growth, engagement rate, top posts |
| Audience insights | "Show Threads audience demographics" | Age, location, active hours |
| Content scheduling | "Schedule a Threads post for tomorrow 9am" | Queue management, best-time suggestions |
| Engagement automation | "Reply to Threads mentions from last 24h" | Auto-reply templates, sentiment filtering |
| Competitor tracking | "Track [competitor]'s Threads activity" | Follower growth, post frequency, engagement |

### CLI Command Reference

```bash
# Post content to Threads
bash SKILL_DIR/scripts/post.sh --text "Your content here" --media image.jpg

# Get growth analytics
bash SKILL_DIR/scripts/analytics.sh --period 7d

# Schedule a post
bash SKILL_DIR/scripts/schedule.sh --text "Content" --time "2026-06-29 09:00"
```

---

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Social Mining** | Monitor Threads conversations for operator pain points and product feedback |
| **Brand Presence** | Maintain daily Threads presence alongside X/Reddit/HN activity |
| **Competitive Intel** | Track competitor Threads growth and content strategies |
| **Lead Discovery** | Identify potential leads through Threads engagement and hashtag monitoring |
| **Content Amplification** | Cross-post blog content and product updates to Threads |
| **Growth Analytics** | Weekly Threads growth reports as part of the marketing dashboard |

---

## Troubleshooting

| Issue | Fix |
|---|---|
| "Access token expired" | Threads tokens expire after 60 days — regenerate at developers.facebook.com |
| "Rate limited" | Threads API has 200 posts/day limit — use scheduling to spread posts |
| "Media upload failed" | Images must be JPEG/PNG, max 10MB — resize before upload |
| "Skill not found after install" | Run `hermes skills reload` to refresh skill registry |

## Verification

```bash
# Verify skill installed
hermes skills list | grep threads-growth-skill

# Quick functional test
echo "Test post" | bash SKILL_DIR/scripts/post.sh --dry-run
```

---

*← [Skills Catalog](/hermes/skills/catalog/) | [June 28 Discovery](/hermes/skills/marketplace/new-june28-2026/) →*
*Powered by CorpusIQ*
