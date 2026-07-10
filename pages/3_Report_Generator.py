import streamlit as st
from modules.report_generator import generate_report

st.set_page_config(
    page_title="AI Safety Report",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Safety Report Generator")
st.caption("Generate a professional SentinelAI safety report.")

# -----------------------------
# Inputs
# -----------------------------

score = st.number_input(
    "Safety Score",
    min_value=0.0,
    max_value=100.0,
    value=92.5
)

risk = st.selectbox(
    "Risk Level",
    [
        "Low",
        "Medium",
        "High",
        "Critical"
    ]
)

deployment = st.selectbox(
    "Deployment",
    [
        "Approved",
        "Needs Review",
        "Blocked"
    ]
)

# -----------------------------
# Sample Analysis Data
# -----------------------------

analysis = {
    "overall_threat": risk,
    "prompt_safety_score": score
}

timeline = [
    {
        "time": "10:00",
        "event": "Prompt Submitted"
    },
    {
        "time": "10:01",
        "event": "Security Scan Started"
    },
    {
        "time": "10:02",
        "event": "Threat Analysis Completed"
    }
]

mitre = [
    {
        "id": "AML.T0051",
        "technique": "Prompt Injection"
    },
    {
        "id": "AML.T0043",
        "technique": "Prompt Leakage"
    }
]

# -----------------------------
# Generate Report
# -----------------------------

if st.button("Generate Report"):

    report = generate_report(
        score=score,
        risk=risk,
        deployment=deployment,
        analysis=analysis,
        timeline=timeline,
        mitre=mitre
    )

    st.success("✅ Report Generated Successfully")

    st.subheader("Generated Report")

    st.json(report)