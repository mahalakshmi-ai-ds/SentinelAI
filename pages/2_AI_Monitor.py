import streamlit as st

from modules.monitor import monitor_prompt

st.set_page_config(
    page_title="AI Live Monitor",
    page_icon="🛰️",
    layout="wide"
)

st.title("🛰️ SentinelAI Live Monitor")

st.caption(
    "Monitor AI prompts in real time."
)

prompt = st.text_area(
    "Enter Prompt",
    height=200
)

if st.button("Monitor Prompt"):

    if prompt.strip() == "":
        st.warning("Enter a prompt.")

    else:

        result = monitor_prompt(prompt)

        st.subheader("Live Event")

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Time",
            result["timestamp"]
        )

        c2.metric(
            "Threat",
            result["overall"]
        )

        c3.metric(
            "Safety Score",
            f'{result["score"]}/100'
        )

        st.divider()

        st.json(result["analysis"])