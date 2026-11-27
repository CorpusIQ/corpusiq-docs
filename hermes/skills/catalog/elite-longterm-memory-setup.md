---
title: "Elite Long-Term Memory - WAL Protocol Agent Memory"
description: "nextfrontierbuilds/elite-longterm-memory: 2.4K combined installs. WAL-protocol long-term memory with vector search, git-notes and daily logs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/elite-longterm-memory-setup/"
robots: "index,follow"
last_updated: "2026-11-27"
tags: ["hermes skill", "agent skill", "skill setup", "long-term memory", "vector search", "write-ahead log"]
---

# Elite Long-Term Memory - Setup Guide

**Source:** [nextfrontierbuilds/elite-longterm-memory](https://www.skills.sh/nextfrontierbuilds/elite-longterm-memory) via skills.sh - 2.4K combined installs across 1 indexed listing; first documented 2026-11-27 (morning sweep)

**GitHub:** [nextfrontierbuilds/elite-longterm-memory](https://github.com/nextfrontierbuilds/elite-longterm-memory) - 16 stars, no license file (package.json and the README badge claim MIT), branch main, last pushed 2026-01-30; a single skill at the repo root SKILL.md plus bin/elite-memory.js and package.json

**Category:** Long-term agent memory: write-ahead-log state persistence with vector search, a git-notes knowledge graph and daily logs

**Quality Tier:** 🟢 Green - the single sampled listing passes all three auditors, but the repository is thin (16 stars, no LICENSE file, last pushed 2026-01-30)

elite-longterm-memory is a single-skill repository from NextFrontierBuilds that packages a long-term memory system for AI agents around a write-ahead-log protocol. The README bills it as combining seven memory approaches: a bulletproof WAL protocol that survives compaction, LanceDB vector search, a git-notes knowledge graph, file-based archives, optional SuperMemory cloud sync, memory hygiene, and Mem0 auto-extraction.

The repository is thin: four files, README.md, SKILL.md, bin/elite-memory.js and package.json, with the bulk of the described architecture living in the SKILL.md and README rather than shipped code. The npm package exposes an elite-memory CLI, and the README documents initialization, status and daily-log commands plus a Clawdbot/Moltbot config snippet and Mem0 integration.

## Installation

The README's Quick Start runs through the npm package:

```bash
npx elite-longterm-memory init
npx elite-longterm-memory status
npx elite-longterm-memory today
```

The Commands section lists the same actions through the installed binary:

```bash
elite-memory init
elite-memory status
elite-memory today
elite-memory help
```

The Mem0 auto-extraction path is recommended in the README and needs its own install and key:

```bash
npm install mem0ai
export MEM0_API_KEY="***"
```

For Clawdbot/Moltbot users the README shows a `memorySearch` block to add to `~/.clawdbot/clawdbot.json`. The README is thin on install detail: it does not document a skills.sh or Hermes-specific command, so install the npm package and load SKILL.md as the skill.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| elite-longterm-memory | 2,396 | Long-term memory for agents: WAL-protocol session state, vector recall, git-notes decisions and daily logs, run through an npm CLI. |

All 1 indexed listings appear in the table above.

## Why This Matters for Hermes Agents

The transferable idea here is the write-ahead-log protocol: write the decision to state before responding, not after. If an agent replies first and crashes before saving, the context is gone; writing first makes the state durable across a crash or compaction. The five-layer model the README describes (hot RAM session state, warm vector store for semantic recall, cold git-notes for permanent decisions, a curated archive, and optional cloud sync) is a reasonable decomposition for persistent agent memory. Mem0 auto-extraction is the token-economy piece, turning conversation facts into retrievable entries rather than replaying everything. For a Hermes agent, the pattern maps onto the existing memory system, and this skill is a compact, agent-agnostic implementation to read rather than a platform to adopt. Note the scale: 16 stars and a last push of 2026-01-30 make this a reference implementation, not a maintained dependency.

## Usage

| You say | What happens |
|---|---|
| "Remember we are using Tailwind for this project" | Writes the decision to SESSION-STATE.md before responding (WAL protocol). |
| "What do we remember about this project?" | Recalls relevant memories through vector search. |
| "Set up daily memory logs" | Runs elite-memory today to create today's log. |
| "Check my memory health" | Runs elite-memory status. |
| "Auto-extract facts from our conversations" | Uses the Mem0 integration, adding facts with a user id and searching them back. |
| "Sync memory across devices" | Uses the optional SuperMemory cloud layer. |

## Verification

The raw path below returned 200 on branch main on 2026-11-27:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/nextfrontierbuilds/elite-longterm-memory/main/SKILL.md
```

Confirm the package wiring, which maps the elite-memory bin to bin/elite-memory.js and lists mem0ai as an optional dependency:

```bash
curl -sL https://raw.githubusercontent.com/nextfrontierbuilds/elite-longterm-memory/main/package.json
```

## Security

skills.sh verdicts for sampled skills (verified 2026-11-27) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| elite-longterm-memory | Pass | Pass | Pass |

The single listing passes all three auditors. The repository ships one JavaScript file (bin/elite-memory.js) and a package.json with an optional mem0ai dependency, so the runtime surface is small. Mem0 is the one external service in the chain; using it sends conversation facts to a third party and needs a MEM0_API_KEY. The optional SuperMemory cloud layer is the other data boundary if you enable sync.

## Limitations

- Snapshot data, verified 2026-11-27: 2,396 combined installs across 1 indexed listing; 16 GitHub stars; no LICENSE file; last pushed 2026-01-30. Counts drift over time.
- The repository is very small (16 stars) and last pushed 2026-01-30, roughly ten months before this sweep; treat it as a pattern reference rather than an actively maintained dependency.
- The repository has no LICENSE file even though package.json and the README badge claim MIT. The npm package is MIT, but the repository tree carries no license text.
- The tree is thin: four files, and the README's described layers (LanceDB vector store, git-notes graph, SuperMemory sync, Mem0 extraction) are instructions in SKILL.md rather than shipped implementation. The package.json files list references a templates/ directory that is not in the tree.
- The install count is a single listing; there is no separate sub-skill set to spread the risk or the maintenance load.

## Related

- [AgentMemory Setup - Persistent Memory for Hermes Agents](/hermes/skills/catalog/agentmemory-setup)
- [Hermes Advanced Memory Setup](/hermes/skills/catalog/hermes-advanced-memory-setup)
- [Honcho Integration Setup](/hermes/skills/catalog/honcho-integration-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Treat WAL as the transferable idea: write the decision to state before responding, even if you adopt none of this skill's files.
- Run elite-memory status before trusting the memory system after a crash or compaction.
- Gate Mem0 behind an explicit key; without MEM0_API_KEY the auto-extraction path is inert.
- Adopt the daily-log habit (elite-memory today) only if a human will read it; otherwise keep vectors lean to avoid token waste.
- Prefer an established memory system for production; this repo is a compact, readable reference implementation rather than a maintained platform.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
