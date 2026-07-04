---
title: "Hermes Desktop Neo Theme — Setup Guide"
description: "Install the Matrix digital rain Neo Theme for Hermes Desktop Electron app. Complete cyberpunk visual overhaul with canvas animations."
skill_name: hermes-desktop-neo-theme
category: Desktop/UI
source_repo: Neo-bot1998/hermes-desktop-neo-theme
stars: 2
language: TypeScript/CSS
platforms: [macOS, Linux, Windows]
---

# Hermes Desktop Neo Theme — Full Setup Guide

A complete Matrix/cyberpunk built-in theme for the Hermes Desktop Electron app. Drop-in 3 files: `presets.ts`, `styles.css`, `context.tsx`.

---

## Features

- **Matrix digital rain** — Canvas animation of binary 0/1 falling code, bold fluorescent green, 50ms frame rate, auto-inject into `#root` DOM
- **Full dark-mode color palette** — Green phosphor (`#00ff41` / `#c8ffc8`) on pure black
- **Light-mode safe** — `html:has(body.neo-active)` + `documentElement.classList.add('dark')` double lock prevents theme bleed
- **Tooltip/Bubble/Button fixes** — Custom CSS overrides prevent the bg-foreground/text-background inversion trap
- **Noto Sans SC** leading font stack with Source Code Pro fallback for legible Chinese
- **Neon glow borders** on search fields, scroll-to-top buttons, focus rings
- **16-color green ANSI** terminal palette

---

## Prerequisites

- **Hermes Desktop** installed (Electron app — macOS `.app`, Linux AppImage, or Windows `.exe`)
- **Hermes Agent source code** accessible locally (needed to rebuild the asar)
- **Node.js 20+** and **npm** (for `npm run build` and `npx asar`)
- Git (to clone the theme repo)

---

## Installation

### First-time install

```bash
# 1. Clone the theme
git clone https://github.com/Neo-bot1998/hermes-desktop-neo-theme.git
cd hermes-desktop-neo-theme

# 2. Copy the 3 source files into Hermes Desktop source tree
cp presets.ts   <hermes-agent>/apps/desktop/src/themes/presets.ts
cp styles.css   <hermes-agent>/apps/desktop/src/styles.css
cp context.tsx  <hermes-agent>/apps/desktop/src/themes/context.tsx

# 3. Build the desktop app
cd <hermes-agent>/apps/desktop
npm run build

# 4. Pack the asar
# ⚠️ NEVER use `npx asar pack dist app.asar` — missing package.json + electron/main.cjs will crash
rm -rf /tmp/neo-asar-root && mkdir -p /tmp/neo-asar-root
cp -r dist assets electron public /tmp/neo-asar-root/
cp package.json /tmp/neo-asar-root/
cd /tmp/neo-asar-root && npx asar pack . <Hermes.app/Contents/Resources/app.asar>

# 5. Restart Hermes Desktop, Cmd+K → /skin neo
```

### Important: MUST pack the complete tree

The common mistake is running `npx asar pack dist app.asar`. This only packs the `dist/` directory and **omits** `package.json`, `electron/main.cjs`, and other files the Electron runtime needs — the app will crash on launch.

Always include: `dist/`, `assets/`, `electron/`, `public/`, and `package.json`.

---

## macOS Paths Reference

| Component | Path |
|-----------|------|
| Hermes Agent source | `~/hermes-agent` or wherever you cloned it |
| Desktop app source | `<hermes-agent>/apps/desktop/` |
| Installed Hermes.app | `/Applications/Hermes.app` |
| asar to replace | `/Applications/Hermes.app/Contents/Resources/app.asar` |

Example full install on macOS:

```bash
HERMES_SRC=~/hermes-agent
THEME_DIR=~/hermes-desktop-neo-theme
APP_ASAR="/Applications/Hermes.app/Contents/Resources/app.asar"

# Backup original asar
cp "$APP_ASAR" "$APP_ASAR.bak-$(date +%Y%m%d-%H%M)"

# Copy theme files
cp "$THEME_DIR/presets.ts"  "$HERMES_SRC/apps/desktop/src/themes/presets.ts"
cp "$THEME_DIR/styles.css"  "$HERMES_SRC/apps/desktop/src/styles.css"
cp "$THEME_DIR/context.tsx" "$HERMES_SRC/apps/desktop/src/themes/context.tsx"

# Build
cd "$HERMES_SRC/apps/desktop"
npm run build

# Pack
rm -rf /tmp/neo-asar-root && mkdir -p /tmp/neo-asar-root
cp -r dist assets electron public /tmp/neo-asar-root/
cp package.json /tmp/neo-asar-root/
cd /tmp/neo-asar-root && npx asar pack . "$APP_ASAR"

# Restart Hermes Desktop → Cmd+K → /skin neo
```

