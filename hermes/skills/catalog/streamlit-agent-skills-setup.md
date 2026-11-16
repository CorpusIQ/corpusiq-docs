---
title: "Streamlit Agent Skills - Data App Development"
description: "streamlit/agent-skills: 3.5K combined installs from one listing, a meta-skill that finds the Streamlit skills bundled in the installed pip package."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/streamlit-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-15"
tags: ["hermes skill", "agent skill", "skill setup", "streamlit", "python", "data apps"]
---

# Streamlit Agent Skills - Setup Guide

**Source:** [streamlit/agent-skills](https://www.skills.sh/streamlit/agent-skills) via skills.sh - 3.5K combined installs across 1 indexed listing; first seen Nov 14, 2026 (Nov 14 evening sweep)
**GitHub:** 227 stars, Apache-2.0 license, `main` branch, last pushed 2026-07-23, one `SKILL.md` at `developing-with-streamlit/SKILL.md`
**Category:** Python data applications
**Quality Tier:** 🟢 Green - the single sampled skill passes all three auditors.

Streamlit's skill is unusual: it contains almost no Streamlit knowledge. It is a meta-skill that detects the active Python interpreter, locates the installed Streamlit package, and points the agent at the development skills that ship inside it. The actual content, covering layouts, theming, session state, caching and custom components, travels with the library.

Read the deprecation notice before you install. The repository is being archived: as of Streamlit 1.60 the meta-skill is bundled in the pip package at `lib/streamlit/.agents/meta-skill/developing-with-streamlit`, and the recommended path is to upgrade Streamlit and run `streamlit skills` rather than install from this repository. Existing installs keep working, and the `v1` tag is preserved so `npx skills` installs still resolve.

## Installation

The recommended path, on Streamlit 1.60 or later:

```bash
pip install --upgrade streamlit
streamlit skills
```

`streamlit skills` is interactive and asks whether to install at project level, symlinking the bundled skills into `.agents/skills/` and `.claude/skills/` when Claude Code is detected, or at user level so one install covers every project.

The repository path still works and is what an agent registry will resolve today:

```bash
npx skills add streamlit/agent-skills
```

If you use the repository copy, pin it: the meta-skill's discovery logic runs locally, so an archived copy keeps functioning as long as Streamlit's bundled layout does not move.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| developing-with-streamlit | 3,499 | Detecting the active Streamlit install and loading its bundled development skills: layouts, theming, session state, caching, custom components and app structure. |

The single indexed listing appears in the table above.

## Why This Matters for Hermes Agents

The interesting idea here is version-matched guidance. Instead of a skill that describes Streamlit once and drifts, the meta-skill resolves whichever Streamlit version the project actually has installed and loads the skills that shipped with it. A project pinned to an older release gets that release's guidance, and upgrading the library silently upgrades the agent's knowledge.

The interpreter detection is the mechanism worth understanding: the skill handles virtualenv, conda, pipenv, poetry, pdm, uv and system Python, then reads the package path. In a machine running several Python environments, that is the difference between an agent following current guidance and an agent following guidance from a different project's Streamlit.

For agents that write data apps for business users, the payoff is concrete: an agent that knows the installed version's layout and theming rules produces an app that runs, rather than one that uses an API removed two releases ago.

## Usage

| You say | What happens |
|---|---|
| "Build a dashboard for this CSV" | Loads the bundled skills for the installed version and scaffolds the app with current layout primitives. |
| "Add a sidebar filter with session state" | Uses the session state guidance that matches the installed release. |
| "Why is my app slower after adding these charts" | Checks the caching patterns from the bundled skills before rewriting the app. |
| "Theme this to match our brand colours" | Applies the theming guidance for the installed version's configuration surface. |
| "Where do I put a custom component?" | Uses the components guidance and the documented structure. |
| "Our project uses an older Streamlit" | Resolves that project's interpreter and loads its own bundled skills instead of the newest ones. |

## Verification

Confirm the Streamlit version and, on 1.60 or later, that the bundled meta-skill exists:

```bash
python3 -c "import streamlit, os; print(streamlit.__version__); print(os.path.dirname(streamlit.__file__))"
streamlit skills --help
curl -fsSL https://raw.githubusercontent.com/streamlit/agent-skills/main/developing-with-streamlit/SKILL.md | head -20
```

If `streamlit skills` does not exist, the installed version predates the built-in installer and the repository copy is the fallback.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-14) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| developing-with-streamlit | Pass | Pass | Pass |

The repository is Markdown plus a local discovery script (`discover.py`) that only inspects the installed Python environment; it makes no network calls.

## Limitations

- Snapshot data, verified 2026-11-14: 3,499 combined installs across 1 indexed listing; 227 GitHub stars; Apache-2.0; last pushed 2026-07-23. Counts drift over time.
- The repository is deprecated and being archived. New development of the meta-skill happens in `streamlit/streamlit`, not here.
- The skill carries no Streamlit knowledge itself. Everything it teaches comes from the package installed in the project, so a project without Streamlit installed gets the documented fallback to online docs.
- The recommended installer needs Streamlit 1.60 or later; 1.58 and 1.59 support `streamlit skills` for installation but the bundled meta-skill arrived later.
- Discovery depends on the interpreter the agent's shell resolves. A tool that runs in its own environment may not see the project's Streamlit at all.

## Related

- [Marimo Skills - Notebook Agents Setup](/hermes/skills/catalog/marimo-skills-setup)
- [Jupyter Live Kernel Setup](/hermes/skills/catalog/jupyter-live-kernel-setup)
- [DuckDB Skills - Local Analytics for Agents](/hermes/skills/catalog/duckdb-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Prefer the bundled path (`streamlit skills`) on 1.60 or later; it upgrades automatically with the library.
- Install at user level if you work across several projects, since discovery follows the active interpreter rather than a fixed path.
- Tell the agent which interpreter to use when a project has its own virtualenv, or the meta-skill may resolve the wrong Streamlit.
- On an older release, point the agent at `docs.streamlit.io/llms-full.txt` as the documented fallback.
- Do not fork the archived repository to add skills: the canonical location is inside the Streamlit package now.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
