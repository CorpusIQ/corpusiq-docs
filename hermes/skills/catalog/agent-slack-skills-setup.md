---
title: "Agent Slack Skills - Slack Automation CLI for AI Agents"
description: "stablyai/agent-slack: 5.1K combined installs. A Slack automation CLI that lets AI agents read, search, send, schedule and manage Slack."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/agent-slack-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-28"
tags: ["hermes skill", "agent skill", "skill setup", "slack", "automation", "cli"]
---

# Agent Slack Skills - Setup Guide

**Source:** [stablyai/agent-slack](https://www.skills.sh/stablyai/agent-slack) via skills.sh - 5.1K combined installs across 1 indexed listing; first seen Nov 28 2026 (morning sweep)

**GitHub:** [stablyai/agent-slack](https://github.com/stablyai/agent-slack) - 589 stars, MIT licence, branch main, last pushed 2026-09-07; ships the skill at `skills/agent-slack/SKILL.md` with `references/output.md` and `references/targets.md`.

**Category:** Slack automation - a TypeScript + Bun CLI giving AI agents read, search, write, channel, user, canvas, draft and scheduled-send access to Slack.

**Quality Tier:** 🟡 Yellow - the single indexed listing passes Gen Agent Trust Hub and Socket but carries a Snyk Warn; MIT licence.

stablyai/agent-slack is a Slack automation CLI for AI agents, published as a single indexed skill on skills.sh. Unlike a Markdown-only skill, it is a TypeScript and Bun command-line tool, so the skill directory wraps an installable binary. The README frames three guiding principles: token-efficient output (compact JSON with null and empty fields pruned so models consume results cheaply), zero-config authentication that works when Slack Desktop is installed, and human-in-the-loop flows for actions such as message compose.

Because the publisher has one indexed listing, the install surface is small: a single agent-slack skill whose SKILL.md delegates to the CLI. The command map spans reading messages and threads, searching messages and files, sending and scheduling messages, Slack-native drafts, channels, users, canvases, unreads, saved-for-later items and workflow triggers, with safe mode as an enforced human-in-the-loop switch.

## Installation

The README installs the CLI via Bun (recommended), npm, or a Nix flake:

```bash
# Bun (recommended)
curl -fsSL https://raw.githubusercontent.com/stablyai/agent-slack/main/install.sh | sh
```

```bash
# npm global (requires Node >= 22.5)
npm i -g agent-slack
```

```bash
# Nix flake
nix run github:stablyai/agent-slack
```

The agent skill installs through skills.sh (recommended) or manually from a clone of the repo:

```bash
npx skills add stablyai/agent-slack
```

```bash
bash ./scripts/install-skill.sh
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| agent-slack | 5,053 | Slack CLI for agents: read threads, history, unreads and later items; search messages and files; send, schedule, edit, delete and react to messages; manage canvases, channels, users and Slack-native drafts. |

This is the publisher's only indexed listing, so the table above is the complete install index.

## Why This Matters for Hermes Agents

This skill is a clean reference for wrapping an installable CLI as an agent skill: a small SKILL.md plus two reference files that document the output shape and target syntax, with the real behavior living in the binary. Builders wiring a Slack surface into a Hermes agent get read, write, search, channel and canvas coverage from one install instead of assembling several tools.

The token-efficient output design is directly relevant to agent context budgets: Slack data commands return compact JSON with null and empty fields pruned, which keeps model context cheap when the agent reads threads, search results or channel lists.

Safe mode is the most transferable idea here. Skill instructions such as "always use draft, never send" are guidance an agent can ignore, but AGENT_SLACK_SAFE_MODE enforces the rule at the tool level, so nothing posts without human review. That pattern is worth copying for any guardrail a builder wants to make un-ignorable.

Finally, the zero-config auth path (reading Slack Desktop local data with browser and token fallbacks) shows how an agent-facing tool can cut setup friction on developer machines, at the cost of relying on browser-session style authentication that some workspaces restrict.

## Usage

| You say | What happens |
|---|---|
| "What are my unread messages?" | `agent-slack unreads` lists unread messages across channels, DMs and threads. |
| "Find messages about smoke tests in #alerts" | `agent-slack search messages` filters channel history by query and time range. |
| "Send a status update to #general" | `agent-slack message send` posts it now, or schedules it with `--schedule-in`. |
| "Draft a message for me to review before it goes out" | `agent-slack message draft create` saves a Slack-native draft that appears in your Slack client. |
| "Summarize the thread at this Slack URL" | `agent-slack message list` fetches the thread root and all replies. |
| "Create a launch-plan canvas from this markdown file" | `agent-slack canvas create` builds a Slack canvas from a Markdown file. |
| "Open a DM with alice and bob" | `agent-slack user dm-open` starts a group DM with the named users. |

## Verification

The layout on branch main is `skills/agent-slack/SKILL.md`. Fetch it before install to review the skill instructions:

```bash
curl -sL https://raw.githubusercontent.com/stablyai/agent-slack/main/skills/agent-slack/SKILL.md
```

After a clone, confirm the skill directory and its reference files:

```bash
git clone --depth 1 https://github.com/stablyai/agent-slack.git /tmp/agent-slack
ls /tmp/agent-slack/skills/agent-slack/
head -3 /tmp/agent-slack/skills/agent-slack/SKILL.md
```

The skill directory holds SKILL.md plus `references/output.md` and `references/targets.md`. After installing the CLI, treat `agent-slack --help` and `agent-slack <command> --help` as authoritative for supported commands and flags, as the README advises.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-28) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| agent-slack | Pass | Pass | Warn |

This guide is Yellow because the single indexed listing carries a Snyk Warn while passing Gen Agent Trust Hub and Socket. All 1 of 1 indexed listings were sampled.

## Limitations

- Snapshot data, verified 2026-11-28: 5,053 combined installs across 1 indexed listing; 589 GitHub stars; MIT licence; last pushed 2026-09-07. Counts drift over time.
- Single indexed listing: agent-slack is the publisher's only skills.sh listing, so the security sample and the install index each cover exactly one skill.
- This is a CLI skill, not Markdown-only: the skill wraps an installable binary, and several commands act on live Slack data, so review the command map before granting an agent write access.
- Safe mode is opt-in: skill instructions such as "always use draft, never send" are guidance an agent can ignore unless AGENT_SLACK_SAFE_MODE is set, so enable it at the environment level for a hard guarantee.
- Several features use Slack's undocumented client endpoints (drafts, later, unreads, search) with browser-session auth; their behavior can change without notice, and Enterprise Grid workspaces may flag or restrict this style of session-token use.
- The `unreads` feature relies on the `client.counts` API, which the README notes may be restricted in some Enterprise Grid workspaces.

## Related

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Set `AGENT_SLACK_SAFE_MODE=1` in agent environments so nothing posts without human review, regardless of what the skill instructions say.
- Use channel-scoped search (`--channel ...`) for reliable results; the README notes it scans history and files and filters locally.
- Prefer `message draft` over `message send` for compose-only requests, and remember `message compose` is send-capable: in CI it skips the editor and sends immediately.
- Read `skills/agent-slack/SKILL.md` before install; the two reference files document the output shape and target syntax the agent relies on.
- Attached files auto-download to `~/.agent-slack/tmp/downloads/` on macOS, so agents can read snippets as `.txt` and images as `.png` directly from those local paths.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
