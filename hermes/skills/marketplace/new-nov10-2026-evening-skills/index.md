---
title: "New Skills - November 10, 2026 Evening"
description: "Skills.sh sweep (Nov 10 evening): 6 publisher guides for 29,700 combined installs across 56 indexed listings"
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-nov10-2026-evening-skills/"
robots: "index,follow"
last_updated: "2026-11-10"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - November 10, 2026 Evening Sweep

Sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog. The standing 20-query window returned 884 unique skills across 0 failed queries: 83 NEW rows and 251 PARTIAL, with the top NEW row at 337 installs and nothing above the 1,000-install trigger. That is the forty-sixth consecutive silent window.

With the standing window silent again, this fire drained the pre-sized candidate queue that the November 10 morning write-up left behind. Eleven sources were named there. All eleven were re-tested against the current tree before any sizing, and all eleven still had zero coverage. Six were documented and five are recorded under Held with the reason each one was stopped, including one publisher whose GitHub account no longer resolves.

Every guide was built from a pre-verified pack holding the exact per-listing install figure for every indexed skill, the repository metadata, the real skill layout read from the GitHub tree, the frontmatter description of each skill and the live security verdicts from skills.sh. Each draft was then checked with three gates: the format gate, the pack cross-check at a per-guide threshold and the frontmatter audit. All 18 gate runs are green.

No fresh topic probe ran this fire. The queue drain plus the docs build consumed the pass, and the next fire should open with a probe over territories this queue does not cover rather than draining further from it.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills (standing 20-query window) | 884 (0 failed queries) |
| NEW (not in catalog) | 83 rows |
| PARTIAL (source known, skill not cataloged) | 251 |
| Above-floor finds in the standing window | 0 (top row 337) |
| Pre-sized queue re-tested | 11 of 11 uncovered |
| Pre-sized queue drained | 6 of 11 |
| Fresh topic probe | none this fire |
| Guides published this fire | 6 |
| Combined installs documented | 29,700 |
| Indexed listings covered | 56 |
| Tier mix | 2 Green, 1 Yellow, 3 Orange |

## New Setup Guides

- [Embedded Skills - Firmware and Debugger Setup](/hermes/skills/catalog/embeddedskills-setup) - zhinkgit/embeddedskills, 8,222 combined, 12 listings, 793 stars, MIT, Embedded systems: Keil and GCC builds, J-Link and OpenOCD flashing, serial, CAN and network debugging, all 12 skill bodies written in Chinese
- [Flutter AI Rules - Dart and Firebase Setup](/hermes/skills/catalog/flutter-ai-rules-setup) - evanca/flutter-ai-rules, 8,083 combined, 37 listings, 670 stars, MIT, Flutter development: state management, architecture, testing, accessibility and 16 Firebase service skills
- [Sanity Context Skills - Structured Content Setup](/hermes/skills/catalog/sanity-context-setup) - sanity-io/context, 3,479 combined, 4 listings, 7 stars, no LICENSE file, Structured content: agent context construction, prompt shaping and GROQ queries over Sanity Content Lake
- [Self-Learning Skill - Agent Improvement Setup](/hermes/skills/catalog/self-learning-skill-setup) - philschmid/self-learning-skill, 3,432 combined, 1 listings, 97 stars, Apache-2.0, Agent self-improvement: researching a new library on the web into a reusable SKILL.md with four anti-fabrication rules
- [draw.io MCP - Diagram Authoring Setup](/hermes/skills/catalog/drawio-mcp-setup) - jgraph/drawio-mcp, 3,421 combined, 1 listings, 5,809 stars, Apache-2.0, Diagramming: the official draw.io MCP server and the drawio skill for .drawio files, ELK layout and PNG, SVG and PDF export
- [UX Writing Skill - Interface Copy Setup](/hermes/skills/catalog/ux-writing-skill-setup) - content-designer/ux-writing-skill, 3,063 combined, 1 listings, 262 stars, MIT, Product copy: interface microcopy, error and empty states, accessibility rules and design-system voice enforcement

## What Was Notable

- **draw.io MCP** is the official jgraph server with 5,809 stars, and the index compresses it to one listing because all five client plugins ship the same skill text. The guide documents both servers and the rule the skill itself states: call the MCP `create_diagram` tool where the chat renders diagrams inline, and use the skill where nothing does.
- **Embedded Skills** is the largest uncovered source in the queue at 8,222 installs, and it earns a guide on substance rather than size: twelve skills that wrap Keil, CMake with arm-none-eabi-gcc, J-Link, OpenOCD, probe-rs, tshark and SSH behind one JSON envelope plus a state file. Every skill body is written in Chinese, which the guide states in the intro and the Limitations rather than working around.
- **Flutter AI Rules** is the only Green tier of the batch on a 25-listing sample that passes all three scanners, and it covers the Flutter surface end to end, including sixteen Firebase product skills. Its one honest gap is a listing with 120 installs and no directory at `main`.
- **Sanity Context** is vendor-published but unlicensed. The guide carries that in four places because the legal position for vendoring the skill text is genuinely unstated, and it draws the line between this read-only endpoint and the older Sanity MCP Server that has full workspace access.

## Held

- **404kidwiz/claude-supercode-skills** (20,036 combined across 96 indexed listings): the GitHub account returns 404 for the repository and for the account itself. skills.sh still serves the listings, so the install count is real demand against a tree that no longer exists. Not cataloged until the publisher reappears.
- **zhaoxuya520/reverse-skill** (63,683 combined across 88 listings): offensive security and reverse-engineering router pack, the standing exclusion class carried since the November 6 evening fire. The install volume is large and the skills are real; the class is not what this catalog documents.
- **dhruvanbhalara/skills** (6,369 combined across 63 listings): 43 Flutter skills on a documentation site, MIT, 30 stars. Held because the Flutter family was claimed this fire by a stronger source with 37 listings and a clean scanner record. It stays first in line for a future Flutter pass.
- **ctsstc/get-shit-done-skills** (3,744 combined across 69 listings): one plugin at 3,668 installs and 68 command-level listings at 1 or 2 installs each. The tree is clean at 69 `SKILL.md` files, but a guide built on that index shape would describe 68 entries nobody installs. Held on index shape, not on quality.
- **devmartinese/awwwards-animations-skill** (3,137 combined, 1 listing): one skill, 15 stars, no LICENSE file and last pushed 2026-02-09. Held on license and public signal.

## Method Notes

- Source sizing came from the skills.sh search API per source rather than from probe rows. That changed three figures materially against the morning note: `zhinkgit/embeddedskills` reads 8,222 now against 8,205, `evanca/flutter-ai-rules` reads 8,083 against 3,075 for the Flutter family, and `content-designer/ux-writing-skill` reads 3,063 against 3,032.
- Drift ratio was checked before drafting, per the rule the morning fire set. All six published sources hold a tree that matches or exceeds their listing count, except sanity (4 listings, 3 directories, named in its Limitations) and flutter (37 listings, 36 directories, also named).
- Security verdicts were read live from each skill page on skills.sh, one per in-table row, not sampled from a single page. That is why the embedded guide can state that `ssh` fails Gen Agent Trust Hub while the other eleven pass it.

## Related

- [Skills Catalog](/hermes/skills/catalog)
- [Skills Marketplace](/hermes/skills/marketplace)
- [November 10, 2026 Morning Sweep](/hermes/skills/marketplace/new-nov10-2026-morning-skills)
