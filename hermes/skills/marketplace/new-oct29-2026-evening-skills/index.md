---
title: "New Skills - October 29, 2026 Evening"
description: "Skills.sh sweep (Oct 29 evening): 885 skills scanned, 12 publisher guides for 821,254 combined installs across 372 indexed listings."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-oct29-2026-evening-skills/"
robots: "index,follow"
last_updated: "2026-10-29"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - October 29, 2026 Evening Sweep

Sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog. The standing 20-query window returned 885 unique skills with 0 failed queries: 86 NEW, 266 PARTIAL.

This fire did not come from the standing window. That window was silent above the 1,000-install trigger for the twenty-second consecutive fire, its top row reading 295 installs, and all 60 of its NEW sources sized below 2,000 combined once queried by publisher. The trending board served 600 entries across 77 sources with every one of them already in the tree. So the fire ran a widened 47-query topic probe across business and engineering subjects, which returned 3,764 unique skills and 710 uncovered sources, 34 of them above the 5,000-install floor once sized by publisher.

Twelve of those clusters are documented below for **821,254 combined installs across 372 indexed listings**, from 128,923 at the top to 9,849 at the bottom. The other 22 above-floor clusters are sized and queued for the next fire.

Every guide was drafted against a pre-built pack holding the exact per-listing install figures, the cloned repository tree, the branch and licence metadata and the three-auditor verdicts sampled from skills.sh, then checked with three gates: the format gate, the pack cross-check at a per-guide threshold, and the frontmatter audit. All 36 gate runs passed, re-run by the orchestrator after an md5 comparison of the three canonical scripts.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills collected (standing window) | 885 (0 failed queries) |
| NEW (not in catalog) | 86 |
| PARTIAL (source known, skill not cataloged) | 266 |
| Trending board | 600 entries / 77 sources, 0 uncovered |
| Above-floor finds in the standing window | 0 (top row 295) |
| Topic probe (47 queries) | 3,764 unique / 710 uncovered sources |
| Above-floor clusters found | 34 |
| New publisher guides | 12 (372 indexed listings, 821,254 combined installs) |
| Queued for the next fire | 22 above-floor clusters |
| Marketplace count | 1,227+ to 1,237+ |

## New Publisher Guides

### 1. Elastic Agent Skills (128,923 combined)

