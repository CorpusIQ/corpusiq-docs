# OpenAPI Specification

The CorpusIQ API is documented using the OpenAPI 3.1 specification.

## Download

The full OpenAPI spec is available at:

```
https://api.corpusiq.io/v1/openapi.json
```

## Using the Spec

You can import the OpenAPI spec into any compatible tool:

- **Postman** — Import URL to generate a collection
- **Swagger UI** — Paste the URL to explore endpoints interactively
- **OpenAPI Generator** — Generate client SDKs in your language of choice
- **AI Tools** — Feed the spec to ChatGPT, Claude, or Cursor for code generation

## Example: Generate a Python Client

```bash
openapi-generator generate \
  -i https://api.corpusiq.io/v1/openapi.json \
  -g python \
  -o ./corpusiq-client
```

## MCP Server

The easiest way to interact with CorpusIQ programmatically is through our MCP server, which gives AI tools direct access without writing API code:

```
https://mcp2.corpusiq.io/mcp
```

See the [MCP guide](../hermes/mcp/index.md) for setup instructions.
