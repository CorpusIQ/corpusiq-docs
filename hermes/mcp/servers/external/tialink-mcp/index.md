---
title: "TiaLink MCP - Siemens TIA Portal Engineering"
description: "A local MCP gateway that lets an agent configure hardware, write SCL blocks, compile, simulate and read back Siemens TIA Portal projects."
category: "Manufacturing & Industrial"
stars: n/a (new listing)
added: 2026-10-14
source: "mcpservers.org /all (October 14, 2026 midday sweep)"
relevance: ★★
tags: [manufacturing, industrial-automation, plc, siemens, tia-portal, engineering, remote-mcp]
last_updated: "2026-10-24"
---

# TiaLink MCP

**Local MCP gateway (Streamable HTTP, Bearer token) - an engineering gateway for Siemens TIA Portal: an agent configures hardware and networks, creates and edits program blocks, writes SCL, compiles, simulates on S7-PLCSIM Advanced and reads the project back, all on the machine that runs TIA Portal. Part of the TIA Forge suite by Hubwiz (hubwiz.com).**

```
Gateway type: Local (Streamable HTTP, runs on the same machine as TIA Portal)
Auth: Bearer token (API token configured on the gateway)
Endpoint: http://<gateway-host>:8080/mcp (LAN)
Underlying: Siemens TIA Portal Openness
Capabilities: hardware and network configuration, block authoring (FB / FC / DB / UDT),
  SCL authoring, SimaticML import, compile and archive, S7-PLCSIM Advanced simulation,
  variable read and write, project read-back
Suite: TIA Forge (reverse-docs, lad2scl, txt2scl, txt2lad, block-sim)
Publisher: Hubwiz (hubwiz.com)
Listing: mcpservers.org /all, October 14, 2026 midday sweep
```

## Why This Matters for Operators

PLC engineering is slow because it is done by hand: a change request arrives, an engineer opens TIA Portal, clicks through hardware configuration, writes or edits blocks, compiles, fixes what the compiler rejects, downloads to a simulator and repeats. Every step is real work in a proprietary tool, and every step is also highly structured - which is exactly the kind of work an agent can draft.

TiaLink puts the TIA Portal project itself behind MCP tools. The agent operates a real project through Siemens' own Openness interface - configuring devices, writing SCL, compiling, running a simulation on S7-PLCSIM Advanced - and reads the project model back for verification. The engineer stays in the review loop, and the project data never leaves the local network.

## Capabilities

| Area | What the agent can do |
|---|---|
| Hardware & networks | Add devices and modules, assign IP addresses, create subnets and IO systems |
| Programs & data | Create FB / FC / DB / UDT blocks, write SCL, import SimaticML blocks (including LAD) |
| Build | Compile, save, export and archive projects |
| Simulate & verify | Download to S7-PLCSIM Advanced, read and write variables, run test scenarios |
| Read back | Project model, block interfaces and the hardware tree for verification |

## Deployment

- The gateway runs on the **same Windows machine as TIA Portal** - Openness only runs where TIA Portal is installed.
- The MCP client can run on a different machine and connect over the LAN, for example `http://<gateway-host>:8080/mcp`.
- Configure an API token on the gateway; the client sends it as a `Bearer` header.
- No internet access is required, and project data stays on the local network - suitable for offline and on-premises environments.

## Example configuration

```json
{
  "mcpServers": {
    "tialink": {
      "type": "http",
      "url": "http://192.168.1.78:8080/mcp",
      "headers": {
        "Authorization": "Bearer <YOUR_API_TOKEN>"
      }
    }
  }
}
```

Replace the host with the IP or hostname of the machine running TiaLink, and the token with the one configured on the gateway.

## Business Relevance

- **System integrators and automation teams** can have an agent draft hardware configuration, block skeletons and SCL from a change request, then review the diff in TIA Portal instead of starting from an empty block
- **Plant engineering groups** get a repeatable way to rebuild documentation and reverse-engineer existing projects (the TIA Forge suite ships a reverse-docs companion for exactly this)
- **Teams with on-premises constraints** keep everything local: the gateway needs no internet, and project data never leaves the network
- **Training and onboarding** benefit from a project that can be interrogated in plain language - what the block interface is, how the hardware tree is wired, what a compile reports

## Integration with CorpusIQ

Engineering work is one half of an automation project; the business picture is the other. CorpusIQ answers the surrounding questions from connected sources such as accounting, CRM and email - what a project is costing, which change requests consume the most engineering time, which integrator is behind schedule - without wiring either system to the other first.

## Limitations

- **Windows and TIA Portal required:** the gateway wraps Openness, which only runs on a machine with TIA Portal installed, and TIA Portal is commercial Siemens software
- **Commercial gateway:** the documentation is CC BY 4.0, but the TiaLink software itself is commercial; terms and pricing are set by the publisher (Hubwiz)
- **Capability-level docs:** the public listing documents capabilities, not a published tool list; there is no public endpoint to probe (the gateway is local by design)
- **Safety scope:** per the vendor's FAQ, the agent handles the verifiable software part - safety functions must be implemented in hardware (safety relay or safety PLC), hard interlocks must be pneumatic or electrical, and time or sensor tuning happens on the real machine
- **New listing (v1 at capture time):** version details and support are as the publisher states on the product page

## FAQ

### Does it require internet access?

No. TiaLink runs on the same machine as TIA Portal, and all operations happen locally; project data stays on-premises. The MCP client can be on another machine on the same LAN.

### Which AI clients can connect?

Any MCP client that supports Streamable HTTP and can send a Bearer header, such as Claude Code, Cursor or VS Code. The vendor states the gateway is agent-agnostic and not tied to one AI vendor.

### What can the agent actually do in a project?

Configure hardware and networks (devices, modules, IPs, subnets, IO systems), create FB / FC / DB / UDT blocks, write SCL, import SimaticML (including LAD), compile, save, export and archive, download to S7-PLCSIM Advanced, read and write variables, run test scenarios, and read back the project model, block interfaces and hardware tree.

### Can AI-generated PLC code go straight to a live plant?

No. The vendor's own FAQ is explicit: AI handles the verifiable software part, safety functions must be implemented in hardware, hard interlocks must be pneumatic or electrical, and time or sensor tuning must be done on the real machine. TiaLink does not replace safety responsibility.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [MechanoFab MCP - Manufacturing Knowledge for Agents](/hermes/mcp/servers/external/mechanofab-mcp/)
- [FT Optix MCP - FactoryTalk Optix Integration](/hermes/mcp/servers/external/ft-optix-mcp/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
