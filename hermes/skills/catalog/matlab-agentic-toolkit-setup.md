---
title: "MATLAB Agentic Toolkit - Engineering Agent Skills Setup"
description: "MathWorks' MATLAB toolkit: 6.8K combined installs across 96 listings, 158 engineer skills that drive a MATLAB MCP server instead of guessing"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/matlab-agentic-toolkit-setup/"
robots: "index,follow"
last_updated: "2026-11-11"
tags: ["hermes skill", "agent skill", "skill setup", "matlab", "engineering", "mcp server", "scientific computing"]
---

# MATLAB Agentic Toolkit - Setup Guide

**Source:** [matlab/matlab-agentic-toolkit](https://www.skills.sh/matlab/matlab-agentic-toolkit) via skills.sh - 6.8K combined installs across 96 indexed listings (6,814 exact, API row cap reached); first seen 2026-11-11 (Nov 11, 2026 sweep)
**GitHub:** 1,290 stars, MathWorks license (GitHub reports NOASSERTION), `main` branch, last pushed 2026-11-09, 158 `SKILL.md` files under `skills-catalog/<group>/<skill>/`
**Category:** Engineering and scientific computing: MATLAB code generation, debugging, testing, app building, and toolbox-specific workflows
**Quality Tier:** 🟡 Mixed - a first-party MathWorks toolkit with a large curated catalog and clean provenance, held back from green by three flagged verdicts across twelve sampled skills and a license that is not a standard OSI one.

This is MathWorks' own attempt at the problem every engineering team hits with coding agents: the agent writes MATLAB that looks right and is not. The README states the target precisely, saying the toolkit can prevent an agent from hallucinating toolbox functions, missing new features, and wasting time on steps an experienced MATLAB user would skip. That framing is the useful one, because a numeric engineer already knows what good MATLAB looks like and mostly wants the agent to stop improvising.

The architecture is two things in one repository. The first is the MATLAB MCP Server, installed automatically, which gives the agent live tools: run code and return command window output, run a program file, run tests through `runtests` with structured results, run the Code Analyzer, and list the installed MATLAB version and toolboxes. The second is the skill catalog, 158 skills in the current tree, grouped by product area and read only when relevant.

The grouping is what makes 158 skills manageable. Six MATLAB groups cover core code work, app building, data import and analysis, external language interfaces, programming, and software development. Then each toolbox gets its own group, and the README's list runs across aerospace, AI and statistics, automotive and further product areas. The README explicitly recommends installing only the groups relevant to your work, on the grounds that agents trigger skills more reliably when fewer are loaded.

## Installation

MathWorks ships an installer rather than a plugin marketplace entry. The README's command line path covers Claude Code, GitHub Copilot CLI and OpenAI Codex users, and sets up this toolkit, the Simulink Agentic Toolkit and the MATLAB MCP Server together through a separate repository:

```bash
# follow github.com/matlab/agentic-toolkit-installer
```

The in-MATLAB path is the one most MATLAB users will take. Download the installer package, open it with MATLAB to install the add-on, then run the setup function in the MATLAB command window:

```matlab
setupAgenticToolkit("install")
```

By default the agent starts a new MATLAB session each time it is called. To attach it to the session you already have open, and to keep variables and figures in place, run this in the MATLAB command window:

```matlab
shareMATLABSession()
```

The README notes that when several MATLAB sessions are open, the agent connects to whichever one ran that command most recently, and that adding the line to your MATLAB startup script makes the attach automatic. The README also points at `Configuration_and_Troubleshooting.md` for offline installs, local files, manual setup, platform-specific notes and an add-skills-only path when the MCP server is already configured.

The supported agent list in the README is Claude Code, GitHub Copilot, OpenAI Codex, Gemini CLI and Amp, with automatic configuration for those and a manual route documented for anything else. MATLAB R2021a or later is the stated requirement. A Simulink Agentic Toolkit exists as a separate repository for Simulink work.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| matlab-review-code | 179 | Reviewing MATLAB code for correctness, conventions and quality issues |
| matlab-analyze-data | 143 | Importing, filtering, aggregating and analyzing data with tables, timetables and time-series operations |
| matlab-design-digital-filter | 125 | Designing digital filters with the signal processing toolchain |
| matlab-modernize-code | 122 | Modernizing legacy MATLAB code toward current syntax and idioms |
| matlab-agentic-toolkit-setup | 121 | Setting up and configuring the toolkit itself |
| matlab-debugging | 117 | Diagnosing and fixing MATLAB errors and unexpected behaviour |
| matlab-create-live-script | 113 | Authoring Live Scripts in the documented plain text format |
| matlab-build-app | 113 | Building MATLAB apps programmatically with UI components, layouts, callbacks and web integration |
| matlab-list-products | 111 | Listing installed MATLAB products and toolboxes |
| matlab-add-awgn | 106 | Adding additive white Gaussian noise for signal and communications modelling |

The remaining 86 indexed listings range from 46 to 99 installs and cover the toolbox-specific skills, from serial link modelling and 5G waveform generation through PCB filter design, GNSS position computation, DuckDB access and performance test authoring.

The tree is larger than the index: 158 `SKILL.md` files exist in the current repository against 96 indexed listings, and 96 is also the API row cap, so treat both published figures as floors rather than totals. The catalog directory structure is `skills-catalog/<group>/<skill>/SKILL.md`, which is also the path you can read before installing anything.

Two rows above do not resolve to a directory of the same name in the current tree, which is index drift rather than a missing skill. `matlab-debugging` is named `matlab-debug-code` in the tree, and `matlab-agentic-toolkit-setup` has no matching catalog directory, since setup is handled by the installer. Seven further indexed listings have no same-named directory, including `matlab-testing`, `matlab-write-database`, `matlab-read-database` and the two SimBiology skills, so search by description when a name lookup fails.

## Why This Matters for Hermes Agents

Model recall of MATLAB is worse than model recall of Python, and the gap is specific. Toolbox function signatures are numerous, version-dependent and documented behind a paywall, so an agent working from memory produces calls that look plausible and fail on the version you actually run. The MCP server closes that gap by executing against the installed MATLAB and reading back real output, which turns a guess into a test.

The task-versus-tool table in the README is the cleanest articulation of the pattern. Running code, running a file, running tests, static analysis and toolbox detection are all mapped to named server tools rather than left to improvisation. When an agent has `check_matlab_code` available it does not have to reason about whether the syntax is valid.

The two MCP resources matter more than they look. `matlab_coding_guidelines` and `plain_text_live_code_guidelines` are reference documents the agent can read on demand, which is how a style standard gets applied without being pasted into every prompt. If your team has its own MATLAB conventions, that is the hook to extend.

The install guidance to only load the groups you need is a real constraint rather than a preference. The README says agents trigger skills more reliably when fewer are loaded, which matches what happens in practice: skill selection degrades as the candidate list grows, so a controls engineer loading the aerospace and automotive groups is buying misfires.

Finally, the toolbox-per-group structure is a template worth copying. Most skill collections in other domains are flat lists, and a flat list of 158 items is unusable. Here the skill name carries the product, so a review of a signal processing task loads signal processing skills and nothing else.

## Usage

| You say | What happens |
|---|---|
| "What version of MATLAB is running, and which toolboxes are installed" | Calls the toolbox detection tool and returns the real installed set instead of describing a generic MATLAB |
| "Review this function for problems" | Runs the Code Analyzer through the MCP server and reports actual diagnostics rather than stylised guesses |
| "Write tests for this function and run them" | Authors tests in the house style and runs them through `runtests`, returning structured pass and fail results |
| "Modernize this legacy script" | Applies the modernization skill to move old idioms to current syntax, then checks the result compiles |
| "Design a lowpass filter at 2 kHz and plot the response" | Loads the digital filter design skill and executes the design in the live MATLAB session |
| "Build a small app with a dropdown and a plot area" | Uses the app building group for UI components, layouts, callbacks and the plotting callback wiring |
| "Port this Python routine to MATLAB" | Applies the external language interface guidance, including the Python interop path and MEX considerations |

## Verification

Read a skill before installing to see what the agent will actually be told. The catalog path is `skills-catalog/<group>/<skill>/SKILL.md`, and this returns 200:

```bash
curl -fsSL https://raw.githubusercontent.com/matlab/matlab-agentic-toolkit/main/skills-catalog/matlab-core/matlab-review-code/SKILL.md | head -6
```

The README's own verification step is a live round trip rather than a file check, and it is the one that matters because it proves the MCP server reaches a real MATLAB:

```text
What version of MATLAB is running? List the installed toolboxes.
```

A correct answer names a specific release and a specific toolbox list. A generic answer, or a refusal, means the server is not connected and the agent is working from memory. To check the attachment to your open session, confirm `shareMATLABSession()` has been run in the session you care about, then ask the agent to read a variable that exists only there.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-11) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| matlab-review-code | Pass | Pass | Pass |
| matlab-analyze-data | Pass | Pass | Pass |
| matlab-design-digital-filter | Pass | Pass | Pass |
| matlab-modernize-code | Pass | Pass | Pass |
| matlab-agentic-toolkit-setup | Pass | Pass | Warn |
| matlab-debugging | Pass | Pass | Fail |
| matlab-create-live-script | Warn | Pass | Pass |
| matlab-build-app | Pass | Pass | Pass |
| matlab-list-products | Pass | Pass | Pass |
| matlab-add-awgn | Pass | Pass | Pass |
| matlab-install-products | Pass | Pass | Fail |

