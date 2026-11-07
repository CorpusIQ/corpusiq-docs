---
title: "Automation Scripts - CorpusIQ Docs"
description: Utility scripts for ecosystem discovery, agent stack installation, submission processing, and directory promotion
last_updated: 2026-11-06
canonical: "https://www.corpusiq.io/docs/hermes/scripts/"
robots: "index,follow"
tags: ["hermes agent", "ai agent", "nous research"]

---

# Automation Scripts

Utility scripts for maintaining and growing the Hermes ecosystem.

## Scripts

### `discover.py` - Ecosystem Discovery Engine

Scans GitHub for new Hermes-compatible repositories across multiple search queries. Scores repos by relevance (stars, activity, topic match) and outputs a ranked list. Used by the [Ecosystem Discovery Engine](/hermes/ecosystem).

**Usage:**

```bash
python3 discover.py                    # Full discovery run
python3 discover.py --dry-run          # Show what would be added
python3 discover.py --score-only REPO  # Score a single repository
```

### `install-agent-stack.sh` - One-Command Setup

Installs the complete Hermes Agent stack on a fresh Linux machine: Node.js, Python dependencies, Playwright browsers, and the Hermes CLI. Used by the [Setup Guide](/hermes/setup).

**Usage:**

```bash
curl -sL https://raw.githubusercontent.com/CorpusIQ/corpusiq-docs/main/hermes/scripts/install-agent-stack.sh | bash
```

### `process_submissions.py` - Community Submission Pipeline

Validates and ingests community-submitted repositories, skills, and MCP servers. Checks for duplicates, validates metadata, and generates pull requests for approved submissions.

**Usage:**

```bash
python3 process_submissions.py --test   # Score a sample submission end to end
python3 process_submissions.py --issue 12   # Process one specific submission issue
```

### `promote_submission.py` - Human-Judgement Promotion

The submission scorer reads only a repository's name, description, and topics, so a repo that genuinely works with Hermes but never names it in metadata scores low and is rejected. This is the manual path that closes that gap: it takes a repo already in the review queue, records why it was promoted, and rewrites every downstream file in one transaction.

**Usage:**

```bash
python3 promote_submission.py --repo owner/name --note "why this was promoted by hand"
python3 promote_submission.py --repo owner/name --note "reason" --category tools --dry-run
```

### `integrate_approved.py` - Publish Auto-Approved Repos

`discover.py` auto-approves repos into `data/approved_repos.json` but never writes the directory page. This script finds approved repos that are missing from the directory and writes them into `ecosystem/index.md`, star-sorted, using the same block builder as `promote_submission.py`.

**Usage:**

```bash
python3 integrate_approved.py                  # Write all missing approved repos
python3 integrate_approved.py --dry-run        # Show what would be written
python3 integrate_approved.py --limit 20       # Cap the number of entries written
```

### `finish_promotion.py` - Complete a Partial Promotion

`promote_submission.py` writes the JSON stores first and the files last. If the file phase fails, this completes it from the approved row. Safe to rerun: both writers skip work that is already done.

**Usage:**

```bash
python3 finish_promotion.py            # Finish the default pending promotion
python3 finish_promotion.py owner/name # Finish a specific repo
```

## Integration

These scripts are referenced by the [Infrastructure](/hermes/infrastructure) and [Governance](/hermes/governance) documentation. See the [Setup Guide](/hermes/setup) for installation patterns.

---

*← [Templates](/hermes/templates) | [Hermes Home](/hermes) →*

*↑ [Scripts Home](/hermes/scripts)*
