from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak
)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.pdfbase.pdfmetrics import stringWidth


# -------------------------------------------------
# Footer
# -------------------------------------------------

def add_footer(canvas, doc):

    canvas.saveState()

    canvas.setFont("Helvetica", 9)

    page = canvas.getPageNumber()

    canvas.drawString(
        40,
        30,
        "SentinelAI v2.0 • Confidential"
    )

    canvas.drawRightString(
        560,
        30,
        f"Page {page}"
    )

    canvas.restoreState()


# -------------------------------------------------
# Main PDF
# -------------------------------------------------

def create_pdf_v2(report, filename):

    doc = SimpleDocTemplate(
        filename,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=50
    )

    styles = getSampleStyleSheet()

    title = styles["Title"]
    title.alignment = TA_CENTER
    title.textColor = HexColor("#0B5394")

    heading = styles["Heading2"]

    normal = styles["BodyText"]

    story = []

    # ======================================================
    # COVER PAGE
    # ======================================================

    story.append(Spacer(1,120))

    story.append(
        Paragraph(
            "🛡 <b>SentinelAI</b>",
            title
        )
    )

    story.append(Spacer(1,25))

    story.append(
        Paragraph(
            "<b>AI Security Assessment Report</b>",
            heading
        )
    )

    story.append(Spacer(1,40))

    story.append(
        Paragraph(
            f"<b>Generated:</b> {report.get('generated_on','N/A')}",
            normal
        )
    )

    story.append(
        Paragraph(
            "<b>Version:</b> 2.0",
            normal
        )
    )

    story.append(
        Paragraph(
            "<b>Prepared By:</b> SentinelAI Digital Immune System",
            normal
        )
    )

    story.append(Spacer(1,180))

    story.append(
        Paragraph(
            "<i>CONFIDENTIAL AI SECURITY REPORT</i>",
            normal
        )
    )

    story.append(PageBreak())

    # ======================================================
    # EXECUTIVE SUMMARY
    # ======================================================

    story.append(
        Paragraph(
            "Executive Summary",
            heading
        )
    )

    story.append(Spacer(1,15))

    story.append(
        Paragraph(
            "SentinelAI performed an AI Prompt Security Assessment "
            "using multiple security detectors and MITRE ATLAS mapping.",
            normal
        )
    )

    story.append(Spacer(1,20))

    summary = [

        ["Metric","Result"],

        [
            "Overall Safety Score",
            f"{report.get('overall_score','N/A')}/100"
        ],

        [
            "Risk Level",
            report.get("risk","N/A")
        ],

        [
            "Deployment",
            report.get("deployment","N/A")
        ],

        [
            "Overall Threat",
            report.get("overall_threat","N/A")
        ],

        [
            "Prompt Safety Score",
            f"{report.get('prompt_safety_score','N/A')}/100"
        ]

    ]

    table = Table(
        summary,
        colWidths=[220,220]
    )

    table.setStyle(

        TableStyle([

            ("BACKGROUND",(0,0),(-1,0),colors.darkblue),

            ("TEXTCOLOR",(0,0),(-1,0),colors.white),

            ("GRID",(0,0),(-1,-1),1,colors.grey),

            ("BACKGROUND",(0,1),(-1,-1),colors.whitesmoke),

            ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),

            ("BOTTOMPADDING",(0,0),(-1,0),10),

            ("ALIGN",(0,0),(-1,-1),"CENTER")

        ])

    )

    story.append(table)

    story.append(PageBreak())

    # ======== PART 2 STARTS HERE ========
    # ======================================================
    # THREAT ANALYSIS
    # ======================================================

    story.append(
        Paragraph(
            "Threat Analysis",
            heading
        )
    )

    story.append(Spacer(1, 15))

    analysis = report.get("analysis", {})

    threat_data = [

        ["Detector", "Threat", "Confidence"],

        [
            "Prompt Injection",
            analysis.get("prompt_injection", {}).get("threat", "N/A"),
            f"{analysis.get('prompt_injection', {}).get('confidence', 0)}%"
        ],

        [
            "Jailbreak",
            analysis.get("jailbreak", {}).get("threat", "N/A"),
            f"{analysis.get('jailbreak', {}).get('confidence', 0)}%"
        ],

        [
            "Prompt Leakage",
            analysis.get("prompt_leakage", {}).get("threat", "N/A"),
            f"{analysis.get('prompt_leakage', {}).get('confidence', 0)}%"
        ],

        [
            "Role Override",
            analysis.get("role_override", {}).get("threat", "N/A"),
            f"{analysis.get('role_override', {}).get('confidence', 0)}%"
        ]

    ]

    threat_table = Table(
        threat_data,
        colWidths=[180, 120, 120]
    )

    threat_table.setStyle(

        TableStyle([

            ("BACKGROUND", (0,0), (-1,0), colors.darkblue),

            ("TEXTCOLOR", (0,0), (-1,0), colors.white),

            ("GRID", (0,0), (-1,-1), 1, colors.black),

            ("BACKGROUND", (0,1), (-1,-1), colors.beige),

            ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),

            ("BOTTOMPADDING", (0,0), (-1,0), 10),

            ("ALIGN", (0,0), (-1,-1), "CENTER")

        ])

    )

    story.append(threat_table)

    story.append(PageBreak())

    # ======================================================
    # MITRE ATLAS INTELLIGENCE
    # ======================================================

    story.append(
        Paragraph(
            "MITRE ATLAS Intelligence",
            heading
        )
    )

    story.append(Spacer(1, 15))

    mitre_rows = [

        [
            "Technique ID",
            "Technique",
            "Description"
        ]

    ]

    for attack in report.get("mitre", []):

        mitre_rows.append([

            attack.get("id", ""),

            attack.get("name", ""),

            attack.get("description", "")

        ])

    if len(mitre_rows) == 1:

        mitre_rows.append([
            "-",
            "No Techniques Detected",
            "-"
        ])

    mitre_table = Table(
        mitre_rows,
        colWidths=[90,150,220]
    )

    mitre_table.setStyle(

        TableStyle([

            ("BACKGROUND",(0,0),(-1,0),colors.darkgreen),

            ("TEXTCOLOR",(0,0),(-1,0),colors.white),

            ("GRID",(0,0),(-1,-1),1,colors.black),

            ("BACKGROUND",(0,1),(-1,-1),colors.whitesmoke),

            ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),

            ("BOTTOMPADDING",(0,0),(-1,0),10),

            ("VALIGN",(0,0),(-1,-1),"TOP")

        ])

    )

    story.append(mitre_table)

    story.append(PageBreak())

    # ======================================================
    # ATTACK TIMELINE
    # ======================================================

    story.append(
        Paragraph(
            "Attack Timeline",
            heading
        )
    )

    story.append(Spacer(1,15))

    timeline = report.get("timeline", [])

    if len(timeline) == 0:

        story.append(
            Paragraph(
                "No attack timeline available.",
                normal
            )
        )

    else:

        for event in timeline:

            story.append(

                Paragraph(
                    f"• {event}",
                    normal
                )

            )

            story.append(
                Spacer(1,8)
            )

    story.append(PageBreak())

    # ======== PART 3 STARTS HERE ========
    # ======================================================
    # RISK ASSESSMENT
    # ======================================================

    story.append(
        Paragraph(
            "Overall Risk Assessment",
            heading
        )
    )

    story.append(Spacer(1, 15))

    risk = report.get("risk", "Unknown")
    threat = report.get("overall_threat", "Unknown")

    story.append(
        Paragraph(
            f"<b>Risk Level:</b> {risk}",
            normal
        )
    )

    story.append(
        Paragraph(
            f"<b>Overall Threat:</b> {threat}",
            normal
        )
    )

    story.append(Spacer(1, 20))

    # ======================================================
    # SECURITY RECOMMENDATIONS
    # ======================================================

    story.append(
        Paragraph(
            "Security Recommendations",
            heading
        )
    )

    story.append(Spacer(1, 10))

    recommendations = [

        "Validate every user prompt before sending it to an LLM.",

        "Enable prompt injection detection before inference.",

        "Protect hidden system prompts from disclosure.",

        "Continuously monitor jailbreak attempts.",

        "Apply human review for High and Critical threats.",

        "Use MITRE ATLAS mapping during security audits.",

        "Maintain prompt logs for forensic investigations.",

        "Re-evaluate prompts before production deployment."

    ]

    for i, rec in enumerate(recommendations, start=1):

        story.append(
            Paragraph(
                f"{i}. {rec}",
                normal
            )
        )

        story.append(
            Spacer(1, 6)
        )

    story.append(PageBreak())

    # ======================================================
    # FINAL SECURITY VERDICT
    # ======================================================

    story.append(
        Paragraph(
            "Final Security Verdict",
            heading
        )
    )

    story.append(Spacer(1, 20))

    score = report.get("overall_score", 0)

    if score >= 90:
        verdict = "✅ APPROVED FOR DEPLOYMENT"

    elif score >= 75:
        verdict = "🟡 APPROVED WITH MONITORING"

    elif score >= 60:
        verdict = "🟠 REQUIRES SECURITY REVIEW"

    else:
        verdict = "🔴 NOT APPROVED FOR DEPLOYMENT"

    story.append(
        Paragraph(
            f"<font size='18'><b>{verdict}</b></font>",
            normal
        )
    )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            f"<b>Overall Safety Score:</b> {score}/100",
            normal
        )
    )

    story.append(
        Paragraph(
            f"<b>Deployment Status:</b> {report.get('deployment','N/A')}",
            normal
        )
    )

    story.append(
        Paragraph(
            f"<b>Risk Level:</b> {risk}",
            normal
        )
    )

    story.append(
        Paragraph(
            "SentinelAI recommends following the security "
            "recommendations listed in this report before "
            "deploying AI applications into production.",
            normal
        )
    )

    story.append(Spacer(1, 40))

    story.append(
        Paragraph(
            "<b>Generated Automatically by SentinelAI v2.0</b>",
            normal
        )
    )

    # ======================================================
    # BUILD PDF
    # ======================================================

    doc.build(
        story,
        onFirstPage=add_footer,
        onLaterPages=add_footer
    )

    return filename