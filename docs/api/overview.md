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
| `/generate/text` | Legacy endpoint for text generation |
| `/images/generations` | Generate images from text prompts |
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

### API Keys & Usage

| Endpoint | Description |
|----------|-------------|
| `/keys` | Manage API keys |
| `/usage` | Get API usage statistics |

## Authentication

All API requests require an API key for authentication. Include your API key in the `Authorization` header of your requests:

```
Authorization: sk-your-api-key
```

You can also use the `x-api-key` header:

```
x-api-key: sk-your-api-key
```

## Available Models

### Free Tier Models

| Model ID | Name | Description |
|----------|------|-------------|
| `euryale-70b` | Euryale 70B | Default model for free users. Maximum 200 tokens per response. |
| `mistral-7b` | Mistral 7B | Lighter model with good performance. Maximum 200 tokens per response. |

### Premium Tier Models

| Model ID | Name | Description |
|----------|------|-------------|
| `euryale-70b-premium` | Euryale 70B Premium | Enhanced version with higher token limit. Maximum 2000 tokens per response. |
| `gemma-7b` | Gemma 7B | Google's advanced lightweight model. Maximum 2000 tokens per response. |
| `mixtral-8x7b` | Mixtral 8x7B | Powerful model with strong reasoning capabilities. Maximum 2000 tokens per response. |
| `claude-3-opus` | Claude 3 Opus | Anthropic's most capable model. Maximum 2000 tokens per response. |

### Image Generation Models

| Model ID | Name | Description | Tier |
|----------|------|-------------|------|
| `novelai/nai-diffusion-3` | NAI Diffusion 3 | NovelAI's latest image generation model | Free & Premium |
| `novelai/nai-diffusion` | NAI Diffusion | NovelAI's stable diffusion model | Free & Premium |

## Response Format

All responses are returned in JSON format. Successful responses typically include the requested data, while error responses include an `error` object with details about what went wrong.

### Success Response Example

```json
{
  "id": "chatcmpl-123abc",
  "object": "chat.completion",
  "created": 1677858242,
  "model": "euryale-70b",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Hello! How can I help you today?"
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 13,
    "completion_tokens": 7,
    "total_tokens": 20
  }
}
```

### Error Response Example

```json
{
  "error": {
    "message": "Invalid API key",
    "type": "authentication_error",
    "code": "invalid_api_key"
  }
}
```

## Rate Limits

Rate limits vary based on your account type and subscription:

- **Free tier**: Limited to 60 requests per minute
- **Premium tier**: Up to 200 requests per minute

API requests that exceed these limits will receive a `429 Too Many Requests` status code with a `Retry-After` header indicating how long to wait before retrying.

## Detailed Documentation

For detailed information about each endpoint, including request parameters and response formats, see the specific endpoint documentation:

- [Authentication](authentication.md)
- [Chat Completions](chat-completions.md)
- [Text Generation](text-generation.md)
- [Image Generation](image-generation.md)
- [Characters](characters.md) 