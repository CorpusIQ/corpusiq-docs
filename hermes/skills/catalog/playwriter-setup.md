---
title: "Playwriter - Agent Control of Your Own Chrome"
description: "remorses/playwriter on skills.sh: 5.9K combined installs across 1 listing; drive your own logged-in Chrome with Playwright snippets via CLI or MCP."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/playwriter-setup/"
robots: "index,follow"
last_updated: "2026-11-05"
tags: ["hermes skill", "agent skill", "skill setup", "browser automation", "chrome", "playwright"]
---

# Playwriter - Setup Guide

**Source:** [remorses/playwriter](https://www.skills.sh/remorses/playwriter) via skills.sh - 5.9K combined installs across 1 indexed listing; first seen 2026-11-05 (Nov 5, 2026 evening sweep, first documentation)
**GitHub:** 4,061 stars, MIT, last pushed 2026-11-03, one SKILL.md at `skills/playwriter/SKILL.md`, plus an `AGENTS.md` at the repository root
**Category:** Browser control for agents: Playwright snippets run against your logged-in Chrome through a CLI or MCP server
**Quality Tier:** 🟡 Caution - the single sampled skill is Warned by both Gen Agent Trust Hub and Snyk; MIT, 4,061 stars.

Playwriter is the opposite bet to every other browser tool. Where Playwright MCP and agent-browser start a fresh browser with a clean profile, Playwriter attaches to the Chrome you are already using, through a Chrome extension, and runs Playwright code inside it. Logins, cookies and extensions are simply there. The README's comparison table puts it in one line: other browser MCPs spawn a new Chrome, which means no logins, no extensions, twice the memory and an automation profile that bot detectors recognise immediately.

The second design decision is the API surface. Instead of dozens of dedicated tools, Playwriter exposes one `execute` tool that runs JavaScript in a stateful sandbox with `context`, `state`, `require` and native `import()` in scope. An agent that already writes Playwright does not have to learn a tool schema; it writes a script. State persists between calls, so a scrape can accumulate results across several turns instead of returning everything at once.

The relay is local by default: a WebSocket server on `localhost:19988` that the extension connects to, which then exposes CDP to the CLI or the MCP client. Tabs are controlled only after you click the extension icon on them, and Chrome shows its automation banner on controlled tabs.

## Installation

The README's route is four steps. Install the extension from the Chrome Web Store, then click the extension icon on a tab so it turns green when connected. Then install the CLI:

```bash
npm i -g playwriter
```

Then install the skill so the agent knows how to drive it:

```bash
npx -y skills add https://playwriter.dev -g -y
```

A first run looks like this, with the session id chosen by the CLI:

```bash
playwriter session new
playwriter -s 1 -e 'state.page = await context.newPage(); await state.page.goto("https://example.com")'
playwriter -s 1 -e 'console.log(await snapshot({ page: state.page }))'
```

For clients that speak MCP rather than shell, the README points at `MCP.md`, which configures a server through `npx` and can be auto-installed:

```bash
npx -y @playwriter/install-mcp playwriter@latest
```

The MCP exposes two tools, `execute` to run Playwright code and `reset` to reconnect when the connection drops. There is no `page` in scope by default: create a tab with `context.newPage()` and store it in `state`, or find an existing tab by URL.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| playwriter | 5,905 | Driving the user's own logged-in Chrome with Playwright snippets in a stateful sandbox, through the CLI or the MCP `execute` tool |

No indexed listings fall below the 500-install threshold; the single listing appears above.

## Why This Matters for Hermes Agents

Most useful web work sits behind a login. A support queue, a dashboard, an internal admin panel, a supplier portal: none of them are reachable by an agent that starts from a clean profile, and asking a human to export data by hand is exactly the task the agent was meant to remove. Playwriter's answer is to borrow the session that already exists, which turns a credential problem into a click on an extension icon.

Playwright as the interface is the second gain. A tool-per-action browser MCP spends context on schemas and forces the agent to express loops and conditions as sequences of calls. An `execute` tool takes real JavaScript, so an agent can paginate with a `while` loop, collect rows into an array, and decide what to do next inside one script. The README's own comparison makes this point about context usage and about the model already knowing the API.

State persistence changes the shape of a long task. Because `state` survives between calls, an agent can open a page in one call, attach a response listener in another, and read the collected requests in a third. That is closer to how a person works with a browser than a single-shot snapshot and click.

The debugger, network interception, live code editing and accessibility-labelled screenshots are extras that matter when automation fails. An agent that can set a breakpoint or read a page's network traffic diagnoses a broken flow instead of retrying it.

## Usage

| You say | What happens |
|---|---|
| "Log into the supplier portal and pull this month's invoices" | The agent uses your existing Chrome session, which is already logged in |
| "Check what the site calls when I click this button" | Attaches a response listener in one call and reads the collected URLs in the next |
| "Screenshot this page with labels I can click" | Accessibility-labelled screenshot returns aria-ref selectors for follow-up clicks |
| "Fill this form across three tabs" | Sessions share tabs, so one script can move between them |
| "This flow keeps timing out, find out why" | Sets a breakpoint through CDP and lists loaded scripts |
| "Keep the scrape in its own window" | Starts a session with a named tab group the user can move or collapse |
| "Patch this minified bundle and retest" | Live code editing through CDP, without a rebuild |

## Verification

The SKILL.md tells the agent to load the full documentation once per session, and that is also the fastest check that the CLI is working:

```bash
playwriter skill
```

It prints the complete guide covering sessions, selector strategy and the rules for avoiding timeouts. Then confirm sessions are visible:

```bash
playwriter session list
```

That shows live sessions with their state keys and tab group. Before installing, read the skill file itself:

```bash
curl -fsSL https://raw.githubusercontent.com/remorses/playwriter/main/skills/playwriter/SKILL.md | head -4
```

If every page returns `about:blank`, the README's known-issues list is explicit: restart Chrome, because the failure is in the `chrome.debugger` API rather than in Playwriter.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-05) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| playwriter | Warn | Pass | Warn |

Read the two Warns as a description of what the tool is rather than a defect: an agent with Playwright access to your real browser can read every page you are logged into, and no scanner can certify that as safe. The README's own controls are a localhost-only relay, origin validation against the extension ID, tab scope limited to tabs you clicked the extension on, and a visible automation banner.

Two things deserve explicit policy. Remote control is not a sandbox: the README says the remote agent gets the same access as a local one, and the denylist only blocks whole-profile cookie APIs and cache clears. Share a remote id only with an agent you would hand your browser to. Separately, the relay sends anonymous usage statistics to Strada by default, covering event names, a random install id, version, OS, session kind and hourly execute counts, never code, URLs or page content. Opt out with `PLAYWRITER_TELEMETRY=0` or `DO_NOT_TRACK=1` and then run `playwriter serve restart`.

## Limitations

- Snapshot data, verified 2026-11-05: 5,905 combined installs across 1 indexed listing; 4,061 GitHub stars; MIT; last pushed 2026-11-03. Counts drift over time.
- It needs Chrome and the extension. On a headless host the README's `playwriter browser start` path launches Chrome for Testing with a bundled extension, which works but is not your logged-in profile, so the main advantage disappears there.
- One skill, one file. All guidance ships in `skills/playwriter/SKILL.md`, and the file tells the agent to call `playwriter skill` and read the output in full once per session.
- Tabs are shared between sessions while state is isolated. Two agents on the same browser can see each other's tabs, which is a coordination problem the CLI does not solve.
- Telemetry is on by default. In a regulated environment, set the environment variable before the relay ever starts.
- The README lists a Chrome bug where the browser can switch to light mode on connect, and another where all pages return `about:blank` until Chrome restarts.

## Related

- [Playwright Skill - Code-First Browser Automation Setup](/hermes/skills/catalog/playwright-skill-setup)
- [Browser-Use - AI-Powered Browser Automation](/hermes/skills/catalog/browser-use-automation-setup)
- [Chrome DevTools AXI - Agent Browser CLI Setup](/hermes/skills/catalog/chrome-devtools-axi-setup)

## Pro Tips

- Use single quotes around `-e`. The README calls this out because bash otherwise eats `$`, backticks and backslashes in your JavaScript.
- Always pass `-s`. Each session has isolated state, and a call without a session id is a call in the wrong context.
- Name the tab group after the job. A group called `scrape` can be moved to its own window, which keeps a long run from disturbing whatever the user is doing.
- Find existing tabs by URL rather than opening new ones. `context.pages()` lists tabs other sessions opened, so match on the exact URL you need.
- Solve a captcha by disconnecting the extension, not by fighting it. The README's comparison tables make that the intended escape hatch on a real browser.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
