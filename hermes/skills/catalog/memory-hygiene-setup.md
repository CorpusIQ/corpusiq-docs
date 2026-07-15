---
title: Memory Hygiene — Setup Guide
description: Audit, clean, and optimize Hermes/Clawdbot vector memory to prevent token waste and performance degradation from memory bloat.
---

# Memory Hygiene — Setup Guide

## Prerequisites
- **Clawdbot / OpenClaw** with LanceDB vector memory (`~/.clawdbot/memory/lancedb/`)
- **Node.js 18+** (for npx)
- Write access to the memory directory

## Capabilities

| Capability | Description |
|-----------|-------------|
| **Memory Audit** | Inspect what's stored in vector memory |
| **Memory Wipe** | Clear all vector memory when bloated |
| **Memory Reseed** | Re-store key facts from MEMORY.md after wipe |
| **Auto-Capture Control** | Disable junk auto-capture while preserving auto-recall |
| **Maintenance Automation** | Set up periodic memory cleanup |

## Installation

```bash
npx skills add aaaaqwq/claude-code-skills/memory-hygiene
```

Verify installation:
```bash
ls ~/.clawdbot/skills/memory-hygiene/SKILL.md
```

## CLI Reference

### Audit Memory
Check what's currently stored in vector memory:
```
memory_recall query="*" limit=50
```

### Wipe Memory
Clear all vector memory when it's bloated with junk:
```bash
rm -rf ~/.clawdbot/memory/lancedb/
clawdbot gateway restart
```

### Reseed Critical Facts
After wiping, re-store essential facts from your MEMORY.md:
```
memory_store text="<key fact>" category="preference|fact|decision" importance=0.9
```

### Disable Auto-Capture (Recommended)
The primary source of memory bloat is `autoCapture: true`. Disable it while keeping auto-recall:

```json
{
  "plugins": {
    "entries": {
      "memory-lancedb": {
        "config": {
          "autoCapture": false,
          "autoRecall": true
        }
      }
    }
  }
}
```

## CorpusIQ Use Cases

1. **Weekly Memory Maintenance:** Schedule a weekly wipe+reseed cycle during low-activity windows. Wipe junk auto-captures, reseed from the Constitution and operating protocol files.

2. **Token Cost Reduction:** Bloated vector memory increases auto-recall payloads, adding 500-2,000 tokens per recall. Regular hygiene cuts this by 60-80%.

3. **Cross-Session Context Quality:** Clean memory = higher-quality auto-recalls. When auto-recall retrieves junk from 3 weeks ago instead of yesterday's decisions, it degrades agent performance.

4. **Memory Migration:** When switching memory backends (LanceDB → Honcho → Sibyl), use the wipe+reseed pattern to cleanly transition.

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| `memory_recall` returns nothing | LanceDB not initialized | Run `clawdbot gateway restart` to recreate DB |
| Token usage still high after wipe | autoCapture still enabled | Check `autoCapture: false` in config |
| Agent forgets recent decisions | Wiped too aggressively | Reseed from MEMORY.md immediately after wipe |
| `rm -rf` permission denied | Gateway process holding file lock | Stop gateway first: `clawdbot gateway stop` |

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace](/hermes/skills/marketplace/) →*
*↑ [Skills Home](/hermes/skills/)*

---

*Curated by CorpusIQ — one MCP endpoint, all your business tools. Content remains attributed to original authors and repositories.*
