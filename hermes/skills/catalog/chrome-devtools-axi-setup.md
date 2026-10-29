---
title: "Chrome DevTools AXI - Agent Browser CLI Setup"
description: "chrome-devtools-axi: 7.1K combined installs. A TypeScript CLI wrapping chrome-devtools-mcp so agents drive Chrome with compact, snapshot-first output."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/chrome-devtools-axi-setup/"
robots: "index,follow"
last_updated: "2026-10-29"
tags: ["hermes skill", "agent skill", "skill setup", "browser automation", "chrome devtools", "cli"]
---

# Chrome DevTools AXI - Setup Guide

**Source:** [kunchenguid/chrome-devtools-axi](https://www.skills.sh/kunchenguid/chrome-devtools-axi) via skills.sh - 7.1K combined installs across 1 indexed listing; snapshot 2026-10-29 (Oct 29 morning sweep)

**GitHub:** [kunchenguid/chrome-devtools-axi](https://github.com/kunchenguid/chrome-devtools-axi) - 445 stars, MIT License, branch main, last pushed 2026-10-28; one skill directory at `skills/chrome-devtools-axi/SKILL.md` inside a real application tree (`src/`, `bin/`, `test/`, `scripts/` and a pnpm workspace), package version 0.1.45

**Category:** Browser automation, Chrome DevTools Protocol tooling and CLI wrappers around MCP browser servers

**Quality Tier:** 🟡 Beta - individual publisher, 445 stars, OSI license, a 27-file vitest suite plus CI on main, but a single maintainer and a Snyk W011 warn on the sampled listing

chrome-devtools-axi is Kun Chen's (@kunchenguid) TypeScript CLI that wraps chrome-devtools-mcp, the Chrome DevTools MCP server, in what the author calls an AXI (agent experience interface). It is not an MCP server and it is not a browser: it is a command line that hides one. Every invocation is short-lived and talks over HTTP to a detached bridge process on localhost port 9224, which holds a single persistent MCP session, which in turn drives headless Chrome through the DevTools Protocol. The bridge starts on the first command, writes a PID file to `~/.chrome-devtools-axi/bridge.pid`, and is only reused after a deep health check that asks the MCP server to list pages, so a dead browser is respawned instead of silently reused.

The command surface is wide for something this small. Navigation and snapshots (`open`, `snapshot`, `reload`, `back`, `scroll`, `wait`), interaction by accessibility reference (`click @uid`, `fill`, `type`, `press`, `hover`, `drag`, `fillform`, `dialog`, `upload`), tab management (`pages`, `newpage`, `selectpage`, `closepage`, `resize`), device and network emulation, console and network inspection, and a performance group (`lighthouse`, `perf-start`, `perf-stop`, `perf-insight`, `heap`). Output is TOON-encoded rather than JSON, every snapshot carries `uid=` refs the agent is expected to pass back verbatim, and every response ends with a suggested next command. The repository also ships `npx -y chrome-devtools-axi --help` as the real documentation, which is exactly what its skill file points at.

What makes it notable here is the split between the CLI and the skill. The CLI is 27 vitest files of behaviour. The skill is a 1,617 character discovery stub generated from `src/skill.ts`: a name, a description written to trigger on "needs a real browser" intents, Hermes metadata in the frontmatter, one paragraph of when to use it, and an explicit instruction not to trust the file's own command guidance because installed copies go stale. It ships no procedure, no command list and no workflow, which is why this guide documents the CLI and treats the skill as a router.

## Installation

The README's Quick Start is the skills CLI, which installs only the skill and leaves the CLI to `npx` on demand:

```bash
npx skills add kunchenguid/chrome-devtools-axi --skill chrome-devtools-axi -g
```

Because this repository has a real skill directory rather than a root-level `SKILL.md`, the same file is also fetchable directly, which is the predictable route when you want the copy to live under the Hermes profile rather than a harness-specific skills folder:

```bash
mkdir -p ~/.hermes/profiles/corpusiq/skills/chrome-devtools-axi
curl -sL -o ~/.hermes/profiles/corpusiq/skills/chrome-devtools-axi/SKILL.md \
  https://raw.githubusercontent.com/kunchenguid/chrome-devtools-axi/main/skills/chrome-devtools-axi/SKILL.md
```

Nothing else is required for the agent path. The skill tells the agent to run everything as `npx -y chrome-devtools-axi <command>`, so the CLI downloads on first use. If you want the binary resident, or you want the ambient session hook, install globally and opt in:

```bash
npm install -g chrome-devtools-axi
chrome-devtools-axi setup hooks
```

`setup hooks` writes a `SessionStart` hook for Claude Code, Codex and OpenCode that prints the live browser session and usage guidance at session start, and the README says to restart the agent session afterwards. Development entrypoints such as `pnpm run dev` and `bin/chrome-devtools-axi.ts` are blocked from installing hooks. Building from source needs Node 20 or later and pnpm: `git clone`, `pnpm install --frozen-lockfile`, `pnpm run build`, `pnpm link`. There is no curl to bash installer anywhere in this repository.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| chrome-devtools-axi | 7072 | A discovery stub that teaches an agent when to reach for a real browser and sends it to `npx -y chrome-devtools-axi --help` for the actual commands: snapshot-first navigation with `uid=` refs, click and form fill with `STALE_REF` freshness checks, console and network inspection, screenshots, device emulation, Lighthouse and performance traces, and explicit instruction to skip Chrome when plain `fetch` or `curl` would do. |

No indexed listings fall below the threshold.

## Why This Matters for Hermes Agents

The thing that costs tokens in a browser session is not the page, it is the tool schema. An MCP browser server registers dozens of tools, and every one of their JSON schemas sits in context on every turn whether or not the agent touches them. AXI moves that surface behind one CLI call, returns a compact snapshot instead of a full accessibility dump, and appends one suggested next command instead of a menu. The repository's own benchmark (14 tasks, 7 setups, 5 repeats, judged by an LLM) puts it at 79,141 average input tokens against 184,711 for raw chrome-devtools-mcp, with 100 percent task success and 4.5 turns against 6.2. Those are the author's numbers on the author's harness, so read them as a direction rather than a measurement of your workload.

The design choices that actually change agent behaviour are the boring ones. Snapshots truncate at about 16k characters unless `--full` is passed, which caps the blast radius of a giant page. Large network bodies go to disk with `--response-file` instead of into the transcript. `eval` keeps its head and tail when truncated, so a long result does not lose the return value. And the tool refuses to lie: uid actions fail loudly with `STALE_REF` when the page mutated since the snapshot, rather than clicking whatever now occupies that ref.

For a Hermes profile that already carries a browser tool, the interesting part is the bridge. Chrome survives between commands, so a five-step checkout flow does not relaunch a browser five times, and named sessions (`CHROME_DEVTOOLS_AXI_SESSION`) give each agent or worktree its own bridge, port and state directory. The README is also unusually explicit about what it will not do: browsers it launches always get `--use-mock-keychain` and `--password-store=basic`, so an automation browser cannot read or offer to reset the OS password store, and saved-password autofill is unavailable inside it.

## Usage

| You say | What happens |
|---|---|
| "Open the staging site and tell me what is on the page" | `open <url>` navigates, captures the accessibility tree, prints `page:` metadata with a ref count, lists `uid=` refs for interactive elements and ends with a `help[1]:` line naming the next command to run. |
| "Click the More information link" | The agent passes the ref exactly as printed, for example `click @g1:1`. The generation prefix is checked against the snapshot it came from; if the page changed, the command fails with `STALE_REF` and the agent re-snapshots instead of clicking blind. |
| "Fill in the signup form and submit it" | `fillform @uid=value @uid=value` sets several fields in one call, then a snapshot or `eval` confirms the fields took, because a valid ref can still produce no visible change. |
| "Why is this page erroring?" | `console --type error --limit 20` lists console messages, `console-get <id>` expands one, and `network --type fetch` narrows requests by resource type; large bodies go to disk with `network-get <id> --response-file /tmp/body.json`. |
| "Run a performance audit on the pricing page" | `lighthouse --device mobile --mode navigation --output-dir ./reports` writes a report, or `perf-start` / `perf-stop --file trace.json` captures a trace and `perf-insight` analyzes a named insight. |
| "Crawl two sites at the same time without them colliding" | `CHROME_DEVTOOLS_AXI_SESSION=worker-1 ... open <url>` and the same with `worker-2` get separate bridges, auto-derived ports and separate on-disk state; pages, refs and selection never cross. |
| "The click worked but the page looks the same" | The agent re-snapshots, or runs `eval` or `screenshot` before reporting success, and uses `snapshot --full` when the truncated tree hides the element it needs. |

## Verification

The raw SKILL.md path in this guide returned 200 on branch main when the guide was written on 2026-10-29:

```bash
curl -sL -o /dev/null -w "%{http_code} SKILL.md\n" \
  https://raw.githubusercontent.com/kunchenguid/chrome-devtools-axi/main/skills/chrome-devtools-axi/SKILL.md
```

Expect `200`. There is exactly one SKILL.md in the repository tree, at `skills/chrome-devtools-axi/SKILL.md`, and the npm package ships that same directory, so the raw URL and the published package agree.

After install, confirm the file landed in the Hermes profile and that the frontmatter is the generated one (name, `user-invocable: false`, `author`, and the `metadata.hermes` block):

```bash
ls -l ~/.hermes/profiles/corpusiq/skills/chrome-devtools-axi/SKILL.md
head -12 ~/.hermes/profiles/corpusiq/skills/chrome-devtools-axi/SKILL.md
```

Then confirm the CLI itself resolves, since the skill calls it through `npx`:

```bash
npx -y chrome-devtools-axi -v
npx -y chrome-devtools-axi --help
```

The current release is 0.1.45, and `chrome-devtools-axi update --check` reports installed versus latest without installing anything. `chrome-devtools-axi stop` shuts the bridge down; leaving it running leaves a detached process holding a browser.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-29) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| chrome-devtools-axi | Pass | Pass | Warn W011 |

No listing fails. Two auditors pass and Snyk records one warn, W011, on the single sampled listing. The pack does not include the finding text behind that rule code, so this guide will not guess at it; open the skills.sh security page for chrome-devtools-axi and read the W011 entry before you put the CLI on a machine that holds credentials.

What installs by default is a 1,617 character markdown stub, so the skill itself executes nothing. The risk is in the CLI the stub instructs the agent to run. It launches a headless Chrome, drives real pages with real credentials if you point it at an authenticated profile, and by default wraps Chrome in `--use-mock-keychain` and `--password-store=basic` so the automation browser stays off the OS keychain. That isolation applies only to browsers AXI launches: in `CHROME_DEVTOOLS_AXI_AUTO_CONNECT`, `CHROME_DEVTOOLS_AXI_BROWSER_URL` and WebSocket endpoint modes the browser belongs to whoever started it and keeps its saved passwords. The other structural point to review is the bridge: a detached process listening on localhost port 9224, which can be pinned or moved with `CHROME_DEVTOOLS_AXI_PORT` and is meant to stay loopback-only. Nothing here pipes a remote script into bash.

## Limitations

- Snapshot data, verified 2026-10-29: 7072 combined installs across 1 indexed listing; 445 GitHub stars; MIT License; last pushed 2026-10-28. Counts drift over time.
- The listing count and the tree do not quite line up. skills.sh indexes one skill named `chrome-devtools-axi`, and the tree has one real skill file, but `.agents/skills/` holds only a `.gitkeep` and `.claude/skills` is a symlink to it, so a `-g` install is the only thing that populates a harness skills directory.
- The SKILL.md is generated, capped at 2,500 characters, and `pnpm test` fails if it drifts from `createSkillMarkdown()`. Hand edits will be reverted by `pnpm run build:skill`, so any local customization belongs in your own profile copy, not in the repository file.
- It is a single-maintainer project. 445 stars, commits and releases concentrated on one person, and a changelog that moves in small point releases (0.1.40 through 0.1.45 in October 2026 alone), so pin a version if you depend on exact flag behaviour.
- The benchmark that justifies the whole design is self-published, on 14 tasks, with the author's own harness and judge. It is directionally credible and independently unverified.
- The skill is not user-invocable. It loads when the agent recognizes a browser task, and it deliberately tells the agent to skip Chrome for anything a plain `fetch` or `curl` handles, so your own routing rules may fight it.

## Related

- [Chrome DevTools MCP Skills - Browser Debugging & Automation Setup](/hermes/skills/catalog/chrome-devtools-mcp-skills-setup)
- [Agent Browser - Vercel Labs CLI for AI Agents Setup](/hermes/skills/catalog/agent-browser-setup)
- [Browser-Use Automation - AI Browser for Anti-Bot Sites Setup](/hermes/skills/catalog/browser-use-automation-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Read `--help`, not the skill. The stub says this outright: installed copies go stale, and the CLI is the only current source for commands, flags and environment variables. Treat any blog post (including this one) as a map, not a manual.
- Pin a named session per worker. `CHROME_DEVTOOLS_AXI_SESSION=worker-1` gives each agent its own bridge, port and state, which prevents two agents from fighting over one selected tab. Do not export `CHROME_DEVTOOLS_AXI_PORT` globally, because it forces every session onto one port and the second one fails to bind.
- Set `CHROME_DEVTOOLS_AXI_IDLE_TIMEOUT_MS` on shared hosts. A bridge otherwise runs until `chrome-devtools-axi stop`, and a cron or subagent that dies without stopping leaves a detached browser behind.
- Prefer `--no-snapshot` on `newpage` and `selectpage` when the next step is `eval`. Capture still runs, refs stay fresh, and you skip printing a tree the agent will not click.
- Write large artifacts to paths the agent already knows. `screenshot`, `heap`, `network-get --response-file`, `lighthouse --output-dir` and `perf-stop --file` all resolve relative paths against the directory you invoked from, not the bridge's, and a failed write exits non-zero rather than printing success.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
