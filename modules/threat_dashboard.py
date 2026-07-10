def get_dashboard_data():

    return {
        "total_prompts": 128,
        "safe_prompts": 91,
        "blocked_prompts": 37,
        "average_score": 84,
        "top_attack": "Prompt Injection",

        "distribution": {
            "Safe": 91,
            "Prompt Injection": 18,
            "Jailbreak": 9,
            "Prompt Leakage": 6,
            "Role Override": 4
        },

        "trend": {
            "09:00": 3,
            "10:00": 7,
            "11:00": 5,
            "12:00": 9,
            "13:00": 6,
            "14:00": 11,
            "15:00": 8
        }
    }