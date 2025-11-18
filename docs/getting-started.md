# Getting Started

Welcome to the Serika.dev API! This guide will help you make your first API request in minutes.

## 1. Get Your API Key

First, you need an API key.
1. Log in to your [Serika.dev Developer Dashboard](https://developers.serika.dev).
2. Navigate to the **API Keys** section.
3. Click **Create New Key** and copy it.

## 2. Install the OpenAI Library

Serika.dev is compatible with the standard OpenAI client libraries, making integration effortless.

<div class="tabbed-set" data-tabs="1:2">
<input checked="checked" id="__tabbed_1_1" name="__tabbed_1" type="radio">
<label for="__tabbed_1_1">Python</label>
<div class="tabbed-content">
```bash
pip install openai
```
</div>
<input id="__tabbed_1_2" name="__tabbed_1" type="radio">
<label for="__tabbed_1_2">Node.js</label>
<div class="tabbed-content">
```bash
npm install openai
```
</div>
</div>

## 3. Make Your First Request

Create a file named `test_api.py` (or `test_api.js`) and add the following code.

<div class="tabbed-set" data-tabs="2:3">
<input checked="checked" id="__tabbed_2_1" name="__tabbed_2" type="radio">
<label for="__tabbed_2_1">Python</label>
<div class="tabbed-content">
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
</div>
<input id="__tabbed_2_2" name="__tabbed_2" type="radio">
<label for="__tabbed_2_2">JavaScript</label>
<div class="tabbed-content">
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
</div>
<input id="__tabbed_2_3" name="__tabbed_2" type="radio">
<label for="__tabbed_2_3">cURL</label>
<div class="tabbed-content">
```bash
curl https://api.serika.dev/api/openai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY_HERE" \
  -d '{
    "model": "openai/gpt-4o-mini",
    "messages": [{"role": "user", "content": "Hello, world!"}]
  }'
```
</div>
</div>

## Next Steps

- Explore [Chat Completions](api/chat-completions.md) to build conversational apps.
- Check out [Image Generation](api/image-generation.md) to create art.
- See the [Examples](examples.md) page for more code snippets.