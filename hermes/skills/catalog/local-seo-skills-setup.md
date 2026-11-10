---
title: "Local SEO Skills - Local Search Playbooks for Agents"
description: "garrettjsmith/localseoskills on skills.sh: 2.2K combined installs; 20 indexed local SEO skills for GBP, citations, reviews and geogrids"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/local-seo-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-09"
tags: ["hermes skill", "agent skill", "skill setup", "local seo", "google business profile", "map pack", "geogrid"]
---

# Local SEO Skills - Setup Guide

**Source:** [garrettjsmith/localseoskills](https://www.skills.sh/garrettjsmith/localseoskills) via skills.sh - 2.2K combined installs across 20 indexed listings; first seen 2026-11-09 (Nov 9, 2026 sweep)
**GitHub:** 147 stars, MIT via LICENSE, `main` branch, last pushed 2026-10-30, 39 SKILL.md files under `skills/`, `.mcp.json` and `.claude-plugin/plugin.json` at the root, `briefs/` and `tasks/` directories for state and scheduled work
**Category:** Local search: Google Business Profile, local citations, reviews, service pages and local rank tracking
**Quality Tier:** 🟡 Solid with caveats - MIT licensed and mostly Pass verdicts, but the repository is small and carries two Snyk Warnings.

This is a local SEO operating system written as skills rather than a collection of prompts. The README frames it in three parts: persistent briefs that hold per-client and per-location state and compound across sessions, 15 scheduled task templates with autonomous, queue and notify approval tiers, and a data layer built for local search rather than bolted on. The skill inventory splits into 26 strategy skills (GBP optimization, audits, citations, reviews, keywords, geogrid, content, AI visibility, multi-location, client deliverables and a dispatch router) and 12 tool skills that wrap specific data providers: Local SEO Data, Local Falcon, LSA Spy, SerpAPI, Semrush, Ahrefs, BrightLocal, DataForSEO, Whitespark, Search Console, Google Analytics and Screaming Frog.

The default data source is Local SEO Data, a paid API with 54 tools behind one MCP connection. The repository ships a `.mcp.json` that points at `https://mcp.localseodata.com/mcp`, and installing the Claude Code plugin connects it automatically. The README is direct about the economics: tool skills consume credits, new accounts start with a free balance, and the strategy skills work without any data source at all. Without a connection the skills still load, but the first audit fails with a message naming the missing MCP.

The tree carries 39 SKILL.md files and skills.sh indexes 20, so the table below is roughly half the suite. The unindexed half is mostly the tool skills and the routing and delivery skills, which have no install count to compare.

## Installation

The README offers five routes. The recommended one for Claude Code is the plugin, which also wires the MCP:

```text
/plugin marketplace add garrettjsmith/localseoskills
/plugin install local-seo-skills@garrettjsmith-localseo
```

A terminal one-liner does the same job on macOS and Linux:

```bash
curl -fsSL https://raw.githubusercontent.com/garrettjsmith/localseoskills/main/install.sh | bash
```

Windows has its own script:

```powershell
irm https://raw.githubusercontent.com/garrettjsmith/localseoskills/main/install.ps1 | iex
```

For Cursor, Codex, OpenClaw or any other Agent Skills host, the README uses the skills CLI with a global flag:

```bash
npx skills add garrettjsmith/localseoskills -g
```

It asks which agents to install for, and `-g` installs for the user rather than the current project. The manual route clones the repository and links each skill folder, because agents look only one folder deep:

```bash
git clone https://github.com/garrettjsmith/localseoskills.git ~/.agents/localseoskills
mkdir -p ~/.agents/skills
for d in ~/.agents/localseoskills/skills/*/; do ln -sfn "${d%/}" ~/.agents/skills/; done
```

Pick one route, not two. The README warns that the plugin and `install.sh` each install the skills, so using both makes every skill appear twice; if you installed with the script and later move to the plugin, run `uninstall.sh` or `uninstall.ps1` first. The plugin route also handles the MCP connection and opens a browser sign-in the first time a tool is used, with no API key written to any file.

Claude Desktop and Claude.ai in the browser install through Settings then Customize then Plugins, adding the same marketplace. The README notes the trade-off there: briefs need filesystem access, so Desktop can read and write briefs in a granted folder while the browser version keeps them session-scoped and requires you to paste them back into the Project. Persistent briefs are a Claude Code CLI feature in practice.

## What It Provides

The threshold for this guide is zero installs, so all 20 indexed listings appear below with the install integers exactly as skills.sh reports them:

| Skill | Installs | Use For |
|---|---|---|
| gbp-optimization | 226 | Google Business Profile setup and optimization for map pack visibility, including the "why am I not in the map pack" diagnosis |
| gbp-posts | 142 | Creating, scheduling and optimizing Google Business Profile posts and a GBP content calendar |
| review-management | 138 | Review generation, review responses, reputation strategy and star rating recovery |
| local-seo-audit | 126 | Full local search audit: local ranking problems, GBP audit findings and a prioritized local presence check |
| local-landing-pages | 118 | Location, city and service-area landing pages plus locally relevant blog and neighborhood content |
| local-schema | 113 | LocalBusiness structured data and local JSON-LD, including NAP markup and location schema |
| local-citations | 110 | Citation building, NAP consistency cleanup, directory listings and data aggregator audit |
| local-competitor-analysis | 106 | Benchmarking map pack rivals to explain who outranks the business and why |
| ai-local-search | 102 | Optimizing for AI Overviews, AI Mode, ChatGPT, Gemini, Perplexity and Grok answers in local search |
| gbp-suspension-recovery | 101 | Suspended or disabled profile triage, guideline violation review and reinstatement requests |
| service-area-seo | 100 | Service-area business strategy for businesses without a storefront, including hiding the address |
| geogrid-analysis | 98 | Geogrid scan interpretation: ARP, ATRP and SoLV metrics across a ranking heatmap |
| local-keyword-research | 96 | Local keyword research: near me terms, geo-modified keywords, city keywords and local intent mapping |
| local-ppc-ads | 96 | Geographically targeted Google Ads for local businesses with radius targeting and location targeting |
| local-reporting | 93 | Local SEO client reports, KPI tracking, GBP insights and reporting dashboards that show return |
| local-content-strategy | 92 | Turning keyword research into concept clusters, content vehicles, geogrid tracking keywords and internal linking |
| local-content-briefs | 89 | Semantic content briefs for location pages, service pages, blog posts, FAQs and pillar pages |
| google-search-console-tool | 86 | Search Console queries, indexing status, impressions, click-through rate and organic performance |
| local-link-building | 86 | Local backlinks from community organizations, sponsorships, chambers of commerce and local PR |
| apple-business-connect | 86 | Apple Maps listings through Apple Business Connect, Siri local visibility and Apple Intelligence local results |

No indexed listing falls below zero, so nothing is summarised into a tail line. The spread runs from 226 down to 86, a narrow range for a suite indexed in the low hundreds, so the ordering reflects attention rather than depth.

The 19 skills the index does not cover are worth knowing about, because several are central to the workflow. `dispatch` routes a request to the right skill, `brief` maintains the per-location state file, `gbp-api-automation` handles profile writes, `multi-location-seo` covers chains, `client-deliverables` packages output, `local-search-ads` and `lsa-ads` cover the paid local surfaces, `bing-places` covers Bing Maps listings, and the tool skills (`localseodata-tool`, `local-falcon-tool`, `ahrefs-tool`, `semrush-tool`, `dataforseo-tool`, `brightlocal-tool`, `whitespark-tool`, `serpapi-tool`, `lsa-spy-tool`, `screaming-frog-tool` and `google-analytics-tool`) do the data fetching. An install that stops at the 20 indexed rows leaves out the router, the state file and most of the data layer, which is why the default install takes all 39.

The README's own tour is the clearest description of scale. An audit of a plumbing business returns 47 issues with a drafted report and an initialized brief; a map pack question returns the top three issues in fix-priority order; a geogrid scan returns a 169-point grid with ARP, ATRP and SoLV computed; an AI visibility question scans four platforms and surfaces mention gaps.

## Why This Matters for Hermes Agents

Local SEO is repetitive work with a long memory requirement, which is exactly the shape an agent should own and exactly the shape a chat window does not. Six months into a client engagement, the useful question is "why did rankings drop in March", and the answer lives in the history of audits, fixes and ranking scans. The briefs system is the part of this repository that addresses that directly: one file per business and location, read and updated automatically, so the agent starts each session with state instead of a blank page.

The geogrid piece is the second reason this suite is more than a prompt pack. Local rank is a geography problem, not a single number, and the ARP, ATRP and SoLV metrics turn a heatmap into something an agent can reason about and a client can read. Any agent that reports local positions without a grid is reporting an average that hides the pattern the business actually cares about.

The third is the approval tiers on scheduled work: autonomous, queue and notify. That is a small piece of design with a large effect, because local SEO monitoring runs daily and a human cannot approve every run. Splitting tasks into those three classes lets monitoring and drafting run unattended while anything that writes to a profile waits.

The counterweight is that the tool half is commercially coupled. The default data layer is a paid API, the free balance does not last, and every data-driven answer spends credits. The strategy skills are portable, the data skills are not, and an agent that promises a weekly local audit is promising a bill as well as a workflow.

## Usage

| You say | What happens |
|---|---|
| "Audit Mike's Plumbing in Buffalo" | Runs the local audit, asks five quick questions, pulls citation and reputation data, and returns a prioritized issue list with a drafted report and an initialized brief |
| "Why am I not in the map pack?" | Applies GBP optimization and local pack data to identify the top three issues, ordered by fix priority rather than by ease |
| "Run a geogrid scan for plumber near me in Buffalo" | Runs the grid scan, renders the point map and computes ARP, ATRP and SoLV across the area |
| "How do I show up in ChatGPT for local searches?" | Scans the AI platforms in scope, compares mentions against competitors and surfaces the gaps that explain missing recommendations |
| "My Google Business Profile got suspended, what now" | Works the suspension path: guideline violation triage, evidence gathering and a reinstatement request sequence |
| "Write the copy for 12 city landing pages" | Builds content briefs from the keyword map, then drafts each page against its own brief with local proof points rather than one template repeated twelve times |
| "Build the monthly client report" | Pulls ranking, GBP insight and audit deltas into a client-facing report with the metrics that moved and the work that caused them |
| "Pick up where we left off on Keystone Insurance" | Reads the brief for the client across its locations, summarises where the work stopped and asks what to do next |

## Verification

The layout is `skills/<name>/SKILL.md`, so every raw path carries that segment. This one returns 200 and is the file the table lists first:

```bash
curl -fsSL https://raw.githubusercontent.com/garrettjsmith/localseoskills/main/skills/gbp-optimization/SKILL.md | head -8
```

It opens with YAML frontmatter holding `name: gbp-optimization`, a description that begins "When the user wants to set up, optimize, or manage a Google Business Profile", then the heading `# GBP Optimization & Map Pack Visibility`. A 404 here means the `skills/` layout moved and every path in this guide needs a new segment.

After an install, confirm the skills landed where the agent reads them. The README's clone route links every skill folder into `~/.agents/skills`, so that is the directory to inspect for a manual or `-g` install:

```bash
ls ~/.agents/skills | grep -E '^(gbp-optimization|geogrid-analysis|local-seo-audit)$'
ls ~/.agents/skills | wc -l
```

Three lines from the first command means those three skills are present, and the second prints how many skills are linked in total, which should be 39 after a full install. An empty first result means the CLI targeted a different agent than the one you are running. A plugin install is not visible there at all, because Claude Code manages it, so confirm that route in the plugin manager rather than on the filesystem.

The count check separates what skills.sh indexes from what the repository ships:

```bash
curl -fsSL "https://api.github.com/repos/garrettjsmith/localseoskills/git/trees/main?recursive=1" | grep -c '"path": ".*SKILL.md"'
```

That returns 39 against 20 indexed listings. The MCP connection is a separate check, and the plugin handles it on first use:

```bash
cat .mcp.json
```

The repository's own file points at `https://mcp.localseodata.com/mcp`. If an audit fails with a missing MCP message, that connection is the thing to fix, not the skill install.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-09) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| gbp-optimization | Pass | Pass | Pass |
| gbp-posts | Pass | Pass | Pass |
| review-management | Pass | Pass | Warn |
| local-seo-audit | Pass | Pass | Pass |
| local-landing-pages | Pass | Pass | Pass |
| local-schema | Pass | Pass | Pass |
| local-citations | Pass | Pass | Pass |
| local-competitor-analysis | Pass | Pass | Warn |
| ai-local-search | Pass | Pass | Pass |
| gbp-suspension-recovery | Pass | Pass | Pass |
| service-area-seo | Pass | Pass | Pass |
| geogrid-analysis | Pass | Pass | Pass |
| local-keyword-research | Pass | Pass | Pass |
| local-ppc-ads | Pass | Pass | Pass |
| local-reporting | Pass | Pass | Pass |
| local-content-strategy | Pass | Pass | Pass |
| local-content-briefs | Pass | Pass | Pass |
| google-search-console-tool | Pass | Pass | Pass |
| local-link-building | Pass | Pass | Pass |
| apple-business-connect | Pass | Pass | Pass |

Eighteen of the twenty are clean on all three scanners. The two Warns are Snyk verdicts on `review-management` and `local-competitor-analysis`, both skills that reach outward for review text and competitor data. No Fail appears in the sample, which is a better record than most suites of this size.

The risk that matters here is data rather than code. Every tool skill sends a client's business name, location, categories and search terms to a third-party API, and the default provider is a commercial service with its own retention policy. The repository ships a `PRIVACY.md` and the plugin declares `localseodata.com/privacy` as its policy URL, so read both before pointing this at client accounts that have their own data processing agreements. For agencies, the local SEO data flow is a processor relationship that usually needs to be named in a client contract.

The second surface is write access. The indexed skills are mostly strategy and reporting, but the tree contains `gbp-api-automation` and `gbp-posts`, which can change a live profile: hours, categories, posts, attributes. A wrong category edit on a verified listing is recoverable but visible, and a post published from a template can be worse. Keep the autonomous tier for read and draft work, put profile writes in the queue tier, and require a human on anything that changes NAP data.

The third is credential handling. The plugin route uses a browser sign-in and states that no API key goes into any file, which is the pattern to prefer; the alternative is an MCP token stored somewhere an agent can read. If you connect specialist tools (Ahrefs, Semrush, DataForSEO, BrightLocal, Whitespark, Local Falcon, LSA Spy, Screaming Frog, SerpAPI), each brings its own key and its own scope, and a single compromised environment variable exposes all of them.

## Limitations

- Snapshot data, verified 2026-11-09: 2,204 combined installs across 20 indexed listings; 147 GitHub stars; MIT; last pushed 2026-10-30. Counts drift over time.
- The skills.sh source page renders at most 20 listings while the repository carries 39 SKILL.md files. Nineteen skills have no published install count, including the dispatch router, the brief system and most of the tool wrappers, so the table describes half the suite.
- The data layer is commercial. Local SEO Data runs on paid credits with a free starting balance, and the specialist tool skills expect their own subscriptions. Strategy skills work without a data source, but the audit, geogrid and reporting examples in the README all spend credits.
- Install counts sit between 86 and 226 with no functional grouping behind them. The suite is young and small, so the ordering is not a quality signal and the absolute numbers are not comparable to repositories indexed in the thousands.
- Persistent briefs depend on a host with filesystem access. In Claude Desktop they work only in a granted folder, and in Claude.ai in the browser they are session-scoped and have to be pasted back into the Project, which removes most of the compounding-history benefit.
- Two Socket Warnings and a mostly clean scan is a snapshot of twenty listings, not an audit of 39. The unindexed tool skills, including the one that writes to Google Business Profile, have no published verdict at all.

## Related

- [Claude SEO - 31-Skill Universal SEO Suite Setup](/hermes/skills/catalog/claude-seo-setup)
- [GEO SEO Claude - Generative Engine Optimisation](/hermes/skills/catalog/geo-seo-claude-setup)
- [Claude Blog - AI Blog Writing and SEO Plugin Setup](/hermes/skills/catalog/claude-blog-setup)

## Pro Tips

- Install all 39, not the 20 with install counts. The dispatch router, the brief system and the tool wrappers are the parts that make the rest work, and they are exactly the ones the index does not surface.
- Start with a brief. Mentioning a business initializes the brief and asks a few questions; filling those in properly is what makes the six-months-later question answerable.
- Connect the data source before the first audit. Without it the audit fails with a missing MCP message, and a new account's free balance is enough to try the geogrid and citation flows before committing to credits.
- Put profile writes in the queue tier. `gbp-posts` and `gbp-api-automation` change a live listing, and the difference between a monitored task and an unattended one is the difference between a draft and a published post.
- Read `ai-local-search` even if you only care about the map pack. The AI answer surfaces cite different signals than the local pack, and the skill is the clearest written explanation of where the two overlap.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
