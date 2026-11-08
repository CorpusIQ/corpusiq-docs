---
title: "Cyrus - Agent Orchestration Setup Skills"
description: "cyrusagents/cyrus on skills.sh: 18.2K combined installs across 19 listings; setup and workflow skills for the Cyrus issue-to-pull-request agent."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/cyrus-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-07"
tags: ["hermes skill", "agent skill", "skill setup", "agent orchestration", "coding agents", "devops"]
---

# Cyrus - Setup Guide

**Source:** [cyrusagents/cyrus](https://www.skills.sh/cyrusagents/cyrus) via skills.sh - 18.2K combined installs across 19 indexed listings; first seen 2026-11-07 (Nov 7, 2026 evening sweep)
**GitHub:** 888 stars, Apache-2.0, last pushed 2026-11-06, 19 SKILL.md directories: 17 under `skills/` and two more, `google` and `release-core-test`, under `.claude/skills`
**Category:** Agent orchestration for issue trackers: guided setup plus investigate, implement, verify and release workflows
**Quality Tier:** 🟢 Green - all three sampled setup skills pass all three scanners, the license is Apache-2.0, and the repo ships a real LICENSE file.

Cyrus is a self-hosted agent runner. It watches Linear, GitHub, GitLab or Slack for issues assigned to it, creates an isolated git worktree per issue, runs a coding agent session inside that worktree, and streams progress back to the tracker. The interesting design choice is that it is model-agnostic on both ends: the issue tracker can be Linear, GitHub, GitLab, Slack, Zulip or Plane, and the worker can be Claude Code, Codex, Cursor, Gemini or OpenCode.

The 19 indexed skills split cleanly into two groups. Ten of them are setup: a top-level `cyrus-setup` orchestrator that walks the whole onboarding, and nine sub-skills for prerequisites, Claude authentication, GitHub, GitLab, Linear, Slack, the webhook endpoint, repositories and launch. The other nine are the work itself: `investigate`, `implementation`, `verify-and-ship`, `debug`, `summarize`, `release`, `f1-test-drive`, plus two repository-specific skills.

That split is why the install counts cluster so tightly. The setup skills occupy the top eight positions between 1,021 and 1,258 installs, because they are the documented entry point and the README's own install command pulls the whole set with `-g`. The workflow skills sit just below, from 731 to 953, and they are the ones that keep running after setup is done.

## Installation

The README's community path is the zero cost route: host everything yourself with your own Linear OAuth app, GitHub App and Slack App, and let the setup skill drive the onboarding.

```bash
npx skills add ceedaragents/cyrus -g
```

Then, in any coding agent:

```text
/cyrus-setup
```

That command installs dependencies, configures authentication, creates the integration apps and connects repositories. The README also points at a manual guide in `docs/SELF_HOSTING.md` if you would rather do the steps yourself.

The paid self-hosted route installs the CLI instead, where the networking and integration layer comes from the hosted service:

```bash
npm install -g cyrus-ai
cyrus auth <your-token>
```

Cyrus is BYOK, so the worker agent's tokens or subscription are yours. For pull requests, the README also requires git and the hosting CLI to be configured; `docs/GIT_GITHUB.md` and `docs/GIT_GITLAB.md` cover that.

Note the organization in the install command. The README still says `ceedaragents/cyrus`, which is the repository's previous name and redirects to `cyrusagents/cyrus` on GitHub, so the command works as written. skills.sh indexes the repo under `cyrusagents/cyrus`.

For a Hermes agent, each skill directory under `skills/` is a plain Agent Skills folder with a single `SKILL.md`, so copying or linking those directories into the agent skills directory is a complete install and skips the Claude-specific parts. The two extra skills in `.claude/skills` need to be copied from there.

Once the agent is running, keep it alive as a persistent process. The README documents three options:

```bash
tmux new -s cyrus
```

```bash
pm2 start cyrus --name cyrus
```

A systemd unit is documented in `docs/SELF_HOSTING.md` under "Running as a Service".

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| cyrus-setup | 1,258 | The orchestrator: install prerequisites, configure auth, create Linear, GitHub and Slack integrations, add repositories and launch |
| cyrus-setup-linear | 1,129 | Creating a Linear OAuth application and wiring Cyrus to it, with browser automation or a guided manual flow |
| cyrus-setup-claude-auth | 1,108 | Configuring Claude Code authentication for the worker: API key, OAuth token or a third-party provider |
| cyrus-setup-github | 1,068 | GitHub CLI login and git config for pull requests, plus optional webhook setup for mention responses |
| cyrus-setup-prerequisites | 1,062 | Checking and installing Node.js, jq, the GitHub CLI and the cyrus-ai package |
| cyrus-setup-endpoint | 1,046 | Standing up the public webhook endpoint through ngrok, Cloudflare Tunnel or a custom URL |
| cyrus-setup-repository | 1,038 | Adding one or more git repositories to the config so Cyrus can process their issues |
| cyrus-setup-launch | 1,021 | Printing a setup summary and offering to start the agent |
| google | 953 | Web search when the agent needs current information or has to research a topic |
| cyrus-setup-slack | 925 | Creating a Slack app from a manifest and guiding the credential save |
| summarize | 909 | Formatting the final summary that streams back into the Linear session |
| investigate | 885 | Researching the codebase to answer a question: find the files, gather context, explain |
| implementation | 873 | Writing the change in production style, following existing patterns with proportionate verification |
| verify-and-ship | 866 | Choosing the right validation, fixing failures, updating the changelog, committing and opening the pull request |
| release | 848 | Preparing, verifying, publishing and finishing a coordinated Cyrus CLI release |
| debug | 847 | Reproduce the bug, find the root cause, apply a minimal fix |
| f1-test-drive | 823 | Assessing applicability, then validating changed workflows or the harness end to end |
| cyrus-setup-gitlab | 805 | GitLab authentication through the glab CLI and git config for merge requests |
| release-core-test | 731 | Publishing cyrus-core as a test prerelease under the npm test dist-tag so a hosted GUI can install it |

No indexed listings fall below the threshold; all 19 appear above.

Two of these are not for general use. `release-core-test` is a maintainer skill for testing changes that span the packaged core and the hosted GUI, and it publishes to a `test` dist-tag specifically to avoid touching `latest`. `f1-test-drive` is named after an internal harness. They are indexed because they ship in the repository, not because a typical install needs them.

## Why This Matters for Hermes Agents

The setup half is the part worth stealing even if you never run Cyrus. Configuring a self-hosted agent end to end means installing prerequisites, creating three OAuth applications, saving secrets without printing them, exposing a webhook endpoint and starting a daemon. That is exactly the class of task agents handle badly, because it is long, stateful and full of one-time clicks. A skill that encodes the order, the choices and the failure modes turns a two hour manual setup into a guided run.

The `cyrus-setup` skill is also unusually careful about secrets for a public repository. It forbids reading or writing `~/.cyrus/.env` directly, and routes every interaction through shell commands the user can see and approve, so keys never enter the conversation context. That pattern is worth copying into any setup skill you write.

The workflow half encodes a discipline that agents usually skip: `investigate` before `implementation`, and `verify-and-ship` as a separate step that chooses proportionate validation rather than running everything. That separation maps onto how a careful engineer works on an unfamiliar codebase.

For Hermes specifically, the architecture is a template. One orchestrator skill with numbered sub-skills, a state file it updates, and a single launch step at the end is a reproducible shape for any long onboarding.

## Usage

| You say | What happens |
|---|---|
| "Set up Cyrus on this machine" | `cyrus-setup` runs the whole sequence and hands off to the sub-skills, writing credentials through shell commands only |
| "Connect Linear" | `cyrus-setup-linear` creates the OAuth app with browser automation or walks you through it manually |
| "I need a public webhook URL" | `cyrus-setup-endpoint` picks between ngrok, Cloudflare Tunnel and a custom domain, then configures it |
| "Investigate why the retry logic drops events" | `investigate` searches the codebase, gathers context and explains the path before anything changes |
| "Fix this bug and open a PR" | `debug` reproduces and fixes, then `verify-and-ship` validates, updates the changelog and opens the pull request |
| "Summarise what you did" | `summarize` formats the final message for the Linear session, which streams it back automatically |
| "Cut a CLI release" | `release` runs the prepare, verify, publish and finish sequence for the cyrus-ai package |

## Verification

Read the orchestrator before installing. This path returned HTTP 200 on the repository's `main` branch:

```bash
curl -fsSL https://raw.githubusercontent.com/cyrusagents/cyrus/main/skills/cyrus-setup/SKILL.md | head -20
```

It should open with `name: cyrus-setup` and the description about installing prerequisites, configuring authentication, creating integrations and launching. The two skills that live outside `skills/` are here:

```bash
curl -fsSL https://raw.githubusercontent.com/cyrusagents/cyrus/main/.claude/skills/google/SKILL.md | head -20
```

After install, confirm the count and that the CLI is on PATH:

```bash
ls ~/.agents/skills | wc -l
cyrus --version
```

The count should be 17 from `skills/` alone, or 19 if you also copied the two `.claude/skills` directories. The `-g` flag in the install command puts the directories in the global `~/.agents/skills`, so that is the path to check. If the CLI is missing, the `npm install -g cyrus-ai` step did not complete.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-07) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| cyrus-setup | Pass | Pass | Pass |
| cyrus-setup-linear | Pass | Pass | Pass |
| cyrus-setup-claude-auth | Pass | Pass | Pass |

