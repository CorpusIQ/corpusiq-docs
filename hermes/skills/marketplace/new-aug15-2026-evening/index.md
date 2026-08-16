---
title: "New Skills — August 15, 2026 (Evening Sweep)"
description: "skills.sh evening sweep: Sentry Agent Skills (85.3K, 31), Three.js Agent Skills (80.0K, 10), Emblem Company Agent Skills (78.6K, 9), CTF Security Skills (71.6K, 12), Bright Data Agent Skills (26.9K, 22), plus 6 more clusters — 11 publisher clusters, 111 skills, 11 setup guides."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-aug15-2026-evening/"
robots: "index,follow"
last_updated: "2026-08-15"
tags: ["hermes skill", "skill marketplace", "skills.sh", "new skills"]
sweep_id: "2026-08-15-evening"
new_publishers: 11
new_skills: 111
guides_drafted: 11
---

# New Skills — August 15, 2026 (Evening Sweep)

Fourth skills.sh sweep of August 15. 40 API queries collected 3,944 unique skills; cross-referenced against the hermes/ tree with the newest batch-page dirs excluded, then re-verified the entire carry-over queue on publisher pages. The dominant pattern again was **queue underestimation**: getsentry 20.7K → 85.3K, emblemcompany 8.8K → 78.6K, cloudai-x 7.9K → 80.0K, ljagiello → 71.6K (never counted before). Every queued candidate was re-verified per the stale-assessment rule before drafting or re-parking.

## New Publisher Clusters — Guided This Sweep

| Cluster | Skills | Installs | Tier | Guide |
|---|---|---|---|---|
| getsentry/skills | 31 | 85.3K | 🟢 | [Sentry Agent Skills Setup](/hermes/skills/catalog/sentry-agent-skills-setup/) |
| cloudai-x/threejs-skills | 10 | 80.0K | 🟡 | [Three.js Agent Skills Setup](/hermes/skills/catalog/threejs-agent-skills-setup/) |
| emblemcompany/agent-skills | 9 | 78.6K | 🟡 | [Emblem Company Agent Skills Setup](/hermes/skills/catalog/emblem-company-agent-skills-setup/) |
| ljagiello/ctf-skills | 12 | 71.6K | 🟡 | [CTF Security Skills Setup](/hermes/skills/catalog/ctf-security-skills-setup/) |
| brightdata/skills | 22 | 26.9K | 🟢 | [Bright Data Agent Skills Setup](/hermes/skills/catalog/brightdata-agent-skills-setup/) |
| digitalsamba/claude-code-video-toolkit | 13 | 14.5K | 🟡 | [Claude Code Video Toolkit Setup](/hermes/skills/catalog/claude-code-video-toolkit-setup/) |
| langfuse/skills | 6 | 13.1K | 🟢 | [Langfuse Agent Skills Setup](/hermes/skills/catalog/langfuse-agent-skills-setup/) |
| 199-biotechnologies/claude-deep-research-skill | 1 | 9.4K | 🟡 | [Deep Research Skill Setup](/hermes/skills/catalog/claude-deep-research-skill-setup/) |
| mintlify/docs | 5 | 9.2K | 🟢 | [Mintlify Docs Skills Setup](/hermes/skills/catalog/mintlify-docs-skills-setup/) |
| lottiefiles/motion-design-skill | 1 | 8.1K | 🟢 | [Motion Design Skill Setup](/hermes/skills/catalog/lottiefiles-motion-design-skill-setup/) |
| ceorkm/mobile-app-ui-design | 1 | 6.7K | 🟢 | [Mobile App UI Design Skill Setup](/hermes/skills/catalog/mobile-app-ui-design-skill-setup/) |

## Method Notes

- 40 API queries → 3,944 unique skills → top-120 clusters all present in the tree → same-day triage recovery excluded `new-aug15-2026*` dirs → 5 not-guided candidates → carry-over queue re-verified on publisher pages (17 fetches) → 11 clusters drafted, 7 parked, 4 dropped.
- Single-skill audit tiers: motion-design 🟢 (3/3 Pass), mobile-app-ui-design 🟢 (3/3 Pass), deep-research 🟡 (Snyk Warn). Multi-skill suites tiered by publisher: official vendor orgs (Sentry, Bright Data, Langfuse, Mintlify, LottieFiles) 🟢; community or crypto-adjacent publishers 🟡.
- resend/react-email and resend/email-best-practices surfaced in the re-diff but were skipped — `resend-skills-setup.md` already covers the family.
- Hot leaderboard (1H delta) added watch candidates: alibaba/open-code-review (4.3K), asksurf-ai/surf-skills (3.8K), streakyc/googleworkspacecli (1.7K), uni-stack/uniwind (5.3K).

## Evaluated and Queued (next sweep)

| Cluster | Installs | Reason parked |
|---|---|---|
| uni-stack/uniwind | 5.3K | RN tooling, at bar; watch next sweep |
| amazonappdev/devices-agent-skills | 5.1K | Fire TV migration niche |
| alibaba/open-code-review | 4.3K | Below bar; brand authority watch |
| asksurf-ai/surf-skills | 3.8K | Below bar |
| ningzimu/codex-ppt-skill | 3.5K | Below bar |
| dmmulroy/anti-slop | 1.1K | Below bar |
| zhaono1/agent-playbook | 50.3K | Top skill (self-improving-agent, 33.0K) already guided via charon-fan; remaining 23 skills ≤1.2K each |

Dropped below minimum: sonilo-ai/skills (234), algolia/skills (235), tencentmusic/qqmusic-skills (714), jimliu/baocut (181).

Carry-over queue remains parked per playbook: herdr, last30days, agent-config, stop-slop, web-access.

## Notable Signals for CorpusIQ

- **Sentry's suite** is the strongest security + code-review skill cluster catalogued to date — a natural pairing for our GitHub work and the PR security gate.
- **Bright Data's competitive-intel, brand-listening, and seo-audit** skills map one-to-one onto our research and SEO operations; scrape/search are a resilient fallback path for degraded search backends.
- **Langfuse tracing** addresses the exact gap our multi-model operation has: attribute cost per model and debug agent loops.
- **The video toolkit** (ffmpeg, remotion, elevenlabs) overlaps the same primitives our UGC pipeline runs on — a reference for pipeline hardening.
- **CTF skills** give a structured offensive-security checklist for authorized testing, plus OSINT methodology we can reuse for research.

## Index State After Sweep

- catalog/index.md: +11 entries
- marketplace/index.md: header 865 → 876, footer 916 → 927
- last_updated on both indexes: 2026-08-15
