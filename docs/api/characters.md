# Characters

Serika.dev allows you to access and use its character database through the API. This enables you to generate AI responses with specific character personalities or retrieve information about available characters.

## List Characters

```
GET /characters
```

This endpoint returns a list of public characters available on Serika.dev.

### Authorization

This endpoint requires an API key with the `character_info` permission.

### Example Request

```bash
curl -X GET https://api.serika.dev/api/openai/v1/characters \
  -H "Authorization: Bearer sk-your-api-key"
```

### Response Format

```json
[
  {
    "id": "12345-abcde",
    "name": "Detective Holmes",
    "description": "A brilliant detective who solves mysteries with deductive reasoning",
    "avatar": "https://api.serika.dev/api/cdn/avatars/detective_holmes.png",
    "creator": "Serika",
    "createdOn": "2023-04-15T10:30:00Z",
    "tags": ["detective", "mystery", "intelligent"],
    "isNSFW": false
  },
  {
    "id": "67890-fghij",
    "name": "Space Captain Nova",
    "description": "A brave space captain exploring the galaxy",
    "avatar": "https://api.serika.dev/api/cdn/avatars/captain_nova.png",
    "creator": "StarExplorer",
    "createdOn": "2023-05-20T14:45:00Z",
    "tags": ["space", "sci-fi", "adventure"],
    "isNSFW": false
  }
  // ... more characters
]
```

## Get Character Details

```
GET /characters/:id
```

This endpoint returns detailed information about a specific character.

### Path Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `id` | string | The unique identifier of the character |

### Authorization

This endpoint requires an API key with the `character_info` permission.

### Example Request

```bash
curl -X GET https://api.serika.dev/api/openai/v1/characters/12345-abcde \
  -H "Authorization: Bearer sk-your-api-key"
```

### Response Format

```json
{
  "id": "12345-abcde",
  "name": "Detective Holmes",
  "description": "A brilliant detective who solves mysteries with deductive reasoning",
  "avatar_url": "https://api.serika.dev/api/cdn/avatars/detective_holmes.png",
  "created_at": "2023-04-15T10:30:00Z",
  "is_nsfw": false,
  "tags": ["detective", "mystery", "intelligent"],
  "has_starter_message": true
}
```

## Using Characters in Completions

To use a character in your chat completions or text generation requests, include the `character_id` parameter in your request:

```bash
curl -X POST https://api.serika.dev/api/openai/v1/chat/completions \
  -H "Authorization: Bearer sk-your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {"role": "user", "content": "I found a strange footprint in my garden. Can you help me identify it?"}
    ],
    "model": "euryale-70b",
    "character_id": "12345-abcde"
  }'
```

The response will be generated using the character's personality and background information:

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
        "content": "Ah, a footprint in your garden! Most intriguing. Can you describe its shape and size? Any distinct patterns? The soil composition can tell us much about when it was made. Was there rain recently? Detective work is all about the details, my dear friend."
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 23,
    "completion_tokens": 45,
    "total_tokens": 68
  }
}
```

## Error Responses

### Character Not Found

```json
{
  "error": {
    "message": "Character not found",
    "type": "not_found_error",
    "param": "id"
  }
}
```

### Private Character

```json
{
  "error": {
    "message": "This is a private character",
    "type": "permission_error",
    "code": "private_character"
  }
}
```

### Insufficient Permissions

```json
{
  "error": {
    "message": "API key does not have permission to access character information",
    "type": "permission_error",
    "code": "insufficient_permissions"
  }
}
```

## Character Ownership and Privacy

- **Public Characters**: Any API key with the `character_info` permission can access public characters
- **Private Characters**: Only the creator can access private characters
- **Character Content**: The API does not expose sensitive character information like full system prompts

## Usage with Billing

Using a character in the chat completions or text generation endpoint does not incur any additional cost beyond the normal token usage.

For more information about billing and usage, see the [Billing](../guides/billing.md) page. 