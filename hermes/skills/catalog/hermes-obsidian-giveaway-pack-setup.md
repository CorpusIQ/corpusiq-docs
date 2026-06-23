---
title: Hermes + Obsidian Giveaway Pack — Setup Guide
description: Complete always-on Hermes + Obsidian integration — VPS setup, self-organizing vault, phone-to-vault capture workflow. 4 repos, 36 stars total.
skill_name: hermes-obsidian-giveaway-pack
author: david-internal
stars: 36 total across repos
license: Not specified
created: June 22, 2026
last_updated: June 22, 2026
---

# Hermes + Obsidian Giveaway Pack — Setup Guide

**Author:** [david-internal](https://github.com/david-internal)
**Total stars:** 36 across 4 repos
**Created:** June 22, 2026

A complete companion bundle for the "Hermes + Obsidian" video series. Gets you from "I watched the video" to "Hermes is running on a VPS, writing into the same Obsidian vault I use on my Mac, and organizing everything I throw at it from my phone."

---

## What's Included

The giveaway pack contains four repos, each a standalone bundle that builds on the previous:

| # | Repo | Stars | What It Does |
|---|------|:-----:|-------------|
| 1 | `hermes-obsidian-giveaway-pack` | 11 ⭐ | All bundles combined — the full pack |
| 2 | `hermes-obsidian-always-on-setup` | 9 ⭐ | VPS + systemd + Obsidian Sync base setup |
| 3 | `hermes-obsidian-self-organizing-vault` | 9 ⭐ | Vault curator skill + starter templates |
| 4 | `hermes-obsidian-capture-and-proof` | 7 ⭐ | Telegram → Obsidian capture + sync doctor |

---

## Bundle 1: Always-On Base Setup (`hermes-obsidian-always-on-setup`)

**Goal:** Get Hermes running on a VPS writing into the same Obsidian vault you use on your Mac.

### Skills Included

| Skill | Type | Purpose |
|-------|------|---------|
| `hermes-obsidian-setup` | Agent skill | Guides full VPS, Hermes, Obsidian Sync, obsidian-headless, systemd, and vault-path setup |

### Reference Files

| File | Content |
|------|---------|
| `references/full-setup-runbook.md` | Long-form setup path with every command |
| `references/troubleshooting.md` | Common failure modes and fixes |
| `copy-paste-setup-plan.md` | Viewer-facing concise command sequence |

### Scripts

| Script | Purpose |
|--------|---------|
| `scripts/check_vps_prereqs.sh` | Reads the VPS and reports what's missing before setup |
| `scripts/install_obsidian_sync_service.sh` | Creates the tested systemd service for continuous sync |

### Installation

```bash
# Clone the repo
git clone https://github.com/david-internal/hermes-obsidian-always-on-setup.git

# Copy the skill
cp -r hermes-obsidian-always-on-setup/skills/hermes-obsidian-setup ~/.hermes/skills/

# Run the prerequisite checker on your VPS
bash hermes-obsidian-always-on-setup/skills/hermes-obsidian-setup/scripts/check_vps_prereqs.sh

# Install the sync service
sudo bash hermes-obsidian-always-on-setup/skills/hermes-obsidian-setup/scripts/install_obsidian_sync_service.sh
```

### Setup Flow

1. SSH into the VPS
2. Run the prerequisite checker
3. Follow `copy-paste-setup-plan.md`
4. Use the agent skill for guided setup or when stuck
5. Consult troubleshooting if notes don't appear on the Mac

### Key Gotchas

- **Obsidian Sync + obsidian-headless must point at the same vault path** — mismatched paths are the #1 failure mode
- **Hermes `obsidian_vault_path` must match the headless client's vault folder** — verify with `hermes config get`
- **systemd service must restart on failure** — the install script includes `Restart=always`

---

## Bundle 2: Self-Organizing Vault (`hermes-obsidian-self-organizing-vault`)

**Goal:** The agent keeps your notes clean without you doing anything.

### Skills Included

| Skill | Type | Purpose |
|-------|------|---------|
| `obsidian-vault-curator` | Agent skill | Turns raw captures into clean Markdown notes with links, tags, maps of content, and indexes |

### Assets

| Asset | Content |
|-------|---------|
| `assets/vault-starter/` | Complete starter vault with folders: Inbox, Sources, Maps, Projects, People |
| `assets/vault-starter/_templates/` | 6 templates: Daily Capture, Map of Content, Captured Source, Person, Project, Atomic Note |

### Reference Files

| File | Content |
|------|---------|
| `references/vault-rules.md` | Folder structure, naming conventions, tag rules, link quality standards |

### Installation

```bash
# Clone the repo
git clone https://github.com/david-internal/hermes-obsidian-self-organizing-vault.git

# Copy the skill
cp -r hermes-obsidian-self-organizing-vault/skills/obsidian-vault-curator ~/.hermes/skills/

# Copy the vault starter into your Obsidian vault
cp -r hermes-obsidian-self-organizing-vault/skills/obsidian-vault-curator/assets/vault-starter/* ~/your-obsidian-vault/
```

### Usage

1. Copy `vault-starter` contents into a new or existing Obsidian vault
2. Point your agent at the `obsidian-vault-curator` skill
3. Tell the agent which vault folder to use
4. Send raw notes through Telegram, CLI, or chat
5. Let the agent create source notes, atomic notes, links, tags, maps, and project updates

### Demo Tip

Open Obsidian's graph view after several captures. The agent continuously creates Markdown relationships while you do nothing but capture raw material.

---

## Bundle 3: Phone-to-Vault Workflow (`hermes-obsidian-capture-and-proof`)

**Goal:** Send messy things from your phone and the agent files them correctly. Plus a way to prove it actually works.

### Skills Included

| Skill | Type | Purpose |
|-------|------|---------|
| `telegram-to-obsidian-capture` | Agent skill | Converts messy Telegram dumps, URLs, PDFs, and pasted conversations into Obsidian-ready notes |
| `obsidian-sync-doctor` | Agent skill | Diagnoses why notes aren't appearing and verifies the end-to-end loop |

### Reference Files

| File | Content |
|------|---------|
| `references/capture-contract.md` | The format contract: what the agent expects and what it produces |
| `references/diagnostic-playbook.md` | Step-by-step diagnosis for sync failures |
| `assets/prompt-cards.md` | Ready-to-send prompts viewers can use from their phone |

### Scripts

| Script | Purpose |
|--------|---------|
| `scripts/verify_hermes_obsidian_loop.sh` | Read-only checks by default; optional write test for end-to-end verification |

### Installation

```bash
# Clone the repo
git clone https://github.com/david-internal/hermes-obsidian-capture-and-proof.git

# Copy both skills
cp -r hermes-obsidian-capture-and-proof/skills/telegram-to-obsidian-capture ~/.hermes/skills/
cp -r hermes-obsidian-capture-and-proof/skills/obsidian-sync-doctor ~/.hermes/skills/
```

### Usage

1. **Prerequisite:** Bundle 1 (always-on setup) must be complete
2. Install both skills
3. Send a demo prompt through Telegram (`assets/prompt-cards.md` has ready examples)
4. If the note doesn't appear on your Mac, run the sync doctor
5. Before recording a final demo shot, use the optional write test

### Testing the Loop

```bash
# Read-only check (safe, no side effects)
bash hermes-obsidian-capture-and-proof/skills/obsidian-sync-doctor/scripts/verify_hermes_obsidian_loop.sh

# With write test (creates a real note, then verifies it lands)
bash hermes-obsidian-capture-and-proof/skills/obsidian-sync-doctor/scripts/verify_hermes_obsidian_loop.sh --write-test
```

---

## Complete Giveaway Pack (`hermes-obsidian-giveaway-pack`)

**Goal:** All three bundles in one ZIP. 

### Installation (Full Pack)

```bash
# Clone the full giveaway pack
git clone https://github.com/david-internal/hermes-obsidian-giveaway-pack.git

# The pack contains all three bundles as subdirectories
ls hermes-obsidian-giveaway-pack/
# → 01-always-on-setup/  02-self-organizing-vault/  03-capture-and-proof/

# Install all skills at once
for bundle in 01-always-on-setup 02-self-organizing-vault 03-capture-and-proof; do
  find hermes-obsidian-giveaway-pack/$bundle/skills -name "SKILL.md" -exec dirname {} \; | while read skill_dir; do
    skill_name=$(basename "$skill_dir")
    cp -r "$skill_dir" ~/.hermes/skills/"$skill_name"
    echo "Installed: $skill_name"
  done
done
```

### Recommended Handout

Give viewers one ZIP containing all three folders, or optionally three separate ZIPs:

- `always-on-setup.zip` — VPS + Hermes + Obsidian Sync
- `self-organizing-vault.zip` — Vault curator + templates
- `capture-and-proof.zip` — Phone workflow + sync doctor
- `hermes-obsidian-giveaway-pack.zip` — Everything

---

## Why This Matters

The hard part of Hermes + Obsidian isn't knowing that Hermes can write Markdown. It's making the always-on VPS, Obsidian Sync, headless client, and Hermes vault path all point at the same folder. This pack eliminates those setup traps:

- **Path alignment** — Every config points at the same vault folder
- **Persistence** — systemd keeps the sync service alive across restarts
- **Consistency** — The vault curator enforces naming, tags, and link rules
- **Debuggability** — The sync doctor diagnoses the full Hermes → Obsidian loop
- **Phone-first** — Telegram capture works from any device

---

## Dependencies

| Dependency | Required For |
|------------|-------------|
| Hermes Agent with Telegram gateway | Phone capture workflow |
| Obsidian Sync subscription | Cross-device vault sync |
| obsidian-headless | VPS-based Obsidian client |
| systemd (Linux VPS) | Always-on sync service |
| Python 3.10+ | Scripts |

## Verification

After setup, verify the complete loop:

```bash
# 1. Check VPS prerequisites
bash skills/hermes-obsidian-setup/scripts/check_vps_prereqs.sh

# 2. Verify sync service is running
systemctl status obsidian-sync

# 3. Send a test capture through Telegram
# (Use a prompt from assets/prompt-cards.md)

# 4. Run the sync doctor if the note doesn't appear
bash skills/obsidian-sync-doctor/scripts/verify_hermes_obsidian_loop.sh
```

---

*← [Skills Catalog](/hermes/skills/catalog/) | [Marketplace Home](/hermes/skills/marketplace/) | [david-internal on GitHub](https://github.com/david-internal)*
