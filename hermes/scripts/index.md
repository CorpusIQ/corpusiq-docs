---
title: Automation Scripts
description: Utility scripts for ecosystem discovery, agent stack installation, submission processing, and link auditing
last_updated: 2026-07-14
---

# Automation Scripts

Utility scripts for maintaining and growing the Hermes ecosystem.

## Scripts

### `discover.py` — Ecosystem Discovery Engine

Scans GitHub for new Hermes-compatible repositories across multiple search queries. Scores repos by relevance (stars, activity, topic match) and outputs a ranked list. Used by the [Ecosystem Discovery Engine](/hermes/ecosystem/).

**Usage:**

```bash
python3 discover.py --since 2026-07-01 --output discovery-results.json
```

### `install-agent-stack.sh` — One-Command Setup

Installs the complete Hermes Agent stack on a fresh Linux machine: Node.js, Python dependencies, Playwright browsers, and the Hermes CLI. Used by the [Setup Guide](/hermes/setup/).

**Usage:**

```bash
curl -sL https://raw.githubusercontent.com/CorpusIQ/corpusiq-docs/main/hermes/scripts/install-agent-stack.sh | bash
```

### `process_submissions.py` — Community Submission Pipeline

Validates and ingests community-submitted repositories, skills, and MCP servers. Checks for duplicates, validates metadata, and generates pull requests for approved submissions.

**Usage:**

```bash
python3 process_submissions.py --input submissions.jsonl --validate
```

## Integration

These scripts are referenced by the [Infrastructure](/hermes/infrastructure/) and [Governance](/hermes/governance/) documentation. See the [Setup Guide](/hermes/setup/) for installation patterns.

---

*← [Templates](/hermes/templates/) | [Hermes Home](/hermes/) →*

*↑ [Scripts Home](/hermes/scripts/)*
