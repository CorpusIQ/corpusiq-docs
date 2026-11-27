---
title: "prompts.chat - Prompt Lookup, Translation and Widget Skills"
description: "f/prompts.chat - 5.8K combined installs across 4 skills: prompt and skill lookup over the prompts.chat library, book translation, and widget plugins."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/f-prompts.chat-setup/"
robots: "index,follow"
last_updated: "2026-11-26"
tags: ["hermes skill", "agent skill", "skill setup", "prompts", "prompt library", "prompt engineering"]
---

# prompts.chat - Setup Guide

**Source:** [f/prompts.chat](https://www.skills.sh/f/prompts.chat) via skills.sh - 5.8K combined installs across 4 indexed listings; first catalogued Nov 26, 2026 (Nov 26, 2026 evening sweep)
**GitHub:** [f/prompts.chat](https://github.com/f/prompts.chat) - 178,621 stars, dual-licensed (MIT for source, CC0 for prompt data; GitHub reports NOASSERTION), last pushed Nov 27, 2026, main branch; four skills across plugins/claude/prompts.chat/skills/ and .windsurf/skills/.
**Category:** Prompt Library (Prompts and Agent Skills)
**Quality Tier:** 🟡 Yellow - 3 Warn cells across the 4 sampled skills and no fails, so the suite stays Yellow.

This is the repository behind prompts.chat, the community prompt library formerly known as Awesome ChatGPT Prompts, live since December 2022. The repo is far larger than its four indexed skills: it hosts the Next.js site, an interactive book of prompting translated into 17 languages, a kids mode, bot and bot-team systems, a CLI, and an MCP server. skills.sh indexes four skills here, and they are capabilities rather than a bundled product: two look up content from the prompts.chat registry, one translates the interactive book, and one generates widget plugins for the feed.

The four skills live in two places. prompt-lookup and skill-lookup sit under plugins/claude/prompts.chat/skills/ and ship as part of the Claude Code plugin, while book-translation and widget-generator sit under .windsurf/skills/. The two lookup skills are the general-purpose pair; the other two are contributor tools for maintaining the prompts.chat project itself.

## Installation

The README documents a Claude Code plugin that packages the two lookup skills, plus an optional MCP server that skill-lookup uses to search and install from the registry. Install the plugin first:

```
/plugin marketplace add f/prompts.chat
/plugin install prompts.chat@prompts.chat
```

book-translation and widget-generator are not part of the plugin, so copy them (or the lookup skills, for agents that read skill files directly) from a clone:

```bash
git clone --depth 1 https://github.com/f/prompts.chat.git
mkdir -p ~/.claude/skills
cp -r prompts.chat/plugins/claude/prompts.chat/skills/prompt-lookup ~/.claude/skills/
cp -r prompts.chat/plugins/claude/prompts.chat/skills/skill-lookup ~/.claude/skills/
cp -r prompts.chat/.windsurf/skills/book-translation ~/.claude/skills/
cp -r prompts.chat/.windsurf/skills/widget-generator ~/.claude/skills/
```

For registry access, point an MCP client at the prompts.chat server:

```json
{
  "mcpServers": {
    "prompts.chat": {
      "url": "https://prompts.chat/api/mcp"
    }
  }
}
```

## What It Provides

skills.sh publishes a per-skill install count for each of the four indexed listings.

| Skill | Installs | Use For |
|---|---|---|
| skill-lookup | 2,691 | Search, retrieve, and install Agent Skills from the prompts.chat registry via MCP tools |
| prompt-lookup | 2,109 | Discover, retrieve, and improve prompts when asked about AI prompts or templates |
| book-translation | 689 | Translate chapters and UI strings of The Interactive Book of Prompting into a new language |
| widget-generator | 318 | Generate customizable widget plugins for the prompts.chat feed system |

No indexed listings fall below the 300-install threshold; all 4 appear in the table above.

## Why This Matters for Hermes Agents

prompts.chat is one of the oldest and largest open prompt libraries, so an agent that reaches for community prompts gets a broad, CC0-licensed corpus to draw from. prompt-lookup gives a Hermes agent structured access to that library instead of scraping the site, and skill-lookup turns the same registry into a source of reusable Agent Skills it can install for Claude. The two are a natural fit for an agent that both consumes prompts and assembles multi-skill toolchains. The other two skills are contributor-facing: book-translation and widget-generator matter when the agent maintains or extends the prompts.chat project itself, not when it merely uses the library. The licensing split is also useful to know up front: prompt data is CC0, so prompts pulled through the lookup skill can be reused freely, while the source code is MIT. The trade-off is surface area, since the four skills are a small slice of a 1,890-file web application.

## Usage

| You say | What happens |
|---|---|
| Find a prompt for writing marketing copy | prompt-lookup searches the prompts.chat library and returns matching prompt templates |
| List Agent Skills I can install | skill-lookup queries the prompts.chat registry and installs a chosen skill for Claude |
| Improve this prompt | prompt-lookup retrieves and refines a prompt from the library |
| Translate the prompting book into Spanish | book-translation translates book chapters and UI strings into the target language |
| Build a widget for my prompt feed | widget-generator scaffolds a customizable widget plugin for the feed system |

## Verification

Confirm the skills and the README resolve on the main branch before installing:

```bash
curl -sL https://raw.githubusercontent.com/f/prompts.chat/main/README.md | head -40
curl -sL https://raw.githubusercontent.com/f/prompts.chat/main/plugins/claude/prompts.chat/skills/skill-lookup/SKILL.md | head -40
curl -sL https://raw.githubusercontent.com/f/prompts.chat/main/plugins/claude/prompts.chat/skills/prompt-lookup/SKILL.md | head -40
curl -sL https://raw.githubusercontent.com/f/prompts.chat/main/.windsurf/skills/book-translation/SKILL.md | head -40
curl -sL https://raw.githubusercontent.com/f/prompts.chat/main/.windsurf/skills/widget-generator/SKILL.md | head -40
```

All five URLs return 200. After installing, review each SKILL.md before relying on it.

## Security

skills.sh verdicts for sampled skills (verified Nov 26, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| skill-lookup | Pass | Warn | Warn |
| prompt-lookup | Pass | Pass | Warn |
| book-translation | Pass | Pass | Pass |
| widget-generator | Pass | Pass | Pass |

Across the 4 sampled skills there are 12 Pass, 3 Warn, and 0 Fail cells; the three Warn cells sit on the two lookup skills (skill-lookup: Socket and Snyk; prompt-lookup: Snyk), which keeps the suite at Yellow.

## Limitations

- Snapshot data, verified Nov 26, 2026: 5,807 combined installs across 4 indexed listings; 178,621 GitHub stars; dual-licensed (MIT for source, CC0 for prompt data); last pushed Nov 27, 2026. Counts drift over time.
- The repo is the full prompts.chat application (1,890 files), not a skill collection; the four skills are a small slice of a large web app.
- book-translation and widget-generator are contributor tools for maintaining prompts.chat itself, not general-purpose agent skills.
- skill-lookup depends on the prompts.chat MCP server for registry access; without MCP configured it cannot search or install skills.
- The Claude Code plugin packages only the two lookup skills; the Wind Surf skills require a manual copy.
- GitHub reports NOASSERTION while the README states dual licensing (MIT for source, CC0 for prompt data); treat prompt data as public domain and source as MIT.

## Related

[Context Engineering Kit - Prompt and MCP Setup](/hermes/skills/catalog/context-engineering-kit-setup) | [LLM Code Skills - Cross-Tool Documentation Pack](/hermes/skills/catalog/llm-code-setup) | [Hermes Agent Skill Authoring - Official SKILL.md Writing Guide](/hermes/skills/catalog/hermes-agent-skill-authoring-setup) | [Dotneet Claude Code Marketplace - Plugin Collection Setup](/hermes/skills/catalog/dotneet-claude-code-marketplace-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Prefer the Claude Code plugin for the two lookup skills; it wires the marketplace entry and MCP config together.
- Configure the prompts.chat MCP server before relying on skill-lookup, since registry search and install run through MCP tools.
- Reuse prompts freely: prompt content is CC0, so prompts pulled via prompt-lookup can ship in your own agent.
- For an agent that only needs prompt templates, load prompt-lookup's SKILL.md alone; you do not need the whole repo.
- Keep the four SKILL.md files in your own skills directory rather than pointing at the monorepo, so upstream changes do not rewrite your copy.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
