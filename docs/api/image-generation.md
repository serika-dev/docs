# Image Generation

Serika.dev offers two endpoints for generating images from text prompts:

1. `/images/generations` - The primary endpoint (OpenAI-compatible)
2. `/generate/image` - Legacy endpoint

This documentation covers both endpoints.

## Primary Endpoint: Images Generations

```
POST /images/generations
```

### Request Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `prompt` | string | Yes | The text description of the image to generate. |
| `model` | string | No | The model to use for generation. Defaults to `novelai/nai-diffusion-3`. |
| `n` | integer | No | The number of images to generate. Defaults to 1. Maximum is 10. |
| `size` | string | No | The size of the generated images. Defaults to `1024x1024`. |
| `response_format` | string | No | The format in which the generated images are returned. Only `url` is supported currently. |
| `negative_prompt` | string | No | Text prompt of things to avoid in the generated image. |
| `seed` | integer | No | Random seed for image generation. Same seed with same prompt will generate similar images. |
| `steps` | integer | No | Number of diffusion steps to perform. Higher values can produce better quality but take longer. |
| `sampler` | string | No | Sampling method to use for generation (e.g., `k_dpmpp_2s_ancestral`). |
| `style` | string | No | The artistic style to apply to the generated image. |

### Example Request

```bash
curl -X POST https://api.serika.dev/api/openai/v1/images/generations \
  -H "Authorization: sk-your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "A majestic mountain landscape at sunset with a lake in the foreground",
    "model": "novelai/nai-diffusion-3",
    "n": 1,
    "size": "1024x1024"
  }'
```

### Advanced Example

```bash
curl -X POST https://api.serika.dev/api/openai/v1/images/generations \
  -H "Authorization: sk-your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "A cyberpunk cityscape with neon lights and flying cars",
    "model": "novelai/nai-diffusion-3",
    "n": 1,
    "size": "1024x1024",
    "negative_prompt": "blurry, bad quality, disfigured, low resolution",
    "steps": 28,
    "sampler": "k_dpmpp_2s_ancestral",
    "seed": 42069
  }'
```

### Response Format

```json
{
  "created": 1677858242,
  "data": [
    {
      "url": "https://api.serika.dev/api/cdn/images/8c7d5a8e1ebf3c2a5b6f4d7c9a8b7c6d_1677858242.png",
      "revised_prompt": "A majestic mountain landscape at sunset with a lake in the foreground"
    }
  ]
}
```

### Generating Multiple Images

To generate multiple images with the same prompt, use the `n` parameter:

```bash
curl -X POST https://api.serika.dev/api/openai/v1/images/generations \
  -H "Authorization: sk-your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "A cyberpunk cityscape with neon lights and flying cars",
    "n": 3
  }'
```

Response:

```json
{
  "created": 1677858242,
  "data": [
    {
      "url": "https://api.serika.dev/api/cdn/images/1a2b3c4d5e6f7g8h9i0j_1677858242.png",
      "revised_prompt": "A cyberpunk cityscape with neon lights and flying cars"
    },
    {
      "url": "https://api.serika.dev/api/cdn/images/2b3c4d5e6f7g8h9i0j1a_1677858242.png",
      "revised_prompt": "A cyberpunk cityscape with neon lights and flying cars"
    },
    {
      "url": "https://api.serika.dev/api/cdn/images/3c4d5e6f7g8h9i0j1a2b_1677858242.png",
      "revised_prompt": "A cyberpunk cityscape with neon lights and flying cars"
    }
  ]
}
```

## Legacy Endpoint: Generate Image

```
POST /generate/image
```

### Request Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `prompt` | string | Yes | The text description of the image to generate. |
| `model` | string | No | The model to use for generation. Defaults to `novelai/nai-diffusion-3`. |
| `parameters` | object | No | Additional model-specific parameters for image generation. |

The `parameters` object can include:

| Parameter | Type | Description |
|-----------|------|-------------|
| `size` | string | The size of the generated image (e.g., `1024x1024`). |
| `negative_prompt` | string | Text prompt of things to avoid in the generated image. |
| `seed` | integer | Random seed for image generation. |
| `steps` | integer | Number of diffusion steps to perform. |
| `sampler` | string | Sampling method to use for generation. |
| `style` | string | The artistic style to apply to the generated image. |

### Example Request

```bash
curl -X POST https://api.serika.dev/api/openai/v1/generate/image \
  -H "Authorization: sk-your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "A futuristic space station orbiting Earth",
    "model": "novelai/nai-diffusion-3",
    "parameters": {
      "size": "1024x1024",
      "negative_prompt": "blurry, pixelated, low resolution",
      "steps": 28,
      "seed": 12345
    }
  }'
```

### Response Format

```json
{
  "url": "https://api.serika.dev/api/cdn/images/4d5e6f7g8h9i0j1a2b3c_1677858242.png",
  "revised_prompt": "A futuristic space station orbiting Earth",
  "model": "novelai/nai-diffusion-3",
  "size": "1024x1024"
}
```

## Available Models

The following models are available for image generation:

| Model ID | Name | Description | Tier | Generation Limit |
|----------|------|-------------|------|-----------------|
| `novelai/nai-diffusion-3` | NAI Diffusion 3 | NovelAI's latest image generation model | Free | 20/month |
| `novelai/nai-diffusion` | NAI Diffusion | NovelAI's stable diffusion model | Free | 20/month |
| `nai-diffusion-4-curated-preview` | NAI Diffusion 4 | NovelAI's latest image generation model | Premium | Unlimited (paid) |

Free users are limited to 20 image generations per month, while premium users with billing setup can generate unlimited images (billed per image).

## Image Sizes

The following image sizes are supported:

- `256x256`
- `512x512`
- `1024x1024` (default)

## Advanced Parameters

### Negative Prompts

Negative prompts help the model avoid certain elements in the generated image. For example:

```json
"negative_prompt": "blurry, bad quality, disfigured, low resolution, ugly, pixelated"
```

### Seeds

Using the same seed value with the same prompt will produce similar images. This is useful for:

- Creating variations of a specific image
- Reproducing previous generations
- A/B testing different prompts with the same base composition

If no seed is provided, a random seed will be used.

### Sampling Methods

Different samplers can produce different visual results:

- `k_dpmpp_2s_ancestral` - Good for detailed images
- Other samplers may be available depending on the model

### Steps

The number of diffusion steps affects the quality of the generated image:

- Lower values (20-30) are faster but may produce less detailed images
- Higher values (30-50) are slower but may produce more detailed images

## Error Responses

### Missing Prompt

```json
{
  "error": {
    "message": "prompt is required",
    "type": "invalid_request_error",
    "param": "prompt"
  }
}
```

### Invalid Number of Images

```json
{
  "error": {
    "message": "n must be between 1 and 10",
    "type": "invalid_request_error",
    "param": "n"
  }
}
```

### Generation Failure

```json
{
  "error": {
    "message": "Failed to generate any images",
    "details": ["Error processing image request"],
    "type": "generation_error"
  }
}
```

## Prompt Guidelines

For best results with image generation:

1. Be specific and descriptive in your prompts
2. Include details like style, lighting, atmosphere, and perspective
3. Avoid prompts that may violate content policies
4. Keep prompts to a reasonable length (under 500 characters is recommended)
5. Use negative prompts to improve image quality by excluding unwanted elements

## Usage and Billing

Image generation usage is billed differently than text generation. Each image generation is counted as approximately 1000 tokens, regardless of the size of the prompt.

This means that generating 1 image is equivalent to about 1000 tokens of text generation for billing purposes.

See the [Billing](../guides/billing.md) page for more information about usage costs. 