This set handles secrets by design: OAuth client secrets, app private keys, API tokens and signing secrets. The setup skill's own rules are the right ones, and they are worth reading before you run it. Never let an agent read `.env` files into context, never paste a token into a chat message, and never commit `~/.cyrus/`.

The browser automation modes deserve a decision before setup rather than during it. `cyrus-setup` prefers the `claude-in-chrome` MCP extension because it reuses your existing signed-in Chrome sessions, which means the agent acts with your live credentials in Linear, Slack and GitHub. If that is too much authority, force the manual guided flow and do the clicks yourself.

The runtime is the other consideration. Cyrus runs coding agents against your repositories with push access, so the token it holds defines the blast radius. Use a dedicated GitHub App or a fine-scoped token per organisation rather than a personal token with repo-wide write.

## Limitations

- Snapshot data, verified 2026-11-07: 18,195 combined installs across 19 indexed listings; 888 GitHub stars; Apache-2.0; last pushed 2026-11-06. Counts drift over time.
- The repository was renamed. The README's install command still reads `ceedaragents/cyrus`, which GitHub redirects to `cyrusagents/cyrus`, and skills.sh indexes it under the new name. Both work today, and the old one can stop working without notice.
- Two skills sit outside the main tree. `google` and `release-core-test` live in `.claude/skills` rather than `skills/`, so an install that copies only `skills/` gets 17 of the 19 indexed listings.
- Setup is interactive by nature. Creating OAuth applications and saving credentials needs a browser and a human, so it does not run unattended in a cron job.
- BYOK means the worker's tokens are your cost. Cyrus itself adds orchestration and hosting, not model capacity.
- The workflow skills assume the Cyrus runner. `summarize` streams to a Linear agent session and `verify-and-ship` opens a pull request, so they are less useful outside a runner that supplies those surfaces.

## Related

- [Multi-Agent Orchestration - PM-style parallel worker](/hermes/skills/catalog/multi-agent-orchestration-setup)
- [Agent Orchestrator - Multi-Agent Coordination Setup](/hermes/skills/catalog/agent-orchestrator-setup)
- [Kanban Orchestrator - Full Setup Guide for Hermes Agents](/hermes/skills/catalog/kanban-orchestrator-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run `cyrus-setup-prerequisites` first even though `cyrus-setup` will call it. It fails fast on a missing Node or jq, which is a cheaper error than a half-written config.
- Decide on the browser automation mode before you start. Reusing your signed-in Chrome is faster and hands the agent your live sessions, so pick the manual flow on a machine that holds production credentials.
- Pin the repository scope before launch. `cyrus-setup-repository` is where you limit which repos Cyrus can see, and that is the cheapest place to reduce blast radius.
- Keep the process under a supervisor from day one. `pm2` or a systemd unit with restart on failure beats discovering the agent died three issues ago.
- Read `verify-and-ship` before you let it push. The skill chooses proportionate validation, and knowing which checks it will skip tells you where a human review still matters.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
