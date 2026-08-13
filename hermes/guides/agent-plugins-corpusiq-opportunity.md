---
title: Agent Plugins 1.0 — The Portable Skill Standard
description: "Setup and usage guide for Agent Plugins 1.0 — The Portable Skill Standard. Part of the Hermes resource directory."
last_updated: 2026-08-12
canonical: "https://www.corpusiq.io/docs/hermes/guides/agent-plugins-corpusiq-opportunity/"
robots: "index,follow"
tags: ["hermes agent", "ai agent", "nous research"]

---

# Agent Plugins 1.0 — The Portable Skill Standard

On August 6, 2026, OpenAI, Vercel, AWS, Microsoft, Google, and Cursor published Agent Plugins 1.0: an open, vendor-neutral standard for packaging AI agent skills and MCP servers into portable plugins. Build once. Deploy everywhere.

## What It Is

A simple directory structure:

```
my-plugin/
├── plugin.json          # name, version, description, requirements
├── skills/              # Agent Skills in SKILL.md format
│   └── summarize/
│       ├── SKILL.md
│       ├── scripts/
│       └── references/
├── mcp.json             # MCP server configuration
└── com.example.client/  # optional client-specific extensions
```

That's it. Three core files. One portable package.

## Who Is Behind It

The technical committee includes Amazon, Cursor, Microsoft, OpenAI, and Vercel. Google joined as a core maintainer. GitHub and Anysphere (Cursor) contributed to the specification. Six of the largest names in AI agreed on a shared format.

## Why This Matters for CorpusIQ

CorpusIQ has 100-plus Hermes skills covering growth operations, content creation, system management, email automation, social posting, and competitive research. Right now, these skills are locked inside a single Hermes profile.

Agent Plugins 1.0 changes that. Every CorpusIQ skill can be packaged as a portable plugin. A business owner using Claude Code could install the CorpusIQ Shopify analytics skill. A developer using Cursor could install the CorpusIQ MCP server configuration. An agency using Codex could install the full CorpusIQ business intelligence plugin.

The distribution model flips: instead of users coming to CorpusIQ and connecting their tools, the tools come to the user, inside whatever AI agent they already use.

## The SkillForge Ecosystem

SkillForge (105 stars, launched August 4, 2026) is already building the "npm for skills" — an MCP-native skill registry that follows the Agent Plugins specification. Skills published to SkillForge are discoverable and installable by any compatible agent.

CorpusIQ should be an early publisher on SkillForge. Every growth skill we have — Reddit commenting, Shopify outreach, email automation, competitive research — becomes a discoverable, installable plugin.

## The Immediate Opportunity

1. **Package the top 10 CorpusIQ skills** as Agent Plugins
2. **Publish to SkillForge** under the CorpusIQ namespace
3. **Include the affiliate link** in every skill's SKILL.md footer
4. **Watch adoption** — each skill install is a warm lead
5. **Iterate** — skills that get traction get deeper MCP integration

## Technical Implementation

The Hermes skill format (SKILL.md with YAML frontmatter) is already compatible with Agent Plugins. The mapping is straightforward:

| Agent Plugins | Hermes Skill | Status |
|---------------|-------------|--------|
| plugin.json | Skill frontmatter (name, description, version) | Compatible |
| skills/*/SKILL.md | SKILL.md content | Compatible |
| skills/*/scripts/ | Linked scripts | Compatible |
| skills/*/references/ | Linked references | Compatible |
| mcp.json | Hermes MCP config | Needs mapping |

The only new requirement is a top-level `plugin.json` manifest and an `mcp.json` file for any MCP server dependencies.

## The Math

If 10 CorpusIQ skills get 100 installs each across Claude Code, Cursor, Codex, and Gemini CLI users, that's 1,000 developers and business owners who now have CorpusIQ capabilities in their agent. Even a 1 percent conversion rate to paid signups means 10 new customers from skills alone.

The cost: one afternoon of packaging. The upside: perpetual distribution.
