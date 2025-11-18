# Authentication

Serika.dev uses API keys to authenticate requests. You can view and manage your API keys in the [Developer Dashboard](https://developers.serika.dev).

## Using Your API Key

Your API key should be included in the `Authorization` header of your HTTP requests.

<div class="tabbed-set" data-tabs="1:3">
<input checked="checked" id="__tabbed_1_1" name="__tabbed_1" type="radio">
<label for="__tabbed_1_1">Python</label>
<div class="tabbed-content">
```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.serika.dev/api/openai/v1",
    api_key="sk-your-api-key"
)
```
</div>
<input id="__tabbed_1_2" name="__tabbed_1" type="radio">
<label for="__tabbed_1_2">JavaScript</label>
<div class="tabbed-content">
```javascript
import OpenAI from 'openai';

const client = new OpenAI({
  baseURL: 'https://api.serika.dev/api/openai/v1',
  apiKey: 'sk-your-api-key',
});
```
</div>
<input id="__tabbed_1_3" name="__tabbed_1" type="radio">
<label for="__tabbed_1_3">cURL</label>
<div class="tabbed-content">
```bash
curl https://api.serika.dev/api/openai/v1/models \
  -H "Authorization: Bearer sk-your-api-key"
```
</div>
</div>

## Security Best Practices

- **Do not share your API keys.** Treat them like passwords.
- **Do not commit API keys to version control.** Use environment variables instead.
- **Rotate your keys** if you suspect they have been compromised.

### Using Environment Variables

It is recommended to store your API key in an environment variable (e.g., `SERIKA_API_KEY`) and read it in your code.

```python
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.serika.dev/api/openai/v1",
    api_key=os.environ.get("SERIKA_API_KEY")
)
```