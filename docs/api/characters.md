# Characters

Serika.dev allows you to interact with specific AI Characters. Each character has a unique personality and system prompt.

## Using Characters in Chat

To use a character, you simply need its `character_id`. You can pass this ID when making a Chat Completion request.

### Finding Character IDs

You can find the `character_id` in the URL of the character on the Serika.dev website, or via the API if you have a list endpoint (not covered here).

### Example Request

When using the OpenAI Python library, pass the `character_id` in the `extra_body` argument.

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.serika.dev/api/openai/v1",
    api_key="your_api_key"
)

response = client.chat.completions.create(
    model="sao10k/l3.3-euryale-70b",
    messages=[
        {"role": "user", "content": "Hello, who are you?"}
    ],
    extra_body={
        "character_id": "12345-abcde" 
    }
)

print(response.choices[0].message.content)
```

The API will automatically inject the character's system prompt and personality into the context.