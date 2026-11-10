---
title: "Paseo - Cross-Session Agent Orchestration"
description: "Paseo setup and evaluation notes: a self-hosted daemon that runs Claude Code, Codex, Copilot, OpenCode, and Pi agents in parallel from desktop, mobile"
canonical: "https://www.corpusiq.io/docs/hermes/orchestration/paseo/"
robots: "index,follow"
last_updated: "2026-11-09"
tags: ["agent orchestration", "multi-agent", "paseo", "coding agents"]

---

# Paseo - Cross-Session Agent Orchestration

Paseo (getpaseo/paseo) is a self-hosted orchestration layer for coding agents. It runs a local daemon that manages multiple agents in parallel, and exposes one interface across desktop, mobile, web, and CLI. It fills the gap between single-session agent loops and full platform orchestration: you spin agents up, watch them work, attach to live output, and send follow-up tasks without opening a terminal per agent.

## Why It Matters

Single-session agent patterns break when you need several agents working at once. Paseo's model is a reference for the orchestration stack:

- One daemon owns all agent lifecycles.
- Clients connect to the daemon, so state survives across devices and sessions.
- Agents run on your own machine with your full dev environment: your tools, your configs, your skills.
- Multi-provider: Claude Code, Codex, Copilot, OpenCode, and Pi through the same interface.
- No telemetry, no tracking, no forced log-in.

## License Verdict

The GitHub API classifies the license as `NOASSERTION`, but the LICENSE file's own terms are **Apache License 2.0** (with third-party components remaining under their respective licenses). The NOASSERTION flag is a classifier artifact caused by the custom preamble header, not a custom or restrictive license. Apache 2.0 is permissive: use, modify, and distribute freely, including commercially, with attribution.

## Architecture

```
Desktop / Mobile / Web / CLI clients
 │
 ▼
 Paseo daemon (local server, manages agent lifecycles)
 │
 ┌──────────┼──────────────┬───────────────┐
 ▼ ▼ ▼ ▼
Claude Code Codex Copilot OpenCode / Pi
```

The daemon is the single source of truth. Clients pair to it locally, over TCP, or through the end-to-end encrypted relay for device pairing.

## Setup

### CLI / headless

```bash
npm install -g @getpaseo/cli
paseo
```

Paseo starts locally, then asks whether to enable the end-to-end encrypted relay for device pairing. If you decline, connect directly over TCP, Tailscale, or another VPN. This path is useful for servers and remote machines.

### Docker

Run the daemon and self-hosted web UI in a container:

```bash
docker run -d --name paseo \
 -p 6767:6767 \
 -e PASEO_PASSWORD=change-me \
 -v "$PWD/paseo-home:/home/paseo" \
 -v "$PWD:/workspace" \
 ghcr.io/getpaseo/paseo:latest
```

Open `http://localhost:6767` after it starts. Extend the base image with the agent CLIs you use, then provide credentials through environment variables or the persistent `/home/paseo` volume.

### Desktop app

Download from [paseo.sh/download](https://paseo.sh/download) or the GitHub releases page. The app starts the daemon automatically. To connect from your phone: Settings → your host → Pair Device.

## CLI Reference

```bash
paseo run --provider claude/opus-4.6 "implement user authentication"
paseo run --provider codex/gpt-5.5 --worktree feature-x "implement feature X"

paseo ls # list running agents
paseo attach abc123 # stream live output
paseo send abc123 "also add tests" # follow-up task

# run on a remote daemon; --cwd is a path on that host
paseo run --host workstation.local:6767 --cwd /workspace "run the full test suite"
```

## Evaluation Notes (refreshed 2026-11-09; first review 2026-08-30)

- **Stars / forks / issues:** 23.7K stars, 2.9K forks, 1.9K open issues at the time of this refresh.
- **Release cadence:** latest release v0.15.3, published 2026-11-06; commits pushed daily (repo active on the refresh date).
- **Velocity:** 2,286 merged pull requests since the repo was created (2025-10-13).
- **Language:** TypeScript.
- **Repo:** https://github.com/getpaseo/paseo · Docs: https://paseo.sh/docs
- **Watch items:** the issue backlog is large relative to project age; verify release stability before relying on it for production workloads.

## Live Install Status (Spark, refreshed 2026-11-09)

Installed on the worker node after founder approval on 2026-08-30:

- CLI: `@getpaseo/cli` 0.6.1 via `npm install -g` → `/home/hermes/.local/bin/paseo`. Upstream is now v0.15.3 (2026-11-06), so the installed CLI is well behind the current release.
- Daemon: not running at this refresh. `paseo status` reports `stale_pid` for the local daemon and `unreachable` for the connected daemon; the last start was 2026-08-30 (PID 734067). Restart with `paseo onboard` or the desktop app before relying on it.
- Health check (last good state, 2026-08-30): Local Daemon `running`, Connected Daemon `reachable`, listen `127.0.0.1:6767`, relay **disabled** (privacy-first default, no telemetry).
- Logs: `~/.paseo/daemon.log` - clean at the 2026-08-30 install, no errors on startup or client connects.
- Prerequisite note: agent CLIs (Claude Code / Codex / OpenCode) are not installed on this host; the daemon runs standalone and agents can be added per provider.

## Native Hermes Support (re-verified 2026-11-09)

**Hermes Agent is one of the 40+ coding agents Paseo natively runs** - listed on the official supported-agents page (paseo.sh/agents): "Hermes Agent - Run Nous Research's Hermes Agent on your machine, drive it from your phone or desktop." This upgrades Paseo from a reference implementation to a directly usable coordination surface for the Hermes stack: launch Hermes sessions, watch them work, and send follow-up tasks from a single daemon, cross-device.

## Fit With This Stack

Paseo complements the orchestration layers documented in this section. It is not a replacement for an execution kernel like Hermes; it is a cross-session control plane: one daemon, many agents, many clients. With Hermes natively supported as a provider, the daemon on Spark is the coordination surface for running multiple Hermes/coding-agent sessions in parallel and monitoring them from one place (CLI, web, or mobile).

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
