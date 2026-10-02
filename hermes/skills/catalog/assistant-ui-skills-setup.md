---
title: "Assistant UI Skills - AI Chat Interface Dev Suite Setup"
description: "Setup guide for assistant-ui/skills: 17 agent skills for building AI chat interfaces with assistant-ui. 89.4K+ combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/assistant-ui-skills-setup/"
robots: "index,follow"
last_updated: "2026-09-30"
tags:
  - hermes skill
  - agent skill
  - skill setup
  - ai chat ui
  - frontend development
  - assistant-ui
---

# Assistant UI Skills - AI Chat Interface Dev Suite Setup

**Source:** [assistant-ui/skills](https://github.com/assistant-ui/skills) (28⭐, no LICENSE file, main branch, updated Sep 25, 2026) / **Skill:** `assistant-ui/skills` (17 installable skills, 89.5K combined installs) / **Publisher:** assistant-ui team (open source org) / **Category:** AI Chat UI / Frontend Development / **Quality Tier:** 🟡 Beta (functional, author-tested; repo has no LICENSE file, see Security, verified Sep 30, 2026)

assistant-ui/skills is the official skills repository from the assistant-ui organization, the team behind the assistant-ui chat library which has about 9K stars on its main project. The skills repo packages 17 agent skills for building AI chat interfaces: runtime setup, streaming, tool calling, UI primitives, thread lists, and framework bindings. Combined installs exceed 89K, which makes it one of the larger chat UI skill suites available. Note that the repository ships without a LICENSE file, so treat reuse as rights-reserved until the organization adds one.

## Installation

```bash
npx skills add assistant-ui/skills
```

After installation, run `npx skills --list` and expect 17 entries under `assistant-ui/skills`. You can also clone the repository with `git clone https://github.com/assistant-ui/skills.git` and copy individual `SKILL.md` folders into your agent's skills directory if you only need a subset.

## Roster

| Skill | Installs | Does |
|---|---|---|
| assistant-ui | 6.6K | Core chat interface components and patterns |
| streaming | 6.0K | Streaming response handling for chat agents |
| tools | 5.8K | Tool calling and function integration in chat UI |
| primitives | 5.8K | Base UI primitives and composition patterns |
| runtime | 5.8K | Assistant runtime wiring and message lifecycle |
| thread-list | 5.7K | Conversation thread list and history components |
| setup | 5.6K | Project setup and configuration for assistant-ui |
| update | 5.4K | Migration and update guides between versions |
| +9 more (cloud, copilots, elements, generative-ui, ink, markdown, observability, react-mcp, react-native) | 42.8K combined | Cloud runtime, copilots, elements, generative UI, ink, markdown rendering, observability, React MCP, and React Native support |

## CorpusIQ Use Cases

| Use Case | How It Helps |
|---|---|
| Prototyping chat interfaces for visual answers | runtime and primitives provide a fast path for chat UI mockups |
| Streaming MCP answers in the dashboard | streaming covers incremental response display |
| Tool call surfaces for internal agents | tools documents rendering and approving tool calls |

## Limitations / Verification

Verified Sep 30, 2026. The repository has 28 stars and 17 `SKILL.md` entries; install figures were confirmed against the skills marketplace on the same date. The organization's main library has about 9K stars, so this skill repo is early and its layout may still change. The eight top skills account for roughly half of all installs; the remaining nine have lower individual counts.

## Security

License: no LICENSE file present in the repository. Without a license, copyright defaults to the rights holder, so confirm reuse terms with the assistant-ui organization before commercial redistribution.

| Scanner | Status |
|---|---|
| Gen Agent Trust Hub | Not published |
| Socket | Not published |
| Snyk | Not published |

## Related

- [Gemini Skills Setup](/hermes/skills/catalog/gemini-skills-setup)
- [Meta Quest Agentic Tools Setup](/hermes/skills/catalog/meta-quest-agentic-tools-setup)
- [Skills Marketplace](/hermes/skills/marketplace)

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*

*Powered by CorpusIQ*
