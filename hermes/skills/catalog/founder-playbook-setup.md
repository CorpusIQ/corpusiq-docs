---
title: "Founder Playbook Skills - Business Book Frameworks"
description: "getagentseal/founder-playbook: 12.6K combined installs across 16 listings of business books distilled into agent skills for offers, sales and growth."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/founder-playbook-setup/"
robots: "index,follow"
last_updated: "2026-11-17"
tags: ["hermes skill", "agent skill", "skill setup", "business", "sales", "growth"]
---

# Founder Playbook Skills - Setup Guide

**Source:** [getagentseal/founder-playbook](https://www.skills.sh/getagentseal/founder-playbook) via skills.sh - 12.6K combined installs across 16 indexed listings; first seen Nov 17, 2026 (this sweep)
**GitHub:** 801 stars, MIT license, `main` branch, last pushed 2026-10-06, 16 `SKILL.md` files in `skills/<name>/`
**Category:** Founder and business framework agent skills
**Quality Tier:** 🟢 Green - all 16 sampled skills pass Gen Agent Trust Hub, Socket and Snyk.

getagentseal/founder-playbook distils 15 proven business books into 16 AI-native skills. Each skill captures the frameworks, decision trees, case studies and templates from a single book, from The Mom Test and The Lean Startup to SPIN Selling and Influence, so an agent can apply the method without the 300 pages of stories.

The skills are built for Claude Code, which auto-triggers them from the question, but work with ChatGPT, Gemini, Cursor or any LLM as reference documents. diagnose is the entry point: it routes a vague startup problem to the right framework skill before you reach for a specific one.

## Installation

Install with the skills.sh CLI, or clone and symlink into the Claude skills directory:

```bash
npx skills add getagentseal/founder-playbook
```

For a manual install, clone the repo and symlink each skill directory:

```bash
git clone https://github.com/getagentseal/founder-playbook.git
for skill in founder-playbook/skills/*/SKILL.md; do
  dir=$(dirname "$skill")
  name=$(basename "$dir")
  ln -sfn "$(pwd)/$dir" ~/.claude/skills/$name
done
```

For ChatGPT, Gemini or another LLM, open the relevant `SKILL.md` and paste it into the conversation; the YAML frontmatter is just metadata. For Cursor, Windsurf or Cline, drop the repo into the project's rules or docs folder.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| 100m-offers | 919 | Design irresistible Grand Slam Offers with the value equation and pricing psychology. |
| 100m-leads | 895 | Build lead generation systems with the Core Four framework and Rule of 100. |
| spin-selling | 830 | Apply SPIN questioning to complex B2B sales cycles. |
| mom-test | 821 | Validate ideas through customer conversations without leading questions. |
| lean-startup | 795 | Iterate with build-measure-learn loops, MVPs and pivot decisions. |
| influence | 791 | Apply Cialdini's seven persuasion principles and Pre-Suasion. |
| storybrand | 790 | Apply the StoryBrand SB7 framework to brand messaging and copy. |
| obviously-awesome | 785 | Position B2B tech products with Dunford's 10-step method. |
| traction | 780 | Choose growth channels with the Bullseye Framework. |
| diagnose | 777 | Route a vague startup problem to the right framework skill. |
| monetizing-innovation | 776 | Design products around price with the 9 monetization rules. |
| made-to-stick | 776 | Make messages memorable with the SUCCESs framework. |
| four-steps | 773 | Apply Customer Development from discovery through company building. |
| blue-ocean-strategy | 771 | Create uncontested market space with Strategy Canvas and ERRC. |
| crossing-the-chasm | 760 | Move B2B tech products from early adopters to the mainstream. |
| money-models | 606 | Sequence offers so customer acquisition funds itself. |

No indexed listing falls below 500 installs; all 16 appear in the table above.

## Why This Matters for Hermes Agents

These skills turn business books into decision trees, scoring rubrics and fill-in templates an agent can actually apply, rather than summaries to skim. diagnose is the entry point: it routes a vague "what is wrong with my startup" question to the right framework before any specific skill is loaded.

The set covers the full founder journey, from customer discovery (mom-test, four-steps) and iteration (lean-startup) through positioning (obviously-awesome, storybrand), pricing (monetizing-innovation), offer design (100m-offers, money-models) and acquisition (traction, 100m-leads). Each skill also ships an honest scope section naming what the book got wrong or where it does not apply, so an agent surfaces the caveats instead of repeating dated advice.

Because the descriptions are short, an agent can keep all 16 loaded and auto-trigger the relevant one from a single natural-language question.

## Usage

| You say | What happens |
|---|---|
| "What's wrong with my startup?" | Loads diagnose, which routes to the right framework skill. |
| "I'm interviewing customers tomorrow" | Loads mom-test for unbiased interview questions. |
| "Should we pivot?" | Loads lean-startup for build-measure-learn and the pivot call. |
| "Which marketing channel should we use?" | Loads traction for Bullseye channel selection. |
| "How do I price this?" | Loads monetizing-innovation for willingness-to-pay and packaging. |
| "Our website doesn't convert" | Loads storybrand for SB7 messaging. |
| "Make an offer people cannot refuse" | Loads 100m-offers for Grand Slam Offer design. |

## Verification

Probe the skills on the `main` branch before installing. All return 200:

```bash
curl -fsSL https://raw.githubusercontent.com/getagentseal/founder-playbook/main/skills/100m-offers/SKILL.md | head -12
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/getagentseal/founder-playbook/main/skills/diagnose/SKILL.md
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/getagentseal/founder-playbook/main/skills/lean-startup/SKILL.md
```

Each skill lives at `skills/<name>/SKILL.md`, with supporting files (frameworks.md, cases.md, examples.md, integration.md) alongside it.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-17) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| 100m-offers | Pass | Pass | Pass |
| 100m-leads | Pass | Pass | Pass |
| spin-selling | Pass | Pass | Pass |
| mom-test | Pass | Pass | Pass |
| lean-startup | Pass | Pass | Pass |
| influence | Pass | Pass | Pass |
| storybrand | Pass | Pass | Pass |
| obviously-awesome | Pass | Pass | Pass |
| traction | Pass | Pass | Pass |
| diagnose | Pass | Pass | Pass |
| monetizing-innovation | Pass | Pass | Pass |
| made-to-stick | Pass | Pass | Pass |
| four-steps | Pass | Pass | Pass |
| blue-ocean-strategy | Pass | Pass | Pass |
| crossing-the-chasm | Pass | Pass | Pass |
| money-models | Pass | Pass | Pass |

