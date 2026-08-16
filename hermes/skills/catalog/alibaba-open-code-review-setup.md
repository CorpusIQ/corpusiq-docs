---
title: "Alibaba Open Code Review — AI Code Review CLI Setup"
description: "alibaba/open-code-review — 2 skills, 4.3K installs: Git-diff AI code review with structured line-level comments from Alibaba."
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/alibaba-open-code-review-setup/"
robots: "index,follow"
last_updated: "2026-08-16"
tags: ["hermes skill", "agent skill", "skill setup", "code review", "alibaba"]
---

# Alibaba Open Code Review — Setup Guide

**Source:** [alibaba/open-code-review](https://skills.sh/alibaba/open-code-review)
**GitHub:** [alibaba/open-code-review](https://github.com/alibaba/open-code-review)
**Skills:** 2 skills · 4.3K total installs
**Category:** Code Review
**First Seen:** catalogued August 16, 2026 sweep (open-code-review on skills.sh since May 29, 2026)
**Quality Tier:** 🟡 Trusted — official Alibaba org; top skill carries a Snyk Fail (see Limitations)

Alibaba's open-code-review (`ocr`) is an open-source AI code review CLI that reads Git diffs and produces structured, line-level review comments — a machine-reviewable format that plugs into PR pipelines. The skill wraps the CLI with environment verification and review workflows.

---

## Installation

```bash
npx skills add alibaba/open-code-review
```

Individual skills install with the explicit repo form:

```bash
npx skills add https://github.com/alibaba/open-code-review --skill open-code-review
```

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js + npx** | For the skill installer |
| **ocr CLI** | Install the `ocr` binary (skill walks through setup) |
| **LLM connectivity** | Verified with `ocr llm test` before any review |

## What It Provides

| Skill | Installs | Purpose |
|---|---|---|
| open-code-review | 3.5K | Core review workflow: reads Git diffs, generates line-level comments, reports findings |
| open-code-review-delegate | 784 | Delegation pattern for multi-agent review |

The skill's environment check runs first (`which ocr`, then `ocr llm test`) and blocks review if the CLI or LLM link is down — a verification discipline consistent with our own pre-flight gates.

## Quick Start

1. Install: `npx skills add alibaba/open-code-review`
2. Verify environment: `which ocr && ocr llm test`
3. Ask: "review this branch's diff with open-code-review and format findings as PR comments"

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **PR security gate** | A second, independent review path alongside our existing review workflow |
| **Diff-level review** | Line-level structured comments integrate cleanly with GitHub review UIs |
| **Multi-agent review** | open-code-review-delegate as a review sub-agent pattern |

## Limitations / Verification

- Security audits on open-code-review: Gen Agent Trust Hub Pass, Socket Pass, **Snyk Fail** — trusted with the Snyk finding named; review the dependency surface before production use
- Publisher-page install counts verified (3.5K + 784); GitHub 20.5K stars on the repo
- Requires external LLM connectivity configured for the `ocr` CLI
- Two-skill suite; delegate skill is sub-1K installs

```bash
npx skills add alibaba/open-code-review   # verify install works
```

## Related

- [Skills Catalog](/hermes/skills/catalog/)
- [Skills Marketplace](/hermes/skills/marketplace/)

*Powered by CorpusIQ*
