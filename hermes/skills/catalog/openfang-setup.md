---
title: "OpenFang Skills - Agent Operating System Setup Guide"
description: "rightnow-ai/openfang: OpenFang's 60 bundled agent skills and autonomous Hands from a Rust agent operating system - 9.5K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/openfang-setup/"
robots: "index,follow"
last_updated: "2026-11-20"
tags: ["hermes skill", "agent skill", "skill setup", "agent operating system", "autonomous agents", "rust"]
---

# OpenFang Skills - Setup Guide

**Source:** [rightnow-ai/openfang](https://www.skills.sh/rightnow-ai/openfang) via skills.sh - 9.5K combined installs across 70 indexed listings; first seen Nov 20, 2026 (Nov 20, 2026 morning sweep)
**GitHub:** [rightnow-ai/openfang](https://github.com/rightnow-ai/openfang) - 18,270 stars, Apache-2.0 per GitHub metadata (the README states MIT and the repo ships both LICENSE-APACHE and LICENSE-MIT), main branch, last pushed Jul 2, 2026. Skills live under `crates/openfang-skills/bundled/<name>/SKILL.md` (60 bundled skills) plus autonomous Hands under `crates/openfang-hands/bundled/<name>/SKILL.md`.
**Category:** Agent Operating Systems
**Quality Tier:** 🟡 Yellow - 1 Warn among 20 sampled verdicts (Snyk: web-search); Apache-2.0 licence.

OpenFang is a Rust agent operating system from RightNow AI that compiles to a single roughly 32 MB binary across 14 crates and 137K lines of code, with 40 messaging-channel adapters and a Tauri desktop app. The skills.sh index covers 70 listings that map to the repository's 60 bundled domain skills (under `crates/openfang-skills/bundled/`) plus its Hands, the autonomous capability bundles that run on schedules without prompting.

The bundled skills compile into the binary, so there is no separate per-skill download or install step. The README documents the platform install flow and the Hands lifecycle, and the project reads SKILL.md natively while remaining compatible with the ClawHub marketplace for additional skills. The project is pre-1.0; the README advises pinning to a specific commit for production use until v1.0.

## Installation

OpenFang installs as one binary, and the bundled skills ship inside it (no pip, npm or Docker pull). Install on macOS/Linux:

```bash
curl -fsSL https://openfang.sh/install | sh
openfang init
openfang start
# Dashboard live at http://localhost:4200
```

Windows (PowerShell):

```powershell
irm https://openfang.sh/install.ps1 | iex
openfang init
openfang start
```

Activate a Hand (an autonomous capability bundle that starts working immediately):

```bash
openfang hand activate researcher
openfang hand status researcher
openfang hand list
```

To move an existing OpenClaw setup (agents, memory, skills, configs):

```bash
openfang migrate --from openclaw
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| sqlite-expert | 415 | SQLite: WAL mode, query optimization, embedded patterns and advanced features |
| pdf-reader | 358 | PDF content extraction and analysis |
| ansible | 237 | Ansible playbooks, roles, inventories and infrastructure management |
| sysadmin | 236 | System administration across Linux, macOS and Windows: services and monitoring |
| css-expert | 234 | CSS: flexbox, grid, animations, responsive design and modern layouts |
| linux-networking | 229 | Linux networking: iptables, nftables, routing, DNS and troubleshooting |
| openapi-expert | 183 | OpenAPI/Swagger API specification design, validation and code generation |
| web-search | 177 | Web search and research: finding and synthesizing information |
| python-expert | 170 | Python: stdlib, packaging, type hints, async/await and performance |
| postgres-expert | 162 | PostgreSQL query optimization, indexing, extensions and administration |
| project-manager | 158 | Project management: Agile, estimation, risk and stakeholder communication |
| docker | 154 | Docker containers, Compose, Dockerfiles and debugging |
| regex-expert | 153 | Regular expressions: crafting, debugging and explaining patterns |

The remaining 57 indexed listings range from 81 to 149 installs (interview-prep 149, nginx 147, ci-cd 147, redis-expert 146, golang-expert 138 and others).

## Why This Matters for Hermes Agents

Most agent skill collections are just prompt files; this one ships inside a working agent operating system, so the skills describe real, exercised workflows rather than untested advice. The bundled set covers the two places agents most often need a reference: infrastructure (Ansible, Docker, Kubernetes, Terraform, Nginx, networking) and deep single-topic expertise (SQLite, PostgreSQL, Redis, Python, Go, Rust, OpenAPI). For a Hermes agent, the value is a compact, curated library of domain references that can be loaded one at a time rather than a single large context dump. The Hands are a separate idea worth studying: each pairs a SKILL.md with a manifest, a multi-phase playbook and approval guardrails, so a capability runs autonomously but stays gated on sensitive actions. The project is Rust, pre-1.0, and MIT/Apache dual-licensed, which matters if you plan to vendor or redistribute the skill text. Its security posture (WASM sandbox, taint tracking, signed manifests, rate limiting) is unusually deep for a skill source, and the sampled skills.sh verdicts are nearly all Pass.

## Usage

| You say | What happens |
|---|---|
| Activate a Hand that researches competitors each morning | `openfang hand activate researcher` starts the autonomous Researcher Hand |
| Optimize a slow SQLite query | The sqlite-expert skill applies WAL mode and query-optimization guidance |
| Debug a broken Nginx reverse proxy | The nginx skill walks TLS, proxy and performance configuration |
| Write an Ansible playbook for a new role | The ansible skill covers playbooks, roles, inventories and management |
| Extract text and tables from a PDF | The pdf-reader skill handles content extraction and analysis |
| Harden a Linux server | The sysadmin and linux-networking skills cover services, monitoring, iptables and DNS |
| Plan a sprint and estimate the work | The project-manager skill covers Agile, estimation and risk |

## Verification

```bash
# start the daemon and confirm its bundled skills are live
openfang start
openfang hand list
# review a bundled SKILL.md before relying on it
curl -sL https://raw.githubusercontent.com/rightnow-ai/openfang/main/crates/openfang-skills/bundled/sqlite-expert/SKILL.md
```

The raw SKILL.md URL above was probed Nov 20, 2026 and returned HTTP 200. Bundled skills are compiled into the binary, so there is no per-skill install directory to list; `openfang hand list` confirms the Hands the daemon exposes.

## Security

skills.sh verdicts for sampled skills (verified Nov 20, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| sqlite-expert | Pass | Pass | Pass |
| pdf-reader | Pass | Pass | Pass |
| ansible | Pass | Pass | Pass |
| sysadmin | Pass | Pass | Pass |
| css-expert | Pass | Pass | Pass |
| linux-networking | Pass | Pass | Pass |
| openapi-expert | Pass | Pass | Pass |
| web-search | Pass | Pass | Warn |
| python-expert | Pass | Pass | Pass |
| postgres-expert | Pass | Pass | Pass |
| project-manager | Pass | Pass | Pass |
| docker | Pass | Pass | Pass |
| regex-expert | Pass | Pass | Pass |
| interview-prep | Pass | Pass | Pass |
| nginx | Pass | Pass | Pass |
| ci-cd | Pass | Pass | Pass |
| redis-expert | Pass | Pass | Pass |
| code-reviewer | Pass | Pass | Pass |
| sql-analyst | Pass | Pass | Pass |
| golang-expert | Pass | Pass | Pass |

## Limitations

- Snapshot data, verified Nov 20, 2026: 9,482 combined installs across 70 indexed listings; 18,270 GitHub stars; Apache-2.0 licence; last pushed Jul 2, 2026. Counts drift over time.
- The repository's last push was Jul 2, 2026, more than four months before this sweep; the project is pre-1.0 (v0.5.10) and the README advises pinning to a specific commit for production use.
- OpenFang is a full agent operating system (14 crates, 137K LOC, 40 channel adapters, a Tauri desktop app); the 70 indexed skill listings are its bundled skill library plus Hands, a smaller part of the platform.
- The licence is stated differently in each source: GitHub metadata says Apache-2.0, the README says MIT, and the repo ships both LICENSE-APACHE and LICENSE-MIT files.
- Only 20 of 70 listings have skills.sh verdicts; the other 50 are unverified on that platform.
- The install index uses marketplace names (browser-automation, trader-hand-skill) while the repo tree uses the Hand directory names (browser, trader).

## Related

- [OpenClaw Agent Skills - Official OpenClaw Org Skill Suite Setup](/hermes/skills/catalog/openclaw-agent-skills-setup)
- [ClawHub Skill Vetting - Security Scanner Setup](/hermes/skills/catalog/clawhub-skill-vetting-setup)
- [Claw Multi-Agent Skill Setup](/hermes/skills/catalog/claw-multi-agent-setup)
- [Openclaw Skill Vetter Setup](/hermes/skills/catalog/openclaw-skill-vetter-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with the Hands (`openfang hand activate researcher`) before drilling into individual skills; the Hands bundle SKILL.md with a manifest, playbook and approval guardrails.
- Treat the bundled skills as references for a specific task, not a bulk import; each covers one domain and loads independently.
- Review the sqlite-expert SKILL.md first: it is the most-installed listing and a good sample of the house style.
- Pin to a commit for production until v1.0; the README explicitly warns of breaking changes between minor versions.
- If you already run OpenClaw, use `openfang migrate --from openclaw` to move agents, memory, skills and configs, then verify the migrated skills still resolve.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
