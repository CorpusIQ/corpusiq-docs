---
title: "SEO Skill - Search Console MCP for Agents Setup"
description: "SEO Skill: 9.4K combined installs. Search Console, Analytics and Bing data for agents through one MCP server and CLI, grounded in real numbers."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/iannuttall-seo-setup/"
robots: "index,follow"
last_updated: "2026-10-23"
tags: ["hermes skill", "agent skill", "skill setup", "seo", "search console", "mcp"]
---

# SEO Skill - Setup Guide

**Source:** [iannuttall/seo](https://www.skills.sh/iannuttall/seo) via skills.sh - 9.4K combined installs across 57 indexed listings; new to this catalog in the Oct 23, 2026 sweep

**GitHub:** [iannuttall/seo](https://github.com/iannuttall/seo) - 590 stars, Apache-2.0 license, last pushed 2026-10-23, branch main, one skill at `skills/seo/SKILL.md` with an `agents/openai.yaml` manifest beside it

**Category:** Marketing / Search Analytics

**Quality Tier:** 🟡 Beta - Apache-2.0, active development on the day of this snapshot, and a clean design that returns facts instead of advice, but Snyk raises two medium warnings because the workflow crawls third-party pages and points at a remote MCP endpoint

The SEO Skill is a data layer, not an advice generator. It exposes Search Console, Google Analytics, Bing Webmaster Tools and Clicky through one remote MCP server and a CLI, so an agent works from the site's own clicks, impressions, positions and indexing reasons instead of from a keyword estimate or a generic checklist. Keyword and backlink data from DataForSEO or Ahrefs is available too, but it is kept separate from the first-party numbers.

The design decision worth noting is subtraction. The author says the first version had about seventy reports and almost nobody used most of them; the shipped surface is a handful of commands, each taking a site or a URL, with no settings to tune and every result ending in the command to run next. That is a shape an agent handles well.

## Installation

The hosted MCP server is the shortest path:

```bash
# Claude Code
claude mcp add --transport http seoskill https://seoskill.dev/mcp

# Codex
codex mcp add seoskill --url https://seoskill.dev/mcp
```

```bash
# The CLI, which owns the parts that run on your machine: crawls and Bing
npm i -g seo
seo start
```

`seo start` signs you in, connects your agents and installs the skill. For Hermes, add `https://seoskill.dev/mcp` as a remote MCP server and keep the skill next to it:

```bash
hermes skills install iannuttall/seo/seo --yes
```

Sign-in is Google OAuth against the account that can read the Search Console property. There is no password and no signup form. `seo crawl --url <url>` needs no sign-in at all, which makes it the one command you can prove before authorizing anything.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| seo | 9,332 | The whole surface in one skill: Search Console overview and movement, a single URL's live page and index status, a before-and-after comparison around a date with Google updates marked, indexing reasons labelled from live checks, keyword and competitor research from your own DataForSEO or Ahrefs key, raw Search Console, Bing, Clicky and Analytics rows, technical crawls including what AI agents can read, internal link suggestions, and the list of properties the account can read. |

The remaining 56 indexed listings carry 1 install each. They are individual workflow skills for the same collection, named things like seo-site-audit, llms-txt-generate and index-coverage-plan, and only `skills/seo/SKILL.md` exists in the current tree.

## Why This Matters for Hermes Agents

An agent asked why organic traffic dropped will produce a plausible list of causes, and every item on it will be a guess. The fix is not a better prompt; it is giving the agent the actual rows. This skill does that with ten commands, which is small enough that an agent can pick the right one without a routing layer.

The weekly indexing loop is the part that changes behavior. `seo index` inspects known URLs in a fixed order, pages that lost clicks first, then pages by clicks, then the sitemap, and labels each of Google's reasons as fix, check, expected or indexed from a live check. Run it once for a baseline, run it again next week with the same count, and diff by URL and reason. A URL that moved to fix, or a new reason, is the report.

For Hermes the practical value is grounding. An agent with this connected can answer "is this page indexed, and if not why" with a fact and a citation instead of a recommendation, and the same is true for the questions that usually get hand-waved: which searches a page appears for that it never mentions, and whether AI crawlers can read the site at all.

## Usage

| You say | What happens |
|---|---|
| "Why did clicks drop on this site last month?" | The agent pulls the overview, compares the weeks around the drop, and lines the change up against Google update dates. |
| "Which pages are close to page one, and for what?" | Striking-distance rows come back as real queries with impressions and positions, not as a keyword list. |
| "Is this page indexed? If not, why not?" | One URL is loaded live and Google's own index status and reason are reported. |
| "Which searches does this page show up for that it never mentions?" | Search Console queries are matched against the page text to find the gap. |
| "Can ChatGPT, Claude and Perplexity read my site?" | A crawl reports what AI agents see when they fetch the site, including what blocks them. |
| "Keep an eye on indexing every week" | You keep the baseline and the weekly result, diff by URL and reason, and report only what moved. |

## Verification

Confirm the skill file exists before installing, and probe the endpoint you will be authorizing:

```bash
curl -sL -o /dev/null -w "%{http_code} SKILL.md\n" \
  "https://raw.githubusercontent.com/iannuttall/seo/main/skills/seo/SKILL.md"
curl -sL -o /dev/null -w "%{http_code} MCP\n" "https://seoskill.dev/mcp"
```

A 401 on the MCP endpoint is the healthy answer: it proves the server exists and is refusing an unauthenticated call rather than being absent.

Read the skill itself, since it defines the command-to-tool mapping:

- https://raw.githubusercontent.com/iannuttall/seo/main/skills/seo/SKILL.md

After install, prove it in the order that needs the least trust. `seo crawl --url https://example.com` runs without a sign-in, so it separates "the CLI works" from "the account is connected". Then `seo sites` should list exactly the properties the account can read. If that list is empty, the sign-in picked the wrong Google account, which is the most common failure.

## Security

skills.sh verdicts for sampled skills (verified October 23, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| seo | Pass | Pass | Warn |
| seo-site-audit | Pass | Warn | Warn |
| llms-txt-generate | Pass | Pass | Warn |

Snyk rates the main skill medium on two counts that are structural. W011 is third-party content exposure: `seo crawl` reads arbitrary web pages, captions and page text written by strangers, which is an indirect prompt injection surface. W012 is an unverifiable external dependency, because the skill points at a remote MCP endpoint the auditor cannot inspect. Socket adds a warning on seo-site-audit for the same crawl surface, and the sibling workflow skills inherit Snyk's warning.

Two consequences. Point the crawler at sites you control, or treat everything it returns as untrusted text. And decide deliberately whether the hosted MCP server or a local `seo mcp serve` is the right trust model for the data, because the hosted route sends your Search Console reads through someone else's infrastructure.

The author's own statement about retention is specific: the hosted server keeps the linked Google accounts and any saved keys, encrypted, and does not keep Search Console data, reports or request logs; the CLI keeps the sign-in in the system keychain. Verify that against the privacy policy before authorizing a property.

## Limitations

- Snapshot data, verified October 23, 2026: 9,388 combined installs across 57 indexed listings; 590 GitHub stars; license Apache-2.0; last pushed 2026-10-23. Counts drift over time.
- The install index outruns the tree. 57 listings are indexed but only one SKILL.md exists at `skills/seo/`; the other 56 carry 1 install each and are workflow names rather than separate installable skills.
- `seo` keeps no history. Weekly indexing comparisons only work if you store the baseline yourself; the tool will not diff against last week for you.
- Crawls and Bing run locally through the CLI, so the MCP server alone will not give you those two commands.
- Keyword and backlink volumes come from your own DataForSEO or Ahrefs key and are estimates. They are deliberately kept apart from the first-party Search Console numbers.
- The skill is one author's project, at 590 stars. It is active, not institutionally supported.

## Related

- [Claude SEO - 31-Skill Universal SEO Suite Setup](/hermes/skills/catalog/claude-seo-setup)
- [SEOJuice Skills - SEO Suite Setup](/hermes/skills/catalog/seojuice-skills-setup)
- [SEO GEO Claude Skills - SEO & Generative Engine Optimization Suite Setup](/hermes/skills/catalog/seo-geo-claude-skills-setup)

## Pro Tips

- Start with `seo crawl` before connecting anything. It needs no sign-in and immediately shows whether the tool sees the site the way a browser does.
- Run `seo index` once with `--detail full` and keep the output. That file is the baseline every later comparison depends on.
- Use `seo compare --site <site> --date <date>` around a traffic change instead of eyeballing weekly totals; the Google update dates in the output are what turn a correlation into an explanation.
- Ask for the query-to-page gap early. It is the cheapest content brief you will get from your own data, and it never appears in a keyword tool.
- Read every crawl result as untrusted text. It is the one part of this stack an outsider can write to.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
