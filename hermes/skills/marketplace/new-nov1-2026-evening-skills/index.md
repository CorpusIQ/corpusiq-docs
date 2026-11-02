---
title: "New Skills - November 1, 2026 Evening"
description: "Skills.sh sweep (Nov 1 evening): 8 publisher guides for 47.6K combined installs across 135 indexed listings from the standing queue."
canonical: "https://www.corpusiq.io/docs/hermes/skills/marketplace/new-nov1-2026-evening-skills/"
robots: "index,follow"
last_updated: "2026-11-01"
tags: ["hermes skill", "agent skill", "skills.sh", "sweep", "marketplace", "hermes agent"]
---

# New Skills - November 1, 2026 Evening Sweep

Sweep of [skills.sh](https://skills.sh) for Hermes-relevant agent skills, cross-referenced against the existing catalog. The standing 20-query window returned 885 unique skills with 0 failed queries: 86 NEW, 263 PARTIAL. A 600-row trending board across 67 sources returned two uncovered publishers, both below the 5,000-install floor: vercel-labs/agent-desktop sized at 1,849 across 6 listings, and archify.si, a domain rather than a repository, with no indexable rows. The seven NEW sources carrying a 100+ row all sized under 5,000 on their owner query, peterhdd/agent-skills at 2,477 the largest.

The standing window was silent above the 1,000-install trigger for the twenty-eighth consecutive fire, its top NEW row reading 304 installs, so the fire drained the queue the morning fire left: the eight undocumented sources still above the 5,000-install floor. That empties the queue, so the next fire probes for new clusters rather than converting stored ones.

Every guide was built from a pre-verified pack holding the exact per-listing install figures, a depth-1 clone with its branch, licence and skill directories, and three-auditor verdicts sampled across each index. Each draft was then checked with three gates: the format gate, the pack cross-check at a per-guide threshold and the frontmatter audit. All 24 gate runs passed on the orchestrator re-run after an md5 comparison of the three canonical scripts. Two guides were re-tiered from Green to Yellow after the mechanical derivation caught a Warn in their sampled verdicts.

## Sweep Summary

| Metric | Value |
|---|---|
| Unique skills (standing 20-query window) | 885 (0 failed queries) |
| NEW (not in catalog) | 86 |
| PARTIAL (source known, skill not cataloged) | 263 |
| Above-floor finds in the standing window | 0 (top row 304) |
| Uncovered publishers on the trending board | 2 (1,849 and 0 installs) |
| Undocumented above-floor sources in the queue | 8 |
| Guides published this fire | 8 |
| Combined installs documented | 47,624 |
| Indexed listings covered | 135 |

## New Setup Guides

- [Video Agent Skills - Video Production for Agents](/hermes/skills/catalog/video-agent-skills-setup) - melvynx/video-agent-skills, 7,837 combined, 24 listings, 86 stars, MIT, thirteen Claude Code skills for short-form video from script to publish: a week of scripts with hooks scored from 22 formulas, hook and outlier research, an editing skill shipping its own Node and ffmpeg render engine, voice-cloned translation and publishing, with two Gen Agent Trust Hub FAILs and a Snyk Warn in the sampled set
- [News Aggregator Skill - Multi-Source News Digest](/hermes/skills/catalog/news-aggregator-skill-setup) - cclank/news-aggregator-skill, 6,015 combined, 1 listing, 1,317 stars, no LICENSE file, one Python skill over 44+ RSS and community sources with OPML extension, Playwright deep fetch and Chinese briefing presets, where scripts/rss_parser.py fetches with TLS verification disabled and the Snyk Warn sits on the only listing
- [LlamaParse Skills - Document Parsing for Agents](/hermes/skills/catalog/llamaparse-agent-skills-setup) - run-llama/llamaparse-agent-skills, 5,979 combined, 4 listings, 85 stars, MIT, three LlamaIndex skills split by where parsing runs: local liteparse with no key, cloud LlamaParse behind LLAMA_CLOUD_API_KEY and agentic retrieval over a LlamaCloud Index v2, three directories against four listings with the fourth named as an index-only row
- [Vue Ecosystem Skills - Version-Aware Vue Context](/hermes/skills/catalog/vue-ecosystem-skills-setup) - skilld-dev/vue-ecosystem-skills, 5,930 combined, 35 listings, 184 stars, MIT, version-aware Vue ecosystem context rebuilt from each published package: Vue 3.6, Pinia, Vue Router, Reka UI, VueUse, Vuetify and TanStack, 20 rows at or above 104 installs, three directories unreachable by the plugin route and every sampled verdict a Pass
- [LLM Code Skills - Cross-Tool Documentation Pack](/hermes/skills/catalog/llm-code-setup) - itechmeat/llm-code, 5,960 combined, 49 listings, 24 stars, MIT, documentation-based skills that work across Copilot, Claude and Cursor from one agentskills.io folder: Vite, FastAPI, Bun, Mantine, Vitest, Kubernetes and more, 38 directories against 49 listings with 11 indexed names carrying no directory and three Snyk Warns in the sample
- [Qodo Skills - Code Review and Standards Suite](/hermes/skills/catalog/qodo-skills-setup) - qodo-ai/qodo-skills, 5,429 combined, 10 listings, 59 stars, MIT, the Qodo local review workflow as provider-neutral skills: setup, codebase wisdom, local review, PR review resolution and an opt-in standards package, 35 SKILL.md directories that are seven canonical skills plus four generated provider projections, Snyk Warns on the review and rules listings
- [Web AI Agent Skills - Browser AI APIs and WebMCP](/hermes/skills/catalog/web-ai-agent-skills-setup) - webmaxru/web-ai-agent-skills, 5,317 combined, 11 listings, 53 stars, no LICENSE file, browser AI APIs as skills: Prompt API, Language Detector, Translator, Writing Assistance, Proofreader, WebMCP and WebNN, each with a per-Chrome-milestone compatibility reference and a deterministic target scanner, four of the eleven listings being repository-maintenance skills
- [Tushare Finance Skill - China Market Data for Agents](/hermes/skills/catalog/tushare-finance-skill-setup) - stanleychanh/tushare-finance-skill-for-claude-code, 5,157 combined, 1 listing, 79 stars, MIT, master branch, one skill wrapping 220+ Tushare Pro interfaces for A-share, Hong Kong and US equities, funds, futures, bonds and macro data behind a TUSHARE_TOKEN, with a Socket FAIL on the single listing and a README that claims Apache-2.0 where the LICENSE file says MIT

## Verification

Every guide carries its exact per-listing install figures, a snapshot line with the verified date and the sampled skills.sh verdicts. Re-check the security pages on skills.sh before production use: install counts and verdicts drift.

## Related

- [Skills Catalog](/hermes/skills/catalog)
- [Skills Marketplace](/hermes/skills/marketplace)
- [November 1, 2026 Morning Sweep](/hermes/skills/marketplace/new-nov1-2026-morning-skills)

---

*[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)*
*Powered by CorpusIQ*
