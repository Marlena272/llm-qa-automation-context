# LLM Evaluation & QA Automation

This repository contains my practical work in **LLM testing, evaluation, and AI quality assurance**.
The main focus is on building realistic evaluation pipelines that combine deterministic rules with
LLM-based judgment for auditing and explainability.

---

## 🔄 Project Update – LLM Evaluation Pipeline

### ✅ What has been implemented

I designed and implemented an **end-to-end LLM evaluation and QA automation pipeline**.
The system evaluates a rule-based decision mechanism and audits its failures using a
Large Language Model acting as an **independent judge**.

The project evolved from a simple rule-based script into a **modular, production-style evaluation system**.

---

## 🧱 Architecture & Structure

The project follows a clear separation of concerns:

- **`main.py`**  
  It is responsible for running the entire evaluation pipeline.

- **`io_utils.py`**  
  Utilities for loading test cases from CSV files and saving raw evaluation results.

- **`evaluator.py`**  
  A deterministic, rule-based system designed to detect logical conflicts
  (e.g. numerical inconsistencies across context).

- **`judge.py`**  
  A standalone **LLM-as-a-Judge module** used to audit and explain failures of the rule-based system.  
  The LLM does **not** make decisions — it only evaluates and explains incorrect outcomes.

- **`analyze_results.py`**  
  Analysis layer built with pandas:
  - merges test cases and evaluation results,
  - calculates error rate,
  - identifies risky test types,
  - analyses false positives and false negatives,
  - selectively invokes the LLM judge **only for failed cases**.

- **`to_pdf.py`**  
  Automatically generates a **human-readable PDF report** containing evaluation metrics
  and LLM explanations.

---

## 🧪 Evaluation Logic

- Test cases are loaded from structured CSV files.
- A deterministic rule-based evaluator produces initial PASS / FAIL decisions.
- Errors are analysed quantitatively:
  - overall error rate,
  - false positives,
  - false negatives,
  - distribution of errors by test type.
- Only a limited subset of failed cases is reviewed by an LLM acting as an **independent auditor**.
- LLM responses are constrained to a strict output format
  (`AGREE / DISAGREE + short explanation`) to ensure reliability.

---

## 📊 Outputs

The pipeline generates multiple artefacts:

- `test_results.csv` – raw evaluation results  
- `analyzed_results.csv` – enriched results with metrics and LLM feedback  
- `llm_results_report.pdf` – final evaluation report for human stakeholders  

This demonstrates how LLM evaluation can be integrated into **realistic QA workflows**, not just notebooks.

---

## 🎯 Key Design Decisions

- Clear separation between **rule-based logic** and **LLM-based judgment**
- LLM used for **auditing and explainability**, not decision control
- Cost-aware design (LLM invoked only on failures)
- Outputs designed for both **technical and non-technical stakeholders**
- Modular structure inspired by real-world QA and evaluation pipelines

---

## 🚀 Skills Demonstrated

- LLM evaluation and testing
- LLM as a Judge pattern
- AI quality assurance
- Error analysis with pandas
- Modular Python application design
- Automated PDF report generation
- Production-oriented thinking beyond notebooks
