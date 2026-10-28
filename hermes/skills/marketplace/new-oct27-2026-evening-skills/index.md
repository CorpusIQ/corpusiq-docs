---
title: "New Skills - October 27, 2026 Evening"
description: "Skills.sh sweep (Oct 27 evening): 886 skills scanned, 9 queued publisher clusters shipped for 182,360 combined installs across 575 listings."
canonical: "https://www.corpusiq.io/docs/hermes/marketplace/new-oct27-2026-evening-skills/"
robots: "index,follow"
last_updated: "2026-10-27"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - October 27, 2026 Evening Sweep

Sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog. The standing 20-query window returned 886 unique skills with 0 failed queries: 90 NEW, 268 PARTIAL.

It was the eighteenth consecutive fire with nothing new above the 1,000-install trigger in the standing window. Its top row was `dannyjpwilliams/ui-sound-design-skill` at 357 installs, and every NEW source with a row above 100 was sized by publisher query before it was written off: the largest of those, `melodic-software/claude-code-plugins`, read as a 170-install window row and sized at 5,328 installs across 200 listings, which cleared the floor and became a guide.

The trending board served 600 entries across 66 sources. Sixty-five of the 66 were already in the catalog, and the single uncovered source, `whobot-ai/skills`, sized at 1,134 installs across 2 listings, well under the floor. So the fire drained the queue the morning fire left behind: nine publisher clusters already sized above the 5,000-install floor, all nine documented below.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills collected (standing window) | 886 (0 failed queries) |
| NEW (not in catalog) | 90 |
| PARTIAL (source known, skill not cataloged) | 268 |
| Trending board | 600 entries / 66 sources, 65 covered |
| Above-floor finds in the window | 0 (top row 357) |
| Queued converts documented | 9 |
| New publisher guides | 9 (575 indexed listings, 182,360 combined installs) |
| Marketplace count | 1,187+ to 1,196+ |

## New Publisher Guides

### 1. Capgo Skills (45,408 combined)

