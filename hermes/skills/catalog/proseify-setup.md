---
title: "Proseify - Anti-Prose-Slop Book Writing Setup"
description: "Setup guide for Proseify's anti-prose-slop skill: a hosted book-writing MCP with a public-domain corpus, genre recipes, and scored chapter drafting."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/proseify-setup/"
robots: "index,follow"
last_updated: "2026-10-08"
tags: ["hermes skill", "agent skill", "skill setup", "proseify", "book writing", "creative writing", "mcp"]
---

# Proseify - Anti-Prose-Slop Setup Guide

**Source:** [proseify.xyz](https://proseify.xyz) via skills.sh - 37,577 installs (`anti-prose-slop`); first seen Oct 8, 2026 (trending pass; the source is the product site itself, sized via the skills.sh API)
**Skill file:** [proseify.xyz/skills/anti-prose-slop/SKILL.md](https://proseify.xyz/skills/anti-prose-slop/SKILL.md) (MIT, fetchable for review - verified Oct 8, 2026)
**MCP server:** [Dionisselami/proseify-mcp](https://github.com/Dionisselami/proseify-mcp) (MIT; published in the official MCP registry as `io.github.Dionisselami/proseify-mcp`)
**Category:** Writing / Creative Content
**Quality Tier:** 🔵 Community (single-vendor product skill distributed from the product site; MIT; no skills.sh security verdicts published - due diligence required)

Proseify is a hosted MCP book-writing engine: give it a one-line premise and it picks a genre recipe, pulls model passages from a curated public-domain corpus, plans the outline, drafts chapter by chapter, and scores its own work. The `anti-prose-slop` skill is the workflow layer - discipline for using those tools well (genre recipe first, corpus grounding, chapter structure, and a per-chapter anti-slop editing pass) instead of raw tool access alone.

The skill's own compatibility line names Hermes among the agents it works with: "Works with any AI agent that can call the Proseify MCP server (Claude Code, Codex, Cursor, OpenCode, Hermes)."

---

## Installation

### 1. Connect the MCP server

Sign in at [proseify.xyz](https://proseify.xyz) and get a key (plans start at $9/month; a one-time lifetime option also exists). Then add the server to your agent's MCP config:

```json
{
  "mcpServers": {
    "proseify": {
      "type": "http",
      "url": "https://mcp.proseify.xyz/mcp",
      "headers": { "Authorization": "Bearer YOUR_KEY" }
    }
  }
}
```

### 2. Install the skill

```bash
npx skills add https://proseify.xyz --skill anti-prose-slop -y
```

The skill has no value without the MCP connection: no key, no tools.

## What It Provides

| Tool | What it does |
|---|---|
| `list_genres` | 11 genres with a growing library of books (theatre, horror, romance, adventure, literary, and more) |
| `search_corpus` | Full-text search across all chapters with FTS5 syntax (quotes, AND/OR/NOT, wildcards) |
| `get_genre_recipe` | Pacing beats, dialogue ratio, and stylistic anchors derived from the genre's tradition |
| `get_style_references` | Model passages from books matching a genre - the register you are aiming for |
| `plan_book` | Chapter-by-chapter outline from a one-line premise |
| `write_book` | The one-shot flow: plan, draft, evaluate in one session |
| `evaluate_book` | Scores a drafted book against genre benchmarks so weak chapters get revised |

The corpus is drawn from Project Gutenberg and similar public-domain collections, verified against original headers (the repository describes 81 classics across 11 genres); the project states commercial use of output built on it is safe.

The skill's anti-slop checklist targets the real failure mode of AI prose - sameness: "seemed to", "began to", stacked adverbs, repeated sentence constructions, filter words, dialogue-as-exposition, and chapter openings that always start with weather.

## Why This Matters for Hermes Agents

Longform creative work is where generic agents fail most visibly: endless prose in a single register. This pipeline forces a genre-first order of operations (recipe, corpus grounding, outline, drafts, scored revision) and gives the agent a scoring loop over its own output. It is also a clean example of the skill-on-top-of-MCP pattern: the MCP server supplies tools, the skill supplies workflow discipline, and the combination produces a manuscript a human can edit and ship.

## Usage

| You say | What happens |
|---|---|
| "I want a gothic horror novel about a lighthouse keeper who finds a body that should not exist. 32 chapters." | Genre recipe, corpus passages, outline, then chapter drafts with scored revision |
| "Find me the register for a Victorian adventure story" | `search_corpus` plus `get_style_references` return model passages from the tradition |
| "Score this draft against genre norms" | `evaluate_book` returns a benchmark comparison the agent uses to revise |
| "Plan the book before writing anything" | `plan_book` produces the full chapter outline for review first |

## Verification

```bash
# Confirm the skill is installed
npx skills list | grep anti-prose-slop

# Confirm the MCP endpoint responds (expect an auth challenge without a key)
curl -s -o /dev/null -w "%{http_code}" https://mcp.proseify.xyz/mcp
```

## Security

No skills.sh content-security verdicts were published for this skill at verification time (the source is the product site, and its skills.sh detail page is not available). What is verifiable:

| Item | Status |
|---|---|
| Skill license | MIT (stated in the skill frontmatter) |
| Skill file | Fetchable and reviewable before install: `https://proseify.xyz/skills/anti-prose-slop/SKILL.md` |
| MCP server repo | [Dionisselami/proseify-mcp](https://github.com/Dionisselami/proseify-mcp), MIT |
| External service | Drafting runs on Proseify's hosted service; your premise and drafts go to their API |

Review the skill file and the service's terms before connecting; the skill instructs the agent to write books via the hosted API with your key.

## Related

- [Book-to-Skill - Book to Agent Skill Converter Setup](/hermes/skills/catalog/book-to-skill-setup) - turns books into agent skills; the inverse direction of this pipeline
- [Writing Plans - Subagent Development Setup](/hermes/skills/catalog/writing-plans-subagent-development-setup) - planning discipline for long agent tasks
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

1. **Connect the MCP first.** The skill explicitly depends on it - installation order matters.
2. **Budget before you generate.** Set a chapter count and word budget in the ask; the pipeline plans against it.
3. **Read the genre recipe yourself once.** It explains why the output reads the way it does; it is short and makes revisions easier.
4. **Do not fight the score loop.** Let `evaluate_book` grade first drafts and revise the weak chapters; that iteration is the product.
5. **Keep the corpus claim in scope.** Public-domain grounding covers the reference library; your manuscript and its commercial use are your own responsibility under the service terms.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
