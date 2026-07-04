---
title: "Hermes ArXiv Agent — ArXiv Paper Fetcher Setup"
description: "Set up the Hermes ArXiv Agent (91⭐) to automatically fetch papers from arXiv, generate AI summaries, push to Feishu, and host a local reading website."
skill_name: hermes-arxiv-agent
category: research
difficulty: Medium
platforms: [Linux, macOS]
---

# Hermes ArXiv Agent — Full Setup Guide

**Repo:** [genggng/hermes-arxiv-agent](https://github.com/genggng/hermes-arxiv-agent) | ⭐ 91
**Author:** genggng | **Language:** Python
**License:** MIT

The Hermes ArXiv Agent is a Hermes skill that automates the academic paper pipeline: daily arXiv fetching, AI-generated Chinese summaries with author affiliations, Feishu (Lark) notifications, and a local static reading website.

---

## Prerequisites

- Python 3.11+
- Hermes Agent installed
- Feishu/Lark bot (for notifications — optional)
- Internet access for arXiv API

---

## Installation

```bash
git clone https://github.com/genggng/hermes-arxiv-agent.git
cd hermes-arxiv-agent
pip install -r requirements.txt
```

---

## Configuration

### 1. arXiv Categories

Edit `config.yaml` to set your categories:

```yaml
arxiv:
  categories:
    - cs.AI        # Artificial Intelligence
    - cs.CL        # Computation and Language
    - cs.LG        # Machine Learning
    - stat.ML      # Machine Learning (Statistics)
  max_results: 50
  fetch_time: "08:00"  # Daily fetch time (UTC)
```

Common categories:
| Code | Field |
|------|-------|
| `cs.AI` | Artificial Intelligence |
| `cs.CL` | Computation & Language (NLP) |
| `cs.CV` | Computer Vision |
| `cs.LG` | Machine Learning |
| `cs.SE` | Software Engineering |
| `stat.ML` | ML (Statistics) |
| `math.OC` | Optimization & Control |

### 2. AI Summary Provider

Configure the AI backend for generating summaries:

```yaml
ai:
  provider: "openai"  # or "deepseek", "ollama", "anthropic"
  model: "gpt-4o"
  api_key: "${OPENAI_API_KEY}"
  summary_language: "zh"  # "zh" for Chinese, "en" for English
  max_tokens: 500
```

### 3. Feishu/Lark Notification (Optional)

```yaml
feishu:
  enabled: true
  webhook_url: "https://open.feishu.cn/open-apis/bot/v2/hook/xxxxx"
  secret: "your-bot-secret"
```

### 4. Local Website

```yaml
website:
  enabled: true
  output_dir: "./public"
  host: "0.0.0.0"
  port: 8080
  title: "My ArXiv Feed"
```

---

## Usage

### Install as Hermes Skill

```bash
# Copy skill to Hermes skills directory
cp -r hermes-arxiv-agent ~/.hermes/profiles/default/skills/

# Or link it
ln -s $(pwd) ~/.hermes/profiles/default/skills/hermes-arxiv-agent
```

### Manual Run

```bash
# Fetch papers for today
python3 fetch.py

# Generate summaries
python3 summarize.py

# Build static website
python3 build_site.py

# Send Feishu notification
python3 notify.py
```

### Scheduled via Hermes Cron

```bash
# Create a daily cron job
hermes cron create \
  --name "arxiv-daily-fetch" \
  --schedule "0 8 * * *" \
  --command "cd ~/hermes-arxiv-agent && python3 fetch.py && python3 summarize.py && python3 notify.py"
```

---

## Output Structure

After running, your directory will look like:

```
hermes-arxiv-agent/
├── papers/
│   ├── 2026-07-04/
│   │   ├── 2401.12345.json      # Raw paper metadata
│   │   ├── 2401.12345_summary.md # AI-generated summary
│   │   └── ...
│   └── index.json                # All-time index
├── public/                       # Static website
│   ├── index.html
│   ├── papers/
│   └── assets/
└── logs/
    └── fetch.log
```

---

## Feishu Notification Format

Each notification card includes:
- Paper title (with arXiv link)
- AI summary (Chinese by default)
- Authors and affiliations
- Categories and keywords
- PDF link

---

## Troubleshooting

### "arXiv API rate limited"

arXiv allows ~1 request per 3 seconds. The agent includes built-in rate limiting. If you still hit limits:
```yaml
arxiv:
  request_delay: 5  # Increase delay between requests
```

### "Feishu webhook returns 403"

Check that:
1. The webhook URL is correct
2. The bot has permission to post in the target chat
3. The secret is configured (if secret-mode webhook)

### "Chinese summaries are low quality"

Try a different model or increase max_tokens:
```yaml
ai:
  model: "deepseek-chat"  # Strong Chinese performance
  max_tokens: 800
```

### "Static site not rendering"

Make sure the `public/` directory is writable and you have basic HTML templates in `templates/`.

---

## Alternatives

| Tool | Language | Notes |
|------|----------|-------|
| hermes-arxiv-agent | Python/Chinese | This guide |
| arxiv-sanity | Python/English | Andrej Karpathy's arxiv browser |
| Semantic Scholar API | REST | Academic paper search |
| Paper Digest | SaaS | Auto-summarization service |

---

*Guide last updated: July 4, 2026 | [Repo](https://github.com/genggng/hermes-arxiv-agent) | [Report issue](https://github.com/CorpusIQ/corpusiq-docs/issues)*
