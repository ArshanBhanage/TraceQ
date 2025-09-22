# Environment Configuration

## Anthropic Claude API Key Setup

To use the Claude AI integration, you need to set your Anthropic API key as an environment variable.

### Option 1: Set Environment Variable (Recommended)

```bash
export ANTHROPIC_API_KEY="your_actual_api_key_here"
```

### Option 2: Create .env file

Create a `.env` file in the backend directory:

```bash
# backend/.env
ANTHROPIC_API_KEY=your_actual_api_key_here
LLM_PROVIDER=claude
BASE_DIR=object_store
REQ_VERSIONS_DIR=req_versions
MAX_FILE_SIZE=50
CHUNK_SIZE=1000
CHUNK_OVERLAP=200
TOP_K=10
```

### Option 3: Set in your shell profile

Add to your `~/.zshrc` or `~/.bashrc`:

```bash
echo 'export ANTHROPIC_API_KEY="your_actual_api_key_here"' >> ~/.zshrc
source ~/.zshrc
```

## Email Configuration

The system supports Gmail API for sending test cases and notifications. You need to set up Gmail API credentials:

### 1. Gmail API Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing one
3. Enable Gmail API
4. Create OAuth 2.0 credentials
5. Download the credentials JSON file

### 2. Set Gmail Environment Variables

```bash
export GOOGLE_CLIENT_ID="your_google_client_id_here"
export GOOGLE_CLIENT_SECRET="your_google_client_secret_here"
export BA_EMAIL="bhanagearshan@gmail.com"
export ADMIN_EMAIL="arshan.bhanage@sjsu.edu"
```

### 3. Quick Setup Script

Run the email setup script to configure Gmail API:

```bash
cd backend
python setup_email.py
```

This will:
- Create credentials.json with your OAuth credentials
- Authenticate with Gmail API
- Create token.json for future use
- Configure email addresses

## Pinecone Vector Database Setup

The system now uses Pinecone for persistent vector storage. You need to set up Pinecone credentials:

### 1. Get Pinecone API Key

1. Go to [Pinecone Console](https://app.pinecone.io/)
2. Create a new project or use existing one
3. Get your API key from the API Keys section

### 2. Set Pinecone Environment Variables

```bash
export PINECONE_API_KEY="your_pinecone_api_key_here"
export PINECONE_ENVIRONMENT="gcp-starter"  # or your preferred environment
export PINECONE_INDEX_NAME="enterprise-requirements"  # or your preferred index name
```

### 3. Add to .env file

```bash
# backend/.env
ANTHROPIC_API_KEY=your_actual_api_key_here
PINECONE_API_KEY=your_pinecone_api_key_here
PINECONE_ENVIRONMENT=gcp-starter
PINECONE_INDEX_NAME=enterprise-requirements
LLM_PROVIDER=claude
BASE_DIR=object_store
REQ_VERSIONS_DIR=req_versions
MAX_FILE_SIZE=50
CHUNK_SIZE=1000
CHUNK_OVERLAP=200
TOP_K=10
```

## Security Notes

- Never commit your API keys to version control
- The `.env` file is already in `.gitignore`
- Use environment variables for production deployments
- Rotate your API keys regularly

## Testing the Integration

After setting the API keys, restart your backend server and test:

```bash
# Test Claude integration
curl http://localhost:8000/api/requirements/provider-info

# Test Pinecone integration
curl http://localhost:8000/api/vector-db/health
curl http://localhost:8000/api/vector-db/stats
```

You should see:
```json
# Provider info
{
  "provider_type": "ClaudeProvider",
  "provider_class": "<class 'app.providers.claude_provider.ClaudeProvider'>",
  "is_claude": true,
  "is_gemini": false,
  "is_openai": false,
  "is_ollama": false
}

# Vector DB health
{
  "status": "healthy",
  "storage_type": "pinecone",
  "vector_count": 0
}
```

## Fallback Behavior

If Pinecone is not configured or unavailable, the system will automatically fall back to in-memory vector storage. This ensures the system continues to work even without external dependencies.
