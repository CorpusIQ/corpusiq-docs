---
title: Hermes Tools & SDK Reference
description: Complete directory of 140+ tools and SDKs compatible with Hermes Agent — browsers, search, code execution, media, deployment, and more.
---

# Hermes Tools & SDK Reference

140+ tools across 20 categories that extend Hermes Agent's capabilities. Every tool listed here is tested and compatible with Hermes.

## Tool Categories

| Category | Count | Key Tools |
|----------|-------|-----------|
| Browser Automation | 6 | browser-use, patchright, Playwright, Selenium, deepcloak, camofox |
| Web Search & Extraction | 8 | Firecrawl, Kindly Search, Kagi MCP, SearXNG, Tavily, Brave, DDGS, Exa |
| Code Execution | 5 | Python REPL, Node.js, Bash, Docker exec, SSH exec |
| File Operations | 4 | read/write/patch/search — built into Hermes core |
| Media Processing | 6 | FFmpeg, ImageMagick, Pillow, Sharp, Whisper, OpenCV |
| Messaging | 20 | Telegram, Discord, Slack, WhatsApp, Signal, Matrix, Feishu, WeCom, QQ, Yuanbao, Teams, iMessage, Photon, Mattermost, Ntfy, Webhook, Email |
| Model Providers | 10 | Anthropic, OpenAI, DeepSeek, Grok, Gemini, Ollama, Bedrock, OpenRouter, MiniMax, Z.ai |
| Memory | 8 | Honcho, GBrain, EverOS, memcore-cloud, claude-mem, mnemosyne, memtrace, YantrikDB |
| MCP Servers | 38+ | CorpusIQ (38+ connectors), Kindly Search, Kagi, Anubis, and more |
| Deployment | 7 | Docker, Kubernetes, Modal, Daytona, Vercel Sandbox, systemd, SSH |
| Video Generation | 3 | HeyGen, HyperFrames, Remotion |
| Image Generation | 5 | FAL, DALL-E, Stable Diffusion, Midjourney (API), Flux |
| Text-to-Speech | 6 | OpenAI TTS, ElevenLabs, Edge TTS, Google TTS, MiniMax TTS, xAI TTS |
| Speech-to-Text | 4 | Whisper (OpenAI), Faster-Whisper, Deepgram, Google STT |
| Vision | 3 | Claude Vision, GPT-4V, Gemini Vision |
| Cron & Scheduling | 1 | Built-in cron scheduler (Hermes cron) |
| Git & GitHub | 3 | gh CLI, Git, GitHub API |
| Email | 4 | Gmail API, Outlook API, SMTP/IMAP (Himalaya), SendGrid |
| Database | 6 | PostgreSQL, MSSQL, MongoDB, Cosmos DB, SQLite, Redis |
| Security | 4 | Shellward, Skillguard, NemoClaw, SSL Guard |

---

## Browser Automation

