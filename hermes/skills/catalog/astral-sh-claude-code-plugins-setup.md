---
title: "Astral Plugins - Python uv, ruff and ty Setup"
description: "astral-sh/claude-code-plugins: 11.9K combined installs. Three skills that teach agents uv project management, ruff linting and ty type checking."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/astral-sh-claude-code-plugins-setup/"
robots: "index,follow"
last_updated: "2026-11-03"
tags: ["hermes skill", "agent skill", "skill setup", "python", "uv", "ruff", "type checking"]
---

# Astral Plugins - Setup Guide

**Source:** [astral-sh/claude-code-plugins](https://www.skills.sh/astral-sh/claude-code-plugins) via skills.sh - 11.9K combined installs across 3 indexed listings; first documented 2026-11-03 (nightly sweep)

**GitHub:** [astral-sh/claude-code-plugins](https://github.com/astral-sh/claude-code-plugins) - 318 stars, Apache-2.0 detected with both `LICENSE-APACHE` and `LICENSE-MIT` present (dual licensed, Apache-2.0 or MIT at your option), branch main, last pushed 2026-02-27; one plugin at `plugins/astral/` carrying its own `.claude-plugin/plugin.json`, with the three skills in `plugins/astral/skills/uv`, `plugins/astral/skills/ruff` and `plugins/astral/skills/ty`, plus a marketplace manifest at `.claude-plugin/marketplace.json`

**Category:** Python tooling practice: package and project management with uv, linting and formatting with ruff, type checking with ty

**Quality Tier:** 🟢 Green - all three sampled listings pass every auditor and the repository ships both licence files

Astral publishes these three skills as a Claude Code plugin, one skill per tool, written in the second person to an agent. Each file opens with the same decisive instruction: always use this tool for the job, and here is how to tell when the project has already chosen something else. The uv skill says not to reach for uv in a Poetry or PDM project; the ruff skill warns against reformatting a file the project never formatted, because a diff touching every line hides the change you were asked to make.

That last detail is the reason the set is worth installing rather than reading once. The value is not the command list, which a model already knows approximately, but the judgment around it: which workflow applies to a script versus a project, when to call `uv run` for the pinned version instead of `uvx` for a one-off, and how to keep a lint fix scoped to the file being edited. Those are the choices that turn a correct-looking command into a clean diff.

All three files are short: `uv` is 182 lines, `ty` is 135 and `ruff` is 134. The plugin also ships a language server entry for ty, which is a Claude Code runtime feature rather than a skill, and it is noted below because it changes what happens at plugin load.

## Installation

The skills CLI route, which is the one that works for a Hermes profile:

```bash
npx skills add astral-sh/claude-code-plugins
```

The plugin route, as the README documents it for Claude Code:

```
/plugin marketplace add astral-sh/claude-code-plugins
/plugin install astral@astral-sh
```

Once installed in Claude Code, skills are invoked explicitly as `/astral:uv`, `/astral:ruff` and `/astral:ty`, and the README recommends one line in `CLAUDE.md` so the model reaches for them without being asked: when working with Python, invoke the relevant `/astral:<skill>` for uv, ty and ruff. For a team install, the same README adds the marketplace and enables the plugin in `.claude/settings.json` with `extraKnownMarketplaces` pointing at `astral-sh/claude-code-plugins` and `enabledPlugins` setting `astral@astral-sh` to true.

For a manual Hermes install, clone and copy the skill directories you want:

```bash
git clone --depth 1 https://github.com/astral-sh/claude-code-plugins.git /tmp/astral-plugins
cp -r /tmp/astral-plugins/plugins/astral/skills/uv ~/.hermes/profiles/corpusiq/skills/
cp -r /tmp/astral-plugins/plugins/astral/skills/ruff ~/.hermes/profiles/corpusiq/skills/
cp -r /tmp/astral-plugins/plugins/astral/skills/ty ~/.hermes/profiles/corpusiq/skills/
```

There is nothing else in each directory to copy. No `references/` tree, no scripts, no hooks: one `SKILL.md` per tool, so the install is three files and the plugin scaffolding is only needed by Claude Code.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| uv | 5,157 | Python packaging and project management with uv: scripts, projects, tools, dependency groups, lockfiles, and recognising projects that use Poetry or PDM instead. |
| ruff | 3,602 | Linting, formatting and fixing Python with ruff: check and format commands, scoped fixes, rule selection and when not to reformat. |
| ty | 3,190 | Type checking Python with ty: check commands, rule configuration, and setting type checking up in a project. |

No indexed listings fall below the threshold; all 3 appear above.

The three skills share a structure, which makes them easy to hold together: a "when to use" section with the file signals to look for, an invocation section choosing between `uv run`, `uvx` and a globally installed binary, and then a command reference. The uv file goes furthest, covering the script, project and tool workflows separately, since those are the three ways people get uv wrong.

## Why This Matters for Hermes Agents

Python is the default language for agent scripts, and the default Python workflow on most machines is whatever the model half-remembers: `pip install` into a system interpreter, a `venv` nobody activated, or a `requirements.txt` invented from imports. The uv skill replaces that with a decision the agent can state out loud, script versus project versus tool, and the commands that follow from it.

The ruff and ty files matter for a subtler reason. An agent that lints aggressively can produce a review diff nobody can read, and both skills anticipate that: ruff tells the agent to scope fixes to the file being edited and to skip formatting a codebase that never used ruff, while ty's file is about wiring the checker in rather than silencing it. That is the behaviour you want from an agent working inside someone else's repository.

There is also a cost argument. A type checker and a linter that run in a second let an agent verify its own work before claiming success, which is cheaper than a round trip through a human reviewer. ty and ruff are both built for that loop, and these skills document the invocation forms that keep the versions pinned to the project.

## Usage

| You say | What happens |
|---|---|
| "Set up a new Python project for this script collection" | Follows the uv project workflow: initialise, add dependencies, and run through `uv run` so the lockfile stays authoritative. |
| "Lint and format the file I just changed" | Loads ruff, runs `uv run ruff check` and `uv run ruff format` scoped to that file, and leaves the rest of the tree alone. |
| "Why is this type error only showing up in CI?" | Uses ty for the check command, rule configuration and the difference between a project-pinned and a one-off invocation. |
| "Convert this requirements.txt repo to uv" | Works the uv project path, checks for `poetry.lock` or `pdm.lock` first, and stops if the project has already chosen another manager. |
| "Add a CI step that fails on lint and type errors" | Combines the two skills into a check job: ruff for lint and format, ty for types, both invoked on the pinned versions. |
| "Run this one script with a package it does not declare" | Uses the uv script workflow, either `uv run --with` for a single run or an inline script dependency when the dependency should persist. |

## Verification

The raw path below returned 200 on branch main on 2026-11-03:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/astral-sh/claude-code-plugins/main/plugins/astral/skills/uv/SKILL.md
```

After a clone, confirm three skills and read the frontmatter the runtime routes on:

```bash
git clone --depth 1 https://github.com/astral-sh/claude-code-plugins.git /tmp/astral-plugins
find /tmp/astral-plugins/plugins/astral/skills -name SKILL.md | wc -l
head -5 /tmp/astral-plugins/plugins/astral/skills/uv/SKILL.md
ls /tmp/astral-plugins/LICENSE-APACHE /tmp/astral-plugins/LICENSE-MIT
```

The count should print 3 and the header should show `name: uv` followed by the description. Both licence files should be listed; if either is missing, the licence claim in this guide no longer holds. On the installed copy:

```bash
ls ~/.hermes/profiles/corpusiq/skills/uv ~/.hermes/profiles/corpusiq/skills/ruff ~/.hermes/profiles/corpusiq/skills/ty
grep -n 'uv run' ~/.hermes/profiles/corpusiq/skills/uv/SKILL.md | head -3
```

Each directory should hold one `SKILL.md`, and the grep should show the invocation guidance rather than an empty result.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-03) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| uv | Pass | Pass | Pass |
| ruff | Pass | Pass | Pass |
| ty | Pass | Pass | Pass |

The three skills are Markdown and nothing else. Loading one runs no code, installs no package and opens no socket; the repository's only non-Markdown files are two licence texts, a README, a CONTRIBUTING guide, a Prettier config and two plugin manifests.

Two execution paths do exist around the skills, and both are worth naming. The first is the skills themselves: they instruct an agent to run `uv add`, `uv sync`, `uv run` and `uvx`, each of which resolves and downloads packages from PyPI, so an agent holding these can change an environment. That is the intent, but it means the skill belongs behind the same review as any dependency change. The second is Claude Code specific: the plugin manifest declares an LSP server for ty as `uvx ty@latest server`, which fetches and runs the latest ty release at startup rather than a pinned one. On a Hermes profile none of that applies, because the plugin manifest is not read, but anyone using the Claude Code route should know the version is unpinned.

The ruff listing carries one code, E501, alongside its three passes. E501 is the line-length rule, so read it as a lint note on the skill's own Markdown rather than a finding about what the skill does.

Licensing is clean here, which is unusual for this catalog. Both `LICENSE-APACHE` and `LICENSE-MIT` ship at the repository root, the README states the dual licence explicitly, and the contribution terms say submissions are dual licensed on the same terms unless stated otherwise. Redistribution is covered.

## Limitations

- Snapshot data, verified 2026-11-03: 11,949 combined installs across 3 indexed listings; 318 GitHub stars; Apache-2.0 (dual licensed with MIT); last pushed 2026-02-27. Counts drift over time.
- Coverage is exactly three tools. There is no packaging, testing, framework or deployment guidance in the plugin, so it complements a broader Python skill set rather than replacing one.
- The last push was roughly eight months before this snapshot, so the commands reflect the tools as of early 2026. Check current flags against the installed versions.
- The ty language server entry pulls `ty@latest` through `uvx` at startup, which is unpinned by design and only relevant on the Claude Code plugin route.
- The documented invocation model is Claude Code's `/astral:<skill>` slash command. Outside that runtime the skills are routed by their descriptions, which works but is less deterministic.
- Agent runs of `uv add` or `uv sync` change the environment and download from PyPI. Treat a run that touches dependencies as a reviewed change, not a read-only step.

## Related

- [OpenAI Agents Python Skills - Multi-Agent Setup](/hermes/skills/catalog/openai-agents-python-skills-setup)
- [Qodo Skills - Code Review and Standards Suite](/hermes/skills/catalog/qodo-skills-setup)
- [Gemini CLI Skills - Repository Workspace Pack](/hermes/skills/catalog/gemini-cli-skills-setup)
- [Science Skills - PubMed, arXiv and Lab Data Setup](/hermes/skills/catalog/science-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install all three. They are 451 lines combined and they cross-reference naturally: uv for the environment, ruff for style, ty for types.
- Tell the agent whether the tool is a project dependency. `uv run ruff` uses the pinned version and `uvx ruff` uses a downloaded one, and the skills only choose correctly if the model knows which situation it is in.
- Ask for scoped fixes explicitly. Without that instruction, ruff will happily reformat a file nobody asked you to touch, and the real diff disappears.
- Check for `poetry.lock` and `pdm.lock` before migrating anything. The uv skill says to leave those projects alone, and it is right.
- Keep the licence files with any internal mirror. This is the rare plugin in the catalog where the dual Apache-2.0 and MIT grant is actually shipped, so a vendored copy stays clean.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
