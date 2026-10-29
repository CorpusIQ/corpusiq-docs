---
title: "Playwright Skill - Code-First Browser Automation Setup"
description: "Playwright Skill: 7.1K combined installs. lackeyjb's MIT skill writes and runs real Playwright scripts, with dev-server detection and reusable tests."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/playwright-skill-setup/"
robots: "index,follow"
last_updated: "2026-10-29"
tags: ["hermes skill", "agent skill", "skill setup", "browser automation", "playwright", "testing"]
---

# Playwright Skill - Setup Guide

**Source:** [lackeyjb/playwright-skill](https://www.skills.sh/lackeyjb/playwright-skill) via skills.sh - 7.1K combined installs across 1 indexed listing; snapshot 2026-10-29 (Oct 29 morning sweep)

**GitHub:** [lackeyjb/playwright-skill](https://github.com/lackeyjb/playwright-skill) - 3,250 stars, MIT License, branch main, last pushed 2026-08-14; one skill at `skills/playwright-skill/` inside a Claude Code plugin root (`.claude-plugin/`), shipping `SKILL.md`, `run.js`, `lib/helpers.js`, `API_REFERENCE.md`, `package.json`, a `tests/` directory and a CI workflow

**Category:** Browser automation and end-to-end testing for coding agents

**Quality Tier:** 🟡 Trusted (individual publisher, MIT LICENSE in-repo, and a real CI story: unit tests plus a skills-ref validation step on Node 20, 22 and 24; Gen Agent Trust Hub and Socket Pass, Snyk Warn W011, and green is reserved for official publishers)

Playwright Skill is a general-purpose automation skill from an individual maintainer, lackeyjb, now at version 5.0.0 and built with Claude Code. The pitch is deliberately narrower than a browser wrapper: the agent writes a real Playwright program for the request in front of it, so loops, multiple contexts, network interception, assertions, video and a script you keep and rerun are all in scope. The README contrasts it with Microsoft's `@playwright/cli` for straightforward interactive browsing and `playwright-mcp` for tool-based control with accessibility snapshots, and positions this project as the code-first option when the automation itself is the useful artifact.

The mechanics are small and legible. A portable executor, `run.js`, runs file-based or inline scripts with stable module resolution and preserves exit codes. A `lib/helpers.js` module offers six functions: `detectDevServers`, `getExtraHeadersFromEnv`, `launchBrowser`, `createContext`, `handleCookieBanner` and `takeScreenshot`. For localhost work the agent detects running dev servers before it writes a URL, uses the only result automatically, asks when there are several, and offers to start a server when there are none. The browser is visible by default, scripts land in the operating system temp directory as `playwright-test-*.js` unless you ask to keep them, and a longer `API_REFERENCE.md` covers network mocking, auth state, video, visual checks, device emulation and CI patterns without loading on every turn.

## Installation

The README documents four routes and recommends Vercel's `skills` CLI, which installs into the native location for each supported agent. The `--skill` flag matters here because the skill sits inside a plugin root rather than at the repository root:

```bash
npx skills add lackeyjb/playwright-skill --skill playwright-skill --global --yes
```

Drop `--global` to install for the current project only, or add `--agent` with one or more agent IDs. The README's second route is the Claude Code plugin, for automatic updates and team distribution:

```bash
/plugin marketplace add lackeyjb/playwright-skill
/plugin install playwright-skill@playwright-skill
```

Hermes is not one of the agent IDs the CLI documents, so the predictable route is the README's Option 3 fallback: install the directory that contains `SKILL.md` into your client's documented skill directory. Because the skill needs `run.js`, `lib/` and `package.json` alongside `SKILL.md`, fetch the whole directory rather than a single file:

```bash
mkdir -p ~/.hermes/profiles/corpusiq/skills/playwright-skill
curl -sL -o /tmp/playwright-skill-main.tar.gz \
  https://github.com/lackeyjb/playwright-skill/archive/refs/heads/main.tar.gz
tar -xzf /tmp/playwright-skill-main.tar.gz -C /tmp
cp -R /tmp/playwright-skill-main/skills/playwright-skill/. \
  ~/.hermes/profiles/corpusiq/skills/playwright-skill/
cd ~/.hermes/profiles/corpusiq/skills/playwright-skill && npm run setup
```

That setup step is the one the README and SKILL.md both prescribe: `npm run setup` expands to `npm install && npx playwright install chromium`. SKILL.md also offers `npm run install-all-browsers` when Firefox or WebKit is required. Node.js 20 or newer is a hard prerequisite, and the first setup needs network access to download Playwright and the Chromium build. Before running scripts, export the directory containing `SKILL.md`, since the executor and helper paths are built from it:

```bash
export SKILL_DIR=~/.hermes/profiles/corpusiq/skills/playwright-skill
export PW_ARTIFACT_DIR=~/playwright-artifacts
node "$SKILL_DIR/run.js" tests/smoke.js
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| playwright-skill | 7056 | Writing and running a real Playwright program for whatever the request needs: dev-server detection before a URL is guessed, reusable scripts in a temp path or a preserved `PW_SCRIPT_DIR`, visible browser by default, screenshots at chosen viewports, login flows against credentials you supply, cookie-banner handling, extra HTTP headers from env, connecting to an existing Chrome over CDP, and a progressive-disclosure API reference for network mocking, auth state, video, visual checks, device emulation and CI. |

No indexed listings fall below the threshold.

## Why This Matters for Hermes Agents

Hermes already drives a browser through its own tooling, and that covers most interactive work, but it does not give you a durable artifact. This skill is aimed at the other half of the job: the automation worth keeping, in a language with a full assertion library, exited with a real status code so CI and cron can act on it. The child-process executor in 5.0.0 preserves exit codes specifically, which is what makes a generated script usable as a check rather than a transcript of a run.

The dev-server detection step is the part that saves the most time in practice. A localhost port guess produces the most common failure in agent browser work, and asking the environment which servers are listening before writing the URL removes it. The visible-browser default is also the right call for verification work, since a headed run plus a full-page screenshot at two viewports is easy to inspect and easy to hand to a reviewer.

The honest boundary is that this is a code generator with a thin helper layer, not a framework. There is no page-object scaffolding, no test runner of its own, no reporting layer and no retry policy beyond what the generated script does. You get Playwright, a way to run it, and a few conveniences, which is more than enough when the automation is the deliverable and not when you want a managed test suite.

One behaviour deserves flagging before adoption: the skill advises reusing an existing Chrome session over CDP, which inherits that browser's cookies and extensions. That is powerful for authenticated checks and it is exactly the wrong default for anything touching real accounts.

## Usage

| You say | What happens |
|---|---|
| "Test the homepage on localhost" | The agent runs `detectDevServers()` before writing a URL, uses the single result automatically, asks which one when several are listed, and offers to start a server when none is listening. |
| "Take screenshots of the dashboard on mobile and desktop" | A script loops two viewports, 1440x900 and 390x844, and writes full-page screenshots named for each viewport into `PW_ARTIFACT_DIR`, defaulting to the OS temp directory. |
| "Verify the signup flow" | A login script fills `getByLabel('Email')` and `getByLabel('Password')` with credentials you supply, clicks the sign-in button by accessible role, waits for `**/dashboard`, then waits on a dashboard heading before reporting success. |
| "Check for broken links on the site" | The agent writes a custom Playwright script rather than picking a pre-built one, then reports the actions taken, the failures, and the artifact paths, and is instructed not to claim success without checking the resulting page. |
| "Run this snippet once, no file" | Inline execution through `node "$SKILL_DIR/run.js" -e "..."`, which exits as soon as the snippet settles, so the snippet has to close the browser itself. |
| "Keep that login script, I want to rerun it" | `PW_SCRIPT_DIR=./playwright-tests` copies the file-based script before execution and adds a timestamp when a filename already exists. |
| "Attach to my already logged-in Chrome" | `chromium.connectOverCDP('http://127.0.0.1:9222')` reuses the cookies and extensions of a Chrome started with remote debugging, which the SKILL.md warns carries that session's access. |

## Verification

The raw SKILL.md path below returned 200 on the main branch when this guide was written:

```bash
curl -sL -o /dev/null -w "%{http_code} SKILL.md\n" \
  https://raw.githubusercontent.com/lackeyjb/playwright-skill/main/skills/playwright-skill/SKILL.md
```

Confirm the directory landed with the files the executor needs, not just the markdown. The frontmatter names the skill `playwright-skill`, version 5.0.0, with `license: MIT` and an `allowed-tools` line of `Bash(node:*) Bash(npm:*) Read Write`:

```bash
ls -l ~/.hermes/profiles/corpusiq/skills/playwright-skill/
head -6 ~/.hermes/profiles/corpusiq/skills/playwright-skill/SKILL.md
```

A good copy shows `SKILL.md`, `run.js`, `lib/helpers.js`, `API_REFERENCE.md`, `package.json` and `package-lock.json`. Then check the runtime, which is where installs actually fail: `node --version` should report 20 or higher, and `node "$SKILL_DIR/run.js" -e "console.log('ok')"` should print `ok` without a module resolution error.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-29) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| playwright-skill | Pass | Pass | Warn W011 |

One listing was sampled: Gen Agent Trust Hub and Socket both pass it, and Snyk returns a warning rather than a failure. W011 is a warning code, and in a skill like this one it points at the class of risk where a package fetches its runtime and browser binaries from the network at setup time and then executes code written on the fly, instead of running only pinned, vendored files. The verdict table records the code and not a finding detail, so read the Snyk page for the specific sink before you rely on the number.

What that class means concretely here. `package.json` declares a single dependency, `playwright` at `^1.62.0`, which is a caret range and not an exact pin, so `npm install` inside `npm run setup` can resolve a newer release than the one the author tested. The same setup step downloads a Chromium build, and `run.js` then executes JavaScript the agent wrote. A lockfile does ship in the repo and CI uses `npm ci` against it, so installing with `npm ci` instead of `npm install` gives you the tested resolution.

No installer in this repository pipes curl to bash. Installation is the `skills` CLI, the Claude Code plugin manager, or a copy plus `npm run setup`, and setup is `npm install` followed by `npx playwright install`. The two behaviours worth a review pass are the declared tool scope, `Bash(node:*)`, `Bash(npm:*)`, `Read` and `Write`, which allows the agent to run arbitrary Node and npm commands, and the CDP advice, which the SKILL.md itself limits by saying not to use it for secrets unless you explicitly ask.

## Limitations

- Snapshot data, verified 2026-10-29: 7056 combined installs across 1 indexed listing; 3250 GitHub stars; MIT License; last pushed 2026-08-14. Counts drift over time.
- Single-maintainer project. The author field is lackeyjb in both the SKILL.md metadata and the plugin manifest, so cadence, security response and the 5.0.0 breaking changes all rest on one person, with no organisation behind the repository.
- Runtime cost is real: Node.js 20 or newer, a network install of Playwright and Chromium at setup, and a headed browser unless `PW_HEADLESS=true` or there is no display. Headless servers need that variable set explicitly.
- The skill is nested at `skills/playwright-skill/` under a plugin root, so any installer that expects a `SKILL.md` at the repository root will miss `run.js`, `lib/` and `package.json`. This guide's pack records 3 owner rows across all sources but only 1 indexed listing carrying an install count, so treat the 7.1K figure as one listing's total and not the publisher's.
- The SKILL.md is internally inconsistent about one variable. The path resolution section says to export `SKILL_DIR`, while the Helpers example reads `process.env.PW_SKILL_DIR`. Neither is set by Hermes, so substitute literal paths or export both.
- Version 5.0.0 removed the helper functions that duplicated Playwright actions, removed stdin execution, and changed `launchBrowser()` so `--no-sandbox` is only added for Chromium when running as root. Tutorials written before August 2026 will reference helper calls and a stdin route that no longer exist.

## Related

- [TestDino Playwright Skills - 79-Guide Testing Suite Setup](/hermes/skills/catalog/testdino-playwright-skill-setup)
- [Playwright Social Media Automation - API-First Browser Fallback Setup](/hermes/skills/catalog/playwright-social-media-automation-setup)
- [LiarJS Skills - Browser Fingerprint & Playwright Stealth Setup](/hermes/skills/catalog/liarjs-fingerprint-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Pass `--skill playwright-skill` to the installer, and check that `run.js` and `lib/helpers.js` arrived. A SKILL.md on its own cannot execute anything.
- Export `SKILL_DIR` and `PW_ARTIFACT_DIR` in the profile environment rather than per command. Screenshots then land somewhere you can inspect and clean up, instead of scattering across the temp directory.
- Keep the visible browser for verification runs. A headed run with a screenshot at 1440x900 and at 390x844 is the cheapest evidence that a change worked, and it costs nothing to ask for both viewports in one script.
- Reach for `PW_SCRIPT_DIR` the second time you run something. The first run can live in temp, but any check you plan to repeat belongs under version control with its output going to `PW_ARTIFACT_DIR`.
- Install with `npm ci` against the shipped lockfile when this runs in CI or cron, so the Playwright version matches the one the repository actually tested on Node 20, 22 and 24.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
