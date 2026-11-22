---
title: "Apifox CLI Skills - API Design and Test Automation Setup"
description: "apifox/apifox-cli-skills: Apifox CLI skills for API projects, interface design, automated tests and branch collaboration - 4.7K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/apifox-cli-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-22"
tags: ["hermes skill", "agent skill", "skill setup", "api", "apifox", "api testing", "test automation"]
---

# Apifox CLI Skills - API Design and Test Automation Setup

**Source:** [apifox/apifox-cli-skills](https://www.skills.sh/apifox/apifox-cli-skills) via skills.sh - 4.7K combined installs across 8 indexed listings; first seen Nov 22, 2026 (Nov 22, 2026 morning sweep)
**GitHub:** [apifox/apifox-cli-skills](https://github.com/apifox/apifox-cli-skills) - 20 stars, no LICENSE file, main branch, last pushed Jul 9, 2026 (four months stale); eight skill directories under `.well-known/agent-skills/<name>/SKILL.md` plus a `.well-known/agent-skills/index.json` discovery manifest, a README.md and an apifox-cli-installation-guide.md at the root.
**Category:** API Development and Test Automation
**Quality Tier:** 🟠 Orange - one of the 8 sampled skills carries a Snyk Fail on apifox-cli, plus no LICENSE file and a four-month-stale repository (last pushed Jul 9, 2026); Gen Agent Trust Hub and Socket are clean across all 8.

Apifox is an API platform that combines interface design, debugging, mocking, automated testing and API documentation, and the Apifox CLI is its command-line surface for managing projects, designing interfaces, orchestrating and running tests, importing and exporting, and collaborating on branches. This repository is Apifox's official agent-skills suite for that CLI, so an assistant can drive an API project through the CLI with structured JSON output and agentHints.nextSteps instead of guessing command syntax. The README and every skill description are written in Chinese; the facts in this guide are translated from them.

Install runs through the skills CLI with an interactive flow that lets you choose which skills to install, the target agent and the install scope. The tree ships eight skill directories under `.well-known/agent-skills/`, a skills discovery index, and a separate first-install guide that covers CLI installation, token login and project selection. All eight indexed listings map one-to-one to the eight skill directories in the tree, so there is no index-versus-tree drift to account for.

## Installation

Install the skills through the skills CLI. The command opens an interactive flow where you pick which skills to install, the target agent and the install scope:

```bash
npx -y skills add https://github.com/apifox/apifox-cli-skills
```

You can also install from the Apifox official site, then list what is installed:

```bash
npx -y skills add https://apifox.com
npx -y skills list
```

The skills run in whichever agent reads the SKILL.md files; there is no daemon or plugin manifest to wire. The repository also ships a first-install guide for the CLI itself: install the CLI globally (`npm i -g apifox-cli@latest`), log in with `apifox login --with-token <TOKEN>`, confirm with `apifox whoami` and `apifox project list`, and save a default projectId to `.apifox/settings.json` so later tasks can read it.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| apifox-cli | 671 | general entry point for managing project resources, running tests and viewing reports through the CLI |
| apifox-test-case | 582 | API test cases: query, create, update, delete, categorize and run test-case and test-data with steps, assertions and extractors |
| apifox-import-export | 574 | import OpenAPI, Postman and Apifox formats and export to OpenAPI, HTML, Markdown and Postman with pre-import and post-import quality checks |
| apifox-cli-checkup | 572 | diagnose CLI issues: a command succeeded but nothing shows, reports are missing, help or agentHints disagree, or the CLI is outdated |
| apifox-test-automation | 572 | automated test execution, suites and CI: test-suite, scheduled-task, runner, apifox run and report upload |
| apifox-test-scenario | 569 | model complex test scenarios with steps, conditions, loops, waits, scripts and database steps plus variable references and assertions |
| apifox-branch | 558 | branch collaboration: regular, iteration and AI branches, pick-to, merge, merge-request and protected branches |
| apifox-workflow-api-lifecycle | 556 | end-to-end API lifecycle from requirements through interface design, Schema, Mock, tests and docs export to branch merge |

All 8 indexed listings clear the 500-install threshold and appear in the table above.

## Why This Matters for Hermes Agents

The CLI is the awkward middle: an agent that knows Apifox's concepts but not its command surface will issue wrong flags and misread the structured JSON it gets back. These skills close that gap, teaching the agent that CLI output is structured JSON that often carries agentHints.nextSteps and that every command supports --help. The skill split mirrors Apifox's real separation of concerns: apifox-cli is the general entry point, apifox-test-case and apifox-test-scenario cover test authoring at two depths (single cases versus multi-step scenario orchestration), and apifox-test-automation runs them through suites, scheduled tasks and runners into CI. The import/export skill encodes quality checks rather than a bare format swap, validating spec completeness, tags and schema/body coverage before import and re-checking counts and visibility after. apifox-workflow-api-lifecycle strings the whole path together, from requirements to interface design, Schema, Mock, tests and docs export. The branch skill is the collaboration layer: AI branches, pick-to, merge and merge-request with protected-branch rules. The caveats are the single Snyk Fail on the core apifox-cli skill, the missing LICENSE file and the four-month-stale repository, so read each SKILL.md before relying on it.

## Usage

| You say | What happens |
|---|---|
| Create a new API interface | apifox-cli walks the query/create/update/delete flow for interfaces, environments, Schema and Mock resources |
| Run the test suite | apifox-test-automation drives test-suite, scheduled-task, runner and apifox run, then uploads the report |
| Import this OpenAPI spec | apifox-import-export validates spec completeness, tags and schema/body coverage before importing, then re-checks counts after |
| Model a complex test flow | apifox-test-scenario chains steps, conditions, loops, waits, scripts and database steps with variables and assertions |
| The command worked but I see nothing | apifox-cli-checkup checks version, help output and agentHints to reconcile CLI behavior with the page |
| Create a branch and merge my changes | apifox-branch handles regular, iteration and AI branches, pick-to, merge and merge-request with protected-branch rules |
| Build a full API with tests and docs | apifox-workflow-api-lifecycle runs from requirements through design, Schema, Mock, tests and docs export to branch merge |

## Verification

Review the core skill before installing and read its routing:

```bash
curl -sL https://raw.githubusercontent.com/apifox/apifox-cli-skills/main/.well-known/agent-skills/apifox-cli/SKILL.md | head -40
```

Inspect the test-case and scenario skills that back the testing workflow:

```bash
curl -sL https://raw.githubusercontent.com/apifox/apifox-cli-skills/main/.well-known/agent-skills/apifox-test-case/SKILL.md | head -40
curl -sL https://raw.githubusercontent.com/apifox/apifox-cli-skills/main/.well-known/agent-skills/apifox-test-scenario/SKILL.md | head -40
```

Check the discovery manifest that indexes all eight skills:

```bash
curl -sL https://raw.githubusercontent.com/apifox/apifox-cli-skills/main/.well-known/agent-skills/index.json | head -40
```

## Security

skills.sh verdicts for sampled skills (verified Nov 22, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| apifox-cli | Pass | Pass | Fail |
| apifox-test-case | Pass | Pass | Pass |
| apifox-import-export | Pass | Pass | Pass |
| apifox-cli-checkup | Pass | Pass | Pass |
| apifox-test-automation | Pass | Pass | Pass |
| apifox-test-scenario | Pass | Pass | Pass |
| apifox-branch | Pass | Pass | Pass |
| apifox-workflow-api-lifecycle | Pass | Pass | Pass |

Seven of the 8 sampled skills pass all three auditors; apifox-cli carries a single Snyk Fail. The skills are markdown reference documents with no bundled executable or postinstall hook, so the clean verdicts elsewhere are unsurprising. The repository has no LICENSE file at the root, so redistribution and modification rights are unclear despite the Apifox publisher.

## Limitations

- Snapshot data, verified Nov 22, 2026: 4.7K combined installs across 8 indexed listings; 20 GitHub stars; no LICENSE file; last pushed Jul 9, 2026. Counts drift over time.
- There is no LICENSE file at the repository root, so redistribution and modification rights are unclear despite the Apifox publisher.
- The repository is four months stale (last pushed Jul 9, 2026), so the skill routing may lag newer CLI releases; the README itself advises trusting current CLI output over skill text when they disagree.
- The core apifox-cli skill carries a Snyk Fail in the skills.sh sample; the other seven sampled skills pass clean.
- The README and every skill description are written in Chinese; this guide's translations are summaries, not authoritative documentation.

## Related

- [Vapi Skills - Voice AI Agent Building Setup](/hermes/skills/catalog/vapi-skills-setup)
- [Anthropic Claude API Skills - Official Claude API](/hermes/skills/catalog/anthropics-claude-api-skills-setup)
- [Apidojo Agent Skills - 100-Skill Social & Market Data](/hermes/skills/catalog/apidojo-agent-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Prefer apifox-cli for general CLI tasks and load a specialized skill only when the task falls into a specific domain, exactly as the README advises.
- Before any write operation, check the current CLI help and JSON Schema and validate the payload with cli-schema validate.
- When skill text and current CLI output disagree, trust the current CLI output; the repository is four months stale.
- Save a default projectId in .apifox/settings.json and add *.private.* to .apifox/.gitignore so the token never lands in version control.
- Re-check the skills.sh security pages before production use; the sample covers all 8 listings but apifox-cli carries a Snyk Fail.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
