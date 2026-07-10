import streamlit as st


def show_timeline(timeline):

    st.header("🛡️ AI Attack Timeline")

    for item in timeline:

        threat = item["threat"]

        if threat == "Critical":
            icon = "🔴"

        elif threat == "High":
            icon = "🟠"

        elif threat == "Medium":
            icon = "🟡"

        elif threat == "Low":
            icon = "🟢"

        else:
            icon = "⚪"

        st.markdown(
            f"### {icon} {item['stage']}"
        )

        st.caption(f"Threat Level: {threat}")

        st.divider()