---
title: "Moonlight Lupin Agent Skills - Hermes Skill Suite Setup"
description: "Setup guide for moonlight-lupin/agent-skills: 35 Hermes-native skills across research, agent-ops, productivity, creative. 88-star MIT repo, ~3.4K installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/moonlight-lupin-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-04"
tags: ["hermes skill", "agent skill", "skill setup", "hermes agent", "skill suite", "research"]
---

# Moonlight Lupin Agent Skills - Setup Guide

**Source:** [moonlight-lupin/agent-skills](https://github.com/moonlight-lupin/agent-skills) (88⭐, 15 forks, MIT LICENSE; actively maintained)
**Skill family:** `moonlight-lupin/agent-skills` (36 SKILL.md files in-repo - 35 installable skills + 1 test fixture; 37 indexed listings)
**Combined Installs:** ~3,354 across indexed listings (Oct 4, 2026 snapshot)
**Category:** Hermes Agent Ecosystem / Skill Suite
**Quality Tier:** 🟡 Beta (CI-tested, versioned skills from a single maintainer; community validation still forming - verified Oct 4, 2026)

A collection of 35 AI agent skills built specifically for Hermes Agent, organised by domain: research, agent-ops, productivity, creative, mlops, devops, and web-scraping, plus two installable plugins (skill-retrieval and lumen). The suite covers the full agent lifecycle: onboarding a customer onto Hermes (hermes-onboarding), auditing token spend (input-token-analysis, input-token-overheads), running source-grounded research (deep-research, fact-checker, source-tracker), and packaging the output (marp-deck, clips-studio). Parked on the Sep 29, 2026 sweep as sub-500 and un-parked Oct 4, 2026 after a growth re-check.

---

## Installation

```bash
# Full suite (all 35 skills)
npx skills add moonlight-lupin/agent-skills

# Or install a single skill
npx skills add moonlight-lupin/agent-skills --skill deep-research
```

The repo also ships two installable Hermes plugins under `plugins/`; the README documents installing them from the plugin catalog or by copying/symlinking into your profile's `plugins/` directory:

```bash
hermes plugins install skill-retrieval
```

## Roster - All 35 Skills

| Skill | Domain | Installs | What It Does |
|---|---|---|---|
| deep-research | research | 119 | Iterative research engine: structured evidence, source-quality ranking, refute queries, deterministic validation gates |
| fact-checker | research | 114 | Claim verification with confidence ratings and cited reports |
| website-scraping | web-scraping | 112 | Recon to lightest-tool extraction to JSONL with run manifest |
| disk-cleanup | devops | 110 | Disk triage: survey mounts, safe/ask buckets, execute approved set, verify delta |
| log-analyzer | agent-ops | 107 | Log pattern detection: error clusters, rate limits, timeouts, tool failures |
| file-organizer | productivity | 107 | LLM-powered directory organizer: scan, propose, confirm, chunked moves |
| source-tracker | research | 106 | Persistent citation database: dedup, topic tags, link health, bibliography export |
| skill-maintainer | agent-ops | 106 | Skill library maintenance: author, curate, upstream drift tracking, publish |
| pexels-stock-photos | creative | 106 | Free real-world stock photos via Pexels API with attribution handling |
| news-monitoring | research | 104 | Recurring news digests with cron delivery, dedup, and multi-language output |
| youtube-topic-research | research | 104 | YouTube search, transcript, and summary pipeline |
| decision-log | productivity | 103 | ADR-style decision journal with superseding chains and cron reviews |
| task-brief | productivity | 103 | Goal/context/constraints brief compiled and confirmed before substantial tasks |
| model-compare | mlops | 103 | Blind multi-model A/B comparison plus embedding benchmark |
| entity-research | research | 103 | Cited company/person dossiers: ownership, adverse media, sanctions, litigation |
| endpoint-probe | research | 103 | API/MCP surface discovery across REST, GraphQL, SOAP, and JSON-RPC |
| claude-plugin-converter | agent-ops | 103 | Convert Claude Code plugins into self-contained Hermes plugins |
| scheduled-summary | productivity | 102 | Cron-driven cross-session digests for messaging platforms |
| media-analyzer | research | 102 | Rhetorical technique detection: loaded language, framing, omission |
| travel-itinerary | productivity | 101 | Business-trip itineraries from emails/PDFs to Markdown + .ics + chat variants |
| people-enrichment | research | 101 | Person/company enrichment via PDL, exported to styled .xlsx |
| notebooklm-mode | research | 101 | Source-grounded Q&A from a source vault (strict or augmented grounding) |
| hermes-onboarding | agent-ops | 101 | 21-step customer onboarding: gateway, dashboard, memory, search, guardrails, crons |
| clips-studio | creative | 101 | Staged fal.ai short-video generation: text-to-video, animate still, camera moves |
| fill-template | productivity | 100 | Bulk-fill Word/Excel templates from a data table (mail-merge) |
| library-rag | research | 99 | Semantic search over a personal library (Nemotron-3-Embed + sqlite-vec) |
| image-studio | creative | 99 | Staged fal.ai image generation/editing with cost logging and --dry-run |
| input-token-overheads | agent-ops | 98 | Audits per-turn input token cost: measure, rank, reduce |
| input-token-analysis | agent-ops | 74 | Explains and fixes input-token spend (pairs with input-token-overheads) |
| operator-brain | agent-ops | 50 | 8-module behavioral stack: act, lead with outcome, ground every claim |
| receipt-compiler | productivity | 49 | Phone-camera receipts to straightened B&W scans to expense-claim PDF |
| marp-deck | productivity | 6 | Marp presentations: Markdown to PDF/PPTX/HTML with themes and render tests |
| skill-retrieval | plugins | 139 | BM25 skill-retrieval plugin: injects only the top-K relevant skills per turn |
| wiki | plugins | 9 | Lumen wiki plugin: OKF frontmatter, three-layer pages, ingest/query/lint workflows |
| curator | plugins | 9 | Lumen wiki plugin: wiki_curator script + memory-source adapters |

## Plugins

Two installable Hermes plugins ship in-repo. **skill-retrieval** replaces the full per-turn skill block with BM25 retrieval (top-K injection, stdlib only, per-profile index caching, optional rerank). **lumen** turns conversation history and memory into a maintained markdown wiki (sessions-first, cap-bounded curation, source-attribution contract). Both include tests runnable with `python3 -m pytest`.

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **Hermes fleet reference** | hermes-onboarding (21-step customer onboarding), input-token-overheads, and skill-retrieval map directly onto the operational stack we run for Hermes deployments - use as a second opinion on our own setup decisions |
| **Research discipline cross-check** | deep-research, fact-checker, and source-tracker implement the same source-grounded discipline we apply in intelligence work: evidence-basis labels, refute queries, validation gates |
| **Plugin packaging pattern** | lumen and skill-retrieval are clean examples of the Hermes plugin layout (plugin.yaml + skills + stdlib tests) for our own plugin development |

## Limitations / Verification

- Verified Oct 4, 2026: 36 SKILL.md files via the GitHub trees API (branch `main`); 88⭐ / 15 forks; MIT LICENSE in-repo; repo created Jul 8, 2026 and actively maintained.
- Single-maintainer provenance (personal project). Despite CI, per-skill tests, and versioned skills, community validation is still forming - treat as supervised-use until you have reviewed the skills you enable.
- skills.sh also indexes one test fixture (`greet`, 48) and one listing with no current in-repo SKILL.md (`document-converter`, 52); both are excluded from the roster but included in the combined-install figure.
- Some skills depend on external services: fal.ai keys for image-studio and clips-studio, Pexels and PDL API keys, tesseract for receipt-compiler; plugin skills assume a Hermes runtime with plugins enabled.
- No live install test was performed; install counts are the Oct 4, 2026 skills.sh sweep snapshot.

## Security

skills.sh per-skill verdicts (sampled 3 skills, verified Oct 4, 2026) - verdicts vary per skill; check the skill's security page on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| deep-research | Pass | Pass | Warn |
| skill-retrieval | Pass | Pass | Warn |
| hermes-onboarding | Pass | Warn | Pass |

## Related

- [Hermes Agent Official Skills - Bundled Batch Setup](/hermes/skills/catalog/hermes-agent-official-skills-batch-setup)
- [Hermes Agent Setup](/hermes/skills/catalog/hermes-agent-setup)
- [Skills Catalog](/hermes/skills/catalog)
- [Skills Marketplace](/hermes/skills/marketplace)

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
