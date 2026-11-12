---
title: "Glebis Claude Skills - Solopreneur Skill Library"
description: "glebis/claude-skills: 14.7K combined installs across 96 listings for research, publishing, image generation and Claude Code operations"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/glebis-claude-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-12"
tags: ["hermes skill", "agent skill", "skill setup", "productivity", "research", "claude code"]
---

# Glebis Claude Skills - Setup Guide

**Source:** [glebis/claude-skills](https://www.skills.sh/glebis/claude-skills) via skills.sh - 14.7K combined installs across 96 indexed listings; first seen Jan 24, 2026 (Nov 12, 2026 sweep)
**GitHub:** 413 stars, MIT license, `main` branch, last pushed 2026-11-10, 131 `SKILL.md` files with one folder per skill at the repository root
**Category:** Solopreneur operations: research, meeting pipelines, publishing, image and audio generation, personal analytics, Claude Code operations
**Quality Tier:** 🟡 Established - a large, actively maintained one-author library with a plugin marketplace and a clean MIT license, held back by per-skill credential setup and scanner Warns on the network-bound skills.

Gleb Kalinin publishes a working library in public: roughly a hundred skills he uses to run a one-person practice, written as self-contained folders rather than a product with a unified interface. The scope is what a solo operator actually does across a week. Meetings get recorded and analyzed, research gets run through FireCrawl or the OpenAI Deep Research API, decks and PDFs get produced, images and voice get generated, and personal health and calendar data get queried.

The repository root carries a `BUNDLES.md` that groups the folders into working sets, which matters because the skill list is long enough that picking from it cold is the hard part. Recent additions show the direction of travel: `bridgework` runs a consent-gated audit of your stack, `luma-event` builds an event page and a Zoom meeting from one prompt, `research-to-integration` turns a research pass into a bounded experiment, `pii-pdf` redacts personal data in PDFs locally, and `app-map` maps an application's screens and tests.

Each skill is a folder with its own `SKILL.md` and, where needed, scripts and assets. Installation is per skill, and so is configuration: the API keys and Python or Node dependencies live in the individual skill documentation rather than in one installer.

The most-installed skills in the index are not the most ambitious ones. Image search, PDF generation, Apple Health queries, FireCrawl research, OpenAI Deep Research and HTML presentations carry the numbers, which is a fair signal about how agents get used in practice: repeatable production work first, judgment work second.

## Installation

The README documents three routes. The plugin marketplace is the recommended one:

```bash
claude plugin marketplace add glebis/claude-skills
claude plugin install tdd@glebis-skills
```

The skills CLI installs a single skill by name:

```bash
npx skills add glebis/claude-skills --skill tdd
```

Manual installation copies the folder:

```bash
git clone https://github.com/glebis/claude-skills.git
cp -r claude-skills/<skill-name> ~/.claude/skills/
```

Per-skill setup is documented inside each `SKILL.md`: API keys, Python and Node dependencies, and any templates the skill expects. `BUNDLES.md` lists the curated groupings if you would rather install a working set than a single folder. Nothing in the repository installs itself, so an agent that is asked to "set up the whole library" will copy folders and skip the credentials.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| google-image-search | 649 | Google Custom Search image lookup with LLM-powered selection for articles and pages. |
| pdf-generation | 490 | Markdown to PDF through Pandoc with the Eisvogel template and EB Garamond typesetting. |
| health-data | 398 | Apple Health SQLite queries for vitals, activity, sleep and workouts, with Markdown, JSON and FHIR output. |
| firecrawl-research | 383 | FireCrawl research runs that enrich notes with scraped web sources. |
| deep-research | 330 | OpenAI Deep Research API runs with prompt enhancement and report output. |
| presentation-generator | 325 | Interactive HTML presentations in neobrutalism styling with Agency brand colours. |
| decision-toolkit | 323 | Structured decision tools: step-by-step guides, bias checkers, scenario explorers and decision dashboards. |
| elevenlabs-tts | 310 | Text to speech through the ElevenLabs API, with voice selection and audio file output. |
| telegram | 284 | Reading, searching, downloading, sending and editing Telegram messages. |
| brand-agency | 274 | Agency brand colours and typography applied to decks, SVG graphics, documents and interfaces. |
| doctorg | 264 | Health research over tiered trusted sources with GRADE-inspired evidence ratings, joined to Apple Health data. |
| tdd | 260 | Test-driven development with the RED-GREEN-REFACTOR loop enforced. |
| transcript-analyzer | 257 | Meeting transcript analysis for decisions, action items, opinions, questions and terminology. |
| gmail | 257 | Gmail search, fetch and attachment download. |
| youtube-transcript | 255 | YouTube transcript extraction with metadata, saved as Markdown into an Obsidian vault. |
| zoom | 251 | Zoom meeting creation and cloud recording access through the Zoom API. |

The remaining 80 indexed listings range from 31 to 248 installs.

Two notes on the numbers. The install index stops at 96 listings while the repository carries 131 `SKILL.md` files, so the family is larger than the table above suggests and the combined figure is a floor. And the per-skill counts are close together across the top twenty, which is what a library looks like when people install bundles rather than single skills.

## Why This Matters for Hermes Agents

An agent's competence is uneven in a predictable way: it writes and reasons well, and it falls apart on the boring operational edges. Producing a PDF that a client will open, getting a transcript out of a meeting, generating a voice file, pulling a transcript off YouTube, creating a Zoom link, checking what an Apple Health export actually contains. Each of those is a small integration problem with a specific tool and a specific failure mode. This library is a collection of those solutions already written down.

The second value is judgment scaffolding. `decision-toolkit` produces bias checks and scenario explorers rather than a single recommendation. `automation-advisor`, one of the July additions, runs a quantified return and break-even analysis before an automation gets built. `pre-session-portrait` builds a seven-lens client portrait before a paid consulting hour. Those are the parts a general-purpose model will not volunteer, because volunteering them looks like slowing the user down.

The third value is that everything is a folder. There is no runtime, no service to keep alive, and no schema to migrate. You can vendor one skill into a project, read it end to end, and delete it later. For an agent stack that has to stay auditable, that property is worth more than a richer framework would be.

## Usage

| You say | What happens |
|---|---|
| "Turn this report into a PDF I can send" | Runs the Pandoc pipeline with the Eisvogel template and returns a typeset PDF. |
| "Find three images for this post and pick the best one" | Searches through Google Custom Search, evaluates the candidates and downloads the chosen file. |
| "Summarize the decisions from this meeting transcript" | Extracts decisions, action items, opinions and open questions into a structured summary. |
| "Research this market and give me a sourced brief" | Uses the FireCrawl or Deep Research skill, keeps the sources with the claims and writes a report. |
| "Make me a deck on this" | Produces an interactive HTML presentation in the Agency brand style. |
| "What did my sleep look like last month?" | Queries the Apple Health database and returns the trend with a summary. |
| "Run this feature as a TDD change" | Enforces the RED-GREEN-REFACTOR sequence instead of writing the implementation first. |

## Verification

Confirm the repository layout before copying anything, since skills sit at the root rather than under a `skills/` directory. This returns 200:

```bash
curl -fsSL https://raw.githubusercontent.com/glebis/claude-skills/main/tdd/SKILL.md | head -6
```

Check the second skill you plan to install the same way, because the folders are independent and one can move without the others:

```bash
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/glebis/claude-skills/main/pdf-generation/SKILL.md
```

After installation, list the agent skills directory and confirm one folder per skill, each containing a `SKILL.md`. Review the skill body before installing: these are personal workflows, and the ones that touch credentials describe exactly which keys they expect.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-12) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| google-image-search | Pass | Warn | Warn |
| pdf-generation | Pass | Pass | Pass |
| health-data | Pass | Pass | Pass |
| firecrawl-research | Pass | Pass | Warn |

