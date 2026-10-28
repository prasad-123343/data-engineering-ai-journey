# Day 11 — CSV Data Processing Pipeline

## Overview

This project demonstrates how to read, validate, and process order data from a CSV file using Python.

The pipeline separates valid and rejected records, calculates revenue summaries, and saves rejected records with their rejection reasons for further investigation.

## Technologies Used

- Python
- CSV module
- Dictionaries and lists
- Sets
- Exception handling
- Git and GitHub

## Pipeline Workflow

1. Read order records from `orders.csv`.
2. Validate customer names and order amounts.
3. Reject missing, invalid, negative, or duplicate records.
4. Store valid records for further processing.
5. Calculate total revenue and revenue by customer.
6. Save rejected records and their rejection reasons to `rejected_orders.csv`.

## Data Quality Rules

The pipeline rejects records with:

- Missing customer names
- Missing amounts
- Amounts that cannot be converted to integers
- Negative amounts
- Duplicate order IDs

## Expected Results

For the supplied practice dataset:

- Total input records: 8
- Valid records: 3
- Rejected records: 5
- Total revenue from valid records: 3500

Revenue by customer:

| Customer | Revenue |
|---|---:|
| Ravi | 1200 |
| Priya | 800 |
| Arjun | 1500 |

## Output

The program produces revenue summaries in the terminal and writes rejected records, including their rejection reasons, to `data/rejected_orders.csv`.

## Learning Outcomes

- Reading CSV files with `csv.DictReader()`
- Validating data using conditional statements
- Converting string values into integers
- Detecting duplicate IDs using a set
- Handling invalid records with `continue`
- Aggregating revenue using Python dictionaries
- Writing CSV files using `csv.DictWriter()`

## How to Run

Run the script from the repository root:


python day11/src/read_csv_basic.py


## Future Improvements

- Add automated unit tests.
- Use Python logging instead of relying only on print statements.
- Load validated records into a database.
- Add stronger handling for malformed CSV files.
- Make pipeline reruns safe and predictable.