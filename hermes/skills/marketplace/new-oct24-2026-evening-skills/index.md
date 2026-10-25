---
title: "New Skills - October 24, 2026 Evening"
description: "Skills.sh sweep (Oct 24 evening): 94 new skills, five publisher clusters from the trending board totalling 456,281 combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-oct24-2026-evening-skills/"
robots: "index,follow"
last_updated: "2026-10-24"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - October 24, 2026 Evening Sweep

Evening sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog. The same 20-query window (15 Hermes-focused plus the 5-query generic pass) served 885 unique skills with 0 failed queries: 94 NEW, 270 PARTIAL.

The NEW lane stayed silent for the twelfth consecutive fire, and its top row this time was nathan-gage/python-skills python-best-practices at 853 installs, a source already sized at 896 combined in the morning fire. Every convert came from the trending board, which served 514 entries across 55 sources: 50 sources were already covered, and all five uncovered sources cleared the floor once queried by publisher. That is the widest convert count this catalog has published from a single board since the Ponytail fire on October 23.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills collected | 885 (0 failed queries) |
| NEW (not in catalog) | 94 |
| PARTIAL (source known, skill not cataloged) | 270 |
| New publisher guides | 5 (35 indexed listings, 456,281 combined installs) |
| Above-floor finds rejected | 0 |
| Zero-catalog audit | 45 PARTIAL sources at 100+; 0 uncovered in catalog/ recursive (737 markdown files); 0 converts |
| Board | Trending 514 entries / 55 sources; 50 covered, 5 uncovered, 5 converts |
| Marketplace count | 1,152+ to 1,157+ |

## New Publisher Guides

### 1. Anthony Fu Skills (375,749 combined)

**Source:** [antfu/skills](https://www.skills.sh/antfu/skills), 21 indexed listings, top skill `vitest` at 43,245; 6,008 stars; MIT; pushed 2026-10-23.

The largest single convert of the fire, and the largest technical-surface suite in the catalog. Anthony Fu maintains Vue, Vite and Nuxt, and this repository generates skills from the official documentation of each project, pinned as git submodules, then adds his own hand maintained conventions on top. Twelve skill directories cover Vue, Nuxt, Vite, Vitest, Pinia, pnpm, UnoCSS, VitePress, Nitro and his own setup, pull request and issue triage rules.

Beta tier, on the author's own words rather than on the auditors: every sampled listing passes all three, and the README calls the project a proof of concept it has not fully tested. The catalog note that matters is the drift: 21 indexed listings against 12 directories, so nine rows in the guide ship as listing only, and `antfu-design` lives in the separate `antfu/design` repository.

### 2. shadcn Improve (37,531 combined)

**Source:** [shadcn/improve](https://www.skills.sh/shadcn/improve), 1 indexed listing, `improve` at 37,531; 9,259 stars; MIT; pushed 2026-09-12.

One skill, one idea: use the capable model to audit a codebase and write plans, then hand execution to a cheaper one. The skill is read-only on source by design, writes only to `plans/`, vets every finding against the cited line before showing it, and stamps each plan with the commit it was written against. `execute` runs an executor in a disposable worktree, `reconcile` refreshes the backlog, `--issues` publishes plans as GitHub issues.

Production tier. It is the cleanest delegation contract in the catalog: source is read only, secrets are never reproduced, merging stays with the human, and all three auditors pass.

### 3. Hypit (18,987 combined)

**Source:** [hypit-ai/hypit](https://www.skills.sh/hypit-ai/hypit), 1 indexed listing, `hypit` at 18,987; 25,425 stars; license reported as NOASSERTION; pushed 2026-10-24.

An agent video production system rather than a generator. Drop in a viral video and the skill clones the workflow into an editable SVML composition, then swap the host, the hook, the product or the language and re-render only what changed. Generated footage and code-rendered visuals sit in the same composition, so anything with text or brand assets can render locally with no model call.

Beta tier. All three auditors pass, and the skill ships no credential of its own, but it drives a separately installed executable and connects to paid generation services. The licence is the reservation: GitHub cannot classify it, the README links a Hypit Open Source License while the repository badge reads Apache-2.0 with conditions.

### 4. Masseater Skills (12,962 combined)

**Source:** [masseater/skills](https://www.skills.sh/masseater/skills), 10 indexed listings, top skill `measure-dont-guess` at 1,619; 2 stars; no LICENSE; pushed 2026-10-24.

Nine engineering judgment skills rather than tool knowledge: measure before you guess, integrate a dependency by migrating the call sites and adding the enforcement, do not write what the repository already has, and write prose a human can read. Every body is a short rule list that starts from why the skill exists.

Beta tier, and the reason is language plus licence rather than quality. Every `SKILL.md` is written in Japanese, the repository has no LICENSE file, and the star count is two against install counts above a thousand per listing. The guide says all of that plainly.

### 5. Ultracite (11,052 combined)

**Source:** [haydenbleasel/ultracite](https://www.skills.sh/haydenbleasel/ultracite), 2 indexed listings, `ultracite` at 11,051; 3,352 stars; MIT; pushed 2026-10-24.

The skill for a lint and format preset rather than a new tool: detect whether the project uses Biome, ESLint or Oxlint, then run `check`, `fix`, `doctor` or `upgrade` correctly, with `--workspace-framework` mapping for monorepos and an optional handoff of unfixable files to Claude Code or Codex. It exists because agents otherwise invent configuration in a repository that already standardized.

Production tier. One narrow skill, MIT, an active release cadence, all three auditors passing, and no code changes without an explicit command.

## Why This Fire Matters

The board produced a different kind of find than the trading and crypto suites of the last week. Three of the five converts are about how an agent should work rather than what it can call: a codebase audit that writes plans instead of patches, a set of rules that forbid guessing, and a lint preset that defines the standard the agent writes to. That is the direction the ecosystem is moving, from capability skills to discipline skills, and it is the lane worth watching.

The Anthony Fu find also shows why the publisher query is not optional. The board showed one row of 576 installs from that source; the publisher query returned 21 listings at 375,749 combined, a 652x multiple. Multiples this fire ran from 2.7x (Masseater, where the board already carried nine rows) to 652x, and earlier fires stayed between 4.6x and 68x. A single board row can understate a publisher by two orders of magnitude, so the query runs on every uncovered source, not only the large ones.

## Cross-Reference Note

The coverage test excludes per-fire report pages (`!**/marketplace/new-*/**`), so a name stays NEW until a guide exists. The zero-catalog audit walked `catalog/` recursively (737 markdown files) and found 0 of the 45 PARTIAL sources at 100 or more installs without a page. `/popular` returned HTTP 404 again and `/skills` remains a shell with no embedded skill JSON, so the trending board is still the only board that returns data.

---

*← [Skills Marketplace](/hermes/skills/marketplace) | [Skills Catalog](/hermes/skills/catalog) →*
*Powered by CorpusIQ*
