---
title: "New Skills — August 15, 2026 (Midday Sweep)"
description: "skills.sh midday sweep: Argent Mobile Agent Skills (154.0K), Oh Story ClaudeCode (146.6K), VueJS AI Skills (129.2K), Rivet Skills (65.3K), plus 11 more clusters — 15 publisher clusters, 273 skills, 15 setup guides."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-aug15-2026-midday/"
robots: "index,follow"
last_updated: "2026-08-15"
sweep_id: "2026-08-15-midday"
new_publishers: 15
new_skills: 273
guides_drafted: 15
tags: ["hermes skill", "skill marketplace", "skills.sh", "new skills"]
---

# New Skills — August 15, 2026 (Midday Sweep)

Third skills.sh sweep of August 15. 40 API queries collected 3,944 unique skills; cross-referenced against the hermes/ tree, the hot leaderboard, and the morning queue. The dominant pattern this sweep was **queue underestimation**: candidates parked this morning at API-sum estimates turned out to be 6-15x larger on their publisher pages (argent 11.9K → 154.0K, oh-story 11.4K → 146.6K, vuejs-ai 10.7K → 129.2K, rivet 10.1K → 65.3K). Per the stale-assessment rule, every queued candidate was re-verified on its publisher page before drafting.

## New Publisher Clusters — Guided This Sweep

| Cluster | Skills | Installs | Tier | Guide |
|---|---|---|---|---|
| software-mansion/argent | 20 | 154.0K | 🟢 | [argent-mobile-agent-skills-setup](/hermes/skills/catalog/argent-mobile-agent-skills-setup/) |
| worldwonderer/oh-story-claudecode | 13 | 146.6K | 🟡 | [oh-story-claudecode-skills-setup](/hermes/skills/catalog/oh-story-claudecode-skills-setup/) |
| vuejs-ai/skills | 11 | 129.2K | 🟢 | [vuejs-ai-skills-setup](/hermes/skills/catalog/vuejs-ai-skills-setup/) |
| rivet-dev/skills | 22 | 65.3K | 🟢 | [rivet-dev-skills-setup](/hermes/skills/catalog/rivet-dev-skills-setup/) |
| dammyjay93/interface-design | 2 | 23.6K | 🟢 | [interface-design-skill-setup](/hermes/skills/catalog/interface-design-skill-setup/) |
| feature-sliced/skills | 1 | 16.6K | 🟢 | [feature-sliced-design-skill-setup](/hermes/skills/catalog/feature-sliced-design-skill-setup/) |
| rampstackco/claude-skills | 103 | 15.7K | 🟡 | [rampstack-claude-skills-setup](/hermes/skills/catalog/rampstack-claude-skills-setup/) |
| lombiq/tailwind-agent-skills | 1 | 10.1K | 🟡 | [tailwind-4-docs-skill-setup](/hermes/skills/catalog/tailwind-4-docs-skill-setup/) |
| bradautomates/claude-video | 1 | 10.1K | 🟡 | [claude-video-watch-skill-setup](/hermes/skills/catalog/claude-video-watch-skill-setup/) |
| tiangong-ai/skills | 58 | 9.0K | 🟡 | [tiangong-ai-skills-setup](/hermes/skills/catalog/tiangong-ai-skills-setup/) |
| rknall/claude-skills | 10 | 8.5K | 🟡 | [rknall-claude-skills-setup](/hermes/skills/catalog/rknall-claude-skills-setup/) |
| superdesigndev/superdesign-skill | 1 | 8.0K | 🟡 | [superdesign-skill-setup](/hermes/skills/catalog/superdesign-skill-setup/) |
| kylezantos/design-motion-principles | 1 | 7.8K | 🟢 | [design-motion-principles-skill-setup](/hermes/skills/catalog/design-motion-principles-skill-setup/) |
| twostraws/swift-testing-agent-skill | 1 | 7.5K | 🟢 | [swift-testing-pro-skill-setup](/hermes/skills/catalog/swift-testing-pro-skill-setup/) |
| trailofbits/skills-curated | 31 | 2.4K | 🟡 | [trailofbits-skills-curated-setup](/hermes/skills/catalog/trailofbits-skills-curated-setup/) |

## Method Notes

- 40 API queries → 3,944 unique skills → top-120 clusters all present in the tree → hit triage separated real guides from queue mentions → 17 not-guided candidates identified (13 from the morning queue + 4 hot-leaderboard finds).
- Publisher pages fetched for all 15 drafted clusters; individual skill pages fetched for all single-skill clusters to get security-audit tiers (7 all-Pass → 🟢; Snyk Warn/Fail or Socket Warn named in Limitations → 🟡).
- Hot leaderboard surfaced trailofbits/skills-curated at #1 and rampstackco/claude-skills — both new to the tree.
- Single-skill audit tiers: interface-design 🟢 (3/3 Pass), feature-sliced-design 🟢 (3/3), design-motion-principles 🟢 (3/3), swift-testing-pro 🟢 (3/3), tailwind-4-docs 🟡 (Snyk Warn), watch 🟡 (Snyk Fail), superdesign 🟡 (Socket Warn + Snyk Fail).

## Evaluated and Queued (next sweep)

| Cluster | Installs | Reason parked |
|---|---|---|
| ceorkm/mobile-app-ui-design | 6.7K | Single-skill, batch size cap this sweep |
| ningzimu/codex-ppt-skill | 3.5K | Below the 5K drafting bar this sweep |
| compshare-cn/compshare-cli | 121 | Below minimum bar — skipped, not queued |

Carry-over queue remains parked per playbook: amazonappdev/devices-agent-skills, lottiefiles/motion-design-skill, sonilo-ai/skills, emblemcompany/agent-skills, dmmulroy/anti-slop, mintlify/docs, ljagiello/ctf-skills, digitalsamba/claude-code-video-toolkit, getsentry/skills, herdr, last30days, agent-config, stop-slop, web-access, brightdata, langfuse, zhaono1/agent-playbook, 199-biotechnologies/claude-deep-research-skill, cloudai-x/threejs-skills.

## Notable Signals for CorpusIQ

- **Argent** (Software Mansion, creators of react-native-reanimated) gives us a vendor-grade mobile dev-agent toolkit — the largest queue underestimate of the day.
- **Oh Story's story-deslop** plus **trailofbits' humanizer** strengthen the de-AI-fication stack for public content.
- **RampStack's 103-skill suite** (seo-aeo-geo, email-deliverability, programmatic-seo, cro-optimization) is the biggest growth-marketing skill library catalogued to date — direct input for the docs SEO/AEO/GEO pass.
- **Tiangong's email SMTP/IMAP skills** are a self-hosted fallback path for our email operations.
- **Rivet's sandbox-agent and ai-agent-workspace** are reference patterns for agent sandboxing design.

## Index State After Sweep

- catalog/index.md: +15 entries
- marketplace/index.md: header 850 → 865, footer 901 → 916
- last_updated on both indexes: 2026-08-15
