# API Reference Overview

The Serika.dev Customer API provides several endpoints for interacting with Serika's AI capabilities. This page provides an overview of the available endpoints.

## Base URL

All API requests should be made to the following base URL:

```
https://api.serika.dev/api/openai/v1
```

## Available Endpoints

### AI Generation

| Endpoint | Description |
|----------|-------------|
| `/chat/completions` | Generate conversational responses with AI models |
| `/images/generations` | Generate images from text prompts |
| `/jobs/image` | Submit asynchronous image generation jobs |
| `/jobs/:id` | Check status of asynchronous jobs |

### Legacy Endpoints

| Endpoint | Description |
|----------|-------------|
| `/generate/text` | Legacy endpoint for text generation |
| `/generate/image` | Legacy endpoint for image generation |

### Models

| Endpoint | Description |
|----------|-------------|
| `/models` | List available AI models |

### Characters

| Endpoint | Description |
|----------|-------------|
| `/characters` | List available characters |
| `/characters/:id` | Get details about a specific character |

## Authentication

All API requests require an API key for authentication. Include your API key in the `Authorization` header of your requests:

```http
Authorization: Bearer sk-your-api-key
```

## Response Format

All responses are returned in JSON format. Successful responses typically include the requested data, while error responses include an `error` object with details about what went wrong.

### Success Response Example

```json
{
  "id": "chatcmpl-123abc",
  "object": "chat.completion",
  "created": 1677858242,
  "model": "openai/gpt-4o-mini",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Hello! How can I help you today?"
      },
      "finish_reason": "stop"
    }
  ]
}
```

## Rate Limits

Rate limits vary based on your account type and subscription:

- **Free tier**: Limited requests per minute.
- **Premium tier**: Higher rate limits for production use.

API requests that exceed these limits will receive a `429 Too Many Requests` status code.

## Detailed Documentation

For detailed information about each endpoint, including request parameters and response formats, see the specific endpoint documentation:

- [Authentication](authentication.md)
- [Chat Completions](chat-completions.md)
- [Image Generation](image-generation.md)
- [Jobs API](jobs.md)
- [Characters](characters.md)