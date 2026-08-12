---
title: Mac Mini M4 — Worker Node Pattern
description: "Apple Mac Mini M4 as a dedicated worker node for browser automation, content operations, and GitHub management in a multi-machine agent setup."
---

# Mac Mini M4 — Worker Node Pattern

The Apple Mac Mini M4 (16 GB) makes an excellent dedicated worker node, offloading browser automation, content operations, and GitHub workflows from a primary GPU workstation.

## Responsibilities

### Browser Automation
Running browser-use with Playwright for automated web interactions. Supports persistent browser contexts with session continuity and cookie persistence. Playwright stealth techniques minimize automation detection.

Target platforms: Product Hunt, LinkedIn, TikTok, Instagram, web navigation, and form completion.

### Content Repository
Hosts a Hermes knowledge repository. All content is authored, committed, and pushed from this machine.

### GitHub Operations
Authenticated via a personal access token. Manages repository creation, push operations, and automated content publishing.

### Video Pipeline
Coordinates with video-generation APIs for UGC video creation. Scripts and review workflows staged here before distribution.

## Software
- macOS with zsh
- Git for version control
- Python 3 for scripts and automation
- SSH for remote operations from the primary node
