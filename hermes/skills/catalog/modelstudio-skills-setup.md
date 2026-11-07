---
title: "ModelStudio Skills - Alibaba Video and Data Tools"
description: "modelstudioai/skills on skills.sh: 7.7K combined installs across 13 listings; Alibaba Model Studio docs, model picks, training and video skills."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/modelstudio-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-07"
tags: ["hermes skill", "agent skill", "skill setup", "alibaba cloud", "model studio", "video generation"]
---

# ModelStudio Skills - Setup Guide

**Source:** [modelstudioai/skills](https://www.skills.sh/modelstudioai/skills) via skills.sh - 7.7K combined installs across 13 indexed listings; first seen 2026-11-07 (Nov 7, 2026 morning sweep)
**GitHub:** 59 stars, Apache-2.0, branch `main`, last pushed 2026-11-07, 14 SKILL.md directories (`skills/<name>/SKILL.md` plus six nested reference skills under `skills/spark-video/references/`)
**Category:** Alibaba Cloud Model Studio for agents: video generation pipelines, model selection, training jobs and documentation lookup
**Quality Tier:** 🟡 Yellow - Gen Agent Trust Hub passes all five sampled skills and Socket passes four, but Snyk fails two of them and every skill drives billable Bailian API calls.

ModelStudio Skills is the official Agent Skills repository for the Aliyun Model Studio (DashScope) platform. It mixes two things in one repo: first-party skills written by the ModelStudio team (docs lookup, model recommendation, financial data, prompt studio, video pipelines) and a curated index of third-party community skills that the team says it verified before listing.

The suite is thin on prose and heavy on workflow. Each skill is a self-contained pipeline that tells the agent which `bl` CLI calls to make, in what order, and where to pause. The video skills are the most structured: `spark-video` runs a screenwriter and director pair per scene, fans out a render DAG, reviews each clip, then stitches, and it stops at four approval gates so billable generation does not run away. The docs skill is the opposite shape: a local library of model specs, pricing and API pages with a `models/index.md` entry point the agent is told to read before answering a spec question.

## Installation

The README's manual route for this repository:

```bash
npx skills add modelstudioai/skills
```

When prompted, the README says to select the skills you want and press Enter to confirm. The core `bailian-cli` skill is not in this repository. The README places it in a separate one and gives its own command:

```bash
npx skills add modelstudioai/cli --all -g
```

There is also an agent-paste block, quoted from the README:

```text
Please install Bailian AI Skills for me:
1. Check if Node.js is installed (>= 18), install it if not
2. Run: npx skills add modelstudioai/skills
3. Once installed, start with "Bailian Skills installed", then list the installed skills and what I can do
```

Three dependencies sit under the skills. Node.js 18 or newer, an Aliyun Model Studio API key (the README links the console page for it), and the `bl` CLI, which ships as the `bailian-cli` npm package with a separate binary install path documented at `bailian.aliyun.com/cli/install.md`. Any skill that generates media spends money against that Alibaba Cloud account.

## What It Provides

Six listings clear the 500-install threshold:

| Skill | Installs | Use For |
|---|---|---|
| bailian-docs-llm-wiki | 2,145 | Local Bailian documentation library: model specs and pricing, API and error codes, agents, RAG, knowledge bases, SDKs, multimodal limits and billing, entered through `models/index.md` and `wiki/index.md` |
| bailian-cli | 1,235 | The core `bl` CLI skill: chat, multimodal, image and video generation, speech, vision, apps, memory, RAG and web search. The README points this listing at `modelstudioai/cli`, so it is not a directory in this repository |
| happyhorse-prompt-studio | 1,091 | Interactive prompt studio for HappyHorse 1.0 video: scenario discovery with worked examples, then production-ready prompts in Japanese, Chinese or English |
| financial-expert | 1,080 | China and Hong Kong market data over `bl mcp`: securities, funds, bonds, indices, macro and industry series, broker research, announcements and enterprise risk |
| bailian-model-recommend | 1,049 | Model selection: takes a scenario or feature description, picks a best-fit Bailian model from the docs data and returns ready-to-run sample code |
| novel-game | 521 | Novel-to-interactive-fiction: a React SPA with branching story engine, generated portraits and cutscenes, optional TTS narration, procedural audio and save slots |

The remaining 7 indexed listings range from 1 to 418 installs.

Behind the table sits a layout quirk worth knowing before install. `bailian-train-deploy` (418 installs, in the tail) walks the data to fine-tune to export to deploy to invoke loop through `bl`, and the video work is a family rather than a single skill: `spark-video` is the orchestrator, and `spark-video-cast`, `spark-video-clip-review`, `spark-video-director`, `spark-video-screenwriter` and `spark-video-vfx-review` live as reference skills under `skills/spark-video/references/`. An install that copies only the top-level directory loses the specialists the orchestrator delegates to. `vox-video-director` (159 installs) is a separate paper-collage video pipeline that pauses at approval gates before anything billable runs.

## Why This Matters for Hermes Agents

Alibaba's model catalogue changes faster than any model's training cut-off, and the failure is specific: an agent asked for a video or speech model invents a plausible name, or quotes a context window and price from memory. The docs skill replaces that with a local mirror the agent reads first, and the model-recommend skill turns the same data into a decision with sample code attached.

The second gain is pipeline discipline. Media generation is the task class where agents most reliably burn money in a loop: retry the render, tweak the prompt, retry again. These skills encode gates and reviews instead. `spark-video` confirms at four checkpoints and reviews each clip before stitching, and `vox-video-director` pauses before billable generation. That structure is the difference between a five-dollar draft and a fifty-dollar surprise.

The third is that the skills teach a CLI rather than an SDK. Every command resolves to `bl`, so the agent is not guessing at REST payload shapes for DashScope endpoints, and a human can replay the same command by hand when something fails.

For a Hermes setup that already runs one or two Alibaba skills, this repository is the extension pack. Because each skill is independent, you can take the docs and model-selection pair without touching the video stack, which is also the cheapest way to try it: those two do not spend anything on generation.

## Usage

| You say | What happens |
|---|---|
| "Which Bailian model should handle a 30-second product video?" | `bailian-model-recommend` reads the model data shipped by the docs skill, weighs the candidates and returns a pick with sample code |
| "What does this DashScope error code mean?" | `bailian-docs-llm-wiki` looks the code up in the local raw docs layer instead of guessing from the model's memory |
| "Make a product ad from this image, one shot" | `spark-video` runs screenwriter and director per scene, fans out the render DAG, reviews each clip, then stitches, stopping at the approval gates |
| "Write a HappyHorse prompt for a manga drama in Japanese" | `happyhorse-prompt-studio` runs scenario discovery, then assembles the prompt in the language you asked for |
| "Turn this short story into a playable web game" | `novel-game` scaffolds the React SPA and generates portraits, cutscenes and optional narration through `bl image`, `bl video` and `bl speech` |
| "Fine-tune a TTS model on these clips and deploy it" | `bailian-train-deploy` validates and uploads the dataset, creates the job, waits, exports the best checkpoint and creates the inference deployment |
| "Pull revenue and ROE for these Hong Kong listed companies" | `financial-expert` queries the market MCP endpoint and returns the series with sources rather than recalled figures |

## Verification

Read the entry skill before installing. This path returned HTTP 200 on the repository's `main` branch:

```bash
curl -fsSL https://raw.githubusercontent.com/modelstudioai/skills/main/skills/bailian-docs-llm-wiki/SKILL.md | head -30
```

Its frontmatter description is written in Chinese and names the trigger set: model lists, API parameters, error codes, app development, model comparison and pricing, SDK and OpenAI-compatible endpoints, multimodal capabilities, and token billing. The same URL shape works for the other first-party skills, for example `skills/spark-video/SKILL.md` (also 200), which is where the orchestration order and the approval gates are spelled out.

After install, confirm the spark-video reference tree came across, because a copy that took only the orchestrator loses the specialists:

```bash
ls .agents/skills/spark-video/references
```

The listing should include `spark-video-cast`, `spark-video-clip-review`, `spark-video-director`, `spark-video-episode`, `spark-video-screenwriter` and `spark-video-vfx-review`. Then confirm the CLI the skills call is actually present:

```bash
command -v bl
```

If `bl` is missing, the skills will describe the right pipeline and fail at the first command. Install `bailian-cli` and set the API key before running any of them.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-07) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| bailian-docs-llm-wiki | Pass | Pass | Pass |
| financial-expert | Pass | Pass | Fail |
| bailian-train-deploy | Pass | Pass | Fail |
| spark-video-screenwriter | Pass | Pass | Pass |
| spark-video-cast | Pass | Warn | Pass |

