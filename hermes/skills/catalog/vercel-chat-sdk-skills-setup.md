---
title: "Vercel Chat SDK Skills - Chat Bot Development Setup"
description: "vercel/chat: 6.1K combined installs. Official Chat SDK skills for building Slack, Teams, Discord and Telegram bots from one TypeScript codebase."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/vercel-chat-sdk-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-30"
tags: ["hermes skill", "agent skill", "skill setup", "chat bots", "typescript", "slack", "adapters"]
---

# Vercel Chat SDK Skills - Setup Guide

**Source:** [vercel/chat](https://www.skills.sh/vercel/chat) via skills.sh - 6.1K combined installs across 3 indexed listings; first seen 2026-10-30 (morning sweep)

**GitHub:** [vercel/chat](https://github.com/vercel/chat) - 2,434 stars, MIT License, branch main, last pushed 2026-10-28; 6 `SKILL.md` files across four skill directories (`skills/chat/`, `.agents/skills/add-adapter/`, `.agents/skills/technical-writer/`, `apps/docs/public/.well-known/agent-skills/chat-sdk/`), of which four files are byte-identical copies of the same `chat-sdk` skill, and `.claude` is a symlink to `.agents`

**Category:** Chat bot SDKs, adapters and Slack integration for agents

**Quality Tier:** 🟢 Green - all sampled skills Pass on all three auditors; MIT-licensed TypeScript SDK guidance, adapter authoring and documentation standards

Chat SDK is Vercel's unified TypeScript layer for chat bots: one `Chat` instance, a map of platform adapters, and the same handlers for mentions, direct messages, reactions, slash commands, cards, modals and file uploads whether the surface is Slack, Microsoft Teams, Google Chat, Discord, Telegram, GitHub, Linear or WhatsApp. The repository is the SDK itself plus the skill suite that teaches a coding agent how to use it, indexed on skills.sh as three listings.

What makes the suite worth installing is that the guidance ships with the package it describes. The `chat-sdk` skill does not paraphrase the website; it points the agent at the documentation bundled inside the `chat` npm package (`node_modules/chat/docs`, `node_modules/chat/resources`, `resources/templates.json`) and at the published page index, so an agent reads the docs that match the installed version (chat 4.43.0 at this snapshot) instead of a page that has drifted. The other two listings, `add-adapter` and `technical-writer`, are the skills Vercel uses in this repo to add third-party adapters to the catalog and to keep prose honest, and both are marked internal in their frontmatter.

## Installation

The README's agent route is one command. It installs the Chat SDK skill so the agent knows the SDK APIs, adapter patterns and project conventions before it writes code:

```bash
npx skills add vercel/chat
```

Vercel also publishes a wider plugin bundle that carries the Chat SDK skill alongside specialist agents and slash commands:

```bash
npx plugins add vercel/vercel-plugin
```

The skill teaches an agent to write Chat SDK code, and the SDK is what makes that code run. Both come straight from the README:

```bash
npm i chat
npm install @chat-adapter/slack @chat-adapter/teams @chat-adapter/gchat
```

A bot project can be scaffolded without prompts, which is the route the `chat-sdk` skill tells an agent to take:

```bash
npx create-chat-sdk@latest my-bot
```

For this Hermes profile the durable route is a directory copy, because the profile's skills tree is the one Hermes reads. Copy `skills/chat/` from a clone into `~/.hermes/profiles/corpusiq/skills/chat-sdk/` so the directory name matches the frontmatter `name: chat-sdk`. For the two repo-authoring skills, copy `.agents/skills/add-adapter/` and `.agents/skills/technical-writer/` whole rather than the markdown alone: both carry `references/`, and `add-adapter` also ships `assets/adapter.mdx` and `assets/adapter-state.mdx` templates that its workflow tells the agent to fill in.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| chat-sdk | 5,433 | Building multi-platform chat bots on the `chat` package: scaffold with create-chat-sdk, then handle mentions, DMs, subscribed threads, reactions, slash commands, cards, modals, files and AI streaming across Slack, Teams, Google Chat, Discord, Telegram, GitHub, Linear and WhatsApp, set up webhook routes and multi-adapter bots, or write a custom adapter or state adapter. |
| add-adapter | 682 | Listing a vendor-official or community adapter in the Chat SDK catalog and docs: the `@chat-adapter/catalog` entry with listing metadata and capabilities, the docs MDX page under `apps/docs/content/adapters/`, `meta.json` and a changeset, following its own sourcing rules and page-layout reference. |

The remaining 1 indexed listings range from 3 to 3 installs.

## Why This Matters for Hermes Agents

Chat bot work is where an agent's confidence most often outruns its knowledge, because every platform has its own vocabulary for the same event and the SDK hides just enough of that difference to make invented API calls look plausible. A skill that names the actual handlers, the adapter factory pattern and the state adapter contract removes most of that failure class before the first file is written.

The bundled-docs route is the second useful property. Because the skill tells the agent to inspect `node_modules/chat/docs` and `node_modules/chat/resources` first and to stop if those paths are absent, it fails honestly on a project where the SDK is missing instead of writing imports for a package that is not installed. That is the same discipline a Hermes cron or subagent needs when it wakes up without conversational context.

The adapter catalog package is also worth knowing about independently of the bot code. `@chat-adapter/catalog` is dependency-free and imports no adapter implementation, so an agent can answer which adapters exist, which capabilities they support and which environment variables they need, without installing anything or holding a credential. For a setup flow or a diagnostic, that is a lookup rather than a guess.

Finally, the two repo-authoring skills are a good model for how a project keeps its own agent instructions in tree. `add-adapter` chains to `technical-writer` before any prose is written and requires a changeset with the catalog entry, which is the kind of enforced order that keeps a growing adapter list consistent.

## Usage

| You say | What happens |
|---|---|
| "Scaffold a Slack bot for our support team" | The skill runs the non-interactive scaffolder, then works inside the generated project: `Chat` configuration, webhook route, `.env.example` and adapter dependencies, with handlers for mentions, DMs and subscribed threads written against the real SDK surface. |
| "It should only answer in threads where it was mentioned" | The skill composes `onNewMention` with `thread.subscribe()` and `onSubscribedMessage`, so follow-up handling is driven by thread subscription state held in the configured state adapter rather than in process memory. |
| "Port our Teams bot to Discord without a rewrite" | The handlers stay on one `Chat` instance and the adapter map changes, because mentions, messages, reactions, cards and file uploads are normalized across platforms. |
| "Stream the model's answer into Slack instead of posting twice" | The skill uses the SDK's AI streaming path (native Slack streaming, Telegram draft previews, post and edit fallback) and can check streaming support for an adapter through the catalog before promising it. |
| "We wrote a Zulip adapter, how do we get it listed?" | The add-adapter skill produces the catalog entry with package, maintainer and capability metadata, the docs MDX page under the vendor-official or community directory, `meta.json` and a changeset, with `technical-writer` loaded first for the prose rules. |
| "Where do the Slack adapter's env vars come from?" | The catalog answers it offline: `listAdapters`, `getSecretEnvVars` and `getFeatureSupport` return package names, peer dependencies and required variables, including which ones are secrets, before any adapter is installed. |
| "Write the getting-started page for our fork" | `technical-writer` applies the repo's editorial standards, content patterns and technical-verification rules, so code samples are checked against the shipped docs rather than written from memory. |

## Verification

Both raw paths below returned 200 on branch main when this guide was written on 2026-10-30, and so did `.agents/skills/technical-writer/SKILL.md` and `apps/docs/public/.well-known/agent-skills/chat-sdk/SKILL.md`:

```bash
curl -sL -o /dev/null -w "%{http_code} chat-sdk\n" \
  https://raw.githubusercontent.com/vercel/chat/main/skills/chat/SKILL.md
curl -sL -o /dev/null -w "%{http_code} add-adapter\n" \
  https://raw.githubusercontent.com/vercel/chat/main/.agents/skills/add-adapter/SKILL.md
```

Expect `200` twice. Read the `chat-sdk` file before installing it, because its frontmatter description is the whole routing contract: one sentence naming the scaffolder, the nine platforms, the event types and the custom-adapter case. Those are the phrases that decide when an agent reaches for this skill at all.

After a copy lands in the profile, confirm the frontmatter and that the supporting directories came along:

```bash
head -5 ~/.hermes/profiles/corpusiq/skills/chat-sdk/SKILL.md
ls ~/.hermes/profiles/corpusiq/skills/add-adapter/
```

A good copy shows `name: chat-sdk` and a `description:` on the second line, and the directory listing shows `SKILL.md`, `references/` and `assets/` for `add-adapter`. The published agent-skills endpoint has its own integrity check: `apps/docs/public/.well-known/agent-skills/index.json` in the repo records a sha256 digest for the served copy of the skill, so a digest mismatch on that file means you are looking at a different revision than the site publishes.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-30) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| chat-sdk | Pass | Pass | Pass |
| add-adapter | n/a | n/a | n/a |
| technical-writer | n/a | n/a | n/a |

Only `chat-sdk` carries verdicts; the other two listings were not sampled by any of the three auditors, so the `n/a` cells are missing coverage rather than a clean result, and they deserve a manual read before install. This is markdown-only guidance: none of the three skills ships a script, a hook or an executable, and the reviewable surface is what the skill instructs an agent to run.

The risk in this collection is operational rather than supply chain. A bot built with these skills holds platform credentials (a Slack bot token, an app signing secret, a Teams or Google Chat registration) and a state store, and the commands it runs reach live chat platforms and Vercel deployments. Keep those credentials in project env files that are already gitignored, as the scaffolder's `.env.example` implies, and never paste a token into a prompt. Because `add-adapter` and `technical-writer` are marked internal, they also assume a checkout of this repository and will point an agent at paths that do not exist elsewhere.

## Limitations

- Snapshot data, verified 2026-10-30: 6,118 combined installs across 3 indexed listings; 2,434 GitHub stars; MIT License; last pushed 2026-10-28. Counts drift over time.
- The index and the tree disagree in both directions. skills.sh indexes three listings, while the checkout holds 6 `SKILL.md` files in four directories: `chat-sdk` exists as four byte-identical copies (`skills/chat/`, the `.well-known/agent-skills` publication, and two inside the `create-chat-sdk` scaffolding template), so a directory named `chat` contains a skill named `chat-sdk`. Only `skills/chat/` is the working copy an editor should touch.
- `add-adapter` and `technical-writer` declare `metadata: internal: true`. They are written for contributing to vercel/chat itself (catalog entries, docs pages, changesets, PR prose) and reference repository paths, so installing them into a general profile mostly adds routing noise.
- Entry points differ by audience. The README sends coding agents to `npx skills add vercel/chat`, ships a separate `npx plugins add vercel/vercel-plugin` bundle, and publishes exactly one skill through `/.well-known/agent-skills/index.json` (chat-sdk, with a sha256 digest). Those three routes can be at different revisions of the same skill.
- The skills carry no install commands or tooling of their own, so everything they describe needs a live environment: the npm packages, a chat platform app with webhooks pointed at your deployment, and a state store such as Redis for thread subscriptions. Nothing here runs offline against a fixture.

## Related

- [Vercel AI SDK Skills - TypeScript AI Development Setup](/hermes/skills/catalog/vercel-ai-skills-setup)
- [Better Icons - Icon Search Skill Setup](/hermes/skills/catalog/better-auth-better-icons-setup)
- [Lavish AXI - Agent Experience Interface Setup](/hermes/skills/catalog/lavish-axi-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the skill before the SDK, then have the agent read `node_modules/chat/docs` in the project. The skill is written to check for those paths and to say the package is missing, which turns a silent wrong import into a clear next step.
- For a multi-platform bot, start with `@chat-adapter/catalog` rather than trial and error. Capability and env-var lookups are static data, so you can confirm that streaming or modals exist on the target platform before writing a handler for them.
- Copy `skills/chat/` and rename the directory to `chat-sdk` in the profile. Leaving it as `chat` creates a skill whose folder and frontmatter name disagree, which some loaders surface as a duplicate or a skipped skill.
- Treat the two internal skills as references worth reading, not defaults worth installing. `technical-writer`'s three reference files are a compact editorial and verification standard that reads well even outside this repo.
- Pair these skills with an AI SDK skill when the bot calls a model. The bundled guides route tool definitions through the AI SDK, so the two skill sets cover the transport and the model layer without overlap.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
