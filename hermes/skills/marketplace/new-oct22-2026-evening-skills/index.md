---
title: "New Skills - October 22, 2026 (Evening)"
description: "Skills.sh sweep (Oct 22 evening): 101 new skills, five publisher clusters from 136.7K to 14.9K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-oct22-2026-evening-skills/"
robots: "index,follow"
last_updated: "2026-10-22"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - October 22, 2026 Evening Sweep

Evening sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog. The same 20-query window (15 Hermes-focused plus the 5-query generic pass) served 887 unique skills with 0 failed queries: 101 NEW, 272 PARTIAL.

None of the five clusters converted here appeared in the NEW lane at all. The window's largest new row was gogf/skills at 3,250 installs, 65 percent of the guide floor, and every conversion came from the two boards instead: the trending board (32 entries, 22 sources) and the popular board (96 entries). Between them they surfaced 95 sources, 68 of which had no catalog page, and five of those were publisher clusters rather than single skills.

That is the pattern worth carrying forward. A board row is one skill; the publisher behind it can be ten to forty times larger. softaworks/agent-toolkit showed 4,011 installs on the popular board and sizes at 136,734 across 44 listings, a factor of 34. mvanhorn/cli-printing-press showed 3,717 and sizes at 62,315, a factor of 17. mapbox/mapbox-agent-skills showed 2,585 and sizes at 33,869. ScrapeCreators/social-media-research-skills showed 1,271 and sizes at 15,374. hoodini/ai-agents-skills showed 3,220 and sizes at 14,854. Together: 136 indexed listings and 263,146 combined installs.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills collected | 887 (0 failed queries) |
| NEW (not in catalog) | 101 |
| PARTIAL (source known, skill not cataloged) | 272 |
| New publisher guides | 5 (136 indexed listings, 263,146 combined installs) |
| Above-floor finds rejected | 0 |
| Zero-catalog audit | 169 sources at 100+; 0 uncovered in catalog/ recursive (721 markdown files); 0 converts |
| Boards | Trending 32 entries / 22 sources; popular 96 entries; 95 sources combined, 68 uncovered |
| Marketplace count | 1,141+ to 1,146+ |

## New Publisher Guides

### 1. Agent Toolkit (136,734 combined)

