# Day 10 --- Python Logging Pipeline

## 1. Project Overview

This project demonstrates how Python's built-in `logging` module tracks
execution of an order-validation pipeline. The pipeline validates order
records, separates valid orders from rejected orders, and logs important
events at different severity levels. Changing the logging level from
`INFO` to `DEBUG` changes the amount of diagnostic information shown,
not the validation logic.

### Objectives

-   Understand why logging matters in a data pipeline.
-   Learn `DEBUG`, `INFO`, `WARNING`, `ERROR`, and `CRITICAL`.
-   Configure logging with `logging.basicConfig()`.
-   Record timestamps, successful processing, and validation failures.
-   Compare `INFO` and `DEBUG`.
-   Understand exception logging and the limitations of console-only
    logs.

## 2. Project Structure

The example commands below assume this structure. If your actual script
has a different path or filename, update the commands accordingly.

``` text
day10/
├── logging_pipeline.py
└── README.md
```

-   **`logging_pipeline.py`** contains sample data, validation logic,
    logging configuration, and order processing.
-   **`README.md`** documents the purpose, behavior, execution, results,
    and limitations.

## 3. Why Logging Was Added

Logging records events that happen while a program runs. In a data
pipeline, it helps developers track processing, identify rejected
records, investigate errors, and check whether a run completed.

### Benefits

1.  **Monitoring:** Records pipeline start and completion.
2.  **Data quality:** Records validation failures and rejection reasons.
3.  **Debugging:** Reveals details about program execution.
4.  **Error investigation:** Can record exceptions and tracebacks when
    exception logging is implemented.
5.  **Auditing:** Helps review events later when logs are retained.
6.  **Maintainability:** Reduces reliance on temporary `print()`
    statements.

## 4. Sample Input Data

The Python example previously reviewed processes three orders:

``` python
orders = [
    {"order_id": 201, "customer": "Ravi", "price": 200, "quantity": 2},
    {"order_id": 202, "customer": "Priya", "quantity": 3},
    {"order_id": 203, "customer": "Arjun", "price": "unknown", "quantity": 1},
]
```

Required fields are `order_id`, `customer`, `price`, and `quantity`.

### Validation rules

-   The record must be a dictionary.
-   All required fields must be present.
-   `customer` must be a non-empty string.
-   `order_id` must be a positive integer.
-   `price` must be numeric, finite, and not negative.
-   `quantity` must be a positive integer.

**Important:** The current Python code allows a price of zero because it
rejects only `price < 0`. If the business rule requires a strictly
positive price, update the code and this documentation together.

### Expected results

    Order ID Issue                    Result     Reason
  ---------- ------------------------ ---------- -------------------------------
         201 All fields valid         Accepted   Total = 200 × 2 = 400
         202 `price` missing          Rejected   Missing required field: price
         203 `price` is `"unknown"`   Rejected   Price must be numeric

Expected totals: **3 processed, 1 accepted, 2 rejected**.

## 5. Logging Configuration

The reviewed code configures logging like this:

``` python
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
```

To see DEBUG messages, change `level=logging.INFO` to
`level=logging.DEBUG` and run the script again.

-   **`level`** sets the minimum severity threshold.
-   **`format`** controls the structure of each log message.
-   **`%(asctime)s`** is the timestamp.
-   **`%(levelname)s`** is the severity name.
-   **`%(message)s`** is the log message.

Because no filename is specified, logging normally writes to the
console. `filename=None` is unnecessary. `logging.basicConfig()`
normally does not reconfigure the root logger if handlers already exist;
`force=True` can replace them, but should be used deliberately.

## 6. Logging Severity Levels

Severity increases in this order:

``` text
DEBUG < INFO < WARNING < ERROR < CRITICAL
```

### DEBUG

Detailed diagnostic messages, such as identifying which order is
currently being validated.

``` python
logging.debug("Validating order %s", order_id)
```

### INFO

Normal progress, such as pipeline startup, number of orders received,
accepted orders, final counts, and completion.

### WARNING

An undesirable but recoverable condition. An invalid order can be logged
as a warning while the pipeline continues processing other orders.

``` python
logging.warning("Order %s rejected: %s", order_id, reason)
```

### ERROR

An operation failed and needs investigation, such as a failed database
write. Logging an error does not automatically raise an exception,
retry, or stop the program.

### CRITICAL

A severe problem that may prevent the application from continuing, such
as the loss of a required service with no safe recovery path.

## 7. INFO vs DEBUG

