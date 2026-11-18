---
title: "Beagle Skills - Agent Skill Marketplace Setup"
description: "existential-birds/beagle: 20.1K combined installs across 96 indexed listings; framework-aware skills for code review, docs, testing, and analysis."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/beagle-setup/"
robots: "index,follow"
last_updated: "2026-11-18"
tags: ["hermes skill", "agent skill", "skill setup", "code review", "agent skills marketplace", "react"]
---

# Beagle Skills - Setup Guide

**Source:** [existential-birds/beagle](https://www.skills.sh/existential-birds/beagle) via skills.sh - 20.1K combined installs across 96 indexed listings; first seen Nov 18, 2026 (this sweep)
**GitHub:** 88 stars, Apache-2.0 license, `main` branch, last pushed 2026-09-15. Skills live in `plugins/<area>/skills/<name>/SKILL.md`, one directory per skill across eleven plugin areas for Python, Go, Rust, Elixir, React, Remix, iOS/Swift, docs, analysis, and testing.
**Category:** Framework-aware agent skill marketplace
**Quality Tier:** 🟡 Yellow - 59 Pass and 1 Warn across the 60 sampled verdict cells; Apache-2.0 licence.

Beagle is an Agent Skills marketplace: framework-aware code review, documentation, testing, architectural analysis, and git workflows for any compatible coding agent. Install with `npx skills add existential-birds/beagle`, then your agent loads the right skill automatically or you run one by name. Skills cover Python, Go, Rust, Elixir, React, Remix v2, and iOS/Swift.

## Installation

The README installs via the skills CLI for any coding agent, with a separate Claude Code marketplace route:

```bash
npx skills add existential-birds/beagle
```

Claude Code users add the repository as a plugin marketplace and install the core plugin:

```bash
claude plugin marketplace add https://github.com/existential-birds/beagle
claude plugin install beagle-core@existential-birds
```

Install additional plugins as needed (for example `beagle-python@existential-birds`). The only prerequisite is a coding agent that supports Agent Skills; the `agent-browser` tool is optional and only needed by the `run-test-plan` skill.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| react-flow | 1,348 | Build React Flow (@xyflow/react) workflow visualizations with custom nodes, edges, and viewport control. |
| python-code-review | 950 | Review Python code for type safety, async patterns, error handling, and common mistakes. |
| langgraph-code-review | 888 | Review LangGraph code for bugs and anti-patterns in state management, graph structure, and async patterns. |
| tailwind-v4 | 826 | Set up Tailwind CSS v4 with CSS-first configuration, theme variables, OKLCH colors, and dark mode. |
| react-flow-advanced | 650 | Implement advanced React Flow patterns such as sub-flows, custom connection lines, programmatic layouts, drag-and-drop, and undo/redo. |
| react-router-v7 | 580 | Apply React Router v7 patterns for data-driven routing with loaders, actions, fetchers, and navigation guards. |
| react-flow-architecture | 542 | Make architectural decisions for node-based UIs, covering state management and integration patterns for React Flow. |
| vitest-testing | 473 | Write Vitest unit and integration tests with mocking, snapshots, and test coverage configuration. |
| docling | 431 | Listed in the install index but absent from the repository tree; behaviour not verified. |
| fastapi-code-review | 391 | Review FastAPI code for routing patterns, dependency injection, validation, and async handlers. |
| react-flow-implementation | 380 | Implement React Flow node-based UIs with nodes, edges, handles, custom components, and viewport control. |

The remaining 85 indexed listings range from 75 to 358 installs.

## Why This Matters for Hermes Agents

The core value is framework-aware auto-loading: the agent pulls only the skills that match the stack it is working in, so a Python session gets the Python and FastAPI review skills while a React session gets the React Flow and React Router skills. Review skills such as `langgraph-code-review` open with a gate that requires quoting the exact code under review before flagging a finding, which keeps review output grounded. Documentation skills follow the Diataxis framework, and testing separates plan generation from execution.

## Usage

| You say | What happens |
|---|---|
| "Review this Python file" | Loads python-code-review to check type safety, async patterns, error handling, and common mistakes. |
| "Add a custom node to this React Flow graph" | Loads react-flow and react-flow-implementation for nodes, edges, handles, and custom components. |
| "Migrate my routes to React Router v7" | Applies react-router-v7 patterns for loaders, actions, fetchers, and protected routes. |
| "Set up Tailwind v4 with dark mode" | Loads tailwind-v4 for CSS-first configuration, design tokens, and dark mode. |
| "Review this FastAPI app" | Loads fastapi-code-review for routing, dependency injection, validation, and async handlers. |
| "Sketch the architecture for a node-based editor" | Loads react-flow-architecture to weigh state management and integration options. |

## Verification

Probe one skill on the `main` branch before installing. It returns 200:

```bash
curl -fsSL https://raw.githubusercontent.com/existential-birds/beagle/main/plugins/beagle-react/skills/react-flow/SKILL.md | head -12
```

Then install and confirm the agent can load a skill by name:

```bash
npx skills add existential-birds/beagle
```

## Security

skills.sh verdicts for sampled skills (verified Nov 18, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| react-flow | Pass | Pass | Pass |
| python-code-review | Pass | Pass | Pass |
| langgraph-code-review | Pass | Pass | Pass |
| tailwind-v4 | Pass | Pass | Pass |
| react-flow-advanced | Pass | Pass | Pass |
| react-router-v7 | Pass | Pass | Pass |
| react-flow-architecture | Pass | Pass | Pass |
| vitest-testing | Pass | Pass | Pass |
| docling | Pass | Pass | Warn |
| fastapi-code-review | Pass | Pass | Pass |
| react-flow-implementation | Pass | Pass | Pass |
| shadcn-ui | Pass | Pass | Pass |
| react-flow-code-review | Pass | Pass | Pass |
| langgraph-architecture | Pass | Pass | Pass |
| swiftui-code-review | Pass | Pass | Pass |
| tutorial-docs | Pass | Pass | Pass |
| bubbletea-code-review | Pass | Pass | Pass |
| zustand-state | Pass | Pass | Pass |
| dagre-react-flow | Pass | Pass | Pass |
| adr-writing | Pass | Pass | Pass |

The sample covers 20 of the 96 indexed listings; the single Warn is Snyk on `docling`, and there is no Fail.

## Limitations

- Snapshot data, verified Nov 18, 2026: 20,079 combined installs across 96 indexed listings; 88 GitHub stars; Apache-2.0; last pushed 2026-09-15. Counts drift over time.
- The `docling` listing (431 installs) appears in the install index but has no directory in the repository tree, so its behaviour is not documented here.
- The 11 skills above carry most of the install volume; the other 85 indexed listings sit between 75 and 358 installs and are long-tail.
- The security sample covers 20 of the 96 indexed listings; the remaining 76 have not been re-checked here.
- Auto-loading spreads installs across many single-framework skills rather than one monolithic suite, so a single skill rarely dominates the total.

## Related

- [CodeStable Skills - AI Coding Workflow Setup](/hermes/skills/catalog/codestable-skills-setup)
- [Claude Code Skills - Agentic Coding & Skill Development Setup](/hermes/skills/catalog/claude-code-skills-setup)
- [OpenAI Codex Skills - Official Skills Catalog Setup](/hermes/skills/catalog/openai-codex-skills-setup)
- [Skill Vetter - Security Audit for Hermes Skills Setup](/hermes/skills/catalog/skill-vetter-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install with `npx skills add existential-birds/beagle` first; the agent then auto-loads only the skills matching the current stack.
- Ask for `react-flow` or `react-router-v7` by name when you want a specific framework skill rather than waiting for auto-load.
- For Claude Code, install `beagle-core` first, then add area plugins such as `beagle-python` or `beagle-react` as needed.
- Read a review skill's gate rules before trusting its output; the review skills require quoting the exact artifact before flagging a finding.
- Probe a skill's SKILL.md on the `main` branch with curl before wiring it into an automated workflow.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
