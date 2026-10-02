---
title: "WeRead Skills - Tencent WeChat Reading Agent Skill Setup"
description: "tencent/wechatreading - official Tencent skill for WeChat Reading (WeRead): book search, bookshelf management, notes and highlights, reading stats, and reviews via a user-bound API key. 41.7K skills.sh installs. Setup guide for Hermes agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/weread-skills-setup/"
robots: "index,follow"
last_updated: "2026-09-11"
tags: ["hermes skill", "agent skill", "skill setup", "reading", "tencent", "productivity", "china"]
---

# WeRead Skills - Setup Guide

**Source:** [skills.sh](https://www.skills.sh/tencent/wechatreading) (1 skill, ~41.7K combined installs)
**GitHub:** [tencent/wechatreading](https://github.com/tencent/wechatreading) (225⭐, 14 forks, pushed Jul 1, 2026)
**Category:** Reading & Personal Knowledge
**First Seen:** May 22, 2026 on skills.sh (surfaced in the Sep 11, 2026 sweep)
**Quality Tier:** 🟡 Trusted (Gen Agent Trust Hub Pass / Socket Pass / Snyk Warn)

The official WeChat Reading (微信读书) skill from Tencent - a single Agent Skills-format package that gives an agent read access to one of China's largest digital reading platforms. Search the book catalog, inspect a user's bookshelf, pull notes and highlights, read public reviews, and produce reading statistics. Published under the first-party `tencent` org, which carries vendor authority on its own; at 41.7K installs it also clears the 20K bar outright.

---

## Installation

```bash
npx skills add tencent/wechatreading
```

The README documents the global variant:

```bash
npx skills add Tencent/WeChatReading -g
```

For Hermes Agent, copy the skill folder from a clone:

```bash
git clone https://github.com/tencent/wechatreading.git
cp -r wechatreading/skills ~/.hermes/skills/weread-skills
```

## Prerequisites

| Requirement | Details |
|---|---|
| **WEREAD_API_KEY** | Get yours at [weread.qq.com/r/weread-skills](https://weread.qq.com/r/weread-skills), then `export WEREAD_API_KEY=wrk-xxxxxxxx` |
| **WeChat Reading account** | The API key is bound to a user identity - all user-scoped endpoints (bookshelf, notes, stats) automatically inject it |
| **Chinese-language tolerance** | README and SKILL.md are written in Chinese; the agent must be able to follow original-language instructions |

## Skill Roster

| Skill | Installs | What It Does |
|---|---|---|
| `weread-skills` | 41.7K | Umbrella skill for WeChat Reading: book search (e-book / audiobook / web-novel / author / full-text), book details and chapter index, bookshelf management, notes and highlights export, reading statistics (hours, days, rankings, preference analysis), public reviews, and discovery/recommendations |

Reference docs shipped alongside the SKILL.md: `search.md`, `book.md`, `shelf.md`, `notes.md`, `readdata.md`, `review.md`, `discover.md`, `profile.md`.

## Quick Start

1. Install the skill and export `WEREAD_API_KEY`
2. Ask in natural language - "帮我搜一下三体" (search for The Three-Body Problem), "看看我的书架" (show my bookshelf), "导出我在这本书里的划线" (export my highlights from this book)
3. The skill resolves the request to the corresponding WeChat Reading endpoint and returns structured results

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **China-market research** | Full-text book search surfaces how Chinese business literature covers a topic - positioning and content research without a China phone number |
| **Operator reading systems** | Notes and highlights export feeds personal-knowledge extraction for founders who track their reading in WeRead |
| **Review intelligence** | Public review browsing gives sentiment and reception data for books, comparable to product-review mining |
| **Reference architecture** | A first-party Tencent skill with a user-bound API key is a clean example of identity-scoped agent integrations |

## Limitations / Verification

- **Snyk Warn:** the skills.sh audit renders Gen Agent Trust Hub Pass, Socket Pass, Snyk Warn. The SKILL.md plus 8 reference files are short API-pattern documents - manual review takes minutes. Review before relying on it in production.
- **Chinese-language content:** all instruction text ships untranslated; agents must handle original-language SKILL.md content.
- **User identity bound:** bookshelf, notes, and stats endpoints always act as the key's owner - no shared/team scope.
- **Platform scope:** WeChat Reading is a China-centric service; utility outside Chinese-language reading is limited.

```bash
# Verify skill installed
ls ~/.hermes/skills/weread-skills/SKILL.md
```

## Security

| Audit | Verdict |
|---|---|
| Gen Agent Trust Hub | Pass |
| Socket | Pass |
| Snyk | Warn |

## Related

- [Wind Skills - Financial Terminal Research Cluster Setup](/hermes/skills/catalog/wind-skills-setup)
- [Hithink Finance - Tonghuashun A-Share Data Skill Setup](/hermes/skills/catalog/hithink-finance-setup)
- [CorpusIQ - one MCP endpoint, all your business tools](https://corpusiq.io)

---

*← [Skills Catalog](/hermes/skills/catalog) | [Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
