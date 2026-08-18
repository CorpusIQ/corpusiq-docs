---
title: "ascii-art — Setup Guide - CorpusIQ Docs"
description: Generate ASCII art, banners, and text-based graphics — terminal-native visual output for Hermes agents.
canonical: "https://www.corpusiq.io/docs/hermes/skills/catalog/ascii-art-setup/"
robots: "index,follow"
last_updated: "2026-08-12"
tags: ["hermes skill", "agent skill", "skill setup"]

---

# ascii-art — Setup Guide

**Source:** [nousresearch/hermes-agent](https://github.com/nousresearch/hermes-agent)
**Skill:** `ascii-art`
**Installs:** 338

The `ascii-art` skill enables Hermes agents to generate ASCII art, text banners, terminal graphics, and decorative text output. Ideal for terminal-native applications, CLI tool headers, markdown decoration, and creative text-based visualization.

## Installation

```bash
npx skills add https://github.com/nousresearch/hermes-agent --skill ascii-art
```

After install, reload skills:
- Hermes CLI: `/reload-skills` or restart session
- Hermes gateway: `/restart` or `hermes gateway restart`

## Prerequisites

| Requirement | Details |
|-------------|---------|
| Hermes Agent | v0.20.0+ |
| Terminal | Unicode-capable terminal for best results |
| Python (optional) | For FIGlet/pyfiglet integration: `pip install pyfiglet` |

## Capabilities

| Capability | Trigger | Output |
|-----------|---------|--------|
| Banner text | "Create a banner that says CORPUSIQ" | Large ASCII text banner |
| Box drawing | "Put this in a framed box" | Text surrounded by box-drawing chars |
| Logo generation | "Create an ASCII logo for Hermes" | Custom ASCII logo/art |
| Table formatting | "Display this as an ASCII table" | Formatted table with borders |
| Progress bars | "Show progress visually" | ASCII progress/loading bar |
| Decorative dividers | "Add a section divider" | Themed horizontal rules |

## Key Features

- **Multiple fonts**: FIGlet integration for dozens of text styles
- **Box styles**: Single/double line, rounded, bold, dashed borders
- **Color support**: ANSI color codes for terminal output
- **Markdown-compatible**: Most ASCII art renders correctly in markdown code blocks
- **Unicode blocks**: Full block characters for smoother gradients and shapes

## Fonts Available (FIGlet)

Standard, slant, mini, big, block, bubble, digital, ivrit, lean, script, shadow, small, smscript, smshadow, smslant, standard, term

## CLI/Command Reference

The skill surfaces through Hermes' text generation:
- ASCII art appears in regular text output
- Combine with `terminal()` for FIGlet: `figlet -f slant "CORPUSIQ"`
- Python integration: `pyfiglet.figlet_format("text", font="slant")`
- Use in `write_file()` for headers in generated markdown/docs

## CorpusIQ Use Cases

1. **CLI tool headers** — Branded headers for CorpusIQ terminal tools
2. **README decoration** — ASCII logos and dividers in GitHub READMEs
3. **Report formatting** — Visual section breaks in automated reports
4. **Terminal UI** — Progress indicators in agent terminal output
5. **Social media** — ASCII art for text-only platforms (HN, Reddit comments)
6. **Docs branding** — ASCII logos in corpusiq-docs sidebars

## Troubleshooting

| Issue | Likely Cause | Resolution |
|-------|-------------|------------|
| Garbled output | Terminal missing Unicode support | Use basic ASCII chars only |
| Alignment off | Variable-width fonts | Switch to monospace font |
| FIGlet not found | Missing figlet package | `apt install figlet` or `pip install pyfiglet` |

## Verification

After installation, verify the skill is loaded:
```bash
hermes skills list | grep ascii-art
```

Test with a banner request:
```
"Create a large ASCII banner that says HERMES in the slant font"
```
