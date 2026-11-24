---
title: "Supermemory Skills - Agent Memory API Suite Setup"
description: "supermemoryai/skills - 4.4K combined installs across 3 listings: Supermemory API and CLI skills for persistent memory, plus an SVG animation skill."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/supermemory-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-23"
tags: ["hermes skill", "agent skill", "skill setup", "agent memory", "semantic search"]
---

# Supermemory Skills - Agent Memory API Suite Setup

**Source:** [supermemoryai/skills](https://www.skills.sh/supermemoryai/skills) via skills.sh - 4.4K combined installs across 3 indexed listings; first catalogued Nov 23, 2026 (Nov 23, 2026 evening sweep)
**GitHub:** [supermemoryai/skills](https://github.com/supermemoryai/skills) - 117 stars, no license (no LICENSE file in the repository), main branch, last pushed Oct 14, 2026; four top-level skill directories (supermemory, supermemory-cli, svg-animations, memorybench) with one SKILL.md each, but no root README.md.
**Category:** Agent Memory and Context Infrastructure
**Quality Tier:** 🟡 Yellow - two of the three sampled skills carry a Snyk Warn cell (supermemory and supermemory-cli); svg-animations passes all three scanners.

Supermemory Skills is a small collection centered on Supermemory, a memory and context API for AI agents that provides a Memory API of learned user context, per-user profiles and semantic search over knowledge bases. The repository publishes no root README and no description field, so the publisher's offering is documented in supermemory/README.md, which frames Supermemory as long-term and short-term memory infrastructure for personalized, context-aware applications.

The three indexed listings split the work. supermemory documents the v5 API and SDKs (TypeScript supermemory 5.x, Python supermemory 5.x and @supermemory/tools 3.x); supermemory-cli documents the supermemory 5.x CLI and its JSON output contract; and svg-animations is an unrelated SVG graphics skill that shares the repository. A fourth directory, memorybench, benchmarks a custom memory implementation against Supermemory, Mem0 and Zep but carries no indexed listing.

## Installation

Install through skills.sh:

```bash
npx skills add supermemoryai/skills
```

Without the CLI, copy the supermemory/ directory, its SKILL.md plus the references/ folder, into a Claude Code skills directory. Project level: .claude/skills/supermemory/. Personal: ~/.claude/skills/supermemory/. Claude Code discovers and loads the skill automatically. For Claude.ai, zip the supermemory/ directory and upload it under Settings, then Capabilities.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| svg-animations | 2,948 | creating animated SVG graphics, icons, logos, path and morphing animations, spinners and illustrations |
| supermemory | 990 | building with the Supermemory v5 API and SDKs for persistent memory, profiles and semantic search |
| supermemory-cli | 484 | driving the Supermemory 5.x CLI from the terminal or scripts for add, search, profile and forget operations |

All 3 indexed listings clear the 400-install threshold and appear in the table above.

## Why This Matters for Hermes Agents

An agent that holds no state between turns re-asks the same questions and forgets the user's preferences the moment the session ends. Supermemory is the layer that fixes that: the supermemory skill teaches the agent the v5 API and SDKs for storing documents, extracting memories, searching them and reading a maintained per-user profile, all scoped to a namespace so one user's memory never bleeds into another's. The supermemory-cli skill covers the same surface from the shell, which matters for agents and scripts that orchestrate memory operations without writing application code.

The two memory skills are precise about the parts that break silently: the namespace must be the first argument or the first URL path segment, the legacy names containerTag, customId, /v3/ and /v4/ must never be emitted because that API shuts down on December 31, 2026, and the search and ingestion options carry typed filters that a general-purpose model will get wrong. For a builder shipping a personalized agent or a document knowledge base, this collection shortens the path from zero to a working memory backend.

## Usage

| You say | What happens |
|---|---|
| Add persistent memory to my chatbot | Uses supermemory to recommend namespaces and wire add, search and profile calls |
| Store a document and search it later | Uses supermemory for ingestion, search modes and typed filters over the v5 API |
| Give me the CLI command to add a memory | Uses supermemory-cli for the exact command, flags and JSON output contract |
| My user profile should learn over time | Uses supermemory to read and maintain the per-namespace profile |
| Make an animated SVG logo | Uses svg-animations for path drawing, morphing, motion paths and spinners |
| My code still uses /v3/ endpoints | Uses supermemory to flag legacy names and point to the v5 migration path |

## Verification

Confirm the Supermemory skill README resolves on the main branch (the repository has no root README.md):

```bash
curl -sL https://raw.githubusercontent.com/supermemoryai/skills/main/supermemory/README.md | head -40
```

Confirm the API skill body is present before building:

```bash
curl -sL https://raw.githubusercontent.com/supermemoryai/skills/main/supermemory/SKILL.md | head -30
```

Confirm the CLI skill body is present before scripting memory operations:

```bash
curl -sL https://raw.githubusercontent.com/supermemoryai/skills/main/supermemory-cli/SKILL.md | head -30
```

Confirm the SVG skill body is present before design work:

```bash
curl -sL https://raw.githubusercontent.com/supermemoryai/skills/main/svg-animations/SKILL.md | head -30
```

## Security

skills.sh verdicts for sampled skills (verified Nov 23, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| svg-animations | Pass | Pass | Pass |
| supermemory | Pass | Pass | Warn |
| supermemory-cli | Pass | Pass | Warn |

supermemory and supermemory-cli each carry a Snyk Warn cell; svg-animations passes all three scanners. All three listings were sampled, so none sit outside the sample.

## Limitations

- Snapshot data, verified Nov 23, 2026: 4,422 combined installs across 3 indexed listings; 117 GitHub stars; no license (no LICENSE file in the repository); last pushed Oct 14, 2026. Counts drift over time.
- The repository carries no LICENSE file and GitHub reports no license. The supermemory skill's own README describes it as Apache 2.0, but the current tree contains no LICENSE file, so treat the repository as unlicensed until one appears.
- The repository publishes no root README or description field; the collection is documented only in supermemory/README.md, which covers the API and CLI skills but not the svg-animations or memorybench directories.
- A fourth skill directory, memorybench, exists in the tree but has no indexed listing, so it is outside this guide's table and install counts.
- Two of the three listings carry a Snyk Warn cell in the sample, so this guide sits at the Yellow tier rather than Green.

## Related

- [Hermes Hybrid Memory - Full Setup Guide](/hermes/skills/catalog/hermes-hybrid-memory-setup)
- [Claude Mem Setup](/hermes/skills/catalog/claude-mem-setup)
- [MemPalace - Local-First AI Memory for Agents](/hermes/skills/catalog/mempalace-setup)
- [Basic Memory Skills Setup](/hermes/skills/catalog/basic-memory-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Scope every call to a namespace, a user id or project id, as the first SDK argument or URL segment, or memory from different users will mix.
- Treat v3 and v4 names as never-emit: containerTag, customId, /v3/ and /v4/ point at the API that shuts down on December 31, 2026.
- Pair supermemory with supermemory-cli so you can script memory operations and read the JSON output contract without hand-building the API calls.
- Keep svg-animations out of memory work; it is a graphics skill that only shares the repository, not the domain.
- Fetch an API key from console.supermemory.ai before the first build and point the SDK at your own namespace.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
