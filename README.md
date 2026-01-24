# LLM Evaluation & QA Automation

This repository contains my practical work in **LLM testing, evaluation, and AI quality assurance**.
The main focus is on building realistic evaluation pipelines that combine deterministic rules with
LLM-based judgment for auditing and explainability.

---

### ✅ What has been implemented

I designed and implemented an **end-to-end LLM evaluation and QA automation pipeline**.
The system evaluates a rule-based decision mechanism and audits its failures using a
Large Language Model acting as an **independent judge**.

The project evolved from a simple rule-based script into a **modular, production-style evaluation system**
with both **batch processing and REST API interfaces**.

In addition to batch regression, the system now exposes evaluation and monitoring
capabilities via a FastAPI-based REST API and is tested using Postman.


## 🧱 Architecture & Structure

The project follows a clear separation of concerns:

- **`main.py`**  
  It is responsible for running the entire batch evaluation pipeline
  and triggering analysis and PDF report generation.

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
  and LLM explanations for stakeholders.

- **FastAPI REST API (`api.py`)**  
  Provides a production-style interface for:
  - real-time evaluation of new inputs,
  - exposing evaluation and quality metrics via dedicated endpoints.


## 🌐 REST API & Monitoring Layer

The project includes a FastAPI-based REST API that exposes evaluation logic and quality metrics.

Key endpoints:

- **POST `/evaluate`**  
  Evaluates a given context in real time and optionally compares it with an expected result.
  Returns:
  - rule-based decision,
  - match status,
  - optional LLM judge feedback for incorrect cases.

- **GET `/stats`**  
  Exposes evaluation quality metrics calculated with pandas, including:
  - total number of tests,
  - overall error rate,
  - false positives,
  - false negatives.

This allows the evaluation system to be used not only in batch mode,
but also as a **service for monitoring and integration with other systems**.


## 🧪 API Testing with Postman

The REST API is tested using Postman with structured collections covering:

- positive (happy path) scenarios,
- negative scenarios (validation errors, missing fields),
- edge cases,
- contract validation (response structure and data types),
- business logic validation (e.g. error rate boundaries).

This demonstrates practical **API QA testing** and contract-based validation.


## 📊 Outputs

The pipeline generates multiple artefacts:

- `test_results.csv` – raw evaluation results  
- `analyzed_results.csv` – enriched results with metrics and LLM feedback  
- `llm_results_report.pdf` – final automated PDF evaluation report for human stakeholders  

This demonstrates how LLM evaluation can be integrated into **realistic QA workflows**,
including automated reporting for technical and non-technical audiences.

## 🎯 Key Design Decisions

- Clear separation between **rule-based logic** and **LLM-based judgment**
- LLM used for **auditing and explainability**, not decision control
- Cost-aware design (LLM invoked only on failures)
- Batch + REST API architecture
- Automated monitoring of evaluation quality via API
- Outputs designed for both **technical and non-technical stakeholders**
- Modular structure inspired by real-world QA and evaluation pipelines

## 🚀 Skills Demonstrated

- LLM evaluation and testing
- LLM as a Judge pattern
- AI quality assurance
- Error analysis with pandas
- REST API design with FastAPI
- API functional and contract testing with Postman
- Modular Python application design
- Automated PDF report generation
- Production-oriented thinking beyond notebooks
