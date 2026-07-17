---
title: Remotion Best Practices — Setup Guide for Hermes Video Automation
description: Install and use remotion-dev/skills@remotion-best-practices (430K installs) for programmatic video creation in Hermes. Composition patterns, rendering optimization, audio sync, and caption generation.
---

# Remotion Best Practices — Setup Guide

**Source:** [remotion-dev/skills](https://github.com/remotion-dev/skills) (430,200 installs)
**Category:** Video Production
**Languages:** TypeScript + React

Official Remotion best practices for AI coding agents. Covers the complete programmatic video creation lifecycle: composition structure, rendering optimization, audio synchronization, caption generation, and asset management. Used by HeyGen HyperFrames, Google Labs Stitch, and thousands of production AI video pipelines.

---

## Installation

```bash
npx skills add remotion-dev/skills@remotion-best-practices
```

Verify:
```bash
npx skills list | grep remotion-best-practices
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Node.js** | 18+ (for Remotion runtime) |
| **FFmpeg** | Required for rendering and audio processing |
| **Remotion** | `npm install remotion @remotion/cli` in your project |
| **Hermes Agent** | Any version — CLI invocation |
| **HyperFrames** | Optional — if using CorpusIQ's video pipeline |

Install FFmpeg if missing:
```bash
# Linux
sudo apt install ffmpeg

# macOS
brew install ffmpeg
```

---

## Key Capabilities

### Composition Patterns

| Pattern | When to Use | Key Rule |
|---|---|---|
| **`<Composition>`** | Root container for every video | Always set `fps`, `durationInFrames`, `width`, `height` |
| **`<Sequence>`** | Timeline-arranged clips | `from` + `durationInFrames` must not overlap incorrectly |
| **`<AbsoluteFill>`** | Full-frame backgrounds | Prefer over manual `position: absolute` styling |
| **`<Series>`** | Auto-sequenced clips | No manual `from` calculation needed |
| **`<Loop>`** | Repeating animations | Set `durationInFrames` to avoid infinite loops |

### Rendering Optimization

```typescript
// ✅ CORRECT: Parallel rendering with concurrency control
npx remotion render --concurrency=4 --scale=0.5

// ❌ WRONG: Unbounded concurrency saturates CPU
npx remotion render --concurrency=16  // Avoid
```

| Optimization | Command / Config | Impact |
|---|---|---|
| **Scale down** | `--scale=0.5` | 4x faster previews |
| **Concurrency** | `--concurrency=<CPU cores - 1>` | Linear speedup |
| **Codec choice** | `--codec=h264` for web, `prores` for editing | File size vs quality |
| **Caching** | `--gl=angle` on Windows, Chromium rendering | Skip re-renders |
| **Off-thread audio** | `RenderMediaOptions.offthreadAudioCacheSizeInBytes` | Prevents audio stutter |

### Audio Workflow

```typescript
import { useAudioData, visualizeAudio } from '@remotion/media-utils';

// ✅ CORRECT: Proper audio loading with error handling
const audioData = useAudioData(audioSrc);
if (!audioData) return null; // Loading state

// ✅ CORRECT: Audio visualization with proper sizing
const visualization = visualizeAudio({
  fps: 30,
  frame,
  audioData,
  numberOfSamples: 64,
});

// ❌ WRONG: Blocking audio load on main thread
const audio = new Audio(src); // Don't use browser Audio API
```

### Caption Generation

```typescript
// ✅ CORRECT: Word-level timing with animation
const { captions } = await parseSrt(fetch(srtUrl));
const currentCaption = captions.find(
  c => frame >= c.startMs / (1000 / fps) && frame <= c.endMs / (1000 / fps)
);

// ❌ WRONG: Manual timing calculations (off-by-one prone)
const time = frame / fps; // Doesn't account for SRT millisecond offsets
```

---

## Common Pitfalls

| Pitfall | Symptom | Fix |
|---|---|---|
| **Duration mismatch** | Video cuts off early or extends with black frames | `durationInFrames` must match `fps * duration_seconds` |
| **Frame rate drop** | Choppy output at >30fps | Lower concurrency, use `--scale=0.5` for previews |
| **Memory leak** | OOM on renders >5 minutes | Use `--every-nth-frame=2` for draft, stagger asset loading |
| **Audio drift** | Audio desyncs from video after 30s | Use `offthreadAudioCacheSizeInBytes`, avoid sample rate mismatch |
| **Static file 404** | Assets missing in production | Use `staticFile()` for local assets, not `fetch()` |
| **`useCurrentFrame()` outside Composition** | Blank render | Only call inside `<Composition>` children |

---

## Hermes/CorpusIQ Relevance

**UGC Video Pipeline:** CorpusIQ's daily video series uses HyperFrames (Remotion-based). These best practices prevent frame drops, audio drift, and memory leaks that caused earlier automation failures.

**Content Production:** The caption generation patterns directly apply to TikTok/Instagram Reels — word-level timing with animation presets for engagement.

**Rendering at Scale:** The concurrency and caching optimizations reduce render costs by 60-80% for the daily video pipeline (15 videos/day across 3 platforms).

---

## See Also

- [HyperFrames Setup](/hermes/skills/catalog/hyperframes-setup/) — HeyGen's Remotion-based video framework
- [Video Skill](/hermes/skills/catalog/video/) — Hermes native video capabilities
- [Remotion Documentation](https://remotion.dev/docs) — Official reference
