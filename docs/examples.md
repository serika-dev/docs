# Examples Cookbook

This page provides practical examples for using the Serika.dev API with the official OpenAI client libraries.

## Prerequisites

Ensure you have the OpenAI library installed:

````` {tab-set}
```` {tab-item} Python
```bash
pip install openai
```
````
```` {tab-item} Node.js
```bash
npm install openai
```
````
`````

## Chat Completions

### Basic Chat

````` {tab-set}
```` {tab-item} Python
```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.serika.dev/api/openai/v1",
    api_key="your_api_key"
)

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
```` {tab-item} JavaScript
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
```` {tab-item} cURL
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

### Streaming Responses

````` {tab-set}
```` {tab-item} Python
```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.serika.dev/api/openai/v1",
    api_key="your_api_key"
)

stream = client.chat.completions.create(
    model="openai/gpt-4o-mini",
    messages=[{"role": "user", "content": "Tell me a story about a dragon."}],
    stream=True,
)

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
```
````
```` {tab-item} JavaScript
```javascript
import OpenAI from 'openai';

const client = new OpenAI({
  baseURL: 'https://api.serika.dev/api/openai/v1',
  apiKey: 'your_api_key',
});

async function main() {
  const stream = await client.chat.completions.create({
    model: 'openai/gpt-4o-mini',
    messages: [{ role: 'user', content: 'Tell me a story about a dragon.' }],
    stream: true,
  });

  for await (const chunk of stream) {
    process.stdout.write(chunk.choices[0]?.delta?.content || '');
  }
}

main();
```
````
```` {tab-item} cURL
```bash
curl https://api.serika.dev/api/openai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your_api_key" \
  -d '{
    "model": "openai/gpt-4o-mini",
    "messages": [{"role": "user", "content": "Tell me a story about a dragon."}],
    "stream": true
  }'
```
````
`````

## Image Generation

### Generate an Image

````` {tab-set}
```` {tab-item} Python
```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.serika.dev/api/openai/v1",
    api_key="your_api_key"
)

response = client.images.generate(
    model="novelai/nai-diffusion-3",
    prompt="A cute anime girl with pink hair, high quality",
    size="1024x1024",
    quality="standard",
    n=1,
)

image_url = response.data[0].url
print(f"Image URL: {image_url}")
```
````
```` {tab-item} JavaScript
```javascript
import OpenAI from 'openai';

const client = new OpenAI({
  baseURL: 'https://api.serika.dev/api/openai/v1',
  apiKey: 'your_api_key',
});

async function main() {
  const response = await client.images.generate({
    model: "novelai/nai-diffusion-3",
    prompt: "A cute anime girl with pink hair, high quality",
    n: 1,
    size: "1024x1024",
  });

  console.log(response.data[0].url);
}

main();
```
````
```` {tab-item} cURL
```bash
curl https://api.serika.dev/api/openai/v1/images/generations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your_api_key" \
  -d '{
    "model": "novelai/nai-diffusion-3",
    "prompt": "A cute anime girl with pink hair, high quality",
    "size": "1024x1024",
    "n": 1
  }'
```
````
`````

## Advanced Usage

### Using a Specific Character

You can influence the AI's personality by passing a `character_id` in the `extra_body` parameter (Python) or directly in the options (Node.js, if typed loosely, otherwise via custom request).

````` {tab-set}
```` {tab-item} Python
```python
response = client.chat.completions.create(
    model="sao10k/l3.3-euryale-70b",
    messages=[{"role": "user", "content": "Hello there!"}],
    extra_body={
        "character_id": "your_character_id_here"
    }
)
```
````
```` {tab-item} JavaScript
```javascript
const response = await client.chat.completions.create({
  model: 'sao10k/l3.3-euryale-70b',
  messages: [{ role: 'user', content: 'Hello there!' }],
  character_id: 'your_character_id_here' // Note: Typescript might complain, cast to any if needed
});
```
````
`````