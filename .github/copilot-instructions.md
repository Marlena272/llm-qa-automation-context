# LLM QA Automation Context - Copilot Instructions

## Project Overview
This is a mini regression suite for testing LLM QA (Question Answering) automation, specifically focused on detecting context conflicts in generated responses. The system evaluates whether two context sentences contain conflicting numerical information.

## Architecture
- **Simple script-based design**: No complex frameworks, just Python modules in `src/`
- **Data-driven testing**: Test cases loaded from CSV, results saved to CSV
- **Modular components**: Separate modules for I/O, evaluation logic, and orchestration

## Key Components
- `src/main.py`: Entry point that orchestrates loading test cases, running evaluation, and saving results
- `src/evaluator.py`: Contains `test_run()` function and `detect_context_conflict()` logic
- `src/io_utils.py`: CSV loading/saving utilities for test cases and results
- `src/analyze_results.py`: Stub for result analysis (currently just imports pandas)

## Data Formats
### Test Cases (data/test_cases.csv)
```csv
test_id,test_type,context_1,context_2,expected
TC-01,context_conflict,I have three cats.,I only have two animals.,FAIL
```
- `context_1`, `context_2`: Two sentences to check for numerical conflicts
- `expected`: "PASS" (no conflict) or "FAIL" (conflict detected)

### Test Results (data/test_results.csv)
```csv
test_id,test_type,result,expected,status
TC-01,context_conflict,FAIL,FAIL,Test Case Passed
```

## Dependencies
- `word2number`: For parsing written numbers ("three" → 3)
- `pandas`: Imported in analyze_results.py (not currently used)

## Running the Suite
```bash
cd /path/to/project
python src/main.py
```
- Loads test cases from `data/test_cases.csv`
- Runs conflict detection on each case
- Saves results to `data/test_results.csv`
- Prints pass/fail status to console

## Context Conflict Detection Logic
The core algorithm in `detect_context_conflict()`:
1. Split each context sentence into words
2. Try to parse each word as:
   - Integer (direct `int()`)
   - Written number (`w2n.word_to_num()`)
3. Collect all parsed numbers from both sentences
4. If >1 unique numbers found → "FAIL" (conflict)
5. If 0-1 unique numbers → "PASS" (no conflict)

## Adding Test Cases
Add rows to `data/test_cases.csv` following the format above. Examples:
- Conflict: "I have three cats." vs "I only have two animals." → FAIL
- No conflict: "I have one cat." vs "I only have one animal." → PASS

## Development Patterns
- Test cases stored as dicts: `{"id": str, "type": str, "context": [str, str], "expected": str}`
- Results as lists: `[test_id, test_type, result, expected, status]`
- Error handling: Try/except blocks for number parsing (graceful failure on unparseable words)
- Console output: Print results immediately for visibility

## File Structure Conventions
- `src/` for all Python modules
- `data/` for CSV inputs/outputs
- Flat structure, no subpackages
- `__init__.py` present but empty (marks as package)