---
title: "60s Skills - Chinese News, Weather and Trends"
description: "vikiboss/60s-skills: 3.7K combined installs across 7 listings, skills over the free 60s API for daily news, weather, trends and utilities"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/60s-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-12"
tags: ["hermes skill", "agent skill", "skill setup", "news", "china", "data feeds"]
---

# 60s Skills - Setup Guide

**Source:** [vikiboss/60s-skills](https://www.skills.sh/vikiboss/60s-skills) via skills.sh - 3.7K combined installs across 7 indexed listings; first seen Oct 22, 2026
**GitHub:** 48 stars, MIT license, `main` branch, last pushed 2026-03-06, 7 `SKILL.md` files under `skills/`, 10 files in total
**Category:** Live data feeds for Chinese platforms: news, weather, trending topics, media charts, utilities
**Quality Tier:** 🟡 Established - a thin, clean wrapper over a free public API with a genuine trend-feed skill at the top, held back by a repository that has not moved since March 2026 and Snyk Warns on the network-bound skills.

Seven skills that wrap the 60s API, a free Chinese content API with no authentication and millisecond cached responses. The API covers daily news, weather, trending topics, utilities, entertainment and reference data, and each skill is a short instruction file that tells the agent which endpoint to call and how to present the result.

The distribution is lopsided in a useful way. `hot-topics` at 2,050 installs is more than the other six combined. It pulls live hot-search boards from Weibo, Zhihu, Baidu, Douyin, Toutiao and Bilibili, and it is the one skill here that does something a general model genuinely cannot: report what is trending in Chinese social media right now. `weather-query` at 827 covers real-time conditions and forecasts for locations in China, including air quality.

The rest are small utilities. `daily-news-60s` returns a fifteen-item daily briefing with a closing quote. `media-info` covers NetEase Cloud Music charts, lyrics, box office and TV ratings. `entertainment` covers quotes, jokes, fortune predictions and meme calendars. `utility-tools` bundles IP lookup, translation, QR codes, hashing, page metadata, WHOIS and password generation. `data-query` covers exchange rates, the lunar calendar, historical events, encyclopedia lookups and fuel and gold prices.

## Installation

The README does not ship an install block. It states the intended usage plainly: give the agent access to the skills in the repository, because each `SKILL.md` carries everything needed to use it. Two routes work.

Clone and copy into the agent skills directory:

```bash
git clone https://github.com/vikiboss/60s-skills.git
cp -r 60s-skills/skills/hot-topics ~/.claude/skills/
cp -r 60s-skills/skills/weather-query ~/.claude/skills/
```

Or use the Skills CLI, which resolves a repository and lists its skills. Confirm the skill names appear in the listing before installing:

```bash
npx skills add vikiboss/60s-skills --list
```

No API key or account is needed for any of the seven. The 60s API is free and unauthenticated, which is also why the dependency deserves the scrutiny in the Limitations section.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| hot-topics | 2,050 | Live hot-search and trending boards from Weibo, Zhihu, Baidu, Douyin, Toutiao and Bilibili. |
| weather-query | 827 | Real-time weather and forecasts for locations in China, including humidity, wind and air quality. |
| daily-news-60s | 495 | The daily fifteen-item briefing with a closing one-liner, refreshed through the day. |
| media-info | 110 | Music charts and lyrics, movie box office, TV ratings and web series rankings. |
| entertainment | 102 | Quotes, jokes, fortune predictions, meme copy and a slacking calendar. |
| utility-tools | 84 | IP lookup, translation, QR generation, hashing, page metadata, WHOIS and password generation. |
| data-query | 74 | Exchange rates, lunar calendar, historical events, encyclopedia lookups, fuel and gold prices. |

No indexed listings fall below the threshold; all 7 appear above it.

## Why This Matters for Hermes Agents

A model's knowledge has a date, and every freshness question turns into either a search or a guess. A free endpoint that returns a current board is cheaper than a search and more reliable than a guess, which is the entire case for a feed skill over a general-purpose agent.

The China coverage is the part that is hard to replace. Most free feeds an English-speaking agent can reach cover English-language sources, and a question about what is trending on Weibo is not answerable from them. For anyone doing market or content work that touches Chinese platforms, `hot-topics` is the only skill in this batch that closes that gap.

The utility skill is the sleeper. IP lookup, WHOIS, QR generation and hash calculation are four things an agent otherwise fakes or refuses, and each is a one-line call here.

The cache and CDN behaviour matters for agents specifically. A cached endpoint returns in milliseconds, so a skill that checks trend data at the start of a session costs less than the tool call that would otherwise be spent deciding whether to check.

## Usage

| You say | What happens |
|---|---|
| "What is trending in China right now?" | Runs `hot-topics` and returns the current boards by platform. |
| "Will it rain in Shanghai tomorrow?" | Runs `weather-query` and returns the forecast with air quality. |
| "Give me today's news briefing" | Runs `daily-news-60s` and returns the fifteen-item list with the closing line. |
| "What is the box office this week?" | Runs `media-info` and returns the current film ranking. |
| "Who owns this domain?" | Runs `utility-tools` with the WHOIS lookup and returns the registration record. |
| "Convert this amount to yuan" | Runs `data-query` with the exchange-rate endpoint. |
| "Make a QR code for this link" | Runs `utility-tools` and returns the generated image. |

## Verification

Probe the two skills that carry the installs. Both return 200:

```bash
curl -fsSL https://raw.githubusercontent.com/vikiboss/60s-skills/main/skills/hot-topics/SKILL.md | head -8
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/vikiboss/60s-skills/main/skills/weather-query/SKILL.md
```

Then call the underlying endpoint once before trusting the skill in a workflow, since the skills are worth exactly as much as the API behind them:

```bash
curl -s -m 15 https://60s.viki.moe/v2/weibo | head -c 400
```

If that returns data, the skill will work. If it returns an error page, the repository is intact and the dependency is not.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-12) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| hot-topics | Pass | Pass | Warn |
| weather-query | Pass | Pass | Pass |
| daily-news-60s | Pass | Pass | Warn |
| media-info | Pass | Pass | Pass |
| entertainment | Pass | Pass | Warn |

