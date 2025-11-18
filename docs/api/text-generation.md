# Text Generation (Legacy)

> [!WARNING]
> This is a legacy endpoint. We strongly recommend using the [Chat Completions](chat-completions.md) endpoint for all new projects.

The text generation endpoint (`/generate/text`) is designed for simple text completion tasks. It does not support the full conversational capabilities of the Chat API.

## Endpoint

`POST https://api.serika.dev/api/openai/v1/generate/text`

## Request Parameters

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `prompt` | string | Yes | The input text to complete. |
| `model` | string | No | The model ID. |
| `max_tokens` | integer | No | Maximum tokens to generate. |
| `temperature` | number | No | Randomness of the output. |

## Example

```bash
curl -X POST https://api.serika.dev/api/openai/v1/generate/text \
  -H "Authorization: Bearer sk-your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Once upon a time",
    "model": "euryale-70b",
    "max_tokens": 50
  }'
```