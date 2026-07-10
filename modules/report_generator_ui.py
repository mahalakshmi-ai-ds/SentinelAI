import streamlit as st
import os

from modules.report_generator import generate_report

# NEW PDF Generator
from modules.pdf_generator_v2 import create_pdf_v2


def show_report_generator(
    score,
    risk,
    deployment,
    analysis,
    timeline,
    mitre
):

    st.header("📄 AI Security Report Generator")

    st.write(
        "Generate a professional AI Security Assessment Report."
    )

    if st.button("Generate Report"):

        report = generate_report(
            score,
            risk,
            deployment,
            analysis,
            timeline,
            mitre
        )

        st.success("✅ Report Generated Successfully!")

        st.subheader("Report Summary")

        st.json(report)

        filename = "SentinelAI_Report_v2.pdf"

        create_pdf_v2(
            report,
            filename
        )

        with open(filename, "rb") as pdf:

            st.download_button(
                label="📥 Download Professional PDF Report",
                data=pdf,
                file_name=filename,
                mime="application/pdf"
            )

        # Optional
        # if os.path.exists(filename):
        #     os.remove(filename)