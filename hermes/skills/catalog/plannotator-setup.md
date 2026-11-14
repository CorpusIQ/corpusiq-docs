---
title: "Plannotator - Plan and Review Workspace Setup"
description: "backnotprop/plannotator: 44.9K combined installs across 12 listings, a human-in-the-loop planning and code review workspace for agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/plannotator-setup/"
robots: "index,follow"
last_updated: "2026-11-14"
tags: ["hermes skill", "agent skill", "skill setup", "code review", "planning", "human in the loop"]
---

# Plannotator - Setup Guide

**Source:** [backnotprop/plannotator](https://www.skills.sh/backnotprop/plannotator) via skills.sh - 44.9K combined installs across 12 indexed listings; first seen Nov 14, 2026
**GitHub:** 10,650 stars, Apache-2.0 license, `main` branch, last pushed 2026-11-14, 24 `SKILL.md` files under `apps/.../skills/` directories
**Category:** Human-in-the-loop planning, code review and annotation workspace for agents
**Quality Tier:** 🟡 Yellow - three sampled skills carry a Warn verdict, with no Fail in the sample.

Plannotator is a local, browser-based review surface for AI coding agents (Claude Code, Codex, Copilot CLI, Gemini CLI, OpenCode, Kiro and others). When an agent proposes a plan, a decision or finished work, the app opens in the browser so you can mark it up and send feedback back to the agent as its next turn. It plugs into agents through plugins, hooks and slash commands.

The indexed listings map to the workflow: plannotator-visual-explainer, plannotator-compound and plannotator-setup-goal cover planning and visualization, while plannotator-review, plannotator-annotate and plannotator-last drive the browser-based review and annotation surfaces. The skills live in several directories in the monorepo - `apps/skills/...`, `apps/kiro-cli/skills/...` and `apps/qwen-code/skills/...` - so list the tree before you fetch a raw SKILL.md URL.

## Installation

One installer covers almost every agent. It installs the `plannotator` binary, auto-detects installed agents, and configures hooks, skills and slash commands for each:

```bash
curl -fsSL https://plannotator.ai/install.sh | bash
```

On Windows PowerShell use `irm https://plannotator.ai/install.ps1 | iex`. Pass `--minimal` (or export `PLANNOTATOR_MINIMAL=1`) to install only the binary. For Claude Code the README also documents the plugin route: `/plugin marketplace add backnotprop/plannotator` then `/plugin install plannotator@plannotator`. Codex needs nothing extra (plan review is enabled automatically via its Stop hook); Kiro installs skills and an example agent automatically.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| plannotator-visual-explainer | 14,248 | Generate self-contained HTML visualizations with Plannotator theming for implementation plans and PRs. |
| plannotator-compound | 13,093 | Analyze a Plannotator plan archive to extract denial patterns, feedback taxonomy, and evolution over time. |
| plannotator-setup-goal | 12,852 | Turn an idea or objective into a goal package for /goal; interview the user and build a reviewed fact sheet. |
| plannotator-review | 1,107 | Open the browser-based code review UI for local changes or a PR/MR URL, then address the returned feedback. |
| plannotator-annotate | 1,097 | Open the annotation UI for a file, folder, or URL, then address the returned annotations. |
| plannotator-last | 1,073 | Open Plannotator on the latest rendered assistant message and use the returned annotations to revise it. |

The remaining 6 indexed listings range from 108 to 298 installs.

## Why This Matters for Hermes Agents

Plannotator gives agents a review loop that keeps a human in control. When an agent calls ExitPlanMode or proposes a decision, the hook fires, a local server reads the plan, and the browser opens a review UI; the human annotates, approves or denies, and the feedback becomes the agent's next turn. An agent that hands off to a review surface produces plans and diffs with a real approval gate instead of a log of edits.

The Inbox is the second point. plannotator-inbox surfaces questions, files and guided reviews from several agents in one local window, and replies arrive as the next turn of the session that asked. Nothing holds an agent session open while the human reads.

For multi-agent work the combination matters: plans, specs, markdown and HTML artifacts can be annotated and sent back, and code review covers Git, GitButler, Jujutsu, Perforce, GitHub and GitLab. The privacy model is local-first - plans, diffs, annotations and history stay on the machine by default with no telemetry.

## Usage

| You say | What happens |
|---|---|
| "Review my current diff" | /plannotator-review opens the browser diff viewer for uncommitted changes. |
| "Annotate this README" | /plannotator-annotate README.md opens the annotation UI for the file. |
| "Annotate this PR" | /plannotator-review with the PR URL fetches it and opens the full diff viewer. |
| "Show me your last message" | /plannotator-last opens the latest assistant message for annotation. |
| "Set up a goal for this idea" | plannotator-setup-goal interviews the user and builds a goal package for /goal. |
| "What did I keep rejecting?" | plannotator-compound analyzes the plan archive for denial patterns and feedback taxonomy. |
| "What is waiting for me?" | plannotator-inbox opens the Inbox with questions, files and reviews from your agents. |

## Verification

Probe skills on the `main` branch before installing. All return 200:

```bash
curl -fsSL https://raw.githubusercontent.com/backnotprop/plannotator/main/apps/skills/extra/plannotator-visual-explainer/SKILL.md | head -12
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/backnotprop/plannotator/main/apps/kiro-cli/skills/plannotator-review/SKILL.md
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/backnotprop/plannotator/main/apps/qwen-code/skills/plannotator-last/SKILL.md
```

Skills live in several directories (`apps/skills/extra/`, `apps/kiro-cli/skills/`, `apps/qwen-code/skills/`, `apps/skills/claude/`); list the tree before fetching rather than assuming a single layout.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-14) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| plannotator-visual-explainer | Pass | Pass | Warn |
| plannotator-compound | Pass | Pass | Pass |
| plannotator-setup-goal | Pass | Pass | Pass |
| plannotator-review | Warn | Warn | Warn |
| plannotator-annotate | Warn | Pass | Pass |
| plannotator-last | Warn | Pass | Warn |

