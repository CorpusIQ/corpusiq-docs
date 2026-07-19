---
title: rigorpilot-skills — Scientific AI Research for Hermes (140K installs)
description: Install and use lllllllama/rigorpilot-skills — deep literature reviews, hypothesis generation, experiment reproduction, and methodology validation with academic-grade rigor.
---

# rigorpilot-skills — Setup Guide

**Source:** [lllllllama/rigorpilot-skills](https://github.com/lllllllama/rigorpilot-skills) (140,100 installs)
**Category:** Research / AI
**Languages:** Python

Scientific-grade AI research skills for coding agents. Two complementary capabilities: `ai-research-explore` (140.1K) performs deep literature reviews, hypothesis generation, and gap analysis across academic and technical domains. `ai-research-reproduction` (139.8K) validates research claims by reproducing experiments, checking methodologies, and verifying statistical results. Built on arXiv, PubMed, Semantic Scholar, and Papers With Code APIs.

---

## Installation

```bash
# Deep literature review & research exploration
npx skills add lllllllama/rigorpilot-skills@ai-research-explore

# Experiment reproduction & methodology validation
npx skills add lllllllama/rigorpilot-skills@ai-research-reproduction
```

Verify:
```bash
npx skills list | grep rigorpilot
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Python** | 3.10+ |
| **Hermes Agent** | Any version |
| **arXiv API** | Free, no key required |
| **Semantic Scholar API** | Free, rate-limited (100 req/5min) |
| **Papers With Code** | Free, no key required |
| **Git** | For cloning paper repositories during reproduction |

---

## Key Capabilities

### ai-research-explore: Deep Literature Review

```
┌──────────────────┐     ┌───────────────────┐     ┌──────────────────┐
│  Research Question│ ──▶ │  Multi-Source     │ ──▶ │  Synthesized     │
│  "How do AI       │     │  Search & Analysis │     │  Report + Gaps   │
│   agents reason?" │     │  (5+ databases)    │     │  + Hypotheses    │
└──────────────────┘     └───────────────────┘     └──────────────────┘
```

```bash
# Comprehensive literature review
rigorpilot explore \
  --query "retrieval augmented generation for enterprise knowledge bases" \
  --sources "arxiv,semantic-scholar,paperswithcode,pubmed" \
  --years "2022-2026" \
  --min-citations 5 \
  --output "research/rag-enterprise-review.md"

# Hypothesis generation from research gaps
rigorpilot explore \
  --query "multi-agent coordination protocols" \
  --mode "gap-analysis" \
  --output "research/multi-agent-gaps.md"
```

**Search sources:**
- arXiv (CS, AI, ML, stats)
- Semantic Scholar (all disciplines, citation graph)
- Papers With Code (implementation + benchmarks)
- PubMed (biomedical, clinical AI)
- dblp (computer science bibliography)

**Output includes:**
- Executive summary (3-5 paragraphs)
- Key papers (ranked by citations + relevance)
- Timeline of idea development (citation graph)
- Research gaps (underexplored areas with supporting evidence)
- Testable hypotheses (formatted for grant proposals)
- Full bibliography (BibTeX-ready)

### ai-research-reproduction: Validate Research Claims

```bash
# Reproduce a published experiment
rigorpilot reproduce \
  --paper "https://arxiv.org/abs/2305.12345" \
  --repo "https://github.com/authors/paper-code" \
  --output "research/reproduction-2305.12345/"

# Audit methodology without running code
rigorpilot reproduce \
  --paper "https://arxiv.org/abs/2401.67890" \
  --mode "methodology-audit" \
  --output "research/audit-2401.67890.md"
```

**Reproduction workflow:**
1. Clone repository + install dependencies
2. Locate experiment entry points (training scripts, eval scripts)
3. Run with original parameters on available hardware
4. Compare results to paper claims (within tolerance)
5. Flag discrepancies: missing hyperparameters, cherry-picked results, unreported failures
6. Generate reproducibility report with pass/fail on each claim

**Methodology audit checks:**
- Statistical validity (p-values, effect sizes, confidence intervals)
- Sample size adequacy (power analysis)
- Confounding variables (controlled for? discussed?)
- Ablation completeness (all components tested?)
- Benchmark contamination (training data in test set?)
- Generalization claims (tested beyond original dataset?)

### Citation Graph Analysis

```bash
# Map influence of a seminal paper
rigorpilot explore \
  --paper "https://arxiv.org/abs/1706.03762" \
  --mode "citation-graph" \
  --depth 2 \
  --output "research/attention-is-all-you-need-graph.md"
```

Outputs:
- Direct citations (papers that cite this work)
- Idea lineage (papers this work builds on → papers that build on this)
- Influence score (weighted by citation count and venue prestige)
- Field impact (which subfields cite this most)

---

## Common Workflows for CorpusIQ

### Competitive AI Tool Research

```bash
# Research papers behind competitor tools
rigorpilot explore \
  --query "autonomous agent frameworks production deployment" \
  --sources "arxiv,paperswithcode,semantic-scholar" \
  --years "2024-2026" \
  --output "research/agent-frameworks-landscape.md"

# Check if competitor claims reproduce
rigorpilot reproduce \
  --paper "https://arxiv.org/abs/competitor-paper" \
  --mode "methodology-audit" \
  --output "research/competitor-audit.md"
```

### Technology Evaluation for Product Roadmap

```bash
# Literature review before choosing a tech stack
rigorpilot explore \
  --query "vector database performance comparison production workloads" \
  --sources "arxiv,semantic-scholar" \
  --min-citations 10 \
  --output "research/vector-db-comparison.md"

# Reproduce benchmark claims from vendors
rigorpilot reproduce \
  --paper "https://arxiv.org/abs/vector-db-benchmark" \
  --output "research/vendor-benchmark-validation/"
```

### Content Authority Building

```bash
# Generate research-backed blog content
rigorpilot explore \
  --query "AI impact on business operations productivity" \
  --mode "executive-summary" \
  --output "blog/research/ai-operations-productivity.md"
```

---

## Integration with CorpusIQ Research Stack

| Tool | Role | When to Use |
|---|---|---|
| **rigorpilot-skills** (this) | Academic/scientific research | Deep literature reviews, claim validation |
| **firecrawl-deep-research** (30.5K) | Web research synthesis | Market research, competitive analysis |
| **firecrawl-market-research** (29.4K) | Competitive landscape | Feature comparison, pricing analysis |
| **web-search-duckduckgo** | Quick lookups | Fact checking, current events |
| **arxiv** (built-in) | Paper search | Quick arXiv paper retrieval |

**Recommendation:** Use rigorpilot for "what does the science say?" — validation before making product claims. Use firecrawl-workflows for "what is the market doing?" — competitive positioning. Together they provide both scientific rigor and market awareness.

---

## Comparison: rigorpilot vs firecrawl-deep-research

| Feature | rigorpilot-skills | firecrawl-deep-research |
|---|---|---|
| **Scope** | Academic papers, preprints, journals | Web pages, blogs, documentation |
| **Sources** | arXiv, PubMed, Semantic Scholar, dblp | Web (Firecrawl index) |
| **Citation tracking** | ✅ Full citation graph | ❌ Not applicable |
| **Reproduction** | ✅ Experiment reproduction | ❌ Not applicable |
| **Methodology audit** | ✅ Statistical validation | ❌ Not applicable |
| **Speed** | Slower (academic depth) | Faster (web breadth) |
| **Output format** | Academic (BibTeX, LaTeX-ready) | Business (exec summaries, bullet points) |
| **Install base** | 140K | 30.5K |
| **CorpusIQ use case** | Validate competitor tech claims | Find competitor positioning |

**Recommendation:** Use both. rigorpilot for "is their AI actually better?" — firecrawl for "how do they position it?"

---

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| arXiv API rate limited | Too many rapid requests | Add `--delay 5` between requests |
| Paper reproduction fails | Missing dependencies | Check paper repo for `requirements.txt` or `environment.yml` |
| Semantic Scholar returns 0 results | Query too specific | Broaden query, remove filters, try different keywords |
| Methodology audit incomplete | Paper paywalled | Use preprint version (arXiv), or `--use-preprint` flag |
| Citation graph slow | High-depth traverse | Reduce `--depth` to 1, or limit to top-50 cited papers |
| GPU out of memory on reproduction | Paper used A100, you have T4 | Set `--tolerance-gpu` to skip GPU-bound experiments |

---

## See Also

- [firecrawl-workflows](/hermes/skills/catalog/firecrawl-workflows-setup/) — Web research & market analysis (120K installs)
- [arxiv](/hermes/skills/catalog/) — Built-in arXiv paper search for Hermes
- [web-search-duckduckgo](/hermes/skills/catalog/) — Quick web search for fact checking
- [corpusiq-research-intelligence-framework](/hermes/skills/catalog/) — CorpusIQ's research methodology
