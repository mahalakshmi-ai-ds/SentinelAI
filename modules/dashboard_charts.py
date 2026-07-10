import plotly.express as px


def threat_distribution():

    data = {
        "Threat": [
            "Prompt Injection",
            "Jailbreak",
            "Prompt Leakage",
            "Role Override"
        ],
        "Count": [35, 20, 15, 10]
    }

    fig = px.pie(
        data,
        names="Threat",
        values="Count",
        title="Threat Distribution"
    )

    fig.update_layout(
        template="plotly_dark"
    )

    return fig