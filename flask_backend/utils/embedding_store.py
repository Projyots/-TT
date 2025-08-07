import chromadb
from chromadb.utils import embedding_functions
from flask_backend.azure_keyvault import get_openai_api_key
import requests
from flask_backend.utils.config import config

class EmbeddingStore:
    def __init__(self, collection_name="openai_embeddings"):
        self.client = chromadb.Client()
        self.collection = self.client.get_or_create_collection(collection_name)
        self.api_key = get_openai_api_key()

    def get_embedding(self, text):
        headers = {
            "Content-Type": "application/json",
            "api-key": self.api_key,
        }
        payload = {
            "input": [text]
        }
        resp = requests.post(config.AZURE_OPENAI_EMBEDDING_ENDPOINT, headers=headers, json=payload, timeout=10)
        resp.raise_for_status()
        result = resp.json()
        return result['data'][0]['embedding']

    def add_text(self, text, metadata=None, doc_id=None):
        embedding = self.get_embedding(text)
        if doc_id is None:
            doc_id = str(hash(text))
        self.collection.add(
            embeddings=[embedding],
            documents=[text],
            metadatas=[metadata or {}],
            ids=[doc_id]
        )
        return doc_id

    def query(self, text, n_results=3):
        embedding = self.get_embedding(text)
        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=n_results
        )
        return results
