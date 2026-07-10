import streamlit as st


def show_monitor(data):

    st.header("🖥️ AI Security Monitor")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Requests",
            data["requests"]
        )

    with col2:
        st.metric(
            "Blocked",
            data["blocked"]
        )

    with col3:
        st.metric(
            "Safe",
            data["safe"]
        )

    st.divider()

    threat = data["threat"]

    if threat == "High":
        st.error(f"🚨 Current Threat : {threat}")

    elif threat == "Medium":
        st.warning(f"⚠️ Current Threat : {threat}")

    else:
        st.success(f"✅ Current Threat : {threat}")

    st.divider()

    st.subheader("Live Security Events")

    for event in data["events"]:
        st.write("•", event)