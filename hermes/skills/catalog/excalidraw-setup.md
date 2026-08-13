---
title: excalidraw — Setup Guide
description: Generate Excalidraw diagrams, sketches, and wireframes from text descriptions — visual thinking for Hermes agents.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/excalidraw-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# excalidraw — Setup Guide

**Source:** [nousresearch/hermes-agent](https://github.com/nousresearch/hermes-agent)
**Skill:** `excalidraw`
**Installs:** 342

The `excalidraw` skill allows Hermes agents to create hand-drawn style diagrams, wireframes, flowcharts, and sketches directly from text descriptions. Uses the Excalidraw library for the distinctive sketch-like aesthetic that communicates "work in progress" and encourages collaboration.

## Installation

```bash
npx skills add https://github.com/nousresearch/hermes-agent --skill excalidraw
```

After install, reload skills:
- Hermes CLI: `/reload-skills` or restart session
- Hermes gateway: `/restart` or `hermes gateway restart`

## Prerequisites

| Requirement | Details |
|-------------|---------|
| Hermes Agent | v0.20.0+ |
| Canvas | Diagram concept or architecture to visualize |

## Capabilities

| Capability | Trigger | Output |
|-----------|---------|--------|
| Architecture diagram | "Diagram the CorpusIQ MCP architecture" | Excalidraw file or exported PNG |
| Flowchart | "Map the user onboarding flow" | Process flowchart |
| Wireframe | "Wireframe a dashboard layout" | Low-fidelity UI wireframe |
| System diagram | "Show how services connect" | System architecture diagram |
| Mind map | "Map out the growth strategy" | Visual mind map |
| Sequence diagram | "Show the OAuth flow" | Sequence/timeline diagram |

## Key Features

- **Hand-drawn aesthetic**: Sketch-like lines that signal draft status
- **JSON-native**: Excalidraw files are plain JSON — easy to version in git
- **Export options**: PNG, SVG, or embeddable links
- **Library integration**: Rich shape library with custom components
- **Collaboration**: Live multi-user editing via excalidraw.com

## CLI/Command Reference

The skill integrates with Hermes' file and rendering tools:
- Diagrams are written as `.excalidraw` JSON files
- Export via Excalidraw API or browser automation
- Combine with `browser_use` to automate Excalidraw.com exports
- Embed in docs with `markdown-viewer` skill for rich rendering

## CorpusIQ Use Cases

1. **Architecture documentation** — System diagrams for corpusiq-docs
2. **Product specs** — Wireframes for new features under development
3. **Client deliverables** — Architecture diagrams for enterprise proposals
4. **Internal communication** — Flowcharts for growth and product processes
5. **Pitch decks** — Visual diagrams for investor and partner presentations
6. **Technical blog posts** — Diagrams for the CorpusIQ engineering blog

## Troubleshooting

| Issue | Likely Cause | Resolution |
|-------|-------------|------------|
| JSON parse errors | Malformed Excalidraw structure | Validate against Excalidraw schema |
| Export fails | Missing browser | Use `browser_use` or `browser_navigate` |
| Shapes misaligned | Coordinate overflow | Keep diagrams under 2000x2000 px |

## Verification

After installation, verify the skill is loaded:
```bash
hermes skills list | grep excalidraw
```

Test with a diagram request:
```
"Create an Excalidraw diagram of the CorpusIQ system architecture showing MCP server, agents, and connectors"
```
