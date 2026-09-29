---
title: "VoiceLabs MCP - TTS, Voice Cloning and Transcription"
description: "VoiceLabs gives AI assistants TTS in your own voices, voice cloning and transcription over a hosted MCP endpoint with OAuth 2.1."
category: Communication
stars: n/a (new listing)
added: 2026-09-29
source: "mcpservers.org listing (voicelabs.now)"
relevance: ★★★
tags: [text-to-speech, voice-cloning, transcription, audio, media, oauth, remote-mcp]
---

# VoiceLabs MCP

**Speech for assistants, in voices you own.** VoiceLabs is a hosted remote MCP server that lets an AI app speak text in your own voices, clone a voice from a recording you provide, and transcribe audio. Seven tools sit behind permissions you approve, with OAuth 2.1 sign-in instead of pasted API keys.

```
Server type: Remote (Streamable HTTP, stateless)
Auth: OAuth 2.1
Endpoint: https://app.voicelabs.now/api/mcp
Tools: list_voice_profiles, list_captures, get_generation, speak, transcription and voice tools
Pricing: vendor pricing (voicelabs.now)
Category: Communication
Built by: VoiceLabs (voicelabs.now, official registry name now.voicelabs/voicelabs)
```

## Why This Matters for Operators

Voice is the last mile for a lot of operator work: narrated walkthroughs, onboarding audio, customer-facing voice prompts, meeting transcription. Doing it today means separate TTS, cloning and transcription products with their own keys and quotas. VoiceLabs puts all three behind one endpoint with permission-scoped tools, so an assistant can only reach the voices and actions you approved.

The engines run on the vendor's GPUs on open-source models, so the operator gets hosted convenience without betting the audio stack on a single proprietary voice vendor.

## Tools & Capabilities

| Tool area | Purpose |
|---|---|
| Voice profiles | List the account's cloned and preset voices, with past generations |
| Voice capture | List recent captures and their transcripts |
| Generation polling | Poll a generation for status, then read its audio URL |
| Speech | Generate speech from text, transcribe audio, add preset voices |

Each tool sits behind a permission the consent screen shows before approval, so an app sees only what its permissions cover.

## Installation

```bash
claude mcp add voicelabs --transport http https://app.voicelabs.now/api/mcp
```

Sign in with OAuth 2.1; there is no API key to paste. Engine and setup details live at voicelabs.now.

## Configuration

```json
{
  "mcpServers": {
    "voicelabs": {
      "type": "http",
      "url": "https://app.voicelabs.now/api/mcp"
    }
  }
}
```

## Business Relevance

- **Content teams** produce narrated assets without leaving the assistant workflow
- **Course and training operators** generate lesson voiceovers in consistent voices
- **Support teams** transcribe calls for QA and ticket enrichment
- **Agencies** clone a client's approved voice for recurring creative production

## Integration with CorpusIQ

VoiceLabs covers audio; CorpusIQ covers the business context the audio refers to. An assistant can pull Q3 numbers through CorpusIQ connectors and voice a client recap in the operator's own cloned voice, or transcribe support calls through VoiceLabs and match them to Stripe and CRM records through CorpusIQ connectors for a full conversation-to-revenue picture.

## Limitations

- Cloning requires a recording you provide, and built-in preset voices cannot clone a real person
- Speech engines are open-source models hosted by the vendor, so quality ceiling is model-bound
- Tool set is intentionally small (seven tools), focused on speech rather than audio editing
- Pricing is not disclosed on the directory listing

## FAQ

### Can it clone any voice?

It clones from a recording you provide, and the built-in preset voices cannot clone a real person. Voice cloning is bounded by the permission model and the recordings you supply.

### How is access controlled?

OAuth 2.1 sign-in with per-tool permissions: the consent screen shows each permission before you approve, and an app only sees the tools its permissions cover.

### Where does the speech run?

On the vendor's GPUs using seven engines built on open-source models, listed at voicelabs.now/engines.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
