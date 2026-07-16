---
title: "July 4, 2026 (Update) — hermes-top Dashboard"
description: "5 new Hermes-relevant repos discovered in late July 4 sweep: hermes-top terminal dashboard (1⭐), Neo Desktop Theme (2⭐), Hermes Full Backup (1⭐), IC-sd Agent Skills (1⭐), AGEL-Comp Safety Framework."
---

# 🆕 July 4, 2026 (Update) — 5 New Repos (Late Sweep)

**Date:** July 4, 2026
**New Repos:** 5 | **New Setup Guides:** 4 | **Combined Stars:** 5

A late-evening sweep of GitHub repos created on July 4 surfaced 5 additional Hermes-relevant projects not captured in the [main July 4 sweep](/hermes/skills/marketplace/new-july4-2026/). The standout is **hermes-top** — a Go-based, read-only `htop`/`btop`-style live terminal dashboard that watches Hermes Agent's `state.db`.

---

## New at a Glance

| # | Project | Stars | Type | Category | Source |
|---|---------|:-----:|------|----------|--------|
| 1 | **hermes-top** | 1 | Tool | Monitoring | markmnl/hermes-top |
| 2 | **Hermes Desktop Neo Theme** | 2 | Theme | UI/Desktop | Neo-bot1998/hermes-desktop-neo-theme |
| 3 | **Hermes Full Backup** | 1 | Tool | DevOps/DR | edouardleroy/hermes-full-backup |
| 4 | **IC-sd Agent Skills** | 1 | Skills | Automation | IC-sd/hermes-agent-skills |
| 5 | **AGEL-Comp Safety** | 0 | Plugin | Security | lesterppo/hermes-agel-comp |

---

## Category Breakdown

### Monitoring & Observability (1 project)

#### hermes-top (1⭐) ⭐ Setup Guide Available