**Source:** [elastic/agent-skills](https://www.skills.sh/elastic/agent-skills), 54 indexed listings, top skill `elasticsearch-esql` at 4,901; 603 stars; Apache-2.0; branch main; 62 `SKILL.md` files under `plugins/<group>/skills/<name>/` and a mirrored `skills/<group>/` tree.

The official Elastic suite, published by the vendor: Elasticsearch query authoring in ESQL and DSL, Kibana dashboards and alerting rules, Observability investigations and APM, Security detections and case management, and Cloud project provisioning. Two facts shape the guide. The 62 in-tree files are 31 skills duplicated byte for byte across the plugin tree and the flat skills tree, so the repository ships half as many distinct skills as its file count suggests. And the install index outruns the code: 23 of the 54 indexed names were removed in the v0.6.0 changelog and still carry 2,691 to 3,152 installs each, while `marketplace.json`, the plugin manifests and a README tip still advertise connectors, streams, log search, SLOs and service health. The guide names which rows have nothing to install and where a current skill absorbed the intent.

Gen Agent Trust Hub passes every sampled listing, with a Socket warn on onboarding and Snyk warns on case management and the CSP investigation skill. Twelve Node scripts live under `scripts/` in three security skills, which the Security section names.

### 2. claude-mem (101,470 combined)

**Source:** [thedotmack/claude-mem](https://www.skills.sh/thedotmack/claude-mem), 34 indexed listings, top skill `mem-search` at 9,016; 104,989 stars; Apache-2.0; branch main; 44 `SKILL.md` files across a plugin tree plus per-harness trees for Cursor, OpenClaw, OpenCode and a Grok bot.

A memory layer for coding agents: session history is compressed into a searchable store, and skills sit on top of it to search it, explore it, build a plan from it, run work against it and report on it. The guide documents the install routes the repository itself documents, including the `--ide` targets and the worker requirement, and reviews what the skills assume about the store being populated.

Five of six sampled listings pass all three auditors, with a Gen Agent Trust Hub warn on `timeline-report`. The guide states the drift plainly: 34 indexed listings against 44 in-tree files, because the same skill name exists in several harness trees with different bodies.

### 3. Claude Ads (98,745 combined)

**Source:** [agricidaniel/claude-ads](https://www.skills.sh/agricidaniel/claude-ads), 34 indexed listings, top skill `ads-meta` at 4,891; 10,586 stars; MIT; branch main; one directory per indexed listing, with the conductor at `ads/` and specialists under `skills/`.

A paid-media suite: a conductor skill that routes to per-platform specialists for Meta, Google, TikTok, X, Amazon and Apple, plus cross-cutting skills for creative, competitor research, attribution, auditing and optimization. The guide is careful about which platform skills write and which only read, because the Snyk warns land on the ones that touch live ad accounts.

Thirty-four listings against thirty-four directories, all rows in the table. Two of the three Snyk warns sit on skills that describe themselves as read-only, and the guide says so rather than inventing an explanation for the mismatch.

### 4. AI Research Skills (97,018 combined)

**Source:** [orchestra-research/ai-research-skills](https://www.skills.sh/orchestra-research/ai-research-skills), 100 indexed listings, top skill `ml-paper-writing` at 2,363; 14,111 stars; MIT; branch main; 98 `SKILL.md` files across eleven numbered topic directories plus an autoresearch orchestrator.

An ML research library organised the way a curriculum is: model architecture, tokenization, fine-tuning, mechanistic interpretability, data processing, post-training, safety alignment, distributed training, infrastructure, optimization and evaluation, with one skill per named framework or paper technique. An installer CLI moves a whole category at a time, which the guide documents as the real unit of install.

The guide leads with a caveat that matters more than the counts: the installer's positional argument matches category ids rather than skill names, and the `hermes` target it registers writes to `~/.hermes/skills` rather than a profile's skills directory. Two indexed listings have no directory, both stale duplicates of skills that exist under current names.

### 5. K2F (62,502 combined)

**Source:** [suzheng/k2f](https://www.skills.sh/suzheng/k2f), 42 indexed listings, top skill `k2f-worksheet` at 3,275; 3 stars; Apache-2.0; branch main; 42 skill directories across ten categories under `skills/`.

An open document format plus the skills that write it: semantic JSON compiles into Word, PowerPoint, fillable PDF and IDML, with skills per document type covering worksheets, quotations, invitations, sales decks, flyers, contracts, academic papers, posters and grant proposals. The core skill is the largest thing in the repository, with a schema, a catalog of templates, starter assets and a pack verifier.

Every sampled listing carries a Snyk warn and five of six carry a Socket warn, structural to a generator that shells out to a Python CLI over user-supplied JSON. The guide states the registry drift it found: `skills/registry.json` names 48 ids while six have no folder and one referenced discovery directory does not exist in the tree.

### 6. Roblox Brain (61,628 combined)

**Source:** [tabooharmony/roblox-brain](https://www.skills.sh/tabooharmony/roblox-brain), 37 indexed listings, top skill `roblox-building` at 2,560; 143 stars; MIT; branch main; 29 skill directories under `skills/core/`, `skills/gameplay/`, `skills/tools/` and similar.

The most complete Roblox Studio library in the catalog: Luau core patterns, architecture, data and persistence, building, lighting, animation and VFX, GUI, economy, testing, publishing and a Studio MCP integration, each skill carrying a review date and a progressive-disclosure reference set.

The security profile is the weakest of the batch and the guide leads with it: `roblox-testing` fails Gen Agent Trust Hub and Snyk while the other five sampled listings pass or warn. The count drift is real too, with eight indexed names having no directory at main, two of them documented as removals in the 2.0.0 changelog.

### 7. Bailian CLI (59,841 combined)

**Source:** [modelstudioai/cli](https://www.skills.sh/modelstudioai/cli), 9 indexed listings, top skill `bailian-cli` at 18,816; 366 stars; Apache-2.0; branch main; 12 `SKILL.md` files under `skills/` and `packages/<pkg>/skills/`.

Alibaba Cloud Model Studio's own CLI, with the agent skills that teach it: the `bl` command surface, protocol and API conventions, generation, fine-tuning, managed agents, web search, knowledge bases and sandbox work. Because the skills are the CLI's operating manual rather than a wrapper, the guide treats the CLI install and auth flow as the real prerequisite and documents it from `INSTALL.md`.

Two Snyk warns land on the managed-agent and knowledge skills, which is where credentials and customer data would sit.

### 8. Coralogix cx CLI (58,206 combined)

**Source:** [coralogix/cx-cli](https://www.skills.sh/coralogix/cx-cli), 32 indexed listings, top skill `cx-telemetry-querying` at 5,090; 233 stars; Apache-2.0; branch master; 19 end-user skills under `skills/` plus four contributor-only skills under `.claude/skills/`.

The vendor's observability CLI with a skill per job: DataPrime and log, span and metric queries, dashboards, alerts, incident management, RUM, instrumentation and the CLI's own reference docs. The guide separates the two trees, because four of the in-tree skills are internal engineering workflow skills marked `internal: true` that an end user should never install.

Sixteen of the thirty-two listings clear the 500-install threshold, and `cx-incident-management` has no directory in the tree at all, which the guide says in its row rather than inventing a description.

### 9. Sent Plugin (54,176 combined)

**Source:** [sentdm/sent-plugin](https://www.skills.sh/sentdm/sent-plugin), 21 indexed listings, top skill `sent` at 2,921; 49 stars; MIT; branch main; 84 `SKILL.md` files across four parallel layouts.

An official messaging suite: SMS and 10DLC registration, WhatsApp Business templates and embedded signup, RCS onboarding, sender profiles, compliance, migration and messaging performance analysis, with six skills shipping offline `scripts/` that carry `--self-test`. A remote MCP endpoint at `mcp.sent.dm` exposes 27 tools for the same surface.

The 84 files are the 21 skills in four adapter layouts, `packages/sent/skills/` being canonical and the plugin, plugin-marketplace and Claude Code trees generated from it. The guide notes that the Claude adapter is a policy overlay rather than a byte copy, so a test written against one layout is not automatically valid on another.

### 10. Base44 Skills (51,043 combined)

**Source:** [base44/skills](https://www.skills.sh/base44/skills), 6 indexed listings, top skill `base44-sdk` at 11,538; 92 stars; MIT; branch main; five product skills under `skills/` plus four contributor-only skills under `.claude/skills/`.

The platform vendor's own skill set for building on Base44: SDK application code, CLI project work, remote development, the sandbox environment and a production troubleshooter, all wired to a documented MCP endpoint. Five rows clear the threshold and one, `base44-coder`, has no directory and no verdict table, which the guide reports as an index listing with nothing to review.

Two facts worth knowing before install: the plugin manifests are pre-release builds, and one plugin's `skills` and `assets` entries are git symlinks, so a tarball or Windows checkout can break them.

### 11. SwiftUI Agent Skill (37,853 combined)

**Source:** [avdlee/swiftui-agent-skill](https://www.skills.sh/avdlee/swiftui-agent-skill), 2 indexed listings, top skill `swiftui-expert-skill` at 35,473; 3,791 stars; MIT; branch main; two skill directories.

The only Production-tier guide of the batch, and the clearest single-skill install in months: one SwiftUI expert skill with 33 reference files, a 33-entry topic router and a 17-item correctness checklist, plus a second skill that rescans Apple documentation and updates the API reference under a soft-deprecation rule. Both sampled listings pass all three auditors.

The guide documents what the expert skill actually checks, how the API reference is segmented by iOS version up to iOS 27.1, and the one environment variable the trace tooling needs that neither the repository nor Hermes sets.

### 12. Slack CLI Skill (9,849 combined)

**Source:** [paymog/slack-cli](https://www.skills.sh/paymog/slack-cli), 1 indexed listing (`slack-cli`); 0 stars; MIT; branch master; `skills/slack-cli/SKILL.md`.

A Go CLI that gives an agent JSON reads and writes on a Slack workspace without a resident MCP server per agent, built on the same engine as the widely used Slack MCP server. One listing, one skill, and a Snyk warn (`S123`) that the guide names without speculating about the finding text.

The same publisher's Groundcover and incident.io CLI guides are already in this catalog, so the guide links both and notes the pattern: a thin CLI plus a long operating contract, where the skill teaches command choice rather than hiding the API.
