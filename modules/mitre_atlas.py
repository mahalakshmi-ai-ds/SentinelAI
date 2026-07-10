MITRE_ATTACKS = {
    "Prompt Injection": {
        "id": "AML.T0051",
        "name": "Prompt Injection",
        "description": "Attempts to manipulate an AI system using malicious prompts."
    },

    "Jailbreak": {
        "id": "AML.T0015",
        "name": "Safety Bypass",
        "description": "Attempts to bypass AI safety mechanisms."
    },

    "Prompt Leakage": {
        "id": "AML.T0048",
        "name": "Prompt Extraction",
        "description": "Attempts to reveal hidden prompts or system instructions."
    },

    "Role Override": {
        "id": "AML.T0026",
        "name": "Identity Manipulation",
        "description": "Attempts to change the AI's assigned identity or role."
    }
}


def map_attacks(analysis):

    findings = []

    if analysis["prompt_injection"]["confidence"] > 0:
        findings.append(MITRE_ATTACKS["Prompt Injection"])

    if analysis["jailbreak"]["confidence"] > 0:
        findings.append(MITRE_ATTACKS["Jailbreak"])

    if analysis["prompt_leakage"]["confidence"] > 0:
        findings.append(MITRE_ATTACKS["Prompt Leakage"])

    if analysis["role_override"]["confidence"] > 0:
        findings.append(MITRE_ATTACKS["Role Override"])

    return findings