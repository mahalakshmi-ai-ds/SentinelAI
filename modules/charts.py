import plotly.graph_objects as go


def create_gauge(score):

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=score,
            number={"suffix": "/100"},
            title={"text": "Sentinel Safety Score"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "royalblue"},
                "steps": [
                    {"range": [0, 50], "color": "#ffcccc"},
                    {"range": [50, 70], "color": "#ffe680"},
                    {"range": [70, 85], "color": "#cce5ff"},
                    {"range": [85, 100], "color": "#ccffcc"},
                ],
            },
        )
    )

    fig.update_layout(height=350)

    return fig


def create_radar_chart(report):

    categories = [
        "Hallucination",
        "Bias",
        "Toxicity",
        "Privacy",
        "Robustness"
    ]

    values = [
        1 - report["hallucination"],
        1 - report["bias"],
        1 - report["toxicity"],
        1 - report["privacy"],
        report["robustness"]
    ]

    values.append(values[0])
    categories.append(categories[0])

    fig = go.Figure()

    fig.add_trace(
        go.Scatterpolar(
            r=values,
            theta=categories,
            fill="toself",
            name="Safety Profile"
        )
    )

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 1]
            )
        ),
        showlegend=False,
        height=500
    )

    return fig