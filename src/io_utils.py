import csv

def load_test_cases(path):
    test_cases = []

    with open(path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            test_case = {
                "id": row["test_id"],
                "type": row["test_type"],
                "context": [row["context_1"], row["context_2"]],
                "expected": row["expected"]
            }
            test_cases.append(test_case)

    return test_cases


def save_results(path, test_results):
    with open(path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["test_id", "test_type", "result", "expected", "status"])

        for row in test_results:
            writer.writerow(row)
