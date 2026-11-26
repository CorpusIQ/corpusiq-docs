---
title: "Claude Elixir Phoenix - Elixir/Phoenix Plugin Setup"
description: "oliver-kriska/claude-elixir-phoenix - 3.6K combined installs: Claude Code plugin with 26 specialist agents and 51 Elixir/Phoenix/LiveView skills."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/claude-elixir-phoenix-setup/"
robots: "index,follow"
last_updated: "2026-11-26"
tags: ["hermes skill", "agent skill", "skill setup", "elixir", "phoenix", "claude code"]
---

# Claude Elixir Phoenix - Setup Guide

**Source:** [oliver-kriska/claude-elixir-phoenix](https://www.skills.sh/oliver-kriska/claude-elixir-phoenix) via skills.sh - 3.6K combined installs across 96 indexed listings; first catalogued Nov 26, 2026 (Nov 26, 2026 morning sweep)
**GitHub:** [oliver-kriska/claude-elixir-phoenix](https://github.com/oliver-kriska/claude-elixir-phoenix) - 578 stars, MIT license, last pushed Nov 20, 2026, main branch; a Claude Code plugin with 26 specialist agents, 51 canonical skills, 140 reference files, 30 hook registrations, and 26 Iron Laws across 1,942 tree files.
**Category:** Backend Web Development (Claude Code / Elixir / Phoenix)
**Quality Tier:** 🟠 Orange - 12 of 96 listings sampled: the security skill carries a Gen Agent Trust Hub Fail plus a Socket Warn, and three others carry Warns.

oliver-kriska/claude-elixir-phoenix is a Claude Code plugin for Elixir, Phoenix, and LiveView that coordinates 26 specialist agents to plan, implement, review, and verify code, with enforced Iron Laws that catch the bugs tests miss (assign_new silently skipping on reconnect, :float corrupting money fields, non-idempotent Oban jobs). Nine workflow commands drive the loop: /phx:plan, /phx:work, /phx:review, /phx:verify, /phx:compound, /phx:quick, /phx:brief, /phx:triage, and /phx:full, plus the /ecto:* and /lv:* compatibility namespaces.

The main plugin lives under plugins/elixir-phoenix/ with its agents/, skills/, hooks/, and settings.json. Around it sit companion plugins (catchup, ecto, lv, rewrite), contributor tools under .claude/skills/ and .claude/agents/, generated skill distributions under targets/ for Amp, Codex, Pi, OpenCode, and DeepSeek Harness, and a lab/ evaluation harness. skills.sh indexes 96 listings, which includes every phx:* workflow command alongside its base skill, so the listing count exceeds the 51 canonical skills.

## Installation

Install as a Claude Code plugin from the marketplace:

```bash
# In Claude Code, add the marketplace
/plugin marketplace add oliver-kriska/claude-elixir-phoenix

# Install the plugin
/plugin install elixir-phoenix
```

Requires Claude Code 2.1.110 or newer. The install name stays elixir-phoenix while the public workflow commands remain /phx:*, and a fresh install pulls in the /ecto:* and /lv:* compatibility namespaces automatically. After an update, run /reload-plugins before using the commands in an already-open session. Generated skills-only distributions exist for Amp, Codex, Pi, OpenCode, and DeepSeek Harness under targets/.

## What It Provides

skills.sh publishes per-skill install counts for all 96 indexed listings. The 11 most-installed listings are listed below; the remaining 85 are summarized under the table.

| Skill | Installs | Use For |
|---|---|---|
| oban | 100 | write, schedule, test, and debug Oban jobs (workers, cron, retries, unique jobs, Pro Workflow) |
| liveview-patterns | 77 | build LiveView with assign_async, PubSub, phx-change, form components, streams, and live_patch |
| phoenix-contexts | 73 | design and split Phoenix contexts, Scope (1.8+), Ecto.Multi, routers, plugs, and controllers |
| tidewave-integration | 73 | use Tidewave MCP runtime tools for debugging, smoke testing, and live state inspection |
| ecto-patterns | 73 | schemas, changesets, validations, queries, preloads, Multi, migrations, and constraints |
| testing | 71 | write and repair ExUnit tests with Mox, ExMachina, LiveViewTest, and async reliability |
| security | 70 | harden Phoenix auth and security (OAuth, hashing, sessions, RBAC, rate limiting, CSRF, XSS) |
| hexdocs-fetcher | 66 | fetch HexDocs for Elixir libraries with HTML-to-markdown conversion |
| elixir-idioms | 65 | OTP/BEAM patterns and Elixir idioms (GenServer, Supervisor, Task, pattern matching, pipes) |
| docs-check | 61 | validate the plugin against the latest Claude Code docs (contributor tool, not distributed) |
| ecto-constraint-debug | 60 | debug Ecto constraint violations (unique, foreign key, and check constraints) |

The remaining 85 indexed listings range from 16 to 58 installs.

## Why This Matters for Hermes Agents

The suite encodes Elixir and Phoenix domain knowledge that a general coding agent gets wrong in production: LiveView reconnect semantics, Ecto changeset and constraint pitfalls, Oban idempotency and retries, and BEAM process design. The parallel-agent loop is what makes it more than a skills bundle: /phx:plan runs four research agents, /phx:work compiles after each change and stops cold on an Iron Law violation, and /phx:review runs four specialist audits in parallel before deduplicating findings. For an agent, that replaces "please check for N+1 queries" with deterministic gates. The deps-audit and deps-vet skills add real supply-chain value, scanning Hex dependencies for CVEs and malware. The trade-offs are the Fail verdict on the security skill, the size of the tree (1,942 files), and that the 96 listings inflate the count because each phx:* command is indexed beside its base skill.

## Usage

| You say | What happens |
|---|---|
| Plan a feature | Uses /phx:plan to run 4 research agents in parallel and write a structured plan |
| Implement the plan | Uses /phx:work to implement task by task and compile after each change |
| Review my changes | Uses /phx:review to run 4 specialist agents in parallel (idioms, security, tests, compilation) |
| Debug an Ecto constraint error | Uses ecto-constraint-debug to trace triggers, migrations, and duplicate data |
| Write or fix tests | Uses testing for ExUnit, Mox, ExMachina, and LiveViewTest |
| Check for N+1 queries | Uses n1-check to find and fix missing preloads |
| Audit my dependencies | Uses deps-audit to scan Hex dependencies for CVEs and malware |

## Verification

Confirm the README and a representative skill body resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/oliver-kriska/claude-elixir-phoenix/main/README.md | head -40
curl -sL https://raw.githubusercontent.com/oliver-kriska/claude-elixir-phoenix/main/plugins/elixir-phoenix/skills/oban/SKILL.md | head -40
```

Both URLs return 200. After installing, review each plugins/elixir-phoenix/skills/<name>/SKILL.md before relying on it, and re-check the security pages on skills.sh for the Fail and Warn verdicts noted below.

## Security

skills.sh verdicts for sampled skills (verified Nov 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| oban | Pass | Pass | Pass |
| liveview-patterns | Pass | Warn | Pass |
| phoenix-contexts | Pass | Pass | Pass |
| tidewave-integration | Pass | Warn | Pass |
| ecto-patterns | Pass | Pass | Pass |
| testing | Pass | Pass | Pass |
| security | Fail | Warn | Pass |
| hexdocs-fetcher | Pass | Pass | Warn |
| elixir-idioms | Pass | Pass | Pass |
| docs-check | Pass | Pass | Pass |
| ecto-constraint-debug | Pass | Pass | Pass |
| deploy | Pass | Pass | Pass |

Across the 12 sampled skills there are 31 Pass, 4 Warn, and 1 Fail cells. The security skill carries the single Fail (Gen Agent Trust Hub) plus a Socket Warn; liveview-patterns and tidewave-integration carry Socket Warns, and hexdocs-fetcher carries a Snyk Warn.

## Limitations

- Snapshot data, verified Nov 26, 2026: 3,602 combined installs across 96 indexed listings; 578 GitHub stars; MIT license; last pushed Nov 20, 2026. Counts drift over time.
- The repository is a large Claude Code plugin: 1,942 tree files spanning the main plugin (26 agents, 51 skills, hooks), companion plugins (catchup, ecto, lv, rewrite), contributor tools, and generated distributions for five other runtimes.
- skills.sh sampled only 12 of the 96 indexed listings; the other 84 carry no published verdict.
- The security skill carries the sample's only Fail (Gen Agent Trust Hub) plus a Socket Warn; read its skills.sh page before relying on the auth and hardening guidance.
- The 96 listings exceed the 51 canonical skills because each phx:* workflow command is indexed alongside its base skill, and install counts sit in a narrow band from 16 to 100.

## Related

[Laravel Boost - Laravel AI Development Setup](/hermes/skills/catalog/laravel-boost-setup) | [Rails Skills - Ruby on Rails Agent Suite Setup](/hermes/skills/catalog/rails-skills-setup) | [Obra Superpowers - Engineering Workflow Skills](/hermes/skills/catalog/obra-superpowers-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run /phx:plan before touching code; the plan lands in .claude/plans/ and gives /phx:work a file to execute from.
- The plugin stops cold when code violates one of the 26 Iron Laws; read them at phxagents.dev before relying on the auto-enforcement.
- After a plugin update, run /reload-plugins before using the commands in an already-open session.
- The security skill carries the sample's only Fail verdict; review its skills.sh page before letting an agent follow its auth guidance.
- For non-Claude runtimes, the targets/ tree ships generated skills-only distributions, not full plugin feature parity.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
