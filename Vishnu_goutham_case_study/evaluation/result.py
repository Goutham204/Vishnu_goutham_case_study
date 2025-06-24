def evaluate(predictions):
    correct = 0
    total = len(predictions)

    for p in predictions:
        if p["expected_route"] == p["actual_route"]:
            correct += 1

    return {
        "accuracy": correct / total,
        "total_cases": total,
        "correct": correct
    }

if __name__ == "__main__":
    dummy_predictions = [
        {"expected_route": "product", "actual_route": "product"},
        {"expected_route": "support", "actual_route": "engineering"},
        {"expected_route": "support", "actual_route": "support"}
    ]
    print(evaluate(dummy_predictions))
