---
title: "ego lite - AI Agent Browser and ego-browser Skill Setup"
description: "citrolabs/ego-lite: 13.2K combined installs. A Chromium browser for humans and AI agents, with parallel Spaces and the ego-browser automation skill."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/ego-lite-setup/"
robots: "index,follow"
last_updated: "2026-10-28"
tags: ["hermes skill", "agent skill", "skill setup", "browser automation", "chromium", "agent browser"]
---

# ego lite - Setup Guide

**Source:** [citrolabs/ego-lite](https://www.skills.sh/citrolabs/ego-lite) via skills.sh - 13.2K combined installs across 3 indexed listings; snapshot 2026-10-28 (Oct 28 evening sweep)

**GitHub:** [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) - 20,467 stars, MIT, branch main, last pushed 2026-10-29; 3 `SKILL.md` directories in the clone, at `skills/ego-browser/`, `.github/dev-skills/ego-lite-simplify/` and `package/ego-browser/skill-body/`

**Category:** Agent browser shipped as a desktop app, plus the skill that drives it

**Quality Tier:** 🟡 Beta - 20,467 GitHub stars and an MIT repository behind real desktop installers for Apple Silicon, Intel and Windows, held at yellow because the skill almost everyone installs carries a Gen Agent Trust Hub Fail and the app it drives is closed source

ego lite from CitroLabs is a Chromium browser built for two users at once: you and your agents. Each agent runs its browser tasks in its own Space, an isolated workspace inside the same browser, so your tabs and your mouse stay where you left them while several agents work in parallel. The browser is distributed as a desktop app (Apple Silicon and Intel `.dmg`, Windows `.exe`), and Linux is listed on the project roadmap.

The skill is the connection layer. `ego-browser` exposes the browser to any agent CLI as in-page JavaScript tools, so a multi-step task becomes one script calling snapshot, fill, click, wait, navigate and capture, rather than a long loop of one-off CLI calls. On first launch the app asks whether to migrate your Chrome data, and if you agree the agent inherits your existing logins, cookies, extensions and bookmarks, which is the whole point of the product and also the thing worth reading the Security section about.

## Installation

The app and the skill install separately. Download the app for your platform from the repository README, then open it:

```text
macOS Apple Silicon: https://cdn.ego.app/setup/macos/arm64/egolite-Y7MbxKIuhzFB.dmg
macOS Intel:         https://cdn.ego.app/setup/macos/x64/egolite-Y7MbxKIuhzFB.dmg
Windows x64:         https://cdn.ego.app/setup/windows/x64/egoliteSetup-Y7MbxKIuhzFB.exe
```

The README states that installing the app also adds the `ego-browser` skill to every agent's skills directory on the machine. To install just the skill through the skills.sh CLI:

```bash
npx skills add citrolabs/ego-lite
```

The README also documents a third route, pasting the following into an agent and letting it drive the install:

```text
Set up ego lite for me: https://github.com/citrolabs/ego-lite

Read `skills/ego-browser/references/install.md` and follow the steps to install ego lite.
```

On macOS that install path runs `skills/ego-browser/scripts/install.sh`, which downloads the DMG for your CPU architecture, installs `ego lite.app` into `/Applications` (falling back to `~/Applications`), strips the quarantine attribute and launches the app. Windows has no script: download the installer from https://lite.ego.app/ and run it.

The skill itself is a bootstrap. Before the first task it tells the agent to run `ego-browser skill`, which prints the usage guide matching the installed app version; after `ego-browser upgrade`, or when the printed guide says so, run it again. The `ego-browser` command is provided by the app, not by the cloned repository, so the skill is inert until the app is installed and onboarding has registered the command on the PATH.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| ego-browser | 13209 | The connection layer between an agent CLI and ego lite: open a page in the agent's own Space, take a structured Snapshot, then fill, click, wait, navigate and capture across sign-in flows, form fills, data extraction, screenshots, web app testing and bug investigation. |
| ego-lite-simplify | 3 | A repository maintenance skill for contributors, finding and implementing evidence-backed simplifications in the ego-lite codebase: dead code, duplicated state or APIs, speculative abstractions and unnecessary compatibility layers. Not needed to use the browser. |
| ego-cli | 4 | Indexed listing with no matching skill directory in the current tree; the repository does ship an `ego-browser` command-line binary, so confirm what the listing resolves to before installing it. |

No indexed listings fall below the threshold; all 3 appear above.

## Why This Matters for Hermes Agents

Browser work is where a Hermes run most often stalls: the page is real, but the agent has no session on it, so the task turns into a login flow it cannot complete. ego lite solves that by giving the agent the browser you already signed into. Accept the Chrome migration at first launch and every Space starts with your cookies and logins, which is the difference between an agent that can read a dashboard behind auth and one that asks you for a password.

The isolation model fits multi-agent work. Each Space belongs to one agent or one task, several run at the same time, and the README's own example is ten parallel Spaces enriching ten leads while a second agent scrapes five competitor sites. For Hermes, that maps onto parallel subagents sharing one browser without racing each other's tabs, which is something a single shared browser session cannot offer.

The code-based interface cuts cost per task. The agent writes one JavaScript snippet against snapshot, fill, click and the rest, instead of executing two commands, reading output, then executing two more. The vendor benchmark reports 47% to 63% faster completion across 31 complex tasks against four other tools; treat that as a vendor claim, but the shape of the saving, fewer tool calls and fewer tokens per task, is consistent with how a scripted page interaction actually behaves.

Data stays local. Browsing data, cookies and history stay on the device, and the README describes deliberately narrow collection, such as whether ego lite is set as the default browser. The trade to accept knowingly is that the browser binary doing the automation is not the MIT-licensed repository, so the skills install and the app install are two separate trust decisions.

## Usage

| You say | What happens |
|---|---|
| "Follow @ego_agent on x.com for me" | The agent loads the ego-browser skill, opens the page in its own Space, takes a Snapshot of the page as structured text, acts on it, and reports back while your own tabs stay untouched. |
| "Sign into the billing dashboard and download last month's invoices" | The agent works inside a Space that already carries your migrated login, navigates to the invoices view, clicks through the period selector and captures the files. |
| "Fill this supplier form with our company details and submit it" | Snapshot identifies the fields, fill writes each value, click submits, and the agent verifies the confirmation page before reporting success. |
| "Scrape the pricing page from these five competitor sites in parallel" | Five Spaces run at once, one per site, each agent extracting structured text, with no collisions and no stolen tabs. |
| "Test the checkout flow on our staging site and screenshot every step" | The agent drives the flow as a user would, captures a screenshot at each step, and reports the step where behavior diverged from expectation. |
| "Something looks wrong on our signup page, reproduce and diagnose it" | The skill's own scope covers web app testing, dogfooding, QA and bug investigation, so the agent reproduces the issue in a Space and records the page state at failure. |

## Verification

All five URLs below returned 200 on branch main when this guide was written. Probe them before installing, and read the first one: it is the whole contract between your agent and the browser.

```bash
for p in skills/ego-browser/SKILL.md \
         skills/ego-browser/references/install.md \
         package/ego-browser/skill-body/SKILL.md \
         .github/dev-skills/ego-lite-simplify/SKILL.md; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/citrolabs/ego-lite/main/$p"
done
```

- https://raw.githubusercontent.com/citrolabs/ego-lite/main/skills/ego-browser/SKILL.md
- https://raw.githubusercontent.com/citrolabs/ego-lite/main/skills/ego-browser/references/install.md

After install, the check that matters is whether the app and the skill agree with each other. The skill prints the guide that matches the app version it finds, so an unknown command is the clearest signal of a version mismatch:

```bash
command -v ego-browser
ego-browser skill | tail -3
ls ~/.hermes/profiles/corpusiq/skills | grep -i ego
head -5 ~/.hermes/profiles/corpusiq/skills/ego-browser/SKILL.md
```

The printed guide ends with a line starting `[ego-browser:skill] end of guide`. If that line is missing, the output was truncated; the skill's own advice is to save it to a file and read it in parts, for example `ego-browser skill > "$TMPDIR/ego-browser-skill.md"`.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-28) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| ego-browser | Fail | Pass | Warn W011/W012 |
| ego-cli | Warn | Warn | Warn W011 |
| ego-lite-simplify | Pass | Pass | Pass |

The Fail sits on `ego-browser`, which accounts for 13,209 of the 13,216 combined installs, so this is the verdict on the thing you would actually install rather than on a peripheral listing. Read it as a consequence of what the product is: a browser binary plus network automation driven by your own logged-in sessions, with an install path that on macOS strips the quarantine attribute from the downloaded app. The two audit passes and one warning point the same way. Security tooling flags a moving binary and a live network surface far more readily than it flags a static skill file, and the one all-Pass listing (`ego-lite-simplify`) is the repository maintenance skill that never touches your browser.

What that means for adoption is a scoping decision rather than a blocker. Keep ego lite on a machine where the migrated Chrome profile holds only accounts you would let an automated agent act as, point it at the sites you actually need rather than accepting a full profile migration by reflex, and review `skills/ego-browser/SKILL.md` plus `references/install.md` before the first run, since the first one defines the whole tool surface the agent gets. Do not install it on a host whose browser profile carries your email, cloud console and payment accounts unless you have decided those are fair game for whatever task the agent is given.

## Limitations

- Snapshot data, verified 2026-10-28: 13216 combined installs across 3 indexed listings; 20467 GitHub stars; MIT license; last pushed 2026-10-29. Counts drift over time.
- The install index outruns the tree by one listing: `ego-cli` carries 4 installs and has no matching skill directory in the current clone, while `package/ego-browser/skill-body/SKILL.md` is a shipped copy of the runtime API guide rather than an indexed listing.
- The MIT license covers the repository. The browser it drives arrives as a desktop installer, and the repository's own `ego-lite-simplify` skill describes the `globalThis.ego` runtime as supplied by the closed-source app, so the app is a separate trust decision from the skill.
- macOS and Windows only. Linux is on the project roadmap with no published date, and `references/install.md` documents only a macOS install script plus a manual Windows installer.
- The skill does nothing without the running app. `ego-browser` is a command the app installs onto your PATH, so a fresh clone of the repository gives an agent a bootstrap file that points at a binary it cannot find.
- The performance figures (47% to 63% faster across 31 tasks, fewer tokens per task) come from the vendor's own Real-World Bench, run by the same judge against per-task rubrics. They are a vendor claim, not an independent result.

## Related

- [Agent Browser - Vercel Labs CLI for AI Agents Setup](/hermes/skills/catalog/agent-browser-setup)
- [Open Browser Use Skills - Browser Automation Setup](/hermes/skills/catalog/open-browser-use-setup)

## Pro Tips

- Run `ego-browser skill` yourself once before handing the browser to an agent. It prints the guide that matches the installed version, and you will spot a version mismatch in ten seconds that an agent would spend ten tool calls discovering.
- Treat the Chrome migration question as a configuration decision, not a convenience prompt. A dedicated profile with only the accounts an agent should reach costs you one login and removes the worst case from every later task.
- Read `skills/ego-browser/SKILL.md` with the app installed, then `package/ego-browser/skill-body/SKILL.md`. The first is the bootstrap and the second is the API surface, and only the pair tells you what the agent can actually call.
- One Space per task, not one Space per session. The whole isolation model depends on the agent not reusing a Space that a previous task left mid-flow on a different site.
- Ask the agent to report the Snapshot it acted on when a result looks wrong. Page state is the input, so a bad outcome is usually a stale or partial Snapshot rather than a bad click.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
