
# Day 3 — Python CSV Data Processing Pipeline

## Project Overview

On Day 3, I built a Python-based CSV data processing pipeline.

The pipeline reads order data from a CSV file, converts the data into appropriate Python data types, handles malformed numeric values, validates the records, separates valid and invalid orders, calculates revenue from valid orders, and writes the results into separate CSV files.

---

## Project Structure

```text
day03/
├── data/
│   └── orders.csv
│
├── output/
│   ├── valid_orders.csv
│   └── invalid_orders.csv
│
├── src/
│   └── csv_pipeline.py
│
└── README.md
```

---

## Input Data

The input file is:

```text
day03/data/orders.csv
```

The CSV contains the following fields:

```text
order_id
customer
price
quantity
```

Example:

```csv
order_id,customer,price,quantity
101,Ravi,250,3
102,Mahesh,500,2
103,Priya,300,2
104,Arun,-100,1
105,,200,2
106,Sita,150,4
```

---

## Pipeline Flow

```text
CSV Input
   ↓
Read CSV using csv.DictReader
   ↓
Convert CSV values to Python data types
   ↓
Handle conversion failures
   ↓
Validate business rules
   ↓
Separate valid and invalid orders
   ↓
Calculate revenue from valid orders
   ↓
Write valid_orders.csv
   ↓
Write invalid_orders.csv
```

---

## Step 1 — Read CSV Data

Python's `csv.DictReader` is used to read the CSV file.

Each CSV row is initially returned as a dictionary, and the values are read as strings.

Example:

```python
{
    "order_id": "101",
    "customer": "Ravi",
    "price": "250",
    "quantity": "3"
}
```

---

## Step 2 — Convert Data Types

The CSV values are converted into appropriate Python data types.

```text
order_id → int
price     → float
quantity  → int
customer  → string
```

For example:

```text
"101" → 101
"250" → 250.0
"3"   → 3
```

This allows the pipeline to perform numerical calculations and validation.

---

## Step 3 — Handle Conversion Errors

The pipeline uses `try` and `except` to handle invalid numeric values.

For example, if the CSV contains:

```csv
103,Priya,abc,2
```

the price cannot be converted to a number.

Instead of crashing the entire pipeline, the record is preserved and marked with:

```text
Invalid numeric value
```

This record is then treated as an invalid record.

---

## Step 4 — Validate Orders

After successful type conversion, each order is checked against validation rules.

### Validation Rules

An order is invalid when:

* Customer is empty
* Price is negative
* Quantity is less than or equal to zero
* Order ID is less than or equal to zero

Valid orders are passed to the next stage.

Invalid orders are stored along with the reason for rejection.

---

## Step 5 — Separate Valid and Invalid Orders

The pipeline creates two groups:

```text
Valid Orders
Invalid Orders
```

Invalid records contain an additional field:

```text
reason
```

For example:

```text
Order 104 → Price is negative
Order 105 → Customer is empty
```

---

## Step 6 — Calculate Revenue

Revenue is calculated only from valid orders.

The calculation is:

```text
revenue = price × quantity
```

For the valid orders:

```text
Ravi    → 250 × 3 = 750
Mahesh  → 500 × 2 = 1000
Priya   → 300 × 2 = 600
Sita    → 150 × 4 = 600
```

Total revenue:

```text
2950.0
```

Invalid orders are excluded from the revenue calculation.

---

## Step 7 — Write Output Files

The pipeline generates two output files.

### Valid Orders

```text
day03/output/valid_orders.csv
```

This file contains the successfully validated orders.

### Invalid Orders

```text
day03/output/invalid_orders.csv
```

This file contains rejected records and their rejection reasons.

---

## Expected Result

For the original input dataset:

```text
Total Orders: 6
Valid Orders: 4
Invalid Orders: 2
Total Revenue: 2950.0
```

Invalid records:

```text
Order 104 → Price is negative
Order 105 → Customer is empty
```

---

## How to Run

From the project root directory:

```bash
python day03/src/csv_pipeline.py
```

Expected output:

```text
Valid orders:
[...]

Invalid orders:
[...]

Total revenue: 2950.0
```

The output CSV files are regenerated each time the pipeline runs.

---

## What I Learned

During Day 3, I practiced:

* Reading CSV files using Python
* Using `csv.DictReader`
* Understanding CSV values as strings
* Converting strings to `int` and `float`
* Handling `ValueError`
* Writing reusable Python functions
* Validating structured data
* Separating valid and invalid records
* Recording rejection reasons
* Calculating revenue from valid data
* Writing CSV files using `csv.DictWriter`
* Using `writeheader()` and `writerows()`
* Organizing a Python script using `main()`
* Using:

```python
if __name__ == "__main__":
    main()
```

* Testing malformed data
* Preventing invalid records from crashing the pipeline
* Producing separate output datasets for valid and rejected records

---

## Key Data Engineering Concept

A major concept from this exercise is that **bad data should be handled explicitly rather than silently dropped or allowed to crash the pipeline**.

The pipeline preserves rejected records and records the reason for rejection.

This creates a simple quarantine pattern:

```text
Raw Data
   ↓
Validation
   ├── Valid → Continue Processing
   │
   └── Invalid → Quarantine with Reason
```

This approach can be extended to larger production data pipelines.