**Repo:** [markmnl/hermes-top](https://github.com/markmnl/hermes-top)
**Author:** markmnl
**Language:** Go

A read-only, `htop`/`btop`-style live terminal dashboard for Hermes Agent. Reads Hermes's SQLite `state.db` directly — no agent plugin, no API dependency. Watches sessions, model usage, tool execution, events, and token consumption in real time. Pure Go with a modernc.org/sqlite driver — zero CGO, single static binary.

**Key features:**
- Live TUI with 3 panes: sessions, actions, events
- Real-time token usage and model tracking
- Expandable JSON inspection for tool args/results
- Event filtering with live regex
- Auto-follow like `tail -f` with freeze-on-scroll
- `--dump` flag for one-shot text snapshots (scriptable)
- Reads `$HERMES_HOME/state.db` — never writes

**Setup Guide:** [hermes-top — Full Setup Guide](/hermes/skills/catalog/hermes-top-setup/)

```bash
git clone https://github.com/markmnl/hermes-top.git
cd hermes-top
go build -o hermes-top ./cmd/hermes-top
./hermes-top
```

**Why this matters:** Hermes's `state.db` is a goldmine of observability data, but until now there was no live dashboard that reads it. `hermes-top` fills the gap with a familiar `htop` UX — processes become sessions, syscalls become tool calls. For power users running long-lived Hermes instances, this is essential infrastructure.

---

### Desktop & UI (1 project)

#### Hermes Desktop Neo Theme (2⭐) ⭐ Setup Guide Available

**Repo:** [Neo-bot1998/hermes-desktop-neo-theme](https://github.com/Neo-bot1998/hermes-desktop-neo-theme)
**Author:** Neo-bot1998
**Language:** TypeScript/CSS

A complete Matrix/cyberpunk built-in theme for the Hermes Desktop Electron app. Matrix digital rain canvas animation (binary 0/1 falling code at 50ms), green phosphor color palette on pure black, Noto Sans SC + Source Code Pro font stack, 16-color ANSI terminal palette, neon glow borders, and comprehensive CSS overrides for tooltips, bubbles, and buttons.

**Key features:**
- Matrix digital rain canvas animation (50ms frame rate)
- Green phosphor (#00ff41 / #c8ffc8) on pure black
- Light-mode safe with `html:has(body.neo-active)` double lock
- 16-color green ANSI terminal palette
- Neon glow borders on search, scroll-to-top, focus rings
- Custom CSS fixes for bg-foreground inversion trap
- Drop-in 3 files: presets.ts + styles.css + context.tsx

**Setup Guide:** [Hermes Desktop Neo Theme — Full Setup Guide](/hermes/skills/catalog/hermes-desktop-neo-theme-setup/)

```bash
git clone https://github.com/Neo-bot1998/hermes-desktop-neo-theme.git
cd hermes-desktop-neo-theme
# Copy 3 source files into Hermes Desktop source tree
cp presets.ts <hermes-agent>/apps/desktop/src/themes/presets.ts
cp styles.css <hermes-agent>/apps/desktop/src/styles.css
cp context.tsx <hermes-agent>/apps/desktop/src/themes/context.tsx
# Build and restart → Cmd+K → /skin neo
```

**Why this matters:** Hermes Desktop themes are trending. After hermes-skins, hermes-mod, and the built-in theme system, Neo Theme shows the community building complete visual overhauls — not just color tweaks but full canvas animations and pixel-level CSS control. At 2 stars (highest among today's late sweep), it's got early community validation.

---

### DevOps & Disaster Recovery (1 project)

#### Hermes Full Backup (1⭐) ⭐ Setup Guide Available

**Repo:** [edouardleroy/hermes-full-backup](https://github.com/edouardleroy/hermes-full-backup)
**Author:** edouardleroy
**Language:** Python

A self-contained Python backup script for Hermes Agent disaster recovery. Creates a `.zip` with config (`config.yaml`, `.env`, `state.db`, `auth.json`), skills, cron jobs, memories, profiles, source code, binaries (`uv.exe`), an `install.bat` installer, and recovery instructions. Stdlib-only (zipfile + argparse) — runs on any Python 3 installation.

**Key features:**
- Complete backup: config, skills, sessions, source code, binaries
- `--quick` mode for frequent lightweight backups (config + skills only)
- `--json-config` for external config override
- Credential warning in generated README
- Cross-platform: Windows, Linux, macOS
- Zero dependencies (stdlib only)

**Setup Guide:** [Hermes Full Backup — Full Setup Guide](/hermes/skills/catalog/hermes-full-backup-setup/)

```bash
git clone https://github.com/edouardleroy/hermes-full-backup.git
cd hermes-full-backup
python hermes-complete-backup.py --quick -o ~/hermes-backup.zip
```

**Why this matters:** Hermes agents accumulate state — skills, memories, sessions, cron schedules — that represents weeks or months of configuration. A single `rm -rf ~/.hermes` or disk failure wipes it all. This backup script is the first community tool focused specifically on Hermes disaster recovery. It's simple, stdlib-only, and immediately useful.

---

### Skills Collection (1 project)

#### IC-sd Agent Skills (1⭐)

**Repo:** [IC-sd/hermes-agent-skills](https://github.com/IC-sd/hermes-agent-skills)
**Author:** IC-sd

A collection of 3 practical Hermes Agent skills with full documentation (SKILL.md + README.md + references + scripts + assets for each skill):

| Skill | Description | Category |
|-------|-------------|----------|
| **evolution-tracker** | Self-evolving AI Agent dashboard — monitors skills, memories, platforms, timeline growth. Auto-deploys to GitHub Pages | Data Visualization |
| **browser-mcp-setup** | Browser MCP automation — 29 Chrome DevTools Protocol tools via MCP for page navigation, clicking, form filling, screenshots, JS execution | Browser Automation |
| **auto-github-sync** | Automated data sync pipeline — scheduled data collection, Git commit/push, message notification. Supports no_agent (pure script) and LLM-driven modes | CI/Automation |

```bash
git clone https://github.com/IC-sd/hermes-agent-skills.git
hermes skill install ./skills/evolution-tracker
```

---

### Security & Safety (1 project)

#### AGEL-Comp Safety Framework (0⭐) ⭐ Setup Guide Available

**Repo:** [lesterppo/hermes-agel-comp](https://github.com/lesterppo/hermes-agel-comp)
**Author:** lesterppo
**Language:** Python

A neuro-symbolic safety layer for Hermes Agent based on the AGEL-Comp framework (Shahid & Rothe, 2026). Automatically blocks reads of secret files and execution of destructive commands. Learns safety rules from mistakes via MCS+ILP (Minimal Contrastive Search + Inductive Logic Programming). Provides a Causal Program Graph (CPG) world model the agent can query and extend via a dedicated `agel_comp` tool with 10 actions. Works transparently through Hermes plugin hooks — zero agent compliance needed.

**Key features:**
- Automatic blocking of secret file reads and destructive commands
- MCS+ILP causal learning from mistakes
- Causal Program Graph (CPG) world model with NTP verification
- 10-action `agel_comp` tool for querying and extending safety rules
- Plugin-based — no agent modification required
- Persists rules to `$HERMES_HOME/agel_comp/`

**Setup Guide:** [AGEL-Comp Safety — Full Setup Guide](/hermes/skills/catalog/hermes-agel-comp-setup/)

```bash
git clone https://github.com/lesterppo/hermes-agel-comp.git
cd hermes-agel-comp
./install.sh
# Restart Hermes — safety layer is active immediately
```

**Why this matters:** As Hermes agents gain more autonomy (file system access, terminal execution, network calls), safety becomes critical. AGEL-Comp is the first community safety plugin that goes beyond static blocklists — it learns from mistakes, generalizes safety rules, and provides a queryable causal model. This is agent safety done right: transparent, learnable, and built into the plugin system.

---

## Why These Matter for Hermes Users

### Observability Gets a Terminal Dashboard
**hermes-top** brings the Unix philosophy to Hermes monitoring: read a file (state.db), render it live, get out of the way. No agent plugin, no HTTP server, no external dependency — just a Go binary and your terminal. This is the kind of tool that becomes a staple in every power user's workflow.

### Desktop Customization Goes Deep
**Neo Theme** proves the Hermes Desktop theme system is capable of complete visual overhauls — canvas animations, custom font stacks, CSS-level overrides. Expect more themes as the community discovers what's possible.

### Safety Infrastructure Arrives
**AGEL-Comp** is the most architecturally ambitious project in this sweep. A neuro-symbolic safety layer with causal learning is the kind of infrastructure that becomes mandatory as agents handle more sensitive operations. At 0 stars today, it's early — but the architecture is sound.

---

## Setup Guides Added

This sweep produced 4 detailed setup guides:

- **[hermes-top Setup](/hermes/skills/catalog/hermes-top-setup/)** — Go build, database path resolution, keyboard shortcuts, TUI navigation
- **[Hermes Desktop Neo Theme Setup](/hermes/skills/catalog/hermes-desktop-neo-theme-setup/)** — File copy, build, asar packing, restore after update
- **[Hermes Full Backup Setup](/hermes/skills/catalog/hermes-full-backup-setup/)** — Quick backup, full backup, JSON config, restore procedure
- **[AGEL-Comp Safety Setup](/hermes/skills/catalog/hermes-agel-comp-setup/)** — Plugin install, safety rules, CPG querying, learning pipeline

---

## Comparison

| Metric | Count |
|--------|:-----:|
| Previously documented (July 4 main sweep) | 24 |
| New this update | 5 |
| New setup guides created | 4 |
| Combined new stars | 5 |

---

*← [July 4 Main Sweep](/hermes/skills/marketplace/new-july4-2026/) | [Marketplace Home](/hermes/skills/marketplace/) →*
*Powered by CorpusIQ*
