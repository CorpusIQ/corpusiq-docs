---
title: "New Skills — July 21, 2026 Marketplace Sweep"
description: "10 new Hermes-relevant skills discovered on skills.sh, with setup guides drafted. 458K+ combined installs across the new skills."
---

# New Skills — July 21, 2026

Skills discovered during the July 21 marketplace sweep. 10 setup guides created for Hermes agents.

## Summary

| Metric | Count |
|---|---|
| New skills found | 10 |
| Setup guides created | 10 |
| Combined installs | ~458,000+ |
| Quality: 🟢 Production | 7 |
| Quality: 🟡 Beta | 2 |
| Quality: 🔵 Community | 1 |

## New Skills

### Agent Infrastructure

| Skill | Publisher | Installs | Tier | Guide |
|---|---|---|---|---|
| **claude-handoff** | mattpocock/skills | 63,500 | 🟢 | [Setup Guide](/hermes/skills/catalog/claude-handoff-setup/) |
| **openclaw-backup** | theagentservice/skills | 3,100 | 🔵 | [Setup Guide](/hermes/skills/catalog/openclaw-backup-setup/) |
| **deep-agents-memory** | langchain-ai/langchain-skills | 12,800 | 🟡 | [Setup Guide](/hermes/skills/catalog/deep-agents-memory-setup/) |

### Security & Governance

| Skill | Publisher | Installs | Tier | Guide |
|---|---|---|---|---|
| **skill-vetter** | useai-pro/openclaw-skills-security | 20,500 | 🟡 | [Setup Guide](/hermes/skills/catalog/skill-vetter-setup/) |

### Web Extraction & Search

| Skill | Publisher | Installs | Tier | Guide |
|---|---|---|---|---|
| **firecrawl-agent** | firecrawl/cli | 73,900 | 🟢 | [Setup Guide](/hermes/skills/catalog/firecrawl-agent-setup/) |
| **tavily-search** | tavily-ai/skills | 25,700 | 🟢 | [Setup Guide](/hermes/skills/catalog/tavily-search-setup/) |
| **tavily-research** | tavily-ai/skills | 14,100 | 🟢 | [Setup Guide](/hermes/skills/catalog/tavily-research-setup/) |
| **apify-ultimate-scraper** | apify/agent-skills | 13,600 | 🟢 | [Setup Guide](/hermes/skills/catalog/apify-ultimate-scraper-setup/) |

### Growth & Content

| Skill | Publisher | Installs | Tier | Guide |
|---|---|---|---|---|
| **content-strategy** | coreyhaines31/marketingskills | 110,200 | 🟢 | [Setup Guide](/hermes/skills/catalog/content-strategy-setup/) |
| **social** | coreyhaines31/marketingskills | 38,500 | 🟢 | [Setup Guide](/hermes/skills/catalog/social-setup/) |

## Notes

- **tavily-search** is the official Tavily CLI skill (25.7K installs), distinct from the existing `tavily-search-openclaw-setup` which covers the community OpenClaw wrapper (797 installs).
- **skill-vetter** from useai-pro (20.5K installs) is distinct from the existing `skill-vetting-setup` which covers the NVIDIA SkillSpector-based system from SoCalStreet.
- **firecrawl-agent** (73.9K installs) extends the existing Firecrawl catalog with AI-powered structured extraction, complementing `firecrawl-workflows-setup`.
- 154 total marketplace skills were cross-referenced against the 173-entry existing catalog during this sweep.
- Web extraction (Firecrawl) and search (Tavily) tools were unavailable during this sweep; guides were drafted from `npx skills use` SKILL.md content.
