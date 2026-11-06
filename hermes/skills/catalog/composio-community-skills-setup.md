---
title: "Composio Skills - Tool Router and Trigger Patterns"
description: "composio-community/skills on skills.sh: 10.7K combined installs across 3 listings; Tool Router, auth and trigger patterns for Composio agents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/composio-community-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-06"
tags: ["hermes skill", "agent skill", "skill setup", "composio", "tool router", "triggers"]
---

# Composio Skills - Setup Guide

**Source:** [composio-community/skills](https://www.skills.sh/composio-community/skills) via skills.sh - 10.7K combined installs across 3 indexed listings; first seen 2026-11-06 (Nov 6, 2026 morning sweep)
**GitHub:** 185 stars, MIT, last pushed 2026-03-19, two SKILL.md directories: `skills/composio` and `.agents/skills/skill-creator` (the latter with a `.claude/skills/skill-creator` symlink pointing at it)
**Category:** Composio for agents: Tool Router sessions, authentication, framework integration and webhook triggers
**Quality Tier:** 🟡 Review - the composio and skill-creator listings both carry a Gen Agent Trust Hub Fail, and composio also carries a Snyk Fail, even though the repository is MIT licensed.

Composio is the integration layer that lets an agent act on external apps: Gmail, Slack, GitHub, Notion and the rest of the catalogue behind them. This repository is the written half of that, and it is a rules corpus rather than a code package. `skills/composio/SKILL.md` is a short router that decides between two jobs (drive the apps from the CLI, or write code against the SDK) and hands off to individual rule files in `rules/`, while `skills/composio/AGENTS.md` is the auto-generated single-file consolidation that `npm run build:agents` rebuilds from those same files.

The second install is `skill-creator`, which keeps a separate home under `.agents/skills/` and is reached from `.claude/skills/skill-creator` through a symlink. Its job is upstream of everything else: it creates or updates the skill files an agent reads. Together the two listings are a modest suite by install count, but `composio` at 7,111 is the one most projects actually load.

## Installation

The README's quick start installs both skills with the Agent Skills CLI:

```bash
npx skills add composiohq/skills
```

The README names the `composiohq` org, which is the repository's previous name: GitHub answers `composiohq/skills` with a 301 that resolves to `composio-community/skills`, so the command and the skills.sh source both land on the same repo.

The skill then walks the CLI side of Composio:

```bash
curl -fsSL https://composio.dev/install | bash
composio login
composio whoami
```

`composio login` is OAuth with an interactive org and project picker (`-y` skips the prompt). For an agent with no browser access, the skill documents a two-step path: `composio login --no-wait | jq` to get the URL and key, share the URL with the user, then `composio login --key <cli_key> --no-wait` once they finish. `composio whoami` prints the org_id, project_id and user_id that the rest of the rules assume.

For the SDK path, run this inside the project before writing code:

```bash
composio init
```

If you are editing the rules rather than consuming them, the repository builds the consolidated file with `npm run build:agents` and watches for changes with `npm run watch:agents`.

## What It Provides

Two listings clear the 500-install threshold. The larger one is the rules corpus; the smaller one is the tool for writing more of it.

| Skill | Installs | Use For |
|---|---|---|
| composio | 7,111 | CLI and SDK access to 1,000+ apps: search, link and execute commands, plus the Tool Router, auth, framework and trigger rules |
| skill-creator | 3,531 | Create or update a skill that extends an agent with new knowledge, workflows or tool integrations, with init, package and validate scripts |

The remaining 1 indexed listing is composio-tool-router (55 installs), and it has no directory in the current tree: the Tool Router material ships inside the composio skill's `rules/tr-*.md` files rather than as its own listing.

## Why This Matters for Hermes Agents

Tool access is where an agent stops being a text generator, and it is also where the confident wrong answer costs the most. An agent that reaches for a Gmail or Slack tool with no per-user connection model will either share one credential across every user or fail unpredictably on the second user. The `tr-userid-best-practices` and `tr-session-lifecycle` rules exist for exactly that class of mistake: user isolation, session creation, and what a session is allowed to outlive.

The rules are written as corrections rather than as reference prose. Each carries a frontmatter `impact` level of CRITICAL, HIGH, MEDIUM or LOW, then shows an incorrect shape and a correct one, with TypeScript and Python examples side by side and a link back to the official docs. That format is what makes them usable by an agent: the failure is visible next to the fix, so a model does not have to infer why one arrangement of calls is wrong.

The second theme is authentication, which is where agents quietly overreach. The repository separates auto authentication in a chat surface, manual authorization flows, and connection management, and it covers how to query toolkit availability and build a connection UI around the states a real account can be in. An agent that can say "this toolkit is not connected yet, here is the link" produces a working product; one that assumes the connection exists produces a support ticket.

Third, the trigger rules cover the part of automation that runs without a user present: creating trigger instances, subscribing during development only, verifying webhooks in production, and managing the trigger lifecycle. Webhook verification is the item most generated code skips, and it is the one that decides whether an attacker can post fake events into your pipeline.

Finally, the framework rules name the integration targets instead of leaving the agent to improvise: Vercel AI SDK, OpenAI Agents, LangChain, Claude, CrewAI and Mastra each get a file, plus a comparison of native tools against MCP tools for the same job. For a Hermes agent working on a Composio project, that means the routing decision is documented rather than guessed.

## Usage

| You say | What happens |
|---|---|
| "Send this Slack message to the team channel" | The composio skill runs the CLI path: search the toolkit, link the account if it is not connected, then execute the tool with the user's parameters |
| "Build an agent where each customer connects their own Gmail" | The Tool Router rules take over: user ID isolation, session creation, and per-user connected accounts rather than one shared credential |
| "Which framework should this use?" | The framework rules supply the Vercel AI SDK, OpenAI Agents, LangChain, Claude, CrewAI and Mastra patterns, plus native tools versus MCP |
| "Notify us when a new GitHub issue opens" | The trigger rules cover creating the trigger, subscribing during development, and verifying the webhook in production |
| "Why is my tool call returning another user's data?" | The user ID and session lifecycle rules are the ones to open first; they are the documented cause of that failure |
| "Add a build UI for connecting accounts" | The toolkit query and chat UI rules cover toolkit availability and the connection states a UI has to render |
| "Write a skill for our deploy runbook" | skill-creator drafts the skill, then initialises, packages and validates it with its bundled scripts |

## Verification

Read both skills from the repository before installing anything:

```bash
curl -fsSL https://raw.githubusercontent.com/composio-community/skills/main/skills/composio/SKILL.md | head -20
curl -fsSL https://raw.githubusercontent.com/composio-community/skills/main/.agents/skills/skill-creator/SKILL.md | head -20
```

The first should open with `name: composio` and the description about using 1,000+ external apps through the CLI or the SDK, followed by a When to Apply section and a Setup block. The second should open with `name: skill-creator`. Both paths returned HTTP 200 on 2026-11-06.

The composio skill is only useful with its `rules/` directory beside it, since SKILL.md is a router and the detail lives in those files. If an installed copy shows `SKILL.md` alone, reinstall rather than letting the agent work from the router.

Once the CLI is in place, the runtime check is the identity the rules key off:

```bash
composio whoami
```

It prints the org_id, project_id and user_id, which is also the fastest way to confirm that an agent is pointed at the project you think it is.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-06) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| composio | Fail | Pass | Fail |
| skill-creator | Fail | Pass | Pass |
| composio-tool-router | ? | ? | ? |

