import random


def get_monitor_data():

    return {

        "requests": random.randint(1000, 1500),

        "blocked": random.randint(20, 60),

        "safe": random.randint(950, 1450),

        "threat": random.choice([
            "Low",
            "Medium",
            "High"
        ]),

        "events": [

            "Prompt Injection Detected",

            "Safe Prompt",

            "Jailbreak Attempt",

            "Prompt Leakage Attempt",

            "Role Override Blocked"

        ]

    }