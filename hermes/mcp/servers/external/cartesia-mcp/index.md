---
title: "Cartesia MCP - Voice AI for Agents"
description: "Official remote MCP for Cartesia voice AI, giving agents text-to-speech, voice cloning and phone-call audio through one hosted endpoint."
category: "Business Operations"
stars: n/a (official hosted server, cartesia.ai)
added: 2026-10-03
source: "mcp.so server page (cartesia-mcp)"
relevance: ★★★
tags: [voice, text-to-speech, tts, audio, phone, agents, remote-mcp]
---

# Cartesia MCP

**Remote MCP server (Streamable HTTP, API key)** - Cartesia MCP is the official remote server for Cartesia, the low-latency voice AI platform, hosted at `https://mcp.cartesia.ai/mcp`. It gives any MCP-compatible agent access to Cartesia's speech models: text to speech, voice cloning and the audio layer behind voice agents and phone calls.

```
Server type: Remote (Streamable HTTP)
Auth: API key (Cartesia account)
Endpoint: https://mcp.cartesia.ai/mcp
Tools: Cartesia speech and voice tools (live list via the server endpoint)
Pricing: Cartesia platform pricing (usage-based)
Category: Business Operations
Built by: Cartesia (cartesia.ai) - official
```

## Why This Matters for Operators

Voice is the channel most business tooling still leaves as a manual step: a product walkthrough, a support line, a personalized follow-up, an agent that can actually answer a phone. Cartesia is one of the fastest speech engines on the market, and this is its official MCP surface, so an operator does not have to stand up audio infrastructure to give an agent a voice.

**The differentiator is that it is first-party.** The server is published and maintained by Cartesia itself (the `cartesia-ai` GitHub org, verified and featured on the directory), so the tools track the platform's own API rather than wrapping a third-party guess at it. That matters for anything an operator relies on in production.

## Tools & Capabilities

The server exposes Cartesia's speech surface to MCP clients, covering:

- **Text to speech** - generate spoken audio from text with Cartesia's voice models
- **Voice selection and cloning** - use stock voices or the operator's own cloned voices
- **Low-latency audio for agents** - the same engine Cartesia sells for real-time voice agents and phone calling

The authoritative tool list is fetched live from `https://mcp.cartesia.ai/mcp`, and the platform documentation lives at `https://docs.cartesia.ai/tools/ai/mcp`.

## Installation

```bash
claude mcp add cartesia-mcp --transport http https://mcp.cartesia.ai/mcp
```

The same endpoint works in Cursor, VS Code and any client that supports remote Streamable HTTP MCP servers. Configuration snippets for each client are on the directory listing and in Cartesia's documentation.

## Configuration

```json
{
  "mcpServers": {
    "cartesia": {
      "type": "http",
      "url": "https://mcp.cartesia.ai/mcp",
      "headers": {
        "Authorization": "Bearer ${CARTESIA_API_KEY}"
      }
    }
  }
}
```

An API key from the Cartesia account is required. Store it in the client's environment or secret store rather than the config file where the client supports it.

## Business Relevance

- **Product and support teams** give an agent a natural voice for walkthroughs, onboarding audio and support responses without building an audio pipeline.
- **Sales and marketing teams** generate personalized spoken follow-ups and voice notes at scale.
- **Voice-agent builders** wire Cartesia's speech layer into an MCP-orchestrated workflow alongside their data and CRM servers.
- **Operators launching phone or call experiences** use the same first-party server that powers Cartesia's own real-time calling stack.
- **Teams already on Cartesia** reach their existing voices and models from inside an agent instead of a separate console.
