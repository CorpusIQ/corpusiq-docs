---
title: "Agent Stuff - Agent Skill Toolkit for Builders"
description: "Armin Ronacher's agent skills: 5.5K combined installs across 21 listings, OpenSCAD, Chrome DevTools browser control, tmux and gh workflows"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/agent-stuff-setup/"
robots: "index,follow"
last_updated: "2026-11-11"
tags: ["hermes skill", "agent skill", "skill setup", "openscad", "browser automation", "developer tools", "tmux"]
---

# Agent Stuff - Setup Guide

**Source:** [mitsuhiko/agent-stuff](https://www.skills.sh/mitsuhiko/agent-stuff) via skills.sh - 5.5K combined installs across 21 indexed listings (5,538 exact); first seen 2026-11-11 (Nov 11, 2026 sweep)
**GitHub:** 3,212 stars, Apache-2.0 license, `main` branch, last pushed 2026-09-27, 18 `SKILL.md` files under `skills/<name>/` alongside `commands/`, `extensions/`, `themes/` and `intercepted-commands/`
**Category:** Builder utilities: 3D modelling, browser control, binary analysis, git and GitHub workflows, terminal session control, document conversion
**Quality Tier:** 🟡 Mixed - Apache-2.0, the highest star count in this sweep and a genuinely useful toolkit, held from green by one trust-hub Fail on the mermaid skill and Socket plus Snyk Warns on the network-facing skills.

This is Armin Ronacher's personal agent configuration, published rather than curated. The README's framing is unusually honest about that: these are commands he uses with agents, mostly Claude, tuned for his workflow and environment, and he tells you to expect to adjust paths, credentials and defaults before reusing them elsewhere.

That provenance is the reason to read this guide differently from the others in the catalog. It is not a product with a support commitment. It is the working setup of someone who has spent a long time building developer tools, and the value is in the specific choices rather than in completeness. Flask, Jinja and the Pallets libraries are his work, which is a reasonable prior that his defaults are worth understanding.

The package is broader than skills. It publishes to npm as `mitsupi` for the Pi Coding Agent, and its `package.json` exports four kinds of thing: extensions as Pi extensions, skills as agent skills, themes as Pi themes, and commands as prompt commands. The skills are the portable part, because they are markdown with helper scripts and most agent runtimes can load them. The extensions are TypeScript for a specific runtime and are worth reading for ideas rather than installing directly.

## Installation

The repository is a Pi package first. The README states the package is published to npm as `mitsupi`, so a global install is the natural distribution path:

```bash
npm install -g mitsupi
```

For an agent that loads skills from a directory, which is the relevant path for a Hermes profile, copy the skill folders and keep their names intact because the skills reference helper scripts by relative path:

```bash
git clone https://github.com/mitsuhiko/agent-stuff
cp -R agent-stuff/skills/* ~/.hermes/profiles/corpusiq/skills/
```

Copy selectively. Several of these skills assume macOS or a specific tool already installed, and the README's warning about adjusting paths applies most to `apple-mail`, `oebb-scotty`, `anachb` and `pi-share`. A skill whose helper script is missing does not degrade gracefully, it fails at the point of use.

Several skills carry their own external dependency rather than bundling it. `ghidra` needs a Ghidra installation for headless analysis. `openscad` needs OpenSCAD on the path. `summarize` runs `uvx markitdown`. `web-browser` drives Chrome or Chromium over the DevTools Protocol. `uv` is a set of conventions plus shell shims rather than a program. Read each `SKILL.md` before installing the family, and install the ones whose dependencies you already have.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| openscad | 1,122 | Creating and rendering OpenSCAD models, previewing angles, extracting parameters, validating syntax and exporting STL files |
| web-browser | 684 | Automating Chrome or Chromium through the Chrome DevTools Protocol |
| ghidra | 661 | Headless Ghidra analysis for binaries: functions, strings, symbols, call graphs and decompilation |
| github | 485 | Driving the `gh` CLI for issues, pull requests, runs and API queries |
| tmux | 393 | Remote-controlling tmux sessions for interactive CLIs by sending keystrokes and scraping pane output |
| summarize | 264 | Converting URLs or local documents to Markdown with `uvx markitdown`, optionally summarising them |
| commit | 248 | Writing concise git commits with good subjects and bodies |
| apple-mail | 248 | Searching and reading Apple Mail's local storage, including raw messages and attachment extraction |
| uv | 230 | Preferring `uv` for Python projects, scripts, dependencies and builds |

The remaining 12 indexed listings range from 13 to 167 installs and cover the rest: `librarian` for caching remote git checkouts, `frontend-design` for distinctive interface work, `sentry` for issue and event triage, `native-web-search`, `google-workspace` for Drive, Docs, Calendar, Gmail, Sheets and People through local helper scripts, `mermaid`, `update-changelog`, `pi-share`, `improve-skill`, and the two Austrian transit skills `oebb-scotty` and `anachb`.

Three of those listings have no directory in the current tree. `frontend-design`, `mermaid` and `improve-skill` are indexed with install counts but have no matching `skills/` folder, and the repository's `commands/` directory holds only `discuss.md`, so they were either removed or live somewhere that is not in the published tree. The guide lists them because the index does, and flags them so you do not go looking for a file that is not there.

## Why This Matters for Hermes Agents

The most transferable idea here is the `tmux` skill, and it is not about tmux. It describes remote-controlling an interactive CLI by sending keystrokes and scraping pane output, which is the pattern for driving any program that assumes a terminal and has no API. Every agent that has needed to run a REPL, a TUI installer or an interactive debugger has hit this problem, and the answer is a session that outlives a single command.

The `web-browser` skill is the other broadly useful one, and it is instructive for what it is not. It drives Chrome over the DevTools Protocol rather than through a scripting library, which means it works on whatever Chrome already has open rather than on a fresh headless instance. For sites with heavy client-side rendering or a login you have already performed, that distinction is the difference between working and not.

`ghidra` is the skill most agents would never write for themselves and most engineers would find hardest to write. Headless Ghidra analysis for functions, strings, symbols, call graphs and decompilation is a capability that turns binary questions into answerable ones, and it is a good example of a skill that is a tool wrapper with real domain knowledge in the wrapping.

The `openscad` skill shows how far a modelling loop can go in plain text. Creating and rendering models, previewing angles, extracting parameters, validating syntax and exporting STL means an agent can iterate on a physical object the way it iterates on code, with the model as the source and the render as the test.

The `intercepted-commands` directory is a small thing worth copying. It holds shell shims for `pip`, `pip3`, `poetry`, `python` and `python3` that exist to nudge an agent toward `uv`, which pairs with the `uv` skill. That is an environment-level intervention rather than an instruction, and it works on an agent that ignores instructions.

## Usage

| You say | What happens |
|---|---|
| "Model a phone stand in OpenSCAD and export an STL" | Writes the model, validates the syntax, renders a preview and exports the mesh |
| "Open this page in my browser and click through the checkout" | Drives the existing Chrome session over the DevTools Protocol rather than starting a fresh browser |
| "What functions are in this binary" | Runs headless Ghidra analysis and returns functions, strings and symbols |
| "Attach to my tmux session and run the tests" | Sends keystrokes into the session and scrapes the pane output back |
| "Turn this PDF into markdown and summarise it" | Runs the conversion through `uvx markitdown` and returns a summary of the result |
| "Write a commit message for these changes" | Reads the diff and produces a concise subject and body |
| "Find the invoice email from last month" | Searches the local Apple Mail store, including raw messages and attachments |

## Verification

The skills sit at `skills/<name>/SKILL.md`. This returns 200:

```bash
curl -fsSL https://raw.githubusercontent.com/mitsuhiko/agent-stuff/main/skills/openscad/SKILL.md | head -6
```

It should open with frontmatter and then the instruction body, followed by references to the helper scripts the skill expects. Because several skills depend on an external binary, verify the dependency before blaming the skill:

```bash
which openscad gh ghidra tmux uv
```

Anything missing from that list is a skill you should either install the dependency for or skip. The README is direct that these are tuned for the author's environment, so a missing tool is expected rather than an error.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-11) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| openscad | Pass | Pass | Pass |
| web-browser | Pass | Warn | Warn |
| ghidra | Pass | Pass | Pass |
| github | Pass | Pass | Warn |
| tmux | Pass | Pass | Pass |
| summarize | Pass | Pass | Warn |
| commit | Pass | Pass | Pass |
| apple-mail | Pass | Pass | Warn |
| uv | Pass | Pass | Pass |
| librarian | Warn | Pass | Warn |
| mermaid | Fail | Warn | Pass |
| frontend-design | Pass | Pass | Pass |

One Fail, on `mermaid` at the trust hub, which is also one of the three listings with no directory in the current tree, so the flagged artefact is not something you would install from this repository today. `librarian` carries a trust-hub Warn and a Snyk Warn, both plausible for a skill that clones remote repositories into a cache.

The skills that warrant the most thought are the ones with local access. `apple-mail` reads your mail store. `web-browser` drives an authenticated browser session, which means whatever you are logged into. `tmux` controls live sessions, and `ghidra` executes analysis tooling. Each is doing exactly what it says, and each is a capability you should grant deliberately rather than by installing the whole folder.

## Limitations

- Snapshot data, verified 2026-11-11: 5,538 combined installs across 21 indexed listings; 3,212 GitHub stars; Apache-2.0; last pushed 2026-09-27. Counts drift over time.
- Personal configuration, not a product. The README states it is tuned for the author's workflow and environment and that paths, credentials and defaults need adjusting before reuse.
- Three indexed listings have no directory in the current tree: `frontend-design`, `mermaid` and `improve-skill` carry install counts but no matching `skills/` folder.
- Several skills assume macOS. `apple-mail` reads a macOS mail store, and `oebb-scotty` and `anachb` are Austrian transit services, so the useful subset shrinks substantially on Linux.
- External binaries are not bundled. OpenSCAD, Ghidra, tmux, `gh`, Chrome and `uv` all have to be present, and the skill fails at the point of use when they are not.
- The extensions and themes are Pi-specific TypeScript and do not transfer to other runtimes. Only the skills are portable markdown.
- Last push is older than the other repositories in this sweep. Nothing suggests abandonment, but the maintenance cadence is not a promise.

## Related

- [Agent Browser - Vercel Labs CLI for AI Agents Setup](/hermes/skills/catalog/agent-browser-setup)
- [gh-stack - GitHub Stacked PRs Skill Setup](/hermes/skills/catalog/gh-stack-setup)
- [Browser-Use Automation - AI Browser for Anti-Bot Sites Setup](/hermes/skills/catalog/browser-use-automation-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the skills whose dependencies you already have. A family install where half the binaries are missing produces failures that look like skill bugs.
- Read `intercepted-commands` even on another runtime. The shim idea, making the environment push the agent toward the right tool, transfers to any stack.
- Prefer `web-browser` over a fresh headless browser for logged-in work. Attaching to an existing Chrome session is the shortest path past a login wall you have already cleared.
- Use `tmux` for anything interactive. If a tool expects a terminal prompt, a one-shot command will hang, and a session you can type into will not.
- Treat `apple-mail` and `web-browser` as privileged. They touch your mail and your authenticated sessions, so install them where that access is acceptable and not on a shared agent.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
