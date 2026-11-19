---
title: "Prompt Master - AI Prompt Engineering Skill Setup"
description: "nidhinjs/prompt-master: 4.8K combined installs across 1 listing; writes accurate prompts for any AI tool with zero wasted tokens and memory retention."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/nidhinjs-prompt-master-setup/"
robots: "index,follow"
last_updated: "2026-11-19"
tags: ["hermes skill", "agent skill", "skill setup", "prompt engineering", "ai prompts"]
---

# Prompt Master - Setup Guide

**Source:** [nidhinjs/prompt-master](https://www.skills.sh/nidhinjs/prompt-master) via skills.sh - 4.8K combined installs across 1 indexed listing; first seen Nov 19, 2026 (Nov 19, 2026 morning sweep)
**GitHub:** 16,140 stars, MIT licence, `main` branch, last pushed 2026-10-22. The skill is a single SKILL.md at the repo root, with references under references/ (patterns.md, templates.md).
**Category:** Prompt engineering
**Quality Tier:** 🟢 Green - the single sampled skill passes all three verdicts; MIT licence.

prompt-master writes production-ready prompts for any AI tool. It detects the target tool, extracts intent, applies a matching prompt architecture, and strips every word that does not change the output, so the user gets one clean copyable prompt instead of a re-prompting loop.

The README lists 20+ tool profiles (Claude, ChatGPT, Codex, Grok, Gemini, Midjourney, Stable Diffusion, ElevenLabs, Zapier, and more) and a Universal Fingerprint for tools not on the list. The skill ships a SKILL.md at the repo root plus patterns and templates references, and its frontmatter states it activates only when the user explicitly asks to write, fix, improve, or adapt a prompt.

## Installation

The recommended install is a browser upload for Claude.ai: download the repo as a ZIP, then in claude.ai go to Sidebar, Customize, Skills, and Upload a Skill. The alternative is cloning into the Claude Code skills directory:

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/nidhinjs/prompt-master.git ~/.claude/skills/prompt-master
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| prompt-master | 4,797 | Write, fix, improve, or adapt a prompt for a specific AI tool: detect the target tool, extract intent, ask up to three clarifying questions, apply a matching framework, and output one token-efficient prompt. |

The single indexed listing clears the threshold and appears in the table above.

## Why This Matters for Hermes Agents

An agent that drafts prompts for other tools faces the same failure the skill exists to fix: vague input becomes wrong output, then a re-prompt loop. prompt-master turns a rough idea into a single production-ready prompt with the target tool, intent, and constraints made explicit, so the downstream tool cannot guess wrong.

The skill routes to tool-specific profiles rather than one generic template: image tools get comma-separated descriptors and negative prompts, coding agents get file scope and stop conditions, and search tools get an explicit mode. It also carries a memory block system so prompts do not contradict decisions made earlier in a session.

For Hermes or any agent that reads skill files, the SKILL.md is directly loadable. It is prompt guidance, not a runtime dependency: nothing is installed beyond the text files.

## Usage

| You say | What happens |
|---|---|
| "Write me a prompt for Cursor to refactor my auth module" | The agent outputs a file-scoped prompt with exact paths and a do-not-touch list. |
| "Here is a bad prompt for GPT-4o, fix it" | The agent detects the target tool, extracts intent, and rewrites the prompt with wasted words stripped. |
| "Generate a Midjourney prompt for a cyberpunk city at night" | The agent outputs comma-separated descriptors with locked aspect ratio and a negative prompt. |
| "Adapt this prompt for Stable Diffusion" | The agent decompiles the prompt and rewrites it with Stable Diffusion weight syntax and CFG guidance. |
| "Build a Claude Code prompt for a landing page" | The agent asks up to three clarifying questions, then outputs a spec with sections, constraints, and done-when criteria. |

## Verification

Probe the skill on the `main` branch before installing. It returns 200:

```bash
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/nidhinjs/prompt-master/main/SKILL.md
```

After install, invoke the skill with /prompt-master or ask for a prompt naturally, then confirm the output names the target tool and drops wasted words.

## Security

skills.sh verdicts for sampled skills (verified Nov 19, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| prompt-master | Pass | Pass | Pass |

The single sampled skill passes all three verdicts; the repo ships no scripts or runtime dependencies, only Markdown.

## Limitations

- Snapshot data, verified Nov 19, 2026: 4,797 combined installs across 1 indexed listing; 16,140 GitHub stars; MIT licence; last pushed 2026-10-22. Counts drift over time.
- The SKILL.md sits at the repo root, not under skills/, so the copy pattern differs from skills-directory repos.
- The skill activates only on explicit prompt-writing requests, not general conversation or coding tasks.
- Tool profiles embed version-specific detail; for requests that depend on the latest model, the skill re-checks provider docs rather than trusting the README.

## Related

- [Useful AI Prompts - 260 Skill Prompt Library Setup](/hermes/skills/catalog/useful-ai-prompts-setup)
- [Stop Slop - AI-Prose Pattern Cleaner Setup](/hermes/skills/catalog/stop-slop-setup)
- [Avoid AI Writing - AI-Pattern Audit & Rewrite Setup](/hermes/skills/catalog/avoid-ai-writing-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Give it the target tool up front; the skill routes on tool, and guessing costs a clarifying question.
- Paste the bad prompt as-is when improving one; the skill fixes the structure rather than starting over.
- For image tools, lock aspect ratio and version in the prompt so re-rolls stay comparable.
- Keep the memory block pattern when prompts reference earlier decisions; it is the biggest fix for long sessions.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
