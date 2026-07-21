---
title: "Beastmode — Mixture of Agents (MofA) for Hermes Workflows"
description: "Orchestrate multiple Hermes agents with Beastmode's Mixture of Agents framework for cost-optimized parallel work."
---

# Beastmode Setup Guide

**Repo:** [lac5q/beastmode](https://github.com/lac5q/beastmode)
**Stars:** ⭐7 | **Language:** Shell

## Overview

Beastmode is a Mixture of Agents (MofA) orchestration framework for Hermes, OpenClaw, and Codex. It enables cost-optimized parallel agent workflows with MemroOS-style context continuity. Uses git worktrees for isolated agent workspaces.

**Key capabilities:**
- Parallel agent dispatch with worktree isolation
- Cost-optimized model routing (Qwen-first, escalate to DeepSeek)
- Self-improving agent workflows
- Context continuity via MemroOS integration

## Installation

```bash
git clone https://github.com/lac5q/beastmode.git
cd beastmode
chmod +x beastmode.sh
```

## Usage

```bash
./beastmode.sh --task "Research competitor pricing" --agents 3
./beastmode.sh --orchestrate workflow.json
```

## Pitfalls

- Shell-based — limited error handling
- Early-stage (7 stars) — test thoroughly before production use
