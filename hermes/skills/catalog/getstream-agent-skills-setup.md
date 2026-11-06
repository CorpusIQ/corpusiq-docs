---
title: "Stream Agent Skills - Chat, Feeds and Video SDK"
description: "getstream/agent-skills on skills.sh: 6.0K combined installs across 12 listings; Stream Chat, Video and Feeds SDKs for web, mobile and games."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/getstream-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-05"
tags: ["hermes skill", "agent skill", "skill setup", "chat", "sdk", "react native"]
---

# Stream Agent Skills - Setup Guide

**Source:** [getstream/agent-skills](https://www.skills.sh/getstream/agent-skills) via skills.sh - 6.0K combined installs across 12 indexed listings; first seen 2026-11-05 (Nov 5, 2026 evening sweep)
**GitHub:** 21 stars, Apache-2.0, last pushed 2026-11-05, 11 SKILL.md directories under skills/
**Category:** In-app chat and feeds for agents: Stream SDK scaffolding across React, React Native, Flutter, Swift, Unity and Unreal
**Quality Tier:** 🟡 Review - Apache-2.0 is in place, but 3 of the 5 sampled skills.sh audits carry a Warn (stream-cli Socket and Snyk, stream-unreal Snyk, stream-unity Snyk).

Stream for AI coding agents is GetStream's own skill pack for wiring Chat, Video, Feeds and Moderation into applications. The skills scaffold new apps and add Stream to existing React, Next.js, React Native, Swift, Android, Flutter, Unity and Unreal projects, and a hosted Stream MCP server signs in with your Stream account so the agent can list your apps and call the Stream API on them.

The pack is organised as one router plus platform skills. `stream` handles generic routing and runs `getstream` CLI commands for data queries, app configuration and onboarding; each platform skill carries the integration guidance for its framework, including the SDK specifics that general knowledge gets wrong. Two older entrypoints, `stream-builder` and `stream-docs`, remain so older CLI installations keep working and forward to the current skills.

## Installation

Claude Code installs the plugin from the repository marketplace:

```text
/plugin marketplace add GetStream/agent-skills
/plugin install getstream@getstream
```

Then run `/mcp` and sign in to the `getstream` server. The MCP server is hosted at `https://mcp.getstream.io/mcp`, and the pack ships it as `mcp.json` for clients that read that file.

Cursor installs through its own UI: open Customize, search for Stream, select Install, and sign in to the `getstream` MCP server when asked.

Any other agent installs through the Stream CLI:

```bash
getstream skills
```

With no arguments it installs the `stream` skill and its compatibility entrypoints. Name platform skills to add them:

```bash
getstream skills stream-react stream-swift
getstream skills -h
```

Project setup is a separate command, covering auth, organisation and app selection, and credentials:

```bash
getstream init
```

The plugins do not bundle the CLI itself. When a skill needs it and it is missing, the `stream` skill runs Stream's install script, which is `curl -fsSL https://getstream.io/cli.sh | bash`.

## What It Provides

Four listings clear the 500-install threshold. Two of them are current skills and two are the compatibility entrypoints that older installations still call.

| Skill | Installs | Use For |
|---|---|---|
| stream | 1,574 | Router and CLI entry point: route any Stream task, run getstream commands for data queries, app config and onboarding, and look up SDK docs |
| stream-docs | 792 | Compatibility entrypoint for requests naming stream-docs; forwards SDK documentation lookups to the current skills |
| stream-builder | 729 | Compatibility entrypoint for requests naming stream-builder; routes application work to the appropriate platform skill |
| stream-react-native | 710 | React Native CLI and Expo apps: scaffold, add Chat/Video/Feeds, upgrade SDKs, migrate from Sendbird, build AI assistants and agentic chat |

The remaining 8 indexed listings range from 57 to 493 installs: stream-android (493) and stream-swift (465) sit just under the threshold, then stream-cli (403), stream-react (311), stream-flutter (309), stream-unreal (73), stream-feeds-migration (73) and stream-unity (57).

## Why This Matters for Hermes Agents

Third-party SDK integration is where an agent's confidence does the most damage. Stream has seven client SDKs with different package names, different authentication flows and different feature coverage, and a model asked to "add chat" will mix them. A Flutter answer that imports the React package, a Unity answer that promises Feeds, an Unreal answer that wires Video, all of them plausible and all of them wrong.

This pack fixes that by making platform selection explicit. The router decides which skill applies, each platform skill carries its own integration guidance and supporting files, and the README states the coverage limits directly: Unity gets Chat and Video with no Feeds SDK, Unreal gets Chat only with no Video or Feeds. An agent that repeats those limits is measurably more useful than one that invents a package.

The CLI and MCP pairing is the second advantage. Skills are instructions, but the `getstream` CLI turns them into actions: list my channels, show flagged messages, any active calls, configure channel types and permissions. That means a verification step after integration is possible instead of assumed, and the MCP server means the agent can see your actual apps rather than a generic example.

The migration paths are unusually concrete for a vendor pack. `stream-feeds-migration` samples a v2 app's live activities and reactions and generates a sync mapping object, with the keys it deliberately left at defaults. `stream-react-native` covers upgrading Chat v8 to v9 and moving off Sendbird's `@sendbird/chat` and `@sendbird/uikit-react-native`. Those are the tasks where an LLM's training data is oldest and an agent's improvisation is most expensive.

Finally, the README is honest about scope. It states that a skill's tool permissions belong to the harness, that the plugins do not include the CLI, and that the skills connect to four named network endpoints. That level of disclosure is what makes a vendor skill reviewable rather than trusted.

## Usage

| You say | What happens |
|---|---|
| "Add chat to this Next.js app" | stream routes to stream-react, which wires the SDK and builds the channel and message UI |
| "Scaffold a new app with video calls" | stream-react scaffolds a Next.js project with Tailwind and the Stream SDKs wired end to end |
| "Wire Stream into my Expo app" | stream-react-native covers package setup, auth and token wiring for Expo or RN CLI |
| "Any active calls right now?" | stream runs the getstream CLI query and returns live data from your app |
| "Show the flagged messages" | stream queries moderation state through the CLI |
| "Plan our Feeds v2 to v3 migration" | stream-feeds-migration samples live activities and produces the sync mapping |
| "We are moving off Sendbird" | stream-react or stream-react-native covers the Sendbird migration path for its platform |
| "Upgrade our Chat SDK version" | The platform skill reads the live release guide and applies the upgrade steps |

## Verification

Confirm the router before installing anything:

```bash
curl -fsSL https://raw.githubusercontent.com/getstream/agent-skills/main/skills/stream/SKILL.md | head -5
```

It should open with `name: stream` and a description naming Chat, Video, Feeds, Moderation and Agents, plus the routing role. Then confirm the CLI sees the pack and what it would install:

```bash
getstream skills -h
```

After installing, confirm the skills are on disk and that the platform skill you wanted is among them:

```bash
ls ~/.claude/skills
```

The `stream` skill directory should contain SKILL.md plus the supporting files it references: `integration-review.md`, `sendbird-data-migration.md` and `ai-backend-contract.md`. A directory with only SKILL.md means a partial install.

Finally, confirm the MCP connection, since half the value is the live account: run `/mcp` and check that the `getstream` server is signed in and lists your apps.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-05) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| stream | Pass | Pass | Pass |
| stream-react-native | Pass | Pass | Pass |
| stream-cli | Pass | Warn | Warn |
| stream-unreal | Pass | Pass | Warn |
| stream-unity | Pass | Pass | Warn |

