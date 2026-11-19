---
title: "Cofoundy Brand Skills - Naming and Brand Identity Setup"
description: "cofoundy/brand-skills: 7.2K combined installs across 17 listings; naming, identity, voice and brand-book skills for building a brand in an agent."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/cofoundy-brand-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-18"
tags: ["hermes skill", "agent skill", "skill setup", "branding", "naming", "brand identity"]
---

# Cofoundy Brand Skills - Setup Guide

**Source:** [cofoundy/brand-skills](https://www.skills.sh/cofoundy/brand-skills) via skills.sh - 7.2K combined installs across 17 indexed listings; first seen Nov 18, 2026 (Nov 18, 2026 evening sweep)
**GitHub:** 80 stars, NOASSERTION licence (GitHub metadata; the repo's LICENSE file and README badge read MIT), `main` branch, last pushed 2026-11-12. Skills live as `skills/<name>/SKILL.md`, one directory per skill.
**Category:** Branding, naming and brand identity
**Quality Tier:** 🟠 Orange - 3 Warn cells among the 12 sampled skills (naming, brand-audit, competitor-branding); GitHub reports NOASSERTION rather than a standard licence.

Cofoundy Brand Skills turns an idea into a real brand (name, identity, voice and a brand book) without leaving the agent. It ships 16 open-source skills for founders, indie hackers and agencies building AI-native products, working in Claude Code, Cursor, Windsurf and 70+ agents. Unlike chat-only brand tools, every skill reads and writes a versioned brand package (brand.yaml plus folders) and a registry, so the brand is a queryable artifact rather than a lost conversation.

The pipeline runs from brand-context and naming through strategy, positioning, voice, messaging and the brand-guidelines book, with brand-mod carrying a finished brand into Claude Code as a branded spinner. The naming engine and brand-genesis skills are adapted from two MIT projects (glacierphonk/naming and arnabbagxd/Brand-building-skills), credited in the repo's NOTICE file.

## Installation

Install every skill with the open Agent Skills CLI, which works across Claude Code, Cursor, Codex, OpenCode and more:

```bash
npx skills add cofoundy/brand-skills           # all skills
npx skills add cofoundy/brand-skills -s naming # one skill
npx skills add cofoundy/brand-skills -g        # global (user dir) install
```

As a Claude Code plugin:

```bash
/plugin marketplace add cofoundy/brand-skills
/plugin install brand-skills@brand-skills
```

Or from a local path with `npx skills add ./path/to/brand-skills`. In Claude Code the agent only sees one skill, `brand`, and routes to the other 16 as brand work comes up.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| naming | 527 | Name products, SaaS and brands via a metaphor-driven process, with prior-art and availability checks. |
| brand-guidelines | 485 | Create the brand book: logo usage, color, typography, voice, messaging and application rules. |
| brand-identity | 484 | Create a visual identity brief: logo direction, color palette, typography and imagery style. |
| brand-context | 474 | Capture and store core brand context (identity, audience, positioning, values, voice); every other skill reads it first. |
| brand-voice | 461 | Define verbal identity: tone, voice, vocabulary, writing style and messaging rules. |
| brand-init | 458 | Scaffold a versioned brand package (brand.yaml plus folders) and register it in a brand portfolio. |
| brand-messaging | 456 | Build the messaging hierarchy: taglines, value propositions, key messages and proof points. |
| brand-strategy | 455 | Run the full brand strategy workflow as a senior strategist, from questionnaire to a polished report. |
| brand-positioning | 454 | Define market positioning: where the brand sits relative to competitors and what it owns. |
| brand-audit | 449 | Assess brand health and consistency across identity, messaging, voice, positioning and market perception. |
| competitor-branding | 447 | Analyze how competitors present their brand to find gaps and differentiation opportunities. |
| brand-architecture | 446 | Define how brands, sub-brands and product lines relate under one organization. |
| target-audience | 446 | Define the ICP, personas, psychographics and audience language. |
| brand-story | 445 | Write the origin story and founder narrative in long, short and one-liner forms. |
| rebranding | 438 | Audit, reposition and relaunch an existing brand. |
| brand-mod | 157 | Turn a finished brand into a Claude Code mod with a branded spinner, previewed in HTML first. |

The remaining 1 indexed listing is brand (109 installs), the entry-point router skill your agent sees; it routes each request to the other skills.

## Why This Matters for Hermes Agents

For an agent that builds brands, the failure mode is a logo with a tagline glued on: a name, a voice and a visual brief that were each generated in isolation and contradict each other. Brand Skills forces coherence by making every skill read and write the same brand package, so naming, voice, messaging and identity all draw from one source of truth.

The persistence layer is the differentiator. A brand is a versioned, git-tracked brand.yaml package plus a registry that indexes every brand you manage, so an agent can answer "what brands do we have and what is the one-liner" in one query instead of re-deriving it from chat. That is a pattern worth copying into any multi-skill agent workflow, brand-related or not.

The skills are plain markdown with a self-contained router, so a Hermes agent can use them directly even though the one-line installers target the Claude plugin and npx skills.

## Usage

| You say | What happens |
|---|---|
| "Name my product" | naming runs the metaphor-driven engine, then checks prior art and availability before returning vetted finalists. |
| "Start a brand from scratch" | brand-init scaffolds the brand package and registers it in the portfolio. |
| "Give me the brand book" | brand-guidelines codifies logo usage, color, type, voice and application rules into one document. |
| "How should our brand sound?" | brand-voice defines tone, vocabulary and writing rules. |
| "Where do we sit versus competitors?" | brand-positioning and competitor-branding map the market and find the territory to own. |
| "Audit our current brand" | brand-audit scores brand health across six dimensions. |
| "Put our brand inside Claude Code" | brand-mod generates a branded spinner, previewed in HTML before it ships. |

## Verification

Probe one skill on the `main` branch before installing. It returns 200:

```bash
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/cofoundy/brand-skills/main/skills/naming/SKILL.md
```

Then install the full set and confirm the skills landed:

```bash
npx skills add cofoundy/brand-skills
cat .claude/skills/naming/SKILL.md
```

## Security

skills.sh verdicts for sampled skills (verified Nov 18, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| naming | Pass | Pass | Warn |
| brand-guidelines | Pass | Pass | Pass |
| brand-identity | Pass | Pass | Pass |
| brand-context | Pass | Pass | Pass |
| brand-voice | Pass | Pass | Pass |
| brand-init | Pass | Pass | Pass |
| brand-messaging | Pass | Pass | Pass |
| brand-strategy | Pass | Pass | Pass |
| brand-positioning | Pass | Pass | Pass |
| brand-audit | Pass | Pass | Warn |
| competitor-branding | Pass | Pass | Warn |
| brand-architecture | Pass | Pass | Pass |

The sample covers 12 of the 17 indexed listings. Three skills carry a Snyk Warn (naming, brand-audit, competitor-branding); the rest pass all three columns.

## Limitations

- Snapshot data, verified Nov 18, 2026: 7,191 combined installs across 17 indexed listings; 80 GitHub stars; NOASSERTION licence (the repo's LICENSE file and README badge read MIT); last pushed 2026-11-12. Counts drift over time.
- GitHub reports NOASSERTION rather than a standard licence even though the repo ships a LICENSE file and an MIT badge; treat the licence as MIT per the repo's own files but note the metadata gap.
- Scope is brand genesis (creating a brand); the suite does not do go-to-market, ads, channels or growth. brand-mod is the one application skill.
- The agent only sees the brand router by default, so the individual skills are reachable as slash commands rather than auto-loaded context.
- The naming engine and brand-genesis skills are adapted from two upstream MIT projects, so review the NOTICE file for attribution before redistributing.

## Related

- [Brand Building Skills - Brand Strategy Suite Setup](/hermes/skills/catalog/arnabbagxd-brand-building-skills-setup)
- [Dembrandt Skills - Design System Judgment for Agents](/hermes/skills/catalog/dembrandt-skills-setup)
- [Bergside Design Skills - Design Systems Setup](/hermes/skills/catalog/bergside-awesome-design-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Run brand-context first on any new brand project; every other skill reads its file before doing work.
- Install all 16 skills rather than a single one so the agent can pick the right skill on its own.
- Treat the brand registry as your source of truth and git-track it; it is a file, not agent memory.
- Use brand-mod last, once the brand is finished, so the spinner shows your real colors and words.
- Validate a name with the naming skill's `validar` command before committing to it (trademark, domains, handles).

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
