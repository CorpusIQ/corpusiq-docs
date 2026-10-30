---
title: "claude-mem - Persistent Memory for Coding Agents Setup"
description: "claude-mem: 101.5K combined installs across 34 indexed listings. Turns agent session history into searchable memory, plus search and planning skills."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/claude-mem-setup/"
robots: "index,follow"
last_updated: "2026-10-29"
tags: ["hermes skill", "agent skill", "skill setup", "persistent memory", "session context", "coding agents"]
---

# claude-mem - Setup Guide

**Source:** [thedotmack/claude-mem](https://www.skills.sh/thedotmack/claude-mem) via skills.sh - 101.5K combined installs across 34 indexed listings; first seen 2026-10-29 (evening sweep)

**GitHub:** [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) - 104,989 stars, Apache-2.0 License, branch main, last pushed 2026-10-29; package version 15.7.0; skills live per harness, with 30 under `plugin/skills/<name>/SKILL.md`, 4 under `openclaw/skills/`, 3 under `claude-mem-cursor/skills/`, 4 under `claude-mem-grok-bot/skills/` and 3 under `cowork/skills/`, alongside a Hermes memory provider at `hermes/claude-mem/plugin.yaml`

**Category:** Persistent agent memory, session capture, and memory-backed coding workflows

**Quality Tier:** 🟡 Beta - one Warn verdict (Gen Agent Trust Hub Warn on timeline-report) against five clean samples; Apache-2.0, 104,989 stars, pushed today

claude-mem is Alex Newman's memory compression system for coding agents. It hooks into an agent's lifecycle (SessionStart, UserPromptSubmit, PreToolUse, PostToolUse, Stop, SessionEnd), records every tool call as an observation, compresses those observations with a model at session end, and injects the relevant ones back into the next session. Storage is a local SQLite database with FTS5 full text search, with a Chroma vector database for hybrid semantic retrieval, all served by a local worker over HTTP with a web viewer.

The skills on skills.sh are the workflow layer on top of that memory, not the memory system itself. A few are heavily used and general purpose (mem-search, smart-explore, learn-codebase, make-plan, do, babysit), a few are report generators over the memory timeline (timeline-report, weekly-digests, knowledge-agent, standup), and the rest are maintenance and release chores (version-bump, cloud-sync, backup-setup, mode-creator). The repository also ships first class integrations for Claude Code, OpenCode, Codex via T3 Code, Grok Bot, Cursor, OMP, Pi, DeepSeek Harness, OpenClaw and Hermes, which is why one repo carries five parallel skill trees with overlapping names.

## Installation

The repository documents its own installers. For Claude Code, the README's single command route is:

```bash
npx claude-mem install
```

The installer provisions dependencies (Bun and uv are auto-installed if missing), registers the lifecycle hooks, starts the worker, then asks you to sign in to claude-mem in a browser for the hosted observer. Pass an explicit `--provider` flag, set `CLAUDE_MEM_ONLINE_OPTIN=false`, or run in a non-interactive shell to skip the account step entirely. `npm install -g claude-mem` installs the SDK only and does not register hooks, so it is not a substitute.

For Hermes, the repository ships a dedicated memory provider and its own install command:

```bash
npx claude-mem install --ide hermes
```

That copies the plugin to `$HERMES_HOME/plugins/claude-mem/` and sets `memory.provider: claude-mem` plus an `mcp_servers.claude-mem` entry in `$HERMES_HOME/config.yaml`, pointing at `plugin/scripts/mcp-server.cjs`. The MCP entry is what gives Hermes the search, timeline and get_observations tools. An existing `mcp_servers.claude-mem` block you wrote yourself is left alone.

Other harnesses use the same installer with a different target, for example `npx claude-mem install --ide opencode`, `--ide cursor`, `--ide grok-bot`, `--ide antigravity`, `--ide omp`, `--ide pi` or `--ide dsh`, and Claude Code can also install it from the marketplace with `/plugin marketplace add thedotmack/claude-mem` followed by `/plugin install claude-mem`. OpenClaw has a separate one liner, `curl -fsSL https://install.cmem.ai/openclaw.sh | bash`, documented in `openclaw/SKILL.md`.

To install an individual skill from the skills.sh index without the full memory system, use the skills CLI convention. This form is not in the repository README; it is how skills.sh listings are installed, and the `--skill` flag matters because the skill files sit inside harness subtrees rather than at the repository root:

```bash
npx skills add thedotmack/claude-mem --skill mem-search
```

Most of these skills assume a running claude-mem worker and its MCP tools, so the installer is the route that actually works end to end.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| mem-search | 9,016 | The default memory search skill: a three step search then timeline then get_observations workflow over the cross-session database, returning a compact index of IDs first so the agent filters before paying for full detail. |
| smart-explore | 7,392 | Token-optimized structural code search on a tree-sitter AST, replacing Read, Grep and Glob with smart_search, smart_outline and smart_unfold so the agent gets a map of the code before loading implementation. |
| make-plan | 7,308 | Orchestrator skill that writes a phased, LLM-friendly implementation plan with documentation discovery, delegating fact gathering to subagents and keeping synthesis in the main context. |
| do | 7,126 | Executes a phased plan by deploying subagents per phase, with the orchestrator routing context and verifying each checklist rather than doing the work itself. |
| timeline-report | 6,853 | Generates a "Journey Into [Project]" narrative analysis of a project's whole development history from the claude-mem timeline. |
| knowledge-agent | 5,786 | Builds and queries focused knowledge bases from observation history: filter a corpus, prime it into a session, then ask questions conversationally. |
| learn-codebase | 5,420 | Primes a codebase by reading every source file in full before work starts, for unfamiliar or newly inherited projects. |
| pathfinder | 5,202 | Maps a codebase into feature-grouped flowcharts, finds duplicated concerns across features, and emits a proposed unified architecture plus per-system make-plan prompts. |
| how-it-works | 5,172 | Explains what claude-mem captures, when memory injection fires, and where the data lives, for the "what is this thing doing to my sessions" question. |
| babysit | 5,011 | Watches a pull request or review cycle until every actionable comment, review thread and CI failure is resolved, instead of stopping after one check pass. |
| wowerpoint | 4,546 | Turns one document into a NotebookLM slide deck, with an explicit slide-deck-only scope. |
| design-is | 4,280 | Audits a design against Dieter Rams' ten principles and hands off a make-plan prompt for new design, refinement or redesign. |
| claude-code-plugin-release | 4,152 | Release mechanics for the Claude Code plugin itself, covering manifest, marketplace and build steps for a plugin release. |
| weekly-digests | 4,128 | Serial week-by-week narrative digest of a project's timeline, one chapter per ISO week, with each subagent receiving the prior week's carry-forward block. |
| oh-my-issues | 4,119 | Clusters a GitHub issue backlog by root cause into plan-master issues, redirects children with a standard comment, and bundles one fix PR per cluster. |
| standup | 3,445 | Read-only standup across git worktrees, branches or PRs that compares changes and produces one consolidation plan. |
| what-the | 2,962 | Plain-English breakdown of something technical: the who, what, where, why and when. |
| cloud-sync | 2,225 | Sets up or checks claude-mem cloud sync against a cmem.ai Pro account, so the memory database is backed up outside the machine. |
| version-bump | 1,884 | Semantic versioning and release workflow across package.json, marketplace.json and plugin.json, with build verification, tagging, GitHub release and changelog. |
| mode-creator | 1,397 | Interactively creates, installs and verifies custom claude-mem modes: domain-specific observation types, concept tags and optional Telegram alerts. |
| mem-setup | 1,034 | Pairs a claude-mem plugin with cmem.ai Connect credentials (sync token, user id, SyncHub URL) so hooks can capture and inject memory. |
| ccs-align | 673 | Hourly alignment seat that proves the local worker is healthy, pulls needle observations through search, timeline and get_observations, and detects rules conflicts. |

The remaining 12 indexed listings range from 21 to 456 installs.

## Why This Matters for Hermes Agents

The failure mode this targets is the one every long-running agent has: a new session knows nothing, so the agent re-reads files it already read, re-derives a decision it already made, and re-walks a dead end it already abandoned. claude-mem turns the tool calls of past sessions into compressed observations and injects the relevant ones at session start, which is context the model did not have to earn twice.

The retrieval shape is the interesting part for token budgets. The index layer returns roughly 50 to 100 tokens per result with IDs, timestamps and titles; full observation bodies cost roughly 500 to 1,000 tokens each. Search, look at the timeline, then fetch only the IDs that survived the filter, and the skill's own claim is about a 10x saving against fetching details first. That is a design rule an agent can follow, not a magic flag.

For Hermes specifically, the provider in `hermes/claude-mem/` maps Hermes events onto claude-mem calls: turn start records the prompt, a post_tool_call hook records each tool call, prefetch pulls semantically matching notes from every agent in the project, and system_prompt_block injects recent project work once at session start. Writes go through one background thread in order so the agent never waits on them, reads time out after three seconds, non-primary agents read but do not record, and every call fails quietly when the worker is down, with three consecutive failures pausing calls for 30 seconds. That is a sensible failure posture for an optional memory layer.

The shared-memory angle is what separates it from a per-agent scratchpad. The project is derived from the session working directory the same way it is for Claude Code, so a Hermes session and a Claude Code session in one checkout read and write the same notes. In a fleet where different agents handle different parts of the same repository, that is the difference between memory per tool and memory per project.

The operational cost is real though: a local worker process managed by Bun, a SQLite database, a Chroma index, and hooks on every tool call. Treat it as infrastructure to install and monitor, not a skill file to drop in.

## Usage

| You say | What happens |
|---|---|
| "Did we already fix this auth bug?" | mem-search runs a full-text search over the memory index, prints matching IDs with timestamps and titles, expands the timeline around the interesting ones, then fetches full detail only for the IDs that stayed relevant. |
| "Plan the migration before touching code" | make-plan writes a phased implementation plan with documentation discovery, delegating fact gathering to subagents, and hands back phases that can each run in a fresh context. |
| "Execute that plan" | do deploys a subagent per phase, routes the minimum context each one needs, and verifies each checklist instead of implementing everything in the main thread. |
| "Show me the history of this project" | timeline-report builds a narrative of the whole development timeline from stored observations, or weekly-digests splits it into one chapter per ISO week for a serial read. |
| "Find the duplicate systems before the refactor" | pathfinder maps the codebase into feature-grouped flowcharts, reports duplicated concerns across features, and emits a proposed unified architecture with per-system make-plan prompts. |
| "Watch this PR until it is mergeable" | babysit polls reviews, comments and CI, keeps working until every actionable item is resolved, and reports what is still open rather than declaring victory after one pass. |
| "Back up the memory database" | backup-setup writes and restores local snapshots of the claude-mem database, or cloud-sync points the worker at a cmem.ai Pro account for off-machine sync. |

## Verification

The raw skill files below returned 200 on branch main when this guide was written on 2026-10-29:

```bash
curl -sL -o /dev/null -w "%{http_code} mem-search\n" \
  https://raw.githubusercontent.com/thedotmack/claude-mem/main/claude-mem-cursor/skills/mem-search/SKILL.md
curl -sL -o /dev/null -w "%{http_code} install\n" \
  https://raw.githubusercontent.com/thedotmack/claude-mem/main/claude-mem-cursor/skills/install/SKILL.md
curl -sL -o /dev/null -w "%{http_code} host-observer\n" \
  https://raw.githubusercontent.com/thedotmack/claude-mem/main/claude-mem-grok-bot/skills/host-observer/SKILL.md
curl -sL -o /dev/null -w "%{http_code} agent-cost-report\n" \
  https://raw.githubusercontent.com/thedotmack/claude-mem/main/cowork/skills/agent-cost-report/SKILL.md
```

Expect `200` on all four. Read one before installing: the frontmatter `name` and `description` are the routing contract, and `claude-mem-grok-bot/skills/host-observer/SKILL.md` is a good contrast case, since it is a five-paragraph output contract for a summarizer model rather than a workflow for a coding agent. The same file name means different things in different harness trees, so check which tree you are reading.

After a Hermes install, confirm the files landed and the wiring is in place:

```bash
ls -l ~/.hermes/plugins/claude-mem/
grep -A6 "memory:" ~/.hermes/config.yaml
ls -l ~/.hermes/plugins/claude-mem/scripts/mcp-server.cjs
```

Then confirm the runtime itself is healthy, since everything else depends on the worker:

```bash
npx claude-mem doctor
```

`doctor` is the README's own diagnostic for the common failure, hooks reporting `Executable not found in $PATH`. If the memory tools do not appear in a new Hermes session, check the `mcp_servers.claude-mem` block first, then the worker, then the hook path.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-29) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| mem-search | Pass | Pass | Pass |
| smart-explore | Pass | Pass | Pass |
| make-plan | Pass | Pass | Pass |
| do | Pass | Pass | Pass |
| timeline-report | Warn | Pass | Pass |
| claude-mem-install | Pass | Pass | Pass |

No listing in the sample fails, and five of the six are clean on all three auditors. The single Warn is Gen Agent Trust Hub on timeline-report, which is a report generator over your own project history: the plausible reason for a warn is breadth rather than a malicious step, because it reads the timeline and writes a narrative document, and the pack does not include the finding text, so this guide will not guess at it. Open the timeline-report security page on skills.sh and read the finding before you let an unattended job run it over a repository that holds credentials.

The larger risk surface is not the skill files at all. A hook on every tool call sends observations to a model for compression, so decide up front which provider sees that text (the hosted observer, your own OpenRouter or Gemini key, or your Anthropic plan), and use the `<private>` tag support to keep secrets out of storage. Cloud sync and screenshots are both opt-in and are the two features that move data off the machine.

## Limitations

- Snapshot data, verified 2026-10-29: 101,470 combined installs across 34 indexed listings; 104,989 GitHub stars; Apache-2.0; last pushed 2026-10-29. Counts drift over time.
- The index and the tree disagree. skills.sh indexes 34 listings, but the repository carries 44 SKILL.md files because the same skill is copied into per-harness trees: 30 under `plugin/skills/`, 4 under `openclaw/skills/`, 3 under `claude-mem-cursor/skills/`, 4 under `claude-mem-grok-bot/skills/` and 3 under `cowork/skills/`. Names like mem-search, agent-cost-report and install exist more than once with different bodies, so the install count per name is not a count of distinct procedures.
- Most of these skills are not standalone. They call a local worker over HTTP and expect its MCP tools (search, timeline, get_observations, save_memory), so a bare `npx skills add` gives you instructions that cannot execute until `npx claude-mem install` has run on that machine.
- Runtime weight is non-trivial: Node 20 or later, Bun auto-installed for the worker, uv for vector search, a SQLite database, a Chroma index and a background service. This is infrastructure with its own upgrade path (15.7.0 at time of writing), not a markdown file.
- Several skills are repository maintenance for claude-mem itself (version-bump, claude-code-plugin-release, build-and-release, release, ccs-align). Installing them for an unrelated project means installing someone else's release choreography.
- Lifecycle hooks mean the agent's tool calls are captured by default, including file contents and command output. Provider choice, `<private>` tags and the opt-in screenshot setting are the controls, and they need a decision before the first session, not after.

## Related

- [AgentMemory Setup - Persistent Memory for Hermes Agents](/hermes/skills/catalog/agentmemory-setup)
- [OpenViking Skills - Agent Context Database Setup](/hermes/skills/catalog/openviking-setup)
- [memoria-vault - Multi-Agent Research OS for Obsidian Setup](/hermes/skills/catalog/memoria-vault-setup)
- [Hermes Memory Stack Setup](/hermes/skills/catalog/hermes-memory-stack-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the worker before the skills. `npx claude-mem install --ide hermes` gives you the provider and the MCP tools; the individual skills only make sense on top of that, and a skill installed without the worker fails quietly rather than loudly.
- Follow the three step retrieval discipline in mem-search. Search returns IDs cheaply, timeline gives context, get_observations is the expensive call. Batch IDs into one get_observations call instead of fetching them one at a time.
- Use `<private>` tags for anything credential shaped. Hooks capture tool output by default, and the compression step sends that text to whichever provider you selected, so redaction has to happen at capture time.
- Read the harness tree that matches your setup. The Cursor, Grok Bot, Cowork and OpenClaw copies of the same skill name vary in runtime and tool names (mem_search versus claude_mem_search versus search), and pasting the wrong variant into a different harness produces calls that do not exist.
- Watch the worker, not the skill. When memory stops appearing, `npx claude-mem doctor` and the worker service are almost always the problem, and the agent will keep working silently without memory in the meantime.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
