# Best Practices

To get the most out of the Serika.dev API, follow these best practices.

## 1. Handle Errors Gracefully

Always wrap your API calls in try-catch blocks to handle potential errors like rate limits or timeouts.

```python
from openai import APIError

try:
    response = client.chat.completions.create(...)
except APIError as e:
    print(f"OpenAI API returned an API Error: {e}")
```

## 2. Use Streaming for Long Responses

For chat applications, streaming provides a much better user experience by showing the response as it's being generated.

## 3. Manage Context Window

Be mindful of the token limit. If a conversation gets too long, you may need to summarize previous messages or remove older ones to fit within the model's context window.

## 4. Secure Your API Keys

Never expose your API keys in client-side code (browsers, mobile apps). Always route requests through your own backend server.

## 5. Use the Jobs API for Heavy Tasks

For complex image generation tasks, especially with TensorArt models, use the [Jobs API](api/jobs.md). This prevents HTTP timeouts and ensures reliable delivery of results.