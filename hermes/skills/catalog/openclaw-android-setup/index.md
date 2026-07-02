---
title: "OpenClaw on Android — Full Setup Guide"
description: "Run OpenClaw agents on Android with Termux — no proot-distro, no Linux overhead. Single-command setup, 1,649+ GitHub stars."
---

# OpenClaw on Android — Setup Guide

**Repo:** [AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android)
**Stars:** 1,649 | **Author:** Aidan Park
**Requirements:** Android 7.0+, Termux
**Skills.sh:** `npx skills add aradotso/hermes-skills --skill openclaw-android-setup`

---

## What It Is

Run OpenClaw — the autonomous AI agent framework — directly on Android without a full Linux distribution. The standard approach requires proot-distro + Debian/Ubuntu (700MB–1GB overhead). This project installs just the glibc dynamic linker (`ld.so`), letting Node.js and OpenClaw run natively on Android's Linux kernel through Termux.

### Architecture Comparison

**Standard approach (heavy):**
```
Linux Kernel → Android/Bionic libc → Termux → proot-distro → Debian/Ubuntu → glibc → Node.js → OpenClaw
```

**This project (lightweight):**
```
Linux Kernel → Android/Bionic libc → Termux → glibc → Node.js → OpenClaw
```

---

## Prerequisites

- **Android 7.0+** (API level 24+)
- **[Termux](https://termux.dev/)** installed (from F-Droid, NOT Google Play — the Play Store version is outdated)
- **~500MB free storage** (vs 1.5GB+ for the proot-distro approach)
- **Internet connection** for initial setup

---

## Installation

### 1. Install Termux

Download from **F-Droid** (recommended):

```
https://f-droid.org/packages/com.termux/
```

⚠️ **Do NOT use the Google Play Store version** — it's outdated and missing critical APIs.

### 2. Run the One-Command Setup

Open Termux and run:

```bash
curl -fsSL https://raw.githubusercontent.com/AidanPark/openclaw-android/main/setup.sh | bash
```

This single command:
- Installs required Termux packages (git, curl, nodejs, etc.)
- Downloads and sets up the glibc dynamic linker
- Installs Node.js with glibc compatibility
- Clones and configures OpenClaw
- Creates startup scripts

### 3. Start OpenClaw

```bash
# Start OpenClaw (first run will prompt for configuration)
openclaw start

# Or use the convenience script
~/openclaw-android/start.sh
```

---

## Configuration

### First-Run Setup

On first launch, OpenClaw will prompt for:
1. **API provider** — OpenAI, Anthropic, DeepSeek, local model, etc.
2. **API key** — Your provider's API key
3. **Model** — Default model selection (e.g., `claude-sonnet-4-20250514`)
4. **Workspace directory** — Where OpenClaw stores sessions and configs

### Config File Location

```bash
~/.openclaw/config.yaml
```

Edit directly:
```bash
nano ~/.openclaw/config.yaml
```

### Example Configuration

```yaml
provider: anthropic
model: claude-sonnet-4-20250514
api_key: ${ANTHROPIC_API_KEY}
workspace: ~/openclaw-workspace
skills_dir: ~/openclaw-skills
```

---

## Usage

### Basic Commands

```bash
# Start OpenClaw in interactive mode
openclaw

# Run a one-shot task
openclaw run "Summarize the latest AI research papers"

# Start in daemon mode (runs in background)
openclaw daemon start

# Check daemon status
openclaw daemon status

# Stop daemon
openclaw daemon stop

# List installed skills
openclaw skills list

# Install a skill from skills.sh
openclaw skills install aradotso/hermes-skills --skill hermes-agent-framework
```

### Running on Old Android Phones

This setup is particularly well-suited for repurposing old Android phones:
- **Samsung Galaxy S8+ (2017)** — runs OpenClaw comfortably
- **Google Pixel 2 (2017)** — known working configuration
- **Any phone with 4GB+ RAM and Android 7.0+**

### Battery Optimization

For long-running agents:
```bash
# Disable battery optimization for Termux (Android settings)
# Settings → Apps → Termux → Battery → Unrestricted

# Or via ADB:
adb shell dumpsys deviceidle whitelist +com.termux
```

---

## Skills Available

Once OpenClaw is running, install Hermes-compatible skills:

```bash
# Agent infrastructure
openclaw skills install aradotso/hermes-skills --skill hermes-agent-framework
openclaw skills install aradotso/hermes-skills --skill hermes-agent-self-evolution

# Communication
openclaw skills install aradotso/hermes-skills --skill hermesclaw-wechat-multi-agent

# Security
openclaw skills install prompt-security/clawsec --skill soul-guardian
```

---

## Troubleshooting

### "glibc not found" error

```bash
# Re-run the glibc setup
cd ~/openclaw-android
./scripts/setup-glibc.sh
```

### "Termux packages outdated"

```bash
# Update Termux packages
pkg update && pkg upgrade
```

### Node.js version mismatch

```bash
# The setup installs a specific Node.js version for glibc compatibility
# To reinstall:
cd ~/openclaw-android
./scripts/install-node.sh
```

### Storage space issues

```bash
# Check free space
df -h /data/data/com.termux/files/home

# Clean up unused packages
pkg clean
```

### Wake lock / sleep issues

Android may kill Termux background processes to save battery:

```bash
# Acquire a wake lock in Termux
termux-wake-lock acquire

# Release when done
termux-wake-lock release
```

---

## Security Notes

- API keys are stored in `~/.openclaw/config.yaml` — set appropriate file permissions
- Consider using environment variables: `provider: anthropic` with `api_key: ${ANTHROPIC_API_KEY}`
- The Android device should have screen lock enabled
- For production use, consider a dedicated device with no personal data

---

## CorpusIQ Use Cases

| Use Case | How |
|----------|-----|
| **Mobile monitoring agent** | Run an OpenClaw agent on an old phone to monitor social mentions 24/7 |
| **Edge AI deployment** | Repurpose old Android devices as low-power Hermes-compatible agent nodes |
| **Field testing** | Test agent skills on mobile before deploying to production servers |
| **Personal assistant** | Always-on agent on your secondary phone for research, scheduling, reminders |
| **Learning platform** | Low-cost Hermes/OpenClaw sandbox for experimenting with agent configurations |

---

## Comparison: Android vs Other Deployment Options

| Platform | Setup Time | Storage | RAM Required | Power Draw |
|----------|:----------:|:-------:|:------------:|:----------:|
| **Android (this project)** | 5 min | 500MB | 2GB | 3-5W |
| Linux server (cloud) | 2 min | 2GB | 4GB | N/A |
| Raspberry Pi 5 | 15 min | 8GB | 4GB | 5-8W |
| Mac Mini | 5 min | 5GB | 8GB | 15-20W |

---

*Setup guide by CorpusIQ. Project by [Aidan Park](https://github.com/AidanPark). OpenClaw framework by the open-source community.*