**Source:** [softaworks/agent-toolkit](https://www.skills.sh/softaworks/agent-toolkit), 44 indexed listings, top skill `mermaid-diagrams` at 5,109; 2,587 stars; MIT; pushed 2026-03-05.

The largest cluster of the fire and the broadest: 44 skills over documentation, planning, professional communication, React, git hygiene and agent self-management. The skills that matter for an agent setup are the meta ones, `agent-md-refactor` for splitting a bloated AGENTS.md into progressive disclosure, `session-handoff` for writing context before compression, and `skill-judge` for scoring a skill against the same specification the repo follows.

The tier is Production with one caveat carried in the guide's security section: `qa-test-planner` takes a MEDIUM warning from both Socket and Gen Agent Trust Hub for an `eval` pattern in two helper scripts, which is a flag on executable code rather than on the instructions. One indexed listing, `lessons-learned` at 1 install, has no SKILL.md in the current tree.

-> [Setup guide](/hermes/skills/catalog/agent-toolkit-setup)

### 2. CLI Printing Press (62,315 combined)

**Source:** [mvanhorn/cli-printing-press](https://www.skills.sh/mvanhorn/cli-printing-press), 20 indexed listings, top skill `printing-press` at 7,508; 4,847 stars; MIT; pushed 2026-10-22.

A research and generation suite that turns any API into a Go CLI designed for agents, then ships the matching agent skill and MCP server in the same run. Ten skills carry almost all of the installs and they describe one pipeline: press, polish, score, output-review, amend, reprint, import, publish, catalog, retro.

This is the most actively developed repo of the fire, pushed the same day as this snapshot, and the tier is Beta on verdicts rather than on activity: Socket and Snyk both return Warn on the research and publish skills, with W011 third-party content exposure and W009 direct money access on the publish path.

-> [Setup guide](/hermes/skills/catalog/cli-printing-press-setup)

### 3. Mapbox Agent Skills (33,869 combined)

**Source:** [mapbox/mapbox-agent-skills](https://www.skills.sh/mapbox/mapbox-agent-skills), 20 indexed listings, top skill `mapbox-web-integration-patterns` at 2,585; 82 stars; MIT; pushed 2026-10-01.

The official Mapbox skill library, and the first location and mapping suite in this catalog. Twenty listings against exactly twenty skill directories: web integration for React, Vue, Svelte and Angular, iOS, Android and Flutter patterns, cartography, style quality, search, store locators, navigation, token security, and two MCP integrations.

The star count is low at 82 because the repo is young, and the install base and the auditor results are the better signal: every sampled skill passes Gen Agent Trust Hub, Socket and Snyk. The two MCP skills are where a Hermes agent gets the most direct value, since they describe wiring Mapbox tools into agent runtimes and composing them into cited answers.

-> [Setup guide](/hermes/skills/catalog/mapbox-agent-skills-setup)

### 4. ScrapeCreators Social Research Skills (15,374 combined)

**Source:** [ScrapeCreators/social-media-research-skills](https://www.skills.sh/ScrapeCreators/social-media-research-skills), 13 indexed listings, top skill `trend-discovery` at 1,271; 4,538 stars; MIT; pushed 2026-08-26.

Thirteen skills that each answer a business question about public social data instead of exposing an endpoint: outlier posts against a creator baseline, comment mining, transcript intelligence, competitor teardowns, ad library teardowns, audience research, product demand research and influencer prospecting. One skill, `scrapecreators-api`, is the data layer across 27+ platforms and the other twelve are workflows that call it.

Every sampled skill carries the same Snyk W011 MEDIUM finding, indirect prompt injection risk, and that is structural rather than a defect in one file: the workflows ingest captions, comments and transcripts written by strangers, and that text reaches the model. The guide keeps the tier at Beta and puts the handling decision with the caller.

-> [Setup guide](/hermes/skills/catalog/scrapecreators-social-research-setup)

### 5. AI Agent Skills (14,854 combined)

**Source:** [hoodini/ai-agents-skills](https://www.skills.sh/hoodini/ai-agents-skills), 39 indexed listings, top skill `github-trending` at 3,220; 290 stars; no LICENSE file; pushed 2026-07-11.

Two collections in one repository. The headline is a 16-skill creative stack installed by a single script (director, design system, decks, short-form video, video edit, two landing-page builders, image generation, Mermaid diagrams, HyperFrames companions), and the long tail is 23 platform and engineering skills covering OWASP security, GitHub trending, MongoDB, Figma, Google Workspace, Bun, LangChain, Vercel, Cloudflare, Railway and AWS.

Three facts decide the tier, which is Beta: there is no LICENSE file at all, the last push is 2026-07-11, and the installer writes outside the project directory into two home-directory skill paths. `google-workspace-cli` is the highest-privilege skill in the set, since it reaches Drive, Gmail, Calendar and Admin surfaces through OAuth.

-> [Setup guide](/hermes/skills/catalog/ai-agents-skills-setup)

## Above-Floor Rejections

None this fire. The standing rejection [cyxzdev/uncodixfy](https://www.skills.sh/cyxzdev/uncodixfy) (5,589 installs, Snyk CRITICAL E004 prompt injection) is still NEW in the window and still excluded, and [404kidwiz/claude-supercode-skills](https://www.skills.sh/404kidwiz/claude-supercode-skills) remains an unreachable repository behind 20,036 indexed installs.

## Zero-Catalog Audit

169 PARTIAL sources sit at 100 or more combined installs, audited against `catalog/` recursively (721 markdown files, full `owner/repo` match then exact owner token). 0 carry no catalog page, so this audit produced no converts and the conversion queue stays empty.

[gogf/skills](https://www.skills.sh/gogf/skills) moved from 3,246 to 3,250 combined, still below the floor at 65 percent of it and carried since October 19. It is the only NEW source this fire with a row above 3,000 installs that is not a conversion.

## Boards

The trending board served 32 entries across 22 sources again, the same small window as the morning fire, so it is a sample rather than a census. The popular board served 96 entries. The two boards together surfaced 95 sources and 68 of them had no catalog page.

None of the five converts cleared the floor as a single board row: the boards saw softaworks/agent-toolkit at 4,011, mvanhorn/cli-printing-press at 3,717, hoodini/ai-agents-skills at 3,220, mapbox/mapbox-agent-skills at 2,585 and ScrapeCreators/social-media-research-skills at 1,271. The publisher query is what turned five below-floor rows into 263,146 combined installs. The rule the morning fire added held, and this fire extends it to the popular board as well as trending: run the publisher query on every uncovered board source, not only on the ones that look like organizations.

The remaining uncovered board sources all sit below the floor as publishers, led by vikiboss/60s-skills (3,703 combined across 7 listings) and nashsu/autocli-skill (2,943 across 2).

## Cross-Reference Note

The coverage test excludes per-fire report pages (`!**/marketplace/new-*/**`), so a reported name stays NEW until a guide exists. The NEW count moved from 103 to 101 between the morning and evening fires and PARTIAL moved from 271 to 272 on the same 887-skill set, which is the expected drift when two names gain a catalog mention.

---

*← [Skills Marketplace](/hermes/skills/marketplace) | [Skills Catalog](/hermes/skills/catalog) →*
*Powered by CorpusIQ*
