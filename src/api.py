import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from src.evaluator import detect_context_conflict
from src.judge import llm_judge


app = FastAPI()

class EvaluateRequest(BaseModel):
    context: list[str]
    expected: str | None = None


@app.post("/evaluate")
def evaluate(req: EvaluateRequest):
    result = detect_context_conflict(req.context)

    if(req.expected is not None):

        if req.expected.lower() == result.lower():
            return {
                "result": result,
                "expected": req.expected,
                "match": True
            } 
        
        llm_agrees, llm_comment = llm_judge(req.context, result) 
        return {
                "result": result,
                "expected": req.expected,
                "match": False,
                "llm_agrees": llm_agrees,
                "llm_comment": llm_comment
            }
    
    return {"result": result}

@app.get("/health")
def health(): 
    return {
        "status" : "ok"
    }

@app.get("/stats")
def stats():
    df = pd.read_csv("data/analyzed_results.csv")
    errors = df[df["result"] != df["expected"]]
    total_tests = len(df)
    error_rate = len(errors)/total_tests * 100 if total_tests > 0 else 0
    false_positives = len(
        df[(df["result"] == "FAIL") & (df["expected"] == "PASS")]
        )
    false_negatives = len(
        df[(df["result"] == "PASS") & (df["expected"] == "FAIL")]
    )


    return {
        "total_tests" : total_tests,
        "error_rate" : round(error_rate, 2),
        "false_positives" : false_positives,
        "false_negatives" : false_negatives
    }
