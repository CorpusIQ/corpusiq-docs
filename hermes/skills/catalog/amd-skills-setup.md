---
title: "AMD Skills - ROCm, Ryzen AI and Kernel Authoring"
description: "amd/skills on skills.sh: 11.9K combined installs across 18 listings; ROCm diagnosis, Ryzen AI local models, Quark quantization and Instinct serving."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/amd-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-06"
tags: ["hermes skill", "agent skill", "skill setup", "amd", "rocm", "gpu"]
---

# AMD Skills - Setup Guide

**Source:** [amd/skills](https://www.skills.sh/amd/skills) via skills.sh - 11.9K combined installs across 18 indexed listings; first seen 2026-11-06 (Nov 6, 2026 morning sweep)
**GitHub:** 481 stars, MIT licence (LICENSE in the repo root), last pushed 2026-11-05, 21 SKILL.md directories in the tree: 17 product skills under skills/, three eval fixtures inside the TraceLens orchestrator and one skill in staging/
**Category:** AMD hardware for agents: ROCm setup, Ryzen AI local models, kernel work with FlyDSL and profiling with rocprofiler
**Quality Tier:** 🟡 Review - official AMD catalog on an MIT licence, but two sampled skills carry Snyk Warns and the README states the catalog is being built in the open with some skills in Tech Preview.

AMD Skills is AMD's own catalog of agent skills for its hardware and software stack: ROCm and HIP, Ryzen AI on the client side, Instinct and EPYC on the server side, plus Quark quantization, FlyDSL kernel authoring and the rocprofiler tooling. The skills follow the Agent Skills format and are written to interoperate with Cursor, Claude Code, Codex and Gemini CLI. The repository organises the first catalog into three focus areas, client-native, cross-stack and server-native.

The design decision worth understanding is federation. Each skill is owned and versioned by the team that owns the product it describes, and `amd/skills` is the catalog that vendors them. `.github/federation.json` is the registry, a nightly workflow compares content hashes against the recorded `.federated.json` and re-vendors only the skills that changed, and each bump lands as its own reviewed pull request. Every skill also ships a `skill-card.md`, a short governance card naming the description, owner and licence, so a reviewer can see who stands behind a skill without reading the source.

## Installation

The README installs with the `skills` CLI through `npx`, with no clone or manual copying:

```bash
npx skills add amd/skills
```

That prompts for a skill and an install destination. To pin a skill and an agent in one command:

```bash
npx skills add amd/skills --skill local-ai-use --agent claude-code
```

To see everything on offer before installing anything:

```bash
npx skills add amd/skills --list
```

The manual path is a clone plus a copy, with the destination depending on the agent:

```bash
git clone https://github.com/amd/skills.git amd-skills
cp -r amd-skills/skills/local-ai-use <agent-skills-dir>/
```

The README's table gives the personal and project locations: `~/.cursor/skills/` or `.cursor/skills/` for Cursor, `~/.claude/skills/` or `.claude/skills/` for Claude Code, and `$HOME/.agents/skills` or `$REPO_ROOT/.agents/skills` for Codex.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| local-ai-use | 1,389 | Routes image generation, text to speech and speech to text through a local Lemonade server so requests stop burning cloud tokens |
| local-ai-app-integration | 1,113 | Adds local AI to an existing app for offline support, privacy and lower API cost, including replacing a cloud backend |
| serving-llms-on-instinct | 1,096 | Deploys LLM inference on Instinct GPUs end to end: detect hardware, validate model fit, apply the vLLM recipe and launch a benchmarked endpoint |
| tracelens-analysis-orchestrator | 1,095 | Orchestrates PyTorch profiler trace analysis with TraceLens: perf reports, parallel system and kernel subagents, and a prioritised stakeholder report |
| magpie-kernel-evaluator | 1,088 | Benchmarks vLLM, SGLang or Atom inference and drives kernel evaluation, comparing HIP, CUDA, PyTorch and Triton implementations |
| serving-llms-on-epyc | 1,034 | Serves an LLM on an EPYC CPU with vLLM and zentorch in Docker, Podman or conda, sizing threads and KV cache for the host |
| lemonade-router-builder | 1,028 | Turns a plain language routing intent into a validated Lemonade collection.router policy JSON |
| hyperloom-workload-optimizer | 1,019 | Runs the Hyperloom multi-agent optimizer against a serving workload and reports a validated throughput gain |
| quark-install | 743 | Installs or verifies AMD Quark with an accelerator-matched PyTorch, then checks imports, kernels and the CLI |
| quark-torch-llm-ptq | 741 | Quantizes PyTorch and Hugging Face LLMs with Quark post-training quantization, from model inspection to a verified FP8 or INT4 artifact |
| rocm-doctor | 591 | Diagnoses broken ROCm, HIP, PyTorch or llama.cpp installs on Linux, Windows or WSL2 and applies a low-risk fix with consent |

The remaining 7 indexed listings range from 1 to 367 installs. `rocprofiler-pc-sampling` (367) profiles with rocprofv3 program counter sampling, `flydsl-kernel-trace-analysis` (233) and `flydsl-kernel-authoring` (232) cover FlyDSL kernel work, the three `rocprofiler-systems-*` skills sit at 42 installs each, and `apu-memory-tuner` (1) is the one listing whose directory lives in `staging/` rather than `skills/`.

## Why This Matters for Hermes Agents

AMD's stack is a place where a plausible answer is expensive. The right `gfx` target, the right container image, the right environment variables and the right order for a vLLM launch on Instinct are decisions a senior engineer makes without thinking and an agent working from general GPU knowledge gets wrong fluently. This catalog encodes the opinionated path rather than the API surface, which is the README's own framing of why a skill beats a doc.

The diagnostic skill is the one to install first. `rocm-doctor` covers the failure modes that eat an afternoon: `torch.cuda.is_available()` returning False, `rocminfo` not seeing the GPU, a llama.cpp build that will not start, and it routes Lemonade, LM Studio and Ollama problems to the right upstream channel. It applies a low-risk fix with consent or hands back the exact next step, which is the right shape for an agent operating on someone's machine.

The local-inference skills are the cost argument. `local-ai-use` changes routing persistently so image generation, transcription and speech synthesis run on the machine through Lemonade while chat stays on a cloud model. That is a configuration decision an agent can hold for you across sessions, and it is the kind of thing that never gets done if it stays a paragraph in a README.

Finally, the federation model is a maintenance property worth having in a fast-moving stack. ROCm, HIP, Ryzen AI and the framework integrations each ship on their own cadence, and a catalog that re-vendors only what changed, with a reviewed bump per skill, ages better than a hand-maintained list of instructions.

## Usage

| You say | What happens |
|---|---|
| "ROCm is not seeing my GPU" | rocm-doctor walks the diagnosis, applies a low-risk fix with consent or returns the exact next command |
| "Serve Qwen3 on my MI300X" | serving-llms-on-instinct detects the hardware, validates the fit, applies the vLLM recipe and launches a benchmarked endpoint |
| "Run images locally instead of paying per call" | local-ai-use reroutes image generation to a local Lemonade server and leaves chat on the cloud model |
| "Quantize this Llama model to FP8" | quark-torch-llm-ptq inspects the model, picks a scheme, builds reproducible artifacts and verifies the quantized result |
| "vLLM on an EPYC box, no GPU" | serving-llms-on-epyc detects the EPYC generation, checks model support and RAM fit, sizes threads and KV and verifies the endpoint |
| "Profile this kernel and tell me where it stalls" | rocprofiler-pc-sampling runs rocprofv3 with PC sampling and maps hotspots and stall reasons |
| "Route sensitive queries to the local model" | lemonade-router-builder generates and validates the router policy JSON, without registering it |

## Verification

Read the two skills most likely to run commands on your machine before you install them:

```bash
curl -fsSL https://raw.githubusercontent.com/amd/skills/main/skills/local-ai-use/SKILL.md | head -5
curl -fsSL https://raw.githubusercontent.com/amd/skills/main/skills/rocm-doctor/SKILL.md | head -5
```

Both return 200 on the `main` branch. The first should open with `name: local-ai-use` and a description about routing image generation, transcription and speech synthesis to a local Lemonade server. The second should describe diagnosing ROCm, HIP, PyTorch and llama.cpp failures, including the `rocminfo` and `hipInfo` checks.

Then install one skill and confirm both files arrived:

```bash
npx skills add amd/skills --skill local-ai-use --agent claude-code
ls ~/.claude/skills/local-ai-use
```

The listing should show SKILL.md next to `skill-card.md`, since every skill in this catalog ships the governance card. If the card is missing, you are looking at a hand-assembled copy rather than a catalog install.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-06) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| local-ai-use | Pass | Pass | Warn |
| magpie-kernel-evaluator | Pass | Pass | Pass |
| quark-torch-llm-ptq | Pass | Pass | Warn |
| flydsl-kernel-authoring | Pass | Pass | Pass |
| apu-memory-tuner | Pass | Pass | Pass |

