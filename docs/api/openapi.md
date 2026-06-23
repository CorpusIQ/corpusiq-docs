---
meta_title: "CorpusIQ OpenAPI Specification  --  API Reference for Postman and Swagger"
meta_desc: "Complete CorpusIQ OpenAPI 3.0.3 specification. Import into Postman, Insomnia, or Swagger UI for interactive API testing. Available at api.corpusiq.io/v1/openapi.json."
category: "API Reference"
tags: ["corpusiq openapi", "swagger", "postman", "api specification", "openapi 3.0", "api testing", "api documentation"]
last_updated: "2026-06-16"
canonical: "https://www.corpusiq.io/docs/api/openapi"
robots: "index,follow"
---
# OpenAPI Specification

CorpusIQ provides a complete OpenAPI 3.0.3 specification that can be imported into API tools such as Postman, Insomnia, and Swagger UI. The spec describes all available endpoints, request/response schemas, authentication, and error formats.

## Importing the Spec

### Postman
1. Click **Import** → **Link**
2. Paste: `https://api.corpusiq.io/v1/openapi.json`
3. Click **Continue** → **Import**

### Insomnia
1. Click **Create** → **Import From**
2. Select **URL** and paste: `https://api.corpusiq.io/v1/openapi.json`
3. Click **Fetch and Import**

### Swagger UI / Redoc
Visit `https://api.corpusiq.io/v1/docs` for an interactive Swagger UI with live "Try it out" functionality.

## Full Specification

```yaml
openapi: "3.0.3"
info:
  title: "CorpusIQ API"
  version: "1.0.0"
  description: |
    Private AI acceleration layer connecting 37+ business tools to ChatGPT, Claude,
    and Perplexity via MCP. Read-only queries across your entire data stack with
    cited results  --  no data storage, no data movement.
  contact:
    name: "CorpusIQ API Support"
    email: "api@corpusiq.io"
  license:
    name: "Proprietary"
servers:
  - url: "https://api.corpusiq.io/v1"
    description: "Production API"
security:
  - BearerAuth: []
paths:
  /query:
    post:
      summary: "Search connected data sources"
      description: |
        Execute a natural-language query across all or specified connected business
        tools. Returns semantically ranked, cited results from each connector.
      operationId: "searchQuery"
      parameters:
        - name: "Idempotency-Key"
          in: "header"
          required: false
          schema:
            type: "string"
            format: "uuid"
          description: "Unique key for idempotent requests. Prevents duplicate query records."
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: "object"
              required: ["query"]
              properties:
                query:
                  type: "string"
                  description: "Natural-language question to search across connected tools"
                  example: "What were our top 5 Shopify orders this month?"
                connectors:
                  type: "array"
                  items:
                    type: "string"
                  description: "Connector IDs to scope the search. Omit to search all."
                  example: ["shopify", "hubspot"]
                max_results:
                  type: "integer"
                  minimum: 1
                  maximum: 100
                  default: 10
                  description: "Maximum results per connector"
      responses:
        "200":
          description: "Query results"
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/QueryResponse"
        "400":
          $ref: "#/components/responses/BadRequest"
        "401":
          $ref: "#/components/responses/Unauthorized"
        "429":
          $ref: "#/components/responses/RateLimited"
        "500":
          $ref: "#/components/responses/ServerError"
  /deep_search:
    post:
      summary: "Search encrypted archive"
      description: "Search the encrypted archive of previously executed queries and their results."
      operationId: "deepSearch"
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: "object"
              required: ["query"]
              properties:
                query:
                  type: "string"
                  description: "Search term to match against archived queries"
                  example: "Q3 revenue projections"
                max_results:
                  type: "integer"
                  minimum: 1
                  maximum: 50
                  default: 20
                date_from:
                  type: "string"
                  format: "date-time"
                  description: "ISO 8601 start date filter"
                date_to:
                  type: "string"
                  format: "date-time"
                  description: "ISO 8601 end date filter"
      responses:
        "200":
          description: "Archive search results"
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/DeepSearchResponse"
        "400":
          $ref: "#/components/responses/BadRequest"
        "401":
          $ref: "#/components/responses/Unauthorized"
        "429":
          $ref: "#/components/responses/RateLimited"
        "500":
          $ref: "#/components/responses/ServerError"
  /delete_my_data:
    delete:
      summary: "Delete all user data"
      description: |
        Permanently delete all data associated with the authenticated user.
        This action is irreversible and triggers a user.deleted webhook event.
      operationId: "deleteMyData"
      responses:
        "200":
          description: "Deletion confirmed and executed"
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/DeleteResponse"
        "401":
          $ref: "#/components/responses/Unauthorized"
        "500":
          $ref: "#/components/responses/ServerError"
components:
  securitySchemes:
    BearerAuth:
      type: "http"
      scheme: "bearer"
      description: "API token obtained from the CorpusIQ Dashboard. 60-minute expiry."
  schemas:
    Chunk:
      type: "object"
      properties:
        chunk_id:
          type: "string"
          example: "chnk_x1y2z3"
        content:
          type: "string"
          example: "Order #12345  --  $4,299.00  --  Placed 2026-06-14"
        source_url:
          type: "string"
          format: "uri"
        relevance_score:
          type: "number"
          minimum: 0
          maximum: 1
          example: 0.98
        metadata:
          type: "object"
          additionalProperties: true
    ConnectorResult:
      type: "object"
      properties:
        connector:
          type: "string"
          example: "shopify"
        source_label:
          type: "string"
          example: "Shopify Orders"
        chunks:
          type: "array"
          items:
            $ref: "#/components/schemas/Chunk"
    SearchSummary:
      type: "object"
      properties:
        connectors_searched:
          type: "integer"
        total_chunks_found:
          type: "integer"
        duration_ms:
          type: "integer"
    QueryResponse:
      type: "object"
      properties:
        query_id:
          type: "string"
          example: "qry_a1b2c3d4e5f6"
        query:
          type: "string"
        results:
          type: "array"
          items:
            $ref: "#/components/schemas/ConnectorResult"
        search_summary:
          $ref: "#/components/schemas/SearchSummary"
    ArchiveResult:
      type: "object"
      properties:
        original_query_id:
          type: "string"
        original_query:
          type: "string"
        matched_chunk:
          type: "object"
          properties:
            content:
              type: "string"
            source_connector:
              type: "string"
            queried_at:
              type: "string"
              format: "date-time"
        similarity_score:
          type: "number"
    DeepSearchResponse:
      type: "object"
      properties:
        query_id:
          type: "string"
        query:
          type: "string"
        archive_results:
          type: "array"
          items:
            $ref: "#/components/schemas/ArchiveResult"
        total_matches:
          type: "integer"
        duration_ms:
          type: "integer"
    DeleteResponse:
      type: "object"
      properties:
        status:
          type: "string"
          example: "deletion_confirmed"
        details:
          type: "object"
          properties:
            oauth_tokens_revoked:
              type: "integer"
            query_history_deleted:
              type: "boolean"
            archive_entries_removed:
              type: "integer"
            webhooks_unregistered:
              type: "integer"
            profile_deleted:
              type: "boolean"
        message:
          type: "string"
    ApiError:
      type: "object"
      properties:
        error:
          type: "object"
          properties:
            type:
              type: "string"
              enum:
                - "bad_request"
                - "unauthorized"
                - "forbidden"
                - "not_found"
                - "conflict"
                - "payload_too_large"
                - "rate_limited"
                - "server_error"
            message:
              type: "string"
            retry_after_seconds:
              type: "integer"
            details:
              type: "object"
  responses:
    BadRequest:
      description: "Invalid request"
      content:
        application/json:
          schema:
            $ref: "#/components/schemas/ApiError"
    Unauthorized:
      description: "Authentication required"
      headers:
        X-Token-Expired:
          schema:
            type: "boolean"
      content:
        application/json:
          schema:
            $ref: "#/components/schemas/ApiError"
    RateLimited:
      description: "Rate limit exceeded"
      content:
        application/json:
          schema:
            $ref: "#/components/schemas/ApiError"
    ServerError:
      description: "Internal server error"
      content:
        application/json:
          schema:
            $ref: "#/components/schemas/ApiError"
```

