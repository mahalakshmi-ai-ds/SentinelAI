from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER


def create_pdf(report, filename):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    title_style = styles["Title"]
    title_style.alignment = TA_CENTER

    heading = styles["Heading2"]
    normal = styles["BodyText"]

    story = []

    # =====================================
    # TITLE
    # =====================================

    story.append(
        Paragraph(
            "🛡 SentinelAI Security Assessment Report",
            title_style
        )
    )

    story.append(Spacer(1, 20))

    # =====================================
    # EXECUTIVE SUMMARY
    # =====================================

    story.append(
        Paragraph("Executive Summary", heading)
    )

    story.append(
        Paragraph(
            "This report summarizes the AI security assessment "
            "performed by SentinelAI. The system evaluates prompts "
            "for prompt injection, jailbreak attempts, prompt leakage, "
            "role override attacks, and maps findings to MITRE ATLAS.",
            normal
        )
    )

    story.append(Spacer(1, 15))

    story.append(
        Paragraph("------------------------------", normal)
    )

    # =====================================
    # ASSESSMENT DETAILS
    # =====================================

    story.append(
        Paragraph("Assessment Details", heading)
    )

    story.append(
        Paragraph(
            f"<b>Generated On:</b> {report['generated_on']}",
            normal
        )
    )

    story.append(
        Paragraph(
            f"<b>Overall Safety Score:</b> {report['overall_score']}/100",
            normal
        )
    )

    story.append(
        Paragraph(
            f"<b>Risk Level:</b> {report['risk']}",
            normal
        )
    )

    story.append(
        Paragraph(
            f"<b>Deployment Status:</b> {report['deployment']}",
            normal
        )
    )

    # =====================================
    # COLORED THREAT
    # =====================================

    threat = report["overall_threat"]

    color_map = {
        "Critical": "red",
        "High": "orange",
        "Medium": "gold",
        "Low": "green"
    }

    story.append(
        Paragraph(
            f"<b>Overall Threat:</b> "
            f"<font color='{color_map.get(threat,'black')}'><b>{threat}</b></font>",
            normal
        )
    )

    story.append(
        Paragraph(
            f"<b>Prompt Safety Score:</b> {report['prompt_safety_score']}/100",
            normal
        )
    )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph("------------------------------", normal)
    )

    # =====================================
    # MITRE ATLAS
    # =====================================

    story.append(
        Paragraph("MITRE ATLAS Techniques", heading)
    )

    if len(report["mitre"]) == 0:

        story.append(
            Paragraph(
                "No MITRE ATLAS techniques detected.",
                normal
            )
        )

    else:

        for attack in report["mitre"]:

            story.append(
                Paragraph(
                    f"• {attack['id']} — {attack['name']}",
                    normal
                )
            )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph("------------------------------", normal)
    )

    # =====================================
    # RECOMMENDATIONS
    # =====================================

    story.append(
        Paragraph("Recommendations", heading)
    )

    recommendations = [

        "Validate every user prompt before processing.",

        "Enable prompt injection filtering.",

        "Monitor jailbreak attempts continuously.",

        "Protect hidden system prompts.",

        "Review role override attacks.",

        "Perform regular AI safety evaluations."

    ]

    for item in recommendations:

        story.append(
            Paragraph(f"• {item}", normal)
        )

    story.append(Spacer(1, 20))

    # =====================================
    # SECURITY VERDICT
    # =====================================

    story.append(
        Paragraph("Security Verdict", heading)
    )

    if report["overall_score"] >= 85:
        verdict = "✅ System is SAFE for deployment."

    elif report["overall_score"] >= 60:
        verdict = "⚠️ System requires additional monitoring."

    else:
        verdict = "❌ System is NOT safe for deployment."

    story.append(
        Paragraph(verdict, normal)
    )

    story.append(Spacer(1, 20))

    # =====================================
    # FOOTER
    # =====================================

    story.append(
        Paragraph(
            "<b>Generated Automatically by SentinelAI v1.0</b>",
            normal
        )
    )

    doc.build(story)

    return filename