from datetime import datetime

def generate_report(
    pdf_path,
    score,
    risk,
    deployment,
    analysis=None,
    timeline=None,
    mitre=None
):
    if analysis is None:
        analysis = {
            "overall_threat": risk,
            "prompt_safety_score": score
        }

    if timeline is None:
        timeline = []

    if mitre is None:
        mitre = []

    report = f"""
===============================
      SENTINELAI REPORT
===============================

Generated On : {datetime.now().strftime("%d %B %Y %H:%M")}

Safety Score : {score}
Risk Level   : {risk}
Deployment   : {deployment}

Overall Threat :
{analysis['overall_threat']}

Prompt Safety Score :
{analysis['prompt_safety_score']}

===============================
Timeline
===============================

{timeline}

===============================
MITRE Mapping
===============================

{mitre}
"""

    with open(pdf_path, "w", encoding="utf-8") as f:
        f.write(report)

    return report