`stream-cli` carries both a Socket and a Snyk Warn and is the entry most likely to execute commands, which fits its role: it is the CLI wrapper rather than a documentation skill. The two game-engine skills carry Snyk Warns as well.

The behaviour to review before production is the CLI bootstrap. If `getstream` is not installed, the `stream` skill runs `curl -fsSL https://getstream.io/cli.sh | bash`, which is a remote script executed with your shell privileges. Pin the CLI version yourself or install it ahead of time rather than letting an agent trigger that path unattended.

The declared network surface is the Stream MCP server at `mcp.getstream.io`, the Stream API through the CLI, docs and SDK source from `getstream.io`, `getstream.github.io`, `github.com`, `raw.githubusercontent.com` and `pub.dev`. If your agent runs under egress restrictions, that list is what the allowlist has to cover, and a blocked endpoint will look like a broken skill rather than a blocked request.

## Limitations

- Snapshot data, verified 2026-11-05: 5,989 combined installs across 12 indexed listings; 21 GitHub stars; Apache-2.0; last pushed 2026-11-05. Counts drift over time.
- The star count is low for a vendor-owned repository. The authoritative documentation is the agent-skills site and each skill's reference page, not the README or the issue tracker.
- 12 listings against 11 SKILL.md directories: `stream-cli` carries 403 installs but has no skill directory of its own, because it names the CLI the other skills call.
- Coverage is uneven by design. Unity has no Feeds SDK and Unreal has Chat only; the pack says so, and an agent that promises otherwise is improvising.
- The plugins do not include the `getstream` CLI, so data queries, app configuration and `getstream docs` fail until it is installed separately.
- The Claude Code install path is `getstream@getstream`, meaning the plugin name and the marketplace name are the same string. `GetStream/agent-skills` is the marketplace source, not the plugin identifier, so keep the two separate when scripting the install.

## Related

- [Vercel Chat SDK Skills - Chat Bot Development Setup](/hermes/skills/catalog/vercel-chat-sdk-skills-setup)
- [Supabase Server Skill - Edge Function Auth Setup](/hermes/skills/catalog/supabase-server-skills-setup)
- [Agent Toolkit - 44 Skills for Coding Agents Setup](/hermes/skills/catalog/agent-toolkit-setup)

## Pro Tips

- Start with the router. Asking for `/stream` gets the right platform skill chosen for you, which is cheaper than installing all seven and guessing.
- Run `getstream init` before the first integration task. Auth, org and app selection and credentials are the three things every platform skill assumes and none of them can invent.
- Name the platform skill explicitly in your prompt for monorepos. A repo with a Next.js admin and a React Native app is exactly where automatic routing picks the wrong one.
- Read the compatibility entrypoints before deleting them. `stream-builder` and `stream-docs` still hold the larger install counts, so older tooling in a fleet is likely calling them.
- Judge the integration by a query, not a build. A green compile plus "list my channels" returning real data is the only combination that proves auth, permissions and SDK wiring at once.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
