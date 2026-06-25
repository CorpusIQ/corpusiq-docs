---
title: ContextForge RAG — Hermes Agent Profile Setup Guide
description: Install and configure codegraphtheory/context-forge-rag — an installable Hermes Agent profile for production RAG architecture, AI agent workflows, evaluation, and observability
---

# ContextForge RAG — Hermes Profile Setup

**Source:** [codegraphtheory/context-forge-rag](https://github.com/codegraphtheory/context-forge-rag)
**Stars:** 1 ⭐ | **License:** MIT
**Created:** June 24, 2026
**Category:** Agent Infrastructure / RAG / AI Architecture
**Type:** Hermes Agent Profile (installable)

---

## 1. What It Is

ContextForge RAG is an installable Hermes Agent **profile** — not just a single skill, but a full agent configuration bundle for principal-level production RAG architecture. Built from [codegraphtheory/hermes-profile-template](https://github.com/codegraphtheory/hermes-profile-template).

**What this profile is good at:**
- **Production RAG architecture:** ingestion, chunking, embeddings, hybrid retrieval, reranking, citation packing, and model routing
- **Agent workflow design:** intent classification, tool contracts, idempotency, escalation, bounded loops, failure handling
- **Evaluation & observability:** golden datasets, retrieval metrics, LLM judge rubrics, traces, cost telemetry, regression gates
- **Delivery planning:** ADRs, implementation-ready GitHub issues, roadmaps, rollout plans, rollback criteria

### Bundled Skills

| Skill | Purpose |
|-------|---------|
| `principal-ai-architect` | ADRs, architecture tradeoffs, diagrams, decision records |
| `technical-roadmapping` | Delivery sequencing, milestones, dependency mapping, risk gates |
| `production-rag-architecture` | Retrieval system design, namespace strategy, chunking, embeddings, reranking, rollout |
| `rag-evaluation-observability` | Golden datasets, metric design, LLM judge rubrics, traces, regression gates |
| `agentic-workflow-issue-factory` | Implementation-ready issues and typed agent tool design |

---

## 2. Prerequisites

- Hermes Agent (profile install support)
- Any Hermes-supported model provider (interactive use)
- Optional: `.env` variables for external services (see `.env.EXAMPLE`)

---

## 3. Installation

### Option A: Direct from GitHub

```bash
hermes profile install github.com/codegraphtheory/context-forge-rag --name context-forge-rag --yes
hermes -p context-forge-rag
```

### Option B: Local Clone

```bash
git clone https://github.com/codegraphtheory/context-forge-rag.git
cd context-forge-rag
python3 scripts/validate_profile.py .
hermes profile install . --name context-forge-rag --yes
hermes -p context-forge-rag
```

### Verify

```bash
python3 scripts/validate_profile.py .
python3 -m py_compile scripts/*.py
```

### Generator Smoke Test

```bash
out=$(mktemp -d /tmp/context-forge-rag.XXXXXX)
python3 scripts/generate_profile.py --params templates/profile.params.yaml --output "$out"
python3 "$out/scripts/validate_profile.py" "$out"
```

---

## 4. First Prompts

Once the profile is active, these are productive starting points:

```text
Design a production RAG architecture for customer support knowledge retrieval.
Include ingestion, metadata, evals, observability, and rollout gates.
```

```text
Turn this ambiguous AI feature into 6 implementation-ready GitHub issues
with acceptance criteria and eval requirements.
```

```text
Review my chunking and namespace strategy. Identify failure modes, metrics,
and a safe migration plan.
```

---

## 5. Architecture

The profile operates as a complete agent identity with bundled skills that load contextually based on the task type:

```
context-forge-rag profile
├── principal-ai-architect     → architecture/design tasks
├── technical-roadmapping       → planning/sequencing tasks
├── production-rag-architecture → retrieval design tasks
├── rag-evaluation-observability → eval/metric tasks
└── agentic-workflow-issue-factory → implementation tasks
```

---

## 6. CorpusIQ Use Cases

| Use Case | Profile Application |
|----------|-------------------|
| **CorpusIQ RAG pipeline design** | Design chunking strategy, embedding model selection, hybrid retrieval architecture |
| **Agent evaluation framework** | Define golden datasets, LLM judge rubrics, regression gates for CorpusIQ agents |
| **Feature roadmapping** | Convert operator feedback into sequenced, dependency-mapped GitHub issues |
| **Observability telemetry** | Design cost tracking, trace aggregation, and performance monitoring for agent workflows |
| **ADR documentation** | Produce Architecture Decision Records for key technical choices |

---

## 7. Security

Never commit `.env`, API keys, OAuth tokens, session dumps, private documents, runtime memories, or customer data. The profile is designed to make architecture and implementation artifacts safer, more observable, and easier to evaluate — not to handle secrets.

---

## 8. Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| Profile validation fails | Missing Python packages | `pip install -r requirements.txt` (check repo for requirements) |
| Skills don't load | Profile not active | Run `hermes -p context-forge-rag` or set as default |
| Generator smoke test fails | Template params outdated | Check `templates/profile.params.yaml` for required fields |
| Model errors | Provider not configured | Profile works with any Hermes-supported model provider |

---

*← [Skills Catalog](/hermes/skills/catalog/) | [June 24 Evening Discovery](/hermes/skills/marketplace/new-june24-2026-evening/) →*
