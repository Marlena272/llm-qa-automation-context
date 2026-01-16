from io_utils import load_test_cases, save_results
from evaluator import test_run
from analyze_results import analyze
  
print("=== MINI REGRESSION SUITE ===")

test_cases = load_test_cases("data/test_cases.csv")
test_results = test_run(test_cases)
save_results("data/test_results.csv",test_results)
analyze("data/test_cases.csv", "data/test_results.csv")