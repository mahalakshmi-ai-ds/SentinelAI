from datetime import datetime

from modules.prompt_engine import analyze_prompt


def monitor_prompt(prompt):

    result = analyze_prompt(prompt)

    return {
        "timestamp": datetime.now().strftime("%H:%M:%S"),
        "overall": result["overall_threat"],
        "score": result["prompt_safety_score"],
        "analysis": result
    }