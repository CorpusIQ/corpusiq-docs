---
title: "Browserbase Skills - Agent Browser Automation"
description: "browserbase/skills: 40.1K combined installs. Eighteen agent skills for Browserbase sessions, traces, UI testing, WebMCP and prospect research."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/browserbase-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-31"
tags: ["hermes skill", "agent skill", "skill setup", "browser automation", "browserbase", "webmcp"]
---

# Browserbase Skills - Setup Guide

**Source:** [browserbase/skills](https://www.skills.sh/browserbase/skills) via skills.sh - 40.1K combined installs across 20 indexed listings; first seen 2026-10-31 (morning sweep)

**GitHub:** [browserbase/skills](https://github.com/browserbase/skills) - 3,747 stars, no LICENSE file, branch main, last pushed 2026-10-27; 18 `SKILL.md` files, one per directory under `skills/`, ten of which also carry a `scripts/` folder of Node standard-library helpers

**Category:** Browser automation for agents: Browserbase platform, sessions, UI testing and grading

**Quality Tier:** 🟡 Yellow - one sampled skill fails the Gen Agent Trust Hub auditor, three carry Snyk warns, one carries a Socket warn, and the repository has no LICENSE file at its root

Browserbase ships this as its first-party skill set, and the shape is unusual for a vendor repository: it is not a wrapper around one SDK call but a working browser harness that an agent can drive end to end. The eighteen skills split into four groups. The core loop is `browser` (natural-language control of a browser through the `browse` CLI), `fetch` and `search` (no session at all), and `browser-trace` (a read-only CDP trace attached to whatever else is running). Around that sit the quality tools: `ui-test` for adversarial UI testing, `agent-experience` for grading how agent-friendly a product or docs site is, and `optimize-agent-prompt` for tuning a Browserbase Agent system prompt. Then the deployment and interop layer: `functions`, `safe-browser`, `cookie-sync`, `webmcp-gen`, `add-webmcp`, `browser-to-api`, `browser-use-to-stagehand` and `autobrowse`. The last group is not browser plumbing at all: `company-research`, `competitor-analysis` and `event-prospecting` are go-to-market research skills that use the Browserbase Search API as their data source.

The dependency to understand before installing is the `browse` CLI. Most skills call it, and their own compatibility lines ask for `npm install -g browse` plus `BROWSERBASE_API_KEY` for remote sessions, or a local Chrome or Chromium for local ones. The two sessionless skills, `fetch` and `search`, need the API key and nothing else. That means the suite is closer to a toolchain install than a markdown drop-in: useful immediately for a profile that already drives a browser, and a second dependency to manage for one that does not.

## Installation

The README's primary route is the skills CLI:

```bash
npx skills add browserbase/skills
```

Claude Code users get a plugin marketplace route as well, which is also documented in the README and installs the `browse` plugin rather than loose skill folders:

```bash
/plugin marketplace add browserbase/skills
/plugin install browse@browserbase
```

The README then points at the CLI the skills actually call. Each skill's `compatibility` line names it, and remote sessions need a key:

```bash
npm install -g browse
export BROWSERBASE_API_KEY="your-key"
```

Neither route knows about Hermes, so the durable install for this profile is a directory copy. Clone shallow and copy the skill directories, not the files, so each `SKILL.md` keeps its `scripts/` neighbours:

```bash
git clone --depth 1 https://github.com/browserbase/skills.git /tmp/browserbase-skills
cp -r /tmp/browserbase-skills/skills/. ~/.hermes/profiles/corpusiq/skills/
```

That copies all 18 directories in the tree. A narrower install is reasonable here, because the research skills pull in report templates and the browser skills do not: take `browser`, `fetch`, `search` and `browser-trace` for the core loop, add `ui-test` and `safe-browser` for testing work, and add `company-research`, `competitor-analysis` and `event-prospecting` only if the profile does prospecting.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| browser | 5,909 | Driving a browser in natural language through the `browse` CLI: navigation, clicks, form fills, screenshots and data extraction, on local Chrome or a remote Browserbase session with Identity, verified browsers, CAPTCHA solving and residential proxies. |
| fetch | 3,058 | Pulling HTML or JSON from static pages with no browser session: status codes, headers, redirect control and page source for light scraping. |
| browser-trace | 3,039 | Attaching a read-only CDP client to a session that is already being driven, recording the DevTools firehose, screenshots and DOM dumps, then slicing them into per-page buckets for search and debugging. |
| ui-test | 3,032 | Adversarial UI testing over the browse CLI: diff-scoped runs for a pull request or full exploratory passes, checking functional correctness, accessibility, responsive layout and UX heuristics. |
| functions | 2,854 | Deploying browser automation as Browserbase cloud functions: scheduled runs, cron jobs and webhook endpoints built with the `browse` CLI. |
| search | 2,829 | Web search without a browser session, returning structured titles, URLs, authors and dates. |
| autobrowse | 2,767 | The self-improving loop: run a browsing task, read the trace, rewrite the navigation strategy, and repeat until the run passes reliably, including parallel runs across tasks. |
| cookie-sync | 2,665 | Exporting cookies from local Chrome into a Browserbase persistent context so the CLI can reach sites you are already signed into. |
| browserbase-cli | 2,489 | Indexed on skills.sh with no matching directory in the clone, so there is no `SKILL.md` to route to. Treat it as a pointer to the `browse` CLI that the other skills document, not as a separate install. |
| company-research | 2,365 | Finding companies that match an ICP with the Search API, deep-researching each one, and scoring fit into a report plus CSV, with quick, deep and deeper depth modes. |
| event-prospecting | 2,092 | Extracting speakers from a conference page, filtering their companies against the ICP, and deep-researching the best-fit people into a person-first report with public links and a DM opener. |
| browser-to-api | 1,957 | Turning a site's observable HTTP traffic into a best-effort OpenAPI 3.1 document plus a coverage report, by replaying a `browser-trace` capture. |
| safe-browser | 1,741 | Generating a local Claude Agent SDK browser agent whose only browser capability is a CDP-gated `safe_browser` tool with domain allowlist enforcement through Fetch interception. |
| agent-experience | 876 | Grading how agent-friendly a product, SDK or docs site is: subagents get a tiny prompt, their traces are captured, and setup friction, speed, error recovery and doc quality are scored A to F. |
| competitor-analysis | 675 | Discovering competitors through the Search API, researching each across marketing, signal, benchmark and strategic-diff lanes, and compiling an HTML report with a feature and pricing matrix. |
| webmcp-gen | 574 | Authoring, compiling and validating site-specific WebMCP init scripts from a target URL, producing a `webmcp.init.js` artifact and testing registration with Stagehand. |
| browser-use-to-stagehand | 503 | Porting browser-use Python scripts to Stagehand v3 on Browserbase, mapping `act`, `extract`, `observe` and `agent` primitives and choosing a determinism level per step. |
| what-antibot | 275 | Indexed on skills.sh with no directory in the clone. There is no `SKILL.md` behind it here, so there is nothing to install and nothing to route on. |
| optimize-agent-prompt | 229 | Tuning a Browserbase Agent `systemPrompt` in an outer loop: fixed task, collected Agent messages and session logs, a score, one revised heuristic, and confirmation runs. |
| add-webmcp | 198 | Adding first-party WebMCP tools to an existing web app by finding safe capabilities across routes, forms, server actions and schemas, then validating discovery with Stagehand. |

All 20 indexed listings clear the threshold and appear above. Two of them, `browserbase-cli` and `what-antibot`, have no directory in the tree, so the install copies 18.

## Why This Matters for Hermes Agents

Most agent browser work fails on the last mile rather than the first. The agent can navigate, but it cannot show what happened when navigation broke, cannot prove that a form submission was the right one, and cannot repeat a run that worked yesterday. This suite is built around that gap: `browser-trace` turns a session into a searchable record, `autobrowse` closes the loop by rewriting the navigation strategy from that record, and `ui-test` treats a diff as the scope of the test rather than the whole application.

The second thing it changes is reach. `browser` is documented as supporting remote sessions with CAPTCHA solving, residential proxies and verified browsers, which is the difference between an agent that can read public pages and an agent that can complete a task on a site that resists automation. `cookie-sync` extends that to sites the operator is already signed into, and `safe-browser` pulls in the other direction, generating an agent whose only browser capability is allowlisted by domain, with Fetch interception failing anything off-list.

The third is that half the repository is about grading rather than browsing. `agent-experience` drops subagents at a product or docs site with a tiny prompt and scores what happened, and `optimize-agent-prompt` does the same for a Browserbase Agent system prompt. For a profile that publishes anything agent-facing, those two are a feedback mechanism that does not otherwise exist.

Finally, the research skills turn the browser harness into a lead pipeline. `company-research`, `competitor-analysis` and `event-prospecting` all use the Search API for discovery and deep research for the per-entity work, and all three emit reports rather than raw output, which is what makes the results reviewable rather than just voluminous.

## Usage

| You say | What happens |
|---|---|
| "Go to Hacker News, pull the top post comments and summarise them" | `browser` drives the page through the `browse` CLI, extracts the comments and returns the summary rather than the raw DOM. |
| "QA test localhost:3000 and fix what breaks" | `ui-test` walks the app over a local browser, checking function, accessibility, responsive layout and UX, then reports bugs it can reproduce. |
| "Why did last night's automation run fail" | `browser-trace` reads the recorded CDP stream for that run, bisects it per page, and answers from network, console and DOM events instead of guessing. |
| "Sync my Chrome cookies so the agent can browse a signed-in site" | `cookie-sync` exports cookies into a Browserbase persistent context, and later `browse` calls reuse that context. |
| "Turn this dashboard's XHR traffic into an OpenAPI spec" | `browser-to-api` pairs request and response events from a trace, templatizes the observed URLs and emits OpenAPI 3.1 with a coverage report. |
| "Find fifty companies that match this ICP and score them" | `company-research` discovers candidates through the Search API, deep-researches each, and writes a scored report plus a CSV. |
| "Our browser-use script needs to move to Stagehand" | `browser-use-to-stagehand` maps the Python script onto Stagehand v3 primitives and picks a determinism level per step instead of a straight transliteration. |

## Verification

The raw path for the core skill returned HTTP 200 on branch main when this guide was written on 2026-10-31:

```bash
curl -sL -o /dev/null -w "%{http_code} browser\n" \
  https://raw.githubusercontent.com/browserbase/skills/main/skills/browser/SKILL.md
```

Expect `200`. After the copy lands, confirm the count and that `scripts/` came along, since `browser-trace`, `browser-to-api` and `webmcp-gen` lose most of their value without it:

```bash
ls -d ~/.hermes/profiles/corpusiq/skills/*/ | wc -l
head -6 ~/.hermes/profiles/corpusiq/skills/browser/SKILL.md
ls ~/.hermes/profiles/corpusiq/skills/browser-trace/scripts
```

The count should print 18 on a profile that had no other skills, the header should show `name: browser` with a `license: MIT` line and a `compatibility` line naming the `browse` CLI, and the script listing should show the Node helpers the trace skill runs.

## Security

One sampled skill carries a Fail and the repository ships no license: `add-webmcp` fails the Gen Agent Trust Hub auditor, and there is no LICENSE file at the root of the repository, so the suite is Yellow and both facts matter before an install.

skills.sh verdicts for sampled skills (verified 2026-10-31) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| browser | Pass | Pass | Warn |
| search | Pass | Pass | Warn |
| event-prospecting | Pass | Pass | Warn |
| webmcp-gen | Pass | Warn | Pass |
| add-webmcp | Fail | Pass | Pass |

The warn surface is what the skills do rather than what they contain. Every skill is a markdown bundle, but ten of them ship `scripts/` folders whose helpers shell out to the `browse` CLI, drive Chrome over CDP, or write trace directories under the working tree, so the risk is the commands an agent is told to run. `cookie-sync` deserves its own note: it reads the operator's local Chrome profile and copies authenticated cookies into a Browserbase context, which is the most sensitive operation in the suite and the one to scope deliberately. `safe-browser` is the opposite case, generating an agent with a single allowlisted browser tool and no shell access at all.

Two mechanical details are worth checking yourself. The root `package.json` declares `"postinstall": "npm run build"`, so installing from the repository root runs a TypeScript build rather than copying files; a directory copy of `skills/` avoids that entirely. And the missing LICENSE is real at the repository level even though each `SKILL.md` carries `license: MIT` in its frontmatter, so the per-skill declaration is the only grant text in the tree. Treat API keys and cookies as environment state, never as prompt content, and keep `BROWSERBASE_API_KEY` scoped to the session that needs it.

## Limitations

- Snapshot data, verified 2026-10-31: 40,127 combined installs across 20 indexed listings; 3,747 GitHub stars; no LICENSE file; last pushed 2026-10-27. Counts drift over time.
- The index runs ahead of the tree. Twenty listings are indexed but the clone holds 18 skill directories: `browserbase-cli` and `what-antibot` resolve to nothing under `skills/`, so an install of "everything" installs 18 and two table rows have no route to point at.
- Install counts are not a ranking of usefulness. `browser` leads at 5,909 while `optimize-agent-prompt` sits at 229 and `add-webmcp` at 198, even though `add-webmcp` is the one skill in the sample with a security Fail; volume says what people tried, not what holds up.
- There is no LICENSE file. The repository root has no grant, and the MIT declared in each `SKILL.md` frontmatter is a per-file claim rather than a repository licence, which is a question for legal review before this ships inside a product.
- The skills are not self-contained. Most depend on the global `browse` CLI, remote sessions depend on `BROWSERBASE_API_KEY`, and `browser-to-api` depends on a trace directory produced by `browser-trace`, so a partial install can leave a skill that cannot run.
- Several skills overlap on purpose. `browser`, `safe-browser` and `autobrowse` all claim browser automation, and `ui-test` and `agent-experience` both test software, so routing depends on the phrasing of the request rather than on a clean boundary.

## Related

- [Open Browser Use Skills - Browser Automation Setup](/hermes/skills/catalog/open-browser-use-setup)
- [browser-act - Record-and-Replay Browser Automation Setup](/hermes/skills/catalog/browser-act-setup)
- [Playwright Social Media Automation - API-First Browser Fallback Setup](/hermes/skills/catalog/playwright-social-media-automation-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the four-skill core first: `browser`, `fetch`, `search` and `browser-trace`. That covers navigation, cheap static fetches, discovery and debuggability, and it is the combination that makes every other skill in the repository easier to evaluate.
- Reach for `fetch` or `search` before `browser` on any read-only task. Both run without a browser session, so they cost a request instead of a session, and the skills say so in their own descriptions.
- Keep traces. `browser-trace` writes per-page buckets into a run directory, and `browser-to-api` and `autobrowse` both consume those directories; a run without a trace is a run the agent cannot learn from.
- Pass `--local` on the first browser command for localhost work, and `--auto-connect` when the agent should reuse an existing Chrome session, both of which the README documents and neither of which is the default.
- Skip the root `npm install`. Copy `skills/` as directories so the `postinstall` build never runs, and read the `add-webmcp` skill itself before adopting it, given its Gen Agent Trust Hub Fail.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
