---
title: "AI Agent Skills - Creative and Platform Stack Setup"
description: "AI Agent Skills: 14.9K combined installs. 39 skills for OWASP security, GitHub trending, Figma, MongoDB, cloud deploys and AI video."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/ai-agents-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-24"
tags: ["hermes skill", "agent skill", "skill setup", "developer tooling", "creative stack", "cloud deploy"]
---

# AI Agent Skills - Setup Guide

**Source:** [hoodini/ai-agents-skills](https://www.skills.sh/hoodini/ai-agents-skills) via skills.sh - 14.9K combined installs across 39 indexed listings; new to this catalog in the Oct 22, 2026 sweep

**GitHub:** [hoodini/ai-agents-skills](https://github.com/hoodini/ai-agents-skills) (290 stars; no LICENSE file; pushed 2026-07-11; layout `skills/<name>/SKILL.md` on the master branch, with 37 of 39 indexed listings mapped to a skill directory)

**Category:** Developer Tooling / Creative and Platform Skills

**Quality Tier:** 🟡 Beta - no LICENSE file in the repository, 290 stars, last pushed 2026-07-11, 37 of 39 indexed listings mapped to a skill directory, and two sampled skills carry auditor warnings

This is two collections in one repository. The headline is a creative production stack, installed as a single package of 16 skills with their tooling: a film and AI-production director skill, an orchestrator that routes by intent, a design system, decks, short-form video, two landing page builders, video editing, image generation through Nano Banana Pro, Mermaid diagrams and the HyperFrames companions. The second collection is the long tail of platform and engineering skills that make up most of the 39 indexed listings: GitHub trending, OWASP secure coding, MongoDB, Figma, Google Workspace, Bun, LangChain, Vercel, Cloudflare, Railway, AWS organization and Bedrock work.

The two halves install differently, and that is the main thing to understand before copying anything out of the tree. The one-line installer gives you the 16-skill creative stack with ffmpeg, Node, Python, faster-whisper, the HyperFrames CLI, Python virtualenvs and cross-tool symlinks into `~/.copilot/skills` and `~/.agents/skills`. Every other skill in the repository is copied out directory by directory into an agent skills folder.

## Installation

```bash
# Full creative stack: 16 skills plus ffmpeg, Node, Python and HyperFrames tooling
curl -sSL https://raw.githubusercontent.com/hoodini/ai-agents-skills/master/install.sh -o install.sh
bash install.sh
```

```bash
# Or copy individual skills out of the repository
cp -r skills/langchain .claude/skills/
cp -r skills/aws-harness ~/.claude/skills/
```

Read the installer before running it. It is a shell script fetched from the network, it writes outside the project directory to `~/.copilot/skills` and `~/.agents/skills`, and it pulls language runtimes and a CLI, so it is a materially different action from copying a directory of Markdown. The project directory style install, one `cp -r` per skill, is the safer default when you only want the platform skills.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| github-trending | 3,220 | Fetches GitHub trending repositories and developers for dashboards, popular project discovery and trend tracking |
| owasp-security | 3,018 | Secure coding against the OWASP Top 10: authentication, API security, XSS, SQL injection, CSRF and security reviews |
| mongodb | 1,670 | MongoDB schema design, queries, aggregation pipelines and performance tuning, including Atlas |
| mobile-responsiveness | 1,355 | Responsive mobile-first builds: breakpoints, touch interactions, mobile navigation and viewport handling |
| google-workspace-cli | 455 | All Google Workspace APIs through the gws CLI: Drive, Gmail, Calendar, Sheets, Docs, Slides, Chat, contacts, Admin, Vault, Classroom, Apps Script and the gws MCP server |
| web-accessibility | 453 | WCAG accessibility work: ARIA patterns, keyboard navigation, screen reader support and compliance |
| figma | 449 | Figma API design automation: design tokens, React and CSS generated from components, design system sync and plugins |
| mermaid-diagrams | 406 | Flowcharts, sequence, class and entity relationship diagrams, Gantt charts and visual documentation in Mermaid syntax |
| analytics-metrics | 380 | Charts, KPI displays, metrics dashboards and data visualisation components, including Recharts |
| ux-design-systems | 270 | Design systems with tokens, component libraries, theming and dark mode |
| aws-strands | 248 | Python agents with the Strands Agents SDK: Agent, the tool decorator, BedrockModel providers, agents-as-tools, Swarm and Graph patterns, conversation management and streaming |
| bun | 190 | Bun runtime projects, Bun APIs, bundling, testing and Node.js alternatives |
| nano-banana-pro | 189 | Image generation with Gemini 3 Pro Image through the Gemini API, for professional visuals and generator features |
| honest-agent | 185 | Detects installed coding agents, adapts to each instruction file such as CLAUDE.md, copilot-instructions.md and .cursorrules, and appends rules that disable sycophancy |
| fal-ai | 175 | fal.ai serverless image, video and audio generation, editing and real-time AI features |
| vercel | 173 | Vercel deploys: Next.js apps, serverless functions, edge functions and project management |
| langchain | 169 | LangChain and LangGraph: RAG pipelines, chains, agent workflows and LLM orchestration |
| local-llm-router | 156 | Routes coding queries to local models in air-gapped networks, with Serena MCP for semantic code understanding, across Ollama, LM Studio, Jan and OpenWebUI |
| aws-agentcore | 148 | Indexed on skills.sh, but the repository tree has no skill directory or SKILL.md for it, so there is no skill text to install from this repo |
| aws-account-management | 148 | AWS Organizations, IAM policies and multi-account strategy, SSO and Identity Center, billing and Cost Explorer |
| copilot-docs | 147 | Custom GitHub Copilot instructions, including .github/copilot-instructions.md and repository-specific guidance |
| cloudflare | 144 | Cloudflare Workers, Pages, D1, R2, KV, AI inference and Durable Objects |
| copilot-sdk | 139 | Copilot SDK agentic apps: custom tools, streaming responses, sessions, MCP servers and custom agents |
| railway | 135 | Railway deploys: containerised apps, databases, private networking and project management |
| shabbat-times | 134 | Jewish calendar data and Shabbat times through the Hebcal API, including holidays, Hebrew dates and Zmanim |

The remaining 14 indexed listings range from 1 to 93 installs.

## Why This Matters for Hermes Agents

The value here is breadth per install. A single clone gives an agent working instructions for a security review, a React responsive pass, a Figma to code translation, a Cloudflare Workers deploy and a MongoDB aggregation, which is the shape of work a general engineering agent actually faces in a week. That is different from a deep single-domain suite: nothing here is a specialist, everything is a competent first pass with the right vocabulary and triggers.

`honest-agent` is the one skill in the set that changes how the agent behaves rather than what it knows. It scans for the instruction files the major coding agents read, adapts the output format to each one, and appends directives that disable sycophancy and enable pushback. For a Hermes setup that already has its own operating protocol, the correct use is to read what it writes and merge the parts you want, not to let it append to files blindly.

The creative stack is where the repository puts its effort, and the pyramid design is the useful part: an orchestrator routes intent to decks, design system, viral video, video edit or landing page skills, so a user says "make a deck about this" and does not need to know which of sixteen skills is the entry point. That routing convention is worth copying even if you never install the stack.

## Usage

| You say | What happens |
|---|---|
| "Build me a deck about this topic" | The creative stack routes to the decks skill with the design system in decks mode |
| "Turn this video into a landing page" | The parallax or sticky hero landing skill, depending on clip length |
| "Review this handler for injection risk" | `owasp-security` walks the OWASP Top 10 checks and returns the fix |
| "Generate a responsive mobile layout" | `mobile-responsiveness` returns breakpoints, touch targets and mobile navigation |
| "Pull the design tokens from this Figma file" | `figma` extracts tokens and can generate React or CSS from the components |
| "Deploy this to Vercel" | `vercel` returns the project configuration, function setup and deploy steps |
| "Stop agreeing with everything I say" | `honest-agent` appends anti-sycophancy directives to the detected agent instruction files |
| "Which AWS accounts are costing the most?" | `aws-account-management` works the Organizations, billing and Cost Explorer side |

## Verification

The branch is `master`, not `main`, so a `main` URL for this repository will 404. Read a skill before installing it:

```bash
curl -s https://raw.githubusercontent.com/hoodini/ai-agents-skills/master/skills/github-trending/SKILL.md | head -40
curl -s https://raw.githubusercontent.com/hoodini/ai-agents-skills/master/skills/owasp-security/SKILL.md | head -40
curl -s https://raw.githubusercontent.com/hoodini/ai-agents-skills/master/skills/mongodb/SKILL.md | head -40
```

Read the installer before running it, since it is the step that writes outside the project:

```bash
curl -s https://raw.githubusercontent.com/hoodini/ai-agents-skills/master/install.sh | head -40
```

Two listings will not resolve, and that is a gap in the repository rather than a local mistake: `aws-agentcore` and `skill-name` are indexed on skills.sh but have no skill directory or SKILL.md in the current tree, so a copy command for either will fail.

## Security

skills.sh verdicts for sampled skills (verified Oct 22, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| github-trending | Pass | Pass | Warn |
| owasp-security | Pass | Pass | Pass |
| mongodb | Pass | Pass | Pass |
| mobile-responsiveness | Pass | Pass | Pass |
| google-workspace-cli | Pass | Warn | Warn |

Two of the five sampled skills carry warnings, which is what the tier line means. `github-trending` takes a Snyk MEDIUM W011, indirect prompt injection risk, because repository names, descriptions and author text fetched from a third party reach the model. `google-workspace-cli` takes the same W011 from Snyk plus a Socket warning on the same path, and it is also the highest-privilege skill here: gws reaches Drive, Gmail, Calendar, Admin, Vault eDiscovery and Classroom, so the OAuth scope it is granted is the real blast radius, not the skill text.

Three things matter more than the verdict table. First, there is no LICENSE file in the repository, so the default is all rights reserved: the code is public to read and not clearly licensed to redistribute, which is a question for anything you plan to vendor or resell. Second, the installer is a network-fetched shell script that installs runtimes and symlinks skills into `~/.copilot/skills` and `~/.agents/skills`, so pin it, read it, or skip it. Third, `honest-agent` writes to agent instruction files, so point it at a scratch project the first time and diff the result before letting it near a home directory config.

## Limitations

- There is no LICENSE file, so the legal terms for reuse are unspecified while the repository remains public.
- 290 stars and a last push of 2026-07-11 make this a quieter project than its install count suggests, so expect less maintenance than the numbers imply.
- Two of the 39 indexed listings, `aws-agentcore` and `skill-name`, have no counterpart in the current tree, so 37 map to a skill directory.
- The installer covers 16 skills, not 39. Everything outside the creative stack is a manual copy, and there is no single command that installs the platform skills.
- The skills are breadth-first. `owasp-security`, `web-accessibility` and `mobile-responsiveness` are checklists and vocabulary for a first pass, not substitutes for a specialist review.
- `google-workspace-cli` needs OAuth credentials with broad Google scopes, which is a heavier permission decision than the rest of the suite combined.
- Snapshot data, verified October 22, 2026: 14854 combined installs across 39 indexed listings; 290 GitHub stars; no LICENSE file; last pushed 2026-07-11. Counts drift over time.

## Related

- [remotion-best-practices - Video Production Setup](/hermes/skills/catalog/remotion-best-practices-setup)
- [Garden Skills - ConardLi's Web Video & Design Suite Setup](/hermes/skills/catalog/garden-skills-setup)
- [Skills Collective AI Media - Image & Video Gen Setup](/hermes/skills/catalog/skills-collective-ai-media-setup)
- [AccessLint Skills - WCAG 2.2 Accessibility Audit Suite Setup](/hermes/skills/catalog/accesslint-skills-setup)

## Pro Tips

- Start with the `cp -r` route for one skill, `owasp-security` or `mongodb`, and see whether the trigger phrasing actually fires in your agent before committing to the 16-skill installer.
- Read `install.sh` end to end. It is short, it writes to two home directory paths, and knowing exactly what it symlinks prevents the classic "why did my agent change behavior" afternoon.
- Treat `honest-agent` as a diff, not a patch. Run it in a scratch repo, read the appended rules, then copy the lines you agree with into your own instruction file by hand.
- Use `github-trending` as a data skill rather than a browsing habit: the description is about dashboards and trend tracking, so ask for the repositories as a table you can store, not a one-off look at the trending page.
- Give `google-workspace-cli` its own OAuth client with the narrowest scopes that satisfy the task. It is the one skill in the set where a mistake reaches real mail, calendars and admin surfaces.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
