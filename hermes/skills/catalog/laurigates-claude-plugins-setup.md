---
title: "Laurigates Claude Plugins - Python and Ops Suite"
description: "laurigates/claude-plugins on skills.sh: 17.4K combined installs across 197 listings; Python quality, uv, pytest and packaging skills for agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/laurigates-claude-plugins-setup/"
robots: "index,follow"
last_updated: "2026-11-04"
tags: ["hermes skill", "agent skill", "skill setup", "python", "uv", "pytest"]
---

# Laurigates Claude Plugins - Setup Guide

**Source:** [laurigates/claude-plugins](https://www.skills.sh/laurigates/claude-plugins) via skills.sh - 17.4K combined installs across 197 indexed listings; first seen 2026-11-04 (Nov 4, 2026 evening sweep)
**GitHub:** 59 stars, MIT licence, last pushed 2026-11-05, 473 SKILL.md directories across plugin directories such as python-plugin/skills and agent-patterns-plugin/skills
**Category:** Python engineering workflow: ruff and ty quality checks, pytest, uv project and workspace management, packaging and interpreter versions, plus image conversion
**Quality Tier:** 🟡 Beta - Snyk Warn on blueprint-prp-create; MIT; 59 stars.

The README describes this as a curated collection of 49 Claude Code plugins providing 400+ skills and 22 agents for development workflows, and the same skills, subagents and safety hooks run in OpenCode, pi and Antigravity CLI. Skills are read in place from a checkout of the repo, so an edit reaches every harness without a copy step; subagents and hooks are exported into each tool's own format.

The install count on skills.sh is dominated by one stack. Fourteen listings clear 250 installs and nearly all of them are the Python toolchain: ruff, basedpyright, vulture, pytest, and six separate uv skills covering projects, workspaces, script runs, packaging, interpreter versions, dependencies and global CLI tools. The only outlier is ImageMagick conversion at 258.

## Installation

Claude Code takes the plugins through its marketplace. From the README:

```bash
claude plugin marketplace add laurigates/claude-plugins
```

```bash
claude plugin install git-plugin@laurigates-claude-plugins
```

```bash
claude plugin install python-plugin@laurigates-claude-plugins
```

Inside a session, `/plugin` browses and installs the same plugins. The Python skills in the table below live in `python-plugin`. For the other harnesses the README clones the repo and runs a `just` recipe. OpenCode needs bun and just:

```bash
git clone https://github.com/laurigates/claude-plugins && cd claude-plugins
(cd adapters && bun install)
just setup-opencode
```

Replace the last line with `just setup-pi` for pi, or run `just setup-antigravity` for Antigravity CLI, which needs just and Python 3. The README states Bash 5+ as a prerequisite for the shell scripts; macOS ships 3.2, so install a newer bash there.

## What It Provides

Fourteen listings clear the 250 install threshold.

| Skill | Installs | Use For |
|---|---|---|
| python-code-quality | 1,041 | Orchestration index over the Python quality stack: ruff, ty, linting, formatting, type checking and code style, routing to the focused skill that owns each tool |
| ruff-linting | 482 | Linting with ruff: rule selection, auto-fixing and configuration for finding bugs and enforcing standards |
| python-testing | 436 | pytest with coverage, fixtures and mocking when writing or debugging Python tests |
| pytest-advanced | 360 | Advanced pytest: fixtures, markers, parametrization and parallel execution for test infrastructure work |
| uv-project-management | 332 | Creating Python projects, managing dependencies, lockfiles and pyproject.toml with uv |
| uv-workspaces | 331 | Multi-package Python projects with uv workspaces: monorepos, shared lockfiles and member dependencies |
| basedpyright-type-checking | 331 | Static type checking with basedpyright, including LSP setup and comparison against pyright and mypy alternatives |
| vulture-dead-code | 330 | Detecting unused functions, classes and imports with vulture and deadcode before a cleanup |
| uv-run | 317 | Running Python scripts with uv, including PEP 723 inline dependencies and one-off dependencies through --with |
| python-packaging | 309 | Building and publishing packages with uv: wheels, sdists, entry points and PyPI uploads |
| uv-python-versions | 307 | Installing and managing CPython and PyPy interpreters with uv python, including .python-version files |
| uv-advanced-dependencies | 307 | Git and path dependencies, editable installs, dependency groups, extras and custom indexes |
| uv-tool-management | 303 | Installing and managing global Python CLI tools with uv tool and uvx, as a pipx replacement |
| imagemagick-conversion | 258 | ImageMagick format conversion, resizing, batch processing, quality settings and thumbnail generation |

The remaining 183 indexed listings range from 45 to 235 installs.

## Why This Matters for Hermes Agents

Python work is where agents most often produce a plausible-looking mess: a requirements file instead of a lockfile, a module-level script that assumes an activated venv, a test suite full of brittle mocks. The uv family here replaces all of that with one deterministic tool that the agent can drive from the command line.

The split into focused skills is the useful part. A single "Python" skill would be too large to load and too vague to act on. Six uv skills mean an agent that needs to run a one-off script loads PEP 723 and `--with` behaviour, and nothing else, while a task about publishing a wheel loads packaging instead.

python-code-quality is deliberately an index rather than an implementation: it routes to the skill that owns each tool and does not restate their commands. That is a good pattern for any skill collection that is growing past the point where one file can hold it.

The collection also solves a problem the README is candid about. Native skill listing in OpenCode and pi measured roughly 34,000 tokens of context per turn for 382 skills, which is unaffordable; the adapter reaches all of them for about 600 by injecting only the top matches as a `search_skills` tool. Any agent whose skill library grows should expect to need the same trick.

Finally, the harness matrix matters for portability. The same SKILL.md files are read by Claude Code, OpenCode, pi and Antigravity CLI, so a workflow written once is not locked to one tool.

## Usage

| You say | What happens |
|---|---|
| "Set up this directory as a uv project" | uv-project-management creates the project, writes pyproject.toml and pins a lockfile |
| "Run this script without activating a venv" | uv-run resolves inline PEP 723 dependencies or takes one-off packages through --with |
| "Why is this test flaky?" | pytest-advanced inspects fixtures, markers and parametrization, and can move to parallel execution |
| "Find dead code before we refactor" | vulture-dead-code scans for unused functions, classes and imports |
| "Split this repo into two installable packages" | uv-workspaces configures members and a shared lockfile |
| "Publish this package to PyPI" | python-packaging builds the wheel and sdist and walks the upload path |
| "Resize these product images to thumbnails" | imagemagick-conversion batches the resize and sets output quality |

## Verification

Fetch one skill file and confirm the frontmatter is intact (probed 2026-11-04, HTTP 200):

```bash
curl -fsSL https://raw.githubusercontent.com/laurigates/claude-plugins/main/python-plugin/skills/ruff-linting/SKILL.md | head -8
```

Then confirm the plugin registered. Inside a Claude Code session, `/plugin` lists what is installed. On disk, count the Python plugin skills, adjusting the root if your harness keeps plugins elsewhere:

```bash
find ~/.claude -name SKILL.md -path '*python-plugin*' | wc -l
```

For the non-Claude routes, `just agy-check` reports what the Antigravity setup installed, and the OpenCode and pi recipes print the paths they wrote.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-04) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| python-code-quality | Pass | Pass | Pass |
| ruff-linting | Pass | Pass | Pass |
| python-testing | Pass | Pass | Pass |
| blueprint-prp-create | Pass | Pass | Warn |

