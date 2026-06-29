---
title: arXiv — Academic Paper Search Setup Guide
description: Install and configure arxiv, the official Hermes Agent skill for searching academic papers via arXiv's free REST API. 77 installs, zero dependencies, no API key needed.
---

# arXiv Research — Setup Guide

**Source:** [nousresearch/hermes-agent](https://skills.sh/nousresearch/hermes-agent/arxiv) (77 peak installs)
**Category:** Research / Academic
**License:** MIT · **Platforms:** Linux, macOS, Windows
**Dependencies:** None (curl only)

Search and retrieve academic papers from arXiv via their free REST API. No API key, no Python packages, no authentication — just curl and the arXiv API. Returns Atom XML with paper metadata, abstracts, and links to full-text PDFs.

---

## What It Does

| Capability | How |
|-----------|-----|
| **Keyword search** | Search by title, abstract, author, or full text |
| **Author lookup** | Find all papers by a specific researcher |
| **Category browse** | Filter by arXiv category (cs.AI, stat.ML, etc.) |
| **Paper by ID** | Retrieve exact paper by arXiv ID |
| **Abstract extraction** | Get clean abstract text via web extraction |
| **Full-text access** | Fetch PDF via arXiv's CDN |

---

## Installation

### Via skills.sh (Recommended)

```bash
npx skills add nousresearch/hermes-agent --skill arxiv
```

### Direct from Hermes Agent Repo

```bash
git clone --depth 1 https://github.com/nousresearch/hermes-agent.git /tmp/hermes-agent
cp -r /tmp/hermes-agent/skills/research/arxiv ~/.hermes/skills/
```

### Manual (Single Install)

```bash
mkdir -p ~/.hermes/skills/arxiv
curl -o ~/.hermes/skills/arxiv/SKILL.md \
  https://raw.githubusercontent.com/nousresearch/hermes-agent/main/skills/research/arxiv/SKILL.md
```

---

## Usage with Hermes Agent

### Quick Reference

| Action | Command / Prompt |
|--------|-----------------|
| Search papers | "Search arXiv for GRPO reinforcement learning papers" |
| Get specific paper | "Get arXiv paper 2402.03300" |
| Read abstract | "Show me the abstract of the latest RAG survey on arXiv" |
| Author search | "Find papers by Yann LeCun on arXiv" |
| Category filter | "Show me recent cs.CL papers about transformer architectures" |

### API Commands (Behind the Scenes)

```bash
# Search papers
curl -s "https://export.arxiv.org/api/query?search_query=all:GRPO+reinforcement+learning&max_results=5&sortBy=submittedDate&sortOrder=descending"

# Get specific paper
curl -s "https://export.arxiv.org/api/query?id_list=2402.03300"

# Search by author
curl -s "https://export.arxiv.org/api/query?search_query=au:lecun&max_results=5"

# Filter by category
curl -s "https://export.arxiv.org/api/query?search_query=cat:cs.AI+AND+all:attention+mechanism&max_results=5"
```

### Clean Output (Parse XML)

The API returns Atom XML. Hermes auto-parses this, but you can also pipe through Python:

```bash
curl -s "https://export.arxiv.org/api/query?search_query=all:GRPO&max_results=3&sortBy=submittedDate&sortOrder=descending" | python3 -c "
import sys, xml.etree.ElementTree as ET
ns = {'atom': 'http://www.w3.org/2005/Atom'}
root = ET.fromstring(sys.stdin.read())
for entry in root.findall('atom:entry', ns):
    title = entry.find('atom:title', ns).text.strip().replace('\n', ' ')
    authors = [a.find('atom:name', ns).text for a in entry.findall('atom:author', ns)]
    link = entry.find('atom:id', ns).text
    print(f'{title}')
    print(f'  Authors: {', '.join(authors[:3])}')
    print(f'  ID: {link.split('/')[-1]}')
    print()
"
```

---

## Search Tips

### arXiv Categories

| Category | Field |
|----------|-------|
| `cs.AI` | Artificial Intelligence |
| `cs.CL` | Computation and Language (NLP) |
| `cs.LG` | Machine Learning |
| `cs.CV` | Computer Vision |
| `stat.ML` | Machine Learning (Statistics) |
| `cs.SE` | Software Engineering |
| `cs.CR` | Cryptography and Security |

### Search Operators

| Operator | Example | Effect |
|----------|---------|--------|
| `all:` | `all:transformer` | Search all fields |
| `ti:` | `ti:GRPO` | Title only |
| `au:` | `au:bengio` | Author name |
| `abs:` | `abs:benchmark` | Abstract only |
| `cat:` | `cat:cs.AI` | Category filter |
| `AND` | `all:RL AND cat:cs.LG` | Both conditions |
| `ANDNOT` | `all:transformer ANDNOT cat:cs.CL` | Exclude category |

---

## Verification

```bash
# Check skill is installed
hermes skills list | grep arxiv

# Test API directly
curl -s "https://export.arxiv.org/api/query?search_query=all:test&max_results=1" | grep -c "<entry>"
# Expected: 1
```

---

## Related Skills

- **[ocr-and-documents](https://skills.sh/nousresearch/hermes-agent/ocr-and-documents)** — Extract text from academic PDFs and scanned documents
- **[research-paper-writing](https://skills.sh/nousresearch/hermes-agent/research-paper-writing)** — Write academic papers with proper formatting
- **[llm-wiki](https://skills.sh/nousresearch/hermes-agent/llm-wiki)** — Build a personal research wiki from collected papers

---

## Pro Tips

1. **Use `sortBy=submittedDate`** — Always sort by date for literature reviews. Default is relevance, which biases toward older highly-cited papers.
2. **Limit `max_results`** — arXiv's API is rate-limited. Start with `max_results=5` and increase only if needed.
3. **Cache results** — For literature reviews, save the XML output to a file and process locally rather than re-querying.
4. **Read PDFs via web_extract** — After finding a paper, use `web_extract(urls=["https://arxiv.org/pdf/PAPER_ID"])` to get the full text without downloading.
5. **Combine with humanizer** — Use the humanizer skill to convert academic abstracts into plain-language summaries.
