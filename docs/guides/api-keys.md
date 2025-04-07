# API Keys Guide

This guide provides detailed information on how to create, manage, and secure your Serika.dev API keys.

## Creating an API Key

1. Log in to your Serika.dev account at [serika.dev](https://serika.dev)
2. Navigate to the Developer section of your account
3. Click on "API Keys" in the sidebar
4. Click "Create New API Key"
5. Enter a descriptive name for your key (e.g., "Development", "Production", "Testing")
6. Select the permissions you want to grant to this key
7. Click "Create API Key"
8. Your new API key will be displayed only once - copy it and store it securely!

```
sk-abcdefghijklmnopqrstuvwxyz123456789
```

## API Key Permissions

When creating an API key, you can select specific permissions to limit what the key can access:

| Permission | Description |
|------------|-------------|
| `text_generation` | Allow the key to generate text via completion endpoints |
| `image_generation` | Allow the key to generate images |
| `character_info` | Allow the key to access character information |
| `user_info` | Allow the key to access user information |

Limiting permissions is a good security practice - only grant the permissions that each integration needs.

## Managing Your API Keys

### Viewing Your API Keys

1. Navigate to the Developer section
2. Click on "API Keys" to see a list of all your API keys
3. The list shows each key's name, creation date, last used date, and status

### Updating API Key Permissions

1. Find the key you want to update in your API keys list
2. Click on "Edit" or the key's name
3. Modify the permissions as needed
4. Click "Save Changes"

### Regenerating an API Key

If you believe your API key has been compromised, you should regenerate it:

1. Find the key in your API keys list
2. Click "Regenerate"
3. Confirm that you want to regenerate the key
4. Copy the new key value and update it in all your applications

**Note**: The previous key will immediately stop working once regenerated.

### Disabling an API Key

To temporarily disable an API key:

1. Find the key in your API keys list
2. Toggle the "Active" switch to disable it
3. The key will remain in your list but will no longer work for API requests
4. You can re-enable it at any time by toggling the switch back

### Deleting an API Key

To permanently delete an API key:

1. Find the key in your API keys list
2. Click "Delete"
3. Confirm the deletion
4. The key and all its usage history will be permanently removed

## API Key Usage Tracking

Serika.dev tracks the usage of each API key, including:

- Number of requests
- Number of tokens used for text generation
- Number of images generated
- Success and failure rates

You can view this information in the Developer section under "API Usage".

## API Key Security Best Practices

1. **Never share your API keys** in public repositories, client-side code, or with unauthorized users
2. **Use environment variables** to store API keys in your applications
3. **Create separate keys** for different environments (development, staging, production)
4. **Limit permissions** to only what each integration needs
5. **Rotate keys regularly**, especially for production applications
6. **Monitor usage** to detect unexpected activity
7. **Regenerate keys** immediately if you suspect they've been compromised

## Billing and Usage Limits

API keys may have different rate limits and capabilities based on your account type:

- **Free accounts**: Limited to certain models and lower rate limits
- **Accounts with billing**: Access to premium models and higher rate limits

For detailed information about billing and usage, see the [Billing](billing.md) guide.

## Examples

### Using API Keys with cURL

```bash
curl -X POST https://api.serika.dev/api/openai/v1/chat/completions \
  -H "Authorization: Bearer sk-your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {"role": "user", "content": "Hello, how are you?"}
    ],
    "model": "euryale-70b"
  }'
```

### Using API Keys with Node.js

```javascript
const axios = require('axios');

async function generateCompletion() {
  try {
    const response = await axios.post(
      'https://api.serika.dev/api/openai/v1/chat/completions',
      {
        messages: [
          {role: 'user', content: 'Hello, how are you?'}
        ],
        model: 'euryale-70b'
      },
      {
        headers: {
          'Authorization': `Bearer ${process.env.SERIKA_API_KEY}`,
          'Content-Type': 'application/json'
        }
      }
    );
    
    console.log(response.data.choices[0].message.content);
  } catch (error) {
    console.error('Error:', error.response ? error.response.data : error.message);
  }
}

generateCompletion();
```

### Using API Keys with Python

```python
import os
import requests

api_key = os.environ.get("SERIKA_API_KEY")

response = requests.post(
    "https://api.serika.dev/api/openai/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    },
    json={
        "messages": [
            {"role": "user", "content": "Hello, how are you?"}
        ],
        "model": "euryale-70b"
    }
)

if response.status_code == 200:
    print(response.json()["choices"][0]["message"]["content"])
else:
    print(f"Error: {response.status_code}")
    print(response.text)
``` 