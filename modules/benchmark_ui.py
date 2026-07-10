import streamlit as st
import pandas as pd


def show_benchmark(models):

    st.header("📊 AI Safety Benchmark")

    df = pd.DataFrame(models)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.bar_chart(
        df.set_index("model")["score"]
    )