---
title: "New Skills - October 26, 2026"
description: "Skills.sh sweep (Oct 26): an extended query probe found 14 publisher clusters above the floor, 917.9K combined installs across 707 listings in one fire."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-oct26-2026-skills/"
robots: "index,follow"
last_updated: "2026-10-26"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - October 26, 2026 Sweep

Sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog. The standing 20-query window served 885 unique skills with 0 failed queries: 91 NEW, 270 PARTIAL. The NEW lane was silent above the 1,000-install trigger for the fifteenth consecutive fire, its top row `zzci/skills` at 364.

The fire still produced the largest guide batch this catalog has recorded, and the reason is a query-space finding rather than a publisher finding. After the standing window came back empty, eleven additional topic queries were run: data engineering, SEO, growth, sales, analytics, marketing, financial analysis, research, CRM, SaaS and business operations skills. That probe collected 959 unique skills across 146 sources with no catalog coverage. Fourteen of those sources cleared the 5,000-install floor once sized by publisher. Every one of them had been invisible to the Hermes-focused window and to the trending board.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills collected (standing window) | 885 (0 failed queries) |
| NEW (not in catalog) | 91 |
| PARTIAL (source known, skill not cataloged) | 270 |
| Extended probe (11 topic queries) | 959 unique, 0 failed, 146 uncovered sources |
| New publisher guides | 14 (707 indexed listings, 917,944 combined installs) |
| Above-floor finds rejected | 0 |
| Zero-catalog audit | 46 PARTIAL sources at 100+; 0 uncovered in catalog/ recursive (740 markdown files); 0 converts |
| Board | Trending 600 entries / 63 sources; 62 covered, 1 uncovered and below floor |
| Marketplace count | 1,160+ to 1,174+ |

## New Publisher Guides

### 1. Swift iOS Skills (305,876 combined)

