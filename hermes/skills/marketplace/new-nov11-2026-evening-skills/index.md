---
title: "New Skills - November 11, 2026 Evening"
description: "Skills.sh sweep (Nov 11 evening): 7 publisher guides for 53,540 combined installs across 88 indexed listings"
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-nov11-2026-evening-skills/"
robots: "index,follow"
last_updated: "2026-11-11"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - November 11, 2026 Evening Sweep

Sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog. The standing 20-query window returned 884 unique skills across 0 failed queries: 82 NEW rows and 249 PARTIAL, with the top NEW row unchanged from the morning fire at 339 installs. That is the forty-eighth consecutive silent window, and the standing board is now providing no new signal at all.

No queue carried over from the morning, so this fire probed. Seventy-two generic queries ran at the 2.7-second pacing the API requires, returning 5,254 rows across 1,294 distinct sources with zero failed queries. The queries were deliberately weighted toward business processes rather than frameworks, because the morning note observed that vertical terms mostly rediscover publishers already in the catalog: sales, marketing, analytics, legal, recruiting, support, e-commerce, finance, plus writing, research, design and engineering-quality lanes.

Cross-referencing the 1,294 sources against the docs tree left 548 uncovered, of which 11 sit above 3,000 combined installs, 27 above 2,000 and 70 above 1,000. That is a better ratio than the morning domain probe produced (2 above 3,000 from 1,745 sources) and supports the morning note's conclusion: the mass is in generic business-process territory, not in verticals.

Forty-one candidates were sized from their own source pages rather than from the probe rows. Eighteen changed by more than 50 percent once sized, and eleven changed by a factor of three or more. The largest distortions were the ones that mattered: `gasserane/personal-skills` read 684 in its probe row and sizes to 22,148 across 52 listings, `brianrwagner/ai-marketing-claude-code-skills` read 495 and sizes to 10,449, and `microsoft/aspire-skills` read 1,607 and sizes to 8,474. A probe row remains a sample of one listing's traffic, never the family size.

Selection this fire was not a pure install floor, because the uncovered mass sits between 4,000 and 8,500. The rule was: sized at 4,000 combined or above, plus a quality signal (an official or vendor publisher, an active release within the last quarter, a multi-skill family), minus anything held on a measured property. Seven sources cleared it.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills (standing 20-query window) | 884 (0 failed queries) |
| NEW (not in catalog) | 82 rows |
| PARTIAL (source known, skill not cataloged) | 249 |
| Above-floor finds in the standing window | 0 (top row 339) |
| Fresh topic probe | 72 queries, 5,254 rows, 1,294 sources, 0 failed |
| Uncovered sources from the probe | 548 |
| Uncovered above 3,000 combined | 11 |
| Candidates sized from source | 41 |
| Changed by more than 50 percent once sized | 18 |
| Held, excluded or duplicate | 6 |
| Guides published this fire | 7 |
| Combined installs documented | 53,540 |
| Indexed listings covered | 88 |
| Tier mix | 0 Green, 7 Yellow |

## New Setup Guides

- [Microsoft Aspire Skills - .NET AppHost Agent Setup](/hermes/skills/catalog/aspire-skills-setup) - microsoft/aspire-skills, 8,474 combined, 8 listings, 94 stars, MIT, .NET distributed apps: AppHost routing, local orchestration, telemetry reads, publish and deploy targets, terminal automation and a Project v2 migration path
- [AI Marketing Skills - 24-Skill Operator Toolkit](/hermes/skills/catalog/ai-marketing-claude-code-skills-setup) - BrianRWagner/ai-marketing-claude-code-skills, 10,449 combined, 24 listings, 455 stars, no LICENSE file, Marketing operations: positioning, cold outreach, content systems, de-AI rewriting, LinkedIn and X voice and an AI search visibility audit
- [Baoyu Design - Local Artifact Editors for Agents](/hermes/skills/catalog/baoyu-design-setup) - jimliu/baoyu-design, 16,167 combined, 10 listings, 6,382 stars, NOASSERTION, Design artifacts: local slide decks, design canvases and systems, data dashboards, chart guidance, motion films and whiteboards, each opened in its own editor
- [Code Review Skill - 20+ Language Review Guides](/hermes/skills/catalog/code-review-skill-setup) - awesome-skills/code-review-skill, 5,093 combined, 2 listings, 2,249 stars, MIT, Engineering quality: a four-phase review process over 21,000 lines of per-language guidance with six severity labels and security checklists
- [YouTube Clipper - AI Chaptering and Bilingual Cuts](/hermes/skills/catalog/youtube-clipper-skill-setup) - op7418/youtube-clipper-skill, 4,415 combined, 1 listing, 2,307 stars, MIT, Video repurposing: semantic chapter detection, frame-accurate cuts, batch bilingual subtitles burned into the video and platform copy
- [Tinybird Agent Skills - Analytics Platform Setup](/hermes/skills/catalog/tinybird-agent-skills-setup) - tinybirdco/tinybird-agent-skills, 4,743 combined, 4 listings, 21 stars, no LICENSE file, Real-time analytics: 18 project rules for datasources, pipes and endpoints, the tb CLI surface and the TypeScript and Python SDKs
- [Apify Awesome Skills - Lead and Market Intelligence](/hermes/skills/catalog/apify-awesome-skills-setup) - apify/awesome-skills, 4,199 combined, 39 listings, 294 stars, Apache-2.0, Market and lead intelligence: e-commerce pricing, verified email lists, ad research, AI answer visibility tracking, jobs and OSINT

