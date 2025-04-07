# API Examples

This page provides example code for using the Serika.dev API in various programming languages.

## Text Generation Examples

### Node.js

```javascript
const axios = require('axios');

// Set your API key
const apiKey = process.env.SERIKA_API_KEY;

async function generateTextWithSerika() {
  try {
    const response = await axios.post(
      'https://api.serika.dev/v1/chat/completions',
      {
        messages: [
          { role: 'user', content: 'Explain quantum computing in simple terms' }
        ],
        model: 'euryale-70b'
      },
      {
        headers: {
          'Authorization': `Bearer ${apiKey}`,
          'Content-Type': 'application/json'
        }
      }
    );
    
    console.log(response.data.choices[0].message.content);
    console.log(`Tokens used: ${response.data.usage.total_tokens}`);
    
    return response.data;
  } catch (error) {
    console.error('Error:', error.response ? error.response.data : error.message);
    throw error;
  }
}

generateTextWithSerika();
```

### Python

```python
import os
import requests

# Set your API key
api_key = os.environ.get("SERIKA_API_KEY")

def generate_text_with_serika():
    try:
        response = requests.post(
            "https://api.serika.dev/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            json={
                "messages": [
                    {"role": "user", "content": "Explain quantum computing in simple terms"}
                ],
                "model": "euryale-70b"
            }
        )
        
        response.raise_for_status()
        result = response.json()
        
        print(result["choices"][0]["message"]["content"])
        print(f"Tokens used: {result['usage']['total_tokens']}")
        
        return result
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        if hasattr(e, "response") and e.response:
            print(e.response.text)
        raise

if __name__ == "__main__":
    generate_text_with_serika()
```

### PHP

```php
<?php

// Set your API key
$apiKey = getenv('SERIKA_API_KEY');

function generateTextWithSerika() {
    global $apiKey;
    
    $data = [
        'messages' => [
            ['role' => 'user', 'content' => 'Explain quantum computing in simple terms']
        ],
        'model' => 'euryale-70b'
    ];
    
    $options = [
        'http' => [
            'method' => 'POST',
            'header' => [
                'Authorization: Bearer ' . $apiKey,
                'Content-Type: application/json'
            ],
            'content' => json_encode($data)
        ]
    ];
    
    $context = stream_context_create($options);
    $response = file_get_contents('https://api.serika.dev/v1/chat/completions', false, $context);
    
    if ($response === FALSE) {
        echo "Error making request";
        return null;
    }
    
    $result = json_decode($response, true);
    
    echo $result['choices'][0]['message']['content'] . "\n";
    echo "Tokens used: " . $result['usage']['total_tokens'] . "\n";
    
    return $result;
}

generateTextWithSerika();
```

## Complete Node.js Example with Advanced Features

This example demonstrates a comprehensive implementation with multiple API features:

```javascript
// Complete example for testing Serika API with text and image generation
const axios = require('axios');
const fs = require('fs').promises;
const path = require('path');
const { promisify } = require('util');
const sleep = promisify(setTimeout);

// Configuration - replace with your actual values
const API_KEY = 'sk-your-api-key';
const API_BASE_URL = 'https://api.serika.dev/v1';

// Create directory for saving test outputs
const OUTPUT_DIR = path.join(__dirname, 'api_outputs');
fs.mkdir(OUTPUT_DIR, { recursive: true }).catch(console.error);

// Helper function for making API requests
async function makeApiRequest(endpoint, method = 'GET', data = null) {
  try {
    // Configure request options
    const options = {
      method: method,
      url: `${API_BASE_URL}${endpoint}`,
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${API_KEY}`
      }
    };
    
    // Only add data for non-GET requests and make sure it's properly stringified
    if (method !== 'GET' && data !== null) {
      options.data = JSON.stringify(data);
    }
    
    const response = await axios(options);
    return response.data;
  } catch (error) {
    if (error.response) {
      // The request was made and the server responded with a status code
      // that falls out of the range of 2xx
      console.error('API Error Response:', error.response.data);
      console.error('Status:', error.response.status);
    } else if (error.request) {
      // The request was made but no response was received
      console.error('No response received:', error.request);
    } else {
      // Something happened in setting up the request that triggered an Error
      console.error('Request error:', error.message);
    }
    throw error;
  }
}

