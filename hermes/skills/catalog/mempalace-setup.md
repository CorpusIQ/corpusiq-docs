---
title: "MemPalace - Local-First AI Memory for Agents"
description: "mempalace/mempalace on skills.sh: 5.3K combined installs across 9 listings; local-first verbatim agent memory with recall and task skills."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/mempalace-setup/"
robots: "index,follow"
last_updated: "2026-11-05"
tags: ["hermes skill", "agent skill", "skill setup", "agent memory", "mcp", "rag"]
---

# MemPalace - Setup Guide

**Source:** [mempalace/mempalace](https://www.skills.sh/mempalace/mempalace) via skills.sh - 5.3K combined installs across 9 indexed listings; first seen 2026-11-05 (Nov 5, 2026 evening sweep)
**GitHub:** 60,419 stars, MIT licence, default branch `develop`, last pushed 2026-11-04, 15 `SKILL.md` files across `skills/`, `.claude-plugin/skills/`, `.antigravity-plugin/skills/`, `.codex-plugin/skills/` and `integrations/openclaw/`
**Category:** Agent memory: verbatim local storage with pluggable backends, recall and task memory driven over a CLI
**Quality Tier:** 🟡 Yellow - Gen Agent Trust Hub Warns on the mempalace setup listing; MIT, 60,419 stars.

MemPalace is a local-first memory system for coding agents. It stores conversation history and project content as verbatim text and retrieves it with semantic search, without summarizing, extracting or paraphrasing. The index is structured rather than flat: people and projects become wings, topics become rooms, and the original content sits in drawers, so a query can be scoped instead of run against a single corpus.

The retrieval layer is pluggable and ChromaDB is the default; the contract lives in `mempalace/backends/base.py`, with SQLite-exact, native Rust, Milvus, Qdrant and pgvector options documented in the README. The headline benchmark claim is 96.6% R@5 raw on LongMemEval with no API key, no cloud and no LLM in the loop, rising to 98.4% on a held-out split for the hybrid pipeline. The same package exposes 47 MCP tools for palace reads and writes, a knowledge graph, agent diaries and logstream coordination.

The repository carries 15 `SKILL.md` files across five locations. The three skills in `skills/` are the documented ones: setup and operations, recall, and task delegation. The `.codex-plugin/skills/` directory carries six more entrypoints named after CLI verbs (status, search, mine, init, help, audit), which is where the six small listings in the install index come from.

## Installation

The documented path is skill first, then let the agent perform the system setup:

```bash
npx skills add MemPalace/mempalace
```

Installing the skill does not install the CLI or the MCP server. The `mempalace` setup skill detects the system, installs the Python package, configures MCP, verifies the live connection, and asks whether you want a private local palace, a shared-brain hub, or a client joining an existing hub.

For a direct CLI install, the README recommends an isolated environment to avoid PEP 668 errors and dependency collisions with `chromadb`, `numpy` and `grpcio`:

```bash
uv tool install mempalace
mempalace init ~/projects/myapp
```

`pipx install mempalace` works the same way. Use plain `pip` only inside an activated virtualenv where you want `import mempalace` available:

```bash
python -m venv .venv && source .venv/bin/activate
pip install mempalace
```

A multi-arch container image runs the MCP server or the CLI without a local Python toolchain:

```bash
docker pull ghcr.io/mempalace/mempalace:latest
docker run -i --rm -v mempalace-data:/data ghcr.io/mempalace/mempalace
```

Everything persists under `/data` (palace, config, cached embedding model), so mount a volume there and reuse it. The first call that needs embeddings downloads roughly 80 MB for the default `minilm` model, or roughly 300 MB for `embeddinggemma`.

## What It Provides

Three listings carry almost all of the installs; the other six are CLI-verb entrypoints.

| Skill | Installs | Use For |
|---|---|---|
| mempalace | 2,128 | Guided install and operations: private local palace, shared-brain hub or client mode, MCP wiring, mining, status, palace audit and repair, wings, rooms, drawers, logstream readiness |
| mempalace-recall | 1,643 | Search-before-answer protocol that reads the palace before answering questions about past work, people, projects or prior decisions |
| mempalace-task | 1,519 | Creating, handing off, claiming, executing and closing agent tasks through the logstream, with task ids and controlled headless launches |

The remaining 6 indexed listings range from 1 to 3 installs.

## Why This Matters for Hermes Agents

Hermes agents accumulate context in sessions that are eventually compacted or dropped. Summaries lose the exact wording of a decision, and an agent that answers from a summary cannot be corrected by reading the source. MemPalace's design choice is to keep the verbatim text and make retrieval responsible for scope, which is a different tradeoff from summarizing memory: recall quality depends on the index instead of on a lossy digest.

The structured index is the part that changes behaviour. Scoping a search to one wing is what lets a recall skill answer "what did we decide about the billing migration" from the right project's drawers instead of from every conversation the agent has ever had. The shipped `mempalace-recall` skill encodes the protocol as a rule: search before answering anything that may already be filed, rather than guessing from model memory.

Task handoff is the second useful surface. `mempalace-task` puts work in the logstream with an id, so one agent can prepare a ready-to-paste task for another, and the receiving agent can claim, execute and close it. That is coordination state that survives a session boundary, which is exactly what a long-running Hermes workflow needs when it fans out.

The local-first claim is also operational, not just promotional. The README states nothing leaves the machine unless you opt in, the default embedding model runs locally, and the optional OpenAI-compatible embedding endpoint can point at a server on the same machine or LAN. For teams that cannot send transcripts to a vendor, that is the difference between using memory and not using it.

## Usage

| You say | What happens |
|---|---|
| "Set up MemPalace for this machine" | The setup skill detects the OS and harness, installs the CLI, wires MCP, verifies the connection and asks which palace mode you want |
| "Mine my Claude Code sessions into the palace" | Runs mining over the transcript directory, with `--mode convos` and per-project wing scoping |
| "What did we decide about the GraphQL migration?" | The recall skill searches the palace first and answers from the verbatim drawers it finds |
| "Hand this refactor to the other agent" | Creates a logstream task with an id and a ready-to-paste brief for the receiving agent |
| "How organized is my palace?" | Runs the read-only audit, which scores structure and can start a guided repair one decision at a time |
| "Load context for a new session" | Runs the wake-up path to pull relevant context before the first answer |
| "Search the palace for why we dropped pgvector" | Runs a scoped semantic search over the relevant wing rather than across the whole corpus |

## Verification

The default branch is `develop`, so every raw URL has to use it:

```bash
curl -fsSL https://raw.githubusercontent.com/MemPalace/mempalace/develop/skills/mempalace/SKILL.md | head -5
```

It should open with `name: mempalace` and a description covering install, MCP wiring, mining, status, audit, wings, rooms and drawers. Then check the CLI that the setup skill is supposed to install, and the palace it points at:

```bash
mempalace --version
mempalace audit
```

`mempalace --version` confirms the Python package is reachable on PATH, which the setup skill treats as a separate question from the package being installed. `mempalace audit` is read-only and documented as safe to run while the MCP server is up.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-05) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| mempalace | Warn | Pass | Pass |
| mempalace-task | Pass | Pass | Pass |
| search | Pass | Pass | Pass |
| init | Pass | Pass | Pass |
| audit | Pass | Pass | Pass |

