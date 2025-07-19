# ----------------------------
# README.md (summary)
# ----------------------------
# Pinecone Vector Search API

## How to Deploy to Google Cloud Run

1. Create `.env` with OpenAI + Pinecone keys.
2. Build and push Docker image:
```
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/pinecone-poc
```
3. Deploy to Cloud Run:
```
gcloud run deploy pinecone-poc \
  --image gcr.io/YOUR_PROJECT_ID/pinecone-poc \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

4. Test API:
- `POST /insert` with JSON `{ "text": "hello", "metadata": {"source": "test"} }`
- `POST /search` with JSON `{ "text": "hello" }`
