---
title: "belt CLI - Cloud Platform Control for Agents"
description: "belt-sh/cli on skills.sh: 6.7K combined installs; the belt CLI skill for hosted AI apps, skills and MCP connectors from one static binary."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/belt-cli-setup/"
robots: "index,follow"
last_updated: "2026-11-06"
tags: ["hermes skill", "agent skill", "skill setup", "cli", "mcp", "inference"]
---

# belt CLI - Setup Guide

**Source:** [belt-sh/cli](https://www.skills.sh/belt-sh/cli) via skills.sh - 6.7K combined installs across 1 indexed listing; first seen 2026-11-06 (Nov 6, 2026 morning sweep)
**GitHub:** 7 stars, MIT licence, last pushed 2026-09-27, one SKILL.md at .agents/skills/belt/SKILL.md, with AGENTS.md and CLAUDE.md alongside at the repository root
**Category:** Agent command line: run hosted apps, search and publish skills, call MCP servers from one static binary
**Quality Tier:** 🟡 Review - the single skill carries a Snyk Warn, and the skill is a typed wrapper over a hosted platform that spends account credits.

belt is a command line client for inference.sh, written in Go and shipped as a single static binary of roughly 4 MB with no runtime and no dependencies. One binary covers four things an agent normally reaches for separately: running hosted AI apps (image, video, audio, LLM, search, 3D), a knowledge store for discoveries and preferences, a skill registry with search, install and publish, and MCP connectors with a `run` command per tool.

The skill in this repository is small and unusually specific. `.agents/skills/belt/SKILL.md` is a single file of command sequences with an `allowed-tools` frontmatter field that allowlists exactly the belt invocations an agent may run, which is the part worth reading before install.

## Installation

The README's install line, verbatim:

```bash
curl -fsSL https://cli.inference.sh -o /tmp/belt-install.sh && sh /tmp/belt-install.sh
```

The package manager routes it also documents:

```bash
brew install inference-sh/tap/belt       # macos / linux
npm install -g @inferencesh/belt         # node.js (downloads native binary)
scoop bucket add belt https://github.com/belt-sh/scoop-belt && scoop install belt  # windows
```

Then authenticate and confirm the account before anything else uses credits:

```bash
belt login
belt me
belt balance
```

The skill file recommends checking an existing install first (`which belt && belt --version`) and describes the manual installer as a short readable script that detects OS and architecture, downloads the matching binary from `dist.inference.sh`, verifies its sha-256 checksum against the published manifest and places it on the path without elevated permissions. It also shows the two step form, `cat /tmp/belt-install.sh` to review then `sh /tmp/belt-install.sh` to run, which is the version to prefer on a shared host.

Agent integration is a separate command per harness:

```bash
belt plugin init claude     # claude code
belt plugin init codex      # openai codex
belt plugin init cursor     # cursor
```

The README lists the same pattern for gemini, pi, opencode and windsurf. That plugin adds skill, knowledge and app suggestions on every prompt, background knowledge capture, and slash commands (`/belt`, `/skill`, `/skillify`, `/knowledge`, `/apps`, `/suggest`, `/agentify`, `/appify`, `/flowify`).

## What It Provides

One listing holds the entire index, and it is the CLI skill rather than a per-task skill.

| Skill | Installs | Use For |
|---|---|---|
| belt | 6,657 | Running hosted AI apps, managing knowledge, searching and publishing skills, and calling MCP connectors from a typed CLI |

No indexed listings fall below the threshold; the table above is the whole index.

## Why This Matters for Hermes Agents

The interesting argument here is architectural rather than about any individual command. An agent that needs an image, a video, a transcription or a search result usually writes `curl` calls against a provider API, which means it composes request bodies by hand, guesses field names, and pastes credentials into shell history. belt replaces that with a schema-validated surface: `belt app get` prints the input schema and pricing, `belt app sample` generates a valid input file, and `belt app run` executes it.

Agent ergonomics are treated as a requirement rather than a nicety. Every list command takes `--json`, which is the difference between an agent parsing prose tables and an agent parsing a document it can rely on. `belt app run --no-wait` submits without blocking and `belt task get <id>` checks later, which suits a job that takes minutes and a session that should not sit idle.

The knowledge store is the part that changes behaviour across sessions. `belt knowledge search` is a semantic lookup over saved discoveries, insights, references and preferences, and `belt knowledge upload` takes a file, so a Hermes agent can persist what it learned about a project without inventing a memory format.

Skill discovery is folded into the same binary. `belt skill store search` browses the registry, `belt skill use` loads a skill on demand without writing to disk, and `belt skill add` installs it persistently. For an agent that already works from markdown skills, that is a searchable path to more of them without leaving the shell.

The MCP connector path is the quieter win: `belt mcp connect slack` then `belt mcp run slack send_message --input '{"channel": "#general", "text": "hello"}'` turns any MCP server into one more belt subcommand, with the same typed input contract as the apps.

## Usage

| You say | What happens |
|---|---|
| "Generate a product video from this image" | The agent checks the app schema, samples an input, and runs it with the local image path, which the CLI uploads |
| "What does this cost before you run it?" | `belt app pricing` prints the cost formula, and `belt task cost <id>` reports the actual charge afterwards |
| "Find a tool for background removal" | `belt suggest` searches apps, skills and knowledge in one call |
| "Save what we learned about this repo" | `belt knowledge upload` or a knowledge entry write, then `belt knowledge search` retrieves it later |
| "Pull a skill from the registry" | `belt skill store search "web"` then `belt skill use` on demand, or `belt skill add` to keep it |
| "Send a Slack message from here" | `belt mcp connect slack` once, then `belt mcp run slack send_message` with a typed input |
| "Give me that as JSON" | Any list command accepts `--json`, so the agent parses fields instead of scraping columns |

## Verification

Confirm what the skill actually allows before installing the plugin, since the allowlist is the contract:

```bash
curl -fsSL https://raw.githubusercontent.com/belt-sh/cli/main/.agents/skills/belt/SKILL.md | head -6
```

That returned HTTP 200 on 2026-11-06 and should print `name: belt`, the description naming hosted AI apps, knowledge, skills and MCP servers, and an `allowed-tools` line scoped to `Bash(belt *)` plus the install commands.

Then confirm the binary and the identity behind it:

```bash
which belt && belt --version
belt me
belt balance
```

If `which belt` prints nothing, the install did not reach the path and `belt login` will fail for the wrong reason. Re-run the README's install line in that case:

```bash
curl -fsSL https://cli.inference.sh -o /tmp/belt-install.sh && sh /tmp/belt-install.sh
```

## Security

skills.sh verdicts for sampled skills (verified 2026-11-06) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| belt | Pass | Pass | Warn |

Read the Snyk Warn as a reason to audit the allowlist, not as a verdict on the platform. The skill's frontmatter grants `Bash(belt *)`, which is broad by design: once granted, an agent can run any belt subcommand, including `belt skill upload`, `belt app deploy`, `belt secrets set` and `belt mcp run`. If you want a narrower surface, cap it at the subcommands you actually want used.

The installer is a remote shell script fetched from `cli.inference.sh` and executed. The skill's own guidance is to download it, read it and verify the checksum against the published manifest before running, and that guidance is worth following on any shared machine.

Secrets are a first-class command here. `belt secrets set` and `belt secrets get` keep credentials in the platform rather than in shell history, and `INFSH_API_KEY` overrides the login config, which is the cleaner route for CI than a persisted login.

The plugin hooks are the part to decide about deliberately. Once installed, they suggest skills and apps on every prompt and capture knowledge from sessions. Disable them per project with `{"hooks_disabled": true}` in `.beltsh/config.json`, or set `BELT_NO_HOOKS=1`, and use `suggest_disabled` or `knowledge_disabled` for the granular version.

## Limitations

- Snapshot data, verified 2026-11-06: 6,657 combined installs across 1 indexed listing; 7 GitHub stars; MIT; last pushed 2026-09-27. Counts drift over time.
- One listing, one skill, and a very small star count. The install figure comes from a single indexed skill, so it says nothing about breadth of adoption in the way a multi-skill suite does.
- The listing is one skill and one maintainer surface. Every app, knowledge, skill and connector command depends on the hosted platform: login, credits, app availability and latency are inference.sh properties, not local ones. `belt balance` and `belt app pricing` exist precisely because runs cost money.
- The skill is not distributed through a skills.sh install command in the README. It ships inside the CLI repository at `.agents/skills/belt/SKILL.md`, and the agent integration path is `belt plugin init <harness>`, which pulls the plugin from the separate belt-sh/skills repository.
- Plugin hooks change agent behaviour beyond the skill itself, adding prompt-time suggestions and background knowledge capture. Turn them off per project if that is not what you want.
- The Snyk Warn is unresolved in the pack's snapshot. Re-check the security page before wiring the skill into an unattended agent.

## Related

- [Inference Sh Skills Setup](/hermes/skills/catalog/inference-sh-skills-setup)
- [CLI Printing Press - Agent-Native CLI Generator Setup](/hermes/skills/catalog/cli-printing-press-setup)
- [Build Mcp Server Setup](/hermes/skills/catalog/build-mcp-server-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run `belt app get` before `belt app run`. It prints the schema, the functions and the pricing formula in one call, which prevents the two common failures: wrong field names and an unexpected charge.
- Prefer `belt app sample --save input.json` over inline JSON. The sample is schema-valid, so the agent edits a working file instead of composing one.
- Use `--session new` for stateful apps that keep a GPU warm between calls, and `--no-wait` plus `belt task get` for anything that takes minutes.
- Keep `BELT_NO_HOOKS=1` in repositories where you do not want prompt-time suggestions. The hooks are useful in a working session and noisy in a build pipeline.
- Read `.agents/skills/belt/SKILL.md` before the README. It is the file the agent loads, it carries the allowlist, and it is shorter than the command documentation.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
