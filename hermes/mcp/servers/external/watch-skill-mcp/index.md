---
title: "Watch Skill - Video Evidence and Verification for Agents"
description: "Video, audio and screen recordings become timestamped frames, transcripts and text, with deterministic verification contracts. 39 MCP tools, MIT."
category: Content & Research
stars: 475 (October 2026)
added: 2026-10-11
source: "Targeted addition from the October 11, 2026 ecosystem watch (oxbshw/watch-skill); installed and wired the same day"
relevance: ★★★
tags: [video, evidence, verification, mcp, local-first, ocr, transcription, agents]
---

# Watch Skill

**Watch Skill gives AI agents eyes, ears and verifiable results.** Video, audio and screen activity become timestamped frames, transcripts and on-screen text: index a source once and query it afterward, with every answer citing a moment you can open. The second capability is verification. A frozen contract over file digests, JSON values, SQL results, HTTP responses or DOM state is evaluated by a separate process, and the verdict comes back as VERIFIED, FAILED, UNVERIFIED or INCONCLUSIVE. That verdict does not come from a language model. The project ships as an MCP server (39 tools), a CLI and a REST API, plus DeepWatch, a ready-made agent workspace built on the official DeepSeek Harness.

```
Server type: Local (stdio MCP server; optional Streamable HTTP on 127.0.0.1)
Auth: None (local-first; OCR and speech models run on the machine)
Tools: 39 across perception, retrieval, verification, THE LOOP, live watching and the workspace
Category: Content & Research
Built by: oxbshw (open source, MIT)
```

## Why This Matters for Operators

Screen-based work has always been hard for agents to read. Support flows, onboarding, checkout pages and dashboards leave their evidence in a recording, not in a log line. Watch Skill turns that recording into searchable, timestamped evidence and proves outcomes with a deterministic contract instead of an opinion. Quality assurance can capture a real browser flow, get a critique that names the timestamp where a fault appears, fix it, then re-capture to prove the fault is gone. Teams working with video (creator research, ad review, competitor teardowns, training material) get frame-level citations instead of a flat summary. And because perception runs locally, the raw footage never has to leave the machine.

## Tools & Capabilities

The server exposes 39 tools in eight groups:

| Group | Tools |
|---|---|
| Perception and retrieval | `watch_video`, `ask_video`, `get_moment`, `search_videos`, `list_videos`, `watch_batch`, `extract_chapters`, `generate_viewer` |
| Content analysis | `extract_bug_report` (QA mode), `analyze_hook` (creator mode) |
| Library | `library_synthesize`, `library_overview`, `check_source` |
| Verification | `verify_contract`, `get_evidence`, `execution_plan`, `report_mistake` |
| THE LOOP | `loop_start`, `loop_iterate`, `loop_status`, `loop_video_gen`, `loop_game`, `loop_monitor` |
| Live watching | `start_live_watch`, `observe_live`, `ask_live`, `aligned_evidence`, `fused_timeline`, `get_live_status`, `stop_live_watch` |
| Jobs and capture | `get_status`, `cancel_job`, `stats`, `capture`, `capture_capabilities`, `doctor` |
| Workspace | `watch_workspace`, `workspace_snapshot`, `workspace_delta` |

The query tools answer most questions: `watch_video` indexes a source, `ask_video` answers follow-ups from the same index, and `get_moment` zooms into one specific timestamp. The verification tools are the differentiator: `verify_contract` decides whether a run actually succeeded, `get_evidence` reads back the evidence bundle and attestation, and `execution_plan` shows what a run would send and cost before it sends anything.

## Installation

```bash
uv tool install "watch-skill[standard]"   # or: pip install "watch-skill[standard]"
watch-skill doctor
```

`[standard]` is frames, retrieval and the MCP server. Add `[ocr]` to read on-screen text, `[whisper]` for local transcription when a source has no captions, `[loop]` for the browser capture behind THE LOOP, `[api]` for the REST surface, or take `[all]`. A bare install gives the CLI and the verifier but cannot extract a frame. `watch-skill doctor` checks the machine (Python, ffmpeg, yt-dlp, GPU, disk, local model runtime) and repairs what it can.

A first run is three commands:

```bash
watch-skill watch <video-url-or-file>
watch-skill ask <id> "what changed at 3:12?"
watch-skill serve            # stdio MCP server, 39 tools
```

## Configuration

In Hermes Agent, the server is wired into `config.yaml`:

```yaml
mcp_servers:
  watch-skill:
    command: /path/to/watch-skill
    args:
      - serve
    connect_timeout: 60
```

Start a new session to pick up the tools. Any other MCP client can run `watch-skill serve` over stdio, or `watch-skill serve --http` for a Streamable HTTP endpoint at `http://127.0.0.1:8747`.

## Integration with CorpusIQ

Watch Skill runs beside CorpusIQ's connector layer. Business questions stay with the connectors, cited to source, and questions about what a recording shows route through Watch Skill's index, cited to a timestamp. Both lanes are local-first and both insist on citable evidence: one cites the business system a number came from, the other cites the moment in the video where it was visible. For QA work the pairing is direct - capture the flow, critique it against written criteria, and let the re-capture prove the fix.

## Limitations

- `[standard]` covers frames, retrieval and the MCP server. On-screen text needs `[ocr]`, local transcription needs `[whisper]`, browser capture for THE LOOP needs `[loop]`, and the REST surface needs `[api]`.
- THE LOOP's critique step needs a vision-capable model. Without one, capture, frames, OCR and verification still work, and the critique reports that it cannot judge rather than guessing.
- OCR and speech model files download on first use.
- The vendor's benchmark table (89.7% groundedness versus 27.9% for a leading video understanding API; 13.23 citations per 100 words versus 0.12) is vendor-published and should be treated as a claim, not an independent result.
- Python 3.11 to 3.13. Node 22.19 or newer is only needed for the DeepWatch workspace.

## FAQ

### Does anything leave my machine?

No provider is required for perception: OCR and speech models run locally, and indexed sources stay on the machine. A provider is only needed for agent chat and the visual critique, and it can point at a local OpenAI-compatible server such as Ollama or vLLM.

### What is the difference between Watch Skill and DeepWatch?

Watch Skill is the engine: perception, evidence, retrieval and verification, reachable over MCP, CLI or REST. DeepWatch is an agent workspace built on top of it, on the official DeepSeek Harness, for teams that want the agent and the UI in one install.

### How is a fix proven?

`verify_contract` evaluates a frozen contract (file digests, JSON values, SQL results, HTTP responses, DOM state) in a separate process and returns VERIFIED, FAILED, UNVERIFIED or INCONCLUSIVE. Nothing in that verdict comes from a language model.

## See Also

- [Screenpipe MCP - Local-First Workflow Memory](/hermes/mcp/servers/external/screenpipe-mcp)
- [External MCP Server Catalog](/hermes/mcp/servers/external)
