
# Day 10 — Python Logging Pipeline

## 1. Project Overview

This project demonstrates how to use Python's built-in `logging` module to track the execution of an order-validation pipeline.

The pipeline processes a list of orders, validates their data, separates valid orders from rejected orders, and records important events using different logging severity levels.

The project also demonstrates how changing the logging level from `INFO` to `DEBUG` affects the amount of information displayed during execution.

### Project Objectives

- Understand why logging is important in Python applications.
- Learn the difference between `DEBUG`, `INFO`, `WARNING`, `ERROR`, and `CRITICAL`.
- Configure logging using `logging.basicConfig()`.
- Include timestamps and severity levels in log messages.
- Record successful operations and validation failures.
- Understand how exception information can be logged.
- Compare program execution at `INFO` and `DEBUG` levels.
- Understand the limitations of console-only logging.
- Apply logging concepts to a simple data-validation pipeline.

---

## 2. Project Structure

```text
day10/
├── logging_pipeline.py
└── README.md
```

### File Descriptions

**logging_pipeline.py**

Contains the order-validation pipeline, logging configuration, sample order data, validation logic, and command-line arguments for selecting the logging level.

**README.md**

Documents the purpose of the project, implementation details, execution instructions, observed results, and limitations.

---

## 3. Why Logging Was Added

Logging is the process of recording events that occur while a program is running.

In a data pipeline, it is important to understand what happened during execution, which records were processed successfully, which records were rejected, and whether unexpected errors occurred.

Without logging, a developer may have difficulty investigating a pipeline failure, especially when processing a large number of records.

For example, if an order contains a negative price, the pipeline should record why that order was rejected.

Logging provides a structured way to record this information.

### Benefits of Logging

1. **Monitoring execution:** Records when the pipeline starts and finishes.
2. **Tracking data quality:** Records validation failures and rejection reasons.
3. **Debugging:** Provides detailed information about program execution.
4. **Error investigation:** Can capture exception messages and tracebacks.
5. **Auditing:** Helps review recorded processing events after execution, provided the logs are retained.
6. **Maintainability:** Makes it easier to understand the behavior of a program without adding many temporary print statements.

In this project, logging is used to record pipeline progress, successful validations, rejected orders, and final processing counts.

---

## 4. Sample Input Data

The pipeline processes five sample orders.

```python
orders = [
    {"order_id": 201, "price": 200, "quantity": 2},
    {"order_id": 202, "price": -50, "quantity": 1},
    {"order_id": 203, "price": 100, "quantity": 3},
    {"order_id": 204, "price": 150, "quantity": 0},
    {"order_id": 205, "price": 80, "quantity": 2},
]
```

Each order contains three fields:

- `order_id`: Identifies the order.
- `price`: Represents the price per unit.
- `quantity`: Represents the number of units ordered.

### Validation Rules

An order is considered valid when:

- It contains an `order_id`.
- It contains a `price`.
- It contains a `quantity`.
- Its price is greater than zero.
- Its quantity is greater than zero.

An order that fails validation is added to the rejected-orders collection.

### Expected Validation Results

| Order ID | Price | Quantity | Result | Reason |
|---|---:|---:|---|---|
| 201 | 200 | 2 | Valid | All checks passed |
| 202 | -50 | 1 | Rejected | Price must be positive |
| 203 | 100 | 3 | Valid | All checks passed |
| 204 | 150 | 0 | Rejected | Quantity must be positive |
| 205 | 80 | 2 | Valid | All checks passed |

The pipeline should process five orders, accept three, and reject two.

---

## 5. Logging Configuration

The project uses Python's built-in `logging` module.

The logging configuration is defined using `logging.basicConfig()`.

```python
logging.basicConfig(
    filename=None,
    level=level,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    force=True,
)
```

The `filename=None` argument is optional and can be omitted. Without a filename, basic logging normally uses a console stream handler.

### Explanation of Configuration Arguments

**level**

Specifies the minimum severity level that the root logger processes.