| Tool | Stars | Description | Hermes Integration |
|------|-------|-------------|-------------------|
| [browser-use](https://github.com/browser-use/browser-use) | 97K | AI-powered browser automation | Native Hermes tool |
| [Playwright](https://playwright.dev) | 70K+ | Cross-browser automation | Via terminal + Python |
| [patchright](https://github.com/Kaliiiiiiiiii-Vinyzu/patchright) | — | Undetected Playwright — bypasses Cloudflare, DataDome | Via Mac Mini worker |
| [deepcloak](https://github.com/deepcloak/deepcloak) | — | Anti-bot bypass for Cloudflare, Turnstile | Standalone service |
| [camofox](https://github.com/daijro/camofox) | — | Camoufox stealth browser REST API | HTTP API from Hermes |
| [Selenium](https://www.selenium.dev) | 30K+ | Legacy browser automation | Via terminal |

---

## Web Search & Extraction

| Tool | Stars | Description | Hermes Integration |
|------|-------|-------------|-------------------|
| [Firecrawl](https://www.firecrawl.dev) | — | Web scraping + search API | Native Hermes tool (Nous subscription) |
| [Kindly Web Search MCP](https://github.com/Shelpuk-AI-Technology-Consulting/kindly-web-search-mcp-server) | 345 | Web search MCP server | MCP `hermes mcp add kindly-search` |
| [Kagi Search MCP](https://github.com/KSroido/Kagi-Session2API-MCP) | 137 | Free Kagi search via session tokens | MCP |
| [SearXNG](https://github.com/searxng/searxng) | 14K+ | Privacy-respecting metasearch | Configure as web provider |
| [Tavily](https://tavily.com) | — | AI-optimized search API | Web provider |
| [Brave Search](https://brave.com/search/api/) | — | Privacy-first search API | Web provider |
| [DuckDuckGo](https://duckduckgo.com) | — | Free web search | Web provider (ddgs) |
| [Exa](https://exa.ai) | — | Semantic search for AI | Web provider |

---

## Code Execution

| Tool | Description | Hermes Integration |
|------|-------------|-------------------|
| Python (execute_code) | Run Python scripts with Hermes tools | Native |
| Terminal (bash) | Shell command execution | Native |
| Node.js | JavaScript/TypeScript runtime | Via terminal |
| Docker exec | Container-isolated execution | Via terminal or Docker backend |
| SSH exec | Remote execution on worker nodes | Via terminal |

---

## Media Processing

| Tool | Description | Hermes Integration |
|------|-------------|-------------------|
| FFmpeg | Video/audio processing (Ken Burns, overlays, transcoding) | Via terminal |
| ImageMagick | Image manipulation and conversion | Via terminal |
| Pillow | Python imaging library | Via execute_code |
| Sharp | Node.js image processing | Via terminal |
| Whisper (OpenAI) | Speech-to-text transcription | Native Hermes tool |
| OpenCV | Computer vision | Via Python |

---

## Model Providers

Hermes supports these model providers natively:

| Provider | Models | Best For |
|----------|--------|----------|
| Anthropic | Claude Opus 4, Sonnet 4, Haiku | Complex reasoning, strategy |
| OpenAI | GPT-4o, GPT-4.1, o3, o4-mini | General purpose |
| DeepSeek | DeepSeek-V3, V4 Pro | Research, content, coding |
| xAI | Grok 4.20 | Real-time knowledge |
| Google | Gemini 2.5 Pro, Flash | Multimodal |
| Ollama | Local models (Llama, Mistral, etc.) | Privacy, free inference |
| AWS Bedrock | Claude, Llama, Titan | Enterprise |
| OpenRouter | 200+ models | Model flexibility |
| MiniMax | MiniMax-01 | Alternative provider |
| Z.ai | Z.ai models | Alternative provider |

---

## Memory Systems

[Full Memory Architecture →](/hermes/knowledge/)

| System | Type | Setup | Stars |
|--------|------|-------|-------|
| [Honcho](https://mcp.honcho.dev) | Peer memory | 2 min | — |
| [GBrain](https://github.com/garrytan/gbrain) | Organizational knowledge | 10 min | 23K |
| [EverOS](https://github.com/EverMind-AI/EverOS) | Self-evolving memory | 5 min | 7.5K |
| [claude-mem](https://github.com/thedotmack/claude-mem) | Persistent context | 5 min | 83K |
| [mnemosyne](https://github.com/AxDSan/mnemosyne) | Sub-ms memory | 2 min | 1.2K |
| [memtrace](https://github.com/syncable-dev/memtrace-public) | Structural memory | 10 min | 193 |
| [YantrikDB](https://github.com/yantrikos/yantrikdb-hermes-plugin) | Self-maintaining DB | 5 min | 60 |
| memcore-cloud | Cross-session context | 5 min | — |

---

## MCP Servers

[Full MCP Guide →](/hermes/mcp/) · [Ecosystem →](/hermes/ecosystem.md)

CorpusIQ MCP alone provides 54 tools across 38+ business platforms. Additional MCP servers listed in the [ecosystem page](/hermes/ecosystem.md#-mcp--integrations).

---

## Messaging Platforms

Hermes connects to 20 messaging platforms:

| Platform | Type | Setup |
|----------|------|-------|
| Telegram | Native | `TELEGRAM_BOT_TOKEN` |
| Discord | Plugin | `DISCORD_BOT_TOKEN` |
| Slack | Native | `SLACK_BOT_TOKEN` |
| WhatsApp | Native | WhatsApp Business API |
| Signal | Native | Signal CLI |
| Matrix | Native | Matrix homeserver |
| Feishu/Lark | Native | Feishu app credentials |
| WeCom | Native | WeCom bot |
| QQBot | Native | QQ bot token |
| Yuanbao | Native | Yuanbao API |
| Microsoft Teams | Plugin | Teams app registration |
| iMessage | Native | macOS only |
| Photon | Plugin | Self-hosted |
| Mattermost | Plugin | Mattermost server |
| Ntfy | Native | Ntfy topic |
| Webhook | Native | HTTP endpoint |
| Email | Native | SMTP/IMAP |
| SMS | Native | Twilio |

---

## Deployment Backends

| Backend | Use Case |
|---------|----------|
| Local | Default — runs on your machine |
| Docker | Containerized isolation |
| SSH | Remote execution on worker nodes |
| Modal | Serverless GPU |
| Daytona | Dev environments |
| Vercel Sandbox | Serverless web |
| Kubernetes | via [hermes-operator](https://github.com/paperclipinc/hermes-operator) |
| systemd | via [hermes-autonomous-server](https://github.com/JackTheGit/hermes-autonomous-server) |

---

## Security Tools

| Tool | Description | Stars |
|------|-------------|-------|
| [Shellward](https://github.com/jnMetaCode/shellward) | 8-layer defense middleware | 109 |
| [Skillguard](https://github.com/buzzicra/skillguard) | Skill safety scanner | — |
| [NemoClaw](https://github.com/NVIDIA/NemoClaw) | Hardware sandboxing | 21K |
| SSL Guard | Built-in SSL/CA verification | Core |
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
