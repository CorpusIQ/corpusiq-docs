---
title: "New Skills - October 11, 2026"
description: "Skills.sh sweep (Oct 11): 892 skills checked; 1 new publisher guide - Claude Code Extensions (9.6K combined, 21 plugins, 60+ agents)."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-oct11-2026-skills/"
robots: "index,follow"
last_updated: "2026-10-24"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - October 11, 2026 (Morning Sweep)

Sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog. The 20-query v3 window (15 Hermes-focused + 5 generic) served 892 unique skills (0 failed queries), cross-referenced in a one-pass rg run on the Mac Mini: 15 NEW, 291 PARTIAL.

The fire produced one above-floor find: Claude Code Extensions (nodnarbnitram/claude-code-extensions, 9.6K combined), a 21-plugin Claude Code extension collection. The queue remains drained from Oct 10 evening; today's remaining NEW finds and the standing zero-catalog audit set all sized below the 5K guide floor and stay in the working set for triage.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills collected | 892 (20 queries, 0 failed) |
| NEW (not in catalog) | 15 |
| PARTIAL (source known, skill not cataloged) | 291 |
| New publisher guides | 1 (~9.6K combined installs) |
| Zero-catalog audit | 9 sources re-sized; all standing, 0 converts |
| Working set | 13 NEW sources below the 5K floor |
| Marketplace count | 1,133+ to 1,134+ |

## New Publisher Guides

### 1. Claude Code Extensions - Agents, Skills & Hooks Setup (9.6K)

**Source:** [nodnarbnitram/claude-code-extensions](https://www.skills.sh/nodnarbnitram/claude-code-extensions) (9,637 combined across 23 indexed listings; 16 stars, MIT; pushed Apr 20, 2026; top: tauri-v2 7,662)

21 self-contained Claude Code plugins: 60+ agents, 18 model-invoked skills, 8 lifecycle hooks, and 11 slash commands. Safety hooks (dangerous-command blocking, .env protection, audit logging), auto-linting, and an interactive installer that merges settings.json. Deep verticals in Home Assistant, ESPHome, Frigate, Kubernetes, Grafana, and Tauri.

-> [Setup guide](/hermes/skills/catalog/nodnarbnitram-claude-code-extensions-setup)

## Zero-Catalog Audit - Findings

All 9 PARTIAL sources at 100+ with no catalog-guide hit re-sized; every disposition standing:

| Source | Combined | Disposition |
|---|---|---|
| melodic-software/claude-code-plugins | 4,042 | Below floor (96 listings; flat vs Oct 10) |
| gogf/skills | 3,186 | Below floor (official GoFrame; flat) |
| zzci/skills | 3,143 | Below floor (flat) |
| cuellarfr/design-skills | 2,931 | Below floor (flat) |
| nodeops-app/skills | 2,684 | Below floor (flat) |
| chadboyda/agent-gtm-skills | 2,562 | Below floor (flat) |
| kv0906/cc-skills | 2,013 | Below floor (flat) |
| 404kidwiz/claude-supercode-skills | n/a | Deleted source (still 404; skip stands) |
| zhaoxuya520/reverse-skill | 956 | Excluded on security verdicts (Oct 10 ruling stands) |

## Working Set - Below the 5K Floor

Today's NEW finds below the 5,000-install guide floor (tracked for future triage; publisher follow-up sizes):

| Source | Combined | Note |
|---|---|---|
| peterhdd/agent-skills | 1,731 | 19 listing role-based engineering skills |
| amirtaherkhani/nestjs-skills | 1,647 | 7 NestJS skills; active (pushed Oct 9, 2026) |
| soljourner/claude-engineering-skills | 1,382 | 36 mechanical/aerospace engineering skills; 84 stars |
| adamlipecz/esp32-firmware-engineer-skill | 1,242 | Single skill; no LICENSE file |
| arjitj2/swiftui-design-principles | 1,227 | Single skill |
| nathan-gage/python-skills | 866 | 3 skills; no LICENSE file |
| trussary/vietnamese-language-skill | 811 | 5 Vietnamese-language copy skills |
| selfdriven-octo/skillzeb | 408 | Engineering role skills |
| dannyjpwilliams/ui-sound-design-skill | 312 | Single skill |
| sjy051/music-composition | 223 | Single skill |
| tomstools11/prompt-engineering-expert | 201 | Single skill |
| noamseg/interview-coach-skill | 189 | Single skill |
| designrique/ai-graphic-design-skill | 117 | Single skill |

## Notes

- **Sweep window steady:** 892 unique vs 893 (Oct 10 evening) and 894 (Oct 10 morning); the 20-query v3 plan holds.
- **Queue empty; no refill:** Oct 10 evening drained all 19 queued sources; today produced no above-floor candidates beyond the one guide, so the queue stays empty.
- **Zero-catalog audit flat:** all nine sources match their Oct 10 sizes; no re-qualifications.
- **Duplicate defense:** no Oct 11 skills-sweep commit existed at the remote tip (eaa5fba0b = MCP night sweep); single scheduled fire for the 1100z slot.
- **Mechanics:** one-pass rg crossref on the Mac Mini; 0 failed queries; all counts are exact-source API sums; guide and this page drafted against Oct 11, 2026 snapshots.

---

*Sweep run: Oct 11, 2026, skills-monitor cron (morning, 0400 MST). Includes the Claude Code Extensions setup guide and the zero-catalog audit re-check.*
