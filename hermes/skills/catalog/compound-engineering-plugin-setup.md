---
title: "Compound Engineering Plugin - Every Inc Workflow Suite Setup"
description: "Setup guide for everyinc/compound-engineering-plugin - 124.2K combined installs. Every Inc's compound engineering workflow suite for coding agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/compound-engineering-plugin-setup/"
robots: "index,follow"
last_updated: "2026-10-10"
tags: ["hermes skill", "agent skill", "skill setup", "agent engineering", "development workflow", "code review"]
---

# Compound Engineering Plugin - Setup Guide

**Source:** [everyinc/compound-engineering-plugin](https://www.skills.sh/everyinc/compound-engineering-plugin) via skills.sh - 124.2K combined installs across 96 indexed listings; first seen Oct 9, 2026 (extended-query probe)
**GitHub:** [everyinc/compound-engineering-plugin](https://github.com/everyinc/compound-engineering-plugin) (25,450 stars, MIT; pushed 2026-10-10; repo layout: one skills/<name>/SKILL.md per skill)
**Category:** Agent Engineering / Development Workflow
**Quality Tier:** 🟢 Production - 25,450-star MIT repo (Every Inc), CI-tested, pushed Oct 10, 2026; mixed sampled verdicts (Pass/Warn) - see Security

Compound Engineering is the official plugin from Every Inc (every.to), the company behind the Chain of Thought blog. It packages 36 skills for AI coding agents into one workflow loop: brainstorm the requirements, plan the implementation, work the plan, simplify the result, review it, then compound the session by writing down what was learned. The plugin runs on 14 agent hosts, including Claude Code, Cursor, and Codex, and is maintained by Kieran Klaassen and Trevin Chow with community contributions.

The skills are grouped by purpose: the six-step core loop, anchors that keep it grounded (ce-strategy, ce-product-pulse, ce-sweep, ce-compound-refresh), on-demand helpers such as ce-debug and ce-explain, a git workflow set, the autonomous lfg pipeline, testing and design skills, collaboration skills, and utilities. After installing, run /ce-setup in any project and then either drive the loop by hand or hand a feature over to /lfg.

---

## Installation

Compound Engineering installs through each host's plugin marketplace. The repository root is the plugin package (plugin.json plus the skills/ directory).

### Claude Code

```text
/plugin marketplace add EveryInc/compound-engineering-plugin
/plugin install compound-engineering
```

### Cursor

In Cursor Agent chat:

```text
/add-plugin compound-engineering
```

### Codex CLI

```bash
codex plugin marketplace add EveryInc/compound-engineering-plugin
codex plugin add compound-engineering@compound-engineering-plugin
```

The plugin supports 14 agent hosts in total. The README also documents installs for Kimi Code CLI, Cline, Grok Build CLI, Devin CLI, GitHub Copilot, Factory Droid, Qwen Code, OpenCode, Pi, oh-my-pi (omp), and Antigravity CLI. If you are upgrading an existing pre-native install, refresh the cached marketplace before updating.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| ce-brainstorm | 3,794 | Interactive Q&A that turns a rough feature idea into a requirements-only plan |
| ce-plan | 3,617 | Enrich a feature idea or requirements doc into an implementation-ready plan |
| ce-code-review | 3,572 | Report-only multi-agent review of a branch against the plan before merge |
| ce-compound | 3,543 | Capture what was learned into docs/solutions/ so the next loop starts smarter |
| ce-doc-review | 3,492 | Review documentation with the same rigor as code review |
| ce-work | 3,469 | Execute an implementation-ready plan step by step |
| lfg | 3,408 | Run the whole pipeline hands-off: work, simplify, review, commit, push, PR |
| ce-debug | 3,381 | Start from a bug report and build the fix path |
| ce-commit | 3,279 | Commit completed work with consistent messages |
| ce-simplify-code | 3,271 | Refine freshly written code for clarity and reuse before review |
| ce-ideate | 3,256 | Generate and pressure-test ideas when the direction is still unclear |
| ce-compound-refresh | 3,254 | Keep captured learnings current as the codebase evolves |
| ce-setup | 3,243 | First-run project setup: tool capabilities, config file, gitignore |
| ce-commit-push-pr | 3,241 | Commit, push, and open a pull request in one flow |
| ce-optimize | 3,190 | On-demand optimization pass for code that needs to improve |
| ce-resolve-pr-feedback | 3,132 | Work through PR review feedback until the threads are resolved |
| ce-worktree | 2,997 | Manage git worktrees for parallel work streams |
| ce-test-browser | 2,962 | Exercise the built result in a browser |
| ce-proof | 2,950 | Produce shareable proof of what was built and verified |
| ce-strategy | 2,928 | Set the strategic anchor the loop works against |
| ce-test-xcode | 2,880 | Run Xcode-side tests for Apple platform builds |
| ce-product-pulse | 2,858 | Feed product health signals into planning |
| ce-riffrec-feedback-analysis | 2,756 | Analyze recorded feedback sessions for durable insights |

The remaining 73 indexed listings range from 164 to 2,494 installs.

## Why This Matters for Hermes Agents

Compound Engineering speaks the same language as Hermes agents: every skill is a plain SKILL.md file with instructions and assets, so an agent can read the workflow directly and follow it step by step. The loop it enforces (brainstorm, plan, work, simplify, review, compound) maps cleanly onto how agentic coding already works, but adds the step most pipelines miss: writing what was learned back into the repository. Because ce-compound stores learnings in docs/solutions/ and later runs read them as grounding, a second task on the same codebase starts with the first task's context already loaded instead of at zero. The plugin is CI-tested and maintained by a team that runs the workflow on its own product, so the patterns are a working base layer rather than a demo. For builders running agents across many repositories, every artifact is a plain file under docs/, which makes the output reviewable, versionable, and portable across hosts.

## Usage

| You say | What happens |
|---|---|
| "Brainstorm a safer background job retry design" | ce-brainstorm runs interactive Q&A and writes a requirements-only plan first. |
| "Turn that into an implementation plan" | ce-plan enriches the requirements into an implementation-ready plan artifact. |
| "I want this shipped, not just planned" | lfg works the plan end to end: simplify, review, capture learnings, commit, then push and open a PR when a git remote exists. |
| "Fix the bug users reported yesterday" | ce-debug starts from the bug report and builds the fix path. |
| "Review this branch before I merge" | ce-code-review runs a report-only multi-agent review against the plan. |
| "Stop relearning the same lesson" | ce-compound writes the learning into docs/solutions/ for future runs to read. |
| "Get this committed and into a PR" | ce-commit-push-pr handles the commit, push, and PR steps in one flow. |

## Verification

Start a new host session after installing so the plugin loads; the ce- skills and /lfg should appear as slash commands. In Claude Code, /plugin opens the plugin manager where you can confirm the plugin is installed and inspect its skills.

Preview the skills from the repository without installing anything:

```bash
npx skills add everyinc/compound-engineering-plugin --list
```

Review a raw SKILL.md before installing (this URL returned 200 when checked on Oct 10, 2026):

```bash
curl -sL https://raw.githubusercontent.com/everyinc/compound-engineering-plugin/main/skills/ce-brainstorm/SKILL.md
```

## Security

skills.sh verdicts for sampled skills (verified Oct 10, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| ce-brainstorm | Pass | Warn | Warn |
| ce-plan | Pass | Warn | Pass |
| ce-code-review | Pass | Pass | Pass |

## Limitations

- License is MIT, but release versions and marketplace manifests are owned by release automation; community PRs do not hand-bump versions.
- The README badge lists 36 skills while skills.sh indexes 96 listings; the extra listings include both variant names (ce:compound and similar forms) and beta-named skills, and 96 is the skills.sh API page cap, so more listings may exist.
- Beta-named skills (ce-work-beta, ce-polish-beta, ce-dogfood-beta) signal preview status; prefer stable names for production work.
- Sampled verdicts are mixed: ce-brainstorm shows Socket and Snyk Warn, and ce-plan shows Socket Warn; review the Security section and the skills.sh pages before production use.
- Behavior differs slightly by host: Codex invokes skills with $skill-name, and the Devin integration maps some Claude-style allowed-tools names differently.


- Snapshot data, verified Oct 10, 2026: 124,214 combined installs across 96 indexed listings; 25,450 GitHub stars; MIT; last pushed 2026-10-10. Counts drift over time.

## Related

- [LangChain Agent Skills - Memory, RAG, Persistence & Middleware Setup](/hermes/skills/catalog/langchain-skills-setup) - persistent memory patterns that complement Compound Engineering's docs/solutions knowledge capture.
- [Mastra AI Skills - TypeScript Agent Framework Setup](/hermes/skills/catalog/mastra-ai-skills-setup) - for teams building agent tooling in TypeScript alongside the CE loop.
- [Hermes Agent Skill Authoring - Official SKILL.md Writing Guide](/hermes/skills/catalog/hermes-agent-skill-authoring-setup) - write your own skills in the same SKILL.md format Compound Engineering uses.
- [Claude Code Skills - Agentic Coding & Skill Development Setup](/hermes/skills/catalog/claude-code-skills-setup) - more Claude Code skill workflows for agentic coding.
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run /ce-setup once per repository; it reports optional tool capabilities and writes .compound-engineering/config.yaml when missing.
- Keep plan and learning artifacts (docs/plans/, docs/solutions/) in version control so ce-compound notes feed later sessions, or relocate all CE artifact folders under one repo-relative root with the docs_root setting.
- Start with /ce-brainstorm before /lfg so the automation plans against real requirements instead of a one-line prompt.
- Invocation differs by host: /skill-name in most, $skill-name in Codex, and /skill:<name> in oh-my-pi (omp).
- When upgrading a pre-native install, refresh the cached marketplace before updating; /plugin update alone stays on the old version.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
