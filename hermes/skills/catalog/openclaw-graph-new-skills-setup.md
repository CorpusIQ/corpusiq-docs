---
title: OpenClaw Graph New Skills — Procedural Generation, ARKit, Testing Setup Guide
description: "Install and use three newly catalogued skills from alphaonedev/openclaw-graph: procedural-generation (noise terrains, BSP dungeons), arkit-advanced (scene reconstruction), and testing-integration (Supertest, Testcontainers, Pact)."
---

# OpenClaw Graph — New Skills Setup Guide

**Source:** [alphaonedev/openclaw-graph](https://skills.sh/alphaonedev/openclaw-graph) (repo: 311 skills, 19.7K installs)
**GitHub:** [github.com/alphaonedev/openclaw-graph](https://github.com/alphaonedev/openclaw-graph) (6⭐)
**Category:** Game Dev / AR / Testing
**First Seen:** March 7, 2026
**Security:** Gen Agent Trust Hub Pass · Socket Pass · Snyk Pass (Warn on `testing-integration`)

The openclaw-graph repo is one of the largest single publishers on skills.sh (311 skills). Earlier sweeps catalogued most of it; this sweep caught three missed skills spanning game development, augmented reality, and integration testing.

---

## Installation

```bash
npx skills add https://github.com/alphaonedev/openclaw-graph --skill procedural-generation
npx skills add https://github.com/alphaonedev/openclaw-graph --skill arkit-advanced
npx skills add https://github.com/alphaonedev/openclaw-graph --skill testing-integration
```

---

## The Three Skills

### procedural-generation (50 installs)

Programmatic game content generation — terrains and levels via Perlin noise and rule-based systems.

| Capability | Detail |
|---|---|
| 2D/3D terrain | Perlin and Simplex noise with scale, octave, and persistence parameters |
| Level generation | Cellular automata caves, binary space partitioning dungeons |
| Reproducibility | Custom seed values for deterministic output |
| Export | JSON for meshes, PNG for heightmaps |

```bash
openclaw generate terrain --noise perlin --seed 42 --width 256 --height 256 --output terrain.json
```

### arkit-advanced (48 installs)

Advanced ARKit for iOS AR development, focused on scene reconstruction and 3D object tracking.

| Capability | Detail |
|---|---|
| Scene reconstruction | `ARWorldTrackingConfiguration` for 3D meshes from real environments |
| Object tracking | `ARObjectScanningConfiguration` to detect and anchor custom objects |
| Lighting | `ARFrame.lightEstimate` for realistic rendering |
| Scene management | RealityKit integration for physics and efficient scenes |

```bash
openclaw run arkit-advanced --config scene-reconstruction.json
```

### testing-integration (46 installs)

Integration testing for APIs and services across Node and Python stacks.

| Tool | Purpose |
|---|---|
| Supertest | HTTP API testing with mocking and assertions (Node) |
| httpx | Async HTTP requests and DB integration (Python) |
| Testcontainers | Isolated containerized test environments (Docker databases) |
| Pact | Contract testing for provider-consumer API agreements |

Set `$API_BASE_URL` in your test environment and structure tests to send requests and assert responses in 2-3 lines; keep pacts in separate files verified against providers.

---

## Prerequisites

| Requirement | Details |
|---|---|
| OpenClaw runtime | Skills invoke via the `openclaw` CLI |
| Unity / Godot | For procedural-generation pipeline integration |
| Xcode + A12+ device | For arkit-advanced (ARObjectScanningConfiguration needs A12 or newer) |
| Node or Python | For testing-integration (Supertest/httpx) |
| Docker | For Testcontainers |

---

## CorpusIQ Use Cases

| Use Case | How |
|---|---|
| **API contract testing** | Pact workflow for CorpusIQ MCP server provider-consumer agreements |
| **Isolated test environments** | Testcontainers for spinning up disposable DBs during connector testing |
| **Data visualization assets** | Perlin-noise heightmaps for dashboard and report imagery |
| **Seeded reproducibility** | Deterministic generation for A/B creative asset variants |

---

## Limitations / Verification

- `testing-integration` carries a Snyk Warn — pin dependencies and review before production CI use
- Repo-level quality varies across its 311 skills; these three have clean Trust Hub and Socket records
- Verify: `openclaw run procedural-generation --help` returns the CLI surface; `npx skills list | grep -E "procedural|arkit|testing-integration"` shows three entries

---

## Related

- [Discovery Page — Aug 12 OpenClaw Ecosystem Sweep](/hermes/skills/marketplace/new-aug12-2026-openclaw-ecosystem/)
- [Skills Catalog](/hermes/skills/catalog/)

*Powered by CorpusIQ*
