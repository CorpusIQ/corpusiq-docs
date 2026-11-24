---
title: "TestMu AI Skills - Test Automation Agent Suite Setup"
description: "lambdatest/agent-skills - 13.0K combined installs: TestMu AI (formerly LambdaTest) agent skills for test automation across 15+ frameworks."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/lambdatest-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-24"
tags: ["hermes skill", "agent skill", "skill setup", "test automation", "qa", "playwright"]
---

# TestMu AI Skills - Setup Guide

**Source:** [lambdatest/agent-skills](https://www.skills.sh/lambdatest/agent-skills) via skills.sh - 13.0K combined installs across 90 indexed listings; first catalogued Nov 24, 2026 (Nov 24, 2026 morning sweep)
**GitHub:** [lambdatest/agent-skills](https://github.com/lambdatest/agent-skills) - 395 stars, MIT license, main branch, last pushed Nov 17, 2026; one directory per framework skill (<name>-skill/SKILL.md with a reference/ playbook), an api-skill/ group holding many api-* SKILL.md files, and migration skills that bundle detect.py and convert_caps.py scripts.
**Category:** Test Automation and QA Agent Skills
**Quality Tier:** 🟠 Orange - appium-skill, selenium-skill, cucumber-skill and robot-framework-skill each fail the Gen Agent Trust Hub check; the other 11 sampled skills pass all three checks.

LambdaTest rebranded to TestMu AI on Jan 12, 2026, and this repository is its agent-skills distribution: production-grade test-authoring skills for the major automation frameworks, migration skills that move an existing suite to the TestMu AI cloud, and a smaller set of best-practice skills for reviewing and hardening existing tests.

The 90 indexed listings span browser automation (Playwright, Cypress, Selenium, WebdriverIO, Puppeteer), unit testing (Jest, Vitest, pytest, JUnit 5, PHPUnit), BDD (Cucumber, Behave, SpecFlow), mobile (Appium, XCUITest, Detox, Espresso) and CI/CD. The high-install head is Playwright (568) and Vitest (509); a migration tail of 13 skills at 7 installs each and an api-skill group at 20-32 installs sit below the 250-install mark. The README documents installation through npx agentskillsforall.

## Installation

Clone and install the skills:

```bash
git clone https://github.com/LambdaTest/agent-skills && cd agent-skills
npx agentskillsforall add https://github.com/LambdaTest/agent-skills.git
```

Set credentials (macOS/Linux):

```bash
export LT_USERNAME="YOUR_USERNAME"
export LT_ACCESS_KEY="YOUR_ACCESS_KEY"
```

Install a specific skill or browse the catalog:

```bash
npx agentskillsforall add https://github.com/LambdaTest/agent-skills.git --skill selenium-skill
npx agentskillsforall list https://github.com/LambdaTest/agent-skills.git
```

The Rook skill (testing AI agents) ships with its own installer and needs Node.js 22+:

```bash
npx @testmuai/rook-skill
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| playwright-skill | 568 | Playwright scripts and E2E tests in TS, JS, Python, Java or C#, local or on the TestMu AI cloud |
| vitest-skill | 509 | Vitest tests in JavaScript or TypeScript with Vite-native speed |
| appium-skill | 452 | Appium mobile automation for Android and iOS in Java, Python or JavaScript |
| pytest-skill | 446 | pytest tests in Python with fixtures, parametrize, markers and mocking |
| selenium-skill | 339 | Selenium WebDriver scripts and tests across Java, Python, JavaScript, C#, Ruby and PHP |
| jest-skill | 295 | Jest unit and integration tests with mocking, snapshots and React component testing |
| junit-5-skill | 293 | JUnit 5 tests in Java with Mockito, parameterized and nested tests |
| cicd-pipeline-skill | 293 | CI/CD pipeline configs for GitHub Actions, Jenkins, GitLab CI and Azure DevOps |
| phpunit-skill | 290 | PHPUnit tests in PHP with data providers, mocking and test doubles |
| cucumber-skill | 286 | Cucumber BDD tests with Gherkin features and step definitions |
| webdriverio-skill | 271 | WebdriverIO (WDIO) automation tests in JavaScript or TypeScript |
| cypress-skill | 267 | Cypress E2E and component tests in JavaScript or TypeScript |
| robot-framework-skill | 256 | Robot Framework keyword-driven tests with SeleniumLibrary and RequestsLibrary |
| detox-skill | 256 | Detox E2E tests for React Native apps |
| hyperexecute-skill | 254 | HyperExecute cloud runs: YAML config, CLI jobs, debugging and CI wiring |
| xcuitest-skill | 253 | XCUITest iOS UI testing (name-level; no published description) |
| puppeteer-skill | 251 | Puppeteer browser automation (name-level; no published description) |

The remaining 73 indexed listings range from 5 to 249 installs.

## Why This Matters for Hermes Agents

TestMu AI's agent-skills repository is a single, coherent source for wiring a coding agent into a test framework. Each framework skill teaches the agent the framework's idioms, fixtures, page objects, waits and mocks, rather than just generating boilerplate, and carries reference playbooks the agent can cite. The migration skills are the unusual part: they convert an existing suite from another cloud (BrowserStack, Sauce Labs, AWS Device Farm and others) to TestMu AI with the smallest working diff and write a TESTMU_MIGRATION.md record. For a Hermes builder this is a template for how a vendor ships domain skills, per-framework SKILL.md plus a shared cloud reference and per-skill evals. The caution is security: four high-install skills fail the Gen Agent Trust Hub check, and several skills bundle helper scripts rather than Markdown-only. Use the framework head, and review before relying on the long tail.

## Usage

| You say | What happens |
|---|---|
| Write Playwright tests for the login page and run them on the TestMu AI cloud | Uses playwright-skill for scripts plus a cloud run |
| Create JUnit 5 tests for the payments service with Mockito and GitHub Actions CI | Uses junit-5-skill and cicd-pipeline-skill |
| Write pytest tests for this Python module | Uses pytest-skill |
| Migrate this repo from BrowserStack to TestMu AI | Uses browserstack-migration-skill |
| Review my Playwright tests | Uses playwright-patterns-skill |
| This test fails one run in ten, find out why | Uses flaky-test-fixes-skill |
| Run my Cypress suite | Uses cypress-skill |

## Verification

Confirm the README resolves on the main branch:

```bash
curl -sL https://raw.githubusercontent.com/lambdatest/agent-skills/main/README.md | head -40
```

Confirm the highest-install skill body is present before installing:

```bash
curl -sL https://raw.githubusercontent.com/lambdatest/agent-skills/main/playwright-skill/SKILL.md | head -30
```

## Security

skills.sh verdicts for sampled skills (verified Nov 24, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| playwright-skill | Pass | Pass | Pass |
| vitest-skill | Pass | Pass | Pass |
| appium-skill | Fail | Pass | Pass |
| pytest-skill | Pass | Pass | Pass |
| selenium-skill | Fail | Pass | Pass |
| jest-skill | Pass | Pass | Pass |
| junit-5-skill | Pass | Pass | Pass |
| cicd-pipeline-skill | Pass | Pass | Pass |
| phpunit-skill | Pass | Pass | Pass |
| cucumber-skill | Fail | Pass | Pass |
| webdriverio-skill | Pass | Pass | Pass |
| cypress-skill | Pass | Pass | Pass |
| robot-framework-skill | Fail | Pass | Pass |
| detox-skill | Pass | Pass | Pass |
| hyperexecute-skill | Pass | Pass | Pass |

## Limitations

- Snapshot data, verified Nov 24, 2026: 12,988 combined installs across 90 indexed listings; 395 GitHub stars; MIT license; last pushed Nov 17, 2026. Counts drift over time.
- Four high-install skills (appium-skill, selenium-skill, cucumber-skill and robot-framework-skill) carry Gen Agent Trust Hub Fail cells.
- The install index and repo tree diverge for the api-skill group; for example the index's api-security-auth-pattern corresponds to api-skill/api-security-patterns/SKILL.md in the tree.
- Many skills bundle helper scripts (scaffold-project.sh, detect.py, convert_caps.py) rather than Markdown-only, a larger audit surface.
- 73 of 90 listings sit below 250 installs, including a migration tail of 13 skills at 7 installs each.
- kanecli-skill ships in the tree but is absent from the 90 indexed listings.

## Related

- [TestDino Playwright Skills - 79-Guide Testing Suite Setup](/hermes/skills/catalog/testdino-playwright-skill-setup)
- [Petr Kindlmann QA Skills - 50-Skill Test Suite](/hermes/skills/catalog/petrkindlmann-qa-skills-setup)
- [Code Review Skill - 20+ Language Review Guides](/hermes/skills/catalog/code-review-skill-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install per-framework skills one at a time rather than cloning the whole tree into every agent.
- Set LT_USERNAME and LT_ACCESS_KEY before first run; the cloud-run skills expect them.
- Use the migration skills when moving an existing suite, and read the generated TESTMU_MIGRATION.md before trusting the change.
- Prefer the framework head (Playwright, Vitest, Appium, pytest) and treat the api-skill and migration tails as exploratory.
- Re-check the security page for appium, selenium, cucumber and robot-framework before production use.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
