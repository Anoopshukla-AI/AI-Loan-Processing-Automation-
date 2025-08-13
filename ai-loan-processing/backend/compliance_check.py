from typing import List

def check_compliance(text: str, kyc_status: str) -> list[str]:
    flags: List[str] = []
    if "cash only" in text.lower():
        flags.append("cash_only_activity")
    if kyc_status != "valid":
        flags.append("kyc_issue")
    if "sanction" in text.lower() or "blacklist" in text.lower():
        flags.append("sanctions_match")
    return flags
