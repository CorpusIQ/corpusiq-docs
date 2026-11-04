---
title: "GEO SEO Claude - Generative Engine Optimisation"
description: "zubair-trabzada/geo-seo-claude on skills.sh: 14.7K combined installs across 16 listings; GEO audits, citability scores, llms.txt and client reports."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/geo-seo-claude-setup/"
robots: "index,follow"
last_updated: "2026-11-04"
tags: ["hermes skill", "agent skill", "skill setup", "generative engine optimization", "seo"]
---

# GEO SEO Claude - Setup Guide

**Source:** [zubair-trabzada/geo-seo-claude](https://www.skills.sh/zubair-trabzada/geo-seo-claude) via skills.sh - 14.7K combined installs across 16 indexed listings; first documented November 4, 2026 (morning sweep)
**GitHub:** 11,491 stars, MIT licence, last pushed 2026-11-04, 16 SKILL.md directories (one orchestrator plus 15 sub-skills)
**Category:** AI search visibility: answer-engine optimization, AI citation auditing, schema and content restructuring for LLM discovery
**Quality Tier:** 🟡 Yellow: four of the five sampled skills draw a Snyk Warn even though Gen Agent Trust Hub and Socket pass on all five

This is a single-purpose suite: make a site more likely to be read, quoted and cited by AI answer engines, and produce the paperwork an agency needs afterwards. One orchestrator skill (geo) routes twelve slash commands, and fifteen sub-skills do the work. Five subagents run in parallel during a full audit (AI visibility, platform analysis, technical, content, schema), then a synthesis step reports a composite GEO Score out of 100.

The tooling is not prompt-only. The repo ships Python scripts for page fetching, citability scoring, brand scanning, llms.txt generation and PDF reports, installed into a dedicated virtual environment at ~/.claude/skills/geo/.venv/ so your system Python is untouched. Reporting skills also keep lightweight CRM state in ~/.geo-prospects/.

Note the name collision risk: this is zubair-trabzada/geo-seo-claude, not aaron-he-zhu/seo-geo-claude-skills, which is a separate 20-skill pack and has its own page in this catalog.

## Installation

The README documents a one-command install for macOS and Linux:

```bash
curl -fsSL https://raw.githubusercontent.com/zubair-trabzada/geo-seo-claude/main/install.sh | bash
```

Or clone and run the installer locally:

```bash
git clone https://github.com/zubair-trabzada/geo-seo-claude.git
cd geo-seo-claude
./install.sh
```

Windows users run install-win.sh from Git Bash rather than PowerShell or CMD:

```bash
curl -fsSL https://raw.githubusercontent.com/zubair-trabzada/geo-seo-claude/main/install-win.sh | bash
```

Requirements are Python 3.10 or later, the Claude Code CLI and Git. If uv is present the installer uses it for a faster dependency install; Playwright is optional and only needed for screenshots.

The installer writes the orchestrator to ~/.claude/skills/geo, the fifteen sub-skills to ~/.claude/skills/geo-*, and five subagent definitions to ~/.claude/agents/geo-*.md. For a Hermes agent, copy those directories into your own agent skills directory after running the installer; the Python scripts are pinned to the installer's venv path, so keep the directory layout intact or edit the shebangs.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| geo-llmstxt | 1,307 | Validate or generate an llms.txt file from a crawl |
| geo | 1,007 | Orchestrator and command router for the whole suite |
| geo-audit | 990 | Full audit with five parallel subagents and a composite score |
| geo-schema | 978 | Detect, validate and generate JSON-LD for AI discoverability |
| geo-crawlers | 937 | robots.txt, meta and header access map for AI crawlers |
| geo-citability | 913 | Citability score out of 100 with rewrite suggestions |
| geo-technical | 906 | Technical SEO audit with GEO-specific checks |
| geo-platform-optimizer | 894 | Per-engine tuning for AI Overviews, ChatGPT, Perplexity, Gemini and Copilot |
| geo-content | 894 | E-E-A-T and content structure assessment |
| geo-report-pdf | 893 | Styled client PDF report built from the audit markdown |
| geo-report | 887 | Client-facing markdown report with scores and priorities |
| geo-brand-mentions | 886 | Brand Authority Score across platforms AI models cite |
| geo-compare | 846 | Baseline versus current audit delta report |
| geo-prospect | 842 | CRM-lite pipeline tracking from lead to won |
| geo-proposal | 839 | Proposal generation with packages, pricing and timeline |
| geo-update | 647 | Pull upstream updates and diff installed files |

No indexed listings fall below the threshold; all 16 appear above.

## Why This Matters for Hermes Agents

GEO work is a chain of small, checkable measurements, which is exactly the shape an agent handles well and a human handles inconsistently. The suite encodes the chain: is the crawler allowed in, is the passage quotable, is the entity recognisable, is the schema valid, is the report deliverable.

The scoring model is the useful design decision. Each category carries a weight (AI citability 25%, brand authority 20%, content and E-E-A-T 20%, technical 15%, structured data 10%, platform optimisation 10%), so an agent can report a defensible number instead of a vibes assessment. Whether you agree with the weights, having them written down means two audits of the same site are comparable.

The parallel subagent pattern is worth copying for any Hermes audit workflow. Five narrow agents with their own context beats one agent that has to hold citability, schema and Core Web Vitals at once, and the orchestrator only has to merge structured findings.

The suite also stops at a specific line: it measures and recommends, it does not edit your site. That makes it safe to point at a production domain.

## Usage

| You say | What happens |
|---|---|
| /geo audit https://example.com | Discovery, five parallel subagents, composite GEO score and prioritised action plan |
| /geo quick https://example.com | 60-second visibility snapshot when you need a fast read |
| /geo citability https://example.com | Scores passages for AI citation readiness and suggests rewrites |
| /geo crawlers https://example.com | Maps which AI crawlers can reach the site and what to change |
| /geo llmstxt https://example.com | Validates an existing llms.txt or generates one from the crawl |
| /geo report https://example.com | Client-ready report combining scores, findings and next actions |
| "Compare this month against the baseline audit" | geo-compare diffs the two audits and writes a client progress report |

## Verification

Confirm the install landed where the skills expect it:

```bash
ls ~/.claude/skills
```

You should see geo plus the geo-* sub-skills, and ~/.claude/agents/ should hold the five geo-* subagent files. Then fetch one raw skill file to confirm the tree matches what skills.sh indexed. This URL is the geo/SKILL.md orchestrator path on branch main:

```bash
curl -fsSL https://raw.githubusercontent.com/zubair-trabzada/geo-seo-claude/main/geo/SKILL.md | head -30
```

A response with YAML frontmatter, a name field and a command routing table confirms the content is live. Finally, run a snapshot against a domain you own:

```text
/geo quick https://example.com
```

## Security

skills.sh verdicts for sampled skills (verified November 4, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| geo-llmstxt | Pass | Pass | Warn |
| geo-crawlers | Pass | Pass | Warn |
| geo-content | Pass | Pass | Warn |
| geo-compare | Pass | Pass | Pass |
| geo-update | Pass | Pass | Warn |

Two things to review before production use. The install path pipes a remote script into bash, so read install.sh first or use the clone-and-run route. The skills execute network fetches and a local Python environment, and the prospect, proposal and compare skills write client data to ~/.geo-prospects/, which the uninstaller deliberately leaves in place.

## Limitations

- Snapshot data, verified November 4, 2026: 14,666 combined installs across 16 indexed listings; 11,491 GitHub stars; MIT licence; last pushed 2026-11-04. Counts drift over time.
- This is zubair-trabzada/geo-seo-claude. The similar aaron-he-zhu/seo-geo-claude-skills pack is a different repository with a different skill set and its own catalog page.
- The README describes "13 specialized sub-skills" but lists 14 in its architecture tree, and the current repository carries 15 under skills/ plus the geo orchestrator. Trust the tree over the prose.
- Four of five sampled skills carry a Snyk Warn; none is an outright fail, but re-check the verdict pages before wiring this into a client engagement.
- The installer targets ~/.claude/skills and ~/.claude/agents, so Hermes users need a manual copy step and may need to repoint the pinned Python shebangs.
- Prospect, proposal and compare data lives in ~/.geo-prospects/ and survives uninstall. Delete it yourself if you handle client data under a retention policy.
- PDF reports need pandoc and a Chrome binary on top of the Python requirements; the markdown report path has no such dependency.

## Related

- [SEO GEO Claude Skills - SEO & Generative Engine Optimization Suite Setup](/hermes/skills/catalog/seo-geo-claude-skills-setup)
- [OpenSEO - Self-Hosted SEO Platform, MCP and Skills Setup](/hermes/skills/catalog/open-seo-setup)
- [SEO Skill - Search Console MCP for Agents Setup](/hermes/skills/catalog/iannuttall-seo-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run /geo quick before /geo audit. The snapshot tells you which category is worth the full parallel run.
- Keep the baseline report. geo-compare needs the earlier audit to compute a delta, and a delta is what renews a retainer.
- Point the crawler check at robots.txt you actually control before changing anything; the recommendation output is specific enough to paste.
- Treat the composite score as a trend line rather than an absolute. The weights are fixed in the README, so compare months, not sites.
- Review the citability rewrites by hand. The script scores passage length and self-containment; it does not know your product claims.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
