---
title: "Claude Obsidian - Self-Organizing Second Brain Setup"
description: "agricidaniel/claude-obsidian - 7.3K combined installs: a self-organizing Obsidian second brain that links sources into one knowledge graph."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/claude-obsidian-setup/"
robots: "index,follow"
last_updated: "2026-11-24"
tags: ["hermes skill", "agent skill", "skill setup", "obsidian", "pkm", "second brain"]
---

# Claude Obsidian - Self-Organizing Second Brain Setup

**Source:** [agricidaniel/claude-obsidian](https://www.skills.sh/agricidaniel/claude-obsidian) via skills.sh - 7.3K combined installs across 15 indexed listings; first catalogued Nov 24, 2026 (Nov 24, 2026 morning sweep)
**GitHub:** [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) - 16,728 stars, MIT license, main branch, last pushed Oct 25, 2026; 15 skills under skills/, three read-only agents under agents/, a Python core under claude_obsidian/, and setup scripts under scripts/.
**Category:** Obsidian and Personal Knowledge Management
**Quality Tier:** 🟡 Yellow - autoresearch, wiki-ingest, and defuddle each carry one Warn cell (Snyk); the other 12 sampled skills pass all three checks.

claude-obsidian is a free, open-source AI second brain for Obsidian built for Claude Code, published by Agrici Daniel. It turns dropped-in sources (papers, articles, transcripts, notes) into linked, source-grounded Markdown notes inside a vault you own, following Andrej Karpathy's LLM Wiki pattern. The repository ships 15 skills and three read-only agents, and works in Claude Code, Codex, OpenCode, Gemini, ZCode, Cursor, and Windsurf.

The design is safety-first: only a single transaction core writes to the vault, every change is planned and shown before it is applied, and interrupted writes can be rolled back from a journal. Skills split into build-and-use workflows (wiki, wiki-ingest, wiki-query, save, wiki-lint), extensions (autoresearch, canvas, defuddle, wiki-fold, wiki-mode, wiki-retrieve, wiki-cli), and reference skills (obsidian-markdown, obsidian-bases, think).

## Installation

Add the plugin marketplace and install the plugin:

```bash
claude plugin marketplace add AgriciDaniel/claude-obsidian
claude plugin install claude-obsidian@agricidaniel-claude-obsidian
```

Then open your vault folder, start Claude Code, and set up the vault:

```bash
claude
```

```text
/claude-obsidian:wiki
```

For other hosts (Codex, OpenCode, Gemini, ZCode), link the same skills from a clone:

```bash
git clone https://github.com/AgriciDaniel/claude-obsidian.git
cd claude-obsidian
bash scripts/setup-multi-agent.sh --host codex
bash scripts/setup-multi-agent.sh --host codex --apply
```

Requires Python 3.11 or newer, and Claude Code for the plugin path.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| obsidian-markdown | 598 | explaining and validating Obsidian Flavored Markdown syntax |
| wiki | 592 | initializing, adopting, and routing work for the vault |
| autoresearch | 576 | bounded, source-grounded research loops with a cited dossier |
| save | 563 | saving one answer or insight into the vault as a transaction |
| wiki-ingest | 558 | ingesting source material with provenance and claim tracking |
| obsidian-bases | 551 | drafting and validating Obsidian Bases .base files |
| wiki-query | 515 | answering vault-scoped questions read-only |
| wiki-lint | 511 | running the read-only vault health check |
| canvas | 505 | creating and updating Obsidian JSON Canvas boards |
| defuddle | 482 | planning clean Markdown capture of a web page |
| wiki-fold | 448 | rolling up recent wiki log entries |
| wiki-retrieve | 351 | building and querying a local BM25 retrieval index |
| wiki-mode | 347 | reading and configuring the vault filing methodology |
| wiki-cli | 344 | using the official Obsidian CLI for read-only access |
| think | 340 | applying a structured review loop to hard decisions |

All 15 indexed listings clear the 300-install threshold and appear in the table above.

## Why This Matters for Hermes Agents

claude-obsidian is a strong reference for anyone building an agent that must read, link, and file unstructured input into a persistent, human-readable store. The capture, ground, compound loop keeps originals untouched, links every claim to a source, and reuses prior notes, which is exactly the discipline a long-running research or note-taking agent needs.

The transaction model is the most reusable idea here. Read-only agents draft pages, one transaction core applies them as a single plan with SHA-256 fingerprints and a rollback journal, and conflicts stop the write instead of overwriting user edits. Builders who want a Hermes agent that writes to files or a knowledge base can adopt this pattern for safety.

Tradeoffs: web research and reranking are opt-in and gated, PDF and EPUB text extraction needs external tools, and the three Warn cells sit on skills that touch network or capture paths. It is also opinionated about Obsidian, though the vault is plain Markdown and works without it.

## Usage

| You say | What happens |
|---|---|
| Set up a knowledge base for my project | Uses wiki to scaffold and route the vault |
| Ingest this article into my vault | Uses wiki-ingest with provenance and claim tracking |
| What does my vault say about X? | Uses wiki-query for a read-only, cited answer |
| Keep this answer as a note | Uses save to record one transaction |
| Check my vault for dead links and orphans | Uses wiki-lint for the health check |
| Research this topic and file it | Uses autoresearch for a bounded, cited dossier |
| Make a visual map of these notes | Uses canvas to build an Obsidian Canvas board |

## Verification

Confirm the README resolves on the main branch:

```bash
curl -sL https://raw.githubusercontent.com/AgriciDaniel/claude-obsidian/main/README.md | head -40
```

Confirm the core wiki skill body is present before setup:

```bash
curl -sL https://raw.githubusercontent.com/AgriciDaniel/claude-obsidian/main/skills/wiki/SKILL.md | head -30
```

After install, the plugin places skills under the Claude Code plugin directory; the vault itself stays wherever you initialized it.

## Security

skills.sh verdicts for sampled skills (verified Nov 24, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| obsidian-markdown | Pass | Pass | Pass |
| wiki | Pass | Pass | Pass |
| autoresearch | Pass | Pass | Warn |
| save | Pass | Pass | Pass |
| wiki-ingest | Pass | Pass | Warn |
| obsidian-bases | Pass | Pass | Pass |
| wiki-query | Pass | Pass | Pass |
| wiki-lint | Pass | Pass | Pass |
| canvas | Pass | Pass | Pass |
| defuddle | Pass | Pass | Warn |
| wiki-fold | Pass | Pass | Pass |
| wiki-retrieve | Pass | Pass | Pass |
| wiki-mode | Pass | Pass | Pass |
| wiki-cli | Pass | Pass | Pass |
| think | Pass | Pass | Pass |

The three Warn cells sit on autoresearch, wiki-ingest, and defuddle (all Snyk), the skills that touch network capture or web research. The other 12 sampled skills pass all three checks.

## Limitations

- Snapshot data, verified Nov 24, 2026: 7,281 combined installs across 15 indexed listings; 16,728 GitHub stars; MIT license; last pushed Oct 25, 2026. Counts drift over time.
- Web research (autoresearch) and web-page capture (defuddle) are opt-in and gated, and both carry a Snyk Warn verdict, so treat their network paths as the highest-audit surface.
- PDF and EPUB sources get metadata only; full text extraction needs a separate external tool you configure.
- The plugin is Claude Code first; other hosts link the same skills through a setup script rather than a native plugin.
- Obsidian is optional for reading but required for the Graph view, Canvas maps, and Bases tables the README showcases.

## Related

- [Obsidian Agent Skills - Markdown, Bases and Canvas](/hermes/skills/catalog/obsidian-skills-setup)
- [Obsidian Visual Skills - Canvas, Excalidraw and Mermaid](/hermes/skills/catalog/axton-obsidian-visual-skills-setup)
- [Hermes Obsidian Integration: Self-Organizing Vault Setup](/hermes/skills/catalog/hermes-obsidian-giveaway-pack-setup)
- [Memory Merger Setup - Agent Session Memory Consolidation](/hermes/skills/catalog/memory-merger-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run /claude-obsidian:wiki first and read the preview before it creates anything; the plan is shown before the apply.
- Keep web research and page capture off until you explicitly approve them, since those are the Warn-flagged paths.
- Use the compound loop deliberately: capture, then query and lint, so each session starts from your existing notes.
- Pick a filing methodology early with wiki-mode (Generic, LYT, PARA, or Zettelkasten); switching later does not move old notes.
- Keep backups even though writes are transactional; the lock only coordinates cooperating local writers.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
