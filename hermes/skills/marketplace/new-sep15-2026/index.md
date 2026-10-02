---
title: September 15, 2026 Skills.sh Sweep - AccessLint WCAG Suite +
description: "Skills.sh sweep September 15, 2026: AccessLint/skills (WCAG 2.2 audit suite, 5.1K combined) + podo/design-agent-skills (150-skill design catalog, 17.3K combined) - 2 setup guides, 2 roster reconciles (devtools-skills, wind-alice), 2 rejections."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-sep15-2026/"
robots: "index,follow"
last_updated: "2026-09-15"
tags: ["hermes skill", "agent skill", "skills.sh", "marketplace", "sweep"]
---

# September 15, 2026 - Skills.sh Sweep: AccessLint WCAG Suite + Podo Design Catalog

**Sweep:** skills-monitor · September 15, 2026 (morning fire) · 4,003 unique skills collected, 44 queries, 0 failed queries · cluster diff: 120 known / 0 candidates · tiered crossref: 643 unique / 45 NEW / 106 PARTIAL · hot board: clean, all sources catalog-covered, exit 0

Two genuinely new publishers surfaced by the tiered crossref (the cluster diff stayed clean - both sit below the ~7.4K collector-cluster floor): AccessLint, the established web-accessibility vendor, and podo, a redistribution catalog of curated design skills. Plus two roster reconciles on already-guided families (reason-machines/devtools-skills and wind-alice/alicemarket).

## New Guides

| Publisher | Skills | Combined Installs | Guide |
|---|---|---|---|
| [AccessLint/skills](https://www.skills.sh/accesslint/skills) | 5 (8 legacy aliases also indexed) | ~5.1K | [AccessLint Skills Setup](/hermes/skills/catalog/accesslint-skills-setup) |
| [podo/design-agent-skills](https://www.skills.sh/podo/design-agent-skills) | 150 indexed (157 in repo) | 17,302 | [Podo Design Agent Skills Setup](/hermes/skills/catalog/podo-design-agent-skills-setup) |

**AccessLint notes:** the most audit-rigorous a11y skill set on skills.sh - WCAG 2.2 end-to-end (scan → inspect → audit → fix → diff) with severity + evidence-basis grading. Agent-agnostic install (live-verified "Found 5 skills"), optional `@accesslint/mcp`. No skills.sh audits published → 🟡 Unverified, disclosed in the guide.

**Podo notes:** redistribution catalog - 149 of 150 indexed skills at 100+ installs; upstreams disclosed honestly in the guide (emilkowalski, anthropics, figma, vercel, sleek, open-design, mastepanoski, addyosmani). Profile picker (24/92/151). Agent-agnostic symlink install across 30+ agents (live-verified "Found 157 skills"). No audits published → 🟡 Unverified.

## Roster Reconciles

| Family | Change |
|---|---|
| reason-machines/devtools-skills | +2 roster rows (subnautica-ii-coop-mod 204, devtools-debugger-mcp-nodejs 195) - the Sep 14 print cap had hidden them; roster now 42 skills / 9,850 combined |
| wind-alice/alicemarket | Roster refreshed to the Sep 15 snapshot: 71 skills indexed, 63 at 100+ (174K combined); the "(63 more) <100 each" claim was stale - most of that band now sits at 100-670 |

## Evaluated and Skipped

| Source | Skill | Installs | Reason |
|---|---|---|---|
| thelobbi/claude | complex-reasoning (also vision-multimodal 541, design-system 135, ~30 more) | 156 | Claude Code plugin marketplace: `/plugin marketplace add`, `.claude-plugin/marketplace.json`, Claude-Code `allowed-tools` frontmatter, `dependencies: extended-thinking` - Claude-family rejection class |
| andurilcode/craftwork | reasoning-orchestrator | 24 | 63-skill reasoning/context suite (7★, MIT); install mechanism IS agent-agnostic (`npx skills add AndurilCode/craftwork`) but 24 installs is below the 40-install floor and last push was Apr 19, 2026 - park as watch |

## Standing Rejections

All other NEW flags re-confirmed as standing rejections at unchanged counts (runwayml 35, aussiegingersnap 29, mercury-api 29, nickcrew 24, preetamnath 23/5, xmzdesign 20, asomelab 18, bankrbot 17, wavestone-sa 16, bfernandois059 16, sd0xdev 15, xuyuan-hub 14, mistakenot 13, cdeistopened 12/7, omer-metin 11, frankxai 11, rolaca11 11, khaki4 11, junhyunny 10 dead, microck 9, nweii 8, pudap 8, aktsmm 8, nvie 8, kriscard 7, ooiyeefei 7, nearai 6, codephobiia 5, fuadnafiz98 5, sanitypress 5, korchard333 5, michaelmerrill 5, chameleon-writer 5, microsoft/cat 3, trollz1004 2, kmshihab7878 2, bog5d 1, tywade1980 1, lproux 1 dead, dance-of-tal 1). All 4 PARTIAL ≥100 flags reconciled in-tree this fire: reason-machines/devtools-skills ×2 (roster rows), wind-alice volume_spike_reasoning_skill (wind roster refresh), podo mastepanoski-skills (podo guide).
