# Jobs API

The Jobs API is designed for asynchronous processing of long-running tasks, such as high-quality image generation with complex models (e.g., TensorArt models). This allows you to submit a request and check back later for the result, avoiding timeouts.

## Workflow

1.  **Submit a Job**: Send a POST request to create a new job.
2.  **Receive Job ID**: The API returns a unique Job ID.
3.  **Poll Status**: Periodically check the status of the job using the Job ID.
4.  **Get Result**: Once the job status is `COMPLETED`, retrieve the final result.

---

## Create Image Job

Submit a new image generation job. This is required for models that are marked as `jobs` only in the model list.

**Endpoint:** `POST /jobs/images`

### Request Parameters

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `model` | string | Yes | The ID of the model to use (e.g., `tensorart-illustrious-xl-v2-aesthetic`). |
| `prompt` | string | Yes | The text description of the image to generate. |
| `negative_prompt` | string | No | Text to exclude from the image. |
| `width` | integer | No | Image width (default: 1024). |
| `height` | integer | No | Image height (default: 1024). |
| `steps` | integer | No | Number of diffusion steps. |
| `cfg_scale` | number | No | Guidance scale. |
| `sampler` | string | No | Sampling method. |
| `seed` | integer | No | Random seed. |

### Example Request

```{tab-set}
```{tab-item} Python
```python
import requests
import time

API_KEY = "your_api_key"
BASE_URL = "https://api.serika.dev/api/openai/v1"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "model": "tensorart-illustrious-xl-v2-aesthetic",
    "prompt": "A futuristic city with neon lights, cyberpunk style",
    "width": 1024,
    "height": 1024
}

# 1. Submit Job
response = requests.post(f"{BASE_URL}/jobs/images", headers=headers, json=data)
job_data = response.json()
job_id = job_data['id']
print(f"Job submitted. ID: {job_id}")

# 2. Poll for Status
while True:
    status_response = requests.get(f"{BASE_URL}/jobs/{job_id}", headers=headers)
    status_data = status_response.json()
    status = status_data['status']
    
    print(f"Status: {status}")
    
    if status == 'COMPLETED':
        print("Job finished!")
        print("Result URL:", status_data['result']['url'])
        break
    elif status == 'FAILED':
        print("Job failed:", status_data.get('error'))
        break
        
    time.sleep(2) # Wait 2 seconds before checking again
```
```
```{tab-item} JavaScript
```javascript
const axios = require('axios');

const API_KEY = "your_api_key";
const BASE_URL = "https://api.serika.dev/api/openai/v1";

const headers = {
    "Authorization": `Bearer ${API_KEY}`,
    "Content-Type": "application/json"
};

const data = {
    "model": "tensorart-illustrious-xl-v2-aesthetic",
    "prompt": "A futuristic city with neon lights, cyberpunk style",
    "width": 1024,
    "height": 1024
};

async function runJob() {
    try {
        // 1. Submit Job
        const submitResponse = await axios.post(`${BASE_URL}/jobs/images`, data, { headers });
        const jobId = submitResponse.data.id;
        console.log(`Job submitted. ID: ${jobId}`);

        // 2. Poll for Status
        while (true) {
            const statusResponse = await axios.get(`${BASE_URL}/jobs/${jobId}`, { headers });
            const status = statusResponse.data.status;
            console.log(`Status: ${status}`);

            if (status === 'COMPLETED') {
                console.log("Job finished!");
                console.log("Result URL:", statusResponse.data.result.url);
                break;
            } else if (status === 'FAILED') {
                console.log("Job failed:", statusResponse.data.error);
                break;
            }

            await new Promise(resolve => setTimeout(resolve, 2000)); // Wait 2 seconds
        }
    } catch (error) {
        console.error("Error:", error.message);
    }
}

runJob();
```
```
```{tab-item} cURL
```bash
# 1. Submit Job
curl -X POST https://api.serika.dev/api/openai/v1/jobs/images \
  -H "Authorization: Bearer sk-your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "tensorart-illustrious-xl-v2-aesthetic",
    "prompt": "A futuristic city with neon lights, cyberpunk style"
  }'

# Response: {"id": "job-12345...", "status": "QUEUED"}

# 2. Check Status (Replace job-12345... with actual ID)
curl -X GET https://api.serika.dev/api/openai/v1/jobs/job-12345... \
  -H "Authorization: Bearer sk-your-api-key"
```
```
```

---

## Get Job Status

Check the current status and result of a job.

**Endpoint:** `GET /jobs/{jobId}`

### Response Format

```json
{
  "id": "job-12345abcde",
  "status": "COMPLETED",
  "created_at": 1677858242,
  "result": {
    "url": "https://api.serika.dev/api/cdn/images/generated-image.png",
    "width": 1024,
    "height": 1024,
    "seed": 123456789
  }
}
```

### Status Values

- `QUEUED`: The job has been received and is waiting for a worker.
- `PROCESSING`: The job is currently being executed.
- `COMPLETED`: The job finished successfully. The result is available.
- `FAILED`: The job encountered an error. Check the `error` field for details.

---

## List Jobs

Get a list of your recent jobs.

**Endpoint:** `GET /jobs`

### Response Format

```json
{
  "jobs": [
    {
      "id": "job-12345abcde",
      "status": "COMPLETED",
      "created_at": 1677858242,
      "model": "tensorart-illustrious-xl-v2-aesthetic"
    },
    {
      "id": "job-67890fghij",
      "status": "PROCESSING",
      "created_at": 1677858300,
      "model": "tensorart-animagine-xl"
    }
  ]
}
```