The skill surface is markdown plus data files: `SKILL.md` bodies, reference skills, and the docs library the wiki skill reads. Nothing in the skill path runs a background service, and the commands they tell the agent to run are `bl` invocations against Alibaba endpoints.

The real exposure is billing, not code execution. These skills instruct the agent to call DashScope on your behalf, and the repository's own disclaimer says exactly that: output is billed to your Alibaba Cloud account and generated content may be inaccurate, so review before use. Keep the API key out of the workspace, and treat any skill that generates video as a spend action rather than a read action. Two sampled skills carry Snyk fails, so review those two bodies yourself before wiring them into an unattended loop.

## Limitations

- Snapshot data, verified 2026-11-07: 7,703 combined installs across 13 indexed listings; 59 GitHub stars; Apache-2.0; last pushed 2026-11-07. Counts drift over time.
- The index outruns the repository in one direction and the repository outruns the index in another. `bailian-cli` (1,235 installs) has no directory here because the README keeps the core CLI skill in `modelstudioai/cli`, while `spark-video` and `spark-video-episode` exist in the tree but are not separate indexed listings.
- Five of the thirteen indexed listings sit at 1 install each (the `spark-video` reference skills). Treat their install counts as noise, not as evidence anyone vetted them separately.
- The publish date matters more than usual. The repository was pushed on the same day as this sweep, and the skills track Alibaba model names, prices and API shapes that change on their own schedule.
- Much of the suite is written in Chinese. `bailian-docs-llm-wiki` and `bailian-train-deploy` carry Chinese frontmatter and bodies, which works for a Chinese-speaking agent but is harder to audit in an English review pass.
- Every media skill spends money. There is no dry-run mode in the skill bodies, and the approval gates depend on the agent actually stopping at them.

## Related

- [Bailian CLI - Alibaba Model Studio Agent Skills Setup](/hermes/skills/catalog/modelstudio-cli-setup)
- [QianWen AI Skills - Alibaba Qwen Multimodal Suite Setup](/hermes/skills/catalog/qianwen-ai-setup)
- [ai-video-generation - AI Video Production (196K installs)](/hermes/skills/catalog/ai-video-generation-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install the docs and model-recommend pair first. They cost nothing to run and fix the most common failure, which is an agent quoting a model spec from memory.
- Read the orchestrator before the specialists. `skills/spark-video/SKILL.md` names the order, the four gates and which reference skill handles cast, clips, review and VFX.
- Keep the API key in the environment, not in a project file. The skills shell out to `bl`, so the CLI reads the key without any skill holding it.
- Ask for the beat map before the video. Both video pipelines produce a plan or beat map first, and correcting that artifact is far cheaper than re-rendering clips.
- Check `bl --version` against the docs library when a command fails. A CLI older than the documented flags produces errors that look like model failures.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
