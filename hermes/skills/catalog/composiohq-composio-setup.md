---
title: "Composio - SDK Monorepo and Agent Toolkit Setup Guide"
description: "Composio: 10.5K combined installs. SDK monorepo for 1000+ pre-authenticated app toolkits, with TypeScript and Python SDKs, a CLI, MCP and 20 skills."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/composiohq-composio-setup/"
robots: "index,follow"
last_updated: "2026-10-28"
tags: ["hermes skill", "agent skill", "skill setup", "composio", "agent sdk", "toolkits", "mcp"]
---

# Composio - Setup Guide

**Source:** [ComposioHQ/composio](https://www.skills.sh/ComposioHQ/composio) via skills.sh - 10.5K combined installs across 20 indexed listings; snapshot 2026-10-28 (Oct 28 evening sweep)

**GitHub:** [ComposioHQ/composio](https://github.com/ComposioHQ/composio) - 30,796 stars, MIT, branch next, last pushed 2026-10-29; 20 `SKILL.md` directories in the tree, 19 under the canonical `.agents/skills/` tree plus the router at `skills/composio/SKILL.md`, with `.claude/skills` kept as a compatibility symlink

**Category:** Agent tool platform, TypeScript and Python SDKs, CLI, MCP sessions and repository engineering skills

**Quality Tier:** 🟡 Beta - vendor maintained, 30,796 GitHub stars, 20 indexed listings against 20 skill directories, one Snyk warning on the router skill, and installs concentrated in one listing

Composio is a tool integration platform for agents. Its README describes 1000+ pre-authenticated toolkits, per-user sessions, authentication, triggers and a sandboxed workbench, so an agent can act across Gmail, Slack, GitHub, Notion, Calendar, Linear and hundreds of other apps without you writing an auth flow per app. This repository is the SDK monorepo behind that platform: `@composio/core` for TypeScript, `composio` for Python, the standalone `composio` CLI, and provider adapters that translate its tools into the native tool format of OpenAI Agents, the Claude Agent SDK, Vercel AI SDK, LangChain, LlamaIndex, Mastra, Google ADK, CrewAI, AutoGen and others. It is MIT licensed and heavily used, at 30,796 stars.

The 20 indexed skills are not connector documentation. They are engineering guidance for the codebase and the SDKs: one router skill, then TypeScript and Python SDK, provider, testing and release skills, a CLI implementation skill and a CLI end-to-end test skill, cross-SDK parity, repository navigation, docs decisions, a documentation voice guide and its audit, skill-tree maintenance, and an Effect v4 reference pinned to `effect@4.0.5`. The toolkit catalogue they talk about lives in the Composio product and behind session and MCP endpoints, not in the skill directories, so install these when the work is building, extending or maintaining Composio itself rather than wiring one named app.

## Installation

The repository documents no skills.sh install command, so the skill tree is installed by copying it into the agent's skills directory. `.agents/skills` is the canonical tree according to the repo's own `AGENTS.md`, and the router lives one level up under `skills/`:

```bash
git clone --branch next https://github.com/ComposioHQ/composio.git
mkdir -p ~/.hermes/profiles/corpusiq/skills
cp -R composio/.agents/skills/* ~/.hermes/profiles/corpusiq/skills/
cp -R composio/skills/composio ~/.hermes/profiles/corpusiq/skills/composio
```

Copy the specific directories you need when you only want a few. The names in `.agents/skills/` match the indexed listing names for 18 of the 20 listings, so a filtered copy is a directory-level choice rather than a rename.

The CLI is a separate install and is the fastest way to get a working tool surface from a shell. `INSTALL.md` and the README both use the same installer, which unpacks into `~/.composio`, links the entry point into `~/.local/bin`, configures your shell's PATH block, and verifies official releases against the SHA-256 entries in the release `checksums.txt`:

```bash
curl -fsSL https://composio.dev/install | sh
composio login
```

Open a new terminal before the first `composio` call, because the PATH block is written for future shells. Two documented switches matter for unattended hosts: `COMPOSIO_INSTALL_SHELL=none` leaves your startup files alone when a dotfile manager owns them, and `COMPOSIO_INSTALL_PLUGINS=0` (or the `--no-plugins` flag) skips plugin setup for detected Codex and Claude Code hosts. Pin a build with `COMPOSIO_INSTALL_VERSION`.

The SDKs install from npm and PyPI, and the README's quickstart pairs each one with a provider adapter for the agent framework in use:

```bash
npm install @composio/core @composio/openai-agents @openai/agents
pip install composio composio-openai-agents openai-agents
```

The TypeScript SDK is tested against Node 22 and above, and the Python SDK supports Python 3.10 and above. `@composio/slim` carries the same API without the packaged source and SDK docs, which is the smaller install when you do not need the source on disk for a coding agent to inspect.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| composio | 8,266 | A router that first separates Composio For You from Composio Platform, then picks the job: explain, set up, build, operate, or debug and migrate, loading only the reference that job needs. |
| typescript-testing | 135 | Choosing the right TypeScript verification for a change: package tests, type checks, lint, builds, Vitest suites, Effect v4 CLI tests, and runtime end-to-end runs. |
| bug-fixing | 132 | Defect work with a focused reproduction, root-cause analysis, a regression test and narrow verification, without drifting into feature design or broad refactors. |
| cli-command | 131 | Designing and implementing `composio` CLI commands under `ts/packages/cli` with Effect, effect/cli services, output conventions, configuration and environment variables. |
| typescript-sdk | 130 | Implementing TypeScript SDK behavior in `@composio/core` and shared packages: tools, toolkits, sessions, auth configs, connected accounts, modifiers and generated surfaces. |
| python-testing | 130 | Python verification with nox, Makefile targets, Ruff, mypy, pytest markers, sanity tests, type inference checks and build checks. |
| typescript-providers | 129 | Provider package work under `ts/packages/providers`, covering the framework adapters for OpenAI, Anthropic, Google, LangChain, Mastra, Vercel, LlamaIndex, Cloudflare and the Claude Agent SDK. |
| repo-guidance | 129 | Orienting work in the monorepo: layout, branch and PR flow, generated-file boundaries, changesets, and deciding which package a change belongs in. |
| docs-decisions | 129 | Docs site work: Fumadocs configuration, changelogs, docs automation prompts, ADR-style records, and requests to record or revise a docs decision. |
| cross-sdk-parity | 129 | Keeping TypeScript and Python aligned when a change affects both: public API naming, generated client pins, docs examples and backend contract shifts. |
| cli-e2e | 129 | Docker-based CLI end-to-end tests under `ts/e2e-tests/cli`, including binary invocation, fixture isolation, output assertions and package manifests. |
| python-sdk | 128 | Implementing Python SDK behavior under `python/composio`: tools, toolkits, sessions, auth configs, connected accounts, client integration and shared models. |
| python-release | 128 | Python release work: build, version bump, packaging metadata, the PyPI client pin, `uv.lock`, the nox and build workflow, and publish verification. |
| python-providers | 128 | Python provider adapters under `python/providers`: framework-specific dependencies, public imports, type inference and provider metadata. |
| skill-maintenance | 127 | Maintaining the repo's own skill tree: `SKILL.md` frontmatter, first-level references, compatibility symlinks and the validation scripts. |
| cli-release | 125 | First-party CLI binary releases: beta builds, stable promotion, candidate selection, asset and installer verification, and recovery from a failed release. |
| good-docs-writing | 117 | A house writing style for docs and technical prose, derived from Modal's voice: direct, second person, confident, low jargon and example first. |
| good-docs-audit | 117 | Auditing a doc, guide, README or block of prose against that style and reporting violations as file, line, rule and suggested rewrite, without editing. |

The remaining 2 indexed listings range from 7 to 53 installs: effect-v4 (53) and composio-cli (7).

## Why This Matters for Hermes Agents

Most agent tool platforms fail in the same place: the agent knows the brand name and invents the rest. The router skill is written against that failure, with an explicit rule not to invent toolkit or tool slugs and to discover them at runtime or through the CLI, and a second rule not to claim a file, framework, identity field or dependency exists until something has inspected it. For a Hermes agent that has been handed a Composio task and no repo checkout, that is the difference between a plan and a fabricated plan.

The product split is the other high-value piece. Composio For You and Composio Platform use different credentials and different setup paths, one for a person's own agent and apps, the other for an application whose users connect their accounts, and the skill refuses to blend them. A `ck_...` consumer key belongs to the first, a `COMPOSIO_API_KEY` project key to the second, and the credential question is the first thing that goes wrong in a mixed setup.

For build work, the engineering skills encode the repository's real conventions: branch from `next`, treat `.agents/skills` as canonical and `.claude/skills` as a symlink that must not be edited as a copy, respect generated and vendored boundaries, and check every command against the current `package.json`, `Makefile`, `noxfile.py` or workflow file. An agent asked to add an SDK method gets the pairing the maintainers use in practice: `typescript-sdk` with `typescript-testing`, and `cross-sdk-parity` when Python has to match.

The verification skills are the underrated ones. They choose a focused command instead of a full run, name the exact marks and targets per language, and say what not to use them for, so a cron-driven agent burns minutes instead of an hour on `pnpm test`. The docs-writing and docs-audit pair is useful beyond Composio too, because it turns "make this read better" into a rule set and a findings report a reviewer can act on.

## Usage

| You say | What happens |
|---|---|
| "Wire Composio into this agent so it can read my Gmail and Slack" | composio asks whether this is your own agent and accounts or a product where users connect their own, then loads the For You reference, points at the hosted MCP endpoint or the CLI, and runs one safe tool call to confirm. |
| "Add a session method to the TypeScript SDK and keep Python in step" | typescript-sdk edits `ts/packages/core` against `references/core-sdk.md`, cross-sdk-parity aligns naming and the generated client pin, and typescript-testing picks the narrowest passing check. |
| "The CLI tool call fails with a 401 after login" | composio asks for the log or request ID, identifies the failing boundary between CLI, project key and connected account, and only retries when execution was authorized. |
| "Our CLI command needs a new flag and an end-to-end test" | cli-command wires the command through effect/cli services with the repo's output conventions, then cli-e2e adds a Docker-based suite under `ts/e2e-tests/cli`. |
| "Write the changelog entry and check the docs voice" | docs-decisions handles the changelog and docs-site convention, good-docs-writing drafts in the house voice, and good-docs-audit returns findings as file, line, rule and rewrite instead of editing. |
| "Cut a Python release and a CLI beta" | python-release walks the build, bump, packaging and PyPI pin steps, while cli-release handles the beta build, candidate selection and post-release asset and installer verification. |
| "Where does this change belong, and how do I open the PR?" | repo-guidance maps the monorepo, picks the package, flags generated files to leave alone, and states the changeset and branch target the PR needs. |

## Verification

Probe the paths before installing. These four URLs returned 200 on branch `next` when this guide was written, and the raw paths are the ones the router and maintainers point at:

```bash
for p in skills/composio/SKILL.md \
         .agents/skills/repo-guidance/SKILL.md \
         .agents/skills/typescript-sdk/SKILL.md \
         AGENTS.md; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/ComposioHQ/composio/next/$p"
done
```

Read two of them before copying anything: the router decides product and job, and `AGENTS.md` carries the skill routing table that maps a request to the smallest relevant skill:

- https://raw.githubusercontent.com/ComposioHQ/composio/next/skills/composio/SKILL.md
- https://raw.githubusercontent.com/ComposioHQ/composio/next/AGENTS.md

After the copy, confirm what landed and that the frontmatter names match the directory names:

```bash
ls ~/.hermes/profiles/corpusiq/skills | grep -cE '^(typescript-|python-|cli-|cross-sdk|repo-guidance|docs-decisions|good-docs|skill-maintenance|bug-fixing|composio)'
head -3 ~/.hermes/profiles/corpusiq/skills/repo-guidance/SKILL.md
```

For the CLI side, `composio login` is the documented first call after install, and `composio search` is the documented way to find a tool rather than guess a slug. Check the binary is on PATH in a new shell before debugging anything else, since the installer only writes the PATH block for future terminals.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-28) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| composio | Pass | Pass | Warn W012 |
| typescript-testing | Pass | Pass | Pass |
| bug-fixing | Pass | Pass | Pass |
| cli-command | Pass | Pass | Pass |
| typescript-sdk | Pass | Pass | Pass |
| python-testing | Pass | Pass | Pass |

One of the six sampled listings carries a Snyk Warn, code W012, and it is the router: the skill that handles credentials, decides between consumer keys and project keys, and reaches for live documentation. Treat the warning as a reason to read that `SKILL.md` and its two product references before installing, not as a verdict on the repository. The other five sampled listings pass all three auditors.

The skill directories themselves are markdown plus first-level reference files. The installer is the part that acts on your host: it unpacks a binary into `~/.composio`, writes a managed PATH block into shell startup files, and, unless told not to, installs plugins into detected Codex and Claude Code hosts. Official releases are verified against the release `checksums.txt` and abort on a missing entry or a mismatch, but the installer warns and continues on hosts with no `sha256sum` or `shasum`. On a shared or managed host, run it with `COMPOSIO_INSTALL_SHELL=none` and `COMPOSIO_INSTALL_PLUGINS=0` and wire PATH yourself.

Credential handling is stated in the router's stable rules and worth enforcing in a Hermes profile: never create, rotate, replace, print or request a `COMPOSIO_API_KEY` in chat, keep keys out of source control, URLs, logs and command output, and do not build a provider OAuth flow, because Composio returns a Connect Link when authentication is needed. Sessions carry user identity, so a session id stored in a note is a capability for that user's connected accounts; keep it with the same care as the key.

## Limitations

- Snapshot data, verified 2026-10-28: 10499 combined installs across 20 indexed listings; 30796 GitHub stars; MIT license; last pushed 2026-10-29. Counts drift over time.
- Index and tree do not line up one to one. `composio-cli` (7 installs) has no directory in the current tree, while `.agents/skills/eve` carries a `SKILL.md` with no indexed listing and is pinned in `skills-lock.json` to the external `vercel/eve` source.
- These skills target the Composio SDK and codebase rather than being a connector catalogue. The 20 indexed listings are engineering and SDK guidance, and the 1000+ toolkits they describe arrive through the platform, a session or an MCP endpoint, so installing the tree does not add a single app integration.
- Installs are concentrated: `composio` alone carries 8,266 of the 10,499 combined installs, and the other 19 listings sit between 7 and 135. Popularity here measures the router, not adoption of the individual engineering skills.
- No skills.sh install command is documented in the README or `INSTALL.md`, so the copy route above is the one to use, and it does not update itself. Re-clone to pick up changes, and note that branch `next` is the default and the branch the repo asks contributors to target.
- Several skills assume the repository is checked out and runnable: they reference `references/*.md` files inside their own directories, `ts/vendor/effect` for the Effect v4 oracle, and `ts/e2e-tests/cli` for CLI end-to-end work. Copied out of the repo with a flat layout, those relative references stop resolving.

## Related

- [Build Mcp Server Setup](/hermes/skills/catalog/build-mcp-server-setup)
- [Awesome Copilot - MCP Server Generators & GitHub Automation Setup](/hermes/skills/catalog/awesome-copilot-setup)

## Pro Tips

- Ask the router one question first: is this your own agent and accounts, or a product where your users connect theirs. Answering it late is the usual cause of a `ck_...` key being pasted into a project that expects `COMPOSIO_API_KEY`.
- Point the agent at `AGENTS.md` before a build task. Its skill routing table is shorter than the skill index and maps a request to the smallest relevant skill, which keeps a bug report from loading the whole release toolchain.
- Install the engineering skills only if you work on the Composio codebase. For using Composio, install `composio` and connect over MCP or the CLI, because a session exposes meta tools that discover, authenticate and execute app tools at runtime instead of loading hundreds of definitions into context.
- Store and reuse `session.session_id` across turns with `composio.use()` rather than creating a session per request, and restrict toolkits, auth configs and connected accounts per session when an agent only needs a few apps.
- Run the installer on a host where you control shell startup files, or pass `COMPOSIO_INSTALL_SHELL=none` and add `~/.local/bin` yourself, so a managed PATH block does not collide with a dotfile manager.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
