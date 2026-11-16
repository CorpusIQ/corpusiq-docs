---
title: "GrepAI Skills - Semantic Code Search and Call Graphs"
description: "yoanbernabeu/grepai-skills - 19.4K combined installs across 27 indexed listings: semantic code search, call graphs, and MCP integration for GrepAI."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/grepai-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-16"
tags: ["hermes skill", "agent skill", "skill setup", "code search", "semantic search", "mcp"]
---

# GrepAI Skills - Setup Guide

**Source:** [yoanbernabeu/grepai-skills](https://www.skills.sh/yoanbernabeu/grepai-skills) via skills.sh - 19.4K combined installs across 27 indexed listings; first seen Nov 16, 2026 (Nov 16 morning sweep)
**GitHub:** 20 stars, MIT license, `main` branch, last pushed 2026-10-30, `SKILL.md` files under `skills/<category>/<name>/`
**Category:** Code search - semantic search, call graph analysis and MCP integration
**Quality Tier:** 🟢 Green - all 12 sampled skills pass the Gen Agent Trust Hub, Socket, and Snyk.

GrepAI is a semantic code search tool that searches by meaning rather than exact text, supports fully local embeddings via Ollama, indexes in real time with file watching, and traces function call graphs. This repository ships 27 agent skills that teach an AI assistant to install, configure, search, and trace with GrepAI, grouped by category: getting started, configuration, embeddings providers, storage backends, indexing, search, trace, integration, and advanced.

Each skill lives under `skills/<category>/<name>/` with its own `SKILL.md`. The suite targets Claude Code, Cursor, Codex, OpenCode, Windsurf, and 30+ other AI agents, and ships a Claude Code plugin plus MCP integrations for Claude Code and Cursor.

## Installation

Install everything with the `skills` CLI:

```bash
npx skills add yoanbernabeu/grepai-skills
```

The common one-liners:

```bash
# Install only search skills
npx skills add yoanbernabeu/grepai-skills --skill grepai-search-basics

# Install globally (available in all projects)
npx skills add yoanbernabeu/grepai-skills -g

# List all available skills
npx skills add yoanbernabeu/grepai-skills --list

# Non-interactive (CI/CD friendly)
npx skills add yoanbernabeu/grepai-skills --all -y
```

Claude Code plugin:

```text
/plugin marketplace add yoanbernabeu/grepai-skills
/plugin install grepai-complete@grepai-skills
```

Manual install by copying the `skills/` directory to your agent's project or global skills path (for example `.claude/skills/` or `~/.claude/skills/`).

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| grepai-search-basics | 942 | Basic semantic code search with GrepAI: fundamental search commands and concepts. |
| grepai-search-advanced | 861 | Advanced search options: JSON output, compact mode, and AI agent integration. |
| grepai-trace-graph | 837 | Build complete call graphs with GrepAI trace, including recursive dependency analysis. |
| grepai-trace-callers | 818 | Find function callers: discover what code calls a specific function. |
| grepai-search-tips | 813 | Tips and best practices for writing effective GrepAI searches. |
| grepai-ollama-setup | 811 | Install and configure Ollama for private, local embedding generation. |
| grepai-trace-callees | 796 | Find function callees: discover what functions a specific function calls. |
| grepai-search-boosting | 784 | Configure search result boosting to prioritize certain paths and penalize others. |
| grepai-embeddings-ollama | 777 | Configure Ollama as the embedding provider for local, private embedding generation. |
| grepai-mcp-tools | 750 | Reference for all GrepAI MCP tools and their parameters. |
| grepai-languages | 738 | Supported programming languages that GrepAI can index and trace. |
| grepai-chunking | 735 | Configure code chunking to optimize how code is split for embedding. |
| grepai-init | 730 | Initialize GrepAI in a project for the first time. |
| grepai-watch-daemon | 729 | Configure and manage the watch daemon for real-time code indexing. |
| grepai-troubleshooting | 723 | Diagnose and fix common GrepAI issues. |
| grepai-config-reference | 723 | Complete configuration reference covering all available options. |
| grepai-workspaces | 717 | Configure multi-project workspaces for monorepos and related projects. |
| grepai-ignore-patterns | 709 | Configure ignore patterns to exclude files and directories from indexing. |

The remaining 9 indexed listings range from 560 to 698 installs.

## Why This Matters for Hermes Agents

Understanding an unfamiliar codebase is one of the hardest things an agent does, and exact-text grep only helps when you already know the words to search for. GrepAI searches by meaning, so an agent can ask for concepts rather than exact strings, and these skills give it expert-level knowledge of the tool instead of forcing it to learn GrepAI's CLI and configuration on the fly.

The call-graph skills matter most for reasoning about code. trace-callers and trace-callees answer the two questions every navigation task reduces to: who calls this, and what does this call. trace-graph extends that to full recursive dependency analysis, which is the foundation for impact analysis before a change.

Because the suite also covers embeddings providers, storage backends, and the watch daemon, a Hermes agent can configure GrepAI for a private local setup or a shared team deployment without leaving the skill set.

## Usage

| You say | What happens |
|---|---|
| "Search for authentication code in this project" | grepai-search-basics covers the fundamental semantic search commands and concepts. |
| "Search with JSON output for an agent" | grepai-search-advanced applies JSON output, compact mode, and AI agent integration. |
| "What calls the Login function?" | grepai-trace-callers finds all callers of a function. |
| "What does Login call?" | grepai-trace-callees finds all functions a given function calls. |
| "Build a full dependency graph" | grepai-trace-graph builds complete call graphs with recursive dependency analysis. |
| "Set up private local embeddings" | grepai-ollama-setup installs and configures Ollama for local embedding generation. |
| "Optimize how code is split for embedding" | grepai-chunking configures code chunking for embedding. |

## Verification

Check the skill files before installing:

```bash
curl -fsSL https://raw.githubusercontent.com/yoanbernabeu/grepai-skills/main/skills/search/grepai-search-basics/SKILL.md | head -20
curl -fsSL https://raw.githubusercontent.com/yoanbernabeu/grepai-skills/main/skills/trace/grepai-trace-graph/SKILL.md | head -20
npx skills add yoanbernabeu/grepai-skills --list
```

Skills live under `skills/<category>/<name>/`; confirm the category path exists in the current tree before installing a specific skill.

## Security

skills.sh verdicts for sampled skills (verified Nov 16, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| grepai-search-basics | Pass | Pass | Pass |
| grepai-search-advanced | Pass | Pass | Pass |
| grepai-trace-graph | Pass | Pass | Pass |
| grepai-trace-callers | Pass | Pass | Pass |
| grepai-search-tips | Pass | Pass | Pass |
| grepai-ollama-setup | Pass | Pass | Pass |
| grepai-trace-callees | Pass | Pass | Pass |
| grepai-search-boosting | Pass | Pass | Pass |
| grepai-embeddings-ollama | Pass | Pass | Pass |
| grepai-mcp-tools | Pass | Pass | Pass |
| grepai-languages | Pass | Pass | Pass |
| grepai-chunking | Pass | Pass | Pass |

All 12 sampled skills pass the Gen Agent Trust Hub, Socket, and Snyk with no Warn or Fail findings.

## Limitations

- Snapshot data, verified Nov 16, 2026: 19,366 combined installs across 27 indexed listings; 20 GitHub stars; MIT; last pushed 2026-10-30. Counts drift over time.
- The skills document GrepAI specifically, so they only add value when you actually run GrepAI for code search and tracing.
- Local embeddings require running Ollama locally; cloud embeddings (OpenAI, LM Studio) send code to an external provider, so choose the backend that matches your privacy requirements.
- The repository has 20 GitHub stars at snapshot, so it carries less community vetting than larger suites.
- GrepAI itself lives in a separate repository (yoanbernabeu/grepai); this suite only ships the agent skills that teach it.

## Related

- [ast-grep Skill](/hermes/skills/catalog/ast-grep-agent-skill-setup)
- [Context7 Skill](/hermes/skills/catalog/context7-skill-setup)
- [Qdrant Skills](/hermes/skills/catalog/qdrant-skills-setup)
- [MCP Integration](/hermes/skills/catalog/mcp-integration-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the full suite with `--all -y` in CI or other non-interactive environments.
- Use `--skill` to install only the search skills when you just need query help.
- Follow the getting-started skills (installation, ollama-setup, quickstart) before the search and trace skills.
- Prefer local Ollama embeddings when the code must stay private.
- Use grepai-mcp-claude or grepai-mcp-cursor to wire GrepAI into your editor via MCP.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
