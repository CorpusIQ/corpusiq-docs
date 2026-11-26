---
title: "GitNexus - Code Intelligence Engine Skills Setup"
description: "abhigyanpatwari/gitnexus - 12.4K combined installs: the zero-server code intelligence engine for indexing codebases into a knowledge graph for agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/abhigyanpatwari-gitnexus-setup/"
robots: "index,follow"
last_updated: "2026-11-25"
tags: ["hermes skill", "agent skill", "skill setup", "code intelligence", "code review", "mcp"]
---

# GitNexus - Setup Guide

**Source:** [abhigyanpatwari/gitnexus](https://www.skills.sh/abhigyanpatwari/gitnexus) via skills.sh - 12.4K combined installs across 15 indexed listings; first catalogued Nov 25, 2026 (Nov 25, 2026 evening sweep)
**GitHub:** [abhigyanpatwari/gitnexus](https://github.com/abhigyanpatwari/gitnexus) - 48,862 stars, NOASSERTION, last pushed Nov 26, 2026, main branch; skill listings under .claude/skills/<name>/SKILL.md with plugin mirrors in gitnexus-claude-plugin/skills/ and gitnexus-cursor-integration/skills/.
**Category:** Code Intelligence (Graph-Based Code Analysis)
**Quality Tier:** 🟠 Orange - 15 sampled skills carry two Fail cells (gitnexus-review on the Gen Agent Trust Hub, pr-tri-review on Snyk) plus eight Warn cells.

abhigyanpatwari/gitnexus is GitNexus, a zero-server code intelligence engine that indexes a codebase into a knowledge graph of symbols, calls, dependencies, and execution flows, then exposes it through an agent's MCP tools, a CLI, and a web graph explorer. Its 15 indexed listings cover exploring a codebase, debugging, impact analysis, refactoring, PR review, taint analysis, PDG queries, planning, and execution workflows, in a repository of 10,556 files with 17 registered language providers plus an experimental R provider.

GitHub reports the license as NOASSERTION, while the repository's own README declares PolyForm Noncommercial 1.0.0 with commercial licensing through akonlabs.com. The CLI indexes code locally without an LLM; optional remote embeddings, wiki generation, and AI chat use the providers you configure.

## Installation

The README installs GitNexus through its own CLI rather than the skills CLI. From your repository root:

```bash
npx gitnexus analyze
npx gitnexus setup
```

analyze builds the index, installs the agent skills, registers Claude Code hooks, and writes AGENTS.md and CLAUDE.md context files; setup configures MCP for your editors. Use gitnexus analyze --index-only to index without those repository integration files. For repeated use, install globally:

```bash
npm install -g gitnexus
```

gitnexus setup detects Claude Code, Cursor, Codex, Antigravity, Factory Droid, OpenCode, CodeBuddy, and Qoder (Windsurf needs manual MCP configuration). To select specific editors:

```bash
gitnexus setup -c cursor,codex
```

Requires Node.js 22.18+ on 22.x, or 24.11+.

## What It Provides

skills.sh publishes per-skill install counts across the 15 indexed listings. The 8 most-installed skills are listed below; the remaining 7 are summarized under the table.

| Skill | Installs | Use For |
|---|---|---|
| gitnexus-impact-analysis | 2,026 | know what will break before editing code, and get safety analysis of a change |
| gitnexus-exploring | 1,959 | understand how code works, trace execution flows, and explore architecture |
| gitnexus-debugging | 1,844 | debug a bug, trace an error, and find where a failure originates |
| gitnexus-refactoring | 1,843 | rename, extract, split, move, or restructure code safely |
| gitnexus-cli | 978 | index or reanalyze a repo, check status, clean the index, generate a wiki, and list repos |
| gitnexus-guide | 914 | learn the GitNexus tools, MCP resources, graph schema, and workflow reference |
| gitnexus-pr-swarm-review | 448 | run a coordinated reviewer swarm for a production-readiness pull request review |
| gitnexus-pr-review | 444 | review pull requests with GitNexus |

The remaining 7 indexed listings range from 22 to 433 installs.

## Why This Matters for Hermes Agents

Hermes agents already do structural code work through tools, but GitNexus fronts a purpose-built index: a knowledge graph of symbols, calls, dependencies, and execution flows that the agent queries instead of re-parsing the repo each time. For a builder running Hermes agents on a large or multi-repo codebase, the impact and taint skills turn "what breaks if I change this" into a query, and the plan plus work skills pair an implementation-ready plan with per-edit impact checks. The CLI runs locally without an LLM, so the index itself does not bill a model; only the optional embeddings, wiki generation, and AI chat call the providers you configure. The main caveats are the two Fail verdicts (gitnexus-review on the Gen Agent Trust Hub, pr-tri-review on Snyk) and the NOASSERTION license metadata, both noted below.

## Usage

| You say | What happens |
|---|---|
| What will break if I change this function | Uses gitnexus-impact-analysis to map dependencies and blast radius |
| How does the auth flow work here | Uses gitnexus-exploring to trace execution flows and architecture |
| Why is this endpoint failing | Uses gitnexus-debugging to trace the error to its source |
| Rename this function everywhere | Uses gitnexus-refactoring to apply a safe semantic rename |
| Index this repo | Uses gitnexus-cli to run analyze and build the knowledge graph |
| Review this pull request | Uses gitnexus-pr-swarm-review to fan out a reviewer swarm |

## Verification

Confirm the README and a representative skill body resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/abhigyanpatwari/gitnexus/main/README.md | head -40
curl -sL https://raw.githubusercontent.com/abhigyanpatwari/gitnexus/main/.claude/skills/gitnexus-impact-analysis/SKILL.md | head -40
```

Both URLs return 200. After installing, review each SKILL.md before relying on it, and re-check the security pages on skills.sh for the verdicts below.

## Security

skills.sh verdicts for sampled skills (verified Nov 25, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| gitnexus-impact-analysis | Warn | Pass | Warn |
| gitnexus-exploring | Warn | Pass | Pass |
| gitnexus-debugging | Pass | Pass | Pass |
| gitnexus-refactoring | Pass | Pass | Pass |
| gitnexus-cli | Pass | Pass | Warn |
| gitnexus-guide | Pass | Pass | Pass |
| gitnexus-pr-swarm-review | Pass | Pass | Warn |
| gitnexus-pr-review | Pass | Warn | Warn |
| gitnexus-taint-analysis | Pass | Pass | Pass |
| gitnexus-pdg-query | Pass | Pass | Pass |
| gitnexus-review | Fail | Pass | Warn |
| gitnexus-work | Pass | Pass | Pass |
| gitnexus-plan | Pass | Pass | Pass |
| gitnexus-lfg | Pass | Pass | Pass |
| pr-tri-review | Pass | Pass | Fail |

Across the 15 sampled listings there are two Fail cells (gitnexus-review on the Gen Agent Trust Hub and pr-tri-review on Snyk), eight Warn cells, and 35 Pass cells.

## Limitations

- Snapshot data, verified Nov 25, 2026: 12,367 combined installs across 15 indexed listings; 48,862 GitHub stars; NOASSERTION; last pushed Nov 26, 2026. Counts drift over time.
- GitHub reports the license as NOASSERTION, while the repository's own README declares PolyForm Noncommercial 1.0.0 with commercial licensing through akonlabs.com; treat it as source-available under a noncommercial license rather than an OSI-approved permissive one.
- gitnexus-pr-review carries 444 installs and a skills.sh verdict but has no dedicated SKILL.md in the current tree.
- The index runs locally without an LLM, but optional remote embeddings, wiki generation, and AI chat call the providers you configure; review SECURITY.md before exposing an index to other users.
- Two sampled skills carry a Fail cell (gitnexus-review and pr-tri-review); review those pages before production use.

## Related

[ast-grep Skill - Structural Code Search](/hermes/skills/catalog/ast-grep-agent-skill-setup) | [Qodo Skills - Code Review and Standards Suite](/hermes/skills/catalog/qodo-skills-setup) | [System Design Skills - Reasoning-Driven Architecture](/hermes/skills/catalog/system-design-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Use gitnexus analyze --watch to reindex as local files change while you work.
- For multiple concurrent agents, run one shared gitnexus mcp --http --port 3111 server and point clients at http://127.0.0.1:3111/mcp.
- Run gitnexus status before trusting an impact or trace answer; resolution depends on language support, index freshness, and available evidence.
- Start broad questions at gitnexus-exploring or gitnexus-impact-analysis, and reserve the plan plus work pair for multi-step changes.
- The web graph explorer (gitnexus serve) reuses the existing index, so no re-upload or re-index is needed.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
