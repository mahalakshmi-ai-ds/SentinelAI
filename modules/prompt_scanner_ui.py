import streamlit as st

from modules.prompt_engine import analyze_prompt
from modules.explainability import generate_explanation

from modules.attack_timeline import build_timeline
from modules.timeline_ui import show_timeline

from modules.mitre_atlas import map_attacks
from modules.mitre_ui import show_mitre

from modules.risk_heatmap import create_heatmap


def show_prompt_scanner():

    st.header("🛡️ Prompt Security Scanner")

    prompt = st.text_area(
        "Paste an AI Prompt",
        height=220,
        placeholder="Paste any prompt here..."
    )

    if st.button("Analyze Prompt"):

        if prompt.strip() == "":
            st.warning("Please enter a prompt.")
            return

        # -----------------------------
        # Analyze Prompt
        # -----------------------------

        analysis = analyze_prompt(prompt)

        timeline = build_timeline(analysis)

        explanations = generate_explanation(analysis)

        mitre = map_attacks(analysis)

        # -----------------------------
        # Save Results for Other Modules
        # -----------------------------

        st.session_state["analysis"] = analysis
        st.session_state["timeline"] = timeline
        st.session_state["mitre"] = mitre

        # -----------------------------
        # Overall Threat
        # -----------------------------

        st.subheader("Overall Threat")

        threat = analysis["overall_threat"]

        if threat == "Critical":
            st.error(f"🚨 {threat}")

        elif threat == "High":
            st.warning(f"⚠️ {threat}")

        elif threat == "Medium":
            st.info(f"ℹ️ {threat}")

        else:
            st.success(f"✅ {threat}")

        st.metric(
            "Prompt Safety Score",
            f'{analysis["prompt_safety_score"]}/100'
        )

        st.divider()

        # -----------------------------
        # Individual Detectors
        # -----------------------------

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Prompt Injection",
                analysis["prompt_injection"]["threat"]
            )

            st.metric(
                "Jailbreak",
                analysis["jailbreak"]["threat"]
            )

        with col2:

            st.metric(
                "Prompt Leakage",
                analysis["prompt_leakage"]["threat"]
            )

            st.metric(
                "Role Override",
                analysis["role_override"]["threat"]
            )

        st.divider()

        # -----------------------------
        # Explainable Threat Report
        # -----------------------------

        st.header("🧠 Explainable Threat Report")

        if len(explanations) == 0:

            st.success("No significant threats detected.")

        else:

            for item in explanations:

                with st.expander(
                    f"🔍 {item['title']}",
                    expanded=True
                ):

                    st.write(item["reason"])
                    st.write(item["impact"])
                    st.success(item["recommendation"])

        st.divider()

        # -----------------------------
        # AI Attack Timeline
        # -----------------------------

        show_timeline(timeline)

        st.divider()

        # -----------------------------
        # MITRE ATLAS Mapping
        # -----------------------------

        show_mitre(mitre)

        st.divider()

        # -----------------------------
        # AI Risk Heatmap
        # -----------------------------

        st.header("🔥 AI Risk Heatmap")

        st.plotly_chart(
            create_heatmap(),
            use_container_width=True
        )