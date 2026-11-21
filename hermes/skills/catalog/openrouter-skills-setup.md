---
title: "OpenRouter Skills - Model Routing and Agent Tooling"
description: "openrouterteam/skills: 19 OpenRouter API skills for model routing, benchmarks, OAuth and multimodal generation - 7.3K combined installs."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/openrouter-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-21"
tags: ["hermes skill", "agent skill", "skill setup", "llm api", "model routing", "openrouter"]
---

# OpenRouter Skills - Model Routing and Agent Tooling

**Source:** [openrouterteam/skills](https://www.skills.sh/openrouterteam/skills) via skills.sh - 7.3K combined installs across 19 indexed listings; first seen Nov 21, 2026 (Nov 21, 2026 morning sweep)
**GitHub:** [OpenRouterTeam/skills](https://github.com/OpenRouterTeam/skills) - 327 stars, no LICENSE file, main branch, last pushed Nov 20, 2026; skills live under `skills/<name>/SKILL.md` with one top-level `open-responses/SKILL.md`, plus Claude Code and Cursor plugin manifests.
**Category:** LLM API and Model Routing
**Quality Tier:** 🟠 Orange - 19 of 19 skills sampled; 2 Fail cells (install-ori-harness Snyk, spawn-ori-eval Snyk) and 6 Warn cells.

OpenRouter Skills is the official skill set for building on OpenRouter, a unified API in front of 600+ AI models. It covers model discovery and comparison, benchmark-backed selection, the Open Responses multi-provider standard, image and video generation, text-to-speech and speech-to-text, usage analytics, OAuth sign-in, and two project scaffolding skills. It carries 7.3K combined installs across 19 indexed listings and 327 GitHub stars, first seen in the Nov 21, 2026 morning sweep.

All scripts key off a single OPENROUTER_API_KEY environment variable, so one key unlocks the whole suite. The scaffolding skills deserve note: create-agent-tui and create-headless-agent generate complete TypeScript agents rather than describing one, with built-in tools, session persistence and tests. The repo ships no LICENSE file, so treat it as source-available with unstated terms.

## Installation

For agents that support plugins, install via the native plugin system so skills auto-update:

```text
/plugin marketplace add OpenRouterTeam/skills
/plugin install openrouter@openrouter
```

In Cursor, add the repo under Settings, Rules, Add Rule, Remote Rule (Github) with `OpenRouterTeam/skills`. For OpenCode, clone and copy the skills into the skills directory:

```bash
git clone https://github.com/OpenRouterTeam/skills.git /tmp/openrouter-skills
cp -r /tmp/openrouter-skills/skills/* ~/.config/opencode/skills/
rm -rf /tmp/openrouter-skills
```

The GitHub CLI path works across Claude Code, Cursor, OpenCode, Codex, Gemini CLI and Windsurf, and requires GitHub CLI v2.90.0 or later:

```bash
gh skill install OpenRouterTeam/skills                       # install all
gh skill install OpenRouterTeam/skills openrouter-images      # single skill
gh skill install OpenRouterTeam/skills openrouter-images --scope user
```

Set the API key before running any skill:

```bash
export OPENROUTER_API_KEY=your_key
```

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| openrouter-models | 1,009 | listing, searching, filtering and comparing models, pricing and provider performance |
| openrouter-images | 577 | generating images from text prompts and editing existing images |
| openrouter-typescript-sdk | 532 | integrating 300+ models through the TypeScript SDK and Agent packages |
| openrouter-benchmarks | 402 | querying benchmark rankings from Artificial Analysis and Design Arena |
| open-responses | 388 | implementing and debugging the Open Responses multi-provider LLM API |
| openrouter-video | 385 | generating video from prompts with an async submit, poll and download flow |
| openrouter-analytics | 383 | answering questions about spend, request volume, models, latency and tokens |
| openrouter-generations | 381 | inspecting a generation's cost, latency, routing and stored content |
| openrouter-agent-migration | 380 | migrating from @openrouter/sdk to @openrouter/agent |
| openrouter-oauth | 360 | adding Sign In with OpenRouter via OAuth PKCE, no SDK or client registration |
| create-agent-tui | 355 | scaffolding a TypeScript terminal agent TUI with @openrouter/agent |
| openrouter-analytics-schema | 353 | discovering analytics metrics, dimensions and filter operators |
| openrouter-analytics-query | 353 | constructing and running analytics queries against the API |
| openrouter-tts | 324 | synthesizing speech from text via the text-to-speech API |

The remaining 5 indexed listings range from 94 to 317 installs.

## Why This Matters for Hermes Agents

OpenRouter is one API in front of 600+ models, which makes model selection and routing the hard part of building on it. These skills turn that into a procedure: openrouter-models searches, filters and compares models, and openrouter-benchmarks pulls rankings from Artificial Analysis and Design Arena, so the agent picks a model on evidence rather than habit. The OAuth skill is notable because it needs no SDK or client registration, which keeps a sign-in flow small enough to reason about.

For a Hermes agent, the suite covers the full surface of the API: model routing, usage analytics, individual generation inspection, images, video, text-to-speech, speech-to-text, and the Open Responses multi-provider standard. The create-agent-tui and create-headless-agent skills scaffold whole TypeScript agents, so an agent can generate a working starter project rather than describe one. Everything keys off a single OPENROUTER_API_KEY environment variable, so one credential controls the entire surface.

## Usage

| You say | What happens |
|---|---|
| Which model should I use for this app? | Runs openrouter-models with openrouter-benchmarks to compare pricing and benchmark rankings |
| Add OpenRouter login to my app | Runs openrouter-oauth to produce a PKCE sign-in module with no SDK |
| Generate an image of a red panda in a coffee shop | Runs openrouter-images against the image generation API |
| Transcribe this meeting recording | Runs openrouter-stt against the speech-to-text API |
| How much did I spend on models last week? | Runs openrouter-analytics to answer from usage data |
| Scaffold me a terminal agent | Runs create-agent-tui to generate a TypeScript TUI project |
| Migrate my code off @openrouter/sdk | Runs openrouter-agent-migration to rewrite callModel and tool() calls |

## Verification

Review a skill's instructions before installing, and confirm the file resolves on the main branch:

```bash
curl -sL https://raw.githubusercontent.com/OpenRouterTeam/skills/main/skills/openrouter-models/SKILL.md | head -40
```

Confirm the key is set, then run one read-only call first, such as listing models, before letting the agent execute anything that spends against the account.

## Security

skills.sh verdicts for sampled skills (verified Nov 21, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| openrouter-models | Pass | Pass | Warn |
| openrouter-images | Pass | Pass | Pass |
| openrouter-typescript-sdk | Warn | Pass | Pass |
| openrouter-benchmarks | Pass | Pass | Pass |
| open-responses | Pass | Pass | Pass |
| openrouter-video | Pass | Pass | Pass |
| openrouter-analytics | Pass | Pass | Warn |
| openrouter-generations | Pass | Pass | Pass |
| openrouter-agent-migration | Pass | Pass | Pass |
| openrouter-oauth | Pass | Pass | Pass |
| create-agent-tui | Pass | Warn | Pass |
| openrouter-analytics-schema | Pass | Pass | Pass |
| openrouter-analytics-query | Pass | Pass | Pass |
| openrouter-tts | Pass | Pass | Pass |
| openrouter-stt | Pass | Pass | Pass |
| create-headless-agent | Pass | Warn | Warn |
| install-ori-harness | Pass | Pass | Fail |
| spawn-ori-eval | Pass | Warn | Fail |
| openrouter-decisions | Pass | Pass | Pass |

The install-ori-harness and spawn-ori-eval skills carry Snyk Fail cells, so review them before use.

## Limitations

- Snapshot data, verified Nov 21, 2026: 7,321 combined installs across 19 indexed listings; 327 GitHub stars; no LICENSE file; last pushed Nov 20, 2026. Counts drift over time.
- The repo ships no LICENSE file, so treat it as source-available with unstated terms rather than under an OSI license.
- Two skills carry Snyk Fail cells (install-ori-harness and spawn-ori-eval), and the two scaffolding skills carry Socket Warn cells (create-agent-tui and create-headless-agent); review them before use.
- The install index and the tree agree at 19 listings, but open-responses lives at the repo root while the other 18 live under skills/.
- Every script keys off one OPENROUTER_API_KEY, so any skill can spend against the same account; scope keys before letting an agent roam.

## Related

- [Replicate Skills - Model Discovery and Inference](/hermes/skills/catalog/replicate-skills-setup)
- [Llm Ops Setup](/hermes/skills/catalog/llm-ops-setup)
- [Awesome LLM Apps Skills - Role-Based Agent Skills Setup](/hermes/skills/catalog/awesome-llm-apps-skills-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Set OPENROUTER_API_KEY once and scope it; every script in the suite reads it.
- Use openrouter-models together with openrouter-benchmarks so selection decisions carry benchmark evidence, not just pricing.
- Try create-agent-tui to scaffold a starter before hand-writing a terminal agent.
- Pin single-skill installs with `gh skill install OpenRouterTeam/skills <name> --scope user` for cross-project reuse.
- Review install-ori-harness and spawn-ori-eval before use; they carry Snyk Fail cells in this snapshot.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