The project uses either `logging.INFO` or `logging.DEBUG`, depending on the command-line argument.

**format**

Defines the structure of each log message.

The format contains three fields:

- `%(asctime)s`: Timestamp of the log record.
- `%(levelname)s`: Severity level of the message.
- `%(message)s`: The actual log message.

**datefmt**

Defines how the timestamp is displayed.

The format `%Y-%m-%d %H:%M:%S` displays the year, month, day, hour, minute, and second.

**force=True**

Reconfigures the root logger by removing and closing its existing handlers before applying the new configuration. This is useful when running the program repeatedly in environments that may already have configured logging.

---

## 6. Logging Severity Levels

Python provides five standard severity levels.

### 6.1 DEBUG

`DEBUG` is used for detailed diagnostic information.

It helps developers understand the internal execution of a program.

In this project, DEBUG messages record the total number of received orders and the validation step for each order.

Example:

```python
logger.debug("Validating order %s", order_id)
```

This message is useful when investigating how the pipeline processes individual orders.

### 6.2 INFO

`INFO` records normal events that confirm the program is operating as expected.

In this project, INFO messages record:

- Pipeline startup.
- Successful order validation.
- Pipeline completion.
- The final number of valid and rejected orders.

Example:

```python
logger.info("Order %s validated successfully", order_id)
```

INFO messages provide a useful overview of the pipeline's execution.

### 6.3 WARNING

`WARNING` indicates an unexpected or undesirable condition that does not necessarily stop the program.

In this project, invalid prices and quantities are treated as expected data-quality problems.

Example:

```python
logger.warning(
    "Order %s rejected: %s",
    order_id,
    error,
)
```

The warning explains why an order was rejected, while the pipeline continues processing the remaining orders.

### 6.4 ERROR

`ERROR` indicates that an operation has failed and needs investigation.

For example, an unexpected failure during an important processing operation may be recorded at ERROR level.

An error log does not automatically raise an exception or terminate the program.

### 6.5 CRITICAL

`CRITICAL` indicates a severe problem that may prevent the application from continuing.

For example, a pipeline might record a critical event if a required service becomes unavailable and processing cannot continue.

This level is not expected to be triggered by the current sample data.

### Severity Order

```text
DEBUG < INFO < WARNING < ERROR < CRITICAL
```

The levels are ordered by increasing severity.

---

## 7. INFO Level vs DEBUG Level

The project accepts a command-line argument named `--log-level`.

The default level is `INFO`.

### Running at INFO Level

Command:

```bash
python day10/logging_pipeline.py --log-level INFO
```

At INFO level, the pipeline records:

- Startup information.
- Successful validation messages.
- Rejected-order warnings.
- Final processing counts.

Detailed DEBUG messages are filtered out.

### Why DEBUG Is Hidden

The severity value of DEBUG is lower than INFO.

When the logging threshold is INFO, DEBUG messages do not meet the threshold and are filtered out.

This reduces unnecessary diagnostic output during normal execution.

### Running at DEBUG Level

Command:

```bash
python day10/logging_pipeline.py --log-level DEBUG
```

At DEBUG level, the pipeline records:

- The total number of input orders.
- The validation step for each order.
- All INFO-level messages.
- All WARNING-level messages.

ERROR and CRITICAL messages would also be eligible for logging if generated.

### Comparison

| Behavior | INFO | DEBUG |
|---|---|---|
| Pipeline startup | Visible | Visible |
| Successful validations | Visible | Visible |
| Rejection warnings | Visible | Visible |
| Total input count in debug message | Hidden | Visible |
| Individual validation steps | Hidden | Visible |
| Validation results | Same | Same |

The logging level changes the visibility of messages, not the validation rules or final counts.

---

## 8. Exception Logging

Exception logging helps developers investigate unexpected failures.

Python provides `logging.exception()` to record an error message together with information about the active exception, including its traceback.

Example:

```python
try:
    result = 100 / 0

except ZeroDivisionError:
    logging.exception("Calculation failed")
```

The resulting log contains the error message and traceback, including the exception type and message.

