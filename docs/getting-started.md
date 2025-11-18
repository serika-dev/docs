# Getting Started

Welcome to the Serika.dev API! This guide will help you make your first API request in minutes.

## 1. Get Your API Key

First, you need an API key.
1. Log in to your [Serika.dev Developer Dashboard](https://developers.serika.dev).
2. Navigate to the **API Keys** section.
3. Click **Create New Key** and copy it.

## 2. Install the OpenAI Library

Serika.dev is compatible with the standard OpenAI client libraries, making integration effortless.

```{tab-set}
```{tab-item} Python
```bash
pip install openai
```
```
```{tab-item} Node.js
```bash
npm install openai
```
```
```

## 3. Make Your First Request

Create a file named `test_api.py` (or `test_api.js`) and add the following code.

```{tab-set}
```{tab-item} Python
```python
from openai import OpenAI

# Initialize the client with Serika's base URL
client = OpenAI(
    base_url="https://api.serika.dev/api/openai/v1",
    api_key="YOUR_API_KEY_HERE"
)

# Create a chat completion
response = client.chat.completions.create(
    model="openai/gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Hello, world!"}
    ]
)

print(response.choices[0].message.content)
```
```
```{tab-item} JavaScript
```javascript
import OpenAI from 'openai';

const client = new OpenAI({
  baseURL: 'https://api.serika.dev/api/openai/v1',
  apiKey: 'YOUR_API_KEY_HERE',
});

async function main() {
  const completion = await client.chat.completions.create({
    messages: [{ role: 'user', content: 'Hello, world!' }],
    model: 'openai/gpt-4o-mini',
  });

  console.log(completion.choices[0].message.content);
}

main();
```
```
```{tab-item} cURL
```bash
curl https://api.serika.dev/api/openai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY_HERE" \
  -d '{
    "model": "openai/gpt-4o-mini",
    "messages": [{"role": "user", "content": "Hello, world!"}]
  }'
```
```
```

## Next Steps

- Explore [Chat Completions](api/chat-completions.md) to build conversational apps.
- Check out [Image Generation](api/image-generation.md) to create art.
- See the [Examples](examples.md) page for more code snippets.