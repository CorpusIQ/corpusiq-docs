---
title: "Cline SDK Skill - Build AI Agents on @cline/sdk"
description: "cline/sdk-skill: 5.1K combined installs. One Apache-2.0 skill on the Cline Agent runtime, ClineCore sessions, custom tools and plugins."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/cline-sdk-skill-setup/"
robots: "index,follow"
last_updated: "2026-11-02"
tags: ["hermes skill", "agent skill", "skill setup", "cline", "agent sdk", "typescript", "multi-agent"]
---

# Cline SDK Skill - Setup Guide

**Source:** [cline/sdk-skill](https://www.skills.sh/cline/sdk-skill) via skills.sh - 5.1K combined installs across 1 indexed listing; first documented 2026-11-02 (evening sweep)

**GitHub:** [cline/sdk-skill](https://github.com/cline/sdk-skill) - 8 stars, Apache-2.0, branch main, last pushed 2026-06-17; one skill at `skill/cline-sdk/` with a 213-line `SKILL.md` and 15 reference files across 9 topic folders

**Category:** Building agents with the Cline SDK: the direct Agent runtime, ClineCore sessions, tools, plugins, providers and multi-agent deployment

**Quality Tier:** 🟢 Green - all three sampled auditors pass, the licence is Apache-2.0, and the repository holds nothing but Markdown

This is the official reference skill for `@cline/sdk`, published by the Cline organisation as a companion to the SDK documentation at docs.cline.bot/sdk. It is small in surface area and deliberately so: one skill, one manifest, and fifteen reference files that an agent loads only when a task needs them. The repository has three top-level entries, `LICENSE`, `README.md` and `skill/`, and no build step, no dependencies and no scripts.

The skill is written for agents that are about to write agent code, which is a narrower audience than it first appears. Its `SKILL.md` spends most of its length on the decisions that are hard to reverse: which of the two API surfaces to use, how the event systems differ between them, when a tool should end the run, and which parts of the plugin system are file-based rather than registered. Get one of those wrong and the code compiles, runs, and then behaves nothing like the author intended.

## Installation

The README gives one command:

```bash
npx skills add cline/sdk-skill
```

It states that this works with Cline CLI, Claude Code, Codex, Cursor, Gemini CLI, GitHub Copilot, Goose, OpenCode and Windsurf. For a manual install the README covers five agents with the same three steps, a clone into `~/sdk-skill` and a symlink from the agent's skill folder. The Claude Code version:

```bash
git clone https://github.com/cline/sdk-skill ~/sdk-skill
mkdir -p ~/.claude/skills
ln -s ~/sdk-skill/skill/cline-sdk ~/.claude/skills/cline-sdk
```

The same pattern is documented for Codex CLI at `~/.codex/skills`, Amp at `~/.config/amp/tools`, Droid at `~/.factory/skills` and pi-coding-agent at `~/.pi/agent/skills`, with a note that project-level paths work for per-project installation.

Because those routes are symlinks into the clone rather than copies, the clone is load-bearing. Move or delete `~/sdk-skill` and the skill disappears from the agent while the folder listing still looks installed. A copy of `skill/cline-sdk/` into a profile avoids that, and it is safe here because the folder is self-contained: the references live inside it, unlike a skill that points at a sibling documentation tree.

Nothing else has to be installed for the skill to load. To use what it describes you need Node.js 22 or later and `@cline/sdk`, which the skill's first rule pins down: install `@cline/sdk`, because that package re-exports `@cline/core`, and import from `@cline/agents`, `@cline/llms` or `@cline/shared` only for the parts core does not re-export.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| cline-sdk | 5,104 | Building agents with `@cline/sdk`: choosing between the direct Agent runtime and ClineCore, creating tools with Zod or JSON Schema, plugin and extension systems, streaming events, LLM provider configuration, scheduling, multi-agent teams and production deployment. |

All 1 indexed listings clear the threshold and appear in the table above.

The references follow a pattern the skill explains explicitly. Both main API surfaces get four files each, `REFERENCE.md` for the overview and quick start, `api.md` for the full class and config surface, `patterns.md` for implementation guidance and `gotchas.md` for pitfalls and debugging. The seven cross-cutting topics, tools, plugins, events, providers, production, scheduling and multi-agent, get a single `REFERENCE.md` each, which is the entry point. The `SKILL.md` then supplies decision trees that map a question to one of those files, so an agent can arrive at "I need scheduled agents" and land on the scheduling reference instead of reading the whole tree.

The nine critical rules in the manifest are where the real value sits, because each one is a mistake that produces working-looking code. Tool names must be `snake_case`. A tool that should end the loop needs `lifecycle: { completesRun: true }`. ClineCore must be disposed. The Agent and ClineCore have different event systems, and a text delta is `assistant-text-delta` on one and an `agent_event` payload with `content_start`, `content_update` and `content_end` on the other, with result text at `result.outputText` versus `result.text`. Direct Agent plugins are `setup(context)` returning tools and hooks, while ClineCore extensions are `AgentPlugin` objects with a manifest. Plugin skills are files at `<package>/skills/<name>/SKILL.md`, discovered and surfaced as slash commands, with no `registerSkill` call to make.

## Why This Matters for Hermes Agents

An SDK skill earns its place when the framework has more than one way to do the same thing and the wrong choice is not obvious until later. The Cline SDK has two surfaces: a lightweight in-memory Agent loop, and ClineCore with persistence, built-in tools, config discovery and hub-backed session sharing. The skill's decision tree resolves that in one question, "do you need sessions, built-in tools, scheduling or multi-client sharing", and stops an agent from hand-rolling persistence on top of the simpler surface.

The event system is the second reason. The two surfaces emit different types, and the skill calls out the specific trap: `content_start` and `content_update` are host-facing `AgentEvent` types carried inside ClineCore `agent_event` events, and using them with `agent.subscribe()` does not work. There is also no top-level `onEvent` field on `AgentRuntimeConfig`, only `agent.subscribe()` or `hooks.onEvent`. Those are the details that cost an afternoon of silent nothing-happens debugging, and they are stated as rules rather than as prose.

The plugin-versus-extension distinction is the third. Direct Agent takes simple runtime plugins; ClineCore takes `AgentPlugin` objects with manifests. Copying an example from one into the other is a natural mistake when both are visible in the same reference tree, and the skill names it directly. It also corrects a misconception that most agents carry from other frameworks: skills in this plugin model are files on disk that the host discovers, not something a plugin registers at runtime.

Finally, the skill is honest about lifecycle. `dispose()` on ClineCore, structured error data for tool failures the agent can recover from, and a completion flag for tools that should end the run are all small rules that keep a long-running agent from leaking resources or looping forever. For a builder wiring agents into services, those three are the difference between a demo and something that survives a week.

## Usage

| You say | What happens |
|---|---|
| "Build a minimal agent that reads a file and answers a question" | Walks the Agent surface, installs `@cline/sdk`, creates the agent with a `createTool` tool and reads `result.outputText` at the end. |
| "I need conversations to survive a restart" | Follows the decision tree to ClineCore, which has session persistence and the built-in file, shell and search tools, and calls `dispose()` when done. |
| "Make the agent stop as soon as it submits an answer" | Adds `lifecycle: { completesRun: true }` to the submit tool, which ends the agent loop instead of letting it continue. |
| "Stream the assistant text into my UI" | Uses `agent.subscribe()` with `assistant-text-delta` on the Agent surface, or `cline.subscribe()` and the `agent_event` payloads with `content_start`, `content_update`, `content_end` and `done` on ClineCore. |
| "Wrap our internal tools as a plugin" | Uses `AgentPlugin` with `setup(api, ctx)` for ClineCore, registers an MCP server with the `mcp` capability, and ships skills as `SKILL.md` files rather than registering them. |
| "Run this agent every morning at eight" | Loads the scheduling reference, which covers ClineCore's automation API rather than an external cron wrapper. |
| "I want a researcher agent and a writer agent that hand off" | Uses the multi-agent reference and configured agent profiles as YAML in `.cline/agents/`, surfaced as `subagent_<name>` tools when spawn is enabled. |

## Verification

The raw path below returned 200 on branch main on 2026-11-02, and so did the Agent reference it points at:

```bash
for p in skill/cline-sdk/SKILL.md skill/cline-sdk/references/agent/REFERENCE.md; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/cline/sdk-skill/main/$p"
done
```

After a clone, confirm the reference tree arrived whole. This is the check that matters, since `SKILL.md` is a set of pointers:

```bash
git clone --depth 1 https://github.com/cline/sdk-skill.git /tmp/cline-sdk-skill
find /tmp/cline-sdk-skill/skill -name '*.md' | wc -l
ls /tmp/cline-sdk-skill/skill/cline-sdk/references
head -4 /tmp/cline-sdk-skill/skill/cline-sdk/SKILL.md
```

The file count should print 16, one manifest plus fifteen references, and the listing should show `agent`, `clinecore`, `events`, `multi-agent`, `plugins`, `production`, `providers`, `scheduling` and `tools`. On the installed copy:

```bash
ls ~/.hermes/profiles/corpusiq/skills/cline-sdk/references/agent
grep -c 'references/' ~/.hermes/profiles/corpusiq/skills/cline-sdk/SKILL.md
```

The agent folder should hold `REFERENCE.md`, `api.md`, `patterns.md` and `gotchas.md`, and the grep should return a non-zero count of pointers. A copy with the manifest alone loads and then answers questions with no detail behind them.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-02) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| cline-sdk | Pass | Pass | Pass |

All three auditors pass, which is consistent with what the repository contains: a licence, a README and a folder of Markdown. Nothing executes on install, there is no dependency to audit, and the skill cannot change the machine it lands on.

The capability it teaches is a different matter, and it is worth naming even under a green tier. This skill documents how to build agents that run shell commands, patch files, search a codebase and fetch web content, and how to register MCP servers and plugins that add more. An agent that reads it is being taught to assemble a system with real reach. Apply the same review you would to any code that spawns a shell, keep the tool policies section in view when you decide which built-in tools to expose, and treat provider API keys as secrets that belong in the environment rather than in an agent profile.

One detail from the plugin rules is also a security boundary: plugin skills are discovered from `<package>/skills/<name>/SKILL.md` and surfaced as slash commands automatically. Anything that can write into a plugin package can therefore add a command, so pin plugin versions rather than installing from a moving branch.

## Limitations

- Snapshot data, verified 2026-11-02: 5,104 combined installs across 1 indexed listing; 8 GitHub stars; Apache-2.0; last pushed 2026-06-17. Counts drift over time.
- The repository was last pushed in June 2026, several months before this snapshot, while the SDK it documents continues to move. The files do not state which `@cline/sdk` version the references were written against, so check the API reference against the installed release before trusting a signature.
- Eight stars and a single package folder is very little third-party scrutiny. The install count reflects skills.sh indexing, not independent adoption, and there is no issue history to mine for known gaps.
- The README's manual install routes are symlinks into `~/sdk-skill`. Deleting or moving that clone silently removes the skill from the agent, and the documented paths are all user-level, so a per-project install needs a path adjustment.
- The documentation lives in nine folders with an explicit reading order. An agent that loads `api.md` without `REFERENCE.md` gets signatures with no guidance on which surface they belong to.
- There is exactly one skill and no scripts, examples folder or test suite, so there is nothing to run to check that the guidance still matches the SDK's current behaviour.

## Related

- [Claude Code Skills - Agentic Coding & Skill Development Setup](/hermes/skills/catalog/claude-code-skills-setup)
- [Cline Skills - Official Cline 43-Skill Collection Setup](/hermes/skills/catalog/cline-skills-setup)
- [Superpowers - Agentic Skills Framework Setup](/hermes/skills/catalog/superpowers-setup)
- [Agent Toolkit - 44 Skills for Coding Agents Setup](/hermes/skills/catalog/agent-toolkit-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Answer the surface question before writing a line. If the task needs persistence, built-in tools, scheduling or multi-client sessions, it is ClineCore; if it needs a browser-compatible loop with no Node dependencies, it is Agent.
- Read `gotchas.md` for the surface you chose. It is the file that lists the event-name and config-shape mistakes, and it is shorter than debugging them.
- Keep the event systems separate in your head. `assistant-text-delta` and `result.outputText` belong to Agent; `agent_event` payloads and `result.text` belong to ClineCore.
- Mark the tool that should end the run with `completesRun: true` rather than prompting the model to stop. The loop, not the model, should own termination.
- Always dispose a ClineCore instance. It is the one rule in the manifest with no visible symptom until a long-running process has leaked for a day.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
