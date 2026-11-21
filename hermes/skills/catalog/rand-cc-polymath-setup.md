---
title: "CC Polymath - Atomic Skills Discovery Setup Guide"
description: "rand/cc-polymath: 410+ atomic Claude Code skills with progressive discovery gateways - 4.3K combined installs for context-efficient development."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/rand-cc-polymath-setup/"
robots: "index,follow"
last_updated: "2026-11-20"
tags: ["hermes skill", "agent skill", "skill setup", "claude code", "atomic skills", "skill discovery"]
---

# CC Polymath - Atomic Skills Discovery Setup Guide

**Source:** [rand/cc-polymath](https://www.skills.sh/rand/cc-polymath) via skills.sh - 4.3K combined installs across 46 indexed listings; first seen Nov 20, 2026 (Nov 20, 2026 evening sweep)
**GitHub:** [rand/cc-polymath](https://github.com/rand/cc-polymath) - 193 stars, MIT license, main branch, last pushed Feb 28, 2026; 2,163 files including 23 discover-* gateway Agent Skills under `skills/discover-*/SKILL.md`, category indexes under `skills/<category>/INDEX.md`, individual skills under `skills/<category>/<skill>.md`, and an MCP server under `mcp-server/`.
**Category:** Claude Code Skills / Skill Discovery
**Quality Tier:** 🟢 Green - all 20 sampled verdicts Pass across Gen Agent Trust Hub, Socket and Snyk.

`cc-polymath` is an atomic-skill index from Rand Lee for Claude Code. Each skill is a small, self-contained discovery entry that routes an agent to deeper references instead of dumping the whole catalog into context on boot. It solves the context-vs-coverage tradeoff: loading every skill upfront burns tens of thousands of tokens before any real work begins, while loading nothing leaves the agent without the patterns it needs. The repository ships 410+ atomic skills behind 23 discover-* gateway Agent Skills that activate on task keywords, plus category indexes and on-demand individual skill files.

The repo is MIT-licensed and installs as a Claude Code plugin. Gateways are roughly 200 lines each and act as entry points that point into category indexes, which in turn point at individual skills. The README counts 410+ atomic skills, 23 gateway Agent Skills and 30+ categories, all CI-validated, while skills.sh indexes 46 listings totaling 4,294 combined installs.

## Installation

Install as a Claude Code plugin, either from the marketplace or straight from GitHub:

```bash
/plugin marketplace add rand/cc-polymath
/plugin install cc-polymath@cc-polymath
```

```bash
/plugin install https://github.com/rand/cc-polymath
```

All 410+ skills and the `/skills` command become available immediately. For local development, clone the repo and install from a local path with `/plugin install /path/to/cc-polymath`. Your first commands after install:

```bash
/skills                      # see what's recommended for your project
/discover-frontend           # load React, Next.js, TypeScript skills (example)
bash scripts/verify-install.sh  # verify installation
```

## What It Provides

| Skill | Installs | Purpose |
|---|---|---|
| anti-slop | 801 | detect and remove generic AI-generated patterns in text, code and design |
| discover-frontend | 218 | gateway to React, Next.js, UI, accessibility and SEO skills |
| discover-research | 203 | gateway to research methodology and evidence synthesis skills |
| elegant-design | 188 | world-class accessible interfaces with chat, terminals and streaming |
| discover-math | 148 | gateway to linear algebra, optimization, statistics and topology skills |
| discover-ml | 136 | gateway to DSPy, HuggingFace, RAG, fine-tuning and diffusion skills |
| discover-database | 127 | gateway to Postgres, MongoDB, Redis, schema and query skills |
| discover-networking | 122 | gateway to TCP, mTLS, NAT, Tailscale and resilience skills |
| discover-cryptography | 120 | gateway to TLS, certificates, PKI and encryption skills |
| discover-wasm | 119 | gateway to WebAssembly, WASI and Rust-to-WASM skills |
| discover-api | 115 | gateway to REST, GraphQL, auth, OAuth and rate-limiting skills |
| discover-engineering | 113 | gateway to code review, profiling and deployment strategy skills |
| discover-cicd | 111 | gateway to GitHub Actions, Jenkins and pipeline skills |
| discover-zig | 110 | gateway to Zig build systems, allocators and C interop skills |
| discover-security | 109 | gateway to authentication, OWASP, headers and secrets skills |
| discover-product | 106 | gateway to PRD writing and product management skills |
| discover-debugging | 106 | gateway to GDB, LLDB, profiling and core-dump skills |
| discover-testing | 103 | gateway to unit, integration, e2e and TDD skills |
| discover-data | 101 | gateway to ETL, streaming, batch and pipeline skills |

The remaining 27 indexed listings fall between 22 and 99 installs each and are not shown in the table above.

## Why This Matters for Hermes Agents

This library is a direct answer to the failure mode of a bloated agent context. Its whole design is progressive discovery: start with zero skills loaded, activate a small gateway on the task's keywords, then descend through a category index into only the individual skills the work actually needs. The README claims a 60-84% context reduction versus loading a monolithic index on boot, which leaves more tokens for the actual code and conversation. For a Hermes agent that already juggles skills and memory, that model is portable: the 23 gateway skills show how to keep a large knowledge base discoverable without paying for it on every turn. The atomic style, roughly 320 lines per skill with a single responsibility, also makes individual skills cheap to load and compose, so an agent pulls a focused reference instead of an 8K-token guide.

## Usage

| You say | What happens |
|---|---|
| /skills | Lists the skills recommended for the current project |
| "REST API with PostgreSQL" | discover-api and discover-database gateways activate automatically |
| /discover-frontend | Loads the frontend gateway with quick reference and loading commands |
| cat skills/database/INDEX.md | Shows all database skills with descriptions and decision trees |
| cat skills/api/rest-api-design.md | Loads the full REST design guide on demand |
| Mention "Zig" or "comptime" | discover-zig gateway activates for systems programming |

## Verification

```bash
# after install, confirm the gateway files are present
ls skills/discover-frontend/SKILL.md
# review one gateway before relying on it
curl -sL https://raw.githubusercontent.com/rand/cc-polymath/main/skills/discover-frontend/SKILL.md
```

The raw SKILL.md URL above was probed Nov 20, 2026 and returned HTTP 200. Gateway skills live under `skills/discover-*/SKILL.md` and are small discovery entries that point at category indexes and individual skills; `bash scripts/verify-install.sh` checks the installation end to end.

## Security

skills.sh verdicts for sampled skills (verified Nov 20, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| anti-slop | Pass | Pass | Pass |
| discover-frontend | Pass | Pass | Pass |
| discover-research | Pass | Pass | Pass |
| elegant-design | Pass | Pass | Pass |
| discover-math | Pass | Pass | Pass |
| discover-ml | Pass | Pass | Pass |
| discover-database | Pass | Pass | Pass |
| discover-networking | Pass | Pass | Pass |
| discover-cryptography | Pass | Pass | Pass |
| discover-wasm | Pass | Pass | Pass |
| discover-api | Pass | Pass | Pass |
| discover-engineering | Pass | Pass | Pass |
| discover-cicd | Pass | Pass | Pass |
| discover-zig | Pass | Pass | Pass |
| discover-security | Pass | Pass | Pass |
| discover-product | Pass | Pass | Pass |
| discover-debugging | Pass | Pass | Pass |
| discover-testing | Pass | Pass | Pass |
| discover-data | Pass | Pass | Pass |
| typed-holes-refactor | Pass | Pass | Pass |

## Limitations

- Snapshot data, verified Nov 20, 2026: 4,294 combined installs across 46 indexed listings; 193 GitHub stars; MIT license; last pushed Feb 28, 2026. Counts drift over time.
- The repo was last pushed Feb 28, 2026, roughly nine months before this snapshot, so gateway coverage and individual skills may lag current tooling and frameworks.
- The skills.sh index lists 43 discover-* gateway entries, but the main-branch tree ships only 23 `discover-*/SKILL.md` files; the 20 missing names sit in the 37-installs-or-fewer tail, while every shipped gateway has 73 or more installs, so low-traffic gateways may be index-only.
- Only 20 of the 46 indexed listings carry skills.sh verdicts; the other 26 are unverified on that platform.
- The README advertises 410+ atomic skills, but skills.sh indexes only 46 listings, so the install totals reflect a small fraction of the full tree.

## Related

- [UI Skills - Design Engineer Skill Registry Setup](/hermes/skills/catalog/ibelick-ui-skills-setup)
- [Design Review - UI Critique Setup](/hermes/skills/catalog/design-review-setup)
- [Frontend God Mode - Frontend Skills Setup](/hermes/skills/catalog/frontend-god-mode-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Let the gateways auto-activate from your prompt keywords instead of loading the whole index; progressive discovery is the point of the design.
- Run `/skills` first on a new project to see what is recommended before loading anything by hand.
- Browse a category index (`skills/<category>/INDEX.md`) when planning, then load only the individual skills the work needs.
- Run `bash scripts/verify-install.sh` after install to confirm the plugin landed correctly.
- Review a gateway before relying on it with a quick curl of its raw SKILL.md; the files are roughly 200 lines.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
