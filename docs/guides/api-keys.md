# API Keys Guide

This guide provides detailed information on how to create, manage, and secure your Serika.dev API keys.

## Creating an API Key

1. Log in to your Serika.dev account at [developers.serika.dev](https://developers.serika.dev)
2. Navigate to the **API Keys** section
3. Click **Create New API Key**
4. Enter a descriptive name for your key (e.g., "Development", "Production")
5. Select the permissions you want to grant
6. Click **Create API Key**
7. Copy your new key immediately. You won't be able to see it again!

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

1. Navigate to the [Developer Dashboard](https://developers.serika.dev)
2. Click on **API Keys** to see a list of all your keys
3. The list shows each key's name, creation date, last used date, and status

### Regenerating an API Key

If you believe your API key has been compromised:

1. Find the key in your list
2. Click **Regenerate**
3. Confirm the action
4. Update your applications with the new key immediately

**Note**: The old key will stop working instantly.

### Deleting an API Key

To permanently remove access:

1. Find the key in your list
2. Click **Delete**
3. Confirm deletion

## API Key Security Best Practices

1. **Never share your API keys** in public repositories or client-side code.
2. **Use environment variables** to store API keys.
3. **Create separate keys** for different environments (dev, prod).
4. **Rotate keys regularly** for production applications.

## Examples

Here is how to use your API key with different languages.

<div class="tabbed-set" data-tabs="1:3">
<input checked="checked" id="__tabbed_1_1" name="__tabbed_1" type="radio">
<label for="__tabbed_1_1">Python</label>
<div class="tabbed-content">
```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.serika.dev/api/openai/v1",
    api_key="sk-your-api-key"
)

response = client.chat.completions.create(
    model="openai/gpt-4o-mini",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response.choices[0].message.content)
```
</div>
<input id="__tabbed_1_2" name="__tabbed_1" type="radio">
<label for="__tabbed_1_2">JavaScript</label>
<div class="tabbed-content">
```javascript
import OpenAI from 'openai';

const client = new OpenAI({
  baseURL: 'https://api.serika.dev/api/openai/v1',
  apiKey: 'sk-your-api-key',
});

async function main() {
  const response = await client.chat.completions.create({
    model: 'openai/gpt-4o-mini',
    messages: [{ role: 'user', content: 'Hello!' }],
  });
  console.log(response.choices[0].message.content);
}
main();
```
</div>
<input id="__tabbed_1_3" name="__tabbed_1" type="radio">
<label for="__tabbed_1_3">cURL</label>
<div class="tabbed-content">
```bash
curl https://api.serika.dev/api/openai/v1/chat/completions \
  -H "Authorization: Bearer sk-your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "openai/gpt-4o-mini",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```
</div>
</div>