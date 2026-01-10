# LLM QA Automation – Context Conflict Detection

A mini Python framework for evaluating language model behavior with a focus on detecting **context conflicts** in multi-turn inputs.

This project demonstrates a practical approach to **LLM evaluation, AI/LLM Quality Assurance, and automated regression testing**.

## What this project does

- Detects contradictory numerical information across user statements (context conflicts)
- Runs automated test cases defined in CSV files
- Generates regression test results in CSV format
- Uses a modular design that separates logic, input/output, and execution

## Example test scenario

The system detects inconsistencies such as:
- "I have three cats."
- "I only have two animals."

Expected result: `FAIL` (context conflict)

## How it works (step by step)

1. Test cases are defined in a CSV file (`test_cases.csv`), including:
   - test ID
   - test type
   - two context statements
   - expected result (PASS / FAIL)

2. The program loads all test cases from the CSV file.

3. For each test case, the system:
   - extracts numerical information from both context statements,
   - normalises numbers (e.g., "two" → 2, "10" → 10),
   - compares all detected values.

4. If more than one unique numerical value is found, the test is marked as:
   - `FAIL` → context conflict detected  
   Otherwise:
   - `PASS` → context is consistent.

5. The actual result is compared with the expected result from the test case.

6. A regression report is generated and saved to a CSV file, allowing repeated evaluation of the same scenarios over time.

## How to run

From the project root directory:
python -m src.main

After execution, results are saved to a CSV file for further inspection and analysis.

## Core functions explained

### detect_context_conflict(context)

This function is responsible for detecting contradictory numerical information in a list of user statements.

**What it does:**
- Iterates over each sentence in the provided context.
- Splits sentences into words.
- Attempts to extract numbers in two ways:
  - Direct integers (e.g., "3", "10")
  - Written numbers using the `word2number` library (e.g., "two", "five")
- Stores all detected numbers in a list.
- Compares unique values:
  - If more than one unique number exists → returns `FAIL`
  - Otherwise → returns `PASS`

This simulates a simplified form of model behavior validation, where internal consistency of user-provided information is tested.

---

### load_test_cases(path)

This function loads structured test cases from a CSV file.

**What it does:**
- Opens the CSV file using `DictReader`.
- Converts each row into a dictionary with:
  - test ID
  - test type
  - context statements
  - expected outcome
- Returns a list of test case objects.

This allows scalable test design without modifying the code when adding new test cases.

---

### test_run(test_cases)

This function executes the regression suite.

**What it does:**
- Iterates over all test cases.
- Applies `detect_context_conflict()` to each context.
- Compares the returned result with the expected value.
- Assigns a status:
  - "Test Case Passed"
  - "Test Case Failed. Correct answer: `<expected>`"
- Collects all results into a structured list for reporting.

This simulates automated evaluation of system behavior.

---

### save_results(path, test_results)

This function generates the regression report.

**What it does:**
- Writes a CSV file containing:
  - test ID
  - test type
  - actual result
  - expected result
  - pass/fail status
- Enables later analysis, comparison between runs, and tracking of regressions.

---

## Why this matters

This project reflects real-world challenges in testing AI systems, including:
- Model behavior evaluation
- Structured test design
- Automated regression testing
- Result reporting for analysis
- Maintainable and extensible architecture

It demonstrates hands-on skills relevant to:
- AI / LLM QA
- Model Evaluation
- Trust & Safety
- QA Automation for AI systems

---

## Future improvements

- Additional test categories (hallucinations, safety, refusal handling)
- SQL-based analysis of test results
- Integration with real LLM APIs for live evaluation

---

## Author

Created as a portfolio project focused on practical LLM evaluation and AI quality assurance.



