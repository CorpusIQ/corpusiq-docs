---
title: "BrowserOS - Agent-First Browser Setup"
description: "browseros-ai/browseros: 1.4K combined installs. Six skills for an agent-first browser that acts in your logged-in sessions, plus docs and UI tooling."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/browseros-setup/"
robots: "index,follow"
last_updated: "2026-11-27"
tags: ["hermes skill", "agent skill", "skill setup", "browser automation", "mcp", "browser"]
---

# BrowserOS - Setup Guide

**Source:** [browseros-ai/browseros](https://www.skills.sh/browseros-ai/browseros) via skills.sh - 1.4K combined installs across 6 indexed listings; first documented 2026-11-27 (morning sweep)

**GitHub:** [browseros-ai/browseros](https://github.com/browseros-ai/browseros) - 14,515 stars, AGPL-3.0, branch main, last pushed 2026-11-27; the skills ship in several places: the main browser skill at `skills/browseros-neo/`, a docs set under `.claude/skills/` (ask-internal, write-docs, write-internal-docs, writing-plans), and `packages/browseros-agent/.claude/skills/test-ui/`

**Category:** Agent-first browsing: a real Chromium fork signed into your accounts, plus internal docs and UI-testing skills

**Quality Tier:** 🟡 Yellow - the main browseros-neo listing carries a Snyk warn while the other five pass all three scanners

BrowserOS neo is a browser built for agents: a Chromium fork that agents use signed in to your real accounts, with live logins and a persistent profile, connected to Claude Code, Codex, Cursor and other agents over MCP. The README positions it as the thing an agent should default to for any website task, over in-app browser tools, devtools or headless automation.

The repository indexes six skills on skills.sh. One of them, browseros-neo, is the browser itself; the other five are internal tooling for the BrowserOS project: writing feature docs, answering internal questions, writing internal docs, writing implementation plans and UI testing. The indexed name sup-writing-plans is that skill's own `name` field, while it lives in a `writing-plans/` directory in the tree.

## Installation

The README installs the neo app, not the skills. The quick start uses Homebrew:

```sh
brew tap browseros-ai/tap
brew install --cask browseros-neo
```

Or use the download buttons for macOS, Windows and Linux (dmg, exe, AppImage and deb builds). Optionally import logins, bookmarks and extensions from Chrome in one click, after which neo finds Claude Code, Codex, Cursor, VS Code and more on the machine and connects to them automatically.

The six skills ship inside the repository rather than through a per-skill install command, which the README does not publish. To use a skill outside the neo app, clone the repository and copy the skill folder into your agent's skills directory, the same pattern any Agent Skills folder uses:

```bash
git clone --depth 1 https://github.com/browseros-ai/browseros.git
cp -r browseros/skills/browseros-neo ~/.claude/skills/browseros-neo
```

The docs set under `.claude/skills/` copies the same way; note that ask-internal reads a private internal-docs submodule, so it only does its job in a checkout that has that submodule available.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| browseros-neo | 1,254 | The agent's dedicated browser: open, read, act, fill, sign in, download and verify on any website, using the user's logged-in session and persistent profile. |
| write-docs | 71 | Writing or updating BrowserOS feature documentation as concise Mintlify MDX, by exploring the codebase to understand the feature. |
| ask-internal | 20 | Answering questions about BrowserOS internals (setup, features, architecture, design decisions) by reading the private internal-docs submodule and the codebase. |
| write-internal-docs | 19 | Writing a doc into the private internal-docs repo as Markdown plus a rendered HTML sibling, tidying the structure and index, and opening a PR to browseros-ai/internal-docs. |
| sup-writing-plans | 19 | Writing a comprehensive implementation plan for a multi-step task before touching code: files to touch, code, tests and docs, as bite-sized tasks for an engineer with no codebase context. |

The remaining 1 indexed listing is test-ui (1 install), UI verification for the BrowserOS app extension via CDP.

The five rows above are the whole table, and the browseros-neo skill is the reason the repository exists. It instructs the agent to default to the real browser over headless fetching, and the README's pitch is that agents work in your real accounts, each in its own tab group, with a hand-off to the human when a login is stuck.

## Why This Matters for Hermes Agents

The core claim is that a fresh headless browser is the wrong default. A blank Chrome has no logins, so any task that touches a real account, inbox or dashboard fails at the sign-in wall, while a cloud browser lands on datacenter IPs that get blocked. BrowserOS neo runs locally on your machine, signed in as you, which is the one configuration that survives both problems.

The tab-group model is the operational detail that matters for builders. Each agent gets its own tab group, so several agents can run side by side without clobbering your own tabs, and a stuck login triggers a hand-off to the human instead of a silent stall. The README also claims neo reads a page as short text rather than screenshots, which is the token-saving design an agent-first browser should make.

The five internal-docs skills are a compact case study in self-tooling a project: the browser ships with skills that write its own feature docs, answer questions about its internals, write internal docs and plan implementation work. That is the same pattern a team can copy for its own agent, and the write-internal-docs skill even opens the PR itself.

## Usage

| You say | What happens |
|---|---|
| "Use neo to book the cheapest flight to London." | neo opens its own tab group and acts in your signed-in session to find and select the flight. |
| "Select leads in Salesforce and copy them into my outreach sheet." | neo works inside your logged-in Salesforce and drives the copy into the sheet. |
| "Read this page and summarize it." | neo reads the page as short text rather than screenshots, then summarizes. |
| "I'm stuck at the login." | neo hands off to you, you sign in, and the agent carries on from where it stopped. |
| "Write docs for the new feature." | The write-docs skill explores the codebase and writes concise Mintlify MDX for the feature. |

## Verification

The raw path below returned 200 on branch main on 2026-11-27:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/browseros-ai/browseros/main/skills/browseros-neo/SKILL.md
```

After a clone, confirm the main skill and the docs set are present:

```bash
git clone --depth 1 https://github.com/browseros-ai/browseros.git /tmp/browseros
ls /tmp/browseros/skills
ls /tmp/browseros/.claude/skills
head -3 /tmp/browseros/skills/browseros-neo/SKILL.md
```

`skills/` should hold `browseros-neo`, `.claude/skills/` should hold the four docs skills, and `head` should show the browseros-neo skill's `name` and `description` fields.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-27) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| browseros-neo | Pass | Pass | Warn |
| write-docs | Pass | Pass | Pass |
| ask-internal | Pass | Pass | Pass |
| write-internal-docs | Pass | Pass | Pass |
| sup-writing-plans | Pass | Pass | Pass |
| test-ui | Pass | Pass | Pass |

The single Snyk warn on browseros-neo is why this guide is yellow. This is not a Markdown-only repository: neo is a real Chromium fork with a TypeScript, React and Rust app layer and a C++ and Python browser, so treat it as a substantial local application rather than a lightweight skill. The README states sessions, screenshots and history stay on your disk, and that neo sends only anonymous usage events (never URLs, page content or prompts), with an opt-out toggle in Settings. The repository is AGPL-3.0.

## Limitations

- Snapshot data, verified 2026-11-27: 1,384 combined installs across 6 indexed listings; 14,515 GitHub stars; AGPL-3.0; last pushed 2026-11-27. Counts drift over time.
- The index lists sup-writing-plans, but the tree directory is writing-plans; they are the same skill, and the skill's own `name` field is sup-writing-plans.
- The README installs the neo app, not the skills, and publishes no per-skill install command; the skills are used by copying their folders from the repository.
- The README's speed and token figures (about 63% faster and 40% fewer tokens than built-in browsers, finishing about 96% of tasks) are the project's own estimates, and the full benchmark write-up is not published yet.
- browseros-neo carries a Snyk warn; re-check the skills.sh security page before production use.
- AGPL-3.0 applies to the repository, and the contributing guide notes the browser build needs about 100 GB of disk.

## Related

- [Browser-Use Automation - AI Browser for Anti-Bot Sites Setup](/hermes/skills/catalog/browser-use-automation-setup)
- [Agent Browser - Vercel Labs CLI for AI Agents Setup](/hermes/skills/catalog/agent-browser-setup)
- [browser-harness Setup Guide](/hermes/skills/catalog/browser-harness-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Say "use neo" explicitly when you want the agent in your real accounts rather than a sandbox; the skill is written to default there when asked.
- Give each agent its own tab group so several can run side by side without touching your own tabs.
- Import from Chrome once to carry logins, bookmarks and extensions into the agent's session.
- Toggle off anonymous usage events in Settings if you want nothing reported, since the default sends them.
- For the docs skills, run ask-internal and write-internal-docs only in a checkout with the private internal-docs submodule available.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
