---
title: "Daymade Claude Code Skills Setup Guide for Hermes Agents"
description: "daymade/claude-code-skills - 58.4K installs across 106 skills, 1.4K stars: a broad general-purpose agent skill suite - X reading, deep research, QA, prompt optimization, docs, slides, and troubleshooting."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/daymade-claude-code-skills-setup/"
robots: "index,follow"
last_updated: "2026-08-31"
tags: ["hermes skill", "agent skill", "skill setup", "research", "productivity", "qa", "docs", "x twitter"]
---

# Daymade Claude Code Skills - Setup Guide

**Source:** [daymade/claude-code-skills](https://skills.sh/daymade/claude-code-skills) (58.4K installs across 106 skills)
**GitHub:** [daymade/claude-code-skills](https://github.com/daymade/claude-code-skills) (1.4K stars)
**Skills:** 106 skills; top skills: `twitter-reader` (2.7K), `i18n-expert` (2.1K), `prompt-optimizer` (1.7K)
**Category:** Development / General-Purpose Productivity
**First Seen:** skills.sh Jan 20, 2026; catalogued in the Aug 31, 2026 sweep
**Quality Tier:** 🟡 Trusted - Gen Agent Trust Hub and Socket Pass, but Snyk carries a warning on the top skill (see Security Audit Status)

A 106-skill general-purpose suite covering the practical middle of agent work: content intake (`twitter-reader` for X posts and articles with media support, `youtube-downloader`, `asr-transcribe-to-text`, `capture-screen`), research and analysis (`deep-research`, `fact-checker`, `competitors-analysis`, `product-analysis`, `benchmark-due-diligence`), documents and media (`pdf-creator`, `docx-creator`, `ppt-creator`, `excel-automation`, `meeting-minutes-taker`, `slides-creator`), engineering workflow (`github-ops`, `github-contributor`, `terraform-skill`, `promptfoo-evaluation`, `qa-expert`, `skill-reviewer`), and systems troubleshooting (`cloudflare-troubleshooting`, `debugging-network-issues`, `tunnel-doctor`, `macos-cleaner`).

The `twitter-reader` skill is a worked example of the suite's style: it prefers the login-free fxtwitter mirror API for post text, documents that `tweet.text` (not `full_text`) carries long-form bodies, and notes that `replies` is a count rather than a thread - concrete, tool-verified guidance rather than vague instructions. Despite the repo name, the skills are standard SKILL.md packages that any agent with a skills loader can use.

---

## Installation

```bash
npx skills add daymade/claude-code-skills
```

Or per-skill:

```bash
npx skills add https://github.com/daymade/claude-code-skills --skill twitter-reader
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js** | Recent LTS for the `npx skills` installer |
| **Python 3** | Several skills (twitter-reader, scrapers, transcription) drive Python scripts |
| **Per-skill tools** | Individual skills assume their domain tools (terraform, cloudflare CLI, etc.) where applicable |

## Core Skills

| Skill | Installs | Use For |
|---|---|---|
| twitter-reader | 2.7K | Reading X posts and articles with media support via fxtwitter mirror API and fetch scripts |
| i18n-expert | 2.1K | Internationalization review and translation workflows |
| prompt-optimizer | 1.7K | Improving prompts for LLM calls |
| ppt-creator | 1.6K | Generating PowerPoint decks |
| qa-expert | 1.6K | Test planning and QA review |
| macos-cleaner | 1.4K | macOS disk and clutter cleanup |
| deep-research | 1.3K | Structured multi-source research |
| ui-designer | 1.2K | UI design guidance |
| fact-checker | 1.2K | Claim verification workflows |
| promptfoo-evaluation | 1.2K | LLM evaluation with promptfoo |

Plus `meeting-minutes-taker`, `mermaid-tools`, `excel-automation`, `skill-reviewer`, `github-ops`, `youtube-downloader`, `skills-search`, `capture-screen`, `docs-cleaner`, `pdf-creator`, `transcript-fixer`, `cloudflare-troubleshooting`, `cli-demo-generator`, `repomix-safe-mixer`, `financial-data-collector`, `doc-to-markdown`, `scrapling-skill`, and 80+ more.

## Security Audit Status (skills.sh, verified Aug 31, 2026)

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| twitter-reader | Pass | Pass | Warn |

Gen Agent Trust Hub and Socket Pass; Snyk carries a warning - the reason this suite ships 🟡 Trusted rather than 🟢 Production.

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **X monitoring** | `twitter-reader` documents login-free, key-free X post extraction - directly useful for CorpusIQ's social listening work |
| **Research sweeps** | `deep-research`, `fact-checker`, and `competitors-analysis` complement the skills.sh and MCP catalog sweeps |
| **Report production** | `pdf-creator`, `ppt-creator`, and `slides-creator` cover the document formats operators request |
| **Agent self-review** | `skill-reviewer` and `promptfoo-evaluation` support CorpusIQ's own skill and prompt quality work |

## Limitations / Verification

- Repo name says claude-code but the skills are standard SKILL.md packages; verify per-skill portability before relying on one in a Hermes workflow (most are tool-driven and agent-agnostic).
- 106 skills is heavy for a full install; use `--skill <name>` for targeted installs.
- Snyk warning is named in the tier above.

Verification after install:

```bash
npx skills add daymade/claude-code-skills --list    # 106 skills discovered
```

## Related

- [Skills Catalog](/docs/hermes/skills/catalog) - full quality-tiered directory
- [Skills Marketplace](/docs/hermes/skills/marketplace) - more discovery batches

---

*← [Skills Catalog](/docs/hermes/skills/catalog) | [Skills Marketplace](/docs/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
