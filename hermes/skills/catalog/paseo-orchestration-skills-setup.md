---
title: "Paseo Skills - A Fleet of Coding Agents"
description: "getpaseo/paseo on skills.sh: 32.4K combined installs; handoff, advisor and committee skills that let one agent orchestrate many, across providers."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/paseo-orchestration-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-06"
tags: ["hermes skill", "agent skill", "skill setup", "multi-agent", "orchestration", "handoff"]
---

# Paseo Skills - Setup Guide

**Source:** [getpaseo/paseo](https://www.skills.sh/getpaseo/paseo) via skills.sh - 32.4K combined installs across 14 indexed listings; first seen 2026-11-06 (Nov 6, 2026 evening sweep)
**GitHub:** 23,334 stars, Apache-2.0, last pushed 2026-11-07, 9 SKILL.md directories across skills/, .agents/skills/ and .claude/skills/
**Category:** Multi-agent orchestration for agents: advisor and committee modes, handoffs, provider switching and release workflows
**Quality Tier:** 🟡 Review - a large, active, well-licensed project with clean verdicts on its core skills, held back by mixed scanner results on the peripheral ones and by a listing set larger than the skills it actually ships.

Paseo is an open source agentic development environment for desktop, mobile, web and the CLI. Its own description is one interface for Claude Code, Codex, Copilot, OpenCode, Pi, Antigravity and Muse Code agents, running many agents at once with each one in its own worktree, on one machine or several. The repository is a monorepo: a daemon in `packages/server`, an Expo client, a `paseo` CLI, an Electron desktop app and the website.

The skills in this guide are a small part of that, and the interesting part. They teach an agent to use Paseo as an orchestration layer: to hand a task to another agent with a proper briefing, to convene two agents for a second opinion or a committee plan, to run a loop until an exit condition holds, and to reference how hosts, workspaces, schedules and heartbeats work. The README's framing is exact: skills teach your agent to use Paseo to orchestrate other agents.

The docs are unusually clear about division of labour. Committee members return analyses without editing files; the main agent synthesises their plans, implements, and sends the diff back for review. The advisor returns a second opinion without editing anything. Handoff transfers context rather than work in progress, so the receiving agent knows the files, decisions, constraints and acceptance criteria before it starts.

## Installation

The README's terminal route:

```bash
npx skills add getpaseo/paseo
```

The product route is inside Paseo itself. The orchestration skills guide says to open Settings, then your host, then Agents, then Orchestration skills, and choose which skills to install on that host. The same settings card updates or uninstalls them, and the host refreshes selected installed Paseo skills on startup.

The repository is also indexed on skills.sh under the same slug, so the command above is what the listing publishes.

Once installed, the skills are invoked by name in an agent conversation. The README names three:

- `/paseo-handoff` to plan with one agent and hand the implementation to another.
- `/paseo-advisor` to get a second opinion without delegating the work.
- `/paseo-committee` to get two contrasting analyses of a hard problem.

The release skills are a different animal. `release-stable` and `release-beta` cut releases of Paseo itself by following the checklists in `docs/release.md`, and `store-screenshots` refreshes app store screenshots. They ship in this repository for its maintainers, and they will be installed alongside the orchestration skills if you pull everything.

## What It Provides

Ten of the fourteen indexed listings clear the 500-install threshold:

| Skill | Installs | Use For |
|---|---|---|
| paseo | 5,612 | Reference for hosts, projects, workspaces, schedules and heartbeats; checks agent profiles before delegating |
| paseo-handoff | 5,221 | Transfer a task with a briefing: relevant files, progress, decisions, constraints, acceptance criteria |
| paseo-committee | 5,117 | Two high-reasoning agents analyse independently and return plans; the main agent synthesises and implements |
| paseo-advisor | 4,021 | One agent gives a judgement on a design, diff or question, without editing anything |
| paseo-loop | 2,574 | Run an agent loop until an exit condition holds: babysit, retry, watch, check every N |
| release-stable | 2,531 | Cut a stable release of Paseo, fresh or promoted from beta, against the release checklist |
| release-beta | 2,379 | Cut a beta release and work the beta completion checklist |
| paseo-help | 1,747 | Answer product questions: setup, configuration, connectivity, providers, workspaces, logs, troubleshooting |
| paseo-plugin | 1,652 | Build and manage local plugins: panels, lifecycle hooks, permissions, themes, RPCs |
| paseo-orchestrate | 749 | Deprecated alias that redirects to paseo-epic and tells the user it was renamed |

The remaining 4 indexed listings range from 35 to 302 installs.

The skills split across three directories for a reason. The orchestration set lives under `skills/` and is what the install command targets. The two release skills live under `.agents/skills/` because they operate on the repository. `store-screenshots` lives under `.claude/skills/`. If you only want orchestration, install the individual skills rather than the whole repo.

There is also a real distinction inside the orchestration set between advice and execution. `paseo-advisor` and `paseo-committee` are read-only by design: the docs state that committee members return analyses without editing files. `paseo-handoff` and `paseo-loop` change things, in another agent's worktree, which is the whole point of the product.

## Why This Matters for Hermes Agents

Single-agent loops fail in a specific way: the agent that got stuck is the agent asked to get unstuck, and it answers from the same context that produced the dead end. The committee and advisor patterns exist to break that, and they are worth copying even if you never install Paseo. Two independent analyses, produced without file edits, then synthesised by the main agent, is a cheap and effective way to escape a tunnel.

The handoff pattern is the other half. A briefing that names the files, the progress so far, the decisions taken, the constraints and the acceptance criteria is the difference between delegation and abandonment. `paseo-handoff` makes that structure explicit, and asks for a separate worktree when the receiving agent should edit independently.

The product-level design is instructive too. Parallel agents, each in its own worktree, across provider families, with profile notes that record what each agent is good at: that is infrastructure most teams are currently building badly by hand. Paseo's answer is a daemon that owns the worktrees and an MCP surface that agents can drive.

The honest caveat is that these skills are thin without the product. They are instructions for driving a daemon; if the daemon and its provider CLIs are not installed and authenticated, the skill has nothing to orchestrate.

## Usage

| You say | What happens |
|---|---|
| "Hand the auth fix to an implementation agent in its own worktree" | paseo-handoff briefs the receiving agent with files, decisions, constraints and acceptance criteria |
| "Get a second opinion on this migration plan" | paseo-advisor picks a profile whose notes fit the work and returns judgement without editing |
| "Why are the websocket connections dropping under load?" | paseo-committee gives the question to two agents for independent root cause analysis, then the main agent synthesises |
| "Keep trying until the deploy is green" | paseo-loop runs the loop with an exit condition instead of a fixed number of attempts |
| "How do I add a provider in Paseo?" | paseo-help answers from the product documentation: setup, connectivity, providers, logs |
| "Build me a plugin with a sidebar panel" | paseo-plugin walks the plugin API: panels, hooks, commands, themes |
| "Cut a beta" | release-beta follows the beta flow and completion checklist in docs/release.md |

## Verification

The core skill is readable before you install anything. This path returned 200 on `main` when checked on 2026-11-06:

```bash
curl -fsSL https://raw.githubusercontent.com/getpaseo/paseo/main/skills/paseo/SKILL.md | head -20
```

It should open with `name: paseo`, a one-line description covering hosts, projects, workspaces, workspace scripts, agents, schedules and heartbeats, and then a body that opens by describing Paseo as a remote daemon controlled through MCP tools or the CLI.

The product route is the most reliable check, because it reflects what the daemon will actually load. Open Paseo, go to Settings, then your host, then Agents, then Orchestration skills: the installed set should appear there, and the host refreshes it on startup.

If you installed from the terminal, confirm the files where the skills CLI put them, which by default is the agent skills directory in the current project:

```bash
ls .claude/skills | grep paseo
ls ~/.claude/skills | grep paseo
```

The first command covers a project install, the second a `-g` install. You should see `paseo`, `paseo-handoff`, `paseo-committee` and `paseo-advisor` alongside whichever others you chose.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-06) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| paseo | Pass | Pass | Pass |
| paseo-advisor | Pass | Pass | Pass |
| paseo-help | Pass | Pass | Warn |
| paseo-chat | Pass | Warn | Pass |
| paseo-orchestrator | Warn | Pass | Pass |

