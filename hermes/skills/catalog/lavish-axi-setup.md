---
title: "Lavish AXI - Agent Experience Interface Setup"
description: "kunchenguid/lavish-axi: 23.5K combined installs. Local CLI that opens agent-written HTML artifacts for annotation, Mermaid whiteboards and feedback."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/lavish-axi-setup/"
robots: "index,follow"
last_updated: "2026-10-30"
tags: ["hermes skill", "agent skill", "skill setup", "html artifacts", "design review", "cli", "mermaid"]
---

# Lavish AXI - Setup Guide

**Source:** [kunchenguid/lavish-axi](https://www.skills.sh/kunchenguid/lavish-axi) via skills.sh - 23.5K combined installs across 3 indexed listings; first seen 2026-10-30 (morning sweep)

**GitHub:** [kunchenguid/lavish-axi](https://github.com/kunchenguid/lavish-axi) - 4,358 stars, MIT License, branch main, last pushed 2026-10-29; 2 `SKILL.md` files in two trees, the public `skills/lavish/SKILL.md` and the internal brand skill at `.agents/skills/lavish-design/SKILL.md`, beside `src/`, `bin/`, `docs/`, `scripts/`, `plugin.json` and `package.json` (npm package `lavish-axi`, version 0.1.96)

**Category:** Agent-facing interface design and agent experience tooling

**Quality Tier:** 🟢 Green - all sampled skills Pass on all three auditors; MIT-licensed local-first CLI that turns agent-written HTML into a reviewable page

Lavish Editor is published by Kun Chen as `kunchenguid/lavish-axi`, and the repository ships both the CLI and the skill that teaches an agent to use it. Lavish describes itself as an AXI, an agent experience interface: a plain command line tool any capable agent can run with no setup, tuned for agent ergonomics with TOON output, long polling and contextual disclosure to stay token efficient. In practice it opens an agent-generated HTML file in a local browser, lets a reviewer pinpoint elements and selected text, edit diagrams the agent authored as Mermaid whiteboards, queue layout issues from an inbox, and send all of that back as feedback the agent collects with `lavish-axi poll`.

The skill itself is deliberately thin. It tells the agent to fetch current guidance from the CLI (`npx -y lavish-axi --help`, `reply --help`, `design` and `playbook`) instead of trusting the markdown, so an installed copy cannot go stale against a newer CLI, and its frontmatter carries Hermes Agent metadata (`hermes-tags`, `hermes-category: productivity`) so a Hermes-compatible harness can classify it as a productivity skill. At 4,358 stars the project is well past the experimental stage, and the install index treats it as one high-volume skill rather than a multi-skill suite.

## Installation

The README's quick start is a single skills CLI call and needs no npm install:

```bash
npx skills add kunchenguid/lavish-axi --skill lavish
```

The skill lands in the current project's skills directory by default; the README notes that adding `-g` installs it for all projects. In agents that expose skills as slash commands the skill is then invocable directly:

```text
/lavish let's discuss our plan here
```

The CLI also runs with nothing installed at all, which is the fallback worth knowing when a global install is not allowed:

```bash
npx -y lavish-axi --help
```

Two optional routes come from the same npm package. The session hook feeds Lavish's ambient context, including live open sessions, into every agent session:

```bash
npm install -g lavish-axi
lavish-axi setup hooks
```

And the Agent Plugin route registers the installed package with the clients that speak that format, with no marketplace involved:

```bash
npm install -g lavish-axi
lavish-axi setup plugin
```

Building from source is also documented:

```bash
git clone https://github.com/kunchenguid/lavish-axi.git
cd lavish-axi
pnpm install --frozen-lockfile
pnpm run build
pnpm link
```

Hermes is not one of the hook or plugin targets (those are Claude Code, Codex, OpenCode, GitHub Copilot CLI, VS Code and Cursor), so the durable route for this profile is the skills directory itself. The public skill is one self-contained file, `skills/lavish/SKILL.md`, with no `scripts/`, `references/` or `assets/` beside it, so a directory copy is the whole install:

```bash
cp -r skills/lavish ~/.hermes/profiles/corpusiq/skills/lavish
```

Do not copy `lavish-design`. It is the internal brand skill for maintainers, it is hidden from `npx skills add --list` and from skills.sh discovery unless `INSTALL_INTERNAL_SKILLS=1` is set, and it is about designing Lavish's own brand assets rather than about reviewing artifacts.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| lavish | 23,423 | Turning a plan, comparison, diagram, table, code diff or report into a reviewable HTML artifact, then running the review loop: open the file in the local Lavish Editor, long-poll for queued feedback, post a reply, and end the session when the review is done. |

The remaining 2 indexed listings range from 5 to 46 installs.

Neither of the two small listings has a directory in the current checkout: the tree holds `lavish` and the internal `lavish-design`, and nothing named `lavish-axi` or `no-mistakes`. Install the `lavish` skill; the other two are index entries without a matching skill to copy.

## Why This Matters for Hermes Agents

Much of what an agent produces for a human to judge is a decision rather than a task: a migration plan, a schema comparison, an architecture diagram, a table of tradeoffs. Hermes can write all of that as prose, but the review then collapses into screenshots and a long reply that says "tell me what to change", which is exactly the loop Lavish is built to replace. The artifact becomes a file, the file opens in a local browser, and the review comes back as prompts on specific elements and text ranges instead of a paragraph of vague dissatisfaction.

The delivery path is also well suited to how Hermes runs work. `lavish-axi poll <file>` is a long poll that returns only when the user sends feedback or ends the session, so a blocking turn can wait on a human without inventing its own sleep and check loop, and the response is a structured prompt set rather than a stream to parse. Sessions are keyed by the canonical HTML file path, which means a subagent or a resumed session can reattach by path with no opaque identifier to carry around.

The stub design holds up over a long-lived profile. Because the workflow, design guidance and playbooks all live in the CLI and the skill only routes to them, upgrading the npm package improves what the skill does without any change to the installed markdown. That is the opposite of the usual failure mode for a copied skill, where the instructions freeze at the version someone committed.

Everything in the core loop stays local. Session state lives under `~/.lavish-axi/`, the server binds to loopback and, when Tailscale is running, to the machine's tailnet address only, and publishing to a hosted page is a separate explicit `share` command. For a profile that handles client material, that split is the useful one: review by default, publish on request.

## Usage

| You say | What happens |
|---|---|
| "Turn that plan into something I can actually review" | The agent writes the artifact as a local HTML file, opens it with `npx -y lavish-axi <file>`, and waits on a poll so the page appears in your browser ready to annotate. |
| "I marked up the comparison table, go fix it" | The queued annotations arrive from `lavish-axi poll` as prompts carrying the element or selected text, the quoted excerpt and the CSS selector, and the agent edits the file in place. |
| "This diagram should be editable, not a picture" | The agent re-authors the figure as Mermaid in a `.mermaid` container, which Lavish renders as an embedded Excalidraw whiteboard; your edits come back as an edit summary plus the scene file. |
| "Nothing is listening, is the session dead?" | The browser chrome shows agent presence, and a poll that ends on `browser_disconnected` returns without ending the resumable session, so the agent asks whether to reopen or end it instead of guessing. |
| "Send me a link I can open on my laptop" | `lavish-axi export` writes a single portable HTML file with local assets inlined and the annotation SDK stripped, or `lavish-axi share` publishes it to the third-party host and prints a URL plus a secret update key. |
| "The layout breaks on my phone" | The passive layout-issue inbox files proven failures per viewport class, and queueing them turns the selected group into one ordinary prompt tagged `layout-warnings` that reaches the agent on its next poll. |
| "We are done with this review" | A user-initiated end from the browser makes open tabs read-only and refuses further feedback; a later plain open returns guidance instead of reopening unless the agent passes `--reopen`. |

## Verification

Both raw paths below returned 200 on branch main when this guide was written on 2026-10-30:

```bash
curl -sL -o /dev/null -w "%{http_code} public\n" \
  https://raw.githubusercontent.com/kunchenguid/lavish-axi/main/skills/lavish/SKILL.md
curl -sL -o /dev/null -w "%{http_code} internal\n" \
  https://raw.githubusercontent.com/kunchenguid/lavish-axi/main/.agents/skills/lavish-design/SKILL.md
```

Expect `200` twice. Read the first one before installing, because it is short on purpose: the only things worth checking are that `description:` names the trigger situations you care about and that the `hermes-category` metadata survived, since those two fields are what routing and classification depend on.

After the copy lands in the profile, confirm the file and the CLI it will drive:

```bash
head -10 ~/.hermes/profiles/corpusiq/skills/lavish/SKILL.md
npx -y lavish-axi --version
```

A good copy shows `name: lavish`, the one-line description and the `metadata:` block with `hermes-tags` and `hermes-category`, and the CLI reports a version without a browser opening. The License line in the frontmatter reads MIT; the repository LICENSE is MIT, copyright Kun Chen.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-30) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| lavish | Pass | Pass | Pass |
| lavish-axi | n/a | n/a | n/a |
| no-mistakes | n/a | n/a | n/a |

No FAIL verdict appears and no Warn either, but only `lavish` was sampled: the other two listings carry no audit result at all, so the Pass column above describes one file, not the suite. That file is a small markdown stub that runs an npm CLI, which is a smaller surface than most skills this catalog covers, and the risk sits in the CLI it delegates to rather than in the markdown.

Three behaviours are worth reading before you point this at client material. The npm release sends anonymous usage telemetry to an Umami server at `https://a.kunchenguid.com` by default: a page view and a command event carrying the command name, version, platform, architecture and status, with no arguments, file paths, artifact content or prompts, and `LAVISH_AXI_TELEMETRY=0` turns it off. The review server is unauthenticated, which is why it binds to loopback and the tailnet address rather than every interface; the README states plainly that binding beyond loopback exposes a server that can read and serve arbitrary local files to anything that can reach it, so the tailnet has to be trusted. And `share` uploads the artifact to ht-ml.app, a third party, public by default, where a password cannot later be removed and there is no delete endpoint: unpublish replaces the page with a locked placeholder while the host still holds what was published.

## Limitations

- Snapshot data, verified 2026-10-30: 23,474 combined installs across 3 indexed listings; 4,358 GitHub stars; MIT License; last pushed 2026-10-29. Counts drift over time.
- The index outruns the tree. skills.sh carries three listings, but the checkout holds two skill directories, `lavish` and the internal `lavish-design`, and no directory named `lavish-axi` or `no-mistakes`, so those two counts have no skill to copy today.
- The counts are not a ranking. One listing holds 23,423 of the 23,474 combined installs; the other two sit at 46 and 5. Judge the skill by its `SKILL.md` and by the CLI, not by the number beside it.
- The installed skill is a stub by design. It carries no workflow, design rules or playbooks and sends the agent to `npx -y lavish-axi --help`, `design` and `playbook` for all of that, so a copy read offline, or in an environment where `npx` cannot fetch the package, tells the agent far less than the CLI would.
- The review loop needs a live local service and a human in a browser. The background server defaults to port 4387 and shuts down after 30 idle minutes, so an agent that starts a poll with no browser attached gets `browser_disconnected` rather than feedback, and nothing here substitutes for someone looking at the page.
- Lavish declares no MCP server, so a Hermes profile gains a CLI and a skill rather than MCP tools, and the `setup hooks` and `setup plugin` installers target other clients: Claude Code, Codex, OpenCode, GitHub Copilot CLI, VS Code and Cursor.

## Related

- [Agent Browser - Vercel Labs CLI for AI Agents Setup](/hermes/skills/catalog/agent-browser-setup)
- [Vercel Chat SDK Skills - Chat Bot Development Setup](/hermes/skills/catalog/vercel-chat-sdk-skills-setup)
- [HeroUI Skills - React & React Native UI Component Setup](/hermes/skills/catalog/heroui-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install `lavish` and stop there. It is one file, it routes to the CLI for everything that changes, and it will not rot; the hook and plugin routes exist to feed other clients, not to make the skill better.
- Set `LAVISH_AXI_TELEMETRY=0` in the profile environment if the default telemetry is not acceptable. It is the cheapest change in this guide and it needs no rebuild.
- Keep local assets next to the artifact and reference them relatively. Root-prefixed paths such as `/assets/logo.png` do not resolve through Lavish's artifact route, and that failure looks like a broken design rather than a broken path.
- Long-poll, do not poll in a loop. `lavish-axi poll <file>` returns when there is feedback, an end, or a disconnect, and the response has to be read in full before truncating because delivery consumes it.
- Open the matching playbook before writing HTML. `lavish-axi playbook` lists ids such as `diagram`, `table`, `comparison`, `plan`, `code`, `input`, `explanation` and `slides`, and one artifact often needs two of them.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
