def analyze_risk(score):

    if score >= 90:
        return "Low"

    elif score >= 70:
        return "Medium"

    elif score >= 50:
        return "High"

    else:
        return "Critical"