The two skills you will actually use for orchestration, `paseo` and `paseo-advisor`, are clean on all three scanners. The mixed verdicts land on `paseo-help`, `paseo-chat` and the deprecated `paseo-orchestrator`, which is the pattern you would want: risk concentrated in the periphery rather than the core.

The licence is unambiguous. Apache-2.0 in the repository root, with an active project behind it and a public changelog. Nothing here is a reverse-engineered wrapper around someone else's product.

The real exposure is what the product does by design. These skills launch other agents, create worktrees and push branches, which means the blast radius of a bad handoff is a real branch on a real remote. The plugin system is the other edge: Paseo's own README warns that plugins run with access to your daemon machine and inside connected clients, and to install only code you trust.

There is one privacy claim worth recording because it is unusual: the README states that Paseo has no telemetry, tracking or forced log-ins. That is a statement about the product, not a guarantee you can verify from the skills, but it is the kind of claim a self-hosted tool should be held to.

## Limitations

- Snapshot data, verified 2026-11-06: 32,407 combined installs across 14 indexed listings; 23,334 GitHub stars; Apache-2.0; last pushed 2026-11-07. Counts drift over time.
- The listings outnumber the skills. Fourteen listings are indexed against nine SKILL.md directories, and `paseo-loop`, `paseo-orchestrate`, `paseo-chat`, `paseo-epic` and `paseo-orchestrator` have no directory in the current tree.
- One listed skill is deprecated. `paseo-orchestrate` exists to redirect to `paseo-epic` and tell the user it was renamed, yet it still carries 749 installs.
- The skills are drivers, not engines. Without the Paseo daemon running and the provider CLIs installed and authenticated, an orchestration skill has nothing to act on.
- Three of the nine shipped skills are maintainer tools. `release-stable`, `release-beta` and `store-screenshots` operate on the Paseo repository and app store listings, not on your project.
- The install pulls everything. `npx skills add getpaseo/paseo` brings the release and screenshot skills along with the orchestration set unless you name individual skills.

## Related

- [Claw Multi-Agent Skill - Setup Guide](/hermes/skills/catalog/claw-multi-agent-setup)
- [Multi-Agent Review - Adversarial Code Review Setup](/hermes/skills/catalog/multi-agent-review-setup)
- [Superpowers - Agentic Skills Framework & Development](/hermes/skills/catalog/superpowers-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Use advisor before committee. One agent's outside take is cheap and usually enough; save the two-agent committee for a problem that has already survived one round of analysis.
- Ask for the worktree explicitly. The docs say to request a separate worktree when the receiving agent should edit independently, and a handoff that skips this creates a merge conflict instead of a task.
- Keep the committee read-only. Analyses that edit files destroy the independence the pattern depends on, and the docs are clear that members return plans rather than patches.
- Install the orchestration skills individually. Pulling the whole repository adds three maintainer-only skills that will never be relevant to your project.
- Check the profile notes before delegating. The `paseo` reference reads agent profile notes to pick a match, so an empty profile set produces a generic handoff.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