**Source:** [cap-go/capgo-skills](https://www.skills.sh/cap-go/capgo-skills), 55 indexed listings, top skill `capacitor-best-practices` at 2,697; 73 stars; MIT; branch main.

Capgo sells the operational half of Capacitor: maintained plugins, cloud native iOS and Android builds, live updates with channels and rollback, and release monitoring. The repository covers that whole lifecycle rather than one library, organized by stage (build, plugins, migrate, upgrade, debug, test, security, publish, live updates) and shipped as 11 plugin groups for the Claude Code, Cursor and Codex marketplaces.

The design worth noticing is the routing layer. `capgo-cli-usage` and `capgo-cloud` are dispatch skills that map the CLI surface and hand off to narrower skills, and most specialists end their description with explicit "do not use for" clauses naming the sibling that should take the request. Version awareness is built in: `capacitor-best-practices` tracks Capacitor 8.5 stable with 9 in alpha, and the upgrade family ships one skill per major step from v4 to v9.

### 2. Mblode Agent Skills (32,370 combined)

**Source:** [mblode/agent-skills](https://www.skills.sh/mblode/agent-skills), 63 indexed listings, top skill `ui-animation` at 10,475; 167 stars; MIT; branch main.

A shipping-oriented suite where one skill carries most of the volume: `ui-animation` alone accounts for a third of the combined installs, and `multi-tenant-architecture`, `ui-design` and `ui-audit` follow a long way behind. The rest is the unglamorous middle of product work: SEO, codebase architecture, planning, pull request review, chat history analysis and CI speedup.

The suite is also honest about its own churn. The repository keeps a `maintenance/retired-names.tsv` that maps old listing names to their replacements (`docs-writing` and `readme-creator` into `ghostwriter`, `optimise-seo` into `seo`, `pr-reviewer` into `tidy`), which is why 63 indexed listings sit against 28 directories in the current tree.

### 3. Ship Shit Dev Skills (27,455 combined)

**Source:** [shipshitdev/skills](https://www.skills.sh/shipshitdev/skills), 150 indexed listings, top skill `financial-operations-expert` at 1,710; 38 stars; no license declared; branch master.

Fourteen command routers (`ship`, `build`, `test`, `deploy`, `review`, `plan`, `research`, `debug`, `optimize`, `document`, `analyze`, `security`, `git`, `task`) that dispatch into a much larger index of named specialist playbooks. The gap between the two is the story: 150 indexed listings against 14 directories in the clone, and a repository-wide history check confirms no commit ever added a directory for any of the 22 highest-traffic indexed names.

Treat this as a router pack plus a catalogue of specialist prompts rather than 150 installable skills. The repository declares no license at its root even though the README and `package.json` both say MIT, so the default position for reuse is all rights reserved until the vendor adds the file.

### 4. Sumsub Agent Skills (24,962 combined)

**Source:** [sumsub/agent-skills](https://www.skills.sh/sumsub/agent-skills), 28 indexed listings, top skill `sumsub-api-auth` at 1,217; 7 stars; no license declared at the repository root; branch main.

The official KYC and AML skill set: applicant and document flows, WebSDK integration, AML screening against sanctions, PEP and adverse-media lists, transaction monitoring, travel rule, and workflow and rule-chain management, one skill per API family. The install band is unusually flat (188 to 1,217), which reads as vendor distribution rather than community triage.

This is the first regulated identity-verification suite in the catalog, and the guide treats it that way. The skills handle applicant personal data, document and selfie images, and screening results, so the security section names the compliance surface explicitly and recommends a sandbox token plus a deliberately narrow scope before anything touches production applicants.

### 5. Qdrant Skills (14,404 combined)

**Source:** [qdrant/skills](https://www.skills.sh/qdrant/skills), 34 indexed listings, top skill `qdrant-search-quality` at 1,793; 265 stars; Apache-2.0; branch main.

The official Qdrant suite, and the first vector-database skill set in the catalog: search quality diagnosis, hybrid search, performance and memory optimisation, multitenancy and tenant scaling, migration, hybrid-cloud setup, and an advisor skill that inspects a deployment before recommending changes. Every directory in the tree maps to an indexed listing with three small tail listings inside them.

The useful property for agents is the target: a self-hosted Qdrant instance needs no cloud account, so a retrieval or memory layer can be stood up without a vendor relationship. The guide keeps that distinction visible, because the same skills also drive Qdrant Cloud with an API key and a cluster endpoint.

### 6. Customware Skills (14,343 combined)

**Source:** [customware-ai/skills](https://www.skills.sh/customware-ai/skills), 17 indexed listings, top skill `domain-context` at 2,550; 2 stars; MIT; branch main.

A low-code builder's own skill set: domain context, task workflow, CRM, CPQ and trades builders, a support widget, HTML-to-app UI conversion and two Playwright skills that drive a live sandbox. Every one of the 17 listings has a directory in the tree.

The constraint is stated plainly in the guide rather than softened: these skills assume the Customware sandbox, its gateway URL and its project-scoped key, and portability to another stack is unproven. Two GitHub stars is the whole community signal. It is still worth reading for the shape of a vendor-authored builder suite, which is an increasingly common pattern.

### 7. Liquid Skills (9,404 combined)

**Source:** [benjaminsehl/liquid-skills](https://www.skills.sh/benjaminsehl/liquid-skills), 3 indexed listings, top skill `shopify-liquid-themes` at 3,672; 121 stars; no license at the repository root; branch main.

Three skills for Shopify theme work: theme structure across `sections/`, `blocks/`, `snippets/`, `layout/`, `templates/`, `assets/` and `locales/`, theme standards for settings and schema, and an accessibility pass. Narrow, and every listing clears 2,800 installs, which is a high floor for three skills.

The guide is explicit that breadth is the trade: three skills is a discipline fragment, not a suite, and there is no deploy step, no CLI and no Admin API token anywhere in the tree. The README's own line counts also drift from the clone, which the guide records instead of smoothing over.

### 8. Claude Code Next.js Skills (8,686 combined)

**Source:** [laguagu/claude-code-nextjs-skills](https://www.skills.sh/laguagu-claude-code-nextjs-skills), 25 indexed listings, top skill `nextjs-seo` at 2,416; 70 stars; MIT; branch main.

A Next.js and TypeScript build pack: Next.js 16 patterns, SEO for the App Router, OpenAI Agents SDK and Vercel AI SDK wiring, AI Elements, shadcn, Supabase Postgres guidance, and a couple of infrastructure skills. The install distribution is concentrated, with two listings carrying more than half the volume and 22 of 25 sitting under 300 installs.

Two operational details matter more than the skill list. `mcp.json` launches `npx -y next-devtools-mcp@latest` over stdio, and `postgres-semantic-search` ships real DDL that creates the vector extension and its tables in whatever database it is pointed at.

### 9. Melodic Claude Code Plugins (5,328 combined)

**Source:** [melodic-software/claude-code-plugins](https://www.skills.sh/melodic-software/claude-code-plugins), 200 indexed listings, top skill `design-thinking` at 259; 28 stars; MIT; branch main.

A broad plugin marketplace rather than a curated skill pack: 91 plugins across 18 categories, 377 skill directories, 29 hook manifests and 1,858 shell scripts. Architecture and documentation, systems engineering, career and business analysis, security, and six formatter plugins that rewrite tracked files on `PostToolBatch`.

This source also produced the fire's sharpest finding. Fifty-nine of the 60 names in the install dump match neither a plugin nor a skill directory in the clone, and the raw path for the top listing returns 404. The install index and the tree do not reconcile, and the guide says so with the probe evidence rather than presenting 200 listings as 200 skills.

## What Was Checked and Rejected

One above-floor source was rejected and one is parked. `senclaw-cdn.italent.cn` carries 31,315 installs across 14 listings (the Beisen HR suite, 1,978 to 2,431 each) but publishes no source tree: no GitHub repository, an HTTP 403 on the host root, no license and no install path to verify. There is nothing to document that a reader could reproduce, so it is recorded here as a rejection rather than converted.

Security verdicts on skills.sh were not sampled this fire. Every guide states that plainly, uses "Not checked" in its auditor table, and instead carries risk observations drawn from the cloned source: which scripts run, which credentials are read, which files or tenants are written. That is the honest form, and it is better than an invented Pass or Warn.

Also worth recording: `melodic-software/claude-code-plugins` was the prior fire's cross-fire watch item at 4,106 installs. It sized at 5,328 this fire and crossed the floor, which is the second time a watch item has converted within two fires.

## Queue for the Next Fire

Four sized clusters remain from the Oct 26 topic probe, all below the 5,000 floor on their best row and each needing a publisher query before dismissal: `latitude-dev/skills`, `peterhdd/agent-skills` (2,298 across 19 listings), `cuellarfr/design-skills` (3,460 across 12) and `soljourner/claude-engineering-skills` (1,550 across 36). Beyond them sit the remaining probed sources from the topic sweep and the standing NEW tail, where the rule holds: a board or window row can understate a publisher by two orders of magnitude, so size before dismissing.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
