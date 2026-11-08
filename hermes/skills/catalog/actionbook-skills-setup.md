---
title: "Actionbook - Research Behind Logins and Paywalls"
description: "actionbook/actionbook on skills.sh: 8.9K combined installs; action manuals and a stateless browser engine for sources behind logins and paywalls."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/actionbook-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-08"
tags: ["hermes skill", "agent skill", "skill setup", "browser automation", "web scraping", "deep research"]
---

# Actionbook - Setup Guide

**Source:** [actionbook/actionbook](https://www.skills.sh/actionbook/actionbook) via skills.sh - 8,945 combined installs across 11 indexed listings; first seen 2026-11-08 (Nov 8 2026 morning sweep, first documentation)
**GitHub:** 1,626 stars, Apache-2.0 LICENSE at the repo root, last pushed 2026-10-19, 14 SKILL.md directories across `skills/`, `playground/` and `packages/openclaw-plugin/`
**Category:** Gated research for agents: web actions, extraction, deep research and article export across paywalled sources
**Quality Tier:** 🟡 Use With Care - Apache-2.0 and a real browser engine, but Snyk warns on four of five sampled skills, the README and the shipped SKILL.md disagree about how the thing is installed, and the licence metadata contradicts the licence file.

Actionbook attacks the slowest, most brittle part of agent browsing. The default loop is snapshot, parse, decide, act, repeated for every step, and it fails on virtualised lists, streaming components and date pickers because the agent is reasoning about a page it cannot see. Actionbook replaces the parse step with an action manual: a precomputed map of selectors and page structure for an indexed site, fetched by name before the agent touches the DOM. When no manual exists, the same CLI drives a real Chrome session with a stateless command surface, explicit `--session` and `--tab` flags on every call, so dozens of tabs run in parallel instead of one after another.

The repository is a pnpm monorepo, and the SKILL.md directories are spread unevenly through it. Only three live in `skills/`: `actionbook` (191 lines, the browser engine), `extract` (366 lines, structured data plus a generated Playwright script) and `active-research` (794 lines, an HTML report generator). Ten more sit under `playground/`, one skill per prototype, and `packages/openclaw-plugin/` ships one copy for the OpenClaw plugin.

The tree duplicates names, which matters when you are reading it. `actionbook` exists at `skills/actionbook/SKILL.md`, again at `playground/rust-learner/skills/actionbook/SKILL.md`, and a third time at `packages/openclaw-plugin/skills/actionbook/SKILL.md`. `agent-browser` appears twice, at `playground/actionbook-scraper/skills/agent-browser/SKILL.md` and `playground/rust-learner/skills/agent-browser/SKILL.md`. Fourteen directories therefore produce eleven indexed listings, and only the `skills/` copies carry the install numbers that matter.

This is not the same source as `actionbook/rust-skills`, which the catalog documents separately. That repository is a Rust coding-guideline pack with its own install counts and no browser engine; this one is the browser and research toolchain, with `rust-learner` as one small playground skill inside it. Installing one does not get you the other.

## Installation

The README's own install is not a package install. Actionbook v1.2 ships as a hosted MCP connector plus a Chrome extension, and the README states plainly that the standalone `@actionbookdev/cli` package is deprecated:

1. Install the Chrome extension from the Chrome Web Store (the README links the listing).
2. Add the connector in your client's settings - Claude under Settings, Connectors, Add custom connector; ChatGPT under Settings, Connectors; or any MCP client including Hermes - and paste the endpoint:

```text
https://edge.actionbook.app/mcp
```

3. Finish linking the extension from the dashboard at actionbook.app/dashboard.

If you came in through skills.sh, the skills themselves install with the standard CLI, and the commands are documented in the repository's own `packages/cli/CHANGELOG.md` and playground READMEs:

```bash
npx skills add actionbook/actionbook
npx skills add actionbook/actionbook --skill extract -g
```

The skills are markdown instruction sets. Their frontmatter declares one optional environment variable, `ACTIONBOOK_API_KEY`, created at actionbook.app/dashboard; without it the public rate limits apply.

## What It Provides

All eleven indexed listings appear here. The table threshold for this pack is zero, and no rows fall below it, so there is no tail.

| Skill | Installs | Use For |
|---|---|---|
| actionbook | 3,058 | The browser engine: action manuals, stateless sessions, snapshot refs, clicks, fills, cookies, storage, HAR capture |
| active-research | 2,860 | Topic research that ends in a rendered HTML report, with SPA-aware waits and batch operations |
| extract | 2,364 | Structured data plus a standalone Playwright `.cjs` script that reproduces the extraction without Actionbook |
| deep-research | 148 | The bilingual variant of the report pipeline, English and Chinese output from one JSON report |
| agent-browser | 136 | A thin wrapper around the same snapshot and click primitives, packaged for another agent harness |
| arxiv-viewer | 133 | arXiv search through the API, plus ar5iv HTML reading for sections, figures and citations |
| actionbook-scraper | 132 | Playground scraper pattern, useful as a reference rather than a product |
| rust-learner | 110 | Rust documentation lookup through the browser |
| article-exporter | 2 | Web article to Obsidian-ready Markdown folder with images downloaded and a translation option |
| actionbook-web-test | 1 | Writing browser tests against a site |
| json-ui | 1 | The JSON to HTML renderer that the research skills call to produce reports |

The three skills with real adoption divide the work cleanly. `actionbook` is the engine and the fallback: `search` and `manual` fetch a precomputed action manual for an indexed site, `browser start` opens a session, `snapshot` labels every element with a ref such as `@e3`, and refs stay stable across snapshots so a chain of commands does not need a re-snapshot after each step. Every command is stateless, which is why parallel tabs work.

`extract` is the one that produces something durable. Its deliverable is always two artefacts: an executable Playwright script and the extracted data as JSON or CSV. Its decision strategy treats Actionbook as a conditional accelerator, not a mandatory step: if `actionbook search` returns a manual with a health score of 70 percent or better, start from those selectors; only fall back to a live snapshot when the site is not indexed or the selectors have gone stale.

`active-research` is the report factory. It detects the input type - arXiv id, DOI, academic keyword, URL or free text - picks a search strategy, reads sources with network-idle waits and `--block-images` for speed, and renders the result through `json-ui` into an HTML report with a default output path of `./output/<topic-slug>.json`.

## Why This Matters for Hermes Agents

Most of the research an agent is asked to do sits behind an account. Pricing pages, analyst reports, arXiv HTML, documentation portals, forums, dashboards: all of it is either login-gated or rendered by a framework that the agent's fetch tool cannot parse. Actionbook's answer is to borrow the browser you are already signed into and give the agent a command surface detailed enough to act on it.

That detail is the difference from a generic Playwright skill. The SKILL.md carries structured error codes and tells the agent how to branch on them rather than parse a message: `CDP_NODE_NOT_FOUND` means the ref is stale, snapshot and retry; `CDP_NAV_TIMEOUT` and `CDP_TARGET_CLOSED` are marked retryable; `EVAL_CROSS_ORIGIN` means proxy the request server-side instead of retrying. That is the kind of guidance that turns a flaky browser skill into one an agent can recover inside.

The login handling is deliberately manual and worth copying. On an auth wall, sign-in page, MFA prompt or CAPTCHA, the skill says to pause, keep the session open, ask the human to finish the login in that same window, and continue in the same session afterwards. It explicitly forbids switching tools because a login page appeared. For an operator, this is the honest boundary: the agent does the reading, the human does the authentication.

For CorpusIQ-style work, the useful pairing is `extract` plus a small script. A one-off reading of a competitor page is a snapshot and a text pull. A recurring reading of the same site belongs in the generated Playwright script, which runs without Actionbook, without the extension, and without the rate limit.

## Usage

| You say | What happens |
|---|---|
| "Grab the pricing tables from these three vendors" | Three sessions in parallel, snapshot, text and table extraction, no serial round trips |
| "Scrape every row of this directory into CSV" | The extract skill returns a Playwright script plus the data file |
| "Research retrieval augmented generation and write me a report" | Active research detects the topic type, reads sources and renders an HTML report |
| "Read this arXiv paper's figures and citations" | The arxiv viewer switches to ar5iv HTML reading rather than the PDF |
| "Save this article into my Obsidian vault" | The article exporter fetches the page, downloads images, rewrites paths and writes an index |
| "Log in and pull my dashboard numbers" | The agent pauses at the auth wall, you sign in in the same window, and it continues |
| "This list is virtualised and the scrape comes back empty" | Wait for hydration, then use the refs from a fresh snapshot instead of the cached ones |

## Verification

Read the engine skill before installing it. This path returned 200 on `main`:

```bash
curl -fsSL https://raw.githubusercontent.com/actionbook/actionbook/main/skills/actionbook/SKILL.md | head -40
```

It should open with frontmatter naming `actionbook`, version 1.5.0, `license: MIT`, platforms macOS, Linux and Windows, a `hermes` metadata block requiring the terminal toolset, and an optional `ACTIONBOOK_API_KEY`. The body should then open with "When to Use This Skill" and the four-step workflow: start, navigate, snapshot, automate.

After install, check that the binary the skill talks about is actually there, and that a session can be created and torn down:

```bash
actionbook --version
actionbook browser start --set-session-id s1
actionbook browser goto https://example.com --session s1 --tab t1
actionbook browser snapshot --session s1 --tab t1
actionbook browser close --session s1
```

The snapshot should return labelled refs rather than raw HTML. If the CLI is not present, the deprecation note in the README applies: the supported path is the extension plus connector, not this binary.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-08) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| actionbook | Pass | Pass | Warn |
| extract | Pass | Pass | Warn |
| arxiv-viewer | Pass | Pass | Warn |
| article-exporter | Pass | Pass | Warn |
| json-ui | Pass | Pass | Pass |

