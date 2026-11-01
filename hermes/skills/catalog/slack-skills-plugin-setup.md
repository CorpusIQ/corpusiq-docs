---
title: "Slack Skills Plugin - MCP Plus Nine Slack Skills"
description: "slackapi/slack-skills-plugin: 15.2K combined installs. Nine Slack skills plus the hosted Slack MCP server for search, messaging and app builds."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/slack-skills-plugin-setup/"
robots: "index,follow"
last_updated: "2026-11-01"
tags: ["hermes skill", "agent skill", "skill setup", "slack", "mcp", "app development"]
---

# Slack Skills Plugin - Setup Guide

**Source:** [slackapi/slack-skills-plugin](https://www.skills.sh/slackapi/slack-skills-plugin) via skills.sh - 15.2K combined installs across 9 indexed listings; first seen 2026-11-01 (morning sweep)

**GitHub:** [slackapi/slack-skills-plugin](https://github.com/slackapi/slack-skills-plugin) - 163 stars, MIT, branch main, last pushed 2026-11-01; 9 `SKILL.md` files, one per directory under `skills/`, wrapped in a full plugin repository that also carries `commands/`, `scripts/`, `tests/`, `package.json`, `pyproject.toml`, `.mcp.json` and per-host plugin manifests

**Category:** Slack work for agents: message composition, workspace search, Web API calls, Block Kit, and building, testing and deploying Slack apps

**Quality Tier:** 🟡 Yellow - two of the three sampled listings carry a Snyk Warn (code W012) on slack-api and slack-docs, while every Gen Agent Trust Hub and Socket verdict is a Pass; the repository itself is MIT

This is an official Slack package rather than a third-party skill set, and it is shaped like a plugin: one hosted MCP server that supplies the tools, plus nine skills that tell an agent when and how to use them. The MCP side covers search, messaging, canvases and user lookups. The skills side splits cleanly into two audiences. Four skills are for using Slack (`slack-messaging`, `slack-search`, `slack-api`, `slack-docs`) and five are for building on it (`slack-cli`, `create-slack-app`, `test-slack-app`, `deploy-slack-app`, `block-kit`).

The instructional style is consistent across the pack, and it is the reason the pack is worth reading even without installing it. Every developer skill begins with a source-of-truth rule: method names, scopes, block types and platform behaviour come from a live `docs.slack.dev` page fetched at the moment of use, never from memory, and a page that fails to fetch is reported as a failure rather than filled in from recall. `slack-api` adds an execution posture on top of that: read-only methods may be run directly, while `chat.postMessage`, any delete or archive, and everything under `admin.*` must be prepared and confirmed before execution.

## Installation

The README documents four install routes, three of which are host marketplaces that carry the MCP server, the skills and five slash commands together:

```bash
# Claude Code
/plugin install slack@claude-plugins-official

# Cursor
/add-plugin slack

# Codex
codex plugin marketplace add slackapi/slack-skills-plugin
codex plugin add slack@slack
```

The fourth route is the skills CLI, which the README recommends for any other agent and documents as agent-agnostic:

```bash
npx skills add slackapi/slack-skills-plugin -y -a <agent>
```

The README lists `hermes-agent` among the supported agent identifiers, so the install is:

```bash
npx skills add slackapi/slack-skills-plugin -y -a hermes-agent
```

Drop `-y` to pick skills from a list, pass `-s <skill>` to name them, and add `-g` for a user-level install instead of a project one. The `-y` flag installs everything without prompting, which is what most operators want here because the skills reference each other.

One consequence needs stating plainly, because the README says it in one line and it changes what you get: the skills CLI path carries the skills only. No slash commands, and no MCP server. `slack-messaging` and `slack-search` are written around tool names that only exist once the Slack MCP server is connected, so on the CLI path you have procedure without callable tools until you wire the hosted server into your MCP client yourself. The repository ships a `.mcp.json` that shows the server entry the plugin route uses, which is the file to read when doing that wiring. Treat that wiring step as ours, not theirs: the README documents it for Claude Code, Cursor and Codex, and not for Hermes.

The README's own limitation is worth repeating before you start: a workspace admin has to approve MCP integration before OAuth will succeed, so a personal workspace that you administer is the easy case and a corporate one may need a ticket.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| slack-api | 3,277 | Discovering the right Web API method, reading its scopes and token type, and calling it with correct cursor pagination and rate-limit handling. |
| slack-messaging | 3,261 | Composing messages through the MCP message tools: markdown formatting, structure, thread etiquette, reactions and scheduling. |
| slack-docs | 3,233 | Finding and reading docs.slack.dev pages as clean markdown, using the docs search API and the per-page `.md` surface. |
| slack-search | 3,194 | Locating messages, files, channels and people with search modifiers such as `in:`, `from:`, `before:` and file-type filters. |
| block-kit | 566 | Building and validating Block Kit layouts for messages, modals and Home tabs, with `blocks.validate` as the check. |
| slack-cli | 530 | Detecting the public Slack CLI, then logging in, running, deploying and calling Web API methods from the terminal. |
| create-slack-app | 510 | Scaffolding a new Bolt for JavaScript or Python app from a template, including workspace selection and authentication. |
| test-slack-app | 476 | Running an app in a developer sandbox or Free Team and confirming that its commands, events and modals respond. |
| deploy-slack-app | 141 | Deploying a Socket Mode app to Railway or Heroku through the CLI deploy hook, as a separate always-on app. |

The index and the tree agree: nine listings, nine directories. The counts fall into two bands that look like two waves of adoption. The four using-Slack skills sit between 3,194 and 3,277, effectively tied. The five building-on-Slack skills run from 141 to 566, an order of magnitude lower, which fits: far more agents are asked to read and write messages than to scaffold a Bolt app.

## Why This Matters for Hermes Agents

Slack is where a large share of an organisation's decisions, approvals and incident chatter actually live, and it is one of the few surfaces where an agent with read access can answer "what was decided and by whom" without a data pipeline. The search skill is the entry point for that: it documents the modifier vocabulary (`in:`, `from:`, `before:`, `has:`, `type:`) and, more usefully, the strategy of starting broad, then narrowing, and running several searches rather than one.

The developer skills solve a different problem: agents are bad at APIs they cannot see. Slack has hundreds of methods named in dot notation, opaque cursors rather than page numbers, per-method scopes and rate tiers, and a deprecation list that includes methods still widely present in old tutorials. The pack's answer is procedural rather than encyclopaedic, which is the right shape: fetch the live index, read the method's own page, then call it, and check the top-level `ok` boolean on every response instead of trusting the HTTP status.

The execution posture is the part to keep if you keep nothing else. `slack-api` distinguishes read-only methods from state-changing ones and requires confirmation before the second group, which includes every message send, delete and archive, and all `admin.*` calls. An agent that can post to a workspace is an agent that can page a company at 3am, so an explicit confirm-before-write rule is a control worth preserving rather than a suggestion to be optimised away.

The build loop is coherent end to end: create, run, test, deploy, with each skill handing to the next and the test skill insisting on a sandbox or Free Team rather than a workspace with real people in it. For an operator who wants an agent to stand up an internal Slack app, that is a full path with the risky steps named.

The cost is coupling. Two of the nine skills are only useful with the MCP server connected, most of the build skills are only useful with the Slack CLI installed and a workspace you administer, and the deploy skill does not cover Request URL apps at all.

## Usage

| You say | What happens |
|---|---|
| "What did the team decide about the pricing page last week" | `slack-search` runs a broad search, then narrows with `in:` and `after:` modifiers, and reads the matching threads in context rather than quoting snippets. |
| "Post in #general that the deploy finished" | `slack-messaging` formats the message as standard markdown for the MCP send tool, and `slack-api` requires confirmation before the write if the raw method is used instead. |
| "Which method lists a channel's members, and what scopes do I need" | `slack-api` looks the method up on its live doc page, names the required scopes and token type, then calls it if asked. |
| "Build a feedback modal with a rating select and a comment box" | `block-kit` picks the surface, reads the block schemas from the live docs, generates the JSON, and validates it with `blocks.validate`. |
| "Scaffold a Bolt for Python app and run it locally" | `create-slack-app` picks a sandbox or Free Team, scaffolds from a template, and `slack-cli` handles login and `slack run`. |
| "Get this app off my laptop so it keeps running" | `deploy-slack-app` confirms the app uses Socket Mode, then deploys to Railway or Heroku through the CLI deploy hook with tokens injected at run time. |
| "How do I set up Socket Mode" | `slack-docs` searches the guides category, fetches the page as markdown, and answers from that page with its source URL kept for citation. |

## Verification

The raw path for the Web API skill returned HTTP 200 on branch main when this guide was written on 2026-11-01:

```bash
curl -sL -o /dev/null -w "%{http_code} slack-api\n" \
  https://raw.githubusercontent.com/slackapi/slack-skills-plugin/main/skills/slack-api/SKILL.md
```

Expect `200`. After a shallow clone, confirm that all nine skills arrived and that the MCP configuration came with them:

```bash
git clone --depth 1 https://github.com/slackapi/slack-skills-plugin.git /tmp/slack-skills-plugin
ls /tmp/slack-skills-plugin/skills
find /tmp/slack-skills-plugin/skills -name SKILL.md | wc -l
```

The count should be 9, and the listing should show `slack-api`, `slack-messaging`, `slack-docs`, `slack-search`, `block-kit`, `slack-cli`, `create-slack-app`, `test-slack-app` and `deploy-slack-app`. The clone root also carries `.mcp.json`, which is the server entry the plugin routes use and the file to read when wiring the same server into an MCP client that the plugin does not support. If your MCP client shows no `slack_` tools after installing the skills, the skills landed but the server did not; that is expected on the CLI route.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-01) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| slack-api | Pass | Pass | Warn |
| slack-messaging | Pass | Pass | Pass |
| slack-docs | Pass | Pass | Warn |

The verdicts describe the skills, and the skills are the smaller half of the risk here. This repository ships a `package.json`, a `pyproject.toml`, a `Makefile`, CI workflows, a `scripts/` directory and a test suite, and the plugin routes configure an MCP server that reaches into a live workspace. The Snyk Warns, code W012 on `slack-api` and on `slack-docs`, are consistent with the instruction-level pattern both skills share: fetch a URL and act on what it returns. That is the documented design, not an accident, but it does mean the agent's trust boundary extends to `docs.slack.dev` content, so a compromised or spoofed docs response is inside the model's context.

The real attack surface is the OAuth grant. Once the server is connected, an agent holding that token can search private channels and DMs if the consenting user granted it, read canvases, and post as that user. Scope the grant to what the task needs, prefer a dedicated workspace for agent work rather than a production one, and remember that `slack_search_public_and_private` exists as a separate tool precisely because private search needs explicit consent.

Two controls inside the pack are worth keeping unmodified. `slack-api` requires reads to run freely and writes to be confirmed, naming `chat.postMessage`, the update and delete variants, any `*.delete` or `*.archive` or `*.kick`, and all `admin.*`. `test-slack-app` refuses to treat a workspace with real coworkers as a test target and asks the developer to confirm which workspace the CLI is pointed at, because the CLI itself cannot tell a sandbox from production. Both are the kind of guardrail that survives only if the operator notices when it is missing.

One dependency note: the `deploy-slack-app` path passes bot and app tokens into a provider deploy script at run time rather than storing them, which is a good pattern, and it depends on the CLI's deploy hook having already installed the deployed app. Do not rewrite that ordering.

## Limitations

- Snapshot data, verified 2026-11-01: 15,188 combined installs across 9 indexed listings; 163 GitHub stars; MIT; last pushed 2026-11-01. Counts drift over time.
- The index lists 9 skills and the tree holds 9 directories, so there is no index-versus-tree drift here.
- Install counts split into two clusters: four using-Slack skills at 3,194 to 3,277 and five building-on-Slack skills at 141 to 566. Ordering inside each cluster says little.
- The skills CLI route installs skills only. No slash commands and no MCP server, so the messaging and search skills have nothing to call until the hosted Slack MCP server is wired into your client separately.
- The skill bodies are written for Claude Code conventions and reference tool names an agent may not have: `AskUserQuestion`, `WebFetch`, `EnterPlanMode`, `$0` argument hints and `/slack:` slash commands. A Hermes operator has to map those onto its own tools, and an agent that takes them literally will stall.
- `deploy-slack-app` covers Socket Mode apps only. Request URL apps are explicitly out of scope in the current version, and the skill points at issue 172 rather than pretending otherwise.
- Workspace admin approval is required before MCP authentication succeeds, which makes this pack unsuitable for a workspace you do not control.

## Related

- [Slack CLI Skill - Agent-Driven Workspace Automation Setup](/hermes/skills/catalog/paymog-slack-cli-setup)
- [Composio - SDK Monorepo and Agent Toolkit Setup Guide](/hermes/skills/catalog/composiohq-composio-setup)
- [Native Mcp Setup](/hermes/skills/catalog/native-mcp-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the skills and wire the MCP server as two separate steps, and verify the second one before blaming the first. `slack-messaging` failing to send is almost always a missing `slack_` tool, not a formatting problem.
- Use `slack-docs` for any factual Slack question rather than letting the agent answer from memory. The skill's whole premise is that the platform changes faster than any stored summary, and it keeps the source URL for citation.
- Keep the confirm-before-write posture and extend it. The pack requires confirmation for message sends and admin calls; add reactions, canvas edits and channel creation to the same list if your workspace is large.
- Point the build skills at a sandbox or a Free Team you created for the purpose. `test-slack-app` will ask, but the CLI cannot verify the answer, so the operator is the control.
- Pass `-s` and install only the skills you need if context is tight. Four skills cover reading and writing messages and docs; the other five are for app development and are dead weight in a support assistant.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
