---
title: "FindingSteel MCP - GB Steel Section Properties"
description: "GB standard steel section properties and weight over MCP: H-beams, channels, angles, purlins, hollow sections, plus a welded-section calculator."
category: "Manufacturing & Industrial"
stars: n/a (new listing)
added: 2026-10-16
source: "chatmcp/mcpso issue #5522 (October 16, 2026 midday sweep)"
relevance: ★★
tags: [manufacturing, steel, construction, engineering, reference-data, calculator, remote-mcp]
last_updated: "2026-10-19"
---

# FindingSteel MCP

**A steel section reference and calculator for AI assistants. FindingSteel exposes the Chinese GB standard section catalogue - H-beams, I-beams, channels, angles, C and Z purlins, square and rectangular hollow sections and welded sections - as a searchable database with the section properties and theoretical weight an engineer or buyer looks up by hand today. Keyless remote server; one initialize call returns the section properties, no account needed.**

```
Server type: Remote (Streamable HTTP, JSON-RPC 2.0)
Endpoint: https://www.findingsteel.com/mcp/
Auth: None (keyless)
Tools: 7 (category listing, search, exact lookup, welded I-section, welded box-section, weight calculator, material densities)
Data: 143 GB/T section records plus welded-section calculation
Materials: Q235/Q355, 304 and 316 stainless, aluminium, copper
Publisher: Guangdong Jiangxin Auto-Manufacture Steelstructure Co., Ltd (findingsteel.com), a steel-structure fabricator
Registry: io.github.cdaily1995-create/findingsteel-steel-sections (official MCP registry)
Repo: github.com/cdaily1995-create/findingsteel-steel-sections-mcp (MIT)
Listing: chatmcp/mcpso issue #5522, October 16, 2026
```

## Why This Matters for Operators

Section properties are the small, exact numbers a steel project stands on: cross-sectional area, the second moments of area, the section moduli and the theoretical weight per metre. They come out of a standards table, and they get looked up constantly - when a detailer checks a member, when a buyer prices a tonnage, when a fabricator confirms what came off the mill.

That lookup is a table question, which is exactly what a model gets wrong unaided and exactly what a tool does well. FindingSteel puts the GB standard catalogue behind typed tools: search by category or keyword, look up an exact designation, and get the properties back as numbers rather than as a remembered approximation. The welded-section tools go a step further and compute the properties of a built-up I or box section from plate dimensions, which is the case the published tables do not cover.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| `section_categories` | List every standard section category (HW/HM/HN, I-beams, channels, angles, C/Z purlins, square and rectangular hollow sections) and the record count in each |
| `section_search` | Search GB section sizes by category or keyword, returning the designation, standard, dimensions and weight per metre |
| `section_lookup` | Look up one exact designation and return its section properties: A, Ix, Iy, Wx, Wy, ix, iy and kg/m |
| `section_welded_i` | Compute the section properties of a welded I-section from total height, web thickness, flange width and flange thickness |
| `section_welded_box` | Compute the section properties of a welded box section from total height, width, web thickness and flange thickness |
| `weight_calculate` | Theoretical weight for common steel shapes: plate, round, square, flat, hexagon, octagon, rebar and pipe |
| `weight_materials` | List the built-in material density table and defaults |

Designations use the standard x-separated form, for example HN400x200x8x13 or HW250x250x9x14.

## Installation

```bash
claude mcp add --transport http findingsteel https://www.findingsteel.com/mcp/
```

There is no key and no account; the endpoint returns the section database on an anonymous initialize.

## Configuration

```json
{
  "mcpServers": {
    "findingsteel": {
      "type": "http",
      "url": "https://www.findingsteel.com/mcp/"
    }
  }
}
```

Live probe: a keyless `initialize` POST to `www.findingsteel.com/mcp/` returns 200 as `findingsteel-steel-sections` v0.1.0 with a `tools` capability block, and `tools/list` returns all seven tools.

## Business Relevance

- **Structural engineers and detailers** check a member's section properties without leaving the drawing or the chat, and compute a built-up section the tables do not carry
- **Estimators and buyers** turn a member list into tonnage with the theoretical-weight tool and the material density table, which is the arithmetic behind a quote
- **Procurement teams** search the catalogue by category and standard instead of paging through a PDF table
- **Fabricators and importers** working to GB standards get one reference for designations, dimensions and weight per metre
- **Anyone pricing a steel job in Asia** gets a deterministic answer to a table question rather than a model's recollection of a standard

## Integration with CorpusIQ

The section database is reference truth, and it composes with the commercial side of a steel business. CorpusIQ reads the operational systems over read-only tools - QuickBooks or Xero for the invoice behind a quote, Stripe for the deposit, a CRM for the customer, GA4 and Search Console for the demand that arrived on the site - so an assistant can look up a section, price the tonnage with FindingSteel's weight tools, then read the customer's account and the open invoice from a connector to put a quote together with the reference numbers and the commercial record in one place. FindingSteel supplies the engineering constant; CorpusIQ supplies the business context it is quoted in.

## Limitations

- **GB standard only:** the catalogue is Chinese GB/T section data, not AISC, EN or JIS; other standards are out of scope for the published records
- **Vertical scope:** steel sections in a construction and fabrication context, not a general materials database
- **Vendor-operated:** the server is published by a steel-structure fabricator as an engineering reference, so the roadmap tracks their catalogue
- **Small catalogue:** 143 GB/T section records plus the welded-section calculations; breadth of grades is limited to the listed materials
- **New listing:** v0.1.0, MIT-licensed, treated as the current revision; treat the tool surface as current for that version

## FAQ

### Do I need an API key?

No. The server is keyless; an anonymous initialize returns the section database and all seven tools.

### Which steel standards are covered?

Chinese GB/T standard sections: H-beams, I-beams, channels, angles, C and Z purlins, square and rectangular hollow sections and welded sections.

### Can it calculate a section that is not in the tables?

Yes for built-up members. `section_welded_i` and `section_welded_box` compute the properties of a welded I or box section from plate dimensions.

### Does it give the weight of a steel shape?

Yes. `weight_calculate` returns theoretical weight for plate, round, square, flat, hexagon, octagon, rebar and pipe shapes, using the density table `weight_materials` returns.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
