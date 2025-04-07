# Getting Started

This guide will help you get up and running with the Serika.dev Customer API.

## Prerequisites

Before you begin, you'll need:

- A Serika.dev account
- An API key (see [API Keys](guides/api-keys.md))
- Basic knowledge of REST APIs

## Step 1: Create an API Key

1. Log in to your Serika.dev account
2. Navigate to the Developer section
3. Click "Create API Key" and follow the prompts
4. Store your key securely - it won't be shown again!

## Step 2: Make Your First API Request

Here's a simple example of generating text with the API:

```bash
curl -X POST https://api.serika.dev/v1/chat/completions \
  -H "Authorization: Bearer sk-your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {"role": "user", "content": "Tell me a joke about programming"}
    ],
    "model": "gpt-3.5-turbo"
  }'
```

## Step 3: Explore the API

Explore the different endpoints available:

- [Chat Completions](api/chat-completions.md) - Generate conversational responses
- [Text Generation](api/text-generation.md) - Legacy endpoint for text generation
- [Image Generation](api/image-generation.md) - Create images from text prompts
- [Characters](api/characters.md) - Access Serika's character database

## Step 4: Handle Responses

All API responses are in JSON format. Here's an example of handling a response:

```javascript
// Example: Handling a response in JavaScript
fetch('https://api.serika.dev/v1/chat/completions', {
  method: 'POST',
  headers: {
    'Authorization': 'Bearer sk-your-api-key',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    messages: [
      {role: 'user', content: 'Hello, how are you?'}
    ],
    model: 'gpt-3.5-turbo'
  })
})
.then(response => response.json())
.then(data => {
  // The AI's response is in data.choices[0].message.content
  console.log(data.choices[0].message.content);
})
.catch(error => console.error('Error:', error));
```

## Step 5: Monitor Usage

Keep track of your API usage to manage costs:

1. Navigate to the Developer section of your Serika.dev account
2. View the "API Usage" section for detailed metrics
3. Set up usage alerts if needed

## Next Steps

- Check out the [API Reference](api/overview.md) for detailed endpoint documentation
- Learn about [Billing](guides/billing.md) and how usage is calculated
- Explore [Examples](examples.md) for common use cases 