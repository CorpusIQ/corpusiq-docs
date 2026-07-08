---
title: "Hermex iPhone App — Setup Guide for Hermes Agent"
description: "Step-by-step guide to install and configure Hermex — the native iPhone app for your self-hosted Hermes agent. App Store install, server pairing, Tailscale setup, and troubleshooting."
category: mobile
tags: [hermes-agent, hermex, ios, iphone, mobile, self-hosted, swiftui]
last_updated: 2026-07-08
---

# Hermex iPhone App — Setup Guide

Hermex is a native SwiftUI iPhone app that turns your phone into a mobile cockpit for your self-hosted Hermes agent. Your agent, its tools, and your data stay on your own hardware — the phone is the control plane, not the compute plane. Free, private (no analytics, no tracking), and native (not a web wrapper).

**Repo:** [uzairansaruzi/hermex](https://github.com/uzairansaruzi/hermex) (286⭐)
**App Store:** [Hermex on the App Store](https://apps.apple.com/app/hermex/id6767006319)
**Website:** [hermexapp.com](https://hermexapp.com)
**Author:** Uzair Ansari ([@uzairansar](https://x.com/uzairansar))
**Requirements:** iOS 18+, self-hosted [hermes-webui](https://github.com/nesquena/hermes-webui) server

---

## Prerequisites

Before installing Hermex, you need a running Hermes Web UI server:

1. **Hermes Web UI server** — Install and start `hermes-webui` on macOS, Linux, or Windows/WSL2
2. **Python 3.11+** on the server
3. **Network access** — Your iPhone must be able to reach the server (see connectivity options below)
4. **Strong password** — Set `HERMES_WEBUI_PASSWORD` on the server

---

## Step 1: Set Up Your Hermes Web UI Server

If you don't already have hermes-webui running:

```bash
# Clone and install
git clone https://github.com/nesquena/hermes-webui.git
cd hermes-webui
pip install -r requirements.txt

# Set a strong password
export HERMES_WEBUI_PASSWORD="your-strong-password-here"

# Start the server
python main.py
```

The server runs on port 8787 by default.

---

## Step 2: Make Your Server Reachable

Hermex needs to connect to your server from your iPhone. Choose one of these methods:

### Option A: HTTPS via Cloudflare Tunnel (Recommended)

```bash
# Install cloudflared
curl -L https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -o cloudflared
chmod +x cloudflared

# Create tunnel
cloudflared tunnel --url http://localhost:8787
```

This gives you an `https://*.trycloudflare.com` URL. Real HTTPS keeps iOS App Transport Security happy with no exceptions.

### Option B: Reverse Proxy with Your Domain

If you own a domain, set up nginx or Caddy as a reverse proxy to terminate TLS:

```nginx
# Example nginx config
server {
    listen 443 ssl;
    server_name hermes.yourdomain.com;
    
    ssl_certificate /path/to/cert.pem;
    ssl_certificate_key /path/to/key.pem;
    
    location / {
        proxy_pass http://127.0.0.1:8787;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
    }
}
```

### Option C: Tailscale (Simplest for Personal Use)

```bash
# Install Tailscale on server
curl -fsSL https://tailscale.com/install.sh | sh
tailscale up

# On your iPhone: install Tailscale app, connect to same tailnet

# Run hermes-webui bound to all interfaces
HERMES_WEBUI_PASSWORD="your-password" python main.py --host 0.0.0.0

# In Hermex: connect to http://<tailnet-ip>:8787
```

The app allows plain HTTP only for Tailscale's `100.64.0.0/10` device range.

### Option D: Local Testing (Simulator Only)

For development on the same Mac, connect to `http://localhost:8787`.

---

## Step 3: Install Hermex

### From the App Store (Recommended)

1. Open the [Hermex App Store page](https://apps.apple.com/app/hermex/id6767006319)
2. Tap **Get** → Install
3. Open Hermex from your home screen

### Build from Source

```bash
git clone https://github.com/uzairansaruzi/hermex.git
cd hermex
open HermesMobile.xcodeproj
```

Requires Xcode 26+ and iOS 18 SDK. Select the `HermesMobile` scheme, target an iPhone simulator or device.

---

## Step 4: Connect to Your Server

1. Open Hermex on your iPhone
2. Enter your server URL (e.g., `https://hermes.yourdomain.com` or `http://100.64.x.x:8787` for Tailscale)
3. Enter the password you set in `HERMES_WEBUI_PASSWORD`
4. Tap **Connect**

Hermex will test the connection and then load your agent's sessions, skills, and configuration.

---

## What You Can Do

Once connected, Hermex gives you access to:

| Feature | What It Does |
|---------|-------------|
| **Chat** | Send messages with model, reasoning-effort, workspace, and profile options. Attach files and images. Watch responses stream with thinking and tool-call detail. |
| **Sessions** | Browse, search, and resume every conversation. Cached sessions stay readable offline. |
| **Models** | Switch between any model or provider your server is configured for, with recents and favorites. |
| **Profiles** | Switch agent profiles and organize sessions into projects. |
| **Tasks** | View and edit your agent's scheduled cron jobs from your phone. |
| **Skills** | Browse and search your agent's installed skills. |
| **Workspace** | Explore your server's file system from the app. |
| **Memory** | Read-only panel for agent memory — see what your agent remembers. |
| **Insights** | Usage analytics — tokens, sessions, model usage. |

---

## Troubleshooting

### Connection Test Fails

Check these in order:

1. **Is the server running?** Run `curl https://<your-server>/health` from a computer on the same network. You should get a 200 OK response.
2. **Is the server reachable?** Verify your tunnel, reverse proxy, or Tailscale is connected.
3. **Correct URL?** Check that you're using the right protocol (`https://` for most setups, `http://` only for Tailscale local IPs).
4. **Correct password?** Verify `HERMES_WEBUI_PASSWORD` is set on the server and matches what you entered.

### "Cannot Connect to Server"

- For Cloudflare Tunnel: the tunnel may have expired (free tunnels have timeouts). Restart `cloudflared`.
- For Tailscale: make sure both devices show as connected in the Tailscale admin console.
- For reverse proxy: verify nginx/Caddy is running (`systemctl status nginx`).

### App Crashes on Launch

- Hermex requires iOS 18+. Check Settings → General → About → iOS Version.
- If building from source, ensure you're using Xcode 26+.

### Slow Response Times

- Hermex streams responses in real time. Latency depends on your model and server hardware, not the app.
- For large responses with many tool calls, the streaming UI may feel sluggish — this is model-side, not app-side.

---

## Privacy & Security

- **No analytics, no tracking.** Hermex sends no data to the developer or any third party.
- **No relay.** All communication is directly between your iPhone and your server.
- **Your data stays on your hardware.** The app only displays what your server returns.
- **Password-protected.** Server authentication via `HERMES_WEBUI_PASSWORD`. Set a strong password — it's your only defense on a publicly reachable hostname.
- **Open source.** MIT licensed. [Full source on GitHub](https://github.com/uzairansaruzi/hermex).

---

## Related Resources

- [Hermex GitHub Repo](https://github.com/uzairansaruzi/hermex)
- [Hermex Website](https://hermexapp.com)
- [Hermes Web UI (server)](https://github.com/nesquena/hermes-webui)
- [Hermes Skills Marketplace](/hermes/skills/marketplace/)

---

*Discovered July 3, 2026. Part of the [Hermes Skills Library](https://github.com/CorpusIQ/corpusiq-docs/tree/main/hermes/skills). Powered by [CorpusIQ](https://www.corpusiq.io).*
