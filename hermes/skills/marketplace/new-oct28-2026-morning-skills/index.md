---
title: "New Skills - October 28, 2026 Morning"
description: "Skills.sh sweep (Oct 28 morning): 886 skills scanned, 43-query topic probe, 9 new publisher guides for 1,647,487 combined installs across 386 listings."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-oct28-2026-morning-skills/"
robots: "index,follow"
last_updated: "2026-10-28"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - October 28, 2026 Morning Sweep

Sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog. The standing 20-query window returned 886 unique skills with 0 failed queries: 89 NEW, 269 PARTIAL.

This fire changed lanes. The standing window produced nothing above the 1,000-install trigger for the nineteenth consecutive fire - its top row was `dannyjpwilliams/ui-sound-design-skill` at 357 installs - and the trending board served 600 entries across 66 sources with 65 already covered, the one exception being `whobot-ai/skills` at 1,134 installs across 2 listings, under the floor.

So the fire ran a widened topic probe instead: 43 business and engineering queries against the skills.sh search API, 2,057 unique sources, 0 failed queries, 1,710 with no page in the catalog. Thirty-one of those sources cleared the 5,000-install floor once sized by publisher query. Nine are documented below for **1,647,487 combined installs across 386 indexed listings**, the largest single batch by install weight in this catalog's record.

Every NEW source with a row above 100 installs was also sized individually before being written off. The largest was `cuellarfr/design-skills` at 3,462 installs across 12 listings, 69 percent of the floor; `chadboyda/agent-gtm-skills` (2,752), `peterhdd/agent-skills` (2,317) and `soljourner/claude-engineering-skills` (1,550) followed. None cleared.

A separate catalog audit walked `catalog/` recursively (776 markdown files) and checked all 46 sources carrying an indexed listing at 100 or more installs: every one already has a catalog page, so there is no undocumented above-floor source hiding in the PARTIAL set.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills collected (standing window) | 886 (0 failed queries) |
| NEW (not in catalog) | 89 |
| PARTIAL (source known, skill not cataloged) | 269 |
| Trending board | 600 entries / 66 sources, 65 covered |
| Above-floor finds in the standing window | 0 (top row 357) |
| Widened topic probe | 43 queries, 2,057 unique sources, 1,710 uncovered |
| Above-floor uncovered sources | 31 |
| New publisher guides | 9 (386 indexed listings, 1,647,487 combined installs) |
| Marketplace count | 1,196+ to 1,205+ |

## New Publisher Guides

### 1. Developer Kit (408,740 combined)

