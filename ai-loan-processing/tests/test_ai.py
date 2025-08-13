from backend.ai_processing import classify_and_validate

def test_classify_and_validate():
    doc_type, kyc, summary, risk = classify_and_validate("Sample OCR text with PAN and Aadhaar mentioned.")
    assert doc_type in {"bank_statement","payslip","aadhaar","pan_card","utility_bill"}
    assert kyc in {"valid","missing","inconsistent"}
    assert 0.0 <= risk <= 1.0