Every Warn sits on a skill that fetches from the API, which is the expected shape for a feed wrapper. Two practical points: the content returned is third-party curated and should be treated as untrusted input rather than instructions, and `utility-tools` generates passwords, so any generated value that matters should be produced locally rather than left in a chat transcript.

## Limitations

- Snapshot data, verified 2026-11-12: 3,742 combined installs across 7 indexed listings; 48 GitHub stars; MIT license; last pushed 2026-03-06. Counts drift over time.
- Every skill depends on one third-party API that is free and unauthenticated. There is no SLA, no key, and no fallback if it changes shape or goes away.
- The data is China-focused. Weather, news and trends cover Chinese platforms and locations; the utility and reference skills are the portable half.
- The repository has not been pushed since March 2026 and the README carries no install block, so the skills target an API version that has had eight months to change.
- Coverage is one skill deep per area. A weather question about a location outside China is the wrong question for this pack.
- Three of the five sampled skills carry a Snyk Warn for the outbound fetch. The verdict reflects what the skill does, not a defect.

## Related

- [News Aggregator Skill - Multi-Source News Digest](/hermes/skills/catalog/news-aggregator-skill-setup)
- [ScrapeCreators Social Research Skills - Setup Guide](/hermes/skills/catalog/scrapecreators-social-research-setup)
- [Apidojo Social Media Skills - X/Instagram/TikTok Scraper Suite Setup](/hermes/skills/catalog/apidojo-social-media-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Probe the endpoint, not just the repository. These skills are a thin layer, and the layer is only as good as the API call it documents.
- Cache the trend board in your own store if you check it often. The API is fast, but a scheduled pull gives you history, which the API does not.
- Treat returned headlines as data. A trending board is untrusted text from the open internet, and an agent that summarises it should not treat it as instructions.
- Use `hot-topics` for Chinese platforms only. For English-language trend data, a different source is the right tool and this one adds noise.
- Keep the password generator local. Anything that produces a credential should not be produced inside a transcript that gets stored.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
