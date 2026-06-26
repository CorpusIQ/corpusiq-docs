---
title: CLI-Anything GUI Harnesses — Setup Guide
description: Install and configure 9 CLI-Anything harness skills for Hermes Agent — make Blender, Audacity, ComfyUI, Ollama, NotebookLM, and other GUI apps agent-controllable. 43K⭐ parent ecosystem.
---

# CLI-Anything GUI Harnesses

[CLI-Anything](https://github.com/hkuds/cli-anything) (43,822 stars, arXiv:2606.03854) makes ANY software agent-native by generating CLI harnesses for GUI applications. These 9 skills let Hermes agents control creative tools, productivity apps, and AI infrastructure through standardized command-line interfaces. **Combined installs: 4,769** (plus 43K from parent ecosystem).

---

## Prerequisites

- Hermes Agent installed and running
- [CLI-Anything](https://github.com/hkuds/cli-anything) installed: `pip install cli-anything`
- Each harness requires its target application installed (see below)
- Python 3.10+

---

## Capabilities

| Harness | Target App | What It Enables |
|---|---|---|
| `cli-anything-browser` | Chromium/Firefox | Browser automation via CLI — navigate, extract, screenshot |
| `cli-anything-freecad` | FreeCAD | Parametric 3D modeling — create, modify, export CAD files |
| `cli-anything-ollama` | Ollama | Local LLM management — pull, run, stop models; query endpoints |
| `cli-anything-notebooklm` | Google NotebookLM | Podcast and audio generation from documents |
| `cli-anything-zotero` | Zotero | Reference management — search, cite, organize papers |
| `cli-anything-audacity` | Audacity | Audio editing — cut, filter, normalize, export |
| `cli-anything-shotcut` | Shotcut | Video editing — trim, transition, render, export |
| `cli-anything-comfyui` | ComfyUI | Stable Diffusion workflow — queue prompts, manage models, batch generate |
| `cli-hub-meta-skill` | (meta) | Discover, compare, and manage CLI-Anything harnesses |

---

## Installation

```bash
# Install CLI-Anything core
pip install cli-anything

# Install all 9 harnesses
npx skills add hkuds/cli-anything --skill cli-hub-meta-skill
npx skills add hkuds/cli-anything --skill cli-anything-browser
npx skills add hkuds/cli-anything --skill cli-anything-freecad
npx skills add hkuds/cli-anything --skill cli-anything-ollama
npx skills add hkuds/cli-anything --skill cli-anything-notebooklm
npx skills add hkuds/cli-anything --skill cli-anything-zotero
npx skills add hkuds/cli-anything --skill cli-anything-audacity
npx skills add hkuds/cli-anything --skill cli-anything-shotcut
npx skills add hkuds/cli-anything --skill cli-anything-comfyui
```

---

## CLI Reference

```bash
# Discover available harnesses
hermes skill hkuds/cli-anything/cli-hub-meta-skill

# Browser: navigate and extract
hermes skill hkuds/cli-anything/cli-anything-browser

# Generate AI images via ComfyUI
hermes skill hkuds/cli-anything/cli-anything-comfyui

# Edit audio with Audacity
hermes skill hkuds/cli-anything/cli-anything-audacity

# Manage local LLMs with Ollama
hermes skill hkuds/cli-anything/cli-anything-ollama
```

---

## CorpusIQ Use Cases

| Use Case | Harness | Value |
|---|---|---|
| Automated video production | `cli-anything-shotcut` | Agent-driven video editing without manual GUI interaction |
| AI image generation at scale | `cli-anything-comfyui` | Batch Stable Diffusion workflows controlled by agents |
| Podcast/audio content | `cli-anything-notebooklm`, `cli-anything-audacity` | Generate and edit audio content programmatically |
| Research & citations | `cli-anything-zotero` | Automated reference gathering for content creation |
| Local AI infrastructure | `cli-anything-ollama` | Manage local models without leaving the agent workflow |
| 3D asset creation | `cli-anything-freecad` | Agent-driven CAD modeling for product visualization |

---

## Troubleshooting

| Issue | Fix |
|---|---|
| `cli-anything` command not found | Install the CLI-Anything package globally: `pip install cli-anything` |
| Target app not launching | Each harness requires the specific GUI app installed — check the app's website |
| FreeCAD errors on headless | FreeCAD requires a display — use `xvfb-run` on headless Linux |
| ComfyUI workflow fails | Ensure ComfyUI server is running on the expected port (default: 8188) |

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace](/hermes/skills/marketplace/) →*
