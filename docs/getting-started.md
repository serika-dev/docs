# Getting Started

Welcome to the Serika.dev API! This guide will help you make your first API request in minutes.

## 1. Get Your API Key

First, you need an API key.
1. Log in to your [Serika.dev Developer Dashboard](https://developers.serika.dev).
2. Navigate to the **API Keys** section.
3. Click **Create New Key** and copy it.

## 2. Install the OpenAI Library

Serika.dev is compatible with the standard OpenAI client libraries, making integration effortless.

````` {tabs}
```` {group-tab} Python
```bash
pip install openai
```
````
```` {group-tab} Node.js
```bash
npm install openai
```
````
`````

## 3. Make Your First Request

Create a file named `test_api.py` (or `test_api.js`) and add the following code.

````` {tabs}
```` {group-tab} Python
```python
from openai import OpenAI

# Initialize the client with Serika's base URL
client = OpenAI(
    base_url="https://api.serika.dev/api/openai/v1",
    api_key="your_api_key"
)

# Create a chat completion
response = client.chat.completions.create(
    model="openai/gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ]
)

print(response.choices[0].message.content)
```
````
```` {group-tab} JavaScript
```javascript
import OpenAI from 'openai';

const client = new OpenAI({
  baseURL: 'https://api.serika.dev/api/openai/v1',
  apiKey: 'your_api_key',
});

async function main() {
  const chatCompletion = await client.chat.completions.create({
    messages: [{ role: 'user', content: 'What is the capital of France?' }],
    model: 'openai/gpt-4o-mini',
  });

  console.log(chatCompletion.choices[0].message.content);
}

main();
```
````
```` {group-tab} cURL
```bash
curl https://api.serika.dev/api/openai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your_api_key" \
  -d '{
    "model": "openai/gpt-4o-mini",
    "messages": [{"role": "user", "content": "What is the capital of France?"}]
  }'
```
````
`````

## Next Steps

- Explore [Chat Completions](api/chat-completions.md) to build conversational apps.
- Check out [Image Generation](api/image-generation.md) to create art.
- See the [Examples](examples.md) page for more code snippets.