# Examples Cookbook

This page provides practical examples for using the Serika.dev API with the official OpenAI client libraries.

## Prerequisites

Ensure you have the OpenAI library installed:

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

## Chat Completions

### Basic Chat

<div class="tabbed-set" data-tabs="2:3">
<input checked="checked" id="__tabbed_2_1" name="__tabbed_2" type="radio">
<label for="__tabbed_2_1">Python</label>
<div class="tabbed-content">
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
</div>
<input id="__tabbed_2_2" name="__tabbed_2" type="radio">
<label for="__tabbed_2_2">JavaScript</label>
<div class="tabbed-content">
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
</div>
<input id="__tabbed_2_3" name="__tabbed_2" type="radio">
<label for="__tabbed_2_3">cURL</label>
<div class="tabbed-content">
```bash
curl https://api.serika.dev/api/openai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your_api_key" \
  -d '{
    "model": "openai/gpt-4o-mini",
    "messages": [{"role": "user", "content": "What is the capital of France?"}]
  }'
```
</div>
</div>

### Streaming Responses

<div class="tabbed-set" data-tabs="3:3">
<input checked="checked" id="__tabbed_3_1" name="__tabbed_3" type="radio">
<label for="__tabbed_3_1">Python</label>
<div class="tabbed-content">
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
</div>
<input id="__tabbed_3_2" name="__tabbed_3" type="radio">
<label for="__tabbed_3_2">JavaScript</label>
<div class="tabbed-content">
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
</div>
<input id="__tabbed_3_3" name="__tabbed_3" type="radio">
<label for="__tabbed_3_3">cURL</label>
<div class="tabbed-content">
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
</div>
</div>

## Image Generation

### Generate an Image

<div class="tabbed-set" data-tabs="4:3">
<input checked="checked" id="__tabbed_4_1" name="__tabbed_4" type="radio">
<label for="__tabbed_4_1">Python</label>
<div class="tabbed-content">
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
</div>
<input id="__tabbed_4_2" name="__tabbed_4" type="radio">
<label for="__tabbed_4_2">JavaScript</label>
<div class="tabbed-content">
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
</div>
<input id="__tabbed_4_3" name="__tabbed_4" type="radio">
<label for="__tabbed_4_3">cURL</label>
<div class="tabbed-content">
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
</div>
</div>

## Advanced Usage

### Using a Specific Character

You can influence the AI's personality by passing a `character_id` in the `extra_body` parameter (Python) or directly in the options (Node.js, if typed loosely, otherwise via custom request).

<div class="tabbed-set" data-tabs="5:2">
<input checked="checked" id="__tabbed_5_1" name="__tabbed_5" type="radio">
<label for="__tabbed_5_1">Python</label>
<div class="tabbed-content">
```python
response = client.chat.completions.create(
    model="sao10k/l3.3-euryale-70b",
    messages=[{"role": "user", "content": "Hello there!"}],
    extra_body={
        "character_id": "your_character_id_here"
    }
)
```
</div>
<input id="__tabbed_5_2" name="__tabbed_5" type="radio">
<label for="__tabbed_5_2">JavaScript</label>
<div class="tabbed-content">
```javascript
const response = await client.chat.completions.create({
  model: 'sao10k/l3.3-euryale-70b',
  messages: [{ role: 'user', content: 'Hello there!' }],
  character_id: 'your_character_id_here' // Note: Typescript might complain, cast to any if needed
});
```
</div>
</div>