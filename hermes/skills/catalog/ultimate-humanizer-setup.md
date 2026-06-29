---
title: Ultimate Humanizer — Anti-AI-Slop Skill Setup Guide
description: Install and configure ultimate-humanizer — 50 anti-AI-slop patterns, 2-pass self-audit, 5D scoring, and auto-evolution. Works with Hermes, Claude Code, and Open Code.
---

# Ultimate Humanizer — Setup Guide

**Source:** [surdijon/ultimate-humanizer](https://github.com/surdijon/ultimate-humanizer) · 1★
**Category:** Content & Social / Quality Assurance
**License:** MIT · **Published:** June 27, 2026

Detects and removes AI-generated writing patterns ("slop") from text. 50 detection patterns, a 2-pass self-audit, and 5-dimensional scoring (naturalness, variety, agency, specificity, rhythm). Optimized for French but works across languages. Includes Google spam-protection mode for SEO content.

---

## Key Capabilities

### Pattern Detection (50 Patterns)

The skill scans for common AI-isms across five categories:

| Pattern Group | Examples Detected | Count |
|--------------|-------------------|:----:|
| P1-P14: Rhetorical voids | "In today's digital landscape", "It's worth noting that" | 14 |
| P15-P28: False agency | "I'd be happy to", "Let me walk you through" | 14 |
| P29-P38: Binary contrasts | "On one hand / on the other hand" | 10 |
| P39-P44: Meta-commentary | "To summarize", "In conclusion" | 6 |
| P45-P50: SEO spam markers | Keyword stuffing, thin content signals | 6 |

### Intensity Modes

| Mode | Patterns | Use Case |
|------|----------|----------|
| `--lite` | P1-P14 only | Quick polish, short text |
| `--full` (default) | P1-P50 | Standard content editing |
| `--strict` | P1-P50 + active SEO scan | Web/SEO content at risk of Google penalties |

### 5D Scoring

Each text receives scores (0-100) across:
- **Naturalness** — Does it read like a human wrote it?
- **Variety** — Sentence length, structure, vocabulary diversity
- **Agency** — Active voice, concrete subjects, real opinions
- **Specificity** — Facts, numbers, examples vs. vague generalities
- **Rhythm** — Flow, pacing, absence of formulaic transitions

---

## Installation

```bash
npx skills add surdijon/ultimate-humanizer
```

Or direct:

```bash
git clone https://github.com/surdijon/ultimate-humanizer.git
cp ultimate-humanizer/SKILL.md ~/.hermes/profiles/corpusiq/skills/ultimate-humanizer.md
```

---

## Usage with Hermes Agent

Activate with the explicit command:

```
/ultimate-humanizer --full
```

Or in natural language:

```
"Humanize this blog post — run the full anti-slop audit"
"Run ultimate-humanizer in strict mode on this landing page"
```

The skill only activates on explicit invocation — it won't interfere with normal agent operation.

---

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| Blog content QA | Run `--strict` on all published posts before going live |
| Email copy editing | `--lite` pass removes AI-isms from templated emails |
| SEO content audit | `--strict` mode catches patterns that trigger Google spam filters |
| Client deliverables | Ensure human-quality tone in all external-facing content |

---

*This guide is part of the [Hermes Skills Catalog](/hermes/skills/catalog/). Discovered June 29, 2026. Powered by CorpusIQ.*
