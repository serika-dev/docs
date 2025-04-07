# Text Generation (Legacy)

The text generation endpoint is a legacy endpoint for generating text responses. For new integrations, we recommend using the [Chat Completions](chat-completions.md) endpoint instead.

## Endpoint

```
POST /v1/generate/text
```

## Request Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `messages` | array | Yes | An array of messages, where each message has a `role` and `content`. Roles can be `user` or `assistant`. |
| `model` | string | No | The model to use for generation. Defaults to `gpt-3.5-turbo`. |
| `character_id` | string | No | ID of a character to use for generation. The character's personality will influence the response. |
| `temperature` | number | No | Controls randomness of the output. Higher values make output more random, lower values make it more deterministic. Defaults to 0.7. |
| `system_prompt` | string | No | Custom system prompt to override or complement the default or character-based system prompt. |

## Example Request

```bash
curl -X POST https://api.serika.dev/v1/generate/text \
  -H "Authorization: Bearer sk-your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {"role": "user", "content": "Tell me about artificial intelligence"}
    ],
    "model": "gpt-3.5-turbo"
  }'
```

## Response Format

```json
{
  "id": "txtgen-123abc",
  "model": "gpt-3.5-turbo",
  "content": "Artificial intelligence (AI) refers to the simulation of human intelligence in machines that are programmed to think like humans and mimic their actions. The term may also be applied to any machine that exhibits traits associated with a human mind such as learning and problem-solving...",
  "usage": {
    "prompt_tokens": 6,
    "completion_tokens": 78,
    "total_tokens": 84
  }
}
```

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

## Differences from Chat Completions

The text generation endpoint differs from the chat completions endpoint in the following ways:

1. The response format is simpler, with just the generated text rather than a choices array
2. Streaming is not supported
3. The endpoint is optimized for single-turn interactions rather than conversations

## Migration to Chat Completions

To migrate from the text generation endpoint to the chat completions endpoint:

1. Update your endpoint URL from `/v1/generate/text` to `/v1/chat/completions`
2. Update your code to handle the different response format
3. Consider using the `stream` parameter for real-time responses

## Usage and Billing

Usage is calculated based on the number of tokens in both the request and response, just like with the chat completions endpoint.

A token is approximately 4 characters or 0.75 words. For example, the sentence "Tell me about artificial intelligence" is approximately 7 tokens.

Usage is billed based on your account's pricing plan. See the [Billing](../guides/billing.md) page for more information. 