---
title: "AI Marketing Skills - 24-Skill Operator Toolkit"
description: "BrianRWagner AI marketing skills: 10.4K combined installs across 24 listings for positioning, outreach, content and AI search visibility audits"
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/ai-marketing-claude-code-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-11"
tags: ["hermes skill", "agent skill", "skill setup", "marketing", "positioning", "cold outreach", "content"]
---

# AI Marketing Skills - Setup Guide

**Source:** [BrianRWagner/ai-marketing-claude-code-skills](https://www.skills.sh/BrianRWagner/ai-marketing-claude-code-skills) via skills.sh - 10.4K combined installs across 24 indexed listings; first seen Feb 15, 2026 (Nov 11, 2026 sweep)
**GitHub:** 455 stars, no LICENSE file in the repository (the README carries an MIT badge), `main` branch, last pushed 2026-03-19, 89 tracked files with 23 `SKILL.md` files at the repository root and an `scripts/install.sh` installer
**Category:** Marketing operations: positioning, cold outreach, content systems, LinkedIn and X voice, AI search visibility
**Quality Tier:** 🟡 Established - 455 stars, a real installer and three Pass verdicts on the flagship skill, held back by a missing LICENSE file and a Snyk Warn on the homepage audit skill.

This is a marketing toolkit written to be executed rather than read. Each folder at the repository root is one `SKILL.md` holding a framework with an output format, so "position my product" produces a positioning statement instead of advice about positioning. The README states 23 free skills plus 10 paid ones, and the March 2026 v3.1 release gave 19 of the free skills three execution modes: quick, standard and deep.

The subject matter is the operator's week rather than the marketer's channel list. Positioning basics, cold outreach sequences, case studies, testimonials, newsletter curation, a daily briefing, an energy-based day plan, and a set of writing skills that strip AI habits out of copy. `de-ai-ify` is the flagship at 599 installs, and it is the one most likely to be useful on its own: it removes the tells that make generated copy read as generated.

Two skills in the pack are structurally different from the rest. `reddit-insights` calls a paid MCP server at reddit-insights.com for semantic Reddit search rather than working from local instructions, and `ai-discoverability-audit` measures how a brand appears in ChatGPT, Perplexity, Claude and Gemini. Both are research surfaces rather than writing frameworks, and both are the reason this pack shows up in operator workflows at all.

## Installation

The repository ships its own installer, which is the route the README recommends for anything other than Claude Code:

```bash
git clone https://github.com/BrianRWagner/ai-marketing-claude-code-skills.git
cd ai-marketing-claude-code-skills
bash scripts/install.sh
```

The script detects installed agent platforms and writes the skills into each one. Four flags are documented:

```bash
bash scripts/install.sh --all              # every detected platform
bash scripts/install.sh --platform=cursor  # one platform only
bash scripts/install.sh --include-pro      # include paid pro/ skills
bash scripts/install.sh --dry-run          # preview without writing
```

For a single Claude Code profile the README's manual route is a flat copy, which is also the simplest way to install into a Hermes profile skills directory:

```bash
mkdir -p ~/.claude/skills
cp -r ai-marketing-claude-code-skills/* ~/.claude/skills/
```

That copy lands the repository's own `scripts/`, `pro/` and documentation alongside the 23 skill folders. Copy only the folders you intend to use if you mind the extra files being visible to the agent.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| de-ai-ify | 599 | Removes AI-generated jargon and restores human voice, built from analysing a large corpus of AI against human writing. |
| linkedin-profile-optimizer | 547 | Scores each section of a LinkedIn profile, rewrites the headline and about copy, and adds an AI visibility checklist. |
| reddit-insights | 521 | Semantic Reddit search through the reddit-insights.com MCP server for pain points, niche markets and product sentiment. |
| voice-extractor | 495 | Extracts a writer's voice from samples into a reusable voice guide for training later outputs. |
| homepage-audit | 489 | Conversion audit for a homepage or landing page, with a ranked list of what to change and why. |
| linkedin-authority-builder | 488 | Builds a LinkedIn content system for thought leadership and inbound lead flow. |
| last30days | 488 | Researches a topic across Reddit, X and the web for the last 30 days and returns trends and community sentiment. |
| content-idea-generator | 477 | Generates content ideas rooted in a positioning statement rather than in generic topic lists. |
| youtube-summarizer | 473 | Fetches a YouTube transcript and produces a structured summary with metadata. |
| plan-my-day | 460 | Produces a time-blocked daily plan from circadian rhythm research and GTD principles. |
| positioning-basics | 459 | Works through who the product is for, the alternative it replaces and the message that follows. |
| cold-outreach-sequence | 449 | Builds personalized LinkedIn and email outreach sequences with follow-up cadence. |
| newsletter-creation-curation | 446 | Industry-adaptive B2B newsletter creation with stage, role and geography-aware workflows. |
| case-study-builder | 440 | Turns a client win into a formatted case study for proposals and sales conversations. |
| marketing-principles | 433 | Applies durable marketing and business principles to a specific decision. |
| daily-briefing-builder | 416 | Generates a morning brief from vault content, today's priorities and unposted drafts. |
| ai-discoverability-audit | 414 | Audits how a brand appears in ChatGPT, Perplexity, Claude and Gemini, with the queries that matter. |
| go-mode | 411 | Autonomous goal execution: takes a goal, returns a plan, confirms, executes and reports. |
| social-card-gen | 407 | Generates platform-specific variants of one post for X, LinkedIn and Reddit with anti-spam guardrails. |
| testimonial-collector | 403 | Gathers, scores and formats client testimonials into usable social proof. |

The remaining 4 indexed listings range from 1 to 380 installs: tweet-draft-reviewer (380), meeting-prep-cc (379), vault-cleanup-auditor (374) and brand-voice-extractor (1). The install index carries 24 listings against 23 `SKILL.md` files in the tree, and `meeting-prep-cc` has no same-named folder in the current checkout.

## Why This Matters for Hermes Agents

Most marketing help an agent produces is generic because the input was generic. A skill with a stated output format forces the agent to collect the inputs that format requires, which is why `positioning-basics` asks who the alternative is before it writes a value proposition.

The pack is unusually honest about the operator's actual constraint. `plan-my-day` and `daily-briefing-builder` are about sequencing work, not producing assets, and `case-study-builder` and `testimonial-collector` turn material a business already owns into collateral it does not have. For a small team, that is where the leverage is: reusing proof that already exists instead of commissioning new content.

The two research skills are the ones to evaluate before installing the pack. `reddit-insights` requires an external MCP server and a subscription, so it fails silently if the server is not configured and the agent falls back to guessing at community sentiment. `ai-discoverability-audit` is a measurement skill in a space where most tools charge for the measurement.

The writing skills deserve separate mention because they are the ones with a measurable effect. `de-ai-ify` and `voice-extractor` are complementary: one removes the patterns that read as machine-written, the other supplies the replacement voice from real samples.

## Usage

| You say | What happens |
|---|---|
| "Remove the AI tone from this landing page" | Runs de-ai-ify, names the specific patterns it found and returns a rewrite with the jargon replaced. |
| "Audit my homepage for conversion" | Works through the homepage-audit checklist and returns findings ordered by expected impact. |
| "Who is this product actually for?" | Runs positioning-basics and returns a for-who, against-what, why-now statement rather than adjectives. |
| "Build me a cold outreach sequence for e-commerce founders" | Produces a multi-touch LinkedIn and email sequence with the trigger behind each message. |
| "How do we show up in ChatGPT?" | Runs ai-discoverability-audit across the four assistants and reports which queries the brand appears in, with gaps. |
| "What are people complaining about in our category right now?" | Uses reddit-insights semantic search for recent complaints, then groups them into themes. |
| "Turn this client win into a case study" | Structures the result, the before state and the mechanism into a formatted case study. |

## Verification

The skills sit at the repository root, one folder each. This returns 200:

```bash
curl -fsSL https://raw.githubusercontent.com/BrianRWagner/ai-marketing-claude-code-skills/main/de-ai-ify/SKILL.md | head -6
```

It should open with frontmatter naming the skill and describing it as removing AI-generated jargon. Check the installer before running it, since it writes into every detected agent directory:

```bash
curl -fsSL https://raw.githubusercontent.com/BrianRWagner/ai-marketing-claude-code-skills/main/scripts/install.sh | head -40
```

If you install by copying, confirm you copied the folders rather than the whole checkout, then list the skills directory and count the folders against the 23 `SKILL.md` files in the tree.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-11) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| de-ai-ify | Pass | Pass | Pass |
| homepage-audit | Pass | Pass | Warn |

