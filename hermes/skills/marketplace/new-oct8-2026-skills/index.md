---
title: "New Skills - October 8, 2026"
description: "Skills.sh sweep (Oct 8 morning): 440 skills in the standard window plus a trending-page compensation pass; 4 new publisher guides - shadcn, Amplitude, mbfinotti, Cloudflare Security Audit."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-oct8-2026-skills/"
robots: "index,follow"
last_updated: "2026-10-08"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - October 8, 2026

Sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog. The standard 15-query window served ~440 unique skills for a third consecutive run (a serving-side change first observed Oct 7), so coverage was compensated with the skills.sh trending page (600 entries across 64 sources), cross-referenced against the catalog and the sweep collection. All four new publishers below were surfaced by the compensation pass; the standard window's 25 NEW flags were all below the guide floor.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills collected (standard window) | 440 (15 queries, 0 failed) |
| NEW (not in catalog) | 25 (all below floor, max 5 installs) |
| PARTIAL (source known, skill not cataloged) | 125 |
| PARTIAL >= 100 installs | 0 |
| Trending compensation pass | 600 entries / 64 sources |
| New publisher guides | 4 |
| Roster reconciles | 4 |

## New Publisher Guides

### 1. shadcn Skill - shadcn/ui Component Workflows (official)

**Source:** [shadcn-ui/ui](https://www.skills.sh/shadcn-ui/ui/shadcn) (93.9K installs; 125,283 stars, MIT; skill at `skills/shadcn/SKILL.md`) - Gen Agent Trust Hub Pass / Socket Warn / Snyk Pass

The official shadcn component skill: project context injection, component docs, registry search, presets, and always-on UI rules for coding agents. Agent-facing (no slash command to learn); activates on any project with a `components.json`.

-> [Setup guide](/hermes/skills/catalog/shadcn-ui-setup)

### 2. Amplitude Agent Skills - Product Analytics (official)

**Source:** [amplitude/mcp-marketplace](https://github.com/amplitude/mcp-marketplace) (38 skills, ~175.2K combined; 42 stars, MIT; pushed Oct 8, 2026)

Official Amplitude plugin skills covering the product-data loop: event discovery, instrumentation planning and diffs, taxonomy governance, then chart, dashboard, experiment, and cohort analysis with daily and weekly briefs.

-> [Setup guide](/hermes/skills/catalog/amplitude-agent-skills-setup)

### 3. mbfinotti Business Skills - Sales, RevOps, Advertising & Partnerships

**Source:** [mbfinotti](https://github.com/mbfinotti) business-skills family (4 MIT repos; 108 skills, ~637.1K combined)

Interview-based operator skills: sales (ICP, pipeline coverage, negotiation), advertising (budget policy, creative tests, account diagnostics), RevOps (forecasting, pipeline hygiene, CRM governance), and partnerships (alliances, affiliate and influencer operations).

-> [Setup guide](/hermes/skills/catalog/mbfinotti-skills-setup)

### 4. Cloudflare Security Audit Skill (official)

**Source:** [cloudflare/security-audit-skill](https://www.skills.sh/cloudflare/security-audit-skill/security-audit) (25.6K installs; 26,403 stars, MIT)

Cloudflare's six-phase vulnerability audit workflow for coding agents (reconnaissance, coverage-led hunting, candidate validation, structured output, independent verification, target-neutral reporting). Originated by 89jobrien, adapted by Cloudflare.

-> [Setup guide](/hermes/skills/catalog/cloudflare-security-audit-setup)

## Roster Reconciles and Notes

- **RunComfy Agent Skills:** counts refreshed (61.1K to 11.5M+ combined installs); `gencraft-labs/skills` recorded as a redistribution mirror.
- **Sleek design-mobile-apps:** counts refreshed (75.1K to 680.6K); the Snyk verdict changed from Pass to Fail and is recorded in the setup guide.
- **inference.sh mirrors:** the mirror list now records six re-upload organizations (`101-skills`, `magentosh`, `qu-skills`, `skills-shell`, `its-a-skill-issue`, `bankai-skills`).
- **uizze:** source-segment note added (the search API also lists `ui-taste` at 452.3K and `ios-design` at 242.5K under `uizze.sh`; detail pages were unreachable at sweep time - revisit next sweep).

## NEW Candidates Below the Guide Floor

| Source | Listings | Installs | Note |
|---|---|---|---|
| delorenj/skills | 94 | ~1,017 combined | Active (pushed Oct 8); no LICENSE file; re-evaluate next sweep |
| kevinnft/ai-agent-skills | 96 | ~228 combined | Re-host of documented Hermes skills; stale since Aug |
| workweonline/hermes-agent-openmontage | 87 | ~178 combined | Video and animation skill bundle; 0 stars |
| trollz1004/antigravity | 70 | ~140 combined | Re-host bundle; 0 stars, no LICENSE |
| winstonkoh87/athena-public | 37 | ~120 combined | 598-star agent-context product (PyPI, CI); skill installs below floor - watching |
| (remaining 20 listings) | 20 | all <= 97 installs | personal or dormant single-skill repos - below floor |

## Notes

- **Collection window:** third consecutive run at ~440 unique (vs 706-733 from Sep 29 through Oct 7 morning). Direct API probes confirm the large publishers still exist on skills.sh (for example mattpocock/skills has 52 listings and anthropics/skills has 20) - they are simply not served in the standard query windows. The trending-page compensation pass now carries discovery; monitoring whether the serving change persists.
- **Zero-catalog audit:** the standing OpenClaw and Azure sources were not served this window; publisher follow-ups for the day's NEW sources confirmed no hidden clusters above the floor.
- **Duplicate defense:** no Oct 8 skills-sweep commit existed at the remote tip (f76928ade); single scheduled fire for the 1100z slot.
- Mechanics: one-pass rg crossref on the Mac Mini (~15s); 0 failed queries; all four new guides drafted against Oct 8, 2026 snapshots.

---

*Sweep run: Oct 8, 2026, skills-monitor cron (morning). Includes the shadcn, Amplitude, mbfinotti Business Skills, and Cloudflare Security Audit setup guides.*
