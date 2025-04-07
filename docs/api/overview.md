# API Reference Overview

The Serika.dev Customer API provides several endpoints for interacting with Serika's AI capabilities. This page provides an overview of the available endpoints.

## Base URL

All API requests should be made to the following base URL:

```
https://api.serika.dev
```

## Available Endpoints

### AI Generation

| Endpoint | Description |
|----------|-------------|
| `/v1/chat/completions` | Generate conversational responses with AI models |
| `/v1/generate/text` | Legacy endpoint for text generation |
| `/v1/images/generations` | Generate images from text prompts |
| `/v1/generate/image` | Legacy endpoint for image generation |

### Models

| Endpoint | Description |
|----------|-------------|
| `/v1/models` | List available AI models |

### Characters

| Endpoint | Description |
|----------|-------------|
| `/v1/characters` | List available characters |
| `/v1/characters/:id` | Get details about a specific character |

### API Keys & Usage

| Endpoint | Description |
|----------|-------------|
| `/v1/keys` | Manage API keys |
| `/v1/usage` | Get API usage statistics |

## Authentication

All API requests require an API key for authentication. Include your API key in the `Authorization` header of your requests:

```
Authorization: Bearer sk-your-api-key
```

You can also use the `x-api-key` header:

```
x-api-key: sk-your-api-key
```

## Available Models

### Free Tier Models

| Model ID | Name | Description |
|----------|------|-------------|
| `euryale-70b` | Euryale 70B | Primary model for free users - high quality roleplay model |
| `deepseek-chat` | DeepSeek Chat | Backup model for free users - high quality roleplay model |
| `llama-3.2-11b-instruct` | Llama 3.2 11B | Backup model for free users - high quality general purpose model |
| `cognitivecomputations/dolphin3.0-mistral-24b:free` | Dolphin 24B | General purpose model for free users |
| `rogue-rose-103b-v0.2` | Rogue Rose 103B | Japanese model for free users - high quality roleplay model |
| `llama-4-scout-17b-instruct` | Llama 4 Scout (Zukijourney) | High quality general purpose model |
| `gemini-2.0-flash` | Gemini 2.0 Flash | Fallback model - high quality general purpose model |

### Premium Tier Models

| Model ID | Name | Description |
|----------|------|-------------|
| `neversleep/llama-3.1-lumimaid-70b` | Lumimaid 70B | Premium model with enhanced roleplay capabilities |
| `sao10k/l3.1-70b-hanami-x1` | Hanami X1 | Backup model for premium users - high quality roleplay model |
| `meta-llama/llama-4-scout` | Llama 4 Scout (openrouter) | High quality general purpose model |
| `meta-llama/llama-4-maverick` | Llama 4 Maverick | High quality general purpose model |
| `sao10k/l3.3-euryale-70b` | Euryale 70B (L3.3) | Backup model for premium users - high quality roleplay model |

### Image Generation Models

| Model ID | Name | Description | Tier |
|----------|------|-------------|------|
| `novelai/nai-diffusion-3` | NAI Diffusion 3 | NovelAI's latest image generation model | Free |
| `novelai/nai-diffusion` | NAI Diffusion | NovelAI's stable diffusion model | Free |
| `nai-diffusion-4-curated-preview` | NAI Diffusion 4 | NovelAI's latest image generation model | Premium |

## Response Format

All responses are returned in JSON format. Successful responses typically include the requested data, while error responses include an `error` object with details about what went wrong.

### Success Response Example

```json
{
  "id": "chatcmpl-123abc",
  "object": "chat.completion",
  "created": 1677858242,
  "model": "gpt-3.5-turbo",
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