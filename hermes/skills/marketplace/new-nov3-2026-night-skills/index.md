---
title: "New Skills - November 3, 2026 Night"
description: "Skills.sh sweep (Nov 3 night): 17 publisher guides for 751K combined installs across 561 indexed listings from a widened topic probe."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-nov3-2026-night-skills/"
robots: "index,follow"
last_updated: "2026-11-03"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - November 3, 2026 Night Sweep

Sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog. The standing 20-query window returned 884 unique skills with 0 failed queries: 84 NEW and 261 PARTIAL, with no NEW source above the 1,000-install trigger and its top row reading 306 installs. That is the thirty-first consecutive fire on which the standing window was silent above the floor.

Every NEW source with a listing at or above 1,000 installs was then sized by its own repository instead of by its best window row, and all 59 NEW sources stayed below the 5,000-install floor, the largest being soljourner/claude-engineering-skills at 1,639 combined. The trending board served 492 entries across 51 sources with one uncovered source, archify.si, a domain with no repository behind it.

The November 2 evening fire had drained the standing queue, so this fire ran a widened 98-query topic probe across business, engineering and infrastructure topics: 3,514 unique sources, 0 failed queries and 2,909 sources with no catalog page. The 321 uncovered sources carrying a window row of 1,000 installs or more were sized by repository, and 19 cleared the 5,000-install floor with a reachable repository and at least one skill directory. Two were held back: gracefullight/stock-checker, a personal aggregator carrying 211 vendored skill directories from other publishers, and gjkim42/kanon-repo, a repository with 0 stars, no licence and no description.

The probe also showed how far a window row understates a publisher. plannotator/effective-html read a 4,254-install board row and sizes at 18,017 across 8 listings, while egonex-ai/understand-anything read 4,040 and sizes at 34,989 across 9 listings. Every guide was built from a pre-verified pack holding exact per-listing install figures, a depth-1 clone with its branch, licence and skill directories, and three-auditor verdicts sampled across each index. Each draft was then checked with three gates: the format gate, the pack cross-check at the pack's own threshold and the frontmatter audit. All 51 gate runs passed on the orchestrator re-run after an md5 comparison of the three canonical scripts, with no fix cycles.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills (standing 20-query window) | 884 (0 failed queries) |
| NEW (not in catalog) | 84 |
| PARTIAL (source known, skill not cataloged) | 261 |
| Above-floor finds in the standing window | 0 (top row 306) |
| Topic probe queries | 98 |
| Unique sources returned by the probe | 3,514 (0 failed) |
| Uncovered sources after the probe | 2,909 |
| Uncovered sources sized by repository | 321 |
| Sources above the 5,000-install floor | 19 |
| Guides published this fire | 17 |
| Combined installs documented | 751,059 |
| Indexed listings covered | 561 |

## Source Detail

| # | Source | K form | Exact combined | Listings | Stars | Tier |
|---|---|---|---|---|---|---|
| 1 | runpod/runpod-plugins-official | 134.1K | 134,136 | 19 | 47 | Yellow |
| 2 | vercel-labs/json-render | 105.8K | 105,845 | 38 | 18,893 | Green |
| 3 | vercel/turborepo | 87.6K | 87,555 | 1 | 31,299 | Green |
| 4 | lobehub/lobehub | 79.9K | 79,938 | 69 | 83,762 | Green |
| 5 | jsmastery-pro/skills | 52.9K | 52,893 | 13 | 1,595 | Yellow |
| 6 | callstack/agent-device | 43.9K | 43,931 | 5 | 5,248 | Yellow |
| 7 | thedivergentai/game-dev-agentic-skills | 41.7K | 41,716 | 100 | 924 | Green |
| 8 | egonex-ai/understand-anything | 35.0K | 34,989 | 9 | 90,113 | Yellow |
| 9 | millionco/react-doctor | 28.2K | 28,201 | 18 | 15,076 | Yellow |
| 10 | hairyf/skills | 25.7K | 25,708 | 81 | 26 | Green |
| 11 | madteacher/mad-agents-skills | 24.5K | 24,479 | 11 | 111 | Green |
| 12 | plannotator/effective-html | 18.0K | 18,017 | 8 | 3,826 | Green |
| 13 | jeremylongshore/tons-of-skills-marketplace | 17.0K | 17,030 | 137 | 2,894 | Green |
| 14 | linear/linear-release | 15.3K | 15,255 | 1 | 70 | Green |
| 15 | software-mansion-labs/skills | 14.9K | 14,921 | 27 | 299 | Yellow |
| 16 | securityskills/skills | 14.5K | 14,496 | 21 | 0 | Yellow |
| 17 | astral-sh/claude-code-plugins | 11.9K | 11,949 | 3 | 318 | Green |

