import re

LEAKAGE_PATTERNS = [

    r"system prompt",

    r"hidden prompt",

    r"developer prompt",

    r"initial instructions",

    r"show your instructions",

    r"reveal your prompt",

    r"print your system prompt",

    r"display hidden instructions",

    r"internal prompt",

    r"configuration"
]


def detect_prompt_leakage(prompt):

    matches = []

    for pattern in LEAKAGE_PATTERNS:

        if re.search(pattern, prompt, re.IGNORECASE):
            matches.append(pattern)

    confidence = min(len(matches) * 25, 100)

    if confidence >= 80:
        threat = "Critical"
    elif confidence >= 60:
        threat = "High"
    elif confidence >= 30:
        threat = "Medium"
    elif confidence > 0:
        threat = "Low"
    else:
        threat = "None"

    return {
        "threat": threat,
        "confidence": confidence,
        "matches": matches
    }