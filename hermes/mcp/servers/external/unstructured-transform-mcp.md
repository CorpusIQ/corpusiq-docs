---
title: "Transform MCP (Unstructured) — Document Parsing for AI Agents"
description: "Connect Unstructured Transform MCP to Hermes Agent. Parse PDFs, CSVs, images, and documents into structured AI-ready data — turns raw files into queryable intelligence."
category: mcp
tags: [mcp-server, document-processing, unstructured, pdf-parsing, data-extraction]
last_updated: 2026-07-15
---

# Transform MCP (Unstructured) ★ New (July 15)

The Unstructured Transform MCP Server connects AI agents to Unstructured, a document processing platform that turns raw files into structured, AI-ready data. Your agent can parse PDFs, CSVs, images, and other document formats — extracting tables, text, and metadata for downstream analysis.

**Source:** mcp.so (submitted July 15, 2026)
**Author:** Unstructured / Chris Maddock
**Transport:** Remote MCP
**Verified:** ✓

## Key Features

- **PDF parsing:** Extract text, tables, and metadata from PDFs — invoices, contracts, reports, and financial statements
- **CSV/structured data:** Parse spreadsheets and tabular data into queryable formats
- **Image document processing:** Extract text from scanned documents and images
- **Multi-format support:** Handles diverse document types beyond PDF — Word, HTML, email, and more
- **Remote MCP transport:** No local installation required — connect via hosted endpoint
- **ADK agent integration:** Built for Google ADK agents, compatible with any MCP client

## Business Relevance

Every operator deals with documents — invoices from vendors, contracts from clients, reports from analytics tools. Transform MCP makes these documents AI-readable. An AI agent can parse a stack of PDF invoices and answer "what's our total spend with Vendor X this quarter?" without manual data entry. Contract analysis becomes queryable: "find all contracts with auto-renewal clauses expiring next month." The document-to-data pipeline that usually requires manual extraction or brittle ETL scripts becomes an MCP tool call.

## Integration with CorpusIQ

Transform MCP fills a critical gap in the business operator stack: unstructured document intelligence. While CorpusIQ provides structured data from 37+ business connectors (QuickBooks, Shopify, HubSpot, etc.), Transform MCP handles the documents those systems generate — parsed invoices, extracted contract terms, and digitized reports become queryable alongside live business metrics. Combined workflow: CorpusIQ pulls live financial data → Transform MCP parses the corresponding PDF invoices → AI agent reconciles and flags discrepancies.

## Limitations

- **Submission-only listing:** Listed on mcp.so as of July 15, 2026. GitHub repository, documentation URL, and endpoint details are not yet publicly linked
- **Unstructured platform dependency:** Requires an Unstructured account/API access — the MCP server is a connector, not a standalone parser
- **Document quality sensitivity:** OCR and parsing accuracy depends on input document quality (scanned vs. digital PDFs)
- **Pricing:** Unstructured platform pricing applies — not a free/open-source tool

## See Also

- [MCP Email Server](/hermes/mcp/servers/external/mcp-email-server/) — parse email attachments and bodies
- [CrustAPI MCP](/hermes/mcp/servers/external/crustapi-mcp/) — web content extraction complement
