import pandas as pd
from judge import llm_judge
from to_pdf import export_to_pdf

def analyze(path_cases, path_results):
    cases_df = pd.read_csv(path_cases)
    results_df = pd.read_csv(path_results)

    df = pd.merge(
        cases_df,
        results_df,
        on="test_id",
        suffixes=("_cases", "_results")
    )

    df["expected"] = df["expected_cases"]
    df["test_type"] = df["test_type_cases"]
    df = df.drop(columns=[
        "expected_cases", "expected_results",
        "test_type_cases", "test_type_results"
    ])

    errors = df[df["result"] != df["expected"]]

    error_rate = len(errors) / len(df)
    print("Error rate:", error_rate)

    risky_types = errors["test_type"].value_counts()
    print("Most common error types: ", risky_types)

    false_positives = errors[(errors["result"] == "FAIL") & (errors["expected"] == "PASS")] #zostaw tylko wiersze, gdzie spełniony jest ten warunek
    print("False Positives:", false_positives)

    false_negatives = errors[(errors["result"] == "PASS") & (errors["expected"] == "FAIL")] #zostaw tylko wiersze, gdzie spełniony jest ten warunek
    print("False Negatives:", false_negatives)

    df["llm_agrees"] = "N/A"
    df["llm_comment"] = "N/A"

    for i, row in errors.head(10).iterrows():
        context = [row["context_1"], row["context_2"]]
        agrees, comment = llm_judge(context, row["result"])
        df.at[i,"llm_agrees"] = agrees
        df.at[i,"llm_comment"] = comment

    df.to_csv("data/analyzed_results.csv", index=False)

    export_to_pdf(df)