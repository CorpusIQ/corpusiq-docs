---
title: "New Skills - October 11, 2026 (Evening)"
description: "Skills.sh sweep (Oct 11 evening): 892 skills checked; 1 new publisher guide - Wayne Sutton Builder Skills (37.6K combined, Convex app development + project workflow)."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-oct11-2026-evening-skills/"
robots: "index,follow"
last_updated: "2026-10-11"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - October 11, 2026 (Evening Sweep)

Sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog. The 20-query v3 window (15 Hermes-focused plus the 5-query generic pass) served 892 unique skills (0 failed queries, re-verified in a second pass), cross-referenced in a one-pass rg run on the Mac Mini (~35s): 2 NEW, 297 PARTIAL.

The fire produced one above-floor find: [waynesutton/builder-skills](https://www.skills.sh/waynesutton/builder-skills) at 37.6K combined installs - seventeen skills for building Convex apps plus a PRD-first project workflow loop, from Wayne Sutton. It surfaced in the sweep as a single skill row (convex-realtime, 2,877 installs); the mandatory publisher follow-up sized the cluster at 18 listings / 37,564 combined, 13x the single-row reading and well above the 5K guide floor. The queue remains drained, all other NEW finds and the zero-catalog audit set sized below the floor, and the working set carries forward essentially flat.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills collected | 892 (20 queries, 0 failed) |
| NEW (not in catalog) | 2 |
| PARTIAL (source known, skill not cataloged) | 297 |
| New publisher guides | 1 (~37.6K combined installs) |
| Zero-catalog audit | 16 sources re-sized; all standing, 0 converts |
| Working set | 13 sources carried; flat |
| Marketplace count | 1,134+ to 1,135+ |

## New Publisher Guides

### 1. Wayne Sutton Builder Skills - Convex App Development (37.6K)

**Source:** [waynesutton/builder-skills](https://www.skills.sh/waynesutton/builder-skills) (37,564 combined across 18 indexed listings; 406 stars, Apache-2.0; pushed Sep 28, 2026; top: convex 5,669)

Seventeen skills from Wayne Sutton: 13 Convex build skills (validators, indexes, schema, realtime, crons, webhooks, file storage, migrations, security checks and audits, agents) plus a four-skill project loop (PRD workflow, docs sync from git evidence, git safety, scope control). Ships via skills.sh, a Claude Code plugin marketplace, and an npm CLI; works with Claude Code, Codex, Cursor, and OpenCode. Distinct from the documented official get-convex set - the README positions it as the author's opinionated tuning.

-> [Setup guide](/hermes/skills/catalog/waynesutton-builder-skills-setup)

## Zero-Catalog Audit - Findings

All 16 PARTIAL sources at 100+ with no catalog-guide hit re-sized (superset of the standing nine: six working-set members now read as PARTIAL via page self-coverage, plus manager-dot-dev/manager-skills newly in the set); every disposition standing, 0 converts:

| Source | Combined | Disposition |
|---|---|---|
| melodic-software/claude-code-plugins | 4,042 | Below floor (96 listings; flat vs Oct 10) |
| manager-dot-dev/manager-skills | 3,503 | Below floor (27 listings; new to the standing set) |
| gogf/skills | 3,187 | Below floor (official GoFrame; flat) |
| zzci/skills | 3,153 | Below floor (flat) |
| cuellarfr/design-skills | 2,954 | Below floor (flat) |
| nodeops-app/skills | 2,684 | Below floor (flat) |
| chadboyda/agent-gtm-skills | 2,562 | Below floor (flat) |
| kv0906/cc-skills | 2,017 | Below floor (flat) |
| peterhdd/agent-skills | 1,733 | Below floor (19 listings; working set member) |
| amirtaherkhani/nestjs-skills | 1,683 | Below floor (7 listings; working set member) |
| soljourner/claude-engineering-skills | 1,383 | Below floor (36 listings; working set member) |
| nathan-gage/python-skills | 871 | Below floor (3 listings; working set member) |
| trussary/vietnamese-language-skill | 812 | Below floor (5 listings; working set member) |
| selfdriven-octo/skillzeb | 408 | Below floor (6 listings; working set member) |
| zhaoxuya520/reverse-skill | 48,582 | Excluded on security verdicts (Oct 10 ruling stands) |
| 404kidwiz/claude-supercode-skills | n/a | Deleted source (GitHub 404 re-verified; skip stands) |

## Working Set - Below the 5K Floor

Carried from the Oct 11 morning triage; the six members re-sized this fire are essentially flat and all stay below the 5,000-install guide floor:

| Source | Combined | Note |
|---|---|---|
| peterhdd/agent-skills | 1,733 | 19 listing role-based engineering skills |
| amirtaherkhani/nestjs-skills | 1,683 | 7 NestJS skills; active (pushed Oct 9, 2026) |
| soljourner/claude-engineering-skills | 1,382 | 36 mechanical/aerospace engineering skills; 84 stars |
| adamlipecz/esp32-firmware-engineer-skill | 1,242 | Single skill; no LICENSE file |
| arjitj2/swiftui-design-principles | 1,227 | Single skill |
| nathan-gage/python-skills | 871 | 3 skills; no LICENSE file |
| trussary/vietnamese-language-skill | 812 | 5 Vietnamese-language copy skills |
| selfdriven-octo/skillzeb | 408 | Engineering role skills |
| dannyjpwilliams/ui-sound-design-skill | 312 | Single skill |
| sjy051/music-composition | 223 | Single skill |
| tomstools11/prompt-engineering-expert | 201 | Single skill |
| noamseg/interview-coach-skill | 189 | Single skill |
| designrique/ai-graphic-design-skill | 117 | Single skill |

## Skipped

| Source | Combined | Disposition |
|---|---|---|
| pedicelmarketing/hermes-multi-agent | 3 | Below floor (3 listings at 1 install each; dormant) |

## Notes

- **Single-row sweep flag sized 13x by the publisher follow-up:** the sweep served one waynesutton row (convex-realtime 2,877); the exact-source re-dump returned 18 rows / 37,564 combined. First-seen check: zero hits in every prior sweep and trending snapshot, confirming the Oct 11 evening first sighting.
- **Queue:** drained (Oct 10 evening) with no above-floor refill this fire; this guide came direct from the NEW set.
- **Zero-catalog audit flat:** the standing nine plus six newly-self-covered working-set sources all re-sized; none re-qualified.
- **Duplicate defense:** no Oct 11 evening skills-sweep commit at the remote tip (1ac846c8a = MCP evening sweep); single scheduled fire for the 2200 MST slot.
- **Mechanics:** one-pass rg crossref on the Mac Mini (~35s); 0 failed queries (re-verified: 892 unique, 0 failed in the second pass); all counts are exact-source API sums; guide and this page drafted against Oct 11, 2026 snapshots.

---

*Sweep run: Oct 11, 2026, skills-monitor cron (evening, 2200 MST). Includes the Wayne Sutton Builder Skills setup guide and the zero-catalog audit re-check.*
