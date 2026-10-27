---
title: "New Skills - October 20, 2026 (Evening)"
description: "Skills.sh sweep (Oct 20 evening): 887 skills checked; 1 new publisher guide - TestDino Playwright Skills (8.7K combined, 79 Playwright 1.64 guides across seven packs)."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-oct20-2026-evening-skills/"
robots: "index,follow"
last_updated: "2026-10-24"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - October 20, 2026 (Evening Sweep)

Sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog. The 20-query v3 window (15 Hermes-focused plus the 5-query generic pass) served 887 unique skills in both passes with 0 failed queries: 20 NEW, 300 PARTIAL.

The fire produced one above-floor find: [testdino-hq/playwright-skill](https://www.skills.sh/testdino-hq/playwright-skill) at 8,684 combined installs across 9 indexed listings. It is a 79-guide Playwright reference set from testdino.com, split into seven installable packs (core, qa, frontend, ci, pom, migration, playwright-cli) and pinned to Playwright 1.64. It surfaced in the sweep as a single 128-install row (playwright-qa); the mandatory publisher follow-up sized the suite at 8,684 combined installs, 68x the single-row reading and above the 5,000-install guide floor, with the flagship skill alone at 6,248. Every other NEW source stayed below the floor, the zero-catalog audit is unchanged at 0 converts, and the standing below-floor set carries forward flat.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills collected | 887 (pass 1 and pass 2, identical; 0 failed) |
| NEW (not in catalog) | 20 |
| PARTIAL (source known, skill not cataloged) | 300 |
| New publisher guides | 1 (8,684 combined installs) |
| Zero-catalog audit | 59 sources at 100+; 15 uncovered in catalog/; 0 converts |
| Marketplace count | 1,135+ to 1,136+ |

## New Publisher Guides

### 1. TestDino Playwright Skills - 79-Guide Playwright Suite (8.7K)

**Source:** [testdino-hq/playwright-skill](https://www.skills.sh/testdino-hq/playwright-skill) (8,684 combined across 9 indexed listings; 397 stars, MIT; pushed Oct 12, 2026; top: playwright-skill 6,248)

A 79-guide Playwright reference set published by testdino.com, written to be loaded on demand by a coding agent rather than read end to end. Seven packs cover the full surface: core testing (50 guides), QA workflows (4), frontend test-hook authoring (2), CI pipelines (9), page objects (2), Cypress and Selenium migration (2), and terminal browser automation through playwright-cli (10). The top-level SKILL.md is the canonical index and carries the Golden Rules plus architecture-decision material. Content tracks current Playwright rather than generic training data: `locator.within()`, WebMCP testing via `page.webmcp.tools()`, `--shuffle`, `test.describe.configure({ lock })`, WebP screenshots and `page.getByRef()` are all documented, with the 1.63 and 1.62 changes that commonly trip agents. TypeScript throughout, JavaScript in most core guides. Security posture is mostly clean (Trust Hub Pass on every sampled skill) with two specific warnings worth reading: a LOW Socket anomaly in `playwright-cli/running-custom-code.md` covering clipboard, auth-state and download handling, and a MEDIUM Snyk prompt-injection warning on the CLI pack for arbitrary-URL browsing.

-> [Setup guide](/hermes/skills/catalog/testdino-playwright-skill-setup)

## Zero-Catalog Audit - Findings

59 PARTIAL sources at 100+ combined installs, audited against `catalog/` recursively (716 markdown files, full `owner/repo` match then exact owner token). 15 carry no catalog page and every one is below the 5,000-install guide floor:

| Source | Combined | Disposition |
|---|---|---|
| gogf/skills | 3,231 | Below floor (real GoFrame repo; closest, 65% of floor) |
| 404kidwiz/claude-supercode-skills | 1,971 | Deleted source (standing exclusion) |
| nodeops-app/skills | 1,679 | Below floor |
| kv0906/cc-skills | 1,367 | Below floor |
| zhaoxuya520/reverse-skill | 1,078 | Security exclusion (standing) |
| nathan-gage/python-skills | 852 | Below floor |
| peterhdd/agent-skills | 466 | Below floor |
| amirtaherkhani/nestjs-skills | 361 | Below floor |
| zzci/skills | 360 | Below floor |
| selfdriven-octo/skillzeb | 295 | Below floor |
| cuellarfr/design-skills | 282 | Below floor |
| trussary/vietnamese-language-skill | 201 | Below floor |
| melodic-software/claude-code-plugins | 170 | Below floor |
| soljourner/claude-engineering-skills | 130 | Below floor |
| chadboyda/agent-gtm-skills | 128 | Below floor |

## Other NEW Sources - All Below the Floor

| Source | Combined | Note |
|---|---|---|
| cnkang/skills | 263 | 4 listings; qdrant-memory carries all but 20 installs |
| gregm1991/skills | 257 | 50 listings (API cap, so a floor) |
| bolone-sengkuni/hermes-brutal-mod | 156 | 50 listings (API cap) |
| deng-yang-dream/anyekoutouming | 57 | 50 listings (API cap) |
| alvedder/skills | 29 | 7 listings |
| tmrisdaone/hermes-skills | 11 | 7 listings |
| arimanyus/hermes-merchant | 6 | 3 listings |
| impact-automation/hermes-vps-backup | 6 | 6 listings |
| xiaoxuan0820-ctrl/hermes-agent | 5 | 3 listings |
| hailorlem/esl-automation-suite | 3 | 2 listings |
| dev-herni/hermes-skill-pack | 2 | 2 listings |
| easy-4-rust/xls-cli | 2 | 1 listing |
| hermesagentai.org | 1 | 1 listing |
| fiz-is/hermes-cron-cost | 1 | 1 listing |

## Notes

- **Single-row sweep flag sized 68x by the publisher follow-up:** the sweep served one testdino row (playwright-qa, 128 installs); the exact-source re-dump returned 9 rows / 8,684 combined. First-seen check: absent from the Oct 19 evening and Oct 20 morning NEW sets, so Oct 20 evening is the first sighting.
- **Both passes agree exactly:** 887 unique / 20 NEW / 300 PARTIAL in pass 1 and pass 2, so no query drift contributed to the find.
- **Catalog audit method:** walked `catalog/` recursively. A flat listing invents above-floor gaps on sources documented as category pages.
- **Duplicate defense:** no Oct 20 evening skills-sweep commit at the remote tip before this push (881a1dad0 = MCP evening sweep).
- **Mechanics:** one-pass rg crossref on the Linux host (41s per pass); counts are exact-source API sums; guide and this page drafted against Oct 20, 2026 snapshots.

---

*Sweep run: Oct 20, 2026, skills-monitor cron (evening, 2200 MST). Includes the TestDino Playwright Skills setup guide and the zero-catalog audit re-check.*
