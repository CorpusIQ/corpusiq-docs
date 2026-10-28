---
title: "OpenSEO - Self-Hosted SEO Platform, MCP and Skills Setup"
description: "OpenSEO: 64.2K combined installs. Self-hosted SEO platform with Docker or Cloudflare, a DataForSEO-backed MCP server, and 12 agent skill workflows."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/open-seo-setup/"
robots: "index,follow"
last_updated: "2026-10-28"
tags: ["hermes skill", "agent skill", "skill setup", "seo", "mcp", "keyword research"]
---

# OpenSEO - Setup Guide

**Source:** [every-app/open-seo](https://www.skills.sh/every-app/open-seo) via skills.sh - 64.2K combined installs across 13 indexed listings; snapshot 2026-10-28 (Oct 28 morning sweep)

**GitHub:** [every-app/open-seo](https://github.com/every-app/open-seo) - 25,425 stars, MIT, branch main, last pushed 2026-10-26; 12 workflow skills under `plugins/openseo/skills/` with matching copies under `.agents/skills/`, which holds 27 directories in total, for 39 `SKILL.md` directories in the clone

**Category:** Self-hosted SEO platform, MCP data layer and agent workflow skills

**Quality Tier:** 🟡 Beta - vendor maintained, 25,425 GitHub stars, 13 indexed listings against 39 skill directories in the tree, and three of the six sampled skills carry a Snyk warning

OpenSEO is an open source alternative to Semrush and Ahrefs from EveryApp, and it is a full application rather than a skill collection. The app covers keyword research, rank tracking, competitor insights, backlinks, site audits and AI visibility in one UI, and it bills through your own DataForSEO API key, so the only cost is the data you actually pull. Self-hosting runs on a Docker image that works with Compose platforms such as Coolify, Portainer and Dokploy, or on your own Cloudflare account with one deploy command, free plan included. A hosted version at openseo.so costs $10/month.

The agent surface sits on top of that app in two layers. An MCP server exposes the SEO data and the project state as tools, and 12 workflow skills tell an agent how to use those tools for one job each: project setup, coaching, keyword research, clustering, competitive landscape, competitor analysis, local SEO, link prospecting, site audit, AI prompt research, AI visibility audit and report writing. Both layers ship as one Claude Code plugin, manifest version 1.0.25, with the same skills installable through the skills.sh CLI, the Codex plugin, the Cursor plugin or a plain directory copy.

The tree carries more directories than the index lists. Thirteen listings have install counts: the 12 plugin skills plus `simple-issue-description`, a contributor helper for writing readable issues. The other 26 directories are the duplicate copies under `.agents/skills/` and 14 repo-maintenance skills such as `deslop`, `merge-ready`, `papercuts`, `review-ui-states`, `test-audit` and `verify-local-mcp` that skills.sh does not index.

## Installation

The skills.sh CLI installs the repository into an agent's skills directory. The project docs list three spellings: interactive, everything, and filtered by agent:

```bash
npx skills add every-app/open-seo
npx skills add every-app/open-seo --skill '*'
npx skills add every-app/open-seo --skill '*' --agent codex
```

The README's own single-skill example, used for the contributor workflow, filters by name:

```bash
npx skills add every-app/open-seo --skill simple-issue-description
```

Claude Code and Claude Cowork take the plugin instead, which adds the MCP server and all 12 skills in one step:

```text
/plugin marketplace add every-app/open-seo
/plugin install openseo@openseo
```

Plugin skills are namespaced by the plugin name, so the audit skill runs as `/openseo:seo-audit` and the rest follow the same pattern. Codex has its own OpenSEO plugin; Cursor and ChatGPT install from their marketplaces.

The MCP server is a separate connection and the skills assume it is reachable. The hosted endpoint is `https://app.openseo.so/mcp`, and Claude Code adds it with:

```bash
claude mcp add --transport http --scope user openseo https://app.openseo.so/mcp
```

The first call sends you through OpenSEO login. For headless or CI use, create a personal API key in the app and pass it as a bearer token, for example `--header "Authorization: Bearer oseo_YOUR_KEY"`. For Hermes, the documented manual route is the one that applies, since the project docs cover Codex and Claude Code skill folders only:

```bash
git clone https://github.com/every-app/open-seo.git
cp -R open-seo/plugins/openseo/skills/* ~/.hermes/profiles/corpusiq/skills/
```

Self-hosting the app is independent of the skills. Docker needs a host and a DataForSEO key, and the Cloudflare path needs a Cloudflare account; both are covered in `docs/SELF_HOSTING_DOCKER.md` and `docs/SELF_HOSTING_CLOUDFLARE.md`.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| keyword-research | 6,874 | Turning seed topics into a prioritized keyword set: volume, difficulty, CPC and intent, a live SERP check per candidate, then saving and tagging the terms worth tracking. |
| seo-project-setup | 6,675 | Interviewing once about one site and writing scope, goals, positioning, competitors, key pages and preferences into the project's shared context, with an MCP connection check and Search Console intake. |
| competitor-analysis | 6,675 | Studying one named competitor: its organic footprint, ranking keywords, content themes, backlinks and the gaps worth counter-positioning against. |
| keyword-clustering | 6,665 | Grouping keywords into page-level clusters by intent and mapping each cluster to an existing or proposed page, rather than stopping at semantic grouping. |
| seo-coach | 6,660 | A coaching mode that explains what each workflow does, picks the next step for someone new to SEO, and shows how to combine the agent's web, scraping and MCP tools. |
| link-prospecting | 6,607 | Finding pages, sites and authors that could reference a linkable asset from SERPs and backlink signals, then discovering contact paths with web and browser tools. |
| competitive-landscape | 6,606 | A market-level view across several competitors: who leads, which content themes win, keyword coverage, backlinks and where the openings are. |
| seo-audit | 5,191 | Auditing one domain end to end: crawl, issues and pages, live ranking checks behind every claim, then one to three recommendations delivered as a saved HTML report. |
| local-seo | 4,391 | Working out why a business does or does not appear in Maps and the local pack: Business Profile audit, review and post data, category slugs, and a rank grid around the location. |
| simple-issue-description | 3,917 | Rewriting a rough bug report, feature request, support note or PR into a short plain-language issue about the problem and the desired behavior. |
| seo-report | 2,056 | Turning finished research into one self-contained HTML page saved to the project with `save_report`, readable on a phone and printable to PDF. |
| ai-visibility-audit | 966 | Auditing how a brand shows up in AI answers: reads saved answers, adds the pages behind them, and recommends the few changes, such as a third-party page to get onto or an owned page to improve. |
| ai-prompt-research | 956 | Finding what people ask ChatGPT about a market, how it answers, and which sites get cited, before choosing prompts to track. Research only, it never saves tracking. |

All 13 indexed listings clear the 500-install threshold and appear in the table above.

## Why This Matters for Hermes Agents

SEO is a domain where an agent without data produces confident generic advice, and this suite is built around removing that failure mode. Most workflows open with MCP calls that produce numbers, and the audit skill goes further: it requires a live SERP check behind each ranking claim, with the query, country, language, date and organic position recorded in an evidence appendix.

The cost model is explicit enough for unattended work. `whoami` confirms the connection and the credit balance before spending, crawl reads are free, and the AI visibility tools separate research that uses credits from reading saved answers that does not. A rank tracker run can be priced first with `estimate_rank_tracker_cost`, which is the difference between an agent that explores and one that quietly bills a few hundred requests.

Project context is the second gain. `seo-project-setup` writes the business overview, goals, competitors and key pages into OpenSEO's shared project context through `update_project_context`, and every other skill calls `get_project_context` first. That context survives new sessions, new machines and new agents, so a Hermes run picks up where the last one stopped instead of re-interviewing you.

The output shape suits agent work as well. Research ends in a saved HTML report rather than a chat wall, and the report is a file on the project that a human can open later. Several skills also state what they will not do: `ai-prompt-research` stops before saving tracking, `seo-coach` is advisory only, and the audit skill declines to write a report when the report skill is missing instead of improvising HTML.

## Usage

| You say | What happens |
|---|---|
| "Set up SEO context for acme.com before we do anything else" | seo-project-setup checks the MCP connection, interviews you once about scope, goals, competitors and key pages, and stores the answers in the project context that every later skill reads. |
| "Find keywords worth targeting for our analytics product" | keyword-research expands seeds into candidates, pulls volume, difficulty, CPC and intent, checks the SERP for the finalists, then saves the shortlist back to the project with tags. |
| "Group the shortlist into pages we should write" | keyword-clustering assigns every cluster to an existing or proposed page and returns a mapping you can hand to a writer. |
| "Audit acme.com and tell me the three things to fix first" | seo-audit starts the crawl with `run_site_audit`, polls status, reads issues and pages, verifies the important rankings with live SERP calls, and saves an HTML report with the top recommendations. |
| "Why does ChatGPT recommend our competitors and not us" | ai-prompt-research finds the prompts and cited domains first, then ai-visibility-audit reads the answers, adds the cited pages, and names the third-party page to get onto or the owned page to improve. |
| "Who owns our category and where are the content gaps" | competitive-landscape maps the leaders, themes and keyword coverage across the market, while competitor-analysis takes one domain deep on keywords, backlinks and gaps. |
| "Find sites that should link to this report" | link-prospecting builds a prospect list from SERPs and backlink data, then discovers authors and contact routes with the agent's web and browser tools. |

## Verification

Probe the paths before installing, and read the two skills that steer everything after them. All five URLs below returned 200 on the main branch when this guide was written:

```bash
for p in plugins/openseo/skills/keyword-research/SKILL.md \
         plugins/openseo/skills/seo-audit/SKILL.md \
         plugins/openseo/skills/seo-project-setup/SKILL.md \
         .agents/skills/simple-issue-description/SKILL.md \
         .agents/skills/setup-openseo/SKILL.md; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/every-app/open-seo/main/$p"
done
```

The two to read first are the audit and the project setup skill, because one decides what to crawl and the other decides what every later skill believes about the business:

- https://raw.githubusercontent.com/every-app/open-seo/main/plugins/openseo/skills/seo-audit/SKILL.md
- https://raw.githubusercontent.com/every-app/open-seo/main/plugins/openseo/skills/seo-project-setup/SKILL.md

After install, confirm what actually landed. The installer decides which directories it copies, and the index name and the frontmatter name should match:

```bash
ls ~/.hermes/profiles/corpusiq/skills | grep -cE '^(seo-|keyword-|ai-|link-|local-|competit)'
head -5 ~/.hermes/profiles/corpusiq/skills/seo-audit/SKILL.md
```

For the MCP side, ask the agent to run `whoami` against the project. A successful call returns the account and credit state without spending anything, which separates a broken connection from an authorization problem before you start a crawl.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-28) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| keyword-research | Pass | Pass | Pass |
| seo-project-setup | Pass | Pass | Warn |
| competitor-analysis | Pass | Pass | Pass |
| keyword-clustering | Pass | Pass | Pass |
| seo-coach | Pass | Pass | Warn |
| link-prospecting | Pass | Pass | Warn |

Three of the six sampled listings carry a Snyk Warn with code W011: seo-project-setup, seo-coach and link-prospecting. The other two auditors pass all six. Those three are also the three that reach outside the app: setup writes to project context, the coach reads the agent's wider toolset, and link prospecting drives web and browser tools for contact discovery, so treat the warning as a reason to read those three SKILL.md files before installing them rather than as a verdict on the repository.

What the install actually runs is small. Every skill directory holds a single `SKILL.md` and nothing else, the root `package.json` has no install or postinstall lifecycle script, and nothing in the skill directories executes on clone. The risk sits in what the skills then do: they call an MCP server that holds your SEO data, your Search Console and Analytics connections and your credit balance.

Credential handling is the part to get right. The hosted server authorizes through OpenSEO login, and an API key is explicitly personal: anything an agent does with the key acts as you in the workspace that was active when the key was created. Keys are shown once, can be revoked under Settings, and a self-hosted instance can drop accounts entirely by putting the app behind Cloudflare Access or a private network. Point an unattended Hermes cron at a key scoped to one workspace, and it will act on that workspace only.

Two surfaces change state. Rank tracker runs and AI visibility research write to the project and consume credits, site crawl reads are free, and reports are private by default on the hosted service until something explicitly calls `set_report_sharing` with `public: true`. If you run the audit on a client site, check that publishing step before the link leaves the building.

## Limitations

- Snapshot data, verified 2026-10-28: 64,239 combined installs across 13 indexed listings; 25,425 GitHub stars; MIT; last pushed 2026-10-26. Counts drift over time.
- The install index is narrower than the tree: 39 `SKILL.md` directories exist against 13 indexed listings. The 12 plugin skills are duplicated under `.agents/skills/`, which holds 27 directories, and the remaining entries there are repo-maintenance workflows with no install counts.
- Three of the six sampled listings carry a Snyk Warn with code W011, on the security page of seo-project-setup, seo-coach and link-prospecting. The repository as a whole is not audited by that sample.
- The skills are useless without a reachable OpenSEO deployment and an account. There is no offline mode, and the hosted endpoint is the only documented MCP URL for the SaaS path; a self-hosted instance serves its own.
- SEO data costs money per call. The app needs a DataForSEO API key, crawl reads and project context are free, and prompt research, live SERP depth and AI visibility runs consume credits. The README states the hosted service charges 28% over the raw DataForSEO request price.
- The documented install paths are the skills.sh CLI, the Claude Code plugin, the Codex plugin, the Cursor marketplace, the ChatGPT plugin and a manual directory copy. Nothing is written for Hermes, so the copy route above is the one to use; the CLI also accepts `--skill <name>` when you want a single workflow.
- The repository is more than skills and an MCP server. It is the full application, a Cloudflare worker plus a Postgres schema plus a client, so a self-hosted deployment is an ops project rather than a skill install. Its own `setup-openseo` and `verify-local-mcp` skills exist for that work but are not indexed.

## Related

- [Claude SEO - 31-Skill Universal SEO Suite Setup](/hermes/skills/catalog/claude-seo-setup)
- [SEO GEO Claude Skills - SEO & Generative Engine Optimization Suite Setup](/hermes/skills/catalog/seo-geo-claude-skills-setup)
- [SEOJuice Skills - SEO Suite Setup](/hermes/skills/catalog/seojuice-skills-setup)
- [SEO Skill - Search Console MCP for Agents Setup](/hermes/skills/catalog/iannuttall-seo-setup)
- [Kostja94 Marketing Skills - Copywriting, SEO, Ads Setup](/hermes/skills/catalog/kostja94-marketing-skills-setup)

## Pro Tips

- Run `seo-project-setup` on day one, per site. Every other skill reads that context first, and the audit skill will fill a missing business overview itself and then ask you to finish the job later, which costs two conversations.
- Ask for `whoami` before anything that costs credits. It confirms the connection and the balance for free, and the audit skill is written to stop and ask you to connect OpenSEO if that call fails rather than guess.
- Install the 12 plugin skills, not the whole tree. The 27 directories under `.agents/skills/` include the repository's own review and release workflows, and they compete for the same trigger phrases your SEO requests will match.
- When a ranking claim matters, ask which SERP query, country and date produced it. The audit skill records that evidence, so a number without it is a number the agent recalled rather than fetched.
- Keep the API key per workspace and per purpose. A key used for a nightly rank check should not also be the key wired into an agent that writes reports for clients, because revoking it signs out both.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
