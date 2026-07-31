---
title: Minions Hermes Mission Control — Multi-Agent Coordination Setup Guide
description: Install and configure Minions Hermes Mission Control for coordinating swarms of Hermes agents with shared task boards and real-time progress tracking.
publisher: aradotso/hermes-skills
installs: 173
quality_tier: 🔵 Community
---

# Minions Hermes Mission Control — Multi-Agent Coordination Setup Guide

Minions Hermes Mission Control is a multi-agent coordination dashboard for Hermes. Dispatch tasks to swarms of agents, track progress on shared boards, and aggregate results — all from a single control interface.

**Publisher:** [aradotso/hermes-skills](https://github.com/aradotso/hermes-skills)  
**Source:** skills.sh  
**Quality Tier:** 🔵 Community

---

## What It Does

- **Swarm Dispatch:** Send tasks to multiple Hermes agents simultaneously
- **Shared Task Boards:** Kanban-style boards visible across agents
- **Progress Tracking:** Real-time status updates from all active agents
- **Result Aggregation:** Collect and merge outputs from parallel agent runs
- **Resource Allocation:** Assign priority levels and compute budgets per agent
- **Conflict Resolution:** Detect and resolve overlapping or contradictory agent outputs

---

## Prerequisites

| Requirement | Check |
|-------------|-------|
| Hermes Agent installed | `hermes --version` |
| Multiple agent profiles | `hermes profile list` (at least 2) |
| `npx` available | `npx --version` |

---

## Installation

```bash
npx skills add https://github.com/aradotso/hermes-skills --skill minions-hermes-mission-control
```

Verify:

```bash
hermes skills list | grep minions-hermes
```

---

## Configuration

Create `~/.hermes/mission-control/config.yaml`:

```yaml
# Minions Mission Control Configuration
swarm:
  max_concurrent_agents: 5
  default_timeout: 300          # seconds
  retry_failed_tasks: true
  max_retries: 2

boards:
  persist_path: ~/.hermes/mission-control/boards/
  auto_archive_days: 7

agents:
  - name: corpusiq-growth
    profile: corpusiq
    priority: high
    max_tasks: 3
  - name: corpusiq-dev
    profile: dev
    priority: medium
    max_tasks: 2
  - name: corpusiq-research
    profile: research
    priority: low
    max_tasks: 5

notifications:
  telegram_topic: "CorpusIQ Team/2"
  on_complete: true
  on_error: true
```

---

## Usage

### Dispatch a Swarm Task

```bash
hermes skill invoke minions-hermes-mission-control \
  --dispatch "Research top 5 AI agent trends for Q3 2026" \
  --agents corpusiq-growth,corpusiq-research \
  --board trends-research
```

### Check Board Status

```bash
hermes skill invoke minions-hermes-mission-control --board trends-research --status
```

**Sample Output:**
```
Board: trends-research | 3 tasks | Updated: 2s ago
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ corpusiq-growth/search-social    — Done (42s)
🔄 corpusiq-growth/analyze-papers   — Running (18s elapsed)
⏳ corpusiq-research/web-scrape     — Queued
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Aggregate Results

```bash
hermes skill invoke minions-hermes-mission-control --board trends-research --aggregate
```

### Cancel a Board

```bash
hermes skill invoke minions-hermes-mission-control --board trends-research --cancel
```

---

## Swarm Task Patterns

| Pattern | Command Flag | Use Case |
|---------|-------------|----------|
| **Fan-Out** | `--strategy fanout` | Same task to all agents, compare results |
| **Pipeline** | `--strategy pipeline` | Agent A output → Agent B input |
| **Scatter-Gather** | `--strategy scatter` | Break large task into sub-tasks, parallel exec, merge |
| **Voting** | `--strategy vote` | Multiple agents solve same problem, majority wins |

---

## Integration with CorpusIQ

For CorpusIQ multi-agent workflows:

- **Content Research:** Fan-out topic research to growth + research agents
- **Competitive Analysis:** Scatter-gather: one agent per competitor, aggregate findings
- **Code + Docs Pipeline:** Dev agent builds feature → growth agent writes announcement
- **Overnight Sweeps:** Dispatch multiple agents for nightly marketplace/social sweeps

### Example: Overnight Content Sweep

```bash
hermes skill invoke minions-hermes-mission-control \
  --dispatch "Full overnight sweep: skills.sh + social mining + email check" \
  --agents corpusiq-growth,corpusiq-research \
  --strategy scatter \
  --board overnight-sweep \
  --schedule "0 2 * * *"
```

---

## Verification

```bash
# List active boards
hermes skill invoke minions-hermes-mission-control --boards

# Test with a simple dispatch
hermes skill invoke minions-hermes-mission-control \
  --dispatch "Self-test: echo 'hello' and return" \
  --agents corpusiq-growth \
  --board test-board

# Check result
hermes skill invoke minions-hermes-mission-control --board test-board --aggregate
```

---

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| "No agents available" | Agent profiles not configured | Add agents to `config.yaml` or use `--agents` flag |
| Tasks stuck in "Queued" | Agent at max task limit | Increase `max_tasks` or reduce concurrent workload |
| "Board not found" | Board name typo or archived | Check `--boards` for active boards |
| Agent timeout | Task too complex for timeout | Increase `default_timeout` or split into smaller tasks |

---

## Related Skills

- [Blueprint Orchestration](/hermes/skills/catalog/blueprint-orchestration-setup/) — Multi-agent blueprint methodology
- [Oh-My-Hermes Workflow](/hermes/skills/catalog/oh-my-hermes-workflow-setup/) — Workflow framework
- [CorpusIQ Supervisor Agent](/hermes/skills/catalog/) — Wave dispatch and swarm coordination

---

*Discovered July 31, 2026 · Published by aradotso/hermes-skills · 173 installs*
