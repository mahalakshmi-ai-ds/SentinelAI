def generate_explanation(result):

    explanations = []

    if result["prompt_injection"]["threat"] in ["High", "Critical"]:
        explanations.append({
            "title": "Prompt Injection",
            "reason": "The prompt attempts to override previous system instructions.",
            "impact": "The AI could ignore safety constraints and execute unintended behavior.",
            "recommendation": "Reject or sanitize the prompt before inference."
        })

    if result["jailbreak"]["threat"] in ["Medium", "High", "Critical"]:
        explanations.append({
            "title": "Jailbreak Attempt",
            "reason": "The prompt contains jailbreak patterns intended to bypass AI safeguards.",
            "impact": "The model may generate unsafe or policy-violating responses.",
            "recommendation": "Require secondary safety verification before processing."
        })

    if result["prompt_leakage"]["threat"] in ["Medium", "High", "Critical"]:
        explanations.append({
            "title": "Prompt Leakage",
            "reason": "The prompt attempts to reveal hidden system or developer instructions.",
            "impact": "Sensitive prompts or internal policies could be exposed.",
            "recommendation": "Block requests for hidden prompts and log the event."
        })

    if result["role_override"]["threat"] in ["Medium", "High", "Critical"]:
        explanations.append({
            "title": "Role Override",
            "reason": "The prompt attempts to change the AI's intended role or identity.",
            "impact": "Role manipulation can weaken safety behavior and increase security risks.",
            "recommendation": "Ignore role-changing instructions and enforce the original system role."
        })

    return explanations