## New Setup Guides

- [Runpod Plugin - GPU Pod and Serverless Skill Setup](/hermes/skills/catalog/runpod-plugins-official-setup) - runpod/runpod-plugins-official, 134,136 combined, 19 listings, 47 stars, Apache-2.0, `runpodctl` and `flash` pass all three auditors but the third sampled skill, `companion-clis`, carries a Warn from Gen Agent Trust Hub, Socket and Snyk
- [JSON Render - Generative UI Framework Setup](/hermes/skills/catalog/json-render-setup) - vercel-labs/json-render, 105,845 combined, 38 listings, 18,893 stars, Apache-2.0, all three sampled listings pass Gen Agent Trust Hub, Socket and Snyk, and the repository ships an Apache-2.0 LICENSE file
- [Turborepo Skill - Monorepo Build System Setup](/hermes/skills/catalog/turborepo-skill-setup) - vercel/turborepo, 87,555 combined, 1 listings, 31,299 stars, MIT, the single sampled listing passes Gen Agent Trust Hub, Socket and Snyk, and the repository ships an MIT LICENSE file
- [LobeHub Skills - Agent Platform Engineering Setup](/hermes/skills/catalog/lobehub-skills-setup) - lobehub/lobehub, 79,938 combined, 69 listings, 83,762 stars, NOASSERTION, all three sampled listings pass Gen Agent Trust Hub, Socket and Snyk, and the repository ships a LICENSE file, though that file is a custom community licence rather than a standard OSI one
- [JS Mastery Skills - Agentic Development Workflow](/hermes/skills/catalog/jsmastery-skills-setup) - jsmastery-pro/skills, 52,893 combined, 13 listings, 1,595 stars, MIT, Snyk warns on the sampled `architect` listing while Gen Agent Trust Hub and Socket pass all three sampled skills, and the repository does ship a LICENSE file (MIT)
- [Agent Device - Mobile Device Control for Agents](/hermes/skills/catalog/agent-device-setup) - callstack/agent-device, 43,931 combined, 5 listings, 5,248 stars, MIT, Snyk warns on the sampled `agent-device` listing while Gen Agent Trust Hub and Socket pass all three sampled skills, and the repository does ship a LICENSE file (MIT)
- [Game Dev Agentic Skills - Godot and Bevy Suite](/hermes/skills/catalog/game-dev-agentic-skills-setup) - thedivergentai/game-dev-agentic-skills, 41,716 combined, 100 listings, 924 stars, LGPL-3.0, all three sampled listings pass every auditor (Gen Agent Trust Hub, Socket and Snyk) and the repository ships an LGPL-3.0 LICENSE file
- [Understand Anything - Code to Knowledge Graph Setup](/hermes/skills/catalog/understand-anything-setup) - egonex-ai/understand-anything, 34,989 combined, 9 listings, 90,113 stars, MIT, Snyk fails the sampled `understand-dashboard` listing while Gen Agent Trust Hub and Socket pass all three sampled skills, and the repository does ship a LICENSE file (MIT)
- [React Doctor - React Codebase Diagnostics Setup](/hermes/skills/catalog/react-doctor-setup) - millionco/react-doctor, 28,201 combined, 18 listings, 15,076 stars, NOASSERTION, Gen Agent Trust Hub fails the deslop listing and Snyk warns on react-doctor and improve-react, even though the repo ships a licence file and the sampled skills are Markdown wrappers around one CLI
- [Hairyf Skills - Vue, Nuxt and Tooling Collection](/hermes/skills/catalog/hairyf-skills-setup) - hairyf/skills, 25,708 combined, 81 listings, 26 stars, MIT, all nine sampled verdicts across three listings pass on Gen Agent Trust Hub, Socket and Snyk, and the repository ships an MIT licence file
- [MAD Agents Skills - Dart and Flutter Suite Setup](/hermes/skills/catalog/mad-agents-skills-setup) - madteacher/mad-agents-skills, 24,479 combined, 11 listings, 111 stars, MIT, all nine sampled verdicts across three listings pass on Gen Agent Trust Hub, Socket and Snyk, and the repository ships an MIT licence file
- [Effective HTML - Artifact and Prototype Skills](/hermes/skills/catalog/effective-html-setup) - plannotator/effective-html, 18,017 combined, 8 listings, 3,826 stars, MIT, all three sampled listings pass Gen Agent Trust Hub, Socket and Snyk, and the repository ships an MIT LICENSE
- [Tons of Skills - Agent Skills Marketplace Platform](/hermes/skills/catalog/tons-of-skills-marketplace-setup) - jeremylongshore/tons-of-skills-marketplace, 17,030 combined, 137 listings, 2,894 stars, MIT, all three sampled listings pass Gen Agent Trust Hub, Socket and Snyk, and the repository ships an MIT LICENSE
- [Linear Release - Release Tracking CLI Setup](/hermes/skills/catalog/linear-release-setup) - linear/linear-release, 15,255 combined, 1 listings, 70 stars, MIT, the sampled listing passes Gen Agent Trust Hub, Socket and Snyk, and the repository ships an MIT LICENSE
- [Software Mansion Skills - React Native Suite Setup](/hermes/skills/catalog/software-mansion-skills-setup) - software-mansion-labs/skills, 14,921 combined, 27 listings, 299 stars, NONE, all three sampled listings pass every auditor, but the repository carries no licence file at all, so the MIT claim exists only in metadata
- [Security Skills - Pentest and Compliance Suite](/hermes/skills/catalog/securityskills-setup) - securityskills/skills, 14,496 combined, 21 listings, 0 stars, NONE, all three sampled listings pass every auditor, but no licence file ships with the repository and it has 0 stars
- [Astral Plugins - Python uv, ruff and ty Setup](/hermes/skills/catalog/astral-sh-claude-code-plugins-setup) - astral-sh/claude-code-plugins, 11,949 combined, 3 listings, 318 stars, Apache-2.0, all three sampled listings pass every auditor and the repository ships both licence files

