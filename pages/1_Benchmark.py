import streamlit as st
import json

from modules.benchmark import benchmark_models

st.set_page_config(
    page_title="AI Safety Benchmark",
    page_icon="🏆",
    layout="wide"
)

st.title("🏆 AI Safety Benchmark")

st.caption(
    "Compare AI models using the Sentinel Safety Score"
)

with open("data/benchmark.json") as f:
    models = json.load(f)

results = benchmark_models(models)

st.subheader("Leaderboard")

rank = 1

for item in results:

    st.write(
        f"#{rank}  {item['model']}  —  {item['score']}"
    )

    rank += 1