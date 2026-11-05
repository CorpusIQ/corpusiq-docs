---
title: "Qt Agent Skills - QML, C++ and Figma Setup"
description: "theqtcompanyrnd/agent-skills on skills.sh: 9.9K combined installs across 14 listings; Qt QML, C++ and CMake review, docs, tests and UI design skills."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/qt-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-05"
tags: ["hermes skill", "agent skill", "skill setup", "qt", "qml", "cpp"]
---

# Qt Agent Skills - Setup Guide

**Source:** [theqtcompanyrnd/agent-skills](https://www.skills.sh/theqtcompanyrnd/agent-skills) via skills.sh - 9.9K combined installs across 14 indexed listings; first seen 2026-11-05 (Nov 5, 2026 morning sweep)
**GitHub:** 523 stars, licence field NOASSERTION (the README's licence section states BSD-3-Clause), last pushed 2026-10-20, 13 SKILL.md directories under skills/
**Category:** Official Qt development suite: QML and C++ review, documentation generation, profiling, testing, CMake projects and Figma design handoff
**Quality Tier:** 🟡 Beta - licence field NOASSERTION; every sampled audit Pass; 523 stars.

Qt ships this repository as its official agentic skill set for Qt software development and quality assurance, built for Claude Code, Codex CLI and GitHub Copilot and tested with frontier models from the Claude, Gemini and GPT families. Thirteen skills are grouped into four working types: Review skills that combine a deterministic linter with deep analysis, Process skills for docs and tests, Conceptual skills that correct known model biases around QML, CMake and the C++/QML boundary, and Tool skills that drive `qmlprofiler` and `qmltestrunner`.

Two MCP servers ship alongside the skills: `qt-documentation-mcp`, a hosted server for Qt API docs across the latest release and active LTS branches, and `qml-live-preview-mcp`, a local server that live-previews QML edits without a rebuild. The README also carries Qt's own warning that the skills use AI and can make mistakes, and that commercial Qt licensing use falls under the Qt AI Services terms.

## Installation

Claude Code installs the whole set as one plugin:

```text
/plugin marketplace add TheQtCompanyRnD/agent-skills
/plugin install qt-development-skills
```

Codex CLI uses Vercel's cross-platform installer:

```bash
npx skills add TheQtCompanyRnD/agent-skills
```

GitHub Copilot CLI reads the same SKILL.md directory format and can install a single skill with GitHub CLI:

```bash
gh skill install TheQtCompanyRnD/agent-skills qt-qml-review
```

Gemini CLI installs the repository as an extension:

```bash
gemini extensions install https://github.com/TheQtCompanyRnD/agent-skills
```

Manual installs are a copy or symlink into the tool's discovery path, for example `~/.claude/skills/`, `~/.codex/skills/`, `~/.copilot/skills/` or a project's `.github/skills/`. A skill-only copy of the two review skills does not include `agents/`, so copy `agents/cpp-review-agent.md` and `agents/qml-review-agent.md` into `~/.claude/agents/` as well if you want the deep-analysis pass.

## What It Provides

Eleven listings clear the 489-install threshold.

| Skill | Installs | Use For |
|---|---|---|
| qt-ui-design | 1,174 | Designing or auditing Qt/QML, web and embedded UI: screen layout, navigation and UX review with platform-aware geometry, input and locale defaults |
| qt-qml | 1,165 | Writing, reviewing, fixing or refactoring QML, correcting systematic model biases around bindings, scoping, modules, JS interop and types |
| qt-cpp-review | 1,076 | Reviewing Qt6 C++: 60+ deterministic lint rules, then deep analysis of model contracts, ownership, threading, API correctness and performance |
| qt-qml-review | 969 | Reviewing Qt6 QML: 48+ lint rules, then deep analysis of bindings, layout, loaders, delegates, states and performance |
| qt-cpp-docs | 841 | Generating Markdown reference docs for Qt/C++ classes, modules, headers, utilities and entry points such as main.cpp |
| qt-qml-docs | 775 | Generating Markdown API reference docs for QML components, modules and whole Qt Quick applications |
| qt-qml-profiler | 762 | Running qmlprofiler on a Qt Quick app, parsing the .qtd trace and analyzing hotspots with frame-time, memory and pixmap-cache summaries |
| qt-qml-test | 662 | Generating Qt Quick Test cases with TestCase, SignalSpy and tryCompare for single QML files or batches |
| qt-qml-test-run | 627 | Building and running qmltestrunner tests for a CMake project, parsing JUnit XML and writing a Markdown report |
| qt-cmake-project | 597 | Setting up Qt 6 CMake projects: executables, libraries, QML modules, plugins, folder layout and static resources |
| qt-figma-token-extraction | 489 | Extracting Figma tokens, text styles and variables into design-tokens.json plus ready-to-use QML singletons |

The remaining 3 indexed listings range from 89 to 487 installs: qt-figma-component-generation (487), qt-canvas2d (158) and qt-project (89).

## Why This Matters for Hermes Agents

Most language models have never written a large body of Qt code, and it shows: they emit `qmake` era build files, treat QML bindings like React state, and confuse Qt Quick `Canvas` with the HTML5 element. This suite exists specifically to correct those pre-training biases rather than to teach Qt from scratch, which is exactly the gap an agentic coding harness hits on day one.

The review skills are the strongest half. They run a deterministic linter first and only then spend model tokens on analysis, and they shard the deep pass above roughly 2,500 lines of C++ or 1,500 lines of QML, so a review of a large repository does not collapse into a shallow skim.

The documentation skills are useful in the opposite direction: they turn existing `.h`, `.cpp` and `.qml` files into Markdown reference material, which gives an agent that is new to a codebase something better than grep.

Pairing the Figma token extraction with component generation gives a design-to-QML path, though generation depends on tokens produced by the extraction skill, so the order matters.

## Usage

| You say | What happens |
|---|---|
| "Review this QML file before I commit" | qt-qml-review lints with 48+ rules and reports findings on bindings, layout and performance |
| "Audit the C++ backend of this Qt Quick app" | qt-cpp-review lints with 60+ rules and runs deep analysis across ownership, threading and API correctness |
| "The list view stutters when scrolling" | qt-qml-profiler runs qmlprofiler, parses the trace and points at hotspots with frame-time summaries |
| "Write tests for this delegate component" | qt-qml-test generates TestCase, SignalSpy and tryCompare cases for the component |
| "Set up a fresh Qt 6 CMake project with a QML module" | qt-cmake-project produces the folder layout, targets and resources without qmake-isms |
| "Document these six widgets classes" | qt-cpp-docs generates Markdown reference pages for each class and header |
| "Pull our Figma tokens into QML" | qt-figma-token-extraction writes design-tokens.json and QML singletons from the design system |

## Verification

Fetch one skill file to see the frontmatter and body before installing:

```bash
curl -fsSL https://raw.githubusercontent.com/theqtcompanyrnd/agent-skills/main/skills/qt-qml/SKILL.md | head -8
```

It should open with `name: qt-qml` and a description naming QML best practices. After an install, confirm the skill directories landed:

```bash
ls ~/.claude/skills | grep qt-
```

The Codex and Copilot paths are `~/.codex/skills/` and `~/.copilot/skills/` respectively. Copilot CLI reports what actually loaded with `/skills list`, and Claude Code auto-discovers skills without a restart.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-05) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| qt-ui-design | Pass | Pass | Pass |
| qt-qml | Pass | Pass | Pass |
| qt-qml-test | Pass | Pass | Pass |
| qt-project | Pass | Pass | Pass |

## Limitations

- Snapshot data, verified 2026-11-05: 9,871 combined installs across 14 indexed listings; 523 GitHub stars; licence field NOASSERTION; last pushed 2026-10-20. Counts drift over time.
- The install index outruns the tree: 14 listings against 13 skill directories, and `qt-project` (89 installs) has no matching directory under `skills/`.
- GitHub reports the licence as NOASSERTION while the README's licence section states BSD-3-Clause. Treat the metadata field as unresolved rather than as a permissive declaration.
- The review skills are strongest inside Claude Code, where the plugin also installs `agents/`. Copilot loads only the static guidance, and Cursor or Windsurf need the condensed `platforms/` variants with no linter or subagents.
- `qt-qml-profiler` covers 2D QML and Qt Quick only, not Qt Quick 3D, and `qt-qml-test` deliberately leaves CMake and runner setup to `qt-qml-test-run`.
- Commercial use under a Qt licence is governed by the Qt AI Services terms, which the README asks you to accept before using the skills or the MCP tools.

## Related

- [Extract Design System - UI Token & Component Extraction Setup](/hermes/skills/catalog/extract-design-system-setup)
- [Uizze UI Skills - Anti-UI-Slop Design Quality Setup](/hermes/skills/catalog/uizze-ui-skills-setup)
- [Claude Code Skills - Agentic Coding & Skill Development Setup](/hermes/skills/catalog/claude-code-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the plugin rather than the individual skill directories when you want the review skills at full strength: the plugin is what places the review agents in `~/.claude/agents/`.
- Run the linter pass before the analysis pass. The review skills already do this, so do not ask for a "deep review" on a 20,000-line module and expect one pass to cover it.
- Use `qt-qml` as a standing rule for QML work rather than a one-off: its values are bias corrections that pay off on every later file.
- Chain the Figma skills in order, tokens first then components. Component generation expects the token output.
- Keep `qt-qml-test` and `qt-qml-test-run` as a pair: the first writes cases, the second builds and runs them and writes the Markdown report.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
