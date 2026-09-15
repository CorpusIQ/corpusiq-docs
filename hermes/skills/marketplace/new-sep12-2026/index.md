---
title: September 12, 2026 Skills.sh Sweep - Aradotso Publisher
description: "Skills.sh sweep September 12, 2026: aradotso org renamed to reason-machines (7 repos, GitHub 301/200 verified) - 25 catalog setup guides updated in place with new Source links, install commands, and skills.sh references."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-sep12-2026/"
robots: "index,follow"
last_updated: "2026-09-12"
tags: ["hermes skill", "agent skill", "skills.sh", "marketplace", "sweep", "publisher rename"]
sweep_id: "2026-09-12-morning"
new_publishers: 0
new_skills: 0
guides_drafted: 0
---

# September 12, 2026 - Skills.sh Sweep: Aradotso Publisher Rename

**Sweep:** skills-monitor · September 12, 2026 (morning fire) · 44 queries, 4,004 unique skills, 0 failed queries · cluster diff: 120 known / 0 candidates · tiered cross-reference: 653 unique / 62 NEW / 101 PARTIAL, PARTIAL ≥100 empty · hot board: clean, all catalog-covered, exit 0

No new publisher clusters cleared the drafting bar. The sweep surfaced a **publisher-org rename** instead: the entire `aradotso` GitHub org has moved to `reason-machines`, taking 7 skill repos with it.

## Publisher Rename Recorded

**`aradotso/*` → `reason-machines/*`** - GitHub 301/200 pairs verified for all 7 repos; skills.sh pages for the old org return 404 while the new org returns 200; the skills.sh API now rewrites all `source` fields to the new owner.

| Old Repo | New Repo | GitHub | skills.sh |
|---|---|---|---|
| aradotso/hermes-skills | reason-machines/hermes-skills | 301 → 200 | 404 → 200 |
| aradotso/ai-agent-skills | reason-machines/ai-agent-skills | 301 → 200 | 404 → 200 |
| aradotso/devtools-skills | reason-machines/devtools-skills | 301 → 200 | 404 → 200 |
| aradotso/marketing-skills | reason-machines/marketing-skills | 301 → 200 | 404 → 200 |
| aradotso/trending-skills | reason-machines/trending-skills | 301 → 200 | 404 → 200 |
| aradotso/security-skills | reason-machines/security-skills | 301 → 200 | 404 → 200 |
| aradotso/mcp-skills | reason-machines/mcp-skills | 301 → 200 | 404 → 200 |

Per the publisher-rename rule (Wind precedent, Sep 11), existing guides are updated in place instead of drafted anew. **25 catalog setup guides updated** (86 owner references): Source lines, GitHub links, install commands, and skills.sh references now point at `reason-machines/*`, and `last_updated` is bumped to 2026-09-12. The rename was discovered when install commands like `npx skills add aradotso/hermes-skills` started resolving against a dead skills.sh listing.

**Updated install command example:**

```bash
npx skills add reason-machines/hermes-skills --skill hermes-webui-agent
```

Historical marketplace batch pages (June-Nov 2026) are intentionally left as-is per the rename precedent - they are dated discovery records.

## Evaluated and Skipped

| Cluster / Skill | Installs | Reason |
|---|---|---|
| reason-machines/hermes-skills openclaw-named set (polymarket-openclaw-trading-bot 67, polymarket-openclaw-ai-arbitrage-bot 66, polymarket-openclaw-ai-trading-bot 66, metamask-openclaw-wallet-integration 61, loader-openclaw-skills 60, deepseek-openclaw-config-generator 69, deepseek-openclaw-integration 59, openclaw-windows-companion 55, openclaw-windows-node 50, metamask-openclaw-desktop-security-analysis 50, moontv-openclaw-skill 49, openclaw-research-paper-push-skill 48, openclaw-dingtalk-channel 44, openclaw-polymarket-trading-bot 36, openclaw-android-setup 31, voltagent-openclaw-skill-loader 71) | 67 and below | OpenClaw-runtime skills (trading bots, WeChat/DingTalk connectors, Windows companions) - OpenClaw-named exclusion class holds; these target the OpenClaw runtime, not Hermes Agent. Repo was already documented via its Hermes-named skills (now under reason-machines after the rename). |
| All other 62 NEW tiered flags | <100 | Standing-rejection roster at unchanged counts (roster carried in the corpusiq-docs-management skill sweep run log). No bar-clearers, no overturns. |

## Rename Verification Method

GitHub 301/200 pairs checked via `curl -sI` on all 7 old repos (all 301 with Location → reason-machines), new repos all 200. skills.sh publisher pages checked via `curl -sL` (old 404, new 200). API `source` field confirmed rewritten by skills.sh (`q=aradotso/hermes-skills` now returns `source=reason-machines/hermes-skills`).

---

*← [Marketplace](/docs/hermes/skills/marketplace) | [Skills Catalog](/docs/hermes/skills/catalog) →*
*Powered by CorpusIQ*
