---
title: "New Skills - October 23, 2026"
description: "Skills.sh sweep (Oct 23): 101 new skills, four publisher clusters from 321.6K to 9.4K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-oct23-2026-skills/"
robots: "index,follow"
last_updated: "2026-10-24"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - October 23, 2026 Sweep

Morning sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog. The same 20-query window (15 Hermes-focused plus the 5-query generic pass) served 886 unique skills with 0 failed queries: 101 NEW, 270 PARTIAL.

All four conversions came from the trending board again, but this fire is worth reading for one row in particular. The board returned 570 entries across 66 sources, the largest window any of these sweeps has seen, and 61 of those 66 sources already had a catalog page. Of the 5 that did not, 4 cleared the floor as publishers. The largest of them, DietrichGebert/ponytail, sizes at 321,598 combined installs across 6 listings, which is the biggest single find since this catalog began tracking the board.

The NEW lane, for the ninth consecutive fire, produced nothing at the guide floor: its top row was 0xdesign/design-plugin at 1,942 installs.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills collected | 886 (0 failed queries) |
| NEW (not in catalog) | 101 |
| PARTIAL (source known, skill not cataloged) | 270 |
| New publisher guides | 4 (68 indexed listings, 399,475 combined installs) |
| Above-floor finds rejected | 0 |
| Zero-catalog audit | 47 PARTIAL sources at 100+; 0 uncovered in catalog/ recursive (730 markdown files); 0 converts |
| Board | Trending 570 entries / 66 sources; 61 covered, 4 uncovered as publishers, 4 converts |
| Marketplace count | 1,146+ to 1,150+ |

## New Publisher Guides

### 1. Ponytail Skills (321,598 combined)

**Source:** [DietrichGebert/ponytail](https://www.skills.sh/dietrichgebert/ponytail), 6 indexed listings, top skill `ponytail` at 102,473; 174,315 stars; MIT; pushed 2026-10-18.

A coding mode, packaged as six skills: the mode itself plus review, whole-repo audit, a deferred-shortcut ledger, a usage card and a savings scoreboard. The mode's rule is a ladder the agent stops at: does it need to exist, is it already in this codebase, does the standard library do it, is there a platform feature, is there an installed dependency, can it be one line, and only then the minimum that works.

Production tier. All six listings pass Gen Agent Trust Hub, Socket and Snyk, the rules are plain instruction files, and the repository carries CI test and publish workflows. The catalog already carries a third-party Hermes port of this project as seven skills; the guide says plainly that the two repositories are different, and this one is canonical.

### 2. Stripe Link CLI Skills (49,047 combined)

**Source:** [stripe/link-cli](https://www.skills.sh/stripe/link-cli), 4 indexed listings, top skill `create-payment-credential` at 19,627; 869 stars; MIT; pushed 2026-10-23.

Stripe's agent payments surface. An agent requests a credential for a specific spend, a human approves it in the Link app, and the agent completes checkout without the real card number ever being present. Three skills cover the credential request, the financial read path and identity attestations; a fourth listing covers the CLI itself and has no matching skill directory in the tree.

Beta tier, and the reason is not maintainability. Snyk raises direct money access and third-party content exposure, Socket warns on the same skill, and both are accurate descriptions of an agent that can spend. US and Canadian Link accounts only.

### 3. Anatomy Skill (19,442 combined)

**Source:** [wheresryan22/anatomy](https://www.skills.sh/wheresryan22/anatomy), 1 indexed listing at 19,442; 19,426 stars; MIT; pushed 2026-10-18.

A figure-building skill that explains a technical idea by building the physical object whose working is the idea, drawn isometrically in SVG with optional WebGL layers that live inside the same perspective, then checked by an audit that proves clearances and depth order per frame.

Beta tier on one specific finding: Gen Agent Trust Hub rates it MEDIUM for data exfiltration, command execution, dynamic execution and indirect prompt injection, and the evidence is a session script that reads local agent conversation logs to compute token metrics. Socket and Snyk both pass. Building a figure does not need that script, and the guide says so.

### 4. SEO Skill (9,388 combined)

**Source:** [iannuttall/seo](https://www.skills.sh/iannuttall/seo), 57 indexed listings, top skill `seo` at 9,332; 590 stars; Apache-2.0; pushed 2026-10-23.

A Google Search Console MCP server and CLI that gives an agent the site's own clicks, impressions, positions, indexing reasons and Bing and Analytics rows, plus a crawler. Ten commands, no settings, and every result ends with the command to run next.

Beta tier. Snyk rates it medium for third-party content exposure through the crawler and for a remote MCP endpoint the auditor cannot inspect, which are structural to a tool that fetches strangers' pages. The remaining 56 indexed listings carry 1 install each and only one SKILL.md exists in the tree.

## Why This Fire Matters

The board is where discovery happens now, and the ratio keeps getting more extreme. Three of this fire's four finds sat well below the 5,000-install floor as single board rows, and one publisher query turned them into 399,475 combined installs across 68 listings. A board row measures one skill; it says almost nothing about the repository behind it.

The second pattern is that the biggest finds are no longer libraries. Ponytail is a behavior, Link CLI is a capability, Anatomy is a craft constraint and the SEO skill is a data source. None of them adds tools an agent did not have; each changes how the agent uses what it has, which is the harder thing to write and the more valuable thing to install.

## Cross-Reference Note

The coverage test excludes per-fire report pages (`!**/marketplace/new-*/**`), so a name stays NEW until a guide exists. The zero-catalog audit walked `catalog/` recursively (730 markdown files) and found 0 of the 47 PARTIAL sources at 100 or more installs without a page, which is the ninth consecutive fire with no convert from that lane.

---

*← [Skills Marketplace](/hermes/skills/marketplace) | [Skills Catalog](/hermes/skills/catalog) →*
*Powered by CorpusIQ*
