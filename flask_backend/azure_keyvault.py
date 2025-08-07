from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
import os

def get_openai_api_key():
    key_vault_name = "open-ai-keys-rob"
    secret_name = "open-ai-resource-rob"
    kv_uri = f"https://{key_vault_name}.vault.azure.net"

    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=kv_uri, credential=credential)
    secret = client.get_secret(secret_name)
    return secret.value

# Usage:
# api_key = get_openai_api_key()
