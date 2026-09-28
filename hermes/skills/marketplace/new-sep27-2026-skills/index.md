---
title: "Sep 27, 2026 - 11 New Skill Publisher Clusters"
description: "Skills.sh sweep: 11 new publisher clusters (11 setup guides) + 7 roster reconciles. Book-to-Skill, Samber DevRel, Layer, AE-CLI, AiCoin, A Smart Bear."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-sep27-2026-skills/"
robots: "index,follow"
last_updated: "2026-09-27"
tags: ["hermes skill", "skill marketplace", "skills.sh"]
---

# Sep 27, 2026 - 11 New Skill Publisher Clusters

**Discovered:** 11 new publisher clusters (161+ skills) · **Guides created:** 11 · **Roster reconciles:** 7

This sweep ran manually after the skills-monitor cron was paused by the Sep 21 inference-drift guard (unpinned model config). It catches the catalog up through Sep 27.

## New Publishers at a Glance

| # | Publisher | Top Skill | Installs | Category | Setup Guide |
|---|-----------|-----------|----------|----------|-------------|
| 1 | virgiliojr94/book-to-skill | book-to-skill | 6,160 | Knowledge Engineering | ✅ |
| 2 | samber/developer-relations-skills | oss-launch | 1,020 | DevRel / OSS Growth | ✅ |
| 3 | layerai/skills | layer | 927 | Generative Media | ✅ |
| 4 | thinkingaiagenticengine/ae-cli | ae-analysis | 675 | Agent Platform | ✅ |
| 5 | aicoincom/coinos-skills | aicoin-market | 672 | Crypto / Trading | ✅ |
| 6 | asmartbear/asb-skills | asb-positioning | 555 | Product Strategy | ✅ |
| 7 | integromat/make-skills | make-scenario-building | 373 | Automation / iPaaS | ✅ |
| 8 | picsart/gen-ai-skills | gen-ai-use | 344 | Generative Media | ✅ |
| 9 | indranilbanerjee/digital-marketing-pro | video-script | 308 | Marketing / Growth | ✅ |
| 10 | kangarooking/kangarooking-skills | twitter-monitor | 198 | Agent Engineering | ✅ |
| 11 | shawnchee/frontend-god-mode | frontend-god-mode | 166 | Frontend Design | ✅ |

## Setup Guides Created

1. **[Book-to-Skill Setup](/docs/hermes/skills/catalog/book-to-skill-setup)** - Turn technical book PDFs into agent skills (32.8K⭐, 6.1K installs)
2. **[Samber DevRel Skills Setup](/docs/hermes/skills/catalog/samber-devrel-skills-setup)** - 50-skill open source strategy and developer GTM suite
3. **[Layer Skills Setup](/docs/hermes/skills/catalog/layerai-skills-setup)** - 14-skill AI game asset creation suite (image, 3D, pixel art, audio, video)
4. **[AE-CLI Skills Setup](/docs/hermes/skills/catalog/ae-cli-skills-setup)** - 34-skill AgenticEngine platform suite (analysis, engagement, community)
5. **[Coinos Skills Setup](/docs/hermes/skills/catalog/coinos-trading-skills-setup)** - 7-skill AiCoin crypto toolkit (market data, freqtrade, hyperliquid)
6. **[A Smart Bear Skills Setup](/docs/hermes/skills/catalog/asmartbear-skills-setup)** - 21-skill positioning and PMF suite from Jason Cohen's frameworks
7. **[Make Skills Setup](/docs/hermes/skills/catalog/make-skills-setup)** - 5 official Make.com automation skills (scenarios, MCP, E2B)
8. **[Picsart Gen-AI Skills Setup](/docs/hermes/skills/catalog/picsart-gen-ai-skills-setup)** - 19-skill generative media suite for marketing creative
9. **[Digital Marketing Pro Setup](/docs/hermes/skills/catalog/digital-marketing-pro-setup)** - 50-skill open-source AI marketing operating system
10. **[Kangarooking Skills Setup](/docs/hermes/skills/catalog/kangarooking-skills-setup)** - 19-skill harness and content suite
11. **[Frontend God Mode Setup](/docs/hermes/skills/catalog/frontend-god-mode-setup)** - One-skill design bundle for UI polish

## Roster Reconciles (7)

Missing skill names added to existing publisher guides:

| Skill | Publisher | Installs | Reconciled In |
|-------|-----------|----------|---------------|
| dbs-bridge / dbs-install-skill | dontbesilent2025/dbskill | 9,062 / 4,520 | [July 27 Night sweep](/docs/hermes/skills/marketplace/new-july27-2026-night) |
| unified-memory | affaan-m/ecc | 2,373 | [ECC Engineering Skills](/docs/hermes/skills/catalog/ecc-engineering-skills-setup) |
| operational-enterprise-ai | mengto/skills | 986 | [Meng To Skills](/docs/hermes/skills/catalog/mengto-skills-setup) |
| add-mouse-driven-orbit | mengto/skills | 800 | [Meng To Skills](/docs/hermes/skills/catalog/mengto-skills-setup) |
| nemoclaw-user-get-started | nvidia/skills | 862 | [NemoClaw User Guide](/docs/hermes/skills/catalog/nemoclaw-user-guide-setup) |
| nemo-relay-install | nvidia/skills | 209 | [NemoClaw User Guide](/docs/hermes/skills/catalog/nemoclaw-user-guide-setup) |
| ckm-banner-design (hyphenated alias) | nextlevelbuilder/ui-ux-pro-max-skill | 367 | [UI/UX Pro Max](/docs/hermes/skills/catalog/ui-ux-pro-max-setup) |
| gstack-openclaw-office-hours | garrytan/gstack | 291 | [design-review](/docs/hermes/skills/catalog/design-review-setup) |
| apify-integration-development | apify/agent-skills | 183 | [Apify Agent Skills](/docs/hermes/skills/catalog/apify-agent-skills-setup) |

## Quick Install

```bash
npx skills add virgiliojr94/book-to-skill
npx skills add samber/developer-relations-skills
npx skills add layerai/skills
npx skills add thinkingaiagenticengine/ae-cli
npx skills add aicoincom/coinos-skills
npx skills add asmartbear/asb-skills
npx skills add integromat/make-skills
npx skills add picsart/gen-ai-skills
npx skills add indranilbanerjee/digital-marketing-pro
npx skills add kangarooking/kangarooking-skills
npx skills add shawnchee/frontend-god-mode
```

## Why This Matters for Hermes

**Book-to-Skill** (6.1K installs, 32.8K⭐) is the standout: it converts books into queryable agent skills, a direct fit for CorpusIQ's knowledge-intake and research pipelines. **A Smart Bear** encodes Jason Cohen's positioning and PMF frameworks as runnable skills - directly applicable to CorpusIQ's own product and GTM work. **Samber's DevRel suite** covers open source growth motions that match the Hermes repo promotion charter. The remaining clusters round out automation (Make), creative (Layer, Picsart), marketing (Digital Marketing Pro), and platform (AE-CLI) coverage.

*← [Skills Marketplace](/docs/hermes/skills/marketplace) | [Skills Catalog](/docs/hermes/skills/catalog) →*
*Powered by CorpusIQ*
