---
title: Sep 28, 2026 - 4 New Skill Publisher Clusters (Jezweb 96
description: "Skills.sh sweep: 4 new publisher guides (Jezweb 96 skills, OmniRoute 44 skills, rlaope/oh-my-hermes 130 skills, react-native-update) + 3 roster reconciles."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-sep28-2026-skills/"
robots: "index,follow"
last_updated: "2026-09-28"
tags: ["hermes skill", "skill marketplace", "skills.sh"]
---

# Sep 28, 2026 - 4 New Skill Publisher Clusters

**Discovered:** 4 new publisher clusters (270+ skills) · **Guides created:** 4 · **Roster reconciles:** 3

Daily sweep of the skills.sh REST API across 12 queries (`hermes`, `hermes agent`, `hermes skill`, `hermes automation`, `nousresearch/hermes-agent`, `aradotso/hermes-skills`, `garrytan/gbrain`, `plastic-labs/honcho`, `aradotso/devtools-skills`, `sickn33/antigravity-awesome-skills`, `varnan-tech/opendirectory`, `cosmicstack-labs/mercury-agent-skills`). 331 unique skills collected, 129 candidates after cross-reference; OpenClaw-only and facebook/hermes (JS engine) hits filtered. Publisher-focused follow-up queries surfaced the full clusters.

## New Publishers at a Glance

| # | Publisher | Top Skill | Installs | Category | Setup Guide |
|---|-----------|-----------|----------|----------|-------------|
| 1 | jezweb/claude-skills | shadcn-ui | 3,541 | Web Dev / Design / SEO | ✅ |
| 2 | diegosouzapw/OmniRoute | omni-combos-routing | 738 | AI Gateway / LLM Infra | ✅ |
| 3 | reactnativecn/react-native-update-skill | react-native-update | 230 | Mobile / OTA Updates | ✅ |
| 4 | rlaope/oh-my-hermes | triage-sweep | 19 | Agent Workflow Packages | ✅ |

## Setup Guides Created

1. **[Jezweb Skills Setup](/docs/hermes/skills/catalog/jezweb-skills-setup)** - 96 skills, 115,071 combined installs (1,034⭐). Cloudflare, Tailwind v4, shadcn/ui, TanStack, WordPress, Shopify, SEO, business English.
2. **[OmniRoute Skills Setup](/docs/hermes/skills/catalog/omniroute-skills-setup)** - 44 skills from the 70,907⭐ MIT AI gateway (359 providers, 1,200+ models). Includes `omni-github-skills` - automated GitHub skill search/score/scan/import.
3. **[React Native Update Skill Setup](/docs/hermes/skills/catalog/react-native-update-skill-setup)** - Host-neutral OTA update integration skill for Pushy/Cresc (230 installs).
4. **[rlaope Oh My Hermes Setup](/docs/hermes/skills/catalog/rlaope-oh-my-hermes-setup)** - 130-skill all-in-one Hermes plugin (3,000⭐): coding intelligence, long-term memory system, workflow packages.

## Roster Reconciles (3)

Missing skill names added to existing publisher guides:

| Skill | Publisher | Installs | Reconciled In |
|-------|-----------|----------|---------------|
| developer-champions | samber/developer-relations-skills | 1,012 | [Samber DevRel Skills](/docs/hermes/skills/catalog/samber-devrel-skills-setup) |
| layer-game-assets | layerai/skills | 923 | [Layer Skills](/docs/hermes/skills/catalog/layerai-skills-setup) |
| asb-interview-debrief | asmartbear/asb-skills | 540 | [A Smart Bear Skills](/docs/hermes/skills/catalog/asmartbear-skills-setup) |

## Quick Install

```bash
npx skills add jezweb/claude-skills
npx skills add diegosouzapw/OmniRoute
npx skills add reactnativecn/react-native-update-skill --skill react-native-update
npx skills add rlaope/oh-my-hermes
```

## Why This Matters for Hermes

**Jezweb** is the sweep's biggest practical win - 115K combined installs of production web-dev skills (Tailwind v4, shadcn/ui, TanStack, Cloudflare) that plug directly into CorpusIQ's landing-page, docs-site, and client-work pipelines. **OmniRoute** (70.9K⭐) puts an open MIT AI gateway in reach with agent-operable skills, including a skill that automates the same GitHub skill-hunt the daily sweep performs. **rlaope/oh-my-hermes** (3,000⭐, pushed today) is a Hermes-native workflow package suite that overlaps CorpusIQ cron, security-gate, and memory patterns. **react-native-update** fills the mobile OTA gap for client work. Known publishers `varnan-tech/opendirectory` (59 additional skills, ≤62 installs) and `cosmicstack-labs/mercury-agent-skills` (34 additional skills, ≤18 installs) also showed expanded rosters - documented at publisher level in prior sweeps, not re-guided here.

*← [Skills Marketplace](/docs/hermes/skills/marketplace) | [Skills Catalog](/docs/hermes/skills/catalog) →*
*Powered by CorpusIQ*
