---
title: "Hermes Bot Mode (Desktop Plugin)"
description: "Bot Mode turns your Hermes agent profiles into a roster of named bots."
last_updated: "2026-11-18"
---

# Hermes Bot Mode (Desktop Plugin)

**Status:** Ships built into the Hermes desktop app and is on by default - no install needed. Announced Aug 16, 2026 by Nous Research.
**Official docs:** [hermes-agent.nousresearch.com/docs/user-guide/bot-mode](https://hermes-agent.nousresearch.com/docs/user-guide/bot-mode)
**Repo:** github.com/NousResearch/Hermes-Bot-Mode (MIT, JavaScript) - the original standalone plugin, now bundled into the app and archived upstream.
**Type:** Desktop UI over the profile primitive. No core patches, no background daemons, no extra storage.

Bot Mode turns your Hermes agent profiles into a roster of named bots. Each bot gets its own chat, avatar, personality, routine schedule, and the ability to message other bots. It appears as a **Bots** tab next to Sessions in the left sidebar, with a **Routines** tile docked beside the conversation while that tab is active.

## What it does

- **Bots tab** - left-side roster, one row per agent profile with avatar, latest message preview, timestamp. Click to enter its chat. The roster searches as you type, and right-click gives "open recent session".
- **Active now** - activity filter over the roster: the owner of the focused live turn, bots that wrote in the last 90 seconds, and bots with a recent worker heartbeat. A connected gateway alone does not mean a bot is working.
- **New Agent** - create a bot in seconds: name, title, description. Advanced mode opens the full profile config: clone an existing profile, pin a provider/model, write a custom SOUL.md, skip bundled skills, and tick the per-skill, per-toolset and per-MCP-server capabilities it needs. Static API keys are copied from the main profile by default; single-use OAuth logins are not, so the bot signs itself in with `hermes -p <name> auth add <provider>`. With more than one connection registered, a **Create on** picker creates the profile on that machine's backend without switching gateways.
- **Sections** - user-made folders (Clients, Team, whatever fits) as a second axis on the roster: drag a bot onto a section to file it, rename or reorder from the heading menu, and membership follows the bot to every desktop connected to that backend. Deleting a section never deletes bots - they return to Unassigned.
- **Group chats** (2-6 bots) - shared rooms where bots coordinate: up to three serial rounds of member turns, @mentions pull bots in, @user escalates to a human with a "needs you" badge, and hard caps (10 messages per send, 3 rounds) stop runaway loops.
- **Bot-to-bot messaging** - every bot has a persistent Bot Chat. Bots message each other with attribution, and their SOUL.md teaches them the protocol. Typing `/new` inside a Bot Chat reroutes to `/compact`, so the standing conversation never forks into a scratch session.
- **Routines** - recurring tasks per bot, backed by standard Hermes cron and namespaced `[bot:<name>] <routine>`. Runs land in the bot's own chat history.
- **Avatars** - blob faces by default (a deterministic soft-body face drawn from the bot's name, with Randomize and Lock face), geometric faces (7 shapes × 10 colors), uploaded images, AI-generated portraits when an image backend is configured, or a pixel pet from the petdex gallery (`hermes pets`) that bounces while the bot works.
- **Hide a bot** - right-click a roster row to take a bot you do not use out of the roster and the Active-now strip. Hiding is display-only: @mentions still resolve, group memberships are untouched, and its routines keep running.

## How it works

A bot **is** a Hermes profile: isolated config, memory, skills, credentials, and chat history under `~/.hermes/profiles/<name>/`. The plugin is a UI over that primitive:

- Chats and sessions use profile-aware navigation
- Creation and editing ride the `profiles.*` gateway RPCs
- Routines are plain Hermes cron jobs, so they show up in `hermes cron list`
- Bot-to-bot messages are real CLI handoffs between profiles - the same agent `hermes -p <bot> chat` opens - and across connected machines they route through the Desktop relay, or through a registered peer (`hermes peer`) when no desktop is open to act as the courier

## Why it matters for operators

Bot Mode is the first mainstream implementation of multi-agent operations inside a desktop app. A business can run a roster of specialized agents: one for email, one for finance questions, one for social, each with its own identity, memory, and credentials, coordinating on shared rooms. This is the agent-team model applied to operations, and it is the same pattern CorpusIQ's governed intelligence layer feeds: named agents with scoped identity and data access.

## Install

Nothing to install. Open the Hermes desktop app and use the **Bots** tab; Bot Mode is on by default. From a terminal, `hermes -p <bot> chat` opens the same agent, and that bot's routines appear in `hermes cron list`. Bots live under `~/.hermes/profiles/<name>/`, so config, memory, skills, and credentials stay where they always were.
