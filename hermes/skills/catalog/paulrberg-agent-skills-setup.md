---
title: "Paul Berg Agent Skills - Solidity and Foundry"
description: "paulrberg/agent-skills: 32.7K combined installs. Forty-three skills plus Rust CLIs for Effect, Tailwind, GitHub workflow, git commits and EVM work."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/paulrberg-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-31"
tags: ["hermes skill", "agent skill", "skill setup", "solidity", "foundry", "evm"]
---

# Paul Berg Agent Skills - Setup Guide

**Source:** [paulrberg/agent-skills](https://www.skills.sh/paulrberg/agent-skills) via skills.sh - 32.7K combined installs across 97 indexed listings; first seen 2026-10-31 (morning sweep)

**GitHub:** [paulrberg/agent-skills](https://github.com/paulrberg/agent-skills) - 104 stars, MIT, branch main, last pushed 2026-10-30; 43 skill directories under `skills/` with one `SKILL.md` each and 169 markdown files between them, plus a `toolkit/` of Rust CLIs and an `mcp/` server

**Category:** Smart contract work for agents: Solidity style, Foundry testing, deployment and code polish

**Quality Tier:** 🟢 Green - all five sampled skills Pass all three auditors and the repository is MIT markdown, though it is one engineer's personal catalog with 104 stars rather than a maintained platform

Paul Berg's repository is a working engineer's setup published as a skills pack: 43 skill directories, plus the command-line tools his skills call (`ai-commit`, `ai-coord`, `ai-handoff`, `ai-notify`, `ai-skillet`), and an MCP server directory. The README opens with a warning worth repeating in full substance: this catalog reflects Paul's preferred tools, defaults, safety boundaries and writing voice, it is not a neutral template, and anyone installing it should review every workflow and customize it for their own stack and agents.

The label on this page reads Solidity and Foundry, and that is the thinnest part of the offer. The top of the install table is TypeScript and styling: `effect-ts` at 3,122, `tailwind-css` at 3,010, `cli-gh` at 2,835, `code-polish` at 2,781. The EVM work is real but small: `cli-cast` covers Foundry's cast CLI for preparing, tracing, simulating, signing and broadcasting transactions, `evm-atlas` covers chain, account, bridge and DEX evidence lookups, `etherscan-api` sits at 26 installs and `evm-chains` at 176. What you install is a disciplined agent workflow kit with a crypto corner in it.

## Installation

The README's skill route is one line:

```bash
bunx skills add PaulRBerg/agent-skills
```

The CLIs are separate, and several skills assume they are on the path. They build from source with Rust nightly:

```bash
cargo +nightly install --locked --git https://github.com/PaulRBerg/agent-skills ai-commit ai-coord ai-handoff ai-skillet
```

macOS users add desktop notifications:

```bash
cargo +nightly install --locked --git https://github.com/PaulRBerg/agent-skills ai-notify
```

From a clone, `just toolkit::install-cli` puts the supported CLIs into `~/.local/bin`, and the toolkit README covers prerequisites and Linux clipboard setup. That last point matters on a Linux host: reading and writing the clipboard is how several of these workflows hand text between agents.

Hermes installs skills from a directory, so clone and copy:

```bash
git clone --depth 1 https://github.com/paulrberg/agent-skills.git /tmp/prb-agent-skills
cp -r /tmp/prb-agent-skills/skills/. ~/.hermes/profiles/corpusiq/skills/
```

That copies all 43 skill directories. A practical subset for a non-crypto profile is `code-polish`, `commit`, `release-bumper`, `node-deps-bumper`, `cli-gh`, `yeet`, `codebase-design`, `large-file-refactor`, `naming-refactor`, `fresh-eyes-sweep` and `agents-brain`. The CLIs stay optional until a skill actually asks for one: `commit` calls `ai-commit`, and `orchestration` wants native subagents in Claude Code or Codex, or an authenticated CLI for shell execution.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| effect-ts | 3,122 | Effect 4 work: services and layers, typed errors, Schema and JsonSchema, Config, runtime and concurrency, `@effect/vitest`, `effect/ai`, `effect/sql` and Effect Atom. |
| tailwind-css | 3,010 | Tailwind v4 styling: adding or fixing classes, configuring or migrating Tailwind, `tailwind-variants` and `tw-animate-css`. |
| cli-gh | 2,835 | GitHub CLI automation: repository reads, workflow runs, search, codespaces, releases and configuration, with contribution writes left to `yeet`. |
| code-polish | 2,781 | A post-implementation pass over an explicit file scope: simplification and risk-profiled review with autofix, driven by `--simplify` and `--review`. |
| yeet | 2,584 | GitHub contribution writes: create and update PRs, issues and discussions, post comments, with each mode named in the argument hint. |
| bump-release | 2,362 | No directory in the clone and no row in the README's 43-skill table; the nearest live entry is `release-bumper`, which bumps versions, writes changelogs, commits and tags. |
| bump-deps | 2,342 | No directory in the clone; dependency work now belongs to `node-deps-bumper`, which builds one taze plan and applies compatible ranged updates. |
| code-simplify | 2,310 | No directory in the clone; `code-polish` carries the simplification half today through its `--simplify` flag over a fixed scope. |
| code-review | 2,014 | No directory in the clone; `code-polish` carries the review half through `--review`, risk profiles and autofix. |
| md-docs | 1,702 | No directory in the clone and nothing in the live table covers markdown documentation authoring, so this install figure is historical. |
| biome-js | 1,067 | No directory in the clone; the repository ships no formatter or linter skill, so treat the count as a listing that predates the current tree. |
| cli-just | 789 | `just` and justfile automation: creating justfiles, writing recipes, settings, modules and attributes for a command runner. |
| commit | 344 | Committing staged or intended changes: a Conventional or natural-language message through `ai-commit`, with `--all`, `--staged`, `--push` and `--squash`. |
| cli-cast | 305 | Foundry's cast CLI: prepare, trace, simulate, sign and broadcast transactions, sign messages, and encode or decode ABI and calldata. |
| spreadsheets | 259 | CSV, TSV and XLSX as the primary input or output: designing text-table schemas, transforming, validating, converting and recalculating formulas. |
| git-squash | 235 | No directory in the clone; `commit` takes `--squash` to fold a branch into one commit today. |
| work | 230 | No directory in the clone and no live equivalent in the README table, so the figure survives from an earlier index. |
| autoresearch | 219 | No directory in the clone; `tool-finder` covers finding and comparing developer tools, which is the adjacent live skill. |
| oracle-codex | 190 | No directory in the clone; `orchestration` covers research, planning and implementation across Claude or Codex agents. |
| evm-chains | 176 | No directory in the clone; `evm-atlas` covers chain names and IDs, native symbols and the evidence lookups this name implies. |

The remaining 77 indexed listings range from 2 to 175 installs.

Thirteen of the 20 rows above point at names the repository no longer ships. Across the whole index the gap is larger: 54 of the 97 listings have no directory in the clone, which is the single most important thing to know before trusting this table as a shopping list. The 43 directories are all in the install counts, so the pack is not stale, but the index has a long memory and the repository does not.

## Why This Matters for Hermes Agents

The skills that carry this pack solve the unglamorous problems that decide whether an agent session is useful. `code-polish` takes an explicit file scope and produces either a simplification pass or a risk-profiled review with autofix, which is a much narrower contract than "review my code" and far easier to trust. `commit` composes a message and hands the actual snapshot to `ai-commit`, which exists to make immutable commits in shared working trees. `release-bumper` and `node-deps-bumper` each do one mechanical job with a dry run. Those are the shapes that survive daily use.

The agent-tooling half is unusually introspective. `agents-brain` maintains repo context and generates AGENTS.md files or repo-local skills, `agents-introspection` assesses recurrence risk from Codex and Claude Code transcript history, `agents-docs` fetches current official Codex and Claude Code documentation including hooks and trust settings, and `skill-harmonization` reconciles a repository portfolio against user-installed skills. For a profile that runs many suites at once, `skill-harmonization` is the answer to skill sprawl rather than another source of it.

The repository also documents its own maintenance loop. `skill-harmonization` reconciles repository and user-installed skill portfolios, `repo-harmonization` aligns interdependent repositories and transfers practices between them, `agents-system` redesigns repo systems for agent understanding and control, and `.agents/internal-skills/` holds the author's own procedures for skill authoring, sync, lifecycle and publication. That is a level of self-hosting most packs skip, and it means the conventions an agent learns here transfer to writing new skills rather than only to using existing ones.

The crypto corner is small but specific. `cli-cast` delegates every standalone RPC read to `evm-atlas` rather than reimplementing chain queries, and `evm-atlas` covers bridges (Across, Hop, LayerZero, LI.FI and more) and DEX routing (Uniswap v1 through v4, 1inch, CoW Swap) as evidence lookups. For Solidity authoring there is no compiler-level skill here: `cli-cast` operates Foundry's cast tool, and testing and deployment discipline has to come from your own project conventions.

## Usage

| You say | What happens |
|---|---|
| "Polish the code I just changed before I review it" | `code-polish` takes the file scope, runs the simplification or risk-profiled review pass, and applies autofix where the profile allows it. |
| "Commit this with a conventional message" | `commit` composes the message and hands the snapshot to `ai-commit`, honouring `--all`, `--staged` or `--squash` and closing issues named in the diff. |
| "Cut a release for the two workspace packages" | `release-bumper` bumps versions, writes the changelog entry, commits and tags, with `--dry-run` available before it writes anything. |
| "Which dependencies are stale, and what will break if I bump them" | `node-deps-bumper` builds a single taze plan, applies compatible ranged updates and isolates the major-version decisions for review. |
| "Simulate this transaction before we broadcast it" | `cli-cast` prepares and traces the call, simulates it, and only then signs and broadcasts, with ABI encoding handled in the same skill. |
| "What is this address, and where did its funds come from" | `evm-atlas` resolves the chain and account, pulls balances and history, and follows funding origin through Etherscan, Blockscout and Chainscout. |
| "Our AGENTS.md is out of date and the repo has no skills" | `agents-brain` regenerates repo context and writes AGENTS.md or repo-local skills from what the repository actually contains. |

## Verification

The raw path for the highest-install skill returned HTTP 200 on branch main when this guide was written on 2026-10-31:

```bash
curl -sL -o /dev/null -w "%{http_code} effect-ts\n" \
  https://raw.githubusercontent.com/paulrberg/agent-skills/main/skills/effect-ts/SKILL.md
```

Expect `200`. After the copy, check that the named directories landed and read a header, since these skills use frontmatter fields beyond the Agent Skills minimum:

```bash
ls -d ~/.hermes/profiles/corpusiq/skills/{code-polish,commit,effect-ts,cli-gh,yeet,agents-brain}/ | wc -l
head -12 ~/.hermes/profiles/corpusiq/skills/code-polish/SKILL.md
```

`code-polish` should show an `argument-hint` line with `[--simplify]` and `[--review]`, a `description:` explaining the fixed file scope, and any `skill-dependencies:` block. If you also installed the CLIs, confirm the binary resolves before a skill calls it, for example `command -v ai-commit` for the commit workflow.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-31) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| effect-ts | Pass | Pass | Pass |
| todo-archive | Pass | Pass | Pass |
| task-handoff | Pass | Pass | Pass |
| ai-prune | Pass | Pass | Pass |
| agent-context-polish | Pass | Pass | Pass |

All five sampled skills Pass all three auditors. No Fail and no Warn appears in the sample.

The auditors scan skill text, and the sharper risk here is what the text tells an agent to delete or publish. `ai-prune` archives stale `.ai` files and moves stale `.cache` entries to the trash on macOS, `todo-archive` moves checked tasks out of TODO.md, `ai-commit` writes immutable commits into shared working trees, `yeet` creates and updates public PRs, issues and discussions, and `social-media` cross-posts. Each of those is a write that cannot be trivially undone, so scope the agent's repository and credentials before enabling them, and prefer the `--dry-run` flag where a skill offers one.

The second surface is the CLIs. They are Rust binaries built from this repository with a nightly toolchain and installed from git rather than from a published registry, so there is no checksum or release provenance to verify, only the commit you cloned. Treat `cargo +nightly install --locked --git ...` as a build from source with the trust that implies, and keep the installed set small. A Hermes profile can use the 43 skill directories without any of the binaries; the only loss is that `commit` and the handoff skills will ask for tooling that is not there.

## Limitations

- Snapshot data, verified 2026-10-31: 32,742 combined installs across 97 indexed listings; 104 GitHub stars; MIT; last pushed 2026-10-30. Counts drift over time.
- Index and tree diverge badly. The clone holds 43 skills and skills.sh lists 97, and 10 of the 20 rows in the table above name skills the repository does not contain, so the table is a record of what people installed, not a description of what you get.
- The catalog is one person's defaults. The README states plainly that it is not a neutral template and reflects Paul's tools, safety boundaries and writing voice, so an install carries opinions about commit message format, release tooling and agent delegation that your team may not share.
- Install counts are not a ranking. The most-installed skill is `effect-ts`, a TypeScript Effects library guide, while the Foundry and EVM skills this page is named for sit at 305 installs and below; popularity here tracks the author's own stack, not the category.
- Several skills assume macOS and third-party accounts. `pdf`, `spreadsheets` and `ai-prune` say macOS in their own descriptions, `evm-atlas` wants the `routemesh` CLI and DeBank or Blockscan access, and the clipboard workflows need Linux setup from the toolkit README.
- Skill text assumes the CLIs. `commit` calls `ai-commit`, and `orchestration` needs native subagents in Claude Code or Codex or an authenticated CLI, so a skills-only install will hit instructions that reference binaries you chose not to build.
- Smart contract advice stops at tooling. There is no Solidity style guide, no compiler-version triage and no Foundry test-pattern skill in the tree, so this is not a substitute for a dedicated Solidity suite.

## Related

- [Dot Skills - 96-Skill Agent Engineering Collection Setup - Setup Guide](/hermes/skills/catalog/dot-skills-setup)
- [components.build - UI Component Standards Setup](/hermes/skills/catalog/vercel-components-build-setup)
- [Claude MPM Skills - 96-Skill Dev Toolchain Collection Setup - Setup Guide](/hermes/skills/catalog/claude-mpm-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install by directory name, not by index row. Ten of the twenty names in the table above do not exist in the clone, so check `ls skills/` before adding a skill to a config, and skip the historical rows entirely.
- Take `code-polish` instead of the retired `code-review` and `code-simplify` pair. It is the live skill with both halves, and its fixed-scope contract makes the output reviewable rather than open-ended.
- Leave the CLIs out until a workflow demands one. The skills work as markdown; `ai-commit` and friends cost a nightly Rust toolchain and a build from git, which is a large ask for the commit-message step alone.
- Copy `agents-brain` even if you skip the crypto skills. It writes AGENTS.md files and repo-local skills from the repository's actual shape, which is the part that makes a Hermes profile usable on an unfamiliar codebase.
- Prefer `evm-atlas` over ad-hoc RPC calls for read-only chain questions. It routes evidence gathering through named explorers and bridges, and `cli-cast` defers every standalone RPC read to it rather than duplicating the lookup.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