**Source:** [dpearson2699/swift-ios-skills](https://www.skills.sh/dpearson2699/swift-ios-skills), 100 indexed listings, top skill `swiftui-animation` at 5,422; 1,237 stars; PolyForm Perimeter 1.0.0; pushed 2026-07-31.

The largest source in this sweep and the deepest single suite: 86 skills for iOS 26, Swift 6.3, SwiftUI and the modern Apple frameworks, with 259 eval scenarios and a `references/` folder on 85 of the 86 skills. It covers the work an agent gets wrong in a codebase it cannot run: SwiftUI state and animation, accessibility, concurrency, WidgetKit, StoreKit, and a two-skill app store review path.

Beta tier. Trust Hub and Socket pass on every sampled listing, but the license is source-available rather than open source, `app-store-review` carries a Snyk warning, and 14 indexed listings have no directory at `main`, most of them older versions of renamed skills.

### 2. Longbridge Skills (108,182 combined)

**Source:** [longbridge/skills](https://www.skills.sh/longbridge/skills), 134 indexed listings, top skill `longbridge` at 4,310; 66 stars; MIT; pushed 2026-10-26.

The official skill layer from Longbridge, a Hong Kong brokerage: market data, quotes, options and portfolio workflows behind a 13-skill tree, with a CLI and API credentials as the prerequisite. Two skills declare `risk_level: mutating`, which is the honest signal that they place or change account state.

Beta tier with caveats stated in the guide. Snyk flags `W009` direct money access on the portfolio skill, Socket and Trust Hub warn on the technical-analysis listing, and the index carries 134 listings against 13 directories, so most of the install base sits on consolidated names.

### 3. Nuxt Skills (69,820 combined)

**Source:** [onmax/nuxt-skills](https://www.skills.sh/onmax/nuxt-skills), 35 indexed listings, top skill `nuxt` at 8,550; 724 stars; no LICENSE file; pushed 2026-10-26.

Vue, Nuxt, Nuxt UI and NuxtHub skills generated from pinned official documentation by a Nuxt ecosystem maintainer, with weekly and biweekly CI that regenerates them. 26 skills cover routing, data fetching, rendering modes, deployment and the UI component layer.

Beta tier. All four sampled verdicts pass all three auditors and the maintenance cadence is the best in this batch, but there is no LICENSE file (the README and the plugin manifest both claim MIT), nine indexed listings have no directory at `main`, and the core skill is generated against a Nuxt 5 release candidate.

### 4. Dynatrace for AI (60,579 combined)

**Source:** [Dynatrace/dynatrace-for-ai](https://www.skills.sh/dynatrace/dynatrace-for-ai), 39 indexed listings, top skill `dt-dql-essentials` at 2,831; 167 stars; Apache-2.0; pushed 2026-10-23.

The official Dynatrace suite for agents working against production observability data: 34 skills and 346 reference files covering DQL, problems, logs, metrics, traces, Kubernetes and the Davis AI layer, plus 6 prompts and a registry-published remote MCP server.

Production tier. Apache-2.0, official attribution, in-repo structural tests on the skill tree, and three of four sampled listings pass all three auditors. The one reservation is a scanner warning on a single skill, quoted with its code in the guide.

### 5. Agent Research Skills (57,762 combined)

**Source:** [lingzhi227/agent-research-skills](https://www.skills.sh/lingzhi227/agent-research-skills), 31 indexed listings, top skill `literature-review` at 3,987; 433 stars; no LICENSE file; pushed 2026-02-27.

A systematic academic literature workflow: search, screen, extract, synthesize, cite and check references, with 16 bundled scripts and a citation-verification path. It is the deepest research suite in the catalog and the direct comparison to the existing academic research page is drawn in the guide.

Community tier, and the reason is verification rather than depth. Snyk fails `citation-management` on HIGH-risk credential handling, Socket and Snyk warn on the two flagship skills, Gen Agent Trust Hub passes two of three, and the repository has no LICENSE file.

### 6. Nia Skill (56,227 combined)

**Source:** [nozomio-labs/nia-skill](https://www.skills.sh/nozomio-labs/nia-skill), 1 indexed listing at 56,227; 26 stars; no LICENSE file; pushed 2026-03-29.

One skill at the repository root that teaches an agent to index and search repositories, documentation, papers and datasets through the Nia API, then answer from retrieved context rather than memory. It is a small, readable integration rather than a suite.

Beta tier, and the install figure is the story: 56,227 installs sit on one listing against 26 stars, which is distribution through a client integration rather than repository popularity. The guide says so plainly, and Snyk fails the single listing while Socket warns on it.

### 7. Sales Skills (51,654 combined)

**Source:** [louisblythe/Sales-Skills](https://www.skills.sh/louisblythe/sales-skills), 122 indexed listings, top skill `appointment-booking` at 882; 188 stars; no LICENSE file; pushed 2026-01-24.

122 sales skills: playbooks, discovery scripts, ICP definition, call analysis, forecast and pipeline hygiene, sales engineering and enablement. The distribution is flat, 122 listings between 396 and 882 installs, which reads as a broad working library rather than a few hits.

Beta tier. Every sampled listing passes all three auditors and the skills are prompt text with no scripts or network calls, but there is no LICENSE file (MIT is claimed only in README prose), the index and the manifest still carry a legacy repo spelling, and nothing has shipped since 2026-01-24.

### 8. Brand Building Skills (48,568 combined)

**Source:** [Arnabbagxd/Brand-building-skills](https://www.skills.sh/arnabbagxd/brand-building-skills), 29 indexed listings, top skill `brand-naming` at 2,216; 787 stars; MIT; pushed 2026-06-13.

29 brand skills that mirror the order of the work: strategy, positioning, naming, identity, voice, messaging, audits and launch. Each skill is a single procedure with a stated output, which is what makes a brand task reviewable instead of a wall of adjectives.

Beta tier, held below Production by maintenance rather than quality: MIT in the repository, Pass on all three auditors for four sampled skills, but evals on only 4 of 29 skills and no push since 2026-06-13.

### 9. AI Labs Claude Skills (42,078 combined)

**Source:** [ailabs-393/ai-labs-claude-skills](https://www.skills.sh/ailabs-393/ai-labs-claude-skills), 27 indexed listings, top skill `travel-planner` at 4,079; 458 stars; MIT with mixed document-skill terms; pushed 2025-11-11.

27 business and personal skills packaged as installable bundles: finance management, business analytics reporting, pitch decks, startup validation, research writing, a personal assistant and document handling. The repository ships its own bundler and installer scripts.

Beta tier. MIT at the repository level, Pass on Trust Hub and Socket for four sampled skills, but the last push was 2025-11-11, the 24 package entrypoints are generated stubs, and the four bundled document skills carry Anthropic proprietary terms instead of the repository license.

### 10. Arize Skills (38,812 combined)

**Source:** [Arize-ai/arize-skills](https://www.skills.sh/arize-ai/arize-skills), 18 indexed listings, top skill `arize-instrumentation` at 3,443; 67 stars; MIT; pushed 2026-10-22.

The official Arize skill suite for LLM observability work driven by the `ax` CLI: datasets, experiments, traces, spans, evaluators, prompt optimization, prompt versioning, annotation, compliance audit, instrumentation health and migrations from LangSmith, Langfuse and Braintrust.

Production tier. MIT, official attribution, all 18 listings resolve to a directory, a pytest suite and a CI skill validator ship in the repo, and release-please tracks the version. One sampled listing carries a Snyk warning, quoted in the guide.

### 11. Recoup Skills (31,987 combined)

**Source:** [recoupable/skills](https://www.skills.sh/recoupable/skills), 141 indexed listings, top skill `recoup-platform-api-access` at 4,957; 9 stars; AGPL-3.0 non-commercial with a paid commercial option; pushed 2026-10-26.

A record label in a box: 125 skills covering catalog audits, royalty reconciliation, release metadata, roster onboarding, song credits, content build, site generation and an internal consulting workflow set. It is the most complete vertical operations suite in this batch and the plainest example of a company publishing its own agent layer.

Beta tier. Very active, and the license is the constraint: AGPL-3.0 non-commercial with a commercial license offered separately, plus a Snyk warning on the sampled platform skills. 65 of the 125 skills are internal agency consulting workflows, which the guide states rather than dresses up.

### 12. Slavingia Skills (26,297 combined)

**Source:** [slavingia/skills](https://www.skills.sh/slavingia/skills), 10 indexed listings, top skill `validate-idea` at 2,992; 10,983 stars; no LICENSE file; pushed 2026-04-14.

Sahil Lavingia's ten book-based business skills, the operating system for The Minimalist Entrepreneur: community, validation, MVP, processization, first customers, pricing, marketing, sustainable growth, values and a decision review. Ten Markdown files, no scripts, no network, no credentials.

Beta tier. All 10 listings map one to one onto real directories and three sampled skills pass all three auditors, so the distribution is as clean as it gets; the reservation is legal rather than technical, because the repository has no LICENSE file while the plugin manifest claims MIT.

### 13. dbt Agent Skills (12,357 combined)

**Source:** [dbt-labs/dbt-agent-skills](https://www.skills.sh/dbt-labs/dbt-agent-skills), 19 indexed listings, top skill `using-dbt-for-analytics-engineering` at 1,169; 746 stars; Apache-2.0; pushed 2026-10-22.

The official dbt Labs suite: running dbt commands, fetching dbt docs, configuring the dbt MCP server, analytics engineering, unit tests, Mesh, state, semantic layer, documentation, job error triage, natural language questions, information schema queries, upgrades and an eval harness.

Production tier. Apache-2.0, official attribution, 17 skill directories, a pytest suite and an `evals/` A/B harness in the repo, pushed the week of this sweep. The flagship skill carries one Snyk warning, stated with its code.

### 14. NotebookLM Skill (7,745 combined)

**Source:** [PleasePrompto/notebooklm-skill](https://www.skills.sh/pleaseprompto/notebooklm-skill), 1 indexed listing at 7,745; 7,790 stars; MIT; ARCHIVED since September 2026.

A browser-automation bridge from Claude Code to Google NotebookLM: drive a real Chrome window, ask the notebook's chat, read the answer back with its sources, and repeat until the question is covered. It is also a readable reference implementation of keeping a Google session alive across launches.

Beta tier and archived. The repository is read-only, the author states it may stop working when upstream services change, Socket and Snyk both warn on the listing, and the alternative the README names is archived as well. The guide documents what it does and what it costs, and says plainly that it should not be depended on in production.

## Why This Fire Matters

The catalog had been instructed by its own measurements for fifteen fires: the standing window was exhausted, the boards were fully covered, and every NEW source sat below the floor. That reading was wrong, and the reason was structural. The 20-query window is built around Hermes, agent frameworks and the current design-engineering wave. It cannot see a brokerage publishing market-data skills, a data company publishing a dbt suite, an observability vendor publishing a DQL suite, or a founder publishing business skills, because none of those sources describe themselves with the words the window searches for.

Eleven topic queries returned 146 uncovered sources and 14 converts, 917,944 combined installs, in roughly two minutes of API calls. The largest is a single iOS suite that no Hermes-focused query would ever rank, and the most relevant to this catalog's audience are the ones with no developer angle at all: business operations, brand, sales, and a founder playbook with 10,983 stars.

The other lesson is about floors and multiples. Every one of the 14 was below the floor as a single row read by the sweep. Publisher sizing is what found them, which is now the fourth consecutive fire where the row-to-publisher multiple, not the row, decided the batch.

## Cross-Reference Note

The coverage test excludes per-fire report pages (`!**/marketplace/new-*/**`), so a name stays NEW until a guide exists. The zero-catalog audit walked `catalog/` recursively (740 markdown files) and found 0 of the 46 PARTIAL sources at 100 or more installs without a page. The trending board served 600 entries across 63 sources; 62 are already in the tree and the one that is not, `notfound-404-office/agent-skills`, sizes at 669 on a single listing and stays below the floor.

For the next fire: the extended topic probe is now the productive lane, so widen it rather than repeating the exhausted window. The remaining 132 uncovered sources from this probe all size below 5,000 individually, which is the same multiple trap that hid this batch, so size the low rows before dismissing them.

---

*← [Skills Marketplace](/hermes/skills/marketplace) | [Skills Catalog](/hermes/skills/catalog) →*
*Powered by CorpusIQ*
