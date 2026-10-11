---
title: "Vapi Skills - Voice AI Agent Building Setup"
description: "Setup guide for vapiai/skills - 8.0K combined installs. Official Vapi skills: create assistants, calls, tools, squads, and phone numbers."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/vapi-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-10"
tags: ["hermes skill", "agent skill", "skill setup", "voice ai", "voice agents", "mcp"]
---

# Vapi Skills - Setup Guide

**Source:** [vapiai/skills](https://www.skills.sh/vapiai/skills) via skills.sh - 8.0K combined installs across 16 indexed listings; first seen Oct 9, 2026 (extended-query probe)
**GitHub:** [vapiai/skills](https://github.com/vapiai/skills) (67 stars, NO LICENSE FILE; pushed 2026-10-08; `create-assistant/SKILL.md` layout, skill dirs at the repo root)
**Category:** Voice AI / Agent Building
**Quality Tier:** 🟡 Beta - official Vapi org; NO LICENSE file; pushed Oct 8, 2026; all sampled verdicts Pass

Vapi is a developer platform for building voice AI agents, and this is the official skills repository from the Vapi team. The skills follow the Agent Skills specification and run in any compatible assistant (Claude Code, Cursor, VS Code Copilot, Gemini CLI), covering the whole build loop: obtain an API key, create an assistant with models, voices, transcribers, tools, and hooks, attach a phone number from Twilio, Vonage, Telnyx, or Vapi, and place outbound calls, web calls, and batch calls. Squads, webhooks, workflows, campaigns, simulations, and structured post-call extraction round out the set.

Each skill lives in its own directory at the repo root (`create-assistant/SKILL.md` and so on), and the repository also ships a Vapi documentation MCP server that gives an agent the full Vapi knowledge base via RAG, auto-detected by Claude Code, Cursor, and VS Code Copilot. The README's quick start is a sensible install order: setup-api-key, then create-assistant, then create-phone-number, then create-call.

---

## Installation

Prerequisites: Node.js for the `npx` skills CLI, plus a Vapi API key at run time. Export it before using any skill:

```bash
export VAPI_API_KEY="your-api-key"
```

Install the full collection (note the case, `VapiAI/skills`, exactly as the README shows):

```bash
npx skills add VapiAI/skills
```

Install only what you need, or target a specific agent:

```bash
npx skills add VapiAI/skills --skill create-assistant
npx skills add VapiAI/skills --skill create-tool
npx skills add VapiAI/skills --skill create-campaign
npx skills add VapiAI/skills -a claude-code
npx skills add VapiAI/skills -a cursor
```

Claude Code can instead use the native plugin flow:

```text
/plugin marketplace add VapiAI/skills
/plugin install vapi-voice-ai@vapi-skills
```

The repository also assembles a Codex plugin from the canonical skill directories:

```bash
python3 scripts/build-codex-plugin.py
python3 scripts/build-codex-plugin.py --check
codex plugin marketplace add .
codex plugin add vapi-voice-ai@vapi-skills
```

Or copy any skill directory into your project's `.claude/skills/` (Claude Code), `.cursor/skills/` (Cursor), or the equivalent directory for your agent.

## What It Provides

Install counts from the Oct 10, 2026 skills.sh snapshot:

| Skill | Installs | Use For |
|---|---|---|
| create-assistant | 1,050 | Create voice AI assistants with models, voices, transcribers, tools, and hooks |
| create-call | 1,025 | Initiate outbound phone calls, web calls, and batch calls |
| setup-api-key | 930 | Obtain and configure a Vapi API key |
| create-phone-number | 921 | Set up phone numbers from Twilio, Vonage, Telnyx, or Vapi |
| setup-webhook | 915 | Configure server URLs to receive real-time call events |
| create-tool | 903 | Build custom tools for assistants: function calls, transfers, integrations |
| create-squad | 861 | Build multi-assistant squads with handoff workflows |
| create-workflow | 611 | Create and manage workflows for voice agent operations |

The remaining 8 indexed listings range from 2 to 273 installs.

## Why This Matters for Hermes Agents

Voice is the interface layer most agent stacks treat as an afterthought, and Vapi is one of the platforms where an agent can provision the whole thing end to end: the assistant, its tools, its phone number, its call flows. Because these skills are official, they encode the platform's current API patterns rather than a community paraphrase, and the payload-first structure (conceptual JSON plus separate SDK examples) means an agent can produce a correct call configuration before it commits to a language SDK. The bundled documentation MCP server is the multiplier: when a skill runs out of documented territory, the agent can query the full Vapi knowledge base instead of guessing. For Hermes agents doing client work in voice, this is close to a turnkey toolchain for building and testing phone agents, from API key setup to a verified test call. Two things to hold onto: there is no license file, and the skills deliberately do not invent SDK methods, so revalidating against current Vapi docs belongs in the loop.

## Usage

| You say | What happens |
|---|---|
| "Create a support assistant that triages billing questions" | create-assistant scaffolds the assistant with model, voice, transcriber, tools, and hooks |
| "Make a test outbound call to our demo line" | create-call places the call; batch and web calls use the same skill |
| "Get our Vapi API key into the project" | setup-api-key walks through obtaining and configuring the key |
| "Attach a phone number for the demo" | create-phone-number sets one up from Twilio, Vonage, Telnyx, or Vapi |
| "Send call events to our backend" | setup-webhook configures server URLs for real-time call events |
| "Give the assistant an order-lookup tool" | create-tool builds the function call, transfer, or integration the assistant needs |
| "Route callers between sales and support" | create-squad builds the multi-assistant handoff workflow |

## Verification

```bash
# Confirm the install through the skills CLI
npx skills list | grep -i vapi

# Or check the skills directory your agent scans
ls .claude/skills/ | grep -E 'create-assistant|create-squad'

# Review the flagship skill straight from GitHub before installing
curl -sL https://raw.githubusercontent.com/vapiai/skills/main/create-assistant/SKILL.md | head -20
```

## Security

skills.sh verdicts for sampled skills (verified Oct 10, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| create-assistant | Pass | Pass | Pass |
| create-squad | Pass | Pass | Pass |
| voice-assistant | - | - | - |

The scored sample passes on all three engines, but coverage is partial; re-check the security pages on skills.sh before production use.

## Limitations

- No LICENSE file in the repository; the README's License section states MIT, but with no license file, confirm terms with Vapi before redistribution.
- 67 GitHub stars: a young repository, so the community review surface is still small.
- Beta tier: the skills are official but early; revalidate SDK syntax against current Vapi documentation.
- Verdict coverage is partial; only a sample was scored on skills.sh.
- The Codex plugin is skills-only; the repository-level MCP configuration is not declared as a plugin dependency.
- Snapshot data, verified Oct 10, 2026: 7,994 combined installs across 16 indexed listings; 67 GitHub stars; NO LICENSE FILE; last pushed 2026-10-08. Counts drift over time.

## Related

- [Assistant UI Skills - AI Chat Interface Dev Suite Setup](/hermes/skills/catalog/assistant-ui-skills-setup) - the front-end side of an assistant product
- [Agent Skill Creator - Skill Generation and Templating Setup](/hermes/skills/catalog/agent-skill-creator-setup) - patterns for writing your own skills like these
- [Build Mcp Server Setup](/hermes/skills/catalog/build-mcp-server-setup) - build your own docs MCP server, like the one bundled here
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the quick-start four first: setup-api-key, create-assistant, create-phone-number, create-call. That is the README's own path to a working voice agent.
- Export VAPI_API_KEY before running any skill; every skill expects it.
- Let the bundled MCP docs server cover the long tail: the skills handle common workflows, the RAG server handles advanced configuration and SDK detail.
- Compare telephony providers (Twilio, Vonage, Telnyx, Vapi) against your existing account before provisioning a number.
- Revalidate SDK snippets against current docs; the skills intentionally never invent SDK methods.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