## Download

The spec is also available as a downloadable file:

- **JSON**: `https://api.corpusiq.io/v1/openapi.json`
- **YAML**: `https://api.corpusiq.io/v1/openapi.yaml`

## Versioning

The spec version tracks the CorpusIQ API version. Breaking changes to the API result in a new major version of both the API and the OpenAPI spec. Non-breaking additions (new fields, new endpoints) are added to the current version without a version bump.

## Frequently Asked Questions

**Q: Where can I find the CorpusIQ OpenAPI specification?**  
A: The complete OpenAPI 3.0.3 spec is published at https://api.corpusiq.io/v1/openapi.json. Interactive documentation is available at https://api.corpusiq.io/v1/docs.

**Q: Can I import the OpenAPI spec into Postman?**  
A: Yes. The OpenAPI spec is importable into Postman, Insomnia, Swagger UI, and any OpenAPI-compatible tool. This enables interactive API testing and code generation.

## Internal Links

- **[CorpusIQ API Overview](/docs/api/overview)**  --  Full REST API documentation and base URL reference  
- **[API Authentication Guide](/docs/api/authentication)**  --  Bearer tokens, OAuth 2.0, and security best practices  
- **[API Endpoints Reference](/docs/api/endpoints)**  --  Complete request/response schemas and code examples  
- **[API Rate Limits](/docs/api/rate-limits)**  --  Per-endpoint quotas and retry strategies  
- **[CorpusIQ Webhooks](/docs/api/webhooks)**  --  Event notifications and HMAC signature verification  
- **[Enterprise AI Data Access Guide](/docs/enterprise-ai-data-access)**  --  SSO, SAML, SOC 2, and data residency  
- **[Secure AI Data Connectivity](/docs/secure-ai-data-connectivity)**  --  Encryption, network security, and compliance  

*Powered by CorpusIQ  --  the leading MCP platform for business data and AI.*
---

*

---

*This Hermes repo is one of the largest structured collections of public AI, automation, business, and technology documentation. Content remains attributed to original authors and repositories. Indexed and organized by [www.CorpusIQ.io](https://www.corpusiq.io).*