---

## Restore After Hermes Desktop Update (~5 min)

When Hermes Desktop updates, it replaces `app.asar` — your Neo theme is lost. To restore:

```bash
# 1. Pull latest theme (or re-clone)
cd ~/hermes-desktop-neo-theme
git pull

# 2. Copy 3 files back into source tree
cp presets.ts   <hermes-agent>/apps/desktop/src/themes/presets.ts
cp styles.css   <hermes-agent>/apps/desktop/src/styles.css
cp context.tsx  <hermes-agent>/apps/desktop/src/themes/context.tsx

# 3. Build
cd <hermes-agent>/apps/desktop
npm run build

# 4. Backup current asar (always!)
cp "$APP_ASAR" "$APP_ASAR.bak-$(date +%Y%m%d-%H%M)"

# 5. Pack complete asar (NOT just dist/)
rm -rf /tmp/neo-asar-root && mkdir -p /tmp/neo-asar-root
cp -r dist assets electron public /tmp/neo-asar-root/
cp package.json /tmp/neo-asar-root/
cd /tmp/neo-asar-root && npx asar pack . "$APP_ASAR"

# 6. Restart Hermes Desktop → Cmd+K → /skin neo
```

---

## Activating the Theme

After installation, activate inside Hermes Desktop:

1. Press `Cmd+K` (macOS) or `Ctrl+K` (Linux/Windows)
2. Type `/skin neo`
3. Press Enter

The Matrix digital rain starts immediately. All panels, chat bubbles, tooltips, and the terminal panel switch to the green phosphor palette.

---

## Customizing

### Changing the phosphor color

Edit `styles.css` and replace the color values:

```css
/* Default (Matrix green) */
--neo-primary: #00ff41;
--neo-secondary: #c8ffc8;

/* Alternative: Amber phosphor */
--neo-primary: #ffb000;
--neo-secondary: #ffe5a0;

/* Alternative: CRT blue */
--neo-primary: #00bfff;
--neo-secondary: #b0e0ff;
```

### Adjusting rain speed

Edit `presets.ts`:

```typescript
// Default: 50ms
rainSpeed: 50,

// Faster: 30ms (more intense)
rainSpeed: 30,

// Slower: 80ms (calmer)
rainSpeed: 80,
```

### Disabling rain animation

Set `rainEnabled: false` in `presets.ts` to keep the green phosphor theme without the falling code animation.

---

## Troubleshooting

### App crashes after asar pack

**Symptom:** Hermes Desktop won't launch, or shows a white screen.

**Cause:** Incomplete asar pack — missing `package.json`, `electron/`, or `assets/`.

**Fix:** Re-pack with ALL required directories:
```bash
rm -rf /tmp/neo-asar-root && mkdir -p /tmp/neo-asar-root
cp -r dist assets electron public /tmp/neo-asar-root/
cp package.json /tmp/neo-asar-root/
cd /tmp/neo-asar-root && npx asar pack . "$APP_ASAR"
```

**Recovery:** Restore the backup:
```bash
cp "$APP_ASAR.bak-YYYYMMDD-HHMM" "$APP_ASAR"
```

### Theme doesn't activate

**Symptom:** `/skin neo` returns "Unknown skin."

**Cause:** Files not copied to the correct paths in the source tree.

**Fix:** Verify files exist:
```bash
ls -la <hermes-agent>/apps/desktop/src/themes/presets.ts
ls -la <hermes-agent>/apps/desktop/src/styles.css
ls -la <hermes-agent>/apps/desktop/src/themes/context.tsx
```

### Upstream breaking changes

If the upstream Hermes Agent updated `presets.ts`, `context.tsx`, or `styles.css` with breaking changes (renamed variables, new theme system, etc.), the Neo theme may need manual adaptation. Check the theme repo for updates:

```bash
cd ~/hermes-desktop-neo-theme
git pull
git log --oneline -5
```

---

## Related Tools

- [hermes-skins](https://github.com/mdgld/hermes-skins) — Monokai-based TUI/CLI skins
- [hermes-mod](https://github.com/Joello2925/hermes-mod) — Web UI for managing CLI skins
- [Hermes Desktop Companion](https://github.com/aradotso/hermes-skills) — Desktop agent companion app

---

*Powered by CorpusIQ*