The Snyk warning is structural rather than accidental. This is a tool whose declared job is to operate sites while authenticated: it runs `browser eval` with arbitrary JavaScript, reads and writes cookies, local storage and session storage, and ships `--stealth` plus fingerprint rotation for protected sites. Any scanner looking at that surface will flag it, and the correct reading is not "the markdown is malicious" but "this skill hands your live session to an agent". Treat the browser profile it touches as a credential.

The delete and write surface deserves the same respect. `browser fill`, `browser click` and `browser eval` act on whatever page is open, so a mis-targeted ref can post, submit or pay. The skill's own guidance to take selectors only from a fresh snapshot is a safety rule as much as an accuracy one.

Licence status is inconsistent across the tree and worth checking before redistribution. The repository root ships an Apache License 2.0 file, while `skills/actionbook/SKILL.md` declares `license: MIT` in its frontmatter. There is a LICENSE file and the repository is not archived, but the metadata and the file do not agree, so confirm with the maintainer if you plan to vendor the skill.

## Limitations

- Snapshot data, verified 2026-11-08: 8,945 combined installs across 11 indexed listings; 1,626 stars; 14 SKILL.md directories; last pushed 2026-10-19. Counts drift.
- Eleven listings against fourteen directories. The gap is duplicated names: `actionbook` appears in `skills/`, in `playground/rust-learner/skills/` and in `packages/openclaw-plugin/skills/`, and `agent-browser` appears twice under `playground/`. Reading the tree, assume only the `skills/` copies are the maintained versions.
- The install story contradicts itself. The README deprecates the standalone `@actionbookdev/cli` package and pushes a hosted connector plus extension, while `skills/actionbook/SKILL.md` is written entirely against the `actionbook browser ...` CLI and declares a terminal toolset requirement. Decide which surface you are installing before you wire anything to it.
- Logged-in browsing needs Chrome and the extension. The remote MCP endpoint alone does not give the agent your sessions, and the extension has to be linked from the dashboard before the endpoint can drive it.
- Auth walls are human work by design. Sign-in, MFA and CAPTCHA are handed back to the user, so an unattended run stops at the first login prompt.
- Most of the adoption sits in three skills (3,058, 2,860 and 2,364 installs). The rest of the table is between 1 and 148 installs, including prototypes last touched in March 2026 such as `article-exporter` at version 0.5.0.
- The star count is modest for a browser automation project, so there is no large third-party review corpus to lean on for the playground skills.
- I could not verify the hosted endpoint end to end, because that needs an account and the extension; only the raw skill paths above were confirmed to return 200.

