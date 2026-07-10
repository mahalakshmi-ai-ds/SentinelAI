import re

ROLE_PATTERNS = [

    r"act as",

    r"pretend to be",

    r"you are now",

    r"from now on",

    r"assume the role",

    r"roleplay",

    r"become",

    r"simulate",

    r"you are no longer",

    r"ignore your identity"
]


def detect_role_override(prompt):

    matches = []

    for pattern in ROLE_PATTERNS:

        if re.search(pattern, prompt, re.IGNORECASE):

            matches.append(pattern)

    confidence = min(len(matches) * 20, 100)

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