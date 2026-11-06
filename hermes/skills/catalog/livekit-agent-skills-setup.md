---
title: "LiveKit Agent Skills - Voice Agent Lifecycle"
description: "livekit/agent-skills on skills.sh: 7.9K combined installs across 9 listings; seven skills for the voice agent loop, docs lookup through deployment."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/livekit-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-06"
tags: ["hermes skill", "agent skill", "skill setup", "livekit", "voice agents", "webrtc"]
---

# LiveKit Agent Skills - Setup Guide

**Source:** [livekit/agent-skills](https://www.skills.sh/livekit/agent-skills) via skills.sh - 7.9K combined installs across 9 indexed listings; first seen 2026-11-06 (Nov 6, 2026 morning sweep)
**GitHub:** 74 stars, MIT, last pushed 2026-10-21, seven SKILL.md directories under `skills/`, plus `.claude-plugin`, `AGENTS.md` and `CLAUDE.md` at the root
**Category:** Voice agents for agents: build, test, debug, operate and simulate LiveKit agents with docs lookup built in
**Quality Tier:** 🟢 Production - MIT licensed, every sampled listing passes Gen Agent Trust Hub, Socket and Snyk, and the suite is small, current and explicitly designed to defer to live docs.

LiveKit is the WebRTC platform most voice agents get built on, and the Agents SDK is its Python and Node.js framework. These seven skills are the development loop for that framework, one skill per stage: know, build, try, test, simulate, ship, operate. Each one is deliberately small and hands off to the others by name, so a task loads two or three of them rather than one large document.

The design choice worth noticing is that the skills are conceptual. They teach what to check, what goes wrong and which tool fits, then send the agent to `lk --help` and the live docs for flags, schemas and API names. That keeps them correct as LiveKit changes, at the cost of expecting your agent to look things up mid-task. The repository's own `AGENTS.md` holds the authoring conventions and the eval harness that checks each skill triggers on the right requests.

## Installation

The LiveKit CLI path installs all seven skills and wires up the docs server in one command:

```bash
lk skills install
```

It installs for the coding agents you pick, with the ones it detects preselected, and adds the LiveKit Docs MCP server to each one that supports it. `lk skills update` pulls the latest and `lk skills --help` has the rest. For a new agent project, `lk agent init` offers to do this for you.

Claude Code users get a plugin that bundles the same seven skills plus the Docs MCP server:

```
/plugin marketplace add livekit/agent-skills
/plugin install livekit@livekit
```

Pick one path or the other, not both. Claude Code does not deduplicate plugin skills against project skills, so with both installed every description loads twice and the copies compete for routing. Third-party marketplaces do not auto-update by default, so either turn on auto-update for the `livekit` marketplace in `/plugin`, or run `/plugin marketplace update livekit` now and then. Plugin skills are namespaced, so a manual invoke is `/livekit:building-livekit-agents`.

The generic path installs all seven for whichever agents you use, and you can also copy folders out of `skills/` into an agent's skills directory yourself:

```bash
npx skills add livekit/agent-skills
```

Two things the skills assume: the `lk` CLI (four of them drive `lk docs`, `lk agent debugger`, `lk agent simulate` and the deploy commands, and they will tell you if a command is missing or stale), and a LiveKit Cloud project with `lk` authenticated to it for simulations and deployment.

## What It Provides

Three listings clear the 500-install threshold, and the two largest are retired skills, which is the most important thing to know before installing from this index.

| Skill | Installs | Use For |
|---|---|---|
| livekit-agents | 4,133 | Legacy listing: the old umbrella skill, split into the seven current skills and removed from the tree |
| livekit-simulations | 581 | Legacy listing: the old simulation skill, removed; a stale copy describes a CLI surface that no longer exists |
| building-livekit-agents | 514 | Architecture for low latency voice agents: latency design, small context, splitting a monolith into handoffs and tasks |

The remaining 6 indexed listings range from 418 to 486 installs, and they are the rest of the current suite: reading-livekit-docs (486), debugging-livekit-agents (468), testing-livekit-agents (451), operating-livekit-agents (427), writing-livekit-scenarios (420) and running-livekit-simulations (418). The install index has not caught up with the split, so the two names with the largest counts are the two names the README tells you to delete.

## Why This Matters for Hermes Agents

A voice agent fails differently from a text agent. The caller hears the latency, the interruptions and the repetition, and none of those show up in a passing unit test of the handler function. An agent that writes a LiveKit agent from general knowledge produces something that compiles, connects, and then feels wrong the moment a real person speaks to it.

The suite attacks that in the order the failures appear. `reading-livekit-docs` runs first and is loaded by the other skills, because LiveKit's flags, model support and changelogs move faster than any model's training data. `building-livekit-agents` handles what an agent gets structurally wrong: context that grows until latency suffers, one monolithic agent where handoffs and tasks belong, and designs written for readers rather than for listeners.

The middle of the loop is where most of the value sits. `debugging-livekit-agents` drives a real multi-turn conversation against the agent running locally and reads the tool calls behind each reply, which is the difference between "the agent said it booked it" and "the booking tool was called with those arguments". `testing-livekit-agents` then writes turn-level assertions into the project's own pytest or Vitest suite, with LLM judging of intent and mocked tools, so the fix is pinned rather than remembered.

The release end is covered too. `writing-livekit-scenarios` builds the scenarios, and `running-livekit-simulations` runs them in text or audio mode against a local or deployed agent in CI, then triages the failures. `operating-livekit-agents` handles production: version deploy and rollback, the worker process model and prewarming, safe async inside workers, provider timeouts, graceful shutdown and SDK upgrades. For a Hermes agent, that means the whole loop has a documented next step instead of stopping at "it works on my machine".

## Usage

| You say | What happens |
|---|---|
| "Does LiveKit support Gemini realtime?" | reading-livekit-docs looks it up through the Docs MCP server or `lk docs` instead of answering from training data |
| "Build a voice agent that takes orders" | building-livekit-agents covers the architecture: latency budget, context size, handoffs and tasks, and voice-first phrasing |
| "This agent feels sluggish and keeps re-asking things" | The build skill restructures context and handoffs; the debugger then shows what each turn actually sent |
| "Test my agent" | debugging-livekit-agents runs a multi-turn conversation locally in text or audio mode and reads the tool calls behind each reply |
| "Pin that bug as a test" | testing-livekit-agents writes a turn-level test into the project's pytest or Vitest suite, with tool mocking and intent assertions |
| "Run my simulations before we deploy" | running-livekit-simulations runs the scenario sets in text or audio mode and triages the failures |
| "Deploy this and roll it back if it breaks" | operating-livekit-agents covers the Cloud version push, rollback, secrets, prewarming and graceful shutdown |

## Verification

Probe the two skills that carry the suite's method before installing:

```bash
curl -fsSL https://raw.githubusercontent.com/livekit/agent-skills/main/skills/building-livekit-agents/SKILL.md | head -20
curl -fsSL https://raw.githubusercontent.com/livekit/agent-skills/main/skills/reading-livekit-docs/SKILL.md | head -20
```

The first should open with `name: building-livekit-agents` and a description naming handoffs, latency and the Agents SDK; the second with `name: reading-livekit-docs` and the docs-lookup description. Both returned HTTP 200 on 2026-11-06.

The install command itself is the check that the CLI half is in place:

```bash
lk skills install
```

A run that completes without complaint has installed the seven skills and added the Docs MCP server to the agents it supports. `lk skills update` refreshes them afterwards, and `lk skills --help` lists what else the command can do, which is also the honest answer to whether your `lk` is new enough for the skills.

In Claude Code, `/livekit:building-livekit-agents` is the namespaced name to look for, and `/plugin` under Marketplaces shows whether the `livekit` marketplace is the one you installed from.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-06) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| livekit-agents | Pass | Pass | Pass |
| building-livekit-agents | Pass | Pass | Pass |
| debugging-livekit-agents | Pass | Pass | Pass |
| operating-livekit-agents | Pass | Pass | Pass |
| running-livekit-simulations | Pass | Pass | Pass |