// List available models
async function listModels() {
  try {
    console.log('Fetching available models...');
    const models = await makeApiRequest('/models');
    console.log('Available models:');
    if (models && models.data && Array.isArray(models.data)) {
      models.data.forEach(model => {
        console.log(`- ${model.id} (Provider: ${model.owned_by})`);
      });
      return models.data;
    } else {
      console.error('Unexpected response format:', models);
      return [];
    }
  } catch (error) {
    console.error('Failed to fetch models:', error.message);
    return [];
  }
}

// Enhanced image generation with advanced parameters
async function generateImage(prompt, model = 'novelai/nai-diffusion-3', parameters = {}) {
  try {
    console.log(`Generating image with prompt: "${prompt}"`);
    console.log(`Using model: ${model}`);
    
    const requestData = {
      prompt,
      model,
      n: parameters.n || 1,
      size: parameters.size || '1024x1024',
      response_format: parameters.response_format || 'url',
      // Additional parameters
      negative_prompt: parameters.negative_prompt,
      style: parameters.style,
      steps: parameters.steps,
      sampler: parameters.sampler,
      seed: parameters.seed || Math.floor(Math.random() * 4294967295)
    };
    
    console.log('Request parameters:', JSON.stringify(requestData, null, 2));
    
    const result = await makeApiRequest('/images/generations', 'POST', requestData);
    
    if (result && result.data && Array.isArray(result.data) && result.data.length > 0) {
      console.log('Image generated successfully!');
      
      // Log all image URLs
      result.data.forEach((img, index) => {
        console.log(`Image ${index + 1} URL: ${img.url}`);
      });
      
      // Try to download the first image
      try {
        const firstImageUrl = result.data[0].url;
        const response = await axios.get(firstImageUrl, { responseType: 'arraybuffer' });
        const timestamp = Date.now();
        const imageName = `image_${timestamp}_${model.replace(/\//g, '-')}.png`;
        const imagePath = path.join(OUTPUT_DIR, imageName);
        
        await fs.writeFile(imagePath, response.data);
        console.log(`Image saved to: ${imagePath}`);
      } catch (downloadError) {
        console.error('Failed to download and save image:', downloadError.message);
      }
      
      return result;
    } else {
      console.error('Unexpected result format:', result);
      throw new Error('Invalid response format from image generation');
    }
  } catch (error) {
    console.error('Failed to generate image:', error.message);
    throw error;
  }
}

// Text generation with chat completions
async function generateText(prompt, model = 'euryale-70b', options = {}) {
  try {
    console.log(`Generating text completion with prompt: "${prompt}"`);
    console.log(`Using model: ${model}`);
    
    const messages = [{ role: 'user', content: prompt }];
    
    if (options.systemPrompt) {
      messages.unshift({ role: 'system', content: options.systemPrompt });
    }
    
    const requestData = {
      messages,
      model,
      stream: options.stream || false,
      character_id: options.character_id,
      temperature: options.temperature || 0.7,
      system_prompt: options.systemPrompt
    };
    
    console.log('Request parameters:', JSON.stringify(requestData, null, 2));
    
    const result = await makeApiRequest('/chat/completions', 'POST', requestData);
    
    if (result && result.choices && result.choices.length > 0) {
      const responseText = result.choices[0].message.content;
      console.log('Generated text:', responseText);
      
      // Save the response to a file
      try {
        const timestamp = Date.now();
        const textFileName = `text_${timestamp}_${model.replace(/\//g, '-')}.txt`;
        const textFilePath = path.join(OUTPUT_DIR, textFileName);
        
        const contentToSave = `Prompt: ${prompt}\n\nModel: ${model}\n\nResponse:\n${responseText}\n\nUsage: ${JSON.stringify(result.usage, null, 2)}`;
        await fs.writeFile(textFilePath, contentToSave);
        console.log(`Text response saved to: ${textFilePath}`);
      } catch (saveError) {
        console.error('Failed to save text response:', saveError.message);
      }
      
      return result;
    } else {
      console.error('Unexpected result format:', result);
      throw new Error('Invalid response format from text generation');
    }
  } catch (error) {
    console.error('Failed to generate text:', error.message);
    throw error;
  }
}

