---
title: Mac Mini M4 — Worker Node
description: Apple Mac Mini M4 as a dedicated worker node for browser automation, content operations, and GitHub management
---

# Mac Mini M4 — Worker Node

The Apple Mac Mini M4 (16 GB) serves as the dedicated worker node, offloading browser automation, content operations, and GitHub workflows from the primary DGX Spark.

## Responsibilities

### Browser Automation
Running browser-use with Playwright for automated web interactions. Supports persistent browser contexts with session continuity and cookie persistence. Playwright stealth techniques minimize automation detection.

Target platforms: Product Hunt, LinkedIn, TikTok, Instagram, web navigation, and form completion.

### Content Repository
Hosts the Hermes Knowledge Repository (`~/hermes-knowledge-repo/`). All content is authored, committed, and pushed from this machine. GitHub token stored at `~/.github-token`.

### GitHub Operations
Authenticated via personal access token for Ben-Home. Manages repository creation, push operations, PR submissions, and automated content publishing.

### Video Pipeline
Coordinates with HeyGen API for UGC video generation. Scripts and review workflows staged here before distribution.

## Software
- macOS with zsh
- Git for version control
- Python 3 for scripts and automation
- SSH for remote operations from DGX
- Playwright for browser automation

## Connection
Accessible from DGX Spark via SSH: `ssh user@worker-node.local`


---
*Curated in the [Hermes Community Hub](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes) — 308+ tools, skills, and agents. Powered by [CorpusIQ](https://www.corpusiq.io).*


---
*Curated in the [Hermes Community Hub](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes) — 308+ tools, skills, and agents. Powered by [CorpusIQ](https://www.corpusiq.io).*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