This is a clean sheet, and the shape of the suite explains why: the skills are markdown that tells an agent to consult documentation and run a first-party CLI. There is no remote install script, no bundled binary and no credential handling of its own.

The surface that does exist is the CLI. Four skills drive `lk`, and `operating-livekit-agents` deploys versions to LiveKit Cloud and rolls them back, so the agent is holding a credential that can change what is running in production. Scope that credential to the project you intend, and treat a deploy prompt the way you would treat any other production change.

Two smaller items. `lk skills install` and the Claude Code plugin both add the LiveKit Docs MCP server, which is a second tool surface with read access to LiveKit's documentation; that is the intended design, not a surprise, but it is a server your agent now talks to. And installing both the plugin and the CLI path leaves duplicate skill descriptions competing for routing, which is a correctness problem rather than a security one, though it does mean the agent may act on a copy you did not intend to update.

## Limitations

- Snapshot data, verified 2026-11-06: 7,898 combined installs across 9 indexed listings; 74 GitHub stars; MIT; last pushed 2026-10-21. Counts drift over time.
- The two highest-install listings are retired. `livekit-agents` and `livekit-simulations` were split into the seven current skills and removed, and the README states that a stale copy of `livekit-simulations` will steer an agent at a CLI surface that no longer exists. Nine listings, seven directories.
- Simulations and deployment need a LiveKit Cloud project with `lk` authenticated to it. Without one, three of the seven skills cannot do their job, and the rest still work locally.
- The skills are conceptual by design. They route the agent to `--help` and the live docs rather than carrying flags and schemas, so a task costs extra lookups and a skill can be right while a flag in the CLI has moved on.
- Four skills depend on the `lk` CLI being installed and current. The skills check for the commands they need, but an old CLI still fails at the point of use.
- Installing the Claude Code plugin and `lk skills install` together loads every skill description twice. The README calls this out explicitly; the fix is to pick one.

## Related

- [Video Agent Skills - Video Production for Agents](/hermes/skills/catalog/video-agent-skills-setup)
- [AI Video Generation Setup](/hermes/skills/catalog/ai-video-generation-setup)
- [Build Mcp Server Setup](/hermes/skills/catalog/build-mcp-server-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with `reading-livekit-docs` in the context even when you think you know the API. It is the skill the other six load first, and it is the cheapest way to stop an agent inventing a flag.
- Delete the old copies before installing. If an agent still has `livekit-agents` or `livekit-simulations`, the README's instruction is to remove them and reinstall, not to let the new skills shadow them.
- Use the debugger before the test suite. A live multi-turn conversation tells you whether the agent is behaving; the turn-level test then keeps it that way.
- Run simulations in audio mode before a release. Text mode catches logic, and barge-in, latency and interruption behaviour only appear once there is audio.
- Keep the deploy skill away from unattended runs. It can roll a version back as well as forward, and a rollback triggered by a misread log line is its own incident.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
