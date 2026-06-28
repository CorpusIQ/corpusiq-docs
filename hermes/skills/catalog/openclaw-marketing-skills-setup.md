---
title: "OpenClaw Marketing Skills — Setup Guide"
description: "Install and configure the openclaw-marketing-skills from aradotso/marketing-skills — campaign management, audience targeting, and content scheduling for Hermes/OpenClaw agents."
last_updated: 2026-06-28
---

# OpenClaw Marketing Skills — Setup Guide

Marketing automation skill for Hermes and OpenClaw agents. Enables campaign management, audience targeting, content scheduling, and marketing analytics — all from agent commands.

**Publisher:** [aradotso/marketing-skills](https://github.com/aradotso/marketing-skills) | **Installs:** 714 | **Source:** [skills.sh](https://skills.sh/aradotso/marketing-skills/openclaw-marketing-skills)

## 1. Prerequisites

- Hermes Agent or OpenClaw installed
- Node.js 18+ (for `npx skills` CLI)
- Skills CLI: `npm install -g skills` or use `npx skills`

## 2. Installation

```bash
# Install the full marketing-skills collection
npx skills add aradotso/marketing-skills

# Or install just the OpenClaw marketing skill
npx skills add aradotso/marketing-skills --skill openclaw-marketing-skills
```

Verify installation:
```bash
npx skills list | grep marketing
```

## 3. Capabilities

The skill provides marketing automation workflows directly from your agent:

- **Campaign Management** — Create, schedule, and monitor marketing campaigns
- **Audience Targeting** — Segment audiences and target specific demographics
- **Content Scheduling** — Schedule posts across platforms at optimal times
- **Marketing Analytics** — Track campaign performance metrics
- **A/B Testing** — Set up and analyze split tests

## 4. Usage Examples

### Launch a Campaign
```
> launch a marketing campaign for our new AI tools product, target SaaS founders on LinkedIn
```

### Schedule Content
```
> schedule 5 posts about data integration this week, best times for B2B tech audience
```

### Analytics Check
```
> how is the Q3 campaign performing? show me conversion rates and top-performing channels
```

## 5. CorpusIQ Use Cases

This skill directly supports CorpusIQ's growth operations:

- **Growth campaigns** — Automate CorpusIQ promotional campaigns across social platforms
- **Content distribution** — Schedule and distribute CorpusIQ blog posts, case studies, and product updates
- **Audience research** — Analyze which channels drive the most qualified leads for CorpusIQ
- **Competitor monitoring** — Track competitor marketing activity and adjust positioning

Combined with existing skills (Threads growth, X/Twitter, LinkedIn), this completes the full social marketing stack for Hermes agents.

## 6. Related Skills

- [Threads Growth Skill](/hermes/skills/catalog/threads-growth-skill-setup/) — Meta Threads automation (745 installs)
- [X/Twitter Scraper](/hermes/skills/catalog/x-twitter-scraper-setup/) — X/Twitter automation
- [Impeccable](/hermes/skills/catalog/impeccable-setup/) — AI writing and content generation

## 7. Troubleshooting

| Issue | Fix |
|-------|-----|
| `npx skills` not found | `npm install -g skills` or use `npx -y skills` |
| Skill not recognized by agent | Restart the agent after installation |
| Marketing data not loading | Check network access and API keys for connected platforms |

---

*Part of the [Hermes Skills Catalog](/hermes/skills/catalog/). Discovered in the [June 28, 2026 evening sweep](/hermes/skills/marketplace/new-june28-2026-update2/).*

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace](/hermes/skills/marketplace/) →*
