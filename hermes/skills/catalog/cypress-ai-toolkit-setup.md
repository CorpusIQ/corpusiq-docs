---
title: "Cypress AI Toolkit - E2E Testing Skills"
description: "cypress-io/ai-toolkit: 30.4K combined installs. Five Cypress skills for authoring, explaining, documenting and driving tests, plus Cloud run triage."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/cypress-ai-toolkit-setup/"
robots: "index,follow"
last_updated: "2026-10-31"
tags: ["hermes skill", "agent skill", "skill setup", "cypress", "e2e testing", "test automation"]
---

# Cypress AI Toolkit - Setup Guide

**Source:** [cypress-io/ai-toolkit](https://www.skills.sh/cypress-io/ai-toolkit) via skills.sh - 30.4K combined installs across 5 indexed listings; first seen 2026-10-31 (morning sweep)

**GitHub:** [cypress-io/ai-toolkit](https://github.com/cypress-io/ai-toolkit) - 46 stars, MIT, branch main, last pushed 2026-10-23; 5 `SKILL.md` files, one per directory under `skills/`, four of which carry a `references/` folder (six files under `cypress-tap`, four under `cypress-cloud-cli`) and `cypress-author` adds a `subskills/` pair

**Category:** End-to-end browser testing: Cypress test authoring, failure triage and test quality for agents

**Quality Tier:** 🟡 Yellow - two of the five sampled skills carry Snyk warns, so the suite is Yellow even though every Gen Agent Trust Hub and Socket verdict is a Pass

The Cypress team publishes this as the first-party skill set for its own framework, and the framing in the README is honest about the problem: AI tools can already write Cypress, but they do it unevenly, underusing the API, misapplying selectors and skipping the conventions an experienced Cypress developer internalises. Five skills are the answer, and they divide cleanly by intent. `cypress-author` creates, updates and fixes E2E and component tests. `cypress-explain` explains and critiques existing ones without editing. `cypress-docs` looks facts up in official documentation and refuses to assert API behaviour it has not verified. `cypress-tap` drives a running `cypress open` session through `cypress tap`. `cypress-cloud-cli` investigates recorded runs, failures, screenshots and Test Replay data through the `cy-cloud` CLI.

The split matters more than the count, because the two authoring skills are instructed to defer to each other: `cypress-author` says to prefer `cypress-explain` when the user only wants an explanation, and `cypress-explain` says to prefer `cypress-author` when code has to change. That is a routing contract written into the skills rather than left to the model, and it is why a five-skill suite covers the test workflow without the usual overlap problem.

## Installation

The README's fastest route is the skills CLI, which installs all five:

```bash
npx skills add cypress-io/ai-toolkit
```

The bundled `skills/README.md` also documents per-skill installs, which is the route to take when only one workflow is wanted:

```bash
npx skills add https://github.com/cypress-io/ai-toolkit --skill cypress-author
npx skills add https://github.com/cypress-io/ai-toolkit --skill cypress-tap
```

The GitHub CLI carries an alternative installer, with or without a named skill:

```bash
gh skill install cypress-io/ai-toolkit
gh skill install cypress-io/ai-toolkit cypress-cloud-cli
```

The README also documents a plugin route for Claude users through the Claude Community Plugins marketplace, where the plugin is listed as `cypress`, and notes that the Cursor marketplace listing is still pending. Neither route knows about Hermes, so the durable install here is a directory copy that keeps each skill's `references/` folder beside its `SKILL.md`:

```bash
git clone --depth 1 https://github.com/cypress-io/ai-toolkit.git /tmp/cypress-ai-toolkit
cp -r /tmp/cypress-ai-toolkit/skills/. ~/.hermes/profiles/corpusiq/skills/
```

Two of the skills need tooling outside the repository. `cypress-tap` requires Cypress 15.21 or newer, a Chromium-family browser and a live `cypress open` session, and `cypress-cloud-cli` assumes `cy-cloud` is already on `PATH`, installing with `npm install -g @cypress/cloud` when it is not. The Cypress Cloud MCP is a separate optional connection: the README points at the Claude connector, the Cursor plugin and the VS Code extension, and `mcp/server.json` declares a remote `streamable-http` endpoint at `https://mcp.cypress.io/mcp` that authenticates with OAuth by default, or a personal access token if you edit `.mcp.json`.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| cypress-author | 9,184 | Creating, updating and fixing Cypress E2E and component tests: a new spec, a test for a specific file or component, or a fix for a failing or flaky test, with `references/` rules for async behaviour and reuse. |
| cypress-docs | 8,345 | Looking Cypress facts up in official documentation and refusing unverified claims: commands, assertions, hooks, config, CLI flags, plugins and types, preferring the LLM markdown under `/llm/*` and the `/llms.txt` index. |
| cypress-explain | 8,147 | Explaining how a test or Cypress itself works, and reviewing or critiquing a suite without changing code, with separate rule sets for explaining tests and explaining Cypress. |
| cypress-tap | 2,851 | Driving a live `cypress open` session through `cypress tap`: running and rerunning specs, waiting for results, reading reporter and command logs, and querying the app through DOM, accessibility, styles and snapshots. |
| cypress-cloud-cli | 1,899 | Investigating Cypress Cloud through `cy-cloud`: organisations, projects, runs, specs, tests, failure screenshots and Test Replay data, with JSON output parsed directly for triage. |

All 5 indexed listings clear the threshold and appear above. Every listing has a matching directory in the tree, so there is no index-versus-tree gap here.

## Why This Matters for Hermes Agents

Cypress is one of the frameworks where generic code generation looks correct and behaves badly. An agent that reaches for a raw CSS selector, chains assertions inside a `cy` callback, or hardcodes a wait produces a suite that passes locally and flakes in CI. `cypress-author` exists to stop exactly that, and its `references/` files carry the rules rather than the summary: async behaviour, authoring rules and reusability each get their own document, so the guidance the agent loads is specific rather than aspirational.

The documentation skill is the quiet win. `cypress-docs` instructs the agent to search official documentation first, to use the `llms.txt` index and the `/llm/*` markdown paths, and to refuse API or behaviour claims it has not verified. For a profile that writes about tooling, that turns a hallucination risk into a lookup step.

`cypress-tap` is what separates this toolkit from a prompt library. It drives a real open-mode session to run a spec, read the reporter, and inspect the app under test through DOM, accessibility and style queries, which is the loop an agent needs to debug its own test rather than hand the failure back to a human. `cypress-cloud-cli` does the same for recorded runs, so a failing CI run becomes an investigation with screenshots and replay data instead of a log excerpt.

## Usage

| You say | What happens |
|---|---|
| "Write tests for this checkout component" | `cypress-author` picks up the component test path, writes the spec against Cypress conventions, and fixes any test it breaks in the process. |
| "Why is this test flaky" | `cypress-explain` reads the spec and its rules, then explains the failure mode without editing the file. |
| "Does `cy.intercept` support response delays in this version" | `cypress-docs` checks the official docs and the `/llm/*` markdown before answering, and declines to assert behaviour it cannot verify. |
| "Run this spec and show me what the app looked like at the failure" | `cypress-tap` drives the running `cypress open` session, reruns the spec, reads the reporter and queries the app state at the failing command. |
| "Why did the run on main fail at 14:02" | `cypress-cloud-cli` pulls the run, its failing spec and its screenshots from Cypress Cloud, and parses the JSON rather than scraping text. |
| "Review this suite before we rewrite it" | `cypress-explain` critiques the tests as written, and `cypress-author` picks up the rewrite when the review ends in edits. |

## Verification

The raw path for the top skill returned HTTP 200 on branch main when this guide was written on 2026-10-31:

```bash
curl -sL -o /dev/null -w "%{http_code} cypress-author\n" \
  https://raw.githubusercontent.com/cypress-io/ai-toolkit/main/skills/cypress-author/SKILL.md
```

Expect `200`. After the copy lands, confirm the count and that `references/` came along, since `cypress-tap` and `cypress-cloud-cli` are mostly reference material:

```bash
ls -d ~/.hermes/profiles/corpusiq/skills/cypress-*/ | wc -l
head -6 ~/.hermes/profiles/corpusiq/skills/cypress-author/SKILL.md
ls ~/.hermes/profiles/corpusiq/skills/cypress-tap/references
```

The count should print 5, the header should show `name: cypress-author` with `allowed-tools: Read, Edit`, and the reference listing should show six files including `session-lifecycle.md` and `reading-the-app.md`.

## Security

Two of the five sampled skills carry Snyk warns: `cypress-author` and `cypress-cloud-cli`, which is what makes this suite Yellow despite clean Gen Agent Trust Hub and Socket verdicts across the board.

skills.sh verdicts for sampled skills (verified 2026-10-31) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| cypress-author | Pass | Pass | Warn |
| cypress-docs | Pass | Pass | Pass |
| cypress-explain | Pass | Pass | Pass |
| cypress-tap | Pass | Pass | Pass |
| cypress-cloud-cli | Pass | Pass | Warn |

The surface is small and readable. There is no package to install, no build step and no postinstall hook: each skill is `SKILL.md` plus markdown references, and the only executables involved are the ones Cypress already ships, `cypress` itself and `cy-cloud`. The two warned skills are also the two that touch the network in a meaningful way, `cypress-cloud-cli` against Cypress Cloud and `cypress-author` against the docs site when it verifies API behaviour, which is the plausible reason for a heuristic warn rather than a specific finding.

The credential question is worth settling before deployment. Cypress Cloud access runs through the MCP connection or the `cy-cloud` CLI, and the README states that the MCP uses OAuth by default with a personal access token as the alternative configured in `.mcp.json`. Keep that token in the environment or in the agent's MCP configuration, never in a prompt, and keep the record key out of any file the agent writes. `cypress-tap` needs no credentials at all, because it drives a local session the operator already started.

## Limitations

- Snapshot data, verified 2026-10-31: 30,426 combined installs across 5 indexed listings; 46 GitHub stars; MIT; last pushed 2026-10-23. Counts drift over time.
- The five listings map one to one onto the five directories in the tree, so there is no index-versus-tree drift, but that also means the suite is small: coverage is one framework and five workflows, not a broad testing catalogue.
- Install counts are not a ranking. `cypress-author` leads at 9,184 while `cypress-tap` sits last at 2,851, even though `cypress-tap` carries the deepest operational material with six reference files covering session lifecycle, result reading and troubleshooting.
- `cypress-tap` does not work headless. It requires Cypress 15.21 or newer, a Chromium-family browser and an already-running `cypress open` session, and the skill itself says it is not for one-shot headless runs, so CI triage falls to `cypress-cloud-cli` instead.
- `cypress-cloud-cli` assumes `cy-cloud` is installed and on `PATH` and warns that the installed CLI may be newer or older than its own instructions, so command flags can drift from the documentation.
- The repository documents its install routes inconsistently. The root README points Claude users at the Community Plugins marketplace and says the Cursor listing is pending, while the bundled `skills/README.md` still lists plugin install as coming soon, so follow the root README and expect the plugin route to lag.
- `cypress-author` and `cypress-explain` overlap on review-style requests. Both instruct the agent to prefer the other for the adjacent intent, which resolves most cases but leaves "review this and fix it" to interpretation.

## Related

- [TestDino Playwright Skills - 79-Guide Testing Suite Setup](/hermes/skills/catalog/testdino-playwright-skill-setup)
- [Dogfood - Systematic QA Testing Setup](/hermes/skills/catalog/dogfood-setup)
- [Playwright Social Media Automation - API-First Browser Fallback Setup](/hermes/skills/catalog/playwright-social-media-automation-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install all five, not a subset. The author and explain skills hand work to each other by design, and a profile that carries only `cypress-author` loses the review path that keeps the generated tests honest.
- Point the agent at `cypress-docs` before any version-sensitive question. It ranks `/llms.txt` and the `/llm/*` markdown first and is instructed to refuse unverified behaviour claims, which is cheaper than debugging a confident wrong answer.
- Use `cypress-tap` for the debug loop and `cypress-cloud-cli` for the post-mortem. The first needs a live session the operator started, the second works from recorded runs, and mixing them up is the usual source of "the command does not exist" failures.
- Model `cypress-tap` commands from `references/json-recipes.md` and `references/reading-results.md` rather than guessing flags; the skill's own troubleshooting file says help is generated from the installed CLI and can differ from the prose.
- Keep the Cypress Cloud token in the MCP configuration, not in the conversation, and prefer the OAuth flow the README defaults to over a pasted PAT.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
