---
title: Humanizer — Anti-AI-Slop Text Humanizer Setup Guide
description: Install and configure humanizer, the official Hermes Agent skill that strips AI-isms and adds real voice to text. 87 installs, built by Siqi Chen (@blader), ported by Nous Research.
---

# Humanizer — Setup Guide

**Source:** [nousresearch/hermes-agent](https://skills.sh/nousresearch/hermes-agent/humanizer) (87 peak installs)
**Category:** Creative / Writing
**License:** MIT · **Author:** Siqi Chen (@blader), ported by Hermes Agent
**Version:** 2.5.1 · **Platforms:** Linux, macOS, Windows

Identify and remove signs of AI-generated text to make writing sound natural and human. Based on Wikipedia's "Signs of AI writing" guide maintained by WikiProject AI Cleanup, derived from observations of thousands of AI-generated text instances. LLMs use statistical algorithms that tend toward the most likely completion — this skill spots and strips those telltale patterns.

---

## What It Detects & Fixes

| Pattern Category | What It Catches | Fix Applied |
|-----------------|-----------------|-------------|
| **Overused transitions** | "Furthermore," "Moreover," "In conclusion," "Additionally" | Replaced with natural connectors or removed |
| **Hedging language** | "It is worth noting that," "It is important to consider" | Stripped — state the point directly |
| **Forced structure** | "First, ... Second, ... Finally, ..." | Converted to organic paragraph flow |
| **AI vocabulary tells** | "delve," "tapestry," "landscape," "realm," "crucial," "paramount" | Replaced with plain-language alternatives |
| **Overly formal tone** | Academic register when casual is appropriate | Adjusted to match target voice |
| **Repetitive sentence rhythm** | Uniform sentence length and structure | Varied for natural cadence |
| **Fake empathy** | "I understand your frustration," "That's a great question" | Removed unless genuinely warranted |

---

## Installation

### Via skills.sh (Recommended)

```bash
npx skills add nousresearch/hermes-agent --skill humanizer
```

### Direct from Hermes Agent Repo

```bash
# Clone and copy the skill
git clone --depth 1 https://github.com/nousresearch/hermes-agent.git /tmp/hermes-agent
cp -r /tmp/hermes-agent/skills/creative/humanizer ~/.hermes/skills/
```

### Manual (Single Install)

```bash
# Create the skill directory
mkdir -p ~/.hermes/skills/humanizer

# Download SKILL.md
curl -o ~/.hermes/skills/humanizer/SKILL.md \
  https://raw.githubusercontent.com/nousresearch/hermes-agent/main/skills/creative/humanizer/SKILL.md
```

---

## Usage with Hermes Agent

### Trigger Phrases

The skill auto-loads when you ask Hermes to:
- "humanize this text"
- "de-AI this paragraph"
- "make this sound less like ChatGPT"
- "strip the AI-slop from this"
- "rewrite this in my voice"

### Input Methods

| Method | How | Best For |
|--------|-----|----------|
| **Inline** | Paste text directly in chat | Quick edits, short passages |
| **File** | Point at a file path | Documents, blog posts, PR descriptions |
| **Voice calibration** | Provide a writing sample | Matching your specific voice |

### Voice Calibration

For best results matching your personal voice, provide a sample of your own writing:

> "Humanize this blog post, matching the voice in ~/writing-samples/my-style.md"

The skill reads your sample first, extracts voice characteristics, then rewrites accordingly.

### Quick Example

**Input (AI-written):**
> "Furthermore, it is worth noting that the implementation of this innovative solution will undoubtedly revolutionize the landscape of modern computing paradigms."

**Output (humanized):**
> "This solution changes how we think about computing."

---

## Verification

After installation, verify the skill is loaded:

```bash
hermes skills list | grep humanizer
```

Test in a Hermes session:

```
You: Humanize this: "It is crucial to understand that leveraging AI capabilities can significantly enhance organizational productivity metrics."
Hermes: [Returns de-slopped version]
```

---

## Related Skills

- **[songwriting-and-ai-music](https://skills.sh/nousresearch/hermes-agent/songwriting-and-ai-music)** — AI music generation with similar creative voice control
- **[ultimate-humanizer](ultimate-humanizer-setup.md)** — Community alternative with 50 patterns and 5D scoring
- **[research-paper-writing](https://skills.sh/nousresearch/hermes-agent/research-paper-writing)** — Academic writing with the same anti-AI-slop pass

---

## Pro Tips

1. **Run a pre-publish pass** — Load humanizer before sending any user-facing text (release notes, docs, PR descriptions).
2. **Combine with voice calibration** — The 5-minute investment of providing a writing sample pays off in every subsequent humanization.
3. **Not just for English** — The patterns are language-agnostic; the skill works across any language the underlying model supports.
4. **Iterative refinement** — Run the humanizer, read the result, then ask for specific adjustments ("make it more casual," "shorter sentences," "add more personality").
