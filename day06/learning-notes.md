# Day 6 — Reliable Data Pipelines and Data Validation

## 1. Objective

Learn how to validate incoming data, separate valid and rejected records, handle errors safely, and monitor pipeline results using logging and basic metrics.

## 2. Raw Data vs. Validated Data

* **Raw data:** Data received from a source before validation or transformation.
* **Validated data:** Data that has passed the required quality checks.
* **Rejected data:** Data that fails validation and is stored with reasons for rejection.

Rejected records should be preserved so they can be investigated and corrected later.

## 3. Data Validation

Validation checks whether incoming records satisfy the expected rules.

In my Python pipeline, I validated:

* Order ID availability.
* Customer name availability and blank values.
* Amount availability.
* Amount data type.
* Negative amounts.

Examples of validation outcomes:

| Input problem     | Rejection reason                 |
| ----------------- | -------------------------------- |
| Missing amount    | `Missing amount`                 |
| Amount is `"abc"` | `Amount must be a valid integer` |
| Amount is `-200`  | `Amount must be zero or greater` |
| Customer is blank | `Missing or blank customer`      |

## 4. Type Conversion and Exception Handling

An API may return a numeric value as an integer (`500`) or a numeric string (`"500"`).

Python's `int()` can convert a valid integer string into an integer.

The `try` and `except` statements help handle conversion errors such as `ValueError`. A conversion failure should result in a rejected record with a clear reason rather than crashing the entire pipeline.

The conversion method must match the expected data contract. Integer conversion is suitable only when amounts are expected to be whole numbers.

## 5. Accepted and Rejected Records

I used two lists:

* `valid_orders` to store accepted records.
* `rejected_orders` to store rejected records and their reasons.

A `reasons` list collects validation failures for each order. If the list contains reasons, the record is rejected; otherwise, it is accepted.

## 6. Logging

Python's `logging` module records pipeline events.

* `INFO`: Records successful processing events.
* `WARNING`: Records records that were rejected or need attention.

Logging helps developers understand pipeline behavior without relying only on printed data.

## 7. Pipeline Count Consistency

I checked whether every input record was accounted for:

`Total orders = Valid orders + Rejected orders`

If this condition is true, the count check reports `PASS`. Otherwise, it reports `FAIL`.

This is a basic consistency check; it does not prove that every validation rule is correct.

## 8. Rejection Rate

The rejection rate measures the percentage of input records that were rejected:

`Rejection rate = (Rejected orders / Total orders) × 100`

For my three-record test:

* Total orders: 3
* Valid orders: 1
* Rejected orders: 2
* Rejection rate: 66.67%

A sudden increase in the rejection rate can indicate a source-data problem, an API change, or an overly strict validation rule.

## 9. SQL Data Quality Checks

I practised SQL queries to identify:

* Orders with negative amounts.
* Orders with missing or blank customer names.
* Orders with missing amounts.
* The count of orders matching a condition.

I learned that `IS NULL` checks for SQL NULL values, while `TRIM(customer) = ''` detects empty or whitespace-only customer names.

## 10. Real-World Application

If an API changes the type of a field, a data engineer should investigate the source change, preserve rejected records, assess the impact, correct and test the parsing logic, and reprocess affected records safely.

Retries are appropriate for certain temporary failures, but invalid data generally needs investigation or correction.

## 11. Key Lessons

* Validate data before allowing it into downstream processing.
* Record clear rejection reasons.
* Handle expected exceptions instead of allowing one bad record to stop the entire pipeline.
* Preserve rejected records for investigation and recovery.
* Use logging and metrics to monitor pipeline behavior.
* Check count consistency.
* Investigate unusual rejection-rate increases.
* Test multiple input cases before considering validation logic complete.

## 12. Day 6 Status

Completed practice exercises for data validation, error handling, logging, rejection-rate calculation, count consistency, and SQL data quality checks.

The work was tested using valid orders, missing amounts, invalid amount strings, negative amounts, and blank customer names.
