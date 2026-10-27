---
title: "New Skills - October 21, 2026 (Evening)"
description: "Skills.sh evening sweep (Oct 21): 887 skills checked, 105 new. Ant Design joins the catalog with a 11.8K-install official antd suite across two repos."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-oct21-2026-evening-skills/"
robots: "index,follow"
last_updated: "2026-10-24"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - October 21, 2026 (Evening Sweep)

Evening sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog. The same 20-query window (15 Hermes-focused plus the 5-query generic pass) served 887 unique skills with 0 failed queries: 105 NEW, 270 PARTIAL.

This fire produced one above-floor find, and it came from the publisher follow-up rather than the sweep window itself. The window saw a single row, [ant-design/antd-skill](https://www.skills.sh/ant-design/antd-skill) at 4,098 installs, which sits below the 5,000 guide floor and has been carried as a below-floor row since October 21 morning. Following the publisher instead of the row surfaced a second repo, [ant-design/ant-design-cli](https://www.skills.sh/ant-design/ant-design-cli), whose `antd` skill carries 5,979 installs on its own. Together the official Ant Design org holds 12 indexed listings and 11,760 combined installs, which is 2.3x the floor, so the cluster converts.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills collected | 887 (pass 1 and pass 2; 0 failed) |
| NEW (not in catalog) | 105 |
| PARTIAL (source known, skill not cataloged) | 270 |
| New publisher guides | 1 (11,760 combined installs) |
| Above-floor finds rejected | 0 this fire (1 standing rejection re-confirmed) |
| Zero-catalog audit | 48 sources at 100+; 0 uncovered in catalog/; 0 converts |
| Trending | 600 entries / 68 sources; 6 uncovered, all previously dispositioned |
| Marketplace count | 1,137+ to 1,138+ |

## New Publisher Guides

### 1. Ant Design Skills - Official antd Suite (11,760 combined)

**Source:** [ant-design/ant-design-cli](https://www.skills.sh/ant-design/ant-design-cli) (5,979 for `antd`) and [ant-design/antd-skill](https://www.skills.sh/ant-design/antd-skill) (4,098 for `ant-design`, 1,329 for `antd`); 12 indexed listings across the org; MIT on both repos; 260 and 136 stars; the CLI repo was pushed on the day of this sweep.

The Ant Design org publishes its own agent layer, and the load-bearing half is a CLI. `@ant-design/cli` ships every antd prop, token, demo, changelog entry and design document inside the npm package, 67 per-version snapshots deep (v3 2, v4 26, v5 31, v6 8), so an agent can query the exact API surface of antd 5.12.0 offline instead of guessing from memory. The bundled skill teaches the order of operations: `antd info` for props, `antd demo` for a working example, then write. Project-side commands finish the loop with `antd lint` for deprecated APIs and accessibility gaps, `antd doctor` for ten configuration checks, `antd usage` for import statistics and `antd migrate` for a v3 to v6 upgrade checklist that splits auto-fixable from manual work.

The sibling repo holds the decision guide: component selection, theming tokens, provider setup for CSR and SSR, accessibility, performance, Pro routing and CRUD direction, and Ant Design X chat and streaming patterns. A `antd mcp` stdio server exposes eight lookup tools and two prompts for agents that prefer MCP over shell calls.

Two facts decided the tier. Both repos are MIT with LICENSE files on disk, and the CLI repo carries a vitest suite per command. The one wrinkle is duplication: the `antd` skill exists in both repos and the copies differ, with the ant-design-cli version allowing `antd upgrade` and claiming v3 to v6 migration coverage while the antd-skill copy allows neither.

-> [Setup guide](/hermes/skills/catalog/ant-design-skills-setup)

## Standing Rejection Re-confirmed

[cyxzdev/uncodixfy](https://www.skills.sh/cyxzdev/uncodixfy) remains the only NEW row at 5,589 installs and remains excluded: Snyk rates it CRITICAL under E004 prompt injection, with instructions telling the agent to act as if it cannot see its own reasoning. It has been published as a rejection since the morning fire and was not re-evaluated here.

## Zero-Catalog Audit

48 PARTIAL sources sit at 100 or more combined installs, audited against `catalog/` recursively (717 markdown files, full `owner/repo` match then exact owner token). 0 carry no catalog page, so the conversion queue is empty and there are no converts this fire.

Two below-floor sources stay on the carry list: [ant-design/antd-skill](https://www.skills.sh/ant-design/antd-skill) is no longer one of them, because this fire's guide covers the whole org; [gogf/skills](https://www.skills.sh/gogf/skills) at 3,236 combined remains below the floor on its own. One standing exclusion holds: 404kidwiz/claude-supercode-skills still returns 404 from GitHub at 1,971 installs, so its counts are unactionable.

## Trending

The trending board served 600 entries across 68 sources. Six sources have no catalog page: dietrichgebert/ponytail (6,551 across 6 entries), wheresryan22/anatomy (1,251), iannuttall/seo (1,011), cathrynlavery/diagram-design (653), morluto/rea (637) and binance/binance-skills-hub (617). All six were dispositioned in earlier fires: the ponytail family is documented as `hermes-ponytail-setup` under its original owner, morluto/rea was handled in the October 10 finds digest, and the other four are low-install single-skill repos below the guide floor. No new trending entrant crossed the floor this fire.

## Cross-Reference Note

The coverage test excludes per-fire report pages (`!**/marketplace/new-*/**`), so names stay NEW until a guide exists. That is why this fire reports 105 NEW where an earlier build of the same test read 0 from the same data, and why the count moved from 106 to 105 rather than drifting: the two dbskill rows the morning fire converted are now genuinely covered.
