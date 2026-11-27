---
title: "Coji Natural Japanese - Japanese Business Writing Setup"
description: "coji/natural-japanese - 6.2K combined installs across 2 indexed listings: Agent Skills for writing clear, natural Japanese business documents."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/coji-natural-japanese-setup/"
robots: "index,follow"
last_updated: "2026-11-26"
tags: ["hermes skill", "agent skill", "skill setup", "japanese", "writing", "business"]
---

# Coji Natural Japanese - Setup Guide

**Source:** [coji/natural-japanese](https://www.skills.sh/coji/natural-japanese) via skills.sh - 6.2K combined installs across 2 indexed listings; first catalogued Nov 26, 2026 (Nov 26, 2026 evening sweep)
**GitHub:** [coji/natural-japanese](https://github.com/coji/natural-japanese) - 2,089 stars, MIT license, last pushed Nov 6, 2026, main branch; two skills at skills/natural-japanese/SKILL.md and skills/critical-thinking/SKILL.md.
**Category:** Japanese Business Writing
**Quality Tier:** 🟡 Yellow - critical-thinking passes all three auditors, but natural-japanese carries a Socket Warn.

coji/natural-japanese is a two-skill suite for polishing Japanese business writing. The flagship natural-japanese skill writes and revises work documents such as meeting minutes, investigation reports, customer-facing reports, internal guides, technical articles, PR descriptions, research memos, proposals, emails, and slide decks so they read as natural, clear Japanese. The companion critical-thinking skill reviews decision-facing documents (approval requests, proposals, plans, reports) from a decision-maker's perspective and rewrites them so the argument survives scrutiny.

Both skills ship Japanese-language instruction sets and examples and respond to Japanese prompts, so the suite is for teams that write Japanese business text. The README's only English is a two-sentence summary; there is no English-language version of either skill, and the docs make no claim of English coverage. The repository is MIT-licensed, holds 2,089 stars, and was last pushed Nov 6, 2026.

## Installation

The README documents a skills CLI install:

```bash
npx skills add coji/natural-japanese
```

Follow the on-screen prompts to choose which skills to install and which agent to target. Claude Code users can add it as a plugin:

```
/plugin marketplace add coji/natural-japanese
/plugin install natural-japanese@natural-japanese
```

An AGENTS.md route is also available through OpenSkills:

```bash
npx openskills install coji/natural-japanese
npx openskills sync
```

For a manual install, download natural-japanese.skill (and critical-thinking.skill if you want both) from the GitHub Releases page and expand them into your agent's skills directory.

## What It Provides

skills.sh publishes a per-skill install count for the two indexed listings.

| Skill | Installs | Use For |
|---|---|---|
| natural-japanese | 5,828 | Write or revise Japanese work documents (minutes, reports, technical articles, PR descriptions, emails, slides) so they read naturally and clearly; also scores AI-sounding text without rewriting |
| critical-thinking | 365 | Review decision-facing Japanese documents (approval requests, proposals, plans, reports) from a decision-maker's perspective; checks logic and premises and rebuilds the argument structure |

No indexed listings fall below the 300-install threshold.

## Why This Matters for Hermes Agents

Japanese business writing has a distinct failure mode: documents written by a general model tend to read as translated-from-English or AI-flavored, with loan-word calques and noun-heavy phrasing that native readers notice but the writer does not. natural-japanese attacks that directly, pairing a machine detector (sudachipy morphological analysis in lint.py) with the agent's own context judgment, because a model rarely sees its own writing tics. critical-thinking handles the other half of a business document: whether the argument would survive a decision-maker, checking contradictions, unsupported claims, and mixed fact and inference before rewriting.

For a Hermes agent the value is a reusable, Japanese-native standard that keeps facts, numbers, and the writer's confidence level intact, which a generic "make it concise" prompt does not guarantee. The suite is MIT-licensed and its detection scripts run standalone through uv, so the lint layer can be reused even outside the skill loop. The trade-off is language: every instruction and example is Japanese, so an agent working in English gains nothing here.

## Usage

| You say | What happens |
|---|---|
| 「読みやすくして」(make this easier to read) | Rewrites the document in natural, plain Japanese without adding facts, numbers, opinions, or confidence |
| 「議事録にして」(turn this into minutes) | Converts a transcript into meeting minutes in readable Japanese |
| 「AI っぽいところを直して」(fix the AI-sounding parts) | Removes AI-typical phrasing so the text reads as human-written |
| /natural-japanese score draft.md | Returns a 0 to 100 naturalness score with reasons, without rewriting the file |
| /critical-thinking 稟議書.md | Reviews an approval document, asks up to 3 writer-only questions, and returns a fixed version plus a separate confirmation file |
| /critical-thinking logic 提案書.md | Checks internal logic only and returns line-numbered questions plus a YAML file, leaving the document untouched |
| 「構成から組み直して」(rebuild the structure) | Rebuilds the argument structure while preserving facts and the requested content, offering 2 to 3 outline options |

## Verification

Confirm the two SKILL.md files resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/coji/natural-japanese/main/skills/natural-japanese/SKILL.md | head -40
curl -sL https://raw.githubusercontent.com/coji/natural-japanese/main/skills/critical-thinking/SKILL.md | head -40
```

Both URLs return 200. After installing, read each SKILL.md and its references before relying on it.

## Security

skills.sh verdicts for sampled skills (verified Nov 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| natural-japanese | Pass | Warn | Pass |
| critical-thinking | Pass | Pass | Pass |

Across the 2 sampled listings there are 5 Pass, 1 Warn, and 0 Fail cells; the single Warn is Socket on natural-japanese.

## Limitations

- Snapshot data, verified Nov 26, 2026: 6,193 combined installs across 2 indexed listings; 2,089 GitHub stars; MIT license; last pushed Nov 6, 2026. Counts drift over time.
- Both skills are Japanese-only: the instruction sets, references, examples, and trigger prompts are Japanese, so teams working in English get no coverage from this suite.
- The README notes natural-japanese misses roughly half of loan-translation idioms and noun-packed phrasing, and that lowering model effort increases the miss rate; use a high-effort setting where available.
- critical-thinking's logic and somosomo checks rely on the model's reading, so running the same document twice can produce different findings.
- Socket returns a Warn on natural-japanese (the other five sampled cells Pass), so treat the suite as reviewed code, not a no-risk dependency.
- The repository holds 322 files, most of them corpus experiments, release-note archives, and evaluation fixtures; only the two skills under skills/ are the catalog listings.

## Related

[Yomiyasu - Japanese AI Prose Refinement Setup](/hermes/skills/catalog/yomiyasu-setup) | [Genshijin Skills - Japanese Concise-Reply Framework Setup](/hermes/skills/catalog/genshijin-skills-setup) | [Philtz JP Skills - Japanese Business Dev Suite](/hermes/skills/catalog/philtzjp-skills-setup) | [Matt Pocock Skills (简体中文) - Localized Engineering Suite Setup](/hermes/skills/catalog/mattpocock-skills-zh-cn-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Use `/natural-japanese score <file>` first to get a naturalness score and reasons before committing to a full rewrite.
- Run the detector standalone with `uv run skills/natural-japanese/scripts/lint.py draft.md` to list suspicious phrasing and suggested fixes without going through the agent.
- After any revision, run `uv run skills/natural-japanese/scripts/newfacts.py original.md revised.md` to confirm no numbers or proper nouns were added.
- Pair the two skills: natural-japanese fixes the wording, critical-thinking fixes the argument behind a decision document.
- Keep the references folder together with each SKILL.md; both skills load doctype and workflow guidance by relative path.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
