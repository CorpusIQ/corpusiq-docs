---
title: HeartMuLa — Skill Setup Guide
description: Install and configure heartmula, the Hermes Agent skill for open-source AI music generation with HeartMuLa models — Apache 2.0 licensed, Suno alternative — 224 installs.
---

# HeartMuLa — Open-Source Music Generation Setup Guide

**Source:** [nousresearch/hermes-agent](https://skills.sh/nousresearch/hermes-agent/heartmula) (224 installs)
**Category:** Creative / AI Music
**License:** Apache 2.0 · **Platforms:** Linux (CUDA recommended)
**Dependencies:** Python 3.10+, CUDA GPU (recommended), 16GB+ RAM

Generate full songs from lyrics and tags using the HeartMuLa family of open-source music foundation models. Apache 2.0 licensed — no API keys, no rate limits, no censorship. Four models work together: HeartMuLa (music generation), HeartCodec (audio codec), HeartTranscriptor (lyrics), and HeartCLAP (audio-text alignment).

---

## What It Does

| Model | Role | Size |
|-------|------|------|
| **HeartMuLa** | Music language model — generates from lyrics + tags | 3B/7B params |
| **HeartCodec** | 12.5Hz music codec for high-fidelity audio reconstruction | ~300M |
| **HeartTranscriptor** | Whisper-based lyrics transcription | ~1.5B |
| **HeartCLAP** | Audio-text alignment for style/tag matching | ~600M |

The full pipeline: lyrics + style tags → HeartMuLa generates tokens → HeartCodec decodes to audio → HeartCLAP verifies style alignment.

---

## Installation

### Via skills.sh (Recommended)

```bash
npx skills add https://github.com/nousresearch/hermes-agent --skill heartmula
```

### Direct from Hermes Agent Repo

```bash
git clone --depth 1 https://github.com/nousresearch/hermes-agent.git /tmp/hermes-agent
cp -r /tmp/hermes-agent/skills/creative/heartmula ~/.hermes/skills/
```

### Python Dependencies

The skill will guide Hermes through installing heartlib and model weights:

```bash
pip install heartlib torch torchaudio transformers
```

---

## Prerequisites

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| **GPU** | 8GB VRAM (3B model) | 24GB+ VRAM (7B model) |
| **RAM** | 16GB | 32GB |
| **Disk** | 10GB (models) | 20GB (all variants) |
| **Python** | 3.10+ | 3.11 |

CPU-only generation is possible but slow (5-10 minutes per song vs 30-60 seconds on GPU).

---

## Basic Usage

### Generate a song from lyrics

```
> Load heartmula skill
> Generate a song with these lyrics:
>   "City lights fade into memory..."
> Style: lo-fi hip hop, melancholic, 85 BPM
```

### Generate with tags only (instrumental)

```
> Generate an instrumental track
> Tags: cinematic, orchestral, epic, 120 BPM, D minor
```

### Transcribe existing audio

```
> Transcribe the vocals from /home/user/mystery-song.mp3
```

---

## Model Sizes — Which to Use

| Model | VRAM | Generation Time | Quality |
|-------|------|----------------|---------|
| HeartMuLa-3B | 8GB | ~30s | Good — suitable for demos |
| HeartMuLa-7B | 16GB | ~60s | Very Good — production ready |
| HeartMuLa-7B-FT | 20GB | ~90s | Best — fine-tuned on curated data |

Hermes will auto-select based on available VRAM.

---

## Tips

- **Lyrics structure matters:** Use verse/chorus/bridge markers for better song structure
- **Tag combinations:** 3-5 tags work best — genre + mood + tempo + key
- **Multilingual:** HeartMuLa supports English, Chinese, Japanese, Korean lyrics
- **Iterative refinement:** Generate, listen, adjust tags, regenerate
- **Offline-first:** No internet needed after model download

---

## Troubleshooting

| Problem | Likely Cause | Fix |
|---------|-------------|-----|
| CUDA out of memory | Model too large for GPU | Force 3B model or use CPU fallback |
| Slow generation | Running on CPU | Verify CUDA is available: `python -c "import torch; print(torch.cuda.is_available())"` |
| Model download fails | Network issue | Download models manually from HuggingFace |

---

## License

HeartMuLa models are Apache 2.0 — commercial use allowed, no royalties, no attribution required. Unlike Suno/Udio, you own the output completely.

---

*← [Skills Catalog](/hermes/skills/catalog/) | [nousresearch/hermes-agent on skills.sh](https://skills.sh/nousresearch/hermes-agent)*

*Powered by CorpusIQ*
