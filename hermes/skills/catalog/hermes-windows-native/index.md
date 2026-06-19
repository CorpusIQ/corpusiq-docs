---
title: Hermes Windows Native — Setup Guide
description: Run Hermes Agent + WebUI on Windows without Docker or WSL2. One-click PowerShell launcher, shared venv, pure native workflow.
category: Platform
source: markwang2658/hermes-windows-native
stars: 20
---

# Hermes Windows Native

**Install:** `git clone https://github.com/markwang2658/hermes-windows-native.git`

A Windows-native integrated package that bundles Hermes Agent v0.16.0 + Hermes WebUI v0.51.454 with a shared Python virtual environment, PowerShell launchers, and one-click startup. No Docker, no WSL2 — the lightest local footprint on Windows.

## Why Use This

| Alternative | Windows Native Benefit |
|-------------|----------------------|
| Docker Desktop | ~4GB RAM overhead eliminated |
| WSL2 | No Linux subsystem required |
| Manual setup | One PowerShell script handles everything |
| Separate venvs | Single `.venv` for Agent + WebUI |
| Source tree pollution | Runtime data in `%USERPROFILE%\.hermes` |

## Quick Start

### Prerequisites
- Windows 10/11
- Python 3.10+ installed
- Git installed

### Step 1: Clone and set up
```powershell
git clone https://github.com/markwang2658/hermes-windows-native.git hermes-windows
cd hermes-windows
```

### Step 2: Create shared Python environment
```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip setuptools wheel
```

### Step 3: Install Hermes Agent
```powershell
cd .\hermes-agent
..\.venv\Scripts\python.exe -m pip install -e ".[all]"
```

### Step 4: Install Hermes WebUI dependencies
```powershell
cd ..\hermes-webui
..\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### Step 5: One-click startup
```powershell
cd ..\hermes-start
.\hermes-start.ps1
```

**Result:**
- One PowerShell window runs Hermes Agent
- One PowerShell window runs Hermes WebUI
- Browser opens `http://127.0.0.1:8787/`
- Normal chat turn completes successfully

## Repository Layout

```
F:\hermes-windows\
├── .venv\                          # Shared Python environment
├── hermes-agent\                   # Agent source + runtime
├── hermes-webui\                   # WebUI source + interface
├── hermes-start\                   # PowerShell launchers
│   ├── hermes-env.ps1              # Environment variables
│   ├── hermes-agent-start.ps1      # Agent launcher
│   ├── hermes-webui-start.ps1      # WebUI launcher
│   └── hermes-start.ps1            # One-click orchestrator
├── LICENSE
└── README.md
```

## Startup Order
1. `hermes-env.ps1` — Loads environment variables
2. `hermes-agent-start.ps1` — Starts Agent, waits until ready
3. `hermes-webui-start.ps1` — Starts WebUI, waits until it responds

## Free Models (Confirmed Working)

Only these **free no-key models** have been confirmed with this Windows-native setup:
- `stepfun/step-3.7-flash:free`
- `nvidia/nemotron-3-ultra:free`

## Pitfalls

- **Hardcoded paths:** Launcher scripts are path-bound to `F:\hermes-windows`. Rename the root directory? Update paths inside `hermes-start` first.
- **PowerShell execution policy:** You may need `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` to run the launchers.
- **Firewall:** Windows Defender may block the WebUI on port 8787. Allow it when prompted.

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Platform](/hermes/skills/catalog/#platform) →*
*Source: [markwang2658/hermes-windows-native](https://github.com/markwang2658/hermes-windows-native)*
*Powered by CorpusIQ*
