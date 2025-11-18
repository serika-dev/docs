# Image Generation

Serika.dev provides a powerful Image Generation API compatible with the OpenAI standard. You can generate high-quality images using various models, including NovelAI and TensorArt.

## Endpoint

`POST https://api.serika.dev/api/openai/v1/images/generations`

> [!NOTE]
> For heavy models (like TensorArt), consider using the [Jobs API](jobs.md) to avoid timeouts.

## Quick Start

````` {tabs}
```` {group-tab} Python
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
```` {group-tab} JavaScript
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
```` {group-tab} cURL
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

## Available Models

### Premium Tier Models (All models require billing)

| Model ID | Name | Description | Provider |
|----------|------|-------------|----------|
| `novelai/nai-diffusion-4-full` | NAI Diffusion 4 | NovelAI's latest image generation model | NovelAI |
| `novelai/nai-diffusion-3` | NAI Diffusion 3 | NovelAI's previous generation model | NovelAI |
| `novelai/nai-diffusion-2` | NAI Diffusion 2 | NovelAI's stable diffusion model | NovelAI |
| `gpt-image-1-low` | GPT Image 1 (Low) | OpenAI's GPT Image 1 model - Low quality setting | OpenAI |

### Premium Tier Models (Requires Billing Setup)

| Model ID | Name | Description | Provider |
|----------|------|-------------|----------|
| `novelai/nai-diffusion-4-5-full` | NAI Diffusion 4.5 Full | NovelAI's latest full image generation model | NovelAI |
| `novelai/nai-diffusion-4-5-curated` | NAI Diffusion 4.5 Curated | NovelAI's latest curated image generation model | NovelAI |
| `gpt-image-1-medium` | GPT Image 1 (Medium) | OpenAI's GPT Image 1 model - Medium quality setting | OpenAI |
| `gpt-image-1-high` | GPT Image 1 (High) | OpenAI's GPT Image 1 model - High quality setting | OpenAI |

### TensorArt Models (Premium)

> [!IMPORTANT]
> TensorArt models are best used with the [Jobs API](jobs.md) due to longer generation times.

| Model ID | Name | Description | Provider |
|----------|------|-------------|----------|
| `tensorart-illustrious-xl-v2-aesthetic` | Illustrious XL v2.0 | High-quality TensorArt model | TensorArt |
| `tensorart-rizmix-noob-illustrious-pastel` | rizMix Noob Illustrious | High-quality TensorArt model | TensorArt |
| `tensorart-toxic-echo-il` | ToxicEchoIL | High-quality TensorArt model | TensorArt |
| `tensorart-animagine-xl` | AnimagineXL | High-quality TensorArt model | TensorArt |
| `tensorart-one-obsession` | One Obsession | High-quality TensorArt model | TensorArt |
| `tensorart-nova-orange-xl` | Nova Orange XL | High-quality TensorArt model | TensorArt |
| `tensorart-wai-illustrious-v11` | WAI-illustrious v11 | High-quality TensorArt model | TensorArt |
| `tensorart-wai-illustrious-v14` | WAI-illustrious v14 | High-quality TensorArt model | TensorArt |
| `tensorart-wai-illustrious-v15` | WAI-illustrious v15 | High-quality TensorArt model | TensorArt |
| `tensorart-illustrious-multistyle-variation-ar` | Illustrious MultiStyle | High-quality TensorArt model | TensorArt |

## Advanced Parameters

You can pass additional parameters to fine-tune your generation. In the OpenAI Python client, these can often be passed as extra arguments or via `extra_body`.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `width` | integer | 1024 | Width of the image. |
| `height` | integer | 1024 | Height of the image. |
| `steps` | integer | 23 | Number of diffusion steps. |
| `scale` | number | 10 | Guidance scale (CFG). |
| `sampler` | string | k_euler_ancestral | Sampling method. |
| `seed` | integer | random | Random seed. |
| `negative_prompt` | string | - | Things to exclude from the image. |