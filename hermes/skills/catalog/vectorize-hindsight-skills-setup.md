---
title: "Vectorize Hindsight Skills - Agent Memory Setup"
description: "vectorize-io/hindsight: 11.5K combined installs. Hindsight agent-memory skills for retain, recall and reflect, self-hosting and Hermes plugin setup."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/vectorize-hindsight-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-30"
tags: ["hermes skill", "agent skill", "skill setup", "agent memory", "retrieval", "self-hosted"]
---

# Hindsight - Setup Guide

**Source:** [vectorize-io/hindsight](https://www.skills.sh/vectorize-io/hindsight) via skills.sh - 11.5K combined installs across 15 indexed listings; first seen 2026-10-30 (morning sweep)

**GitHub:** [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) - 56,373 stars, MIT License, branch main, last pushed 2026-10-30; 20 `SKILL.md` files in the checkout across four layouts, `skills/<name>/SKILL.md` for the five published skills, `.claude/skills/<name>/SKILL.md` for the repository's own workflow skills, `hindsight-integrations/<host>/skills/<name>/SKILL.md` for the per-host memory skills, and `hindsight-docs/static/skills/openbot/hindsight-memory/SKILL.md` inside the docs site

**Category:** Long-term agent memory, retrieval and self-hosted deployment

**Quality Tier:** 🟡 1 sampled FAIL verdict(s) in the security table; review before install - the install index covers the two published memory skills plus the documentation skill, and the checkout also carries a Hermes memory-provider plugin

Hindsight is Vectorize.io's agent memory system, and the repository is its whole surface: server, SDKs, 60+ integrations and the agent skills that teach a coding agent how to use them. The README frames the product as biomimetic memory rather than conversation recall, with four memory types (world facts, experiences, consolidated observations and mental models), isolated memory banks with disposition traits, and three operations an agent actually calls, `retain`, `recall` and `reflect`. Recall fans out across semantic, BM25 keyword, graph and temporal retrieval and merges the results with reciprocal rank fusion plus a cross-encoder reranker; every server ships an MCP endpoint per bank at `http://localhost:8888/mcp/{bank_id}/`, and 25+ LLM providers are supported, including local ones through `ollama`, `lmstudio` and `llamacpp`.

What makes this pack unusual is that it is not a skills-only repository. The checkout carries 20 `SKILL.md` files in four families: five published skills under `skills/`, the maintainers' own workflow skills under `.claude/skills/`, per-host memory skills under `hindsight-integrations/` for Cursor and its Grok bots, and a copy of the OpenBot variant inside the docs site. It also ships a first-class Hermes memory-provider plugin at `hindsight-integrations/hermes`, which moved out of the Hermes core tree and is now installed from the plugin catalog at a reviewed commit pin. skills.sh indexes 15 listings for 11.5K combined installs, three of which clear the 500-install threshold, and the index does not track the tree one to one: `create-agent` and `agent-knowledge` carry install counts but have no directory of that name in the current checkout.

## Installation

The README's only skills-CLI line covers the documentation skill, and it is the shortest way to give an agent Hindsight knowledge in a code session:

```bash
npx skills add https://github.com/vectorize-io/hindsight --skill hindsight-docs
```

The README documents no skills-CLI command for `hindsight-self-hosted`, `hindsight-local` or the per-host variants, so for those the durable route is a directory copy into this profile. Copy the whole directory, not the markdown alone:

```bash
cp -R /path/to/hindsight/skills/hindsight-docs ~/.hermes/profiles/corpusiq/skills/
cp -R /path/to/hindsight/skills/hindsight-self-hosted ~/.hermes/profiles/corpusiq/skills/
cp -R /path/to/hindsight/skills/hindsight-local ~/.hermes/profiles/corpusiq/skills/
```

`hindsight-docs` is the one where the copy matters most: its `references/` tree holds 163 files, including `best-practices.md`, `faq.md`, `openapi.json` and the changelog by integration. Copying only `SKILL.md` leaves the agent describing documentation it cannot open.

The third route is the one this profile should lead with. The repository ships a Hermes memory-provider plugin, and its own README documents the install:

```bash
hermes plugins install hindsight
hermes memory setup
```

`hermes plugins install` asks for confirmation before enabling, so pass `--enable` in a script or an unattended run. `hermes plugins enable` is not what activates a memory provider, because Hermes treats providers as exclusive and activates them through `memory.provider: hindsight` in `config.yaml`, which `hermes memory setup` writes. The manual equivalent is `hermes config set memory.provider hindsight`, plus `HINDSIGHT_API_KEY` in `~/.hermes/.env` for cloud mode.

CLI coding agents have their own package, and the README documents both directions of it:

```bash
npx @vectorize-io/hindsight-coding-agents install all          # every detected agent, wired natively
npx @vectorize-io/hindsight-coding-agents uninstall all        # removes exactly what install added
```

That package wires Claude Code, Codex CLI, Cursor CLI, GitHub Copilot CLI, opencode, Kilo, Cline, Antigravity, Devin, pi, Prime Agent, Grok Build and DeepSeek Harness. Hermes is not one of them, so on this host the plugin route is the install and the coding-agents package is a reference for how the per-repo bank is meant to behave.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| hindsight-docs | 9,326 | Complete Hindsight documentation inline in a coding session: architecture and core concepts, the retain, recall and reflect contracts, bank and disposition configuration, server deployment on Docker, Helm or pip, SDK usage, retrieval strategies and the OpenAPI spec, all backed by a 163-file references tree. |
| hindsight-self-hosted | 532 | Team memory against a server you run: verify `~/.hindsight/config`, install the CLI when the command is missing, then retain, recall and reflect against a named bank that other agents on the same repository also read and write. |
| hindsight-local | 501 | Per-user memory through the `hindsight-embed` CLI: check `uvx hindsight-embed daemon status`, run the interactive configure step for an LLM provider, then retain rich context under labels such as procedures and learnings, recall before a task and reflect to synthesize what it already knows. |

The remaining 12 indexed listings range from 1 to 282 installs.

## Why This Matters for Hermes Agents

The reason to read this repository before any other memory pack is that it already contains a Hermes provider. At `hindsight-integrations/hermes` there is a plugin that registers `hindsight_retain`, `hindsight_recall` and `hindsight_reflect`, recalls memory in the background before a turn and retains the turn afterwards, so an agent profile gets continuity without a single prompt change. The skills layer sits on top of that: it teaches the agent when to store, what to store and how to read a bank back.

The bank model is the part that fits how Hermes runs. A profile resolves exactly one config, and banks are selected through `bank_id_template` placeholders for profile, workspace, project, platform, user and session, so `hermes-{profile}` isolates a profile while `{project}` gives each git repository its own brain. `trusted_project_dirs` is empty by default on purpose, which means a repository you clone cannot redirect your memory through its own `.hindsight/config.toml` until you name its folder.

Two defaults are worth knowing before you wire memory into an autonomous loop. Retention is automatic per turn, but subagent runs and kanban workers are never auto-retained and `retain_cron` is off by default while the retain tool still works from a cron; recall surfaces observations only, not the raw world and experience facts behind them, and `recall_min_scores` with `{"reranker": 0.25}` is the documented way to turn an off-topic bank into an empty recall instead of a page of least-bad hits.

Finally, the local mode removes the credential problem. `local_embedded` runs the Hindsight server as a separate process, either an installed `hindsight-api` binary or a `uvx hindsight-api` fallback with its own environment, and the Hermes venv keeps only the client and embed packages. That means a workstation profile can have durable memory backed by an embedded PostgreSQL instance with one LLM key and no hosted account.

## Usage

| You say | What happens |
|---|---|
| "Remember that this repo's tests only pass with NODE_ENV=test" | The memory skill retains the full observation with a `procedures` or `learnings` label rather than a tidy summary, because the server extracts entities, facts and temporal links itself on the way in. |
| "What did we decide about the billing bank schema?" | `memory-reflect` or `hindsight_reflect` reasons across stored memories and answers with the decision and its context instead of running a keyword search over the conversation. |
| "Point my memory at our own Hindsight server" | `hindsight-self-hosted` checks `~/.hindsight/config`, installs the CLI with the documented `get-cli` one-liner, writes the URL and key with `chmod 600`, then asks for the bank id it should use. |
| "How do I back a bank up, or run this on Oracle?" | `hindsight-docs` answers from `references/developer/`, citing storage, configuration hierarchy, monitoring and the admin CLI rather than guessing at flags. |
| "Design memory for our support agent" | `hindsight-architect` inspects the project for existing Hindsight config and returns an implementation plan with bank config, tag schema and code, and says plainly that it will not write the code itself. |
| "Each nightly run should pick up where the last one stopped" | `routine-memory` writes the recall and retain steps into the routine's own instructions, then on every run recalls the last run note and retains what changed plus what the next run should check first. |
| "Hand this half-finished migration to the other agent" | `bot-handoff` retains a durable handoff record to the shared bank, tagged so the next bot can find it even though it never saw this conversation. |

## Verification

All three raw paths below returned 200 on branch main when this guide was written on 2026-10-30:

```bash
curl -sL -o /dev/null -w "%{http_code} docs\n" \
  https://raw.githubusercontent.com/vectorize-io/hindsight/main/skills/hindsight-docs/SKILL.md
curl -sL -o /dev/null -w "%{http_code} self-hosted\n" \
  https://raw.githubusercontent.com/vectorize-io/hindsight/main/skills/hindsight-self-hosted/SKILL.md
curl -sL -o /dev/null -w "%{http_code} routine\n" \
  https://raw.githubusercontent.com/vectorize-io/hindsight/main/hindsight-integrations/grok-bot/skills/routine-memory/SKILL.md
```

Expect `200` three times. Read one before installing, because the description is the routing contract: `hindsight-self-hosted` names the server and the shared bank, while `hindsight-local` names the `hindsight-embed` CLI, and a Hermes profile that holds both needs that distinction to pick correctly.

After the copy lands, confirm the frontmatter and the reference tree:

```bash
head -4 ~/.hermes/profiles/corpusiq/skills/hindsight-docs/SKILL.md
ls ~/.hermes/profiles/corpusiq/skills/hindsight-docs/references
```

A good copy shows `name:` and `description:` in the frontmatter and a `references` directory holding `best-practices.md`, `faq.md`, `openapi.json`, `developer/`, `sdks/` and `changelog/`. If you took the plugin route instead, the equivalent check is `hermes memory status`, which should report `hindsight` as the active provider with `Status: available`, and `~/.hermes/hindsight/config.json` should carry the mode and bank settings the setup wizard wrote.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-30) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| hindsight-docs | Pass | Pass | Pass |
| hindsight-self-hosted | Pass | Warn | Pass |
| hindsight-local | Pass | Pass | Pass |
| hindsight-architect | Pass | Pass | Pass |
| agent-knowledge | Pass | Pass | Fail |

