# Authentication

All requests to the Serika.dev Customer API require authentication using API keys. This guide explains how to create, use, and manage your API keys.

## API Keys

API keys are unique identifiers that authenticate your requests to the Serika.dev API. Each key is associated with your account and has specific permissions and usage tracking.

### Creating an API Key

1. Log in to your Serika.dev account at [serika.dev](https://serika.dev)
2. Navigate to the Developer section
3. Click "Create API Key"
4. Enter a name for your key (e.g., "Development", "Production")
5. Click "Create"
6. **Important**: Copy and securely store your API key. It will only be shown once!

```
sk-abcdefghijklmnopqrstuvwxyz123456789
```

## Using Your API Key

To authenticate your API requests, include your API key in one of the following header formats:

```
Authorization: Bearer sk-your-api-key
```

Or alternatively:

```
x-api-key: sk-your-api-key
```

### Example Request with Authentication

```bash
curl -X POST https://api.serika.dev/v1/chat/completions \
  -H "Authorization: Bearer sk-your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {"role": "user", "content": "Hello, how are you?"}
    ],
    "model": "gpt-3.5-turbo"
  }'
```

## API Key Permissions

Each API key can have different permissions, allowing you to control what operations it can perform. When creating or updating a key, you can specify these permissions:

| Permission | Description |
|------------|-------------|
| `text_generation` | Allow the key to generate text via completion endpoints |
| `image_generation` | Allow the key to generate images |
| `character_info` | Allow the key to access character information |
| `user_info` | Allow the key to access user information |

By default, new API keys are granted all permissions. It's a good security practice to restrict permissions to only what each integration needs.

### Endpoint-Permission Mapping

Here's how permissions map to specific endpoints:

| Endpoint | Required Permission |
|----------|---------------------|
| `/v1/chat/completions` | `text_generation` |
| `/v1/generate/text` | `text_generation` |
| `/v1/images/generations` | `image_generation` |
| `/v1/generate/image` | `image_generation` |
| `/v1/characters/*` | `character_info` |
| `/v1/users/*` | `user_info` |

Accessing an endpoint without the required permission will result in a `403 Forbidden` error with a message indicating the missing permission.

## Managing API Keys

### Viewing Your API Keys

You can view all your API keys in the Developer section of your Serika.dev account. This view shows:

- Key name
- Creation date
- Last used date
- Total usage (tokens and images)
- Status (active/disabled)
- Billing setup status

### Regenerating an API Key

If you believe your API key has been compromised, you should regenerate it:

1. Navigate to the Developer section
2. Find the key you want to regenerate
3. Click "Regenerate"
4. Confirm the action
5. Copy the new key value and update it in all your applications

**Note**: The previous key will immediately stop working once regenerated.

### Disabling an API Key

To temporarily disable an API key:

1. Navigate to the Developer section
2. Find the key you want to disable
3. Click "Disable"
4. The key will remain in your list but will no longer work for API requests

Requests made with a disabled API key will receive a `401 Unauthorized` response with a message indicating that the key has been deactivated.

### Deleting an API Key

To permanently delete an API key:

1. Navigate to the Developer section
2. Find the key you want to delete
3. Click "Delete"
4. Confirm the deletion
5. **Note**: This action cannot be undone, and all usage history for the key will be permanently removed

## Rate Limiting

Serika.dev applies rate limits to API requests based on your account type:

- **Free tier**: 60 requests per minute
- **Premium tier**: 200 requests per minute

Rate limiting is applied at the user level, meaning all API keys associated with your account share the same rate limit pool.

If you exceed your rate limit, you'll receive a `429 Too Many Requests` status code response with a `Retry-After` header indicating how long to wait before making another request.

## Billing Setup and Premium Features

Some endpoints and features require billing setup:

- Premium AI models (like Llama 4 Maverick, Lumimaid 70B, etc.)
- Higher rate limits
- Higher token limits for completions

When making a request to a premium endpoint without billing setup, you'll receive a `403 Forbidden` response with an error type of `billing_error` and code `billing_not_setup`.

## Error Responses

### Invalid API Key

```json
{
  "error": {
    "message": "Invalid API key provided",
    "type": "invalid_request_error",
    "code": "invalid_api_key"
  }
}
```

### Missing API Key

```json
{
  "error": {
    "message": "No API key provided",
    "type": "invalid_request_error",
    "code": "no_api_key"
  }
}
```

### Disabled API Key

```json
{
  "error": {
    "message": "This API key has been deactivated",
    "type": "invalid_request_error",
    "code": "inactive_api_key"
  }
}
```

### Insufficient Permissions

```json
{
  "error": {
    "message": "API key does not have the required permission: text_generation",
    "type": "permission_error",
    "code": "insufficient_permissions"
  }
}
```

### Rate Limit Exceeded

```json
{
  "error": {
    "message": "Too many requests, please try again later.",
    "type": "rate_limit_error",
    "code": "rate_limit_exceeded"
  }
}
```

### Billing Not Setup

```json
{
  "error": {
    "message": "This endpoint requires billing setup",
    "type": "billing_error",
    "code": "billing_not_setup"
  }
}
```

## Security Best Practices

- Never share your API keys or commit them to public repositories
- Use environment variables or secret management services to store your keys
- Create separate API keys for different applications or environments
- Regularly rotate your API keys, especially for production applications
- Use the minimum required permissions for each key
- Monitor your API key usage for unexpected activity 