import os, json, random
from dotenv import load_dotenv
from typing import Tuple

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")

# NOTE: Kept simple and provider-agnostic; integrate your preferred SDK in production.
PROMPT_TEMPLATE = """
You are an AI assistant that reads OCR text from a loan application document.
1) Identify document_type (one of: bank_statement, payslip, aadhaar, pan_card, utility_bill, other).
2) Determine kyc_status (valid / missing / inconsistent).
3) Provide a 3-4 sentence summary focusing on key applicant details.
Return JSON with keys: document_type, kyc_status, summary.
TEXT:
{ocr_text}
"""

def fake_llm_call(prompt: str) -> dict:
    # Offline-friendly fallback for demo/testing
    doc_type = random.choice(["bank_statement","payslip","aadhaar","pan_card","utility_bill"])
    kyc = random.choice(["valid","missing","inconsistent"])
    return {
        "document_type": doc_type,
        "kyc_status": kyc,
        "summary": "Parsed applicant income and address; basic KYC fields present; ready for risk scoring."
    }

def classify_and_validate(ocr_text: str) -> Tuple[str, str, str, float]:
    # In production, replace with OpenAI call
    # resp = client.chat.completions.create(...)
    parsed = fake_llm_call(PROMPT_TEMPLATE.format(ocr_text=ocr_text[:6000]))
    # Heuristic risk scoring: penalize missing/inconsistent KYC
    base = 0.3
    penalty = 0.4 if parsed["kyc_status"] != "valid" else 0.0
    risk = min(0.95, base + penalty)
    return parsed["document_type"], parsed["kyc_status"], parsed["summary"], risk