The sample covers all 16 indexed listings, and every skill passes all three auditors.

## Limitations

- Snapshot data, verified 2026-11-17: 12,645 combined installs across 16 indexed listings; 801 GitHub stars; MIT; last pushed 2026-10-06. Counts drift over time.
- The repo has not been pushed since 2026-10-06, about six weeks before this snapshot, so the frameworks are stable but dated material is flagged inside the skills rather than refreshed.
- The skills are study aids and critical commentary, not replacements for the books; the README asks readers to buy the book when a skill helps.
- Several frameworks come from the 1990s and 2000s and carry notes where they do not apply to modern PLG and AI-native products.
- All 16 indexed listings map to a matching `skills/<name>/` directory, and the covers/ and assets/ files sit alongside the skills, so the skill-level verdicts do not cover the whole repository.

## Related

- [Book-to-Skill - Book to Agent Skill Converter Setup](/hermes/skills/catalog/book-to-skill-setup)
- [Wondelai Skills - Book Framework Business & Design Setup](/hermes/skills/catalog/wondelai-skills-setup)
- [A Smart Bear Skills - Positioning & PMF Suite Setup](/hermes/skills/catalog/asmartbear-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with diagnose when the problem is vague; it routes before you load a specific skill.
- Load the supporting files (frameworks.md, cases.md, examples.md) only when you need depth, not by default.
- Read the honest-scope section before applying a 1990s framework to a modern AI-native product.
- Pair 100m-offers with money-models so the offer sequence funds acquisition instead of converting once.
- For customer interviews, run mom-test before any feature work so the questions do not bias the answers.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