## Related

- [Actionbook Rust Skills - Rust Guidelines Setup](/hermes/skills/catalog/actionbook-rust-skills-setup)
- [Browser-Use - AI-Powered Browser Automation](/hermes/skills/catalog/browser-use-automation-setup)
- [Playwright Skill - Code-First Browser Automation Setup](/hermes/skills/catalog/playwright-skill-setup)

## Pro Tips

- Do not install this collection whole and hope. `npx skills add actionbook/actionbook` pulls eleven listings across three quality levels; the `--skill` flag lets you take `actionbook` and `extract` and leave the playground prototypes alone.
- Prefer the generated script over the live browser for anything recurring. The `extract` skill's Playwright output runs without Actionbook installed, which removes the rate limit, the extension dependency and the session lifetime problem in one step.
- Pass `--session` and `--tab` on every single command, including in throwaway scripts. The interface has no notion of a current tab, and half the reported flakiness in stateless browser tools is a command landing in the wrong tab.
- Snapshot again after any navigation or form submit. Refs are stable only while the element stays the same; a stale `@e3` after a page change produces `CDP_NODE_NOT_FOUND`, not a wrong click, and that failure is much cheaper than the alternative.
- Keep a dedicated Chrome profile for this. The extension drives your real browser, so anything signed in there is reachable by the agent, including mail and billing.
- When a page returns empty text but the screenshot shows content, wait for hydration rather than retrying the extraction. The skills document this explicitly, and it is the most common false negative on React and Next.js sites.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
