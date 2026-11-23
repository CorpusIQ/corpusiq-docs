---
title: "Okou Skills - Integration and Automation Skills Setup"
description: "okou-ai/okou-skills: reusable Agent Skills for SaaS and API integrations, independent of the VM0 connector catalog - 16.3K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/okou-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-23"
tags: ["hermes skill", "agent skill", "skill setup", "integration", "api", "saas"]
---

# Okou Skills - Setup Guide

**Source:** [okou-ai/okou-skills](https://www.skills.sh/okou-ai/okou-skills) via skills.sh - 16.3K combined installs across 96 indexed listings; first catalogued Nov 23, 2026 (Nov 23, 2026 morning sweep)
**GitHub:** [okou-ai/okou-skills](https://github.com/okou-ai/okou-skills) - 81 stars, no LICENSE file, main branch, last pushed Nov 23, 2026; each skill is a directory with its SKILL.md at the repository root, with office/ bundling docx, pdf and xlsx subskills redistributed from MiniMax-AI/skills.
**Category:** SaaS and API Integration Skills
**Quality Tier:** 🟠 Orange - minio carries Fail cells in both the Gen Agent Trust Hub and Snyk columns, with 11 Snyk Warn cells across the rest of the 20-skill sample.

okou-skills is a collection of reusable Agent Skills that follow the Agent Skills specification and are independent of okou's VM0 connector catalog. Each skill holds practical guidance for one well-defined capability, keeps its instructions and supporting resources self-contained, and documents its commands in SKILL.md so the skill can be audited and compliance-checked.

The collection spans API and SaaS connectors such as hackernews, cloudflare-tunnel, google-sheets and strava, alongside larger bundles: office (docx, pdf and xlsx, redistributed from MiniMax-AI/skills), a business-skill-index covering 62 skills across 18 scenarios, an event-flyer-pack and people-search. Skills owned by a VM0 connector live with their connector definition in the separate okou-connectors repository.

## Installation

Install specific skills through the Claude Code marketplace:

```bash
# Add marketplace
/plugin marketplace add okou-ai/okou-skills

# Install specific skills
/plugin install github-copilot@vm0-skills
/plugin install hackernews@vm0-skills
```

Or clone and copy individual skill directories:

```bash
git clone https://github.com/okou-ai/okou-skills.git
cp -a okou-skills/github-copilot ~/.claude/skills/
cp -a okou-skills/hackernews ~/.claude/skills/
```

After installation, restart Claude Code and ask "What skills are available?" to confirm.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| hackernews | 3,156 | Hacker News stories and comments via the official API |
| cloudflare-tunnel | 891 | Cloudflare Tunnel API for secure, named tunnels |
| google-sheets | 849 | Google Sheets data connector |
| strava | 584 | Strava activity data connector |
| line | 434 | LINE messaging connector |
| minimax | 429 | MiniMax model connector |
| apify | 379 | Apify actor and scraping connector |
| lark | 285 | Lark collaboration connector |
| firecrawl | 283 | Firecrawl web scraping connector |
| deepseek | 282 | DeepSeek model connector |
| discord-webhook | 258 | Discord webhook messaging |
| minio | 213 | MinIO object storage connector |

The remaining 84 indexed listings range from 47 to 190 installs.

Use For is name-level for most rows: only hackernews and cloudflare-tunnel carry in-tree SKILL.md descriptions in the repository, and most indexed connector skills have no directory in this repository (see Limitations).

## Why This Matters for Hermes Agents

An agent that needs to read Hacker News, push a Discord message or query a spreadsheet otherwise writes ad hoc fetch-and-parse code that breaks the moment an API changes. These skills wrap one well-defined capability each with tested usage and documented commands, so the agent calls a procedure instead of improvising. The most valuable are hackernews (the flagship at 3,156 installs, wrapping the official stories and comments API) and cloudflare-tunnel (secure tunnels by name). The security-first principle matters for operators: every SKILL.md documents its commands, so a skill can be audited and compliance-checked before use. Keeping connector-owned skills in a separate repo keeps this collection self-contained and focused.

## Usage

| You say | What happens |
|---|---|
| What are the top stories on Hacker News? | hackernews fetches stories and comments from the official API |
| Set up a Cloudflare tunnel for this service | cloudflare-tunnel creates a secure named tunnel via the API |
| Read this spreadsheet and summarize it | google-sheets connector reads the sheet data |
| Post this update to Discord | discord-webhook connector sends the message |
| Scrape this site | firecrawl or apify connector fetches page content |
| Is this object in MinIO? | minio connector checks the object store |

## Verification

Confirm the flagship skill resolves on the main branch:

```bash
curl -sL https://raw.githubusercontent.com/okou-ai/okou-skills/main/hackernews/SKILL.md | head -30
```

Spot-check a second root-level skill to confirm the flat layout:

```bash
curl -sL https://raw.githubusercontent.com/okou-ai/okou-skills/main/cloudflare-tunnel/SKILL.md | head -30
```

Review the README before relying on install commands:

```bash
curl -sL https://raw.githubusercontent.com/okou-ai/okou-skills/main/README.md | head -40
```

## Security

skills.sh verdicts for sampled skills (verified Nov 23, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| hackernews | Pass | Pass | Warn |
| cloudflare-tunnel | Pass | Pass | Pass |
| google-sheets | Pass | Pass | Warn |
| strava | Pass | Pass | Warn |
| line | Pass | Pass | Warn |
| minimax | Pass | Pass | Warn |
| apify | Pass | Pass | Warn |
| lark | Pass | Pass | Pass |
| firecrawl | Pass | Pass | Warn |
| deepseek | Pass | Pass | Pass |
| discord-webhook | Pass | Pass | Pass |
| minio | Fail | Pass | Fail |
| browserless | Pass | Pass | Warn |
| bitrix | Pass | Pass | Pass |
| gmail | Pass | Pass | Pass |
| slack-webhook | Pass | Pass | Pass |
| htmlcsstoimage | Pass | Pass | Warn |
| chatwoot | Pass | Pass | Warn |
| cloudinary | Pass | Pass | Pass |
| scrapeninja | Pass | Pass | Warn |

minio is the only Fail: both the Gen Agent Trust Hub and Snyk columns flag it, and the other 11 Warn cells are all Snyk (hackernews, google-sheets, strava, line, minimax, apify, firecrawl, browserless, htmlcsstoimage, chatwoot and scrapeninja); 76 of the 96 indexed listings carry no published verdict.

## Limitations

- Snapshot data, verified Nov 23, 2026: 16,328 combined installs across 96 indexed listings; 81 GitHub stars; no LICENSE file; last pushed Nov 23, 2026. Counts drift over time.
- The index is capped at 96 listings (the skills.sh API ceiling), so the collection may hold more skill directories than the index shows.
- Index and tree diverge substantially: 79 of the 96 indexed listings (google-sheets, strava, line, minimax and dozens more) have no directory in the current tree, while the tree also holds many directories that are not indexed (business-skill-index, office, people-search, event-flyer-pack and the illustration-template and extract-template families).
- The repository has no LICENSE file at its root; the office/ subpackages carry their own MIT licenses from the upstream MiniMax-AI/skills distribution.
- Below the top four skills, install counts fall into a long flat band from 434 down to 47, so most of the collection is indistinguishable by installs alone.

## Related

- [Apify Agent Skills - Full Setup Guide for Hermes Agents](/hermes/skills/catalog/apify-agent-skills-setup)
- [Firecrawl Skills - Setup Guide](/hermes/skills/catalog/firecrawl-skills-setup)
- [Cloudflare Skills - Edge Computing & Workers Platform](/hermes/skills/catalog/cloudflare-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install per-skill rather than the whole repository: the README copies individual directories, so you pull only what you need.
- After installation, restart Claude Code and ask "What skills are available?" to confirm the install.
- Connector-owned skills live in okou-connectors, not this repository; check there when a connector skill is missing from the tree.
- Review the minio Fail verdict (Gen Agent Trust Hub and Snyk) before using that skill in production.
- The office bundle (docx, pdf, xlsx) is redistributed from MiniMax-AI/skills and carries its own upstream licenses; read UPSTREAM.md in each subdirectory.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