### Why Tracebacks Matter

An exception message alone may not provide enough information to identify where a failure occurred.

The traceback helps locate the code path that caused the exception.

In the order-validation pipeline, expected validation failures are handled and recorded as warnings. The `logger.exception()` call is reserved for the unexpected data-error handling branch in the sample implementation.

The supplied sample orders should not trigger that branch because their fields have the expected types and structure.

---

## 9. Results and Output Analysis

After processing all five sample orders, the expected counts are:

```text
Valid orders: 3
Rejected orders: 2
```

### Valid Orders

- Order 201
- Order 203
- Order 205

### Rejected Orders

- Order 202: Price must be positive.
- Order 204: Quantity must be positive.

### Interpretation

The pipeline correctly separates valid and rejected records according to the implemented validation rules.

The INFO run provides an overview of processing. The DEBUG run adds more detailed information about the execution of each validation step.

Both runs should produce the same valid and rejected counts.

The output counts should be verified by running the program rather than inferred solely from the logging messages.

---

## 10. Limitations of Console-Only Logging

The current implementation uses console logging rather than persistent log-file storage.

This is sufficient for a small learning exercise, but it has limitations.

### 10.1 No Persistent Log File

The application does not explicitly save its log records to a dedicated log file.

Once terminal output is lost, the messages may no longer be available for investigation.

### 10.2 Limited Historical Investigation

Without retained logs, it is difficult to compare failures across multiple runs or investigate problems that occurred earlier.

### 10.3 No Automatic Monitoring

The application does not send alerts when a pipeline fails.

A developer must inspect the output or use an external monitoring system.

### 10.4 No Centralized Logging

In a distributed data pipeline, different components may run on different machines or services.

Console output from one process is not automatically collected and searchable alongside logs from other components.

### 10.5 No Log Rotation or Retention Policy

A production application may need to control how long logs are retained and how much storage they consume.

This project does not implement log rotation or retention policies.

### 10.6 Sensitive Data Risks

Logs can accidentally expose confidential information if complete records, passwords, access tokens, or personal information are recorded.

Production pipelines should log only the information necessary for debugging and monitoring.

### Possible Future Improvements

- Write log records to a file using `filename="pipeline.log"`.
- Configure both console and file handlers.
- Add automated tests for valid and rejected orders.
- Introduce structured logging for easier analysis.
- Add log rotation and retention policies.
- Integrate monitoring and alerting for production failures.

These improvements are outside the scope of the current exercise.

---

## 11. How to Run the Project

Run the commands from the repository root.

### INFO Run

```bash
python day10/logging_pipeline.py --log-level INFO
```

### DEBUG Run

```bash
python day10/logging_pipeline.py --log-level DEBUG
```

On Windows, use `py` instead of `python` if necessary.

### What to Verify

After both runs, verify that:

1. The pipeline processes five orders.
2. Three orders are accepted.
3. Two orders are rejected.
4. INFO messages appear in both runs.
5. DEBUG messages appear only in the DEBUG run.
6. The rejection reasons are recorded correctly.
7. The final counts remain unchanged between runs.

---

## 12. Key Learnings

Through this project, I learned:

- How to use Python's built-in logging module.
- How to configure logging using `basicConfig()`.
- How severity levels control the visibility of log records.
- How to include timestamps and severity levels in log messages.
- How to record successful processing events and validation warnings.
- How exception logging helps investigate unexpected failures.
- How INFO and DEBUG runs differ.
- How logging supports data-quality monitoring in a data pipeline.
- Why console-only logging is limited for production applications.

---

## 13. Conclusion

This project demonstrates how logging improves the visibility and debuggability of a Python order-validation pipeline.

The pipeline processes sample orders, records successful validations, reports rejected orders, and displays final processing counts.

Running the program at INFO and DEBUG levels demonstrates how logging configuration controls the amount of diagnostic information without changing the underlying processing results.

This forms a foundation for building more reliable data pipelines, where logging, validation, exception handling, and monitoring work together to make failures easier to identify and investigate.
