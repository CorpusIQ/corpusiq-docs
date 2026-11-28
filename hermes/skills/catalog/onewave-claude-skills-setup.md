---
title: "OneWave Claude Skills - Business and Agent Skills Setup"
description: "onewave-ai/claude-skills: 52.0K combined installs. A 200+ skill library spanning sales, marketing, design, engineering and AI agent architecture."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/onewave-claude-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-27"
tags: ["hermes skill", "agent skill", "skill setup", "claude skills", "sales", "marketing", "design"]
---

# OneWave Claude Skills - Setup Guide

**Source:** [onewave-ai/claude-skills](https://www.skills.sh/onewave-ai/claude-skills) via skills.sh - 52.0K combined installs across 96 indexed listings; first documented 2026-11-27 (evening sweep)

**GitHub:** [OneWave-AI/claude-skills](https://github.com/OneWave-AI/claude-skills) - 449 stars, MIT, branch main, last pushed 2026-10-20; each skill is a single-file folder at the repo root (`landing-page-copywriter/SKILL.md`) with no build step, plus three Claude plugins under `plugins/` (agent-army, scout-pro, scout).

**Category:** Sales, marketing, design, engineering and AI agent architecture as single-file Claude skills

**Quality Tier:** 🟡 Yellow - MIT with 449 stars; Snyk warns on two sampled listings (knowledge-base-builder and color-palette-extractor) and no sampled listing fails.

OneWave Claude Skills is a large single-file skill library from OneWave AI, a Florida-based boutique consulting firm focused on Claude and the Anthropic ecosystem. The README groups the library into three pillars it calls business (sales, marketing, consulting, ops), everyday life (personal finance, travel, fitness, job hunting) and coding (engineering, design, AI agent architecture), so one clone spans an entire business workflow rather than one discipline.

The README advertises 200+ skills and the body counts 230, while skills.sh indexes 96 listings totaling 52,020 combined installs, so the index understates the advertised library. Every skill ships as a self-contained SKILL.md with no dependencies and no build step, and the files follow the Agent Skills open standard, so the same clone runs in Claude Code, Codex, Gemini CLI, Cursor and 30+ other tools.

## Installation

The README offers two install paths: install a single skill by name, or clone the whole library into a skills directory. Each skill is a self-contained SKILL.md, so there is no build step:

```text
claude skill install OneWave-AI/claude-skills/<skill-name>
```

```bash
# Claude Code: clone the full library
git clone https://github.com/OneWave-AI/claude-skills.git ~/.claude/skills

# OpenAI Codex CLI (same files, unchanged)
git clone https://github.com/OneWave-AI/claude-skills.git ~/.codex/skills
```

Because the files follow the Agent Skills open standard, the same clone works in Gemini CLI, Cursor and 30+ other tools; point each tool's skills directory at the clone and it will discover the SKILL.md files. The bundled `plugins/` directory (agent-army, scout-pro, scout) is the exception: those ship as Claude Code plugins with their own manifest, so they are installed through the plugin path rather than as bare skills.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| landing-page-copywriter | 6,703 | Conversion-focused landing page copy (headlines, subheads, value props, social proof, FAQs, CTAs) using PAS, AIDA or StoryBrand. |
| code-review-pro | 2,635 | Deep review of files, diffs or branches for OWASP Top 10:2025 security issues, correctness, performance and maintainability, ranked by severity. |
| screenshot-to-code | 1,637 | Turns a screenshot, mockup or Figma export into React + Tailwind CSS v4 code (or Next.js, Vue, HTML/CSS), then renders and compares to close visual gaps. |
| csv-excel-merger | 1,195 | Merges, joins and deduplicates CSV, TSV and Excel files with pandas, mapping mismatched columns to one schema and tracking row provenance. |
| technical-writer | 1,090 | Writes and restructures technical docs (READMEs, tutorials, runbooks, SOPs) grounded in the actual code, with commands verified where possible. |
| sports-betting-analyzer | 881 | Analyzes spreads, over/unders and prop bets with historical trends and situational stats; entertainment and education only. |
| css-animation-creator | 871 | Professional CSS animations, transitions and micro-interactions: hover states, loading, page transitions and scroll animations. |
| social-media-content-repurposer | 775 | Indexed listing with no counterpart in the current repo tree; the README documents social-repurposer for adapting content across platforms. |
| workout-program-designer | 755 | Custom training plans by goal (strength, cardio, flexibility) with progressive overload, rest-day and deload planning. |
| job-application-optimizer | 755 | Tailors resumes to job postings, generates customized cover letters and prepares role-specific interview questions. |
| knowledge-base-builder | 700 | FAQ identification from support tickets, step-by-step tutorials, screenshot and video script guidance, and self-service deflection tracking. |
| color-palette-extractor | 691 | Extracts color palettes from images, websites or designs into HEX, RGB, HSL, Tailwind and CSS variables. |
| stock-photo-finder | 652 | Searches multiple free stock photo sites at once, filtered by license type, orientation and color scheme. |
| font-pairing-suggester | 631 | Recommends font combinations for different use cases, with Google Fonts alternatives to premium fonts and hierarchy examples. |
| presentation-design-enhancer | 620 | Turns text-heavy slides into visual storytelling with layout improvements, icon usage and data visualization. |
| itinerary-optimizer | 613 | Routes multi-stop trips efficiently with transportation, reservations timeline and buffer time for spontaneity. |
| quiz-maker | 574 | Creates multiple choice, true/false, fill-in-blank and matching quizzes with auto-generated distractors and instant grading. |
| cold-email-sequence-generator | 535 | Generates personalized 7-14 email cold sequences with A/B subject lines, follow-up timing and social proof. |
| linkedin-sales-navigator-alt | 526 | Builds targeted prospect lists from LinkedIn profiles, identifying decision-makers and tracking job changes for warm outreach. |
| portfolio-analyzer | 503 | Reviews investment portfolios for risk, diversification and fees, with allocation, tax-loss harvesting and rebalancing guidance. |

The remaining 76 indexed listings range from 334 to 490 installs.

## Why This Matters for Hermes Agents

OneWave Claude Skills is a model of the single-file skill pattern at scale: hundreds of small SKILL.md files, each self-contained with no dependencies and no build step, which makes the suite trivial to install into any runtime that reads the Agent Skills open standard. A Hermes-style builder can clone once and point Claude Code, Codex, Gemini CLI or Cursor at the same directory.

The breadth is the point. The library spans sales, marketing, design, engineering and AI agent architecture under one roof, so a single clone covers an entire business workflow instead of one discipline; the sales and revenue section alone runs from deal-closer-playbook through renewal-predictor to quota-setting-calculator. For a builder wiring a router, that is a full revenue operation expressed as skills.

The README draws a clean line between single-file skills and companion artifacts: anything with a manifest, a team or a build step lives in the separate Open Agent Stack repo, so a skill stays disposable and a plugin owns the heavier machinery. That is a boundary worth copying when deciding whether a capability belongs in a skill file or a plugin.

The trust boundary is also explicit. Each description is written to drive auto-selection, and the scripted "Work Tools" group (bookkeeping-close, spreadsheet-model-auditor, bi-measure-builder and others) ships Python scripts and reference data precisely because those are jobs a model gets wrong on its own. For a builder, that is a reminder to ground an agent in scripts and fixtures, not just instructions.

## Usage

| You say | What happens |
|---|---|
| "Write the landing page copy for my pricing page" | Loads landing-page-copywriter to write headlines, value props, social proof and CTA text using PAS, AIDA or StoryBrand. |
| "Review this diff for security issues before we ship" | Loads code-review-pro to return severity-ranked findings mapped to OWASP Top 10:2025. |
| "Turn this mockup into a working React page" | Loads screenshot-to-code to build React + Tailwind CSS v4, render it and compare against the image. |
| "Merge these three CSVs and dedupe the leads" | Loads csv-excel-merger to join, normalize and dedupe the files, tracking which row came from where. |
| "Write a runbook for our on-call process" | Loads technical-writer to write docs grounded in the actual code with verified commands. |
| "Build a cold email sequence for this launch" | Loads cold-email-sequence-generator to draft a 7-14 email sequence with A/B subject lines and follow-up timing. |
| "Extract the brand colors from our site" | Loads color-palette-extractor to pull the palette into HEX, RGB, HSL, Tailwind and CSS variables. |

## Verification

The raw path below returned 200 on branch main on 2026-11-27:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/OneWave-AI/claude-skills/main/landing-page-copywriter/SKILL.md
```

After a clone, confirm the single-file layout at the repo root and read one skill's frontmatter before trusting it:

```bash
git clone --depth 1 https://github.com/OneWave-AI/claude-skills.git /tmp/onewave-skills
ls /tmp/onewave-skills/ | head -20
head -6 /tmp/onewave-skills/landing-page-copywriter/SKILL.md
```

The listing should show skill folders at the repo root plus `plugins/`, and `head` should print the frontmatter of landing-page-copywriter. The index names 96 listings, so do not expect the tree to hold every indexed name; social-media-content-repurposer carries installs but has no counterpart directory in the current repo.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-27) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| landing-page-copywriter | Pass | Pass | Pass |
| code-review-pro | Pass | Pass | Pass |
| screenshot-to-code | Pass | Pass | Pass |
| csv-excel-merger | Pass | Pass | Pass |
| technical-writer | Pass | Pass | Pass |
| sports-betting-analyzer | Pass | Pass | Pass |
| css-animation-creator | Pass | Pass | Pass |
| social-media-content-repurposer | Pass | Pass | Pass |
| workout-program-designer | Pass | Pass | Pass |
| job-application-optimizer | Pass | Pass | Pass |
| knowledge-base-builder | Pass | Pass | Warn |
| color-palette-extractor | Pass | Pass | Warn |
| stock-photo-finder | Pass | Pass | Pass |
| font-pairing-suggester | Pass | Pass | Pass |
| presentation-design-enhancer | Pass | Pass | Pass |
| itinerary-optimizer | Pass | Pass | Pass |
| quiz-maker | Pass | Pass | Pass |
| cold-email-sequence-generator | Pass | Pass | Pass |
| linkedin-sales-navigator-alt | Pass | Pass | Pass |
| portfolio-analyzer | Pass | Pass | Pass |

This guide is Yellow because Snyk warns on two sampled listings (knowledge-base-builder and color-palette-extractor) while no sampled listing fails. The Gen Agent Trust Hub and Socket pass all 20 sampled listings. Only 20 of the 96 indexed listings were sampled, so treat the other 76 as unverified before installing into a production profile.

## Limitations

- Snapshot data, verified 2026-11-27: 52,020 combined installs across 96 indexed listings; 449 GitHub stars; MIT; last pushed 2026-10-20. Counts drift over time.
- The README advertises 200+ skills and the body counts 230, but skills.sh indexes 96 listings, so the index understates the advertised library.
- The install index outruns the tree: social-media-content-repurposer (775 installs) has no counterpart directory in the current repo, which ships social-repurposer and social-selling-content-generator instead.
- Only 20 of the 96 indexed listings were sampled for security verdicts in this sweep; the remaining 76 have no published skills.sh verdicts here.
- Skills are single SKILL.md files with no dependencies, but the "Work Tools" group ships Python scripts and reference data, so review those files before running them.
- Branch main.

## Related

- [AI Marketing Skills - 24-Skill Operator Toolkit](/hermes/skills/catalog/ai-marketing-claude-code-skills-setup)
- [Claude Marketing - Full Marketing Department Skills Setup](/hermes/skills/catalog/claude-marketing-setup)
- [Digital Marketing Pro - AI Marketing OS Setup](/hermes/skills/catalog/digital-marketing-pro-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the whole library once and let each runtime auto-select from descriptions; the description field is what drives skill selection, so keep it specific.
- Verify against the tree, not the index: skills ship as single-file folders at the repo root, and at least one indexed name has no counterpart on disk.
- Separate single-file skills from build-step artifacts; the README routes anything with a manifest, a team or a build step to the separate Open Agent Stack repo.
- For the scripted "Work Tools" skills (bookkeeping-close, spreadsheet-model-auditor, bi-measure-builder), review the bundled Python and fixtures before trusting the output.
- Re-check the two Snyk Warn listings (knowledge-base-builder, color-palette-extractor) on skills.sh before production use.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
