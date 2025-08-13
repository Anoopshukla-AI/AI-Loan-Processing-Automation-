from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import os, uuid, io
from PIL import Image
from .ocr_extraction import extract_text
from .ai_processing import classify_and_validate
from .compliance_check import check_compliance
from .storage import init_db, insert_application

load_dotenv()
app = FastAPI(title="AI Loan Processing API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()

class ProcessResult(BaseModel):
    application_id: str
    document_type: str
    kyc_status: str
    risk_score: float
    compliance_flags: list[str]
    summary: str

@app.post("/upload", response_model=ProcessResult)
async def upload(file: UploadFile = File(...)):
    if file.content_type not in ["image/png", "image/jpeg", "application/pdf"]:
        raise HTTPException(status_code=400, detail="Only PNG/JPEG/PDF supported")
    app_id = f"A-{uuid.uuid4().hex[:8]}"
    content = await file.read()

    # Convert to image or multiple images
    text = extract_text(content, file.content_type)

    # LLM classify + validate fields
    doc_type, kyc_status, summary, risk_score = classify_and_validate(text)

    # Compliance
    flags = check_compliance(text, kyc_status)

    # Persist
    insert_application(app_id, doc_type, kyc_status, risk_score, flags, summary)

    return ProcessResult(
        application_id=app_id,
        document_type=doc_type,
        kyc_status=kyc_status,
        risk_score=risk_score,
        compliance_flags=flags,
        summary=summary,
    )

@app.get("/health")
def health():
    return {"status": "ok"}
