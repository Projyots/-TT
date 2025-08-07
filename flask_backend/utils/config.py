import os

from typing import Union
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Application settings loaded from environment variables or .env file.
    """
    
    AZURE_OPENAI_ENDPOINT: str = "https://open-ai-resource-rob.openai.azure.com/openai/deployments/gpt-4o-mini/chat/completions?api-version=2024-08-01-preview"
    AZURE_OPENAI_EMBEDDING_ENDPOINT: str = "https://open-ai-resource-rob.openai.azure.com/openai/deployments/text-embedding-3-large/embeddings?api-version=2023-05-15"
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"