# OAuth 2.0 API

Serika.dev provides a full OAuth 2.0 implementation, allowing you to build applications that can access user data and perform actions on their behalf.

## Client Management

Since there is no UI for managing OAuth clients in the dashboard yet, you must use the API directly via cURL.

### Create a Client

**Endpoint:** `POST /oauth/clients`

**Headers:**
- `Authorization`: Bearer <your-session-token-or-api-key> (Note: This endpoint requires authentication)
- `Content-Type`: `application/json`

**Body Parameters:**
- `name` (string): Name of your application
- `redirectUris` (array of strings): Allowed callback URLs
- `scopes` (array of strings): Requested permissions (e.g., `profile`, `generations`)

**Example:**

```bash
curl -X POST https://api.serika.dev/api/openai/v1/oauth/clients \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "My Cool App",
    "redirectUris": ["https://myapp.com/callback"],
    "scopes": ["profile", "generations"]
  }'
```

**Response:**

```json
{
  "clientId": "client_12345...",
  "clientSecret": "secret_abcde...",
  "name": "My Cool App",
  "redirectUris": ["https://myapp.com/callback"],
  "scopes": ["profile", "generations"]
}
```

> [!IMPORTANT]
> Save your `clientSecret` immediately. It cannot be retrieved later, only reset.

### List Clients

**Endpoint:** `GET /oauth/clients`

```bash
curl https://api.serika.dev/api/openai/v1/oauth/clients \
  -H "Authorization: Bearer YOUR_TOKEN"
```

### Reset Client Secret

**Endpoint:** `POST /oauth/clients/:clientId/reset-secret`

```bash
curl -X POST https://api.serika.dev/api/openai/v1/oauth/clients/CLIENT_ID/reset-secret \
  -H "Authorization: Bearer YOUR_TOKEN"
```

## OAuth Flow

Serika.dev supports the Authorization Code flow with PKCE (Proof Key for Code Exchange).

### 1. Authorization Request

Redirect the user to the authorization endpoint:

`GET https://api.serika.dev/api/openai/v1/oauth/authorize`

**Parameters:**
- `response_type`: `code`
- `client_id`: Your Client ID
- `redirect_uri`: One of your registered redirect URIs
- `scope`: Space-separated list of scopes (e.g., `profile generations`)
- `state`: Random string to prevent CSRF
- `code_challenge`: PKCE code challenge
- `code_challenge_method`: `S256`

### 2. Token Exchange

Exchange the authorization code for an access token.

**Endpoint:** `POST /oauth/token`

**Body Parameters:**
- `grant_type`: `authorization_code`
- `code`: The code received in the callback
- `redirect_uri`: The same redirect URI used in step 1
- `client_id`: Your Client ID
- `client_secret`: Your Client Secret
- `code_verifier`: PKCE code verifier

### 3. Use Access Token

Use the access token to make API requests on behalf of the user.

**Header:** `Authorization: Bearer <access_token>`

## Scopes

| Scope | Description |
|-------|-------------|
| `profile` | Access user profile information (ID, username, avatar) |
| `generations` | Generate text and images on behalf of the user |
| `characters` | Access user's characters |

## Protected Endpoints

Once you have an access token, you can use these endpoints:

- `GET /oauth/userinfo`: Get user profile
- `POST /oauth/chat/completions`: Generate chat completions
- `POST /oauth/images/generations`: Generate images
- `GET /oauth/characters/:id`: Get character details
