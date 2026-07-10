import streamlit as st
import plotly.express as px

from modules.threat_dashboard import get_dashboard_data

st.set_page_config(
    page_title="Threat Intelligence",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ Threat Intelligence Dashboard")

data = get_dashboard_data()

st.divider()

c1, c2, c3, c4, c5 = st.columns(5)

c1.metric(
    "Total Prompts",
    data["total_prompts"]
)

c2.metric(
    "Safe",
    data["safe_prompts"]
)

c3.metric(
    "Blocked",
    data["blocked_prompts"]
)

c4.metric(
    "Average Score",
    f'{data["average_score"]}/100'
)

c5.metric(
    "Top Attack",
    data["top_attack"]
)

st.divider()

pie = px.pie(
    names=list(data["distribution"].keys()),
    values=list(data["distribution"].values()),
    title="Threat Distribution"
)

st.plotly_chart(
    pie,
    use_container_width=True
)

bar = px.bar(
    x=list(data["trend"].keys()),
    y=list(data["trend"].values()),
    labels={
        "x": "Time",
        "y": "Attack Count"
    },
    title="Attack Trend"
)

st.plotly_chart(
    bar,
    use_container_width=True
)