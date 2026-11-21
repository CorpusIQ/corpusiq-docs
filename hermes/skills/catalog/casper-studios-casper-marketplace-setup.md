---
title: "Casper Marketplace - Workflow Skills Setup Guide"
description: "casper-studios/casper-marketplace: 54 Claude Code skills for scraping, design, data and engineering tooling - 10.3K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/casper-studios-casper-marketplace-setup/"
robots: "index,follow"
last_updated: "2026-11-20"
tags: ["hermes skill", "agent skill", "skill setup", "claude code", "scraping", "workflow automation"]
---

# Casper Studios Casper Marketplace - Skills Setup Guide

**Source:** [casper-studios/casper-marketplace](https://www.skills.sh/casper-studios/casper-marketplace) via skills.sh - 10.3K combined installs across 54 indexed listings; first seen Nov 20, 2026 (Nov 20, 2026 evening sweep)
**GitHub:** [Casper-Studios/casper-marketplace](https://github.com/Casper-Studios/casper-marketplace) - 14 stars, MPL-2.0 license, main branch, last pushed Nov 13, 2026; skills live under `plugins/<workstream>/<plugin>/skills/<name>/SKILL.md` with shared `.claude-plugin/plugin.json` and `marketplace.json` manifests for Claude Code and Codex.
**Category:** Claude Code Skills Marketplace
**Quality Tier:** 🟠 Orange - the 20-skill sample carries 2 Fail and 13 Warn cells across Gen Agent Trust Hub, Socket and Snyk.

`casper-marketplace` is a Claude Code marketplace from Casper Studios that bundles 54 indexed skills for business automation, data analysis and productivity. The collection spans social and web scraping (Apify actors and Firecrawl), interface design (Apple's Liquid Glass and the Casper design system), content work (LinkedIn post generation and YouTube tooling), data analysis for financial and RevOps contexts, and a large set of engineering best-practice references for React, TanStack, TypeScript, Zod, Valibot, Drizzle and Python.

Skills are organized as plugins under `plugins/<workstream>/<plugin>/` and share `.claude-plugin/plugin.json` plus `marketplace.json` manifests, so the same skills install into Claude Code and Codex from one source. First seen in the Nov 20, 2026 evening sweep with 10.3K combined installs across 54 indexed listings.

## Installation

```bash
# install every skill globally
npx skills add https://github.com/Casper-Studios/casper-marketplace --all -g
```

The `--all` flag is idempotent: it installs new skills and overwrites existing ones, and the CLI handles cloning, diffing and symlinking internally.

Install individual skills by name:

```bash
npx skills add https://github.com/Casper-Studios/casper-marketplace --skill commit
npx skills add https://github.com/Casper-Studios/casper-marketplace --skill resolve-pr-comments
```

Claude Code users can add the marketplace and install plugins with slash commands:

```text
/plugin marketplace add Casper-Studios/casper-marketplace
/plugin install research
/plugin install data-analysis
/plugin install git-pr
```

Codex users install from a local checkout of the repository:

```bash
codex plugin marketplace add .
codex plugin add research@casper-studios
```

To keep plugins current on session start, download `sync-skills.sh` and register it as a Claude Code SessionStart hook (the README carries the exact `~/.claude/settings.json` block).

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| google-workspace | 348 | Google Workspace automation |
| apify-scrapers | 348 | Social media and web scraping via Apify actors |
| liquid-glass | 345 | Native Apple apps using the Liquid Glass design language |
| firecrawl-scraping | 341 | Web scraping via Firecrawl |
| data-analysis | 340 | Data analysis and storytelling for financial and RevOps contexts |
| csv-analyzer | 331 | CSV data inspection and analysis |
| content-generation | 313 | Content generation |
| attio-crm | 312 | Attio CRM workflows |
| linkedin-post-generator | 311 | LinkedIn posts from transcripts and notes in your writing style |
| commit | 308 | Conventional commit messages and staged changes |
| youtube-tools | 306 | YouTube download, transcript and metadata via yt-dlp |

The remaining 43 indexed listings range from 18 to 296 installs. That tail splits into a mid-band of workflow and tooling skills (pr-comments, pr-summary, bump-deps, video-production, casper-design-system and similar, 224 to 296 installs) and a low band of engineering best-practice references (typescript-best-practices, react-best-practices, zod-best-practices and a dozen more, 18 to 22 installs).

## Why This Matters for Hermes Agents

This marketplace matters because it concentrates the grunt work of business workflows into installable skills. The scraping skills route social and web data collection through Apify actors and Firecrawl, so an agent spends its budget on analysis instead of hand-rolling request code. The data-analysis skill adds decision logging and bias-aware interpretation, which keeps analytical claims auditable. The engineering best-practice skills are concise reference packs that steer generated code toward idiomatic React, TanStack, TypeScript, Zod, Valibot, Drizzle and Python patterns instead of plausible-looking shortcuts. The design skills give an agent a concrete visual language, Casper's design system for SaaS UI and Apple's Liquid Glass for native apps, so output matches a real product language. The shared plugin manifests mean the same skills install into Claude Code and Codex, so the guidance travels with the agent across hosts.

## Usage

| You say | What happens |
|---|---|
| Scrape Twitter/X posts and Reddit threads about a topic | apify-scrapers runs the matching Apify actor and returns posts, trends or contact details |
| Generate a LinkedIn post from this meeting transcript | linkedin-post-generator drafts the post in your writing style from the transcript or a Slack dump |
| Download this YouTube video and pull its transcript | youtube-tools retrieves the video, transcript or metadata with yt-dlp, no API key needed |
| Analyze this revenue CSV and build a dashboard | data-analysis cleans the data, sanity-checks claims and produces a report or dashboard |
| Commit these changes | commit writes a conventional commit message and stages the changes |
| Build a native macOS settings screen | liquid-glass applies Apple's Liquid Glass materials, spacing and SF Symbols |

## Verification

```bash
# review a skill before relying on it
curl -sL https://raw.githubusercontent.com/Casper-Studios/casper-marketplace/main/plugins/engineering/git-pr/skills/commit/SKILL.md
```

The raw SKILL.md URL above was probed Nov 20, 2026 and returned HTTP 200. Skills live under `plugins/<workstream>/<plugin>/skills/<name>/SKILL.md`; the `commit` skill sits at `plugins/engineering/git-pr/skills/commit/SKILL.md`.

## Security

skills.sh verdicts for sampled skills (verified Nov 20, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| google-workspace | Pass | Pass | Warn |
| apify-scrapers | Fail | Pass | Warn |
| liquid-glass | Pass | Pass | Pass |
| firecrawl-scraping | Pass | Pass | Warn |
| data-analysis | Warn | Pass | Pass |
| csv-analyzer | Pass | Pass | Pass |
| content-generation | Pass | Pass | Warn |
| attio-crm | Pass | Pass | Pass |
| linkedin-post-generator | Warn | Warn | Warn |
| commit | Pass | Pass | Pass |
| youtube-tools | Pass | Pass | Warn |
| pr-comments | Pass | Pass | Warn |
| pr-summary | Pass | Pass | Pass |
| extract-my-action-items | Pass | Pass | Warn |
| bump-deps | Pass | Pass | Warn |
| casper-design-system | Pass | Pass | Pass |
| video-production | Pass | Pass | Fail |
| polishing | Pass | Pass | Pass |
| recover-branch-context | Pass | Pass | Pass |
| composio-connect | Pass | Pass | Warn |

## Limitations

- Snapshot data, verified Nov 20, 2026: 10,292 combined installs across 54 indexed listings; 14 GitHub stars; MPL-2.0 license; last pushed Nov 13, 2026. Counts drift over time.
- The 20-skill sample carries 2 Fail verdicts (apify-scrapers on Gen Agent Trust Hub, video-production on Snyk) and 13 Warn cells, so each skill needs its own review before production use rather than inheriting a clean bill from the marketplace.
- MPL-2.0 is file-level copyleft: any file you modify from these skills keeps MPL-2.0 terms, so review individual files before bundling them into a proprietary product.
- The install index outruns the tree: 27 of the 54 indexed listings (google-workspace, firecrawl-scraping, csv-analyzer, content-generation, attio-crm, video-production, pr-comments and others) carry install counts but have no matching skill directory in the current main tree.
- The README states MIT while GitHub metadata reports MPL-2.0, so confirm the license on the exact file you copy.

## Related

- [Apify Agent Skills - Web Scraping for Hermes Setup](/hermes/skills/catalog/apify-agent-skills-setup)
- [Firecrawl Skills - Web Scraping Setup](/hermes/skills/catalog/firecrawl-skills-setup)
- [Code Review Skill - Review Workflow Setup](/hermes/skills/catalog/code-review-skill-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the whole marketplace once with `--all -g`; the flag is idempotent and safe to re-run for updates.
- Prefer `--skill <name>` for a focused install so you can review one skill before it enters your workflow.
- Curl a skill's raw SKILL.md before relying on it; the index lists more skills than the current tree actually holds.
- Watch the two Fail verdicts (apify-scrapers, video-production) and re-check the skills.sh security pages before production use.
- Register `sync-skills.sh` as a Claude Code SessionStart hook so plugins stay current without manual reinstalls.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
