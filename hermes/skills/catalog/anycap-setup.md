---
title: "AnyCap Skills - Capability Harness Setup"
description: "anycap-ai/anycap: 5.8K combined installs across 9 listings, a capability harness covering media production, deep research, SEO and social workflows."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/anycap-setup/"
robots: "index,follow"
last_updated: "2026-11-17"
tags: ["hermes skill", "agent skill", "skill setup", "media production", "deep research", "seo", "social media"]
---

# AnyCap Skills - Setup Guide

**Source:** [anycap-ai/anycap](https://www.skills.sh/anycap-ai/anycap) via skills.sh - 5.8K combined installs across 9 indexed listings; first seen Nov 17, 2026 (this sweep)
**GitHub:** 51 stars, MIT license, main branch, last pushed 2026-11-17, skills under skills/<name>/SKILL.md
**Category:** Media production, research and SEO capability skills for agents
**Quality Tier:** 🟡 Yellow - four of the nine sampled skills carry a Snyk Warn.

anycap-ai/anycap ships AnyCap, a capability runtime that gives coding agents a single CLI, an Agent Skill and a local MCP server for media production, deep research, AI tool SEO, social meme workflows, human interaction and blog production. The nine indexed skills are one skill per capability, each a workflow an agent can route into from a natural-language request.

The project is packaged as skills over SDKs: the same installed runtime and authentication state back the CLI, the MCP server and the skills, so an agent can generate images, search and crawl the live web, and publish results without switching tools. Media-production is the most-installed skill at 852; deep-research and AI tool SEO follow at 814 and 746.

## Installation

Install the CLI, the Agent Skill and authenticate:

```bash
curl -fsSL https://anycap.ai/install.sh | sh
npx -y skills add anycap-ai/anycap -s '*' -g -y
anycap login
anycap status
```

Install as an agent plugin in Claude Code:

```text
/plugin marketplace add anycap-ai/anycap
/plugin install anycap@anycap
```

For a stdio MCP client, configure anycap mcp and add a narrowly scoped --allow-root path only when the server needs local media access.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| anycap-media-production | 852 | Generate and refine images, video, music, speech and audio scenes from text or reference inputs. |
| anycap-deepresearch | 814 | Run multi-source research with AI-grounded citations, web crawl and synthesis into reports. |
| anycap-ai-tool-seo | 746 | Audit and plan organic search for AI tools, SaaS and product-led sites. |
| anycap-social-meme-workflows | 723 | Create meme images, captioned photos and lightweight social visuals. |
| anycap-human-interaction | 722 | Collect structured visual feedback via annotation and collaborative whiteboards. |
| anycap-blog-production | 722 | Turn data, notes and research into AnyCap-style blog posts with evidence blocks. |
| anycap-worldcup-predict | 642 | Predict World Cup matches and scorelines backed by verifiable pre-match intel. |
| anycap-gemini-omni-video-edit | 517 | Edit short videos with Gemini Omni via natural-language instructions. |

The remaining 1 indexed listing is anycap-seedance-2 (43 installs), which has no matching directory in the current tree.

## Why This Matters for Hermes Agents

The value is breadth through one harness: a single CLI and authentication state back media generation, live web research, SEO analysis and human-feedback collection, so an agent does not stitch together separate tools per capability. Media-production and deep-research are the two most-installed skills, which reflects the split between creative asset work and research-heavy tasks.

The skills are written for agents that can run shell commands: they route natural-language requests into CLI command patterns, and the README ships llms.txt and llms-install.md so another agent can install and configure AnyCap by reading instructions rather than guessing.

Human-in-the-loop is first-class: anycap-human-interaction covers image annotation, screen recording review and Excalidraw whiteboards, which fits supervised Hermes workflows where a person approves or corrects work-in-progress before it ships.

## Usage

| You say | What happens |
|---|---|
| "Generate an image of a product mockup" | Runs anycap-media-production for image generation. |
| "Research the market and write a report" | Runs anycap-deepresearch for multi-source search and synthesis. |
| "Audit our site's AI-tool SEO" | Runs anycap-ai-tool-seo for visibility and indexing diagnosis. |
| "Turn this joke into a meme" | Runs anycap-social-meme-workflows for meme image generation. |
| "Show me the design and let me mark it up" | Runs anycap-human-interaction for annotation and whiteboard review. |
| "Write a blog post from these notes" | Runs anycap-blog-production for an AnyCap-style draft. |

## Verification

Probe the skills on the main branch before installing. All return 200:

```bash
curl -fsSL https://raw.githubusercontent.com/anycap-ai/anycap/main/skills/anycap-media-production/SKILL.md | head -12
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/anycap-ai/anycap/main/skills/anycap-deepresearch/SKILL.md
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/anycap-ai/anycap/main/skills/anycap-ai-tool-seo/SKILL.md
```

Skills live at skills/<name>/SKILL.md on main. Confirm the CLI is healthy with anycap status after login.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-17) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| anycap-media-production | Pass | Pass | Pass |
| anycap-deepresearch | Pass | Pass | Warn |
| anycap-ai-tool-seo | Pass | Pass | Warn |
| anycap-social-meme-workflows | Pass | Pass | Pass |
| anycap-human-interaction | Pass | Pass | Warn |
| anycap-blog-production | Pass | Pass | Pass |
| anycap-worldcup-predict | Pass | Pass | Warn |
| anycap-gemini-omni-video-edit | Pass | Pass | Pass |
| anycap-seedance-2 | Pass | Pass | Pass |

The sample covers all 9 indexed listings. Five pass every auditor; four skills - anycap-deepresearch, anycap-ai-tool-seo, anycap-human-interaction and anycap-worldcup-predict - carry a Snyk Warn.

## Limitations

- Snapshot data, verified 2026-11-17: 5,781 combined installs across 9 indexed listings; 51 GitHub stars; MIT; last pushed 2026-11-17. Counts drift over time.
- The index lists 9 skills but the tree holds 9 directories including anycap-cli, which has no indexed listing; anycap-seedance-2 has no matching directory in the current tree.
- anycap-seedance-2 carries installs but no SKILL.md in the tree, so its security verdict is index-level rather than file-level.
- The runtime reaches the network for live search, crawl and media generation; authenticate with anycap login before use and read the security guide before granting --allow-root.
- Model availability and input schemas change; the README says to query the CLI for current models rather than copy IDs from old examples.

## Related

- [Generative Media Skills - 153-Skill Media Production Suite Setup](/hermes/skills/catalog/generative-media-skills-setup)
- [SEO GEO Claude Skills - SEO & Generative Engine Optimization Suite Setup](/hermes/skills/catalog/seo-geo-claude-skills-setup)
- [Tavily Research - AI-Powered Deep Research Setup](/hermes/skills/catalog/tavily-research-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Give the agent llms.txt (raw.githubusercontent.com/anycap-ai/anycap/main/llms.txt) and let it install and configure AnyCap itself.
- Run anycap status after login and anycap mcp --help before wiring the MCP server.
- Query live model catalogs (anycap image models, anycap video models) instead of copying IDs from old examples.
- Keep --allow-root narrowly scoped to the media path the server must read.
- For publishable output, pair anycap-blog-production with anycap-deepresearch so the prose is backed by sourced evidence.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
