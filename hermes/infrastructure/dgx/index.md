---
title: NVIDIA DGX Spark — Primary Compute Pattern
description: "Running Hermes Agent on an NVIDIA DGX Spark for production inference, model routing, and 24/7 autonomous operations."
canonical: "https://www.corpusiq.io/docs/hermes/infrastructure/dgx/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes agent", "ai agent", "nous research"]

---

# NVIDIA DGX Spark — Primary Compute Pattern

The DGX Spark is a compact GPU workstation well suited as the primary inference and orchestration node for an agent platform. It handles model inference, cron scheduling, memory management, and the majority of operational workloads.

## Hardware

NVIDIA GPU with CUDA support. Local inference eliminates API latency and cost for lightweight tasks. The machine runs 24/7 with automatic recovery for any agent process failures.

## Software Stack

| Layer | Component | Purpose |
|-------|-----------|---------|
| OS | Ubuntu Linux | Base system, NVIDIA drivers |
| Runtime | Python 3.11+ | Agent and script execution |
| Inference | Ollama | Local LLMs for routine tasks |
| Scheduling | cron + systemd | 24/7 job execution |
| Process guard | systemd `Restart=on-failure` | Auto-recovery of agent processes |

## Workloads

### Model Routing
Local Ollama models handle routine execution at zero API cost. Complex reasoning escalates to premium APIs. This hybrid approach keeps the monthly API bill low while preserving quality on hard tasks.

### Cron Scheduling
All recurring jobs run from the primary node. Each cron references standalone wrapper scripts — never inline shell with complex quoting.

### Memory Management
Session state and knowledge stores live on local disk. Regular pruning keeps databases lean.

### Multi-Profile Isolation
Multiple agent profiles run on one machine. Each profile gets its own directory tree, environment, and token storage.

## Lessons Learned

1. **Wrapper scripts over inline cron commands.** A cron Script field that points to a script file survives environment changes; inline pipelines break silently.
2. **Watchdog everything.** If the agent goes dark, something must notice. A watchdog cron that checks gateway health catches silent failures.
3. **Token expiry is a silent killer.** JWT/API tokens expire without warning. Schedule proactive refresh checks rather than waiting for failures.