The sample shows no Fail verdicts but four Warn verdicts: plannotator-review warns across all three auditors, plannotator-visual-explainer warns Snyk, plannotator-annotate warns the Gen Agent Trust Hub, and plannotator-last warns the Gen Agent Trust Hub and Snyk. plannotator-compound and plannotator-setup-goal pass all three. The sample covers 6 of the 12 indexed listings. The repo's released binaries ship SHA256 sidecars, SLSA provenance attestations and a CycloneDX SBOM evaluated with Grype, but those cover release artifacts, not the skill-level verdicts. Each review surface makes a GitHub request on load to check for releases (no plan or review content is sent); disable it with `plannotator review --no-git-remote-check` or `PLANNOTATOR_GIT_REMOTE_CHECK=0`.

## Limitations

- Snapshot data, verified 2026-11-14: 44,929 combined installs across 12 indexed listings; 10,650 GitHub stars; Apache-2.0; last pushed 2026-11-14. Counts drift over time.
- GitHub reports Apache-2.0, but the README states the repo is dual-licensed under Apache 2.0 or MIT at your option.
- The sample covers 6 of 12 listings and shows Warn verdicts on the three review and annotation skills; the rest publish no verdict on skills.sh.
- This is a monorepo, not a prompt-only pack: the tree tracks 6,335 files across apps, packages and plugins, which the skill-level verdicts do not cover.
- Skills live in several directories (`apps/skills/...`, `apps/kiro-cli/skills/...`, `apps/qwen-code/skills/...`), so probe the exact path before fetching.

## Related

- [Superpowers - Agentic Skills Framework Setup](/hermes/skills/catalog/superpowers-setup)
- [Open SDD Skills - Spec-Driven Development Setup](/hermes/skills/catalog/open-skilled-sdd-setup)
- [Design Judge Skills - Design Award Workflow Setup](/hermes/skills/catalog/design-judge-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install once and let the installer configure every detected agent; it sets up hooks, skills and slash commands per agent.
- Use the Claude Code plugin path (`/plugin marketplace add backnotprop/plannotator`) if you prefer the plugin system over manual hooks.
- Turn off the release check on strict-network machines with `plannotator review --no-git-remote-check`.
- For multi-agent review, reach for the Inbox (plannotator-inbox): questions and files from several agents in one window.
- Keep the human in the loop deliberately: approve or deny plans in the browser, and the feedback becomes the agent's next turn.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
