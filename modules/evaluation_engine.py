import json
import os

from modules.prompt_engine import analyze_prompt


def evaluate_dataset(folder="evaluation"):

    results = []

    files = [
        "safe_prompts.json",
        "prompt_injection.json",
        "jailbreak.json",
        "prompt_leakage.json",
        "role_override.json"
    ]

    for filename in files:

        path = os.path.join(folder, filename)

        with open(path, "r") as f:
            prompts = json.load(f)

        correct = 0

        total = len(prompts)

        for item in prompts:

            prompt = item["prompt"]

            expected = item["expected"]

            analysis = analyze_prompt(prompt)

            prediction = analysis["overall_threat"]

            if expected == "Safe":

                if prediction == "Safe":
                    correct += 1

            else:

                if prediction != "Safe":
                    correct += 1

        accuracy = round(correct / total * 100, 2)

        results.append({

            "dataset": filename,

            "accuracy": accuracy,

            "correct": correct,

            "total": total

        })

    return results