---
title: "Karpathy LLM Wiki - Knowledge Base Skill Setup"
description: "astro-han/karpathy-llm-wiki: 8.8K combined installs across 1 listing; an Agent Skills LLM wiki that ingests sources, cites answers, and lints."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/karpathy-llm-wiki-setup/"
robots: "index,follow"
last_updated: "2026-11-17"
tags: ["hermes skill", "agent skill", "skill setup", "llm wiki", "knowledge base", "agent memory"]
---

# Karpathy LLM Wiki - Setup Guide

**Source:** [astro-han/karpathy-llm-wiki](https://www.skills.sh/astro-han/karpathy-llm-wiki) via skills.sh - 8.8K combined installs across 1 indexed listing; first seen Nov 17, 2026 (this sweep)
**GitHub:** 2,761 stars, MIT license, `main` branch, last pushed 2026-07-23, a single root `SKILL.md` plus `references/`, `scripts/`, `examples/`, and `tests/` directories
**Category:** LLM knowledge base / agent memory skills
**Quality Tier:** 🟡 Yellow - Snyk flags the single indexed skill (karpathy-llm-wiki) with Fail.

`karpathy-llm-wiki` packages Andrej Karpathy's LLM Wiki idea into one installable Agent Skills skill. A coding agent ingests sources into `raw/`, compiles durable knowledge pages into `wiki/`, answers questions with citations, and lints the wiki for consistency. It ships as a single root `SKILL.md` with `references/` templates, a Python evidence-check script, and `examples/` from a production wiki.

The skill is tool-agnostic: it works with Claude Code, Cursor, Codex, OpenCode, or any tool that follows the agentskills.io standard. It is optimized for the wiki model rather than RAG, so knowledge compounds during ingest and maintenance instead of being re-derived on every query.

## Installation

```bash
npx add-skill Astro-Han/karpathy-llm-wiki
```

Works with any tool that follows the Agent Skills standard. For Codex CLI, copy `SKILL.md`, `references/`, and `scripts/` into `.agents/skills/karpathy-llm-wiki/`; other tools copy the same files into their own skill directory.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| karpathy-llm-wiki | 8,772 | Build a Karpathy-style LLM wiki: ingest sources, answer with citations, and lint for consistency. |

No indexed listings fall below the threshold; the single listing appears above.

## Why This Matters for Hermes Agents

The skill packages Karpathy's LLM Wiki workflow so an agent maintains durable markdown knowledge pages instead of re-searching raw documents on every question. New sources are compiled into wiki pages, cross-references are updated over time, and answers cite the pages that already hold the synthesized knowledge.

For a Hermes agent this means compounding knowledge: each ingest can update multiple pages, strengthen cross-references, and record contradictions, so the wiki improves with use rather than re-deriving relationships on every query. The ingest, query, and lint operations run inside whatever agent harness hosts the skill, so the workflow ports across Claude Code, Cursor, Codex, and Hermes without a service to run.

The lint operation is the durability mechanism: it checks index integrity, links, and wiki health, catching the drift that otherwise makes a knowledge base silently go stale.

## Usage

| You say | What happens |
|---|---|
| "Ingest this article: https://..." | Stores the source in `raw/`, then compiles or updates the matching wiki pages. |
| "What do I know about attention mechanisms?" | Searches the wiki and answers with citations linking to markdown pages. |
| "Lint my wiki" | Checks index integrity, links, and wiki health, then auto-fixes reported issues. |
| "Add this PDF to the wiki" | Converts the source to markdown under `raw/` and compiles it into `wiki/`. |
| "What did we ingest this week?" | Reads the append-only operation log for recent ingest and update activity. |

## Verification

Probe the skill on the `main` branch before installing. The root SKILL.md returns 200:

```bash
curl -fsSL https://raw.githubusercontent.com/astro-han/karpathy-llm-wiki/main/SKILL.md | head -12
```

The skill lives at the repository root as `SKILL.md`, with `references/` holding the page and index templates, `scripts/check_evidence.py` powering the lint checks, and `examples/` showing a production wiki.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-17) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| karpathy-llm-wiki | Pass | Pass | Fail |

The sample covers the only indexed listing, so this is a full census. Snyk flags the single indexed skill with Fail while Gen Agent Trust Hub and Socket pass; the in-repo content is markdown instructions plus a small Python evidence-check script (`scripts/check_evidence.py`), so review that script before relying on the skill in production.

## Limitations

- Snapshot data, verified 2026-11-17: 8,772 combined installs across 1 indexed listing; 2,761 GitHub stars; MIT; last pushed 2026-07-23. Counts drift over time.
- The repository has not been pushed since 2026-07-23, so the workflow is stable but not under active development.
- A single indexed listing means there is no suite to install selectively; the whole skill arrives as one unit.
- Snyk flags the single indexed skill with Fail; the in-repo content is markdown instructions plus a Python evidence-check script, so review that script before production use.
- This is a workflow and prompt structure, not a hosted service: ingest, query, and lint run inside whichever agent harness hosts the skill.

## Related

- [Inkeep Open Knowledge Skills - Collaborative Knowledge Base Suite Setup](/hermes/skills/catalog/inkeep-open-knowledge-skills-setup)
- [Knowledge Work Plugins - Anthropic Productivity Setup](/hermes/skills/catalog/knowledge-work-plugins-setup)
- [claude-mem - Persistent Memory for Coding Agents Setup](/hermes/skills/catalog/claude-mem-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with one topic and let the wiki compound: ingest a few sources, then ask cited questions to confirm pages are forming.
- Treat `raw/` as immutable; new information arrives as new sources rather than edits to old ones.
- Run "Lint my wiki" after each ingest batch to keep index entries and cross-links healthy.
- The workflow is tuned for 50K-100K tokens of curated wiki, where grep and read beat vector search; add search tooling only when recall degrades.
- Skim the append-only `log.md` to see what changed between sessions.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
