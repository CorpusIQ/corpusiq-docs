---
title: "NVIDIA Skills - Physical AI and Robotics Agent Suite"
description: "nvidia/skills: 192.6K combined installs across 95 listings. NVIDIA-verified skills and plugins for Physical AI, robotics, simulation, CUDA and RAG."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/nvidia-skills-setup/"
robots: "index,follow"
last_updated: "2026-11-27"
tags: ["hermes skill", "agent skill", "skill setup", "nvidia", "physical ai", "cuda", "rag"]
---

# NVIDIA Skills - Setup Guide

**Source:** [nvidia/skills](https://www.skills.sh/nvidia/skills) via skills.sh - 192.6K combined installs across 95 indexed listings; first documented 2026-11-27 (evening sweep)

**GitHub:** [nvidia/skills](https://github.com/nvidia/skills) - 4,181 stars, Apache-2.0, branch main, last pushed 2026-11-27; skills live under `skills/<name>/SKILL.md`, with NVIDIA Verified plugins bundled under `plugins/nvidia-<product>/skills/<name>/SKILL.md`.

**Category:** Physical AI and robotics, simulation, CUDA-X libraries, RAG and AI Blueprints, and NVIDIA platform tooling

**Quality Tier:** 🟠 Orange - the Gen Agent Trust Hub fails omniverse-cad-to-simready and Socket warns on it, while Snyk warns on eight listings and fails cuopt-developer and rag-perf.

NVIDIA Skills is the official NVIDIA-verified Agent Skills and Plugins catalog. It teaches coding agents how to use NVIDIA software optimally: Physical AI and robotics workflows, simulation, CUDA-X libraries, RAG and AI Blueprints, and platform tools. The repository is a catalog of both forms. Skills are maintained in their product repos and mirrored here daily through an automated sync pipeline, while plugins bundle a product's skills plus a local MCP server where the product needs one. Every skill and every NVIDIA Verified Plugin is signed, scanned, and evaluated before it ships.

The install counts form a flat band, 1,710 to 3,527 across all 95 indexed listings, because one unit (a plugin or a bulk skills install) pulls the whole suite, so counts spread evenly instead of concentrating on a few hero skills. Twenty-one of the 95 listings carry install counts but have no SKILL.md in the current tree: the aiq-research and aiq-deploy pair, the five cuopt listings, the four cupynumeric listings, and ten vss listings.

## Installation

The README splits installation by runtime. Install individual skills with the skills CLI, or install a whole product toolset as an NVIDIA Verified plugin:

```text
npx skills add nvidia/skills --agent claude-code
npx skills add nvidia/skills --agent codex
```

The CLI prompts you to choose skills and an install destination; you do not need to clone the repo. To skip prompts and install a known skill:

```text
npx skills add nvidia/skills --skill cuopt-numerical-optimization-api --yes
```

Claude Code and Codex can install plugins through their official marketplaces instead:

```text
/plugin marketplace add NVIDIA/skills
/plugin install <plugin>@nvidia-official
```

```text
codex plugin marketplace add NVIDIA/skills
codex plugin add <plugin>@nvidia-official
```

Replace `<plugin>` with a name from the Plugin column of the README plugin catalog (nvidia-doca-plugin, nvidia-nvflare, nvidia-skills, nvidia-tao-toolkit). Installing the `nvidia-skills` plugin also installs the NVIDIA Skill Finder, which searches the catalog and recommends the right skills for a use case. The skills CLI requires version 1.5.16 or newer; `npx skills@latest add nvidia/skills` always uses the latest. Refresh installed skills with `npx skills update`, and preview what changed with `npx skills list` and `npx skills check`.

## What It Provides

| Skill | Installs | Use For |
|---|---|---|
| rag-blueprint | 3,527 | Deploy, configure, troubleshoot and manage the NVIDIA RAG Blueprint with Docker Compose or Helm. |
| accelerated-computing-cudf | 3,238 | NVIDIA cuDF GPU DataFrames: pandas acceleration, dask-cuDF, joins, groupby and CSV/Parquet I/O. |
| aiq-research | 2,905 | NVIDIA AI-Q research workflows. |
| dynamo-recipe-runner | 2,764 | Select, validate, patch and deploy NVIDIA Dynamo Kubernetes recipes. |
| cuopt-developer | 2,761 | GPU-accelerated optimization with cuOpt: LP, MILP, QP and VRP development. |
| cuopt-install | 2,556 | Install and set up NVIDIA cuOpt. |
| rag-eval | 2,546 | Filesystem RAG benchmarks (RAGAS quality) for a RAG Blueprint corpus. |
| aiq-deploy | 2,522 | NVIDIA AI-Q deployment workflows. |
| cudaq-guide | 2,519 | CUDA-Q setup, simulation targets, QPU access and @cudaq.kernel authoring. |
| deepstream-dev | 2,468 | DeepStream SDK development with the Python pyservicemaker API for video analytics. |
| omniverse-cad-to-simready | 2,461 | End-to-end CAD to SimReady USD conversion, conformance and packaging. |
| omniverse-usd-performance-tuning | 2,374 | Diagnose and optimize USD stages for slow loading, high memory or low FPS. |
| deepstream-import-vision-model | 2,327 | Bring an object-detection model into a DeepStream pipeline with ONNX, TRT engine build and benchmark. |
| skill-card-generator | 2,301 | Generate or update a governance skill card for an existing skill directory. |
| cuopt-routing-api-python | 2,299 | cuOpt vehicle routing (VRP) through the Python API. |
| omniverse-realtime-viewer | 2,267 | Router for Omniverse Realtime Viewer USD apps, XR delivery and SPG GPU processing. |
| rag-perf | 2,235 | Performance benchmarking for a deployed RAG Blueprint server (profiling plus aiperf load test). |
| cuopt-numerical-optimization-formulation | 2,208 | Formulate numerical optimization problems for cuOpt. |
| cuopt-server-api-python | 2,187 | cuOpt server-side Python API usage. |
| physical-ai-neural-reconstruction | 2,177 | Router for NVIDIA NuRec/NRE: USDZ, NCore conversion, 3DGS and sensor simulation. |
| nemotron-customize | 2,174 | End-to-end Nemotron model development, customization, evaluation and deployment. |
| nemotron-speech | 2,128 | Deploy and operate Nemotron Speech (Riva) NIMs for ASR, TTS and NMT. |
| nemo-rl-session-memory | 2,101 | NeMo-RL RLHF training session memory. |
| dali-dynamic-mode | 2,085 | GPU-accelerated data loading and processing with NVIDIA DALI. |
| nemotron-retrieval-recipes | 2,068 | Nemotron retrieval recipes for retrieval-augmented workflows. |
| physical-ai-infrastructure-setup-and-resilient-scaling | 2,065 | Physical AI infrastructure setup and resilient scaling. |
| physical-ai-video-data-augmentation | 2,012 | Physical AI video data augmentation. |
| physical-ai-defect-image-generation | 1,996 | Physical AI synthetic defect image generation. |
| nemo-automodel-distributed-training | 1,985 | NeMo AutoModel PyTorch-native distributed training for LLMs and VLMs. |
| nemo-automodel-recipe-development | 1,977 | Develop NeMo AutoModel training recipes. |
| cupynumeric-install | 1,976 | Install NVIDIA cuPyNumeric. |
| nemo-automodel-model-onboarding | 1,955 | Onboard models to NeMo AutoModel with Hugging Face support. |
| vss-summarize-video | 1,950 | Video Search and Summarization: summarize video content. |
| physicsnemo-discover | 1,949 | Discover PhysicsNeMo physics-ML models and methods. |
| dynamo-router-starter | 1,942 | Start Dynamo router-only mode deployments. |
| nemo-rl-auto-research | 1,939 | NeMo-RL automated RL research workflows. |
| cupynumeric-migration-readiness | 1,938 | Assess readiness to migrate NumPy code to cuPyNumeric. |
| dynamo-troubleshoot | 1,932 | Triage broken NVIDIA Dynamo deployments. |
| nemo-automodel-launcher-config | 1,931 | Configure NeMo AutoModel launchers. |
| dicom-metadata-extract | 1,923 | Extract DICOM metadata for medical imaging workflows. |
| vss-ask-video | 1,919 | Video Search and Summarization: question answering over video. |
| nemo-mbridge-perf-cuda-graphs | 1,916 | NeMo MBridge performance tuning with CUDA graphs. |
| cupynumeric-parallel-data-load | 1,910 | Parallel data loading with cuPyNumeric. |
| nemo-mbridge-perf-memory-tuning | 1,907 | NeMo MBridge memory tuning. |
| dynamo-interconnect-check | 1,905 | Validate disagg NIXL/UCX/NCCL interconnect for Dynamo. |
| dicom-series-preflight | 1,898 | Preflight DICOM series for medical imaging pipelines. |
| nemotron-policy-generator | 1,893 | Generate policies for Nemotron models. |
| earth2studio-install | 1,882 | Install Earth2Studio for AI weather and climate workflows. |
| cupynumeric-hdf5 | 1,882 | HDF5 I/O with cuPyNumeric. |
| dicom-series-to-volume | 1,881 | Convert DICOM series to volume. |
| digital-health-clinical-asr-setup | 1,876 | Set up the clinical ASR evaluation flywheel. |
| digital-health-clinical-asr-build | 1,873 | Build clinical-speech benchmarks for ASR. |
| vss-search-archive | 1,872 | Video Search and Summarization: search a video archive. |
| launch-nemo-rl | 1,872 | Launch NeMo-RL RLHF training (GRPO, DPO, SFT). |
| digital-health-clinical-asr-eval | 1,870 | Score clinical ASR with Keyword Error Rate. |
| earth2studio-discover | 1,868 | Discover Earth2Studio capabilities. |
| earth2studio-data-fetch | 1,867 | Fetch weather and climate data with Earth2Studio. |
| digital-health-clinical-asr-finetune | 1,867 | Fine-tune clinical ASR models. |
| nemo-mbridge-recipe-recommender | 1,865 | Recommend NeMo MBridge training recipes. |
| earth2studio-deterministic-forecast | 1,865 | Run deterministic weather forecasts with Earth2Studio. |
| vss-generate-video-report | 1,863 | Video Search and Summarization: generate video reports. |
| tilegym-adding-cutile-kernel | 1,863 | TileGym: add new cuTile kernels for tile-based GPU programming. |
| nemo-mbridge-perf-activation-recompute | 1,854 | NeMo MBridge activation recompute tuning. |
| nemo-mbridge-perf-parallelism-strategies | 1,853 | NeMo MBridge parallelism strategies. |
| nemo-mbridge-perf-moe-optimization-workflow | 1,853 | NeMo MBridge MoE optimization workflow. |
| nemo-mbridge-mlm-bridge-training | 1,853 | NeMo MBridge MLM bridge training between Hugging Face and Megatron-Core. |
| nemo-mbridge-perf-moe-vlm-training | 1,852 | NeMo MBridge MoE VLM training. |
| nemo-mbridge-multi-node-slurm | 1,851 | NeMo MBridge multi-node Slurm training. |
| nemo-mbridge-perf-sequence-packing | 1,850 | NeMo MBridge sequence packing. |
| vss-deploy-detection-tracking-3d | 1,849 | VSS Blueprint: deploy 3D detection and tracking. |
| nemo-mbridge-perf-expert-parallel-overlap | 1,849 | NeMo MBridge expert parallel overlap. |
| vss-deploy-profile | 1,848 | VSS Blueprint: profile a deployed stack. |
| nemo-mbridge-perf-cpu-offloading | 1,847 | NeMo MBridge CPU offloading. |
| nemo-mbridge-perf-moe-comm-overlap | 1,845 | NeMo MBridge MoE communication overlap. |
| nemo-mbridge-perf-moe-long-context | 1,844 | NeMo MBridge MoE long-context training. |
| vss-deploy-detection-tracking-2d | 1,840 | VSS Blueprint: deploy 2D detection and tracking. |
| vss-deploy-dense-captioning | 1,839 | VSS Blueprint: deploy dense captioning. |
| vss-deploy-video-embedding | 1,838 | VSS Blueprint: deploy video embedding. |
| nemo-mbridge-perf-moe-hardware-configs | 1,837 | NeMo MBridge MoE hardware configurations. |
| nemo-mbridge-perf-hierarchical-context-parallel | 1,837 | NeMo MBridge hierarchical context parallel. |
| nemo-rl-docs | 1,836 | NeMo-RL documentation guidance. |
| nemo-mbridge-resiliency | 1,835 | NeMo MBridge training resiliency. |
| holoscan-setup | 1,835 | Set up the Holoscan SDK for streaming AI applications. |
| vss-manage-video-io-storage | 1,833 | VSS Blueprint: manage video I/O and storage. |
| vss-generate-video-calibration | 1,832 | VSS Blueprint: generate video calibration. |
| vss-setup-video-analytics-api | 1,831 | VSS Blueprint: set up the video analytics API. |
| vss-query-analytics | 1,831 | VSS Blueprint: query analytics. |
| nemo-mbridge-perf-megatron-fsdp | 1,831 | NeMo MBridge Megatron FSDP. |
| vss-manage-alerts | 1,830 | VSS Blueprint: manage alerts. |
| nemo-mbridge-perf-moe-dispatcher-selection | 1,828 | NeMo MBridge MoE dispatcher selection. |
| nemo-mbridge-perf-tp-dp-comm-overlap | 1,823 | NeMo MBridge TP/DP communication overlap. |
| mcore-linting-and-formatting | 1,820 | Megatron-Core linting and formatting. |
| vss-setup-behavior-analytics | 1,819 | VSS Blueprint: set up behavior analytics. |
| holoscan-install-container | 1,818 | Install the Holoscan SDK as a container. |
| tao-setup-nvidia-gpu-host | 1,710 | TAO Toolkit: set up an NVIDIA GPU host for vision AI fine-tuning. |

All 95 indexed listings appear in the table above; none sit below 1,700 installs. The band stays flat because one install pulls the whole suite, as noted above.

## Why This Matters for Hermes Agents

NVIDIA Skills is a model of the plugin-first pattern at vendor scale: a single Verified Plugin bundles a product's skills plus a local MCP server where the product needs one, so an agent gets both the knowledge and the live tooling in one install. The repository is explicit that every skill and plugin is signed, scanned, and evaluated before it ships, which is the trust pipeline any builder should want before wiring a third-party suite into a router.

The catalog split is the useful discipline to copy. Skills are maintained in their product repos and mirrored here daily, so the monorepo stays a mirror rather than a fork, and each plugin is published to build.nvidia.com and the major agent marketplaces. That separation keeps attribution and maintenance ownership with the product teams instead of drifting inside a single repo.

The coverage is deliberately wide, from Physical AI and robotics through simulation, CUDA-X libraries, RAG and AI Blueprints. For a Hermes-style builder, the RAG Blueprint skills alone (rag-blueprint, rag-eval, rag-perf) form a deploy, evaluate, and benchmark loop that is hard to find in a single vendor suite, and the NVIDIA Skill Finder skill is documented as the entry point that routes to the right skill from a plain-language request.

The mirror-and-verify posture also encodes the trust boundary clearly: this is guidance, not a source of truth, and the per-product source repos and NVIDIA documentation remain authoritative. That keeps the skill layer disposable as the underlying products release.

## Usage

| You say | What happens |
|---|---|
| "Deploy an NVIDIA RAG Blueprint with Docker Compose" | Uses rag-blueprint to configure, deploy and manage the RAG pipeline. |
| "Benchmark my deployed RAG server" | Uses rag-perf for the profiling pass and aiperf load test, or rag-eval for RAGAS quality scoring. |
| "Solve a linear programming problem with cuOpt" | Uses the cuopt skills to build the GPU-accelerated optimization model. |
| "Bring a Hugging Face object-detection model into DeepStream" | Uses deepstream-import-vision-model for ONNX download, TRT engine build and benchmark. |
| "Convert this CAD model to SimReady USD" | Uses omniverse-cad-to-simready to coordinate conversion, conformance and packaging. |
| "Fine-tune a vision AI model on my own data" | Uses the TAO Toolkit skills to fine-tune a pretrained model and export it for deployment. |
| "Find the right NVIDIA skill for my GPU workload" | Uses nvidia-skill-finder to search the catalog and install the matching skills. |

## Verification

The raw path below returned 200 on branch main on 2026-11-27:

```bash
curl -sL -o /dev/null -w "%{http_code}\n" \
  https://raw.githubusercontent.com/nvidia/skills/main/skills/rag-blueprint/SKILL.md
```

After a clone, confirm the skill layout and count the top-level skill directories:

```bash
git clone --depth 1 https://github.com/nvidia/skills.git /tmp/nvidia-skills
ls /tmp/nvidia-skills/skills/ | wc -l
ls /tmp/nvidia-skills/plugins/
head -3 /tmp/nvidia-skills/skills/rag-blueprint/SKILL.md
```

The first count prints several hundred skill directories, the plugins listing shows the Verified Plugin directories, and head shows the rag-blueprint frontmatter. The index tracks 95 listings, but the current tree holds far more skills than the indexed set, and some indexed names have no counterpart on disk.

## Security

skills.sh verdicts for sampled skills (verified 2026-11-27) - re-check the security pages on skills.sh before production use:

| Skill | Gen Agent Trust Hub | Socket | Snyk |
|---|---|---|---|
| rag-blueprint | Pass | Pass | Pass |
| accelerated-computing-cudf | Pass | Pass | Warn |
| aiq-research | Pass | Pass | Warn |
| dynamo-recipe-runner | Pass | Pass | Warn |
| cuopt-developer | Pass | Pass | Fail |
| cuopt-install | Pass | Pass | Warn |
| rag-eval | Pass | Pass | Warn |
| aiq-deploy | Pass | Pass | Warn |
| cudaq-guide | Pass | Pass | Warn |
| deepstream-dev | Pass | Pass | Pass |
| omniverse-cad-to-simready | Fail | Warn | Pass |
| omniverse-usd-performance-tuning | Pass | Pass | Pass |
| deepstream-import-vision-model | Pass | Pass | Pass |
| skill-card-generator | Pass | Pass | Warn |
| cuopt-routing-api-python | Pass | Pass | Pass |
| omniverse-realtime-viewer | Pass | Pass | Pass |
| rag-perf | Pass | Pass | Fail |
| cuopt-numerical-optimization-formulation | Pass | Pass | Pass |
| cuopt-server-api-python | Pass | Pass | Pass |
| physical-ai-neural-reconstruction | Pass | Pass | Pass |

This guide is Orange because three sampled listings fail a scanner: the Gen Agent Trust Hub fails omniverse-cad-to-simready (where Socket warns), and Snyk fails cuopt-developer and rag-perf while warning on eight listings. The repository is mostly Markdown skills plus plugin directories and CI scripts, so read the specific findings on the skills.sh security pages before installing a flagged skill into a production profile.

## Limitations

- Snapshot data, verified 2026-11-27: 192,633 combined installs across 95 indexed listings; 4,181 GitHub stars; Apache-2.0; last pushed 2026-11-27. Counts drift over time.
- The install index outruns the tree: twenty-one of the 95 indexed listings (the aiq pair, five cuopt listings, four cupynumeric listings, and ten vss listings) carry install counts but have no SKILL.md in the current tree.
- The flat install band, 1,710 to 3,527, reflects the plugin-plus-suite install model rather than per-skill popularity, so a single listing's count is a weak signal of its individual usefulness.
- Skills are maintained in per-product source repos and mirrored here daily; the catalog names can drift from skills.sh listings as products rename or consolidate skills.
- The three Fail verdicts are published without their reasons, and Snyk warns on eight of the twenty sampled listings, so check the security pages on skills.sh before installing flagged skills into production.

## Related

- [NemoClaw User Guide - Security Setup](/hermes/skills/catalog/nemoclaw-user-guide-setup)
- [Qdrant Skills - Vector Search, Retrieval and Memory Setup](/hermes/skills/catalog/qdrant-skills-setup)
- [Skill Vetting Setup Guide - CorpusIQ Docs](/hermes/skills/catalog/skill-vetting-setup)

[Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace)

## Pro Tips

- Start with the NVIDIA Skill Finder (`npx skills add nvidia/skills --skill nvidia-skill-finder --yes`) so the agent routes to the right skill instead of guessing across 95 names.
- Use plugins on Claude Code and Codex, not the skills CLI, so the bundled MCP configuration and updates arrive through the official marketplace.
- Keep `npx skills update` in your maintenance cadence; skills are renamed and consolidated as products release, and the CLI flags stale local copies.
- When the tree and the index disagree, trust the tree: the current SKILL.md files are what install, and twenty-one indexed names have no counterpart on disk.
- Treat the RAG Blueprint trio (rag-blueprint, rag-eval, rag-perf) as one workflow: deploy with the first, score with the second, load-test with the third.

---

*← [Skills Catalog](/hermes/skills/catalog) | [Skills Marketplace](/hermes/skills/marketplace) →*
*Powered by CorpusIQ*
