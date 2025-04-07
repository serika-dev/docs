# Text Generation (Legacy)

The text generation endpoint is a legacy endpoint for generating text responses. For new integrations, we recommend using the [Chat Completions](chat-completions.md) endpoint instead.

## Text Generation Endpoint

> **Note:** This is a legacy endpoint. While it still works, we recommend using the [Chat Completions](/api/chat-completions) endpoint for new integrations.

```
POST /generate/text
```

This endpoint generates text completions based on a given prompt. It's useful for scenarios where you need straightforward text continuation rather than a conversational experience.

### Request Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `prompt` | string | Yes | The text prompt to generate a completion for |
| `model` | string | No | The AI model to use. Default is `euryale-70b` |
| `max_tokens` | integer | No | Maximum number of tokens to generate. Default is 100. Free users limited to 200, Premium users up to 2000 |
| `temperature` | number | No | Controls randomness (0-1). Lower is more deterministic, higher is more creative. Default is 0.7 |
| `stop` | string or array | No | Sequences where the API will stop generating further tokens |
| `character_id` | string | No | ID of a character to use for generating the response |

### Available Models

#### Free Tier
- **euryale-70b** - Default model for free users. Maximum 200 tokens per response.
- **mistral-7b** - Lighter model with good performance. Maximum 200 tokens per response.

#### Premium Tier
- **euryale-70b-premium** - Enhanced version with higher token limit. Maximum 2000 tokens per response.
- **gemma-7b** - Google's advanced lightweight model. Maximum 2000 tokens per response.
- **mixtral-8x7b** - Powerful model with strong reasoning capabilities. Maximum 2000 tokens per response.
- **claude-3-opus** - Anthropic's most capable model. Maximum 2000 tokens per response.

Free users are limited to Free Tier models and a maximum of 200 tokens per response. Premium users can access all models with up to 2000 tokens per response.

### Example Request

```bash
curl -X POST https://api.serika.dev/api/openai/v1/generate/text \
  -H "Authorization: sk-your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Once upon a time in a distant galaxy",
    "model": "euryale-70b",
    "max_tokens": 150,
    "temperature": 0.8
  }'
```

### Response Format

```json
{
  "id": "txt-abc123def456",
  "text": "Once upon a time in a distant galaxy, there existed a civilization of beings who had mastered the art of interstellar travel. Their ships, powered by the energy of collapsed stars, could traverse the vast emptiness between solar systems in mere days. The people of this advanced society had evolved beyond the need for physical bodies, existing instead as pure consciousness stored in crystalline matrices. They called themselves the Luminous, for their essence glowed with an inner light that could be perceived across dimensions.",
  "usage": {
    "prompt_tokens": 8,
    "completion_tokens": 86,
    "total_tokens": 94
  }
}
```

### Error Responses

| Status Code | Error Code | Message | Description |
|-------------|------------|---------|-------------|
| 400 | `invalid_request` | Missing required field: prompt | The prompt parameter is missing |
| 400 | `invalid_request` | Invalid model: [model] | The specified model is not supported |
| 401 | `authentication_error` | Invalid API key | The API key is invalid or missing |
| 402 | `billing_required` | This request requires billing | The request requires a premium account |
| 429 | `rate_limit_exceeded` | You have exceeded your rate limit | Too many requests in a given time period |

## Differences from Chat Completions

The text generation endpoint is simpler but less flexible than the [Chat Completions](/api/chat-completions) endpoint:

1. It doesn't support multi-turn conversations
2. It doesn't have the concept of different message roles (system, user, assistant)
3. It's optimized for straightforward text continuation rather than conversation

## Migrating to Chat Completions

If you're using the text generation endpoint, we recommend migrating to the chat completions endpoint for better results and more flexibility:

```bash
# Text Generation (Legacy)
curl -X POST https://api.serika.dev/api/openai/v1/generate/text \
  -H "Authorization: sk-your-api-key" \
  -d '{
    "prompt": "Tell me about the solar system",
    "model": "euryale-70b"
  }'

# Chat Completions (Recommended)
curl -X POST https://api.serika.dev/api/openai/v1/chat/completions \
  -H "Authorization: sk-your-api-key" \
  -d '{
    "messages": [
      {"role": "user", "content": "Tell me about the solar system"}
    ],
    "model": "euryale-70b"
  }'
```

## Usage and Billing

Usage is calculated based on the number of tokens in both the request and response, just like with the chat completions endpoint.

A token is approximately 4 characters or 0.75 words. For example, the sentence "Tell me about artificial intelligence" is approximately 7 tokens.

Usage is billed based on your account's pricing plan. See the [Billing](../guides/billing.md) page for more information. 