## Distribution Notes

Eleven of the seventeen are Yellow and six Green. The tier rule is mechanical: a source is Green only when every sampled auditor verdict is a Pass and the repository ships a licence file. runpod/runpod-plugins-official is Yellow on a Warn across all three auditors for its companion-clis skill; lobehub/lobehub is Green because every sampled verdict passed and a LICENSE file exists, though GitHub reports NOASSERTION over the LobeHub Community License; software-mansion-labs/skills and securityskills/skills carry no licence file at all; millionco/react-doctor ships a Modified MIT text the GitHub detector does not assert; and millionco/react-doctor's own deslop listing fails the Gen Agent Trust Hub audit, as do the understand-dashboard listing for egonex-ai/understand-anything and one listing for jsmastery-pro/skills.

## What This Fire Changed

The topic probe is now the only lane producing converts. The standing window has been silent above the 1,000-install trigger for thirty-one consecutive fires, and consecutive fires that converted have done so entirely from probe output. Publisher sizing is not optional on probe results: a single window row understated this batch's sources by as much as 8.7 times, and every one of the 59 NEW sources stayed below the floor once sized properly.

## Distribution Notes

10 of the 17 are Green and 7 are Yellow. The tier rule is mechanical: a source is Green only when every sampled auditor verdict is a Pass and the repository ships a licence file, so the Warn, the Fail or the absent licence is named in the guide rather than footnoted.

The Yellow set splits two ways. Five carry an auditor finding: runpod/runpod-plugins-official is Warned across all three auditors for its companion-clis skill, jsmastery-pro/skills and callstack/agent-device take a Snyk Warn on one listing each, egonex-ai/understand-anything takes a Snyk Fail on understand-dashboard, and millionco/react-doctor carries a Gen Agent Trust Hub Fail on deslop plus Snyk Warns on two more, with a Modified MIT text the GitHub detector does not assert. Two ship no licence file at all: software-mansion-labs/skills has no LICENSE in the tree, and securityskills/skills has none either, at 0 stars. Among the Green, lobehub/lobehub is the one to read the licence on: it runs a LobeHub Community License that GitHub reports as NOASSERTION.

## What This Fire Changed

The topic probe is now the only lane producing converts. The standing window has been silent above the 1,000-install trigger for thirty-one consecutive fires, and consecutive fires that converted have done so entirely from probe output. Publisher sizing is not optional on probe results: a single window row understated this batch's sources by as much as 8.7 times, and every one of the 59 NEW sources stayed below the floor once sized properly.

Index-versus-tree drift is stated factually wherever it appears: lobehub/lobehub indexes 69 names against 56 skill directories with four above-threshold names absent from the canary tree, thedivergentai/game-dev-agentic-skills indexes 100 names against 184 directories, jeremylongshore/tons-of-skills-marketplace indexes 137 names against 5,758 directories, and software-mansion-labs/skills carries 26 SKILL.md files that are 11 top-level skills plus 15 nested sub-skills.

