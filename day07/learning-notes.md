\# Day 7 — Weekly Review and Assessment



\## 1. Objective



Review the foundational concepts learned during the first six days of the Data Engineering apprenticeship and apply them in a practical order-validation pipeline.



\## 2. Data Pipeline Lifecycle



A typical data pipeline follows these stages:



1\. Source — where data originates.

2\. Ingestion — bringing data into the pipeline.

3\. Validation and transformation — checking data quality and preparing records.

4\. Storage — saving processed data.

5\. Consumption — making data available to reports, applications, or analytics.



Rejected records should be preserved with reasons so they can be investigated and potentially reprocessed.



\## 3. Validation vs Transformation



\- Validation checks whether data meets defined rules.

\- Transformation changes data into the required format.



Examples:

\- Checking whether an order ID exists: validation.

\- Rejecting a negative amount: validation.

\- Converting `"500"` into integer `500`: transformation.

\- Trimming unnecessary spaces from a customer name: transformation.



\## 4. Raw, Valid, and Rejected Data



\- Raw data preserves the original input.

\- Valid data contains records that pass the required rules.

\- Rejected data contains records that fail validation, together with their rejection reasons.



Preserving raw data can support investigation and reprocessing when rules change. Retention must still respect privacy and data-retention requirements.



\## 5. Duplicate Detection and Idempotency



A Python set can track IDs already encountered during one program run.



However, an in-memory set is lost when the program restarts. Production systems need durable duplicate protection, such as database uniqueness constraints and clearly defined handling for duplicate records.



Idempotency means that replaying the same operation does not create unintended duplicate effects.



\## 6. Checkpointing and Recovery



A checkpoint records progress so a pipeline can resume after a failure.



Checkpoints must represent successfully committed work. If a pipeline crashes after saving data but before updating its checkpoint, replay may process the same records again. Idempotency and durable constraints help prevent duplicate effects.



\## 7. Data Quality Metrics



For this assessment:



\- Total orders: 5

\- Valid orders: 1

\- Rejected orders: 4

\- Rejection rate: 80%

\- Count consistency: PASS



Count consistency checks:



Total orders = Valid orders + Rejected orders



For the sample:



5 = 1 + 4



Rejection rate:



Rejected orders / Total orders × 100



4 / 5 × 100 = 80%



\## 8. Logging and Monitoring



\- Logging records events and details useful for investigating individual failures.

\- Monitoring tracks pipeline health and trends, such as rising rejection rates or repeated failures.



A sudden increase in rejected records should trigger investigation of the source data, validation rules, schema changes, and recent pipeline changes.



\## 9. Retry and Reliability Principles



\- Retry temporary failures, such as some network timeouts, using a bounded retry policy.

\- Use backoff between attempts to avoid overwhelming a failing service.

\- Do not blindly retry permanent validation failures.

\- Record useful error details for investigation.



\## 10. Assessment Deliverable



File: `weekly\_assesment.py`



The program:

\- Detects duplicate order IDs.

\- Validates customer names.

\- Validates and converts amounts.

\- Separates valid and rejected records.

\- Stores rejection reasons.

\- Calculates the rejection rate.

\- Checks count consistency.



\## 11. Improvements to Make Later



\- Handle missing order IDs without crashing.

\- Prevent fractional amounts from being silently truncated by `int()`.

\- Add automated tests for valid records, invalid records, and edge cases.

\- Preserve original raw input separately from transformed data.

\- Use database constraints and durable checkpoints in production pipelines.



\## 12. Weekly Learning Outcome



I practised Python collections, validation, exception handling, logging concepts, duplicate detection, data-quality metrics, and Git version control. I also learned that a successful script is not automatically production-ready: reliability, edge cases, observability, and recovery need deliberate design.



