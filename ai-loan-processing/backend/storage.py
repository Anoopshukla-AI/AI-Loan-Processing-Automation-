import os, json, sqlite3
from typing import List

DB_PATH = os.getenv("DB_PATH", "./ai.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS applications (
        id TEXT PRIMARY KEY,
        document_type TEXT,
        kyc_status TEXT,
        risk_score REAL,
        compliance_flags TEXT,
        summary TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)
    conn.commit()
    conn.close()

def insert_application(id: str, doc_type: str, kyc_status: str, risk_score: float, flags: list[str], summary: str):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO applications(id, document_type, kyc_status, risk_score, compliance_flags, summary)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (id, doc_type, kyc_status, risk_score, json.dumps(flags), summary))
    conn.commit()
    conn.close()