The Warns land on the two skills that leave the machine and spend money: image search calls a paid Google API, and FireCrawl research calls a scraping service with a key. Both are flagged for what they do rather than for anything hidden, and both need a scoped key with a spend limit.

The more sensitive skills are the ones that read personal data. `health-data` queries an Apple Health database, `gmail` searches a mailbox, `telegram` reads and sends messages, `zoom` reaches recordings. The scanners pass them because the code is straightforward, but the practical control is the account scope and the local machine, not the scanner verdict.

## Limitations

- Snapshot data, verified 2026-11-12: 14,683 combined installs across 96 indexed listings; 413 GitHub stars; MIT license; last pushed 2026-11-10. Counts drift over time.
- 96 is the cap of the skills.sh search API. The repository carries 131 `SKILL.md` files, so the indexed family and the combined install total both undercount what is installable.
- Every skill needs its own setup. API keys, Python and Node packages and template files are documented per `SKILL.md`, and a bulk copy installs the folders without configuring any of them.
- No version pinning. `npx skills add` pulls the current tree, so a library that is pushed to several times a week changes under a fixed install.
- Several skills read personal data or spend money per call: Apple Health, Gmail, Telegram, Zoom, Google image search, FireCrawl, ElevenLabs. Treat the keys as production credentials.
- The library is one author's working practice, not a supported product. There is no changelog discipline across the 131 folders and no compatibility statement beyond the Claude Code plugin manifest.

## Related

- [Baoyu Skills - Content Generation & Publishing Suite Setup](/hermes/skills/catalog/baoyu-skills-setup)
- [memoria-vault - Multi-Agent Research OS for Obsidian Setup](/hermes/skills/catalog/memoria-vault-setup)
- [Eachlabs Skills - Creative Generation Setup](/hermes/skills/catalog/eachlabs-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start from `BUNDLES.md`, not the full list. Installing a working set gets you a coherent workflow, while installing single skills in alphabetical order gets you folders you never call.
- Read the `SKILL.md` before installation for anything that touches credentials. Each one states the keys it needs, and installing first means discovering the dependency as a failure later.
- Run `pdf-generation` and `presentation-generator` with the brand skill installed alongside them if the output goes to a client. The visual style is defined there, not in the generators.
- Keep personal-data skills on a local machine and scoped accounts. `health-data`, `gmail` and `zoom` are written for direct API access, so an agent with a work account can read more than the task needs.
- Ask the agent to name the skill it used. With 131 folders in a flat layout, a wrong pick is hard to spot in the output and obvious in the trace.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
