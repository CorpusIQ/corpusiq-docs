---
title: "Run a Local Coding Agent: OpenCode + Nemotron on GPU"
description: "Set up opencode as a free local coding agent: Nemotron served by vLLM, sandbox discipline, and the directory-pinning gotcha that saves your repos."
canonical: "https://www.corpusiq.io/docs/hermes/best-practices/local-coding-agent"
robots: "index,follow"
last_updated: "2026-09-16"
tags: ["local llm", "coding agent", "opencode", "vllm", "dgx spark"]
---

# Run a Local Coding Agent: OpenCode + Nemotron on GPU

Frontier coding agents are powerful and expensive. Most repository work is not frontier work: conformance passes, bulk edits, small refactors, test scaffolding. Running those on a local model turns a metered cost into an electricity bill, and your code never leaves the machine.

This guide walks through a setup that works: opencode as the agent, Nemotron 3.5 Lightning served by vLLM on a DGX Spark, with the operational details that separate a demo from a tool you trust.

## What you need

- A machine with a modern NVIDIA GPU and enough unified or device memory for the model (a 30B model in NVFP4 fits comfortably on 128GB unified memory).
- Docker or Podman with GPU access (CDI on recent Podman).
- Node.js for opencode, Python for the serving stack.

## Serve the model

Run vLLM as a supervised service, not a manual container. A systemd unit with automatic restart is the difference between a toy and infrastructure:

```bash
podman run --rm --name nemotron-vllm \
  --device nvidia.com/gpu=all --ipc=host \
  -p 127.0.0.1:8100:8000 \
  -v /models/main:/models/main:ro \
  docker.io/vllm/vllm-openai:latest \
  --model /models/main --served-model-name nemotron-35-lightning \
  --kv-cache-dtype fp8 --enable-prefix-caching \
  --gpu-memory-utilization 0.70 --max-num-seqs 16
```

Two flags matter more than they look. Memory utilization sets how much of the device the engine may claim. On a unified-memory box the host stack needs real headroom, and an aggressive value causes the engine to die under load, taking your agent sessions with it. Start at 0.70 and leave room. Capping concurrent sequences bounds KV cache growth when several agent loops run at once.

## Install and configure opencode

```bash
npm i -g opencode-ai
```

Point it at the local endpoint in `~/.config/opencode/opencode.json`:

```json
{
  "permission": { "edit": "allow", "bash": "allow" },
  "provider": {
    "local": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Local (GPU)",
      "options": { "baseURL": "http://127.0.0.1:8100/v1", "apiKey": "local" },
      "models": { "nemotron-35-lightning": { "name": "Nemotron 3.5 Lightning (local)" } }
    }
  }
}
```

## The gotcha that costs you a repository

When you spawn opencode from a script, a cron job, or Python instead of an interactive shell, it resolves its working directory from the inherited `PWD` environment variable, not from the process working directory. The writes land wherever that variable points. We learned this the hard way: a task suite meant for a sandbox clone wrote 47 files into a different repository checkout.

Always pin the directory explicitly:

```python
env = dict(os.environ, PWD=workdir)
subprocess.run(["opencode", "run", "--dir", workdir, "-m", model, prompt],
               cwd=workdir, env=env)
```

After every run, verify placement (`find <workdir> -name <expected-file>`) and check that no other repository gained files. A one-line guard that runs `git status --short` on your real checkouts after each task catches misroutes immediately.

## Make it pass real tasks

Local models are literal. Prompts that assume context fail. Four rules close most of the gap:

1. Name the exact output path and say to create parent directories. Without this, files appear at the repository root.
2. End every prompt with a verification instruction and a continue-until-it-passes sentence.
3. For bulk work, instruct a loop: list targets with grep, fix all, re-run the check until it reports zero.
4. Put repository conventions in an `AGENTS.md` at the repo root; opencode reads it automatically.

## Sandbox everything

Run task suites against fresh clones, never live repositories. Keep one runner with per-task deterministic checks, archive results per round, and treat the checker, not the agent's summary, as the source of truth. Models occasionally report success without making a single edit; state-based checks catch that instantly.

## Honest limits

Local coding agents are strongest on mechanical and structural work: bulk edits, format conformance, repetitive refactors, test scaffolding. They are weaker on novel implementation and long-form writing. Route accordingly: local for volume, frontier for judgment, and verification gates on both.
