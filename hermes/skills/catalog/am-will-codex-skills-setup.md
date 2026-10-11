---
title: "CodexSkills - Agent Orchestration Skills Setup"
description: "Setup guide for am-will/codex-skills - 20.2K combined installs. 19 skills: planners, parallel task runners, docs access, and frontend design."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/am-will-codex-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-10"
tags: ["hermes skill", "agent skill", "skill setup", "agent orchestration", "codex", "parallel agents"]
---

# CodexSkills - Setup Guide

**Source:** [am-will/codex-skills](https://www.skills.sh/am-will/codex-skills) via skills.sh - 20.2K combined installs across 19 indexed listings; first seen Oct 9, 2026 (extended-query probe)
**GitHub:** [am-will/codex-skills](https://github.com/am-will/codex-skills) (1,035 stars, no license file; pushed Jul 14, 2026; `skills/<name>/SKILL.md` layout)
**Category:** Agent Orchestration / Dev Workflow
**Quality Tier:** 🟡 Beta - 1,035-star collection; NO LICENSE file; mixed sampled verdicts (Context7: Socket + Snyk Warn)

am-will's CodexSkills is a 19-skill collection built around a planning-and-execution loop: `planner` and `plan-harder` produce phased implementation plans, `parallel-task` executes those plans by launching subagents in waves, and `llm-council` runs multi-agent planning with Claude, Codex, and Gemini planners feeding a judge agent (with a real-time web UI). Around that core sit documentation access skills (`context7`, `openai-docs-skill`, `read-github`), frontend design guidance imported from Anthropic and Vercel, Codex tooling (`role-creator`, `create-hook`, `pluginstaller`), and browser automation built on Gemini Computer Use and Vercel Labs' agent-browser. Everything installs through the standard skills CLI, so it works with Codex, Claude Code, and other agents even though the README is written Codex-first.

The repo also carries material beyond the skills: a `hooks/` catalog of 51 ready-to-install Codex hook bundles and custom multi-agent TOML definitions under `agents/`, both of which install manually alongside the skill set.

---

## Installation

Prerequisites: Node.js for the skills CLI. Install from the README's command set:

```bash
# List available skills first
npx skills add am-will/codex-skills --list

# Install specific skills globally
npx skills add am-will/codex-skills --skill planner --skill context7 -g

# Install all skills interactively
npx skills add am-will/codex-skills -g

# Target specific agents and skip prompts
npx skills add am-will/codex-skills --skill planner -a claude-code -a codex -g -y
```

Requirements the README calls out: the Context7 docs skill needs a Context7 API key in `CONTEXT7_API_KEY` (see `skills/ctx7old/.env.example`), `gemini-computer-use` needs a `GEMINI_API_KEY`, and `llm-council` needs API access or subscriptions for multiple providers, configured by running `./setup.sh` in the skill directory.

## What It Provides

Install counts from the Oct 10, 2026 skills.sh snapshot:

| Skill | Installs | Use For |
|---|---|---|
| frontend-design | 1,426 | Distinctive frontend design system guidance (imported from Anthropic) |
| context7 | 1,220 | Fetch up-to-date library documentation via the Context7 CLI |
| planner | 1,196 | Comprehensive, phased implementation plans with sprints and atomic tasks |
| read-github | 1,193 | Read and search GitHub repository documentation through gitmcp.io |
| parallel-task | 1,176 | Execute plan files by launching multiple parallel subagents at once |
| plan-harder | 1,163 | Enhanced planning variant with deeper analysis and task breakdown |
| llm-council | 1,160 | Multi-agent planning: Claude, Codex, and Gemini planners plus a judge agent and a live web UI |
| openai-docs-skill | 1,159 | Query OpenAI developer docs through the OpenAI Docs MCP server |
| gemini-computer-use | 1,159 | Gemini 2.5 Computer Use browser control with a Playwright safety confirmation loop |
| swarm-planner | 1,157 | Dependency-aware implementation plans optimized for parallel multi-agent execution |
| vercel-react-best-practices | 1,156 | React/Next.js performance guidance (imported from Vercel) |
| role-creator | 1,152 | Create and update custom Codex agents as standalone TOML files |
| parallel-task-spark | 1,149 | Sparky wave-based executor that orchestrates subagents from plan files in dependency order |
| super-swarm-spark | 1,146 | Rolling-pool orchestrator that keeps up to 15 Sparky subagents running until the plan completes |
| tdd-test-writer | 857 | Test-driven development test-writing workflow |

Two indexed listings use space-containing names and are omitted from the table above: Frontend Responsive Design Standards at 1,242 installs, and Agent Browser at 1,161 installs.

The remaining 2 indexed listings (both under the 500-install threshold) range from 1 to 309 installs.

## Why This Matters for Hermes Agents

Planning is the bottleneck skill in agentic work, and this collection treats it as a pipeline: a plan file from `planner` or `plan-harder` is structured input that `parallel-task` can execute as subagent waves. `llm-council` extends the idea to model diversity, having Claude, Codex, and Gemini generate independent plans and a judge agent synthesize them, which is directly relevant to anyone running multi-model setups. The documentation skills (`context7`, `openai-docs-skill`, `read-github`) attack a permanent agent problem, stale training data, by pulling live library and API docs at task time. Frontend guidance imported from Anthropic and Vercel plus the browser skills cover the build-and-verify half of the loop. Even if you install only the skills, the repo's 51 Codex hook bundles and TOML agent definitions are worth studying as patterns. One caution shapes adoption: there is no license file, so review the terms before internal or commercial reuse.

## Usage

| You say | What happens |
|---|---|
| "Plan this feature as a phased implementation" | planner produces sprints and atomic tasks as a structured plan file |
| "Run the plan with parallel agents" | parallel-task launches multiple subagents in waves and logs results |
| "Get a second opinion on this architecture" | llm-council has Claude, Codex, and Gemini planners generate options, then a judge synthesizes |
| "What does the latest version of this library do?" | context7 fetches current library documentation through the Context7 CLI |
| "Read this GitHub repo and summarize its docs" | read-github converts the repo to a gitmcp.io view for LLM-friendly access |
| "Review my landing page design" | frontend-design applies Anthropic's design system guidance |
| "Automate this browser task" | gemini-computer-use or the agent-browser skill drives the browser with a safety confirmation step |

## Verification

```bash
# Confirm the install through the skills CLI
npx skills list | grep -iE 'planner|frontend-design|llm-council'

# Review the layout-verified skill straight from GitHub before installing
curl -sL https://raw.githubusercontent.com/am-will/codex-skills/main/skills/frontend-design/SKILL.md | head -20
```

Also confirm any required keys are in place (`CONTEXT7_API_KEY`, `GEMINI_API_KEY`) before invoking the skills that need them.

## Security

skills.sh verdicts for sampled skills (verified Oct 10, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| frontend-design | Pass | Pass | Pass |
| context7 | Pass | Warn | Warn |
| planner | Pass | Pass | Pass |

The Context7 docs skill is the flagged one in the sample (Socket and Snyk Warn); the sampled planner and frontend-design skills pass on all three engines. Coverage is three of nineteen listings.

## Limitations

- No license file in the repository; treat distribution and commercial reuse as unresolved until the maintainer adds one.
- Maintenance cadence: last pushed Jul 14, 2026, and the Codex event model plus provider APIs this collection targets move fast.
- Mixed sampled verdicts: context7 scored Socket plus Snyk Warn; only three of nineteen listings were sampled.
- Several skills need external keys or accounts: Context7, Gemini, and multi-provider access for llm-council.
- The 51 hook bundles and TOML agent definitions are not indexed by skills.sh; install and manage those manually.
- Snapshot data, verified Oct 10, 2026: 20,182 combined installs across 19 indexed listings; 1,035 GitHub stars; no license file; last pushed Jul 14, 2026. Counts drift over time.

## Related

- [OpenAI Codex Skills - Official Skills Catalog Setup](/hermes/skills/catalog/openai-codex-skills-setup) - official Codex skills to pair with this community set
- [Mosif16 Codex Skills - iOS Design Setup](/hermes/skills/catalog/mosif16-codex-skills-setup) - Codex skills focused on iOS design work
- [Agent Browser - Vercel Labs CLI for AI Agents Setup](/hermes/skills/catalog/agent-browser-setup) - the browser automation CLI referenced by this collection
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Feed `parallel-task` a plan file produced by `planner`; the executor is designed around that structured input, not free-form prompts.
- Pick one browser path: the README recommends `agent-browser` for speed and simplicity over `gemini-computer-use`.
- Set keys before invoking: `CONTEXT7_API_KEY` for the docs skill and `GEMINI_API_KEY` for computer use; `llm-council` needs multi-provider access plus its `./setup.sh`.
- Try `llm-council` when a plan's stakes justify multiple models; its judge step is the part single-model planning cannot replicate.
- Review the license situation (none in the repo) before using these skills or the hook bundles in a commercial workflow.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
