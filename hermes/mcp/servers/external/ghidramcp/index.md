---
title: "GhidraMCP - Reverse Engineering from Any MCP Client"
description: "Ghidra 12.1.4 behind an MCP server: 28 local tools for decompilation, symbols, cross references and annotations. Headless, no GUI, no cloud calls."
category: Security
stars: 11k+ (October 2026)
added: 2026-10-11
source: "Ecosystem discovery scan (LaurieWired/GhidraMCP); catalogued at the October 11, 2026 targeted addition"
relevance: ★★★
tags: [reverse-engineering, ghidra, decompiler, binary-analysis, security, local-first, headless]
last_updated: "2026-10-19"
---

# GhidraMCP

**GhidraMCP is an MCP server for Ghidra**, the NSA's open source reverse engineering platform. An assistant connected to it can decompile functions, list symbols and segments, walk cross references, read memory and annotate what it finds, all through one local endpoint. Version 2.0 (October 10, 2026) dropped the Python bridge, added headless mode and moved to Ghidra 12.1.4, so the whole pipeline runs with no GUI at all, and nothing leaves the machine.

```
Server type: Local (Ghidra plugin plus a Python MCP client; stdio or Streamable HTTP)
Auth: None (fully local; no telemetry, no accounts, no API keys)
Tools: 28 across decompilation, listing, cross references, memory reads and annotations
Category: Security
Built by: LaurieWired (open source, Apache-2.0)
```

## Why This Matters for Operators

Reverse engineering used to sit behind a specialist's GUI session. With a local MCP server, the assistant reads what Ghidra already produces: what a binary imports, which functions it wires together, and what its code decompiles to in readable C. Security teams get a first pass on a suspicious file before a human analyst opens it. Engineers can check what a compiler actually emitted. Small teams handling sensitive or regulated workloads get the analysis without shipping the binary anywhere, because both the plugin and the server bind to the local machine.

## Tools & Capabilities

The server exposes 28 tools in five groups:

| Group | Tools |
|---|---|
| Decompilation | `decompile_function`, `decompile_function_by_address`, `disassemble_function` |
| Listing | `list_methods`, `list_functions`, `list_classes`, `list_namespaces`, `list_segments`, `list_imports`, `list_exports`, `list_data_items`, `list_strings`, `search_functions_by_name`, `get_function_by_address`, `get_program_info` |
| Cross references | `get_xrefs_to`, `get_xrefs_from`, `get_function_xrefs`, `get_function_calls` |
| Memory | `read_memory` |
| Annotations | `rename_function`, `rename_function_by_address`, `rename_data`, `rename_variable`, `set_function_prototype`, `set_local_variable_type`, `set_decompiler_comment`, `set_disassembly_comment` |

The read tools answer most questions; the annotation tools rename symbols and leave comments in the Ghidra project, which is useful when the analysis will be handed to a person later.

## Installation

Prerequisites: Ghidra 12.1.4 and a JDK 21 runtime (the headless path runs Ghidra in process through PyGhidra).

```bash
# Python 3.10 to 3.13
pip install "ghidra-mcp[headless] @ git+https://github.com/LaurieWired/GhidraMCP"
```

Or with uv, no permanent install:

```bash
uvx --python 3.13 --from "ghidra-mcp[headless] @ git+https://github.com/LaurieWired/GhidraMCP" \
  ghidra-mcp --headless --binary /path/to/target
```

For the GUI route, download the latest release, import the extension zip in Ghidra via File > Install Extensions, restart, and enable the GhidraMCPPlugin under File > Configure > Developer. The plugin then serves on port 8080 and the MCP client connects to it.

One platform note from a live install: the release ships decompiler natives for Linux x86_64 and Windows x86_64. On Linux arm64 the decompiler needs a one time local build of its natives from the Ghidra directory:

```bash
cd support/gradle && ./gradlew buildNatives
```

## Configuration

Headless with a streamable HTTP endpoint:

```bash
export GHIDRA_INSTALL_DIR=/path/to/ghidra_12.1.4_PUBLIC
ghidra-mcp --headless --binary /path/to/target \
  --transport streamable-http --mcp-host 127.0.0.1 --mcp-port 8097
```

Then add `http://127.0.0.1:8097/mcp` as a remote server in any MCP client. For command based clients, the stdio form is:

```json
{
  "mcpServers": {
    "ghidra": {
      "command": "ghidra-mcp",
      "args": ["--headless", "--binary", "/path/to/target"]
    }
  }
}
```

Useful flags: `--project DIR` keeps the Ghidra project and saves changes between runs (the default is a temporary project that discards them), `--no-analyze` skips auto analysis when only quick reads are needed, and `--ready-timeout` controls how long a tool call waits for the initial load and analysis.

## Business Relevance

- **Security teams and consultancies**: first pass triage of suspicious binaries, CTF work and vulnerability research, with decompiled C and cross reference maps produced conversationally.
- **Engineering groups**: inspect what a compiled dependency or a shipped build actually contains, without standing up a full Ghidra workstation for every question.
- **Regulated environments**: the binary and the analysis stay inside the perimeter. There is no cloud component to clear.
- **Education and research**: a low friction way to demonstrate decompilation and symbol recovery interactively.

## Integration with CorpusIQ

GhidraMCP runs beside CorpusIQ's connector layer. The assistant answers business questions from your own systems, cited to source, and reaches for Ghidra when the question is about a compiled binary. Both lanes stay local-first: business data through CorpusIQ's read-only connectors, binary analysis through a server bound to 127.0.0.1. For teams that already restrict what leaves the network, that pairing keeps security work and business reporting under the same roof without widening the data perimeter.

## Limitations

- Requires Ghidra 12.1.4 plus JDK 21; the host default Java is often older and must be pointed at a 21 runtime.
- Linux arm64 needs the one time decompiler natives build shown above; Linux x86_64 and Windows x86_64 are covered by the release.
- Analysis time scales with binary size; tool calls wait for the load and analysis window before answering.
- It wraps Ghidra, so the usual limits apply: packed, obfuscated or damaged binaries remain hard.
- Read tools dominate, but the rename and rename related tools do modify the program in Ghidra; keep the default temporary project, or save deliberately.
- Version 2.0 removed the old Python bridge, so tutorials referencing `bridge_mcp_ghidra.py` describe version 1 only.

## FAQ

### Do I need the Ghidra GUI?

No. Headless mode added in 2.0 runs Ghidra in process through PyGhidra, with no GUI anywhere. The GUI route still works if you prefer it: install the extension, and the MCP client connects to the plugin on port 8080.

### Does anything leave my machine?

No. The Ghidra plugin and the MCP server both bind locally, and there is no telemetry, account or API key involved.

### Which MCP clients work?

Any client that speaks stdio or Streamable HTTP: a uvx command config, a command based JSON config, or a remote URL pointing at `http://127.0.0.1:8097/mcp` while the server runs.

## See Also

- [Security Recipes MCP](/hermes/mcp/servers/external/security-recipes-mcp)
- [CT Logs MCP](/hermes/mcp/servers/external/ctlogs-mcp)
- [External MCP Server Catalog](/hermes/mcp/servers/external)
