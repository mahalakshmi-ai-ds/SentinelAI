from modules.prompt_injection import detect_prompt_injection
from modules.jailbreak_detector import detect_jailbreak
from modules.prompt_leakage import detect_prompt_leakage
from modules.role_override import detect_role_override


def analyze_prompt(prompt):

    injection = detect_prompt_injection(prompt)
    jailbreak = detect_jailbreak(prompt)
    leakage = detect_prompt_leakage(prompt)
    role = detect_role_override(prompt)

    detectors = [
        injection,
        jailbreak,
        leakage,
        role
    ]

    confidence = max(
        detector["confidence"]
        for detector in detectors
    )

    if confidence >= 80:
        overall = "Critical"

    elif confidence >= 60:
        overall = "High"

    elif confidence >= 30:
        overall = "Medium"

    elif confidence > 0:
        overall = "Low"

    else:
        overall = "Safe"

    safety_score = 100 - confidence

    return {

        "overall_threat": overall,

        "prompt_safety_score": safety_score,

        "prompt_injection": injection,

        "jailbreak": jailbreak,

        "prompt_leakage": leakage,

        "role_override": role

    }