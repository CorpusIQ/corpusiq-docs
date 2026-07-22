# API Endpoints

The CorpusIQ API is organized around REST principles. All endpoints return JSON.

Base URL: `https://api.corpusiq.io/v1`

## Connectors

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/connectors` | List all connected data sources |
| GET | `/connectors/{id}` | Get connector details and status |
| POST | `/connectors` | Add a new connector |
| DELETE | `/connectors/{id}` | Remove a connector |

## Queries

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/queries` | Execute a natural language query |
| GET | `/queries/{id}` | Get query status and results |
| GET | `/queries` | List recent queries |

## Account

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/account` | Get account details |
| PATCH | `/account` | Update account settings |
| GET | `/account/usage` | Get usage statistics |

## Teams (Enterprise)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/teams` | List team members |
| POST | `/teams` | Invite a team member |
| DELETE | `/teams/{id}` | Remove a team member |

For full endpoint details, see the [OpenAPI specification](openapi.md).