The one Fail in the sample is `agent-knowledge`, which is also the listing with no counterpart directory in the current checkout, so the skill you would actually install here is the one that carries no failing verdict. The two Warnings sit on `hindsight-self-hosted` (Socket) and `hindsight-local` (Snyk), both of which are memory skills that shell out to a CLI and write to a bank, and the pack records the verdict rather than the finding behind it, so read those two entries on skills.sh before install. The repository's own defensive story is Memory Defense, an opt-in per-bank policy that scans every retain for secrets and PII against 45 patterns and either redacts the match as `[REDACTED:github_token]` or blocks the item before it reaches storage. The skills repeat a hard rule of their own: never store passwords, one-time codes, API keys, card or account numbers, and never delete a bank or clear memories on the user's behalf.

The part to review on this repository is the write surface plus the network surface. Memory skills send whatever the agent decides to retain to a server that may be hosted or yours, extraction on that server is an LLM call, and `local_embedded` sends the same content to whichever provider key you configured. Banks are isolated from each other, but isolation is per bank and not per user, so a shared team bank means every agent with access reads and writes the same memory.

## Limitations

- Snapshot data, verified 2026-10-30: 11,470 combined installs across 15 indexed listings; 56,373 GitHub stars; MIT License; last pushed 2026-10-30. Counts drift over time.
- The install index and the checkout disagree in both directions. skills.sh lists 15 names against 20 `SKILL.md` files: `create-agent` (149) and `agent-knowledge` (1) have no directory of that name anywhere in the tree, `hindsight-coding-agent` (14) lives at `hindsight-integrations/coding-agents/skill/SKILL.md`, and `hindsight-memory` (3) exists twice, once under `hindsight-integrations/agent-plugin/skills/` and once as the OpenBot copy under `hindsight-docs/static/skills/`.
- Install counts do not rank these skills. One listing holds 9,326 of the 11,470, and the 12-name tail runs from 1 to 282 installs while containing the repository's own workflow skills (`code-review`, `ship-it`, `triage`, `hs-release`, `figure`), which are useful to a maintainer of this repo and mostly noise to anyone else.
- There is exactly one documented skills-CLI install. The README shows `--skill hindsight-docs` and nothing else, so every other skill is a manual directory copy or a plugin install, and there is no `--skill '*'` path to quote.
- Nothing here works without a service. The self-hosted skill needs a running Hindsight server and a bank id, the cloud variants need an API key, and `local_embedded` needs an LLM key for extraction plus the `hindsight-embed` daemon; without those the skills can only walk you through setup.
- The Hermes plugin has its own update path. `hermes update` reinstalls dependencies but does not move the plugin code, `hermes plugins update hindsight` is what moves to the catalog pin, and a `--ref` install is pinned on purpose, takes a full 40-character commit SHA and rejects tag names.