// Run a series of API tests
async function runTests() {
  try {
    console.log('==================================================');
    console.log('🚀 Starting Serika API Tests');
    console.log('==================================================');
    
    // First list the available models
    console.log('\n===== TEST 1: List Models =====');
    const models = await listModels();
    
    // Text generation - basic test
    console.log('\n===== TEST 2: Text Generation - Basic =====');
    await generateText('Explain the concept of APIs in three sentences.', 'euryale-70b');
    
    // Wait to avoid rate limiting
    console.log('Waiting 2 seconds before next request...');
    await sleep(2000);
    
    // Text generation with system prompt
    console.log('\n===== TEST 3: Text Generation - With System Prompt =====');
    await generateText(
      'What are three benefits of using AI in software development?',
      'llama-4-scout-17b-instruct',
      { systemPrompt: 'You are an expert software engineer. Keep responses technical but concise.' }
    );
    
    // Wait to avoid rate limiting
    console.log('Waiting 2 seconds before next request...');
    await sleep(2000);
    
    // Generate an image with basic parameters
    console.log('\n===== TEST 4: Image Generation - Basic =====');
    await generateImage('A serene mountain landscape with cherry blossoms at sunset', 'novelai/nai-diffusion-3');
    
    // Wait to avoid rate limiting
    console.log('Waiting 2 seconds before next request...');
    await sleep(2000);
    
    // Generate an image with advanced parameters
    console.log('\n===== TEST 5: Image Generation - Advanced Parameters =====');
    await generateImage(
      'A cyberpunk cityscape with neon lights and flying cars',
      'novelai/nai-diffusion-3',
      {
        negative_prompt: 'blurry, bad quality, disfigured, low resolution',
        size: '1024x1024',
        steps: 28,
        sampler: 'k_dpmpp_2s_ancestral',
        seed: 42069
      }
    );
    
    console.log('\n==================================================');
    console.log('✅ All tests completed successfully!');
    console.log('==================================================');
  } catch (error) {
    console.error('\n❌ Test execution failed:', error.message);
    process.exit(1);
  }
}

// Execute the tests
runTests();
```

## Image Generation Examples

### Node.js

```javascript
const axios = require('axios');
const fs = require('fs');
const path = require('path');

// Set your API key
const apiKey = process.env.SERIKA_API_KEY;

async function generateImageWithSerika() {
  try {
    const response = await axios.post(
      'https://api.serika.dev/v1/images/generations',
      {
        prompt: 'A beautiful mountain landscape with a lake at sunset',
        model: 'novelai/nai-diffusion-3',
        n: 1
      },
      {
        headers: {
          'Authorization': `Bearer ${apiKey}`,
          'Content-Type': 'application/json'
        }
      }
    );
    
    console.log('Image generated:');
    console.log(response.data.data[0].url);
    
    // Optional: Download the image
    const imageUrl = response.data.data[0].url;
    const imageResponse = await axios.get(imageUrl, { responseType: 'arraybuffer' });
    const outputPath = path.join(__dirname, 'generated-image.png');
    fs.writeFileSync(outputPath, Buffer.from(imageResponse.data));
    console.log(`Image saved to ${outputPath}`);
    
    return response.data;
  } catch (error) {
    console.error('Error:', error.response ? error.response.data : error.message);
    throw error;
  }
}

generateImageWithSerika();
```

### Python

```python
import os
import requests
import shutil

# Set your API key
api_key = os.environ.get("SERIKA_API_KEY")

def generate_image_with_serika():
    try:
        response = requests.post(
            "https://api.serika.dev/v1/images/generations",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            json={
                "prompt": "A beautiful mountain landscape with a lake at sunset",
                "model": "novelai/nai-diffusion-3",
                "n": 1
            }
        )
        
        response.raise_for_status()
        result = response.json()
        
        image_url = result["data"][0]["url"]
        print(f"Image generated: {image_url}")
        
        # Optional: Download the image
        image_response = requests.get(image_url, stream=True)
        image_response.raise_for_status()
        
        with open("generated-image.png", "wb") as f:
            shutil.copyfileobj(image_response.raw, f)
        
        print("Image saved to generated-image.png")
        
        return result
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        if hasattr(e, "response") and e.response:
            print(e.response.text)
        raise