Two Snyk Fails in the sample, on `matlab-debugging` and `matlab-install-products`, plus one trust-hub Warn on `matlab-create-live-script`. The pattern suggests the flags cluster on skills that touch the environment rather than on content generation, but that is an observation from the sample and not a guarantee about the rest of the 158.

The bigger consideration is what the MCP server can do. It executes MATLAB code, which is arbitrary code execution by design and in your own interpreter. That is exactly the capability that makes the toolkit useful and exactly the capability to scope: run it in a MATLAB session you are willing to see modified, keep the working directory where you intend the agent to write, and do not attach it to a session holding production data.

The license also constrains deployment. The README's licensing section states that MCP servers are only permitted for use with MATLAB under the MathWorks Software License Agreement and must not be shared by multiple users, so a shared multi-user agent endpoint pointed at one MATLAB licence is out of bounds.

## Limitations

- Snapshot data, verified 2026-11-11: 6,814 combined installs across 96 indexed listings; 1,290 GitHub stars; MathWorks license reported as NOASSERTION; last pushed 2026-11-09. Counts drift over time.
- Both published figures are floors. The skills.sh API returns at most 96 rows per query and that cap was reached, while the repository carries 158 `SKILL.md` files, so the real install total is higher than 6,814 and the real listing count higher than 96.
- A MATLAB installation and licence are hard requirements. Nothing in the toolkit substitutes for the interpreter, and the skill files alone give an agent documentation without the ability to run anything.
- The MCP server may not be shared across users per the MathWorks licence, which rules out a single shared agent backend serving a team.
- Toolbox coverage follows the licence you own. A skill for a toolbox you have not installed produces advice the interpreter cannot execute.
- Skill triggering is description-based. The README recommends installing only relevant groups and notes that a skill can still be invoked by name, for example `/matlab-write-tests` in Claude Code, so name the task rather than assuming the right skill loads.
- The Simulink path is a separate repository with a separate installer, so a modelling workflow that spans both products needs both setups.

## Related

- [EvoSkills - Scientific Research Skill Packs Setup](/hermes/skills/catalog/evoskills-setup)
- [Text to CAD Skills - 3D Model and URDF Setup](/hermes/skills/catalog/text-to-cad-skills-setup)
- [Frames Engineering Skills - Agent Tools Setup](/hermes/skills/catalog/frames-engineering-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install narrow, not complete. The README's own advice is to load only the groups relevant to the work, and a smaller candidate set is what makes automatic triggering dependable.
- Run `shareMATLABSession()` before a long session if you want to keep variables, figures and workspace state. Without it the agent gets a fresh interpreter each call and your context disappears between turns.
- Ask for the toolbox check early. One question about installed toolboxes tells you whether the agent is grounded before you spend a turn chasing a wrong function signature.
- Use the Code Analyzer as a gate rather than as a suggestion. Having the agent run static analysis after every generated function catches the hallucinated-call class before it reaches a test run.
- Keep the working directory deliberate. The server executes whatever it is asked to execute in the session it is attached to, so start the agent from the project folder you want written to.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
