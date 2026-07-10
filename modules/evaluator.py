from modules.sss_calculator import calculate_sss
from modules.risk_analyzer import analyze_risk


def evaluate(report):

    score = calculate_sss(report)

    risk = analyze_risk(score)

    return {
        "sss": score,
        "risk": risk
    }