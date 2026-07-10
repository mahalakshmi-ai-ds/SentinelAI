import plotly.express as px
import pandas as pd

def create_heatmap():

    data = pd.DataFrame(
        [
            [0.1, 0.2, 0.6, 0.8],
            [0.2, 0.3, 0.7, 0.9],
            [0.1, 0.4, 0.5, 0.6],
            [0.3, 0.6, 0.8, 1.0],
        ],
        columns=["Hallucination", "Bias", "Privacy", "Toxicity"],
        index=["Low", "Medium", "High", "Critical"]
    )

    fig = px.imshow(
        data,
        text_auto=".2f",
        aspect="auto",
        color_continuous_scale="RdYlGn_r",
        title="AI Risk Heatmap"
    )

    return fig