if __name__ == "__main__":
    generate_image_with_serika()
```

## Using Characters

### Node.js

```javascript
const axios = require('axios');

// Set your API key
const apiKey = process.env.SERIKA_API_KEY;

async function getCharacters() {
  try {
    const response = await axios.get(
      'https://api.serika.dev/v1/characters',
      {
        headers: {
          'Authorization': `Bearer ${apiKey}`
        }
      }
    );
    
    console.log('Available characters:');
    response.data.forEach(character => {
      console.log(`${character.name} (ID: ${character.id})`);
    });
    
    return response.data;
  } catch (error) {
    console.error('Error:', error.response ? error.response.data : error.message);
    throw error;
  }
}

async function generateWithCharacter(characterId) {
  try {
    const response = await axios.post(
      'https://api.serika.dev/v1/chat/completions',
      {
        messages: [
          { role: 'user', content: 'Tell me about yourself' }
        ],
        model: 'euryale-70b',
        character_id: characterId
      },
      {
        headers: {
          'Authorization': `Bearer ${apiKey}`,
          'Content-Type': 'application/json'
        }
      }
    );
    
    console.log(response.data.choices[0].message.content);
    return response.data;
  } catch (error) {
    console.error('Error:', error.response ? error.response.data : error.message);
    throw error;
  }
}

// Get characters and then use the first one to generate text
getCharacters().then(characters => {
  if (characters.length > 0) {
    return generateWithCharacter(characters[0].id);
  }
});
```

## Streaming Responses

### Node.js

```javascript
const axios = require('axios');

// Set your API key
const apiKey = process.env.SERIKA_API_KEY;

async function streamCompletionWithSerika() {
  try {
    const response = await axios.post(
      'https://api.serika.dev/v1/chat/completions',
      {
        messages: [
          { role: 'user', content: 'Tell me a story about a dragon' }
        ],
        model: 'euryale-70b',
        stream: true
      },
      {
        headers: {
          'Authorization': `Bearer ${apiKey}`,
          'Content-Type': 'application/json'
        },
        responseType: 'stream'
      }
    );
    
    let fullResponse = '';
    
    response.data.on('data', chunk => {
      const lines = chunk.toString().split('\n').filter(line => line.trim() !== '');
      
      for (const line of lines) {
        if (line.startsWith('data: ')) {
          const data = line.substring(6);
          
          if (data === '[DONE]') {
            console.log('\nStream completed.');
          } else {
            try {
              const parsed = JSON.parse(data);
              const content = parsed.choices[0]?.delta?.content || '';
              if (content) {
                process.stdout.write(content);
                fullResponse += content;
              }
            } catch (e) {
              console.error('Error parsing chunk:', e);
            }
          }
        }
      }
    });
    
    return new Promise(resolve => {
      response.data.on('end', () => {
        resolve(fullResponse);
      });
    });
  } catch (error) {
    console.error('Error:', error.response ? error.response.data : error.message);
    throw error;
  }
}

streamCompletionWithSerika();
```

### Python

```python
import os
import json
import requests
import sseclient

# Set your API key
api_key = os.environ.get("SERIKA_API_KEY")

def stream_completion_with_serika():
    try:
        response = requests.post(
            "https://api.serika.dev/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
                "Accept": "text/event-stream"
            },
            json={
                "messages": [
                    {"role": "user", "content": "Tell me a story about a dragon"}
                ],
                "model": "euryale-70b",
                "stream": True
            },
            stream=True
        )
        
        response.raise_for_status()
        client = sseclient.SSEClient(response)
        
        full_response = ""
        for event in client.events():
            if event.data == "[DONE]":
                print("\nStream completed.")
                break
                
            try:
                data = json.loads(event.data)
                content = data["choices"][0]["delta"].get("content", "")
                if content:
                    print(content, end="", flush=True)
                    full_response += content
            except json.JSONDecodeError:
                print(f"Error decoding: {event.data}")
        
        return full_response
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        if hasattr(e, "response") and e.response:
            print(e.response.text)
        raise

