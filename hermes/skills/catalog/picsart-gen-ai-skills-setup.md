---
title: "Picsart Gen-AI Skills - Generative Media Suite Setup"
description: "Setup guide for picsart/gen-ai-skills - 19 agent skills for Picsart's gen-ai CLI: text-to-visual, product photos, headshots, app assets, ads."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/picsart-gen-ai-skills-setup/"
robots: "index,follow"
last_updated: "2026-09-27"
tags: ["hermes skill", "agent skill", "skill setup", "picsart", "image generation", "creative"]
---

# Picsart Gen-AI Skills - Setup Guide

**Source:** [picsart/gen-ai-skills](https://github.com/picsart/gen-ai-skills) (pushed Aug 28, 2026)
**Skill:** `picsart/gen-ai-skills` (19 installable skills)
**Installs:** ~300 per top skill, ~5.6K combined (Sep 27, 2026 snapshot)
**Category:** Generative Media / Marketing Creative
**Quality Tier:** 🔵 Community (no skills.sh security verdicts published - verified Sep 27, 2026)

Picsart's official agent skills wrap its gen-ai CLI for generative workflows. The 19 skills span creative production end to end: text-to-visual generation, product photo studios, headshot studios, developer app assets and avatars, screenshot beautification, ad-variant factories, campaign localization, multi-brand packs, persona creation, and explainer generation. The marketer-facing skills (ad variants, localization, multi-brand) make it a practical production suite for agent-driven creative ops.

---

## Installation

```bash
# Full suite
npx skills add picsart/gen-ai-skills

# Marketing subset
npx skills add picsart/gen-ai-skills --skill marketer-ad-variant-factory
```

## Roster - Top Skills

| Skill | Installs | Does |
|---|---|---|
| gen-ai-use | 344 | Platform entry: auth and usage patterns |
| text-to-visual | 309 | General text-to-image generation |
| product-photo-studio | 304 | Product photography on generated scenes |
| prosumer-headshot-studio | 303 | Pro headshot generation |
| dev-app-assets | 300 | App icons, screenshots, and store assets |
| gen-ai-explainer | 299 | Explainer visual generation |
| gen-ai-persona-creation | 296 | Brand persona and style guides |
| marketer-ad-variant-factory | 291 | Ad creative variants at scale |
| dev-avatar-service | 291 | Avatar generation service |
| dev-screenshot-beautifier | 290 | Polish screenshots for docs/marketing |
| agency-multi-brand-pack | 290 | Multi-brand asset packs for agencies |
| marketer-localize-campaign | 288 | Localize campaign creative |

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **UGC and social creative** | `text-to-visual` and `marketer-ad-variant-factory` feed the daily content pipeline |
| **Docs screenshots** | `dev-screenshot-beautifier` polishes screenshots for corpusiq-docs |
| **Multi-brand client work** | `agency-multi-brand-pack` supports brand-asset work |
| **Localization** | `marketer-localize-campaign` supports worldwide promotion angles |

## Limitations / Verification

- Requires a Picsart API key; generation is metered
- CLI-backed, so Node.js 18+ required for `npx skills`
- Verify: `npx skills add picsart/gen-ai-skills --list` shows 19 skills

## Security

No skills.sh security audits published (verified Sep 27, 2026):

| Audit | Verdict |
|---|---|
| Gen Agent Trust Hub | Not published |
| Socket | Not published |
| Snyk | Not published |

## Related

- [Generative Media Skills Setup](/hermes/skills/catalog/generative-media-skills-setup)
- [Layer Skills Setup](/hermes/skills/catalog/layerai-skills-setup)
- [Skills Marketplace](/hermes/skills/marketplace)

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
