---
title: "Borghei Claude Skills - 385 Business Skill Library"
description: "borghei/claude-skills on skills.sh: 34.5K combined installs across 200 listings; 385 business skills from pricing to board and compliance work."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/borghei-claude-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-03"
tags: ["hermes skill", "agent skill", "skill setup", "business operations", "compliance"]
---

# Borghei Claude Skills - Setup Guide

**Source:** [borghei/claude-skills](https://www.skills.sh/borghei/claude-skills) via skills.sh - 34.5K combined installs across 200 indexed listings; first documented November 3, 2026 (evening sweep)
**GitHub:** 1,043 stars, NOASSERTION licence (README says MIT plus Commons Clause), last pushed 2026-10-23, 386 SKILL.md directories
**Category:** Business operations for agents: pricing, churn, deal desk, partnerships, CRO and compliance audit skills
**Quality Tier:** 🟡 Yellow: pr-review-expert draws a Snyk Warn, and GitHub reports the licence as NOASSERTION rather than a recognised identifier

This is the largest business-operations pack in the catalog: 385 skills, 76 expert agents and 906 stdlib Python tools, organised into 21 domains. skills.sh indexes 200 of those skills, and the visible repo tree shows role-based directories such as business-growth, business-operations and c-level-advisor.

The design is consistent across the set. Each skill opens by asking the questions that change the answer, then runs its own Python tool on your numbers. The README's worked example is board-deck-builder, which asks which kind of meeting it is and what the board needs to decide, then runs a metrics dashboard generator over a JSON input.

## Installation

The README documents four routes, and the plugin route is the shortest:

```bash
/plugin marketplace add borghei/Claude-Skills
```

```bash
/plugin install c-level-skills@claude-code-skills
```

For one skill at a time on Cursor, Codex, Gemini CLI, Copilot, Windsurf, Cline, Goose or Aider, the CLI needs Node 18 or later:

```bash
npx @borghei/claude-skills search "board"
```

```bash
npx @borghei/claude-skills add board-deck-builder
```

The Claude desktop app takes a different path: open Customize, then Browse plugins, then enter borghei/Claude-Skills. For Hermes, the practical option is to copy the skill directory you need, including its scripts/ folder, out of the domain directory in the clone.

## What It Provides

Twenty of the 200 indexed listings clear 260 installs.

| Skill | Installs | Use For |
|---|---|---|
| product-designer | 4,886 | Product design workflow; not in the visible tree sample |
| business-intelligence | 1,543 | BI reporting and metric review |
| brand-strategist | 779 | Brand positioning and messaging |
| data-analyst | 615 | Ad hoc analysis over supplied data |
| cfo-advisor | 455 | Finance and board metrics advisory |
| data-scientist | 443 | Modelling and experiment analysis |
| growth-marketer | 431 | Growth campaign planning |
| hr-business-partner | 395 | People and org advisory |
| solutions-architect | 370 | Pre-sales architecture scoping |
| senior-pm | 364 | Product management review pass |
| senior-frontend | 349 | Frontend implementation review |
| talent-acquisition | 345 | Hiring pipeline design |
| operations-manager | 322 | Ops process and capacity work |
| senior-fullstack | 315 | Full stack implementation review |
| senior-mobile | 312 | Mobile implementation review |
| marketing-analyst | 310 | Marketing measurement |
| senior-backend | 293 | Backend implementation review |
| sales-operations | 284 | Sales ops and deal process |
| agile-coach | 267 | Agile ceremony and team health |
| cmo-advisor | 260 | Marketing leadership advisory |

The remaining 180 indexed listings range from 63 to 258 installs.

## Why This Matters for Hermes Agents

Most agent skill libraries are engineering only. This one covers the work that surrounds engineering: pricing, churn, deal desk, partnerships, contracts, compliance audits and board reporting, which is often where an autonomous agent has nothing to work from.

The pattern worth copying is the question-first opening. Each skill spends its first section on the inputs that change the output, which stops a Hermes agent from generating a confident deck from half a data set.

The Python tooling is the second transferable piece. The skills are not just prose prompts; they ship scripts that parse a JSON input and print a structured table, so an agent gets a deterministic result instead of a plausible summary.

Compliance coverage is unusually broad for a general pack, with frameworks including ISO 27001, SOC 2, PCI DSS, NIS2, DORA and the EU AI Act represented as their own audit skills.

Two cautions for builders: the 386 directories include both skills and expert agents, so not every directory is a plain skill, and the Commons Clause in the licence restricts resale.

## Usage

| You say | What happens |
|---|---|
| "Build the metrics page for Thursday's board meeting" | board-deck-builder asks what the board must decide, then runs its dashboard generator on your numbers |
| "Should we change pricing on the team plan?" | pricing-strategy works through willingness to pay, packaging and the migration path |
| "Customers are churning in month three" | churn-prevention maps the leak and proposes interventions |
| "Review this contract before we sign" | contract-review flags the clauses and the negotiation points |
| "Prepare for our SOC 2 audit" | soc2-compliance-expert lists the controls and evidence needed |
| "Qualify this vendor" | vendor-due-diligence runs a structured assessment |
| "Write the release notes for this version" | changelog-generator and release-notes produce the changelog from changes |

## Verification

Confirm the CLI is reachable and can see the library:

```bash
npx @borghei/claude-skills search "board"
```

Then fetch one raw skill file to confirm the tree matches what skills.sh indexed. This URL is built from the business-growth/pricing-strategy/SKILL.md path in the repo tree, on branch main:

```bash
curl -fsSL https://raw.githubusercontent.com/borghei/claude-skills/main/business-growth/pricing-strategy/SKILL.md | head -30
```

A response with skill frontmatter plus the question-first opening confirms the content is live.

## Security

skills.sh verdicts for sampled skills (verified November 3, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| product-designer | Pass | Pass | Pass |
| playwright-pro | Pass | Pass | Pass |
| pr-review-expert | Pass | Pass | Warn |
| site-architecture | Pass | Pass | Pass |
| terraform-patterns | Pass | Pass | Pass |

## Limitations

- Snapshot data, verified November 3, 2026: 34,493 combined installs across 200 indexed listings; 1,043 GitHub stars; NOASSERTION licence; last pushed 2026-10-23. Counts drift over time.
- GitHub reports NOASSERTION because the licence is MIT plus a Commons Clause. Check the terms before shipping these skills inside a paid product.
- 386 SKILL.md directories exist against 200 indexed listings, so roughly half the library has no public install data.
- pr-review-expert carries a Snyk Warn; it is one of the skills that runs repository commands.
- Only the top listing, product-designer, has install counts in the thousands. Everything after business-intelligence is in the hundreds.
- The skill set spans 21 domains, so naming overlaps across domains are likely; confirm you are adding the directory you meant.

## Related

- [Anthropic Claude API Skills - Official Claude API](/hermes/skills/catalog/anthropics-claude-api-skills-setup)
- [AI Labs Claude Skills - 27 Skill Business Suite Setup](/hermes/skills/catalog/ailabs-claude-skills-setup)
- [Agent Toolkit - 44 Skills for Coding Agents Setup](/hermes/skills/catalog/agent-toolkit-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Use the search command before adding anything. With 386 directories, guessing the name wastes more time than it saves.
- Copy the scripts/ folder with the skill. The value in these skills is the tool that runs on your numbers, not the prompt alone.
- Answer the opening questions with real figures; the skills are written to stop and ask when the input is thin.
- Keep compliance skills on read-only inputs until you have read what evidence they expect to collect.
- Pin to a tag rather than main if you depend on a specific skill, since the library is large and changes often.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