## Related

- [Qdrant Skills - Vector Search, Retrieval and Memory Setup](/hermes/skills/catalog/qdrant-skills-setup)
- [claude-mem - Persistent Memory for Coding Agents Setup](/hermes/skills/catalog/claude-mem-setup)
- [memoria-vault - Multi-Agent Research OS for Obsidian Setup](/hermes/skills/catalog/memoria-vault-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- If the goal is memory inside Hermes, install the plugin first and the skills second. The plugin gives the agent the three tools and the automatic recall and retain loop; the skills teach it when to use them.
- Name the bank before you store anything. `bank_id_template: "hermes-{profile}"` keeps profiles apart, `{project}` gives each repository its own brain, and a bank renamed later strands its memories under the old id.
- Turn off `recall_indicator` and `retain_indicator` on any customer-facing gateway. Both print a status line into the channel, which is fine in a terminal and wrong in a Telegram reply to a client.
- Set `recall_min_scores` to `{"reranker": 0.25}` once you have a bank of real size. Recall ranks, it does not judge relevance, so an unrelated question otherwise returns the least-bad memories up to the token budget.
- Read `hindsight-architect` (282 installs) before writing memory code of your own. It produces a plan with bank config, tag schema and code and explicitly declares that it does not write the code, which is the right shape for review before an agent starts storing things.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
