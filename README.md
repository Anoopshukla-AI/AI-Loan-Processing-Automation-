AI Loan Processing Automation (End-to-End)

A production-style, AI + automation project that extracts data from loan documents, validates KYC, scores risk, checks compliance, and pushes results to a dashboard + notifications. Built around FastAPI + n8n + GPT (LLM). Ready for recruiters to scan and for you to demo live.
✨ Why this repo helps you get hired

    Solves a real business problem (fintech-style loan workflows).
    Uses LLM integration, OCR, rules + AI hybrid, and automation orchestration.
    Clean architecture, tests, Docker, and an n8n workflow JSON included.

🏗️ Architecture

User Upload -> FastAPI (/upload) -> OCR -> LLM classify/validate -> Risk Score -> Compliance Check
           -> Persist SQLite -> Notify (Slack/Email via n8n) -> Streamlit/BI dashboard

Optional: Trigger/augment via n8n webhook: CRM event -> HTTP to FastAPI -> Slack/Email.
🔧 Tech Stack

    Backend: FastAPI, Pydantic, SQLite (for demo)
    AI: OpenAI (or compatible), simple heuristics + prompts
    OCR: Tesseract (or Azure Form Recognizer adapter)
    Automation: n8n workflow (JSON provided)
    Frontend: Streamlit dashboard
    Packaging: Docker + docker-compose

🚀 Quickstart (Local)

    Python env

python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env

    Run API

uvicorn backend.main:app --reload --port 8000

    Run dashboard

streamlit run frontend/app.py

    Try an upload

curl -F "file=@data/sample_docs/sample_loan_form.png" http://localhost:8000/upload

☁️ Deploy (one-liners)

Docker

docker build -t ai-loan-processing .
docker run -p 8000:8000 --env-file .env ai-loan-processing

Railway/Render: point to uvicorn backend.main:app --host 0.0.0.0 --port $PORT
🔐 Environment Variables

Create .env (see .env.example):

OPENAI_API_KEY=sk-...
MODEL_NAME=gpt-4o-mini
DB_PATH=./ai.db

🧪 Tests

pytest -q

📊 Sample Output

On a sample doc, you’ll get JSON like:

{
  "application_id": "A-2025-001",
  "kyc_status": "valid",
  "document_type": "bank_statement",
  "risk_score": 0.31,
  "compliance_flags": []
}

🧭 n8n Workflow

Import workflows/n8n_workflow.json, update URLs and secrets, and you're live.
⚠️ Notes

    This repo is demo-first; replace Tesseract with your preferred OCR; plug a real risk model later.
    Use Azure/OpenAI/Gemini interchangeably by adapting the ai_processing.py provider.

Made by Anoop Shukla – AI Automation & Cloud Solutions