Two Warns in the sample, on the two skills that change a machine's behaviour most: `local-ai-use` rewrites how an agent routes model calls, and `quark-torch-llm-ptq` installs quantization tooling and writes model artifacts. Both are worth reading in source before you run them on a host you care about.

The broader risk is ordinary for hardware skills. They run GPU commands, install wheels and containers, and read hardware counters, so a mistake lands on a real machine rather than in a text buffer. The repository ships a SECURITY.md and a CONTRIBUTING.md, and the README points contributors at `amd/skillscope` as the grader that produces the same verdict the catalog's own checks use. That is a healthy sign, but a passing scan says nothing about whether a launch recipe is correct for your exact card.

## Limitations

- Snapshot data, verified 2026-11-06: 11,896 combined installs across 18 indexed listings; 481 GitHub stars; MIT; last pushed 2026-11-05. Counts drift over time.
- The catalog is explicitly unfinished. The README states it is being built in the open and will evolve frequently, and that some skills may be in Tech Preview, with status held in the underlying product.
- The tree carries more SKILL.md files than the index names skills. 17 product skills sit under `skills/`, three evaluation fixtures live inside `skills/tracelens-analysis-orchestrator/evals/skills/`, and `apu-memory-tuner` sits in `staging/`; only the 18 index names are listings, and the staging skill is the least used at 1 install.
- Hardware-specific advice needs matching hardware. The serving skills detect the GPU or CPU generation, but detection is not validation: a driver and ROCm version that disagree with the recipe still fail, and the skill can only tell you what it found.
- The profiler and FlyDSL skills are the thin end of the catalog. `rocprofiler-pc-sampling` at 367 installs and the three `rocprofiler-systems-*` skills at 42 each are far less exercised than the serving skills above 1,000, so expect to debug more.
- Federation means version drift is by design. A vendored skill mirrors its upstream folder, so the behaviour you get depends on when the last bump landed, not only on the catalog commit you cloned.

## Related

- [Inference Sh Skills Setup](/hermes/skills/catalog/inference-sh-skills-setup)
- [GPUI Kit - Rust Desktop UI Components for Agents](/hermes/skills/catalog/gpui-kit-setup)
- [LLM Code Skills - Cross-Tool Documentation Pack](/hermes/skills/catalog/llm-code-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Install `rocm-doctor` first on any AMD box. It is the skill that tells you whether the rest of the catalog can work at all on that machine.
- Read the `skill-card.md` before the SKILL.md for anything unfamiliar. The card names the owner and licence, which tells you how fast the skill moves and who to believe about it.
- Prefer the `--skill` and `--agent` flags over the interactive prompt when scripting a setup. It makes the install reproducible and keeps the catalog from pulling skills you did not ask for.
- Ask for the validated-gain number from `hyperloom-workload-optimizer` rather than a claim of improvement. The skill is built to report a measured delta on your workload.
- Check `.github/federation.json` when a skill looks stale. It names the upstream repository, so you can read the source of truth rather than wait for the next bump.

---
*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