if __name__ == "__main__":
    stream_completion_with_serika()
```

## Error Handling

### Node.js

```javascript
const axios = require('axios');

// Set your API key
const apiKey = process.env.SERIKA_API_KEY;

async function handleApiErrors() {
  try {
    // Example: Missing required parameter
    const response = await axios.post(
      'https://api.serika.dev/v1/chat/completions',
      {
        // Intentionally missing the 'messages' parameter
        model: 'euryale-70b'
      },
      {
        headers: {
          'Authorization': `Bearer ${apiKey}`,
          'Content-Type': 'application/json'
        }
      }
    );
    
    console.log(response.data);
  } catch (error) {
    if (error.response) {
      // The request was made and the server responded with a status code
      // that falls out of the range of 2xx
      console.error('Error response:', {
        status: error.response.status,
        data: error.response.data
      });
      
      if (error.response.data && error.response.data.error) {
        const apiError = error.response.data.error;
        
        switch (apiError.type) {
          case 'invalid_request_error':
            console.error(`Invalid request: ${apiError.message}`);
            // Handle invalid request (e.g., missing parameters)
            break;
            
          case 'authentication_error':
            console.error(`Authentication error: ${apiError.message}`);
            // Handle authentication issues (e.g., invalid API key)
            break;
            
          case 'rate_limit_error':
            console.error(`Rate limit exceeded: ${apiError.message}`);
            // Handle rate limiting (e.g., implement exponential backoff)
            break;
            
          case 'billing_error':
            console.error(`Billing error: ${apiError.message}`);
            // Handle billing issues (e.g., notify user to set up billing)
            break;
            
          default:
            console.error(`API error: ${apiError.message}`);
        }
      }
    } else if (error.request) {
      // The request was made but no response was received
      console.error('No response received:', error.request);
    } else {
      // Something happened in setting up the request that triggered an Error
      console.error('Request setup error:', error.message);
    }
  }
}

handleApiErrors();
```

### Python

```python
import os
import requests
import time

# Set your API key
api_key = os.environ.get("SERIKA_API_KEY")

def handle_api_errors():
    try:
        # Example: Missing required parameter
        response = requests.post(
            "https://api.serika.dev/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            json={
                # Intentionally missing the 'messages' parameter
                "model": "euryale-70b"
            }
        )
        
        response.raise_for_status()
        print(response.json())
        
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 400:
            error_data = e.response.json()
            if "error" in error_data:
                api_error = error_data["error"]
                
                if api_error["type"] == "invalid_request_error":
                    print(f"Invalid request: {api_error['message']}")
                    # Handle invalid request (e.g., missing parameters)
                    
                elif api_error["type"] == "authentication_error":
                    print(f"Authentication error: {api_error['message']}")
                    # Handle authentication issues (e.g., invalid API key)
                    
                elif api_error["type"] == "rate_limit_error":
                    print(f"Rate limit exceeded: {api_error['message']}")
                    # Handle rate limiting (e.g., implement exponential backoff)
                    retry_after = int(e.response.headers.get("Retry-After", 5))
                    print(f"Retrying after {retry_after} seconds")
                    time.sleep(retry_after)
                
                elif api_error["type"] == "billing_error":
                    print(f"Billing error: {api_error['message']}")
                    # Handle billing issues (e.g., notify user to set up billing)
                    
                else:
                    print(f"API error: {api_error['message']}")
            else:
                print(f"HTTP error: {e}")
        else:
            print(f"HTTP error: {e}")
            
    except requests.exceptions.ConnectionError:
        print("Connection error: Failed to connect to the API")
        
    except requests.exceptions.Timeout:
        print("Timeout error: Request timed out")
        
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")

if __name__ == "__main__":
    handle_api_errors()
```

For more examples and detailed documentation on each endpoint, refer to the [API Reference](api/overview.md) section. 