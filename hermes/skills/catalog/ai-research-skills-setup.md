---
title: "AI Research Skills - 100-Skill ML Research Library Setup"
description: "orchestra-research/ai-research-skills: 97.0K combined installs. 98 atomic ML research skills plus an autoresearch orchestrator, ideation to paper."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/ai-research-skills-setup/"
robots: "index,follow"
last_updated: "2026-10-29"
tags: ["hermes skill", "agent skill", "skill setup", "ml research", "fine-tuning", "model serving"]
---

# AI Research Skills - Setup Guide

**Source:** [orchestra-research/ai-research-skills](https://www.skills.sh/orchestra-research/ai-research-skills) via skills.sh - 97.0K combined installs across 100 indexed listings; first seen 2026-10-29 (evening sweep)

**GitHub:** [orchestra-research/ai-research-skills](https://github.com/orchestra-research/ai-research-skills) - 14,111 stars, MIT License, branch main, last commit 2026-06-15; 98 skill directories laid out as `NN-topic/<skill>/SKILL.md`, for example `20-ml-paper-writing/ml-paper-writing/SKILL.md`, `12-inference-serving/vllm/SKILL.md` and `0-autoresearch-skill/SKILL.md`, with 267 files under per-skill `references/` folders and 60 more under `templates/`

**Category:** ML and AI research engineering, from ideation and fine-tuning through evaluation, serving and paper writing

**Quality Tier:** 🟡 Beta - Orchestra Research's library, MIT licensed, 14,111 stars and 98 in-tree skill directories, but one Socket Warn on the sampled `ml-paper-writing` listing and a last commit of June 2026

AI Research Skills is Orchestra Research's library of atomic, tool-specific skills for machine learning work, positioned in its README as the layer that lets an agent run a research project from literature survey to submitted paper. It is not one skill. It is 98 directories across 23 category folders, each holding a `SKILL.md` plus optional reference and template files, and the set covers the practical surface of ML engineering: model architecture, tokenization, fine-tuning, post-training and RL, distributed training, quantization, inference serving, evaluation, safety, agents, RAG, multimodal, MLOps and observability.

Two things make the package more than a prompt dump. The first is the `autoresearch` skill in `0-autoresearch-skill/`, a two-loop orchestrator that runs fast experiment iterations inside an outer loop that synthesizes results and picks the next direction, routing into the domain skills as each step needs them. The second is the naming discipline: every `SKILL.md` opens with a frontmatter block carrying a `name`, a trigger-shaped `description`, `tags` and an explicit `dependencies` list, so an agent can decide whether to load a skill, and a human can see what a skill will install, before anything runs.

## Installation

The README's recommended path is the interactive installer, which detects installed coding agents and offers everything, a quickstart bundle, a category, or individual skills:

```bash
npx @orchestra-research/ai-research-skills
```

The non-interactive form, documented in `WELCOME.md`, installs the whole library in one shot:

```bash
npx @orchestra-research/ai-research-skills install --all
```

Direct commands from the README:

```bash
npx @orchestra-research/ai-research-skills list
npx @orchestra-research/ai-research-skills update
```

The installer clones the repository once into a temp directory, keeps the canonical copy in `~/.orchestra/skills`, records state in `~/.orchestra/.lock.json`, and then symlinks each skill into every agent directory it detected. Hermes Agent is a supported target: `src/agents.js` registers it under the id `hermes` with config directory `~/.hermes` and skills directory `skills`. Two caveats worth knowing before you run it. First, `--local` (or `-l`) installs into the current project instead, writing a `.orchestra-skills.json` lock into the repository root, which is the better fit if you want the skills versioned with a project. Second, the positional argument the CLI calls `skill` is matched against category ids and names in `src/prompts.js`, not against individual skill names, so `npx @orchestra-research/ai-research-skills 12-inference-serving` installs that whole category. `WELCOME.md` notes that a restart of the agent session is usually needed before newly installed skills are recognized.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| ml-paper-writing | 2,363 | Drafting publication-ready ML papers for NeurIPS, ICML, ICLR, ACL, AAAI and COLM: structuring the argument, verifying citations against Semantic Scholar and arXiv, and preparing camera-ready LaTeX from a research repo. |
| brainstorming-research-ideas | 1,249 | Structured ideation frameworks for finding high-impact directions, pivoting between projects, or getting a novel angle on existing work before any compute is spent. |
| academic-plotting | 1,217 | Publication figures for a paper: architecture diagrams generated from a section description, and data-driven charts where the skill picks the chart type and renders matplotlib or seaborn output. |
| creative-thinking-for-research | 1,212 | Cognitive-science framing for genuinely new directions: combinatorial creativity, analogical reasoning and constraint manipulation applied to CS and AI problems. |
| mlflow | 1,078 | Experiment tracking, model registry with versioning, and framework-agnostic deployment across PyTorch, TensorFlow, scikit-learn and HuggingFace runs. |
| serving-llms-vllm | 1,076 | Production LLM serving with PagedAttention and continuous batching, OpenAI-compatible endpoints, tensor parallelism and GPTQ, AWQ or FP8 quantized weights. |
| faiss | 1,062 | Billion-scale similarity search and clustering of dense vectors with Flat, IVF and HNSW index types, CPU or GPU, when you want retrieval without a metadata layer. |
| tensorrt-llm | 1,053 | Maximum-throughput NVIDIA inference on A100 and H100: FP8 and INT4 quantization, in-flight batching and multi-GPU scaling for a latency-critical endpoint. |
| stable-diffusion-image-generation | 1,047 | Text-to-image generation through HuggingFace Diffusers, including image-to-image translation, inpainting and custom diffusion pipelines. |
| peft-fine-tuning | 1,023 | LoRA, QLoRA and 25-plus parameter-efficient methods for tuning 7B to 70B models on one or two GPUs, training under one percent of parameters, and serving multiple adapters. |
| autoresearch | 1,019 | The orchestration layer: a two-loop loop that runs experiment iterations, synthesizes results, steers direction, routes to domain skills, and drives a project through to a paper. |
| audiocraft-audio-generation | 1,008 | Audio generation with MusicGen and AudioGen: text-to-music, text-to-sound effects, and melody-conditioned generation from a reference clip. |
| ray-train | 1,007 | Distributed training orchestration from laptop to thousands of nodes, with Ray Tune hyperparameter sweeps, fault tolerance and elastic scaling across PyTorch, TensorFlow and HuggingFace. |
| gguf-quantization | 1,006 | GGUF conversion and llama.cpp quantized inference in the 2-bit to 8-bit range for consumer GPUs, Apple Silicon or CPU-only hosts. |
| weights-and-biases | 1,006 | Experiment tracking with automatic logging, real-time training curves, hyperparameter sweeps and a model registry across framework boundaries. |
| segment-anything-model | 1,002 | Zero-shot image segmentation prompted by points, boxes or masks, including automatic generation of every object mask in an image. |

The remaining 84 indexed listings range from 2 to 999 installs.

## Why This Matters for Hermes Agents

Most skill libraries fail on routing, not on content: the agent has a hundred files and no way to know which one applies. This one is built around a name plus trigger-shaped description pair in every frontmatter, so a loader can match on intent before spending context on a full body. The `description` fields are unusually specific about when to fire and when not to, and more than one names its neighbour explicitly, which gives you a cheap first pass for a retrieval or keyword filter over the installed set.

The `autoresearch` skill is the part that changes agent behaviour rather than just informing it. It keeps structured project state, runs an inner experiment loop against a stated optimization target, and uses an outer loop to synthesize results and redirect. That division is what stops a long research session from degenerating into an agent that retrains the same model with slightly different seeds. It also gives Hermes a place to hang a heartbeat or cron: the skill is written to be invoked repeatedly rather than in one pass.

Progressive disclosure is the other design choice worth copying. Skill bodies average about 13 KB, with details pushed into 327 files under `references/` and `templates/`, so the marginal cost of having the library installed is a name and a description per skill, and the cost of loading one is bounded by the skill you actually needed. Total on-disk size of the 98 skill files is about 1.28 MB, which is small for a library of this scope.

Finally, the dependency lists are honest. `ml-paper-writing` declares `semanticscholar`, `arxiv`, `habanero` and `requests`; `tensorrt-llm` declares `tensorrt-llm` and `torch`; `gguf-quantization` declares `llama-cpp-python`. Those fields are a machine-readable statement of what a skill expects to find on the host, which is exactly the signal a Hermes operator needs before granting a skill permission to run anything.

## Usage

| You say | What happens |
|---|---|
| "Draft a NeurIPS paper from this training repo" | `ml-paper-writing` structures the paper section by section, pulls related work through Semantic Scholar and arXiv and checks each citation, then produces camera-ready LaTeX, falling back to `academic-plotting` for the figures. |
| "Write the paper for a systems venue instead" | The skill routes to `systems-paper-writing` for OSDI, NSDI, ASPLOS and SOSP conventions, which the ML-paper skill explicitly declines to cover. |
| "Run this research question end to end overnight" | `autoresearch` bootstraps literature, sets up continuous operation, runs the experiment loop, synthesizes results and writes the paper, calling domain skills as each stage needs them. |
| "Fine-tune a 13B model on two A100s without blowing memory" | `peft-fine-tuning` sets up LoRA or QLoRA with bitsandbytes, and `deepspeed` or `pytorch-fsdp2` takes over sharding if the model needs more than one GPU. |
| "Serve this checkpoint at high throughput" | `serving-llms-vllm` stands up an OpenAI-compatible vLLM endpoint with continuous batching; `tensorrt-llm` is the lower-latency alternative when the host is H100 and quantization is acceptable. |
| "Quantize the model so it runs on a laptop" | `gguf-quantization` converts to GGUF and picks a 2-bit to 8-bit level for llama.cpp, or `awq-quantization` and `gptq` handle GPU-side weight-only quantization. |
| "Track these runs and compare them" | `weights-and-biases` or `mlflow` logs the sweep, renders the curves, and records the artifacts so a later session can reproduce the comparison. |

## Verification

The three raw paths cited here returned 200 on branch main when the guide was written on 2026-10-29:

```bash
for p in 20-ml-paper-writing/ml-paper-writing/SKILL.md \
         0-autoresearch-skill/SKILL.md \
         12-inference-serving/vllm/SKILL.md; do
  curl -sL -o /dev/null -w "%{http_code} $p\n" \
    "https://raw.githubusercontent.com/orchestra-research/ai-research-skills/main/$p"
done
```

Expect `200 20-ml-paper-writing/ml-paper-writing/SKILL.md`, `200 0-autoresearch-skill/SKILL.md` and `200 12-inference-serving/vllm/SKILL.md`.

Review a skill before installing it by reading its frontmatter, which is where the trigger and the dependency exposure are declared:

```bash
curl -sL https://raw.githubusercontent.com/orchestra-research/ai-research-skills/main/20-ml-paper-writing/ml-paper-writing/SKILL.md | head -20
```

Read three fields and stop. `description` tells you when the skill fires, so you can tell whether it will hijack tasks you meant to handle yourself. `dependencies` tells you what it expects installed, and whether that is a pip install on a GPU host or a network service. `version` and `author` tell you who owns the maintenance, which for a 98-skill library matters more than for a single-purpose skill.

After install, confirm what landed:

```bash
ls ~/.orchestra/skills
npx @orchestra-research/ai-research-skills list
```

The canonical copy lives in `~/.orchestra/skills/<category>/<skill>/`, with `~/.orchestra/.lock.json` recording what the installer put there. The `list` command prints the skills it believes are installed per detected agent, which is the fastest way to spot a symlink that never got created.

## Security

skills.sh verdicts for sampled skills (verified 2026-10-29) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| ml-paper-writing | Pass | Warn | Pass |
| brainstorming-research-ideas | Pass | Pass | Pass |
| academic-plotting | Pass | Pass | Pass |
| creative-thinking-for-research | Pass | Pass | Pass |
| mlflow | Pass | Pass | Pass |
| pytorch-fsdp | no verdict table rendered | n/a | n/a |

No sampled listing fails. The one socket Warn sits on `ml-paper-writing`, the most installed skill in the library, and the pack does not include the finding text behind it, so this guide will not guess at the rule. In practice a Socket Warn on a writing skill means the review flagged something in the packaging rather than in a live runtime path, and the same skill passes both other auditors, but the honest read is that you should open the skills.sh security page for `ml-paper-writing` and read the finding before installing it into an agent that holds repository write access.

The larger risk here is structural, not per-skill. This is a library whose value is that an agent may invoke any of 98 skills on its own initiative, and several of them instruct the agent to install Python packages, download model weights from the Hugging Face Hub and reach external services such as Semantic Scholar, arXiv or Weights and Biases. `pytorch-fsdp` renders no verdict table at all, so it is unsampled rather than cleared. Treat the verdicts as coverage for five skills out of 98, install categories rather than the whole library when you can, and pin what you do install.

## Limitations

- Snapshot data, verified 2026-10-29: 97,018 combined installs across 100 indexed listings; 14,111 GitHub stars; MIT License; last pushed 2026-06-15. Counts drift over time.
- The index runs ahead of the tree. skills.sh lists 100 names while the repo holds 98 skill directories, and the two extras are stale entries with almost no adoption: `writing-systems-papers` at 5 installs and `pytorch-fsdp` at 2, which correspond to the directories `20-ml-paper-writing/systems-paper-writing` and `08-distributed-training/pytorch-fsdp2` under their current names.
- Directory names and skill names disagree in 48 of the 98 directories. The `name:` field in frontmatter is what skills.sh indexes, so `12-inference-serving/vllm/` declares `serving-llms-vllm` and `03-fine-tuning/peft/` declares `peft-fine-tuning`; grep the frontmatter, not the path, when you are looking for a specific skill.
- One skill is much larger than the rest. `08-distributed-training/deepspeed/SKILL.md` is about 145 KB against an average of about 13 KB, which will blow most per-skill context budgets; read it in sections or point the agent at its `references/` files instead of loading the body.
- `10-optimization/ml-training-recipes/SKILL.md` uses CRLF line endings, so a naive grep for `^name:` returns `ml-training-recipes` with a trailing carriage return and a strict frontmatter parser sees `---\r`.
- The installer's canonical location is `~/.orchestra/skills` with symlinks into detected agent directories, and for Hermes it targets `~/.hermes/skills`. A Hermes profile keeps its own skills under `~/.hermes/profiles/<profile>/skills`, so on a multi-profile host the links do not land in the profile you meant; copy or link the specific skill directories yourself.
- The last commit is June 2026 and the root `package.json` says ISC while the repository `LICENSE` and GitHub both report MIT. Neither is a blocker, but pin a commit if you depend on exact behaviour.

## Related

- [Research Paper Writing Pipeline - Academic ML/AI Paper Production Setup](/hermes/skills/catalog/research-paper-writing-setup)
- [RigorPilot Skills - AI Research & Paper Reproduction Setup](/hermes/skills/catalog/rigorpilot-skills-setup)
- [HuggingFace Agent Skills - Datasets, Papers, ML Tools Setup](/hermes/skills/catalog/huggingface-agent-skills-setup)
- [Arxiv Setup](/hermes/skills/catalog/arxiv-setup)
- [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install by category, not by `--all`. The library spans 23 category folders and you will never need all of them in one profile; `npx @orchestra-research/ai-research-skills 12-inference-serving` installs four serving skills instead of ninety-eight, and the positional argument matches the category id.
- Start with `autoresearch` alone if you are testing the orchestration idea. It routes to the domain skills and will tell you which ones it wants, which is a better signal than reading 98 descriptions.
- Read the `dependencies` field before the body. It is the one line in each skill that tells you whether an invocation will try to pip install something on a GPU host or call a paid service, and it is cheap to scan across the whole set with a single grep over the installed directory.
- Use `--local` for anything you want reproducible. It writes `.orchestra-skills.json` into the project root and installs into the project tree instead of the home directory, so the skill set travels with the repository and a fresh clone gets the same versions.
- Prefer the raw `SKILL.md` URL over the installer when you want exactly one skill in a Hermes profile. The canonical copy plus symlink design is convenient for machines with one agent, but a single `curl` into `~/.hermes/profiles/<profile>/skills/<name>/SKILL.md` gives you the file where you expect it with nothing hidden.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
