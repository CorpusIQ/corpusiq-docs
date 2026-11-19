---
title: "Infrasity Dev GTM Skills - SEO, GEO and Marketing Setup"
description: "infrasity-labs/dev-gtm-claude-skills: 10.2K combined installs across 96 listings; SEO, GEO and developer-marketing skills for docs AI systems cite."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/infrasity-dev-gtm-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-18"
tags: ["hermes skill", "agent skill", "skill setup", "seo", "geo", "developer marketing"]
---

# Infrasity Dev GTM Skills - Setup Guide

**Source:** [infrasity-labs/dev-gtm-claude-skills](https://www.skills.sh/infrasity-labs/dev-gtm-claude-skills) via skills.sh - 10.2K combined installs across 96 indexed listings; first seen Nov 18, 2026 (Nov 18, 2026 evening sweep)
**GitHub:** 172 stars, MIT licence, `main` branch, last pushed 2026-06-28. Skills live as one `SKILL.md` per directory across five bundles (`skills/`, `marketing-skills/`, `writing-skills/`, `seo-skills/`, `notion-skills/`), with a mirror under `.claude/skills/` for Claude Code.
**Category:** SEO, GEO and developer marketing
**Quality Tier:** 🟠 Orange - 4 Fail cells among the 12 sampled skills (api-docs-quality-report, docs-auditor, sdk-docs-auditor, blog-post-counter); MIT licence.

Infrasity's dev-gtm-claude-skills is a collection of open-source Claude skills for SEO, GEO (Generative Engine Optimization), AI discoverability, and developer marketing. Each skill is a self-contained `SKILL.md` package with optional stdlib-only Python tooling and reference docs, so it runs in Claude Code, Claude Desktop, Claude.ai, and any agent that reads the open `SKILL.md` standard; the README lists Hermes Agent among the tested targets.

The set is aimed at developer-focused companies (DevTools, AI-agent platforms, observability, B2B SaaS) that need their documentation and content cited by AI systems such as ChatGPT, Claude, Perplexity and Gemini, not just indexed by Google. The top of the install list is the docs-auditing cluster (llms-txt-checker, docs-auditor, sdk-docs-auditor, api-docs-quality-report), with the blog and marketing engines filling the long tail.

## Installation

The README's quick install pulls every skill into Claude Code in one command:

```bash
npx skills add Infrasity-Labs/dev-gtm-claude-skills
```

The blog engine adds five subagents and shared Python scripts, which need one extra step:

```bash
git clone https://github.com/infrasity-labs/dev-gtm-claude-skills.git
cd dev-gtm-claude-skills
./scripts/claude-blog-install.sh
pip install -r writing-skills/requirements.txt
```

Manual install copies a single skill into the Claude Code skills directory:

```bash
git clone https://github.com/infrasity-labs/dev-gtm-claude-skills.git
cp -r dev-gtm-claude-skills/skills/<skill-name> ~/.claude/skills/
```

For Claude Desktop or Claude.ai, zip a skill directory and upload it under Settings > Customize > Skills. Most skills need no API keys; the live-search skills (growth-report, blog-post-counter, api-docs-quality-report) pull data through a DataForSEO MCP server.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| llms-txt-checker | 147 | Audit a domain's AI-readiness by probing robots.txt, llms.txt and llms-full.txt with curl and scoring each against a checklist. |
| growth-report | 139 | Generate a 3-month SEO performance HTML report for a domain using DataForSEO traffic and keyword data. |
| brief-outline-generator | 139 | Generate a structured SEO content outline and export it as a formatted .docx for a writer to fill in. |
| api-docs-quality-report | 138 | Audit an API docs site by crawling endpoint pages and scoring five checks, with an interactive HTML report. |
| docs-auditor | 137 | Audit a developer documentation site across 33 checks in 7 categories and return a score out of 100. |
| sdk-docs-auditor | 136 | Audit an SDK documentation site and produce a fully scored, downloadable HTML report. |
| blog-post-counter | 136 | Count and compare blog posts against competitors, audit content freshness, and map competitor keyword gaps. |
| no-outlinks-audit | 135 | Find dead-end pages with zero outgoing internal links and generate link suggestions with anchor text. |
| orphan-pages-internal-linking-opportunities | 135 | Audit orphan blog pages, map internal links, and generate keyword-backed interlinking briefs. |
| ai-seo | 120 | Optimize content so it gets cited and surfaced by AI assistants and AI search engines (AEO and GEO). |
| copywriting | 120 | Write or rewrite marketing copy for home, landing, pricing, feature and product pages. |

The remaining 85 indexed listings range from 92 to 119 installs.

## Why This Matters for Hermes Agents

For an agent that writes documentation and marketing content, the default failure mode is content that is readable but invisible: published pages that no AI answer engine ever cites because there is no llms.txt, no structured data, and no internal linking. These skills turn that around with concrete, crawler-backed audits rather than vibes.

The docs-auditing cluster is the standout: llms-txt-checker, docs-auditor, sdk-docs-auditor and api-docs-quality-report each crawl a real site, score it against a named checklist, and return pass/warn/fail findings with fixes. Because they are plain `SKILL.md` files with stdlib-only tooling, a Hermes agent can run them directly, not only through the Claude-oriented installers.

The rest of the set spans the developer-marketing funnel, from SEO content briefs and competitor keyword mapping to pricing, cold email and growth reporting. Install the auditing cluster first, then pull specific marketing skills as needed.

## Usage

| You say | What happens |
|---|---|
| "Check if this domain is AI-ready" | llms-txt-checker probes robots.txt, llms.txt and llms-full.txt and returns pass/warn/fail findings with fixes. |
| "Audit our developer docs" | docs-auditor runs 33 checks in 7 categories and returns a score out of 100. |
| "Score our API reference docs" | api-docs-quality-report crawls endpoint pages, scores five checks, and renders an interactive HTML report. |
| "How many blog posts do we have versus Competitor X?" | blog-post-counter compares post counts, freshness, and keyword gaps between the two domains. |
| "Find our dead-end pages" | no-outlinks-audit detects pages with zero outgoing internal links and suggests three links per page. |
| "Make our content get cited by ChatGPT" | ai-seo applies AEO and GEO optimization so the content surfaces in AI answers. |
| "Rewrite our pricing page copy" | copywriting rewrites the page for persuasion and conversion. |

## Verification

Probe one skill on the `main` branch before installing. It returns 200:

```bash
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/infrasity-labs/dev-gtm-claude-skills/main/skills/llms-txt-checker/SKILL.md
```

Then install the full set and trigger a docs audit to confirm the skill loads:

```bash
npx skills add Infrasity-Labs/dev-gtm-claude-skills
```

## Security

skills.sh verdicts for sampled skills (verified Nov 18, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| llms-txt-checker | Pass | Pass | Warn |
| growth-report | Pass | Pass | Warn |
| brief-outline-generator | Pass | Pass | Warn |
| api-docs-quality-report | Pass | Pass | Fail |
| docs-auditor | Pass | Pass | Fail |
| sdk-docs-auditor | Fail | Warn | Warn |
| blog-post-counter | Fail | Pass | Warn |
| no-outlinks-audit | Pass | Pass | Warn |
| orphan-pages-internal-linking-opportunities | Pass | Pass | Pass |
| ai-seo | Pass | Pass | Pass |
| copywriting | Pass | Pass | Pass |
| analytics | Pass | Pass | Pass |

The sample covers 12 of the 96 indexed listings. The four Fail cells sit on the docs-auditing and blog-reporting skills that crawl and shell out the most; every skill in this sample carries at least one Warn or Fail in one column.

## Limitations

- Snapshot data, verified Nov 18, 2026: 10,155 combined installs across 96 indexed listings; 172 GitHub stars; MIT licence; last pushed 2026-06-28. Counts drift over time.
- The eleven skills shown above carry most of the install volume; the other 85 indexed listings sit between 92 and 119 installs and are long-tail.
- The live-search skills (growth-report, blog-post-counter, api-docs-quality-report) depend on a DataForSEO MCP server for their data, so those need extra setup before they return results.
- The blog engine needs its subagents and shared scripts installed separately, plus Python dependencies (textstat, beautifulsoup4) and per-skill credentials for a few blog sub-skills.
- The repo has not been pushed since 2026-06-28, so treat the installer commands and paths as current at snapshot time only.

## Related

- [Claude GTM Plugin Skills - GTM Teams Setup](/hermes/skills/catalog/claude-gtm-plugin-setup)
- [GTM Agents - Go-to-Market Sales Skills Setup](/hermes/skills/catalog/gtm-agents-setup)
- [SEO GEO Claude Skills - SEO & Generative Engine Optimization Suite Setup](/hermes/skills/catalog/seo-geo-claude-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the auditing cluster first (llms-txt-checker, docs-auditor, sdk-docs-auditor, api-docs-quality-report); they are the most installed and need no API keys.
- Run llms-txt-checker on any docs domain before writing GEO content, so you know what is already discoverable.
- Copy a single skill directory into ~/.claude/skills/ to try one without pulling all 96.
- Add the DataForSEO MCP server only if you use growth-report, blog-post-counter or api-docs-quality-report; the rest run without it.
- Re-run npx skills add Infrasity-Labs/dev-gtm-claude-skills any time to refresh to the latest skills.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
