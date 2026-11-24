# Linux-Based Customer ETL Pipeline

## Project Overview

A beginner Data Engineering project that demonstrates customer CSV ingestion, data-quality validation, SQLite storage, SQL-based checks, and pipeline log analysis using Python and Ubuntu Linux.

The project combines Python scripting, SQL, Linux command-line operations, and logging into a simple sequential ETL workflow.

## Technology Stack

- Python 3
- Ubuntu Linux (WSL2)
- SQLite
- SQL
- CSV
- Bash

## Project Structure

```text
customer_etl/
├── data/
│   ├── raw/
│   │   └── customers.csv
│   ├── processed/
│   │   └── cleaned_customers.csv
│   └── customers.db
├── scripts/
│   ├── create_staging.py
│   ├── data_quality.py
│   ├── log_analyzer.py
│   └── query_customers.py
├── logs/
│   ├── data_quality_report.txt
│   ├── operations_report.txt
│   ├── etl.log
│   └── log_analysis_report.txt
├── main.py
└── README.md
```

## Pipeline Workflow

1. Read customer records from the raw CSV file.
2. Create the SQLite customer staging table.
3. Load customer records into SQLite.
4. Validate customer IDs and detect duplicate or missing IDs.
5. Run SQL-based data-quality checks.
6. Analyze ETL log messages.
7. Generate data-quality and log-analysis reports.

## Features

- CSV ingestion using Python's `csv` module.
- SQLite database creation and loading.
- Duplicate customer ID detection.
- Missing customer ID validation.
- SQL record-count and data-quality checks.
- Log-level counting for INFO, WARNING, and ERROR.
- Extraction of error details.
- Report generation.
- Centralized execution through `main.py`.
- File paths resolved using `pathlib`.
- Pipeline execution logging.

## How to Run

### Prerequisites

- Ubuntu Linux or WSL2
- Python 3

SQLite is available through Python's standard library.

### Clone or download the project

Navigate to the project directory:

```bash
cd ~/linux_practice/customer_etl
```

### Configure the project name

```bash
export PROJECT_NAME="customer_etl"
```

### Execute the pipeline

```bash
python3 main.py
```

## Sample Validation Results

The current sample dataset contains:

| Metric | Result |
|---|---:|
| Total customer records | 8 |
| Valid records | 8 |
| Invalid records | 0 |
| Unique customer IDs | 8 |
| Missing customer IDs | 0 |
| Duplicate customer IDs | 0 |

## Logging and Monitoring

The project uses Python logging to report pipeline execution stages.

The log analyzer counts:

- INFO messages
- WARNING messages
- ERROR messages

It also extracts error details and saves a report.

## Current Limitations

- Uses a small local CSV dataset.
- Uses SQLite rather than a production database.
- Does not implement automated retries.
- Does not implement scheduled execution.
- Does not include a dedicated transformation stage in the main pipeline.
- Log analysis reads an existing log file and can include historical errors.
- Does not yet include automated unit tests.

## Future Improvements

- Implement dedicated ingestion and transformation modules.
- Add automated tests using pytest.
- Add structured logging and run identifiers.
- Implement retry and recovery mechanisms.
- Integrate PostgreSQL.
- Add workflow orchestration using Apache Airflow.
- Add cloud storage using AWS S3.

## Learning Outcomes

This project provided practical experience with:

- Linux filesystem and command-line operations.
- Python file handling and CSV processing.
- Data-quality validation.
- SQLite and SQL queries.
- Python subprocess execution.
- Logging and error analysis.
- Organizing a small ETL project.
