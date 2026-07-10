import re

JAILBREAK_PATTERNS = {
    r"developer mode": 30,
    r"dan mode": 40,
    r"do anything now": 40,
    r"jailbreak": 40,
    r"unrestricted": 25,
    r"ignore openai": 35,
    r"bypass": 20,
    r"no ethical restrictions": 35,
    r"simulate": 15,
    r"pretend": 15,
    r"roleplay": 15,
    r"act without restrictions": 35,
}


def detect_jailbreak(prompt):

    prompt = prompt.lower()

    matches = []
    confidence = 0

    for pattern, weight in JAILBREAK_PATTERNS.items():

        if re.search(pattern, prompt):
            matches.append(pattern)
            confidence += weight

    confidence = min(confidence, 100)

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