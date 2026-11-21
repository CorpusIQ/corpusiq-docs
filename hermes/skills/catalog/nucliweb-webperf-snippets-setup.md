---
title: "WebPerf Snippets - Web Performance Skills Setup Guide"
description: "nucliweb/webperf-snippets: tested JavaScript snippets that measure and debug web performance - 1.7K combined installs across 6 indexed listings."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/nucliweb-webperf-snippets-setup/"
robots: "index,follow"
last_updated: "2026-11-20"
tags: ["hermes skill", "agent skill", "skill setup", "web performance", "core web vitals", "performance debugging"]
---

# WebPerf Snippets - Web Performance Skills Setup Guide

**Source:** [nucliweb/webperf-snippets](https://www.skills.sh/nucliweb/webperf-snippets) via skills.sh - 1.7K combined installs across 6 indexed listings; first seen Nov 20, 2026 (Nov 20, 2026 evening sweep)
**GitHub:** [nucliweb/webperf-snippets](https://github.com/nucliweb/webperf-snippets) - 1,457 stars, MIT license, main branch, last pushed Nov 19, 2026; canonical skills under `skills/<name>/SKILL.md` with wrapper trees for Claude (`.claude/skills/`) and Antigravity (`dist/antigravity/`) plus a flat browser build under `dist/`.
**Category:** Web Performance
**Quality Tier:** 🟠 Orange - five of six sampled skills carry a Gen Agent Trust Hub Fail with a Snyk Warn, so review the source snippets before running them in a production codebase.

`webperf-snippets` is a Web Performance snippets library from Joan Leon (nucliweb) that gives AI agents deterministic measurement code for Core Web Vitals, loading, media, interaction and resource hints. The core idea is that AI agents are good at interpreting performance data and unreliable when they write measurement code on the fly, so the measurement stays fixed code, tested in CI, that returns structured data, and the agent reasons about the result. The same snippets run in the DevTools console, a CLI, a DevTools extension and the Agent Skills, and every one returns an object that follows a single contract.

The repository ships six skills under a canonical `skills/` tree with wrapper trees for Claude and Antigravity, and installs through the `skills` CLI in the Agent Skills format, backed by Chrome DevTools MCP for driving the browser. Each skill pairs the measurement scripts with workflows (predefined sequences) and decision trees that pick the next snippet from the result of the previous one. First seen in the Nov 20, 2026 evening sweep.

## Installation

```bash
npx skills add nucliweb/webperf-snippets
```

This installs the skills from the GitHub repository into `~/.claude/skills/`. To install them from a clone instead:

```bash
git clone https://github.com/nucliweb/webperf-snippets.git
cd webperf-snippets
npm run install-skills   # into .claude/skills/ of the current project
npm run install-global   # into ~/.claude/skills/, for every project
```

The skills pass each script to Chrome DevTools MCP by path, and the server only reads files inside its workspace roots. For skills outside the project, such as in `~/.claude/skills/`, add a `--workspace` argument to the server with the real folder of the skills and not a symlink to it:

```json
"args": ["-y", "chrome-devtools-mcp@latest", "--workspace=/absolute/path/to/skills"]
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| webperf-core-web-vitals | 302 | LCP, CLS and INP measurement with automated workflows and decision trees for guided debugging |
| webperf-media | 275 | Image, video and SVG audits with lazy loading checks and layout shift risk detection |
| webperf-interaction | 275 | INP debugging, scroll jank, long tasks and main thread blocking analysis |
| webperf-loading | 274 | TTFB, FCP, render-blocking resources, scripts, fonts and resource hint validation |
| webperf | 271 | Main entry point for all web performance analysis, spanning 57 snippets |
| webperf-resources | 257 | Network bandwidth and connection quality with adaptive loading strategies |

All 6 indexed listings appear in the table above.

## Why This Matters for Hermes Agents

The skills in this library address the weakest link in agent-driven performance work: agents that estimate or rewrite measurement code instead of running the same tested code every time. webperf-snippets keeps the measurement fixed and CI-tested, returning a structured object the agent reads, so a Hermes agent reports the measured value, the cause and the issues rather than a plausible guess. Every snippet follows one contract, so results stay comparable across the console, the CLI, the DevTools extension and the skills. The decision trees make the agent self-correcting: when TTFB reads above 600 ms, the agent runs the TTFB sub-parts snippet to split the time across DNS, connection and server. The six skills decompose cleanly by concern, from Core Web Vitals through loading, interaction, media and resources, so an agent picks the right scope instead of running a monolithic audit. Because the snippets are deterministic and the CLI exposes a `--json` mode, the same numbers an agent produces in a session can gate a pull request in CI.

## Usage

| You say | What happens |
|---|---|
| Audit this page for Core Web Vitals | Runs the webperf-core-web-vitals skill to measure LCP, CLS and INP with follow-up analysis |
| Why is my TTFB so high? | Runs TTFB.js, then TTFB sub-parts when slow to split DNS, connection and server time |
| Check for image optimization issues | Runs the webperf-media skill to audit image and video elements and flag oversized assets |
| Debug slow interactions or janky scrolling | Runs the webperf-interaction skill for INP, long tasks and long animation frames |
| Measure the page on a slow connection | Runs the webperf-resources skill to detect connection type and recommend adaptive loading |

## Verification

```bash
# after install, confirm the skills landed in the shared skills path
ls ~/.claude/skills/
# review one skill before relying on it
curl -sL https://raw.githubusercontent.com/nucliweb/webperf-snippets/main/skills/webperf/SKILL.md
```

The raw SKILL.md URL above was probed Nov 20, 2026 and returned HTTP 200. The canonical tree lives under `skills/<name>/SKILL.md`; the `.claude/skills/` and `dist/antigravity/` trees are generated wrappers of the same six skills.

## Security

skills.sh verdicts for sampled skills (verified Nov 20, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| webperf-core-web-vitals | Fail | Pass | Warn |
| webperf-media | Fail | Pass | Warn |
| webperf-interaction | Fail | Pass | Warn |
| webperf-loading | Fail | Pass | Warn |
| webperf | Pass | Pass | Warn |
| webperf-resources | Fail | Pass | Pass |

## Limitations

- Snapshot data, verified Nov 20, 2026: 1,654 combined installs across 6 indexed listings; 1,457 GitHub stars; MIT license; last pushed Nov 19, 2026. Counts drift over time.
- Five of the six sampled skills carry a Gen Agent Trust Hub Fail with a Snyk Warn, so read the source snippets before running them in a production codebase.
- The snippets target Chromium DevTools performance tooling: all are tested in Google Chrome, most also work in other Chromium-based browsers and Firefox, and Safari has limited Performance API support.
- The umbrella `webperf` skill overlaps the five sub-skills, so install only the ones your agent actually audits rather than the full set.

## Related

- [Skill for SEO - Technical SEO Audit Setup](/hermes/skills/catalog/iannuttall-seo-setup)
- [Claude SEO - SEO Analysis Setup](/hermes/skills/catalog/claude-seo-setup)
- [Community Access Accessibility - A11y Skills Setup](/hermes/skills/catalog/community-access-accessibility-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start from the umbrella `webperf` skill as the entry point, then let its decision trees route to the specialized sub-skills.
- Point Chrome DevTools MCP at the real skills folder rather than a symlink, or the server returns an Access denied answer.
- Read a snippet's source before trusting its numbers: five of six skills carry a Gen Agent Trust Hub Fail.
- Use the CLI's `--json` mode when you need reproducible numbers that can gate a pull request in CI.
- Start from the symptom: the Which snippet should I use page maps a symptom to a snippet before you ask the agent to run anything.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
