# Azure OpenAI LLM Exercise

## Overview
This project demonstrates a simple full-stack application with a Python backend and a React frontend. The backend exposes RESTful APIs and integrates with an LLM (Large Language Model) hosted on Azure OpenAI. The frontend interacts with the backend and displays the processed data to the user.

## Exercise Requirements
- Build a backend (Flask or Django REST) that handles RESTful API requests and connects to Azure OpenAI endpoints.
- Build a frontend (React) that interacts with the backend and displays LLM responses.
- Deploy both backend and frontend to Azure.

## Technical Details
- Use the pre-setup Azure OpenAI endpoints:
  - GPT-4o-mini: https://open-ai-resource-rob.openai.azure.com/openai/deployments/gpt-4o-mini/chat/completions?api-version=2024-08-01-preview
  - Text-embedding: https://open-ai-resource-rob.openai.azure.com/openai/deployments/text-embedding-3-large/embeddings?api-version=2023-05-15
- API key is stored in Azure Key Vault: `open-ai-keys-rob`, secret name: `open-ai-resource-rob`.

## Project Structure
```
ai-app-exercise/
├── backend/                  # Python backend (Flask or Django REST)
│   ├── app.py                # Main application entry point
│   ├── requirements.txt      # Dependencies
│   ├── .env                  # Environment variables (not committed)
│   ├── openai_service.py     # Azure OpenAI integration
│   └── Dockerfile            # Container configuration
├── frontend/                 # React application
│   ├── public/
│   ├── src/
│   │   ├── components/       # UI components
│   │   ├── App.js            # Main application
│   │   └── index.js          # Entry point
│   ├── package.json
│   └── Dockerfile
├── .gitignore
└── README.md
```

## Tips
- Focus on user experience in the frontend.
- Ensure backend scalability and robust error handling.
- Use secure practices for API keys and secrets.
- Use clean, readable code and keep setup simple.

---
For more details, see the code and comments in each folder.

# LLM Azure Integration Project

## Django REST Backend
- Django REST API at `/api/llm/`
- Interacts with Azure OpenAI

## Flask Backend
- Flask REST API at `/api/llm`
- Interacts with Azure OpenAI

## Frontend
- React app
- Calls backend API

## Setup

### Django REST Backend
```sh
cd backend
python -m venv env
env\Scripts\activate  # or source env/bin/activate
pip install -r requirements.txt
set AZURE_OPENAI_API_KEY=your-key  # or export AZURE_OPENAI_API_KEY=...
python manage.py migrate
python manage.py runserver
```

### Flask Backend
```sh
cd flask_backend
python -m venv env
env\Scripts\activate  # or source env/bin/activate
pip install -r requirements.txt
set AZURE_OPENAI_API_KEY=your-key  # or export AZURE_OPENAI_API_KEY=...
python app.py
```

### Frontend
```sh
cd frontend
npm install
npm start
```