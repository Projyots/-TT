import os
from flask_backend.utils.config import config
import requests
from flask_backend.utils.embedding_store import EmbeddingStore
from flask_backend.azure_keyvault import get_openai_api_key

AZURE_OPENAI_API_KEY = get_openai_api_key()

# Initialize the embedding store
embedding_store = EmbeddingStore()

def call_openai_chat(prompt):
    # Retrieve similar context from ChromaDB using embeddings
    similar = embedding_store.query(prompt, n_results=2)
    context = ""
    if similar and similar.get("documents"):
        # Flatten and join the most relevant documents as context
        docs = [doc for doc_list in similar["documents"] for doc in doc_list]
        context = "\n".join(docs)
    # Prepend context to the prompt if available
    full_prompt = f"Context:\n{context}\n\nUser: {prompt}" if context else prompt

    headers = {
        "Content-Type": "application/json",
        "api-key": config.AZURE_OPENAI_API_KEY,
    }
    payload = {
        "messages": [
            {"role": "user", "content": full_prompt}
        ],
        "max_tokens": 256,
    }
    resp = requests.post(config.AZURE_OPENAI_CHAT_ENDPOINT, headers=headers, json=payload, timeout=10)
    resp.raise_for_status()
    result = resp.json()
    return result['choices'][0]['message']['content']

def call_openai_embedding(text):
    headers = {
        "Content-Type": "application/json",
        "api-key": AZURE_OPENAI_API_KEY,
    }
    payload = {
        "input": [text]
    }
    resp = requests.post(config.AZURE_OPENAI_EMBEDDING_ENDPOINT, headers=headers, json=payload, timeout=10)
    resp.raise_for_status()
    result = resp.json()
    return result['data'][0]['embedding']