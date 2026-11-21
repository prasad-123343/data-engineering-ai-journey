
# PostgreSQL Order Analytics Pipeline

## 1. Project Overview

A Python-based data analytics pipeline that extracts order and customer data from PostgreSQL, calculates business metrics, and generates an analytics report.

## 2. Technologies Used

- Python 3.13
- PostgreSQL 18
- Psycopg 3
- SQL
- Logging

## 3. Project Structure

project/
├── main.py
├── database.py
├── analytics.py
├── README.md
└── output/

## 4. Pipeline Architecture

PostgreSQL → Python Extraction → Analytics Processing → Business Report

## 5. Key Features

- PostgreSQL database connectivity
- Order data extraction
- Customer-level revenue analysis
- Revenue and order aggregations
- Parameterized SQL practice
- Logging and exception handling
- Modular Python architecture

## 6. Business Metrics

| Metric | Result |
|---|---:|
| Total Orders | 4 |
| Completed Orders | 3 |
| Cancelled Orders | 1 |
| Total Revenue | 8700.50 |
| Completed Revenue | 5500.50 |
| Average Order Value | 2175.125 |

## 7. Database Configuration

The application reads database credentials from environment variables:

- DB_HOST
- DB_PORT
- DB_NAME
- DB_USER
- DB_PASSWORD

Never commit actual credentials to GitHub.

## 8. How to Run

Install Psycopg:

pip install "psycopg[binary]"

Run the pipeline from the repository root:

python .\day14\practical\project\main.py

## 9. Error Handling

The pipeline uses Python logging to record execution events and capture database or unexpected errors.

## 10. Limitations and Future Improvements

- Add automated unit and integration tests.
- Add retry handling for temporary database failures.
- Export reports to CSV or JSON.
- Add data quality validation.
- Introduce orchestration using Apache Airflow.
- Add structured logging and monitoring.