**Source:** [giuseppe-trisciuoglio/developer-kit](https://www.skills.sh/giuseppe-trisciuoglio/developer-kit), 130 indexed listings, top skill `shadcn-ui` at 22,376; 365 stars; MIT; branch main; 119 `SKILL.md` directories across 11 plugin groups.

A modular plugin marketplace for Claude Code and agentic CLIs covering the daily work of a full-stack engineer: Spring Boot, Java, Angular, React, Next.js, NestJS, Tailwind, Drizzle, AWS and a block of unit-test skills. It is the second-largest batch entry by installs and the widest by surface count in this fire.

The install index outruns the tree: 14 indexed names, `knowledge-graph` among them, have no directory anywhere in the clone, which reads as a spec and project family from an earlier layout. The guide states that with the counts rather than presenting 130 listings as 130 installable skills.

### 2. BMad Method Skills (383,849 combined)

**Source:** [bmad-code-org/bmad-method](https://www.skills.sh/bmad-code-org/bmad-method), 81 indexed listings, top skill `bmad` at 13,809; 54,667 stars; MIT licence file (GitHub reports the license field as NOASSERTION); branch main.

The Breakthrough Method for Agile AI Driven Development, packaged as 28 workflow skills plus three retired-name records: brainstorm, PRD, architecture, stories, implementation, review and a party-mode session where several agent personas argue a decision. It is the largest-starred entry of this fire and the only agile process framework the catalog carries.

Three indexed names (`bmad-spec`, `bmad-correct-course`, `bmad-ticket`) have no directory in the current tree and were grounded from the repository's own retired-name records and changelog, each stated as such in the guide.

### 3. PStack Skills (300,310 combined)

**Source:** [backnotprop/pstack](https://www.skills.sh/backnotprop/pstack), 61 indexed listings, top skill `unslop` at 7,021; 3,030 stars; MIT; branch main.

Engineering discipline as installed behaviour: 24 principle skills (`principle-fix-root-causes`, `principle-measure-before-guessing`), 23 playbooks, and task skills such as `unslop`, `interrogate`, `how`, `why` and `technical-writing`. 57 of the 58 `skills/` directories set `disable-model-invocation: true`, so the skills are invoked deliberately rather than auto-selected, which is a design choice worth copying.

### 4. PixiJS Skills (151,735 combined)

**Source:** [pixijs/pixijs-skills](https://www.skills.sh/pixijs/pixijs-skills), 26 indexed listings, top skill `pixijs` at 6,929; 358 stars; MIT; branch main.

The official PixiJS suite for 2D WebGL and WebGPU rendering: application bootstrap, scene graph and graphics, assets, performance, text, filters, particles, sound, accessibility and project scaffolding. Every one of the 26 indexed listings has a matching directory, which is unusual in this fire.

### 5. MSW AI Coding Plugins (119,426 combined)

**Source:** [msw-git/msw-ai-coding-plugins-official](https://www.skills.sh/msw-git/msw-ai-coding-plugins-official), 18 indexed listings, top skill `msw-general` at 9,989; 38 stars; no LICENSE file in the repository; branch main.

MapleStory Worlds (Nexon's sandbox game platform) as a skill suite, in Korean: scripting, avatars, combat systems, UI kits and search over the platform documentation. Four of the 18 indexed names have no directory in the current tree, and the guide says so with the exact counts.

### 6. ClickHouse Agent Skills (83,246 combined)

**Source:** [clickhouse/agent-skills](https://www.skills.sh/clickhouse/agent-skills), 11 indexed listings, top skill `clickhouse-best-practices` at 21,833; 561 stars; Apache-2.0; branch main.

The official ClickHouse suite: schema and query best practices, an architecture advisor, `chdb` embedded analytics, JavaScript client patterns, managed Postgres root-cause analysis and CLI-based local and cloud deployment. All 11 listings have directories. Snyk fails `clickhouse-managed-postgres-rca`, which the guide records with the code rather than summarizing away.

### 7. PriceWin Skills (68,400 combined)

**Source:** [price-win/pricewin-skills-hub](https://www.skills.sh/price-win/pricewin-skills-hub), 6 indexed listings, top skill `pricewin-hotel-deal-finder` at 19,455; 2 stars; MIT-0; branch main.

Six travel-commerce skills for hotel and flight price comparison across Agoda, Booking and other OTA sources, plus a booking assistant and a deal finder. Small repository, heavy distribution, and the weakest security profile of the batch: two Snyk fails (`pricewin-flight-search` with E005, E006 and W013; `pricewin-booking-assistant` with W007, W009 and W011) and two Gen Agent Trust Hub warnings. The guide leads with that instead of the install count.

### 8. 365 Skills (67,542 combined)

**Source:** [agents365-ai/365-skills](https://www.skills.sh/agents365-ai/365-skills), 40 indexed listings, top skill `drawio-skill` at 9,009; 97 stars; no LICENSE file at the root; branch main.

A daily-use suite built around visual artifacts and research: `drawio-skill`, `excalidraw`, `creating-mermaid-diagrams`, `plantuml-skill`, `tldraw-skill`, `paper-fetch`, video and podcast production, Obsidian, Zotero and tmux tooling. Licensing is mixed: 31 manifests declare MIT while three skills ship CC BY-NC 4.0, and the guide carries that in four places.

### 9. OpenSEO (64,239 combined)

**Source:** [every-app/open-seo](https://www.skills.sh/every-app/open-seo), 13 indexed listings, top skill `keyword-research` at 6,874; 25,425 stars; MIT; branch main.

An open source alternative to Semrush and Ahrefs, shipped as three layers rather than a skill folder: the self-hosted application (Docker or your own Cloudflare account, billed through your own DataForSEO key), an MCP server at `https://app.openseo.so/mcp`, and 12 workflow skills for project setup, keyword research, clustering, competitive landscape, competitor analysis, local SEO, link prospecting, site audit, AI prompt research, AI visibility and report writing.

The tree carries 39 `SKILL.md` directories against 13 indexed listings; the difference is duplicate copies plus 14 repository-maintenance skills that skills.sh does not index. Three sampled skills carry a Snyk W011 warning.

## Queue for the Next Fire

Twenty-two sources from this fire's topic probe already carry a publisher-sized combined total above the 5,000-install floor and are waiting for guides: `pilioai/skills` (64,041), `qianwen-ai/qianwen-ai` (56,010), `kadajett/agent-nestjs-skills` (30,632), `ejirocodes/agent-skills` (18,671), `pluginagentmarketplace/custom-plugin-java` (17,531), `halthelobster/proactive-agent` (15,164), `tw93/kami` (13,390), `citrolabs/ego-lite` (13,062), `referodesign/refero_skill` (12,121), `igorwarzocha/opencode-workflows` (12,006), `fallow-rs/fallow-skills` (10,833), `composiohq/composio` (10,435), `teng-lin/notebooklm-py` (9,961), `tanis90/pdf-converter-mineru` (9,612), `leonxlnx/unlazy` (9,556), `paymog/groundcover-cli` (9,354), `paymog/incidentio-cli` (9,066), `elestio/elestio-skill` (7,445), `lackeyjb/playwright-skill` (7,005), `kunchenguid/chrome-devtools-axi` (6,948), `agents365-ai/drawio-skill` (6,492) and `nick-vels/skills` (5,462).

The 1,710 uncovered sources from the probe that did not clear the floor stay on the list for a publisher query before dismissal, since a single board-style row has understated a publisher by as much as 652x in this catalog's history.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
