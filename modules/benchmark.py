from modules.sss_calculator import calculate_sss


def benchmark_models(models):

    results = []

    for model in models:

        score = calculate_sss(model)

        results.append({
            "model": model["model"],
            "score": round(score, 2)
        })

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results