The previously reviewed code changes the logging level in
`basicConfig()`; it does **not** use a `--log-level` command-line
argument unless you add argument-parsing code.

  Behavior                                  INFO        DEBUG
  ----------------------------------------- ----------- -----------
  Pipeline startup                          Visible     Visible
  Number of input orders (logged at INFO)   Visible     Visible
  Accepted-order messages                   Visible     Visible
  Rejection warnings                        Visible     Visible
  Per-order validation messages             Hidden      Visible
  Final counts                              Visible     Visible
  Processing logic and results              Unchanged   Unchanged

At `INFO`, DEBUG messages are filtered out. At `DEBUG`, DEBUG and
higher-severity messages are eligible to be emitted. Handler
configuration and filters can also affect what is ultimately displayed.

## 8. Exception Logging

`logging.exception()` records a message at ERROR level and includes
information about the active exception, including its traceback. It is
normally used inside an `except` block.

``` python
try:
    result = 100 / 0
except ZeroDivisionError:
    logging.exception("Calculation failed")
```

A traceback helps locate where an exception occurred and shows the call
sequence leading to it.

**Implementation note:** The Python code previously reviewed did not
contain a `logging.exception()` branch. The example above explains the
concept separately; do not claim exception logging is implemented in the
pipeline unless you add and test it. Expected validation failures should
normally be recorded as rejection warnings.

## 9. Results and Output Analysis

For the sample data, expected results are:

``` text
Valid orders: 1
Rejected orders: 2
```

-   **Accepted:** Order 201, total 400.
-   **Rejected:** Order 202 because `price` is missing.
-   **Rejected:** Order 203 because `price` is not numeric.

The INFO run provides an overview. The DEBUG run adds per-order
validation messages. Both runs should produce the same processing
counts. Run the script to verify the actual output.

## 10. Limitations of Console-Only Logging

-   **No dedicated persistent log file:** Output may be lost when the
    terminal closes if it was not saved elsewhere.
-   **Limited historical investigation:** It is harder to compare runs
    without retained logs.
-   **No automatic alerts:** The script does not alert anyone when a
    failure occurs.
-   **No centralized logging:** Logs from different services are not
    automatically collected into one searchable place.
-   **No retention or rotation:** The project does not limit log storage
    or define how long logs are kept.
-   **Sensitive-data risk:** Logs must not expose passwords, access
    tokens, or unnecessary personal information.

### Possible improvements

-   Add a file handler or `filename="pipeline.log"`.
-   Configure console and file handlers if both are needed.
-   Add automated tests for accepted and rejected orders.
-   Consider structured logging for easier searching.
-   Add log rotation and retention policies.
-   Integrate monitoring and alerting.
-   Include useful identifiers, such as a pipeline run ID, without
    exposing sensitive data.

These are future improvements, not features claimed to be implemented in
the current example.

## 11. How to Run the Project

Run commands from the repository root. These examples assume the script
is `day10/logging_pipeline.py`; change the path if needed.

1.  Set `level=logging.INFO`, save the file, and run:

    ``` bash
    python day10/logging_pipeline.py
    ```

2.  Change the level to `logging.DEBUG`, save the file, and run the same
    command again:

    ``` bash
    python day10/logging_pipeline.py
    ```

On Windows, use `py` instead of `python` if necessary.

### Verify

1.  Three orders are processed.
2.  One order is accepted and two are rejected.
3.  INFO messages appear in both runs.
4.  Per-order DEBUG messages appear only in the DEBUG run.
5.  Rejection reasons are correct.
6.  Final counts are unchanged between runs.

## 12. Key Learnings

-   Using Python's built-in logging module.
-   Configuring logging with `basicConfig()`.
-   Understanding severity thresholds and message formatting.
-   Recording accepted orders and validation warnings.
-   Understanding the purpose of exception logging and tracebacks.
-   Comparing INFO and DEBUG output.
-   Applying logging to data-quality monitoring.
-   Recognizing the limitations of console-only logs.

## 13. Conclusion

This project demonstrates how logging improves the visibility and
debuggability of a Python order-validation pipeline. The pipeline
validates sample orders, records accepted and rejected records, explains
rejection reasons, and displays processing counts. Comparing INFO and
DEBUG demonstrates how the logging threshold changes diagnostic detail
without changing the intended processing logic.

These concepts are a foundation for more reliable data pipelines, where
validation, logging, exception handling, monitoring, and recovery help
developers identify and investigate failures.
