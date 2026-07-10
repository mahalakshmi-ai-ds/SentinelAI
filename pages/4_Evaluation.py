import streamlit as st

from modules.evaluation_engine import evaluate_dataset

st.set_page_config(
    page_title="Evaluation",
    page_icon="🧪",
    layout="wide"
)

st.title("🧪 SentinelAI Evaluation Suite")

st.caption(
    "Evaluate detector performance using benchmark datasets."
)

results = evaluate_dataset()

st.subheader("Detection Performance")

for item in results:

    st.metric(
        item["dataset"],
        f"{item['accuracy']}%"
    )

st.divider()

st.subheader("Detailed Results")

st.table(results)