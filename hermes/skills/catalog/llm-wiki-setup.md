---
title: llm-wiki — Setup Guide
description: Generate wiki-style documentation from any codebase or knowledge source using LLMs — 369 installs from nousresearch/hermes-agent.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/llm-wiki-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# llm-wiki — Setup Guide

**Source:** [nousresearch/hermes-agent](https://github.com/nousresearch/hermes-agent)
**Skill:** `llm-wiki`
**Installs:** 369

The `llm-wiki` skill enables Hermes agents to generate comprehensive wiki-style documentation from codebases, knowledge bases, or any source material. Produces structured, cross-linked reference documentation with automatic table of contents, backlinks, and search indexing.

## Installation

```bash
npx skills add https://github.com/nousresearch/hermes-agent --skill llm-wiki
```

After install, reload skills:
- Hermes CLI: `/reload-skills` or restart session
- Hermes gateway: `/restart` or `hermes gateway restart`

## Prerequisites

| Requirement | Details |
|-------------|---------|
| Hermes Agent | v0.20.0+ |
| Source material | Codebase, API docs, knowledge base to document |

## Capabilities

| Capability | Trigger | Output |
|-----------|---------|--------|
| Codebase wiki | "Generate wiki from this repo" | Cross-linked wiki pages |
| API documentation | "Document the API endpoints" | API reference with examples |
| Knowledge base | "Organize these notes into a wiki" | Structured wiki hierarchy |
| Glossary | "Generate a glossary of terms" | Term definitions with links |
| FAQ generation | "Create FAQ from this documentation" | Question-answer pairs |
| Cross-referencing | "Add wikilinks between these pages" | Interlinked documentation |

## Key Features

- **Automatic structure**: Infers page hierarchy from content relationships
- **Wikilink generation**: `[[page-name]]` links between related pages
- **Table of contents**: Auto-generated from headings
- **Search indexing**: Embeds pages for semantic search
- **Change tracking**: Detects stale/outdated wiki pages
- **Markdown output**: Standard markdown compatible with MkDocs, GitBook, Obsidian

## CLI/Command Reference

The skill integrates with Hermes' file tools:
- Wiki pages are written as `.md` files in a `wiki/` directory
- Compatible with GBrain for semantic search (`gbrain import wiki/ --no-embed && gbrain embed --stale`)
- Use with `corpusiq-docs-management` skill for publishing to docs site

## CorpusIQ Use Cases

1. **corpusiq-docs expansion** — Auto-generate documentation pages for new features
2. **Internal knowledge base** — Wiki for agent operating procedures
3. **Connector documentation** — Standardized docs for each of 37+ connectors
4. **Onboarding wiki** — Structured onboarding for new team members
5. **API reference** — Auto-generated from MCP server tool definitions

## Troubleshooting

| Issue | Likely Cause | Resolution |
|-------|-------------|------------|
| Circular wikilinks | Self-referencing pages | Use `--max-depth` to limit recursion |
| Large codebase timeout | Too many files | Process by directory, not whole repo |
| Broken links | Update existing wiki | Use `--update` mode to refresh |
| Duplicate pages | Multiple sources | Use `--merge` to consolidate |

## Verification

After installation, verify the skill is loaded:
```bash
hermes skills list | grep llm-wiki
```

Test with a documentation request:
```
"Generate a wiki for the CorpusIQ MCP server architecture from the source code"
```
