# Chat Completions

The Chat Completions endpoint is the core of the Serika.dev API, allowing you to generate conversational responses using state-of-the-art AI models. It is fully compatible with the OpenAI API standard.

## Endpoint

`POST https://api.serika.dev/api/openai/v1/chat/completions`

## Quick Start

The easiest way to use the API is with the official OpenAI client libraries.

<div class="tabbed-set" data-tabs="1:3">
<input checked="checked" id="__tabbed_1_1" name="__tabbed_1" type="radio">
<label for="__tabbed_1_1">Python</label>
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
        {"role": "user", "content": "Hello!"}
    ]
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
  apiKey: 'your_api_key',
});

async function main() {
  const completion = await client.chat.completions.create({
    messages: [{ role: 'user', content: 'Hello!' }],
    model: 'openai/gpt-4o-mini',
  });

  console.log(completion.choices[0].message.content);
}

main();
```
</div>
<input id="__tabbed_1_3" name="__tabbed_1" type="radio">
<label for="__tabbed_1_3">cURL</label>
<div class="tabbed-content">
```bash
curl https://api.serika.dev/api/openai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your_api_key" \
  -d '{
    "model": "openai/gpt-4o-mini",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```
</div>
</div>

## Request Parameters

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `messages` | array | Yes | A list of messages comprising the conversation so far. |
| `model` | string | Yes | The ID of the model to use. |
| `stream` | boolean | No | If set, partial message deltas will be sent. |
| `temperature` | number | No | Sampling temperature (0 to 2). Higher values like 0.8 are more random. |
| `max_tokens` | integer | No | The maximum number of tokens to generate. |
| `character_id` | string | No | **(Serika Specific)** ID of a character to adopt a persona. |

## Available Models

### Premium Tier Models (All models require billing)

| Model ID | Name | Description | Provider |
|----------|------|-------------|----------|
| `openai/gpt-4o-mini` | GPT-4o Mini | Reliable general purpose model | OpenRouter |
| `openai/gpt-4o` | GPT-4o | Reliable general purpose model | OpenRouter |
| `anthropic/claude-3-haiku` | Claude 3 Haiku | Fast and efficient Claude model | OpenRouter |
| `google/gemini-2.0-flash-lite-001` | Gemini 2.0 Flash | Google's latest general purpose model | OpenRouter |
| `deepseek/deepseek-r1` | DeepSeek-R1 | Reliable Reasoning model | OpenRouter |
| `openai/gpt-5-mini` | GPT-5 Mini | Compact version of GPT-5 | OpenRouter |
| `openai/gpt-5-nano` | GPT-5 Nano | Ultra-efficient GPT-5 variant | OpenRouter |
| `openai/gpt-5-chat` | GPT-5 Chat | GPT-5 optimized for conversations | OpenRouter |
| `openai/gpt-5` | GPT-5 | OpenAI's most advanced model | OpenRouter |
| `grok-3` | Grok 3 | Azure deployment of Grok-3 conversational model | Azure |
| `gpt-4.1` | GPT-4.1 | Azure deployment of GPT-4.1 | Azure |
| `gpt-5-chat` | GPT-5 Chat | Azure deployment of GPT-5 Chat | Azure |
| `Llama-4-Scout-17B-16E-Instruct` | Llama 4 Scout | Azure deployment of Llama-4 Scout Instruct variant | Azure |
| `gpt-oss-120b` | GPT-OSS 120B | Azure deployment of GPT-OSS 120B open-source style model | Azure |
| `gpt-5-nano` | GPT-5 Nano | Azure deployment of GPT-5 Nano | Azure |
| `gpt-5-mini` | GPT-5 Mini | Azure deployment of GPT-5 Mini | Azure |
| `openai/gpt-5.1` | GPT-5.1 | OpenAI's GPT-5.1 model | OpenRouter |
| `openai/gpt-5.1-chat` | GPT-5.1 Chat | OpenAI's GPT-5.1 Chat model | OpenRouter |
| `moonshotai/kimi-linear-48b-a3b-instruct` | Kimi Linear 48B | MoonshotAI's Kimi Linear 48B model | OpenRouter |
| `openai/gpt-5.1-codex` | GPT-5.1 Codex | OpenAI's GPT-5.1 Codex model | OpenRouter |
| `openai/gpt-5.1-codex-mini` | GPT-5.1 Codex Mini | OpenAI's GPT-5.1 Codex Mini model | OpenRouter |
| `kwaipilot/kat-coder-pro:free` | Kat Coder Pro | KwaiPilot's Kat Coder Pro model | OpenRouter |
| `moonshotai/kimi-k2-thinking` | Kimi K2 Thinking | MoonshotAI's Kimi K2 Thinking model | OpenRouter |
| `sao10k/l3.3-euryale-70b` | Euryale 70B | Primary model for free users - high quality roleplay model | OpenRouter |
| `sao10k/l3-lunaris-8b` | Lunaris 8B | High quality roleplay model for free users | OpenRouter |
| `inception/mercury` | Mercury | High quality general purpose model | OpenRouter |
| `cognitivecomputations/dolphin-mistral-24b-venice-edition:free` | Dolphin Mistral 24B | Primary model for free users - high quality roleplay model | OpenRouter |
| `x-ai/grok-3-mini` | Grok 3 Mini | Primary model for free users - high quality roleplay model | OpenRouter |
| `nousresearch/deephermes-3-mistral-24b-preview:free` | DeepHermes | Primary model for free users - high quality roleplay model | OpenRouter |
| `meta-llama/llama-3.2-11b-vision-instruct:free` | Llama 3.2 11B | Backup model for free users - high quality general purpose model | OpenRouter |
| `qwen/qwen-2.5-72b-instruct:free` | Qwen 2.5 72B | Backup model for free users - high quality general purpose model | OpenRouter |
| `google/gemma-2-27b-it:free` | Gemma 2 27B | Backup model for free users - high quality general purpose model | OpenRouter |
| `mistralai/mistral-nemo` | Mistral Nemo | General purpose model | OpenRouter |
| `cognitivecomputations/dolphin3.0-mistral-24b:free` | Dolphin 24B | General purpose model for free users | OpenRouter |
| `thedrummer/unslopnemo-12b` | UnslopNemo 12B | High quality unslop model for free users | OpenRouter |
| `thedrummer/cydonia-24b-v4.1` | Cydonia 24B | Creative model for free users - high quality roleplay model | OpenRouter |
| `thedrummer/rocinante-12b` | Rocinante 12B | Creative model for free users - high quality roleplay model | OpenRouter |
| `shisa-ai/shisa-v2-llama3.3-70b:free` | Shisa v2 Llama 3.3 70B | Japanese model for free users - high quality roleplay model | OpenRouter |
| `mistralai/mistral-saba` | Mistral Saba | General Asian model for free users - high quality roleplay model | OpenRouter |
| `z-ai/glm-4.6` | GLM 4.6 | High quality general purpose model | OpenRouter |

### Premium Tier Models (Requires Billing Setup)

| Model ID | Name | Description | Provider |
|----------|------|-------------|----------|
| `google/gemini-3-pro-preview` | Gemini 3 Pro Preview | Google's latest Gemini 3 Pro Preview model | OpenRouter |
| `anthropic/claude-3.5-sonnet` | Claude 3.5 Sonnet | Fast and cost-effective Claude model | OpenRouter |
| `thedrummer/anubis-70b-v1.1` | Anubis 70B | Roleplay model for premium users - high quality roleplay model | OpenRouter |
| `thedrummer/valkyrie-49b-v1` | Valkyrie 49B | Premium roleplay model - high quality creative model | OpenRouter |
| `sao10k/l3.1-70b-hanami-x1` | Hanami X1 | Roleplay model for premium users - high quality roleplay model | OpenRouter |
| `x-ai/grok-4` | Grok 4 | Primary model for premium users - high quality roleplay model | OpenRouter |
| `x-ai/grok-3` | Grok 3 | Primary model for premium users - high quality roleplay model | OpenRouter |
| `qwen/qwen3-32b` | Qwen3 32B | Roleplay model for premium users - high quality roleplay model | OpenRouter |
| `gryphe/mythomax-l2-13b` | Mythomax 13B | Roleplay model for premium users - high quality roleplay model | OpenRouter |
| `arcee-ai/arcee-blitz` | Arcee Blitz | High quality general purpose model | OpenRouter |
| `thedrummer/anubis-pro-105b-v1` | Anubis Pro 105B | High quality Creative model | OpenRouter |
| `thedrummer/skyfall-36b-v2` | Skyfall 36B | High quality Creative model | OpenRouter |
| `anthropic/claude-3.5-haiku` | Claude Haiku 3.5 | High quality general purpose model | OpenRouter |
| `anthropic/claude-haiku-4.5` | Claude Haiku 4.5 | High quality general purpose model | OpenRouter |
| `meta-llama/llama-4-scout` | Llama 4 Scout | High quality general purpose model | OpenRouter |
| `meta-llama/llama-4-maverick` | Llama 4 Maverick | High quality general purpose model | OpenRouter |

## Advanced Features

### Using Characters

To use a specific character persona, include the `character_id` in your request.

```python
response = client.chat.completions.create(
    model="sao10k/l3.3-euryale-70b",
    messages=[{"role": "user", "content": "Hello!"}],
    extra_body={"character_id": "12345"}
)
```

### Streaming

Streaming allows you to receive the response token by token, which is useful for real-time applications.

```python
stream = client.chat.completions.create(
    model="openai/gpt-4o-mini",
    messages=[{"role": "user", "content": "Write a long story."}],
    stream=True
)

for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="")
```