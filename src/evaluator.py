from word2number import w2n

def detect_context_conflict(context):
    numbers = []

    for sentence in context:
        for word in sentence.split():
            try:
                number = int(word)
                numbers.append(number)
            except ValueError:
                try:
                    number = w2n.word_to_num(word.lower())
                    numbers.append(number)
                except ValueError:
                    pass

    if len(set(numbers)) > 1:
        return "FAIL"
    else:
        return "PASS"


def test_run(test_cases):
    test_results = []

    for tc in test_cases:
        result = detect_context_conflict(tc["context"])

        if result == tc["expected"]:
            status = "Test Case Passed"
            print("Result:", tc["id"], "->", result, "Test Case Passed")
        else:
            status = "Test Case Failed. Correct answer: " + str(tc["expected"])
            print("Result:", tc["id"], "->", result,
                  "Test Case Failed. Correct answer:", tc["expected"])

        test_results.append([tc["id"], tc["type"], result, tc["expected"], status])

    return test_results