The composio verdicts are the ones to weigh, because it is the listing most projects install first and 7,111 installs is a lot of surface. What the skill instructs an agent to do is visible in the file: it pipes a remote install script from composio.dev into bash, runs an OAuth login, and then executes third-party tools with the user's connected accounts. Each of those is a legitimate step for this product, and each one is a step an agent takes on your machine without further confirmation.

The access model is the real blast radius. Composio tool calls run with the OAuth scopes the user granted to each connected app, so a mis-scoped Gmail or GitHub connection is reachable by anything the agent does afterwards. The repository's own user ID rules are a security control, not a convenience: a shared user ID across customers means one customer's connection answers another customer's request.

skill-creator carries file-writing scripts (`init_skill.py`, `package_skill.py`, `quick_validate.py`) and a Gen Agent Trust Hub Fail of its own. Read them before pointing it at a directory you care about, since it creates and packages files by design. `composio-tool-router` has no security sampling at all, and it also has no directory in the tree, so there is nothing to audit.

The licence is the one clean signal here: MIT, with a `LICENSE` file in the repository root, so redistribution and commercial use are ordinary.

## Limitations

- Snapshot data, verified 2026-11-06: 10,697 combined installs across 3 indexed listings; 185 GitHub stars; MIT; last pushed 2026-03-19. Counts drift over time.
- The install index outruns the tree. `composio-tool-router` carries 55 installs but has no directory in the current repository; the Tool Router rules live inside `skills/composio/rules/`.
- The last push was 2026-03-19, months before this snapshot. The rules describe an SDK that moves quickly, so check docs.composio.dev for anything that changed after the files were last touched.
- The README's file statistics say 14 or more rules; `skills/composio/rules/` currently holds 30 rule files plus a `_template.md`. The count in the README is stale, the directory is the truth.
- skill-creator is not in the README's Structure block at all, and its listing name matches a widely reused skill name. Its description here comes from its own SKILL.md frontmatter, not from the repository README.
- The GitHub repository description is GitHub's default boilerplate ("Contribute to ... development by creating an account on GitHub"), so there is no publisher-written summary to check the category line against.

## Related

- [Composio - SDK Monorepo and Agent Toolkit Setup Guide](/hermes/skills/catalog/composiohq-composio-setup)
- [Awesome Codex Skills - Curated Codex Index](/hermes/skills/catalog/composio-awesome-codex-skills-setup)
- [Build Mcp Server Setup](/hermes/skills/catalog/build-mcp-server-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Read `tr-userid-best-practices` before any multi-user work. It is the rule that decides whether one customer can reach another customer's connected account.
- Install the CLI before installing the skill if you want a clean first run; the skill's Setup section spends its first block on the install script and the login, and an agent that hits that mid-task will stop to ask.
- Use the CLI path for one-off actions and the SDK path for products. The skill draws that line explicitly, and mixing them produces code that shells out to a CLI from inside a service.
- Prefer `AGENTS.md` when context is tight and `SKILL.md` when you need to load one rule. They hold the same content in different shapes, and the consolidated file is generated, so edit the rules and rebuild rather than editing it.
- Verify webhooks in production. The trigger rules mark event subscription as development only and webhook verification as the production path, and that distinction is the one real security control in the trigger half.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
