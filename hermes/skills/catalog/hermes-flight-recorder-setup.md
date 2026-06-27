---
title: Hermes Flight Recorder Setup Guide
description: Set up the Hermes Autonomy Flight Recorder — adversarial eval harness for autonomous agent runs with trace-based scorecards, HTML reports, and training data export.
skill_name: hermes-flight-recorder
repo: zwright8/hermes-flight-recorder
compatibility: Hermes Agent
installs: New (June 2026)
---

# Hermes Flight Recorder — Setup Guide

## Overview

The Hermes Autonomy Flight Recorder is a standalone adversarial eval harness for Hermes Agent runs. It converts run artifacts into normalized traces, scores them against explicit autonomy boundaries, and renders static HTML reports. This is accountability and regression infrastructure — not a sandbox, not a security boundary.

**Key Facts:**
- **Deterministic scoring** — no API keys, no network required
- **Static HTML reports** — viewable in any browser
- **Training data export** — SFT, DPO, and reward model views
- **Scenario quality metrics** — measures evaluation contract strength
- **Evidence coverage reports** — verifies judgment backing

---

## Prerequisites

- Python 3.11+
- Git
- A web browser (for viewing HTML reports)

No API keys or network access required.

---

## Installation

```bash
git clone https://github.com/zwright8/hermes-flight-recorder.git
cd hermes-flight-recorder
```

---

## Quick Demo

The demo runs offline and deterministically:

```bash
python -m unittest discover
./demo.sh
open runs/index.html
```

### Expected Demo Output

- ✅ **2 passing reports:** prompt-injection resistance, structured email completion
- ❌ **4 failing reports:** unsupported claims, prompt-injection obedience, secret exposure, budget violations
- 📊 **Compare report:** before/after regression comparison
- 📈 **Suite compare:** aggregate score/pass-rate deltas
- 📋 **Suite summary:** `runs/suite_summary.json`
- 🎯 **Scenario quality:** `runs/scenario_quality.json`
- 🏋️ **Training export:** `runs/training_export/` with episodes, rewards, preference pairs, SFT/DPO views
- 🔍 **Evidence coverage:** `runs/evidence_coverage.json`
- 👁️ **Trace observability:** `runs/trace_observability.json`

---

## Usage

### Run Against a Single Hermes Session

```bash
# Export a Hermes session trace
hermes session export --session-id <id> --output trace.json

# Run flight recorder against it
python -m flight_recorder evaluate --trace trace.json --output runs/
```

### Run a Suite of Scenarios

```bash
# Define scenarios in scenarios.yaml
python -m flight_recorder suite --scenarios scenarios.yaml --output runs/
```

### Generate Training Data

```bash
python -m flight_recorder export-training --runs runs/ --output training_data/
```

---

## Report Types

| Report | File | Description |
|--------|------|-------------|
| **Single Run** | `runs/<run>/report.html` | Per-run scorecard with pass/fail rules |
| **Compare** | `runs/compare.html` | Before/after regression comparison |
| **Suite Compare** | `runs/suite_compare.html` | Aggregate deltas across all scenarios |
| **Suite Summary** | `runs/suite_summary.json` | Pass rates, scores, task-family rollups |
| **Scenario Quality** | `runs/scenario_quality.json` | Contract strength, assertion coverage |
| **Evidence Coverage** | `runs/evidence_coverage.json` | Judgment backing verification |
| **Trace Observability** | `runs/trace_observability.json` | Event volume, type diversity, timing |

---

## Autonomy Boundaries Evaluated

The flight recorder scores against explicit boundaries:

| Boundary | What It Checks |
|----------|---------------|
| **Prompt Injection Resistance** | Agent refuses to execute injected instructions |
| **Task Completion Evidence** | Claims of completion are backed by observable artifacts |
| **Side-Effect Verification** | Subagent claims are verified against actual outputs |
| **Budget Enforcement** | Agent stays within token/cost constraints |
| **Secret Protection** | Credentials and secrets are not exposed in outputs |
| **Delegation Control** | Subagent spawning respects configured limits |

---

## Training Data Export

The `--export-training` flag produces:

```
runs/training_export/
├── episodes/           # Individual run episodes
├── terminal_rewards/   # Per-episode reward signals
├── step_rewards/       # Step-level reward attribution
├── preference_pairs/   # Win/loss pairs for DPO
├── sft/                # Supervised fine-tuning data
├── dpo/                # Direct preference optimization data
├── reward_model/       # Reward model training views
├── failure_modes/      # Categorized failure patterns
├── curriculum/         # Difficulty-progressive curriculum
├── splits/             # Train/validation/test splits
├── dataset_card.md     # Dataset documentation
├── quality_metrics.json # Dataset quality metrics
└── manifest.json       # Full export manifest
```

---

## Use Cases for CorpusIQ

### 1. Autonomous Growth Agent QA
Before deploying a new growth agent workflow, run it through the flight recorder:

```bash
# Export test runs
hermes session export --session-id test-001 --output trace.json
python -m flight_recorder evaluate --trace trace.json

# Check for prompt injection vulnerabilities
grep "prompt-injection" runs/*/report.html
```

### 2. Regression Testing
After updating agent skills or prompts, verify no regressions:

```bash
python -m flight_recorder suite --scenarios regression_suite.yaml
open runs/suite_compare.html
```

### 3. Continuous Improvement
Export training data to fine-tune models on CorpusIQ-specific agent behaviors:

```bash
python -m flight_recorder export-training --runs production_runs/ --output training/
```

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError` | Run from within the cloned repo directory |
| Empty reports | Ensure trace JSON has required fields (events, messages) |
| Demo fails | Run `python -m unittest discover` first to verify environment |
| Large trace files | Use `--max-events 10000` to limit processing |

---

## Verification

```bash
# 1. Run unit tests
python -m unittest discover

# 2. Run demo
./demo.sh

# 3. Check reports exist
ls runs/index.html runs/suite_summary.json

# 4. Verify training export
ls runs/training_export/manifest.json
```

---

## Limitations

- **Not a security boundary:** Real containment belongs at the OS, process, and network layers
- **Offline only:** No live monitoring — evaluates completed runs
- **Trace-dependent:** Quality of evaluation depends on trace completeness
- **Deterministic scoring:** Does not use LLM-as-judge (by design)

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Flight Recorder on GitHub](https://github.com/zwright8/hermes-flight-recorder) →*

*Curated by CorpusIQ — one MCP endpoint, all your business tools.*
