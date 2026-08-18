---
title: "Hermes Bot Mode (Desktop Plugin)"
description: "Bot Mode turns your Hermes agent profiles into a roster of named bots. Each bot gets its own chat, avatar, personality, routine schedule, and the abilit..."
---

# Hermes Bot Mode (Desktop Plugin)

**Status:** Early beta — announced Aug 16, 2026 by Nous Research
**Repo:** github.com/NousResearch/Hermes-Bot-Mode (MIT, JavaScript)
**Type:** Desktop-app plugin. No core patches, no background daemons, no extra storage.

Bot Mode turns your Hermes agent profiles into a roster of named bots. Each bot gets its own chat, avatar, personality, routine schedule, and the ability to message other bots.

## What it does

- **Bots pane** — left-side roster, one row per agent profile with avatar, latest message preview, timestamp. Click to enter its chat. Sessions view filters a profile's 200 most recent stored conversations.
- **Active now** — presence strip showing every bot currently working (gateway-busy profile plus any bot that wrote in the last 90 seconds).
- **New Agent** — create a bot in seconds: name, title, description. Advanced mode opens the full profile config: clone an existing profile, pin a provider/model, write a custom SOUL.md, skip bundled skills.
- **Groups** — organize the roster into labeled sections. Group chats (2-6 bots) are shared rooms where bots coordinate: @mentions pull bots in, @user escalates to a human with a "needs you" badge, hard caps (10 messages per turn, 3 rounds) stop runaway loops.
- **Bot-to-bot messaging** — every bot has a persistent Bot Chat. Bots message each other with attribution, and their SOUL.md teaches them the protocol.
- **Routines** — recurring tasks per bot, backed by standard Hermes cron. Runs land in the bot's own chat history.
- **Avatars** — geometric faces, uploaded images, AI-generated portraits, or pixel pets that bounce while the bot works.

## How it works

A bot **is** a Hermes profile: isolated config, memory, skills, credentials, and chat history under `~/.hermes/profiles/<name>/`. The plugin is a UI over that primitive:

- Chats and sessions use profile-aware navigation
- Creation and editing ride the `profiles.*` gateway RPCs
- Routines are plain Hermes cron jobs namespaced `[bot:<name>] <routine>`
- Bot-to-bot messages are real CLI handoffs: `hermes -p <bot> chat --in ~ -c "Bot Chat" -Q -q "Message from ..."`

## Why it matters for operators

Bot Mode is the first mainstream implementation of multi-agent operations inside a desktop app. A business can run a roster of specialized agents: one for email, one for finance questions, one for social, each with its own identity, memory, and credentials, coordinating on shared rooms. This is the agent-team model applied to operations, and it is the same pattern CorpusIQ's governed intelligence layer feeds: named agents with scoped identity and data access.

## Install

Installs where the Hermes Desktop app runs. See the repo README for current install steps (early beta, plugin installation path).
