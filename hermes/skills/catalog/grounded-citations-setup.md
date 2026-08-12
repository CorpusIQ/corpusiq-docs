---
title: Grounded Citations — Skill Setup Guide
description: Install and configure grounded-citations, the Hermes Agent skill for inline numbered citations with verifiable source chains — Perplexity-style fact-checking for research and documents — 22 installs.
---

# Grounded Citations — Setup Guide

**Source:** [nousresearch/hermes-agent](https://skills.sh/nousresearch/hermes-agent/grounded-citations) (22 installs)
**Category:** Research / Quality Assurance
**License:** MIT · **Platforms:** Linux, macOS, Windows
**Dependencies:** Hermes Agent, web retrieval tools (web_search/web_extract)

Every claim from an outside source gets an inline numbered citation and a `Sources:` reference list, Perplexity-style. A ledger script owns the `url → [n]` mapping so numbers and URLs come from retrieval, never from model memory. For high-stakes work, the same ledger doubles as a fact-checking chain — verbatim quotes are verified against source text, and model-knowledge claims are flagged `[unverified]`.

---

## What It Does

| Capability | How |
|-----------|-----|
| **Inline citations** | Every external claim gets `[n]` linking to numbered source |
| **Source ledger** | `url → [n]` mapping owned by retrieval, not model memory |
| **Verbatim verification** | Quotes rejected unless they literally appear in fetched text |
| **Unverified flagging** | Model-knowledge claims tagged `[unverified]` |
| **Evidence validation** | `verify --evidence` fails drafts with unsupported claims |
| **Multi-format support** | Works in chat, markdown, PDF, docx, and slides |

---

## How It Works

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  Research     │────▶│  Source       │────▶│  Output       │
│  Question     │     │  Ledger       │     │  with [n]     │
│               │     │  url → [1..N] │     │  citations    │
└──────────────┘     └──────┬───────┘     └──────┬───────┘
                            │                     │
                   ┌────────▼───────┐    ┌────────▼───────┐
                   │  Fetch pages   │    │  verify         │
                   │  Extract text  │    │  --evidence     │
                   └────────────────┘    └────────────────┘
```

---

## Installation

### Via skills.sh (Recommended)

```bash
npx skills add https://github.com/nousresearch/hermes-agent --skill grounded-citations
```

### Direct from Hermes Agent Repo

```bash
git clone --depth 1 https://github.com/nousresearch/hermes-agent.git /tmp/hermes-agent
cp -r /tmp/hermes-agent/skills/research/grounded-citations ~/.hermes/skills/
```

---

## Basic Usage

### Research with citations

```
> Load grounded-citations skill
> Research: What's the current state of RAG retrieval techniques?
> Use grounded citations
```

Hermes will search, fetch pages, extract text, and produce:

```
Recent advances in RAG retrieval have shifted toward agentic
multi-step retrieval [1] and hybrid dense-sparse approaches [2].
ColBERT-style late interaction has shown 15-20% improvement over
single-vector methods on the BEIR benchmark [3].

Sources:
[1] https://arxiv.org/abs/2401.xxxxx — "Agentic RAG: A Survey"
[2] https://blog.langchain.dev/... — Hybrid Search in Production
[3] https://arxiv.org/abs/2004.12832 — ColBERT (original paper)
```

### Verify existing content

```
> Verify the citations in /home/user/report.md --evidence
```

This checks every `[n]` citation — if a claim doesn't trace to source text, it fails.

---

## Citation Format Examples

**In chat:**
```
...as demonstrated by Smith et al. [1].
```

**In markdown:**
```markdown
...as demonstrated by Smith et al. [^1].

[^1]: https://example.com/paper — "Title Here" (2024)
```

**In documents (PDF/docx):**
Superscript numbers with endnote-style source list.

---

## When to Use vs When Not

| ✅ Use For | ❌ Don't Use For |
|-----------|-----------------|
| Research reports & briefings | Casual conversation |
| Factual claims about the world | Personal opinions/advice |
| Content for publication | Creative writing |
| Stakeholder-facing documents | When speed matters more than accuracy |
| Academic or professional writing | Model self-knowledge about its own capabilities |

---

## Integration with Other Skills

| Skill | How It Integrates |
|-------|------------------|
| **research-paper-writing** | Feeds citation chain into academic paper pipeline |
| **arxiv** | Auto-cites arXiv papers with proper BibTeX-ready references |
| **web-search-duckduckgo** | Primary retrieval source for web citations |
| **blogwatcher** | Citations from blog monitoring feeds |

---

## Tips

- **Trust the ledger, not memory:** The `url → [n]` mapping is deterministic — model never invents URLs
- **Verbatim quotes only:** If the text isn't literally in the fetched page, the citation fails
- **`[unverified]` is honest:** Better to flag model knowledge than fabricate a source
- **Re-run `verify --evidence` after edits:** Adding/removing claims may break citation chains
- **Use with `research-paper-writing` for academic work:** This skill handles web citations; that skill adds BibTeX and formatting

---

## Troubleshooting

| Problem | Likely Cause | Fix |
|---------|-------------|-----|
| All citations flagged `[unverified]` | Web retrieval tools down | Check web_search/web_extract availability |
| "Evidence verification failed" | Source page changed since fetch | Re-fetch and re-verify |
| Missing citations in output | Skill not loaded before research | Load skill before starting research |
| Too many citations | Model over-citing | Narrow scope or use `--citation-density low` |

---

*← [Skills Catalog](/hermes/skills/catalog/) | [nousresearch/hermes-agent on skills.sh](https://skills.sh/nousresearch/hermes-agent)*

*Powered by CorpusIQ*
