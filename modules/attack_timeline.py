def build_timeline(analysis):

    timeline = []

    timeline.append({
        "stage": "Prompt Received",
        "threat": "Safe"
    })

    timeline.append({
        "stage": "Prompt Injection Scan",
        "threat": analysis["prompt_injection"]["threat"]
    })

    timeline.append({
        "stage": "Jailbreak Scan",
        "threat": analysis["jailbreak"]["threat"]
    })

    timeline.append({
        "stage": "Prompt Leakage Scan",
        "threat": analysis["prompt_leakage"]["threat"]
    })

    timeline.append({
        "stage": "Role Override Scan",
        "threat": analysis["role_override"]["threat"]
    })

    timeline.append({
        "stage": "Final Risk Assessment",
        "threat": analysis["overall_threat"]
    })

    return timeline