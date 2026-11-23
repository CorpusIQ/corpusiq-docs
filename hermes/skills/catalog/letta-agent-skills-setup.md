---
title: "Letta Skills - Shared Agent Knowledge Base Setup"
description: "letta-ai/skills: shared community knowledge base where agents share tool integrations, patterns and Letta design - 8.6K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/letta-agent-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-23"
tags: ["hermes skill", "agent skill", "skill setup", "letta", "agent memory", "community skills"]
---

# Letta Skills - Shared Agent Knowledge Base Setup

**Source:** [letta-ai/skills](https://www.skills.sh/letta-ai/skills) via skills.sh - 8.6K combined installs across 94 indexed listings; first catalogued Nov 23, 2026 (Nov 23, 2026 morning sweep)
**GitHub:** [letta-ai/skills](https://github.com/letta-ai/skills) - 157 stars, NOASSERTION license, main branch, last pushed Oct 1, 2026; one SKILL.md per skill directory under letta/, tools/ and meta/, each with optional references/, scripts/ and assets/ subfolders, plus a root LICENSE and per-skill LICENSE files.
**Category:** Agent Skills and Community Knowledge Base
**Quality Tier:** 🟠 Orange - 4 Fail cells and 11 Warn cells across the 20-skill sample: Gen Agent Trust Hub Fails on imessage, agent-slack and letta-configuration, Socket Fails on letta-api-client, and Warns are scattered across the top listings.

This repository is a community knowledge base where AI agents learn from each other's experience building applications. As agents discover patterns, integrate tools and validate best practices, they share that knowledge back through a living repository that is explicitly inspired by Anthropic Skills and intended to work with Letta Code, Claude Code, Codex CLI and other agents that support skills.

The suite is organized into three flat groups: letta/ for the Letta product ecosystem (agent design, fleet management, memory import and provider configuration), tools/ for general integrations (PDF, spreadsheets, slides, MCP servers, Slack, Yelp and more), and meta/ for the skill-development skill that documents how to contribute. This guide covers letta-ai/skills only; the separate Letta Code repository has its own catalog page.

## Installation

Clone the repository into a `.skills` directory in any project you work from. Letta Code and Claude Code both support skills and discover them automatically:

```bash
git clone git@github.com:letta-ai/skills.git .skills
```

Or over HTTPS:

```bash
git clone https://github.com/letta-ai/skills.git .skills
```

Letta agents perform dynamic skill discovery, so after cloning you can ask the agent to check for new skills and update its skills memory block. The README's recommended path is to install Letta Code and ask the agent to browse the repository and download the skills that fit the task.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| letta-api-client | 355 | Letta API client - no matching directory in the current tree |
| pdf | 277 | reading, creating and reviewing PDFs with rendered page checks |
| extracting-pdf-text | 257 | extracting text from PDFs |
| letta-development-guide | 214 | designing and building Letta agents: architecture, memory, model and tool selection |
| imsg | 210 | iMessage and SMS CLI for listing chats, history and sending messages |
| imessage | 206 | iMessage messaging |
| video-processing | 189 | video processing |
| morph-warpgrep | 179 | Morph WarpGrep fast code search and Fast Apply editing for coding agents |
| ai-news | 177 | fetching and summarizing recent AI news from RSS feeds and YouTube channels |
| letta-fleet-management | 171 | managing and orchestrating multiple Letta agents |
| agent-slack | 170 | Slack integration for searching and sending messages |
| yelp-search | 165 | searching Yelp for local businesses, ratings and hours |
| Letta Conversations API | 162 | managing agent conversations and message history |
| mcp-builder | 155 | creating MCP servers that connect LLMs to external services |
| spreadsheet | 155 | creating, editing and analyzing spreadsheets with formula-aware workflows |
| skill-development | 154 | creating and contributing skills to the knowledge base |
| letta-configuration | 152 | configuring LLM models and providers for Letta agents and servers |

The remaining 77 indexed listings range from 34 to 141 installs.

## Why This Matters for Hermes Agents

An agent that has never integrated a specific tool or framework will improvise, and the improvisation is usually wrong. This repository replaces that with skills contributed and peer-reviewed by other agents, so an agent inherits validated patterns instead of guessing at PDF rendering, MCP server structure or Letta provider settings. The highest-value skills for a builder are letta-configuration, which names the exact model handles and provider settings a Letta agent needs, and mcp-builder, which turns an external API into a well-designed MCP server in Python or Node/TypeScript. For operators running many agents, letta-fleet-management and the skill-development meta skill matter most: the former covers orchestration and canary deployments, the latter documents how to contribute new skills back so the base keeps improving. The memory-focused skills (importing-chatgpt-memory, navigating-chatgpt-history, memfs-search) let an agent review past conversations as reference memory instead of forcing full upfront ingestion. Because skills load on demand rather than all at once, an agent pulls only the directory it needs.

## Usage

| You say | What happens |
|---|---|
| Install letta skills | Clones the repository into .skills; Letta Code and Claude Code discover skills automatically |
| Configure a new LLM provider for my Letta agent | The letta-configuration skill walks model handles, provider settings and environment variables |
| Build an MCP server for this API | The mcp-builder skill guides server creation with FastMCP or the Node/TypeScript SDK |
| Read this PDF and check the layout | The pdf skill renders pages for visual checks instead of text-only extraction |
| Search Yelp for local restaurants | The yelp-search skill returns business info, ratings and hours |
| Create a slide deck | The slides skill builds a .pptx deck with bundled layout helpers |
| Help me contribute a skill | The skill-development skill walks the contribution and validation workflow |

## Verification

Confirm the agent development guide resolves on the main branch:

```bash
curl -sL https://raw.githubusercontent.com/letta-ai/skills/main/letta/agent-development/SKILL.md | head -30
```

Spot-check a tool integration to confirm the flat directory layout:

```bash
curl -sL https://raw.githubusercontent.com/letta-ai/skills/main/tools/pdf/SKILL.md | head -30
```

Confirm the meta skill is present before contributing:

```bash
curl -sL https://raw.githubusercontent.com/letta-ai/skills/main/meta/skill-development/SKILL.md | head -30
```

## Security

skills.sh verdicts for sampled skills (verified Nov 23, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| letta-api-client | Pass | Fail | Warn |
| pdf | Pass | Pass | Pass |
| extracting-pdf-text | Pass | Pass | Warn |
| letta-development-guide | Pass | Pass | Pass |
| imsg | Pass | Pass | Warn |
| imessage | Fail | Pass | Pass |
| video-processing | Pass | Pass | Pass |
| morph-warpgrep | Pass | Pass | Pass |
| ai-news | Pass | Pass | Warn |
| letta-fleet-management | Pass | Warn | Warn |
| agent-slack | Fail | Pass | Warn |
| yelp-search | Pass | Warn | Warn |
| Letta Conversations API | not parsed | not parsed | not parsed |
| mcp-builder | Pass | Pass | Pass |
| spreadsheet | Warn | Pass | Pass |
| skill-development | Pass | Pass | Pass |
| letta-configuration | Fail | Warn | Pass |
| doc | Pass | Pass | Pass |
| slides | Pass | Pass | Pass |
| visual-identity | Pass | Pass | Pass |

The Fail cells are Gen Agent Trust Hub on imessage, agent-slack and letta-configuration plus Socket on letta-api-client; the Letta Conversations API listing carries no parsed verdict, and 74 of the 94 indexed listings were outside the 20-skill sample.

## Limitations

- Snapshot data, verified Nov 23, 2026: 8,594 combined installs across 94 indexed listings; 157 GitHub stars; NOASSERTION license; last pushed Oct 1, 2026. Counts drift over time.
- The install index outruns the tree: letta-api-client, extracting-pdf-text, imessage, video-processing and agent-slack carry install counts but have no matching directory in the current tree, and indexed names like letta-development-guide and letta-fleet-management map to the letta/agent-development and letta/fleet-management directories under a different spelling.
- The index carries near-duplicate listings: imsg (210) and imessage (206) both describe the iMessage CLI, and agent-slack (170) sits alongside slack (36) as separate listings.
- GitHub reports the repository license as NOASSERTION, but the README states MIT by default with per-skill LICENSE files taking precedence for their own directory; upstream skills keep their original terms.
- Several integrations are platform-specific: imsg and screenshot target macOS, and the README's example prompts assume Letta Code or Claude Code.

## Related

- [Letta Code - 24-Skill Stateful Agent Harness Setup Guide](/hermes/skills/catalog/letta-ai-agent-harness-setup)
- [AgentMemory Setup - Persistent Memory for Hermes Agents](/hermes/skills/catalog/agentmemory-setup)
- [Awesome AI Agent Skills - 103-Skill Agent Library](/hermes/skills/catalog/awesome-ai-agent-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Clone to .skills and let the agent discover skills dynamically instead of preloading all 94 listings into context.
- Start with letta-configuration to pin model and provider settings before any Letta build.
- Use the pdf and slides skills for rendered checks on any document you hand an agent to edit.
- Read CULTURE.md before contributing; the skill-development skill documents the peer-review and validation workflow.
- Treat per-skill LICENSE files as authoritative for their directory; the root is MIT by default but upstream skills keep their own terms.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
