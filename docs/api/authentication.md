# Authentication

Serika.dev uses API keys to authenticate requests. You can view and manage your API keys in the [Developer Dashboard](https://developers.serika.dev).

## Using Your API Key

Your API key should be included in the `Authorization` header of your HTTP requests.

````` {tab-set}
```` {tab-item} Python (Install)
```bash
pip install openai
```
````
```` {tab-item} Node.js (Install)
```bash
npm install openai
```
````
```` {tab-item} Python
```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.serika.dev/api/openai/v1",
    api_key="sk-your-api-key"
)
```
````
```` {tab-item} JavaScript
```javascript
import OpenAI from 'openai';

const client = new OpenAI({
  baseURL: 'https://api.serika.dev/api/openai/v1',
  apiKey: 'sk-your-api-key',
});
```
```
```{tab-item} cURL
```bash
curl https://api.serika.dev/api/openai/v1/models \
  -H "Authorization: Bearer sk-your-api-key"
```
```
```

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