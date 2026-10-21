---
title: "TestDino Playwright Skills - 79-Guide Testing Suite Setup"
description: "testdino-hq/playwright-skill: 8.7K combined installs across 9 listings. 79 Playwright 1.64 guides for E2E, QA, CI, CLI automation, and migration."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/testdino-playwright-skill-setup/"
robots: "index,follow"
last_updated: "2026-10-20"
tags: ["hermes skill", "agent skill", "skill setup", "playwright", "testing", "browser automation"]
---

# TestDino Playwright Skills - Setup Guide

**Source:** [testdino-hq/playwright-skill](https://www.skills.sh/testdino-hq/playwright-skill) via skills.sh - 8.7K combined installs across 9 indexed listings; first seen Oct 20, 2026 (evening sweep)
**GitHub:** [testdino-hq/playwright-skill](https://github.com/testdino-hq/playwright-skill) (397 stars, MIT; pushed 2026-10-12; repo layout: one top-level SKILL.md index plus seven pack directories, each with its own SKILL.md and guide files)
**Category:** Testing & QA / Browser Automation
**Quality Tier:** 🟡 Beta - 397-star MIT collection from testdino.com; 79 guides pinned to Playwright 1.64, sampled verdicts mostly Pass with one LOW Socket anomaly and one MEDIUM Snyk prompt-injection warning on the CLI pack

TestDino Playwright Skill Guides is a 79-guide Playwright reference set published by [testdino.com](https://www.testdino.com), a Playwright test-management product. Every guide is written to be loaded on demand by a coding agent, and the top-level SKILL.md is the canonical index the agent reads first: it carries the Golden Rules (prefer `getByRole()` over CSS or XPath, never `page.waitForTimeout()`, isolate every test, keep `baseURL` in config, mock external services only) plus the architecture-decision material.

The content tracks current Playwright rather than generic training-data knowledge. The README documents 1.64 coverage including `locator.within()` for combining a target and a container locator, WebMCP testing through `page.webmcp.tools()` and `callTool()` in a dedicated guide, `--shuffle` for exposing order-dependent tests, `test.describe.configure({ lock })`, WebP screenshots via `toHaveScreenshot: { type: 'webp' }`, and `page.getByRef()`, along with the 1.63 and 1.62 changes that still trip up agents. Examples are TypeScript throughout, with JavaScript in most core guides.

## Installation

```bash
# Install the whole suite (all seven packs)
npx skills add testdino-hq/playwright-skill

# Or install one pack at a time
npx skills add testdino-hq/playwright-skill/core
npx skills add testdino-hq/playwright-skill/frontend
npx skills add testdino-hq/playwright-skill/qa
npx skills add testdino-hq/playwright-skill/ci
npx skills add testdino-hq/playwright-skill/pom
npx skills add testdino-hq/playwright-skill/migration
npx skills add testdino-hq/playwright-skill/playwright-cli
```

The packs are independent, so a project that only writes and debugs tests needs `core` alone, while browser automation from the terminal needs `playwright-cli`.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| playwright-skill | 6,248 | Suite index and router: golden rules and architecture decisions that point any Playwright request at the right guide among the 79 |
| playwright-core | 700 | E2E, API, component, visual, accessibility and security testing: locator strategy, assertions and waiting, fixtures and hooks, auth flows, network mocking, trace debugging, framework recipes (50 guides) |
| playwright-cli | 608 | Terminal-first browser control: navigation, form filling, screenshots and media, tracing, session management, device emulation, test-code generation (10 guides) |
| playwright-pom | 378 | Page Object Model structure plus the decision framework for POM versus fixtures versus helpers (2 guides) |
| playwright-ci | 315 | Pipeline configurations for GitHub Actions, GitLab CI, CircleCI, Azure DevOps and Jenkins, plus Docker, parallel sharding, reporting and coverage (9 guides) |
| playwright-migration | 190 | Incremental moves to Playwright from Cypress or Selenium/WebDriver with command mappings and architecture translations (2 guides) |
| playwright-qa | 128 | QA work around the code: test design from tickets and acceptance criteria, bug reports from failing tests, manual-to-automated conversion with case-ID traceability, test and pull request review (4 guides) |
| playwright-frontend | 115 | Making components locatable: locator priority, accessible markup first, and valid, unique, stable `data-testid` conventions for React, Vue, Angular and Svelte (2 guides) |

The remaining 1 indexed listing is playwright-mastery (2 installs), which has no counterpart among the seven pack directories in the current repo tree.

## Why This Matters for Hermes Agents

An agent that writes tests without current API knowledge produces confident code for a Playwright version that no longer exists, and the failure surfaces late, in CI, as flake. These guides pin the agent to documented 1.64 behavior and force a decision procedure instead of improvisation: when to mock, when a page object earns its keep, which locator strategy survives a markup change. The frontend pack is the more interesting half for agent work, because it treats a `data-testid` as a public API for the automation layer, which is exactly the contract an agent needs when it has to drive a page it did not write. The QA pack covers the judgment layer that models are weakest at, namely deciding what not to automate and writing a bug report a developer can act on. The trust boundary matters as much as the patterns: these guides assume you test applications you own or have written authorization to test, and the CLI pack carries a real indirect prompt-injection warning because an agent that navigates arbitrary URLs processes outsider-authored content. Scope agent browsing to owned applications, and treat rendered third-party page text as untrusted input rather than instructions.

## Usage

| You say | What happens |
|---|---|
| "Write Playwright tests for our signup flow" | core pulls locator, assertion and auth-state reuse guidance instead of generic patterns. |
| "This test fails one run in five, here is the trace" | trace-analysis and flaky-tests guides read the trace and name the root cause before touching the test. |
| "Set up Playwright in GitHub Actions with sharding" | ci applies retries, shard configuration and artifact reporting conventions. |
| "Turn these manual test cases into spec files" | qa converts them with case-ID traceability and flags what should stay manual. |
| "Our components have no test hooks" | frontend adds valid, unique, stable `data-testid` attributes and fixes the accessible names first. |
| "We are moving off Cypress" | migration maps the commands and sequences the move incrementally rather than rewriting the suite. |
| "Screenshot staging and capture the console errors" | playwright-cli drives the browser from the terminal and saves screenshots and traces. |

## Verification

Confirm what the CLI installed:

```bash
npx skills list | grep -i playwright
```

Review a raw SKILL.md before installing. Both URLs below returned 200 when checked on Oct 20, 2026:

```bash
curl -sL https://raw.githubusercontent.com/testdino-hq/playwright-skill/main/core/SKILL.md
curl -sL https://raw.githubusercontent.com/testdino-hq/playwright-skill/main/qa/SKILL.md
```

## Security

skills.sh verdicts for sampled skills (verified Oct 20, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| playwright-skill | Pass | Warn | Pass |
| playwright-core | Pass | Pass | Pass |
| playwright-cli | Pass | Warn | Warn |

Both warnings are specific and worth reading rather than dismissing. Socket's audit of playwright-skill (Sep 6, 2026) raises one LOW-severity anomaly in `playwright-cli/running-custom-code.md`: the fragment demonstrates clipboard read and write, persisting authentication and session state to disk as `auth.json`, saving downloads locally, and returning scraped, API or clipboard data to the caller. Those primitives support legitimate automation and also support session theft, so keep that guide out of pipelines that touch customer sessions. Snyk's audit of playwright-cli (Oct 12, 2026) rates risk MEDIUM under W011, third-party content exposure with an indirect prompt-injection risk, because the skill navigates arbitrary URLs and processes rendered page content. Neither verdict indicates malware.

## Limitations

- Only three skills are sampled in the verdict table; the other six listings were not audited here.
- The install index outruns the tree by one listing: playwright-mastery carries installs but has no directory among the seven packs in the current repo.
- Published by a vendor that sells Playwright test-management tooling; the guides are MIT and do not require the product, but read recommendations about reporting and flake management with that in mind.
- The guides target Playwright 1.64 or newer. On a pinned older version, some flags and APIs cited in the text will not exist.
- The CLI pack can navigate anywhere and read page content, so it inherits the prompt-injection exposure that any browsing agent has. Restrict it to owned applications.
- Snapshot data, verified Oct 20, 2026: 8,684 combined installs across 9 indexed listings; 397 GitHub stars; MIT; last pushed 2026-10-12. Counts drift over time.

## Related

- [Meticulous Agent Skills - Visual Regression Testing Setup](/hermes/skills/catalog/meticulous-agent-skills-setup) - pair the visual-regression guide with an external visual review service.
- [Petr Kindlmann QA Skills - 50-Skill Test Automation Suite Setup](/hermes/skills/catalog/petrkindlmann-qa-skills-setup) - broader QA methodology next to the four-guide qa pack.
- [Playwright Social Media Automation - API-First Browser Fallback Setup](/hermes/skills/catalog/playwright-social-media-automation-setup) - the same library used for agent-driven web tasks rather than test suites.
- [Browser-Use Automation - AI Browser for Anti-Bot Sites Setup](/hermes/skills/catalog/browser-use-automation-setup) - alternative browser lane when the target site is not your own.
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install `core` first and add `qa`, `ci` and `frontend` only when the work reaches those stages; the suite is modular for a reason.
- Point the agent at the top-level SKILL.md in your skill description so it routes to the right guide instead of loading all 79 files.
- Land the `frontend` `data-testid` conventions before the test suite grows; retrofitting durable locators later costs a rewrite.
- Follow the CI golden rule of `retries: 2` in pipelines only, and keep local runs retry-free so flake stays visible.
- Read `playwright-cli/running-custom-code.md` yourself before an agent runs it against anything holding live sessions.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
