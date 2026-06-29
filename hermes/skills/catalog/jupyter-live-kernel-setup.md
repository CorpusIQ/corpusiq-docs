---
title: Jupyter Live Kernel — Interactive Python REPL Setup Guide
description: Install and configure jupyter-live-kernel, the official Hermes Agent skill for stateful Python via a live Jupyter kernel. 80 installs, perfect for data science and iterative exploration.
---

# Jupyter Live Kernel — Setup Guide

**Source:** [nousresearch/hermes-agent](https://skills.sh/nousresearch/hermes-agent/jupyter-live-kernel) (80 peak installs)
**Category:** Data Science / Development
**License:** MIT · **Platforms:** Linux, macOS, Windows
**Dependencies:** uv, JupyterLab, hamelnb

A stateful Python REPL via a live Jupyter kernel that gives Hermes persistent variable state across executions. Use this instead of `execute_code` when you need to build up state incrementally — explore APIs, inspect DataFrames, train models, or iterate on complex code without losing context between steps.

---

## What It Does

| Capability | How |
|-----------|-----|
| **Persistent state** | Variables survive across executions — no re-running setup code |
| **Data exploration** | Load data once, then query, filter, and visualize iteratively |
| **ML workflows** | Load models, run inference, tune hyperparameters step by step |
| **API exploration** | Authenticate once, then explore endpoints incrementally |
| **Notebook-style** | Same workflow as Jupyter, but driven by Hermes agent |

---

## When to Use This vs Other Tools

| Tool | Use When |
|------|----------|
| **jupyter-live-kernel** | Iterative exploration, state across steps, data science, ML, "let me try this and check" |
| `execute_code` | One-shot scripts needing Hermes tool access (web_search, file ops). Stateless. |
| `terminal` | Shell commands, builds, installs, git, process management |

**Rule of thumb:** If you'd reach for a Jupyter notebook, use this skill.

---

## Prerequisites

### Step 1: Install uv

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Verify
uv --version
```

### Step 2: Install JupyterLab

```bash
uv tool install jupyterlab

# Verify
jupyter lab --version
```

### Step 3: Install hamelnb

```bash
# Clone the hamelnb repo
git clone https://github.com/nousresearch/hamelnb.git ~/.agent-skills/hamelnb

# Install the Python package
cd ~/.agent-skills/hamelnb
uv pip install -e .
```

---

## Installation

### Via skills.sh (Recommended)

```bash
npx skills add nousresearch/hermes-agent --skill jupyter-live-kernel
```

### Direct from Hermes Agent Repo

```bash
git clone --depth 1 https://github.com/nousresearch/hermes-agent.git /tmp/hermes-agent
cp -r /tmp/hermes-agent/skills/data-science/jupyter-live-kernel ~/.hermes/skills/
```

### Manual (Single Install)

```bash
mkdir -p ~/.hermes/skills/jupyter-live-kernel
curl -o ~/.hermes/skills/jupyter-live-kernel/SKILL.md \
  https://raw.githubusercontent.com/nousresearch/hermes-agent/main/skills/data-science/jupyter-live-kernel/SKILL.md
```

---

## Starting the Kernel

### Start Jupyter Server

```bash
# Start JupyterLab in the background
jupyter lab --no-browser --port=8888 &
```

### Launch the Kernel via Hermes

In a Hermes session, the skill auto-launches the kernel when you make a request that benefits from stateful execution:

> "Load the Titanic dataset, show me the first 10 rows, then compute survival rates by passenger class."

Hermes loads the data once, then runs successive queries against the live kernel without reloading.

### Manual Kernel Launch

```bash
python3 ~/.agent-skills/hamelnb/skills/jupyter-live-kernel/scripts/jupyter_live_kernel.py
```

---

## Usage Examples

### Example 1: Data Exploration

```
You: Load this CSV: ~/data/sales_2026.csv. Show me:
     1. Column names and types
     2. Top 5 rows
     3. Revenue by region
     4. Plot monthly trend
Hermes: [Loads data once, runs 4 queries against live kernel]
```

### Example 2: ML Model Iteration

```
You: Load the sklearn diabetes dataset. Train a random forest,
     check R², then try gradient boosting and compare.
Hermes: [Loads data → trains RF → checks score → trains GB → compares — all in one kernel session]
```

### Example 3: API Exploration

```
You: Connect to the GitHub API with my token.
     First, list my repos.
     Then, for each repo, show the last commit.
Hermes: [Authenticates once, then iterates through repos in the same kernel]
```

---

## Verification

```bash
# Check skill is installed
hermes skills list | grep jupyter-live-kernel

# Verify Jupyter is running
curl -s http://localhost:8888/api/status | python3 -c "import sys,json; print(json.load(sys.stdin).get('started','NOT RUNNING'))"

# Test kernel launch
python3 -c "
from jupyter_client import BlockingKernelClient
kc = BlockingKernelClient()
kc.load_connection_file('.agent-skills/hamelnb/kernel.json')
kc.start_channels()
kc.execute('print(1+1)')
print('Kernel OK')
"
```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `jupyter: command not found` | Run `uv tool install jupyterlab` |
| `No kernel connection file` | Ensure `jupyter lab` is running on port 8888 |
| `Connection refused` | Check Jupyter with `curl http://localhost:8888/api/status` |
| `ModuleNotFoundError: hamelnb` | Run `cd ~/.agent-skills/hamelnb && uv pip install -e .` |
| Kernel timeout | Restart Jupyter: `pkill jupyter && jupyter lab --no-browser --port=8888 &` |

---

## Related Skills

- **[data-science](https://skills.sh/nousresearch/hermes-agent)** — Umbrella skill for all data science tools
- **[mlops-model-operations](https://skills.sh/nousresearch/hermes-agent)** — Production ML model deployment and operations
- **[arxiv](arxiv-setup.md)** — Academic paper search for research context
- **[local-inference-optimizer](https://github.com/ForgetMeAI/local-inference-optimizer-skill)** — Community skill for optimizing local LLM inference

---

## Pro Tips

1. **Keep kernels alive** — The kernel persists until you explicitly shut it down. Long-running data explorations benefit from keeping one kernel open.
2. **Use for code review** — Load a codebase into the kernel, then ask Hermes to explore specific functions and their call chains without re-parsing.
3. **Combine with web_extract** — Fetch data from APIs or web pages, load into the kernel, then analyze iteratively.
4. **Save checkpoints** — Periodically ask Hermes to save the kernel state with `%store` magic commands for recovery.
5. **Monitor resources** — Live kernels consume RAM. Check with `!free -h` (Linux) or `!vm_stat` (macOS) inside the kernel.
