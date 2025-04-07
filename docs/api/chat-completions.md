# Chat Completions

The chat completions endpoint allows you to generate conversational AI responses using various models available on Serika.dev.

## Endpoint

```
POST /chat/completions
```

## Request Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `messages` | array | Yes | An array of messages, where each message has a `role` and `content`. Roles can be `user` or `assistant`. |
| `model` | string | No | The model to use for generation. Defaults to `euryale-70b` for free users. |
| `stream` | boolean | No | If set to `true`, the response will be streamed as data chunks. Defaults to `false`. |
| `character_id` | string | No | ID of a character to use for generation. The character's personality will influence the response. |
| `temperature` | number | No | Controls randomness of the output. Higher values (e.g., 0.8) make output more random, lower values (e.g., 0.2) make it more deterministic. Defaults to 0.7. |
| `system_prompt` | string | No | Custom system prompt to override or complement the default or character-based system prompt. |
| `max_tokens` | integer | No | Maximum number of tokens to generate. Free tier is limited to 200 tokens, premium users can use up to 2000 tokens. |

## Available Models

### Free Tier Models

| Model ID | Name | Description | Max Tokens |
|----------|------|-------------|------------|
| `euryale-70b` | Euryale 70B | Primary model for free users - high quality roleplay model | 200 |
| `deepseek-chat` | DeepSeek Chat | Backup model for free users - high quality roleplay model | 200 |
| `llama-3.2-11b-instruct` | Llama 3.2 11B | Backup model for free users - high quality general purpose model | 200 |
| `cognitivecomputations/dolphin3.0-mistral-24b:free` | Dolphin 24B | General purpose model for free users | 200 |
| `rogue-rose-103b-v0.2` | Rogue Rose 103B | Japanese model for free users - high quality roleplay model | 200 |
| `llama-4-scout-17b-instruct` | Llama 4 Scout (Zukijourney) | High quality general purpose model | 200 |
| `gemini-2.0-flash` | Gemini 2.0 Flash | Fallback model - high quality general purpose model | 200 |

### Premium Tier Models (Requires Billing Setup)

| Model ID | Name | Description | Max Tokens |
|----------|------|-------------|------------|
| `neversleep/llama-3.1-lumimaid-70b` | Lumimaid 70B | Premium model with enhanced roleplay capabilities | 2000 |
| `sao10k/l3.1-70b-hanami-x1` | Hanami X1 | Backup model for premium users - high quality roleplay model | 2000 |
| `meta-llama/llama-4-scout` | Llama 4 Scout (openrouter) | High quality general purpose model | 2000 |
| `meta-llama/llama-4-maverick` | Llama 4 Maverick | High quality general purpose model | 2000 |
| `sao10k/l3.3-euryale-70b` | Euryale 70B (L3.3) | Backup model for premium users - high quality roleplay model | 2000 |

Free users are limited to the free tier models and a maximum of 200 tokens per response. Premium users (with billing setup) can access all models with up to 2000 tokens per response.

## Example Request

### Basic Request

```bash
curl -X POST https://api.serika.dev/api/openai/v1/chat/completions \
  -H "Authorization: sk-your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {"role": "user", "content": "Tell me a joke about programming"}
    ],
    "model": "euryale-70b"
  }'
```

### Conversation Request

```bash
curl -X POST https://api.serika.dev/api/openai/v1/chat/completions \
  -H "Authorization: sk-your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {"role": "user", "content": "Hello, how are you?"},
      {"role": "assistant", "content": "I'm doing well, thank you for asking! How can I help you today?"},
      {"role": "user", "content": "Can you explain how APIs work?"}
    ],
    "model": "meta-llama/llama-4-maverick"
  }'
```

### Using a Character

```bash
curl -X POST https://api.serika.dev/api/openai/v1/chat/completions \
  -H "Authorization: sk-your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {"role": "user", "content": "Hello, how are you today?"}
    ],
    "model": "euryale-70b",
    "character_id": "12345-abcde"
  }'
```

### Using a Custom System Prompt

```bash
curl -X POST https://api.serika.dev/api/openai/v1/chat/completions \
  -H "Authorization: sk-your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {"role": "user", "content": "Write a poem about the ocean"}
    ],
    "model": "neversleep/llama-3.1-lumimaid-70b",
    "system_prompt": "You are a professional poet who specializes in nature poetry. You write in a style reminiscent of Emily Dickinson."
  }'
```

### Streaming Response

```bash
curl -X POST https://api.serika.dev/api/openai/v1/chat/completions \
  -H "Authorization: sk-your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {"role": "user", "content": "Tell me a story about a dragon"}
    ],
    "model": "sao10k/l3.1-70b-hanami-x1",
    "stream": true
  }'
```

## Response Format

### Standard Response

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
        "content": "Why did the programmer quit his job? Because he didn't get arrays!"
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 13,
    "completion_tokens": 15,
    "total_tokens": 28
  }
}
```

### Streaming Response

When the `stream` parameter is set to `true`, the response will be delivered as a series of server-sent events (SSE). Each event contains a chunk of the response:

```
data: {"choices":[{"delta":{"content":"Why"},"index":0}]}

data: {"choices":[{"delta":{"content":" did"},"index":0}]}

data: {"choices":[{"delta":{"content":" the"},"index":0}]}

data: {"choices":[{"delta":{"content":" programmer"},"index":0}]}

... (more chunks) ...

data: {"choices":[{"delta":{"content":"!"},"index":0}]}

data: [DONE]
```

## Model Fallbacks

If your requested model is unavailable, Serika.dev will automatically try to use appropriate fallback models:

1. First, it will try alternate models from the same provider
2. Then, it will try models from different providers
3. If all models fail, a generic fallback message will be returned

This ensures your requests will be processed even if specific models are temporarily unavailable.

## Error Responses

### Invalid Request

```json
{
  "error": {
    "message": "messages is required and must be an array",
    "type": "invalid_request_error",
    "param": "messages"
  }
}
```

### Authentication Error

```json
{
  "error": {
    "message": "Invalid API key provided",
    "type": "authentication_error"
  }
}
```

### Billing Required for Premium Models

```json
{
  "error": {
    "message": "This endpoint requires billing setup",
    "type": "billing_error",
    "code": "billing_not_setup"
  }
}
```

### Rate Limit Error

```json
{
  "error": {
    "message": "Rate limit exceeded",
    "type": "rate_limit_error"
  }
}
```

## Usage and Billing

Usage is calculated based on the number of tokens in both the request and response. A token is approximately 4 characters or 0.75 words.

For example, the sentence "Hello, how are you?" is approximately 4 tokens.

Usage is billed based on your account's pricing plan. See the [Billing](../guides/billing.md) page for more information.

### Token Limits

- **Free tier**: Maximum of 200 tokens per response
- **Premium tier**: Up to 2000 tokens per response

## Best Practices

1. **Select the appropriate model** for your use case:
   - For roleplay or creative content: `euryale-70b`, `neversleep/llama-3.1-lumimaid-70b`, or `sao10k/l3.1-70b-hanami-x1`
   - For technical or factual content: `meta-llama/llama-4-maverick` or `meta-llama/llama-4-scout`
   - For Japanese content: `rogue-rose-103b-v0.2`

2. **Structure conversations properly** with alternating user and assistant messages for better context understanding.

3. **Use system prompts** to guide the model's behavior and response style.

4. **Consider streaming responses** for a more interactive user experience with real-time feedback. 