## Held, with the reason measured

- **gasserane/personal-skills** (22,148 across 52 listings, 3 stars): no LICENSE file and no public signal. Standing hold since the Nov 11 morning fire, and still the largest figure in the probe.
- **manaflow-ai/cmux-skills** (6,373 across 12 listings): same publisher and same subject as the existing `manaflow-ai/cmux` guide already in the catalog. A second page would document a renamed sibling of a documented family.
- **workos/skills** (4,824 across 45 listings, 46 stars, MIT): 45 indexed listings against 3 `SKILL.md` files in the tree, a 15x drift ratio, and 40 of those listings carry no description at all. Index shape rather than size, the same disposition as the earlier workos review.
- **diodeinc/pcb** (8,562 across 12 listings, 501 stars): twelve listings against five `SKILL.md` files on a tree that is mostly application code. Held for the second fire running pending an explanation of the drift.
- **colosseumorg/colosseum-copilot** (4,476 across 1 listing): a single skill for Solana program work. A legitimate niche, but one skill is a note rather than a guide.
- **404kidwiz/claude-supercode-skills**: the standing dangling-publisher check. GitHub still returns 404 for the repository while skills.sh serves its listings.

## New pitfalls found this fire

- **The HTTP client decides whether a probe finishes.** The first probe used Python's `urllib` against the same search endpoint and averaged about 60 seconds per query, which would have turned a five-minute sweep into an hour; the identical queries through `curl` averaged one second. Nothing about the endpoint changed, only the client. Time the first three queries before committing to a 72-query plan.
- **The search API carries no verdicts and no repository metadata.** `/api/search` returns only `id`, `source`, `skillId`, `name` and `installs`. First-seen dates, stars and the three audit verdicts live on the skill page HTML, which means a manifest built from the search API alone cannot fill the Security table and a second fetch per source is mandatory.
- **A vendor can publish under a name that does not exist in its own tree.** Tinybird indexes the core skill as `tinybird` while the directory and the README both call it `tinybird-best-practices`. An installer that matches on the listing name finds nothing, and a guide that quotes the listing name as the folder is wrong.
- **A flagship listing can outlive its directory.** `baoyu-design` still carries 6,972 installs but the skill now lives in `archive/`, superseded by the per-artifact skills. An install index measures what people installed, not what the repository currently ships.

## Next fire

The uncovered band between 4,000 and 8,500 is now drained of everything with a clean property set, so the queue below is where the next fire should look, sized from source before anything is drafted:

- `boristane/agent-skills` (4,962 across 1 listing) and `streamlit/agent-skills` (3,614 across 19) are the two largest single-skill and framework finds left.
- `lawve-ai/awesome-legal-skills` (4,370 across 96 listings, 945 stars) carries 281 `SKILL.md` files, so the index is capped rather than drifted. Legal operations has no guide in the catalog.
- `microsoft/dataverse-skills` (3,100 across 11) is a second Microsoft first-party pack.
- `wispbit-ai/skills` (3,579 across 5), `geoffjay/claude-plugins` (3,514 across 25), `vikiboss/60s-skills` (3,741 across 7), `zlanqing/codex-claude-academic-skills` (3,257 across 24) and `dexhunter/seedance2-skill` (3,559 across 2) all size above 3,000 with a clean shape.
- The next probe should keep at least one generic business-process lane. This fire's generic lanes produced a third of the uncovered mass and a better ratio than the vertical probe that preceded it.

Every guide was built from a pre-verified manifest holding the exact per-listing install figure for every indexed skill, the repository metadata, the real skill layout read from the GitHub tree, and the live security verdicts from skills.sh. Each draft was then checked with three gates: the format gate, the pack cross-check at a per-guide threshold and the frontmatter audit.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
