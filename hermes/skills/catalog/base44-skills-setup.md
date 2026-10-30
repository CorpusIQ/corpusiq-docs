---
title: "Base44 Skills - AI App Builder Platform Suite Setup"
description: "Base44 Skills: 51.0K combined installs. Base44's own MIT suite covers CLI project work, SDK app code, MCP remote dev and production troubleshooting."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/base44-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-29"
tags: ["hermes skill", "agent skill", "skill setup", "base44", "ai app builder", "mcp"]
---

# Base44 Skills - Setup Guide

**Source:** [base44/skills](https://www.skills.sh/base44/skills) via skills.sh - 51.0K combined installs across 6 indexed listings; first seen 2026-10-29 (evening sweep)

**GitHub:** [base44/skills](https://github.com/base44/skills) - 92 stars, MIT License, branch main, last pushed 2026-10-29; five product skills at `skills/base44-cli/`, `skills/base44-sdk/`, `skills/base44-troubleshooter/`, `skills/base44-remote-dev/` and `skills/base44-sandbox/` (each a `SKILL.md` plus `references/` where needed), four contributor-only skills under `.claude/skills/`, and plugin manifests for Claude Code (`.claude-plugin/marketplace.json`), Codex, Cursor and Antigravity

**Category:** AI app builder platform skills for Base44 full-stack projects

**Quality Tier:** 🟡 Beta (functional and actively maintained by the platform vendor, but two Warns in the sampled five: Socket Warn on base44-sdk and Snyk Warn on base44-sandbox; MIT LICENSE in repo, six indexed listings only)

Base44 Skills is published by Base44 itself, so this is first-party platform documentation written as agent instructions rather than a community wrapper around somebody else's API. The README labels the suite Beta, states that the skills are functional and actively maintained, and points feedback at GitHub Discussions. The compatibility list is broad on purpose: Cursor, Claude Code, Codex CLI, OpenCode and any agent that can read a `SKILL.md` directory, with prebuilt plugin manifests for the Claude Code marketplace, Codex, Cursor and Antigravity.

The suite covers one product from five angles rather than five unrelated tricks. `base44-cli` owns everything the command line does: project creation and scaffolding, entity, function, actor and agent configuration, deployment, and calls against the public API for settings, domains, users and source export. `base44-sdk` owns the JavaScript client for entities, backend functions, realtime actors, AI agents and the AI gateway. `base44-troubleshooter` reads production evidence, backend function logs and workflow run history. `base44-remote-dev` and `base44-sandbox` cover the newer cloud-sandbox workflow, where an external agent connects over MCP or the `base44 sandbox` CLI and never holds a local checkout. The 51.0K combined installs across six indexed listings put this among the more heavily used platform-vendor suites on skills.sh, which is worth noting given that the repository holds only 92 stars.

## Installation

The README documents four routes. Claude Code gets the plugin marketplace, which also carries updates:

```bash
/plugin marketplace add base44/skills
/plugin install base44@base44-skills
```

The same thing non-interactively, and the Codex CLI route, which registers the marketplace and then installs from the `/plugins` menu by selecting Base44 and choosing Install Plugin:

```bash
claude plugin install base44@base44-skills
codex plugin marketplace add base44/skills
```

Antigravity installs from a URL, either through Customizations then Plugins then Install from URL, or from a terminal:

```bash
agy plugin install https://github.com/base44/skills/tree/main/antigravity/base44
```

Every other agent uses Vercel's `skills` CLI, which is the route the README recommends for anything outside those three:

```bash
# Install all skills
npx skills add base44/skills

# Install globally (user-level)
npx skills add base44/skills -g
```

If you build inside Base44's cloud sandbox, where the platform auto-builds and auto-commits and you never run deploy or push, the README steers you to the narrower plugin, which bundles four skills and leaves out the deploy-oriented `base44-cli`:

```bash
claude plugin install base44-sandbox@base44-skills

npx skills add base44/skills --skill base44-remote-dev --skill base44-sandbox --skill base44-sdk --skill base44-troubleshooter
```

Hermes is not one of the agent IDs the `skills` CLI documents, so the predictable route is the same fallback this catalog uses elsewhere: fetch the repository and copy each skill directory into the profile skills folder. Hermes expects one directory per skill at the top level there, so copy the five children of `skills/` rather than the parent folder:

```bash
mkdir -p "$TMPDIR/base44"
curl -sL -o "$TMPDIR/base44/main.tar.gz" \
  https://github.com/base44/skills/archive/refs/heads/main.tar.gz
tar -xzf "$TMPDIR/base44/main.tar.gz" -C "$TMPDIR/base44"
for s in base44-cli base44-sdk base44-troubleshooter base44-remote-dev base44-sandbox; do
  cp -R "$TMPDIR/base44/skills-main/skills/$s" ~/.hermes/profiles/corpusiq/skills/
done
```

The CLI skill carries its own prerequisite, and it is strict about how the binary is invoked. Install the `base44` package as a project dev dependency with no version specifier, then always call it through a package manager:

```bash
npm install --save-dev base44
npx base44 whoami
```

`npx base44 login` is the interactive step when `whoami` fails. Provisioned apps authenticate from `BASE44_ACCESS_TOKEN` and `BASE44_REFRESH_TOKEN`, and for unattended work a workspace API key in `BASE44_API_KEY` (prefix `b44k_`) skips the login entirely.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| base44-sdk | 11,538 | Building a Base44 app's client code with the JavaScript SDK: entities, backend functions, realtime actors, AI agents, and the AI gateway for image, video, speech and code generation. Ships a module and type reference plus a do-not-hallucinate-APIs section that tells the agent to read the skill's own references instead of searching the web. |
| base44-cli | 11,448 | Everything through `npx base44`: creating an app or scaffolding local files for an existing one, configuring entities, backend functions, realtime actors and AI agents, deploying, and operating an existing app through the public API for settings, domains, users, members and source export. Global `--app-id` and `--json` flags, plus a mandatory `npx base44 whoami` authentication check at session start. |
| base44-troubleshooter | 10,426 | Diagnosing production failures from backend function logs and workflow run history: `npx base44 logs --app-id ... --level error`, `--follow`, `--function`, and `--since`/`--until` windows, plus `npx base44 workflows runs --status failed`. Also explains why logs are not read-after-write and what an empty result actually means. |
| base44-remote-dev | 8,836 | Pointing your own agent at a Base44 app over the MCP endpoint at `https://app.base44.com/mcp` or the `base44 sandbox` CLI subcommands (read, ls, grep, run, edit, checkpoint), the OAuth PKCE and device flows, the `sandbox:write` scope the mutating tools require, the edit-preview-verify loop, change persistence and builder-versus-agent concurrency. |
| base44-sandbox | 8,793 | Authoring inside Base44's cloud sandbox, where writing a resource file is what ships it: conventions for backend functions, realtime actors, entities and agents, the auto-commit that persists a written file, `create_checkpoint` and how the builder's Restore rolls an app back, and connector setup with no local filesystem. |

The remaining 1 indexed listing ranges from 2 to 2 installs: base44-coder, which has no directory in the repository tree and whose skills.sh page renders no verdict table, so there is no description to quote for it.

## Why This Matters for Hermes Agents

Platform-vendor skills are the cheapest way to stop an agent inventing an API. The `base44-sdk` skill opens with an instruction to read its own references before touching documentation or the web, and the module list it points at is the same one the platform ships, so a Hermes run that loads it stops guessing at resource names and method signatures.

The MCP route changes the shape of the job. Hermes can attach to `https://app.base44.com/mcp`, authenticate, and read, write and run commands inside a Base44 sandbox without cloning anything or holding deploy credentials on the box. For a hosted agent that is a much smaller attack surface than a local checkout plus a push step, and it is the natural fit when the app under work is not ours.

For unattended work the CLI path is the durable one. A workspace key in `BASE44_API_KEY` authenticates `npx base44` without an interactive login, which is what makes a cron job able to read error logs or workflow failures and act on them rather than waiting for a human to run `whoami` first.

The troubleshooting skill is the piece most agent suites leave out. It reads production evidence instead of guessing, tells the agent that logs are not read-after-write, and gives it `--follow`, function filters and time windows so a diagnosis comes from the actual failure rather than a plausible story about it.

The honest caveat is coupling. These are instructions for one proprietary platform, they are marked Beta, and the CLI route assumes a Node project with the `base44` package installed. None of it transfers to another stack, so load the skills when the work is Base44 work and do not let a mandatory-activation rule pull them into unrelated sessions.

## Usage

| You say | What happens |
|---|---|
| "Create a Base44 app for a job board" | The `base44-cli` skill runs `npx base44 whoami` first, then `npx base44 create` for a new project, and refuses to run `create` when an app was already provisioned, using `npx base44 scaffold` instead so no duplicate app appears. |
| "Add an entity for saved searches and a backend function to refresh them" | The `base44-cli` skill writes the resource configuration and pushes it; if the code itself is the task it hands over to `base44-sdk` for the client or function body, following each skill's own when-to-use-which section. |
| "Why is my scheduled function failing in production?" | `base44-troubleshooter` checks authentication, reads logs with `npx base44 logs --level error`, narrows with `--function` and a `--since`/`--until` window, checks `npx base44 workflows runs --status failed`, and reports the failing invocation instead of a guess. |
| "Work on my Base44 app in the cloud sandbox, I have no local checkout" | `base44-remote-dev` connects to the MCP endpoint, completes the OAuth flow, calls `list_user_apps` to find the app id, then reads before writing and verifies through the preview URL. |
| "Add a realtime presence feature to the board" | The `base44-sandbox` or `base44-sdk` conventions for actors cover the realtime primitive, matching the skill's own framing of actors as the layer behind presence, live cursors and in-room chat. |
| "Call my function's errors up and fix them" | `base44-troubleshooter` finds the error, the fix lands through `base44-sdk` for function code, and the sandbox path ships it by writing the file rather than deploying. |
| "Finish up for now" | The sandbox workflow calls `create_checkpoint` before stopping, since the auto-commit persists files but only checkpoints appear in the builder's version history. |

## Verification

The three raw paths below returned 200 on the main branch when this guide was written:

```bash
for p in skills/base44-sdk/SKILL.md skills/base44-cli/SKILL.md skills/base44-troubleshooter/SKILL.md; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/base44/skills/main/$p"
done
```

Confirm the five directories landed with a readable `SKILL.md` each, and that the frontmatter `name` matches the directory name, which is what a skill loader keys on:

```bash
for s in base44-cli base44-sdk base44-troubleshooter base44-remote-dev base44-sandbox; do
  echo "== $s"; head -3 ~/.hermes/profiles/corpusiq/skills/$s/SKILL.md
done
```

Read a `SKILL.md` before you install it, at minimum the activation block at the top and any command it says to run. `skills/base44-sdk/SKILL.md` and `skills/base44-cli/SKILL.md` both open with an immediate-action section that fires on any mention of base44, so it is worth knowing what the agent will do unprompted. The contributor-only skills are worth a look too if you plan to extend the suite, since `https://raw.githubusercontent.com/base44/skills/main/.claude/skills/skill-creator/SKILL.md` also returned 200 on main.

Finally check the runtime path the CLI skill depends on: `npx base44 whoami` should print an identity, and a failure there means `npx base44 login`, a token in the environment, or a workspace key is still missing.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-29) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| base44-sdk | Pass | Warn | Pass |
| base44-cli | Pass | Pass | Pass |
| base44-troubleshooter | Pass | Pass | Pass |
| base44-remote-dev | Pass | Pass | Pass |
| base44-sandbox | Pass | Pass | Warn |
| base44-coder | no verdict table rendered | n/a | n/a |

No sampled skill failed. The worst results are two warnings, Socket Warn on base44-sdk and Snyk Warn on base44-sandbox, and a warning is the scanner flagging a pattern it cannot clear by inspection rather than evidence of a payload. In practice both of these skills exist to drive remote operations: the SDK skill tells an agent to call live Base44 services and the AI gateway, and the sandbox skill tells it to write files that the platform then builds and deploys, so an analyser sees network reach plus remote code execution as the intended function rather than an accident. That is the right shape for the job and also the exact reason to grant `sandbox:write` deliberately instead of by default.

Two things to read for yourself. base44-coder carries a listing at 2 installs but no verdict table renders on its skills.sh page and no directory with that name exists in the tree, so treat it as an unverified listing rather than a sixth audited skill. And the plugin manifests in this repository install skills that the agent is told to activate on any mention of "base44", so the scope of what gets loaded is broader than a single explicit request. There is no curl-to-bash installer here: installation is a plugin marketplace command, the `skills` CLI, or a copy.

## Limitations

- Snapshot data, verified 2026-10-29: 51,043 combined installs across 6 indexed listings; 92 GitHub stars; MIT License; last pushed 2026-10-29. Counts drift over time.
- Index and tree do not line up exactly. Six listings carry install counts but the tree holds five product skill directories plus four contributor-only ones under `.claude/skills/` (review-skills, skill-creator, sync-cli-skill, sync-sdk-skill), nine tracked skill directories in all. base44-coder is indexed with no directory behind it, and the `.claude/` four are tooling for maintainers of this repo, not skills for Base44 app work.
- Beta, in name and in manifest. The Claude Code marketplace and plugin manifests all read `1.0.0-beta.1`, and the README asks for feedback through GitHub Discussions, so layout, skill names and activation rules can still move between releases.
- The CLI route is local-install only by design. The skill forbids calling `base44` directly and requires `npx base44`, which means a Node project with the `base44` package, or an environment token for headless use. A bare Hermes session with no project cannot run those commands.
- The sandbox plugin's `skills/` and `assets/` entries are symlinks (`plugins/base44-sandbox/skills` points at `../../skills`), so a tarball, zip or Windows checkout that does not preserve links yields a plugin with no skills inside it. Its `plugin.json` lists four skills, excluding base44-cli.
- The Antigravity bundle under `antigravity/base44/skills/` ships three of the five (cli, sdk, troubleshooter), so that install route is narrower than the README's general claim.

## Related

- [Next.js Agent Skills - Official Vercel Next.js Skill Suite Setup](/hermes/skills/catalog/nextjs-agent-skills-setup)
- [Vercel AI SDK Skills - TypeScript AI Development Setup](/hermes/skills/catalog/vercel-ai-skills-setup)
- [Vercel Agent Skills - Official Vercel Collection Setup](/hermes/skills/catalog/vercel-agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Decide between the two plugin sets before installing. The full `base44@base44-skills` plugin is for agents that run deploys; `base44-sandbox@base44-skills` is the four-skill set for work that happens inside the cloud sandbox, and it deliberately omits the CLI skill.
- For unattended runs, set `BASE44_API_KEY` to a workspace key so `npx base44 whoami` succeeds without a login prompt. An agent that stalls on an interactive login is indistinguishable from one that failed.
- Add `--skill` filters when you install with the `skills` CLI. Pulling the whole suite into a project that only ever reads logs over-fetches the activation rules that fire on any mention of base44.
- Reach for `base44-remote-dev` before `base44-sandbox` when the connection is the problem. The first covers the MCP endpoint, the OAuth scopes and the `sandbox:write` requirement; the second assumes you are already connected and covers what to author.
- In the sandbox, call `create_checkpoint` at the end of each unit of work. The auto-commit preserves files, but a Restore in the builder rolls back to the last checkpoint and discards everything written after it.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
