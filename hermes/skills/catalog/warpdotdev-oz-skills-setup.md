---
title: "Warp Oz Skills - Agent Skills Collection Setup"
description: "warpdotdev/oz-skills - 3.4K combined installs: Warp Oz agent skills for SEO audits, CI fixes, MCP building, and dev workflows."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/warpdotdev-oz-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-25"
tags: ["hermes skill", "agent skill", "skill setup", "warp", "dev workflow", "mcp"]
---

# Warp Oz Skills - Setup Guide

**Source:** [warpdotdev/oz-skills](https://www.skills.sh/warpdotdev/oz-skills) via skills.sh - 3.4K combined installs across 15 indexed listings; first catalogued Nov 25, 2026 (Nov 25, 2026 morning sweep)
**GitHub:** [warpdotdev/oz-skills](https://github.com/warpdotdev/oz-skills) - 823 stars, MIT license, last pushed Aug 15, 2026, main branch; 15 skill folders under .agents/skills/<name>/SKILL.md.
**Category:** Developer Workflows (Warp / Oz Agents)
**Quality Tier:** 🟡 Yellow - 15 sampled skills: nine carry a Warning (webapp-testing carries two) and six pass all three checks; no Fails.

warpdotdev/oz-skills is Warp's curated collection of reusable Agent Skills for Warp AI agents and Oz. The 15 indexed listings cover SEO and AI-visibility audits, GitHub issue triage and dedupe, CI failure fixes, accessibility and performance audits, web app testing with Playwright, MCP server building, pull request creation, and a few data and infrastructure helpers. Each skill is a Markdown file that teaches an agent conventions and workflows, auto-discovered from .agents/skills/ directories.

This repository covers the Oz skills only; the related Warp common-skills collection is a separate repository. The skills.sh index lists 15 listings, all with a matching .agents/skills/<name>/SKILL.md in the current tree.

## Installation

The README documents a copy-and-paste install: take a skill folder from the repository's .agents/skills/ directory and place it in your project's .agents/skills/ directory, or in ~/.agents/skills/ to use it across all projects. Warp detects the new skill on the next interaction.

```bash
# Project-local install of one skill (example: docs-update)
cp -r .agents/skills/docs-update ./.agents/skills/

# Global install, available across all projects
cp -r .agents/skills/docs-update ~/.agents/skills/
```

Each skill is a folder containing a SKILL.md file with YAML frontmatter and Markdown content. Skills are auto-discovered from .agents/skills/ directories when relevant to the current task; there is no CLI installer or plugin marketplace command in the README.

## What It Provides

skills.sh publishes per-skill install counts for all 15 indexed listings. The 10 most-installed skills are listed below; the remaining 5 are summarized under the table.

| Skill | Installs | Use For |
|---|---|---|
| seo-aeo-audit | 631 | SEO and AI visibility: meta tags, structured data, ranking, and AI citations |
| github-bug-report-triage | 382 | triage GitHub bug reports for actionability and missing detail |
| scheduler | 296 | schedule on-device reminders and local actions only, never cloud agents |
| web-accessibility-audit | 211 | WCAG accessibility audits with remediation guidance |
| docs-update | 207 | update user-facing documentation when code changes |
| ci-fix | 207 | diagnose and fix GitHub Actions CI failures, push fix branches |
| web-performance-audit | 202 | audit page load, Lighthouse scores, and site speed via Chrome DevTools MCP |
| webapp-testing | 192 | test local web apps with Playwright: frontend checks, screenshots, logs |
| mcp-builder | 186 | build MCP servers in Python (FastMCP) or Node/TypeScript (MCP SDK) |
| create-pull-request | 177 | create GitHub pull requests following project conventions via gh CLI |

The remaining 5 indexed listings range from 124 to 143 installs.

## Why This Matters for Hermes Agents

These skills encode the repetitive, convention-heavy work a coding agent does all day: triaging bug reports, deduplicating issues, fixing red CI, updating docs after a code change, and opening clean pull requests. For a builder running Hermes agents on their own repos, that means an agent can follow a known-good workflow instead of improvising one per task, and the SEO, accessibility, and performance audit skills give it concrete checklists and scripts rather than vague advice. The mcp-builder skill is the standout for agent work, teaching well-designed MCP servers in Python or TypeScript that let an LLM reach external services through real tools. The collection is small, MIT-licensed, and every listing has a matching folder in the tree, which makes it fast to review. The main caveat is the scheduler skill's explicit boundary: it handles on-device reminders and local actions only and is not for scheduling cloud agents or background agentic jobs.

## Usage

| You say | What happens |
|---|---|
| Audit this page for SEO and AI visibility | Uses seo-aeo-audit to check meta tags, structured data, and citations |
| Why is CI failing | Uses ci-fix to inspect workflow runs and push a minimal fix branch |
| Update the docs for this change | Uses docs-update to review commits and update user-facing docs |
| Open a pull request | Uses create-pull-request to handle commits, branches, and the gh CLI |
| Check this site for accessibility issues | Uses web-accessibility-audit against WCAG criteria |
| Build an MCP server for this API | Uses mcp-builder with FastMCP (Python) or the MCP SDK (Node) |
| Test my local web app | Uses webapp-testing with Playwright for frontend checks and screenshots |

## Verification

Confirm the README and a representative skill body resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/warpdotdev/oz-skills/main/README.md | head -40
curl -sL https://raw.githubusercontent.com/warpdotdev/oz-skills/main/.agents/skills/seo-aeo-audit/SKILL.md | head -40
```

Both URLs return 200. After installing, review each .agents/skills/<name>/SKILL.md before relying on it, and re-check the security pages on skills.sh for the Warnings noted below.

## Security

skills.sh verdicts for sampled skills (verified Nov 25, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| seo-aeo-audit | Pass | Pass | Warn |
| github-bug-report-triage | Pass | Pass | Warn |
| scheduler | Warn | Pass | Pass |
| web-accessibility-audit | Pass | Pass | Pass |
| docs-update | Pass | Pass | Pass |
| ci-fix | Pass | Pass | Warn |
| web-performance-audit | Pass | Pass | Warn |
| webapp-testing | Pass | Warn | Warn |
| mcp-builder | Pass | Pass | Warn |
| create-pull-request | Pass | Pass | Pass |
| analysis-artifacts | Pass | Pass | Pass |
| github-issue-dedupe | Pass | Pass | Warn |
| slack-qa-investigate | Pass | Pass | Warn |
| terraform-style-check | Pass | Pass | Pass |
| dbt-model-index | Pass | Pass | Pass |

All 15 listings were sampled; nine carry a Warning (webapp-testing carries two) and six pass all three checks, with no Fails.

## Limitations

- Snapshot data, verified Nov 25, 2026: 3,381 combined installs across 15 indexed listings; 823 GitHub stars; MIT license; last pushed Aug 15, 2026. Counts drift over time.
- Nine of 15 skills carry a skills.sh Warning (mostly Snyk); review the specific security pages before production use.
- This repository covers the Oz skills only; the related Warp common-skills collection is a separate repository.
- There is no CLI installer or plugin marketplace command; the documented path is manual copy into .agents/skills/ directories.
- The scheduler skill is explicitly scoped to on-device reminders and local actions, not cloud or background agent scheduling.

## Related

[Warp Common Skills - Spec-Driven Development Workflow Setup](/hermes/skills/catalog/warpdotdev-common-skills-setup) | [Zebbern Claude Code Guide - Usage and Pentest Skills Setup](/hermes/skills/catalog/zebbern-claude-code-guide-setup) | [Gohypergiant Agent Skills - Engineering Collection](/hermes/skills/catalog/agent-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install skills globally (~/.agents/skills/) when you want them across all projects, or project-locally (.agents/skills/) to keep a repo self-contained.
- Use mcp-builder for any task that needs an agent to reach an external API; it covers Python (FastMCP) and Node (MCP SDK) patterns.
- Run the seo-aeo-audit and web-accessibility-audit scripts (lighthouse.sh, run-eslint.sh) before shipping a frontend change.
- Respect the scheduler boundary: it is for local reminders, not for scheduling cloud agents or Oz-managed workflows.
- Keep the Warp common-skills collection in mind as a companion for spec-driven development workflows.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
