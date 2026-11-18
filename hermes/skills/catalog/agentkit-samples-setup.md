---
title: "AgentKit Samples - Volcengine AgentKit Suite Setup"
description: "bytedance/agentkit-samples: 6.4K combined installs across 96 listings; ByteDance's Volcengine AgentKit and VeADK sample suite."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/agentkit-samples-setup/"
robots: "index,follow"
last_updated: "2026-11-18"
tags: ["hermes skill", "agent skill", "skill setup", "volcengine", "agentkit", "media generation"]
---

# AgentKit Samples - Setup Guide

**Source:** [bytedance/agentkit-samples](https://www.skills.sh/bytedance/agentkit-samples) via skills.sh - 6.4K combined installs across 96 indexed listings; first seen Nov 18, 2026 (this sweep)
**GitHub:** 492 stars, Apache-2.0 license, `main` branch, last pushed 2026-11-18. Skills live under `skills/`, with a few AgentKit examples under `skills/agentkit/`, and runnable Python sample agents under `python/`.
**Category:** Volcengine AgentKit samples and media skills
**Quality Tier:** 🟠 Orange - 46 Pass, 12 Warn and 2 Fail across the 60 sampled verdict cells; Apache-2.0 licence.

AgentKit Samples is ByteDance's official sample suite for the Volcengine AgentKit platform with VeADK. The repository mixes installable skills with runnable Python agents: most skills wrap Volcengine model endpoints such as Doubao text to speech, Seedream image generation, Seedance video generation, and the Imagination music API, so the model calls run on Volcengine infrastructure rather than locally.

The README and most skill descriptions are written in Chinese, and this guide translates them. Skills are listed on skills.sh under the bytedance publisher, while the repository itself is a code workshop of tutorials and use cases aimed at getting an agent running on AgentKit.

## Installation

The README requires Python 3.10 or newer, plus the VeADK and AgentKit SDK Python libraries. Docker is optional for local container builds.

```bash
python --version
pip install veadk-python agentkit-sdk-python
```

To run the sample agents, clone the repository and enter a tutorial or use case:

```bash
git clone https://github.com/bytedance/agentkit-samples.git
cd agentkit-samples
```

Tutorials live under `python/01-tutorials/` and use cases under `python/02-use-cases/`; each is a complete example that shows how to assemble AgentKit components.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| byted-web-search | 627 | Web search via the Volcengine search API, returning web and image results for questions that depend on current facts. |
| byted-seedream-image-generate | 304 | Generate high-quality images from text prompts using Volcengine Seedream models across styles and aspect ratios. |
| byted-las-video-edit | 212 | Smart video editing that pulls clips from long videos using a natural language description of the segment to keep. |
| byted-text-to-speech | 190 | Text to speech via the Volcengine Doubao TTS API with streaming, multiple voices, and speed and pitch controls. |
| byted-seedance-video-generate | 188 | Generate videos from text prompts, images, or reference material using Seedance models. |
| byted-las-pdf-parse-doubao | 167 | Parse PDFs and scans into structured Markdown or text with table and multi-column layout support. |
| byted-data-search | 141 | Industry data query and analysis across compliant public data sources with exact match, fuzzy search, and aggregation. |
| byted-las-vlm-video | 128 | Multimodal video understanding that generates descriptions, summaries, and tags and answers questions about video content. |
| code-optimization | 110 | Optimize code performance through iterative improvements with execution time and memory benchmarks. |
| byted-music-generate | 101 | Generate music with the Volcengine Imagination API, covering vocal songs, instrumental BGM, and lyrics. |
| byted-marketing-agent-inspiration-insight | 100 | Find creative inspiration, viral video storyboards, and reusable prompts; manually triggered with /inspiration. |

The remaining 85 indexed listings range from 28 to 98 installs.

## Why This Matters for Hermes Agents

AgentKit Samples is the fastest path to ByteDance's hosted model catalogue from inside a Hermes agent. Instead of wiring Volcengine SDKs by hand, each skill exposes one capability (search, image, video, speech, music, data) as a promptable action, so an agent can compose several Volcengine endpoints in a single task without leaving its own skill harness.

The samples half of the repository shows how the same capabilities assemble into full agents with VeADK: the tutorials and use cases cover memory, RAG over VikingDB, MCP tool calls, multi-agent collaboration, and A2A communication. The skills are the individual tools; the Python samples are the worked examples that combine them.

## Usage

| You say | What happens |
|---|---|
| "Search for the latest on this topic" | byted-web-search returns web and image results from the Volcengine search API. |
| "Generate an image of a red panda in watercolor style" | byted-seedream-image-generate produces an image from the text prompt via Seedream. |
| "Turn this article into spoken audio" | byted-text-to-speech synthesizes speech with the Volcengine Doubao TTS API. |
| "Make a short video from these reference images" | byted-seedance-video-generate creates video from text, images, or reference material. |
| "Pull the tables out of this PDF" | byted-las-pdf-parse-doubao converts the PDF into structured Markdown or text. |
| "Speed up this Python function" | code-optimization benchmarks and iteratively improves the code over up to two rounds. |

## Verification

Confirm the two required Python libraries installed, then probe one skill file on the `main` branch. The skill file returns HTTP 200:

```bash
pip show veadk-python agentkit-sdk-python
curl -fsSL https://raw.githubusercontent.com/bytedance/agentkit-samples/main/skills/byted-web-search/SKILL.md | head -12
```

## Security

skills.sh verdicts for sampled skills (verified Nov 18, 2026) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| byted-web-search | Pass | Pass | Fail |
| byted-seedream-image-generate | Pass | Warn | Pass |
| byted-las-video-edit | Pass | Pass | Pass |
| byted-text-to-speech | Pass | Pass | Pass |
| byted-seedance-video-generate | Pass | Pass | Pass |
| byted-las-pdf-parse-doubao | Pass | Pass | Warn |
| byted-data-search | Pass | Pass | Pass |
| byted-las-vlm-video | Pass | Pass | Pass |
| code-optimization | Pass | Pass | Pass |
| byted-music-generate | Pass | Pass | Pass |
| byted-marketing-agent-inspiration-insight | Pass | Pass | Warn |
| byted-voice-to-text | Pass | Pass | Warn |
| byted-las-asr-pro | Pass | Pass | Pass |
| byted-marketing-agent-trending-list | Pass | Warn | Pass |
| image-video-gen | Pass | Pass | Warn |
| byted-security-clawsentry | Pass | Warn | Fail |
| byted-skillhub-download | Pass | Warn | Pass |
| tos-file-access | Warn | Warn | Warn |
| veadk-skills | Warn | Pass | Pass |
| volcengine-rds-mysql | Pass | Pass | Pass |

The sample covers 20 of the 96 indexed listings. The two Fail cells are Snyk flags on byted-web-search and byted-security-clawsentry, and tos-file-access is flagged Warn by all three scanners. Many skills send prompts and files to Volcengine-hosted model endpoints, so review what each skill transmits before using it with sensitive data.

## Limitations

- Snapshot data, verified Nov 18, 2026: 6,363 combined installs across 96 indexed listings; 492 GitHub stars; Apache-2.0; last pushed 2026-11-18. Counts drift over time.
- The README and most skill descriptions are written in Chinese; this guide translates them, and working in the repository means reading Chinese SKILL.md files and docs.
- Many skills wrap Volcengine-hosted model endpoints (Doubao TTS, Seedream, Seedance, Imagination music), so they need a Volcengine account and API credentials and send your prompts to Volcengine infrastructure rather than running on-device.
- The skills shown above carry most of the install volume; the remaining listings form a long tail of lower-install skills.

## Related

- [OpenAI Codex Skills - Official Skills Catalog Setup](/hermes/skills/catalog/openai-codex-skills-setup)
- [Claude Code Skills - Agentic Coding & Skill Development Setup](/hermes/skills/catalog/claude-code-skills-setup)
- [Eachlabs Skills - Creative Generation Setup](/hermes/skills/catalog/eachlabs-skills-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with byted-web-search for any answer that depends on current facts; the skill is designed to prefer itself for online-search scenarios.
- Group the byted-las-* skills together: video edit, PDF parse, and VLM video are one media-processing family that shares the same LAS CLI version metadata.
- Expect "Complete terms in LICENSE" in the frontmatter of byted-text-to-speech and byted-music-generate rather than Apache-2.0, so check each skill's license field before redistribution.
- Install veadk-python and agentkit-sdk-python before expecting the sample agents under `python/` to run.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
