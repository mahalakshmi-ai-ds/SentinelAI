import re

PROMPT_INJECTION_PATTERNS = {
    r"ignore\s+all\s+previous\s+instructions": 40,
    r"ignore\s+previous\s+instructions": 30,
    r"forget\s+everything": 20,
    r"system\s+prompt": 25,
    r"developer\s+message": 25,
    r"reveal\s+your\s+instructions": 35,
    r"act\s+as": 15,
    r"pretend\s+to\s+be": 15,
    r"override": 20,
    r"bypass": 20,
    r"disable\s+safety": 35,
    r"jailbreak": 40,
    r"do\s+anything\s+now": 40,
    r"\bdan\b": 40,
}


def detect_prompt_injection(prompt: str):

    prompt_lower = prompt.lower()

    matches = []
    confidence = 0

    for pattern, weight in PROMPT_INJECTION_PATTERNS.items():

        if re.search(pattern, prompt_lower):
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
        threat = "Safe"

    return {
        "threat": threat,
        "confidence": confidence,
        "matches": matches
    }