Gen Agent Trust Hub Warns on the `mempalace` setup listing, which is also the skill that installs a Python package and edits MCP configuration on your behalf. Read that skill before letting an agent run it unattended, and keep the palace on a volume you control. Socket and Snyk return Pass on every sampled skill, including the setup one.

The README carries its own warning worth repeating: MemPalace has no other official websites, and the only official sources it names are the GitHub repository, the PyPI package and `mempalaceofficial.com`. Any other domain is described by the project as an impostor site.

## Limitations

- Snapshot data, verified 2026-11-05: 5,306 combined installs across 9 indexed listings; 60,419 GitHub stars; MIT; last pushed 2026-11-04. Counts drift over time.
- The default branch is `develop`, not `main`. Every raw URL in this guide and in the repository's own links must use it, and the README notes that a build from a clone uses whatever branch you checked out.
- Yellow tier follows the sampled audits: Gen Agent Trust Hub Warns on the `mempalace` listing, the same skill that installs the package and writes MCP configuration.
- The install index counts nine listings, but only three are documented skills. The other six are CLI-verb entrypoints under `.codex-plugin/skills/` with 1 to 3 installs each.
- Only three of the 15 `SKILL.md` files are the documented skills. The rest are plugin copies under `.claude-plugin/skills` and `.antigravity-plugin/skills`, the six `.codex-plugin` CLI-verb entrypoints, and one OpenClaw integration entrypoint, so the file count is much larger than the number of distinct skills.
- Claude Code sessions expire in 30 days without auto-save hooks wired, per the README's own notice; the hooks, not the skills, are what make retention automatic.
- Native Termux install is unsupported because ChromaDB and ONNX Runtime publish no Android wheels, and the Docker image runs as uid 1000, so a bind-mounted `0700` directory fails with a permission error rather than a clear message.

## Related

- [Basic Memory Skills Setup Guide for Hermes Agents](/hermes/skills/catalog/basic-memory-skills-setup)
- [AgentMemory Setup - Persistent Memory for Hermes Agents](/hermes/skills/catalog/agentmemory-setup)
- [Hermes Memory Stack - Memory OS Setup Guide](/hermes/skills/catalog/hermes-memory-stack-setup)

## Pro Tips

- Scope the mine, not the search. Mining a whole home directory into one wing makes every later recall query compete with irrelevant drawers.
- Wire the auto-save hooks before the first long session. The retention notice is about what happens when hooks are missing, and backfilling from JSONL afterwards is extra work.
- Run `mempalace audit` on a schedule. It is read-only, it is safe while the server runs, and structural drift is cheaper to fix early.
- Use the recall skill as a rule rather than a request. Its value is that the agent searches before answering, which only happens if the skill is active during ordinary conversation.
- Keep the embedding model consistent per palace. The README notes that changing models requires `mempalace repair rebuild-index`, because the vector space changes.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
