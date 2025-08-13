import os, sqlite3, pandas as pd
import streamlit as st

DB_PATH = os.getenv("DB_PATH", "./ai.db")
st.set_page_config(page_title="AI Loan Processing Dashboard", layout="wide")

st.title("📊 AI Loan Processing Dashboard")
st.caption("Live view of processed applications")

@st.cache_data(ttl=10)
def fetch():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM applications ORDER BY created_at DESC", conn)
    conn.close()
    return df

df = fetch()
st.metric("Total Applications", len(df))
if len(df):
    st.dataframe(df, use_container_width=True)
    st.bar_chart(df["risk_score"])
else:
    st.info("No data yet. Upload via POST /upload on the API.")
