---
title: "Replicate Skills - Model Discovery and Inference"
description: "replicate/skills: 17.7K combined installs across 8 listings, skills for finding, comparing and running Replicate models plus Cog packaging and prompting."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/replicate-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-14"
tags: ["hermes skill", "agent skill", "skill setup", "replicate", "inference", "cog"]
---

# Replicate Skills - Setup Guide

**Source:** [replicate/skills](https://www.skills.sh/replicate/skills) via skills.sh - 17.7K combined installs across 8 indexed listings; first seen Nov 14, 2026 (Nov 14 evening sweep)
**GitHub:** 148 stars, Apache-2.0 license, `main` branch, last pushed 2026-06-04, seven `SKILL.md` files under `skills/`
**Category:** Model inference and packaging
**Quality Tier:** 🟢 Green - both sampled skills pass all three auditors.

Replicate's skill set covers the whole loop of using someone else's model: find it, decide between candidates, run it, and, if you are the one building it, package and publish your own. The seven skills map onto those steps rather than onto API endpoints, which is the right altitude for an agent: it asks what to run before it asks how to call it.

This is also the largest single-publisher find of this sweep by install count, and the distribution is unusually even. Every skill sits between 1,970 and 2,985 installs, which says the set is being adopted as a whole rather than through one popular entry point.

## Installation

Install the whole collection with the skills CLI:

```bash
npx skills add replicate/skills
```

The README states the skills work with any agent that supports the Agent Skills standard, including Claude Code, OpenCode, OpenAI Codex and Pi. Running a model also needs a Replicate account and an API token in the environment the agent uses.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| prompt-images | 2,985 | Prompting techniques for image generation and editing models. |
| prompt-videos | 2,765 | Prompting techniques for video generation and editing models. |
| find-models | 2,534 | Searching models, browsing collections, reading schemas and choosing the right model. |
| run-models | 2,520 | Creating predictions, polling, webhooks, streaming, file handling and concurrent runs. |
| compare-models | 2,440 | Evaluating models by cost, speed, quality and capability. |
| build-models | 2,020 | Packaging custom models with Cog: `cog.yaml`, `predict.py`, weights and local serving. |
| publish-models | 1,970 | Pushing models to Replicate with `cog push` and CI/CD releases. |

The remaining 1 indexed listing is replicate (459 installs), which has no matching skill directory in the current tree.

## Why This Matters for Hermes Agents

Model choice is where agent output quality is decided, and it is usually made by habit. `find-models` plus `compare-models` turn it into a decision with stated axes: cost, speed, quality, capability. An agent that can read a model schema before calling it also stops inventing input fields, which is the most common way an inference call fails.

The prompting skills are the part most collections omit. Image and video models respond to prompt structure, not just prompt content, and the two skills encode the structure per family. That is knowledge an agent cannot infer from an API reference.

The packaging half makes this useful beyond consumption. `build-models` and `publish-models` cover Cog, which is how a team ships its own model to Replicate with reproducible weights and a declared environment. For an agent asked to productionise a model, that is the difference between advice and a deployable artifact.

## Usage

| You say | What happens |
|---|---|
| "Find a cheap model that upscales images" | Searches models, compares cost and quality, and reports candidates with their schemas. |
| "Run this prompt on three image models and compare" | Creates predictions concurrently and reports the outputs side by side. |
| "Package our model for Replicate" | Writes `cog.yaml` and `predict.py` with the declared environment and weights. |
| "Publish this to Replicate with a release workflow" | Uses the publish skill for `cog push` and the CI/CD path. |
| "This prediction keeps timing out" | Checks the polling and webhook patterns, then the concurrency approach. |
| "Why do my video prompts look static?" | Uses the video prompting skill's structure for motion and camera language. |

## Verification

Read the run skill and confirm your token before installing:

```bash
curl -fsSL https://raw.githubusercontent.com/replicate/skills/main/skills/run-models/SKILL.md | head -20
curl -fsSL -o /dev/null -w "%{http_code}\n" https://raw.githubusercontent.com/replicate/skills/main/skills/find-models/SKILL.md
npx skills add replicate/skills --list
```

Skills sit at `skills/<name>/SKILL.md`, one directory per skill, with no nested plugin layout.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-14) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| run-models | Pass | Pass | Pass |
| prompt-images | Pass | Pass | Pass |

These skills make network calls to Replicate with your token, and predictions are billed per run. Scope the token and set a spending limit before an agent runs models unattended.

## Limitations

- Snapshot data, verified 2026-11-14: 17,693 combined installs across 8 indexed listings; 148 GitHub stars; Apache-2.0; last pushed 2026-06-04. Counts drift over time.
- The last push is more than five months before this snapshot, so model families released since then are not covered in the prompting guidance.
- Eight listings against seven `SKILL.md` files: the extra `replicate` listing has no matching skill directory in the current tree.
- Inference costs money per call, and concurrent runs multiply it. There is no built-in budget guard in the skills.
- Cog packaging assumes Docker, so local model building needs a working container runtime.
- Prompting guidance is model-family specific and will age faster than the API skills.

## Related

- [AnySearch - Real-Time Search Engine Skill](/hermes/skills/catalog/anysearch-skill-setup)
- [Text-to-Lottie - Animation Generation Setup](/hermes/skills/catalog/text-to-lottie-setup)
- [Claude Ads - Paid Media Skill Suite Setup](/hermes/skills/catalog/claude-ads-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Ask for the model schema before the first call; most failed predictions are input mismatches.
- Use `compare-models` rather than picking the most-installed model for a job.
- Set a Replicate spending limit before handing the token to an agent that runs batches.
- For video work, read `prompt-videos` first: motion and camera phrasing changes output far more than adjectives do.
- Package with Cog even for internal models; it makes the environment reproducible outside your machine.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
