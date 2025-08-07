import os
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
from azure_keyvault import get_openai_api_key
from flask_backend.utils.config import config
from flask_backend.utils.chat import call_openai_chat, call_openai_embedding


app = Flask(__name__)
CORS(app)


@app.route('/api/llm', methods=['POST'])
def llm():
    data = request.get_json()
    prompt = data.get('prompt', '')
    try:
        content = call_openai_chat(prompt)
        return jsonify({"response": content})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/embedding', methods=['POST'])
def embedding():
    data = request.get_json()
    text = data.get('text', '')
    try:
        embedding = call_openai_embedding(text)
        return jsonify({"embedding": embedding})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