The flagships pass, and one sampled sibling draws a single Snyk Warn. The larger point is licence rather than scanner: the repository has no LICENSE file while the README displays an MIT badge, so treat it as source-available with an unclear grant until the author adds the file.

Two operational notes. The installer executes shell that writes outside the repository, which is expected for an installer and still worth reading before running. And `reddit-insights` depends on a third-party MCP server, so installing the skill grants nothing until that server is configured and its own terms are accepted.

## Limitations

- Snapshot data, verified 2026-11-11: 10,449 combined installs across 24 indexed listings; 455 GitHub stars; no LICENSE file (README states MIT); last pushed 2026-03-19. Counts drift over time.
- The license position is unresolved in the repository itself. GitHub reports no licence and the README shows an MIT badge, so the safe reading is source-available with the author's intent stated informally.
- 24 indexed listings against 23 `SKILL.md` files, and `meeting-prep-cc` has no folder in the current tree. Its behaviour is therefore undocumented here.
- Ten of the skills are paid and live in a `pro/` directory that is not in the public checkout. The installer's `--include-pro` flag only does something if you have bought them.
- `reddit-insights` needs the reddit-insights.com MCP server and a subscription. Without it the skill has no data source.
- The pack is English-language and US-market shaped, and the README states its last content update as March 2026, so platform-specific advice on LinkedIn and X formats may already be behind the platforms.

## Related

- [OpenClaudia Skills - 78-Skill Marketing Toolkit Setup](/hermes/skills/catalog/openclaudia-skills-setup)
- [HyperFX Marketing Skills - Paid Media and Audience Playbooks](/hermes/skills/catalog/hyperfx-marketing-skills-setup)
- [Claude Blog - AI Blog Writing and SEO Plugin Setup](/hermes/skills/catalog/claude-blog-setup)

## Pro Tips

- Ask for the mode. After v3.1, "quick" returns a short answer and "deep" runs the full audit, and saying which one you want is faster than re-prompting a shallow result.
- Run `de-ai-ify` on the skill's own output. Marketing copy produced by a marketing skill is exactly where the patterns accumulate.
- Give `positioning-basics` the competitor page URL rather than the competitor name. The skill needs the alternative's claims, not its logo.
- Use `voice-extractor` before `linkedin-authority-builder`. The second skill writes in a voice, and without samples that voice is the model's default.
- Audit before you generate. Running `ai-discoverability-audit` first tells you which queries to write for, which is cheaper than writing and then measuring.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
