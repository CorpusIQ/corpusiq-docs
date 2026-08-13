---
title: "New Skills — July 24, 2026 Evening Marketplace Sweep"
description: "3 new publishers, 3 setup guides created, 255.9K+ combined installs. Evening cron sweep of skills.sh marketplace for Hermes-relevant skills."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-july24-2026-evening/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "skill marketplace", "skills.sh"]

---

# New Skills — July 24, 2026 (Evening)

## Summary

| Metric | Count |
|---|---|
| New skills found | 49 (post-dedup) |
| Setup guides created | 3 |
| Combined installs | ~255,900+ |
| Quality: 🟢 Production | 1 |
| Quality: 🟡 Beta | 2 |
| Quality: 🔵 Community | 0 |

## New Skills

### Web Scraping

| Skill | Publisher | Installs | Stars | Tier | Guide |
|---|---|---|---|---|---|
| **just-scrape** | scrapegraphai/just-scrape | 244.9K | 37 ★ | 🟢 | [Setup Guide](/hermes/skills/catalog/just-scrape-setup/) |

### System Administration

| Skill | Publisher | Installs | Stars | Tier | Guide |
|---|---|---|---|---|---|
| **terminal-skills** | chaterm/terminal-skills | 2.4K+ combined | 49 ★ | 🟡 | [Setup Guide](/hermes/skills/catalog/terminal-skills-setup/) |

### Business Intelligence

| Skill | Publisher | Installs | Stars | Tier | Guide |
|---|---|---|---|---|---|
| **finance-skills** | himself65/finance-skills | 8.6K+ combined | 3,064 ★ | 🟡 | [Setup Guide](/hermes/skills/catalog/finance-skills-setup/) |

## Notes

- **scrapegraphai/just-scrape** is the standout: 244.9K installs for a universal web scraping CLI. Directly applicable to Hermes agents for search, page scraping, structured extraction, multi-page crawling, and page-change monitoring. Requires ScrapeGraph AI API key.
- **chaterm/terminal-skills** provides structured knowledge for cron, systemd, network-tools, and VPN management. Primary documentation is in Chinese but commands are universal. Complements existing `linux-systemd` and `cron-design-workflow` skills.
- **himself65/finance-skills** enables market data fetching (yfinance), stock correlation analysis, options modeling, and financial UI generation. Useful for CorpusIQ business operators needing market intelligence.
- 46 additional candidates were identified but deprioritized: mostly Claude Code-specific skills, niche use cases with low install counts (<500), private repos, or non-English-only documentation.
- Notable skipped: `composiohq/awesome-claude-skills` (69.9K ★, Claude Code focused), `lobehub/lobe-chat` (80.8K ★, full application not skills), `greensock/gsap-skills` (12.3K ★, already covered by HyperFrames docs), `sickn33/antigravity-awesome-skills` (43.8K ★, mentioned in existing catalog guides).
