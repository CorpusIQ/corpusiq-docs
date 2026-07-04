---
title: "memoria-vault — Multi-Agent Research OS for Obsidian Setup"
description: "Deploy memoria-vault (4⭐) — seven specialized AI agents that read, enrich, and write inside your Obsidian vault. Turn your notes into an active research laboratory."
skill_name: memoria-vault
category: research-pkm
difficulty: Medium
platforms: [Linux, macOS, Windows]
---

# memoria-vault — Full Setup Guide

**Repo:** [eranroseman/memoria-vault](https://github.com/eranroseman/memoria-vault) | ⭐ 4
**Author:** eranroseman | **Language:** Python
**License:** MIT

memoria-vault is a research operating system for Obsidian. It deploys seven specialized AI agents — Researcher, Summarizer, Linker, Critic, Archivist, Publisher, and Orchestrator — that operate on your Obsidian vault, turning passive notes into an active research laboratory.

---

## Prerequisites

- Python 3.11+
- Obsidian vault (local)
- LLM API key (OpenAI, Anthropic, or local Ollama)
- Hermes Agent or any shell-capable agent (for agent integration)

---

## Installation

```bash
git clone https://github.com/eranroseman/memoria-vault.git
cd memoria-vault
pip install -r requirements.txt
```

---

## Configuration

### 1. Vault Path

Edit `config.yaml`:

```yaml
vault:
  path: "~/Documents/Obsidian/MyVault"  # Absolute path to your vault
  exclude:
    - ".obsidian/"
    - ".trash/"
    - "_templates/"
    - "archive/"
```

### 2. LLM Configuration

```yaml
llm:
  provider: "openai"  # or "anthropic", "ollama"
  model: "gpt-4o"
  api_key: "${OPENAI_API_KEY}"
  
  # For Ollama (local):
  # provider: "ollama"
  # model: "llama3.1:8b"
  # base_url: "http://localhost:11434"
```

### 3. Agent Configuration

Each of the seven agents can be configured independently:

```yaml
agents:
  researcher:
    model: "gpt-4o"           # Uses more capable model for research
    max_sources_per_query: 5
    temperature: 0.3
    
  summarizer:
    model: "gpt-4o-mini"      # Lighter model for summarization
    max_output_tokens: 500
    style: "concise"          # or "detailed", "bullet-points"
    
  linker:
    model: "gpt-4o-mini"
    similarity_threshold: 0.7
    max_links_per_note: 5
    
  critic:
    model: "gpt-4o"
    temperature: 0.7          # Higher temp for creative criticism
    critique_style: "socratic" # or "direct", "steelman"
    
  archivist:
    model: "gpt-4o-mini"
    auto_organize: true
    folder_structure: "para"  # or "flat", "zettle", "custom"
    
  publisher:
    model: "gpt-4o-mini"
    output_formats: ["markdown", "html", "pdf"]
    template_dir: "./templates/publish/"
    
  orchestrator:
    model: "gpt-4o"
    max_concurrent_agents: 3
    workflow_timeout_minutes: 30
```

---

## The Seven Agents

### 1. Researcher
Reads and extracts information from external sources (URLs, PDFs, APIs) and writes findings into your vault.

```bash
# Command
python3 memoria.py research "What are the latest advances in RAG architectures?"

# What it does:
# 1. Searches the web / your configured sources
# 2. Reads and extracts key findings
# 3. Creates a structured note in your vault
```

### 2. Summarizer
Distills long notes or source materials into concise summaries.

```bash
python3 memoria.py summarize "Research/RAG Survey 2026.md"
# Output: Adds a "## Summary" section to the note
```

### 3. Linker
Connects ideas across notes by identifying relationships and creating bidirectional links.

```bash
python3 memoria.py link "Research/RAG Survey 2026.md"
# Output: Identifies related notes and adds [[wikilinks]]
```

### 4. Critic
Challenges assumptions, finds gaps, and provides counter-arguments.

```bash
python3 memoria.py critique "Projects/Q4 Strategy.md"
# Output: Adds a "## Critique" section with challenges and gaps
```

### 5. Archivist
Organizes and maintains the vault — tags, folders, naming conventions, deduplication.

```bash
python3 memoria.py archive
# Output: Reorganizes vault, suggests merges, fixes naming
```

### 6. Publisher
Formats notes for external sharing — blog posts, reports, presentations.

```bash
python3 memoria.py publish "Research/RAG Survey 2026.md" --format html
# Output: Creates Research/RAG Survey 2026.html
```

### 7. Orchestrator
Coordinates multi-agent workflows. Runs the full research pipeline.

```bash
python3 memoria.py orchestrate "Deep dive into transformer alternatives"
# Output: Orchestrates Researcher → Summarizer → Linker → Critic → Publisher
```

---

## Usage Patterns

### Pattern 1: One-Shot Research

```bash
# Full pipeline on a single topic
python3 memoria.py orchestrate "State of AI agents in 2026"
```

### Pattern 2: Incremental Enrichment

```bash
# Research first
python3 memoria.py research "Mamba architecture"

# Link to existing notes
python3 memoria.py link "Research/Mamba.md"

# Get critical feedback
python3 memoria.py critique "Research/Mamba.md"

# Publish when ready
python3 memoria.py publish "Research/Mamba.md"
```

### Pattern 3: Vault Maintenance

```bash
# Weekly organization
python3 memoria.py archive

# Find orphan notes (no incoming links)
python3 memoria.py orphans

# Find stale notes (not modified in 90 days)
python3 memoria.py stale --days 90
```

---

## Integration with Hermes Agent

### As a Hermes Skill

```bash
# Link into Hermes skills
mkdir -p ~/.hermes/skills/memoria-vault
ln -s $(pwd)/memoria.py ~/.hermes/skills/memoria-vault/

# Hermes can now invoke:
# "Research AI agent frameworks and add findings to my Obsidian vault"
# "Summarize my meeting notes from this week"
# "Find connections between RAG and agent architectures in my vault"
```

### Cron-Based Automation

```bash
# Daily vault maintenance at 2 AM
hermes cron create \
  --name "memoria-daily-archive" \
  --schedule "0 2 * * *" \
  --command "cd ~/memoria-vault && python3 memoria.py archive"

# Weekly research digest
hermes cron create \
  --name "memoria-weekly-digest" \
  --schedule "0 9 * * 1" \
  --command "cd ~/memoria-vault && python3 memoria.py orchestrate 'Weekly AI research digest'"
```

---

## Troubleshooting

### "Vault path not found"

Make sure the path is absolute and uses `~` expansion:
```yaml
vault:
  path: "/home/username/Documents/Obsidian/MyVault"  # Use absolute path
```

### "Orchestrator timed out"

The default timeout is 30 minutes. For large research tasks:
```yaml
agents:
  orchestrator:
    workflow_timeout_minutes: 60
```

### "Linker created too many links"

Adjust the similarity threshold:
```yaml
agents:
  linker:
    similarity_threshold: 0.85  # Higher = fewer, higher-quality links
    max_links_per_note: 3       # Hard cap per note
```

### "API rate limited"

The orchestrator can run agents sequentially to avoid rate limits:
```yaml
agents:
  orchestrator:
    max_concurrent_agents: 1    # Sequential execution
    request_delay_seconds: 2    # Pause between LLM calls
```

---

## Security Notes

- The agents read from and write to YOUR vault. Test on a copy first.
- LLM API calls send note content to the provider. Use local Ollama for sensitive vaults.
- The `archivist` agent can reorganize your vault. Always review its suggestions before applying.
- **Back up your vault** before running memoria-vault for the first time.

---

*Guide last updated: July 4, 2026 | [Repo](https://github.com/eranroseman/memoria-vault) | [Report issue](https://github.com/CorpusIQ/corpusiq-docs/issues)*
