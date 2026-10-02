---
title: "AAHL Skills - Smart Home & TTS Setup"
description: "Practical agent skills: Home Assistant smart-home control, Edge TTS, DuckDuckGo search, crypto data, weather, Lark/Feishu, video search, and price compare."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/aahl-skills-setup/"
robots: "index,follow"
last_updated: "2026-09-29"
tags: ["hermes skill", "agent skill", "skill setup", "smart home", "text-to-speech"]
---

# AAHL Skills - Setup Guide

**Source:** [aahl/skills](https://github.com/aahl/skills) (160⭐)
**Skill family:** `aahl/skills` (6 installable skills)
**Combined Installs:** ~41,082 across indexed listings (Sep 29, 2026 snapshot)
**Category:** Automation
**Quality Tier:** 🟡 Unverified (no skills.sh Trust Hub / Socket / Snyk verdicts published - verified Sep 29, 2026)

AAHL's Agent Skills is a collection of practical agent skills covering Home Assistant smart-home control, Microsoft Edge TTS and Zhipu GLM-TTS text-to-speech, DuckDuckGo search, DeepWiki doc retrieval, crypto market data, weather, Lark/Feishu, video search, and product price comparison. The six indexed skills span smart-home control (mcp-hass), speech (edge-tts), search and documentation (mcp-duckgo, mcp-deepwiki), and market/buying data (crypto-report, maishou). Combined installs total ~41,082 across indexed listings (Sep 29, 2026 snapshot).

---

## Installation

```bash
npx skills add aahl/skills
```

## Roster - Top Skills

| Skill | Installs | What It Does |
|---|---|---|
| edge-tts | 7668 | Edge TTS text-to-speech |
| maishou | 3669 | Buyer assistant / product price comparison |
| crypto-report | 3178 | Cryptocurrency market reports |
| mcp-duckgo | 2961 | DuckDuckGo search via MCP |
| mcp-hass | 2909 | Home Assistant smart-home control |
| mcp-deepwiki | - | DeepWiki documentation retrieval |

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| Smart-home agent | Give your agent Home Assistant control via mcp-hass for lights, climate, and device status. |
| Spoken briefings | Use edge-tts to read crypto-report or weather output aloud. |
| Keyless research | Route web lookups through mcp-duckgo and doc retrieval through mcp-deepwiki. |

## Limitations / Verification

- Verified: skills.sh marketplace indexing captured Sep 29, 2026 (skill names, install counts, repo stars); 6/6 sampled SKILL.md files verified by the sweep.
- Not verified: no live `npx skills add` install test has been run for this family.

## Security

| Audit | Verdict |
|---|---|
| Gen Agent Trust Hub | Not published |
| Socket | Not published |
| Snyk | Not published |

## Related

- [Skills Marketplace](/hermes/skills/marketplace)

---

*← [Skills Catalog](/hermes/skills/catalog) | [Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