## Limitations

- Snapshot data, verified 2026-11-04: 17,424 combined installs across 197 indexed listings; 59 GitHub stars; MIT licence; last pushed 2026-11-05. Counts drift over time.
- The index and the tree count differently: 197 listings on skills.sh against 473 SKILL.md directories in the repo, because the tree also includes repo-local `.claude/skills` entries, plugin skills that the index groups separately, and test fixtures under `adapters/tests/fixtures/`.
- The README describes 49 plugins carrying 400+ skills; that figure is the repo's own count of everything it ships, not the number of indexed listings in the table above.
- Installing python-plugin does not bring the git, agent-patterns or health plugins. The README recommends `/health-plugin:health-check` and its Plugin Map for a tiered install order.
- The OpenCode and pi routes need a clone plus bun and just, and the shell scripts need Bash 5+. macOS ships Bash 3.2.
- blueprint-prp-create carries a Snyk Warn while the three Python skills sampled pass all three scanners, so the warn is not a property of the Python stack.

## Related

- [Astral Plugins - Python uv, ruff and ty Setup](/hermes/skills/catalog/astral-sh-claude-code-plugins-setup)
- [CXUU Golang Skills - Go Engineering Suite](/hermes/skills/catalog/cxuu-golang-skills-setup)
- [Cypress AI Toolkit - E2E Testing Skills](/hermes/skills/catalog/cypress-ai-toolkit-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with python-code-quality when you are unsure which tool applies. It is an index, so it routes rather than duplicating the focused skills.
- Prefer uv-run over activating a venv in agent sessions. A command with inline dependencies is reproducible and leaves no shell state behind.
- Install only the plugins a project needs. The collection is 49 plugins, and the per-turn skill listing cost is real once a library grows.
- Keep `just setup-opencode` output. It prints the local model and adapter paths, which is the fastest way to diagnose a missing skill later.
- Treat the Snyk Warn on blueprint-prp-create as a reason to read that skill before running it, not as a reason to avoid the Python stack.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
