---
title: "fixRAgent MCP - Property Maintenance Triage"
description: "One photo of a building problem becomes urgency, the trade to call and the resident message, through a keyless remote MCP server for property teams."
category: "Real Estate & Property Management"
stars: n/a (new listing)
added: 2026-10-14
source: "mcp.so feed (October 14, 2026 night sweep)"
relevance: ★★
tags: [property-management, maintenance, triage, landlords, field-service, remote-mcp, keyless]
---

# fixRAgent MCP

**Remote MCP server (Streamable HTTP, no key needed to connect)** - a photo-triage endpoint for property maintenance: one photo of something in a building comes back as a Triage Profile in about ten seconds - the asset, an urgency tier, the trade to call and a line for the resident. Built by AR Logic LLC in Ohio for property managers, landlords and maintenance teams.

```
Server type: Remote (Streamable HTTP)
Auth: None to connect (free key for direct REST use, 60 requests a UTC day)
Endpoint: https://fixragent.com/mcp
Tools: 3 (try_sample, assess_property_photo, get_triage_profile)
Pricing: Free tier; paid use is quoted
Built by: AR Logic LLC (Ohio); server reports fixragent v1.0.1
Listing: mcp.so feed, October 14, 2026 night sweep
```

## Why This Matters for Operators

Maintenance requests arrive as photos and improvisation: a resident sends a picture of a leaking joint or a rusted panel, and someone has to decide in seconds what it is, whether it can wait, who to send and what to tell the person who took the photo. Get it wrong in one direction and a plumber is dispatched for a cosmetic crack; get it wrong in the other and water sits next to a live panel overnight.

fixRAgent turns that first read into a tool call. The photo goes in, a fixed response comes back - asset type, a fault flag, an urgency tier (EMERGENCY, TODAY, THIS WEEK or WHENEVER), the trade required, a resident-ready explanation - and the reply reports how many of the three reads (five on deep) agreed. One rule is enforced in code: wiring a person could touch, or water near anything electrical, is always EMERGENCY.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| assess_property_photo | Assess a photo of something in a building - an appliance, a boiler, a pipe, a water heater, an electrical panel, a fitting, damage |
| try_sample | Return a stored assessment of a sample photo from fixRAgent's test set, with no photo or key needed |
| get_triage_profile | Read a saved assessment back by its diagnosis_id |

## Installation

```
claude mcp add fixragent-maintenance-triage --transport http https://fixragent.com/mcp
```

Any MCP client that speaks Streamable HTTP can add the same endpoint. The server connects without a key; a free key (60 requests a UTC day, emailed after a short form) covers direct REST calls to the triage API, where the same engine is used from JavaScript, Python and any HTTP client.

## Configuration

```json
{
  "mcpServers": {
    "fixragent": {
      "type": "http",
      "url": "https://fixragent.com/mcp"
    }
  }
}
```

## Business Relevance

- **Property managers and landlords** triage maintenance photos in seconds instead of a callback loop: urgency, trade and the resident message come back together, and the resident line can be sent as written
- **Maintenance teams** get a consistent first read on after-hours requests, with the four urgency words mapped to their own priority fields and safety-relevant photos taken out of the normal queue
- **Teams with a work-order system** map the response fields (tier, asset_type, trade_required, fault_summary, safety_hazard) onto priority, equipment, vendor category and description fields with no integration to install, and can post the outcome back through the callback_url
- **Portfolios using the resident flow** let residents scan a sticker and snap a photo, so the request arrives already structured

## Integration with CorpusIQ

fixRAgent covers the triage moment. CorpusIQ answers the surrounding business question from connected sources such as work orders, accounting and email, so the volume of maintenance - what it costs, which trades consume it, which properties generate it - can be read alongside the operations it drives.

Used together: send the photo through fixRAgent for the urgency read, and ask CorpusIQ for the operating picture behind the ticket - spend by property, vendor or month - without wiring either system to the other first.

## Limitations

- A triage aid, not an inspection: the output is a first read of one photo, and a qualified trade still makes the call
- New listing (v1.0.1 at capture time): the service, quota and pricing are as the vendor states on fixragent.com
- The MCP endpoint connects without a key; direct REST use carries the free key's limit of 60 requests per UTC day, and paid use is quoted by the vendor
- Privacy as the vendor documents it: location details are stripped before assessment, the cleaned photo and its profile are kept by default (send keep_photo false to opt out), and the vendor's model provider keeps what it is sent for 55 days

## FAQ

### Does it work without a key?

Yes. A live probe returns 200 on initialize and `tools/list` with all 3 tools, no account or key, and the vendor's FAQ states the MCP server does not require authentication. The free key (60 requests a UTC day) is for direct REST calls to the same engine.

### What exactly comes back for a photo?

One fixed, versioned shape of about twenty core fields: what the asset is, whether a fault is visible, the urgency tier, which trade to call, a fault summary, a resident explanation, a safety flag and a callback URL for the outcome. The same shape comes back whether the photo shows a leak or nothing at all.

### How does it decide urgency?

The photo is read three times (five on deep) and the reply reports how many reads agreed. One rule runs in code on top of the reads: wiring a person could touch, or water near anything electrical, forces EMERGENCY. The vendor docs show a MOVE NOW and a CAN WAIT example, both with full agreement.

### Who is it for?

Property managers, landlords and maintenance teams, per the vendor. It is built by AR Logic LLC in Ohio, and the vendor also ships a no-code resident flow (stickers, a queue and the same four urgency words) for teams that want triage without writing any code.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [Skywalk MCP - AppFolio Data for Property Managers](/hermes/mcp/servers/external/skywalk-appfolio-mcp/)
- [Hercules Property Integrations MCP](/hermes/mcp/servers/external/hercules-property-mcp/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
