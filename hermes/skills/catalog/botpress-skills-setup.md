---
title: "Botpress Skills - Agent Development Kit (ADK) Setup"
description: "Setup guide for botpress/skills - 11.2K combined installs. Official Botpress ADK skills for building, debugging, and evaluating agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/botpress-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-10"
tags: ["hermes skill", "agent skill", "skill setup", "botpress", "agent development", "chatbots", "typescript"]
---

# Botpress Skills - Setup Guide

**Source:** [botpress/skills](https://www.skills.sh/botpress/skills) via skills.sh - 11.2K combined installs across 7 indexed listings; first seen Oct 9, 2026 (extended-query probe)
**GitHub:** [botpress/skills](https://github.com/botpress/skills) (12 stars, MIT; default branch master, pushed 2026-10-02; skills at `skills/<name>/SKILL.md`)
**Category:** Agent Development / Chatbots
**Quality Tier:** 🟡 Beta - official Botpress org; MIT; small repo (12 stars); all sampled verdicts Pass

Botpress Skills is the official Botpress collection for AI coding agents building with the Botpress Agent Development Kit (ADK), a convention-based TypeScript framework where file structure maps directly to bot behavior. Seven indexed skills span the core ADK framework, frontend integration, evals, debugging, documentation, the dev console, and integrations, totaling 11.2K combined installs. The skills follow the Agent Skills format and ship as packaged instructions plus reference documentation, with ten Claude Code slash commands as quick entry points.

Start with the adk skill, which covers Actions, Tools, Workflows, Conversations, and Triggers, plus data storage and the Zai LLM utility library. From there, adk-frontend handles the client-side story, adk-evals and adk-debugger cover testing and diagnosis, and adk-docs keeps project documentation in sync.

---

## Installation

Install the core skill with the skills.sh CLI:

```bash
npx skills add botpress/skills --skill adk
```

Claude Code users can install the plugin, which adds all skills and the slash commands:

```bash
/plugin marketplace add botpress/skills
/plugin install adk@botpress-skills
```

Skills are automatically available once installed; the agent picks them up when relevant tasks appear.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| adk | 2,034 | Core ADK framework: Actions, Tools, Workflows, Conversations, Triggers, Zai, storage |
| adk-frontend | 1,624 | Frontend integration: auth, @botpress/client, type-safe action calls |
| adk-evals | 1,605 | Writing and running evals with assertion types and CI-friendly workflows |
| adk-debugger | 1,599 | Systematic debugging with traces, logs, and an 8-step debug loop |
| adk-docs | 1,589 | Creating, reviewing, and syncing documentation for your bot |
| adk-dev-console | 1,556 | Working with the ADK developer console |
| adk-integrations | 1,212 | Discovering, adding, and configuring integrations |

## Why This Matters for Hermes Agents

Agents building on the Botpress ADK face a convention-driven TypeScript framework where folder structure maps to bot behavior, so small mistakes in Actions, Tools, or Workflows are hard to spot without help. The debugging and evals skills give a coding agent the vocabulary to read traces, classify failures, and convert them into automated conversation tests. The frontend skill matters for full-stack work: it covers @botpress/client setup, authentication, and generated types so a React or Next.js UI does not need hand-written glue. Documentation skills keep project docs in sync with a codebase that changes fast. For teams standardizing on Botpress, installing this suite means the agent already knows the framework's idioms instead of improvising from stale training data.

## Usage

| You say | What happens |
|---|---|
| Create an Action that fetches user data | The adk skill applies ADK conventions for strongly-typed Actions |
| How do I use Zai to extract structured data? | The adk skill covers Zai operations: extract, check, label, and summarize |
| My bot is not responding, how do I debug this? | adk-debugger follows its 8-step loop with adk check, adk logs, and adk traces |
| Write an eval that tests my createTicket tool | adk-evals walks the eval format, assertion types, and the write-test-iterate loop |
| Call my bot's actions from a Next.js frontend | adk-frontend covers @botpress/client, auth, and type generation |
| Check whether my docs match the code | adk-docs reviews and syncs project documentation |
| Add a Slack integration to my bot | The adk skill plus the /adk-integration command path guides discovery and configuration |

## Verification

Confirm the skills are registered:

```bash
npx skills list | grep adk
```

Review the core skill before installing it - this raw file comes from the repo's default branch (master):

```bash
curl -sL https://raw.githubusercontent.com/botpress/skills/master/skills/adk/SKILL.md | head -60
```

## Security

skills.sh verdicts for sampled skills (verified Oct 10, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| adk | Pass | Pass | Pass |
| adk-frontend | Pass | Warn | Pass |
| adk-evals | Pass | Pass | Pass |

## Limitations

- Small repo: 12 GitHub stars, so fewer outside eyes on each change.
- The catalog rates this suite Beta rather than Production.
- adk-frontend carries a Socket Warn among the sampled verdicts; adk-dev-console and adk-integrations were outside the sampled set.
- Slash commands are Claude Code-only; other agents get the skills without the command wrappers.
- The README documents five skills in depth; adk-dev-console and adk-integrations appear as indexed listings without full README sections yet.


- Snapshot data, verified Oct 10, 2026: 11,219 combined installs across 7 indexed listings; 12 GitHub stars; MIT; last pushed 2026-10-02. Counts drift over time.

## Related

- [Assistant UI Skills - AI Chat Interface Dev Suite Setup](/hermes/skills/catalog/assistant-ui-skills-setup) - chat interface components for agent frontends
- [CopilotKit Skills - Agent Frontend Stack Setup](/hermes/skills/catalog/copilotkit-copilotkit-skills-setup) - in-app agent frontend tooling
- [LangChain Agent Skills - Memory, RAG, Persistence & Middleware Setup](/hermes/skills/catalog/langchain-skills-setup) - adjacent agent-building suite for the LangChain ecosystem
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install adk first; every other skill assumes the core conventions it documents.
- In Claude Code, slash commands like /adk-debug and /adk-eval are faster entry points than describing the task.
- Write evals early with adk-evals and wire them into CI before the bot grows.
- When a bot misbehaves, start from traces and logs (adk check, adk logs, adk traces) before changing code.
- Skills include references/ directories; ask the agent to read the relevant reference file when you need depth.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
