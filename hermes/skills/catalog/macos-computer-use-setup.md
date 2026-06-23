---
title: macos-computer-use Setup Guide
description: Complete setup guide for the macos-computer-use skill from nousresearch/hermes-agent. Drive macOS desktop automation  --  screenshots, mouse, keyboard, scroll, drag  --  without stealing user focus.
---

# macos-computer-use Setup

**Source:** [nousresearch/hermes-agent](https://github.com/nousresearch/hermes-agent)
**Skills.sh:** [macos-computer-use](https://skills.sh/nousresearch/hermes-agent/macos-computer-use)
**Installs:** 134

## 1. Installation

```bash
npx skills add nousresearch/hermes-agent --skill macos-computer-use
```

## 2. Prerequisites

| Requirement | Details |
|-------------|---------|
| macOS | Required  --  this skill drives native macOS desktop |
| Accessibility permissions | System Preferences → Privacy & Security → Accessibility  --  grant to Terminal/Hermes |
| Screen Recording permission | System Preferences → Privacy & Security → Screen Recording |
| `computer_use` tool | Must be enabled in Hermes tool config |
| No external API keys | Local-only  --  no cloud dependency |

## 3. Capabilities

| Capability | Trigger | Notes |
|-----------|---------|-------|
| Screenshot capture | "take a screenshot" | Full screen or region; returned for vision analysis |
| Mouse control | "click on X", "move to Y" | Absolute coordinates + UI element targeting |
| Keyboard input | "type X", "press Enter" | Full keyboard simulation including shortcuts |
| Scroll | "scroll down" | Smooth scrolling with configurable speed |
| Drag operations | "drag X to Y" | Click-and-drag for file movement, UI manipulation |
| Background operation | Automatic | Never steals cursor, keyboard focus, or Space |

## 4. CLI / Command Reference

```bash
# Skills are auto-loaded when computer_use tool is available
# No manual CLI commands  --  the skill enhances the existing computer_use tool

# In a Hermes session:
# "Take a screenshot of my desktop"
# "Click on the Safari icon in the Dock"
# "Open System Preferences → Network"
# "Scroll down in the current window"
# "Type 'Hello World' in the focused text field"

# The skill works with ANY tool-capable model  --  no model-specific requirements
```

## 5. CorpusIQ Use Cases

| Use Case | How It Works |
|----------|-------------|
| **Browser testing** | Drive Safari/Chrome to test CorpusIQ web app on real macOS rendering |
| **Desktop automation** | Automate repetitive macOS tasks  --  file organization, app launching, window management |
| **Visual QA** | Screenshot comparisons for UI regression testing |
| **Data extraction** | Screenshot + OCR for data trapped in desktop apps |
| **Demo recording prep** | Set up desktop state for screen recordings automatically |

## 6. Troubleshooting

| Issue | Solution |
|-------|----------|
| "No accessibility permission" | Grant in System Preferences → Privacy → Accessibility → add Terminal.app and/or Hermes |
| Screenshots are black | Grant Screen Recording permission; restart Terminal |
| Mouse clicks at wrong position | Use "take a screenshot first" so the model can see current layout before clicking |
| Keyboard input not registering | Ensure the target window has focus; use "click on [window]" first |
| "computer_use tool not available" | Check Hermes config.yaml  --  `tools.computer_use` must be enabled |
| Slow operation | Reduce screenshot frequency; use coordinates directly for repetitive tasks |

**Verification:**
```bash
# Verify skill installed
npx skills list | grep macos-computer-use

# Test basic operation in Hermes session:
# "Take a screenshot of my desktop"
# Should return a screenshot image  --  confirms permissions are working
```

*Part of the [Hermes Skills Library](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/skills)  --  133+ agent skills. Built by [CorpusIQ](https://www.corpusiq.io).*

*Part of the [Hermes Skills Library](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/skills)  --  133+ agent skills. Built by [CorpusIQ](https://www.corpusiq.io).*
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
