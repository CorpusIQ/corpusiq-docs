---
title: "RecallsAPI MCP - US Product and Vehicle Recall Data"
description: "Check any product, food, drug, device or vehicle against US recall data from FDA, USDA, CPSC and NHTSA."
category: Compliance
stars: n/a (new listing)
added: 2026-10-12
source: "mcpservers.org /all (Oct 12, 2026 evening sweep)"
relevance: ★★
tags: [recalls, compliance, product-safety, vehicle, fda, cpsc, nhtsa, remote-mcp]
last_updated: "2026-10-24"
---

# RecallsAPI MCP

**Remote MCP server (Streamable HTTP)** - turn "is this product recalled?" into a lookup an assistant can run mid-task. Search US recall data across food, drug, device, consumer-product and vehicle sources, check a specific product by name, brand, barcode, model, NDC or lot, and check a vehicle by VIN or by make, model and year; every result carries the source link.

```
Server type: Remote (Streamable HTTP)
Auth: initialize and tools/list are open; tool calls take an API key as a Bearer header (free key via POST /v1/keys on the API)
Endpoint: https://api.recallsapi.com/mcp
Tools: 4 (check_product, search_recalls, check_vehicle, get_recall)
Pricing: metered per call against a daily quota; keys issued at recallsapi.com
Category: Compliance / Product Safety
Built by: RecallsAPI (recallsapi.com, hosted service)
Website: recallsapi.com
Listing: mcpservers.org /all (Oct 12, 2026 evening sweep)
```

## Why This Matters for Operators

Recall exposure is a data problem until it is a legal problem. A retailer listing a recalled line, a distributor shipping a lot that was flagged last week, or a fleet with an open NHTSA campaign all find out late because the check lives in someone's browser ritual. RecallsAPI makes the check callable: before an order ships, before a listing goes up, before a vehicle goes out, an assistant can verify against the recall sources and show the source link for anything it flags.

The design is quiet and honest. Matching runs across the identifiers operators actually have (name plus brand, barcode, model, NDC, lot), the vehicle check reports campaign level facts and says so, and every result carries the source link so the finding can be confirmed where it matters.

## Tools & Capabilities

| Tool | Purpose |
|---|---|
| check_product | Is this product recalled? Match on name, brand, UPC, model, NDC or lot (at least one required) |
| search_recalls | Full-text search across all sources, with category, since-date and limit filters |
| check_vehicle | NHTSA campaigns for a vehicle by VIN, or by make, model and year |
| get_recall | The full record for one recall id, with every identifier and the source link |

## Installation

```bash
claude mcp add --transport http recallsapi https://api.recallsapi.com/mcp \
  --header "Authorization: Bearer $RECALLSAPI_KEY"
```

## Configuration

```json
{
  "mcpServers": {
    "recallsapi": {
      "type": "http",
      "url": "https://api.recallsapi.com/mcp",
      "headers": {
        "Authorization": "Bearer ${RECALLSAPI_KEY}"
      }
    }
  }
}
```

## Business Relevance

- **E-commerce and retail teams** can screen a product catalog or a single order line before fulfillment, by barcode or model number.
- **Supply-chain and receiving teams** get a lot-level check for food and drug lines without leaving the receiving workflow.
- **Fleets and dealerships** can check a VIN against open NHTSA campaigns and cite the campaign record.
- **Compliance and support desks** can answer "is this recalled?" with a source link instead of an escalation.

## Integration with CorpusIQ

CorpusIQ reads the business systems where the exposure lives; RecallsAPI supplies the safety verdict. Connect a Shopify or QuickBooks source and ask which products in the catalog match recall data, or which stalled inventory sits behind an open recall; the assistant reads the SKUs, prices and quantities from the source of record and returns the recall matches with their source links. For vehicle fleets, the same pattern works against invoiced sales or service records.

## Limitations

- The service covers US recall sources (food, drug, device, consumer product and vehicle); other jurisdictions are out of scope.
- Tool calls are metered per call against a daily quota, so set expectations for batch screening; the key comes from the vendor.
- The vehicle check reports campaign-level facts (make, model, year); whether a specific vehicle's repair is done is held by the manufacturer's records, and the vendor says so.

## FAQ

### Can I try it without a key?

Partly: the endpoint answers keyless initialize and tools/list, so an assistant can enumerate the four tools with no credentials. Actual lookups need an API key, which the vendor issues at recallsapi.com.

### How fresh is the recall data?

The server aggregates the US recall sources and returns the source link for every record, so freshness is checkable at the source itself; re-check before acting on a critical finding.

### Does it cover vehicles and food, or only products?

All of the above: check_product for consumer goods, food, drugs and devices, and check_vehicle for NHTSA campaigns.

## See Also

- [MCP Servers Index](/hermes/mcp/servers/external/)
- [CorpusIQ Connectors](/hermes/mcp/connectors/)
